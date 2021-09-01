# Schedule
**The Friday before the first Saturday of each month**: Release branch gets created. Push the release branch onto a test server.
Features merged into `develop` after this date will only go out in the following release. 

The Friday before the first Saturday of each month is the soft deadline for the start of the release. The release cut should be made on the soft deadline if there is no PR that needs to get into the release. If there is some PR that needs to get into the release, the release cut can be delayed. The maximum delay for the release cut is one week, so the Friday before the second Saturday of each month is the hard deadline for the release cut. In between the soft and the hard deadline the release coordinator is the person that decides when the release should happen exactly.

**First weekend of each month**: The release team will focus on testing. Typically the testing deadline is chosen to be the Monday after the weekend. The testing should be completed by the deadline. All bugs caught should be filed as blocking bugs on Github, and should be assigned to a bugfixer ASAP.

**Second weekend of each month**: The release/QA team and the project leads council will focus on fixing the reported bugs. By the Monday after the second weekend, the bug-fixing phase should be completed.

**Third week of each month**: First the fixes will be cherrypicked and deployed to the test server, and then we test that the bugs are fixed on the test server. Once this verification is complete, we can go ahead with the next step. 

**Third weekend of each month**: The release will be made and an update will be pushed to the live site.

# Instructions for deciding whether a bug is blocking

Bugs reported during a release fall under two categories: Blocking & Non-blocking. The release coordinator and QA coordinator are responsible for deciding, in a timely manner, which bugs should block the release. To make this decision, the following rules should be followed:

1. **Interference with Critical Journeys**: If a bug prevents a user from completing any of the critical user journeys, it should block the release. This requirement should only be overridden in the most extreme circumstances. For example, if a bug prevents the publication of new explorations, it should block the release.

2. **Confusing User Interface**: If a bug results in a confusing or unintuitive user interface, especially for critical user journeys, that bug should block the release. This requirement should be overridden only in the most extreme circumstances. For example, a bug that swaps the labels of the "Create" and "Learn" buttons in the top menu bar should not be allowed to go live.

3. **Poor Aesthetics**: If a bug results in a poor aesthetic appearance, the bug should probably block the release. A common example is a CSS issue that causes text to extend beyond a box or page elements to overlap. Such a bug should normally block a release, except perhaps when the problem is so obscure that users are highly unlikely to encounter it.

4. **Problems with Live Behaviour**: If the discovered bug is already live, whether the bug should block the release depends on how established the live behaviour is:

    * **Behaviour is Long-Standing**: In this case, the bug is probably more of a feature request. The existing behaviour has been live for a while, so a deployment without fixing the bug just maintains the status quo. The bug should still be fixed, but it probably does not need to block the release. For example, if we discover that our quality control for new explorations has never checked for profanity in exploration text, we might deploy the release without fixing the bug, but work on a profanity checker for the next release. The reasoning here is that deploying without the checker is okay because it does not make the user experience any worse -- we just haven't made it better yet. An important note here is that there might be debate within the Oppia developer community over whether this "bug" is intended behaviour or over how it should be addressed. It may be important to let this debate be resolved in due time, rather than rushing to get a release out with the "fix."

    * **Behaviour is Newly Introduced**: If the behaviour was only introduced in the last few releases, then it may make sense to ensure that the upcoming release fixes it. For example, if we discover that the previous release resulted in explorations crashing for users with slow connections, we might want to make sure that the upcoming release fixes this problem, even if that means delaying the release, because it is important to fix the crashes as soon as possible.

5. **Invisible Bugs**: Sometimes we discover bugs that have no apparent impact on the user experience, for example console warnings that don't seem to change the site's behaviour. If we are sure that the user experience is not impacted, it might make sense to plan a fix for the bug, but not let it hold up the release.

6. **Regressions**: Regressions can be thought of as bugs where the behaviour of something on the current live site is better than its behaviour in the release cut. This entails a breakage of existing functionality, and needs to be considered blocking since it impacts the user experience.

7. **Broken Jobs**: If a job cannot be run on the test server, this should be considered a blocking bug.

# Instructions for fixing release bugs
## Deciding whether to fix the bug or remove the changes from the release
If the blocking bug arises from a newly introduced feature, the release coordinator **can** allow small fixes for UI problems. However, for all other problems, the feature needs to be removed from the release (preferably by disabling the feature via the appropriate flag), and the issues need to be fixed before the **next release**.

If the blocking bug arises from a job that cannot be run, the decision whether to exclude or include it in the release depends on whether the job can be delayed to the next release or not. Jobs that clean up old stuff should be delayed until the next release, but jobs needed for a new feature should be fixed immediately.

