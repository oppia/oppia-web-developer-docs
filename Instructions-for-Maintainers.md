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
We're listing our 'starter project' issues on [OpenHatch](http://www.openhatch.org), and in order to do that, we needed to give them the names of the labels to look at. Changing label names may cause this to break, so please check with @seanlip before you do that!

## Reference: branch conventions

In general, we use the gitflow workflow. This uses several special branches:

  * develop: this is the central branch for development, which should be clean and ready for release at any time
  * master: this is the branch that the production server at [Oppia.org](https://www.oppia.org) is synced to
  * "hotfix"-prefixed branches: these are used for hotfixes to master that can't wait until the next release
  * "release"-prefixed branches: these are used for testing and QA of new releases
