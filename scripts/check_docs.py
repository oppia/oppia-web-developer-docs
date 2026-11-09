"""Validate Oppia wiki Markdown: links, TOC consistency, alert notation."""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BASELINE_PATH = REPO_ROOT / "scripts" / "toc_baseline.txt"

LINK_RE = re.compile(r'\[([^\]]*)\]\((?!\()([^)\s]+)(?:\s+"[^"]*")?\)')
HEADER_RE = re.compile(r'^(#{2,6})\s+(.+?)\s*#*\s*$')
FENCE_RE = re.compile(r'^\s*(```|~~~)')
TOC_START_RE = re.compile(r'^#{1,6}\s+table\s+of\s+contents?\s*$', re.I)
TOC_ITEM_RE = re.compile(r'^\s*[-*]\s+\[([^\]]+)\]\([^)]*\)')
PIPE_LINK_RE = re.compile(r'\[\[[^\]]+\]\]')
ASSET_EXT_RE = re.compile(
    r'\.(png|jpe?g|gif|svg|webp|bmp|ico|pdf|mp4|webm|mov|zip|tar|gz)$',
    re.I,
)
ZERO_WIDTH_RE = re.compile(r'[\u200b-\u200f\u2060\ufeff]')
ESCAPE_RE = re.compile(r'\\([_*`\[\]()#+\-.!&{}|<>~])')
INLINE_LINK_RE = re.compile(r'\[([^\]]+)\]\([^)]*\)')
EMPHASIS_RE = re.compile(r'^(\*{1,3}|_{1,3})(.+?)\1$')

CATEGORY_LABELS = {
    "mediawiki": "Broken MediaWiki link",
    "relative":  "Broken relative link",
    "asset":     "Broken asset link",
    "header-missing": "Header not in TOC",
    "toc-orphan":     "TOC entry has no matching header",
    "toc-mismatch":   "TOC entry differs from header (near match)",
}


def make_issue(category, file, lineno, text, hint=""):
    key = f"{file}:{lineno}: {CATEGORY_LABELS[category]}: {text}"
    return {
        "category": category, "file": file, "lineno": lineno,
        "text": text, "hint": hint, "key": key,
    }


def find_md_files():
    return sorted(p for p in REPO_ROOT.glob("*.md") if p.is_file())


