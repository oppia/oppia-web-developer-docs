# Migrating to Async-Await

We are migrating all of the end-to-end tests to use async-await instead of Protractor's native control flow. This should help improve stability since async-await is a native Javascript feature and better supported. It is also necessitated by the removal of control flow management from the latest version of Protractor.

We have a lot of code to migrate, and we have to migrate it all at once because async-await is incompatible with Protractor's control flow. We're trying to get this done as quickly as possible before more changes are pushed to the end-to-end tests, so **we need your help!**

## Instructions for Helping with Migration

The "Migrate by File" instructions are for contributors who:

* Cannot work as intensively on the migration (< 1 hour a day), or
* Have limited experience working on the end-to-end tests

If you are more experienced and can spare more time, please see "Migrate by Suite" below.

Regardless of which instructions you follow, start by reaching out to [@U8NWXD](https://github.com/U8NWXD) at cs.temporary@icloud.com to get edit privileges for the branch we are working on.

### Migrate by File

* Read "Introduction to Async-Await"
* Read "Migrating Common Patterns"
* Claim an available file from the PR [#9267](https://github.com/oppia/oppia/pull/9267) under `protractor_utils/`
    * Like with starter issues, we claim files by adding our usernames to the end
* Clone the branch from the PR. If you already cloned the branch, update from the remote branch. **Pull in remote changes daily if not hourly!**
    * With so many people working on one branch, there's a lot of potential for merge conflicts. Keep this to a minimum by pulling in remote changes early and often.
* Migrate the file
* **Create a single commit with your changes** and push it to the PR branch
    * This PR is going to be a huge diff, and it will help us review the changes if every file is migrated in its own commit.
* Check the box next to your claimed file.
* You're done! Thanks for helping us do this migration. Please take up another file and repeat!

### Migrate by Suite

* Read "Introduction to Async-Await"
* Read "Migrating Common Patterns"
* Read "Debugging Migrated Tests"
* Claim an available file from the PR [#9267](https://github.com/oppia/oppia/pull/9267) under `protractor_desktop/`
    * Like with starter issues, we claim files by adding our usernames to the end
* Clone the branch from the PR. If you already cloned the branch, update from the remote branch. **Pull in remote changes daily if not hourly!**
    * With so many people working on one branch, there's a lot of potential for merge conflicts. Keep this to a minimum by pulling in remote changes early and often.
* Migrate the file and all of its dependencies by working through the file line-by-line. Each time you find a call to another file, migrate that function in the other file and all of its dependencies recursively. By the time you finish, you should have a fully migrated suite that runs and passes consistently.
* When you are debugging your migrated code, add to the list of debugging tips below to help future contributors.
* **Commit your changes, keeping one commit per file or group of files if possible,** and push it to the PR branch
    * This PR is going to be a huge diff, and it will help us review the changes if every file is migrated in its own commit. In this case you might only be migrating parts of files, so you may need to break this rule. Try and keep your commit history easy to understand though.
* Check the box next to your claimed file.
* You're done! Thanks for helping us do this migration. Please take up another suite and repeat!

## Introduction to Async-Await

You're probably used to seeing end-to-end tests written like this:

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

## Migrating Common Patterns

Simple Patterns

* Getting a URL
  ```js
  await browser.get('someURL');
  ```
* .then() functions
  ```js
  someAsynchronousFunction().then(async function(output) {
    return await // doing something with output
  });
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

Trickier Patterns

* `forEach` does not work for async-await. Use a `for ... of` loop instead if you want to operate in sequence, or use `map()` to operate in parallel. See [this stackoverflow post](https://stackoverflow.com/a/37576787) for examples.
* `map()` returns a list of promises, but `await` will only wait if the expression it is provided evaluates to a single promise. To wait until all of the `map()` operations are complete, use `Promise.all` like this:
  ```js
  await Promise.all(myList.map(async function(elem) {
    await elem.click();
  }));
  ```
* When multiple elements might match a locator, we often use `element.all` to get an [`ElementArrayFinder`](https://www.protractortest.org/#/api?view=ElementArrayFinder). This object can usually be used just like a list, but it appears that with async-await, we can only use the functions it defines. In particular:
    * Use `elems.count()` instead of `elems.length` to get the length
    * Use `elems.get(i)` instead of `elems[i]`. `elems.first(i)` and `elems.last(i)` work too.

  Calling these functions is asynchronous, so you need to `await` them. You do *not* need to `await` the `element.all` call itself (we think).

## Debugging Migrated Tests

* Check for a missing `await`. This problem probably won't give you very helpful error messages, so carefully read the code and comment out blocks to isolate the problem.
* Empty lists don't have a `.first()` method (or a `.last()`), so if you have a pattern like this:
  ```js
  var elems = await element.all(by.css('.protractor-test-elem'));
  await waitFor.visibilityOf(elems.first(), 'elem not visible');
  ```
  and `elems` matches no elements, you'll get a `elems.first is not a function` error.