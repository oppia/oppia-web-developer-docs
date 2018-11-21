## Table Of Contents
* [Introduction](#introduction)
* [List of Starter Projects](#list-of-starter-projects)
* [Some Useful Links](#some-useful-links)
* [Project List](#project-list)
  * [Project 1](#project-1-takeout-functionality)
  * [Project 2](#project-2-translation-tab-tests)
  * [Project 3](#project-3-implement-practice-sessions)
  * [Project 4](#project-4-add-a-linked-questions-section-to-the-skill-editor)
  * [Project 5](#project-5-introduce-issues-tab)
  * [Project 6](#project-6-strengthen-presubmit-checks)
  * [Project 7](#project-7-strengthen-python-and-css-lint-checks)
  * [Project 8](#project-8-building-a-contributor-dashboard)
  * [Project 9](#project-9--implement-role-based-art-contributions-for-explorations)
  * [Project 10](#project-10-translation-tab-accessibility-and-analytics)

## Introduction

This is a list of "bite-sized" projects that we created in 2018 for a collaboration with SWESkills. Unfortunately, due to infrastructural issues, the collaboration did not work out, but the list of projects is still relevant and useful! If you're interested in taking up a project, please contact the relevant team lead.

(Also, if you're interested in GSoC: please note that these projects are somewhat smaller than the ones we typically propose for GSoC. However, they might be good practice if you're interested in doing a larger project with Oppia in the future.)

## List of starter projects

- [Designing and selecting proper icons for audio bar in the translation tab.](https://github.com/oppia/oppia/issues/5745)
- [Animating state content height while the height changes dynamically changes the height.](https://github.com/oppia/oppia/issues/5747) 
- [Replace proper text for latex symbols in autogen audio (Fraction, Power etc.)](https://github.com/oppia/oppia/issues/5303)
- [Provide a numerical status at the end of the progress bar.](https://github.com/oppia/oppia/issues/5729)
- [Add saving log in the audio bar while saving is in progress.](https://github.com/oppia/oppia/issues/5746)
- [Create a python script that does a size check for third_party.](https://github.com/oppia/oppia/issues/5310)
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
1. [Small] Implement established pattern for storage models to provide takeout data using a single model. Implement the backend functionality needed to serialize and export takeout dicts into a machine-readable format that can be downloaded by users' browsers.
2. [Small] Implement the Takeout UI and backend controller to hook up to the download Takeout functionality. Verify this works end-to-end.
3. [Medium] Apply the pattern to all remaining models per the data policies, and enforce that storage models properly use this via backend tests. Implement integration tests to ensure exported models are correctly exported via Takeout. Add documentation to the Oppia wiki describing how to write storage models that need Takeout functionality.

***

### Project 2: Translation tab tests

**Aim**: Oppia has introduced a new translation tab for exploration translators. This was made to ease the process of translating an exploration. The aim of this project is to add e2e tests for the translation tab, and simplify the backend tests. (Currently, the latter are clunky because they need to handle the content IDs for translatable content manually; we would like to automate this process and clean up the related test file.)

**Team**: Audio translations (mentor: **@DubeySandeep**)

**Type**: Backend and frontend

**Skills/knowledge utilized**:
- End-to-end testing
- Unit testing
- Python

**Helpful resources**:
- [Oppia's wiki page](https://github.com/oppia/oppia/wiki/End-to-End-Tests), for understanding the structure and pattern of end-to-end tests.
- [Translation tab project design doc](https://github.com/oppia/oppia/wiki/pdfs/GSoC2018SandeepDubey.pdf) to understand the functionality.

**Suggested milestones**:
1. [Small] Add e2e test for translation tab (Part-1). Currently the e2e test coverage for the translation tab is too small, and most functionality isn't covered. This milestone covers the following functionality:
    - Uploading translated audio.
    - Checking that the status color is correct for each card ("state") in the exploration overview.
2. [Small] Add e2e test for translation tab (Part-2). This milestone covers the remaining e2e test functionality:
    - Check the status of each component for a card.
    - Check that the progress bar display is correct.
3. [Medium] Clean up backend tests. Currently, when a developer adds feedback, hints and solutions while writing backend tests, they have to manually add content_ids to those components and also add the same content id in the content_ids_to_audio_translations dict. This milestone aims to simplify this process. The expected workflow is described in the points below:
    - Create helpful utility functions to, e.g., add feedback to a State object.
    - Make each of add_hint, add_feedback, add_solution do both of the following: handle the content_id, and add the content IDs directly to the content_ids_to_audio_translations dict.
    - Clean up the test files in the codebase wherever possible.

***

### Project 3: Implement Practice Sessions ([#5893](https://github.com/oppia/oppia/issues/5893))

**Aim**: A topic (like "Fractions") is a collection of lessons. The topic viewer page is supposed to be the location where everything related to a topic can be accessed. This includes the stories that teach the topic, as well as practice sessions which include a set of questions that test skills associated with the topic. This project aims to add practice sessions to the topic viewer page, so that learners can quickly attempt some questions associated with the skills taught by the topic.

**Team**: New Structures (mentor: **@aks681**)

**Type**: Frontend

**Skills/knowledge utilized**:
- AngularJS
- HTML/CSS
- Python (able to read and understand it, not required to write code in it)

**Suggested milestones**
_Note: The ENABLE_NEW_STRUCTURES flag in constants.js has to be set to true to access the topic viewer page._
1. [Small] Add a frontend API call to use the backend controller that returns a set of random questions given a set of skill ids to get the questions requested by the user.
2. [Small] Add a UI to the topic viewer page for the user to select a set of subtopics, after which the backend service created in milestone 1 should be called to get a random set of questions linked to the skills in the selected subtopics.
3. [Medium] The PretestEngineService can be used to render the received questions to the user, which the user should be able to play through. When they complete the series of questions, they should be redirected back to the topic viewer page.

***
### Project 4: Add a "linked questions" section to the skill editor. ([#5894](https://github.com/oppia/oppia/issues/5894))

**Aim**: A skill is meant to be the most basic unit of learning in Oppia. It has a concept card (that teaches the skill), some worked examples, and a list of misconceptions associated with the skill. It also has a set of linked questions that test the skill. Currently, in the skill editor, the former 3 fields are editable, but the set of linked questions associated with the skill is not visible in the editor. So, this project aims to add that feature to the skill editor.

**Team**: New Structures (mentor: **@aks681**)

**Type**: Full-stack

**Skills/knowledge utilized**:
- AngularJS
- HTML/CSS
- Python

**Suggested milestones**
_Note: The ENABLE_NEW_STRUCTURES flag in constants.js has to be set to true to access the the mentioned pages._
1. [Small] Modify get() in EditableSkillDataHandler in skill_editor.py to return all linked questions (querying the already existing function in question_services) as well.
2. [Small] Add a 'Questions' tab to the skill editor (similar to current editor tab) which is blank for now.
3. [Medium] Modify SkillEditorStateService to also store these questions (refer to TopicEditorStateService for examples) and render them as a table in the newly-created tab.

***
### Project 5: Introduce Issues Tab ([#5798](https://github.com/oppia/oppia/issues/5798))

**Aim**: Add a new Issues Tab to the exploration editor page. The Issues Tab will use the stats we gather from students to create "issues" a creator can resolve to improve their exploration. For this project, we will begin by showing "Feedback" (things a learner had to say about an exploration) as issues that lesson creators can address. These already exist, so the main part of this project will involve re-displaying the data in a new format.

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
    - Unit tests for the directive and flag's behavior should be implemented.
2. [Small] Expose Feedback Data through an API.
    - There will be a JSON schema we’d like you to follow. Your job will be adding data to the schema appropriately, and implementing a function which returns the list of feedback items.
    - Unit tests should be implemented to ensure that the behavior works as expected. (We will provide the list of desired behaviors.)
3. [Medium] Render and Implement the Feedback Card.
    - This card takes the JSON object prepared in step 2 and displays it to the users. We already have a mock of the card, so you will need to implement the HTML/CSS to mirror that mock.
    - The card should contain an "archive" button. When this button is pressed, the corresponding item should be removed from the list created in step 2 (consequently updating the list we show to users)
    - You will need to devise and implement tests to verify the expected frontend and end-to-end behaviors.

***
### Project 6: Strengthen presubmit checks

**Aim**: At Oppia, we try our best to keep the codebase clean so that it's as easy as possible for new developers to understand the code's functionality. To enforce this, we rely on a number of checks, one of which are the pre-submit checks. These checks run before a developer pushes the code to a branch. This project aims to strengthen these pre-submit checks.

**Team**: Dev Workflow (mentor: **@apb7**)

**Type**: Backend and frontend

**Skills/knowledge utilized**:
- Basic understanding of AngularJS
- HTML
- Python

**Suggested milestones**
1. [Small] https://github.com/oppia/oppia/issues/5420 -- parse .travis.yml to ensure consistency between the two lists of variables.
2. [Small] https://github.com/oppia/oppia/issues/5426 -- have a lint check to ensure that each Angular file contains exactly one service/directive/etc.
3. [Medium] https://github.com/oppia/oppia/issues/5069 -- remove $parent from HTML files. This involves two parts:
    - Remove all occurrences of $parent from html files without breaking anything -- this will require manual testing and a good understanding of the code base. At the moment, we have 50 occurrences of $parent in 16 html files.
    - Add a check in the pre-commit script for this, similar to the one we have for JavaScript files.

***
### Project 7: Strengthen Python and CSS lint checks

**Aim**: At Oppia, we give a lot of focus to code readability and maintenance. The code base includes a number of custom checks which help us to realize this goal. This project aims to improve these checks by adding new lint checks for Python and CSS files.

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

**Aim**: For the community to help out in creating lessons effectively, there needs to be a way for creators to communicate their requirements to contributors. The current idea is to enable creators to display their lessons on a contributor dashboard. When a contributor accesses this lesson, items that require contributions should be highlighted. This includes open image requests, open translation requests, requests to improve hints/solutions, etc. No, when a contributor visits this dashboard, they should be able to easily identify something of interest and start helping with it. This can be done using search options/filters for the open requests.

**Team**: Community Contributions (mentor: **@nithusha21**)

**Type**: Full-stack

**Skills/knowledge utilized**:
- Full-stack development
- Technical design and implementation
- UI/UX development


**Suggested milestones**
1. [Small] Implement the backend changes required to make it possible for certain explorations to be searchable in the contributor dashboard. This would involve creating a model which records which explorations are in this state, and functions to move explorations into and out of this state. Also, a function should be written that gets statistics of existing placeholders, missing translation count, and other details to be displayed to an incoming contributor.
2. [Small] In the above model that tracks explorations in the newly created state, we should add all the tags associated with the exploration to aid searching in the contributor dashboard. The tags may include things like "images", "translations", "update hints", or similar. Write a cron job that populates these tags on all the entries in the model. Write backend controller endpoints to retrieve data corresponding to the contributor dashboard.
3. [Medium] The following tasks are to be completed
    - Make the frontend for the contributor dashboard (this is the view that displays all the issues). 
    - Implement a search bar or a set of filters. This enables a translator to easily find which lessons have requests for translations, or a designer to easily find lessons requiring images, and so on. The contributor dashboard must contain filters to allow contributors to narrow down their search.
    - On selecting a particular lesson, the relevant details for that lesson must be fetched from the backend created in milestones 1 and 2. Design an appropriate view that displays these details to a contributor, and also provides an easy pathway for the contributor to create a suggestion.

***
### Project 9:  Implement role-based art contributions (for explorations)

**Aim**: This project aims to implement a framework which allows users to become designers for explorations. This will further aid in explorations being built by many users! The designers for an exploration are responsible for adding images and illustrations. Typically, the person who wrote the exploration (creator/editor) will have some requirements for the image in mind. While drafting the exploration, placeholders with sufficient description should be added by the author. A designer can then create an image to replace the placeholder. This project has significant impact because a lesson cannot be published unless all images are complete, and, especially since we are working with low-literacy students, images form a significant part of the learner experience. 

**Team**: Community Contributions (mentor: **@nithusha21**)

**Type**: Full-stack

**Skills/knowledge utilized**:
- Technical design and implementation
- UI/UX development

**Suggested milestones**
1. [Small] Create the concept of an "image placeholder". A placeholder should contain a description which describes the image required in the placeholder. Make the backend changes to implement a placeholder. Also, create a "designer" role for explorations; the designer should only be able to add images to an exploration. 
2. [Small] The only operation allowed for a designer is to add an image to a placeholder. Functions that allow operations on explorations need to be modified to include this new operation. Permission checks need to be added to make sure that a designer is only allowed to perform this operation. 
3. [Medium] Implement the frontend changes to make this feature work end to end. Provisions to add placeholders while creating a lesson must be added. The UI to add an image to a placeholder must be designed and implemented. An option must be provided in the exploration settings page to add users as designers for an exploration. Also, a complete end-to-end test must be written in Protractor that tests this user flow.

***
### Project 10: Translation tab accessibility and analytics

**Aim**: Oppia has introduced a new translation tab for exploration translators to ease the process of translating an exploration. Currently, the translation tab is in working condition, but it lacks accessibility features. Now that the translation tab is released and the community is aware about it, it would be great to make it more accessible and understand how it is being used. The aim of this project is to make the new translation tab more accessible and to make the translation process easier for contributors. 

**Team**: Audio translations (mentor: **@DubeySandeep**)

**Type**: Full-stack

**Skills/knowledge utilized**:
- Frontend
- ARIA (developing for accessibility)

**Helpful resources**:
- [Learn ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
- [Video tutorial](https://www.youtube.com/watch?v=cOmehxAU_4s) on auditing accessibility.
- [A11ycast tutorial playlist](https://www.youtube.com/watch?v=Ag3DMNbL_ig&list=PLNYkxOF6rcICWx0C9LVWWVqvHlYJyqw7g) to learn more about accessibility testing. 

**Suggested milestones**
1. [Small] Add google analytics for usage of translation tab. Currently we record usages of Oppia features through google analytics, the code for which can be found in SiteAnalyticsService.js. Through this milestone, we want to additionally cover the use of translation tab features.
2. [Small] Add keyboard shortcuts for "starting" and "stopping" recording.
3. [Medium] Perform an accessibility audit on the translation tab and make any necessary changes to fix the accessibility issues. Auditing can be done in the following ways:
    - Tabbing through the translation tab.
    - Running an Accessibility Audit test from devtools. 
***