Oppia has tests! These tests help ensure that the code is in a working state. (We always appreciate help with writing more tests, especially for the frontend, so [please let us know](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia) if you can help.)

Before checking in any commits to the Oppia repository, please ensure that every single test passes by following the steps below. Also, please start up a development server and click around a bit, especially in places affected by your commit, to ensure that everything is working as expected. Otherwise, people who build on top of your commit will not be able to tell if the tests or the server are failing due to their changes, or due to existing bugs in the Oppia code -- and this will be rather frustrating for them.

## Server-side tests ##

See [[the backend tests wiki page|Backend-tests]].

## Client-side tests ##

Client-side JavaScript tests need to be run separately from the backend tests, by executing the following command in a terminal:
```
    python -m scripts.run_frontend_tests
```

This will open a [Karma](http://karma-runner.github.io/0.10/index.html) server that runs in the background, together with a browser window (which you can ignore). The results of the tests will be displayed in the terminal.

(If you want the tests to run continuously, go to `core/tests/karma.conf.js` and set `singleRun` to `false`. If you do this, the tests will automatically re-run when you save an HTML/JS file, which is very useful for iterative development. To exit the test runner when it is in this mode, type Ctrl-C in the terminal that is running the server.)

The tests each relate to specific front-end components; the test file for `foo.js` is located in the same directory and called `fooSpec.js`.

Karma has a handy shortcut for running a single test or a single test suite: all you need to do is to change 'it' to 'fit' or 'describe' to 'fdescribe' for that test or test suite, respectively.

We also have a coverage tool that displays what fraction of the front-end code is currently covered by unit tests. After running the tests you can view the results at
```
   ../karma_coverage_reports/[your chrome version]/index.html
```
and clicking through will show exactly which parts of the code are still in need of tests.

Unfortunately the failure messages from the frontend tests are somewhat unhelpful. The line numbers in the stack trace correspond to a file that results from combining all the spec files together, so they are correct in relative but not absolute terms. Until we figure out how to fix this, you can use `console.log(...)` statements to isolate problems.

## End-to-end tests ##

Oppia has an end-to-end testing framework (Protractor) that incorporates both the client and server. It is run using the following command:
```
    python -m scripts.run_e2e_tests
```
This will load a test version of the server (on ports 4444 and 4445), open a Google Chrome browser and automatically run through a series of simulated user actions. If any of the tests fail the simulation will attempt to move on to the next test, and then report the problem at the end. However a single failure may leave the browser in a state (e.g. with an open alert message) that causes a cascade of failures in the other tests, so generally the first failure reported is the significant one.

**Setting chromedriver version**

The end-to-end tests are run on Chrome browser. The chromedriver version to be used depends on the Chrome browser version installed on the machine. To manually set the chromedriver version, please use the following command:

```
    python -m scripts.run_e2e_tests --chrome_driver_version <version>
```

If you see a failure due to the webdriver, please double check that the chromedriver version provided is in sync with the Chrome browser version installed on the machine. To determine which version of chromedriver to use, please follow these steps:

1. Find the Chrome browser version installed on your machine by going to `chrome://version/`. eg. In the screenshot below, the version number is `83.0.4103.61`.

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/11008603/87473539-3c972880-c63f-11ea-9455-04edb0196731.png"/>
</p>

2. Remove the last part of the version number from step 1 and append the result to URL `https://chromedriver.storage.googleapis.com/LATEST_RELEASE_`. eg. If your version number is `83.0.4103.61`, the URL will look like "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_83.0.4103".
3. Go to the URL from step 2 and copy the version number on the screen.
4. The version number obtained in step 3 is the chromedriver version to be passed along to the script.

Note: If this flag is not used, the chromedriver version is determined automatically.

**Sharding tests**

The end-to-end tests are also sharded across 3 Chrome browser instances. It is recommended to close background processes to maximize the test performance. You can disable sharding as follows:

```
    python -m scripts.run_e2e_tests --sharding=false
```

You can configure the number of browser instances to use for sharding as follows:
```
    python -m scripts.run_e2e_tests --sharding-instances=#
```

**Running a single end-to-end test**

To run just one test, change the "it" to "fit" for that test, and change the suite config in `core/tests/protractor.conf.js` to refer to only the file containing that test.


**Running end-to-end tests in production mode**

To run the end-to-end tests using minified versions of the files, use the `--prod_env` flag:
```
    python -m scripts.run_e2e_tests --prod_env
```
Note that, on [Travis CI](https://travis-ci.com/github/oppia/oppia/pull_requests), the end-to-end tests run only in this mode (to save time).

**Other notes**

Protractor has a screenshot reporting feature, but it needs to be enabled by setting `_ADD_SCREENSHOT_REPORT` to true in
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
together with various `protractor.js` files throughout the `extensions` directory. You can replace `it` with `fit` or `describe` with `fdescribe` to run a single test or test suite. For more information about modifying and writing such tests, see [[Writing End-to-End Tests|End-to-End-Tests]].

Please report any unexpected or inexplicable failures of the tests, together with the error log produced, as there have been some stability issues that we are trying to iron out.

#### Debugging

If you find that the e2e tests are failing, first check the error message. If it looks something like "Cannot determine loading status", "Cannot read property 'nodeType' of undefined", or "A Jasmine spec timed out", this is probably a transient issue, and the best thing to do (if the failure is on Travis) is to ask a maintainer to restart the relevant test.

Otherwise, run the affected test on your local machine, and watch it running, so that you can see where things are going wrong. Note that you can pass in a 'suite' parameter to run a subset of the tests -- see scripts/run_e2e_tests.sh for details. Another alternative is to go to core/tests/protractor.js and modify the *.js to just the specific file you want to test.

- **Important:** When running the tests locally, make sure to use exactly the same commands as TravisCI/CircleCI. You'll want your local environment to match those environments as closely as possible, and those commands include additional arguments that could cause unwanted differences. You can find the TravisCI/CircleCI config files in `.travis.yml` (in the Oppia root directory) and in `.circleci/config.yml` -- look through them to find the "script" section or the "command" sections respectively, which contain the commands that you can run on your local machine.

Finally, if this isn't helping (e.g. the issue is with console errors or something that's not obviously apparent), look up the test file in `core/tests/protractor` and follow its actions manually on a fresh dev server (they should be pretty easy to understand). Keep the browser console open so that you can spot any warnings. This should help you find problems, and fix them.

Also, note that the test logs can sometimes be quite long. In general, it is better to focus on the earliest error for each suite (i.e. the one that appears top-most in the log) since that error will usually cause other follow-up errors. If you fix that error, then the later ones may end up getting fixed automatically as well!


**Troubleshooting**

If you get an error similar to this:
```
 selenium standalone is up to date.
 chromedriver is up to date.
 nc: connect to localhost port 8181 (tcp) failed: Connection refused
 nc: connect to localhost port 4444 (tcp) failed: Connection refused
 seleniumProcess.pid: undefined
 nc: connect to localhost port 4444 (tcp) failed: Connection refused
 nc: connect to localhost port 4444 (tcp) failed: Connection refused
 nc: connect to localhost port 4444 (tcp) failed: Connection refused
 nc: connect to localhost port 4444 (tcp) failed: Connection refused
```
while running e2e tests, download and install [Java SE Development Kit 7u79](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html).
If the problem still persists, try installing/updating Java Runtime Environment. This should resolve the issue -- see discussion in [#1824](https://github.com/oppia/oppia/issues/1824#issuecomment-219192563)

## Typescript tests ##

You can run typescript tests using
```
    python -m scripts.typescript_checks
```

These tests compile all ts files in the codebase and checks for errors during compilation.

The compiled files are generated in a folder `local_compiled_js_for_test` which is automatically deleted after the tests.

**How do you know whether the tests have passed?**

The tests pass if, at the end of the test output, you see the message:
```
    Compilation successful!
```

However, if you get a message:

```
    Errors found during compilation
```

then this means that the test has failed, and the error messages will be displayed below this line.
