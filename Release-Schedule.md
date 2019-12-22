# Schedule
**The Friday before the first Saturday of each month**: Release branch gets created. Push the release branch onto a test server.
Features merged into `develop` after this date will only go out in the following release.

**First weekend of each month**: The release team will focus on testing. By the Monday after the first weekend, the testing phase should be completed.

**Second weekend of each month**: The release team will focus on fixing the reported bugs. By the Monday after the second weekend, the bug-fixing phase should be completed.

**Third weekend of each month**: The release will be made and an update will be pushed to the live site.

# Instructions for fixing release bugs
1. Make a branch off of `develop`, and fix the bug.
1. Apply the label [PR: for current release](https://github.com/oppia/oppia/labels/PR%3A%20for%20current%20release) to PRs containing bugfixes that need to go into the current release.
1. When the PR has been cherry-picked onto the release branch, apply the label [PR: released](https://github.com/oppia/oppia/labels/PR%3A%20released). (The release coordinator will do this step.)

# Responsibilities of the release testing team
The release testing team focuses on testing the [critical user journeys](https://docs.google.com/document/d/1T3HyMU8cMvXY1tyzs801Zgf5oSxLqaHICUH_YZJa4JM/edit#heading=h.ri1uw1xkq033) on Oppia. This ensures that all the core functionality is working fine!

The QA coordinator for the month assembles the release testing team before the QA testing weekend (the first weekend of every month). All bugs that need to be prioritized for the current release needs to be reported and triaged by the Monday after the QA weekend. All bugs will need to be fixed before the following Monday, and the release will be pushed during the third weekend.

The testers have to be in constant touch with both the QA coordinator as well as the release coordinator for that release. During the testing weekend and the week after that, please prioritize fixing issues under the [blocking bugs milestone](https://github.com/oppia/oppia/milestone/39) so that we can complete the release process on time.  

**Note:** If you would like to help out with the release testing, please contact @nithusha21 or @aks681. They will be able to guide you further. 

# Instructions for QA member in charge of monitoring PRs
* This is a weekly rota. During the week, monitor all PRs that come in, and all issues being filed.
* For PRs, make sure the PR maintains quality of the codebase. This means that: 
    * PR must maintain backend and frontend coverage values. Any new code being added needs to come with unit tests.
    * If the PR completes a new feature (or a part, for which the following apply), the PR must add e2e tests for the same. Make sure to record this in the critical user journeys, or the functional capabilities as applicable. If this is a large feature, which needs to be tested with a small subset of the end users (intuitiveness testing) before we can make it public, initiate discussions regarding the same. 
* For issues, make sure that any breakage of existing functionality reported is escalated to the appropriate contributor(s). Add user-facing bugs to the [bug fixing team project](https://github.com/oppia/oppia/projects/27#column-4117882).
* At the end of the week (Sunday), notify the next QA team member about their upcoming shift. 

**Note: ** If you can't make it to a shift mentioned in the below rota, please make sure to swap with someone else in advance! 

# Team members
* Release coordination team: Ankita Saxena (@ankita240796), Sandeep (@DubeySandeep), Nithesh (@nithusha21), Akshay (@aks681), Vojtech (@vojtechjelinek)

* QA coordinators team: Nithesh (@nithusha21), Akshay (@aks681), Rishabh (@Showtim3), Chris (@U8NWXD)

# Release coordinators and QA coordinators for upcoming releases
* Dec: Sandeep(@DubeySandeep) and Nithesh(@nithusha21)
* Jan: TBD and Chris (@U8NWXD)
* Feb: TBD
* Mar: TBD
* Apr: TBD
* May: TBD
* Jun: TBD
* Jul: TBD
