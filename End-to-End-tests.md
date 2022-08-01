## Table of contents

* [Introduction](#introduction)
* [Flaky tests](#flaky-tests)
  * [What is a flake](#what-is-a-flake)
  * [Why flakes are problematic](#why-flakes-are-problematic)
  * [Preventing flakes](#preventing-flakes)
  * [If the end-to-end tests are failing on your PR](#if-the-end-to-end-tests-are-failing-on-your-pr)
* [Run E2E tests](#run-e2e-tests)
  * [Set chromedriver version](#set-chromedriver-version)
  * [Configure test sharding](#configure-test-sharding)
  * [Run a single end-to-end test](#run-a-single-end-to-end-test)
  * [Run end-to-end tests in production mode](#run-end-to-end-tests-in-production-mode)
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

## Run E2E tests

If you don't know the name of the suite you want to run, you can find it in `core/tests/wdio.conf.js` or `core/tests/protractor.conf.js`. Then you can run your test like this:

```console
python -m scripts.run_e2e_tests --suite="suiteName"
```

Chrome will open and start running your tests.

### Set chromedriver version

The end-to-end tests are run on the Chrome browser and depend on chromedriver. The chromedriver version to be used depends on the Chrome browser version installed on the machine. We try to determine this version automatically, but if our automatic determination fails, you'll see an error with this advice:

```text
Please set the chromedriver version manually using the --chrome_driver_version flag.
```

You may also want to set the chromedriver version manually if you want to test a particular version.

To manually set the chromedriver version, use the `--chrome_driver_version` argument:

```console
python -m scripts.run_e2e_tests --chrome_driver_version <version>
```

To determine which version of chromedriver to use, please follow these steps:

1. Find the Chrome browser version installed on your machine by going to `chrome://version/`. For example, in the screenshot below, the version number is `83.0.4103.61`.

   ![Screenshot of Chrome version page.](https://user-images.githubusercontent.com/11008603/87473539-3c972880-c63f-11ea-9455-04edb0196731.png)

2. Remove the last part of the version number from step 1 and append the result to URL `https://chromedriver.storage.googleapis.com/LATEST_RELEASE_`. For example, if your version number is `83.0.4103.61`, the URL will look like "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_83.0.4103".

3. Go to the URL from step 2 and copy the version number on the screen.

4. The version number obtained in step 3 is the chromedriver version to be passed along to the script.

If you see a failure due to the webdriver, please follow the instructions above to double check that the chromedriver version provided is in sync with the Chrome browser version installed on the machine.

### Configure test sharding

If you run all the E2E tests at once (i.e. if you don't specify a suite), the tests will be sharded across multiple Chrome browser instances. By default, the tests will use 3 shards (i.e. 3 browsers). If you do this, you should close background processes to maximize the compute resources available to the tests. You can configure the number of shards like this:

```console
python -m scripts.run_e2e_tests --sharding-instances=<number of shards>
```

You can disable sharding like this:

```console
python -m scripts.run_e2e_tests --sharding=false
```

Note that when we run tests on CI, we run one suite at a time, so there is no sharding.

### Run a single end-to-end test

To run just one test, change the "it" to "fit" for that test. Then when you run the tests, specify the suite containing your test.

### Run end-to-end tests in production mode

To run the end-to-end tests in production mode, use the `--prod_env` flag:

```console
python -m scripts.run_e2e_tests --prod_env
```

On CI, we run all the E2E tests in production mode to more closely mimic how the Oppia application behaves in production.

## Versions of end-to-end tests

Currently, we have two versions of E2E test suites present: Protractor and WebDriverIO. The following [webdriverio migration tracker](https://docs.google.com/spreadsheets/d/1Mj-llYXMURtis54vpL2VL7BwgRiFIZ1nIFtK3fY3Se4/edit?usp=sharing) contains the information about which suite is present in which version (see Suites migrated to WebdriverIO, Suites still in Protractor)

* [[E2E test Protractor|Protractor]]

* [[E2E test WebdriverIO|WebdriverIO]]
