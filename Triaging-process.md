## General
This wiki outlines the steps to triage new and existing issues. This ensures that all issues are being effectively tracked and prioritized.

### Steps to triage incoming issues coming into Oppia as a whole (first-stage triage):
The Dev Workflow team lead (currently Chris) should do the following every week for any [filed issues that aren’t assigned to a project](https://github.com/oppia/oppia/issues?q=is%3Aissue+is%3Aopen+no%3Aproject):

- Check that the issue is written clearly enough. Request clarification if needed.
- Assign the issue to the appropriate task force, if applicable. Otherwise, assign it to the relevant team (LaCE, CD, Dev Workflow) based on which type of user it affects.
- If you’re not sure how to categorise an issue, feel free to ping Sean for help!

### Steps to triage incoming issues for each team (second-stage triage):
Team leads should do an audit every week to categorise new issues in their GitHub Projects board, following these steps:

1. Verify that the issue lies within the scope of the team (see definitions below).
    - If not, assign the issue to the appropriate project/team.
2. Determine whether the issue is a bug or a enhancement
    - If the issue is a feature request (enhancement), contact the relevant PM (product manager) for the team and ask them to take a look and decide whether it needs to be worked upon. (See the list of PMs [below](##pm-contacts-for-each-team).)
3. (For simple UI issues) Make sure the bug is reproducible
    - The issue should be consistently reproducible on either develop or the test/backup server.
    - If that isn’t the case, ask the issue author for clarity.
4. Once the issue has been confirmed, the team lead should add the  appropriate ‘Impact’ label (asking the PM or tech lead for help if they’re not sure), as well as the appropriate ‘Work’ label to the issue.
    - ‘Impact’ defines how much the issue affects the functionality of the user-facing features. There are 3 associated labels: **Impact: High**, **Impact: Medium** and **Impact: Low**. For eg., the issue is considered to have a high impact if it breaks a critical feature or blocks a release. General bugs (non-blocking) and improvements can be considered to be of medium impact while issues that occur in a few edge cases or affect a small number of users are issues with a low impact.

    ||||||
    |--- |--- |--- |--- |--- |
    ||Severity|Severe (blocks or represents a primary user journey – e.g. end user playing a lesson, developer installing Oppia)|Moderate severity (blocks or represents a secondary user journey – e.g. end user changing a profile picture, developer easily seeing the output of frontend tests at the bottom of the CI log)|Minor (neither of the others, relates to “polish”)|
    |Users Affected|||||
    |(roughly) 60+%||High|Medium|Low|
    |(roughly) 5-60%||High|Low|Low|
    |(roughly) < 5%||Medium|Low|Low|

    <p style="text-align:center; font-size:12px"> Table: How “impact” is determined </p>

    - ‘Work’ defines how hard it would be to solve/resolve a particular issue. This is generally correlated with the amount of ambiguity in the task. We use the following rough system for assigning this label:
        - Solution is clear and broken into good-first-issue-sized chunks – assign **Work: Low**
        - Otherwise, if the means to find the solution is clear – assign **Work: Medium**
        - Everything else – assign **Work: High**

5. Once the appropriate ‘Impact’ and ‘Work Required’ labels has been added, determine its severity and assign the fitting priority label based on its impact (and possibly the work required label)
    - If the issue is a high-impact bug, put it in the high-priority bucket and prioritise it within the team.
    - For the priority bucket, team leads should include “important” issues – typically, a selection of high-impact enhancements and low-work medium-impact bugs – while keeping the size of that bucket about 2-3 times the projected stable number of team members. (Note: This exercise might also help with determining how large the team itself needs to be.)
    - Other issues go in the ‘backlog’ bucket.
    - Any issue with an external dependency that the team cannot resolve by itself (eg. missing mocks) goes in the ‘blocked’ bucket, and the reason should be specified on the ‘Issue specific status’ field (using free-text). Team leads should make sure an issue spends as little time here as possible.

6. Determine if the issue is potentially a good first issue
    - If the issue seems like something a new contributor to Oppia can take up, make sure to add enough information in the issue description for a new contributor to start work on that issue then ask Sandeep or Vojta to add the Good First Issue label. (Note: typically these are “Work: Low” issues.)
        - For such issues, also assign purple “technology: TypeScript”, “technology: Apache Beam”, “technology: Python”, etc. labels as appropriate. This helps new contributors identify issues that they would find approachable.

7. After triaging all issues, make sure the issues in the 'Priority' and 'High Priority' buckets are sorted based on severity/priority (high to low).


## PM contacts for each team
- **LaCE Quality**: @dchen97 (learners), @seanlip (creators)
- **Contributor dashboard**: @dchen97
- **Dev workflow**: @U8NWXD
- **Android**: @seanlip

