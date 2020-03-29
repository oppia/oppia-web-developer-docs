# Intreprating CircleCI Results

## tl;dr
If your test status does not report, check the upstream test result.

  ![CircleCI Workflow](images/circleCIWorkflow.png)


## Detailed Explanation
Our CircleCI tests run in a staggered manner as to alleviate the overall pressure on the queue. As a result, some tests may never run if the upstream test fails. For example, see the following:

  ![CI Status](images/ciStatusSample.png)

In the example above, the frontend tests failed. Therefore, the following tests: typescript, backend, and all of e2e tests will not run. The statuses of those tests will remain pending, when in fact, they will never run for this commit.
