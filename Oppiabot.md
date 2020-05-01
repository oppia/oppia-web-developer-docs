# Oppiabot

[Oppiabot](https://github.com/oppia/oppiabot) is a GitHub app built with [probot](https://github.com/probot/probot). It acts as a helper for the Oppia code repository to maintain the development workflow. It is hosted on [Heroku](https://www.heroku.com/). @ankita240796 leads develop of Oppiabot.

The bot currently performs the following functions:

1. **Checks whether a contributor creating a pull request has signed the CLA**:
    If the contributor has not signed the CLA, it puts up a `PR: don't merge - NEEDS CLA` label and comments on the pull request thread with `Hi! @<PR-Author>. Welcome to Oppia! Please, could you follow the instructions here to get started? You'll need to do this before we can accept your PR. Thanks!`.
    Once the contributor signs the CLA and pings the pull request thread, the bot rechecks the CLA status and removes the label if the GitHub username of the contributor is found in the CLA Sheet.

2. **Checks merge conflicts in all open pull requests**:
    The bot checks all open pull requests for merge conflicts. It puts a label `PR: don't merge - HAS MERGE CONFLICTS` and comments on the pull request thread with `Hi @<PR-Author>. The latest commit in this PR has resulted in a merge conflict. Please follow this link if you need help to resolve the conflict. Thanks!`. If the pull request author resolves the conflict before the next run of the merge conflict check, the bot automatically removes the label from all such open pull requests whose conflicts have been resolved.

3. **Closes stale pull requests**:
     The bot puts up a `stale` label on all open pull requests after 10 days of inactivity from the date of last updation (Please refer to [this link](https://github.com/probot/stale#how-are-issues-and-pull-requests-considered-stale) for further information regarding how pull requests are considered stale). If after 7 days of putting up the label, there is no activity on the pull request, the bot automatically closes it. These settings have been configured in [stale.yml](https://github.com/oppia/oppia/blob/develop/.github/stale.yml).
