## Overview

Currently, Oppia E2E tests are in a hybrid state where we have both WebdriverIO and Protractor test suites. The GSoC project **Migrate away from Protractor** aims to migrate all the existing E2E tests to WebdriverIO.

This guide is to help contributors in migrating end-to-end tests from Protractor to WebdriverIO during the hybrid state.

## Selectors

A Selector is used to query an element. The WebDriver Protocol provides several selector strategies to query an element. WebdriverIO simplifies them to keep selecting elements simple

The `$` command is a short way to call the findElement command in order to fetch a single element on the page

| Goal                                     | Protractor                               |WebdriverIO           |
| -----------------------------------------| -----------------------------------------|----------------------|
| Select element by class name             |`element(by.css('.some-css-class'))`           |`$('..some-css-class')`     |
| Select element containing certain string Text |`element(by.cssContainingText(tag, text))`|`$('tag=text')`       |
| Selecting Multiple Elements              |`element.all(by.css('.some-css-class'))`       |`$$('..some-css-class')`    |
| Select element by ID                     |`element(by.css('#some-css-id'))`              |`$('#some-css-id')`        |
| Select element inside a element with some class name |`element(by.css('some-css')).element(by.css('tag-within-css'))`  | `$('some-css').$('tag-within-css’)`      |
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

For more details please visit [ webdriverio ](https://webdriver.io/docs/gettingstarted) official documentation page.

## Points to note while migration

1. The basic utility files i.e. forms.js, waitFor.js, action. zjs, general.js, user.js will already be migrated for the ease of contributors.

2. For more information on how to add new tests or modify the existing tests please refer to [Write E2E tests](WebdriverIO.md#run-e2e-tests) section.

## Some example cases

1. Protractor

  ```js
  var clear = async function(inputName, inputElement) {
    await click(inputName, inputElement);
    await inputElement.clear();
  };

  var click = async function(elementName, clickableElement, elementIsMasked) {
    await waitFor.visibilityOf(
      clickableElement, `${elementName} is not visible.`);
    await waitFor.elementToBeClickable(
      clickableElement, `${elementName} is not clickable.`);
    if (elementIsMasked) {
      await browser.executeScript(
        'arguments[0].click()', await clickableElement.getWebElement());
    } else {
      await clickableElement.click();
    }
  };
  ```

* WebdriverIO

  ```js
  var clear = async function(inputName, inputElement) {
    await click(inputName, inputElement);
    await inputElement.clearValue();
  };
  
  var click = async function(elementName, clickableElement, elementIsMasked) {
    await waitFor.visibilityOf(
      clickableElement, `${elementName} is not visible.`);
    await waitFor.elementToBeClickable(
      clickableElement, `${elementName} is not clickable.`);
    if (elementIsMasked) {
      await browser.execute(
        'arguments[0].click()',
        await browser.findElement('css selector', clickableElement));
    } else {
      await clickableElement.click();
    }
  };
  ```

2. Protractor

  ```js
  var clear = async function(inputName, inputElement) {
    await click(inputName, inputElement);
    await inputElement.clear();
  };
  
  var click = async function(elementName, clickableElement, elementIsMasked) {
    await waitFor.visibilityOf(
      clickableElement, `${elementName} is not visible.`);
    await waitFor.elementToBeClickable(
      clickableElement, `${elementName} is not clickable.`);
    if (elementIsMasked) {
      await browser.executeScript(
        'arguments[0].click()', await clickableElement.getWebElement());
    } else {
      await clickableElement.click();
    }
  };
  ```

* WebdriverIO

  ```js
  var getText = async function(elementName, element) {
    await waitFor.visibilityOf(
      element, `${elementName} is not visible for getText()`);
    return await element.getText();
  };
  
  var getAttribute = async function(elementName, element, attribute) {
    await waitFor.presenceOf(
      element, `${elementName} is not present for getAttribute(${attribute})`);
    return await element.getAttribute(attribute);
  };
  ```

3. Protractor

  ```js
  var matSelect = async function(selectorName, selectorElement, optionToSelect) {
    await click(selectorName, selectorElement);
    var optionElement = element(
      by.cssContainingText('.mat-option-text', optionToSelect));
    await click(`${optionToSelect} in ${selectorName}`, optionElement);
  };
  
  var select2 = async function(selectorName, selectorElement, optionToSelect) {
    await click(selectorName, selectorElement);
    var select2Results = element(by.css('.select2-results'));
    await waitFor.visibilityOf(
      select2Results, `${selectorName} options are not visible.`);
    var option = select2Results.element(
      by.cssContainingText('li', optionToSelect));
    await click(`${optionToSelect} in ${selectorName}`, option);
  };
  
  var sendKeys = async function(
      inputName, inputElement, keys, clickInputElement = true) {
    if (clickInputElement) {
      await click(inputName, inputElement);
    }
    await inputElement.sendKeys(keys);
  };
  ```

* WebdriverIO

  ```js
  var matSelect = async function(selectorName, selectorElement, optionToSelect) {
    await click(selectorName, selectorElement);
    var optionElement = await $(`.mat-option-text=${optionToSelect}`);
    await click(`${optionToSelect} in ${selectorName}`, optionElement);
  };
  
  var select2 = async function(selectorName, selectorElement, optionToSelect) {
    await click(selectorName, selectorElement);
    var select2Results = await $('.select2-results');
    await waitFor.visibilityOf(
      select2Results, `${selectorName} options are not visible.`);
    var option = await $(`li=${optionToSelect}`);
    await click(`${optionToSelect} in ${selectorName}`, option);
  };
  
  var sendKeys = async function(
      inputName, inputElement, keys, clickInputElement = true) {
    if (clickInputElement) {
      await click(inputName, inputElement);
    }
    await inputElement.setValue(keys);
  };
  ```
