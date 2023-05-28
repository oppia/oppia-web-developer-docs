# Interpreting GitHub Actions Results

## Detailed Explanation

Our workflow tests run in parallel as to alleviate the overall pressure on the queue.

  ![GHCI Status](images/ghciSample.png)

In the example above, the lint checks and type checks have failed. However, the rest of the tests have passed.

### What should you do?

Following the example above, you must first fix both the lint check and type check tests and push.
