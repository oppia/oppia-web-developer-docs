## Overview

Oppia currently uses **Protractor** for end-to-end testing, but as the Angular team plans to end the development of Protractor at the end of 2022, we are planning to migrate all these tests to **WebdriverIO**.

As long as the migration is going on, the tests will be present in the **Hybrid State**, i.e. the tests will be present in both webdriverIO and protractor.

There are a few important points about the hybrid state:

* We will have two tools to run the E2E tests: protractor and webdriverIO

* Each test suite will be either present in webdriverIO or protractor, never in both.

* When a utility file is needed by both a protractor test and a webdriverIO test, we will have two copies of the file: one in webdriverIO and one in protractor.

* No file will contain the code of both webdriverIO and protractor.

* Protractor suite can only work on protractor utils and vice versa for webdriverIO.

## E2E Migration tracker

The [webdriverIO migration tracker](https://docs.google.com/spreadsheets/d/1Mj-llYXMURtis54vpL2VL7BwgRiFIZ1nIFtK3fY3Se4/edit?usp=sharing) contains the following details:

* Suites migrated to webdriverIO.

* Suites still in protractor.

* Expected date of migration of protractor suites.

* Dependencies migrated to webdriverIO.

* Dependencies still in protractor.

* List of common dependencies which are present in both protractor and webdriverIO.

Contributors can use this to get the idea about when a test suite is going to be migrated and hence plan their PR accordingly in order to avoid clashes which have been discussed in Add/Modify E2E tests section (See the edge case in point 2 for more information in next section).

## Add or Modify E2E tests

1. **If contributor wants to add a new suite:**

  * Add the new e2e test suite in webdriverIO.

    **Note**: As the first new suite will be added in late August, we will have most of the files already migrated to WebdriverIO like action.js, forms.js, user.js, general.js waitFor.js which are mostly needed for writing a new test.

2. **If contributor wants to modify a suite** 

  * If the suite is migrated to webdriverIO then make the changes in webdriverIO.
  
  * If the suite is still in protractor then make the changes in protractor.

    **Edge Case**: If we already have a migration PR open for a particular suite and at the same time any other contributor also made a PR adding the tests in the same suite then, if migration's PR will be merged first, the contributor needs to write the tests in webdriverIO (contributor can take help from [Shivam Jha](#contact)).  Otherwise, migration PR needs to be updated with the changes.

    Also, if migration PR will get merged first then everyone will be notified about it accordingly as migration PR will have the **PR: that requires post-merge sync to the HEAD label.**

3. **If contributor is planning to make some changes in the common files**

   The tests might break if the changes are only applied in one version of the common file. So we need to make sure to keep the two versions of the common file in sync. We will not merge the PR of the contributor if it's not synced. Contributor can take help from [Shivam Jha](#contact) or the migration guide in order to make the necessary changes for the other version.
  
#### Current approach to migrate the dependencies

To reduce the duplicate code in the codebase we are going to migrate only those portions of the dependencies which are used in the suite that we are migrating. The remaining portions will be migrated when a suite which depends upon them is being migrated.

Let's understand this situation with a simple test case.

We have two test files:

|**File**            | **Dependencies**         |
|--------------------|--------------------------|
|AdditonalPlayer     |ExplorationEditorPage, ExplorationPlayerPage, LibraryPage|
|AdditonalEditorFeaturesModals| ExplorationEditorPage |

**Common Files** : ExplorationEditorPage

* While migrating **AdditionalPlayer** we will migrate its dependencies, there will be no issue with **ExplorationPlayerPage**, **LibraryPage** as they do not have any other suites dependent on them, we will just migrate them and delete their protractor version. But for **ExplorationEditorPage** we still have one dependent suite i.e. **AdditonalEditorFeatures**, so we need to migrate it to successfully migrate **AdditionalPlayer** suite, but we cannot delete the protractor version (as a protractor suite cannot work on webdriverIO util files).

* So now the **ExplorationEditorPage** file will be a common file that presents in both webdriverIO and protractor version. To reduce code duplicity to some extent I will migrate only that portion of ExplorationEditorPage that will be used in the **AdditonalPlayer** suite, rest can be migrated when we will migrate **AdditonalEditorFeaturesModals**.

## Contact

For any queries related to E2E migration, please don't hesitate to reach out to **Shivam Jha (@ShivamJhaa)**.

Email: 20bcs206@iiitdmj.ac.in
