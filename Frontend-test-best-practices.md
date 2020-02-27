# Guide for writing frontend tests

## What are automated tests?
- Automated tests are dedicated code blocks that run to ensure a system works correctly.
- Automating tests reduces the need for humans to verify correctness.
- Tests can be done at any granularity level of a stack: the Oppia app, a specific class, or even a specific method.
- Tests prevent regressions which helps ensure your code doesn't break your teammates (and who wants to be remembered as the person who breaks everyone's code?).
- Tests also provide satisfaction & confidence when they verify that your code was written correctly.

## What are the various types of tests?
The most popular tests include unit tests, integration testing, end-to-end (e2e) tests, and manual tests. In Oppia Frontend, we write unit tests using Karma. Currently, we don’t really write integration tests in the frontend, but we do write e2e tests using Protractor. Apart from this every month, we do manual testing of the critical features every monthly release.

## What are unit tests?
- A unit test verifies a particular behaviour of a small component, for example, the component would be a function, and the behaviour would be the functionality under a particular set of inputs.
- A unit test should be dependent only on the functionality being tested. It should be independent of other functionalities.
- A unit test typically has 3 parts
     - Setup: This is the place where you create variables, dependencies, etc.
     - Action: This part performs the logic to be tested.
     - Assertions: Here you add commands to verify that the above action was completed (or not completed) as expected.
- [Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/skill/RubricObjectFactorySpec.ts#L28-L41) is a simple unit test that demonstrates these points.


## Best practices for good tests:
- Naming the test is important. The name should include the name of the component being tested, the conditions imposed on the test and the expected outcome of the test.
    - The test name follows this format: describe(<component name>) and it(‘should <do this action> when <this condition is imposed>’)
- All possible code paths in the function should be tested. This is important from a coverage perspective. [Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/objects/FractionObjectFactorySpec.ts) is a good example of testing all code paths
- Any common code can be extracted into a helper function to reduce duplication. Make sure the helper function deals with only one of the 3 parts, ie, the helper function can help with either setup, action or assertion, avoid overlapping across the parts.
- Assert as many things as possible. An example of this is say, the function returns the list, you can assert that the number of elements is as expected, and each element you expect is in the list. Another example is if an object is expected, then assert the various fields of the object are as expected.
- In the frontend, while writing tests, we don’t make actual calls to the backend. All http calls are mocked, to keep the tests independent of the backend. Similarly, any services can also be mocked. We try to keep such mocks as low as possible. [Here](https://github.com/oppia/oppia/blob/ae649aa08f1375457ec9e3c90257197b68fec7cd/core/templates/domain/learner_dashboard/learner-playlist.service.spec.ts#L27) is an example usage of $httpBackend to mock the backend responses.
- When writing asynchronous tests, if your asynchronous calls does not involves `intervalTimer()` functions like `setInterval` use `fakeAsync()` and `flushMicrotasks()`. A sample of code is given below:
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

  If your asynchronous calls involves `intervalTimer()` functions such as `setInterval()` then use
  `done`. A code sample for the same is given below:

  ```typescript
  it('does a thing', function(done) {
    someAsyncFunction(result) {
      expect(result).toEqual(someExpectedValue);
      done();
    });
  });
  ```
  You can read here https://angular.io/guide/testing to know more about jasmine testing. It's a long document so
  search and read whatever is relevant to you.
## Practical tips for writing tests:
- If you're trying to fully cover a specific file's behaviour using frontend tests, change the outer `describe` to `fdescribe` before running the tests locally (with coverage checks), so that only the tests in the file you're writing will run on Karma. This helps to ensure that all methods for the corresponding file are being tested thoroughly, and that the code in the file you're testing isn't being covered "by chance" due to some test from another file. (Remember to change the tag back to `describe` before committing your changes!)
