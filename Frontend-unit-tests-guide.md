This guide is intended to provide guidance for writing new frontend unit tests. It provides information about the established standards and provides tips on how to address specific failures. 

This guide can be used by both new Oppia members and developers who have contributed for a long time. If you have suggestions or tips to add, please contact mari.zangue@gmail.com.

## Summary
- [Goals](#goals)
- [What are unit tests](#what-are-unit-tests)
- [Helpful resources](#helpful-resources)
- [Generating coverage reports](#generating-coverage-reports)
  - [Ensuring that coverage is maintained](#ensuring-that-coverage-is-maintained)
- [Fundamentals](#fundamentals)
  - [How to analyze the file's coverage](#how-to-analyze-a-files-coverage)
  - [Rules](#rules)
  - [Unit test structure](#unit-test-structure)
  - [Good practices](#good-practices)
  - [How to choose a file to work on](#how-to-choose-a-file-to-work-on)
- [General tips](#general-tips)
  - [Spy utilities](#spy-utilities)
    - [Spying on and handling with third-party libraries](#spying-on-and-handling-with-third-party-libraries)
    - [Spying a same object more than one time in same context](#spying-the-same-methodproperty-more-than-one-time-in-same-context)
    - [Creating spies reassigning expressions](#creating-spies-reassigning-expressions)
  - [Handling Window events and reloads](#handling-window-events-and-reloads)
    - [When window calls reload](#when-window-calls-reload)
    - [Using the same object reference in both file and spec file](#using-the-same-object-reference-in-both-file-and-spec-file)
  - [Handling with asynchronous code](#handling-with-asynchronous-code)
    - [Making HTTP calls](#making-http-calls)
      - [Setting up CsrfToken](#setting-up-csrftoken)
      - [AngularJS](#angularjs)
      - [Angular 2+](#angular-2)
    - [Using done and done.fail from Jasmine](#using-done-and-donefail-from-jasmine)
    - [Mocking with $q API in AngularJS](#mocking-with-q-api-in-angularjs)
  - [When should the upgraded services be imported in the test file?](#when-should-the-upgraded-services-be-imported-in-the-test-file)
  - [beforeEach calls in AngularJS](#beforeeach-calls-in-angularjs)
  - [How to handle common errors](#how-to-handle-common-errors)
- [Services](#services)
  - [AngularJS](#angularjs-1)
    - [Testing controller property on $uibModal.open method](#testing-controller-property-on-uibmodalopen-method)
  - [Angular 2+](#angular-2-1)
- [Controllers](#controllers)

## Goals
Our goal is to achieve **100% coverage** in all files on the frontend application. It means each line should be tested, ascertaining if its behavior is the expected one, thinking from a **behavior-first perspective**. That is, instead of just increasing the line coverage, it’s more important to test the file behavior by checking happy (expected) and unhappy (unexpected) paths. [Here](https://github.com/oppia/oppia/blob/ae649aa08f/core/templates/services/questions-list.service.spec.ts#L19) is a good example to follow when talking about behavior testing -- note the detailed descriptions of what the expected behavior is in each case.

Our goal is also to be sure the coverage won’t suffer any changes that may decrease it. **The coverage must be stable** and any changes made that may cause a regression shouldn’t happen without a warning. Then, in order to make the goal a real achievement, some rules (see the [Rules section](#rules) below) must be followed when handling unit tests.

## What are unit tests
A unit test checks the behavior of small components, which are called units. A component can be a function, and its behavior would be determined by the output produced, given a particular set of inputs.
A unit test should depend only on the “external” behavior to be tested, not the specific implementation of the function. This means that the behavior of other components is out of scope (it may confuse you when working on components that are using other components method, for example).
[Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/skill/RubricObjectFactorySpec.ts#L28-L41) is a simple unit test that demonstrates these points.

## Helpful resources
This list contains some resources that might help you while writing unit tests:
- [Jasmine documentation](https://jasmine.github.io/api/edge/global)
- [Karma](https://karma-runner.github.io/)
- [Angular 2+ testing](https://angular.io/guide/testing)
- [AngularJS testing](https://docs.angularjs.org/guide/unit-testing)

## Generating coverage reports
Coverage reports are an indispensable tool when working with unit tests. They can show you which lines are being tested and which are not. Use these reports to help you write better tests and to ensure that all the files and functionality are totally covered by the tests you write.  
To generate a new coverage report, run the following in the terminal:  
    `python -m scripts.run_frontend_tests`  

The report will be generated at the `karma_coverage_reports/index.html` path, please be sure you’re at `opensource/` path when trying to access it. The coverage will look like this page:  

![Karma Coverage reports](https://user-images.githubusercontent.com/34922478/80640321-9e30f900-8a39-11ea-8b8e-98dab4a3d48b.png)  

You can use this report to determine which lines in the codebase still need to be covered by tests.

### Ensuring that coverage is maintained  
In order to make the coverage stable, all fully-covered files are listed in the file `scripts/check_frontend_coverage.py`. This list is very helpful for some reasons:
- If your changes decrease the coverage of a fully covered file, you can’t push it to GitHub.
- If you have tested a file until it reaches 100% coverage, you can’t push it to Github, unless you add the file name to the whitelist in the `scripts/check_frontend_coverage.py` file.
- If you have removed a fully covered file (it may happen for many reasons: e.g. the file is not used anymore, the file is being migrated to Angular 2+, etc), you need to remove it manually from the whitelist. Then, you can push your commit to GitHub.  

If you need to track the coverage changes (maybe a new file has achieved 100% coverage, or a fully-covered file has had its coverage reduced) before pushing the changes to GitHub, you can pass a flag to the command:  
    `python -m scripts.run_frontend_tests --check_coverage`  

For example, let’s suppose `local-storage.service.ts` is fully covered but your changes had decreased it. By running this command, you’ll be able to see an output like this:  

![Example of output by tracking the changes in the frontend unit tests](https://user-images.githubusercontent.com/34922478/80845732-8182f580-8be0-11ea-9c47-0f46f1f44c2f.png)

## Fundamentals

### How to analyze a file's coverage

When writing tests, the goal is to completely cover the file. In order to do that, you need to understand what the coverage report is telling you. Basically, the coverage tells which line is being hit, partially hit, or missed:
- **Hit**: the line was executed by the test suite.
- **Partially hit**: the line was partially executed by the test suite. There’s another possibility where this line is missed.
- **Missed**: the line wasn’t executed by the test suite.

More than just reporting the “covered” state of each line, the coverage report also reports something called **branch coverage**. A branch refers to a branch in the program (if/else statements, loops, and so on). To be fully covered, all the file’s branches need to be tested. However, the Karma coverage report uses symbols (with letter I - for if - and E - for else) to refer to if/else statements branches. It’s important to note that these symbols will appear even if the branch is being covered, So, please **ignore** these symbols and pay attention to only the line coverage information (as you see above). Here’s an example:  

![Example for branch coverage symbols](https://user-images.githubusercontent.com/34922478/80809691-9340aa80-8b98-11ea-9a22-6fd21171db85.png)

### Rules
Before starting to write a unit test, you need to be aware of some rules that must be followed in order to make your test consistent and correct and regression-proof.

Karma is a test runner that is used in the frontend codebase. Karma runs tests by compiling them all at once. This causes a tricky problem: a method in a file might be covered by a test suite for a different file, which can provide a false positive on the coverage report because each file is supposed to be fully covered by its corresponding spec file.
Thus, when testing a file, make sure that:
- Each file has its own spec file which tests each line of the file.
- **You should run the tests locally using fdescribe** in the outer describe of the file, and then make sure that the coverage is 100%. See the [Unit Test Structure](#unit-test-structure) section below.

### Unit test structure
A unit test is made of functions that configure the test environment, make assertions, and separate the different contexts of each situation. There are some test functions that are used across the codebase:
- **describe**  
  The describe function has a string parameter which should contain the name of the component being tested or     (when nested within another describe function) should describe the conditions imposed on the specific context pertaining to the tests in that “describe” block. Here are some examples:
  ```
  describe('Component Name', function() {
  });
  ```
  _The outer describe function._

  ```
  describe('Component Name', function() {
    describe('when it is available', function() {});

    describe('when it is not available', function() {});
  });
  ```
  _A describe function nested in another describe function._

  Check it out [a real example](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/creator-dashboard-page/suggestion-modal-for-creator-view/suggestion-modal-for-creator-view.controller.spec.ts#L24-L310) in codebase to how use describe properly.

  The describe function has also some variants to help you. Use these variants only in the development environment:  
  - **fdescribe**: This is used when you want to run only the test suite marked as `fdescribe`. You should use it quite frequently when testing locally, in order to ensure that the coverage remains stable.
  - **xdescribe**: This is used when you want to run all test suites except the one marked with `xdescribe`.

- **beforeEach**
  The beforeEach function is used to set up essential configurations and variables before each spec runs. This function is used basically for three things:
  - Injecting the modules to be tested or to be used as a helper inside the test file, for [example](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/splash-page/splash-page.controller.spec.ts#L37-L49).
  - Mocking the unit test’s external dependencies (It’s used only on AngularJS files):
    ```
    beforeEach(angular.mock.module(function($provide) {
      $provide.value('ExplorationStatesService', {
        getState: () => ({ interaction: null })
      });    
    }));
    ```
  - Providing Angular 8 services in downgrade files when it uses any upgraded service as a dependency.
    ```
    beforeEach(angular.mock.module('oppia', function($provide) {
      var ugs = new UpgradedServices();
      for (let [key, value] of Object.entries(ugs.getUpgradedServices())) {
        $provide.value(key, value);
      }
    }));
    ```
- **it**  
  The it function is where the test happens. Like the describe function, its first parameter is a string which should determine the action to be tested and the expected outcome of the tests. The string should have a clear description of what is going to be tested. Also, **the string must start with a should word**.  
  All possible code paths in the function should be tested. Here is a good example of testing all code paths. The names of the various tests in this [example in codebase](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/search.service.spec.ts#L82-L451) give you an idea of what is expected.
  Like describe, the it function has the variants `fit` and `xit` and they can be used in the same as `fdescribe` and `xdescribe`.

- **afterEach**  
  The afterEach function is not used often in the unit tests. It’s used when we are handling async features as HTTP and timeout calls (both in AngularJS and Angular 2+). [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/domain/exploration/read-only-exploration-backend-api.service.spec.ts#L100-L103)'s an example to handle HTTP mocks in AngularJS and [here](https://github.com/oppia/oppia/blob/ae649aa08f/core/templates/domain/classroom/classroom-backend-api.service.spec.ts#L72-L74)'s an example of doing the same in Angular 2+.
- **afterAll**  
  The afterAll function is almost never used in the codebase. But there is a specific case which it might be very helpful: when a global variable needs to be reassigned during the tests, you need to reset it to the default value after all the assertions are finished. Check an example of this case [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/site-analytics.service.spec.ts#L40-L42).

- **expect**  
  The expect function is used to assert a condition in the test. You can check all its methods in the [Jasmine documentation](https://jasmine.github.io/api/edge/matchers.html). [Here's](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/services/graph-data.service.spec.ts#L92-L112) a good example of how to use expect correctly.

### Good practices

#### Do not test private methods/properties
Private methods/properties can be accessed just by the class or function where it belongs. They starts with `_` and they are called in other methods inside the class or function scope. It's not a good practice to test private methods/properties because since they should not be access from the outside. Instead, you should only test public methods and their output. For example:

Bad:
```js
it('should get generic name', function() {
  var name = component._name;
  expect(name).toBe('foo');
});
```

Good:
```js
it('should get generic name', function() {
  var name = component.getName();
  expect(name).toBe('foo');
});
```

#### Care about behavior and not about percentage
In despite of our mainly goal, make sure your spec tests the file's behavior. It means that writing tests just to get 100% coverage (just making karma to execute all lines) is not a good practice and it makes the coverage unstable. As you can see on [What are unit tests](#what-are-unit-tests) section, unit tests is about testing the expected output and not the internal implementation. For example:

Bad:
```js
it('should get items from api', function() {
  var consoleSpy = spyOn(console, 'log').and.callThrough();
  component.fetchApi();
  expect(consoleSpy).haveBeenCalledWith('fetched!);
});
```

Good:
```js
it('should get items from api', function() {
  var MAX_ITEMS_TO_FETCH = 10;
  component.fetchApi();
  expect(component.itemsFetched).toEqual(10);
});
```

### How to choose a file to work on
When trying to choose the first files to work on, you might get confused. All the files are separated by complexity criteria, so you can focus on files which you feel comfortable working with.

|            |      Easy       |     Medium      |        Hard        |
|------------|:---------------:|:---------------:|:------------------:|
| Complexity | Up to 100 lines | Up to 250 lines | At least 250 lines |

## General tips

### Spy utilities  
One of the main features of Jasmine is allowing you to spy on a method or property of an object. This is helpful in some cases for seeing what is going on:  
- It can spy on an object's properties (using the `spyOnProperty` method). [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/contextual/device-info.service.spec.ts#L48-L55)'s an example.
- It can mock a property value or a method return. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/feedback-tab/services/thread-data.service.spec.ts#L147)'s an example.
- It allows you to provide fake implementations that can be called when a method is executed. This is commonly used when mocking AngularJS promises with `$defer`. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/email-dashboard-pages/email-dashboard-page.controller.spec.ts#L121-L133)'s an example.
- It can spy on a method to check whether that method is being called when the spec runs. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/schema-default-value.service.spec.ts#L109-L118)'s an example.

#### Spying on and handling with third-party libraries  
Also, the spy can be used when mocking third-party libraries, like JQuery, mostly when doing ajax calls. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/assets-backend-api.service.spec.ts#L274-L292)'s a good example when mocking JQuery ajax calls.

#### Spying the same method/property more than one time in same context  
It is impossible to spy twice the same method or property in the same context (block). For instance, the code below would throw an error:
```
spyOn('should throw an error when spying twice', function() {
  spyOn(console, 'warn').and.stub();
  spyOn(console, 'warn').and.stub();
});
```
However, there are some situations where you need to change a value or a method’s return value spy in the same spec, for instance by changing the location path in a mock `window` object, or even reseting a mock to call the original code. You can do it by assigning the spy (without calling any method) into a variable. Then you can use this variable to call the spy methods as many times you want. For example (this code won't throw an error anymore):
```
spyOn('should not throw an error when spying twice', function() {
  var warnSpy = spyOn(console, 'warn');
  warnSpy.and.stub();
  warnSpy.and.stub();
});
```
You can check real examples of this approach [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/landing-pages/topic-landing-page/topic-landing-page.controller.spec.ts#L94-L109) (dealing with window location properties) and [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/about-page/about-page.controller.spec.ts#L72-L89) (resetting to spy to original code).

#### Creating spies reassigning expressions
Sometimes you might face some issues trying to spy a certain property or method (mainly when you want to return a custom value). There are many ways to spy and return a custom value for property or a method as you can see in the sections above. However, you must not use spies that are declared by reassigning a **global expression**, like the window object or its properties and methods. Let's suppose you need to return a custom value from `document.getElementById` but you're facing some problems trying to do it. You may find nice solutions searching over the internet, however, make sure the chosen solution is not changing a global value, like in this [case](https://github.com/oppia/oppia/blob/bc8625cb38aef8f93844954d0b0cb797e1bd753b/core/templates/pages/preferences-page/modal-templates/edit-profile-picture-modal.controller.spec.ts#L51-L52). You should find another approach for the goal, like this [example](https://github.com/oppia/oppia/blob/1f20eda67be9bfb78b5885916ce37ddea7f05183/core/templates/pages/preferences-page/modal-templates/edit-profile-picture-modal.controller.spec.ts#L49-L50).  

The problem with the first case is that when changing a global value, it will affect other files that use the expression you've reassigned, making the unit tests error-prone. [Here](https://github.com/oppia/oppia/issues/9660)'s a good example of a bug that appears after using the first case.

### Handling Window events and reloads
Spying on window object is very common, mainly because some native behaviors can cause the tests to fail or make them unpredictable. This happens in two specific cases:

#### When window calls reload  
When reload is called in the native form, it will fail the tests. You can fix it by using the Spy `returnValue()` method. Also, the image below gives an example of how to avoid native `reload()` calls by mocking using an empty function, but you may need to adjust this based on the context you’re testing. Check it out how to mock `reload()` correctly [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/about-page/about-page.controller.spec.ts#L72-L77).

#### Using the same object reference in both file and spec file  
In some cases, you might need to share the same window object in the file you’re testing and in the spec file itself, mainly if you’re working on window events. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/about-page/about-page.controller.spec.ts#L24-L29)’s an example of how to do it.

### Handling with asynchronous code  

#### Making HTTP calls  
In the frontend, while writing tests, we don’t make actual calls to the backend. All HTTP calls are mocked since the frontend tests actually run without a backend in place.  
Similarly, any services can also be mocked. We try to keep the usage of such mocks as low as possible since the more mocks there are, the more divergence there is with the underlying code.  

##### Setting up CsrfToken
In order to make HTTP calls in a secure way, it's common that applications have tokens to authenticate the user while they using the platform. In the codebase, there is a specific service to handle the token, called CsrfTokenService. When mocking HTTP calls, you must use this service in the test file so the tests won't fail (you don't have a real token when running unit tests so it needs to be mocked). Then, you should just copy and paste this piece of code inside a beforeEach block (the CsrfService will be a variable with the return of `$injector.get('CsrfTokenService')` -- in AngularJS -- or `TestBed.get(CsrfTokenService)` -- in Angular 2+):
```
spyOn(CsrfService, 'getTokenAsync').and.callFake(function() {
  var deferred = $q.defer();
  deferred.resolve('sample-csrf-token');
  return deferred.promise;
});
```

##### AngularJS
[Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/learner_dashboard/learner-playlist.service.spec.ts#L84-L99) is an example which uses `$httpBackend` to mock the backend responses. A brief version of the code there, with some explanatory comments is given below.     
To mock a backend call, you need to use `$httpBackend` dependency. There are two ways to expect a HTTP method (you can use both):
- `$httpBackend.expectMETHODNAME(URL)` - like `expectPOST` or `expectGET` for instance
- `$httpBackend.expect(‘METHOD’, URL)` - You pass the HTTP method as the first argument.  

When writing HTTP tests (which are asynchronous) we need to always use `$httpBackend.flush()` method. This will ensure that the mocked request call will be executed. So don’t forget to put it into the spec test (otherwise it will throw an error).

##### Angular 2+ 
When writing HTTP tests on Angular 2+, use `httpTestingController` with `fakeAsync()` and `flushMicrotasks()`. [Here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/domain/classroom/classroom-backend-api.service.spec.ts#L77-L96)’s a good example to follow.  

As the AngularJS way to mock HTTP calls, the Angular 2+ has flush functions to return the expected response and execute the mock correctly as well.

#### Using `done` and `done.fail` from Jasmine  
Using `done` and `done.fail` is another way to test asynchronous code in Jasmine. You can use it on promises (HTTP calls and so on), timers as `setTimeout` and `setInterval` (`$interval` and `$timeout` in AngularJS).  

There’s a specific case where you should use `done` on mocking HTTP calls: when you want to assert the result of the fulfilled or reject promise, as you can see [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/assets-backend-api.service.spec.ts#L274-L292). In this piece of code, we need to assert the response variable, then we use `done` after doing the assertion so Jasmine understands the asynchronous code has been completed. You can use `done.fail` when handling with rejected promises.

You can use `done` in timing events as well, check out this [example](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/teach-page/teach-page.controller.spec.ts#L53-L67).

#### Mocking with `$q` API in AngularJS  
When mocking a promise in AngularJS, you might use `$q` API. In these cases, you must use `$scope.$apply()` or `$scope.$digest` because it forcibly `$q` promises to be resolved through a Javascript digest. Here are some examples using [$apply](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/email-dashboard-pages/email-dashboard-page.controller.spec.ts#L101-L108) and [$digest](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/services/exploration-states.service.spec.ts#L209-L221).

### When should the upgraded services be imported in the test file?  
One of the active projects in Oppia is the Angular 8 migration. By now, the AngularJS services are being migrated and it’s still being used in downgrade files. When testing AngularJS files which uses an Angular 8 as a dependency (directly or not), you must use the beforeEach call below: 
```
beforeEach(angular.mock.module('oppia', function($provide) {
  var ugs = new UpgradedServices();
  for (let [key, value] of Object.entries(ugs.getUpgradedServices())) {
    $provide.value(key, value);
  }
}));
``` 

If the file you’re testing doesn’t use any upgraded files, you don’t need to copy and paste this beforeEach call.

### BeforeEach calls in AngularJS  
If you’re testing an AngularJS file that uses an upgraded service, you’ll need to copy and past the beforeEach block which mocks all the upgraded services. Then, you might notice in beforeEach calls we follow a specific sequence (as you can see [here](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/editor-tab/training-panel/training-modal.controller.spec.ts#L35-L48)).  

However, you might face the following situation: you need to mock an Angular 8 service by using `$provide.value`. Here’s the problem: if you use `$provide.value` before calling the updated services, your mock will be overwritten by the original code of the service.

So, what you need to do is to change the order of beforeEach calls, as you can see in this [test](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/improvements-tab/services/improvement-suggestion-thread-modal.controller.spec.ts#L36-L51).

### How to handle common errors  
- If you see an error like `Error: Trying to get the Angular injector before bootstrapping the corresponding Angular module`, it means you are using a service (directly or indirectly) that is Upgraded to Angular and this error can throw or two reasons:
  - Your test that is written in AngularJS is unable to get that particular service.  
    You can fix this by importing `UpgradedServices` and using it in a `beforeEach` block:

    ```
    import { UpgradedServices } from 'services/UpgradedServices';
    .
    .
    beforeEach(angular.mock.module('oppia', function($provide) {
      var ugs = new UpgradedServices();
      for (let [key, value] of Object.entries(ugs.getUpgradedServices())) {
        $provide.value(key, value);
      }
    }));
    ```
  - The upgraded service is not listed on `UpgradedServices.ts` file.  
    You can fix this by adding the upgraded service in `UpgradedService.ts`:
    
    ```
    import { ServiceName } from 'path/to/service';
    .
    .
    .
    upgradedServices['ServiceName'] = new ServiceName();
    ```
- If you’re working with async on AngularJS and your tests don’t seem to run correctly, make sure you’re using `$apply` or `$digest` in the spec, as in this [example](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/topic-editor-page/services/topic-editor-state.service.spec.ts#L716-L720).

## Services  
Services are one of the most important features in the codebase. They contain logic that can be used across the codebase multiple times. There are three possible extensions for services:  
- *.service.ts
- *Factory.ts
- *.factory.ts
- *.tokenizer.ts  

As a good first issue, all the services that need to be tested are listed in [issue #4057](https://github.com/oppia/oppia/issues/4057), grouped by the [complexity criteria](#how-to-choose-a-file-to-work-on).

### AngularJS

Use some files that are correctly following the testing patterns as reference:  
- [current-interaction.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-player-page/services/current-interaction.service.spec.ts#L39)
- [editable-exploration-backend-api.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/domain/exploration/editable-exploration-backend-api.service.spec.ts#L30)
- [improvement-task.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/improvement-task.service.spec.ts#L29)

#### Testing controller property on $uibModal.open method  
There are some services which use the $uibModal.open method from [Angular UI Bootstrap](https://angular-ui.github.io/bootstrap/) library, which can make the service itself very tricky to test:  
![Tricky test](https://user-images.githubusercontent.com/34922478/80816478-f7b63680-8ba5-11ea-81d7-ddd408e35682.png)  
_Code from [exploration-states.service.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/services/exploration-states.service.ts#L41)_  

So, for modals, the correct approach to follow is:  
- Create a new controller in a separate file and copy the method controller to it.
- Instead of declaring the controller in the method, you should refer to the controller you have created.
- Then, the service can be tested correctly, and the controller as well. [Here](https://github.com/oppia/oppia/tree/2e60d69d7b06f45ac807d66f6de571c627db1397/core/templates/pages/exploration-editor-page/improvements-tab/services/improvement-modal.service.ts#L56-L66)’s an example.  

If you’re interested in working with this kind of file, please check [issue #8924](https://github.com/oppia/oppia/issues/8924) containing all the files with `$uibModal` to be migrated to a separated file.  

### Angular 2+  
Use some files that are correctly following the testing patterns as reference:  
- [exploration-features-backend-api.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/exploration-features-backend-api.service.spec.ts#L26)
- [editability.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/editability.service.spec.ts#L21)
- [exploration-html-formatter.service.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/services/exploration-html-formatter.service.spec.ts#L27)

## Controllers  
Use some files that are correctly following the testing patterns as reference:  
- [improvement-confirmation-modal.controller.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/exploration-editor-page/improvements-tab/services/improvement-confirmation-modal.controller.spec.ts#L19)
- [stewards-landing-page.controller.spec.ts](https://github.com/oppia/oppia/blob/2e60d69d7b/core/templates/pages/landing-pages/stewards-landing-page/stewards-landing-page.controller.spec.ts#L25)

Also, please take a look at [Pull Request #8528](https://github.com/oppia/oppia/pull/8528) where you can find more about how to test controllers.



