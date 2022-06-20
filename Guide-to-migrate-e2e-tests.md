## Table of contents

* [Overview](#overview)
* [Selectors](#selectors)
* [Events on selected elements](#events-on-selected-elements)
* [Points to note while migrating](#points-to-note-while-migrating)
* [Example migration](#example-migration)

## Overview

Currently, Oppia End-to-End tests are in a hybrid state where we have both WebdriverIO and Protractor test suites. The GSoC project **Migrate away from Protractor** aims to migrate all the existing End-to-End tests to WebdriverIO.

This guide is to help contributors in migrating end-to-end tests from Protractor to WebdriverIO during the hybrid state.

## Selectors

A selector is used to query an element. The WebDriver Protocol provides several selector strategies to query an element. WebdriverIO simplifies them to keep selecting elements simple.

The `$` command is a short way to call the findElement command in order to fetch a single element on the page

| Goal                                     | Protractor                               |WebdriverIO           |
| -----------------------------------------| -----------------------------------------|----------------------|
| Select element by class name             |`element(by.css('.some-css-class'))`           |`$('.some-css-class')`     |
| Select element containing certain string Text |`element(by.cssContainingText(tag, text))`|`$('tag=text')`       |
| Selecting Multiple Elements              |`element.all(by.css('.some-css-class'))`       |`$$('..some-css-class')`    |
| Select element by ID                     |`element(by.css('#some-css-id'))`              |`$('#some-css-id')`        |
| Select element inside a element with some class name |`element(by.css('some-css-class')).element(by.css('tag-within-css'))`  | `$('some-css-class').$('tag-within-css’)`      |
| Selecting element one by one in loop     |`element.get(i)`                          |`$$(selector)[i]`     |

There is no proper substitute available for the command `element.getWebElement()` in webdriverIO, but we can use `browser.findElement()` as a substitute for this.

For example, take look at the following code of protractor:

```js
await browser.executeScript(
  'arguments[0].click()', await clickableElement.getWebElement());
```

WebdriverIO version will be like this:

```js
 await browser.execute(
  'arguments[0].click()',
  await browser.findElement('css selector', clickableElement));
```

## Events on selected elements

| Events                                  | Protractor                               |WebdriverIO            |
| -----------------------------------------| -----------------------------------------|-----------------------|
| Click on the element                     |`element.click()`                         |`$(selector).click()`  |
| Get the text content from a DOM-element  |`element.getText())`                      |`$(selector).getText()`|
| Navigate to the given destination        |`browser.get(url)`                        |`browser.url(url)`     |
| Get the url of the currently opened website.|`browser.getCurrentUrl()`              |`browser.getUrl()`     |
| Get an attribute from a DOM-element based on the attribute name.|`element.getAttribute(attributeName)`|`$(selector).getAttribute(attributeName)`|
| Wait until a given condition is fulfilled.|`browser.wait(condition, time, optional_msg)`|`browser.waitUntil(condition, { timeout, timeoutMsg, interval })`|
| Send a sequence of keystrokes to the active element|`element.sendKeys(keys)` |`element.setValue(keys)`     |
| Selected DOM-Element is clickable, visible, and exists.|`until.elementToBeClickable(element)` |`$(selector).isClickable()`|
|Get the value of a `<textarea>`, `<select>` or `<input>` found by given selector|`element.getText()` |`$(selector).getValue()`|
|Clear a `<textarea>` or `<input>` element’s value   |`element.clear()` |   `$(selector).clearValue()`  |

For more details please visit [webdriverio's official documentation](https://webdriver.io/docs/gettingstarted).

## Points to note while migrating

1. Currently, we are having two versions of the end-to-end test present in the codebase, so before moving forward with migration please refer to [Hybrid state doc](Hybrid-state.md) for a better understanding of this state.

2. The basic utility files i.e. forms.js, waitFor.js, action.js, general.js, user.js will already be migrated for the ease of contributors.

   | Files                                      | Expected Migration Date            |
   | -------------------------------------------|  ----------------------------------|
   |  waitFor.js, action.js, general.js, user.js|   2 July 2022                      |
   | forms.js                                   |   20 July 2022                     |

3. For more information on how to add new tests or modify the existing tests please refer to [Write E2E tests in WebdriverIO](WebdriverIO.md#run-e2e-tests) section.

## Example migration

**Protractor**

  ```js
var until = protractor.ExpectedConditions;

this.editUserRole = async function(username) {
  await browser.get('/admin');
  
  var adminRolesTab = element(by.css('.protractor-test-admin-roles-tab'));
  await adminRolesTab.click();

  expect(await adminRolesTab.getAttribute('class')).toMatch('active');

  var adminRolesTabContainer = element(by.cssContainingText('h1', 'Role Conainer'));
  await browser.wait(
    await until.visibilityOf(element),
    10000, 'Element not visible');

  var usernameInputFieldForRolesEditing = element.all(by.css(
    '.protractor-test-username-for-role-editor'));
  await usernameInputFieldForRolesEditing.first().sendKeys(username);

  var editUserRoleButton = element(by.id('protractor-test-button');
  await buttonText = editUserRoleButton.getText();
  expect(buttonText).toBe('Button Text');
};
```

**WebdriverIO**

  ```js
var until = require('wdio-wait-for');

this.editUserRole = async function(username) {
  await browser.url('/admin');

  var adminRolesTab = $('.webdriverio-test-admin-roles-tab');
  await adminRolesTab.click();

  expect(await adminRolesTab.getAttribute('class')).toMatch('active');

  var adminRolesTabContainer = $('h1=Role Conainer');
  await browser.waitUntil(
    await until.visibilityOf(adminRolesTabContainer),
    {
      timeout: 10000,
      timeoutMsg: 'Element not visible'
    });

  var usernameInputFieldForRolesEditing = (
    $$('.webdriverio-test-username-for-role-editor'));
  await usernameInputFieldForRolesEditing[0].setValue(username);

  var editUserRoleButton = $('#webdriverio-test-button');
  await buttonText = editUserRoleButton.getText();
  expect(buttonText).toBe('Button Text');
};
```
