## Table of Contents

* [Introduction](#introduction)
  * [Goal](#goal)
  * [Unit tests](#unit-tests)
  * [Code coverage](#code-coverage)
* [Helpful resources](#helpful-resources)
* [Run frontend tests](#run-frontend-tests)
  * [Coverage reports](#coverage-reports)
    * [Reading a coverage report](#reading-a-coverage-report)
    * [Ensuring that coverage is maintained](#ensuring-that-coverage-is-maintained)
* [Write frontend tests](#write-frontend-tests)
  * [Unit test structure](#unit-test-structure)
    * [`describe`](#describe)
    * [`beforeEach`](#beforeeach)
    * [`it`](#it)
    * [`afterEach`](#aftereach)
    * [`afterAll`](#afterall)
    * [`expect`](#expect)
    * [`tick`](#tick)
    * [`flush`](#flush)
  * [Good practices](#good-practices)
    * [Tests should work in any order](#tests-should-work-in-any-order)
    * [Do not test private methods/properties](#do-not-test-private-methodsproperties)
    * [Worry about behavior and not about coverage](#worry-about-behavior-and-not-about-coverage)
    * [Name variables clearly](#name-variables-clearly)
    * [Name tests clearly](#name-tests-clearly)
    * [Check return values from the code being tested](#check-return-values-from-the-code-being-tested)
    * [Test the interface, not the implementation](#test-the-interface-not-the-implementation)
    * [Keep tests clean and clear](#keep-tests-clean-and-clear)
    * [Similar tests should have similar checks](#similar-tests-should-have-similar-checks)
    * [Validate external side-effects](#validate-external-side-effects)
* [General tips](#general-tips)
  * [Debugging](#debugging)
  * [Spy utilities](#spy-utilities)
    * [Spying on third-party libraries](#spying-on-third-party-libraries)
    * [Spying on the same method/property more than one time in the same scope](#spying-on-the-same-methodproperty-more-than-one-time-in-the-same-scope)
    * [Spies that change global values](#spies-that-change-global-values)
    * [Handling window events and reloads](#handling-window-events-and-reloads)
      * [When window calls reload](#when-window-calls-reload)
      * [Using the same object reference in both file and spec file](#using-the-same-object-reference-in-both-file-and-spec-file)
  * [Handling dates](#handling-dates)
  * [Handling asynchronous code](#handling-asynchronous-code)
    * [Making HTTP calls](#making-http-calls)
      * [Setting up CsrfToken](#setting-up-csrftoken)
      * [HTTP calls in AngularJS](#http-calls-in-angularjs)
      * [HTTP calls in Angular 2+](#http-calls-in-angular-2)
    * [Using `done` and `done.fail` from Jasmine](#using-done-and-donefail-from-jasmine)
    * [Handling `$timeout` correctly](#handling-timeout-correctly)
    * [Mocking with `$q` API in AngularJS](#mocking-with-q-api-in-angularjs)
  * [When upgraded services should be imported in the test file](#when-upgraded-services-should-be-imported-in-the-test-file)
  * [`beforeEach` calls in AngularJS](#beforeeach-calls-in-angularjs)
  * [How to handle common errors](#how-to-handle-common-errors)
* [Testing services](#testing-services)
  * [Testing AngularJS services](#testing-angularjs-services)
  * [Testing Angular 2+ services](#testing-angular-2-services)
* [Testing controllers](#testing-controllers)
* [Testing directives and components](#testing-directives-and-components)
  * [Testing AngularJS directives and components](#testing-angularjs-directives-and-components)
  * [Testing Angular2+ directives and components](#testing-angular2-directives-and-components)
* [Contacts](#contacts)

## Introduction

### Goal

Our goal is for every file with frontend code to be thoroughly tested by its associated test file. For example, `user.service.ts` should be comprehensively tested by `user.service.spec.ts`. By "comprehensively," we mean that the tests should cover all possible ways the code in `user.service.ts` might be used. It's especially important for test to cover both happy (expected) and unhappy (unexpected) usages. [Here](https://github.com/oppia/oppia/blob/ae649aa08f/core/templates/services/questions-list.service.spec.ts#L19) is a good example of a comprehensive set of test cases.

### Unit tests

A unit test checks the behavior of small pieces of code, which are called units. Often, the unit is a funtion, in which case the behavior being tested would be the function's outputs given some inputs.

A unit test should depend only on the "external" behavior to be tested, not the specific implementation of the function. This means that the behavior of other units is out of scope.
[Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/skill/RubricObjectFactorySpec.ts#L28-L41) is a simple unit test that demonstrates these points.

### Code coverage

We get a rough idea of how comprehensive our tests are by measuring _code coverage_, which is the fraction of testable lines of code that were executed when the tests were run. For example, consider the following pseudocode:

```text
1 # Compute the absolute value of a number
2 function absoluteValue(number) {
3   if number <= 0 {
4     return -number
5   } else {
6     return number
7   }
8 }
```

Now consider the following sets of test cases:

* `absoluteValue(1)` and `absoluteValue(5)`: These test cases are not comprehensive because they only test positive numbers. Code coverage is also not 100% because line 4 is never executed.
* `absoluteValue(0)` and `absoluteValue(1)`: These test cases are not comprehensive because they do not test negative numbers, and it's important for an absolute value function to correctly handle negative inputs. However, the code coverage is 100% because both blocks of the `if` statement are executed.
* `absoluteValue(-1)`, `absoluteValue(0)`, and `absoluteValue(1)`: These test cases are comprehensive, and code coverage is 100%. Note that even though line 1 doesn't execute, coverage is 100% because line 1 is not executable.

This example illustrates something very important about code coverage: **Code coverage less than 100% implies that the tests are not comprehensive, but code coverage of 100% does not imply that tests are comprehensive.** Therefore, while code coverage is a useful tool, you should primarily think about whether your tests cover all the possible behaviors of the code being tested. In other words, you should have a behavior-first perspective. Don't just think about which lines are covered.

When we achieve our goal, then for every frontend code file, executing only its associated test file should result in 100% coverage of the code file. Note that to execute only a single test file, you can change `describe`s in that file to `fdescribe`s.

## Helpful resources

This list contains some resources that might help you while writing unit tests:
- [Jasmine documentation](https://jasmine.github.io/api/edge/global)
- [Karma](https://karma-runner.github.io/)
- [Angular 2+ testing](https://angular.io/guide/testing)
- [AngularJS testing](https://docs.angularjs.org/guide/unit-testing)

## Run frontend tests

Running the frontend tests is as simple as running this command:

Docker:
```console
make run_tests.frontend
```

Python:
```console
python -m scripts.run_frontend_tests
```

These tests also run whenever you push changes to the frontend code.

**Tips for speeding things up**:
- When running the tests locally, you can add `--skip_install` (included by default for the Docker command) after the first run to skip installing dependencies (and speed up the test).
- The file `combined-tests.spec.ts` has a require statement with a regex that matches and compiles all the specs files (irrespective of whether we want to run the spec files or not). To debug a specific unit test, you can replace the regex with the name of the specific file (make sure to escape all the hyphens (-), dots (.) and any other reserved regex characters). This will make the test run faster.

**Note: Typically, these tests take around 2.5 to 5 minutes (exclusive of the time taken for setting up ChromeHeadless) to run, assuming the machine has sufficient resources. If the total time taken is significantly longer than this, it may indicate an issue with the testing environment. In case such an issue is noticed or observed, please raise it on our [issue tracker](https://github.com/oppia/oppia/issues).**

### Coverage reports

Coverage reports are an indispensable tool when working with unit tests. They can show you which lines are being tested and which are not. Use these reports to help you write better tests and to ensure that all the files and functionality are totally covered by the tests you write.

Whenever you run the frontend tests, a coverage report will be generated at the `oppia/../karma_coverage_reports/index.html`.  The report will look like this:

![Karma Coverage reports](https://user-images.githubusercontent.com/34922478/80640321-9e30f900-8a39-11ea-8b8e-98dab4a3d48b.png)

#### Reading a coverage report

When writing tests, the goal is to completely cover the file. In order to do that, you need to understand what the coverage report is telling you. Basically, the report tells you which line is being hit, partially hit, or missed:

* **Hit**: the line was executed by the test suite.
* **Partially hit**: the line was partially executed by the test suite. There’s another possibility where this line is missed.
* **Missed**: the line wasn’t executed by the test suite.

More than just reporting the “covered” state of each line, the coverage report also reports something called **branch coverage**. A branch refers to a branch in the program (if/else statements, loops, and so on). To be fully covered, all the file’s branches need to be tested. The Karma coverage report uses symbols (with letter I - for if - and E - for else) to refer to if/else statements branches. It’s important to note that these symbols will appear even if the branch is being covered, so please **ignore** these symbols and pay attention to only the line coverage information (as you see above). Here’s an example:

![Example for branch coverage symbols](https://user-images.githubusercontent.com/34922478/80809691-9340aa80-8b98-11ea-9a22-6fd21171db85.png)

#### Ensuring that coverage is maintained

In order to make the coverage stable, by default we require that every frontend file is fully covered. Since we are still increasing frontend coverage, there are some exceptions to this rule. Files that are not fully covered are listed in `scripts/check_frontend_coverage.py`.

If you pass the `--check_coverage` flag when running the tests, then the tests will check whether all expected files are fully covered. The output looks like this:

![Example of output by tracking the changes in the frontend unit tests](https://user-images.githubusercontent.com/34922478/80845732-8182f580-8be0-11ea-9c47-0f46f1f44c2f.png)

## Write frontend tests

### Unit test structure

A unit test is made of functions that configure the test environment, make assertions, and separate the different contexts of each situation. There are some test functions that are used across the codebase:

#### `describe`

The `describe` function has a string parameter which should contain the name of the component being tested or (when nested within another `describe` function) should describe the conditions imposed on the specific context pertaining to the tests in that `describe` block. Here are some examples:

* An outer `describe` function:

  ```js
  describe('Component Name', function() {
    ...
  });
  ```

* Two `describe` functions nested inside another `describe` function:

  ```js
  describe('Component Name', function() {
    describe('when it is available', function() {...});

    describe('when it is not available', function() {...});
  });

  ```

Check out [a real example](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/creator-dashboard-page/suggestion-modal-for-creator-view/suggestion-modal-for-creator-view.controller.spec.ts#L24-L310) in the codebase to see how to use `describe` properly.

The `describe` function also has some variants to help you. Use these variants only on your local machine for testing.

* **fdescribe**: This is used when you want to run only the test suite marked as `fdescribe`.

* **xdescribe**: This is used when you want to run all test suites except the one marked with `xdescribe`.

#### `beforeEach`

The `beforeEach` function is used to set up essential configurations and variables before each test runs. This function is mostly used for three things:

* Injecting the modules to be tested or to be used as helpers inside the test file. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/splash-page/splash-page.controller.spec.ts#L37-L49) is an example.

* Mocking the unit test’s external dependencies (only on AngularJS files):

  ```js
  beforeEach(angular.mock.module(function($provide) {
    $provide.value('ExplorationStatesService', {
      getState: () => ({ interaction: null })
    });
  }));
  ```

* Providing Angular2+ services in downgrade files when the AngularJS service being tested uses any upgraded (Angular2+) service as a dependency. For example, assume that the test requires MyExampleService which is an Angular2+ service:

  ```js
  import { TestBed } from '@angular/core/testing';
  import { MyExampleService } from 'services/my-example.service';
  ...
    beforeEach(() => {
      TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    });
  });
  beforeEach(angular.mock.module('oppia', function($provide) {
    $provide.value('MyExampleService',
      TestBed.get(MyExampleService));
  }));
  ```

#### `it`

The `it` function is where the test happens. Like the `describe` function, its first parameter is a string which should determine the action to be tested and the expected outcome of the tests. The string should have a clear description of what is going to be tested. Also, **the string must start with "should"**.

All possible code paths in the function should be tested. See this [example in codebase](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/search.service.spec.ts#L82-L451) and notice how the test names give you an idea of what is expected.

Like `describe`, the `it` function has the variants `fit` and `xit` and they can be used in the same way as `fdescribe` and `xdescribe`.

#### `afterEach`

The `afterEach` function runs after each test, and it is not used often. It’s mostly used when we are handling async features such as HTTP and timeout calls (both in AngularJS and Angular 2+). [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/domain/exploration/read-only-exploration-backend-api.service.spec.ts#L100-L103)'s an example to handle HTTP mocks in AngularJS and [here](https://github.com/oppia/oppia/blob/ae649aa08f/core/templates/domain/classroom/classroom-backend-api.service.spec.ts#L72-L74)'s an example of doing the same in Angular 2+.

#### `afterAll`

The `afterAll` function runs after all the tests have finished, but it is almost never used in the codebase. There is a specific case which it might be very helpful: when a global variable needs to be reassigned during the tests, you need to reset it to the default value after all the assertions are finished. Check an example of this case [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/site-analytics.service.spec.ts#L40-L42).

#### `expect`

The `expect` function is used to assert a condition in the test. You can check all its methods in the [Jasmine documentation](https://jasmine.github.io/api/edge/matchers.html). [Here's](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/services/graph-data.service.spec.ts#L92-L112) a good example of how to use it correctly.

#### `tick`

We call [the tick function](https://angular.io/api/core/testing/tick) when there are pending asynchronous activities we want to complete. The tick() function blocks execution and simulates the passage of time until all pending asynchronous activities complete. Asynchronous activities such as timeouts and promises will be handled using the tick() function.
##### Note: This function will only work if the tests are running in the fakeAsync() block.

#### `flush`

While testing asynchronous functions, we can use [the flush function](https://angular.io/api/core/testing/flush) instead of awaiting them individually. The difference between flushMicrotasks and flush is that the former only processes the pending microtasks ( promise callbacks), but not the (macro) tasks ( scheduled callbacks), while flush processes both.
##### Note: This function will only work if the tests are running in the fakeAsync() block.

### Good practices

#### Tests should work in any order

It is possible to write frontend tests that only pass when run in a particular order. Here's an example:

```js
describe('oppia', () => {
  var test = 2;

  it('should do something', () => {
    test = 3;
  });

  it('should do something else', () => {
    expect(test).toBe(2);
  });
});
```

This test will pass when `should do something else` runs before `should do something`, but not when the tests run in the opposite order. This is bad! Since Karma runs tests in a non-deterministic order, you should never assume that tests will run in a particular order.

#### Do not test private methods/properties

Private methods/properties should only be accessed just by the class or function where they are defined. Their names start with `_`. It's not a good practice to test private methods/properties because they should not be accessed from the outside. Instead, you should only test public methods and their output. For example:

* Bad:

  ```js
  it('should get generic name', function() {
    var name = component._name;
    expect(name).toBe('foo');
  });
  ```

* Good:

  ```js
  it('should get generic name', function() {
    var name = component.getName();
    expect(name).toBe('foo');
  });
  ```

#### Worry about behavior and not about coverage

Make sure your tests check the file's behavior, not just that they get to 100% coverage. Unit tests are about testing the expected output, not the internal implementation. For example:

* Bad:

  ```js
  it('should get items from api', function() {
    var consoleSpy = spyOn(console, 'log').and.callThrough();
    component.fetchApi();
    expect(consoleSpy).haveBeenCalledWith('fetched!);
  });
  ```

* Good:

  ```js
  it('should get items from api', function() {
    var MAX_ITEMS_TO_FETCH = 10;
    component.fetchApi();
    expect(component.itemsFetched).toEqual(10);
  });
  ```

#### Name variables clearly

* Expected variables must be named so that it's clear that they store expected data.
  * **Example**: ‘expectedAdjacencyList’, ‘expectedNodeData’.
* Variables storing return values must have names that suggest that they have been returned.
  * **Example**: ‘returnedNodeData’, ‘returnedGraphHeight’.
* For variables that have a unit, mention the unit in the variable name.
  * **Example**: ‘graphHeightInPixels’, ‘graphHeightInCm’

#### Name tests clearly

Test description should clearly state what the test is testing. Generally, follow the format `should do X if Y happens`. For example:

* **Good test name** - ‘it should not return indentation level greater than MAX_INDENTATION_LEVEL’
* **Bad test name** - ‘it should return indentation levels’

Also, write the test descriptions in a way such that they reflect the user's perspective rather than including implementation details.

#### Check return values from the code being tested

Do not just call the code being tested; check that the thing returned is correct. ([example](https://github.com/oppia/oppia/blob/3fa63711440b4320350c48dd63ffd8b163d07143/core/templates/components/graph-services/graph-layout.service.spec.ts#L528))

#### Test the interface, not the implementation

See [this link](https://eng.libretexts.org/Bookshelves/Computer_Science/Book%3A_Object-Oriented_Reengineering_Patterns_(Demeyer_Ducasse_and_Nierstrasz)/06%3A_Tests__Your_Life_Insurance/6.05%3A_Test_the_Interface_Not_the_Implementation) for a rough outline of the concept. If the code that’s being tested changes, but the interface remains stable, your tests should still continue to pass.

* Here, "interface" does not refer to the user interface. It refers to the part of the directive/service/component that can be accessed externally through public functions. So, services have an interface too (i.e. the public functions that they expose to other components/services). You basically want to check whether inputs to those functions result in the correct output.

* Where possible, try to check the inputs and the outputs of the code being tested rather than just whether a particular method has been called. That's because the latter tends to be directly testing a specific implementation. The exception is when the method being called is a **requirement** of the test, e.g. if we need to verify that a third-party API which we treat as a black box is called — but that's fairly rare.

  * **Example**: To test that all the subscriptions in a component have been unsubscribed successfully, you can check the .closed flag which indicates whether the subscription has already been unsubscribed:

    ```js
      it('should unsubscribe when component is destroyed', function() {
        spyOn(ctrl.directiveSubscriptions, 'unsubscribe').and.callThrough();

        expect(ctrl.directiveSubscriptions.closed).toBe(false);

        ctrl.$onDestroy();

        expect(ctrl.directiveSubscriptions.unsubscribe).toHaveBeenCalled();
        expect(ctrl.directiveSubscriptions.closed).toBe(true);
      });
    ```

#### Keep tests clean and clear

* Keep the body of the test clean and clear. Having too many big blocks of data obscures what we are trying to check. In a case where big blocks of data are necessary to test the code, add comments to explain (as [here](https://github.com/oppia/oppia/blob/3fa63711440b4320350c48dd63ffd8b163d07143/core/templates/components/graph-services/graph-layout.service.spec.ts#L772-L784)).

* Do not include unnecessary data in the test.
  * **Example** : if you are testing that the X property of a dict is modified by a function, then only check the X property. Do not include other properties in the expected variable.

* Leave comments to explain the steps in the test whenever things get complicated. This helps the reader understand what your test does. Ideally, a reader should be able to understand the tests without reading the code file.

* Add visual explanations if possible ([example](https://github.com/oppia/oppia/blob/1013c9a33af0179ad394088c08ef18ed2f03bd64/core/templates/components/graph-services/graph-layout.service.spec.ts#L28-L57)).

* For all hardcoded values, explain where the values come from in comments.

* Write the expectations in order, so that each test has a coherent story. That makes the test easier to follow.

#### Similar tests should have similar checks

For example, if in a test you check that a spy was called when a certain condition was satisfied, then also check that the spy was not called when that condition was not satisfied.

#### Validate external side-effects

An external side-effect is an effect that we expect from running the function but that isn't part of the outputs. For example, consider this pseudocode:

```text
function login(username, password) {
  valid = whether the username and password are valid
  if valid {
    setLoginCookie(username)
    return True
  }
  return False
}
```

Here, the call to `setLoginCookie()` is an external side-effect. In our unit tests, it's not enough to check that the function's return value is correct; we also need to check that `setLoginCookie()` is called (and not called) correctly.

## General tips

### Debugging

See our [[guide to debugging frontend tests|Debug-frontend-tests]] for debugging tips.

### Spy utilities

One of the main features of Jasmine is allowing you to spy on a method or property of an object. This is helpful in some cases for seeing what is going on:

* You can spy on an object's properties (using the `spyOnProperty` method). [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/contextual/device-info.service.spec.ts#L48-L55)'s an example.

* You can mock a property value or a method return. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/feedback-tab/services/thread-data.service.spec.ts#L147)'s an example.

* You can provide fake implementations that will be called when a method is executed. This is commonly used when mocking AngularJS promises with `$defer`. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/email-dashboard-pages/email-dashboard-page.controller.spec.ts#L121-L133)'s an example.

* You can spy on a method to check whether that method is being called when the spec runs. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/schema-default-value.service.spec.ts#L109-L118)'s an example.

#### Spying on third-party libraries

Also, the spy can be used when mocking third-party libraries, like JQuery, mostly when doing ajax calls. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/assets-backend-api.service.spec.ts#L274-L292)'s a good example when mocking JQuery ajax calls.

#### Spying on the same method/property more than one time in the same scope

It is impossible to spy twice on the same method or property in the same [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope). For instance, the code below would throw an error:

```js
spyOn('should throw an error when spying twice', function() {
  spyOn(console, 'warn').and.stub();
  spyOn(console, 'warn').and.stub();
});
```

However, there are some situations where you need to change a value or a method’s return value spy in the same spec, for instance by changing the location path in a mock `window` object, or even reseting a mock to call the original code. You can do it by assigning the spy (without calling any method) to a variable. Then you can use this variable to call the spy methods as many times you want. For example, this code won't throw an error:

```js
spyOn('should not throw an error when spying twice', function() {
  var warnSpy = spyOn(console, 'warn');
  warnSpy.and.stub();
  warnSpy.and.stub();
});
```

You can check real examples of this approach [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/landing-pages/topic-landing-page/topic-landing-page.controller.spec.ts#L94-L109) (dealing with window location properties) and [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/about-page/about-page.controller.spec.ts#L72-L89) (resetting spy to original code).

#### Spies that change global values

You must not use spies that are declared by reassigning a **global expression**, like the window object or its properties and methods.

Let's suppose you need to return a custom value from `document.getElementById` but you're facing some problems trying to do it. You may find nice solutions searching over the internet; however, make sure the chosen solution is not changing a global value, like in this [case](https://github.com/oppia/oppia/blob/bc8625cb38aef8f93844954d0b0cb797e1bd753b/core/templates/pages/preferences-page/modal-templates/edit-profile-picture-modal.controller.spec.ts#L51-L52). You should find another approach for the goal, like this [example](https://github.com/oppia/oppia/blob/1f20eda67be9bfb78b5885916ce37ddea7f05183/core/templates/pages/preferences-page/modal-templates/edit-profile-picture-modal.controller.spec.ts#L49-L50).

The problem with the first case is that changing a global value will affect other files that use the expression you've reassigned, making the unit tests error-prone. [Here](https://github.com/oppia/oppia/issues/9660)'s a good example of a bug that appears after using the first case.

#### Handling window events and reloads

Spying on the window object is very common because some native behaviors can cause the tests to fail or make them unpredictable. This happens in two specific cases:

##### When window calls reload

When reload is called in its native form, it will fail the tests. You can fix this by using the Spy `returnValue()` method. Check it out how to mock `reload()` correctly [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/about-page/about-page.controller.spec.ts#L72-L77).

##### Using the same object reference in both file and spec file

In some cases, you might need to share the same window object in the file you’re testing and in the spec file itself, mainly if you’re working on window events. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/about-page/about-page.controller.spec.ts#L24-L29)’s an example of how to do it.

### Handling dates

As Oppia is a worldwide project, testing date methods turns to be very tricky. For example, if you want to get a date from unix time, you can get different dates depending on the timezone of where you live, making the tests unstable. To avoid errors when testing any date method that can change its value depending on timezone, you should mock it to return a fixed date. Check this [example](https://github.com/oppia/oppia/blob/7aa80c49f81270c886818e3dce587715dcebac68/core/templates/pages/exploration-editor-page/feedback-tab/thread-table/thread-table.component.spec.ts#L52-L59).

### Handling asynchronous code

#### Making HTTP calls

All HTTP calls must be mocked since the frontend tests actually run without a backend available. Similarly, any services can also be mocked. We try to keep the usage of such mocks as low as possible since the more mocks there are, the more divergence can arise between the mocks and the underlying code being mocked.

##### Setting up CsrfToken

In order to make HTTP calls in a secure way, it's common that applications have tokens to authenticate the user while they are using the platform. In the codebase, there is a specific service to handle the token, called CsrfTokenService. When mocking HTTP calls, you must mock this service in the test file so the tests won't fail due to lacking a token. Then, you should just copy and paste this piece of code inside a `beforeEach` block (the CsrfService will be a variable with the return of `$injector.get('CsrfTokenService')` -- in AngularJS -- or `TestBed.get(CsrfTokenService)` -- in Angular 2+):

```js
spyOn(CsrfService, 'getTokenAsync').and.callFake(function() {
  var deferred = $q.defer();
  deferred.resolve('sample-csrf-token');
  return deferred.promise;
});
```

##### HTTP calls in AngularJS

[Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/learner_dashboard/learner-playlist.service.spec.ts#L84-L99) is an example which uses `$httpBackend` to mock the backend responses.

To mock a backend call, you need to use the `$httpBackend` dependency. There are two ways to expect an HTTP method (you can use both):

* `$httpBackend.expectMETHODNAME(URL)` - like `expectPOST` or `expectGET` for instance
* `$httpBackend.expect(‘METHOD’, URL)` - You pass the HTTP method as the first argument.

When writing HTTP tests (which are asynchronous) we need to always use the `$httpBackend.flush()` method. This will ensure that the mocked request call will be executed.

##### HTTP calls in Angular 2+

When writing HTTP tests on Angular 2+, use `httpTestingController` with `fakeAsync()` and `flushMicrotasks()`. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/domain/classroom/classroom-backend-api.service.spec.ts#L77-L96)’s a good example to follow.

Just like the AngularJS way to mock HTTP calls, the Angular 2+ has flush functions to return the expected response and execute the mock correctly.

#### Using `done` and `done.fail` from Jasmine

Using `done` and `done.fail` is another way to test asynchronous code in Jasmine. You can use it on promises (HTTP calls and so on) and timers such as `setTimeout`.

There’s a specific case where you should use `done` on mocking HTTP calls: when you want to assert the result of the fulfilled or rejected promise, as you can see [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/assets-backend-api.service.spec.ts#L274-L292). In this piece of code, we need to assert the response variable, and then we call `done` after doing the assertion so Jasmine understands the asynchronous code has been completed. You can use `done.fail` when handling rejected promises.

You can use `done` when using `setTimeout` for specific cases as well, check out this [example](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/teach-page/teach-page.controller.spec.ts#L53-L67).

#### Handling `$timeout` correctly

We use `$timeout` a lot across the codebase. When testing a `$timeout` callback, we used to call another `$timeout` in the unit tests, in order to wait for the original callback to be called. However, this approach was tricky and it was making the tests fail. When testing `$timeout` behavior, you should use [$flushPendingTasks](https://docs.angularjs.org/api/ngMock/service/$flushPendingTasks), which is cleaner and less error-prone than `$timeout`. Here's an example:

**Bad code:**

```js
it('should wait for 10 seconds to call console.log', function() {
  spyOn(console, 'log');
  $timeout(function() {
    expect(console.log).toHaveBeenCalled();
  }, 10);
});
```

**Good code:**

```js
it('should wait for 10 seconds to call console.log', function() {
  spyOn(console, 'log');
  $flushPendingTasks();
  expect(console.log).toHaveBeenCalled();
});
```

#### Mocking with `$q` API in AngularJS

When mocking a promise in AngularJS, you might use the `$q` API. In these cases, you must use `$scope.$apply()` or `$scope.$digest` because they force `$q` promises to be resolved through a Javascript digest. Here are some examples using [$apply](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/email-dashboard-pages/email-dashboard-page.controller.spec.ts#L101-L108) and [$digest](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/services/exploration-states.service.spec.ts#L209-L221).

### When upgraded services should be imported in the test file

One of the active projects in Oppia is the Angular2+ migration. When testing AngularJS files which rely on an Angular2+ dependency, you must use a `beforeEach` call below to import the service. For example, assume that the test requires MyExampleService which is an Angular2+ service.

```js
import { TestBed } from '@angular/core/testing';
import { MyExampleService } from 'services/my-example.service';
...
  beforeEach(() => {
    TestBed.configureTestingModule({
    imports: [HttpClientTestingModule]
  });
});
beforeEach(angular.mock.module('oppia', function($provide) {
  $provide.value('MyExampleService',
    TestBed.get(MyExampleService));
}));
```

If the file you’re testing doesn’t use any upgraded files, you don’t need to use this `beforeEach` call.

### `beforeEach` calls in AngularJS

If you’re testing an AngularJS file that uses an upgraded service, you’ll need to include a `beforeEach` block which mocks all the upgraded services. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/editor-tab/training-panel/training-modal.controller.spec.ts#L35-L48) is an example.

However, you might face the following situation: you need to mock an Angular2+ service by using `$provide.value`. Here’s the problem: if you use `$provide.value` before calling the updated services, your mock will be overwritten by the original code of the service. So, you need to change the order of `beforeEach` calls, as you can see in [this test](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/improvements-tab/services/improvement-suggestion-thread-modal.controller.spec.ts#L36-L51).

### How to handle common errors

* If you see an error like `Error: Trying to get the Angular injector before bootstrapping the corresponding Angular module`, it means you are using a service (directly or indirectly) that is upgraded to Angular.

  * Your test that is written in AngularJS is unable to get that particular service. You can fix this by providing the value of the Angular2+ service using $provide. For example, let us assume that the test requires MyExampleService which is an Angular2+ service. Then you can provide the service like this:

    ```js
    import { TestBed } from '@angular/core/testing';
    import { MyExampleService } from 'services/my-example.service';
    ...
      beforeEach(() => {
        TestBed.configureTestingModule({
        imports: [HttpClientTestingModule]
      });
    });
    beforeEach(angular.mock.module('oppia', function($provide) {
      $provide.value('MyExampleService',
        TestBed.get(MyExampleService));
    }));
    ```

* If you’re working with async on AngularJS and your tests don’t seem to run correctly, make sure you’re using `$apply` or `$digest` in the spec, as in this [example](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/topic-editor-page/services/topic-editor-state.service.spec.ts#L716-L720).

## Testing services

Services are one of the most important features in the codebase. They contain logic that can be used across the codebase multiple times. There are three possible extensions for services:

* `*.service.ts`
* `*Factory.ts`
* `*.factory.ts`
* `*.tokenizer.ts`

As a good first issue, all the services that need to be tested are listed in [issue #4057](https://github.com/oppia/oppia/issues/4057).

### Testing AngularJS services

Use these files that are correctly following the testing patterns for reference:

* [current-interaction.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-player-page/services/current-interaction.service.spec.ts#L39)
* [editable-exploration-backend-api.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/domain/exploration/editable-exploration-backend-api.service.spec.ts#L30)
* [improvement-task.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/improvement-task.service.spec.ts#L29)

### Testing Angular 2+ services

Use these files that are correctly following the testing patterns for reference:

* [exploration-features-backend-api.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/exploration-features-backend-api.service.spec.ts#L26)
* [editability.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/editability.service.spec.ts#L21)
* [exploration-html-formatter.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/exploration-html-formatter.service.spec.ts#L27)

## Testing controllers

Controllers are used often for AngularJS UI Bootstrap library's modals. Here are some files that are correctly being tested and follow the testing patterns for reference:

* [welcome-modal.controller.spec.ts](https://github.com/oppia/oppia/blob/aa288fd246dec2f8a30a1e9f72a77bd97952c132/core/templates/pages/exploration-editor-page/modal-templates/welcome-modal.controller.spec.ts)
* [merge-skill-modal.controller.spec.ts](https://github.com/oppia/oppia/blob/3642a4c21e387493f85c7bb72fe1789d214ffffb/core/templates/components/skill-selector/merge-skill-modal.controller.spec.ts)
* [skill-preview-modal.controller.spec.ts](https://github.com/oppia/oppia/blob/125e4388c665c86cb932dc2391093fa6946a5a83/core/templates/pages/skill-editor-page/editor-tab/skill-preview-modal.controller.spec.ts)
* [improvement-confirmation-modal.controller.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/improvements-tab/services/improvement-confirmation-modal.controller.spec.ts#L19)
* [stewards-landing-page.controller.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/landing-pages/stewards-landing-page/stewards-landing-page.controller.spec.ts#L25)

**Note:** If you intend to create a new modal using `$uibModal.open` method, please be sure to create its controller in a separate file. See [issue #8924](https://github.com/oppia/oppia/issues/8924) for more information.

Also, there are controllers that are not linked to modals. Here is an example:

* [logic-demo-test.controller.spec.ts](https://github.com/oppia/oppia/blob/04570fb22780d9a22d94e33916a1d0e8d17c2a6d/extensions/interactions/LogicProof/static/js/tools/logic-demo-test.controller.spec.ts)

## Testing directives and components

### Testing AngularJS directives and components

> [!NOTE]
> If you're creating a new AngularJS directive, please make sure the value of the restrict `property` is not `E`. If it's an `E`, change the directive to an AngularJS component. You can check out [this PR](https://github.com/oppia/oppia/pull/9850) to learn how to properly make the changes.

Use these AngularJS component files that are correctly following the testing patterns for reference:

* [search-bar.component.spec.ts](https://github.com/oppia/oppia/blob/a9bece78fd45344f5e0e741ab21f8ea0c289a923/core/templates/pages/library-page/search-bar/search-bar.component.spec.ts)
* [preferences-page.component.spec.ts](https://github.com/oppia/oppia/blob/3642a4c21e387493f85c7bb72fe1789d214ffffb/core/templates/pages/preferences-page/preferences-page.component.spec.ts)
* [practice-tab.component.spec.ts](https://github.com/oppia/oppia/blob/fcb44f8cc6e0e00aaa082045cf8b363daa510479/core/templates/pages/topic-viewer-page/practice-tab/practice-tab.component.spec.ts)

Use these AngularJS directive files that are correctly following the testing patterns for reference:

* [value-generator-editor.directive.spec.ts](https://github.com/oppia/oppia/blob/7aa80c49f81270c886818e3dce587715dcebac68/core/templates/pages/exploration-editor-page/param-changes-editor/value-generator-editor.directive.spec.ts)
* [audio-translation-bar.directive.spec.ts](https://github.com/oppia/oppia/blob/4ec7b9cc70e2a255653952450fe44932607755af/core/templates/pages/exploration-editor-page/translation-tab/audio-translation-bar/audio-translation-bar.directive.spec.ts)
* [oppia-visualization-click-hexbins.directive.spec.ts](https://github.com/oppia/oppia/blob/89a809b521af0c2d21b71db5cdc8c644d893a577/extensions/visualizations/oppia-visualization-click-hexbins.directive.spec.ts)

### Testing Angular2+ directives and components

Let us assume that we are writing tests for an Angular2+ component called BannerComponent. The first thing to do is to import all dependencies, we have a boilerplate for that:

```js
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { BannerComponent } from './banner.component';

describe('BannerComponent', () => {
  let component: BannerComponent;
  let fixture: ComponentFixture<BannerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BannerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BannerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeDefined();
  });
});
```

Once this is done, you have the class instance in the variable called `component` and you can continue writing the tests as a class testing.

At the moment, we don't enforce [DOM testing](https://angular.io/guide/testing-components-basics#component-dom-testing). However, as the docs say, the component is not fully tested until we test the DOM too. Eventually we hope to add DOM tests for all our components, however, for now if you are making a PR fixing a bug caused due to incorrect DOM bindings, then add DOM tests for that component. Our coverage checks do not require DOM tests.

Use these Angular2+ component files that are correctly following the testing patterns for reference:

* [donate-page.component.spec.ts](https://github.com/oppia/oppia/blob/327df0c22ec839d4ad4232492749c78443b15fb0/core/templates/pages/donate-page/donate-page.component.spec.ts)
* [teach-page.component.spec.ts](https://github.com/oppia/oppia/blob/13b1da20ee6c0e4eabc9720a3d1ca3d87c62fe8c/core/templates/pages/teach-page/teach-page.component.spec.ts)
* [about-page.component.spec.ts](https://github.com/oppia/oppia/blob/b46dd92fdb40e51ce8a9b66c507acd23a55a69d5/core/templates/pages/about-page/about-page.component.spec.ts)

## Contacts

If you have any questions about the above, you can contact any of the people below:

* @aishwary023 - aishwary.saxena.min19@iitbhu.ac.in
* @gp201 - praneethg2001@gmail.com
* @Radesh-kumar - imradesh@gmail.com
