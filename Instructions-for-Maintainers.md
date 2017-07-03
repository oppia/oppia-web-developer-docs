## Maintainer responsibilities
- **At the start of your shift** (see [rota](https://github.com/oppia/oppia/wiki/Instructions-for-Maintainers#maintainer-rota)):
  - if you aren't already watching the repository, please change your [notification preferences](https://github.com/oppia/oppia/subscription) to "watching", just for this week.
  - go to the [list of PRs](https://github.com/oppia/oppia/pulls), and make sure all PRs are moving forward; act on any that are being sat on for too long. Also, ensure that the PR's "assignee" is the person who's supposed to next act on it (usually, this would be either the committer or the reviewer). **Please do this before looking at the issue tracker in the next step, since some issues will have PRs already in progress (and GitHub doesn't always make this clear).**
  - go to the [list of recommended issues](https://github.com/oppia/oppia/milestone/42). For any existing issue with an assignee, ping them and ask for a status update if there's been no response for 6-7 days. Deassign the issue from the current assignee if there's been no indication of progress or response to pings for > 14 days.
- **During the week**:
  - Make sure all incoming issues/PRs are triaged and labelled. In particular, ensure that incoming PRs are assigned to the owners of the issue that's being fixed by the PR.
  - Welcome new contributors (e.g. on gitter).
  - Do code reviews for simple incoming PRs.
- **After your shift**:
  - [Optional] If you changed your notification preferences at the start of the shift, you might want to reset them to "not watching" so that you only get emails when you are @mentioned.

### General
1. Ensure that your "Settings > Notification center" page is set to send you activity notifications, so that you're aware of all activity on the repository.
2. When you get an email saying that a pull request has been made, go to GitHub and assign it to someone. Before doing so, ensure that the requester has signed the CLA). To check this, look for the "Member" **or** "Collaborator" tag next to their name. For example:
[[images/memberTagExample.png]]

### Doing code reviews
Please see [Instructions for Reviewers](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers) (note the [squash-merging instructions](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers#merging-into-develop) too).

### Handling incoming issues
1. Tidy up the title, if necessary.
2. Ensure that the issue has one of each of the following labels:
  * an owner
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
* `design (UX)`: the way that the user interacts with this feature needs to be planned. The next thing to be done here is to outline the core user journeys (probably using a doc and/or screenshots), and discuss them on the issue thread, so that the feature can move forward.
* `design (UI)`: UI design is needed. In contrast to the TODO: design (UX) label, what needs to be done here is more localized, and typically means we already have an idea of how the user is going to interact with it. This should be suitable for new design contributors.
* `tech (design doc)`: means that the problem is known, but the solution needs fleshing out. The next thing to do is to prepare a short doc outlining the solution approach and implementation plan, add a link to it on the issue thread, then discuss it before starting implementation.
* `tech (breakdown)`: a design doc/detailed steps is completed, but we need to break them into single-person chunks.
* `tech (instructions)`: the overall solution is generally known, but newcomers to the codebase may need additional instructions (e.g. which files are relevant) to be able to implement them. Adding instructions, such as where to make the necessary changes, will help move these issues to the `TODO: code` stage.
* `code`: the overall solution is known and is described in the issue, and the only thing left to do is code it. This issue should be suitable for new developers.

**Note:** We list our 'starter project' issues on [OpenHatch](http://www.openhatch.org), and have told OpenHatch that the 'starter project' label corresponds to our starter projects. This is why the 'starter project' tag is added to issues with TODO: design (UI) and TODO: code.

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
26 Jun -  2 Jul   Avijit        @526avijitgupta
 3 Jul -  9 Jul   Allan         @AllanYangZhou

10 Jul - 16 Jul   Jacob         @jacobdavis11
17 Jul - 23 Jul   Prasanna      @prasanna08
24 Jul - 30 Jul   Allan         @AllanYangZhou
31 Jul -  6 Aug   Kristin       @anthkris
 7 Aug - 13 Aug   Barnabas      @MAKOSCAFEE
14 Aug - 20 Aug   Kevin         @kevinlee12
21 Aug - 27 Aug   Allan         @AllanYangZhou
28 Aug -  3 Sep   Sean          @seanlip
 4 Sep - 10 Sep   Xinyu         @wxyxinyu
11 Sep - 17 Sep   Tony          @tjiang11

18 Sep - 24 Sep   Anmol         @anmolshkl
25 Sep -  1 Oct   Prasanna      @prasanna08
 2 Oct -  8 Oct   Barnabas      @MAKOSCAFEE
 9 Oct - 15 Oct   Sean          @seanlip
16 Oct - 22 Oct   Tony          @tjiang11
23 Oct - 29 Oct   Kristin       @anthkris
30 Oct -  5 Nov   Jacob         @jacobdavis11
 6 Nov - 12 Nov   Xinyu         @wxyxinyu   
13 Nov - 19 Nov   Anmol         @anmolshkl
20 Nov - 26 Nov   Prasanna      @prasanna08

27 Nov -  3 Dec   Barnabas      @MAKOSCAFEE
 4 Dec - 10 Dec   Sean          @seanlip
11 Dec - 17 Dec   Jacob         @jacobdavis11
18 Dec - 24 Dec   Kevin         @kevinlee12
25 Dec - 31 Dec   Tony          @tjiang11
```

## Areas of expertise

```
Allan        Rich-text editor, suggestions
Anmol        Machine learning
Arunabh      Subscriptions, learner dashboard, general frontend
Barnabas     Iframed explorations
Ben          Answer handling, frontend refactoring, backend migrations
Corey        Mobile frontend
Himanshu     Simple editor
Jacob        Metrics
Jared        User journeys
Kevin L      Collection editor, library index page
Kevin T      Collection viewer, hints
Kristin      Accessibility
Mark         General UI design, mathematics lessons
Prasanna     Emails, machine learning
Rachel       User research
Tony         Learner view (both collections and explorations)
Vojtěch      Speed
Xinyu        Exploration saving/publishing, editor history tab, release process
Sean         Everything else
```
