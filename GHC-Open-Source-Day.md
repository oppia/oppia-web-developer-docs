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
* Then follow the appropriate installation instructions -- [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29), [Windows](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29). (If you run into any problems during installation, please read [these notes](https://github.com/oppia/oppia/wiki/Issues-with-installation%3F).)

### Join the Gitter channel
* Join the GHC open source day chatroom at https://gitter.im/oppia/ghc2018 to meet other mentors and participants!

## Some useful links
_Gitter_ [GHC chatroom](https://gitter.im/oppia/ghc2018) | [General chatroom](https://gitter.im/oppia/oppia-chat)

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
   * Run `python -m scripts.start` and play with the dev server in order to make sure that everything still works, and also to install any new dependencies that have been added since you last synced the repo.
   * WARNING: Do not make changes using the online GitHub editor -- this bypasses lint/presubmit checks, and will cause the code on GitHub to diverge from the code on your machine. Always make commits locally, and then push to GitHub.

5. Tidy up! After the PR status has changed to "Merged", delete the feature branch from both your local clone and the GitHub repository

6. Celebrate. Congratulations, you have contributed to Oppia!

## What to do when you are stuck
Oppia has a [Gitter chat room](https://gitter.im/oppia/oppia-chat) where everyone can post their questions and help each other out! The organizers and mentors will also be walking around to help with any questions. We also have a dedicated [GHC Open Source Day chatroom](https://gitter.im/oppia/ghc2018) that you can use too!

## List of Projects

For Open Source Day, we tried to shortlist projects that are fairly self-contained, and can be completed within 3-4 hours by a group of 2-3 people. We also tried to pick those projects directly from our issue tracker, so that you get an idea of what it’s like to contribute to Oppia on a regular basis.

Each project has a brief explanation, a link to the issue tracker, the skills required, and some deliverables. We encourage you to look at the issue tracker link for the project that interests you. You can comment expressing interest in that project (and mention you will be working on it for OSD). Feel free to ask questions on the issue thread to gain more context, to help get a kickstart for the day! **We recommend working in groups of 2-3 people.** 

This list is not an exhaustive list of projects. If none of these projects appeal to you, take a look at our [issue tracker](https://github.com/oppia/oppia/issues) and comment on an issue that interests you. (Also, please mention that you will be working on it during the OSD event, so that others are aware. Please also tag us (**@seanlip** and **@vinitamurthi**) in any comment expressing interest in a project so that we get notified about this!)

**Note:** Some of the projects relate to functionality (like topics, skills and questions) that is still in development. You can turn it on by flipping the ENABLE_NEW_STRUCTURES flag in feconf.py. Also, if you'd like to understand the vocabulary and general structure of content in Oppia, please take a look at [this document](https://docs.google.com/document/d/1yFrFAXaKARzj1DSfiiy1pOH6ypugNkRLQGz5W5QifMQ/edit?usp=sharing). Please don't hesitate to ask us if you have any questions about this!

***
### Project List

We've tried to categorize the projects by difficulty, but please note that this is just a rough estimate and your mileage may vary. Feel free to pick any project that interests you :)

Also, we recommend trying any file within Project 8 (unit tests) before taking on larger projects, so that you can get a good feel for the codebase and the development workflow. You're welcome to do this before Open Source Day, if you like!

Starter project
* [Project 8: Improve unit tests](#project-8-improve-unit-tests)

Easy
- [Getting Ready for Open Source Day](#getting-ready-for-open-source-day)
  - [Table Of Contents](#table-of-contents)
  - [How To Get Started](#how-to-get-started)
  - [Setting Up Before Open Source Day](#setting-up-before-open-source-day)
    - [Sign the CLA](#sign-the-cla)
    - [Create a GitHub account](#create-a-github-account)
    - [Install Oppia on your machine](#install-oppia-on-your-machine)
    - [Join the Gitter channel](#join-the-gitter-channel)
  - [Some useful links](#some-useful-links)
  - [Making A Code Change](#making-a-code-change)
  - [What to do when you are stuck](#what-to-do-when-you-are-stuck)
  - [List of Projects](#list-of-projects)
    - [Project List](#project-list)
    - [Project 1: Implement a reusable sort/filter list view for skills](#project-1-implement-a-reusable-sortfilter-list-view-for-skills)
    - [Project 2: Create toasts for success messages](#project-2-create-toasts-for-success-messages)
    - [Project 3: Use case-insensitive names rather than IDs in the URL for a topic](#project-3-use-case-insensitive-names-rather-than-ids-in-the-url-for-a-topic)
    - [Project 4: Allow users to suggest new questions for a skill](#project-4-allow-users-to-suggest-new-questions-for-a-skill)
    - [Project 5: Allow users to suggest edits to concept cards](#project-5-allow-users-to-suggest-edits-to-concept-cards)
    - [Project 6: Allow translators to see the changes made in content by editor](#project-6-allow-translators-to-see-the-changes-made-in-content-by-editor)
    - [Project 7: Improve linter checks](#project-7-improve-linter-checks)
    - [Project 8: Improve unit tests](#project-8-improve-unit-tests)
    - [Project 9: Writing Selenium tests for interactions](#project-9-writing-selenium-tests-for-interactions)
    - [Project 10: Expose "upload exploration" functionality in admin page](#project-10-expose-%22upload-exploration%22-functionality-in-admin-page)
    - [Project 11: Randomize the pretest questions.](#project-11-randomize-the-pretest-questions)
    - [Project 12: Multiple choice answers could be shuffled](#project-12-multiple-choice-answers-could-be-shuffled)
    - [Project 13: Find ways to make the audio translation tab interface clearer](#project-13-find-ways-to-make-the-audio-translation-tab-interface-clearer)
    - [Project 14: Feedback threads in feedback tab do not reorder by recent updates in real time](#project-14-feedback-threads-in-feedback-tab-do-not-reorder-by-recent-updates-in-real-time)
    - [Project 15: Speed Improvements](#project-15-speed-improvements)
    - [Project 16: Cross Browser Compatibility Improvement - Translation console for Safari](#project-16-cross-browser-compatibility-improvement---translation-console-for-safari)
    - [Project 17: Improving the library page experience on mobile](#project-17-improving-the-library-page-experience-on-mobile)
    - [Project 18: Accessibility Improvements - Tabbing Order](#project-18-accessibility-improvements---tabbing-order)
    - [Project 19: Accessibility Improvements - Fixing Contrast in Image Region Selectors](#project-19-accessibility-improvements---fixing-contrast-in-image-region-selectors)


Intermediate
* [Project 1: Implement a reusable sort/filter list view for skills](#project-1-implement-a-reusable-sortfilter-list-view-for-skills)
* [Project 3: Use case-insensitive names rather than IDs in the URL for a resource](#project-3-use-case-insensitive-names-rather-than-ids-in-the-url-for-a-resource)
* [Project 11: Randomize the pretest questions](#project-11-randomize-the-pretest-questions)
* [Project 12: Multiple choice answers could be shuffled](#project-12-multiple-choice-answers-could-be-shuffled)
* [Project 15: Speed Improvements](#project-15-speed-improvements)

Hard
* [Project 4: Allow users to suggest new questions for a skill](#project-4-allow-users-to-suggest-new-questions-for-a-skill)
* [Project 5: Allow users to suggest edits to concept cards](#project-5-allow-users-to-suggest-edits-to-concept-cards)
* [Project 6: Allow translators to see the changes made in content by editor](#project-6-allow-translators-to-see-the-changes-made-in-content-by-editor)


***
### Project 1: Implement a reusable sort/filter list view for skills
**Context**

We are currently working on organizing our lessons into topics. At Oppia, a topic is a high-level concept related to a subject. Each topic can have multiple skills within it -- for example, the topic "Fractions" may contain the skill "find the sum of two fractions with the same denominator". Questions will always be tied to a skill, and when we want to test a skill, we look up questions for that particular skill. Hence, when creating topics, as well as questions, we need to go through a list of skills to tie that topic/question to. Unfortunately, the number of skills can be extremely large and going through such a big list gets difficult. So we would like to have a simple sort/filter view for the skills, which is reusable wherever the skills are listed down. (Bonus: Instead of creating a reusable sort/filter view only for skills, it would be nice to have a generic sort/filter list view that can be used for all types of data). Note that, since the feature is currently in development, you'll need to enable the feconf.ENABLE_NEW_STRUCTURES flag and log in as an admin to use the skill editor.
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

We have various flows where a user does a task and an AJAX request is sent to the backend. When this results in an error, we show a toast with the error message. However, we do not inform the user on success. We would like to show a toast message to inform the user that their action is completed successfully.
[[Issue Tracker Link](https://github.com/oppia/oppia/issues/5671)]

**Deliverables**
* Go through the UI of oppia and try creating questions/skills/topics etc. Identify and list down all places where success message toasts would be useful. (Note that, since skills etc. are currently in development, you'll need to enable the feconf.ENABLE_NEW_STRUCTURES flag and log in as an admin to use these pages.)
* Create success message toasts in those areas with meaningful messages.

**Required Skills**

AngularJS, Web Development

**Difficulty**

Easy

***

### Project 3: Use case-insensitive names rather than IDs in the URL for a topic
**Context**

Currently the ID of a topic shows up on the URL whenever we open that page. We would like to have a human-readable topic name show up in the URL instead, similar to Wikipedia. These names should probably be case-insensitive. (Note that, since topics are currently in development, you'll need to enable the feconf.ENABLE_NEW_STRUCTURES flag and log in as an admin to use these pages.) [[Issue Tracker Link](https://github.com/oppia/oppia/issues/5672)]

**Deliverables**
* Write a small design document (1-2 pages) explaining the approach you will be taking to solve this problem, including ensuring that URLs are unique across topics.
* Remove the IDs from the URLs for all resources

**Required Skills**

Python, AngularJS, Web Development

**Difficulty**

Intermediate


***

### Project 4: Allow users to suggest new questions for a skill
**Context**

We are currently working on a project to add practice questions to Oppia. Currently, Oppia supports the creation of questions by topic managers and admins. However, in the long run, Oppia aims to be a collaborative platform for create lessons, so it would be great if we could enable any user to suggest a new question for a particular skill. These suggestions can then be reviewed and then either added (with or without modifications), or rejected. We need to design a framework to support this option. We already have a suggestion framework designed for edits to lesson content, and if possible we would like to reuse that for question suggestions as well.

_This project is more aimed at creating a design rather than a working implementation, as it is quite open ended and will take time to create a working solution. However, if you plan on taking this up, we encourage you to continue to work with us on this project even after open source day!_
[[Issue Tracker Link](https://github.com/oppia/oppia/issues/5673)]

**Deliverables**
* Present a design for a framework that can enable user suggestions for questions.

**Required Skills**

Python, AngularJS, Web Development

**Difficulty**

Hard

***
### Project 5: Allow users to suggest edits to concept cards
**Context**

We are developing a feature that allows topic managers to add concept cards whenever they create a topic. These concept cards each aim to explain a particular skill, and they get shown on-demand in lessons when Oppia detects that a student is having difficulty with that skill. It would be very useful to have users suggest edits to the concept cards. Edit suggestions could range from grammar issues or typos, semantic improvements, or even adding new content like examples to better explain the concept. The topic manager can review the edit, and either add it (with modifications), or reject it with some explanation. 

_This project is more to create a design rather than a working implementation, as it is quite open-ended and will take time to create a working solution. However, if you plan on taking this up, we encourage you to continue to work with us on this project even after open source day!_
[[Issue Tracker Link](https://github.com/oppia/oppia/issues/5674)]

**Deliverables**
* Present a design for a framework that can enable user suggestions for concept cards.

**Required Skills**

Python, AngularJS, Web Development

**Difficulty**

Hard

***
### Project 6: Allow translators to see the changes made in content by editor
**Context**

All lessons in Oppia aim to have audio subtitles for learners who do not have a good command of English. These audio files are translated to multiple languages by translators. Currently, when a lesson creator marks an audio file as "needing update", the translators get informed about this through a warning icon, but it's not easy for them to figure out what changes the lesson creator has made. We would like to develop this functionality for the translators. For this, we would have to design and implement a UI which helps translators identify where the change was made and what the change was. 
[[Issue tracker link](https://github.com/oppia/oppia/issues/5571)]

**Deliverables**
* Write a design document for a user interface that solves this problem.
* Create an MVP (minimum viable product) for the interface.

**Required Skills**

Python, AngularJS, Web Development

**Difficulty**

Hard
***
### Project 7: Improve linter checks
**Context**

Coding style is very important when maintaining a large codebase with multiple contributors! Oppia has a [style guide](https://github.com/oppia/oppia/wiki/Coding-style-guide) that highlights basic requirements for coding style. To ensure our code follows the style guide, we use lint-check scripts that are called before any code is pushed in the github repo. However, our Python linter doesn’t check if strings use single quotes and not double quotes. It would be useful to have that check added for Python as well.
[[Issue tracker link](https://github.com/oppia/oppia/issues/5663)]

**Deliverables**
* Update the python linter checks to ensure strings use single quotes
* (Optional) Identify any other code style issues that are not being caught by our linter

**Required Skills**

Python, Bash

**Difficulty**

Easy

***

### Project 8: Improve unit tests
**Context**

Unit tests are just as important as coding style while maintaining a large codebase with multiple contributors. At Oppia, we try to ensure all code paths are covered by some unit test. This also ensures that changes to the code don’t break our code base. Before pushing code to github, we run all frontend tests and the push is blocked if even one test is broken. Also, code cannot be merged into the main branch unless both frontend and backend tests pass (the backend checks are done through a [Travis](https://travis-ci.com/) continuous integration system). We analyze the code coverage of unit tests to identify which functions still need unit tests. 

_These projects are typically the kinds of starter projects we assign to new developers. Consider giving this a shot before moving to a larger project!_

Frontend Tests: [[Issue tracker link](https://github.com/oppia/oppia/issues/4057)]

Backend Tests: [[Issue tracker link](https://github.com/oppia/oppia/issues/5134)]

**Deliverables**
* Write a unit test for any frontend or backend file that covers all code paths.

**Required Skills**

AngularJS (Frontend), Python (Backend)

**Difficulty**

Easy
***

### Project 9: Writing Selenium tests for interactions
**Context**

While unit tests cover a lot of cases, end-to-end integration tests are also extremely useful to ensure all UI elements are working as intended. It can also catch bugs that unit tests may not be able to, such as UI elements not being in view, browsers freezing, and so on. We use Protractor end-to-end tests to cover these cases (Protractor is an end-to-end testing framework based on Selenium). The goal would be to pick up one of Oppia's question types ("interactions") and write Protractor tests for it that are similar to the existing examples for other interactions in the codebase.
[[Issue tracker link](https://github.com/oppia/oppia/issues/4558)]

**Deliverables**
* Write one end to end interaction test in selenium

**Required Skills**

Javascript 

**Difficulty**

Easy
***

### Project 10: Expose "upload exploration" functionality in admin page
**Context**

Oppia uses explorations to present lessons to the user ([example](https://www.oppia.org/explore/umPkwp0L1M0-?collection_id=4UgTQUc1tala)). When developing, it is sometimes useful to upload an exploration, but this functionality should be limited to developers and not turned on in production. We would therefore like to create an upload exploration button in the Activities tab of the admin page (which gets shown only on develop and not in production).
[[Issue tracker link](https://github.com/oppia/oppia/issues/5438)]

**Deliverables**
* Fix the issue mentioned in the tracker and present it

**Required Skills**

AngularJS, Web Development

**Difficulty**

Easy
***
### Project 11: Randomize the pretest questions.
**Context**

A pretest is a variably-long set of questions that has been randomly created from the list of prerequisite skills specified by a lesson. Before learning a lesson with prerequisites, students have to pass the pretest for every prerequisite skill. Currently, the first 3 pretest questions sorted by their keys will be returned for a fixed set of prerequisite skill ids for an exploration. This needs to be changed to make it a random set of 3 questions (or potentially some other smarter approach to selecting the questions). (Note that, since questions are currently in development, you'll need to enable the feconf.ENABLE_NEW_STRUCTURES flag and log in as an admin to use these pages.) [[Issue tracker link](https://github.com/oppia/oppia/issues/5436)]

**Deliverables**
* Design and implement a solution to randomize the pretest questions
* (Optional) Create a design to select pretest questions in a smarter way (some possible directions could be to select maybe by difficulty or by user performance in the previous questions or similar skills)

**Required Skills**

AngularJS, Python

**Difficulty**

Intermediate
***
### Project 12: Multiple choice answers could be shuffled

**Context**

In the learner view, multiple-choice answers are always in the same order. We should instead consider shuffling them on-the-fly (while preserving the "index" that's currently reported to the backend) so that the student does not end up memorizing the correct answer based on its location if they need to repeat the question later. (This sometimes happens when, in a future question, Oppia detects that the student has not mastered a prerequisites skill.) [[Issue tracker link](https://github.com/oppia/oppia/issues/5254)]

**Deliverables**
* Write a design document with the approach to solve this problem
* Implement a solution that can shuffle multiple choice answers

**Required Skills**

AngularJS, Python

**Difficulty**

Intermediate
***

### Project 13: Find ways to make the audio translation tab interface clearer
**Context**

The UI for the audio translation isn’t very intuitive. Users have asked questions like - 
* "I uploaded the voiceover but can't find where I can listen to it?"
* "Also how do I move to the next section?"

This suggests that we might need to make the UI/layout a bit more clear.
[[Issue tracker link](https://github.com/oppia/oppia/issues/5639)]

**Deliverables**
* Write a design document with mocks for a potential UI
* Present the mocks and (optional) create the bare bones UI for the same.

**Required Skills**

UI/UX Design experience would be useful

**Difficulty**

Easy
***
### Project 14: Feedback threads in feedback tab do not reorder by recent updates in real time
**Context**

It is possible for students to submit feedback to any exploration, and this generates an "issue thread" which can have further messages appended to it. The feedback threads are viewable within the exploration editor, but they are not ordered correctly. We would like to order them in real-time to show the most recent feedback threads at the top.
[[Issue tracker link](https://github.com/oppia/oppia/issues/5508)]

**Deliverables**
* Take a look at the issue and design and implement a solution that follows the expected behavior.

**Required Skills**

AngularJS, Python

**Difficulty**

Easy
***
### Project 15: Speed Improvements
**Context**

A primary audience of Oppia is students in developing countries such as India and Africa. At such places, network issues arise quite often. Moreover, the devices that the students use tend to be low-performing, and optimization and speed improvements are something we constantly try to work towards. One case is to determine which version/resolution of an image to send, based on the quality of the network.
[[Issue tracker link](https://github.com/oppia/oppia/issues/5470)]

**Deliverables**
* Write a design doc explaining the approach to solving this problem
* Implement the solution and present it (You can use chrome dev tools to change network conditions)

**Required Skills**

AngularJS, Python

**Difficulty**

Intermediate
***


### Project 16: Cross Browser Compatibility Improvement - Translation console for Safari
**Context**

Audio subtitles in lessons are really important for learners in our target audience. However, we have encountered several issues with the Safari browser. For example, the translation console in Safari doesn’t play the audio correctly. Users have reported that after uploading audio, they click on the icon to the far left to listen but nothing happens. This is only on Safari; it works fine in Chrome.
Also, the audio player at the bottom shows NaN/NaN which indicates that the audio is most likely not loading correctly on Safari. The UI elements also dont seem to be rendered correctly. We would like to fix the audio player experience for the translation console on Safari browsers.
[[Issue tracker link](https://github.com/oppia/oppia/issues/5642)]

**Deliverables**
* Design and implement a fix for the audio player in the translation console, that works across all major browsers.

**Required Skills**

AngularJS, Web Development

**Difficulty**

Easy

### Project 17: Improving the library page experience on mobile
**Context**

The Oppia library can show only one exploration at a time on the mobile UI. It has arrow icons that can be clicked to move to the next exploration, but this is not very intuitive for mobile views, especially now that swipe gestures are so common. We would like to make the explorations into a swipeable carousel for the mobile UI.
[[Issue tracker link](https://github.com/oppia/oppia/issues/5678)]

**Deliverables**
* Create a swipeable carousel for the explorations in oppia.org
* (Optional) Create a reusable swipeable carousel element that can be used as a template. Write a design document for this as well

**Required Skills**

AngularJS, Web Development

**Difficulty**

Easy
***

### Project 18: Accessibility Improvements - Tabbing Order
**Context**

We have found some accessibility-related issues in Oppia that we would like to improve. This project looks at tabbing order. Tabbing is useful for screen readers and various other accessibility software, and our order of tabbing is wrong; we would like to fix that. More details can be found in the issue tracker:
[[Issue tracker link](https://github.com/oppia/oppia/issues/4883)]

**Deliverables**
* Fix the tabbing order for the menu bars and other buttons and UI elements

**Required Skills**

Web Development

**Difficulty**

Easy

***
### Project 19: Accessibility Improvements - Fixing Contrast in Image Region Selectors
**Context**

Our Image region indicators show a red dot when a user clicks on a portion of the image (regardless of the image background at that area). The aim of this issue is to ensure that the indicator contrasts with the background, so that it's clear that it's a touch indicator. 
[[Issue tracker link](https://github.com/oppia/oppia/issues/4615)]

**Deliverables**
* Design and implement a solution that can clearly show image region indicators to the user (either by using dots with contrasting colors, or using a different shape or a larger size)

**Required Skills**

AngularJS, Web Development

**Difficulty**

Easy
***
