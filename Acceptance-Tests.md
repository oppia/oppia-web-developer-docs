# Introduction

Acceptance tests are end-to-end tests that test the complete functionality of the application, and this will help users to catch bugs and regressions before they are released ensuring that the code does what it is supposed to do.

This guide will help you to get started on how to write `e2e acceptance test` for a particular user-type.


## Files and Directory Structure

```
oppia/core/tests/
 └── puppeteer-acceptance-tests
    ├── spec
    │  ├── blog-admin-tests (give user type name)
    │  │    ├── assign-role-to-users-and-change-tag-properties.spec.js
    │  ├── blog-editor-tests
    │  │    ├── create-draft-and-delete-draft-blog-post.spec.js
    │  │    └── publish-blog-post-and-delete-published-blog-post.spec.js
    |  |    └── check-blog-editor-unable-to-publish-duplicate-blog-post.spec.js
    ├── images
    │  └── blog-post-thumbnail.svg
    ├── puppeteer-testing-utilities
    │  ├── puppeteer-utils.js
    │  ├── show-message-utils.js
    │  ├── test-constants.js
    │  └── user-factory.js
    └── user-utilities
       └── blog-post-admin-utils.js
       └── super-admin-utils.js
```

The directory structure is as follows:
1) The `spec` directory contains all the top-level test files. Each test file is named as `*.spec.js` and contains the test for a particular user type. For example, `blog-admin-tests` directory contains all the tests for the `Blog Admin` user.

2) The `puppeteer-testing-utilities` directory contains all the utility files and helper functions, which you would require to write new acceptance tests. This directory can also be used to append more utility functions as when required or needed by the user.
Files included inside this directory are :
  - `puppeteer-utils.js` -> This file contains the base _*puppeteerUtilities*_ class which provides the most common and useful methods such as _*openBrowser*_, _*goto*_ etc. This class also serves the purpose of providing a base for defining other user oriented subclasses for eg. _*e2eBlogPostAdmin*_ class of _*blog-post-admin-utils.js*_ .
  - `user-factory.js` -> This file contains methods for creating a certain user. The file has different methods for creating different types of user.
  - `test-constants.js` -> This file contains defined constants such as _*URLs, classname, id etc. which are used in the tests.
  - `show-message-utils.js` -> This file contains method for logging the progress and errors during a test.

3) The `user-utilities` directory holds the utility files for different user types. Each user utility class is build upon the base `puppeteerUtilities` class containing the original methods along with the ones related to that user type. For eg. `e2eBlogPostAdmin` contains base functions as well as additional functions just related to `Blog Admin` user.

4) The `images` directory contains all the images used in the tests.


## How to run the acceptance tests
From the root directory of oppia, run the following command:
```  
python -m scripts.run_acceptance_tests --suite={{suiteName}}  
``` 

Docker:
```
make run_tests.acceptance suite=SUITE_NAME
```

For example, to run the `check-blog-editor-unable-to-publish-duplicate-blog-post.spec.js` test, run the following command:
Python:
```
python -m scripts.run_acceptance_tests --suite="blog-editor-tests/check-blog-editor-unable-to-publish-duplicate-blog-post.spec.js"
```

Docker:
```
make run_tests.acceptance suite="blog-editor-tests/check-blog-editor-unable-to-publish-duplicate-blog-post.spec.js"
```


## How to write new tests for a specific user

1) Create a new directory for the specific user if it doesn't already exists inside the `spec` directory. For ex. `Topic Manager` user can have directory named as `topic-manager-tests`, and within the user directory, each test file is named as `*.spec.js`. 
> Note: Naming convention for directories / files is kebab case, where each word is separated by a (-)

2) Within the user directory, create a new file for each test. For ex. `create-new-topic.spec.js` and `delete-topic.spec.js` for `Topic Manager` user. And these top-level test contains single user stories checking their test steps and expectations mentioned in the [testing spreadsheet](https://docs.google.com/spreadsheets/d/1O8EHiSAGrG0yoNUBz9E4DIwKNS8Rfsv_ffC4k1WK5jc/edit?usp=sharing).

3) The functionality of the top-level tests for each user-type is defined in the `user-utilities` directory. For ex. the blog editor tests are written within the `spec/blog-editor-tests` directory, and the functionality of the tests are defined in the `user-utilities/blog-post-editor-utils.js` file.
> Note: A utility file is maintained for each user type. The purpose of maintaining this file is to add methods specific to that user on top of the already provided basic methods. This file maintains a user class which is extended from the base class of puppeteer-utils.js . For ex. blog-post-admin-utils.js have a class e2eBlogPostAdmin which have methods like `createDraftBlogPostWithTitle`, `deleteDraftBlogPostWithTitle` etc. specific to Blog Admin only.


4) The utility files are imported in the top-level test files and the methods are called to perform the required actions. For ex. in the `create-draft-and-delete-draft-blog-post.spec.js` file, the `createDraftBlogPostWithTitle` method is called to create a draft blog post with a given title. The `deleteDraftBlogPostWithTitle` method is called to delete the draft blog post with the given title.

5) For each test, the user is created using the `userFactory` class. For ex. in the `create-draft-and-delete-draft-blog-post.spec.js` file, the `createNewBlogPostEditor` method is called to create a new blog post editor user. The `createNewBlogPostEditor` method is defined in the `user-factory.js` file. The `createNewBlogPostEditor` method creates a new user with the given username and returns the user object. The user object is used to perform the required actions (that are defined in the `user-utilities/*-utils.js`).

6) After successful completition of any test step or any expectation, the `showMessage` method is called to log the progress. For ex. in the `create-draft-and-delete-draft-blog-post.spec.js` file, the `showMessage` method is called to log the progress after the draft blog post is created. The `showMessage` method is defined in the `show-message-utils.js` file.

7) If there is any error during the test, then we throw errors in the expectation step or there would be timeout error if some component does not behave as intended.

8) The `puppeteer-testing-utilities` directory contains all the utility files and helper functions, which you would require to write new acceptance tests. This directory can also be used to append more utility functions as when required or needed by the user.

9) The test must be thoroughly tested before submitting a PR. The test can be run locally by running the following command as mentioned above or you can run the test on the CI server by pushing your code to the remote branch in your fork. The CI server will run the test and will show the result.

## Reference Links
Blog Admin and Blog Editor Tests - 
  [Blog Admin top-level tests](https://github.com/oppia/oppia/tree/develop/core/tests/puppeteer-acceptance-tests/spec/blog-admin-tests)
  [Blog Editor top-level tests](https://github.com/oppia/oppia/tree/develop/core/tests/puppeteer-acceptance-tests/spec/blog-editor-tests)
  [user utility files](https://github.com/oppia/oppia/blob/develop/core/tests/puppeteer-acceptance-tests/user-utilities/blog-post-admin-utils.js)
  [puppeteer utility files - base class](https://github.com/oppia/oppia/blob/develop/core/tests/puppeteer-acceptance-tests/puppeteer-testing-utilities/puppeteer-utils.js)
  [puppeteer utility files - user factory](https://github.com/oppia/oppia/blob/develop/core/tests/puppeteer-acceptance-tests/puppeteer-testing-utilities/user-factory.js)
