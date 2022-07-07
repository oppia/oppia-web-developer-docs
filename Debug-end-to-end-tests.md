## Table of contents

* [Introduction](#introduction)
* [How to debug the two versions of the end to end tests](#how-to-debug-the-two-versions-of-the-end-to-end-tests)

## Introduction

Whenever you are debugging tests, you should create a debugging doc to document your work. This helps future contributors if they run into a similar bug in the future. If other people come in later to help you, they can also use the debugging doc to get up to speed on what you've already figured out. You can make a copy of [this template debugging doc](https://docs.google.com/document/d/1qRbvKjJ0A7NPVK8g6XJNISMx_6BuepoCL7F2eIfrGqM/edit?usp=sharing) to get started. Also check out the [[debugging docs wiki page|debugging-docs]].

There are many ways to go about debugging an E2E test, but here is one approach:

1. Create a [[debugging doc|debugging-docs]].
2. Look through the logs from the failed test to try and understand what went wrong. In particular:

   * Look for a line that says just `Killed`. This line indicates that some process was killed by the operating system for consuming too much memory. It's fairly safe to assume that the test failure was because of that process being killed.
   * Look for the stack trace and error message of the _first_ error. The trace might point you to where the error was thrown in the test code, and the message may help explain what went wrong.

3. If you don't understand what the error message means, search for it online. Also look through the test code, `core/test/protractor_utils/action.js`, and `core/test/webdriverio_utils/action.js` to see if the error message (or something like it) is in our test code.

4. Enable video recordings and rerun the test until you reproduce the error. Then watch the video recordings and follow along in the test code. Try and understand why the error was thrown.

5. Try and reproduce the error locally. If you succeed, you can use your local debugger to investigate.

## How to debug the two versions of the end to end tests

Currently, we have two versions of E2E test suites present, Protractor and WebDriverIO, so it's important to first find out which framework the failing test suite is written in. The [webdriverio migration tracker](https://docs.google.com/spreadsheets/d/1Mj-llYXMURtis54vpL2VL7BwgRiFIZ1nIFtK3fY3Se4/edit?usp=sharing) contains the information about which suite is present in which framework (see "Suites migrated to WebdriverIO" and "Suites still in Protractor").

* [Debug E2E test protractor](Debug-end-to-end-tests-protractor.md#table-of-contents)

* [Debug E2E test webdriverio](Debug-end-to-end-tests-webdriverio.md#table-of-contents)
