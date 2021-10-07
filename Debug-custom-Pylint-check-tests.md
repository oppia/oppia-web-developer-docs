## Table of contents

* [Introduction](#introduction)
* [Run a single checker](#run-a-single-checker)
  * [Print statements](#print-statements)
  * [The Python debugger](#the-python-debugger)

## Introduction

When trying to debug the tests for a custom Pylint checker, remember that the tests are just like any other backend test. You may find our [[guide to debugging backend tests|Debug-backend-tests]] useful. That said, there are some helpful tips for working with Pylint checkers in particular. We describe them below.

## Run a single checker

Debugging a Pylint checker's tests often comes down to debugging the checker itself. To see how your checker behaves on some code, put that code into `test.py`. Then assuming that your checker has message with symbol `my-checker-message`, you can run your checker on `test.py` like this:

```console
$ PYTHONPATH=scripts/linters ../oppia_tools/pylint-2.8.3/bin/pylint --load-plugins=pylint_extensions --disable=all --enable=my-checker-message test.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

```

(These instructions come from the [Pylint documentation](https://pylint.pycqa.org/en/latest/how_tos/custom_checkers.html#debugging-a-checker).) Note that the Pylint version number (2.8.3 in this case) may vary.

In this case, the checker found no issues with our code in `test.py`, but your checker might flag problems with the code in `test.py`. In either case, you should consider whether your checker behaved as expected. Did the checker flag any code that isn't actually a problem? Did the checker miss any problematic code? If the checker behaved unexpectedly, you should debug further. You may find two other debugging strategies useful: print statements and the Python debugger.

### Print statements

You can print out debugging information from your checker code using `print()` statements. The output will appear when you run the checker as shown above. For example, if we added a `print('DEBUGGING')` statement to our checker, we might see:

```console
$ PYTHONPATH=scripts/linters ../oppia_tools/pylint-2.8.3/bin/pylint --load-plugins=pylint_extensions --disable=all --enable=my-checker-message test.py
DEBUGGING

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

```

### The Python debugger

Just like when debugging backend tests, you can use the Python debugger, pdb, with Pylint checkers. You just need to add this code to your checker:

```python
import pdb; pdb.set_trace()
```

If you aren't familiar with pdb, take a look at our [[guide to debugging backend tests|Debug-backend-tests]].
