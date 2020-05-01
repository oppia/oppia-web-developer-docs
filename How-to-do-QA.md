# Introduction
QA is an important part of software development. Testing is typically done in two parts:
1. Automated tests
2. Manual tests
The below sections give guidelines on how to perform all the above tests.

## Automated testing
Any piece of code that we merge into develop is expected to have unit tests and end-to-end tests. Unit testing is important to make sure that each individual section of code is behaviourally correct. Make sure that the unit tests test the behaviour and not the implementation as such. Tests are expected to be written for both Frontend and Backend code.

End-to-end tests, on the other hand, ensure that a combined feature functions correctly. Once a feature is complete, before it is released to the public, we expect end-to-end tests to be written for the same.

***

## Manual testing
Manual testing is done at 2 places in the development workflow. Every PR must be manually tested by the author and the reviewer. We expect you to test all kinds of user paths involved in the PR (and not just "happy paths", i.e. the desired user path).

Before releasing code to users (we do monthly releases), we have a testing phase, where we have a group of people manually testing various critical user flows on Oppia. If you are interested in participating in release testing, contact @nithusha21.

The general guidelines for the above testing are:
* Keep the console open at all times. There should be no console errors.
* Try to deviate from the desired path, and make sure that any such deviation is handled appropriately.
* Test across various browsers and platforms (if possible). At least try to cover Chrome + Firefox.
* Test on mobile devices (actual mobile device, and not just small screen sizes on chrome). Many non-trivial bugs have been caught while testing on a mobile device.
* For looking at console logs on mobile, you can use chrome developer tools, with USB debugging.
* If your feature impacts learners, make sure to test with slow internet connections (Most browsers come with tools to simulate this).
