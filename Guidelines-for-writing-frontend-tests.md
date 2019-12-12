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

## General guidelines for good tests:
- Naming the test is important. The name should include the name of the component being tested, the conditions imposed on the test and the expected outcome of the test. 
    - The test name follows this format: describe(<component name>) and it(‘should <do this action> when <this condition is imposed>’)
- All possible code paths in the function should be tested. This is important from a coverage perspective.
- Any common code can be extracted into a helper function to reduce duplication. Make sure the helper function deals with only one of the 3 parts, ie, the helper function can help with either setup, action or assertion, avoid overlapping across the parts.
- Assert as many things as possible. An example of this is say, the function returns the list, you can assert that the number of elements is as expected, and each element you expect is in the list. Another example is if an object is expected, then assert the various fields of the object are as expected.
- In the frontend, while writing tests, we don’t make actual calls to the backend. All http calls are mocked, to keep the tests independent of the backend. Similarly, any services can also be mocked. We try to keep such mocks as low as possible.
