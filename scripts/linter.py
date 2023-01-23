import os
import re
from typing import Pattern, List

search_note_pattern: Pattern = re.compile(r'^\*\*Note\*\*')
search_warning_pattern: Pattern = re.compile(r'^\*\*Warning\*\*')
correct_note_string: str = '> **Note**'
correct_warning_string: str = '> **Warning**'

def find_regex_in_file_content(
    search_pattern: Pattern,
    correct_string: str,
    filenames: List[str]
) -> bool:
    """Function that looks for a regex pattern in the given file contents."""

    match_found = False
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                if search_pattern.search(line):
                    print(f'{filename}:{i+1}: error: wrong notation "{search_pattern.search(line).string}"; expected "{correct_string}"')
                    match_found = True
    return match_found
def main() -> None:
    """Runs the check."""

    all_markdown_filenames: List[str] = [
        filename for filename in os.listdir() if filename.endswith('.md')
    ]
    found_note_pattern: bool = find_regex_in_file_content(
        search_note_pattern, correct_note_string, all_markdown_filenames
    )
    found_warning_pattern: bool = find_regex_in_file_content(
        search_warning_pattern, correct_warning_string, all_markdown_filenames
    )

    if found_note_pattern or found_warning_pattern:
        print("Lint Check Failed!!")
        exit(1)


if __name__ == '__main__':
    main()