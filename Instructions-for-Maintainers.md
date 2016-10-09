## Maintainer responsibilities
- At the start of your shift, audit all existing issues that have someone assigned to them, and make sure that none are being sat on for too long. Deassign the issue from the current assignee if there's been no indication of progress or response to pings for > 7 days.
- Look at the list of [blocker bugs](https://github.com/oppia/oppia/milestone/39) and ensure that they are being worked on. Blocker bugs mean that the next release cannot happen without resolving these.
- Triage incoming issues/PRs and welcome new contributors (see [rota](https://github.com/oppia/oppia/wiki/Instructions-for-Maintainers#rota-for-triaging-issuesprs-and-welcoming-new-contributors) below)
- Do code reviews
- Within your given area of responsibility:
  - Figure out what needs to get done
  - Ensure progress is being made
  - Ensure that contributors aren’t blocked. If you can't easily solve a problem, feel free to escalate it to a tech lead or another maintainer.

### General
1. Ensure that your "Settings > Notification center" page is set to send you activity notifications, so that you're aware of all activity on the repository.
2. When you get an email saying that a pull request has been made, go to GitHub and assign it to someone. Before doing so, ensure that the requester is a member of the Committers team (which means they've signed the CLA).

### Doing code reviews
Please see [Instructions for Reviewers](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers) (note the [squash-merging instructions](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers#merging-into-develop) too).

### Handling incoming issues
1. Tidy up the title, if necessary.
2. Ensure that the issue has one of each of the following labels:
  * a team
  * a location (frontend/backend/full-stack)
  * a type (bug/feature)
  * a TODO describing the type of work needed, and the stage that the issue is in. If the TODO is a light green tag, also add a separate 'starter project' tag (see below for more information about why).
3. (Optional) It may also be helpful to add a list of checkboxes that describe the issue's sub-steps.
4. (Optional) If the issue has a design doc associated with it, add a link to the design doc.

You can find issues which need to have labels applied to them using [this link](https://github.com/oppia/oppia/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20-label%3A%22type%3A%20bug%20(major)%22%20-label%3A%22type%3A%20bug%20(minor)%22%20-label%3A%22type%3A%20feature%20(important)%22%20-label%3A%22type%3A%20feature%20(minor)%22%20-label%3A%22type%3A%20infrastructure%22%20-label%3A%22TODO%3A%20triage%22%20). We want that list to be empty as often as possible.

**Note:** you do not need to assign a milestone, unless you know what you're doing! Milestones are for explicit tracking of certain high-priority issues. They do not need to be applied to all issues.

#### Assigning TODO labels
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

**Note:** We list our 'starter project' issues on [OpenHatch](http://www.openhatch.org), and have told OpenHatch that the 'starter project' label corresponds to our starter projects. This is why the 'starter project' tag is added to issues with TODO: design (UI/Interaction), TODO: design (usability) and TODO: code.

#### Assigning the type of an issue
To label the type of an issue, please follow the following guidelines:
* (Bug or feature) Something is a *bug* if it breaks existing functionality that is expected to work in a particular way, but that doesn’t work. It is a *feature* if it’s a new thing. For the sake of consistency, writing a test should be considered a bug.
* (Important bug or minor bug) Important bugs lie along user journeys that are accessed frequently, and fixing these result in significant improvements in usability etc. Minor bugs are things like UI fixes that aren't that frequently seen. 
* (Important feature or minor feature) Important features are those that are in line with our strategy, i.e. they are in line with our current priorities. Minor features are nice to have, but not being prioritized.
* (Infrastructure) Infrastructure issues are those which don't quite fall under the purview of either features or issues. For instance, performing refactoring work, cleaning up code, or introducing new tests would fall under the infrastructure type.

#### Blocking bugs
There is also a [blocking bugs milestone](https://github.com/oppia/oppia/milestone/39) where we keep track of bugs which we use to keep track of blocking bugs. This milestone is different from the regular milestones, in that it has no due date and the goal is to keep it at 100% done. Blocking bugs are bugs which impact core creator/learner functionality, or regressions (i.e. break current functionality). A release cannot happen without all current blocking bugs being resolved, and some of these bugs may need hotfixes. 

If you encounter such a bug, please add it to the milestone! At the start of your maintainer rotation, please check that all blocking bugs (if any) are being actively worked on. If a bug is not actively being worked on, you could take on the bug yourself, find someone to do it, ask the maintainer in charge of the area the bug is in, or escalate it to the tech leads.

### Branch name conventions

In general, we use the gitflow workflow. This uses several special branches:

  * develop: this is the central branch for development, which should be clean and ready for release at any time
  * master: this is the branch that the production server at [Oppia.org](https://www.oppia.org) is synced to
  * "hotfix"-prefixed branches: these are used for hotfixes to master that can't wait until the next release
  * "release"-prefixed branches: these are used for testing and QA of new releases

### Large feature branching

When contributors are working on a sufficiently large feature (like a new editor) or multiple contributors are working on a single feature, they should have a single feature branch to contain the entirety of the new feature (or a minimal viable version of it), but they should not commit directly to `develop`. Essentially, `develop` should never be in a bad state.

If a feature cannot be broken down to fit comfortable in one PR, then it needs to be built-up in pieces. Each piece of the feature can instead be developed and PR-merged into a consolidated feature branch. That feature branch may not always be in a good state, but that's fine. Once the feature is sufficiently completed, then that branch can be merged into `develop`, keeping `develop` in a good state while ensuring the development of the feature is not too difficult to manage.

For instance, if we wanted to create a new editor for creating a custom creator landing page then we would want to make sure the project is sufficiently broken down. We could have a branch called ``creator-landing-page-editor`` to contain all of the changes. Certain sub-parts to this project like ``creator-landing-page-editor-settings-tab`` would have their own branches. When the settings tab work is completed, a pull request will be created to merge the settings tab branch into the main landing page editor branch. This is done with standard [squash merging](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers#squash-merging). Once all of the sub-parts of the landing page editor are completed, the ``creator-landing-page-editor`` branch can be merged into ``develop``. This is done with [standard merging](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers#standard-merging) instead of squash-merging, since all the commits have been created by squash-merges and we should retain development history for this branch.

Note that all sub-feature branches (like ``creator-landing-page-editor-settings-tab``) should be branched off of ``creator-landing-page-editor``, not ``develop``. Sometimes the main feature branch may need to be brought up-to-date with ``develop`` to avoid code skew and complicated merges later on, but this is up to the discretion of the contributors.

----

## Maintainer Rota

```
 3 Oct -  9 Oct   Jacob
10 Oct - 16 Oct   Madiyar
17 Oct - 23 Oct   Kevin
24 Oct - 30 Oct   Barnabas
31 Oct -  6 Nov   Prasanna
 7 Nov - 13 Nov   Xinyu
14 Nov - 20 Nov   Sourav
21 Nov - 27 Nov   Avijit
28 Nov -  4 Dec   Allan
 5 Dec - 11 Dec   Ben

12 Dec - 18 Dec   Madiyar
19 Dec - 25 Dec   Kevin
26 Dec -  1 Jan   Jacob
 2 Jan -  8 Jan   Barnabas
 9 Jan - 15 Jan   Prasanna
16 Jan - 22 Jan   Xinyu
23 Jan - 29 Jan   Sourav
30 Jan -  5 Feb   Avijit
 6 Feb - 12 Feb   Allan
13 Feb - 19 Feb   Ben

20 Feb - 26 Feb   Kevin
27 Feb -  5 Mar   Jacob
 6 Mar - 12 Mar   Madiyar
13 Mar - 19 Mar   Barnabas
20 Mar - 26 Mar   Xinyu
27 Mar -  2 Apr   Prasanna
```

## Areas of responsibility

```
Allan        Rich-text editor
Avijit       Creator dashboard
Barnabas     Iframed explorations
Ben          Answer handling, code health
Jacob        Metrics
Kevin        Collections, library index page
Madiyar      Learner view
Prasanna     Emails
Sean         Exploration editor
Sourav       Critical user journeys
Xinyu        Exploration saving and publishing
```
