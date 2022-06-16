## Table of contents

* [Introduction](#introduction)
* [Flaky tests](#flaky-tests)
  * [What is a flake](#what-is-a-flake)
  * [Why flakes are problematic](#why-flakes-are-problematic)
  * [Preventing flakes](#preventing-flakes)
  * [If the end-to-end tests are failing on your PR](#if-the-end-to-end-tests-are-failing-on-your-pr)
* [Versions of end-to-end tests](#versions-of-end-to-end-tests)

## Introduction

At Oppia, we highly regard the end user, so we have end-to-end (E2E) tests to test our features from the user's perspective. These tests interact with pages just like a user would, for example by clicking buttons and typing into text boxes, and they check that pages respond appropriately from the user's perspective, for example by checking that the correct text appears in response to the user's actions.

## Flaky tests

### What is a flake

Unfortunately, E2E tests are much less deterministic than our other tests. The tests operate on a web browser that accesses a local Oppia server, so the non-determinism of web browsers makes the tests less deterministic as well. For example, suppose that you write a test that clicks a button to open a modal and then clicks a button inside the modal to close it. Sometimes, the modal will open before the test tries to click the close button, so the test will pass. Other times, the test will try to click before the modal has opened, and the test will fail. We can see this schematically:

```text
               <---A--->

                        +-------+
                        | Modal |
+----------+   +---//---+ opens +-----------+
| Click to |   |        +-------+           |
| open     +---+                            +---->
| modal    |   |        +-------------+     |
+----------+   +---//---+ Click to    +-----+
                        | close modal |
                        +-------------+

               <---B--->


--------------------- time ---------------------->
```

The durations of steps `A` and `B` are non-deterministic because `A` depends on how quickly the browser executes the frontend code to open the modal, and `B` depends on how fast the test code runs. Since these operations are happening on separate processes, the operating system makes no guarantees about which will complete first. In other words, we have a race condition.

This race condition means that the test can fail randomly even when there's nothing wrong with the code of the Oppia application (excluding tests). These failures are called _flakes_.

### Why flakes are problematic

Flakes are annoying because they cause failures on PRs even when the code changes in those PRs are fine. This forces developers to rerun the failing tests, which slows development.

Further, flakes are especially problematic to certain groups of developers:

* **New contributors**, who are often brand-new to open source software development, can be discouraged by flakes. When they see a failing E2E test on their PR, they may think that they made a mistake and become frustrated when they can't find anything wrong with their code.

* **Developers without write access to the repository** cannot rerun tests, so they have to ask another developer to restart their tests for them. Waiting for someone to restart their tests can really slow down their work.

Finally, flakes mean that developers rerun failing tests more readily. We even introduced code to automatically rerun tests under certain conditions. These reruns make it easier for new flakes to slip through because if a new flake causes a test to fail, we might just rerun the test until it passes.

### Preventing flakes

Conceptually, preventing flakes is easy. We can use `waitFor` statements to make the tests deterministic despite testing a non-deterministic system. For example, suppose we have a function `waitForModal()` that waits for a modal to appear. Then we could write our test like this:

```text
               <---A--->

                        +-------+
                        | Modal |
+----------+   +---//---+ opens +---------------------------------+
| Click to |   |        +-------+                                 |
| open     +---+                                                  +---->
| modal    |   |        +----------------+    +-------------+     |
+----------+   +---//---+ waitForModal() +-//-+ Click to    +-----+
                        +----------------+    | close modal |
                                              +-------------+

               <---B---><-------C-------->


--------------------- time -------------------------------------------->
```

Now, we know that the test code won't move past `waitForModal()` until after the modal opens. In other words, we know that `B + C > A`. This assures us that the test won't try to close the modal until after the modal has opened.

The challenge in writing robust E2E tests is making sure to always include a waitFor statement like `waitForModal()`. It's common for people to write E2E tests and forget to include a waitFor somewhere, but when they run the tests, they pass. Their tests might even pass consistently if their race condition only causes the test to fail very rarely. However, months later, an apparently unrelated change might change the runtimes enough that one of the test starts flaking frequently.

### If the end-to-end tests are failing on your PR

First, check that your changes couldn't be responsible. For example, if your PR updates the README, then there's no way it caused an E2E test to fail.

If your changes could be responsible for the failure, you'll need to investigate more. Try running the test locally on your computer. If it fails there too, you can debug locally. Even if you can only reproduce the flake on CI, there are lots of other ways you can debug. See our [[guide to debugging E2E tests|Debug-end-to-end-tests]].

If you are _absolutely certain_ that the failure was not caused by your changes, then you can restart the test. Remember that restarting tests can let new flakes into our code, so please be careful.

## Versions of end-to-end tests

Currently, we have two versions of E2E test suites present: Protractor and WebDriverIO. The following [webdriverio migration tracker](https://docs.google.com/spreadsheets/d/1Mj-llYXMURtis54vpL2VL7BwgRiFIZ1nIFtK3fY3Se4/edit?usp=sharing) contains the information about which suite is present in which version (see Suites migrated to WebdriverIO, Suites still in Protractor)

* [E2E test Protractor](Protractor.md#table-of-contents)

* [E2E test WebdriverIO](WebdriverIO.md#table-of-contents)
