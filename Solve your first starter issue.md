# Solve Your First Starter Issue

Welcome! This guide walks you through how to solve your first issue in Oppia’s codebase. Following this process ensures your contribution aligns with Oppia’s standards and helps maintain high code quality.

## 1. Before You Start

Todo: Review the [Getting Started Guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). Make sure to:

- Sign the CLA (Contributor License Agreement)
- Fill out the Oppia contributor survey
- Introduce yourself on the GitHub [Discussion Board](https://github.com/oppia/oppia/discussions)

Notes: If you run into any issues with signing the CLA, submitting the survey, or posting in Discussions, check the [Get Help](https://github.com/oppia/oppia/wiki/Get-help) page for troubleshooting steps or reach out in [GitHub Discussions](https://github.com/oppia/oppia/discussions).

## 2. Fork the Repo and Set Up Remotes

Todo: Follow the instructions to set up the development envrionment:

- Fork the [Oppia repository](https://github.com/oppia/oppia)
- Clone your fork locally
- Follow the [Installing Oppia](https://github.com/oppia/oppia/wiki/Installing-Oppia) guide to set up your local development environment

Notes: Once your setup is successful, you can run docker-compose up and check if Oppia loads at http://localhost:8181. If you encounter errors while cloning the repo or setting up the environment (e.g. Git errors, dependency issues, or Docker problems), try the following resources:

- If you run into any problems during installation, please read [these notes](https://github.com/oppia/oppia/wiki/Issues-with-installation) and the [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting) page.
- Take a look at our guide for [getting started with some common code editors](https://github.com/oppia/oppia/wiki/Tips-for-common-IDEs).
- [Set up your dev Tools](https://github.com/oppia/oppia/wiki/Tips-for-common-IDEs)
- [Git cheat sheet](https://github.com/oppia/oppia/wiki/Git-cheat-sheet)

## 3. Find an Issue

Todo: Follow the [Finding Something to Do](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#finding-something-to-do) guide:

- Look for a [good first issue](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) that matches your interest or skill level.

Notes:
Try to avoid the following when choosing an issue:

- Issues without a lable (every issue needs to be reviewed and labled by the oppia maintainers first)
- Issues that don’t have the "good first issue" label (if you're a newcomer)
- Issues already claimed by someone else (check the assignee part and the comments)
- Closed or stale issues

If you're unsure whether an issue is right for you, feel free to leave a comment asking!

## 4. Understand and Reproduce the Issue

Todo: Before jumping into code, get familiar with current [Oppia Codebase](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase):

- [Tips for Finding the Right Code to Change](https://github.com/oppia/oppia/wiki/Find-the-right-code-to-change)
- [Tips for Analyzing the Codebase](https://github.com/oppia/oppia/wiki/Analyzing-the-Codebase)
- Try to reproduce the issue locally (if applicable)

Note: Some issues are complex and may involve several parts of the codebase. To make this step easier, you can:

- Rread the Codebase policies and processes part in the side bar if you have enough time.

## 5. Write a Fix Plan and Get Approval

Todo: Before coding, you need to follow [how to tackle good first issues](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#how-to-tackle-good-first-issues) in Oppia and comment on the issue that you find:

- Write a short plan explaining how you’ll approach the fix. 
- Wait for a maintainer to approve your plan before starting work.

Note: Sometimes your fix plan might not move forward due to reasons like:

- The issue has already been assigned to someone else
- A maintainer asks for changes to your plan
- The issue gets closed before approval

That’s okay! These things happen. Just move on to another issue — every attempt builds your experience.

## 6. Work on the Fix Locally

Todo: Once your fix plan is approved, work on it locally:

- Create a new branch on your fork from `develop`
- Make your changes
- Write and run relevant tests

Note: You might face situations like:

- Tests fail unexpectedly after small changes
- You’re unsure if tests are needed or how to write them
- You're not sure if your approach is correct

All of these are common! Useful testing resources were listed out at [Oppia Tests](https://github.com/oppia/oppia/wiki/Tests).

## 7. Open a Pull Request (PR)

Todo: When you're ready to submit your changes, make a PR:

- Follow [PR Guidelines](https://github.com/oppia/oppia/wiki/Rules-for-making-PRs).
- Match the [coding style](https://github.com/oppia/oppia/wiki/Coding-style-guide).

Note: Once your PR is submitted, maintainers will review and provide feedback. Common challenges during the PR process include:

- CI checks failing (style, linting, or tests)
- Reviewers suggesting changes to your code
- Merge conflicts with other PRs

This is totally normal! Just follow the feedback and update your PR. Every revision gets your contribution closer to being merged.



## 8. Ask for Help

If you're stuck at any other point:

- Check the [Get Help](https://github.com/oppia/oppia/wiki/Get-help) page
- Comment on the issue thread
- Reach out via GitHub Discussions or Oppia’s chat

Thank you for contributing! 
Every small fix makes Oppia better for learners around the world.

# Solve Your First Starter Issue

Welcome! This guide walks you through how to solve your first issue in Oppia’s codebase. Following this process ensures your contribution aligns with Oppia’s standards and helps maintain high code quality.

---

## 1. Before You Start

**To-do:**  
Review the [Getting Started Guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). Make sure to:

- Sign the CLA (Contributor License Agreement)  
- Fill out the Oppia contributor survey  
- Introduce yourself on the GitHub [Discussion Board](https://github.com/oppia/oppia/discussions)

**Note:**  
If you run into issues with signing the CLA, submitting the survey, or posting in Discussions, check the [Get Help](https://github.com/oppia/oppia/wiki/Get-help) page for troubleshooting steps or reach out via [GitHub Discussions](https://github.com/oppia/oppia/discussions).

---

## 2. Fork the Repo and Set Up Remotes

**To-do:**  
Follow the instructions to set up your development environment:

- Fork the [Oppia repository](https://github.com/oppia/oppia)  
- Clone your fork locally  
- Follow the [Installing Oppia](https://github.com/oppia/oppia/wiki/Installing-Oppia) guide

**Note:**  
Once your setup is successful, run `docker-compose up` and check if Oppia loads at `http://localhost:8181`.

If you encounter errors (e.g. Git issues, dependency problems, or Docker errors), consult:

- [Issues with Installation](https://github.com/oppia/oppia/wiki/Issues-with-installation)  
- [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting)  
- [Tips for Common IDEs](https://github.com/oppia/oppia/wiki/Tips-for-common-IDEs)  
- [Git Cheat Sheet](https://github.com/oppia/oppia/wiki/Git-cheat-sheet)

---

## 3. Find an Issue

**To-do:**  
Follow the [Finding Something to Do](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#finding-something-to-do) guide:

- Look for a [good first issue](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) that matches your interests or skill level.

**Note:**  
Try to avoid:

- Issues without a label (all issues should be reviewed and labeled by Oppia maintainers)  
- Issues without the "good first issue" label (especially if you're new)  
- Issues already claimed by someone else (check the "Assignees" section and comments)  
- Closed or stale issues

If you're unsure whether an issue is right for you, feel free to leave a comment asking!

---

## 4. Understand and Reproduce the Issue

**To-do:**  
Before diving into code, get familiar with the [Oppia Codebase](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase):

- [Tips for Finding the Right Code to Change](https://github.com/oppia/oppia/wiki/Find-the-right-code-to-change)  
- [Tips for Analyzing the Codebase](https://github.com/oppia/oppia/wiki/Analyzing-the-Codebase)  
- Try to reproduce the issue locally (if applicable)

**Note:**  
Some issues may be complex and involve multiple parts of the codebase. If you have time, consider reading the Codebase Policies and Processes section in the sidebar.

---

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

---

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

---

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

---

## 8. Ask for Help

If you’re stuck at any point:

- Check the [Get Help](https://github.com/oppia/oppia/wiki/Get-help) page  
- Comment directly on the issue thread  
- Reach out through GitHub Discussions or Oppia’s chat

---

**Thank you for contributing!**  
Every small fix helps make Oppia better for learners around the world.


