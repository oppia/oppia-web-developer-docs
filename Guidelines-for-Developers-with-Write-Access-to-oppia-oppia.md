Write access to the `oppia/oppia` repository comes with increased expectations. Individuals with write access have greater potential to damage the project, so everyone with write access is expected to follow these guidelines, which are designed to minimize the risk of such damage.

## Approving CI Test Runs

When new contributors open PRs, a developer with write access has to approve their CI test runs (note that this is different from approving a PR). Before approving, you should check any changes they make to the CI tests (e.g. the files in `.circleci/` and `.github/`, as well as the script files used by the tests) to make sure they are safe. We are primarily worried about 2 kinds of changes:

1. A new contributor could change the tests to mine cryptocurrency, which violates GitHub's terms.
2. We have secrets that are available to our CI runners that we don't want to be public. These are stored in environment variables and, in the case of GitHub Actions, in contexts. We don't want to allow changes that would leak these secrets.

## Merging Pull Requests

Before merging a pull request, ensure that all of the following criteria have been met:

1. All mandatory CI checks are passing (GitHub shouldn't let you merge without this).
2. There are no "don’t merge" labels on the PR.
3. The PR has been approved by all the necessary codeowners (GitHub shouldn’t let you merge without this).
4. All unresolved comments have been addressed. Note that reviewers should no longer approve a PR while they still have unresolved comments, but you should double-check.

## Opening Branches

With write access you can open branches in the `oppia/oppia` repository. Unless you are a release coordinator, you should not do this. Instead, open branches on your personal fork like usual.

## Rerunning Tests

### Flakes

With flaky tests, we often get in the habit of blindly rerunning failing tests until they pass. Please do not do this. Blind rerunning lets flaky code get in! Instead, inspect the error message to see if it looks like a flake. You should evaluate whether a failure is likely to be a flake based on these criteria:

1. Check whether the code that failed is at all related to the changes in the PR. If it's completely unrelated (e.g. the PR only changes a backend test but a frontend test is failing), that suggests that the failure is a flake.
2. For the end-to-end tests, we use a logging server that keeps a record of known flakes. Check the log output for a line (in green) reporting whether the logging server thinks the failure is a flake.
3. Have the contributor try running the test locally. If the test passes there, that’s another indication that this might be a flake.
Based on these criteria, you have to make a judgement call about whether the failure is likely to be a flake. If it is, then (and only then) should you restart the test.

## SSH

On Circle CI, you can restart a test and SSH into the container while the test is running. This is very useful for debugging, but it also invalidates the test results. If you ever SSH into a container, make sure you rerun the test without SSH access afterwards to make sure the tests still pass.
