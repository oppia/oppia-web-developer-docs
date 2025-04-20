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


