# Interpreting CircleCI Results

## tl;dr

If your test status does not report, check the upstream test result. Here's the workflow job diagram:

  ![CircleCI Workflow](images/circleCIWorkflow.png)

## Detailed Explanation

Our workflow tests run in a staggered manner as to alleviate the overall pressure on the queue.

  ![GHCI Status](images/ghciSample.png)

In the example above, the lint checks and type checks have failed. However, the rest of the tests have passed.

### What should you do?

Following the example above, you must first fix both the lint check and type check tests and push.
