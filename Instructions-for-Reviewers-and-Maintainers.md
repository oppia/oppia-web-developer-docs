# Instructions for Reviewers

## When you first receive a review request

1. When you get an email saying a pull request issue has been assigned to you for review, click on the link to open it in GitHub. (You may need to open the issue on GitHub to see if it is a pull request or not.)
2. Do two pre-review checks:
  * Ensure that the requester is in the "Committers" team (which means they've signed the CLA), otherwise direct them to the instructions in the README.
  * Ensure that the correct target branch (usually "develop") has been selected to merge the branch into.
3. Add the "IN REVIEW" label to the issue.
4. If you want to CC additional reviewers, you can do so using "/cc @username". Say why you're adding them.

## Doing the review

5. Perform the code review.
  * If you want to checkout the branch and run on your local machine, follow the instructions [https://help.github.com/articles/checking-out-pull-requests-locally/](here). (Basically, just click "command line" on the pull request page, and follow the given steps.)

6. If the developer pushes subsequent commits to the pull request, you'll automatically be notified by email. When you review these, make sure that all previous review comments have been addressed (both in the code and by the developer's replies.)
  
7. If all review comments have been addressed, and the code looks good and is ready to be merged into develop, remove the "IN REVIEW" label and replace it with the "LGTM" label, then click “Merge pull request”. Before doing this, ensure that the developer resolves any merge conflicts (which GitHub will warn you about).

# Instructions for Maintainers

## General
1. Ensure that you’re watching all activity on the repository, and that your "Settings > Notification center" page is set to send you activity notifications.
2. When you get an email saying that a pull request has been made, go to GitHub and assign it to someone. Before doing so, ensure that the requester is a member of the Committers team (which means they've signed the CLA).

## To add a new committer
1. Ensure that the person has signed the appropriate CLA.
2. Go to Settings > Collaborators, and then add that collaborator.

## When a new issue is filed
1. Tidy up the title, if necessary.
2. Add the issue to a milestone. (You can create a new milestone if necessary. Just keep its name short).
3. Ensure that the issue has the following labels:
  * a code reference
  * a type (bug/feature/refactor)
  * a TODO describing the type of work needed.
  * a 'starter project' label, if the issue would be a suitable starter project for new contributors. In this case, add a comment to the issue providing clear instructions on what to do (referencing files if necessary).

## Note on changing label names
We're listing our 'starter project' issues on [http://www.openhatch.org](OpenHatch), and in order to do that, we needed to give them the names of the labels to look at. Changing label names may cause this to break, so please check with @seanlip before you do that!