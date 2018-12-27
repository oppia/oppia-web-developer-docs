## Table of Contents
* [Getting started](#getting-started)
* [FAQs](#faqs)
* [GSoC Proposal Template](#gsoc-proposal-template)
  * [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan)
  * [Sample proposals from past years](#sample-proposals-from-past-years)
* [Types of work related to Oppia projects](#types-of-work-related-to-oppia-projects)
* [Selection Criteria](#selection-criteria)
* [Oppia's Project Ideas](#oppias-project-ideas)
* [Other useful information](#other-useful-information)
    * [Dates and Deadlines](#dates-and-deadlines)
    * [List of Mentors](#list-of-mentors)
    * [Communication](#communication)

Oppia is participating in [Google Summer of Code 2018](https://developers.google.com/open-source/gsoc/)! GSoC is a global program which offers post-secondary students an opportunity to discover and work with open source organizations over the course of 3 months, while being paid a stipend. Students work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

You might be interested in our GSoC info pages from previous years: [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

Also, please note that acceptance into GSoC isn't a prerequisite for [becoming an Oppia contributor](https://github.com/oppia/oppia/wiki). The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out!

## Accepted Proposals:

The project's we've accepted (as of 23 Apr 2018) are:
- [@aks681's proposal](pdfs/GSoC2018AkshayAnand.pdf) for implementing skills functionality. Mentor: Sean Lip.
- [@apb7's proposal](pdfs/GSoC2018ApurvBajaj.pdf) for improving the development workflow. Mentor: Kevin Lee.
- [@bansalnitish's proposal](pdfs/GSoC2018NitishBansal.pdf) for upgrading the rich-text editor. Mentor: Allan Zhou.
- [@DubeySandeep's proposal](pdfs/GSoC2018SandeepDubey.pdf) for implementing a lesson translation dashboard. Mentors: Tony Jiang and Anmol Shukla.
- [@ishucr7's proposal](pdfs/GSoC2018AashishGaba.pdf) for improving the image loading pipeline. Mentor: Vojtěch Jelínek.
- [@nithusha21's proposal](pdfs/GSoC2018NitheshHariharan.pdf) for implementing a generalized review system. Mentor: Anmol Shukla.
- [@pranavsid98's proposal](pdfs/GSoC2018PranavSiddharth.pdf) for visualizing learner playthroughs. Mentor: Brian Rodriguez.
- [@vibhor98's proposal](pdfs/GSoC2018VibhorAgarwal.pdf) for implementing two new interactions. Mentor: Prasanna Patil.

# Students
GSoC is an excellent opportunity for students to get paid to work on an open source project. If you're interested in applying as a student, you should definitely read the following resources:

- [Google Summer of Code student guide](http://write.flossmanuals.net/gsocstudentguide/what-is-google-summer-of-code/)
- [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
- [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)

## Getting started

If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. If you like, you can also sign up to the [oppia-gsoc-discuss@](https://groups.google.com/forum/#!forum/oppia-gsoc-discuss) mailing list to participate in general discussion related to Oppia's involvement in GSoC (see point 5 below, too). Make sure to set your preferences correctly so that you actually get the emails!

1. Get a better understanding of what Oppia is all about by taking a look at our [user documentation](http://oppia.github.io/#/) -- this will help you become familiar with important concepts like explorations and interactions. We also recommend having a go at playing/creating lessons on [Oppia.org](https://www.oppia.org), which hosts a live instance of Oppia.

1. Read and follow the instructions in the [contributors' guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) carefully.

1. Consider taking up one or more starter projects in order to become familiar with the contribution process. This will help us get an idea of what it's like to work with you -- e.g. how independent, resourceful, responsive, etc. you are. It will also help you get a better understanding of the codebase, so that you can write a good, detailed project proposal.
    - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to follow the [dev workflow](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#instructions-for-making-a-code-change) carefully, manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide), and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

1. When you've done enough starter projects to get a good understanding for the "lay of the land", select one or more GSoC projects that you're most interested in, and write your project proposal! We strongly encourage you to discuss your project ideas and share your proposal with the community, so that you can get feedback and ensure that what you're writing makes sense to others. The best way to do this is to put your proposal into a collaborative editing tool like Google Docs, allow others to comment on it, and share a link to it on the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com). You can also email the mailing list if you have any questions about a project, or would like to discuss your approach with the Oppia community and get feedback. Please be specific when asking questions, since this makes it easier for us to help you.

## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: Familiarity with AngularJS (v1), Python 2.7 and Google App Engine is useful and recommended for most Oppia work. In addition, UI design skills are useful for frontend, user-facing work. Please see the individual project ideas to determine whether these skills are recommended for the project in question.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other students, successfully contributing patches, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: GSoC is intended to be a full-time commitment, so the main concern is whether you can still get the project done on time. Be upfront about your other commitments and make sure you schedule your time accordingly when creating your proposal. Other commitments you should list include time where you'll be in school and will commit less time to GSoC, time when you'll be travelling and away from GSoC work, any summer jobs you need to commit to, etc. We will try to be flexible around other time commitments, as long as your proposal convinces us that you will have enough time to complete the project by the end of the summer. On the other hand, if you do not disclose other commitments, and it turns out that you are unable to commit to what you wrote on your proposal, this is grounds for failing the program.

**Q: Which projects are most important for Oppia?**

A: All the projects we've listed here are important, and we'd be very happy to see good progress made on any of them! Projects are treated as equally important during selection. Note that the relative importance of a project to Oppia is not part of the selection criteria (see below).

## GSoC Proposal Template

**Important:** Please make sure that your final proposal is self-contained! In particular, to be fair to all applicants, key components of the proposal should not be editable after the deadline, and you shouldn't assume that reviewers will follow external links.

When submitting a proposal, please use the following template:

**Project Details**
- Name of the project.
- Why are you interested in working with Oppia?
- What interests you about this project? Why is it worth doing?
- Prior experience (especially with regards to technical skills that are needed for the project).
- Links to 1-5 PRs you've made that showcase your best work, especially any Oppia ones. The list should include at least one Oppia PR, but you can also include some other PRs from major open-source projects if you like.
- Project plan and implementation strategy.

**Summer Plans**
- Which timezone(s) will you primarily be in during the summer?
- How much time will you be able to commit to this project?
- What jobs, summer classes, and other obligations might you need to work around? Please be upfront about any existing commitments you may have. (See the [FAQs](#faqs).)

**Communication**
- What is your contact information, and preferred method of communication?
- How often, and through which channel(s), do you plan on communicating with your mentor?

### Tips for writing a good project plan

The project plan is the most important section of the proposal, since it outlines what you'll be doing during the summer. Here's some guidance on what the mentors and organization admins will be looking for in this section:

- **Three clear milestones** explaining the deliverables to be achieved by the end of each of the three GSoC coding periods. Strong proposals will have clear, concrete and well-defined milestones, whose success can be readily evaluated by an external observer. It's OK to break up a milestone into smaller milestones over smaller timescales, but individual milestones should represent *concrete* deliverables that can be merged safely into the "develop" branch and included in a subsequent Oppia release. **<u>Please try to be realistic when setting milestones, and don't over-promise.</u>**

- **A technical design and implementation plan**. The project ideas below are annotated with some notes from the mentors, but please bear in mind that these notes are not exclusive and shouldn't serve as a substitute for thinking carefully and critically about the project from first principles -- their main purpose is to suggest ideas or possible starting points. If, in your thinking, you find aspects not mentioned in the notes, feel free to include a discussion of these aspects in your proposal. (For example, certain projects may require a migration of existing production data, and this needs to be accounted for in the project plan.) Strong proposals will demonstrate familiarity with the codebase, a realistic implementation plan, and attention to detail.

- **Mocks or wireframes**, if appropriate. For user-facing projects, we strongly favour proposals that demonstrate an empathy for the user. If you're proposing frontend design mocks, we suggest showing your ideas to your friends and getting their critical feedback, so that you can be confident that others find them intuitive as well. Note that you do not need to make your mocks pixel-perfect, but they should illustrate the primary user journeys clearly enough for us to understand exactly what you're proposing. Also, bear in mind that "more is not necessarily better" -- an important aspect of user-focused design is deciding what _not_ to do.

### Sample proposals from past years

If you'd like to get a sense of what a proposal might contain, here are some examples of student proposals that we accepted in 2017:
- [Prasanna's proposal](https://github.com/oppia/oppia/wiki/pdfs/GSoC2017PrasannaPatil.pdf) for applying ML to the code interaction
- [Arunabh's proposal](https://github.com/oppia/oppia/wiki/pdfs/GSoC2017ArunabhGhosh.pdf) for a new learner dashboard
- [Yogesh's proposal](https://github.com/oppia/oppia/wiki/pdfs/GSoC2017YogeshSharma.pdf) for a sitewide ACL refactor

## Types of work related to Oppia projects
In order to ensure a well-rounded engineering experience, developers will do some or all of the following depending on their project:
- Meet with their mentors regularly
- Meet with other contributors related to their project area
- Receive code reviews for all code they write for their project
- Write automated tests for their projects
- Create UI mocks (if doing frontend development)
- Write design documents (if implementing large features or introducing new systems)

## Selection Criteria

In order to select students for GSoC, we will mainly be looking at three things:

- The quality of the submitted proposal
- The quality of the applicant's previously-submitted PRs (in order to assess their ability to code, debug, break down complex tasks, etc.). Note that quantity isn't a prerequisite in itself, though contributors who've submitted multiple PRs are likely to have had more opportunities to demonstrate the abilities needed to succeed in GSoC.
- Our prior experience working with the student (e.g. do they keep commitments, communicate well, demonstrate independence/initiative/responsiveness, help others, etc.)

We believe that strong performance in these dimensions is likely to correlate well with the student having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the GSoC program.

For the proposal, we generally look for a clear indication that the student has a good, deep understanding of the project, and has broken it down sufficiently well, in a way that makes it very likely to succeed. Some indicators that could help with this include:
- A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating a simple, intuitive experience for end users.
- A concrete, specific breakdown of the work to be done for each milestone. Here's an [example](https://docs.google.com/document/d/1vuwXvHOYXqfM2S2B2KIWhZrAa1PL59wJRUYsqJEd67E/edit) from a previous design doc. (Note that, in this example, the author has carefully considered and listed which tests need to be written alongside the code; this is a positive indicator.)
- Sufficient concreteness (e.g. references to particular files and methods) to demonstrate that the applicant is familiar with both the scope of the problem and the existing codebase.
- A description, if applicable, of how the applicant plans to mitigate risks that could potentially derail the project.
- Clear, unambiguous communication. (This is important; your proposal will be read by many mentors!)

# Oppia's Project Ideas

The following is a list of Oppia's 2018 GSoC project ideas. You are welcome to choose among these ideas, or propose your own! However, if you are proposing something original, it's essential to engage with the Oppia community in order to get feedback and guidance to improve the proposal, as well as to make sure that it fits in with the team's overall plans.

Please note that all mentor assignments are provisional, and that they may change depending on which proposals are eventually accepted.

This year, the Oppia team is offering three types of projects: infrastructure projects, projects that improve the learner experience, and projects that improve the creator experience. Some of the project ideas are annotated with notes and suggestions from the mentors, but please bear in mind that the main purpose of these notes is simply to suggest ideas or possible starting points; they aren't meant to be prescriptive. You'd also be welcome to include discussions of other relevant aspects (that aren't mentioned in the notes) to your proposal. For more information, see: [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan).

- [Infrastructure Projects](#infrastructure-projects)
  - [Static serving](#static-serving)
  - [Improving the development workflow](#improving-the-development-workflow)
  - [Rich-text-editor upgrade](#rich-text-editor-upgrade)
  - [Adding a training interface for machine learning](#adding-a-training-interface-for-machine-learning)
  - [Cleaning up the backend tests](#cleaning-up-the-backend-tests)
  - [Improve the image loading pipeline](#improve-the-image-loading-pipeline)
- [Learner View Projects](#learner-view-projects)
  - [New interactions](#new-interactions)
  - [Add functionality for skills](#add-functionality-for-skills)
  - [Audio bar improvements](#audio-bar-improvements)
  - [Questions frontend](#questions-frontend)
- ["Creator Experience" Projects](#creator-experience-projects)
  - [Lesson translation dashboard](#lesson-translation-dashboard)
  - [Crowdsourced audio translations](#crowdsourced-audio-translations)
  - [General crowdsourcing and review system](#general-crowdsourcing-and-review-system)
  - [Visualizing learner playthroughs](#visualizing-learner-playthroughs)
  - [Answer statistics visualizations](#answer-statistics-visualizations)



## Infrastructure Projects

### Static serving

**Aim:** Currently, Oppia serves all pages using the Jinja templating engine, which isn't very efficient -- for one thing, because pages are dynamically composed using Jinja, they can’t be cached. The aim of this project is therefore to serve as much of Oppia's pages as we can statically, and handle all dynamic content using AJAX calls. In order to do this, we'll need to get rid of the Jinja footprint in our codebase. Furthermore, we sometimes use Jinja to include static files (like header_js_libs.html or footer.html); and will therefore need to find an alternative way to include these in a Jinja-less environment (perhaps in our build process, or with ngInclude).

**Skills/knowledge required:**
* Full-stack development
* Technical design
* Python

**Difficulty:** Medium

**Potential mentor(s):** @vojtechjelinek (primary), @brianrodri, @kevinlee12

**Suggested milestones:**
1. Devise a way to serve the About page statically (this requires getting rid of Jinja on that page), using an approach that is generalizable to other pages. Identify other issues that can arise from serving the remaining pages statically.
1. Convert all mostly-static pages in Oppia, as well as at least one non-static page, to use the new framework developed in milestone 1.
1. Serve all pages in Oppia statically.

**Related issues (you might like to tackle a few of these, in order to get a feel for the domain):**
* [#2641](https://github.com/oppia/oppia/issues/2641): There should be tests which verify that all HTML/JS components which need to be served together are indeed bundled together in every page they appear in.
* [#4220](https://github.com/oppia/oppia/issues/4220): MusicNotesInput static images are not hash interpolated.
* [#2308](https://github.com/oppia/oppia/issues/2308): Add pre-rendering and other pre improvements to Oppia pages.

**Notes:**
* The proposal should include a clear analysis of how to get rid of Jinja for all pages.
* This project may require some changes in the build process, because we currently sometimes use `{% include %}` just to have clearer dev processes. Good proposals will include a coherent analysis of how to deal with this issue, as well as the pros/cons of possible approaches. Some starting-point ideas are provided below, but there may be others:
    *  re-build the finalized templates at release time, then serve them statically from then on (rather than try to re-construct them at every request). But how would we handle local development, where the changed files must be available immediately?
    * Look into stuff like ngInclude in Angular. But that might lead to too many calls to the server (even if only to retrieve static files). That said, we could cache the templates.
* The main goal of this project is to improve the bandwidth and latency of Oppia as much as possible, so other changes that would improve these metrics are highly appreciated. However, such changes should not supersede the 'static serving' part of the project.

### Improving the development workflow

**Aim:** The aim of this project is to improve the development workflow for Oppia developers and code reviewers. For example, a fair amount of reviewer time is currently spent handling common situations that should be automatable via presubmit checks (such as linting and CLA checking). Also, in order to catch errors before they end up in production, we need a thorough suite of non-flaky end-to-end tests in order to ensure that changes don’t cause regressions, and these tests should incorporate mobile views and multiple browsers. Other improvements might also be possible.

**Skills/knowledge required:**
* Bash and python scripting
* Process automation
* End-to-end testing
* Familiarity with GitHub APIs
* Good debugging ability
* Attention to detail

**Difficulty:** Medium

**Potential mentors:** @kevinlee12 (primary), @seanlip

**Suggested milestones:**
1. Implement automatic lint checks that catch all common errors before a PR is pushed to GitHub. These checks should run automatically for all contributors before submit (and if this isn’t the case, this should be fixed, or a GitHub linter bot created so that reviewers can assume that PRs are linted prior to review). In particular, fix and close all bugs related to linting and presubmit checks, such as #4119 and #3905, and provide documentation on how to write lint checks for newly-discovered common issues.
1. Organize and tidy up the e2e tests, and define policies for what to test. Extend the existing e2e framework to support an additional browser (Firefox), as well as mobile viewports. Fix any flakiness issues that arise, such as those in #4044. Draw up a plan for manual release testing that covers the gaps left by e2e tests. Provide documentation on how to update these plans and e2e tests if a new page gets added to the Oppia application.
1. Create GitHub bots to automate common tasks, and provide documentation on how to write new GitHub bots for other automatable tasks that arise, going forward. Such tasks may include:
    1. checking CLAs (currently maintained in a Google Form) and directing new contributors to the "Getting Started" instructions if the CLA is not signed
    1. emailing PR authors when their PR has a merge conflict (e.g. when the develop branch is updated) or their Travis tests fail, and providing guidance on how to address it; emailing the maintainer-on-duty if any Travis tests fail in develop
    1. warning PR authors if PRs look abandoned, and then auto-closing those PRs after a few more days
    1. (stretch) auto-updating translations from translatewiki once a month

**Related issues (you might like to tackle a few of these, in order to get a feel for the domain):**
* [#4122](https://github.com/oppia/oppia/issues/4122): refactor the startup scripts so that Karma tests run with minimal downloads.
* [#4119](https://github.com/oppia/oppia/issues/4119): ensure that the linter script diffs correctly.
* [#3905](https://github.com/oppia/oppia/issues/3905): add lint checks for common coding issues arising in code reviews.
* [#1977](https://github.com/oppia/oppia/issues/1977): lint CSS files
* [#1736](https://github.com/oppia/oppia/issues/1736): make Protractor tests also run on Firefox in Travis.

**Notes:**
* The overall goal of this project is to automate as much of the development workflow as possible. There should be a noticeable improvement in the dev experience when this project is completed (e.g. in terms of review turnaround times and developers getting quick feedback on their PRs).
* A primary emphasis of this project is on developing repeatable processes that can run reliably, long after the GSoC project is over. Strong proposals will provide a coherent analysis and breakdown of each part of the project, and propose procedures for triaging and handling new instances of each type of task going forward. Most of the coding period will involve implementing these procedures.
* Some lint checks are harder to implement than others. Proposals should enumerate different ways to handle lint checks, and systematically explain how to implement fixes for the known issues. A starter list is provided in #3905, but it is not exhaustive, and strong proposals would extend this list with other issues that commonly arise in code reviews.
* In addition to the deliverables laid out above, proposers may optionally suggest and implement further improvements to the development workflow and review process. However, in general, such improvements should not supersede the core ones laid out above.
* It might be a good idea to tackle one or two of the sub-issues in [#3905](https://github.com/oppia/oppia/issues/3905) to become familiar with how the linting process works. This might also help you write a more concrete proposal.

### Rich-text-editor upgrade
**Aim:** The aim of this project is to upgrade Oppia’s Rich Text Editor (RTE), which authors use to create lesson content. Our current RTE, based on [textAngular](http://textangular.com/), cannot render previews of certain rich-text components during editing. For [example](https://github.com/oppia/oppia/issues/1933), if the creator adds a hyperlink, we want to display that link in the editor -- but the current editor can only show a generic link icon placeholder. The same issue exists with math equations, images, and the other rich text components. We want to upgrade our RTE to use [CKEditor](https://ckeditor.com/ckeditor-4/), which would allow us to actually render rich text components during editing, instead of having placeholders. This will result in an improvement to the lesson creation experience.

**Skills/Knowledge Required**:
* JavaScript
* HTML/CSS
* Python (backend)
* Familiarity with Document Object Model (DOM) parsing and manipulation

**Difficulty:** Medium

**Potential Mentors:** @AllanYangZhou (primary), @prasanna08

**Suggested Milestones:**
1. **Content Migration**: Write and execute a one-off job that migrates existing RTE content (i.e., the content currently in our existing explorations which was created through textAngular) into a format compatible with CKEditor. We should have a function that checks whether the given content is acceptable for CKEditor, to be sure that our migration works properly.
1. **CKEditor Integration**: Replace textAngular with CKEditor in our RTE. A lot of this work has already been covered in [#1715](https://github.com/oppia/oppia/pull/1715), but that work is likely outdated due to changes in both Oppia and CKEditor, and needs to be updated. All the frontend functionality described in [#3032](https://github.com/oppia/oppia/pull/3032) should be implemented.
1. **Polish**: Address any new minor bugs introduced by the CKEditor integration. Modify the [RTE documentation](https://github.com/oppia/oppia/wiki/Rich-Text-Editor-%28RTE%29-Overview) to include all changes due to the upgrade.

**Related Issues:**
* [#3576](https://github.com/oppia/oppia/pull/3576): RTE content validation
* [#2083](https://github.com/oppia/oppia/pull/2083): Math equation expression conflict

**Notes:**
* Milestone 1 (Content Migration) is likely to be more challenging and time-consuming than the other 2 milestones. Proposals should have a particular emphasis on addressing the content migration.
* Integrating a new RTE is likely to introduce many new minor bugs. It is fine to leave these to milestone 3 (post-migration) as long as the new RTE is still usable.
* The existing [RTE documentation](https://github.com/oppia/oppia/wiki/Rich-Text-Editor-%28RTE%29-Overview) may be useful.

### Adding a training interface for machine learning

**Aim:** One of the things that makes Oppia useful is that it can give learners targeted feedback at scale. This is done using explicit, creator-defined rules that allow Oppia to choose a response to a learner's answer. However, creating a large number of such rules is time-consuming and not scalable, especially for questions that are more complex. This is a problem that could be tackled using machine learning.

In GSoC 2017, we developed core infrastructure to support machine learning on Oppia and built a pipeline for training classification models for text and code answers. This year, we'd like to build upon this work to fully launch ML in production. In particular, we would like to make it easier for the creators to label "unresolved" answers (i.e. answers for which no feedback was predicted by a classifier) with a piece of feedback. We will need a way to store an answer together with the number of times it appears, so that we can prioritize resolution of answers by their frequencies, and also so that we can provide information to creators in the Statistics tab; this motivates the definition of an AnswerWithFrequencyModel. In addition, we will also need to design and implement a training interface which supports the AnswerWithFrequencyModel, as well as additional features like (i) viewing the answers in an answer group, (ii) adding/deleting an answer from an answer group, and (iii) moving an answer to the "default" answer group.

**Skills/knowledge required:**
* AngularJS
* Python
* Database concepts (Google App Engine and working with NoSQL databases)
* Machine Learning (not necessary, but strongly recommended)

**Difficulty:** Hard

**Potential mentors:** @prasanna08 (primary), @anmolshkl, @AllanYangZhou

**Suggested milestones:**
1. Implement the answer frequency backend model and required functions. (See the notes for more detail about the design requirements for this model.)
1. Implement a MapReduce job that populates AnswerWithFrequencyModel instances with all the existing answers in the exploration. Implement all the necessary controllers and backend functions that the training interface depends on.
1. Implement the front-end part of the training interface. By the end of GSoC, the training interface should be fully functional and ready for use in production.

**Related issues:**
* [#3836](https://github.com/oppia/oppia/issues/3836): Upgrade training interface in creator view to show unresolved answers

**Notes**:
* For Milestone 1, some of the design requirements for AnswerWithFrequencyModel can be found in [this doc](https://docs.google.com/document/d/19v-zTFS7_8nysUAggDau3xCDN_WS4x20heJJjpZdALs/edit), but the doc is not completely finished yet. It will be finished by 25th February and posted here so that proposers can reference it in their proposal. The proposal should build upon this document, and address all the open questions.
* Milestone 2 involves the implementation of an MapReduce job for AnswerWithFrequencyModel. You may find the [Creating MapReduce](https://github.com/oppia/oppia/wiki/Calculating-statistics#8-create-mapreduce-jobs) jobs section on the wiki useful for getting more familiar with Oppia's MapReduce infrastructure.
* Students can EITHER use the existing training interface and improve/re-design it, OR propose a new training interface. We strongly suggest finding an approach that maximizes code reuse without sacrificing functionality.
* For Milestone 3, the proposal should describe a suitable frontend user interface that allows creators to easily assign feedback classes to the surfaced unresolved answers. For this purpose, you may want to look at how the current training interface works, and what changes you'd like to make to it in order to meet the given requirements. The design details for the new training interface can be found in [this doc](https://docs.google.com/document/d/1IIYt6QiC0-wzM6AbDwXrQPY33U_rRBZDWyaAOKMxvao/edit), which is partially finished. We will complete the backend design (in terms of the behaviours of necessary functions and controllers) and post it here by 25th February, but the frontend UI design is left to the proposer. You might want to prepare some simple mocks that give a rough idea of the proposed UI and the workflow for the creator.
* As a stretch goal, you are welcome to add/suggest additional features for the training interface. However, if you do, please also explain how it will help creators, explain the implementation details, and indicate in which milestone you will deliver this feature.

### Cleaning up the backend tests

**Aim:** The Oppia backend is currently quite solid, but we would like to strengthen it further by ensuring that it is fully tested. The aim of this project is to clean up the backend tests and implement missing ones, as well as to lay down guidelines/rules for future backend developers to ensure that the backend code continues to be well-covered by tests. Particular emphasis is placed on introducing a framework that encapsulates common "user actions" and makes it easy to write backend _integration_ tests simulating user flows against various server endpoints, such as [this one](https://github.com/oppia/oppia/blob/6d9650886f580dbca538981521c10d0be3a28849/core/controllers/editor_test.py#L930).

**Skills/knowledge required:**
* Python
* Experience writing tests
* A "testing" mentality of trying to find creative ways to break the code

**Difficulty:** Medium

**Potential mentors:** @kevinlee12 (primary), @seanlip

**Suggested milestones:**
1. Implement a framework that makes it easy to write backend integration tests. Illustrate it by writing a few integration tests for common scenarios that occur in practice (e.g. creating an exploration and then playing it).
1. Implement a full suite of backend integration tests that covers all major (and some minor) use cases. Enable coverage checking and improve the coverage of the backend unit tests to 85%.
1. Improve the coverage of the backend unit tests to 100%.

**Notes**:
* Proposals should explain their approach for creating a framework that makes the creation of backend integration tests easier. One possible approach is to encapsulate common actions in helper functions, all stored in a test_actions.py file, and use these to simulate common behaviours (e.g. `test_actions.login(user_id)`). The proposal should describe the API for the framework.
* Proposals should explain how they would enable coverage checking, and which tests they will focus on writing in milestone 2 vs milestone 3.
* A strong proposal will describe, in some detail, a list of backend integration tests to write (that corresponds to core user journeys). Finding a way to organize this effectively is important; we don't want to end up with many tests with mostly-overlapping functionality.

### Improve the image loading pipeline

**Aim:** Currently, images in lessons take a while to load. This results in students (especially those with poor connectivity) seeing no images for an extended period, which causes them to misinterpret questions and select incorrect answers, leading to frustration. We currently have a system for loading audio that preloads and caches audio files, and we want to extend this system to accommodate images as well.

**Skills/knowledge required:**
* Full-stack programming in Python and AngularJS
* A good sense for technical design
* Attention to detail
* Experience with refactoring/migrations (not necessary, but strongly recommended)

**Difficulty:** Medium

**Potential mentors:** @vojtechjelinek (primary), @seanlip

**Suggested milestones:**
1. Extend the audio asset caching and preloading functionality in the frontend to handle images as well. Ensure that a loading placeholder is shown while an image is in the process of loading (currently, there is no such indication, which results in a poor user experience as learners would be reading a card with important information missing).
1. Write code to analyze and extract image details from the rich-text content of an exploration, such that the full list of images contained in a given exploration can be retrieved. Implement code for a one-off migration of existing image data from the App Engine datastore to Google Cloud Storage, so that the image files sit alongside the audio files.
1. Perform the migration. Ensure that image files get saved to Google Cloud Storage going forward, and deprecate the old system.

**Notes**:
* The trickiest part of this project is finding a way to do the refactoring/migration _safely_. Potential pitfalls include having new files get written to both systems at once, new files not get written to any system at all, incomplete transfer of files from the old system to the new system, references to image URLs in the new system while files are still in the old system, stale references to the old system, etc. Your proposal should provide a set of migration instructions and a timeline for PRs/releases that ensures that a release can always be cut from the develop branch without causing anything to break. (Note that Oppia releases generally happen once a month, around the 15th or so.)
* Be careful to also account for images in all previous versions of an exploration; we should migrate those images too. This is necessary because explorations can be reverted to older ones.
* The proposal should explain how to validate that the migration has taken place correctly before doing anything destructive (such as deleting the images from the old system).
* As a stretch goal, it would be nice to try and compress images automatically when large images are uploaded to the server.

## Learner View Projects

### New interactions

**Aim:** The aim of this project is to implement new interactions in Oppia. (An "interaction" is the name for the form which a learner uses to submit an answer.) In particular, two new interactions should be implemented: a "Number with units" interaction, and a "Sorting" interaction. The number-with-units interaction is an extended version of the NumericInput interaction which will allow creators to check an answer that is submitted as a number with associated units (such as 2.56 metres or $2.15), and that understands relationships between units (e.g. 2.56 m = 256 cm). The "sorting" interaction allows students to sort or rank items relative to each other. For example, a student might be asked to arrange fractions in ascending/descending order; they should be able to drag the items around and sort/rank them. It should also be possible for the creator to allow multiple items to occupy the same position/rank in the list, e.g. when sorting 1/2, 1/4, 2/4, 3/4 it should be possible to put 1/2 and 2/4 in the same position.

**Skills/knowledge required:**
* Full-stack development using AngularJS and Python
* Attention to detail

**Difficulty:** Medium

**Potential mentors:** @prasanna08 (primary), @AllanYangZhou, @tjiang11, @kevinlee12

**Suggested milestones:**
1. Implement a preliminary version of the "number with units" interaction. The interaction should have support for SI units (supported by the math.js library) as well as support for conversion between units (e.g. detecting that two answers are equivalent using rules like K = 273.15 + ℃). At the end of this milestone, the "number with units" interaction should support rules for "answer is equivalent to" and "answer exactly matches".
1. Implement a preliminary version of the "sorting" interaction which works when all elements have distinct positions. In addition, at the end of this milestone, the "sorting" interaction should support the following rules: "is equal to this ordering", "is equal to this ordering with at most one element in the wrong place", "has element X at position Y in the list" and "has element X coming before element Y".
1. Release a v2 of both interactions. The v2 for the "number with units" interaction should include support for custom (non-SI) units such as currencies, e.g. $1 = 100 cents or ₹1 = 100 paisa, and the v2 for the "sorting" interaction should add support for having multiple elements in the same position.

**Related issues:**
* [#556](https://github.com/oppia/oppia/issues/556): Create a NumberWithUnits interaction.
* [#3793](https://github.com/oppia/oppia/issues/3793): Add a new drag-and-drop sorting interaction

**Notes:**
* Some familiarity with interactions and the Oppia answer classification workflow would be useful for this project. The following wiki pages will be helpful for getting started with Oppia's interactions system: [Overview of Extensions](https://github.com/oppia/oppia/wiki/Extensions-Overview), [Creating Interactions](https://github.com/oppia/oppia/wiki/Creating-Interactions), and [Creating Rules](https://github.com/oppia/oppia/wiki/Creating-Rules).
* Both interactions should be usable by creators and learners without any difficulties. To this end, students are encouraged to include their design and implementation plans in their proposal. A good way to communicate the design aspects would be to fully describe the main user journeys for both the creator and the learner.
* Currently, we have an [initial design doc](https://docs.google.com/document/d/1nL0jK-fkxPjNT4-PCGkSYbjwcqCM8R1MM26KGgxVIA0/) prepared for the "number with units" interaction, which might help with understanding the requirements for this interaction. (Note that no prior work has been done on the sorting interaction.) That said, this initial draft is only meant as a starting point, and students are welcome to propose better and more intuitive approaches if any are discovered.

### Add functionality for skills

**Aim:** For the Oppia randomized control trial in Delhi, India, we are piloting some experimental functionality for redirecting to a short refresher lesson if the learner has clearly failed to master a prerequisite. The current functionality for doing this is clunky, and involves going to a separate exploration and back again. Instead, we would like to introduce a new construct called "skills". Skills are global in Oppia. Each skill has a human-readable name and is associated with a "concept card" explaining the skill and providing some examples. When a gap in prerequisite knowledge is detected, the lesson should go into "flashback/revision mode", and show the concept card to the learner. The learner would then need to correctly complete a streak of 3-4 questions on that skill before continuing from where they left off in the main lesson. This would help to ensure that a learner has mastered a prerequisite skill and has a solid foundation before going on to new material.

**Skills/knowledge required:**
* AngularJS
* UI/UX design

**Difficulty:** Medium/Hard

**Potential mentors:** @seanlip (primary), @prasanna08

**Suggested milestones:**
1. Implement the backend models, domain objects and controllers related to skills. Migrate skills and questions out of collections, and into the global namespace.
2. Implement a basic editor interface for skills.
3. Implement the desired learner experience using the new Skill object.

**Notes:**
* For reference, here is an example of an existing ["prerequisite lesson"](https://www.oppia.org/explore/xHwiGtvK2N4L) that follows the structure described above.
* The proposal should describe the data schema for a Skill.
* Collections already have skills and questions, but we should move these out into the global namespace. The proposal should explain how to do this safely.
* Skills should live in the global namespace. (I.e., on an instance of Oppia, there should only be a single "skill practice" construct for "Adding fractions with the same denominator".) We intend for this to be community-editable (like a wiki) over the long term.
* The questions should be taken from a question bank, and be selected from questions that are tagged with the given skill name. (We already have a Question construct in the Oppia backend that can be used for this.)
* As a stretch, the proposal might also consider whether any changes need to be made to the way we handle exploration analytics.

### Audio bar improvements

**Aim:** Audio functionality is very important for learners whose primary language is not English. In recent trials we have conducted, the presence of audio subtitles in a student's native language has led to substantial improvements in students' understanding of lesson content. This project aims to improve the audio functionality so that it is more intuitive and useful.

**Skills/knowledge required:**
* AngularJS

**Difficulty:** Medium

**Potential mentors:** @anmolshkl (primary), @tjiang11

**Suggested milestones:**
1. Improve the automatic English audio subtitles, and fix them if they don't say the correct thing (for example, when reading LaTeX). The issues here can be discovered by manual testing, and the proposal should enumerate a specific list of desired fixes.
1. Add support for creators to store written versions of the audio translations, so that if the exploration content changes it is easy for the creators to update these written versions and re-record the audio. (At some point in the future we might also surface these to the student.)
1. Allow students to flag audio translations that they can't understand.

### Questions frontend

**Aim:** In order to practice skills, students need a way to be given randomly-selected questions from a question bank. The backend for questions has already been built, but the frontend has not been started yet. The aim of this project is to implement the frontend interfaces for question editing and question practice. Questions are currently used in three places: at the beginning of a lesson (as recaps), at the end of a lesson (as post-tests / final challenges), and as standalone practice.

**Skills/knowledge required:**
* AngularJS (and a bit of Python)
* UI/UX design

**Difficulty:** Medium/Hard

**Potential mentors:** @tjiang11 (primary), @seanlip

**Suggested milestones:**
1. Implement a basic editor UI for adding, viewing and editing new questions associated with a specific skill.
1. Implement a standalone frontend for repetitive practice of questions that pertain to a particular skill (or set of skills).
1. Find a clean way to incorporate functionality for randomized questions into the beginning and end of an exploration (which the creator can optionally enable), so that instead of hard-coding the recap/final questions, a creator can just specify the skills for which questions should be asked.

**Notes:**
* Much, but not all, of the Questions backend has already been built. So, the bulk of the work for this project will take place in the frontend (though there may be a few small Python seams that need to be implemented).
* The proposal should describe how a learner would access the standalone questions frontend (e.g. do they do so via their learner dashboard, or from the relevant collection page, or either?) as well as the desired UX for the standalone questions frontend.

## "Creator Experience" Projects

### Lesson translation dashboard

**Aim:** Many students in Oppia's target demographic do not speak English as a primary language, and rely on audio subtitles in order to help them understand the content of a lesson (whilst still relating it to the English text in front of them). Recording audio subtitles for lessons is therefore a vital part of the creation process, but the process for doing so is currently quite manual and involves manually creating and uploading a lot of local files. The aim of this project is to build a mobile-friendly translation dashboard that makes this part of the process easier to manage.

**Skills/Knowledge required:**
* UX/UI design
* Technical design
* Full-stack development (AngularJS, Python)

**Difficulty:** Medium/Hard

**Potential Mentors:** @tjiang11 (primary), @anmolshkl

**Suggested milestones:**
1. In the backend, remove the need for the conversion step so that the creator just needs to record and upload (rather than the current flow of record, convert to MP3 at 128kpbs, then upload). Implement all backend functionality needed (domain, controllers) for the translation dashboard. Update the backend rights management to allow for a new role that allows direct edit access to the translation dashboard but not the rest of the exploration.
1. Implement the frontend for each translation dashboard. This dashboard should list all the different pieces of text that need translation, and allow the creator to record translations directly via the browser/device they're using. The dashboard should be mobile-friendly and should include indicators that show where translations are missing/flagged, as well as a progress bar to indicate the completeness of the lesson's translations.
1. Make it possible to bulk-upload translations, so that contributors working with a desktop can record all their translations, put them in a folder, and upload the folder. (Some creators prefer this workflow.)

**Notes:**
* The proposal should explain the user flow for how somebody would contribute an audio translation(s). Note that, if multiple audio translations are contributed, there would need to be a way to associate each audio translation with the specific hint, feedback, content, etc. it corresponds to.
* A stretch goal would be to hash translations by the translated text, so that they can be automatically reused. (This is because some feedback text, like "No, that's not correct", is often repeated.) However, this isn't a requirement for successful completion of the project.

### Crowdsourced audio translations

**Aim:** On Oppia, learners can listen to audio translations while playing through an exploration. Often, however, a lesson creator does not have the means to create certain audio translations on their own. The goal of this project is to provide a way for _anyone_ to contribute audio translations to an exploration. This project is different from the "lesson translation dashboard" project, in that the focus here is on making the translation process more globally accessible so that many people can contribute incrementally to it.

**Skills/Knowledge required:**
* UX design
* UI design
* Technical design
* Full-stack development

**Difficulty:** Hard

**Potential Mentors:** @anmolshkl (primary), @tjiang11

**Suggested Milestones:**

1. Implement back-end logic and front-end changes needed to allow creators to flag a language, or a set of audio translations, as needing contribution. This should be visible to the community in some form.
1. Implement any necessary backend logic changes, and perform any necessary migrations to allow for anyone to contribute audio translations and for creators to incorporate them into the exploration.
1. Implement the front-end for the "global dashboard" for contribution of audio translations.

**Related Issues:**
* Issues related to audio (there will probably be quite a few in the near-future; see the ["Learner Experience" project](https://github.com/oppia/oppia/projects/18)).
* Any issues related to the generalized review system, suggestions, or feedback threads, e.g.
    * [#3666](https://github.com/oppia/oppia/issues/3666)
    * [#4072](https://github.com/oppia/oppia/issues/4072)
    * [#3982](https://github.com/oppia/oppia/issues/3982)

**Notes:**
* The people who might contribute audio translations to an exploration are not necessarily the learners of that exploration.
* For consistency, it might be nice to encourage the same individual to do the audio translations for an entire lesson. However, this isn't a requirement; it is OK for different cards in the same exploration to be translated by different people.
* Consider breaking down the translation process into two steps: "create written translations", and "record those translations". That may make it simpler for contributors.
* A good proposal would address the following questions:
  * How is the need for audio translations presented to the community? Can the creator specify languages that need translating to? Can learners request a language?
  * How are contributed audio translations presented to the creator? Should the creator be able to preview the exploration while it plays the contributed audio translation(s)?
  * How will contributed audio translations ultimately be included into the exploration? Is there a review process? If so, how will it work? Also, can contributed audio translations replace existing audio translations in the same language?
  * Can creators get in contact with people who have contributed audio translations? How? Right now, creators and learners can communicate via feedback threads.
* This project has ties to the "Lesson translation dashboard" and "General crowdsourcing and review system" projects. It might be worth collaborating with the owners of these projects if either of them is also worked on during the summer.

### General crowdsourcing and review system

**Aim:** For Oppia to become a fully community-driven, crowdsourced platform, anyone should be able to contribute to key explorations and perform certain actions. These actions may include suggesting an edit, adding a question, training an answer, adding new written/audio translations for a lesson, supplying a demonstrative image for a lesson, etc. The creator(s) should be able to manage (accept/reject) these suggestions through a generalized review system. The suggestion-and-review system should be generic enough so that it can be extended to different types of tasks.

**Skills/Knowledge required:**
* UX design
* UI design
* Technical design
* Full-stack development (AngularJs, Python)

**Difficulty:** Hard

**Potential Mentors:** @AllanYangZhou (primary), @anmolshkl

**Milestones:**
1. Generalize and migrate the existing suggestions framework to a general review system (which can be used in the future for adding a question, training an answer, etc.).
1. Set up a system for defining and onboarding trusted reviewers/contributors.
1. Demonstrate the framework’s generalizability by extending it to a second type of task.

**Notes:**
* In general, we have a Task that we want anyone to be able to handle. We can assume that the task takes a small amount of time, and is therefore non-reservable (if someone wants to do it, they can do it there and then). Some tasks are optional/infinite (suggest an edit, add a question), and others have a fixed bucket (provide feedback for an answer, add a new written/audio translation, supply a demonstrative image for a lesson).
* When someone completes a task, it shouldn't immediately be incorporated into the lesson. The work product is reviewed by someone (usually an exploration’s owner/editor or a trusted reviewer). There should be a standard system for marking people as trusted reviewers for a given exploration or type of task (and maybe extending that to all explorations past a certain point).
* The submitted proposal should explain the structure of how such a system would work, and provide a concrete example of its application to one use case.

### Visualizing learner playthroughs

**Aim**: We want to give creators a tool for visualizing how users play through explorations. In particular, it would be nice to let creators see playthroughs which lead to early quits, or where many incorrect answers are attempted. Through this tool we hope to provide an effective way for creators to identify problematic areas in their lesson and address them appropriately.

**Skills/knowledge required**:
* Full-stack development: Python, Javascript, HTML, CSS.
* Debugging and testing.
* Read, write, and follow through with Design Documents.

**Difficulty**: Medium/Hard

**Potential mentors**: @brianrodri (primary), @kevinlee12

**Suggested milestones**:
1. Backend code has the functionality to store and fetch learner playthroughs.
    *The backend for storing and fetching playthroughs (controllers, domain layer, storage layer) should be fully implemented. There should be backend handlers that store and fetch playthroughs as simple value objects, and backend integration tests that ensure that these handlers function correctly.
1. Playthroughs are programmatically stored when deemed useful by the Exploration Player UI, and the most recent one can be viewed in the Exploration Editor UI.
    * There are two types of "useful" playthroughs: playthroughs where a learner gives <admin-defined number> wrong answers in a row, or playthroughs where the learner quits after <admin-defined duration>. Of these playthroughs, there is an <admin-defined %> probability that they actually get stored. All other playthroughs are not recorded.
    * The frontend stores the playthrough data using backend handler URL calls.
    * The Exploration Editor UI displays the raw data of the most recently recorded playthrough.
    * The above functionality should be covered by Karma tests and end-to-end Protractor tests, as appropriate.
1. The Exploration Editor UI displays all playthrough data to creators.
    * A creator can view the details of each recorded playthrough.
    * A creator can mark playthroughs as "resolved", and filter them.
    * The above functionality should be covered by Karma tests and end-to-end Protractor tests, as appropriate.

**Notes**:
* Regarding (1):
    * You must decide which __data__ from a learner's playthrough gets recorded. Keep in mind that we're prioritizing creator-utility here, so nothing too crazy is required. For example: "the path of a learner's mouse" is overkill but "the items a learner selects" is essential!
    * Also decide which __metadata__ from a learner’s playthrough gets recorded. For example, we should be able to answer questions like: "has the creator already viewed or addressed the issues from this playthrough?" and "which version of the lesson was this playthrough recorded in?"
    * It must be impossible for anyone to identify a learner through their playthroughs. This means minimizing the data we take, and anonymizing it as much as possible. This **must** be addressed in your proposal.
* Regarding (2):
    * The admin defined values are stored in a config file (in the feconf file, for example).
* Regarding (3):
    * It's more important for all the information to be displayed than it is for it to look amazing. For example, don't plan to write a "ghost player" that performs each step in a playthrough; a simple text-list describing each action is already incredibly useful and far simpler to implement.

### Answer statistics visualizations

**Aim**: An important part of the Oppia lesson development workflow is improving a lesson after it has been created. Aggregate statistics about student answers are very useful for this. However, at the moment, this functionality only works well for text input, number input, and item selection input. The aim of this project is to make the necessary UI and infrastructural fixes that enable the visualization of statistics for several other commonly-used interaction types, in a way that makes intuitive sense to the creator.

**Skills/knowledge required**:
* Full-stack development: Python, AngularJS, HTML/CSS.
* Debugging and testing.
* UI/UX.

**Difficulty**: Medium

**Potential mentors**: @brianrodri (primary), @kevinlee12, @AllanYangZhou

**Suggested milestones**:
1. Fractions answer visualizations should be shown as fractions. They are currently shown as JSON dicts, which are ugly and hard for a reader to parse. Note that this is likely to require some infrastructural changes; the proposal should describe specifically what changes are needed.
1. ImageClickInput and InteractiveMap visualizations should be clustered. Currently, the coordinates of the clicks are shown, but this is not useful in aggregate.
1. Multiple choice answer visualizations should refer to summaries of the answer labels, rather than the indices of the choices. The proposal should include a clear explanation of the proposed UI/UX, particularly with regards to how long labels and labels containing rich-text components will be handled.


# Other useful information

## Dates and Deadlines
Noteworthy dates for 2018:

* **Jan 04 - Jan 23**: Mentoring organizations apply
* **Feb 12**: Mentoring organizations are announced
* **Mar 12 - Mar 27**: Student application period
* **Apr 23**: Accepted students are announced
* **Apr 23 - May 14**: Community bonding period
* **May 14 - Aug 06**: Students enjoy the summer by contributing code to their projects
* **Aug 22**: GSoC officially ends

## List of Mentors
The following individuals will be serving as mentors during GSoC 2018:

* Allan Zhou (@AllanYangZhou)
* Anmol Shukla (@anmolshkl)
* Brian Rodriguez (@brianrodri)
* Kevin Lee (@kevinlee12)
* Prasanna Patil (@prasanna08)
* Rachel Chen (@rachelwchen)
* Sean Lip (@seanlip)
* Tony Jiang (@tjiang11)
* Vojtěch Jelínek (@vojtechjelinek)

## Communication

**Chat**

Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](
https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any questions related to getting started. For project-specific questions, please direct your queries to the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).

**Email**

If you have questions pertaining to "how-to-get-started", please ask them on [Gitter](
https://gitter.im/oppia/oppia-chat), or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you.

To discuss your project ideas or share your proposal for feedback from the community, please email the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).