# Interpreting GitHub Actions Results

## Detailed Explanation

Our workflow tests run in parallel as to alleviate the overall pressure on the queue.

  ![GHCI Status](images/ghciSample.png)

In the example above, the lint checks and Mypy checks have failed. However, the rest of the tests have passed.

We also have two checks that have been skipped. These are checks that we have configured to be skipped during the execution of the workflow because they may not be necessary to that particular Pull Request.

### What should you do?

Following the example above, you must first fix both the lint check and Mypy check tests and push.
Go to 'Details' to view the test logs.

