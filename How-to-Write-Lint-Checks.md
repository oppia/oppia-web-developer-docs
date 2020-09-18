## Introduction

The Oppia linter is a tool which runs over all files in the codebase, with the purpose of finding common syntax errors and bad expressions in the files. It flags these issues and reports them on the terminal asking the user to look at specific line numbers where the issue is and fix them.

This makes the task of reviewers easy, since they don't need to manually investigate all the syntax errors (as the lint tests will catch these). Furthermore, the linter is automatically run before a commit is pushed to GitHub, and the push will be stopped if there are any errors in the changed files.


## How to run the linter

To run the linter:
1. To lint only files that have been touched in a commit

   ```
   python -m scripts.linters.pre_commit_linter
   ```

2. To lint all files in the folder or to lint just a specific file

   ```
   python -m scripts.linters.pre_commit_linter --path filepath
   ```

3. To lint a specific list of files. Separate file paths by spaces

   ```
   python -m scripts.linters.pre_commit_linter --files filepath_1 filepath_2 ... filepath_n
   ```

4. To lint files in verbose mode

   ```
   python -m scripts.linters.pre_commit_linter --verbose
   ```

5. To lint a specific list of file extensions. Separate file extensions by spaces

   ```
   python -m scripts.linters.pre_commit_linter --only-check-file-extensions py js
   ```

## Directory Structure
All code related to the linter resides in the [scripts/linters](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/scripts/linters/) directory. The linters are split as follows:

* [Codeowner linter](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/scripts/linters/codeowner_linter.py): Lints the codeowner file.

* [CSS Linter](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/scripts/linters/css_linter.py): Lints all the CSS files in the codebase. These are additional checks over the default [stylelintrc](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/.stylelintrc) checks.

* [HTML Linter](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/scripts/linters/html_linter.py): Lints all the HTML files in the codebase. These are additional checks over the default [htmllintrc](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/.htmllintrc) checks.

* [Python Linter](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/scripts/linters/python_linter.py): It is used to lint all the python files in the codebase. These are additional checks over default [pylint](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/.pylintrc) and [isort](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/.isort.cfg) checks.

* [JS/TS Linter](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/scripts/linters/js_ts_linter.py): Lints all the javascript and typescript files in the codebase. These are additional checks over default [eslint](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/.eslintrc) checks.

* [General purpose linter](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/scripts/linters/general_purpose_linter.py): Lints all files and contains checks which are not dependent on file extension.

