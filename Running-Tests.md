Oppia has tests! These tests help ensure that the code is in a working state. (We always appreciate help with writing more tests, especially for the frontend, so [please let us know](https://github.com/oppia/oppia/blob/develop/CONTRIBUTING.md) if you can help.)

Before checking in any commits to the Oppia repository, please ensure that every single test passes by following the steps below. Also, please start up a development server and click around a bit, especially in places affected by your commit, to ensure that everything is working as expected. Otherwise, people who build on top of your commit will not be able to tell if the tests or the server are failing due to their changes, or due to existing bugs in the Oppia code -- and this will be rather frustrating for them.

## Server-side tests ##

You can run server-side tests using
```
    bash scripts/run_backend_tests.sh
```

Alternatively, to run just a single test module, you can type, e.g.:
```
    bash scripts/run_backend_tests.sh --test_target=core.controllers.editor_test
```

For more information about `--test_target` and other flags, please see the documentation at the top of the [run_backend_tests.sh](https://github.com/oppia/oppia/tree/master/scripts/run_backend_tests.sh) script.

The variable `EXPECTED_TEST_COUNT` in `scripts/backend_tests.py` stores the total number of Python tests. After adding tests, you'll need to update this variable to reflect the new test count.

(Note: While the tests are running, you may see the word `ERROR` show up in the test logs. This does not necessarily mean that an error has occurred; it happens because some tests explicitly expect an error to be raised under particular circumstances.)

**How do you know whether the tests have passed?**

The tests pass if, at the end of the test output, you see the message:
```
    All tests pass.
```
and every line representing a test class starts with `SUCCESS`.

However, if you get something like this instead:

```
    Ran 326 tests in 47 test classes.
    (1 ERRORS, 0 FAILURES)
```

then this means that a test has failed, and the change cannot be checked in as-is -- you'll need to resolve the test failures first. You can find more information about the exact errors by scrolling up and looking through the error log. Pay particular attention to the parts marked `FAILED` and `ERROR`.

## Client-side tests ##

Client-side JavaScript tests need to be run separately from the backend tests, by executing the following command in a terminal:
```
    bash scripts/run_frontend_tests.sh
```

This will open a [Karma](http://karma-runner.github.io/0.10/index.html) server that runs in the background, together with a browser window (which you can ignore). The results of the tests will be displayed in the terminal, and are automatically updated when you save an HTML/JS file, which is very useful for iterative development. Note that the script will not terminate when a test run are completed. Instead, to exit the test runner, type Ctrl-C in the terminal that is running the server.

The tests each relate to specific front-end components; the test file for `foo.js` is located in the same directory and called `fooSpec.js`.

Karma has a handy shortcut for running a single test or a single test suite: all you need to do is to change 'it' to 'iit' or 'describe' to 'ddescribe' for that test or test suite, respectively.

We also have a coverage tool that displays what fraction of the front-end code is currently covered by unit tests. After running the tests you can view the results at
```
   ../karma_coverage_reports/[your chrome version]/index.html
```
and clicking through will show exactly which parts of the code are still in need of tests.

## End-to-end tests ##

Oppia has an end-to-end testing framework (Protractor) that incorporates both the client and server. It is run using the following command:
```
    bash scripts/run_e2e_tests.sh
```
This will load a test version of the server (on ports 4444 and 4445), open a Google Chrome browser and automatically run through a series of simulated user actions. If any of the tests fail the simulation will attempt to move on to the next test, and then report the problem at the end. However a single failure may leave the browser in a state (e.g. with an open alert message) that causes a cascade of failures in the other tests, so generally the first failure reported is the significant one.

** Sharding tests **

The end-to-end tests are also sharded across 3 Chrome browser instances. It is recommended to close background processes to maximize the test performance. You can disable sharding as follows:

```
    bash scripts/run_e2e_tests.sh --sharding=false
```
You can configure the number of browser instances to use for sharding as follows:
```
    bash scripts/run_e2e_tests.sh --sharding-instances=#
```
** Running a single end-to-end test **

To run just one test, change the "it" to "fit" for that test, and change the suite config in `core/tests/protractor.conf.js` to refer to only the file containing that test.

** Other notes **

Protractor has a screenshot reporting feature, but it needs to be enabled by seeing `_ADD_SCREENSHOT_REPORT` to true in
```
    core/tests/protractor.conf.js
```
Once enabled, you can view screenshots of the point at which each test failed by navigating to
```
    ../protractor-screenshots/
```
**Note**: this reporting feature is disabled by default because it sometimes obscures the actual protractor error logs and does not close the browser after a failed run.

The tests are located in
```
    core/tests/protractor/
```
and are based on utilities located in
```
   core/tests/protractor_utils/
```
together with various `protractor.js` files throughout the `extensions` directory. You can replace `it` with `fit` or `describe` with `fdescribe` to run a single test or test suite. For more information about modifying and writing such tests, see [[Writing End-to-End Tests|Writing-End-to-End-Tests]].

Please report any unexpected or inexplicable failures of the tests, together with the error log produced, as there have been some stability issues that we are trying to iron out.
