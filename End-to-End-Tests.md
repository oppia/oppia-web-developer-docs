At Oppia, we highly regard the end user, that is, both the creator as well as the learner. Therefore, we have an extensive system of end-to-end tests to test each functionality thoroughly. The end-to-end tests cover both the desktop as well as mobile intefaces.
The tests are organized as follows:
1. `protractor`: This directory contains test suites which are common for both desktop and mobile interfaces. Certain operations are possible only on one or the other interface. To distinguish between the interfaces, we use the boolean, `browser.isMobile` defined in `onPrepare` of the protractor configuration file.
2. `protractor_desktop`: This directory houses all test suites which are exclusive for desktop interfaces. This generally includes core creator components like the rich-text editor.
3. `protractor_mobile`: This directory contains all test suites which are exclusive for mobile interfaces. This includes navigating around the website using the hamburger menu.
4. `protractor_utils`: This directory contains utilities for performing actions using elements from the core components of oppia (those found in `core/templates`).
5. `extensions/**/protractor.js`: This directory houses utilities for actions specific to a particular extension (such as interactions and rules).

**Note**: The e2e test files are owned by the QA team.


## Configuration ##

The end-to-end tests for desktop interface run on Travis using a headless Chrome browser. The mobile tests use appium. Since protractor does not [officially support](http://www.protractortest.org/#/mobile-setup) appium as of now and neither does Travis provide a headless mobile browser, we use Browserstack to run the mobile tests on Travis. Also, mobile tests require a different configuration. Therefore, we have two protractor configuration files, `protractor.conf.js` and `protractor-browserstack.conf.js`.
For details on how to use Browserstack with Travis CI, please follow [this link](https://docs.travis-ci.com/user/browserstack/).
To run local tests for mobile on Browserstack, copy the contents of `core/tests/.browserstack.env.example` into a newly created file, `core/tests/.browserstack.env` and follow [this link](https://github.com/oppia/oppia/wiki/Browser-and-Device-Testing-Using-BrowserStack#get-access-to-browserstack) to get access to the login credentials required to run tests on Browserstack.

If you are just creating a new interaction and want to add end-to-end tests for it then you can follow the guidance given at [[Creating Interactions|Creating-Interactions]], though the "forms and objects" section of this page may also be helpful.

## The Tests ##

This section lists down all the suites directory-wise.

#### 1. `core/tests/protractor`:
* `accessibility.js`: End-to-end tests for testing screenreader and keyboard user accessibility features and that console errors are logged appropriately.
* `learnerFlow.js`: End-to-end tests for learner flow using the learner dashboard functionality.
* `libraryFlow.js`: End-to-end tests for library flow.
* `profileMenuFlow.js`: End-to-end tests to login, check various pages and then logout using the profile menu.
* `subscriptionsFlow.js`: End-to-end tests for the subscriptions functionality.

#### 2.`core/tests/protractor_desktop`:
* `collections.js`: End-to-end tests for collections.
* `editorAndPlayer.js`: The largest and most important suite, this uses `editor.js` to create various different explorations and then `player.js` to play them and validate their behaviour. In particular it contains the test that runs all the interaction-specific test suites.
* `editorFeatures.js`: End-to-end tests for feedback on explorations. Tests the following sequence:
   * User 1 creates and publishes an exploration.
   * User 2 plays the exploration and leaves feedback on it
   * User 1 reads the feedback and responds to it.
* `embedding.js`: Tests that oppia explorations can be embedded into other webpages, and interact correctly with those pages.
* `extensions.js`: End-to-end tests for rich-text components and interactions.
* `learnerDashboardSubscriptionsAndFeedbackThreads.js`: End-to-end tests for learner dashboard subscriptions and feedback functionality.
* `publicationAndLibrary.js`: End-to-end tests of the publication and featuring process, and the resultant display of explorations in the library.
* `stateEditor.js`: End-to-end tests of the state editor.
* `userJourneys.js`: End-to-end tests for user management.

#### 3. `core/tests/protractor_mobile`:
* `navigation.js`:  End-to-end tests for testing navigation on mobile as a guest.

## Core Utilities ##

The core protractor utilities consist of the following files:
  * `AdminPage.js`: Manipulations of controls on the /admin page.
  * `CollectionEditorPage.js`: Page object for Collection Editor Page, for use in Protractor tests.
  * `CreatorDashboardPage.js`: Page object for the creator dashboard, for use in Protractor tests.
  * `ExplorationEditorFeedbackTab.js`: Page object for the exploration editor's feedback tab, for use in Protractor tests.
  * `ExplorationEditorHistoryTab.js`: Page object for the exploration editor's history tab, for use in Protractor tests.
  * `ExplorationEditorMainTab.js`: Editor page functionality. The most important functions this exposes are:
    * `setContent`: This sets the rich-text of the main state content, potentially including custom extensions.
    * `setInteraction`: To choose a particular interaction, and customize it in whatever ways that interaction makes available.
    * `RuleEditor`: When given a rule number this returns an editor for that rule, which provides functions `setDescription`, `setFeedback`, `setDestination` and others to specify various aspects of the rule.
    * `createState`
    * `moveToState`
    * `saveChanges`
  * `ExplorationEditorPage.js`: Page object for the exploration editor, for use in Protractor tests.
  * `ExplorationEditorSettingsTab.js`: Page object for the exploration editor's settings tab, for use in Protractor tests.
  * `ExplorationEditorStatsTab.js`: Page object for the exploration editor's stats tab, for use in Protractor tests.
  * `ExplorationPlayerPage.js`: Functionality for playing an exploration. The `richTextInstructions` here refer to functions that take a `richTextChecker` of the type described above.
  * `forms.js`: Utilities for interacting with forms when carrying out end-to-end testing with protractor.
  * `general.js`: Various components, some of them specific to oppia and others providing new features not found in Protractor.
  * `LearnerDashboardPage.js`: Page object for the learner dashboard, for use in Protractor tests.
  * `LibraryPage.js`: Page object for the library pages, for use in Protractor tests.
  * `PreferencesPage.js`: Page object for the preferences page, for use in Protractor tests.
  * `SubscriptionDashboardPage.js`: Page object for the subscription dashboard, for use in Protractor tests.
  * `ThanksPage.js`: Page object for the thanks page, for use in Protractor tests.
  * `users.js`: Means of creating and logging in and out users.
  * `waitFor.js`: Utilities for delaying actions with Protractor's ExpectedConditions.
  * `workflow.js`: Tools for moving explorations through the process of creation, publication, featuring and adding new roles.

The protractor tests use the above functions to simulate a user interacting with Oppia. They should not engage in direct interactions with the page (e.g. using `element`) but instead make use of the `protractor_utils`. If new functionality is needed for a test then it should be added in the utilities directory, so that is available for future tests to use and easy to maintain. A minor exception to this are the `embedding.js` tests which interact with a page constructed specifically to demonstrate embedding, and which is thus not of any wider interest.

## Forms and objects ##

There are certain types of input that are used so commonly throughout oppia that they have specialised functionality, which can be found in `core/templates/forms/`. There are corresponding protractor functions to manipulate the different forms located in `core/tests/protractor_utils/forms.js`. The available forms are:
  * Dictionary: This provides the function `editEntry` which will return the relevant protractor editor for the given entry of the dictionary.
  * List: Similarly this provides `editItem` to obtain a new editor for a particular list item, together with various other list editing functions.
  * Real.
  * Rich text: see below.
  * Select2 autocomplete dropdowns and multi-select dropdowns.

There are more specialised input types in `extensions/objects` which you can also make use of (generally in interactions). The dictionary and list functions above will look for entry / item editors first in `core/tests/protractor_utils/forms.js` and then in `extensions/objects/protractor.js`.

### Rich Text ###

One of the most important forms is the rich-text editor, which is used both directly in the editor and in various interactions. When you want to use it, then you will be provided with a function such as `setContent` (for the state content) to which you should send a function that performs your desired actions using the relevant rich text editor. This second function will be supplied with a `richTextEditor` that exposes various functions such as `appendBoldText` for you to use. So for example you might write the function
```
    function(richTextEditor) {
      richTextEditor.appendBoldText('bold');
      richTextEditor.appendItalicText('italic');
    }
```
which will write first bold then italic text.

Later on you will probably want to check that your content is being displayed correctly, for example using the function `expectContentToMatch`. To this you should send a function which will then be supplied with a `richTextChecker` which exposes analagous functions. So for example you might send
```
    function(richTextChecker) {
      richTextChecker.readBoldText('bold');
      richTextChecker.readItalicText('italic');
    }
```
which will check that first bold then italic text is displayed in the order specified.

The full range of editing and checking functions can be found in `core/tests/protractor_utils/forms.js` in the `RichTextEditor` and `RichTextChecker` classes.

Frequently you will just want to put plain text into a rich text area. For this you can replace functions of the above form with the abbreviated
```
    forms.toRichText('plain text')
```
which will work for both the editing and checking cases.

### Writing utilities ###

Much of the difficulty of writing protractor code lies in specifying the element with which you wish to interact. It is important to do so in a way that is as insensitive as possible to superficial DOM features such as text and styling, so as to reduce the likelihood that changes will have to be made when the production html is changed. The order in which to attempt to specify an element in Oppia is as follows:
  1. Adding a `protractor-test-some-name` code to the class of the element in question, and then referencing it by `by.css('.protractor-test-some-name')`. We do not use `by.id` for this purpose because Oppia frequently displays multiple copies of a DOM element on the same page, and if an `id` is repeated then references to it will not work properly. This is the preferred method, since it makes clear to those editing production code exactly what the dependence on protractor is, thus minimising the likelihood of confusing errors when they make changes. Sometimes this may not work, though (e.g. for embedded pages, third-party libraries and generated HTML), in which case you may instead need to use one of the options (2) - (4) below.
  2. Existing element ids, for example `explorationLanguageCode`. We avoid using existing classes for this purpose as they are generally style specifications such as `big-button` that may be changed in the future.
  3. You can use `by.tagName` if you are sure you are in a context where only one element will have (or is likely to have in future) the given name. The `<input>` and `<button>` tags often fall under this category. Try to avoid `by.buttonText` and `by.linkText` since they are sensitive to the choice of user-facing text.
  4. Finally, you can use `by.xpath` to specify an exact path from the starting element to the one you get to. This is not ideal since it renders the tests fragile to changes in the DOM. However sometimes it is necessary, for example to send elements to `expectRichText` in `forms.js` which requires it receive an exact element that cannot be directly specified.

Sometimes you need to distinguish between several different sibling elements, for which purpose you can use commands of the form
```
    .all(by.css(...)).first()
    .all(by.css(...)).last()
    .all(by.css(...)).get(n)
```
in place of `.element(by.css(...))`. If this does not suffice then you may need to iterate over all the candidates, examining each in turn until you find the right one. An example of how to do so is given by `moveToState` in `core/tests/protractor_utils/editor.js`.

** WARNING: This can lead to flaky and fragile tests, so avoid this if possible. See below for details.**

All the protractor code assumes you are working in an Angular webpage. If you need to move to non-Angular context (for example in an iframe) then look at the login function of `users.js` or the `embedding.js` test for examples of how to proceed.

It can happen that a test fails because the webpage has not finished loading functionality by the point at which protractor attempts to use it; failures of this kind can be inconsistent between successive runs of the same test. If one occurs you can try the following:
  1. Use ExpectedConditions to determine if the element in question is either present, visible or clickable, depending on your use case.
  2. If you are attempting to use an element that is not visible you can try `general.scrollElementIntoView(elem)` to get to it, though normally this should happen automatically.

## Writing Robust Tests ##

### Flakiness ###

It is easy to accidentally write _flaky_ end-to-end tests, which means that the tests sometimes pass and sometimes fail for non-deterministic reasons. For example, you might write a test assuming that all the elements of the page load at once. However, you have probably noticed that when your browser slows down, it sometimes loads parts of the page before others. This could lead your test to fail randomly, which is called flaking. Here are some tips for avoiding flakiness in your tests:

* HTML tags should be unique if possible. When they are not unique, for instance when multiple copies of the same HTML are created dynamically, we should not find one with indexing, `.first()`, or `.last()`. A great example of how to do this correctly is in `this.playTutorial` in `ExplorationEditorMainTab.js`.
    * There is really only one case where it is acceptable to identify HTML elements by index, which is when the following conditions all hold:
        1. The elements you want to choose among are siblings, meaning that they share the same parent element. If they aren't siblings, then you can add use the parent elements to distinguish between them, for example by adding HTML classes to the parents.
        2. The elements you want to choose among are identical. In particular, if the elements contain different text, then you can use that text to distinguish them.
        3. The elements you want to choose among are generated dynamically, so you can't modify them to add HTML classes.
* Avoid for loops where the loop index is used in asynchronous calls. `this.expectHintsTabContentsToMatch` in `ExplorationEditorTranslationTab.js` is a better way because it puts the index in the CSS selector, so the index is used before the asynchronous part kicks in.
* Do not use URLs to:
    * Get IDs, for example IDs for explorations, collections, or topics
    * Navigate to a page, for example opening the about page by navigating to `/about` instead of clicking the appropriate buttons
* Do not use `browser.sleep(` calls. This is great for debugging, but in the final test you should use `waitFor` instead.
* In page objects, each function should use `waitFor` to wait for the elements it acts on to appear or be clickable. If the function effects a change, it should also wait for the change to complete (e.g. the next page to finish loading if the function clicks a link).

### Independence ###

The tests may be run either sequentially or in isolation, and they need to be written to function correctly in both cases. Further, we may rearrange which tests are run together to optimize performance. This means that each `describe(...` block of tests should work regardless of what tests are run before (or after) it. Here are some tips for writing independent tests:

* Ensure that usernames and emails used in each test are unique by giving them a distinctive form; in e.g. the editorAndPlayer page usernames should look like `user1EditorAndPlayer` and emails like `user1@editorAndPlayer.com`. Use this pattern for other names in the tests, for example topic and skill names, for example `skill1EditorAndPlayer`. Some structures have character limits that may disallow this convention. In that case, feel free to shorten the name, e.g. with an abbreviation. You may want to use a constant though if the name gets too unreadable.
* Avoid accessing items by index. For example, to select an exploration from a list, search for the name of the exploration instead of assuming the exploration will be at some index. Take a look at the `_getExplorationElements` function in [`core/tests/protractor_utils/LibraryPage.js`](https://github.com/oppia/oppia/blob/develop/core/tests/protractor_utils/LibraryPage.js) for an example.

## Async-Await Tips ##

### Good Patterns ###

* Getting a URL
  ```js
  await browser.get('someURL');
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
* When multiple elements might match a locator, we often use `element.all` to get an [`ElementArrayFinder`](https://www.protractortest.org/#/api?view=ElementArrayFinder). This object can usually be used just like a list, but it appears that with async-await, we can only use the functions it defines. In particular:
    * Use `elems.count()` instead of `elems.length` to get the length. This is asynchronous!
    * Use `elems.get(i)` instead of `elems[i]`. `elems.first(i)` and `elems.last(i)` work too.

  You do *not* need to `await` the `element.all` call itself. Also note that a `.map()` or `.filter()` operation on an `ElementArrayFinder` yields a normal array, so you *need* to use `.length` instead of `.count()`.
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
  await (await browser.switchTo().activeElement()).sendKeys(explanation);
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
  Here we want to check that `elem` is moving (represented as its `pos` attribute changing). This might work because the `getAttribute` calls take long enough to execute that in the meantime, `elem` has moved. After migrating to async-await, however, they might run faster. To address this, we can instead wait for the element to move:
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

### Anti-Patterns ###

* `forEach` does not work for async-await. Use a `for ... of` loop instead if you want to operate in sequence, or use `map()` to operate in parallel. See [this stackoverflow post](https://stackoverflow.com/a/37576787) for examples.
* `filter` can be problematic. Consider re-writing as a `for` loop instead.
* .then() functions
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

## Important Tips ##

* All test blocks should have an `afterEach` that runs `general.checkForConsoleErrors` to verify no unexpected console errors appeared while the test was running.
* Check your assumptions! For example, if you are assuming that only one exploration on the server will have a particular title, use an `expect` call to check.
* End-to-end tests are written using the async-await paradigm. To learn how to write tests in this way, see the [async-await wiki page](https://github.com/oppia/oppia/wiki/Migrating-End-to-End-Tests-to-Async-Await)