# **[IN PROGRESS]**

This guide is intended to provide guidance for writing new frontend unit tests. It provides information about the established standards and provides tips on how to address specific failures. 

This guide can be used by both new Oppia members and developers who have contributed for a long time. If you have suggestions or tips to add, please contact mari.zangue@gmail.com.

## Summary
- [Goals](#goals)
- [What are unit tests](#what-are-unit-tests)
- [Helpful resources](#helpful-resources)
- [Generating coverage reports](#generating-coverage-reports)
  - [Ensuring that coverage is maintained](#ensuring-that-coverage-is-maintained)
- [Fundamentals](#fundamentals)
  - [How to analyze the file's coverage](#how-to-analyze-the-files-coverage)
  - [Rules](#rules)
  - [Unit test structure](#unit-test-structure)
  - [How to choose a file to work on](#how-to-choose-a-file-to-work-on)
- [General tips](#general-tips)
  - [Spy utilities](#spy-utilities)
    - [Spying on and handling with third-party libraries]()
    - [Spying a same object more than one time in same context]()
  - [Handling Window events and reloads]()
    - [When window calls reload]()
  - [Handling with asynchronous code]()
    - [Making HTTP calls]()
      - [AngularJS]()
      - [Angular 2+]()
    - [Using done and done.fail from Jasmine]()
    - [Mocking with $q API in AngularJS]()
  - [When should the upgraded services be imported in the test file?]()
  - [beforeEach order calls in AngularJS]()
  - [How to handle some common errors]()
- [Services](#services)
  - [AngularJS]()
    - [Testing controller property on $uibModal.open method]()
  - [Angular 2+]()
- [Controllers]()

## Goals
Our goal is to achieve **100% coverage** in all files on the frontend application. It means each line should be tested, ascertaining if its behavior is the expected one, thinking from a **behavior-first perspective**. That is, instead of just increasing the line coverage, it’s more important to test the file behavior by checking happy (expected) and unhappy (unexpected) paths. [Here](https://github.com/oppia/oppia/blob/ae649aa08f/core/templates/services/questions-list.service.spec.ts) is a good example to follow when talking about behavior testing -- note the detailed descriptions of what the expected behavior is in each case.

Our goal is also to be sure the coverage won’t suffer any changes that may decrease it. **The coverage must be stable** and any changes made that may cause a regression shouldn’t happen without a warning. Then, in order to make the goal a real achievement, some rules (see the Rules section below) must be followed when handling unit tests.

## What are unit tests
A unit test checks the behavior of small components, which are called units. A component can be a function, and its behavior would be determined by the output produced, given a particular set of inputs.
A unit test should depend only on the “external” behavior to be tested, not the specific implementation of the function. This means that the behavior of other components is out of scope (it may confuse you when working on components that are using other components method, for example).
[Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/skill/RubricObjectFactorySpec.ts#L28-L41) is a simple unit test that demonstrates these points.

## Helpful resources
This list contains some resources that might help you while writing unit tests:
- [Jasmine documentation](https://jasmine.github.io/api/edge/global)
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
- If you have tested a file until it reaches 100% coverage, you can’t push it to Github, unless you add the file name to the whitelist in the `scripts/check_frontend_coverage.p`y file.
- If you have removed a fully covered file (it may happen for many reasons: e.g. the file is not used anymore, the file is being migrated to Angular 2+, etc), you need to remove it manually from the whitelist. Then, you can push your commit to GitHub.  

If you need to track the coverage changes (maybe a new file has achieved 100% coverage, or a fully-covered file has had its coverage reduced) before pushing the changes to GitHub, you can pass a flag to the command:  
    `python -m scripts.run_frontend_tests --check_coverage`  

For example, let’s suppose `local-storage.service.ts` used to be fully covered but your changes have decreased it. By running this command, you’ll be able to see an output like this:  

![Example of an output by tracking the changes in the frontend unit tests](https://user-images.githubusercontent.com/34922478/80845732-8182f580-8be0-11ea-9c47-0f46f1f44c2f.png)

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

  Check it out [a real example](https://github.com/oppia/oppia/blob/develop/core/templates/pages/creator-dashboard-page/suggestion-modal-for-creator-view/suggestion-modal-for-creator-view.controller.spec.ts) in codebase to how use describe properly.

  The describe function has also some variants to help you. Use these variants only in the development environment:  
  - **fdescribe**: This is used when you want to run only the test suite marked as fdescribe. You should use it quite frequently when testing locally, in order to ensure that the coverage remains stable.
  - **xdescribe**: This is used when you want to run all test suites except the one marked with xdescribe.

- **beforeEach**
  The beforeEach function is used to set up essential configurations and variables before each spec runs. This function is used basically for three things:
  - Injecting the modules to be tested or to be used as a helper inside the test file. For example:
    ```
    beforeEach(angular.mock.inject(function($injector) {
      $timeout = $injector.get('$timeout');
      $q = $injector.get('$q');
      UserService = $injector.get('UserService');
      SiteAnalyticsService = $injector.get('SiteAnalyticsService');

      var $rootScope = $injector.get('$rootScope');
      $scope = $rootScope.$new();
      var directive = $injector.get('splashPageDirective')[0];
      ctrl = $injector.instantiate(directive.controller, {
        $rootScope: $scope
     });
    }));
    ```
    _Code from splash-page.controller.spec.ts_
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
  The it function is where the test happens. Like the describe function, its first parameter is a string which should determine the action to be tested and the expected outcome of the tests. The string should have a clear description of what is going to be tested. Also, the string must start with a should word.  
  All possible code paths in the function should be tested. Here is a good example of testing all code paths. The names of the various tests in this [example in codebase](https://github.com/oppia/oppia/blob/develop/core/templates/services/search.service.spec.ts) give you an idea of what is expected.
  Like describe, the it function has the variantes fit and xit and they can be used in the same as fdescribe and xdescribe.

- **afterEach**  
  The afterEach function is not used often in the unit tests. It’s used when we are handling async features as HTTP and timeout calls:
  ```
  afterEach(function() {
    $httpBackend.verifyNoOutstandingExpectation();
    $httpBackend.verifyNoOutstandingRequest();
  });
  ```
- **afterAll**  
  The afterAll function is almost never used in the codebase. But there is a specific case which it might be very helpful: when a global variable needs to be reassigned during the tests, you need to reset it to the default value after the all the assertions is finished. Check an example of this case [here](https://github.com/oppia/oppia/blob/develop/core/templates/services/site-analytics.service.spec.ts#L40-L42).

- **expect**  
  The expect function is used to assert a condition in the test. You can check all its methods in the [Jasmine documentation](https://jasmine.github.io/api/edge/global). [Here's](https://github.com/oppia/oppia/blob/develop/core/templates/pages/exploration-editor-page/services/graph-data.service.spec.ts#L92-L112) a good example of how to use expect correctly.

### How to choose a file to work on
When trying to choose the first files to work on, you might get confused. All the files are separated by a complexity criteria, so you can focus on files which you feel comfortable working with.

|            |      Easy       |     Medium      |        Hard        |
|------------|:---------------:|:---------------:|:------------------:|
| Complexity | Up to 100 lines | Up to 250 lines | At least 250 lines |

## General tips

### Spy utilities  
One of the main features of Jasmine is allowing you to spy on a method or property of an object. This is helpful in some cases for seeing what is going on:  
- It can spy on properties of an object (using the spyOnProperty method). [Here](https://github.com/oppia/oppia/blob/develop/core/templates/services/contextual/device-info.service.spec.ts#L48-L55)'s an example.
- It can mock a property value or a method return. [Here](https://github.com/oppia/oppia/blob/develop/core/templates/pages/exploration-editor-page/feedback-tab/services/thread-data.service.spec.ts#L147)'s an example.
- It allows you to provide fake implementations that can be called when a method is executed. This is commonly used when mocking AngularJS promises with $defer. [Here](https://github.com/oppia/oppia/blob/develop/core/templates/pages/email-dashboard-pages/email-dashboard-page.controller.spec.ts#L121-L133)'s an example.
- It can spy on a method to check whether that method is being called when the spec runs. [Here](https://github.com/oppia/oppia/blob/develop/core/templates/services/schema-default-value.service.spec.ts#L109-L118)'s an example.

#### Spying on and handling with third-party libraries  
Also, the spy can be used when mocking third-party libraries, like JQuery, mostly when doing ajax calls. [Here](https://github.com/oppia/oppia/blob/develop/core/templates/services/assets-backend-api.service.spec.ts#L274-L292)'s a good example when mocking JQuery ajax calls.

#### Spying the same method/property more than one time in same context  
It is impossible to spy twice the same method or property in the same context (block). For instance, the code below would throw an error:
```
spyOn('should throw an error when spying twice', function() {
  spyOn(console, 'warn').and.stub();
  spyOn(console, 'warn').and.stub();
});
```
However, there are some situations where you need to change a value or a method’s return value spy in the same spec, for instance by changing the location path in a mock window object, or even reseting a mock to call the original code. You can do it by assigning the spy (without calling any method) into a variable. Then you can use this variable to call the spy methods as many times you want. For example (this code won't throw an error anymore):
```
spyOn('should not throw an error when spying twice', function() {
  var warnSpy = spyOn(console, 'warn');
  warnSpy.and.stub();
  warnSpy.and.stub();
});
```
You can check real examples of this approach [here](https://github.com/oppia/oppia/blob/develop/core/templates/pages/landing-pages/topic-landing-page/topic-landing-page.controller.spec.ts#L94-L109) and [here](https://github.com/oppia/oppia/blob/develop/core/templates/pages/about-page/about-page.controller.spec.ts#L24-L29).

#### Handling Window events and reloads
Spying on window object is very common, mainly because some native behaviors can cause the tests to fail or make them unpredictable. This happens in two specific cases:

##### When window calls reload  
When reload is called in the native form, it will fail the tests. You can fix it by using the Spy `returnValue()` method. Also, the image below gives an example of how to avoid native `reload()` calls by mocking using an empty function, but you may need to adjust this based on the context you’re testing. Check it out how to mock `reload()` correctly [here](https://github.com/oppia/oppia/blob/develop/core/templates/pages/about-page/about-page.controller.spec.ts#L72-L77).

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

## Best practices for good tests:
- Naming the test is important. The name should include the name of the component being tested, the conditions imposed on the test and the expected outcome of the test.
    - The test name follows this format: describe(<component name>) and it(‘should <do this action> when <this condition is imposed>’)
    - Here is an example

      ![image](https://user-images.githubusercontent.com/11898234/75883048-5da56c80-5e48-11ea-89f1-bc097e73bdef.png)

- All possible code paths in the function should be tested. This is important from a coverage perspective. [Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/objects/FractionObjectFactorySpec.ts) is a good example of testing all code paths. The names of the various tests in the below image should give you an idea of what is expected.

  ![image](https://user-images.githubusercontent.com/11898234/75883131-83cb0c80-5e48-11ea-91e8-2a36dcefd218.png)

- Any common code can be extracted into a helper function to reduce duplication. Make sure the helper function deals with only one of the 3 parts, ie, the helper function can help with either setup, action or assertion, avoid overlapping across the parts.
- Assert as many things as possible. An example of this is say, the function returns the list, you can assert that the number of elements is as expected, and each element you expect is in the list. Another example is if an object is expected, then assert the various fields of the object are as expected.
- In the frontend, while writing tests, we don’t make actual calls to the backend. All http calls are mocked, to keep the tests independent of the backend. Similarly, any services can also be mocked. We try to keep such mocks as low as possible. [Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/learner_dashboard/learner-playlist.service.spec.ts#L27) is an example usage of $httpBackend to mock the backend responses. A brief version of the code there, with some explanatory comments is given below

  ![image](https://user-images.githubusercontent.com/11898234/75883248-bb39b900-5e48-11ea-9d50-83157e8f6515.png)


- When writing asynchronous tests, if your asynchronous call involves `promises` use `fakeAsync()` and `flushMicrotasks()`. A sample of code is given below:
  ```typescript
  it('should test some asynchronous code', fakeAsync(() => {

        let flagOne = false;
        let flagTwo = false;

        Promise.resolve(true).then((result) => {
            flagOne = true;
        });

        Promise.resolve(true).then((result) => {
            flagTwo = true;
        });

        flushMicrotasks();

        expect(flagOne).toBe(true); // PASSES
        expect(flagTwo).toBe(true); // PASSES

  }));
  ```

  If your asynchronous calls involves functions like `setInterval()`, `setTimeout()` then use
  `done`. A code sample for the same is given below:

  ```typescript
  it('does a thing', function(done) {
    someAsyncFunction(result) {
      expect(result).toEqual(someExpectedValue);
      done();
    });
  });
  ```
  If your async calls involves anything other than above two conditions, contact **Nitish**(@bansalnitish).

  You can read here https://angular.io/guide/testing to know more about jasmine testing. It's a long document so
  search and read whatever is relevant to you.
## Practical tips for writing tests:
- If you're trying to fully cover a specific file's behaviour using frontend tests, change the outer `describe` to `fdescribe` before running the tests locally (with coverage checks), so that only the tests in the file you're writing will run on Karma. This helps to ensure that all methods for the corresponding file are being tested thoroughly, and that the code in the file you're testing isn't being covered "by chance" due to some test from another file. (Remember to change the tag back to `describe` before committing your changes!)

## Services  
Services are one of the most important features in the codebase. They contain logic that can be used across the codebase multiple times. There are three possible extensions for services:  
- *.service.ts
- *Factory.ts
- *.factory.ts
- *.tokenizer.ts  

As a good first issue, all the services that need to be tested are listed in [issue #4057](https://github.com/oppia/oppia/issues/4057), grouped by the [complexity criteria](https://github.com/oppia/oppia/wiki/Frontend-unit-tests-guide#how-to-choose-a-file-to-work-on).

### AngularJS

Use some files that are correctly following the testing patterns as reference:  
- current-interaction.service.spec.ts
- editable-exploration-backend-api.service.spec.ts
- improvement-task.service.spec.ts

#### Testing controller property on $uibModal.open method  
There are some services which use the $uibModal.open method from [Angular UI Bootstrap](https://angular-ui.github.io/bootstrap/) library, which can make the service itself very tricky to test:  
![Tricky test](https://user-images.githubusercontent.com/34922478/80816478-f7b63680-8ba5-11ea-81d7-ddd408e35682.png)  
_Code from exploration-states.service.ts_  

So, for modals, the correct approach to follow is:  
- Create a new controller in a separate file and copy the method controller to it.
- Instead of declaring the controller in the method, refers to the controller you have created.
- Then, the service can be tested correctly, and the controller as well. [Here](https://github.com/oppia/oppia/blob/develop/core/templates/pages/exploration-editor-page/improvements-tab/services/improvement-modal.service.ts#L56-L66)’s an example.  

If you’re interested in working with this kind of file, please check [issue #8924](https://github.com/oppia/oppia/issues/8924) containing all the files with $uibModal to be migrated to a separated file.  

### Angular 2+  
Use some files that are correctly following the testing patterns as reference:  
- exploration-features-backend-api.service.spec.ts
- editability.service.spec.ts
- exploration-html-formatter.service.spec.ts

## Controllers  
Use some files that are correctly following the testing patterns as reference:  
- improvement-confirmation-modal.controller.spec.ts
- stewards-landing-page.controller.spec.ts

Also, please take a look at [Pull Request #8528](https://github.com/oppia/oppia/pull/8528) where you can find more about how to test controllers.



