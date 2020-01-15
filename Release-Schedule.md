# Schedule
**The Friday before the first Saturday of each month**: Release branch gets created. Push the release branch onto a test server.
Features merged into `develop` after this date will only go out in the following release.

**First weekend of each month**: The release team will focus on testing. Typically the testing deadline is chosen to be the Monday after the weekend. The testing should be completed by the deadline. All bugs caught should be filed as blocking bugs on Github, and should be assigned to a bugfixer ASAP.

**Second weekend of each month**: The release/QA team and the project leads council will focus on fixing the reported bugs. By the Monday after the second weekend, the bug-fixing phase should be completed.

**Third week of each month**: First the fixes will be cherrypicked and deployed to the test server, and then we test that the bugs are fixed on the test server. Once this verification is complete, we can go ahead with the next step. 

**Third weekend of each month**: The release will be made and an update will be pushed to the live site.

# Instructions for fixing release bugs
1. Make a branch off of `develop`, and fix the bug.
1. Apply the label [PR: for current release](https://github.com/oppia/oppia/labels/PR%3A%20for%20current%20release) to PRs containing bugfixes that need to go into the current release.
1.  (**This should only be done by the release coordinator.**) When the PR has been cherry-picked onto the release branch, apply the label [PR: released](https://github.com/oppia/oppia/labels/PR%3A%20released) to the PR.

# Responsibilities of the release coordinator
- Ensuring that the release (and all related processes) for the month happen correctly and on schedule.
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
* Release coordination team: Ankita Saxena (**@ankita240796**), Sandeep Dubey (**@DubeySandeep**), Nithesh Hariharan (**@nithusha21**), Akshay Anand (**@aks681**), Vojtěch Jelínek (**@vojtechjelinek**)

* QA coordinators team: Nithesh Hariharan (**@nithusha21**), Akshay Anand (**@aks681**), Rishabh Rawat (**@Showtim3**), Chris Skalnik (**@U8NWXD**)

# Release coordinators and QA coordinators for upcoming releases

**Note:** If you can't make it to a shift mentioned in the below rota, please make sure to swap with someone else in advance! 

* Dec: Sandeep (**@DubeySandeep**) and Nithesh (**@nithusha21**)
* Jan: Akshay (**@aks681**) and Chris (**@U8NWXD**)
* Feb: Ankita (**@ankita240796**) and Rishabh (**@Showtim3**)
* Mar: Nithesh (**@nithusha21**) and Akshay (**@aks681**)
* Apr: Vojtěch (**@vojtechjelinek**) and Nithesh (**@nithusha21**)
* May: Sandeep (**@DubeySandeep**) and Chris (**@U8NWXD**)
* Jun: Ankita (**@ankita240796**) and Akshay (**@aks681**)
* Jul: Nithesh (**@nithusha21**) and Rishabh (**@Showtim3**)
