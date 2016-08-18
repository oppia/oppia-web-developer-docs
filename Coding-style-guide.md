Please follow the following style rules when writing code, in order to minimize unnecessary back-and-forth during code review. (Note that most, but not all, of the rules on this page are baked into the default linters and the pre-push hook.)

## General
- Ensure that your code looks consistent with the code surrounding it.
- Strings should use single quotes (`'`) throughout Python and JavaScript.
- Prefer having comments on their own line (above the code that's being commented on), as opposed to next to a line. The exception is when you need to disable a pylint warning for a specific line.
- The last character in each file should be a newline. (If you're using Sublime, you can enforce this locally by adding `"ensure_newline_at_eof_on_save": true` to your user preferences file.)

## Python
- Prefer `xrange` to `range`, so as not to hold the entire range in memory unnecessarily.
- Consider using a frozenset or tuple to a list, if the data structure is not meant to be subsequently modified. This applies especially to constants.
- If you need to raise an Exception, just do `raise Exception` -- no need to define custom exceptions. We tend to use exceptions fairly sparingly, though.
- Otherwise, please follow the [Google Python style guide](https://google.github.io/styleguide/pyguide.html). In particular:
  - There should be two empty lines before any top-level class or function definition.
  - Prefer string interpolation over concatenation -- e.g. prefer: `'My string %s' % varname` to `'My string ' + varname`.
  - When indenting from an open parenthesis ('('), prefer indenting by 4 rather than indenting from the position of the parenthesis. E.g., prefer:

    ```
      my_function_with_a_really_long_name(
          'abc', 'def', None)
    ```

    over
    
    ```
      my_function_with_a_really_long_name('abc',
                                          'def',
                                          None)
    ```
  - Docstrings should start with """ and end with """. The content of each docstring should be left-aligned. For example:

    ```
      """Check whether an email message with the same recipient_id,
      email_subject and (cleaned) email_html_body has been sent in
      the last DUPLICATE_EMAIL_INTERVAL_MINS.
      """
    ```
  - Never use backslashes to end a line. It's hard to tell whether they're escaping newlines, spaces, or something else. Use parentheses instead to break the line up, e.g.:

    ```
       my_variable = (
           my_very_long_module_name.my_really_long_function_name())
    ```
  - Be careful [not to use mutable objects](https://google.github.io/styleguide/pyguide.html?showone=Default_Argument_Values#Default_Argument_Values) as default values in the function or method definition. I.e., don't do things like `def foo(a, b=[]):`.

## JavaScript
- We use extra parentheses if a statement breaks across multiple lines, similar to Python.
- The indentation is always 2 spaces.
- We are moving away from using underscores as prefixes for variable names, so, in the future, use `var localVariable` and not `var _localVariable`. Instead, we are adopting the convention that anything declared using `var` is private to the controller/service/etc. If you want a variable to be accessible to the controller, declare it on $scope instead.
- We have started compiling a [style guide for JavaScript](https://docs.google.com/document/d/1ZDmLN66f53WdDPItFChu9Lr37z0dKoqR-ASX8UM5y60). This is currently a work in progress. However, please use this as the definitive guide when figuring out the correct way to name things (CamelCase, snake_case, etc.)

## CSS
- Do not include units if the value is 0. E.g. `margin-left: 0` instead of `margin-left: 0px`.
- Within each CSS rule, attributes should be alphabetized (e.g. 'height' before 'margin' before 'top'). This makes it easy to find the value of an attribute if there are lots of them.
- If the CSS class is oppia-specific, prefix it with `oppia-`. This helps distinguish it from CSS classes used by other third-party libraries. 
- For directives, include the CSS in the directive template file, similar to what we do in `core/templates/dev/head/components/exploration_summary_tile_directive.html`. (Note that, in this case, all CSS rules should start with the top-level CSS class of the directive, so that they don't affect other elements outside it.) All other CSS should go in `core/templates/dev/head/css/oppia.css`.
