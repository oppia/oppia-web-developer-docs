## Overview

Currently, Oppia E2E tests are in a hybrid state where we have both WebdriverIO and Protractor test suites. The project **Migrate away from Protractor** aims to migrate all the existing E2E tests to WebdriverIO.

This guide is to help contributors write/modify E2E tests in webdriverIO during the hybrid state.

## Selectors

The `$` command is a short way to call the findElement command in order to fetch a single element on the page

| Name                                     | Protractor                               |WebdriverIO           |
| -----------------------------------------| -----------------------------------------|----------------------|
| By class name                            |`element(by.css('.className'))`           |`$('.className')`     |
| Element containing certain string Text   |`element(by.cssContainingText(tag, text))`|`$('tag=text')`       |
| Multiple Elements                        |`element.all(by.css('.className'))`       |`$$('.className')`    |
| By ID                                    |`element(by.css('#idName'))`              |`$('#idName')`        |
| Chain Selectors                          |`element(by.css('some-css')).element(by.css('tag-within-css'))`  | `$('some-css').$('tag-within-css’)`      |
| Selecting element one by one in loop     |`element.get(i)`                          |`$$(selector)[i]`     |

There is no proper substitute available for the command `element.getWebElement()` in webdriverIO but we can use `browser.findElement()` as a substitute for this.

## Actions

| Actions                                  | Protractor                               |WebdriverIO            |
| -----------------------------------------| -----------------------------------------|-----------------------|
| Click on the element                     |`element.click()`                         |`$(selector).click()`  |
| Get the text content from a DOM-element  |`element.getText())`                      |`$(selector).getText()`|
| Navigate to the given destination        |`browser.get(url)`                        |`browser.url(url)`     |
| Get the url of the currently opened website.|`browser.getCurrentUrl()`              |`browser.getUrl()`     |
| Get an attribute from a DOM-element based on the attribute name.|`element.getAttribute(attributeName)`|`$(selector).getAttribute(attributeName)`|
| Wait until a given condition is fulfilled.|`browser.wait(condition, time, optional_msg)`|`browser.waitUntil(condition, { timeout, timeoutMsg, interval })`|
| Send a sequence of keystrokes to the active element|`element.sendKeys(keys)` |`browser.keys(value`     |
| Selected DOM-Element is clickable, visible, and exists.|`until.elementToBeClickable(element)` |`$(selector).isClickable()`|
|`Get the value of a <textarea>, <select> or text <input> found by given selector`|`element.getText()` |`$(selector).getValue()`|
|`Clear a <textarea> or text <input> element’s value`   |`element.clear()` |   `$(selector).clearValue()`  |

For more details please visit [ webdriverio ](https://webdriver.io/docs/gettingstarted) official documenation page.

## Points to Note While Migration

1. `expect` calls must be prefixed with an `await`.

Example of **incorrect** code for this rule:

```js
it('should visit the Get started page', async() => {
    await getStartedPage.get();
    expect(await $(
      '.webdribverio-test-get-started-page').isExisting()).toBeTrue();
});
```

Example of **correct** code for this rule:

```js
it('should visit the Get started page', async() => {
    await getStartedPage.get();
    await expect(await $(
      '.webdribverio-test-get-started-page').isExisting()).toBeTrue();
});
```

2. The basic utility files i.e forms.js, waitFor.js, action.js, general.js, user.js will already be migrated for the ease of contributors.

3. For more information on how to add new tests or modify the existing tests please refer to Write E2E tests section.
