# SWESkills 2018

## Table Of Contents
* [Introduction](#introduction)
* [Structure of the Program](#structure-of-the-program)
* [List of Starter Projects](#list-of-starter-projects)
* [Some Useful Links](#some-useful-links)
* [Project 1](#project-1)
* [Project 2](#project-1)
* [Project 3](#project-1)
* [Project 4](#project-1)
* [Project 5](#project-1)
* [Project 6](#project-1)
* [Project 7](#project-1)
* [Project 8](#project-1)
* [Project 9](#project-1)
* [Project 10](#project-1)

## Introduction

[SWESkills Academy](http://www.sweskills.org/), a tech accelerator based in Nigeria, is collaborating with Oppia in 2018 to provide real-world engineering project opportunities for their students. This page documents the projects and general instructions.

## Structure of the Program

Participants should do 1 starter project, followed by one main project. The expected timelines are as follows:
- Starter project: by 28 October
- Main project (milestone 1): by 18 November (3 weeks)
- Main project (milestone 2): by 2 December (2 weeks)
- Main project (milestone 3): by 13 January (5 weeks)

It’s fine to start on a milestone early, but each milestone must be completed by the due date in order to pass the program. Otherwise, the participant fails.

Participants are expected to spend at least 3 hours each day working on their projects, for a total of at least 15 hours a week.

All code for the relevant project should pass review and be merged into the main trunk. Code will not be merged if it does not include sufficient tests, or if it does not function, or if it is messy and not maintainable. Mentors will try to review code within 24 hours of submission.

## List of starter projects

- [Designing and selecting proper icons for audio bar in the translation tab.](https://github.com/oppia/oppia/issues/5745)
- Animating state content height while the height changes dynamically changes the height. 
- [Replace proper text for latex symbols in autogen audio (Fraction, Power etc.)](https://github.com/oppia/oppia/issues/5303)
- [Provide a numerical status at the end of the progress bar.](https://github.com/oppia/oppia/issues/5729)
- Add saving log in the audio bar while saving is in progress.
- [https://github.com/oppia/oppia/issues/5310](https://github.com/oppia/oppia/issues/5310)
- [Other starter projects](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#finding-something-to-do)

_Note: These are just suggestions. Feel free to pick any issue on GitHub as well! These starter issues are intended to help you get familiar with the codebase and development workflow, so feel free to do more than one if you like._

## Some useful links
_Gitter_ [General chatroom](https://gitter.im/oppia/oppia-chat)

_Oppia_ [Wiki Page](https://github.com/oppia/oppia/wiki) | [Documentation](https://oppia.github.io/#/) | [Full "Getting Started" page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up)

_Github_ [Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) | [Guide](https://guides.github.com/activities/hello-world/)

_AngularJS_ [Tutorial](https://docs.angularjs.org/tutorial/index) | [Guide](https://docs.angularjs.org/guide)

_Python 2.7_ [Introduction](https://docs.python.org/2/library/intro.html) | [Tutorial](https://docs.python.org/2/tutorial/index.html) | [Documentation](https://docs.python.org/2/index.html)

_Bash_ [Introduction](http://cs.lmu.edu/~ray/notes/bash/)

***

### Project List

### Project 1: Takeout functionality

**Aim**: Being a good steward of user data includes providing easy and effective pathways for users to explore the data Oppia has stored in their Oppia profile. This project involves implementing the infrastructure, backend support, and frontend UIs needed for users to download user data associated with their profile from Oppia in a machine-readable format, and to provide an established pattern for exporting future user data.

**Team**: Data Privacy (mentor: **@BenHenning**)

**Type**: Full-stack

**Skills/knowledge utilized**:
- Python
- End-to-end web development
- App Engine & storage models
- Data representation

**Suggested milestones**
1. [Small] Implement established pattern for storage models to provide takeout data using a single model. Implement the backend functionality needed to serialize and export takeout dicts into a machine-readable format that can be downloaded by users’ browsers.
2. [Small] Implement the Takeout UI and backend controller to hook up to the download Takeout functionality. Verify this works end-to-end.
3. [Medium] Apply the pattern to all remaining models per the data policies, and enforce that storage models properly use this via backend tests. Implement integration tests to ensure exported models are correctly exported via Takeout. Add documentation to the Oppia wiki describing how to write storage models that need Takeout functionality.

***

### Project 2: Translation tab tests

**Aim**: Currently the backend test for adding state components goes manually for adding content id of each components and it covers the whole codebase, but we would like to make this process automate via a function and cleanup the test file related to it.  Also, this projects covers the e2e test for the translation tab in the initial milestones.

**Team**: Audio translations (mentor: **@DubeySandeep**)

**Type**: Backend and frontend

**Skills/knowledge utilized**:
- End-to-end testing
- Unit testing
- Python

**Helpful resources**:
- [Oppia's wiki page](https://github.com/oppia/oppia/wiki/End-to-End-Tests) for understanding end-to-end tests structure and pattern.
- [Translation tab project design doc](https://github.com/oppia/oppia/wiki/pdfs/GSoC2018SandeepDubey.pdf) to understand the functionality.

**Suggested milestones**:
1. [Small] Add e2e test for translation tab (Part-1). Currently the e2e test coverage for the translation tab is very less and most of the functionality aren’t covered through this milestone we are expecting to cover the given below functionality:
  - Uploading translated audio.
  - Check status color for each state in map view.
2. [Small] Add e2e test for translation tab (Part-2). In this milestone cover the remaining part of the e2e test:
  - Check components statuts for a state.
  - Check the progress bar.
3. [Medium] Cleanup backend tests. Currently once a developer adds feedback, hints & solution while writing backend tests they have to manually add content_id to those components and also add the same content id in the content_ids_to_audio_translations dict., through this milestone we are expecting to make this process automated. The expected workflow is mentioned in the points below:
  - Create a function to add feedback in the State object.
  - Make add_hint, add_feedback, add_solution handle content_id and add them directly to the contents_ids_to_audio_translations.
  - Cleanup the testfile in the codebase everywhere possible.

***

### Project 3: Implement Practice Sessions

**Aim**: The topic viewer page is supposed to be the location where everything related to a topic can be accessed. This includes the stories that teach the topic and the questions that test the skills associated with the topic. This project aims to add the latter, called practice sessions, to the topic viewer page, where a learner can quickly get some questions associated with the skills taught by the topic. 

**Team**: New Structures (mentor: **@aks681**)

**Type**: Frontend

**Skills/knowledge utilized**:
- AngularJS
- HTML/CSS
- Python (able to read and understand it, not required to write code in it)

**Suggested milestones**
_Note: The ENABLE_NEW_STRUCTURES flag in constants.js has to be set to true to access the topic viewer page._
1. [Small] Add a frontend API call to use the backend controller that returns a set of random questions given a set of skill ids to get the questions requested by the user.
2. [Small] Add the UI to the topic viewer page for the user to select a set of subtopics, after which the above created backend service should be called to get a random set of questions linked to the skills in the selected subtopics.
3. [Medium] The PretestEngineService can be used to render the received questions to the user, which the user should be able to play through, on completion of which, should be redirected back to topic viewer page.

***
### Project 4: Add "linked questions" section to skill editor.

**Aim**: A skill is meant to be the most basic unit of learning in Oppia. It has a concept card (that teaches the skill), some worked examples and a list of misconceptions associated with the skill. It also has a set of linked questions that tests the skill. Currently, in the skill editor, the former 3 fields are editable, but the set of linked questions associated with the skill are not visible in the editor. So, this project aims to add that feature to the skill editor.

**Team**: New Structures (mentor: **@aks681**)

**Type**: Full-stack

**Skills/knowledge utilized**:
- AngularJS
- HTML/CSS
- Python

**Suggested milestones**
_Note: The ENABLE_NEW_STRUCTURES flag in constants.js has to be set to true to access the the mentioned pages._
1. [Small] Modify get() in EditableSkillDataHandler in skill_editor.py to return all linked questions (querying the already existing function in question_services) as well.
2. [Small] Add a tab to skill editor (similar to current editor tab) which is blank for now, called ‘Questions’.
3. [Medium] Modify SkillEditorStateService to store these questions also (refer to TopicEditorStateService for examples) and render these questions as a table in the newly created tab.

***
### Project 5: Introduce Issues Tab

**Aim**:  Introduce Issues Tab to the exploration editor. The Issues Tab will use the stats we gather from students to create "issues" a creator can resolve to improve their exploration. For this project, we will begin by showing "Feedback" (things a learner had to say about an exploration) as issues. These already exist, so this will be a job of re-displaying the data as a new format.

**Team**: Lesson Improvement (mentor: **@brianrodri**)

**Type**: Frontend

**Skills/knowledge utilized**:
- AngularJS
- HTML/CSS
- Unit testing

**Suggested milestones**
1. [Small] Implement the empty Issues Tab page.
  - The page will be an empty HTML layout, with a supporting (but empty) directive.
  - This page will be hidden by a config flag. It should only be visible to creators when that flag is on.
  - Unit tests for the directive and flag’s behavior.
2. [Small] Expose Feedback Data through an API.
  - There will be a JSON schema we’d like you to follow. Your job will be adding data to the schema appropriately, and implementing a function which returns the list of feedback items.
  - Unit tests to make sure behavior works as expected (we will provide the list of desired behavior).
3. [Medium] Render and Implement the Feedback Card.
  - This card will be taking the JSON object prepared in step 2 and displaying it to the users. We have a mock already of the card, so you will need to implement the HTML/CSS to mirror that mock.
  - The card should contain an “archive” button, which when pressed, removes that particular item from the list created in step 2 (consequently updating the list we show to users)
  - Behavior tests which you will decide on and implement.

***
### Project 6: Strengthen presubmit checks

**Aim**: At Oppia, we try our best to keep the code base clean so that it’s easy for just any developer to take a glance and understand the code’s functionality. To enforce this, we rely on a number of checks, one of which are the pre-submit checks. These checks run before a developer pushes the code to a branch. This project aims to strengthen these pre-submit checks.

**Team**: Dev Workflow (mentor: **@apb7**)

**Type**: Backend and frontend

**Skills/knowledge utilized**:
- Basic understanding of AngularJS
- HTML
- Python

**Suggested milestones**
1. [Small] https://github.com/oppia/oppia/issues/5310 -- create a python script that does a size check for third_party
2. [Small] https://github.com/oppia/oppia/issues/5426 -- have a lint check to ensure that each Angular file contains exactly one service/directive/etc.
3. [Medium] https://github.com/oppia/oppia/issues/5069 -- remove $parent from HTML files. This involves two parts:
  - Remove all $parent from html files without breaking anything -- this will require manual testing and a good understanding of the code base. At the moment, we have 50 occurrences of $parent in 16 html files.
  - Add a check in the pre-commit script for this, similar to the one we have for js files.

***
### Project 7: Strengthen Python and CSS lint checks

**Aim**: At Oppia, we give a lot of focus to code readability and maintenance. Thus, the code base houses a number of custom checks which help us to realise the goal. This project aims to improve these checks by adding new lint checks for Python and CSS files.

**Team**: Dev Workflow (mentor: **@apb7**)

**Type**: Backend and frontend

**Skills/knowledge utilized**:
- CSS
- HTML
- Python

**Suggested milestones**
1. [Small] https://github.com/oppia/oppia/issues/5477 -- ensure that pylint pragmas are used only for disabling single lines
2. [Small] https://github.com/oppia/oppia/issues/5465 -- prevent storage layer importing domain layer, or domain layer importing controller layer
3. [Medium] Fully complete https://github.com/oppia/oppia/issues/5097 (add rules for CSS lint checks)

***
### Project 8: Building a contributor dashboard

**Aim**: For the community to help out in creating lessons effectively, there needs to be some mechanism using which the creators can communicate their requirements to the contributors. The current idea is to enable creators to display their lessons on a contributor dashboard. When a contributor accesses this lesson, items that require contributions should be highlighted. This includes open image requests, open translation requests, requests to improve hints/solutions, etc. Now when a contributor comes in, there must be an easy way for the contributor to isolate something of interest. This can be done using search options/filters for the open requests. 

**Team**: Community Contributions (mentor: **@nithusha21**)

**Type**: Full-stack

**Skills/knowledge utilized**:
- Full-stack development
- Technical design and implementation
- UI/UX development


**Suggested milestones**
1. [Small] Implement the backend changes required to move an exploration into a state where it is searchable in the contributor dashboard. This would involve creating a model which records which explorations are in this state, functions to move explorations into and out of this state. Also, a function should be written that gets statistics of existing placeholders, missing translation count, and other details to be displayed to an incoming contributor.
2. [Small] In the above model that tracks explorations in the newly created state, we should add all the tags associated with the exploration to aid searching in the contributor dashboard. The tags maybe something like "images", "translations", "update hints", or similar. Write a cron job that populates these tags on all the entries in the model. Write controllers to access data corresponding to the contributor dashboard.
3. [Medium] The following tasks are to be completed
  - Make the frontend for the contributor dashboard (this is the view that displays all the issues). 
  - A search bar or a set of filters would need to be implemented. This is to enable a translator to easily find which lesson has requests for translations, or a designer to easily find lessons requiring images, and so on. The contributor dashboard must contain filters to narrow down the search for a contributor.
  - On selecting a particular lesson, the relevant details for that lesson must be fetched from the backend created in tasks 1 and 2. Design an appropriate view that displays these details to a contributor, and also provides an easy pathway for the contributor to create a suggestion.

***
### Project 9:  Implement role-based art contributions (for explorations)

**Aim**: This project aims at implementing a framework which allows users to become designers for explorations. This will further aid in explorations being built by many users! The designers for an exploration are users responsible for adding images and illustrations. Typically, the person who wrote the exploration (creator/editor) will have some requirements for the image in mind. While drafting the exploration, placeholders with sufficient description should be added by the author. A designer will be able to add an image to a placeholder, or add a new image that wasn’t drafted earlier. This project is very significant as a lesson cannot be published unless all images are complete and images forms a significant part of the learner experience. 

**Team**: Community Contributions (mentor: **@nithusha21**)

**Type**: Full-stack

**Skills/knowledge utilized**:
- Technical design and implementation
- UI/UX development

**Suggested milestones**
1. [Small] Create a "designer" role for explorations. The designer should be able to only add images to an exploration. The concept of a placeholder needs to be created. A placeholder should contain a description which describes the image required in the placeholder. Make the backend changes to implement a placeholder.
2. [Small]  The operations allowed for a designer are add an image to a placeholder, create a new image. Functions that allow operations on explorations need to be modified to perform these new operations. Permission checks need to be added to make sure that a designer is only allowed to perform these operations. 
3. [Medium] Implement the frontend changes to make this feature work end to end. Provisions to add placeholders while creating a lesson must be added. The UI to add an image to a placeholder must be designed and implemented. An option must be provided in exploration settings page to add users as designers for an exploration. Also, a complete end to end test must be written in protractor that tests this user flow.

***
### Project 10: Translation tab accessibility and analytics

**Aim**: The aim of this project is to make the new translation tab more accessible and make easier to use and at the same time record the use case.

**Team**: Audio translations (mentor: **@DubeySandeep**)

**Type**: Full-stack

**Skills/knowledge utilized**:
- Frontend
- ARIA (developing for accessibility)

**Helpful resources**:
- [Learn ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
- [Video tutorial](https://www.youtube.com/watch?v=cOmehxAU_4s) on auditing accessibility. 

**Suggested milestones**
1. [Small] Add google analytics for usage of translation tab. Currently we use to record use case of oppia features through google analytics which can be found on SiteAnalyticsService.js, through this milestone we want to cover the use case of translation tab features.
2. [Small] Add keyboard shortcuts for "start" and "stop" recording. It would be great to have shortcut functionality for our recording feature, like keyboard shortcut to start and stop recording. 
3. [Medium] Accessibility audit of translation tab. Do a accessibility audit on translation tab and make the changes as such required to fix the accessibility issues. Auditing can be done through following ways:
  - Tabbing through translation tab.
  - Running "audit" for accessibility test from devtools. 

***