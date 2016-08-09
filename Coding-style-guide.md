## General guidelines

In general, code should be formatted consistently with other code around it. We use Google's [Python](https://google.github.io/styleguide/pyguide.html) and [JavaScript](https://google.github.io/styleguide/javascriptguide.xml) style guides as a reference. 

The pre-push hook should take care of most of the style issues (for Python and JavaScript code). However, we follow a few additional rules that aren't baked into the linter, and which are detailed on this page. Please adhere to these as well, in order to minimize back-and-forth during review.

### General
- The last character in each file should be a newline. (If you're using Sublime, you can enforce this locally by adding `"ensure_newline_at_eof_on_save": true` to your user preferences file.)

### Python
- There should be two empty lines before any top-level class or function definition.
- Prefer string interpolation over concatenation -- e.g. prefer:

  ```
  'My string %s' % varname
  ```
over

  ```
  'My string ' + varname
  ```
- When indenting from an open parenthesis ('('), prefer indenting by 4 rather than indenting from the position of the parenthesis. For example, prefer:

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

### JavaScript
- We are moving away from using underscores as prefixes for variable names, so, in the future, use `var localVariable` and not `var _localVariable`. Instead, we are adopting the convention that anything declared using `var` is private to the controller/service/etc. If you want a variable to be accessible to the controller, declare it on $scope instead.

### CSS
- Within each CSS rule, attributes should be alphabetized (e.g. 'height' before 'margin' before 'top'). This makes it easy to find the value of an attribute if there are lots of them.
- If the CSS class is oppia-specific, prefix it with `oppia-`. This helps distinguish it from CSS classes used by other third-party libraries. 
- For directives, include the CSS in the directive template file, similar to what we do in `core/templates/dev/head/components/exploration_summary_tile_directive.html`. (Note that, in this case, all CSS rules should start with the top-level CSS class of the directive, so that they don't affect other elements outside it.) All other CSS should go in `core/templates/dev/head/css/oppia.css`.
