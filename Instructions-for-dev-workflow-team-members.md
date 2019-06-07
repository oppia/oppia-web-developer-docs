## How to join the Dev Workflow Team?

* **If you’re interested in joining the team, please ensure that you are a part of at most one team at Oppia.** This is to ensure that you’re able to devote sufficient time to each team.
* Go through the team’s mission, ongoing workflow and the project on GitHub [here](https://github.com/oppia/oppia/projects/23).
* **You need to solve a couple of dev-workflow issues before being inducted as a permanent member of the team.** Feel free to assign yourself any project-specific starter issue [here](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+project%3Aoppia%2Foppia%2F23+label%3A%22Project-specific+starter+issue%22). When you create a PR for any of these issues, ask **@apb7** for review.
* After you’ve successfully fixed two dev-workflow-specific starter issues, follow these steps:
  * Ping **@apb7** to make you a member of the dev-workflow-team.
  * Ping **@apb7** to assign you one of the sub-missions of the Team. If the sub-mission is already being led by any team member, please ping them for suggested work. The following are the current sub leads:
    * **Apurv**: Builds and Review Workflow
    * **Rishav**: Oppiabot and Setup issues
    * **Anubhav**: Optimize speed of scripts
    * **Yash**: Tracking and adding new lint checks to the codebase.
  * Ping **@apb7** to extend the team meeting invites to you. Please RSVP to them as soon as possible.
  * Ping **@apb7** to add you to the Dev Workflow Team Hangouts group. The Team usually has quick discussions here.
  * Ping **@lilithxxx** to assign you a rota for tracking setup issues, [here](https://github.com/oppia/oppia/wiki/Instructions-for-dev-workflow-team-members#dev-flow-rota).
  * Subscribe to both, CircleCI and Travis build notifications. Please follow this:
    * CircleCI: Login to CircleCI using your GitHub account and go to [this link](https://circleci.com/gh/oppia/oppia/edit). There you’ll find an option to follow oppia/oppia.  
    * Travis: Make a PR adding your email id to .travis.yml similar to [this PR](https://github.com/oppia/oppia/pull/6330/files).
  * You’re all set now -- start working on the assigned sub mission. This generally involves fixing devflow issues on GitHub.


***

## Instructions for existing team members
Jot down the issues faced by developers related to developer-workflow in the [setup-issues spreadsheet](https://docs.google.com/spreadsheets/d/1pKN1otvhaI8IYlNj79MX_qxArbD4p4L-CdsnQT022Pc/edit?usp=sharing
) with the possible solutions (if known) from which they will be noted in the [Troubleshooting page](https://github.com/oppia/oppia/wiki/Troubleshooting) of the wiki.

### Tasks:
* Look through the gitter channel, the mailing list and all issues/PRs where the dev-flow team (@dev-workflow-team) is tagged.
* If a setup issue is seen more than 2 times in the codebase then open a new issue with the label ‘setup issues’ in github.

#### [@apb7 + @lilithxxx + @anubhavsinha98 + @YashJipkate]: 
_If a new issue comes in_, clearly explain the issue faced by the developer with its possible solutions (if known) in the above issues spreadsheet.
If the issue is solved by you:
* **Update the troubleshooting page of the wiki.**
* Remove the issue from the spreadsheet after its been written down in the wiki.

#### Dev-flow Rota for tracking setup issues:
```
January	  Apurv         @apb7
February  Rishav        @lilithxxx
March  	  Anubhav       @anubhavsinha98
April     Yash          @YashJipkate
May 	  Apurv         @apb7
June      Rishav        @lilithxxx
July 	  Anubhav       @anubhavsinha98
August 	  Yash          @YashJipkate
September Apurv         @apb7
October	  Rishav        @lilithxxx
November  Anubhav       @anubhavsinha98
December  Yash          @YashJipkate
```
#### Dev Workflow Rota for Co-Lead:
```
April     Apurv (@apb7)        Anubhav (@anubhavsinha98)
May 	  Yash (@YashJipkate)  Anubhav (@anubhavsinha98)
June      Yash (@YashJipkate)  Rishav (@lilithxxx)
July 	  Apurv (@apb7)        Rishav (@lilithxxx)
August 	  Apurv (@apb7)        Anubhav (@anubhavsinha98)
September Yash (@YashJipkate)  Anubhav (@anubhavsinha98)
October	  Yash (@YashJipkate)  Rishav (@lilithxxx)
November  Apurv (@apb7)        Rishav (@lilithxxx)
```
#### Responsibilities of Co-Lead:-
1. Manage the whole dev workflow team and ensure that every team member is working on at least one issue/bug/feature. 

2. Figure out the lint errors facing by the contributors.

3. Ensure that every comment is being addressed by the dev workflow team member where the dev workflow is cc’d. 

4. Ping the team to update their tasks in meeting minutes, before the meeting.

5. Do daily passes on the PRs that are more than 1 month old and move them along. (These would be the first few PRs in [this list](https://github.com/oppia/oppia/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc).)

**Duties of the dev-flow rota coordinator:**
1. Ensure member rotation is followed.
2. Send a ping/email to the member reminding him/her of the rota if it has been missed. 

#### Rota coordinator: Rishav


#### [@lilithxxx]: 
* If the issue is solved by someone other than a dev-flow member, write down the issue with its solution in the troubleshooting page of the wiki so that other contributor does not face the same problem.
* Monitor that the solutions of all setup issues are indeed jotted down in the wiki. 

#### Rota for updating metrics tracker:
```
April     Apurv (@apb7)
May 	  Anubhav (@anubhavsinha98)
June      Yash (@YashJipkate)
July 	  Rishav (@lilithxxx)
August 	  Anubhav (@anubhavsinha98)
September Yash (@YashJipkate)
October	  Apurv (@apb7)
November  Rishav (@lilithxxx)
Decemeber Anubhav (@anubhavsinha98)
```
***

### Triaging issues and keeping the team updated with progress -- what’s the system we’re using for this?
* Create an issue first if it’s not already present.
* If the issue is related to an outage, mark it as important.
* If it’s an outage, inform oppia-dev regarding the same and the probable causes known at that point of time.
* Keep the team updated by sending in regular mails to oppia-dev-workflow-team informing them about the progress on the fix. For an outage, post the same on oppia-dev.
* Keep repeating the above step until the issue is fixed.
* Once the issue is fixed, post a final update on oppia-dev & oppia-dev-workflow-team. Create a postmortem if the issue is an outage.
* Responsibilities:
  **Anubhav** - Updating oppia-dev and the team.
* The fix can be carried out by one of the team members as per discussion on the Hangouts group.


## Communication Channel:
To discuss anything with oppia dev workflow, mail us at : oppia-dev-workflow-team@googlegroups.com

Or post your query here [oppia-dev-workflow-team](https://groups.google.com/forum/#!forum/oppia-dev-workflow-team)