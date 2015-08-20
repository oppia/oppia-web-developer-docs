Code review is an important part of the Oppia development cycle. Having a second pair of eyes look at your code can help to catch silly mistakes and serve as a check for whether your code is readable/understandable by other team members (which is important for maintainability).

When you receive a code review request, please try to do the review as soon as possible! Otherwise, the submitter will be blocked.

## When you first receive a review request

  1. When you get an email saying a pull request issue has been assigned to you for review, click on the link to open it in GitHub. (You may need to open the issue on GitHub to see if it is a pull request or not.)
  2. Do two pre-review checks:
    * Ensure that the requester is in the "Committers" team (which means they've signed the CLA), otherwise direct them to the instructions in the README.
    * Ensure that the correct target branch (usually "develop") has been selected to merge the branch into.
  3. Add the "IN REVIEW" label to the issue.
  4. If you want to CC additional reviewers, you can do so using "/cc @username". Say why you're adding them.

## Doing the review

  5. Perform the code review. Here are some things to look for:
    * Do you understand what the code is doing? If not, it's probably the writer's fault, and you should tell him/her so.
    * Is the code doing the right thing?
    * Does the design look sensible?
    * Are there tests/docs which should be present, but aren't?
    * If the change affects the UI, check out the branch and look at it in a browser. Does the UI look good and intuitive to the user? (To checkout a branch to your local machine, follow [https://help.github.com/articles/checking-out-pull-requests-locally/](these instructions) -- basically, just click "command line" on the pull request page and follow the given steps.)

  6. If the developer pushes subsequent commits to the pull request, you'll automatically be notified by email. When you review these, make sure that all previous review comments have been addressed (both in the code and by the developer's replies.)

  7. If all review comments have been addressed, and the code looks good and is ready to be merged into develop, remove the "IN REVIEW" label and replace it with the "LGTM" label, then click “Merge pull request”. Before doing this, ensure that the developer resolves any merge conflicts (which GitHub will warn you about).
