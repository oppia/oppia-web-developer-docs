# Getting Ready for Open Source Day

## Table Of Contents
* [How To Get Started](#how-to-get-started)
* [Setting Up Before Open Source Day](#setting-up-before-open-source-day)
* [Some Useful Links](#some-useful-links)
* [Making A Code Change](#making-a-code-change)
* [What To Do When You Are Stuck](#what-to-do-when-you-are-stuck)
* [List Of Projects](#list-of-projects)

## How To Get Started
Welcome to Oppia! This wiki page aims to provide a quick-start guide to Oppia and guide you in making your first changes to Oppia's codebase. For a longer, more comprehensive guide to getting started, please see our [full "Getting Started" page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up).

Some background info about the project:
* The Oppia codebase sits in Github at https://github.com/oppia. Some knowledge of Github would be useful to make changes to the repository. Take a look at the [Github guides](https://guides.github.com/activities/hello-world/) for a brief introduction to Github along with some common methods! 
* AngularJS (v1) is used for Oppia's frontend. A nice youtube video tutorial can be found [here](https://www.youtube.com/watch?v=nO1ROKMjPqI&list=PLvZkOAgBYrsS_ugyamsNpCgLSmtIXZGiz). For an outline of AngularJS, please see this [short overview](https://egghead.io/articles/new-to-angularjs-start-learning-here) with pointers to other resources. 
* If you are new to HTML, some useful tutorials are [Mozilla's guide](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) (which includes some practice assessments), as well as [this tutorial for beginners](http://htmldog.com/guides/html/beginner/).
* Some new features will require backend work. Oppia's backend is written in Python 2.7.

## Setting Up Before Open Source Day

### Sign the CLA

Oppia is licensed under Apache v2. Please [sign the CLA](https://goo.gl/forms/AttNH80OV0) so that we can accept your contributions and redistribute the code you contribute under this license.

Once you've done this, you'll receive a confirmation email which includes some suggestions for next steps! These are completely optional, but if time permits, it might not be a bad idea to try a [starter project](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#finding-something-to-do) to get familiar with the codebase and development workflow.

### Create a GitHub account

To make code changes, you will require a Github account with 2 factor authentication set up.

* [Install Github](https://help.github.com/articles/set-up-git/).
* [Set up 2FA](https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/) on your GitHub account. This is important to prevent people from impersonating you.
  * You might need to create a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) so you can log in from the command line.
* Go to your settings page (click the Settings option under the profile menu in the top right), then go to 'Notifications' and ensure that everything's as you want it.
* (Optional) Consider setting up [automatic auth](https://help.github.com/articles/caching-your-github-password-in-git/) so you don't have to type in a username and password each time you commit a change.
* (Optional) Go to the [Oppia repo](https://github.com/oppia/oppia), and click 'Watch' at the top right. Ensure that you're not 'ignoring' the repo, so that you'll be notified when someone replies to a conversation you're part of.

### Install Oppia on your machine
* Create a new, empty folder called `opensource/` in your computer's home folder. Navigate to it (`cd opensource`), then [fork and clone](https://help.github.com/articles/fork-a-repo/) the Oppia repo so that it gets downloaded into `opensource/oppia`.
* Then follow the appropriate installation instructions -- [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29), [Windows](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29), [Vagrant](https://github.com/oppia/oppia/wiki/Installing-Oppia%28Vagrant%29). (If you run into any problems during installation, please read [these notes](https://github.com/oppia/oppia/wiki/Issues-with-installation%3F).)

## Some useful links
_Oppia_ [Wiki Page](https://github.com/oppia/oppia/wiki) | [Documentation](https://oppia.github.io/#/) | [Full "Getting Started" page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up)

_Github_ [Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) | [Guide](https://guides.github.com/activities/hello-world/)

_AngularJS_ [Tutorial](https://docs.angularjs.org/tutorial/index) | [Guide](https://docs.angularjs.org/guide)

_Python 2.7_ [Introduction](https://docs.python.org/2/library/intro.html) | [Tutorial](https://docs.python.org/2/tutorial/index.html) | [Documentation](https://docs.python.org/2/index.html)

_Bash_ [Introduction](http://cs.lmu.edu/~ray/notes/bash/)

## Making A Code Change
Our central development branch is **develop**, which should be clean and ready for release at any time. In general, all changes should be done as feature branches based off of _develop_. For a more detailed explanation on how to make a code change, please take a look at [this wiki page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#instructions-for-making-a-code-change). 
In order to make a change in the repository, you can follow the steps below:

1. Sync with the _develop_ branch and create a new branch, starting from _develop_ (e.g. _your-branch-name_). The branch name should be descriptive, lowercase, and hyphen-separated. It shouldn’t start with the words _hotfix_ or _release_.
```bash
git fetch upstream
git checkout develop  
git merge upstream/develop 
git checkout -b your-branch-name
```

2. Make commit(s) to your feature branch. Each commit should be self-contained and have a descriptive commit message that helps other developers understand why the changes were made.
   * Before your code gets uploaded to GitHub, a script is automatically executed that checks the styling of all changed files and runs some front-end tests. **Run the 'push' command in command line** as the script needs access to other tools like pip.
   * If any of the tests fail, the push will be interrupted. If this happens, fix the issues that the tests tell you about and repeat the instructions above ('commit' and then 'push').

3. When your feature is ready to merge, create a pull request on Github. When you create a pull request, you will be assigned a reviewer who will take a look at your code.

4. **Address review comments until all reviewers give LGTM ('looks good to me').**
   * Resolve any merge conflicts that arise.
   * Run `bash scripts/start.sh` and play with the dev server in order to make sure that everything still works, and also to install any new dependencies that have been added since you last synced the repo.
   * WARNING: Do not make changes using the online GitHub editor -- this bypasses lint/presubmit checks, and will cause the code on GitHub to diverge from the code on your machine. Always make commits locally, and then push to GitHub.

5. Tidy up! After the PR status has changed to "Merged", delete the feature branch from both your local clone and the GitHub repository

6. Celebrate. Congratulations, you have contributed to Oppia!

## What to do when you are stuck
We have a [Gitter chat room](https://gitter.im/oppia/oppia-chat) where everyone can post their questions and help each other out! The organizers and mentors will also be walking around to help with any questions.



## List of Projects

For this open source day, we tried to shortlist projects that are fairly self contained, and can be completed within 3-4 hours by a group of 2-3 people. We also tried to pick those projects from our issue tracker itself so that you get an idea of what it’s like to contribute to Oppia on a regular basis. 

Each project has a brief explanation, a link to the issue tracker, the skills required, and some deliverables. We encourage you to look at the issue tracker link for the project that interests you. You can comment expressing interest in that project (and mention you will be working on it for OSD). You can also gain more context and ask questions to help get a kickstart for the day. **Please work in groups of 2-3 people.** We also recommend everyone to try any one file within Project 8 (unit tests) before taking on larger projects, to get a feel for the codebase.

This list is not an exhaustive list of projects. If none of these projects appeal to you, [take a look at our issue tracker](https://github.com/oppia/oppia/issues) and comment on the issue that interests you. (also mention that you will be working on it during the OSD event so that we are aware). 

Please tag us (@seanlip and @vinitamurthi) in any comment expressing interest in a project so that we get notified about this!
If you would like to understand the vocabulary and general structure of content in Oppia, you can take a look at [this document](https://docs.google.com/document/d/1yFrFAXaKARzj1DSfiiy1pOH6ypugNkRLQGz5W5QifMQ/edit?usp=sharing).

***
### Project List

* [Project 1: Implement a reusable sort/filter list view for skills](#project-1-implement-a-reusable-sortfilter-list-view-for-skills)
* [Project 2: Create toasts for success messages](#project-2-create-toasts-for-success-messages)
* [Project 3: Use case-insensitive names rather than IDs in the URL for a resource](#project-3-use-case-insensitive-names-rather-than-ids-in-the-url-for-a-resource)
***
### Project 1: Implement a reusable sort/filter list view for skills
**Context**

At oppia, a topic is a high level concept related to a subject. Each topic can have multiple skills within it. For example - Topic ‘Fractions’ may contain skills - Finding the sum of two fractions with the same denominator. Questions will always be tied to a skill, and when we want to test a skill, we look up questions for that particular skill. Hence when creating topics, as well as questions, we need to go through a list of skills to tie that topic/question to.
The number of skills can be extremely large and going through such a big list gets difficult. So we would like to have a simple sort/filter view for the skills, which is reusable wherever the skills are listed down. (Bonus: Instead of creating a reusable sort/filter view only for skills, it would be nice to have a generic sort/filter list view that can be used for all types of data).
[[Issue Tracker Link](https://github.com/oppia/oppia/issues/5670)]

**Deliverables**

* Create a simple design document (1 - 2 pages) explaining the approach
* Create the sort/filter list view for skills in AngularJS
* (Optional) Make a sort/filter list view that can work with any data that is given to it (explain the design in the document)

**Required Skills**

Python, AngularJS, Web Development

**Difficulty**

Intermediate

***
### Project 2: Create toasts for success messages
**Context**

We have various flows where a user does some task and an AJAX request is sent to the backend. In case that results in an error, we show a toast with the error message. However, we do not inform the user on success. We would like to show a toast message to inform the user that their action is completed successfully.
[[Issue Tracker Link](https://github.com/oppia/oppia/issues/5671)]

**Deliverables**
* Go through the UI of oppia and try creating questions/skills/topics etc. Identify and list down all places where success message toasts would be useful
* Create the success message toasts in those areas with meaningful messages

**Required Skills**

AngularJS, Web Development

**Difficulty**

Easy

***

### Project 3: Use case-insensitive names rather than IDs in the URL for a resource
**Context**

Currently the ID of any resource (such as an exploration, collection, topic etc) shows up on the URL whenever we open that page. We do not want to expose these values in the URL and it would be nice to have the topic name show up instead. These names also need to be case insensitive.
[[Issue Tracker Link](https://github.com/oppia/oppia/issues/5672)]

**Deliverables**
* Write a small design document (1-2 pages) explaining the approach you will be taking to solve this problem
* Remove the IDs from the URLs for all resources

**Required Skills**

Python, AngularJS, Web Development

**Difficulty**

Intermediate