def iter_links(md_file):
    content = md_file.read_text(encoding="utf-8")
    in_fence = False
    for lineno, line in enumerate(content.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        masked_line = PIPE_LINK_RE.sub(lambda match: " " * len(match.group(0)), line)
        for match in LINK_RE.finditer(masked_line):
            yield lineno, match.group(2).strip()


def classify(target):
    if not target:
        return "skip"
    low = target.lower()
    if low.startswith(("http://", "https://")):
        return "external"
    if low.startswith("#"):
        return "anchor"
    if low.startswith("mailto:"):
        return "mailto"
    if target.startswith(("./", "../", "/")):
        return "relative"
    if "@" in target and "/" not in target:
        return "mailto"
    if ASSET_EXT_RE.search(target.split("#")[0]):
        return "asset"
    if "/" not in target.split("#")[0]:
        return "mediawiki"
    return "relative"


def check_links(md_file):
    issues = []
    for lineno, target in iter_links(md_file):
        kind = classify(target)
        if kind in ("external", "anchor", "mailto", "skip"):
            continue
        file_part = target.split("#", 1)[0]
        if not file_part:
            continue

        if kind == "mediawiki":
            if not (REPO_ROOT / f"{file_part}.md").exists():
                issues.append(make_issue(
                    "mediawiki", md_file.name, lineno, file_part,
                    hint=f"Expected file: {file_part}.md",
                ))
        elif kind in ("asset", "relative"):
            if not (md_file.parent / file_part).resolve().exists():
                hint = ""
                if kind == "asset" and "." in file_part.split("/")[0]:
                    hint = f"Possible typo: did you mean {file_part.replace('.', '/', 1)}?"
                issues.append(make_issue(kind, md_file.name, lineno, target, hint=hint))
    return issues


def extract_toc_and_headers(md_file):
    lines = md_file.read_text(encoding="utf-8").splitlines()
    headers, toc_entries = [], []
    in_fence = in_toc = toc_done = False

    for idx, line in enumerate(lines, start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if not in_toc and not toc_done and TOC_START_RE.match(line):
            in_toc = True
            continue

        if in_toc:
            hm = HEADER_RE.match(line)
            if hm:
                in_toc, toc_done = False, True
                headers.append((idx, hm.group(2).strip()))
                continue
            item = TOC_ITEM_RE.match(line)
            if item:
                text = item.group(1).strip()
                if len(text) >= 2 and not text.startswith("["):
                    toc_entries.append((idx, text))
            continue

        hm = HEADER_RE.match(line)
        if hm:
            headers.append((idx, hm.group(2).strip()))

    return toc_entries, headers


def normalize(text):
    text = text.strip()
    text = ZERO_WIDTH_RE.sub("", text)
    text = INLINE_LINK_RE.sub(r"\1", text)
    text = ESCAPE_RE.sub(r"\1", text)
    for _ in range(2):
        m = EMPHASIS_RE.match(text)
        if not m:
            break
        text = m.group(2).strip()
    text = re.sub(r"\s+", " ", text).strip()
    return text.rstrip(".:;!?,…").rstrip().lower()


def near_match(a, b):
    if a == b or a in b or b in a:
        return True
    ta, tb = set(a.split()), set(b.split())
    if not ta or not tb:
        return False
    return len(ta & tb) / max(len(ta), len(tb)) >= 0.8


def check_toc(md_file):
    toc_entries, headers = extract_toc_and_headers(md_file)
    if not toc_entries:
        return []

    header_norm = [(ln, txt, normalize(txt)) for ln, txt in headers]
    toc_norm = [(ln, txt, normalize(txt)) for ln, txt in toc_entries]

    used_toc, issues = set(), []

    for h_ln, h_txt, h_norm in header_norm:
        exact = next(
            (i for i, (_, _, t) in enumerate(toc_norm)
             if t == h_norm and i not in used_toc),
            None,
        )
        if exact is not None:
            used_toc.add(exact)
            continue

        near = next(
            (i for i, (_, _, t) in enumerate(toc_norm)
             if i not in used_toc and near_match(h_norm, t)),
            None,
        )
        if near is not None:
            used_toc.add(near)
            t_ln, t_txt, _ = toc_norm[near]
            issues.append(make_issue(
                "toc-mismatch", md_file.name, h_ln,
                f"header: {h_txt!r}  vs  TOC: {t_txt!r}",
                hint=(
                    f"Header (line {h_ln}) and TOC entry (line {t_ln}) "
                    f"differ only in formatting."
                ),
            ))
        else:
            issues.append(make_issue(
                "header-missing", md_file.name, h_ln, h_txt,
                hint="Add this header as a list item under the TOC section.",
            ))

    for i, (t_ln, t_txt, _) in enumerate(toc_norm):
        if i in used_toc:
            continue
        issues.append(make_issue(
            "toc-orphan", md_file.name, t_ln, t_txt,
            hint="No header with this text exists. Remove or update this entry.",
        ))

    return issues


def load_baseline():
    if not BASELINE_PATH.exists():
        return set()
    return {
        line.rstrip()
        for line in BASELINE_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def write_baseline(issues):
    keys = sorted({i["key"] for i in issues})
    header = (
        "# Auto-generated baseline of known documentation issues.\n"
        "# Regenerate with: python scripts/check_docs.py --update-baseline\n"
        "# CI fails only on issues NOT listed here.\n\n"
    )
    BASELINE_PATH.write_text(header + "\n".join(keys) + "\n", encoding="utf-8")
    print(f"Wrote {len(keys)} entries to {BASELINE_PATH.relative_to(REPO_ROOT)}")


def print_report(issues, baseline, verbose):
    new_issues = [i for i in issues if i["key"] not in baseline]
    known = len(issues) - len(new_issues)
    n_files = len({i["file"] for i in issues})

    print("=" * 72)
    print(f"Docs check — {len(issues)} issue(s) across {n_files} file(s)")
    print("=" * 72)

    print("\nSUMMARY BY CATEGORY")
    by_cat = defaultdict(int)
    for i in issues:
        by_cat[i["category"]] += 1
    for cat in sorted(by_cat, key=lambda c: -by_cat[c]):
        print(f"  {CATEGORY_LABELS[cat]:<40} {by_cat[cat]:>5}")

    print("\nSUMMARY BY FILE (top 10)")
    by_file = defaultdict(int)
    for i in issues:
        by_file[i["file"]] += 1
    for fname, count in sorted(by_file.items(), key=lambda kv: -kv[1])[:10]:
        print(f"  {fname:<55} {count:>5}")

    print("\n" + "-" * 72)
    print("DETAILED ISSUES")
    print("-" * 72)

    to_show = issues if verbose else new_issues
    if not to_show:
        print("\n(no NEW issues — everything is in the baseline)")
        return

    grouped = defaultdict(list)
    for i in to_show:
        grouped[i["file"]].append(i)

    for fname in sorted(grouped):
        entries = sorted(grouped[fname], key=lambda i: i["lineno"])
        new_count = sum(1 for i in entries if i["key"] not in baseline)
        marker = f"[{new_count} NEW]" if new_count else "[baseline only]"
        print(f"\n### {fname}  ({len(entries)} issue(s)) {marker}")
        for i in entries:
            is_new = i["key"] not in baseline
            suffix = "  [NEW]" if is_new and not verbose else ""
            print(f"  L{i['lineno']:<5}{CATEGORY_LABELS[i['category']]}: {i['text']!r}{suffix}")
            if i["hint"]:
                print(f"         -> {i['hint']}")

    print()
    print("=" * 72)
    print(f"TOTAL: {len(issues)} issue(s), {known} known, {len(new_issues)} new.")
    print("=" * 72)


def self_test():
    normalize_cases = [
        ("MERGE\\_MSG Newer than Swap File", "merge_msg newer than swap file"),
        ("MERGE_MSG Newer than Swap File", "merge_msg newer than swap file"),
        ("5. Tested \\& Verified", "5. tested & verified"),
        ("Important note:", "important note"),
        ("**Activities Tab**", "activities tab"),
        ("*Trial 1*", "trial 1"),
        ("When you encounter an installation error...",
         "when you encounter an installation error"),
        ("[TS-1]:", "[ts-1]"),
        ("**\u2060\u2060Translate Text Tab**", "translate text tab"),
        ("Run pylint on python files in the [Oppia-docs-repo](https://x).",
         "run pylint on python files in the oppia-docs-repo"),
    ]
    classify_cases = [
        ("https://example.com", "external"),
        ("#anchor", "anchor"),
        ("mailto:a@b.c", "mailto"),
        ("web-server-admins@oppia.org", "mailto"),
        ("./foo.md", "relative"),
        ("../bar", "relative"),
        ("images/foo.png", "asset"),
        ("Contributing-code-to-Oppia", "mediawiki"),
        ("Contributing-code-to-Oppia#section", "mediawiki"),
        ("", "skip"),
    ]
    failed = 0
    for inp, expected in normalize_cases:
        got = normalize(inp)
        if got != expected:
            print(f"FAIL normalize({inp!r}) expected {expected!r} got {got!r}")
            failed += 1
    for inp, expected in classify_cases:
        got = classify(inp)
        if got != expected:
            print(f"FAIL classify({inp!r}) expected {expected!r} got {got!r}")
            failed += 1
    if LINK_RE.findall("see [label]((https://example.com/x))"):
        print("FAIL LINK_RE matched malformed target")
        failed += 1

    if failed:
        print(f"\n{failed} self-test failure(s).")
        return 1
    print(f"Self-test passed ({len(normalize_cases) + len(classify_cases) + 1} checks).")
    return 0


def collect_all_issues():
    files = find_md_files()
    if not files:
        print("No markdown files found.", file=sys.stderr)
        return None
    issues = []
    for f in files:
        issues.extend(check_links(f))
        issues.extend(check_toc(f))
    return issues


def main():
    parser = argparse.ArgumentParser(description="Validate Oppia wiki docs.")
    parser.add_argument("--update-baseline", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    issues = collect_all_issues()
    if issues is None:
        return 1

    if args.update_baseline:
        write_baseline(issues)
        return 0

    baseline = load_baseline()
    new_issues = [i for i in issues if i["key"] not in baseline]

    if args.quiet:
        print(f"Docs check: {len(issues)} total, "
              f"{len(issues) - len(new_issues)} known, {len(new_issues)} new.")
    else:
        print_report(issues, baseline, verbose=args.verbose)

    if new_issues:
        print(f"\nERROR: {len(new_issues)} new issue(s) not in baseline.", file=sys.stderr)
        print("Run --update-baseline and commit the file if these are intentional.",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())