## How to fix a release bug
1. Make a branch off of `develop`, and fix the bug.
1. Apply the label [PR: for current release](https://github.com/oppia/oppia/labels/PR%3A%20for%20current%20release) to PRs containing bugfixes that need to go into the current release.
1.  (**This should only be done by the release coordinator.**) When the PR has been cherry-picked onto the release branch, apply the label [PR: released](https://github.com/oppia/oppia/labels/PR%3A%20released) to the PR.

# Responsibilities of the release coordinator
- Ensuring that the release (and all related processes) for the month happen on schedule and are performed correctly.
- Handling all deployments to the test server and the production server.
- Running any one-off jobs for the release.

# Responsibilities of the QA coordinator
- Gathering a group of testers for the release testing team for the month.
- Adding any new user journeys which are critical to the [critical user journeys](https://docs.google.com/document/d/1T3HyMU8cMvXY1tyzs801Zgf5oSxLqaHICUH_YZJa4JM/edit#heading=h.ri1uw1xkq033) doc. Any changes to existing user journeys will also need to be reflected in the doc.
- Assigning tasks (in the doc for the release), and notifying the testers about the same.
- Making sure all assigned tasks are completed on time.
- Triaging all reported bugs as blocking/non-blocking. The blocking bugs need to be assigned to a bugfixer ASAP. Help with fixing some of the blocking bugs.
- Once bug fixes are complete, and deployed to the test server, verify that the bugs no longer exist and affected user journeys play out fine. (This can be a team effort too).

# Responsibilities of the release testing team
The release testing team focuses on testing the [critical user journeys](https://docs.google.com/document/d/1T3HyMU8cMvXY1tyzs801Zgf5oSxLqaHICUH_YZJa4JM/edit#heading=h.ri1uw1xkq033) on Oppia. This ensures that all the core functionality is working fine!

The QA coordinator for the month assembles the release testing team before the QA testing weekend (the first weekend of every month). All bugs that need to be prioritized for the current release need to be reported and triaged by the Monday after the QA weekend. All bugs will need to be fixed before the following Monday, and the release will be pushed during the third weekend.

The testers have to be in constant touch with both the QA coordinator as well as the release coordinator for that release. During the testing weekend and the week after that, please prioritize fixing issues under the [blocking bugs milestone](https://github.com/oppia/oppia/milestone/39) so that we can complete the release process on time.

We also have a project leads council who will be contacted about project specific bugs, and the QA team will report the bug to the concerned project lead. This will help us get people with experience in the area to help fix the bug quicker.

**Note:** If you would like to help out with the release testing, please contact @nithusha21 or @aks681. They will be able to guide you further. 


# Team members
* Release team: 
  * Sandeep Dubey (**@DubeySandeep**)
  * Nithesh Hariharan (**@nithusha21**)
  * Akshay Anand (**@aks681**)
  * Vojtěch Jelínek (**@vojtechjelinek**)
  * Kevin Thomas (**@kevintab95**)
  * Chris Skalnik (**@U8NWXD**)

* Release Coordination team:
  * Nithesh Hariharan (**@nithusha21**)
  * Vojtěch Jelínek (**@vojtechjelinek**)

* QA coordinators team: 
  * Nithesh Hariharan (**@nithusha21**)
  * Akshay Anand (**@aks681**)
  * Chris Skalnik (**@U8NWXD**)
  * Kevin Thomas (**@kevintab95**)
  * Vojtěch Jelínek (**@vojtechjelinek**)
  * Rohit Katlaa (**@rohitkatlaa**)

# Release coordinators and QA coordinators for upcoming releases

**Note:** If you can't make it to a shift mentioned in the below rota, please make sure to swap with someone else in advance! 

| Month         | Release team member         | QA coordinator              | Server errors coordinator   |
| ------------- | --------------------------- | --------------------------- | --------------------------- |
| June          | Nithesh (**@nithusha21**)   | Rohit (**@rohitkatlaa**)    | Kevin (**@kevintab95**)     |
| July          | Sandeep (**@DubeySandeep**) | Rohit (**@rohitkatlaa**)    | Vojta (**@vojtechjelinek**) |
| August        | Kevin (**@kevintab95**)     | Chris (**@U8NWXD**)         | Kevin (**@kevintab95**)     |
| September     | Nithesh (**@nithusha21**)   | Akshay (**@aks681**)        | Kevin (**@kevintab95**)     |
| October       | Vojta (**@vojtechjelinek**) | Kevin (**@kevintab95**)     | Vojta (**@vojtechjelinek**) |
| November      | Chris (**@U8NWXD**)         | Vojta (**@vojtechjelinek**) | Kevin (**@kevintab95**)     |
| December      | Akshay (**@aks681**)        | Nithesh (**@nithusha21**)   | Kevin (**@kevintab95**)     |