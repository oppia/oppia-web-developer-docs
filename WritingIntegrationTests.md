# Writing integration tests in Protractor #

The protractor components are located in three places:
  * `core/tests/protractor/*`: the tests themselves.
  * `core/tests/protractor_utils/*`: utilities for performing actions using elements from the core components of oppia (those found in `core/templates/dev/head`).
  * `extensions/**/protractor.js`: utilities for actions specific to a particular extension (such as interactions and rules).

If you are just creating a new interaction and want to add integration tests for it then you can follow the guidance given [here](CreatingInteractiveWidgets.md), though the "forms and objects" section of this page may also be helpful.

## Forms and objects ##

There are certain types of input that are used so commonly throughout oppia that they have specialised functionality, which can be found in `core/templates/dev/head/forms/`. There are corresponding protractor functions to manipulate the different forms located in `core/tests/protractor_utils/forms.js`. The available forms are:
  * Dictionary: This provides the function `editEntry` which will return the relevant protractor editor for the given entry of the dictionary.
  * List: Similarly this provides `editItem` to obtain a new editor for a particular list item, together with various other list editing functions.
  * Real.
  * Rich text: see below.
  * Autocomplete dropdowns.

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


## Core Utilities ##

The core protractor utilities consist of the following files:
  * `admin.js`: Manipulations of controls on the /admin page.
  * `editor.js`: Editor page functionality. The most important functions this exposes are:
    * `setContent`: This sets the rich-text of the main state content, potentially including custom extensions.
    * `setInteraction`: To choose a particular interaction, and customize it in whatever ways that interaction makes available.
    * `RuleEditor`: When given a rule number this returns an editor for that rule, which provides functions `setDescription`, `setFeedback`, `setDestination` and others to specify various aspects of the rule.
    * `createState`
    * `moveToState`
    * `saveChanges`
  * `forms.js`: See above.
  * `gallery.js`: Controls for the gallery, mainly to filter or select or explorations.
  * `general.js`: Various components, some of them specific to oppia and others providing new features not found in Protractor.
  * `player.js`: Functionality for playing an exploration. The `richTextInstructions` here refer to functions that take a `richTextChecker` of the type described above.
  * `users.js`: Means of creating and logging in and out users.
  * `workflow.js`: Tools for moving explorations through the process of creation, publication, featuring and adding new roles.

### Writing utilities ###

Much of the difficulty of writing protractor code lies in specifying the element with which you wish to interact. It is important to do so in a way that is as insensitive as possible to superficial DOM features such as text and styling, so as to reduce the likelihood that changes will have to be made when the production html is changed. The order in which to attempt to specify an element in Oppia is as follows:
  1. Adding a `protractor-test-some-name` code to the class of the element in question, and then referencing it by `by.css('.protractor-test-some-name')`. We do not use `by.id` for this purpose because Oppia frequently displays multiple copies of a DOM element on the same page, and if an `id` is repeated then references to it will not work properly. This is the preferred method, since it makes clear to those editing production code exactly what the dependence on protractor is, thus minimising the likelihood of confusing errors when they make changes.
  1. Existing element ids, for example `explorationLanguageCode`. We avoid using existing classes for this purpose as they are generally style specifications such as `big-button` that may be changed in the future.
  1. You can use `by.tagName` if you are sure you are in a context where only one element will have (or is likely to have in future) the given name. The `<input>` and `<button>` tags often fall under this category. Try to avoid `by.buttonText` and `by.linkText` since they are sensitive to the choice of user-facing text.
  1. Finally, you can use `by.xpath` to specify an exact path from the starting element to the one you get to. This is not ideal since it renders the tests fragile to changes in the DOM. However sometimes it is necessary, for example to send elements to `expectRichText` in `forms.js` which requires it receive an exact element that cannot be directly specified.

Sometimes you need to distinguish between several different sibling elements, for which purpose you can use commands of the form
```
    .all(by.css(...)).first()
    .all(by.css(...)).last()
    .all(by.css(...)).get(n)
```
in place of `.element(by.css(...))`. If this does not suffice then you may need to iterate over all the candidates, examining each in turn until you find the right one. An example of how to do so is given by `moveToState` in `core/tests/protractor_utils/editor.js`.

All the protractor code assumes you are working in an Angular webpage. If you need to move to non-Angular context (for example in an iframe) then look at the login function of `users.js` or the `embedding.js` test for examples of how to proceed.

It can happen that a test fails because the webpage has not finished loading functionality by the point at which protractor attempts to use it; failures of this kind can be inconsistent between successive runs of the same test. If one occurs you can try the following:
  1. Run `protractor.getInstance().waitForAngular()` before the command that causes the failure. This will cause the test to wait for the page to finish all its computations, including receiving data from the server, before proceeding.
  1. If this fails, run `general.waitForSystem()` after `waitForAngular()`. This will wait a few seconds before continuing and is crude but effective.
  1. If you are attempting to use an element that is not visible you can try `general.scrollElementIntoView(elem)` to get to it, though normally this should happen automatically.

## The Tests Themselves ##

The protractor tests use the above functions to simulate a user interacting with Oppia. They should not engage in direct interactions with the page (e.g. using `element`) but instead make use of the `protractor_utils`. If new functionality is needed for a test then it should be added in the utilies directory, so that is available for future tests to use and easy to maintain. A minor exception to this are the `embedding.js` tests which interact with a page contstructed specifically to demonstrate embedding, and which is thus not of any wider interest.

The current tests are as follows:
  * `editorAndPlayer.js`: The largest and most important suite, this uses `editor.js` to create various different explorations and then `player.js` to play them and validate their behaviour. In particular it contains the test that runs all the interaction-specific test suites.
  * `embedding.js`: Tests that oppia explorations can be embedded into other webpages, and interact correctly with those pages.
  * `privileges.js`: Checks the awarding of rights to an exploration using roles.
  * `publicationAndGallery.js`: Checks the functions from used to `workflow.js` to publish and feature explorations, and the resultant display of those explorations in the gallery, using `gallery.js`.
  * `userManagement.js`: Brief and largely superseded tests of creating different classes of user using `users.js` and `admin.js`.

## Important Gotchas ##

The tests may be run either sequentially or in isolation, and they need to be written to function correctly in both cases. To this end care should be taken ensure that the **user names and emails used in each test are unique**. That way the only point of contact between different tests is the gallery, which so far is used only be `embedding.js` and `publicationAndGallery.js` and has not been a problem. The user names in different files have different themes to minimise the likelihood of conflict.

All test blocks should have an `afterEach` that runs `general.checkForConsoleErrors` to verify no unexpected console errors appeared while the test was running.