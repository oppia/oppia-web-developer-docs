Code review is an important part of the Oppia development cycle. Having a second pair of eyes look at your code can help to catch silly mistakes and serve as a check for whether your code is readable/understandable by other team members (which is important for maintainability).

When you receive a code review request, please try to do the review as soon as possible! Otherwise, the submitter will be blocked.

## When you first receive a review request

  1. When you get an email saying a pull request has been assigned to you for review, click on the link to open it in GitHub.
  1. Do two pre-review checks:
    * Ensure that the requester is in the "Committers" team (which means they've signed the CLA), otherwise direct them to the instructions in the README.
    * Ensure that the correct target branch (usually "develop") has been selected to merge the branch into.
  1. If you want to CC additional reviewers, you can do so using "/cc @username". Say why you're adding them.

## Doing the review

  1. Look out for the following things:
    * Do you understand what the code is doing? If not, it's probably the writer's fault, and you should tell him/her so.
    * Is the code doing the right thing?
    * Does the design look sensible?
    * Are there tests/docs which should be present, but aren't?
    * If the change affects the UI, check out the branch and look at it in a browser. Does the UI look good and intuitive to the user?

  **Note**: To checkout branch BRANCH_NAME from committer COMMITTER_USERNAME to your local machine, run:
  ```
    git checkout -b {{COMMITTER_NAME}}-{{BRANCH_NAME}} develop
    git pull https://github.com/{{COMMITTER_NAME}}/oppia.git {{BRANCH_NAME}}
  ```
  See also [Checking out pull requests locally](https://help.github.com/articles/checking-out-pull-requests-locally/).

  1. After submitting the review, set the Assignee field to the developer's GitHub username, so that they know it's their turn.

  1. If the developer pushes subsequent commits to the pull request, you'll automatically be notified by email. When you review these, make sure that all previous review comments have been addressed (both in the code and by the developer's replies.)

  1. If all review comments have been addressed, and the code looks good and is ready to be merged into develop, write a comment saying "LGTM".

## Merging into develop

### Squash-Merging

_Note that only maintainers and project leads can merge PRs into develop._

If all commits in a PR are done by a single committer, we recommend using GitHub's 'Squash-Merge' functionality, which you can select as an option after clicking the green "Merge pull request" button. This allows the history of both the author and maintainer who merged it to be retained, while doing a standard squash of all the changes in the PR to a single commit.

The commit message of the squash should be a clear one-line summary of the changes introduced in the PR. It should begin with a present-tense, transitive verb. Here are some examples of good commit messages:
* ``Fix #bugnum: introduce the first version of the collection editor.``
* ``Update the exploration editor to do X better.``

Getting this message correct is important, since it will be used to compile the CHANGELOG during the next release. If you like, feel free to also add optional follow-up sentences after the one-line summary.

### Standard Merging

There are special circumstances when standard merging should be done instead of a squash-merge. Generally speaking, commits which have already been squash-merged should not be squash-merged again. Also, if there are multiple contributors who have contributed to a PR, please don't squash-merge -- we want to preserve their history.