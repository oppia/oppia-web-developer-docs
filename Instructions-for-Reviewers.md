Code review is an important part of the Oppia development cycle. Having a second pair of eyes look at your code can help to catch silly mistakes and serve as a check for whether your code is readable/understandable by other team members (which is important for maintainability).

When you receive a code review request, please try to do the review as soon as possible! Otherwise, the submitter will be blocked.

## When you first receive a review request

  1. When you get an email saying a pull request issue has been assigned to you for review, click on the link to open it in GitHub. (You may need to open the issue on GitHub to see if it is a pull request or not.)
  1. Do two pre-review checks:
    * Ensure that the requester is in the "Committers" team (which means they've signed the CLA), otherwise direct them to the instructions in the README.
    * Ensure that the correct target branch (usually "develop") has been selected to merge the branch into.
  1. If you want to CC additional reviewers, you can do so using "/cc @username". Say why you're adding them.

## Doing the review

  1. Perform the code review. Here are some things to look for:
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

  1. If the developer pushes subsequent commits to the pull request, you'll automatically be notified by email. When you review these, make sure that all previous review comments have been addressed (both in the code and by the developer's replies.)

  1. If all review comments have been addressed, and the code looks good and is ready to be merged into develop, write a comment saying "LGTM".

## Merging into develop

### Squash-Merging

Only maintainers can merge PRs into develop. Due to changes to Git, we are preferring that maintainers use the 'Squash-Merge' functionality. This is a clever feature of GitHub which allows the history of both the author and maintainer who merged it to be retained, while doing a standard squash of all the changes in the PR to a single commit. Maintainers should make sure the commit message of this squash is a strong one-line summary of the changes introduced in the PR. As is standard Git commit message convention, the squash message should begin with a present-tense, transitive verb. For instance:

``Introduces the first version of the collection editor.``

``Fixes #bugnum.`` or ``Fix #bugnum.``

``Updates the exploration editor to do X better.``

The message is describing in what way the PR is changing Oppia. Feel free to add follow-up sentences after the one-line summary, though those are optional. The one-line summary is what will be used when the PR is being added to the CHANGELOG during the next release.\

### Standard Merging

There are special circumstances when standard merging should be done instead of a squash-merge. The possible situations cannot be enumerated here. However, commits which have already been squash merged should not be squash merged again. For instance, a PR which is a major feature branch with several squash-merged commits should not itself be squash merged. We want to retain the history of all those squash-merges, so a standard merge suffices in this situation.