## Overview

Oppia currently uses **Protractor** for end-to-end testing but as the Angular team plans to end the development of Protractor at the end of 2022, we are plannning to migrate all these tests to **WebdriverIO**.
Till the time the migration will be complete the tests will be present in **Hybrid State**, i.e the tests will be present in both webdriverIO and protractor.

There are a few important points about the hybrid state:

* We will have two tools to run the E2E tests i.e protractor and webdriverIO

* Each test suite will be either present in webdriverIO or protractor.

* Same utils files can be present in both webdriverIO and protractor.

* No file will contain the code of both webdriverIO and protractor.

* Protractor suite can only work on protractor utils and vice versa for webdriverIO.

## E2E Migration tracker

The [webdriverio migration tracker](https://docs.google.com/spreadsheets/d/1Mj-llYXMURtis54vpL2VL7BwgRiFIZ1nIFtK3fY3Se4/edit?usp=sharing) holds the record of suites migrated to webdriverIO, suites still in protractor and when I am going to migrate them, dependencies migrated to webdriverIO, dependencies still in protractor, and common dependencies which are present in both protractor and webdriverIO.
Contributors can use this to get the idea about when a test suite is going to be migrated and hence plan their PR accordingly in order to avoid clashes such as if Shivam Jha opened a PR to migrate a particular suite and the contributor also opens a PR making changes in the same suite at the same time.

## Add/Modify E2E tests

1. **If contributor want to add a new suite:**

* Add the new e2e test suite in webdriverio.
**Note**: As the first new suite will be added in late August, we will have most of the files already migrated to WebdriverIO like action.js, forms.js, user.js, general.js waitFor.js which are mostly needed for writing a new test.

2. **If contributor want to modify a suite** 

* If the suite is migrated to webdriverIO then add the tests in webdriverIO.

* If the suite is still in protractor then add the tests in protractor.

**Edge Case**: If Shivam Jha already have a migration PR open for a particular suite and at the same time any other contributor also made a PR adding the tests in the same suite, in this case, if Shivam Jha's PR will be merged first then the contributor needs to write the tests in webdriverIO (contributor can take help from Shivam Jha) otherwise Shivam Jha need to update his PR with the changes.

3. **If contributor is planning to make some changes in the common files**

The tests might break if the changes are only applied in one version of the common file. So we need to make sure to keep the two versions of the common file in sync. We will not merge the PR of the contributor if it's not synced. Contributor can take help from Shivam Jha or the migration guide in order to make the necessary changes for the other version.

####Current Approach to migrate the dependencies

To reduce the duplicate code in the codebase we are going to migrate only those portions of the dependencies which are used in the suite that we are migrating. The remaining portions will be migrated when other suite which depends upon the same dependencies will be migrated.
Let's understand this situation with a simple test case. We have two test files **AdditonalPlayer** (having dependencies **ExplorationEditorPage**, **ExplorationPlayerPage**, **LibraryPage**), and **AdditonalEditorFeaturesModals** (having dependencies **ExplorationEditorPage**). We can see that the **ExplorationEditorPage** is common in both the test suites. So now we need to migrate the AdditionalPlayer then we will also have to migrate its dependencies, there will be no issue with **ExplorationPlayerPage**, **LibraryPage** as they do not have any suites dependent on them, we will just migrate them and delete their protractor version. But for **ExplorationEditorPage** we still have one dependent suite i.e **AdditonalEditorFeatures** so we will migrate it to successfully migrate out the **AdditionalPlayer** suite but we will not delete the protractor version of it (as a protractor suite cannot work on webdriveriO util files). So now the **ExplorationEditorPage** file will be a common file that presents in both webdriverIO as well as protractor version. To reduce code duplicacy to some extent I will migrate only that portion of ExplorationEditorPage that will be used in the **AdditonalPlayer** suite, rest can be migrated when we will migrate **AdditonalEditorFeaturesModals**.


## Contact

For any queries related to E2E migration, please don't hesitate to reach out to **Shivam Jha (@ShivamJhaa)**.
Email: 20bcs206@iiitdmj.ac.in