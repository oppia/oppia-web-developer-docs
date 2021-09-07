## Why do we use Type Annotations?

Type Annotations are a new feature added in [PEP 484](https://www.python.org/dev/peps/pep-0484/) that allow for adding type hints to variables. They give information about types of variables to someone who is reading the code. This brings a sense of statically-typed control to the dynamically typed Python. Though Python ignores these type hints during code execution, third-party libraries can be used to statically type-check the codebase.


## When to add type annotations
We use mypy to type check the backend part of our codebase. A file becomes eligible for type checking if it falls under one of the following 3 cases:
1. If a **new file** is being added, it must be fully type annotated and hence type checked.
2. If an **already type annotated file** is being updated, then the updated code must also have type annotations.
3. If you are adding type annotations to a currently **non type-annotated file**, then make sure to fully type annotate it, and remove it from the mypy denylist.

### Mypy Denylist - Important Note!
Currently we are in the process of adding type annotations the whole codebase. We maintain a denylist called `NOT_FULLY_COVERED_FILES` inside `scripts/run_mypy_checks` - it holds the list of files/folders for which we want to skip mypy type checking. When you add/modify files, make sure to **remove the file(s) eligible for type checking from this denylist if you have fully type annotated them**, otherwise it won't be considered for type checking, and the file might be even left with incorrect annotations.

## Running MyPy check script

Mypy checks script (`scripts/run_mypy_checks.py`) is the script used to run our mypy type checks.

It has two modes of running:

1. `python -m scripts.run_mypy_checks`\
  This runs the type checks on all the type annotated files in the codebase.
2. `python -m scripts.run_mypy_checks --files path/file1.py path/file2.py`\
  This runs the type checks on the files specified, i.e., file1 and file2.

**Note:**
- [Helpful trick for faster runs]`python -m scripts.run_mypy_checks --skip-install` can be used to skip installation of third party libraries. Please use the `--skip-install` flag **only** when you already have all the third party libraries installed.


## Adding type annotations

Once you've figured whether or not to add type annotations to a file, follow these steps. Here the method is simply to figure out types of the variables and mention them according to the syntax.

### Steps to add type annotations to a file:

**Note**: Test file should **always** be type annotated along with the main code file (if the latter one is going to be fully annotated).

1.  Run mypy type checks on the main code file you are trying to annotate. This will give the errors. (Either use the `--files` version or use the normal version but ensure that the file is removed from mypy denylist)
2.  Start solving these errors one by one.
3.  Let’s say a function is not type annotated, you should first look at the function arguments and the return value. Try to get information of the types from the function docstring, test file, function code and function usage. Let’s say in the example given below, where we have a function to take two integers and convert them to string and return the concatenated string, you can figure out from the function code that the return type will be a string. The type of the arguments can be figured out by taking a look at the docstring, tests and usage of the functions.

    - The original example code:
     ```python
     def concat(x, y):
         return str(x) + str(y)
     ```
    - After adding type annotation:
     ```python
     def concat(x: int, y: int) -> str:
         return str(x) + str(y)
     ```
    - **Avoid using `Any` type**. Always try to reason out why it is needed, try to arrive at a stricter type. In case you go ahead with `Any` type, make sure you have a proper reason and add an explanatory comment for it. [Example 1](https://github.com/oppia/oppia/blob/b0c6ffb917663fb6482022d0f607377f7e1ee3d0/constants.py#L31-L33), [Example 2](https://github.com/oppia/oppia/blob/develop/core/controllers/access_validators.py#L40-L42).

4.  You may get errors when **Mypy is not able to infer the type of a variable**, then you must specify the type of the variable as demonstrated below.

    - The original code example:
     ```python
     d = {
       ‘a’: 1,
       ‘b’: 2,
       ‘c’: 3
     }
     ```
    - After adding type annotation:
     ```python
     d: Dict[str, int] = {
       ‘a’: 1,
       ‘b’: 2,
       ‘c’: 3
     }
     ```

5.  **To understand what different error codes mean** take a look at different [Error Codes](https://mypy.readthedocs.io/en/latest/error_code_list.html) in MyPy docs.

    - First try to find the reason behind that error. If that error can be resolved by some improvements in the codebase, then make the necessary changes.
    - If there are no options left to resolve that error, then only go for ignoring the error. **For any kind ignore** other than `[no-untyped-call]`, make sure you have a proper reason and add an explanatory comment for it - [Example 1](https://github.com/oppia/oppia/blob/b0c6ffb917663fb6482022d0f607377f7e1ee3d0/core/platform/cache/redis_cache_services.py#L61), [Example 2](https://github.com/oppia/oppia/blob/b0c6ffb917663fb6482022d0f607377f7e1ee3d0/core/controllers/oppia_root.py#L31-L33).
    - Some ignored errors can be fixed in future, so make a TODO issue for them with clear explanation like [this](https://github.com/oppia/oppia/issues/13059) and write a TODO in the file with the issue number of the issue created.


6.  When the main code file has no errors, start type annotating its corresponding test file. Note that in the test file, there may be **cases where we deliberately provide wrong (or wrongly typed) arguments to test** that the function fail on them. Such errors must be silenced using `# type: ignore[<error-code>]` where <error-code> is the code of the error to be silenced with an explanatory comment.
    - Example of such error code is `[arg-type]`. All cases of [arg-type] ignores should be explained and a TODO for the [issue](https://github.com/oppia/oppia/issues/13528) should be added above such ignores so that this test can be removed if it is unnecessary like [here](https://github.com/oppia/oppia/blob/f7a5746a80730753b32b555306f20c55d4023822/core/storage/email/gae_models_test.py#L164-L166).

7.  When you are done with **fully** adding type annotations to the files, make sure to **remove them from the mypy denylist** as told before. Also run the mypy type checks again on the entire codebase to ensure there are no more type errors.

For more information on adding types, refer to [Mypy Cheat Sheet(Python 3)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).

## Special Cases
1. Description: Code using `inspect.getargspec` method is throwing an error `ValueError: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them` after adding type annotation.
    - Explanation: `getargspec` has been [deprecated](https://docs.python.org/3/library/inspect.html#inspect.getargspec) and does not support parsing annotations
    - Solution: Use the updated version of the method - `getfullagrspec` - this supports parsing of type annotations. [Example](https://github.com/oppia/oppia/blob/b0c6ffb917663fb6482022d0f607377f7e1ee3d0/schema_utils_test.py#L280).

## Other Important points
1. Use `str` instead of Text wherever applicable. (Text was used in the Python2 version of codebase. We also have a lint check now to prevent usage of Text in type annotations)
2. For external libraries we obtain the type information from the type stubs defined in the [typeshed](https://github.com/python/typeshed) package (which come bundled with mypy for it's current version `0.812` that we use).
    - In case of **missing stubs** (when typeshed doesn't support a library yet), mypy will throw errors and ask you to use type `Any` or type ignores to silence those errors, but this can lead to loose and inconsistent typing for imports from those packages, so we avoid that practice.
    - Instead, to overcome that, we follow the practice of **defining the stubs ourselves** only for the part of the library we are using, and place those stubs inside the `stubs/` folder. You can look at the existing stubs as an example to understand how this works.
3. Types (like Dict, Any, Union etc) from the typing module can be imported in the same line. Do not use `isort:ignore`. If the import exceeds line length limit, use parenthesis to span across multiple lines. See the following cases to understand.
```python
# Wrong usage
from typing Any
from typing import Dict

# Correct usage (1)
from typing import Any, Dict
# Correct Usage (2)
from typing import (
    Any, Callable, Dict, Iterable, Iterator, List, Optional, Sequence,
    Type, TypeVar, Tuple, Union)

```

## Troubleshooting
1. If you are seeing type errors for unchanged files, especially which are not part of the Oppia codebase, a possible reason could be that you have the virtual environment directory inside the Oppia root folder. Moving the environment folder out of the Oppia root directory resolves this error.
