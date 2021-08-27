## Type Annotations
 
Type Annotations are a new feature added in [PEP 484](https://www.python.org/dev/peps/pep-0484/) that allow for adding type hints to variables. They give information about types of variables to someone who is reading the code. This brings a sense of statically-typed control to the dynamically typed Python. Though Python ignores these type hints during code execution, third-party libraries can be used to statically type-check the codebase.
 
 
## Where to add type annotations
 
1. If a new file is added, it must have type annotations.
2. If a file is updated, then:
   - If the file already has type annotations, then the updated code must also have type annotations.
   - If the file has no type annotations, then the updated code may or may not have type annotations.
 
 
## Running MyPy check script
 
Mypy checks script (`scripts/run_mypy_checks.py`) is the script used to run our mypy type checks.
 
It has two modes of running:
 
1. `python -m scripts.run_mypy_checks`\
  This runs the type checks on all the type annotated files in the codebase.
2. `python -m scripts.run_mypy_checks --files path/file1.py path/file2.py`\
  This runs the type checks on the files specified, i.e., file1 and file2.
 
**Note:**
- `python -m scripts.run_mypy_checks --skip-install` can be used to skip installation of third party libraries. Please use the `--skip-install` flag only when you already have all the third party libraries installed.
 
-  Move environment directories out of the oppia root folder as mypy will throw errors for environment directory files too.
 
 
## Adding type annotations
 
The method to write type annotations is to figure out types of the variables and mention them.
 
### Steps to add type annotation to a file:
 
**Note**: Type annotation to a main code file and its test file will be added together.
 
1.  Run mypy type checks on the main code file you are trying to annotate. This will give the errors.
2.  Start solving these one by one.
3.  Let’s say a function is not type annotated, you should first look at the function arguments and the return value. Try to get information of the types from the function docstring, test file, function code and function usage. Let’s say in the example given below, where we have a function to take two integers and convert them to string and return the concatenated string, you can figure out from the function code that the return type will be a string. The type of the arguments can be figured out by taking a look at the docstring, tests and usage of the functions.
 
    - The original example code:
     ```
     def concat(x, y):
         return str(x) + str(y)
     ```
    - After adding type annotation:
     ```
     def concat(x: int, y: int) -> str:
         return str(x) + str(y)
     ```
    - Avoid using `Any` type. If you have no other option, make sure you have a proper reason and add an explanatory comment for it.
 
4.  You may also get errors when Mypy is not able to infer the type of a variable, then you must specify the type of the variable.
 
    - The original code example:
     ```
     d = {
       ‘a’: 1,
       ‘b’: 2,
       ‘c’: 3
     }
     ```
    - After adding type annotation:
     ```
     d: Dict[str, int] = {
       ‘a’: 1,
       ‘b’: 2,
       ‘c’: 3
     }
     ```
 
5.  To understand what different error codes mean take a look at different [Error Codes](https://mypy.readthedocs.io/en/latest/error_code_list.html) in MyPy docs.
 
    - First try to find the reason behind that error. If that error can be resolved by some improvements in the codebase, then make the necessary changes.
    - If there are no options left to resolve that error, then only go for ignoring the error. For any ignore other than `[no-untyped-call]`, make sure you have a proper reason and add an explanatory comment for it.
    - Some ignored errors can be fixed in future, so make a TODO issue for them like [this](https://github.com/oppia/oppia/issues/13059) and write a todo in the file with the issue number of the issue created.
 
 
6.  When the main code file has no errors, start type annotating the corresponding test file. Note that in the test file, there may be deliberate errors which are used to test that the functions should fail. These errors must be silenced using `# type: ignore[<error-code>]` where <error-code> is the code of the error to be silenced. Example of such error code is `[arg-type]`. Explain such ignores and add a TODO for the [issue](https://github.com/oppia/oppia/issues/13528) above such ignores so that this test can be removed if it is unnecessary.
 
7.  When both the main code file and its test file have been type annotated, remove both of them from the list `NOT_FULLY_COVERED_FILES` in `scripts/run_mypy_checks.py` so that these files are considered as type annotated.
 
For more information on adding types, refer to [Mypy Cheat Sheet(Python 3)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).
