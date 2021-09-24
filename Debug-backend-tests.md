## Table of contents

* [Introduction](#introduction)
* [Interpret log output](#interpret-log-output)
* [Find tests](#find-tests)
* [Run tests in isolation](#run-tests-in-isolation)
* [Increase verbosity](#increase-verbosity)
* [Use the Python debugger](#use-the-python-debugger)
  * [Step 1: Insert break points](#step-1-insert-break-points)
  * [Step 2: Run test with unittest](#step-2-run-test-with-unittest)
  * [Step 3: PDB commands](#step-3-pdb-commands)

## Introduction

When your backend tests fail, the strategies below can help you figure out how to fix them. We recommend the following workflow:

1. [Look at the log output](#interpret-log-output) to understand what it means.
2. [Find the test that failed](#find-tests) and examine its code.
3. [Run the failing test in isolation](#run-tests-in-isolation) so that you can iterate more quickly.
4. Use [print statements](#increase-verbosity) and/or [the Python debugger](#use-the-python-debugger) to investigate further.

## Interpret log output

When your backend tests fail, look near the end of the log for output that looks like this:

```text
======================================================================
FAIL: test_failed_api_call_logs_the_exception (jobs.jobs_manager_test.RefreshStateOfBeamJobRunModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/oppia/oppia/jobs/jobs_manager_test.py", line 158, in test_failed_api_call_logs_the_exception
    lambda: jobs_manager.refresh_state_of_beam_job_run_model(
  File "/home/runner/work/oppia/oppia/core/tests/test_utils.py", line 1306, in assertRaisesRegexp
    expected_exception, expected_regex, *args, **kwargs)
AssertionError: Exception not raised by <lambda>

---------------------------------------------------------------------
```

This is the part of the log that you should pay attention to. It tells you which test failed and why the failure occurred. Here's how to read it:

* At the top, the line beginning with `FAIL` tells you which test failed. In this case, it's the `test_failed_api_call_logs_the_exception` test in the `jobs.jobs_manager_test.RefreshStateOfBeamJobRunModelTests` class. Note that this line can also start with `ERROR`. `FAIL` indicates that an assertion failed, while `ERROR` indicates that an exception (other than `AssertionError`) was raised unexpectedly.
* Next is the traceback. This shows you the state of the stack when the error was raised. In this example:

  * The `AssertionError` was raised by line 1306 of `test_utils.py` in the `assertRaisesRegexp()` function.
  * That `assertRaisesRegexp()` function was called on line 158 of `jobs_manager_test.py` in the `test_failed_api_call_logs_the_exception()` function. Since this is the function defining our test, it's the end of the trace.

* Lastly, the line starting with `AssertionError` describes what caused the test to fail. In this case, it's because we expected an exception to be raised, but that didn't happen.

## Find tests

You usually want to look at the full code of the failing test to better understand what could have gone wrong. Unittest, the Python testing framework we use, makes this really easy: the description of which test failed also tells us exactly where to find it. In the example above, we saw this line:

```text
FAIL: test_failed_api_call_logs_the_exception (jobs.jobs_manager_test.RefreshStateOfBeamJobRunModelTests)
```

This means that the full dotted name of the failing test function is:

```text
jobs.jobs_manager_test.RefreshStateOfBeamJobRunModelTests.test_failed_api_call_logs_the_exception
```

In Python, the first part of a dotted name describes a file path. In this case, the `jobs` at the start of the name refers to the `jobs/` folder at the root of the repository. Inside that folder is `jobs_manager_test.py`, which matches the `jobs_manager_test` part of the dotted name. (Notice that the `.py` extension of the file name disappeared.)

Now that we've reached a file, the rest of the dotted name refers to Python attributes. The `jobs_manager_test.py` file defines the `RefreshStateOfBeamJobRunModelTests` class, which has a `test_failed_api_call_logs_the_exception` method. This is the method that defines our test!

## Run tests in isolation

When you know which test is causing you problems, running it in isolation can help you debug. For one thing, the tests will run much faster if you only run a few in isolation. Further, the console output from the test run will be much easier to understand.

To run a test in isolation, you can use the `--test_target` option:

```console
python -m scripts.run_backend_tests --test_target jobs.jobs_manager_test.RefreshStateOfBeamJobRunModelTests.test_failed_api_call_logs_the_exception
```

If you wanted to run all the tests defined by the `RefreshStateOfBeamJobRunModelTests`, you could do that too. Just shorten the dotted name to end at the class:

```console
python -m scripts.run_backend_tests --test_target jobs.jobs_manager_test.RefreshStateOfBeamJobRunModelTests
```

Note that if you want to run all the tests in a directory, you need to use `--test_path` instead like this:

```console
python -m scripts.run_backend_tests --test_path jobs
```

**Make sure that you can reproduce the problem you are trying to debug when you run the test in isolation!** While rare, it is possible for a test failure to have been caused by previous tests. In these cases, you may not be able to reproduce the problem when you only run the test that initially failed.

## Increase verbosity

Normally, we suppress any console output from passing tests, so even if you add print statements for debugging, you'll only see a success message:

```text
[datastore] Sep 19, 2021 3:30:21 PM io.gapi.emulators.grpc.GrpcServer$3 operationComplete
[datastore] INFO: Adding handler(s) to newly registered Channel.
[datastore] Sep 19, 2021 3:30:21 PM io.gapi.emulators.netty.HttpVersionRoutingHandler channelRead
[datastore] INFO: Detected HTTP/2 connection.
19:30:23 FINISHED scripts.run_e2e_tests_test.RunE2ETestsTests.test_is_oppia_server_already_running_when_ports_closed: 22.1 secs
Stopping Redis Server(name="redis-server", pid=37086)...
Stopping Cloud Datastore Emulator(name="python2.7", pid=37069)...

+------------------+
| SUMMARY OF TESTS |
+------------------+

SUCCESS   scripts.run_e2e_tests_test.RunE2ETestsTests.test_is_oppia_server_already_running_when_ports_closed: 1 tests (1.2 secs)

Ran 1 test in 1 test class.
All tests passed.
```

However if you pass the `--verbose` flag when running the backend tests, you'll see console output. For example, here we added a `print('HELLO THERE')` statement to the test:

```text
[datastore] Sep 19, 2021 3:32:28 PM io.gapi.emulators.grpc.GrpcServer$3 operationComplete
[datastore] INFO: Adding handler(s) to newly registered Channel.
[datastore] Sep 19, 2021 3:32:28 PM io.gapi.emulators.netty.HttpVersionRoutingHandler channelRead
[datastore] INFO: Detected HTTP/2 connection.
19:32:30 LOG scripts.run_e2e_tests_test.RunE2ETestsTests.test_is_oppia_server_already_running_when_ports_closed:
HELLO THERE
test_is_oppia_server_already_running_when_ports_closed (scripts.run_e2e_tests_test.RunE2ETestsTests) ... ok

----------------------------------------------------------------------
Ran 1 test in 1.455s

OK
----------------------------------------
19:32:30 FINISHED scripts.run_e2e_tests_test.RunE2ETestsTests.test_is_oppia_server_already_running_when_ports_closed: 26.3 secs
Stopping Redis Server(name="redis-server", pid=37294)...
Stopping Cloud Datastore Emulator(name="python2.7", pid=37277)...

+------------------+
| SUMMARY OF TESTS |
+------------------+

SUCCESS   scripts.run_e2e_tests_test.RunE2ETestsTests.test_is_oppia_server_already_running_when_ports_closed: 1 tests (1.5 secs)

Ran 1 test in 1 test class.
All tests passed.
```

If a test fails, you'll always see its console output:

```text
[datastore] Sep 19, 2021 3:34:41 PM io.gapi.emulators.grpc.GrpcServer$3 operationComplete
[datastore] INFO: Adding handler(s) to newly registered Channel.
[datastore] Sep 19, 2021 3:34:41 PM io.gapi.emulators.netty.HttpVersionRoutingHandler channelRead
[datastore] INFO: Detected HTTP/2 connection.
19:34:42 ERROR scripts.run_e2e_tests_test.RunE2ETestsTests.test_is_oppia_server_already_running_when_ports_closed: 21.1 secs
Error 1
HELLO THERE
test_is_oppia_server_already_running_when_ports_closed (scripts.run_e2e_tests_test.RunE2ETestsTests) ... FAIL

======================================================================
FAIL: test_is_oppia_server_already_running_when_ports_closed (scripts.run_e2e_tests_test.RunE2ETestsTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/oppia/scripts/run_e2e_tests_test.py", line 70, in test_is_oppia_server_already_running_when_ports_closed
    raise AssertionError('hi')
AssertionError: hi

----------------------------------------------------------------------
Ran 1 test in 1.078s

FAILED (failures=1)
Traceback (most recent call last):
  File "/oppia/core/tests/gae_suite.py", line 126, in <module>
    main()
  File "/oppia/core/tests/gae_suite.py", line 122, in main
    result.testsRun, len(result.errors), len(result.failures)))
Exception: Test suite failed: 1 tests run, 0 errors, 1 failures.

Stopping Redis Server(name="redis-server", pid=38032)...
Stopping Cloud Datastore Emulator(name="python2.7", pid=38015)...

+------------------+
| SUMMARY OF TESTS |
+------------------+
...
```

Notice that the `HELLO THERE` output appears above the summary of tests.

## Use the Python debugger

The Python debugger, or [pdb](https://docs.python.org/3/library/pdb.html), is very helpful for debugging tests. It is very similar to [GDB](https://www.gnu.org/software/gdb/), the GNU Debugger, in case you are familiar with GDB already.

With pdb, you set break points to tell the debugger where to pause when executing your code. When the debugger pauses, you are dropped into a debugging shell where you can execute normal Python statements or pdb commands. The shell reflects the state of your program at the break point, so you can print out variable values, call functions, and even change variables in your program.

### Step 1: Insert break points

To begin, insert a break point in your code like this:

```python
import pdb; pdb.set_trace()
```

When your test executes, the debugger will pause every time it executes this line.

### Step 2: Run test with unittest

To use pdb, you cannot use the `run_backend_tests.py` script. Instead, you need to run the test you want to debug using Python's native [unittest](https://docs.python.org/3/library/unittest.html) command:

```console
python -m unittest [full dotted name to test function]
```

### Step 3: PDB commands

Once you are in a debugging shell, you can also use any of the following pdb commands:

* `w(here)`: Print a stack trace based on your current location in the program.
* `d(own)`: Move down one frame in the stack (to a newer frame).
* `u(p)`: Move up one frame in the stack (to an older frame).
* `s(tep)`: Execute the current line and stop at the next line of code, even if that next line is inside the function called on the current line. You can think of this as stepping into the function call on the current line.
* `n(ext)`: Execute the current line and stop at the next line in the current function. If a function is called on the current line, the debugger will not stop inside that function.
* `c(ontinue)`: Continue executing the program until the next break point.
* `l(ist)`: List the source code around your current line, or continue your previous listing if you've already called `list` on the current line.
* `p [expression]`: Evaluate `[expression]` and print it.
* `pp [expression]`: Evaluate `[expression]` and pretty-print it.
* `q(uit)`: Abort the program and quit the debugger.

The parentheses indicate optional parts of the commands. For example, you can use the `where` command either by typing `w` or by typing `where`. These are just a few of the most useful commands. See the [pdb documentation](https://docs.python.org/3/library/pdb.html#debugger-commands) for more information.

**Be careful when executing Python code directly in the debugging shell. If your commands look like a PDB command, the PDB command may be executed instead.**

For example, this works just as you'd expect:

```python
(Pdb) z = 1
(Pdb) z
1
```

However, this fails:

```python
(Pdb) p = 1
*** SyntaxError: invalid syntax
```

This second case fails because `p` looks to PDB like the print command, not a variable.
