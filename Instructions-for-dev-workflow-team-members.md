## How to join the Dev Workflow Team?

* **If you’re interested in joining the team, please ensure that you are a part of at most one team at Oppia.** This is to ensure that you’re able to devote sufficient time to each team.
* Go through the team’s mission, ongoing workflow and the project on GitHub [here](https://github.com/oppia/oppia/projects/23).
* **You need to solve a couple of dev-workflow issues before being inducted as a permanent member of the team.** Feel free to assign yourself any project-specific starter issue [here](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+project%3Aoppia%2Foppia%2F23+label%3A%22Project-specific+starter+issue%22). When you create a PR for any of these issues, ask **@kevinlee12** for review.
* After you’ve successfully fixed two dev-workflow-specific starter issues, follow these steps:
  * Ping **@kevinlee12** to make you a member of the dev-workflow-team.
  * Ping **@kevinlee12** to assign you one of the sub-missions of the Team. If the sub-mission is already being led by any team member, please ping them for suggested work. The following are the current sub leads:
    * **Apurv**: Builds, Review Workflow and Oppiabot
    * **Anubhav**: Optimize speed of scripts and Setup issues
    * **Yash**: Tracking and adding new lint checks to the codebase.
  * Ping **@kevinlee12** to extend the team meeting invites to you. Please RSVP to them as soon as possible.
  * Ping **@kevinlee12** to add you to the Dev Workflow Team Hangouts group. The Team usually has quick discussions here.
  * Subscribe to both, CircleCI and Travis build notifications. Please follow this:
    * CircleCI: Login to CircleCI using your GitHub account and go to [this link](https://circleci.com/gh/oppia/oppia/edit). There you’ll find an option to follow oppia/oppia.
    * Travis: We will add you a mailing list.
  * You’re all set now -- start working on the assigned sub mission. This generally involves fixing devflow issues on GitHub.


***

## Instructions for existing team members
~Jot down the issues faced by developers related to developer-workflow in the [setup-issues spreadsheet](https://docs.google.com/spreadsheets/d/1pKN1otvhaI8IYlNj79MX_qxArbD4p4L-CdsnQT022Pc/edit?usp=sharing
) with the possible solutions (if known) from which they will be noted in the [Troubleshooting page](https://github.com/oppia/oppia/wiki/Troubleshooting) of the wiki.~
File the issues faced by developers related to developer-workflow directly on [the issue tracker](https://github.com/oppia/oppia/issues). Possible solutions (if known) should be noted down in the issue thread. Before closing down the issue, note it down in the [Troubleshooting page](https://github.com/oppia/oppia/wiki/Troubleshooting) of the wiki.

### Tasks:
* Look through the gitter channel, the mailing list and all issues/PRs where the dev-flow team (@dev-workflow-team) is tagged.
* If a setup issue is seen more than 2 times in the codebase then open a new issue with the label ‘setup issues’ in github.

#### [@kevinlee12]:
_If a new issue comes in_, clearly explain the issue faced by the developer with its possible solutions (if known) in the filed issue's thread.
If the issue is solved by you:
* **Update the troubleshooting page of the wiki.**
* Close the issue after its been written down in the wiki.

### Triaging issues and keeping the team updated with progress -- what’s the system we’re using for this?
* Create an issue first if it’s not already present.
* If the issue is related to an outage, mark it as important.
* If it’s an outage, inform oppia-dev regarding the same and the probable causes known at that point of time.
* Keep the team updated by sending in regular mails to oppia-dev-workflow-team informing them about the progress on the fix. For an outage, post the same on oppia-dev.
* Keep repeating the above step until the issue is fixed.
* Once the issue is fixed, post a final update on oppia-dev & oppia-dev-workflow-team. Create a postmortem if the issue is an outage.
* Responsibilities:
  **Kevin Lee** - Updating oppia-dev and the team.
* The fix can be carried out by one of the team members as per discussion on the Hangouts group.


## Communication Channel:
To discuss anything with oppia dev workflow, mail us at : oppia-dev-workflow-team@googlegroups.com

Or post your query here [oppia-dev-workflow-team](https://groups.google.com/forum/#!forum/oppia-dev-workflow-team)
