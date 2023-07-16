Oppia releases happen monthly, and are typically cut on the first Saturday of each month. (Features merged into `develop` after this date will only go out in the following release.)

Please see the rota below for the expected release dates. We expect QA testing to be completed 1 week after the release cut, and final deployment to take place 1 week after that.

Sometimes, we do hotfixes outside the release cycle for PRs that need to be urgently deployed. If you need to request a hotfix, please fill in [this form](https://forms.gle/4CRqXovA3xS27rDLA) and work with the corresponding release coordinator to get your changes into production safely.

## Release Team members
* Team lead:
  * Kevin Thomas (**@kevintab95**)

* Release coordinators:
  * Sandeep Dubey (**@DubeySandeep**)
  * Akshay Anand (**@aks681**)
  * Vojtěch Jelínek (**@vojtechjelinek**)
  * Kevin Thomas (**@kevintab95**)
  * Chris Skalnik (**@U8NWXD**)
  * Sagang Wee (**@sagangwee**)
  * Hasitha Kaushan (**@chris7716**)
  * Sanjay Saju (**@SanjaySajuJacob**)

* QA coordinators:
  * Akshay Anand (**@aks681**)
  * Chris Skalnik (**@U8NWXD**)
  * Kevin Thomas (**@kevintab95**)
  * Vojtěch Jelínek (**@vojtechjelinek**)

## Release coordinators and QA coordinators for upcoming releases

**Note:** If you can't make it to a shift mentioned in the below rota, please make sure to swap with someone else in advance!

| Month     | Release cut date | Release coordinator           | Release coordinator mentor  | QA coordinator              | Server errors coordinator |
|-----------|------------------|-------------------------------|-----------------------------|-----------------------------|-------------------------|
| February  | 1st February     | Kevin (**@kevintab95**)       | Kevin (**@kevintab95**)     | Vojta (**@vojtechjelinek**) | Kevin (**@kevintab95**) |
| March     | 1st March        | Sanjay (**@SanjaySajuJacob**) | Chris (**@U8NWXD**)         | Sandeep (**@DubeySandeep**) | Kevin (**@kevintab95**) |
| April     | 3rd April        | Sagang (**@sagangwee**)       | Akshay (**@aks681**)        | Kevin (**@kevintab95**)     | Kevin (**@kevintab95**) |
| May       | 6th May          | Hasitha (**@chris7716**)      | Sandeep (**@DubeySandeep**) | Chris (**@U8NWXD**)         | Kevin (**@kevintab95**) |
| June      | 31st May         | Praneeth (**@gp201**)         | Kevin (**@kevintab95**)     | Akshay (**@aks681**)        | Kevin (**@kevintab95**) |
| July      | 28th June        | Priyansh (**@Priyansh61**)    | Chris (**@U8NWXD**)         | Sandeep (**@DubeySandeep**) | Kevin (**@kevintab95**) |
| August    | 2nd August       | Akshay (**@aks681**)          |                             | Kevin (**@kevintab95**)     | Kevin (**@kevintab95**) |
| September | 30th August      | Sandeep (**@DubeySandeep**)   |                             | Chris (**@U8NWXD**)         | Kevin (**@kevintab95**) |
| October   | 4th October      | Kevin (**@kevintab95**)       |                             | Akshay (**@aks681**)        | Kevin (**@kevintab95**) |
| November  | 1st November     | Chris (**@U8NWXD**)           |                             | Sandeep (**@DubeySandeep**) | Kevin (**@kevintab95**) |
| December  | 29th November    | Akshay (**@aks681**)          |                             | Kevin (**@kevintab95**)     | Kevin (**@kevintab95**) |


## Responsibilities of the release coordinator
- Communicate clearly during the release process, especially in the group chat to share updates as the release steps are completed, and keeping the team apprised of any delays.
- Ensuring that the release (and all related processes) for the month happen on schedule and are performed correctly.
    - If you are unable to conduct a release due to any reason, please inform the release team lead at least a month before and try to find a backup to replace you as the release coordinator.
    - If the release does not follow the usual process or is delayed, a 1:1 will be scheduled with the release team lead to find the issues and work on mitigations to avoid them in the future.
- Handling all deployments to the test server and the production server.
- Running any one-off jobs for the release.

## Responsibilities of the QA coordinator
- Gathering a group of testers for the release testing team for the month.
- Adding any new user journeys which are critical to the [critical user journeys](https://docs.google.com/document/d/1T3HyMU8cMvXY1tyzs801Zgf5oSxLqaHICUH_YZJa4JM/edit#heading=h.ri1uw1xkq033) doc. Any changes to existing user journeys will also need to be reflected in the doc.
- Assigning tasks (in the doc for the release), and notifying the testers about the same.
- Making sure all assigned tasks are completed on time.
- Triaging all reported bugs as blocking/non-blocking. The blocking bugs need to be assigned to a bugfixer ASAP. Help with fixing some of the blocking bugs.
- Once bug fixes are complete, and deployed to the test server, verify that the bugs no longer exist and affected user journeys play out fine. (This can be a team effort too).

## Responsibilities of the release testing team
The release testing team focuses on testing the [critical user journeys](https://docs.google.com/document/d/1T3HyMU8cMvXY1tyzs801Zgf5oSxLqaHICUH_YZJa4JM/edit#heading=h.ri1uw1xkq033) on Oppia. This ensures that all the core functionality is working fine!

The QA coordinator for the month assembles the release testing team before the QA testing weekend (the first weekend of every month). All bugs that need to be prioritized for the current release need to be reported and triaged by the Monday after the QA weekend. All bugs will need to be fixed before the following Monday, and the release will be pushed during the third weekend.

The testers have to be in constant touch with both the QA coordinator as well as the release coordinator for that release. During the testing weekend and the week after that, please prioritize fixing issues under the [blocking bugs milestone](https://github.com/oppia/oppia/milestone/39) so that we can complete the release process on time.

**Note:** If you would like to help out with release testing, please contact @vojtechjelinek or @kevintab95. They will be able to guide you further.

## Instructions for fixing bugs found during QA testing

We want to avoid introducing new bugs in our releases.

If a regression is found by the testing team, the first step is to identify the PR that introduced it (using `git bisect`) and revert that PR. If the PR cannot be reverted (e.g. due to large merge conflicts), the release coordinator will start a discussion with the PR author, the Web tech lead, and the release team lead to determine the best course of action.

We generally prefer to revert rather than fix-forward, since the release operates on a timeline. However, in rare cases, we might decide to fix-forward a bug. Here are the instructions for doing this:

1. Make a branch off of `develop`, and fix the bug.
2. Apply the label [PR: for current release](https://github.com/oppia/oppia/labels/PR%3A%20for%20current%20release) to PRs containing bugfixes that need to go into the current release.
3.  (**This should only be done by the release coordinator.**) When the PR has been cherry-picked onto the release branch, apply the label [PR: released](https://github.com/oppia/oppia/labels/PR%3A%20released) to the PR.
