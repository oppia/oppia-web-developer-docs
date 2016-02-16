## General
1. Ensure that you’re watching all activity on the repository, and that your "Settings > Notification center" page is set to send you activity notifications.
2. When you get an email saying that a pull request has been made, go to GitHub and assign it to someone. Before doing so, ensure that the requester is a member of the Committers team (which means they've signed the CLA).

## To add a new committer
1. Ensure that the person has signed the appropriate CLA.
2. Go to Settings > Collaborators, and then add that collaborator.

## Conducting a code review
1. Please see the instructions at https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers

## Merging a Pull Request
Please ensure that the merge commit message
1. Starts with 'Fix #XXX' if it is fixing an issue. This will automatically close the issue.
2. Describes the changes that were merged

## When a new issue is filed
1. Tidy up the title, if necessary.
2. Ensure that the issue has one of each of the following labels:
  * a team
  * a type (bug/feature)
  * a TODO describing the type of work needed, and the stage that the issue is in. If the TODO is a light green tag, also add a separate 'starter project' tag (see below for more information about why).
3. (Optional) It may also be helpful to add a list of checkboxes that describe the issue's sub-steps.

**Note:** you do not need to assign a milestone, unless you know what you're doing! Milestones are for explicit tracking of certain high-priority issues. They do not need to be applied to all issues.

The TODO labels represent what help the issue needs in order to move forward. This helps people find something they want to do, and also helps us track the progress of issues. The rough sequence of labels is as follows (but note that not all of these will be part of the workflow for every issue):

* `triage`: we need to discuss whether we are going to address this issue.
* `design (UX)`: we need to design the user journey
* `design (breakdown)`: this issue needs to be broken down into single-person tasks.
* `design (UI/Interaction)`: UI design is needed. In contrast to the TODO: design (UX) label, what needs to be done here is more localized, and typically means we already have an idea of how the user is going to interact with it. This should be suitable for new design contributors.
* `design (usability)`: usability testing is needed. This should be suitable for new user research contributors.
* `tech (design doc)`: we need to create a technical design doc that describes how to resolve the issue.
* `tech (breakdown)`: a design doc/detailed steps is completed, but we need to break them into single-person chunks.
* `tech (instructions)`: the overall solution is generally known, but newcomers to the codebase may need additional instructions (e.g. which files are relevant) to be able to implement them.
* `code`: the overall solution is known and is described in the issue, and the only thing left to do is code it. This issue should be suitable for new developers.

## Note on changing label names
We're listing our 'starter project' issues on [OpenHatch](http://www.openhatch.org), and have told OpenHatch that the 'starter project' label corresponds to our starter projects. This is why the 'starter project' tag is added to issues with TODO: design (UI/Interaction), TODO: design (usability) and TODO: code.

## Reference: branch conventions

In general, we use the gitflow workflow. This uses several special branches:

  * develop: this is the central branch for development, which should be clean and ready for release at any time
  * master: this is the branch that the production server at [Oppia.org](https://www.oppia.org) is synced to
  * "hotfix"-prefixed branches: these are used for hotfixes to master that can't wait until the next release
  * "release"-prefixed branches: these are used for testing and QA of new releases
