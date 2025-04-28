## Table of contents

- [Table of contents](#table-of-contents)
- [Why It Matters](#why-it-matters)
- [Before You Open Your PR](#before-you-open-your-pr)
- [What Makes a PR “Great”](#what-makes-a-pr-great)
  - [1. Clear Purpose](#1-clear-purpose)
  - [2. Focused Scope](#2-focused-scope)
  - [3. Helpful Description](#3-helpful-description)
  - [4. Show, Don’t Tell](#4-show-dont-tell)
  - [5. Tested \& Verified](#5-tested--verified)
- [Common Mistakes to Avoid](#common-mistakes-to-avoid)
- [Final Checklist Before You Request Review](#final-checklist-before-you-request-review)
- [Reviewers Appreciate...](#reviewers-appreciate)
- [Need Help?](#need-help)

This page is an introduction to creating a great Pull Request(PR). A great Pull Request (PR) is more than just code—it’s clean, clear, and easy for reviewers to understand. This guide shares best practices for writing high-quality PRs that are easy to review and quick to merge.

## Why It Matters

Contributing code is awesome—but making it **easy to review** is just as important. A thoughtful PR saves time for reviewers, avoids misunderstandings, and helps Oppia maintain a high standard of quality.

## Before You Open Your PR

Make sure you’ve:

- Created a branch off the latest `develop`
- Pulled the latest code: `git pull upstream develop`
- Tested your changes locally
- Passed all relevant tests
- Cleaned up your code (no stray debug logs or commented code)
- Written a fix plan (if required) and got it approved

## What Makes a PR “Great”

Here’s what makes a PR stand out:

### 1. Clear Purpose

Use a **descriptive PR title** and mention the issue number.

**Good:**  
`Fix #4567: Align navbar correctly on small screens`

**Bad:**  
`Update UI stuff`

### 2. Focused Scope

- Stick to **one topic per PR**
- Don’t sneak in unrelated changes
- Keep your PRs small when possible—**smaller PRs are faster to review**

### 3. Helpful Description

Fill out the PR template completely:

- What did you change?
- Why was it needed?
- Any tricky parts?
- Screenshots for UI changes
- Questions you want feedback on

### 4. Show, Don’t Tell

If your PR changes the UI, **include before-and-after screenshots**. This helps reviewers instantly understand the visual impact.

### 5. Tested & Verified

Before requesting review:

- All tests pass (unit, integration, lint)
- You've tested manually (especially for UI or logic changes)
- Edge cases are handled

## Common Mistakes to Avoid

| ❌ Don’t Do This | ✅ Do This Instead |
|------------------|--------------------|
| "Fix some stuff" in title | "Fix #1234: Add padding to dashboard cards" |
| Combine unrelated fixes | Separate into focused PRs |
| Skip writing a description | Clearly explain what and why |
| Add unfinished code | Only push code that’s ready |
| Forget screenshots | Add visual proof for UI changes |

## Final Checklist Before You Request Review

- My PR addresses **one issue only**
- I followed **Oppia’s code style**
- All **tests pass**
- I filled out the **PR template**
- I included **screenshots** (if needed)
- My commit message is clear and formatted
- I pushed the **latest code**
- I’m ready to **respond to reviews** promptly

## Reviewers Appreciate...

- Clean, readable code  
- Clear commit history  
- Context provided in comments if something’s non-obvious  
- Respect for their time  

## Need Help?

Don’t be afraid to ask! You can:

- Tag reviewers in comments
- Use GitHub Discussions
- Ask in Oppia’s chat or community channels

Thanks for taking the time to make your PR shine.  
High-quality PRs make Oppia better for everyone!
