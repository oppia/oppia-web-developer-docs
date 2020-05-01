# Frontend unit tests guide

This guide is intended to provide guidance for writing new frontend unit tests. It provides information about the established standards and provides tips on how to address specific failures. 

This guide can be used by both new Oppia members and developers who have contributed for a long time. If you have suggestions or tips to add, please contact mari.zangue@gmail.com.

## Goals
Our goal is to achieve **100% coverage** in all files on the frontend application. It means each line should be tested, ascertaining if its behavior is the expected one, thinking from a **behavior-first perspective**. That is, instead of just increasing the line coverage, it’s more important to test the file behavior by checking happy (expected) and unhappy (unexpected) paths. [Here](https://github.com/oppia/oppia/blob/ae649aa08f/core/templates/services/questions-list.service.spec.ts) is a good example to follow when talking about behavior testing -- note the detailed descriptions of what the expected behaviour is in each case.

Our goal is also to be sure the coverage won’t suffer any changes that may decrease it. **The coverage must be stable** and any changes made that may cause a regression shouldn’t happen without a warning. Then, in order to make the goal a real achievement, some rules (see the Rules section below) must be followed when handling unit tests.

## What are unit tests
A unit test checks the behavior of small components, which are called units. A component can be a function, and its behavior would be determined by the output produced, given a particular set of inputs.
A unit test should depend only on the “external” behavior to be tested, not the specific implementation of the function. This means that the behavior of other components is out of scope (it may confuse you when working on components that are using other components method, for example).
[Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/skill/RubricObjectFactorySpec.ts#L28-L41) is a simple unit test that demonstrates these points.

## Generating coverage reports
Coverage reports are an indispensable tool when working with unit tests. They can show you which lines are being tested and which are not. Use these reports to help you write better tests and to ensure that all the files and functionality are totally covered by the tests you write.  
To generate a new coverage report, run the following in the terminal:
    `python -m scripts.run_frontend_tests`  
The report will be generated at the `karma_coverage_reports/index.html` path, please be sure you’re at **opensource/** path when trying to access it. The coverage will look like this page:
![Karma Coverage reports](https://user-images.githubusercontent.com/34922478/80640321-9e30f900-8a39-11ea-8b8e-98dab4a3d48b.png)
You can use this report to determine which lines in the codebase still need to be covered by tests.

## Fundamentals

### Rules
Before starting to write a unit test, you need to be aware of some rules that must be followed in order to make your test consistent and correct and regression-proof.

Karma is a test runner that is used in the frontend codebase. Karma runs tests by compiling them all at once. This causes a tricky problem: a method in a file might be covered by a test suite for a different file, which can provide a false positive on the coverage report because each file is supposed to be fully covered by its corresponding spec file.
Thus, when testing a file, make sure that:
- Each file has its own spec file which tests each line of the file.
- **You should run the tests locally using fdescribe** in the outer describe of the file, and then make sure that the coverage is 100%. See the “Unit Test Structure” section below.

### How to choose a file to work on
When trying to choose the first files to work on, you might get confused. All the files are separated by a complexity criteria, so you can focus on files which you feel comfortable working with.

|            |      Easy       |     Medium      |        Hard        |
|------------|:---------------:|:---------------:|:------------------:|
| Complexity | Up to 100 lines | Up to 250 lines | At least 250 lines |


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

## Fixing frontend test errors
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