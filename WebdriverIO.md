## Table of contents

* [Layout of the E2E test files](#layout-of-the-e2e-test-files)
  * [Suite files](#suite-files)
    * [`core/tests/webdriverio`](#coretestswebdriverio)
    * [`core/tests/webdriverio_desktop`](#coretestswebdriverio_desktop)
    * [`core/tests/webdriverio_mobile`](#coretestswebdriverio_mobile)
  * [Utilities](#utilities)
    * [`core/tests/webdriverio_utils`](#coretestswebdriverio_utils)
    * [`extensions/**/webdriverio.js`](#extensionswebdriverios)
* [Run E2E tests](#run-e2e-tests)
  * [Set chromedriver version](#set-chromedriver-version)
  * [Configure test sharding](#configure-test-sharding)
  * [Run a single end-to-end test](#run-a-single-end-to-end-test)
  * [Run end-to-end tests in production mode](#run-end-to-end-tests-in-production-mode)
* [Write E2E tests](#write-e2e-tests)
  * [Where to add the tests](#where-to-add-the-tests)
    * [Interactions](#interactions)
    * [Existing suite](#existing-suite)
    * [New suite](#new-suite)
  * [Writing the tests](#writing-the-tests)
  * [Writing utilities](#writing-utilities)
    * [Selecting elements](#selecting-elements)
    * [Non-Angular pages](#non-angular-pages)
  * [Writing robust tests](#writing-robust-tests)
    * [Flakiness](#flakiness)
    * [Independence](#independence)
  * [Checking for flakiness](#checking-for-flakiness)
  * [Codeowner Checks](#codeowner-checks)
  * [Important Tips](#important-tips)
* [Metrics](#metrics)
* [Reference](#reference)
  * [Forms and objects](#forms-and-objects)
    * [Rich Text](#rich-text)
  * [Async-Await Tips](#async-await-tips)
    * [Good Patterns](#good-patterns)
    * [Anti-Patterns](#anti-patterns)

## Layout of the E2E test files

E2E test logic is divided between two kinds of files: suite files and utility files. Utility files provide functions for interacting with pages, for example by clicking buttons or checking that the expected text is visible. Suite files define the E2E tests using calls to the utility files.

Suppose you wanted to write an E2E test that changes a user's profile picture and then checks that the change was successful. Your utility file might define `setProfilePicture()` and `checkProfilePicture` functions. Then your suite file would first call `setProfilePicture()` and then call `checkProfilePicture()`.

### Suite files

Note that "suite files" are also known as "test files."

#### `core/tests/webdriverio`

This directory contains test suites which were applicable to both desktop and mobile interfaces. However, we don't run the mobile tests anymore. Certain operations were possible only on one or the other interface. To distinguish between the interfaces, we use the boolean, `browser.isMobile` defined in `onPrepare` of the webdriverio configuration file. Even though we don't run the mobile tests anymore, you might see some legacy code that uses this boolean.

#### `core/tests/webdriverio_desktop`

This directory houses all test suites which are exclusive to desktop interfaces. This generally includes core creator components like the rich-text editor.

#### `core/tests/webdriverio_mobile`

This directory contains all test suites which are exclusive to mobile interfaces. This includes navigating around the website using the hamburger menu. However, we don't run these tests anymore.

### Utilities

#### `core/tests/webdriverio_utils`

This directory contains utilities for performing actions using elements from the core components of Oppia (those found in `core/templates`).

The core webdriverio utilities consist of the following files:

* Page objects, for example `AdminPage` in `AdminPage.js`. These objects provide functions for interacting with a particular page.
* `forms.js`: Utilities for interacting with forms.
* `general.js`: Various utilities that are useful for many different pages.
* `users.js`: Utilities for creating users, logging in, and logging out.
* `waitFor.js`: Utilities for delaying actions with WebdriverIO's wdio-wait-for library. This lets you wait for some condition to be true before proceeding with the test.
* `workflow.js`: Functions for common tasks like creating explorations and assigning roles.
* `action.js`: Functions for common interactions with elements, such as clicking or sending keys. All new tests should use these functions instead of interacting with elements directly because these functions include appropriate waitFor statements. For example, use `action.click('Element name', elem)` instead of `elem.click()`.

The webdriverio tests use the above functions to simulate a user interacting with Oppia. They should not interact with the page directly (e.g. using `element()`) but instead make use of the utilities in `webdriverio_utils/`. If new functionality is needed for a test then it should be added in the utilities directory, so that is available for future tests to use and easy to maintain.

#### `extensions/**/webdriverio.js`

Extensions provide `webdriverio.js` files to make them easier to test. The E2E test files call the utilities provided by these files to interact with an extension. For example, interactions include a `webdriverio.js` file that provides functions for customizing an interaction and checking that the created interaction matches expected criteria.

## Run E2E tests

If you don't know the name of the suite you want to run, you can find it in `core/tests/wdio.conf.js`. Then you can run your test like this:

```console
$ python -m scripts.run_e2e_tests --suite="suiteName"
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

## Write E2E tests

We expect E2E tests to be written for any new feature that is released to the public.

### Where to add the tests

#### Interactions

If you are just creating a new interaction and want to add end-to-end tests for it then you can follow the guidance given at [[Creating Interactions|Creating-Interactions]], though the [forms and objects](#forms-and-objects) section of this page may also be helpful.

If you are adding functionality to an existing interaction, you can probably just add test cases to its `protractor.js` file. For example, the `AlgebraicExpressionInput` interaction's file is at [`oppia/extensions/interactions/AlgebraicExpressionInput/webdriverio.js`](https://github.com/oppia/oppia/blob/develop/extensions/interactions/AlgebraicExpressionInput/webdriverio.js).

#### Existing suite

First, take a look at the existing test suites in [`core/tests/webdriverio`](https://github.com/oppia/oppia/tree/develop/core/tests/webdriverio) and [`core/tests/webdriverio_desktop`](https://github.com/oppia/oppia/tree/develop/core/tests/webdriverio_desktop). If your test fits well into any of those suites, you should add it there.

#### New suite

If you need to, you can add a new test suite to [`core/tests/webdriverio_desktop`](https://github.com/oppia/oppia/tree/develop/core/tests/webdriverio_desktop) like this:

1. Create the new suite file under `core/tests/webdriverio_desktop`.
2. Add the suite to [`core/tests/wdio.conf.js`](https://github.com/oppia/oppia/blob/develop/core/tests/wdio.conf.js).
3. Add your new suite to GitHub Actions, whose workflow files are in [`.github/workflows`](https://github.com/oppia/oppia/tree/develop/.github/workflows). If there is an existing workflow that your suite would fit well with, add your suite there. Otherwise, create a new workflow. Note that we want all CI workflows to finish in less than 30 minutes, so check the workflow runtimes after your change!

### Writing the tests

1. Think through what user journeys you want to test. Each user journey is a sequence of actions that a user could take. The end-to-end tests you write should execute those steps and make sure that Oppia behaves appropriately. Remember:

    * Test everything from the user's perspective. For example, instead of jumping to a page by the URL, navigate to the page using the links on the webpage like a user would.
    * Check the "happy paths" where the user does what you expect.
    * Check the "unhappy paths" where the user does something wrong. For example, if a text field only accepts 30 characters, your test should try entering 31 characters to make sure the appropriate error messages appear.
    * E2E tests are relatively "expensive," meaning that they take a while to run. Therefore, you should avoid testing something twice wherever possible. This usually means that fewer, larger tests are preferable to more, smaller tests. For example, consider these tests:

      * Test exploration creation by creating a new exploration.
      * Test exploration deletion by creating a new exploration and then deleting it.

      Notice that we create an exploration in both tests. It would be more efficient to combine these into a single test:

      * Test exploration creation and deletion by creating an exploration and then deleting it.

2. Write the [utilities](#writing-utilities) you will need. Your test file should never interact with the page directly. Use utilities instead. A good way to check that you're doing all page interactions through the utilities is to ensure that you have no element selectors (e.g. `$('.className')`) in your suite files.

3. Write the tests! Each test should step through one of your user journeys, asserting that the page is in the expected state along the way.

For information on writing tests with protractor, see the [webdriverio documentation](https://webdriver.io/docs/gettingstarted). If you need to work out why your tests aren't working, check out our [[debugging guide for E2E tests|Debug-end-to-end-tests-webdriverio]].

### Writing utilities

#### Selecting elements

Much of the difficulty of writing webdriverio code lies in specifying the element with which you wish to interact. It is important to do so in a way that is as insensitive as possible to superficial DOM features such as text and styling, so as to reduce the likelihood that the test will break when the production HTML is changed. Here are some ways to specify an element, in order of decreasing preference:

1. Adding a `webdriverio-test-some-name` class to the element in question, and then referencing it by `$('.webdriverio-test-some-name')`. We do not use `$('#id')` for this purpose because Oppia frequently displays multiple copies of a DOM element on the same page, and if an `id` is repeated then references to it will not work properly. This is the preferred method, since it makes clear to those editing production code exactly what the dependence on protractor is, thus minimizing the likelihood of confusing errors when they make changes. Sometimes this may not work, though (e.g. for embedded pages, third-party libraries and generated HTML), in which case you may instead need to use one of the options below.

2. Using existing element ids. We avoid using existing classes for this purpose as they are generally style specifications such as `big-button` that may be changed in the future.

3. You can use `$('<tag-name>')` if you are sure you are in a context where only one element will have (and is likely to have in future) the given name. The `<input>` and `<button>` tags often fall under this category. Try to avoid `$('button=btnText')` and `$('=linkText')` since they are sensitive to the choice of user-facing text.

4. Finally, you can use `$('//body/path-to-element')` to specify an exact path from the starting element to the one you get to. This is not ideal since it renders the tests fragile to changes in the DOM.

If you use one of options 2-4, you should create a chain of element selectors where the top of the chain uses option 1. Suppose we have a DOM like this:

```text

       Root
       /  \
      /   ...
     /      \
   ...   Element A: class="webdriverio-test-elem-a"
             \
             ...
            /  \
           ...  \
                 \
              Element B: id="elem-b"
```

Then you can select Element B with this selector chain:

```js
var elemB = $('.webdriverio-test-elem-a').$('#elem-b');
```

Notice that the top of the chain, where we select Element A, uses method 1.

Sometimes you need to distinguish between several different elements which all look the same to element selectors. You can iterate over all the elements to find the right one. For example, suppose we want to click on the button to open a topic, where the button text is the topic name. We could find the right button like this:

```js
var buttons = $$('.webdriverio-test-button');
...
var openTopic = async function(topicName) {
  await waitFor.elementToBeClickable(
    buttons[0],
    'Topic buttons taking too long to become clickable.'
  );
  for (i = 0; i < buttons.length; i++) {
    var button = buttons[i];
    var buttonText = await action.getText(
      `Topic button ${i}`, button);
    if (buttonText === topicName) {
      await action.click('Topic button ${i}', button);
      return True;
    }
  }
  return False;
}
```

It might be tempting to use the `buttons[0]`, `buttons[last]`, and `buttons[n]` directly when you know what order the elements will come in. However, this makes the tests fragile to changes in the page, and it makes the code hard to read. You should also avoid accessing page elements by index because that's not how most users will find elements. They will be relying on the text identifying those elements, and your test should too.

Except for cases where an element selector is crafted dynamically, all element selectors should be at the top of a utility file. There should be no element selectors in suite files.

#### Non-Angular pages

All the protractor code assumes you are working in an Angular webpage. If you need to move to non-Angular context (for example in an iframe) then look at the login function of `users.js` or the `embedding.js` test for examples of how to proceed.

### Writing robust tests

#### Flakiness

It is easy to accidentally write _flaky_ end-to-end tests, which means that the tests sometimes pass and sometimes fail for non-deterministic reasons. For example, you might write a test assuming that all the elements of the page load at once. However, you have probably noticed that when your browser slows down, it sometimes loads parts of the page before others. This could lead your test to fail randomly, which is called flaking. Here are some tips for avoiding flakiness in your tests:

* HTML tags should be unique if possible. When they are not unique, for instance when multiple copies of the same HTML are created dynamically, we should not find one with indexing. A great example of how to do this correctly is in `this.playTutorial` in `ExplorationEditorMainTab.js`.

  There is really only one case where it is acceptable to identify HTML elements by index, which is when the following conditions all hold:

  1. The elements you want to choose among are siblings, meaning that they share the same parent element. If they aren't siblings, then you can add use the parent elements to distinguish between them, for example by adding HTML classes to the parents.
  2. The elements you want to choose among are identical. In particular, if the elements contain different text, then you can use that text to distinguish them.
  3. The elements you want to choose among are generated dynamically, so you can't modify them to add HTML classes.

* Avoid for loops where the loop index is used in asynchronous calls. `this.expectHintsTabContentsToMatch` in `ExplorationEditorTranslationTab.js` is a better way because it puts the index in the CSS selector, so the index is used before the asynchronous part kicks in.

* Do not use URLs to navigate to a page, for example opening the about page by navigating to `/about` instead of clicking the appropriate buttons

* Do not use `browser.pause()` calls. They are fine for debugging, but in the final test you should use `waitFor` instead.

* In page objects, each function should use `waitFor.js` to wait for the elements it acts on to appear or be clickable. Alternatively, you can use a function from `action.js` that has the waitFor calls built-in. If the function effects a change, it should also wait for the change to complete (e.g. the next page to finish loading if the function clicks a link).

#### Independence

The tests may be run either sequentially or in isolation, and they need to be written to function correctly in both cases. Further, we may rearrange which tests are run together to optimize performance. This means that each `describe(...` block of tests should work regardless of what tests are run before (or after) it. Here are some tips for writing independent tests:

* Ensure that usernames and emails used in each test are unique by giving them a distinctive form; in e.g. the editorAndPlayer page usernames should look like `user1EditorAndPlayer` and emails like `user1@editorAndPlayer.com`. Use this pattern for other names in the tests, for example topic and skill names, for example `skill1EditorAndPlayer`. Some structures have character limits that may disallow this convention. In that case, feel free to shorten the name, e.g. with an abbreviation. You may want to use a constant though if the name gets too unreadable.

* Avoid accessing items by index. For example, to select an exploration from a list, search for the name of the exploration instead of assuming the exploration will be at some index. Take a look at the `_getExplorationElements` function in [`core/tests/webdriverio_utils/LibraryPage.js`](https://github.com/oppia/oppia/blob/develop/core/tests/webdriverio_utils/LibraryPage.js) for an example.

### Checking for flakiness

When submitting a pull request that adds end-to-end tests, please re-run your new tests many times to make sure they pass consistently. We will ask for screenshots in the PR thread showing 5 consecutive passes of the suite(s) where you added tests.

When re-running your test, you will likely see flakes that are not related to your changes. These do not count toward the required number of passes, and they do not count against the requirement that the passes be consecutive. For example, the following would be sufficient:

1. All tests pass
2. All but one test pass. The failing test is not one you added.
3. All tests pass
4. All tests pass
5. All tests pass
6. All tests pass

Please re-run your tests on CI, not locally on your machine, because flakes often appear only on CI and are not reproducible locally.

### Codeowner Checks

When the Automated QA Team does a codeowner review on your PR that changes the e2e tests, they will be looking to make sure that you follow all the guidance in this wiki page. In the checklist below, we list some of the most common problems we see. To get your PR merged faster, please check that your PR satisfies each item:

* [ ] All constants should be in all-caps. (This isn't really an e2e test issue, but we see it a lot.)
* [ ] All element selectors, e.g. `$('.webdriverio-test-my-element')`, need to be at the top of the file. There are a few exceptions:
    * Keeping selectors with the code that uses them is okay in some utility files where the utilities do not generally share selectors.
    * When you are chaining selectors, only the root selector (first in the chain) needs to be at the top of the file.
* [ ] Any time you create something in Oppia that needs a globally unique name to be identified by the tests (e.g. explorations, topics, skills, and users), make sure to follow the naming guidance in the [Independence](https://github.com/oppia/oppia/wiki/WebdriverIO#independence) section above.
* [ ] Each `it` block in the test must be able to be run independently of the others. Imagine running any number of your `it` blocks in any order. Regardless of which you choose and in what order you run them, they should work correctly.
* [ ] Before you interact with _any_ element on the page, you must wait for it to be present, visible, or clickable (depending on how you interact with it) using the [`waitFor`](https://github.com/oppia/oppia/blob/develop/core/tests/webdriverio_utils/waitFor.js) functions. The [`actions`](https://github.com/oppia/oppia/blob/develop/core/tests/webdriverio_utils/action.js) functions handle this for you.
* [ ] If you repeat some code a lot, make it a function! This also makes it a lot easier to review your code.
* [ ] If you make a generally useful function, add it to the relevant utilities file so that other people can benefit from it too.
* [ ] You will need to provide screenshots showing that the tests aren't flaky after your changes. The requirements are detailed above in the [Temporary Flakiness Mitigation Measures](https://github.com/oppia/oppia/wiki/WebdriverIOs#temporary-flakiness-mitigation-measures) section.
* [ ] Variables should be named as nouns, and functions should be named as verbs. In particular, make sure your page element variable names are nouns. For example, use `itemSelectButton` instead of `itemSelect`.
* [ ] All HTML classes you reference in root selectors in the tests should begin with `webdriverio-test-`. If you can't change the classes on an element you need to select, find a parent element you can change and then chain the selectors like this: `$('.webdriverio-test-parent-element').$('.class-of-element-you-cannot-change')` or like this: `$('.webdriverio-test-parent-element .class-of-element-you-cannot-change')`.

### Important Tips

* All test blocks should have an `afterEach` that runs `general.checkForConsoleErrors` to verify no unexpected console errors appeared while the test was running.

* Check your assumptions! For example, if you are assuming that only one exploration on the server will have a particular title, use an `expect` call to check.

## Metrics

We track passes, known flakes, and failures that aren't known to be flakes (called "failures") using a logging server. You can view these metrics at https://oppia-e2e-test-results-logger.herokuapp.com.

## Reference

### Forms and objects

There are certain types of input that are used so commonly throughout Oppia that they are defined in `core/templates/forms/` and reused across many pages. There are corresponding webdriverio functions to manipulate the forms, and these functions are located in `core/tests/webdriverio_utils/forms.js`.

There are more specialized input types in `extensions/objects` which you can also make use of (generally in interactions).

To get a form or object editor, you can use the `getEditor` function in `forms.js`. It accepts the name of the form or object as an argument, and it searches first in `forms.js` and then in `extensions/objects/webdriverio.js` for a function of the same name. For example, suppose we want to set the value of a real number field. We can use `getEditor` like this:

```js
var realNumberFieldElement = $('.webdriverio-test-real-number');
...
var realEditor = getEditor('RealEditor')(realNumberFieldElement);
await realEditor.setValue(3.14);
```

Notice that we did not use an `await` before `getEditor` because the `RealEditor` function is not asynchronous. However, other editors are, in which case they will include `async` in their declaration lines. For these, you will need to use `await`.

#### Rich Text

One of the most important forms is the rich-text editor, which is used both directly in the editor and in various interactions. Commonly, a page utility will provide a `setContent` function that accepts an "instructions" argument. This argument accepts an instructions function that the `setContent` function will call with the rich text editor as an argument. For example, you might have an instructions function like this:

```js
var instructions = async function(richTextEditor) {
  await richTextEditor.appendBoldText('bold');
  await richTextEditor.appendItalicText('italic');
}
```

Then you can pass this function to `ExplorationEditorMainTab.setContent`:

```js
await explorationEditorMainTab.setContent(instructions);
```

Then inside `setContent`, you instructions function will be called:

```js
var editorElement = $('.protractor-test-editor');
...
this.setContent = async function(instructions) {
  ...
  var richTextEditor = await forms.RichTextEditor(editorElement);
  instructions(richTextEditor);
  ...
}
```

Later on you will probably want to check that your content is being displayed correctly, for example using a page utility function `expectContentToMatch`. To this you should send a function which will then be supplied with a `richTextChecker` which exposes analogous functions. For example you might send:

```js
var instructions = async function(richTextChecker) {
  await richTextChecker.readBoldText('bold');
  await richTextChecker.readItalicText('italic');
}
```

Then inside the `expectContentToMatch` function, we can pass your instructions to the `forms.expectRichText` function:

```js
var richTextDisplay = $('.protractor-test-rich-text');
...
this.expectContentToMatch = async function(instructions) {
  await forms.expectRichText(richTextDisplay).toMatch(instructions);
}
```

The full range of editing and checking functions can be found in `core/tests/webdriverio_utils/forms.js` in the `RichTextEditor` and `RichTextChecker` classes.

Frequently you will just want to put plain text into a rich text area. For this you can quickly generate instruction functions like this:

```js
var instructions = await forms.toRichText('plain text');
```

This works for both editors and checkers.

### Async-Await Tips

#### Good Patterns

* Getting a URL
  ```js
  await browser.url('someURL');
  ```
* Expectations
  ```js
  expect(await elem.getText()).toEqual('expectedText'));
  ```
* Variable assignments
  ```js
  var myVar = await myAsyncFunc();
  ```
* If statements
  ```js
  if (await elem.getText() === "hi") {
    await elem.click();
  }
  ```
* `driver.findElement`:
  ```js
  await driver.findElement(...)
  ```
* `map()` returns a list of promises, but `await` will only wait if the expression it is provided evaluates to a single promise. To wait until all of the `map()` operations are complete, use `Promise.all` like this:
  ```js
  await Promise.all(myList.map(async function(elem) {
    await elem.click();
  }));
  ```
  * This is the advice we see online, but we've also encountered cases where removing the `Promise.all` seems to fix bugs, so this guidance might not be right. Try both.
  * If you are mapping over an `$$` selector, we've encountered cases where ```$$(selector).map(function)``` does not properly await for async functions. Instead of this:

    ```js
    let mappedElements = $$(selector)
    await Promise.all(await mappedElements.map(async(x) => {
        return await functionThatIsAsync(x);
    }));
    ```

    Try:

    ```js
    let mappedElements = $$(selector)
    for (let x of (await mappedElements)) {
      await functionThatIsAsync(x);
    }
    ```

    The above should properly await for each functionThatIsAsync to resolve.

* Chained Function Calls
  ```js
  await (await asyncFunc1()).asyncFunc2();
  ```
  We have to `await` the result of `asyncFunc1` before calling `asyncFunc2`. This won't work:
  ```js
  await asyncFunc1().asyncFunc2();
  ```
  Here's a common example of when we need these nested `await`s:
  ```js
  await (await browser.switchTo().activeElement()).keys(explanation);
  ```
* Rejection callbacks
  ```js
  waitFor.visibilityOf(dismissWelcomeModalButton,
    'Welcome modal not becoming visible').then(
    () => {
      waitFor.elementToBeClickable(
        dismissWelcomeModalButton,
        'Welcome modal is taking too long to appear');
      dismissWelcomeModalButton.click();
    },
    (err) => {
      // Since the welcome modal appears only once, the wait for its
      // visibilty will only resolve once and timeout the other times.
      // This is just an empty error function to catch the timeouts that
      // happen when the the welcome modal has been dismissed once. If
      // this is not present then protractor uses the default error
      // function which is not appropriate in this case as this is not an
      // error.
    }
  );
  ```
  Here, we specify an empty rejection callback so that the test can still pass if the wait times out. To replicate this behavior with async-await, we can use a `try` block:
  ```js
  try {
    await waitFor.visibilityOf(
      dismissWelcomeModalButton, 'Welcome modal not becoming visible');
    await waitFor.elementToBeClickable(
      dismissWelcomeModalButton,
      'Welcome modal is taking too long to appear');
    await dismissWelcomeModalButton.click();
    await waitFor.invisibilityOf(
      translationWelcomeModal,
      'Translation welcome modal takes too long to disappear');
  } catch (e) {
    // Since the welcome modal appears only once, the wait for its
    // visibilty will only resolve once and timeout the other times.
    // This is just an empty error function to catch the timeouts that
    // happen when the the welcome modal has been dismissed once. If
    // this is not present then protractor uses the default error
    // function which is not appropriate in this case as this is not an
    // error.
  }
  ```
* Checking for movement:
  ```js
  var pos1 = elem.getAttribute('pos');
  var pos2 = elem.getAttribute('pos');
  expect(pos1).not.toBe(pos2);
  ```
  Here we want to check that `elem` is moving (represented as its `pos` attribute changing). This might work because the `getAttribute` calls take long enough to execute that in the meantime, `elem` has moved. To address this, we can instead wait for the element to move:
  ```js
  var pos1 = await elem.getAttribute('pos');
  try {
    await waitFor.elementAttributeToBe(elem, 'pos', pos1 + 1, 'elem not moving');
  } except (e) {
    var pos2 = await elem.getAttribute('pos');
    expect(pos1).not.toBe(pos2);
  }
  ```
  Notice that here, we wait for `elem` to advance one unit. If that happens, then the test passes. However, what if `elem` advances 2 units before `waitFor` checks again? To address this, we check whether `elem` has moved after catching the error from the `waitFor`.
* Make sure you add `async` and `await` in the `afterAll` blocks if they check for console errors (they all should). If you don't the test might pass even though errors are appearing in the console log.

#### Anti-Patterns

* `forEach` does not work for async-await. Use a `for ... of` loop instead if you want to operate in sequence, or use `map()` to operate in parallel. See [this Stack Overflow post](https://stackoverflow.com/a/37576787) for examples.
* `filter` can be problematic. Consider re-writing as a `for` loop instead.
* `.then()` functions
  ```js
  someAsynchronousFunction().then(function(output) {
    return // doing something with output
  });
  ```
  should be written instead as
  ```js
  var output = await someAsynchronousFunction();
  await // do something with "output"
  ```
* `browser.switchTo().activeElement()` can cause problems when combined with our `action` functions. One such problem is a `Cannot read property 'bind' of undefined` error. Instead, use the normal `element(...)` element selectors to get the element you want to interact with. You can use a `await browser.debug()` statement right before `browser.switchTo().activeElement()` to find what active is element there.
