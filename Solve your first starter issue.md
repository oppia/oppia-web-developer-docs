# Solve Your First Starter Issue

Welcome! This guide walks you through how to solve your first issue in Oppia’s codebase. Following this process ensures your contribution aligns with Oppia’s standards and helps maintain high code quality.

## 1. Before You Start

**To-do:**  
Review the [Getting Started Guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). Make sure to:

- Sign the CLA (Contributor License Agreement)
- Fill out the Oppia contributor survey
- Introduce yourself on the GitHub [Discussion Board](https://github.com/oppia/oppia/discussions)

**Note:**  
If you run into issues with signing the CLA, submitting the survey, or posting in Discussions, check the [Get Help](https://github.com/oppia/oppia/wiki/Get-help) page.

## 2. Fork the Repo and Set Up Remotes

**To-do:**  
Follow the instructions to set up your development environment:

- Fork the [Oppia repository](https://github.com/oppia/oppia)  
- Clone your fork locally
- Follow the [Installing Oppia](https://github.com/oppia/oppia/wiki/Installing-Oppia) guide

**Note:**  
Once your setup is successful, run `python -m scripts.start` and check if Oppia loads at `http://localhost:8181`.

If you encounter errors (e.g. Git issues or dependency problems), consult:

- [Issues with Installation](https://github.com/oppia/oppia/wiki/Issues-with-installation)
- [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting)
- [Tips for Common IDEs](https://github.com/oppia/oppia/wiki/Tips-for-common-IDEs) 
- [Git Cheat Sheet](https://github.com/oppia/oppia/wiki/Git-cheat-sheet)

## 3. Find an Issue

**To-do:**  
Follow the [Finding Something to Do](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#finding-something-to-do) guide to find an issue:

- Look for a [good first issue](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) that matches your interests or skill level.

If you can reproduce and understand the issue locally, you're good to go!

**Note:**  
Try to avoid:

- Issues without a label (all issues should be reviewed and labeled by Oppia maintainers)
- Issues with the "Impact: Low", "Backlog", or "triage needed" issues (those issues often haven't been looked at closely yet, and might not be priorities for implementation.)
- Issues already claimed by someone else (check the "Assignees" section and comments)
- Closed or stale issues

## 4. Understand and Reproduce the Issue

**To-do:**  
Before diving into code, get familiar with the [Oppia Codebase](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase):

- [Tips for Finding the Right Code to Change](https://github.com/oppia/oppia/wiki/Find-the-right-code-to-change)
- [Tips for Analyzing the Codebase](https://github.com/oppia/oppia/wiki/Analyzing-the-Codebase)
- Try to reproduce the issue locally (if applicable)

**Note:**  
Some issues may be complex and involve multiple parts of the codebase. If you have time, consider reading the Codebase Policies and Processes section in the sidebar.

## 5. Write a Fix Plan and Get Approval

**To-do:**  
Before writing any code, follow [How to Tackle Good First Issues](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#how-to-tackle-good-first-issues):

- Leave a comment on the issue with a short plan explaining how you’ll approach the fix
- Wait for a maintainer to approve your plan before starting work

**Note:**  
Sometimes your fix plan may not be approved because:

- The issue has already been assigned to someone else
- A maintainer suggests changes to your plan
- The issue gets closed before approval

That’s totally fine! Just move on to another issue—every attempt builds experience.

## 6. Work on the Fix Locally

**To-do:**  
Once your fix plan is approved:

- Create a new branch on your fork from the `develop` branch
- Make your changes
- Write and run relevant tests

**Note:**  
You might run into issues like:

- Tests failing unexpectedly after small changes
- Not sure if tests are needed or how to write them
- Unsure whether your approach is correct

These are common! Refer to the [Oppia Tests Guide](https://github.com/oppia/oppia/wiki/Tests) for help.

## 7. Open a Pull Request (PR)

**To-do:**  
Once you're ready to submit your changes:

- Open a pull request
- Follow [PR Guidelines](https://github.com/oppia/oppia/wiki/Rules-for-making-PRs) 
- Match the [Coding Style Guide](https://github.com/oppia/oppia/wiki/Coding-style-guide)

**Note:**  
After submitting your PR, maintainers will review and provide feedback. Common challenges include:

- CI checks failing (style, linting, or tests)
- Reviewers suggesting changes
- Merge conflicts with other PRs

All of this is totally normal! Just follow the feedback and keep improving your PR until it’s ready to merge.

## 8. Respond to Reviewers' Comments

**To-do:**

After you open a pull request, make sure the reviewer are assigned to the PR (make sure they appear in "Assignees"). Reviewers will leave comments or suggestions. Review carefully and take action accordingly:

- Make the requested changes to your code
- Reply to each comment to confirm what you've done or to ask for clarification, following [Address review comments until all reviewers approve](https://github.com/oppia/oppia/wiki/Rules-for-making-PRs#step-5-address-review-comments-until-all-reviewers-approve) in our PR guide
- Be respectful and collaborative—reviewers are here to help

**Note:**

Common pitfalls to avoid:

- Ignoring comments or forgetting to reply
- Making changes but not pushing them to your PR branch
- Being defensive—feedback is part of the process, not a personal critique

If you're unsure how to address a comment, it's totally fine to ask follow-up questions. Clear communication is key!

## 9. Get Your PR Merged

**To-do:**

Once all reviewer comments are resolved:

- Make sure all required checks (CI, lint, tests) are passing, following [Make sure all continuous integration checks pass](https://github.com/oppia/oppia/wiki/Rules-for-making-PRs#step-6-make-sure-all-continuous-integration-checks-pass) in our PR guide
- Ping your reviewer if the PR has been inactive for a few days after all updates are made

**Note:**

Even at this final step, some issues can block a merge:

- Merge conflicts (solve them by updating your branch with the latest develop)
- Unaddressed comments or incomplete explanations
- New reviewers jumping in with additional suggestions

Stay patient and proactive—once your PR is approved and all checks pass, a maintainer will merge it. Congratulations, you’ve contributed to Oppia! Every small fix helps make Oppia better for learners around the world!


