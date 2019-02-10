## Instructions to track metrics
- Number of issues present in the bug-fixing team project, which weren’t reported during the monthly QA. 
- Backend and frontend coverage values. For frontend, read off codecov’s label on github.com/oppia/oppia. For backend, run locally, and report the value. 
- Note whether a hotfix was needed, and whether all QA milestones happened on time.

## Instructions for QA member in charge of monitoring PRs
- This is a weekly rota. During the week, monitor all PRs that come in, and all issues being filed.
For PRs, make sure the PR maintains quality of the codebase. This means that:
    - PR must maintain backend and frontend coverage values. Any new code being added needs to come with unit tests.
    - If the PR completes a new feature (or a part, for which the following apply), the PR must add e2e tests for the same. Make sure to record this in the critical user journeys, or the functional capabilities as applicable. If this is a large feature, which needs to be tested with a small subset of the end users (intuitiveness testing) before we can make it public, initiate discussions regarding the same.
- For issues, make sure that any breakage of existing functionality reported is escalated to the appropriate contributor(s). Add user-facing bugs to the bug fixing team project.
- At the end of the week (Sunday), notify the next QA team member about their upcoming shift.

**Note:** If you can't make it to a shift mentioned in the below rota, please make sure to swap with someone else in advance!

## Instructions on getting a notification from @oppia/qa-team
- If the notification was on a PR thread, it would relate to adding new CUJs, functional capabilities, or initiating intuitiveness testing. As per request of the contributor, add these details or initiate these processes. 
- If the notification was on an issue, triage the issue. Try reproducing it on oppia.org and locally, to check if it is a regression during the current release. Add it to the bug-fixing team project. 
