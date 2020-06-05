# Using Async-Await with Protractor Tests

## Introduction to Async-Await

Without async-await, end-to-end tests are written like this:

```js
// ...
var myButton = element(by.css('protractor-test-my-button'));
var myElem = element(by.css('protractor-test-my-element'));
// ...

describe('my test page', function() {
  it('should click the button and go to the next page', function() {
    browser.get('/myPage');
    waitFor.elementToBeVisible(myButton, 'button not visible');
    myButton.click();
    waitFor.elementToBeVisible(myElem, 'element not visible');
    expect(elem.getText()).toEqual('hi');
  });
});
```

Many of these actions, like `waitFor` and `.click()` happen asynchronously, but Protractor's control flow figures out what order to run everything in so we can write code that looks synchronous. In the async-await world, we ditch the control flow and instead have code like this:

```js
// ...
var myButton = element(by.css('protractor-test-my-button'));
var myElem = element(by.css('protractor-test-my-element'));
// ...

describe('my test page', function() {
  it('should click the button and go to the next page', async function() {
    await browser.get('/myPage');
    await waitFor.elementToBeVisible(myButton, 'button not visible');
    await mayButton.click();
    await waitFor.elementToBeVisible(myElem, 'element not visible');
    var expectedText = 'hi';
    expect(await elem.getText()).toEqual(expectedText);
  });
});
```

Notice that every asynchronous action is prefixed immediately by `await`, and functions that contain `await`s are prefixed by the `async` keyword. Some actions though, like assigning `'hi'` to `expectedText`, happen synchronously, so we don't need an `await`. If we had though, that would be fine. If the expression after `await` doesn't evaluate to a promise, `await` will immediately return the evaluated expression, so the code runs as if the `await` weren't even there.

For more information, see [Protractor's documentation on async-await](https://github.com/angular/protractor/blob/master/docs/async-await.md).

### Async-Await and Control Flow

Unfortunately async-await is fundamentally incompatible with Protractor's control flow (see [this GitHub issue](https://github.com/SeleniumHQ/selenium/issues/3037)). To use async-await with Protractor, we have to disable control flow by adding `SELENIUM_PROMISE_MANAGER: false,` to the protractor configuration file at [`core/tests/protractor.conf.js`](https://github.com/oppia/oppia/tree/develop/core/tests/protractor.conf.js). This is why we had to do a single migration of all the e2e tests at once in [#9267](https://github.com/oppia/oppia/pull/9267/).

### Promise Rejections

Protractor's control flow causes tests to fail when `browser.wait(...)` calls time out, which is exactly what we want to happen. However when we migrated to async-await, we discovered that these timeouts were raising warnings but not crashing the test. To fix this, we added the `--unhandled-rejections=strict` argument when running protractor (see [`scripts/run_e2e_tests.py `](https://github.com/oppia/oppia/tree/develop/scripts/run_e2e_tests.py)).

## Migrating Common Patterns

Simple Patterns

* Getting a URL
  ```js
  await browser.get('someURL');
  ```
* .then() functions
  ```js
  someAsynchronousFunction().then(function(output) {
    return // doing something with output
  });
  ```
  can be written instead as
  ```js
  var output = await someAsynchronousFunction();
  await // do something with "output"
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

Trickier Patterns

* `forEach` does not work for async-await. Use a `for ... of` loop instead if you want to operate in sequence, or use `map()` to operate in parallel. See [this stackoverflow post](https://stackoverflow.com/a/37576787) for examples.
* `filter` can be problematic. Consider re-writing as a `for` loop instead.
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

If you aren't sure whether a function is asynchronous, check what it returns. Anything that returns a promise needs to be `await`ed.

## Debugging Migrated Tests

* Check for a missing `await`. This problem probably won't give you very helpful error messages, so carefully read the code and comment out blocks to isolate the problem.
* Empty lists don't have a `.first()` method (or a `.last()`), so if you have a pattern like this:
  ```js
  var elems = await element.all(by.css('.protractor-test-elem'));
  await waitFor.visibilityOf(elems.first(), 'elem not visible');
  ```
  and `elems` matches no elements, you'll get a `elems.first is not a function` error.
* Make sure you add `async` and `await` in the `afterAll` blocks if they check for console errors (they all should). If you don't the test might pass even though errors are appearing in the console log.
* Sometimes we see this error:
  ```
  Failed: java.net.SocketException: Connection reset
  ```
  We're not sure what causes it, though. Please let us know if you find out!
* If you see an error like this:
  ```
  Expected $.length = 2 to equal 0.

      Expected $[0] = Entry({ level: SEVERE, message: 'http://localhost:9001/third_party/static/angularjs-1.7.9/angular.min.js 126:302 Error: Possibly unhandled rejection: null
  ...
          timestamp: 1590690168677, type: '' }) to equal undefined.
  ```
  Then this error is likely a console error that is being detected by the `checkForConsoleErrors` call in the `afterAll` block. You can check the stack trace to confirm. One potential cause is that the test is clicking outside of an open modal. You may need to add some `waitFor`s to make sure the modal closes before you click.