* [Other files linter](https://github.com/oppia/oppia/blob/c7e56a72ecf3d8761f5172e80973d104b3611e73/scripts/linters/other_files_linter.py): Lints remaining file types like json and config files.

Note that each linter has a test file to ensure that it works as expected.

The other files in the linters folder have the following use case:

* [Custom Eslint Checks](https://github.com/oppia/oppia/tree/develop/scripts/linters/custom_eslint_checks/): Adds custom checks to be applied via eslint.
* [Pylint Extensions](https://github.com/oppia/oppia/blob/develop/scripts/linters/pylint_extensions.py): Additional pylint checks added as custom extensions.
* [Linter utils](https://github.com/oppia/oppia/blob/develop/scripts/linters/linter_utils.py): Utility functions shared across all the linters

## How to add new lint checks?

1. Confirm the file type for which you want to add the lint check. 

2. If it is possible to introduce the test by just adding a rule in the [eslint](https://github.com/oppia/oppia/blob/develop/.eslintrc) (for JS/TS)  [pylint] / (https://github.com/oppia/oppia/blob/develop/.pylintrc) (for python) / [htmllint](https://github.com/oppia/oppia/blob/develop/.htmllintrc) (for HTML) / [stylelint](https://github.com/oppia/oppia/blob/develop/.stylelintrc) (for CSS) configs, just add the new rule there.

   * Refer to this documentation for the list of available rules:

      * HTML: https://github.com/htmllint/htmllint/wiki/Options

      * CSS: https://github.com/stylelint/stylelint/blob/master/docs/user-guide/get-started.md

      * Python: http://pylint.pycqa.org/en/latest/

      * JS/TS: https://eslint.org/docs/user-guide/configuring

3. If no existing rule is found, add a custom method in the respective linter file for the check to work.

   * If the check is for a python file, prefer adding a custom [pylint extension](https://github.com/oppia/oppia/blob/develop/scripts/linters/pylint_extensions.py) instead of a new method in [python_linter](https://github.com/oppia/oppia/blob/develop/scripts/linters/python_linter.py) file. (Refer this [guide](http://pylint.pycqa.org/en/latest/how_tos/plugins.html) for adding pylint extensions).

   * If the check is for a js/ts file, prefer adding a [custom eslint extension](https://github.com/oppia/oppia/tree/develop/scripts/linters/custom_eslint_checks/) instead of a new method in [js/ts linter](https://github.com/oppia/oppia/blob/develop/scripts/linters/js_ts_linter.py) file. (Refer this [guide](https://eslint.org/docs/developer-guide/working-with-rules) for adding eslint extensions).

4. Update the corresponding **_test** file by adding new test cases for the new check which is added and verify that the test is running as expected:

   ```
   python -m scripts.run_backend_tests --test_target=scripts.linters.<test-file-name>
   ```

5. Run the pre_commit_linter module over the file type for which the linter is added, fix all the issues and re-run the linter to verify. Once that is done, push the changes to github.

## Important code pointers

### Python:

1. If the code is for python files and cannot be done with a regex check, then the code will be written in pylint_extensions file. In the pylint extensions file we have three types of checks --  IAstroidChecker, ITokenChecker, IRawChecker.
IAstroidChecker provides the different nodes, which we can use to access a particular part of the code. For example, to access the classes we have visit_class node and to access functions we have visit_function node. These are the available nodes in the pylint(http://pylint.pycqa.org/projects/astroid/en/latest/api/astroid.nodes.html)

2. ITokenChecker provides access to the token like brackets, parenthesis.

3. IRawChecker provides the whole code of a file and we can write the checks on it. But it is not recommended to use since it requires reading of the complete file, reducing the efficiency. Use it only if there are no other options available. It is only used at two places across the codebase. 
   * [SingleCharAndNewlineAtEOFChecker](https://github.com/oppia/oppia/blob/5d0095c6cd6393287e31595439817ae49d3cb1d8/scripts/linters/pylint_extensions.py#L1540): Used to check new line at the end of file.
   * [BackslashContinuationChecker](https://github.com/oppia/oppia/blob/5d0095c6cd6393287e31595439817ae49d3cb1d8/scripts/linters/pylint_extensions.py#L1402): Used to check if the backslash is being used to extend a line. (We need to use IRawChecker for this because there are no nodes/tokens available for backslashes.)

### ESLint custom checker

If the code is for js or ts files and cannot be done with a regex check, then the code will be written in a new file under custom_eslint_checks directory. In custom eslint checks, we can visit source code of the file and tokens and nodes just like the python linter.
   1. Use the node to access specific parts of code. For example we used the node to access the call expression whose name is ‘it’ to check the only ‘it’ call expression. It helps us in getting better efficiency because then we do not have to visit all the lines of code. We are only visiting the required call expression named “it”. Below is the code snippet:

   ```
   return {
        CallExpression(node) {
          if (node.callee.name === 'it') {
            const testMessageNode = node.arguments[0];
            var testMessage = extractMessage(testMessageNode);
            checkMessage(testMessageNode, testMessage);
          }
        }
      };
   ```


   2. Use tokens to access tokens present in a file.
   3. sourceCode is used to access the code of a file in raw format.

### Writing general checks:

In cases where the above approaches don’t work, you may be able to use regex checks as a possible fallback. Do this only for checks which apply in the same way to multiple types of files (e.g. formatting of TODO comments).

However, if your test is specific to either Python files or to JS/TS files, **please do not use this approach**. Instead, use a filetype-specific custom checker (as mentioned above). This will help with reducing the time taken for checks.

Here is an example of a regex check:

   ```
   {
        'regexp': re.compile(r'TODO[^\(]*[^\)][^:]*[^A-Z]+[^\w]*$'),
        'message': 'Please assign TODO comments to a user '
                   'in the format TODO(username): XXX. ',
        'excluded_files': (),
        'excluded_dirs': ()
    }
   ```

We have 4 keys in a dictionary here:
**Regexp**: Write the regex expression here which you want to match
**Message**: Add message here, it will show after the linter catches the error.
**Excluded_files**: Add excluded files here if really necessary (not recommended)
**Excluded_dirs**: Add excluded directories here if really necessary (not recommended)

All our general lint checks which can be easily implemented by a regex will be written like this. This is the same for all files types -- py, js, ts, html. We do not use this pattern for CSS files.

The above code will go in the general_pupose_linter.py and will be placed there according to the file type. We have the following list of checks for files:

   1. BAD_PATTERNS: This is used if the regex will work in the same way for all files.
   2. BAD_PATTERN_JS_AND_TS_REGEXP: This is used if the regex is only for .js or .ts files.
   3. MANDATORY_PATTERN_REGEXP: This is used if the pattern is mandatory to have in all files (like the file overview).
   4. MANDATORY_PATTERNS_JS_REGEXP: This is used only for mandatory patterns that are only used for .js or .ts files.
   5. BAD_LINE_PATTERNS_HTML_REGEXP: This is used if it is a bad pattern for html files.
   6. BAD_PATTERN_PYTHON_REGEXP: This is used if it is a bad pattern for python files.
   7. If it is a more complex check and used in all types of file, then create a new method in the GeneralPurposeLinter class and add the required there.

## Example for Reference
Sample PRs where checks were added:

* Custom Eslint check added: https://github.com/oppia/oppia/pull/10494

   * A new eslint plugin added in custom_eslint_checks folder along with a test file: https://github.com/oppia/oppia/pull/10494/files#diff-f84fecf97b5ab1bd91993f21f866a8e7

   * Rule enabled in eslintrc: https://github.com/oppia/oppia/pull/10494/files#diff-1dc6ee56b778cd91e0327b52aaeaa1b9

   * All the files which violated the test are fixed in the PR.

* Custom Pylint check added: https://github.com/oppia/oppia/pull/10107

   * A new case added in pylint_extensions.py and the test file is updated for that check: https://github.com/oppia/oppia/pull/10107/files#diff-c9f33564b072eb94beb16826ae5f8a28

   * Note, that no update is required to pylintrc. By default, it includes all extensions in the pylint_extensions file.

   * All the files which violated the test are fixed in the PR.

* Examples of independent checks that were added to extra linters not working via eslint/pylint:

   * Verifying ts ignore in typescript files: https://github.com/oppia/oppia/blob/develop/scripts/linters/js_ts_linter.py#L273. 

   * Checking type definitions for third party libs: https://github.com/oppia/oppia/blob/develop/scripts/linters/other_files_linter.py#L118

   * Verifying all jobs are registered in jobs_registry file: https://github.com/oppia/oppia/blob/develop/scripts/linters/python_linter.py#L129 

## Contact
Please reach out to **Anshul Hudda (@Hudda, anshulhudda.ssap@gmail.com) and Nitish (@bansalnitish, nitishbansal2297@gmail.com)** in case you’ve any queries.
