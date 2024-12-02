## Table of contents

* [Introduction](#introduction)
* [Run linters](#run-linters)
* [Write lint checks](#write-lint-checks)
* [Types of lint checks](#types-of-lint-checks)
  * [Third-party linters](#third-party-linters)
    * [ESLint](#eslint)
    * [Pylint](#pylint)
    * [isort](#isort)
    * [htmllint](#htmllint)
    * [stylelint](#stylelint)
  * [Our custom linters](#our-custom-linters)
    * [JS/TS linter](#jsts-linter)
    * [HTML linter](#html-linter)
    * [General-purpose linter](#general-purpose-linter)
    * [Codeowner linter](#codeowner-linter)
    * [Other files linter](#other-files-linter)
* [Examples](#examples)
* [Contact](#contact)

## Introduction

We use linters to check our code for common errors or bad patterns. The Oppia linter runs our linters, flags any problems the linters find, and reports those problems on the terminal.

## Run linters

1. To lint only files that have been changed but not committed:

   ```console
   python -m scripts.linters.run_lint_checks
   ```

2. To lint the file or files at a path:

   ```console
   python -m scripts.linters.run_lint_checks --path {{path}}
   ```

   If you specify the path to a file, only that file will be linted, but if you provide a directory, all the files under that directory will be linted.

3. To lint a specific list of files:

   ```console
   python -m scripts.linters.run_lint_checks --files {{file paths}}
   ```

   Separate file paths with spaces. For example, to lint `scripts/start.py` and `servers.py`, you could run this:

   ```console
   python -m scripts.linters.run_lint_checks --files scripts/start.py servers.py
   ```

4. To lint files in verbose mode, add the `--verbose` flag like this:

   ```console
   python -m scripts.linters.run_lint_checks --verbose
   ```

   This also enables logging, so it is very useful for debugging!

5. To lint a specific list of file extensions (separated by spaces):

   ```console
   python -m scripts.linters.run_lint_checks --only-check-file-extensions {{extensions}}
   ```

   For example, to lint Python and JavaScript files, you could run this:

   ```console
   python -m scripts.linters.run_lint_checks --only-check-file-extensions py js
   ```

## Write lint checks

If you see a bad pattern cropping up a lot in the code base, you might want to add a lint check to help you find and fix them all. Then, the lint check will ensure no one ever uses that bad pattern again. When adding a new lint check, you should follow the following approach:

1. Identify what types of files your lint check needs to evaluate. This is important because we use different linters for different file types.

2. Check which of [our linters](#types-of-lint-checks) apply to your file types, and decide which linters you want to use. Add your lint check following the linter-specific instructions below.

3. Run your lint check locally to find all existing violations in the code base. Fix these until the linter passes.

4. Open a PR that both fixes all existing violations and adds the lint check. Once your PR merges, your lint check will prevent any future PRs from introducing new violations.

## Types of lint checks

### Third-party linters

We make use of several third-party linters, some of which also accept custom rules.

#### ESLint

We use [ESLint](https://eslint.org) to lint our JavaScript and TypeScript code. It has lots of [built-in rules](https://stylelint.io/), and if one of them does what you want, you can enable it in [`.eslintrc`](https://github.com/oppia/oppia/tree/develop/.eslintrc). If no existing rule does what you need, you can write a [[custom rule|Custom-ESLint-checks]].

The ESLint checks are run by `scripts.linters.js_ts_linter.JsTsLintChecksManager`.

#### Pylint

We use [Pylint](https://pylint.pycqa.org) to lint our Python code. It provides many [rules and configuration options](https://pylint.pycqa.org/en/latest/technical_reference/features.html) that you may find useful. They are configured in [`.pylintrc`](https://github.com/oppia/oppia/tree/develop/.pylintrc). If they aren't enough though, you can also write a [[custom rule|Custom-Pylint-checks]].

The Pylint checks are run by `scripts.linters.python_linter.ThirdPartyPythonLintChecksManager`.

#### isort

We use [isort](https://pycqa.github.io/isort/) to make sure our Python imports are properly sorted. It is configured by [`.isort.cfg`](https://github.com/oppia/oppia/tree/develop/.isort.cfg), but it does not support custom rules.

The isort checks are run by `scripts.linters.python_linter.ThirdPartyPythonLintChecksManager`.

#### htmllint

We lint our HTML code with [htmllint](https://github.com/htmllint/htmllint/), which is configured in [`.htmllintrc`](https://github.com/oppia/oppia/tree/develop/.htmllintrc). See the [htmllint documentation](https://github.com/htmllint/htmllint/wiki/Options) for a list of the available configuration options.

Unfortunately, htmllint doesn't support custom rules.

The htmllint checks are run by `scripts.linters.html_linter.ThirdPartyHTMLLintChecksManager`.

#### stylelint

We lint CSS and HTML files with [stylelint](https://stylelint.io). The linter is configured by [`.stylelintrc`](https://github.com/oppia/oppia/tree/develop/.stylelintrc) for HTML files and by [`core/templates/css/.stylelintrc`](https://github.com/oppia/oppia/blob/develop/core/templates/css/.stylelintrc) for CSS files. Check out its documentation for a list of the available [rules](https://stylelint.io/user-guide/rules/list) and [configuration options](https://stylelint.io/user-guide/configure).

Since stylelint does not support custom rules, you'll need to use other linters if the built-in rules don't suit your needs.

### Our custom linters

Even with custom rules, the third-party linters above are sometimes insufficient. That's why we also wrote some linters ourselves.

#### JS/TS linter

Our custom JavaScript and TypeScript lint checks are defined in the `JsTsLintChecksManager` class of [`scripts/linters/js_ts_linter.py`](https://github.com/oppia/oppia/blob/develop/scripts/linters/js_ts_linter.py). The individual lint checks are defined as private helper methods in that class, and those methods are called from the `JsTsLintChecksManager.perform_all_lint_checks()` method when the linter runs.

We do not allow adding new checks to this linter. Instead, you should use [ESLint](#eslint).

#### HTML linter

Since we cannot add custom rules to htmllint, we have written our own HTML linter in the `HTMLLintChecksManager` class in [`scripts/linters/html_linter.py`](https://github.com/oppia/oppia/blob/develop/scripts/linters/html_linter.py). If you need to add custom HTML lint checks, you can do so here.

#### General-purpose linter

The general-purpose linter relies on regular expressions to identify bad patterns in the code, but it is less efficient since it has to run over every file. We do not allow adding Python, JavaScript, or TypeScript checks here. Instead, you should use [Pylint](#pylint) or [ESLint](#eslint).

Even though we do not allow new checks to this linter, we explain below how the checks are defined to help you understand the existing checks.

We define regular expression checks like this:

```python
{
    'regexp': re.compile(r'TODO[^\(]*[^\)][^:]*[^A-Z]+[^\w]*$'),
    'message': 'Please assign TODO comments to a user '
               'in the format TODO(username): XXX. ',
    'excluded_files': (),
    'excluded_dirs': ()
}
```

We have 4 keys in this dictionary:

* `regexp`: The regular expression here that the check matches. Depending on the situation, this could be either a forbidden or a required pattern.
* `message` The error message that will be shown to the user if the lint check fails.
* `excluded_files`: A tuple of excluded files, if really necessary (**not recommended**).
* `excluded_dirs`: A tuple of excluded directories if really necessary (**not recommended**).

These regular expression checks can be added to any of the following constants in `general_purpose_linter.py`:

* `BAD_PATTERNS_REGEXP`: The regular expressions here are forbidden in any file.
* `MANDATORY_PATTERNS_REGEXP`: The regular expressions here must be present in every file. The `included_types` key may be specified to limit what files this applies to.
* `MANDATORY_PATTERNS_JS_REGEXP`: The regular expressions here must be present in all JavaScript and TypeScript files. The `included_types` key should specify JavaScript files, TypeScript files, or both.
* `BAD_LINE_PATTERNS_HTML_REGEXP`: The regular expressions here are forbidden in HTML files.
* `BAD_PATTERNS_PYTHON_REGEXP`: The regular expressions here are forbidden in Python files.

There are also two additional constants you can add values to:

* `BAD_PATTERNS`: This dictionary stores mappings from forbidden substrings to dictionaries like those defining regular expression checks, but without the `regexp` key.
* `BAD_STRINGS_CONSTANTS`: This dictionary stores mappings from forbidden substrings to dictionaries like those defining regular expression checks, but without the `regexp` key. These substrings are only checked in `constants.ts`.

For more complicated rules, you can also add a method to the `GeneralPurposeLinter` class.

#### Codeowner linter

In [`scripts/linters/codeowner_linter.py`](https://github.com/oppia/oppia/blob/develop/scripts/linters/codeowner_linter.py), we have a custom linter that helps us maintain the codeowners file. You probably won't ever have to change this linter, but if you ever get a warning that says `{{some file}} is not listed in the .github/CODEOWNERS file`, that's the codeowner linter reminding you to add a new file to the codeowners file.

#### Other files linter

Finally, we have some miscellaneous lint checks defined in the `CustomLintChecksManager` class in [`scripts/linters/other_files_linter.py`](https://github.com/oppia/oppia/blob/develop/scripts/linters/other_files_linter.py).

## Examples

Sample PRs where checks were added:

* Custom ESLint check: https://github.com/oppia/oppia/pull/10494

* Custom Pylint check: https://github.com/oppia/oppia/pull/10107

## Contact

Please reach out to **Sajal Asati (@sajalasati, sajalasati107@gmail.com) or Sandeep Dubey (@DubeySandeep, dubeysandeep.in@gmail.com)** with any questions.
