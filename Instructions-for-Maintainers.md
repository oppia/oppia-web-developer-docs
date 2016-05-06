## Maintainer duties
- Participate in triaging issues/PRs (see [rota](https://github.com/oppia/oppia/wiki/Instructions-for-Maintainers#rota-for-triaging-issuesprs) below)
- Do code reviews
- Within your given area of responsibility:
  - Figure out what needs to get done
  - Ensure progress is being made
  - Ensure that contributors aren’t blocked. If you can't easily solve a problem, feel free to escalate it to a tech lead or another maintainer

## General
1. Please ensure that your "Settings > Notification center" page is set to send you activity notifications, so that you're aware of all activity on the repository.
2. When you get an email saying that a pull request has been made, go to GitHub and assign it to someone. Before doing so, ensure that the requester is a member of the Committers team (which means they've signed the CLA).

## To add a new committer
1. Ensure that the person has signed the appropriate CLA.
2. Go to Settings > Collaborators, and then add that collaborator.

## Conducting a code review
Please see [Instructions for Reviewers](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers). Note the [squash-merging instructions](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers#merging-into-develop), too.

## When a new issue is filed
1. Tidy up the title, if necessary.
2. Ensure that the issue has one of each of the following labels:
  * a team
  * a type (bug/feature)
  * a TODO describing the type of work needed, and the stage that the issue is in. If the TODO is a light green tag, also add a separate 'starter project' tag (see below for more information about why).
3. (Optional) It may also be helpful to add a list of checkboxes that describe the issue's sub-steps.
4. (Optional) If the issue has a design doc associated with it, add a link to the design doc.

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

Due to changes to Git, we are going to start allowing committers to create new branches on the public Oppia Git repository. This involves creating a feature branch off of oppia:develop and under the Oppia repository. Although the gitflow workflow works well, there have been many headaches associated with keeping forked repositories synchronized with the original repository. Although PRs created through the gitflow workflow are still accepted, we want to start moving developers over to using the Google Code approach we used before moving to GitHub.

### Large feature branching

When contributors are working on a sufficiently large feature (like a new editor) or multiple contributors are working on a single feature, they should have a single feature branch to contain the entirety of the new feature (or a minimal viable version of it), but they should not commit directly to this branch. Essentially, develop should never be in a bad state. If a feature cannot be broken down to fit comfortable in one PR, then it needs to be built-up in pieces. Each piece of the feature can instead be developed and PR-merged into a consolidated feature branch. That feature branch may not always be in a good state, but that's fine. Once the feature is sufficiently completed, then that branch can be merged into develop, keeping develop in a good state while ensuring the development of the feature is not too difficult to manage.

For instance, if we wanted to create a new editor for creating a custom creator landing page then we would want to make sure the project is sufficiently broken down. We could have a branch called ``creator-landing-page-editor`` to contain all of the changes. Certain sub-parts to this project like ``creator-landing-page-editor-settings-tab`` would have their own branches. When the settings tab work is completed, a pull request will be created to merge the settings tab branch into the main landing page editor branch. This is done with standard [squash merging](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers#squash-merging). Once all of the sub-parts of the landing page editor is completed, the ``creator-landing-page-editor`` branch will be requested to be merged into ``develop``. This is done with [standard merging](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers#standard-merging) instead of squash-merging, since all the commits have been created by squash-merges and we should retain development history for this branch.

It's worth pointing out that all sub-feature branches (like ``creator-landing-page-editor-settings-tab``) should be branched off of ``creator-landing-page-editor``, not ``develop``. Sometimes the main feature branch may need to be brought up-to-date with ``develop`` to avoid code skew and complicated merges later on, but this is up to the discretion of the contributors.

----

## Rota for triaging issues/PRs

```
9 May - 15 May    Sean
16 May - 22 May   Jacob
23 May - 29 May   Allan
30 May - 5 Jun    Kevin
6 Jun - 12 Jun    Ben
13 Jun - 19 Jun   Barnabas
20 Jun - 26 Jun   Bren
27 Jun - 3 Jul    Madiyar
4 Jul - 10 Jul    Xinyu
	
11 Jul - 17 Jul   Allan
18 Jul - 24 Jul   Sean
25 Jul - 31 Jul   Kevin
1 Aug - 7 Aug     Ben
8 Aug - 14 Aug    Madiyar
15 Aug - 21 Aug   Barnabas
22 Aug - 28 Aug   Jacob
29 Aug - 4 Sep    Bren
5 Sep - 11 Sep    Xinyu
	
12 Sep - 18 Sep   Allan
19 Sep - 25 Sep   Kevin
26 Sep - 2 Oct    Bren
3 Oct - 9 Oct     Jacob
10 Oct - 16 Oct   Madiyar
17 Oct - 23 Oct   Barnabas
24 Oct - 30 Oct   Xinyu
```

## Areas of responsibility

```
Allan: rich-text editor
Barnabas: iframed explorations
Ben: answer handling; collections
Bren: devops
Jacob: TBD
Kevin: TBD
Madiyar: TBD
Xinyu: TBD
Sean: exploration editor
```
