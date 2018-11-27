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
The release testing team focuses on testing the critical user journeys on Oppia. This ensures that all the core functionality is working fine!

The QA coordinator for the month assembles the release testing team before the QA testing weekend (the first weekend of every month). All bugs that need to be prioritized for the current release needs to be reported and triaged by the Monday after the QA weekend. All bugs will need to be fixed before the following Monday, and the release will be pushed during the third weekend.

The testers have to be in constant touch with both the QA coordinator as well as the release coordinator for that release. During the testing weekend and the week after that, please prioritize fixing issues under the [blocking bugs milestone](https://github.com/oppia/oppia/milestone/39) so that we can complete the release process on time.  

**Note:** If you would like to help out with the release testing, please contact @nithusha21 or @aks681. They will be able to guide you further. 

# Team members
* Bug fixing team: Vibhor (@vibhor98), Christopher (ctao5660), Rishav (@lilithxxx), Nithesh (@nithusha21), Akshay (@aks681)
* QA coordinators team: Nithesh (@nithusha21), Akshay (@aks681), Nitish (@bansalnitish), Vibhor (@vibhor98)

# Release coordinators and QA coordinators for upcoming releases
* Dec: Ben(@BenHenning) and Nithesh(@nithusha21)
* Jan: Sean(@seanlip) and Vibhor(@vibhor98)
* Feb: Nithesh(@nithusha21) and Nitish (@bansalnitish)
* Mar: Ben(@BenHenning) and Akshay (@aks681)
* Apr: Sean(@seanlip) and Nithesh (@nithusha21)
* May: Nithesh(@nithusha21) and Vibhor(@vibhor98)
* Jun: Ben(@BenHenning) and Nitish (@bansalnitish)
* Jul: Sean(@seanlip) and Akshay (@aks681)
* Aug: Nithesh(@nithusha21) and Vibhor(@vibhor98)
* Sept: Ben(@BenHenning) and Akshay (@aks681)
* Oct: Sean(@seanlip) and Nithesh (@nithusha21)
* Nov: Nithesh(@nithusha21) and Vibhor(@vibhor98)
* Dec: Ben(@BenHenning) and Nitish (@bansalnitish)