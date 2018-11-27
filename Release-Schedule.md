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
The release testing team focuses mainly on 2 types of testing. One is to make sure that the core functionality of Oppia is intact (called Happy-paths testing) and the other is to make sure the newly added functionality works fine (testing the PRs added in the current release). 

During the first week of the month the QA lead will send out a mail to the release testers for the month asking for their confirmation of participation. After confirmation, the QA lead will assign tasks to each of the testers before the first Saturday (when the release cut is made) so that the testing can begin on time. 

The testers have to be in constant touch with both the QA lead as well as the release coordinator for that release. During the testing week and the week after that, please prioritize fixing issues under the [blocking bugs milestone](https://github.com/oppia/oppia/milestone/39) so that we can complete the release process on time.  

**Note:** If you would like to help out with the release testing, please contact @nithusha21 or @aks681. They will be able to guide you further. 

# Release coordinators and QA coordinators for upcoming releases
* Aug: Ben(@BenHenning) and Akshay(@aks681)
* Sep: Tony(@tjiang) and Nithesh(@nithusha21)
* Oct: Sean(@seanlip) and Akshay(@aks681)
* Nov: Ben(@BenHenning) and Nithesh(@nithusha21)
* Dec: Ben(@BenHenning) and Nithesh(@nithusha21)
