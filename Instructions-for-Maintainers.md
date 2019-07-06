## Maintainer responsibilities
- If you cannot make your shift (see [rota](https://github.com/oppia/oppia/wiki/Instructions-for-Maintainers#maintainer-rota)), please swap with someone else **in advance**.
- **On Saturday, at the start of your shift**:
  - Pin this tab, so you have it handy for reference!
  - If you aren't already watching the repository, please change your [notification preferences](https://github.com/oppia/oppia/subscription) to "watching", just for this week.
  - Go to the [list of important issues](https://github.com/oppia/oppia/issues?q=is%3Aissue+is%3Aopen+label%3Aimportant). For any existing issue with an assignee, ping them and ask for a status update if there's been no response for 6-7 days. Deassign the issue from the current assignee if there's been no indication of progress or response to pings for > 10 days.
  - Do the same for projects without leads: [link 1](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+project%3Aoppia%2Foppia%2F22), [link 2](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+project%3Aoppia%2Foppia%2F21), [link 3](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+project%3Aoppia%2Foppia%2F20), [link 4](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+project%3Aoppia%2Foppia%2F12), [link 5](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+project%3Aoppia%2Foppia%2F1).
- **During the week**:
  - Make sure all incoming issues/PRs are triaged and labelled. Assign incoming PRs to the owners of the issue that's being fixed by the PR.
  - Ensure that all PRs have at least one assignee at any point of time. 
  - Ensure that all PRs have clear titles that start with "Fix #bugnum:" or "Fix part of #bugnum:", followed by a clear description. (This is important for generating the changelog during releases.)
  - Welcome and help out new contributors (e.g. on gitter).
  - Do code reviews for simple incoming PRs.
- **After your shift**:
  - Pass the baton to the next maintainer. In doing so, confirm that:
    - All issues have labels applied to them (i.e. [this list](https://github.com/oppia/oppia/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+no%3Alabel) should be empty).
    - All non-starter issues have project assignments (i.e. [this list](https://github.com/oppia/oppia/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20no%3Aproject) should only contain broken-down starter projects owned by **@shubha1593**).

  - [Optional] If you changed your notification preferences at the start of the shift, you might want to reset them to "not watching" so that you only get emails when you are @mentioned.

### General
1. Ensure that your "Settings > Notification center" page is set to send you activity notifications, so that you're aware of all activity on the repository.
2. When you get an email saying that a pull request has been made, go to GitHub and assign it to someone.

### Doing code reviews
Please see [Instructions for Reviewers](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers) (note the [squash-merging instructions](https://github.com/oppia/oppia/wiki/Instructions-for-Reviewers#merging-into-develop) too).

### Handling incoming issues
1. Tidy up the title, if necessary.
2. Ensure that the issue has one of each of the following:
   * a project assignment (if you're not sure which project it falls under, add "TODO: TRIAGE" and the tech leads will handle it).
   * a "talk-to" person (this usually matches the appropriate project lead)
   * a location (frontend/backend/full-stack)
3. (Optional) Add the following:
   * a "good first issue" label, if the issue seems like one that can be easily tackled by a new contributor. This tag gets automatically picked up by GitHub.
   * one of "needs UI design", "needs UX design", "needs design doc", "needs debugging", as appropriate.
   * a list of checkboxes describing the issue's sub-steps
   * a link to any design doc associated with the issue
4. Further, if you find an issue pertaining to setup which may be caused due to the local specifications of the developers' machine or that may not be fixed from our end (similar to [this](https://github.com/oppia/oppia/issues/5785) issue), please provide a general solution to the issue. You can redirect the developer to any answer found online (StackOverflow etc).   
**Note:** you do not need to assign a milestone, unless you know what you're doing! Milestones are for explicit tracking of certain high-priority issues.

Here are the meanings of the "needs X" labels:

* `needs UX design`: the way that the user interacts with this feature needs to be planned. The next thing to be done here is to outline the core user journeys (probably using a doc and/or screenshots), and discuss them on the issue thread, so that the feature can move forward.
* `needs UI design`: UI design is needed. In contrast to the "needs UX design" label, what needs to be done here is more localized, and typically means we already have an idea of how the user is going to interact with it. This should be suitable for new design contributors.
* `needs design doc`: means that the problem is known, but the solution needs fleshing out. The next thing to do is to prepare a short doc outlining the solution approach and implementation plan, add a link to it on the issue thread, then discuss it before starting implementation.
* `needs debugging`: something weird is going on, and we don't know exactly what the issue is. Some investigation is needed.

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
29 Jun -  5 Jul	  Apurv         @apb7
 6 Jul - 12 Jul	  Kevin         @kevinlee12
13 Jul - 19 Jul	  Sandeep       @DubeySandeep
20 Jul - 26 Jul	  Allan         @AllanYangZhou
27 Jul -  2 Aug	  Vojtěch       @vojtechjelinek
 3 Aug -  9 Aug	  Jacob         @jacobdavis11
10 Aug - 16 Aug	  Akshay        @aks681
17 Aug - 23 Aug	  Nithesh       @nithusha21
24 Aug - 30 Aug	  Apurv         @apb7 
31 Aug -  6 Sep   Ankita        @ankita240796
 7 Sep - 13 Sep	  Kevin         @kevinlee12
14 Sep - 20 Sep	  Sandeep       @DubeySandeep
21 Sep - 27 Sep	  Allan         @AllanYangZhou
28 Sep -  4 Oct	  Akshay        @aks681
 5 Oct - 11 Oct	  Jacob         @jacobdavis11
12 Oct - 18 Oct	  Allan         @AllanYangZhou
19 Oct - 25 Oct	  Nithesh       @nithusha21
26 Oct -  1 Nov	  Apurv         @apb7
 2 Nov -  8 Nov	  Ankita        @ankita240796
 9 Nov - 15 Nov	  Kevin         @kevinlee12
16 Nov - 22 Nov	  Sandeep       @DubeySandeep
23 Nov - 29 Nov	  Vojtěch       @vojtechjelinek
30 Nov - 6 Dec	  Akshay        @aks681
 7 Dec - 13 Dec	  Jacob         @jacobdavis11
14 Dec - 20 Dec	  Nithesh       @nithusha21
21 Dec - 27 Dec	  Apurv         @apb7
```

### Maintainer rota coordinator
**Duties of the maintainer rota coordinator:**
1. Ensure maintainer rotation is followed.
2. Send a ping/email to the maintainer reminding him/her of the rota if it has been missed. 

Current rota coordinator: Apurv

## Areas of expertise

```
Allan        Rich-text editor
Ankita       Production migration jobs, Angular migration, Dev workflow
Anmol        Machine learning
Apurv        Dev workflow
Akshay       Questions, skills, topics and stories
Ben          Migrations, Storage
Brian        Exploration statistics tab
Jacob        Metrics
Joe          Oppia's blog
Kevin L      Embedding, collection editor, library index page
Mark         General UI design, mathematics lessons
Nitish       Rich-text editor
Nithesh      Suggestions, Questions
Prasanna     Machine learning
Rachel       User research
Sandeep      Starter projects, Audio translation
Tony         Learner experience
Vojtěch      Speed Improvement
Sean         Everything else
```

***

### How to clear caches for CIs?

We've observed cases in the past where the cache got corrupted leading to build failures for the develop branch and PRs
If you suspect that PR builds are failing for no apparent reasons, then clearing the cache might fix the builds. In such cases, please ping **Apurv (@apb7)** first. If he's not available at the moment, please follow these instructions to clear build cache.

**Travis CI**
1. Go to [https://travis-ci.org/oppia/oppia/caches](https://travis-ci.org/oppia/oppia/caches).
2. You can either delete all repository caches by clicking on `Delete all repository caches` or delete cache for a particular PR by clicking on the `Bin` icon at the end of that PR's row.
 
**Circle CI**
Clearing cache for builds on CircleCI is not straight forward like Travis CI. Therefore, CircleCI caches are re-built each day. If you think that the problem still persists, then please follow these steps:

1. Create a PR with all `restore_cache` steps commented out in [`.circleci/config.yml`](https://github.com/oppia/oppia/blob/develop/.circleci/config.yml). Basically, comment out the following lines in the above-mentioned config file: [L26-27](https://github.com/oppia/oppia/blob/develop/.circleci/config.yml#L26-L27), [L41-42](https://github.com/oppia/oppia/blob/develop/.circleci/config.yml#L41-L42), [L59-60](https://github.com/oppia/oppia/blob/develop/.circleci/config.yml#L59-L60) and [L77-78](https://github.com/oppia/oppia/blob/develop/.circleci/config.yml#L77-L78).
2. If the problem is actually with the cache, the PR should be build flawlessly.
3. If the PR is indeed built successfully, merge this PR into develop to unblock PRs.
