## General
1. Ensure that you’re watching all activity on the repository, and that your "Settings > Notification center" page is set to send you activity notifications.
2. When you get an email saying that a pull request has been made, go to GitHub and assign it to someone. Before doing so, ensure that the requester is a member of the Committers team (which means they've signed the CLA).

## To add a new committer
1. Ensure that the person has signed the appropriate CLA.
2. Go to Settings > Collaborators, and then add that collaborator.

## When a new issue is filed
1. Tidy up the title, if necessary.
2. Ensure that the issue has one of each of the following labels:
  * a team
  * a type (bug/feature)
  * a TODO describing the type of work needed, and the stage that the issue is in.
3. (Occasionally) Assign a milestone. Note that milestones are meant to track progress towards goals we have defined, and not every issue filed against a component should be assigned to a milestone regarding that component. Please consult with the people in charge of that milestone if you feel that an issue should be included in that milestone.

The TODO labels represent the bug/suggested feature's stage of development. This means that an issue will be assigned a tag based on how far along it is from reaching production. The intention is for people to be able to find something they want to do easily, and also for us to be able to track the progress of issues. Not all tags are part of the process of every bug, and someone may advance a bug by more than 1 step when working on it. There should only be 1 tag on the issue. It should should reflect the current public state of the issue, i.e. if someone takes up the issue now, what needs to be done? In the issue description, it may also be helpful to list future steps using checkboxes. 

For reference, here are the TODO tags and descriptions:
* TODO: triage means we need to discuss whether we are going to address this issue.
* TODO: design (UX) means we need to design the user journey
* TODO: design (breakdown) means this issue needs to be broken down into single-person tasks.
* TODO: design (UI/Interaction) means UI design is needed. In contrast to the TODO: design (UX) label, what needs to be done here is more localized, and typically means we already have an idea of how the user is going to interact with it. This should be suitable for new contributors who are designers.
* TODO: design (usability) means usability testing is needed. This should be suitable for new contributors who are researchers.
* TODO: tech (design doc) means we need to create a technical design doc that describes how to resolve the issue.
* TODO: tech (breakdown) means a design doc/detailed steps is completed, but we need to break them into single-person chunks.
* TODO: tech (instructions) means that the overall solution is generally known, but newcomers to the codebase may need additional instructions (e.g. which files are relevant) to be able to implement them.
* TODO: code means that the overall solution is known and is described in the issue, and the only thing left to do is code it. This issue should be suitable for developers new to the codebase.

## Note on changing label names
We're listing our 'starter project' issues on [OpenHatch](http://www.openhatch.org), and in order to do that, we needed to give them the names of the labels to look at. Changing the 'starter project' label name can break this. This is also why the 'starter project' tag is added to issues with TODO: design (UI/Interaction), TODO: design (usability) and TODO: code.

## Reference: branch conventions

In general, we use the gitflow workflow. This uses several special branches:

  * develop: this is the central branch for development, which should be clean and ready for release at any time
  * master: this is the branch that the production server at [Oppia.org](https://www.oppia.org) is synced to
  * "hotfix"-prefixed branches: these are used for hotfixes to master that can't wait until the next release
  * "release"-prefixed branches: these are used for testing and QA of new releases
