Please follow the following style rules when writing code, in order to minimize unnecessary back-and-forth during code review. (Note that most, but not all, of the rules on this page are baked into the default linters and the pre-push hook.)

If you use [Sublime Text](http://www.sublimetext.com/), consider installing the SublimeLinter, [SublimeLinter-jscs](https://github.com/SublimeLinter/SublimeLinter-jscs) and [SublimeLinter-pylint](https://github.com/SublimeLinter/SublimeLinter-pylint) plugins, following the instructions on their respective pages.

## General
- Ensure that your code looks consistent with the code surrounding it.
- Strings should use single quotes (`'`) throughout Python and JavaScript.
- Prefer having comments on their own line (above the code that's being commented on), as opposed to next to a line. The exception is when you need to disable a pylint warning for a specific line.
- The last character in each file should be a newline. (If you're using Sublime, you can enforce this locally by adding `"ensure_newline_at_eof_on_save": true` to your user preferences file.)
- Avoid introducing `TODO (#XYZ): ...` comments in the files and instead try to do things correctly the first time. If you are going to add a TODO comment in any file then there needs to be (at minimum) a full comment and justification explaining what has been tried and what the issue is. The TODo should also reference an issue created on GitHub for thracking the problem.

## Design tips
- Avoid referencing elements of a list by a hardcoded index number, e.g. `item[0]`, `item[1]`. This is because the reader typically has no idea what is significant about the element index in question. If the values in the list are of different types, consider using a domain object instead to model the item being passed around.
- Avoid passing raw "dictionaries" (Python dicts or JS objects) between functions, because it's possible to add new fields to them midway through their lifecycle, which can get confusing for readers of the code. Use domain objects instead, since they have a fixed set of fields.
  - Similarly, if you are passing in two lists of variables and you require both lists to be the same length (because the elements need to correspond with each other), consider using one list of composite domain objects instead.
- Avoid redefining the same variable more than once. Use different names to represent different variables, since each variable (conceptually) stores a different thing.
- Functions that start with "get", or which have GET semantics, should, under no circumstances, update or delete anything. They should be safe to call and have no side effects.


## Python
- Consider using a frozenset or tuple to a list, if the data structure is not meant to be subsequently modified. This applies especially to constants.
- If you need to raise an Exception, just do `raise Exception` -- no need to define custom exceptions. We tend to use exceptions fairly sparingly, though.
- Do not use `str()` under any circumstances. Please try to use `python_utils.convert_to_bytes()` or the `b'` prefix for the strings used in webapp2\'s built-in methods or for strings used directly in NDB datastore models. If you need to cast ints/floats to strings, please use `python_utils.UNICODE()` instead. Avoid casting strings to other types of strings using str(), unicode(), etc. Also, there should be no need to prefix any string literals with b' or u', since all string literals in Python files are prefixed with `u'` by default (due to the import of unicode_literals at the top of the file).
- Otherwise, please follow the [Google Python style guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md). In particular:
  - There should be two empty lines before any top-level class or function definition.
  - It's OK for the initial documentation string to be more than one line long.
  - Prefer string interpolation over concatenation -- e.g. prefer: `'My string %s' % varname` to `'My string ' + varname`.
  - When indenting from an open parenthesis ('('), prefer indenting by 4 rather than indenting from the position of the parenthesis. e.g., prefer:

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
    Docstrings should also contain `Args`, `Returns` and `Raises` whenever applicable in a method. For example:

    ```
    def function_name(arg1, arg2):
        """Brief description about the function.

        Args:
            arg1: type. Short description.
            arg2: type. Short description.

        Returns:
            type. Short description.

        Raises:
            TypeOfException: Short description.
        """
    ```
  - Never use backslashes to end a line. It's hard to tell whether they're escaping newlines, spaces, or something else. Use parentheses instead to break the line up, e.g.:

    ```
       my_variable = (
           my_very_long_module_name.my_really_long_function_name())
    ```
  - Be careful [not to use mutable objects](https://google.github.io/styleguide/pyguide.html?showone=Default_Argument_Values#Default_Argument_Values) as default values in the function or method definition. i.e., don't do things like `def foo(a, b=[]):`.

  - Imports should be in three groups: standard libraries, files within the Oppia codebase, and third-party files. Each group should be separated by a single newline. Within each group, imports should be organized alphabetically. If you have additional questions, feel free to reference the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#313-imports-formatting).

### Apache Beam logic
  - For pipe operations that span multiple lines, always have the pipe operator (`|`) begin on the new line.

    e.g., prefer:

    ```python
    pcoll = (
        input_pcoll
        | "Op1" >> Operation1()
        | "Op2" >> Operation2()
        | "Op3" >> Operation3()
        | "Op4" >> Operation4()
    )
    ```

    over:

    ```python
    pcoll = (
        input_pcoll | "Op1" >> Operation1() | "Op2" >>
        Operation2() | "Op3" >> Operation3() |
        "Op4" >> Operation4() 
    )
    ```

    Note: when all pipe operations can fit in a single line, there's no need to break them up:
    ```python
    pcoll = input_pcoll | "Sort" >> Sort()
    pcoll = (
        input_pcoll | "Sort" >> Sort() | "Unique" >> Unique())
    ````

## JavaScript
_General note: We use the ES2017 standard for our JavaScript/TypeScript code. (See [tsconfig.json](https://github.com/oppia/oppia/blob/57333f23af7b67914dc039671f4bc4e029fbb6e7/tsconfig.json#L4).)_

- We use extra parentheses if a statement breaks across multiple lines, similar to Python. In particular, when code in '(...)' or '[...]' spans more than one line, make a line break after the opening parentheses or bracket.
- The indentation is always 2 spaces.
- Try to start only function names with verbs to help distinguish them from variables. Conversely, do not start variable names with verbs.

   For example:

   - For a boolean variable to check if a card is displayed:
        - Correct: `cardIsDisplayed`
        - Wrong: `isCardDisplayed`

   - For a function to check if a card is displayed:
        - Correct: `isCardDisplayed()`
        - Wrong: `cardIsDisplayed()`
- We have started compiling a [style guide for JavaScript](https://docs.google.com/document/d/1ZDmLN66f53WdDPItFChu9Lr37z0dKoqR-ASX8UM5y60). This is currently a work in progress. However, please use this as the definitive guide when figuring out the correct way to name things (CamelCase, snake_case, etc.)
- The dependencies mentioned in strings and functional parameters of controllers, directives and factories should be in the following manner: dollar imports (e.g. ```$log, $scope``` etc.), regular imports (e.g. ```ContextService, PageService``` etc.), and constant imports (e.g ```COLLECTION_TAGS, DELETE_COLLECTION``` etc.) all in sorted order.

    For Example:
    ```javascript
    oppia.thing('ThingName', [
      '$sortedDollarImports', 'SortedRegularImports',
      'SORTED_CONSTANT_IMPORTS',
      function(
          $sortedDollarImports, SortedRegularImports,
          SORTED_CONSTANT_IMPORTS) {
        // The implementation of `ThingName`.
      }]);
    ```
- For asynchronous functions that return a promise, use the following convention:
  - At the function declaration, use the keyword `async` (see [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)).
  - Add 'Async' to the function name. example:
    ```ts
    const getUserInfoAsync = async function() {
      return new Promise(resolve => {
        setTimeout(function() {
          resolve("something");
        }, 2000);
       });
    }
    ```
- For functions or variables that are private and that should not be exposed outside their immediate controller/service, prefix their names with an underscore (`_`) and add the `private` keyword.

## Typescript
- Make sure to follow all the javascript rules here as well.
- Keep line lengths to at most 80 characters (with the exception of lines containing URLs, which are allowed to have a length of greater than 80 characters).
- Declare a variable before usage. For instance:

  **Wrong usage:**
  ```javascript
  exampleVar = true;
  if (someCondition) {
    exampleVar = false;
  }
  ```
  **Right usage:**
  ```javascript
  var exampleVar = true;
  if (someCondition) {
    exampleVar = false;
  }
  ```
- All loop variables should be declared. For instance:

  **Wrong usage:**
  ```javascript
  for (item in itemList) {
    ...
  }
  ```
  **Right usage:**
  ```javascript
  for (var item in itemList) {
    ...
  }
  ```

- Do not add new properties to a declared variable. Ensure that all properties are declared in the variable declaration. For instance:

  **Wrong usage:**
  ```javascript
  var person = {
    name: 'name',
    age: 'age'
  };
  if (someCondition) {
    person.address = 'address';
  }
  ```
  **Right usage:**
  ```javascript
  var person = {
    name: 'name',
    age: 'age',
    address: null
  };
  if (someCondition) {
    person.address = 'address';
  }
  ```
- Always initialize a variable at declaration. If you do not want a specific value at declaration, initialize the variable with a null value. For instance:

  **Wrong usage:**
  ```javascript
  var person;
  if (someCondition) {
    person = 'name';
  }
  ```
  **Right usage:**
  ```javascript
  var person = null;
  if (someCondition) {
    person = 'name';
  }
  ```
- Do not overwrite the variable with a different type. Instead create a new variable whenever you have a different use case. For instance:

  **Wrong usage:**
  ```javascript
  var person = {
    name: 'name',
    schoolName: 'school name'
  };
  ...
  person = {
    name: 'name',
    officeName: 'office name'
  };
  ```
  **Right usage:**
  ```javascript
  var personForSchool = {
    name: 'name',
    schoolName: 'school name'
  };
  ...
  var personForOffice = {
    name: 'name',
    officeName: 'office name'
  };
  ```
- If you get compilation error which says that a property does not exist on a particular type, go through the type definitions of the type and do a type casting if required. For instance:
  ```javascript
  var checkMismatch = function(searchQuery) {
    var isMismatch = true;
    $('.oppia-search-bar-input').each(function(index) {
      if ((<string>$(this).val()).trim() === searchQuery) {
        isMismatch = false;
      }
    });
    return isMismatch;
  };
  ```
  Here `$(this).val()` is type casted to a string by using `<string>$(this).val()`
  If we do not use a typecast, typescript will give a error `Property 'trim' does not exist on type 'string | number | string[]'` since val can be a string or a number or a string array. So, to use trim we specifically need it as a string.

  In many cases, you may also need to typecast to `<any>` first and then to the desired type. For example, for converting a number to string, you will need `<string><any>` because neither type sufficiently overlaps with the other.

  You can add a new custom type definitions if type casting is not possible. In the file `typings/custom-element-defs.d.ts`, we add a new property to `HTMLElement` by adding a custom type defintion. In this type casting cannot be used, since we are adding a new property to the existing type instead of changing it to some other type.

### Karma test specific guidelines
- Use `angular.mock.module` instead of `module` since the typings for angular-mocks does not support the usage of module.
- Use `angular.mock.inject` instead of `inject` to maintain a consistent behaviour.

### When to add custom type defintions to the typings folder?
- If you find a missing property in a typings package, create an issue [here](https://github.com/DefinitelyTyped/DefinitelyTyped) and a new file for the custom types with the issue link in the top of the file.
- If you add a package for which type definitions are not found [here](https://github.com/DefinitelyTyped/DefinitelyTyped), add it to `third-party-defs.d.ts`
- If you add a new property on window which is not present in typings for window, add it to `custom-window-defs.d.ts`
- If you add a property on scope defined in a link function, add it to `custom-scope-defs.d.ts` and add a comment specifying the filename for which it is added.
- Make sure that all files have comments which explain why these custom type defintions are required and additional comments to explain each new added property if required. For example, `typings/custom-scope-defs.d.ts` has a top level comment explaining that the type defintions are needed for properties defined on scope in link function and then there are additional comments with properties added specifying which file they belong to. Go through the existing files and try to follow the same pattern when adding a new file.

### Component Directives
Usage of old-style AngularJS directives is discouraged. Instead, use component directives. Component directives are an advanced version of AngularJS directives and are more preferred because of the "isolated scope" it creates and the reusability it offers across modules. This is also the way forward in Angular 2+.

- Do not create standalone controllers. The standalone controllers are those which are associated with the `ng-controller` directive in the HTML file.
- While creating a new directive, make sure to use the component directive instead of the old style directives. Now, here's something: The component directives create what is called an "isolated scope". So the component directive can be thought of as a reusable component not dependent on its surroundings and hence "isolated". Therefore you must not use `$scope` in the directive, except for some exceptions like `$scope.$on`, `$scope.$apply` and other internal functions of `$scope` which do not have a full replacement. Also `$uibmodal`s are exempted from this rule.
- There are many instances where this "isolated scope" needs to communicate with the surrounding, in such cases you must pass such data through the `bindToController` key of the component directive. This binds the values to the controller of the component directive and you can access those values in your directive's isolated scope.

## Webpack

In all TypeScript files in `core/templates` we use webpack. That means that instead of including the required files by `<script src="…"></script>` in HTML files we include them by using `require(…)` in the individual TS files.

### Adding `require(…)` to the TypeScript files with service/filter/factory
When you add new service/filter/factory dependency to service/filter/factory, you need to also `require(…)` it at the top of the file.

For example if you have this filter:
```javascript
oppia.filter('normalizeWhitespace', [function() {
  return function(input) {…};
}]);
```
and need to use `UtilsService` in this filter, you also need to add `require('services/UtilsService.ts');` (the paths are relative to the `core/templates` directory), the final filter will look like this:
```javascript
require('services/UtilsService.ts');

oppia.filter('normalizeWhitespace', ['UtilsService', function(UtilsService) {
  return function(input) {…};
}]);
```

**The requires should be sorted in alphabetical order.**

### Adding `require(…)` to the TypeScript files with directive
The rules for directives are little bit more complex. You also need to add `require(…)` for service/filter/factory dependencies, but also if you use custom directive in the HTML you need to `require(…)` it in the TypeScript file too.

For example, if you have directive:
```javascript
require('domain/utilities/UrlInterpolationService.ts');

oppia.directive('storySummaryTile', ['UrlInterpolationService', function(UrlInterpolationService) {
    return {…};
}]);
```
and add `<sharing-links>` into the **story_summary_directive.html** you need to also add the new `require('components/share/SharingLinksDirective.ts');` into the TypeScript file:
```javascript
require('components/share/SharingLinksDirective.ts');

require('domain/utilities/UrlInterpolationService.ts');

oppia.directive('storySummaryTile', ['UrlInterpolationService', function(UrlInterpolationService) {
    return {…};
}]);
```

**The requires for directives that are in HTML are included first and separated from the regular requires by empty line.**

### Exporting variables and functions from a Typescript file to be imported in another Typescript file.

If the file adds variable to the global scope:
```javascript
// functions.ts
var functions = function() {
  // something happens here.
}
```
We want to isolate that scope, this can be done by exporting the variable using ES6 exports.
```javascript
// functions.ts
var functions = function() {
  // something happens here.
}
export default functions;
```
And then the variable can be loaded by `import functions from 'folder/folder/functions.ts';`

## CSS
- Do not include units if the value is 0. E.g. `margin-left: 0` instead of `margin-left: 0px`.
- Within each CSS rule, attributes should be alphabetized (e.g. 'height' before 'margin' before 'top'). This makes it easy to find the value of an attribute if there are lots of them.
- Avoid using `!important` as much as possible.
- For colours, use hex values (like "#012345") or rgb(a) values, instead of names (like "white"). When using hex colour codes, try to use the 3 char version if possible (see [example](https://google.github.io/styleguide/htmlcssguide.html#Hexadecimal_Notation)).
- If the CSS class is oppia-specific, prefix it with `oppia-`. This helps distinguish it from CSS classes used by other third-party libraries.
- For directives, include the CSS in the directive template file, similar to what we do in [this file](https://github.com/oppia/oppia/blob/37a43ca249ffd2b60bf98f791995048ce0ec5269/core/templates/components/summary_tile/exploration_summary_tile_directive.html). (Note that, in this case, all CSS rules should start with the top-level CSS class of the directive, so that they don't affect other elements outside it.) All other CSS should go in `core/templates/css/oppia.css`.

----
### How to ensure that your code follows the coding guidelines:

You can invoke the pre-commit script to ensure that your code follows the coding guidelines for a particular file that you've modified by running the following command from the root directory:
```bash
python -m scripts.linters.pre_commit_linter --path filepath
```

If you'd like to run the checks for a list of files, run the following command:
```bash
python -m scripts.linters.pre_commit_linter --files file_1 file_2 ... file_n
```

If you'd like to run the checks for a list of file-types, run the following command:
```bash
python -m scripts.linters.pre_commit_linter --only-check-file-extensions file_extension_type_1 file_extension_type_2 ... file_extension_type_n
```

### Note for Sublime Text users

If you use Sublime Text, the following settings may be useful for your "Preferences.sublime-settings -- User" file (go to Preferences > Settings)

```
{
    "ensure_newline_at_eof_on_save": true,
    "font_size": 9,
    "highlight_line": true,
    "rulers":
    [
        80
    ],
    "shift_tab_unindent": true,
    "spell_check": true,
    "tab_size": 4,
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true,
    "update_check": false
}
```
