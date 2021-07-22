
## How to handle regressions

1. File a detailed issue on the Github [tracker](https://github.com/oppia/oppia/issues/).

2. If the regression introduced causes a functionality to be broken or unusable on production, send an email to the release coordinator (see [assignments](https://github.com/oppia/oppia/wiki/Release-Schedule#release-coordinators-and-qa-coordinators-for-upcoming-releases)) of the previous release so that they can do a hotfix to fix the bug on the production server. Also, cc the original PR author (or notify them in some other way) so that they’re aware.

3. If the regression causes problems for developers (e.g. failing tests), send an email to oppia-dev to let developers know. The email should include a link to the issue you opened so that developers can follow along as we fix the regression.

3. Investigate to find the cause of the regression. Ideally, we want to find the PR that introduced the regression, but failing that, we want to understand what problem in the code is causing the regression.

   * If you identify the PR that caused the regression, mention it in the issue thread and @-mention the author of the PR so that they are aware of the problem. The problematic PR may be reverted if it matches the criteria mentioned in the [”When to revert a PR?” section](#when-to-revert-a-pr).
   * If you can’t find the PR / commit that caused the regression, make sure to mention this in the issue thread. Instead of reverting the PR, you should open a PR to fix the problem.

4. Consider what mitigation steps we could take to prevent similar regressions in the future. Here are some potential mitigations to consider:

   * New tests, for example if a breakage occurred in a bit of code that wasn't thoroughly tested.
   * Adding lint checks, for example if the regression was caused by a coding pattern we should avoid.
   * Changes to how we review PRs, for example if the regression was a UI bug that would have been caught had the PR description included screenshots.
     * Consider how much your mitigation will slow down the review process. Some mitigations, like adding screenshots, might not be a problem. Others, like requiring many more reviewers, might be more trouble than they're worth.
   * Emailing oppia-dev, for example to warn developers to avoid the coding pattern that caused the regression.
     * While we want to notify the developer community of how they can avoid regressions, we don't want to spam them with so many emails that they stop reading oppia-dev. Emailing oppia-dev is often the easiest mitigation, but it is not always the most effective.

   You may conclude that no mitigation is worth implementing, for example if the mitigations would introduce too much friction into the PR approval process. However, you should document your thought process in the issue in case someone has an idea for a mitigation you didn't consider.

6. Unless you can implement the mitigations immediately, you should open an issue for them. You should assign the issue to whoever is going to be in charge of implementation (often the dev workflow team lead).

## How to identify the bad commit

To systematically locate a bad commit, you can use the git-bisect tool. It internally uses a binary search algorithm to find the offending commit from the project history. To use this tool:

1.  Git checkout develop branch where the bug is observed (`git checkout develop`).
    
2.  Run `git bisect start` to start a bisect session.
    
3.  Run `git bisect bad` to verify that the current commit contains the bug.
    
4.  Go to [this](https://github.com/oppia/oppia/commits/develop) page to find an older (“good”) commit where the bug did not exist. Copy the commit id of the commit, and do git checkout on it (git checkout <commit-id>). Start the dev server (by running the start script) and try to figure out whether the error still exists. If so, you will need to find an even older commit than the current one. Kill the server, and repeat this step until you find a “good” commit.
    
5.  Once you’ve found a “good” commit, run “git bisect good”. The tool will automatically perform a binary search and checkout a commit between the “good” commit and “bad” commit. Start the dev server (by running the start script) and try to reproduce the error. At each step:
    - If the bug is reproducible, run “git bisect good”.
    - If not, run “git bisect bad”.
    
    Repeat this step until the tool reports the offending commit.

## When to revert a PR

If the PR exhibits either of the following two cases:

-   Introduces a flaky (there is any reported failure of the test on the develop branch) or consistently failing test.
    
-   Introduces a regression in a critical functionality.
    

Then, follow these steps:

1.  Automatically revert the PR if it has no merge conflicts or merge conflicts are trivial to resolve and inform the author that you have reverted their PR. You can find instructions for reverting PRs on Github [here](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/reverting-a-pull-request).
    
2.  If the revert PR has non-trivial merge conflicts, do not revert. Create an issue and mark it as a blocking bug for the on-going release and inform the author of the PR about the same by @-mentioning on the PR thread.
    
3.  If the PR introduced a flaky or failing test and contains other changes too, create a PR to delete or disable the test. Also, create an issue to add back the deleted/disabled test and inform the author of the PR about the same by @-mentioning on the PR thread.
    
4.  If the functionality is broken on the production server and needs to be fixed, inform the [release coordinator](https://github.com/oppia/oppia/wiki/Release-Schedule#release-coordinators-and-qa-coordinators-for-upcoming-releases) for the previous release so that a hotfix can be done.
    
5.  Add "PR: require post-merge sync to HEAD" label to the revert or fix PR if developers need to update their branches once the fix/revert PR has been merged into develop. Oppiabot will comment on open PRs to merge from develop once the reverted PR has been merged.

## How to revert a PR?

In the PR page, you will find a “revert” button at the point where the PR was merged.  
![](https://lh5.googleusercontent.com/dGgjIANi9zathEV_g9e5FKjpWTSn2tUSIUCdwalzUN6w1ocR1j5cuMoxq6tPOMYtk-1xsMPxj7tdkkK9jbOJP8f399DE1AAKmmCIcBMyYmd0MGJ3j3tO6P1R3b4frVMZy72UnAW_)

Clicking on this button will create a new PR with the reverted changes. Feel free to add a detailed comment in the PR description explaining why the PR needs to be reverted and tag the author of the original PR.

If you see this:

![](https://lh3.googleusercontent.com/4uYWOO2yXW8eBVTG9BH-wYZKRo7rB2WNUBbBudtaprlp4btYJ3avdQP-fRnZSBXGAq1DM05Hc_c9haASvHTFF8gRHgPZNqQ3ZKZc7vkZrPy13rTZ2EwOuQXQM6Sz7j0gVpF-61Z5)  
  
You will need to make the code changes on your local machine and create a PR by hand.

## What do I do if I caused a regression?

If the PR that introduced the regression hasn't been reverted, please follow the steps above to revert. Once your PR is reverted, follow these steps:

1.  Ensure you can repro the issue fully. If you can't, talk to the original author to better understand how to repro the issue.
    
2.  Make sure you fully understand why your change caused the observed regression(s)--without this step, no progress can actually be made. Remember: fix issues not symptoms. We don't just want the observed problem to go away, we want the underlying root cause to be understood & addressed.
    
3.  Once you understand the root cause, think through potential edge cases that may break other aspects of the app. It's quite likely that the observed regression was just one of several broken behaviors caused by the underlying issue.
    
4.  Turn the behaviors from (3) into tests. Verify that these tests fail without a fix, and pass with a fix to the original regression.
    
5.  Submit a new PR with your original changes + the fixes and tests from (4). Make sure to detail the investigation in this new PR, and reference the original issue that tracked the regression.

Finally, be aware that everyone causes regressions. While we have a lot of checks in place to try and avoid regressions from being checked in, they will still happen. Focus on learning from the situation rather focusing on the fact that a regression happened.