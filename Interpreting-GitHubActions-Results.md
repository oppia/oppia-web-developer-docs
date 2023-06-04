# Interpreting GitHub Actions Results

## Detailed Explanation

Our workflow tests run in parallel as to alleviate the overall pressure on the queue.

  ![GHCI Status](images/ghciSample.png)

In the example above, the lint checks and Mypy checks have failed. However, the rest of the tests have passed.

We also have two checks that have been skipped due to the failure of one of the e2e tests. In the event of an e2e test failure, any remaining e2e tests that are queued or currently running will be terminated and marked as "skipped."

### What should you do?

- Following the example above, you must first fix both the lint check and Mypy check tests and push.
- Go to 'Details' to view the test logs.

