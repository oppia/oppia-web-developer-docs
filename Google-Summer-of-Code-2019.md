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
    * [List of Mentors](#list-of-potential-mentors)
    * [Communication](#communication)

Oppia is participating in [Google Summer of Code 2019](https://developers.google.com/open-source/gsoc/)! GSoC is a global program which offers post-secondary students an opportunity to discover and work with open source organizations over the course of 3 months, while being paid a stipend. Students work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

You might be interested in our GSoC info pages from previous years: [2018](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018), [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

Also, please note that acceptance into GSoC isn't a prerequisite for [becoming an Oppia contributor](https://github.com/oppia/oppia/wiki). The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out!


## Completed Projects

The following projects were fully completed during GSoC 2019:
- [@anubhavsinha98's proposal](pdfs/GSoC2019AnubhavSinha.pdf) and [final blog post](https://medium.com/@anubhavsinha98/gsoc19-journey-oppia-308704ffa3a) for enabling students to say why they provided a given answer. Mentor: Akshay Anand.
  - **Milestone 1**: The creator can add an option, for each state, to ask learners for a response. The infrastructure for storing, retrieving and processing responses from the datastore is implemented.
  - **Milestone 2**: Learners can submit responses for states (if the creator has asked for this).
  - **Milestone 3**: The creator can view all responses received for a state, and can resolve a set of responses by creating a new answer group or updating an existing one.
- [@Jamesjay4199's proposal](pdfs/GSoC2019JamesJohnJames.pdf) and [final blog post](https://medium.com/@jamesjay4199/google-summer-of-code-19-at-oppia-foundation-ce18bf34eb8c) for enabling pages to be served statically. Mentor: Vojtěch Jelínek.
  - **Milestone 1**: All static pages serve without Jinja. (NB: dynamic pages are: profile, admin, library, creator_dashboard, skill_editor, story_editor, exploration_{player|editor}, topic_{viewer|editor}, collection_{player|editor}. All others are static.)
  - **Milestone 2**: All dynamic pages have no Jinja constructs except: interaction_templates, dependencies_html, visualizations_html, value_generators_js, rich_text_components.
  - **Milestone 3**: Jinja is fully removed from the Oppia codebase.
- [@lilithxxx's proposal](pdfs/GSoC2019RishavChakraborty.pdf) and [final blog post](https://medium.com/@reshav01/google-summer-of-code-19-with-oppia-a4d4318b1808) for making the codebase compatible with Python 3 and covering the backend fully with tests. Mentor: Brian Rodriguez.
  - **Milestone 1**: At most 500 lines of Python code (outside ‘scripts/’) remain untested.
  - **Milestone 2**: The Python coverage for the codebase reaches 100% and the codebase supports both Python 2 and 3. There are checks which ensure that both these conditions are preserved going forward.
  - **Milestone 3**: All bash files are removed from the codebase.
- [@sophiewu6's proposal](pdfs/GSoC2019ShiqiWu.pdf) and [final blog post](https://medium.com/@wushiqi1998/google-summer-of-code-2019-with-oppia-bf585e142a65) for improvements to the questions framework. Mentor: Vinita Murthi.
  - **Milestone 1**: Students encounter review tests after every 2-3 explorations. The modal after each test shows their results for that test.
  - **Milestone 2**: The results of the review test are used to pass or fail students, and show follow-up learning advice. Answer groups are linked to misconceptions in the state editor.
  - **Milestone 3**: Skill mastery levels are updated after every test, and shown in the frontend (in both the skills tab and the result modals). Questions are selected based on difficulty and skill mastery levels.



# Students
GSoC is an excellent opportunity for students to get paid to work on an open source project. If you're interested in applying as a student, you should definitely read the following resources:

- [Google Summer of Code student guide](https://google.github.io/gsocguides/student/)
- [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
- [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)

## Getting started

If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. If you like, you can also sign up to the [oppia-gsoc-discuss@](https://groups.google.com/forum/#!forum/oppia-gsoc-discuss) mailing list to participate in general discussion related to Oppia's involvement in GSoC (see point 5 below, too). Make sure to set your mailing list preferences correctly so that you actually get the emails!

1. Get a better understanding of what Oppia is all about by taking a look at our [user documentation](http://oppia.github.io/#/) -- this will help you become familiar with important concepts like explorations and interactions. We also recommend having a go at playing some of the existing lessons on [Oppia.org](https://www.oppia.org), like [these ones on Fractions](https://www.oppia.org/fractions), to get a better idea of what they look like.

1. Read and follow the instructions in the [contributors' guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) carefully.

1. Consider taking up one or more starter projects in order to become familiar with the contribution process. This will help us get an idea of what it's like to work with you -- e.g. how independent, resourceful, responsive, etc. you are. It will also help you get a better understanding of the codebase, so that you can write a good, detailed project proposal.
    - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to follow the [dev workflow](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#instructions-for-making-a-code-change) carefully, manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide), and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

1. When you've done enough starter projects to get a good understanding for the "lay of the land", select one or more GSoC projects that you're most interested in, and write your project proposal! We strongly encourage you to discuss your project ideas and share your proposal with the community, so that you can get feedback and ensure that what you're writing makes sense to others. The best way to do this is to put your proposal into a collaborative editing tool like Google Docs, allow others to comment on it, and share a link to it on the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com). You can also email this mailing list if you have any questions about a project, or would like to discuss your approach with the Oppia community and get feedback. Please be specific when asking questions, since this makes it easier for us to help you.

## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: Familiarity with AngularJS (v1), Python 2.7 and Google App Engine is useful and recommended for most Oppia work. In addition, UI design skills are useful for frontend, user-facing work. Please see the individual project ideas to determine whether these skills are recommended for the project in question.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other students, successfully contributing patches, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: GSoC is intended to be a full-time commitment, so the main concern is whether you can still get the project done on time. Be upfront about your other commitments and make sure you schedule your time accordingly when creating your proposal. Other commitments you should list include time when you'll be in school and will commit less time to GSoC, time when you'll be travelling and away from GSoC work, any summer jobs you need to commit to, etc. We will try to be flexible around other time commitments, as long as your proposal convinces us that you will have enough time to complete the project by the end of the summer. On the other hand, if you do not disclose other commitments, and it turns out that you are unable to commit to what you wrote on your proposal, this is grounds for failing the program.

**Q: Which projects are most important for Oppia?**

A: All the projects we've listed here are important, and we'd be very happy to see good progress made on any of them! Projects are treated as equally important during selection. Note that the relative importance of a project to Oppia is not part of the [selection criteria](#selection-criteria).

**Q: Can I submit more than one proposal to Oppia?**

A: Yes you can. However, we strongly recommend picking one project and writing a solid proposal for the same. Splitting attention across multiple projects might not be a great idea. 

**Q: How early should I start working on the proposal?**

A: As early as possible. Make sure to get feedback from mentors before finally submitting the proposal. This will help you to write a better proposal as you can refine the details based on the feedback you receive. The mentors would need some time to review, and hence it is a good idea to begin as early as possible.  


## GSoC Proposal Template

**Important:** Please make sure that your final proposal is self-contained! In particular, to be fair to all applicants, key components of the proposal should not be editable after the deadline, and you shouldn't assume that reviewers will follow external links.

When submitting a proposal, please use the following template:

**Project Details**
- Name of the project.
- Why are you interested in working with Oppia?
- What interests you about this project?
- Prior experience (especially with regards to technical skills that are needed for the project).
- Links to 1-5 PRs you've made that showcase your best work, especially any Oppia ones. The list should include at least one Oppia PR, but you can also include some other PRs from major open-source projects if you like.
- Project plan and implementation strategy. This is the most important section of the proposal. If you're not sure how to structure it, we strongly recommend following a structure similar to [Oppia's design doc template](https://docs.google.com/document/d/1eMivKj5uWkOkj4AB684JVJslAe49gSskZ-VsyUjgPN4/edit).

**Summer Plans**
- Which timezone(s) will you primarily be in during the summer?
- How much time will you be able to commit to this project?
- What jobs, summer classes, and other obligations might you need to work around? Please be upfront about any existing commitments you may have. (See the [FAQs](#faqs).)

**Communication**
- What is your contact information, and preferred method of communication?
- How often, and through which channel(s), do you plan on communicating with your mentor?

### Tips for writing a good project plan

The project plan is the most important section of the proposal, since it outlines what you'll be doing during the summer. We recommend that you follow a structure similar to [Oppia's design doc template](https://docs.google.com/document/d/1eMivKj5uWkOkj4AB684JVJslAe49gSskZ-VsyUjgPN4/edit) -- if any section isn't relevant for the project, please keep the section and explain why it's not relevant. 

Here's some guidance on what the mentors and organization admins will be looking for in this section:

- **Three clear milestones** explaining the deliverables to be achieved by the end of each of the three GSoC coding periods. Strong proposals will have clear, concrete and measurable milestones, whose success can be objectively evaluated by an external observer. It's OK to break up a milestone into smaller milestones over smaller timescales, but individual milestones should represent *concrete* deliverables that can be merged safely into the "develop" branch and included in a subsequent Oppia release. **<u>Please try to be realistic when setting milestones, and don't over-promise.</u>**

- **A technical design and implementation plan**. The project ideas below are annotated with some notes from the mentors, but please bear in mind that these notes are not exclusive and shouldn't serve as a substitute for thinking carefully and critically about the project from first principles -- their main purpose is to suggest ideas or possible starting points. If, in your thinking, you find aspects not mentioned in the notes, feel free to include a discussion of these aspects in your proposal. (For example, certain projects may require a migration of existing production data, and this needs to be accounted for in the project plan.) Strong proposals will demonstrate familiarity with the codebase, a realistic implementation plan, and attention to detail.

- **Mocks or wireframes**, if appropriate. For user-facing projects, we strongly favour proposals that demonstrate an empathy for the user. If you're proposing frontend design mocks, we suggest showing your ideas to your friends and getting their critical feedback, so that you can be confident that others find them intuitive as well. Note that your mocks need not be pixel-perfect, but they should illustrate the primary user journeys clearly enough for us to understand exactly what you're proposing. Also, bear in mind that "more is not necessarily better" -- an important aspect of user-focused design is deciding what _not_ to do.

- **A testing plan.** Testing is an important part of any coding project, and should be taken into account when planning the schedule. In particular, any new functionality added to Oppia's codebase should be backed by unit tests, and any new core user journey should be accompanied by a corresponding end-to-end test. If your project includes migrations, please also take the [pre-release testing in production](https://github.com/oppia/oppia/wiki/Running-jobs-in-production) process into account when planning. Finally,  make sure to budget enough time to test your changes manually before submitting each PR -- otherwise, any bugs that are subsequently discovered during review (or the monthly QA process) could result in significant delays and lead to the failure of an otherwise successful project.

**[NEW!]** Here's some advice about proposals and milestone timeline planning that we collated from 2018 students and mentors:
- Choose a project you're interested in! If you have a strong interest in your project, this will help you pick up necessary skills and tackle any unforeseen difficulties that arise during GSoC.
- Familiarize yourself with the relevant part of the codebase for your project, especially if you haven't touched it before. It's important to think about how to integrate your project with the current Oppia structure -- don't design in a vacuum.
- Define milestones with enough detail to get a proper ETA for each milestone (so, don't just say "write e2e tests"), otherwise you run the risk of significantly underestimating the timeline.
- Try to design milestones in such a way that the last 1 week of each milestone period is free, and can be used as a testing period.
- The timeline should account for the time it will take to get PRs reviewed. One way to do this is to explicitly specify two dates: (a) when the initial PR should be sent in by, and (b) when it should be merged by.
- If work needs to be done in time for a particular release, the initial PR should be sent well in advance of the [release cutoff date](https://github.com/oppia/oppia/wiki/Release-Schedule).
- If you're working on tasks that depend on jobs being [run in production](https://github.com/oppia/oppia/wiki/Running-jobs-in-production), the timeline should account for any delays inherent in this process.

### Sample proposals from past years

If you'd like to get a sense of what a proposal might contain, please see our [GSoC 2018 page](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018) for examples of proposals that we accepted in 2018. 

_**Note:** although some of these proposals are a bit on the long side, there's no formal length requirement for your proposal -- in general, the quality of what you write is much more important than the amount of text you write. For the actual requirements, please see the [GSoC Proposal Template](#gsoc-proposal-template) section above._

## Types of work related to Oppia projects
In order to ensure a well-rounded engineering experience, developers will do some or all of the following depending on their project:
- Meet with their mentors regularly
- Meet with other contributors related to their project area
- Receive code reviews for all code they write for their project
- Write automated tests for their projects
- Create UI mocks (if doing frontend development)
- Write design documents (if implementing large features or introducing new systems)

**[NEW!]** In 2018, we asked our students what they learned during GSoC. Here are the collated answers:
- Technical ability
  - Writing clean code with comments
  - Writing tests
  - My debugging skills improved a lot.
  - Refactoring skills.
- Technical domain knowledge
  - I'm much more fluent in Python and AngularJS.
  - I feel that I can now pick up any new framework/language/skill easily, without much uncertainty.
  - I got to know about the one-off jobs in detail.
- Technical leadership skills
  - Single-handedly releasing a big feature end-to-end.
  - Reviewing others' code
  - Technical design skills (and validation of technical ideas)
  - Organizing release testing teams
  - I feel that I can think about a feature end to end and prune out all the not so essential features, so that we can create a minimum viable product!
  - I learnt how to coordinate with folks around me.
- Communication
  - Putting forward my thoughts more systematically and deeply so that everyone can understand me well.
  - Better communication skills.
  - How to write a good proposal.
- I learned a lot other than coding, including writing technical documents, doing meetings, presentations, testing, etc. This was also the first time I was writing well-tested backend code, which was also an interesting learning experience for me.

## Selection Criteria

In order to select students for GSoC, we will mainly be looking at three things:

- The quality of the submitted proposal
- The quality of the applicant's previously-submitted PRs (in order to assess their ability to code, debug, break down complex tasks, etc.). Note that quantity isn't a prerequisite in itself, though contributors who've submitted multiple PRs are likely to have had more opportunities to demonstrate the abilities needed to succeed in GSoC.
- Our prior experience working with the student (do they keep commitments, communicate well, demonstrate independence/initiative/responsiveness, help others, etc.)

We believe that strong performance in these dimensions is likely to correlate well with the student having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the GSoC program.

For the proposal, we generally look for a clear indication that the student has a good, deep understanding of the project, and has broken it down sufficiently well, in a way that makes it very likely to succeed. Some indicators that could help with this include:
- A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating a simple, intuitive experience for end users.
- A concrete, specific breakdown of the work to be done for each milestone. Here's an [example](https://docs.google.com/document/d/1vuwXvHOYXqfM2S2B2KIWhZrAa1PL59wJRUYsqJEd67E/edit) from a previous design doc. (Note that, in the implementation plan, the author has carefully considered and listed which tests need to be written alongside the code; this is a positive indicator.)
- Sufficient concreteness (e.g. references to particular files and methods) to demonstrate that the applicant is familiar with both the scope of the problem and the existing codebase.
- A description, if applicable, of how the applicant plans to mitigate risks that could potentially derail the project.
- Clear, unambiguous communication. (This is important; your proposal will be read by many mentors!)

# Oppia's Project Ideas

The following is a list of Oppia's 2019 GSoC project ideas. (Please note that all mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted.)

You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community in order to get feedback and guidance to improve the proposal. We also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

This year, the Oppia team is offering three types of projects: projects that improve the creator experience, projects that improve the learner experience, and infrastructure projects. Some of the project ideas are annotated with notes and suggestions from the mentors, but please bear in mind that the main purpose of these notes is simply to suggest ideas or possible starting points; they aren't meant to be prescriptive. You'd also be welcome to include discussions of other relevant aspects (that aren't mentioned in the notes) in your proposal. For more information, see: [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan).

### "Creator Experience" Projects

1.1. [Building a lesson artist dashboard](#11-building-a-lesson-artist-dashboard)

1.2. [Infrastructure for measuring exploration enjoyability](#12-infrastructure-for-measuring-exploration-enjoyability)

1.3. [Translation infrastructure enhancements](#13-translation-infrastructure-enhancements)

1.4. [Improvements to the editor saving flow](#14-improvements-to-the-editor-saving-flow)

1.5. [Creating a "reviewer view" for explorations](#15-creating-a-reviewer-view-for-explorations)

1.6. [Allow creation of parameterized questions](#16-allow-creation-of-parameterized-questions)

1.7. [Community-based voice-over and translation](#17-community-based-voice-over-and-translation)

### Learner View Projects

2.1. [Highlight text in a lesson as audio is played](#21-highlight-text-in-a-lesson-as-audio-is-played)

2.2. [Review tests and other improvements to the questions framework](#22-review-tests-and-other-improvements-to-the-questions-framework)

2.3. [Asking students why they picked a particular answer](#23-asking-students-why-they-picked-a-particular-answer)

2.4. [Memorization experience for learners](#24-memorization-experience-for-learners)

### Infrastructure Projects

3.1. [Improve frontend and end-to-end tests](#31-improve-frontend-and-end-to-end-tests)

3.2. [Improve backend test coverage and upgrade it to support Python 3](#32-improve-backend-test-coverage-and-upgrade-it-to-support-python-3)

3.3. [Migrate the frontend to Angular 2](#33-migrate-the-frontend-to-angular-2)

3.4. [Upgrade third-party libraries](#34-upgrade-third-party-libraries)

3.5. [Static serving](#35-static-serving)

3.6. [Validate invariants between data models](#36-validate-invariants-between-data-models)

## "Creator Experience" Projects
### 1.1. Building a lesson artist dashboard
Art and graphics form an integral part of most explorations on Oppia, and are especially important for making lessons learner-friendly and communicating key concepts to learners, especially since good graphics can transcend language barriers. However, one major blocker when creating lessons is the lack of an easy way for designers/artists to add images to lessons. We would like to enable artists to contribute to lessons as easily as developers can contribute to GitHub repositories.

This project has two goals. Firstly, we would like to make it possible to have dedicated artists for explorations: this will allow creators to assign artist roles, and allow the art development workflow to happen in parallel with other creative work. Secondly, we would like to implement a way to organize creation of graphics (using the existing suggestions framework) in a way that mimics the issue tracker on GitHub. More specifically, all open image requests should be surfaced to non-editors/artists of the exploration, who should have the option to suggest an image; once a suggested image is subsequently approved by the editors/artists, it can be added to the lesson.

**Potential mentors**: **@nithusha21** (primary)

**Difficulty**: Medium

**Knowledge/Skills needed**
* Good technical design 
* UX design
* Full stack development (Python + AngularJS)

**Suggested milestones**
1. Implement an "image placeholder" component in rich-text editor fields for explorations, and implement a new role for artists that gives them permissions to contribute images to these image placeholders (or replace existing images). It should also be possible for exploration creators (who, typically, aren't artists) to upload temporary images to these placeholders, but mark those temporary images as still needing to be replaced with a proper image.
1. Implement a single common view for all explorations that lists all open image requests. The creator of the exploration should be able to flip a boolean setting which would enable image placeholders within their (typically, not yet published) explorations to be displayed in this common view. The common view should be accessible to all logged-in users and easily reachable from the creator/learner dashboards. Suggestions for images would be submitted through this view.
1. Enable users to contribute images for the requests in the common view. Suggested images should appear on the feedback tab of the editor page for the specific exploration. The exploration's artists/editors should then be able to review the suggestion. If the image is accepted, the suggested image should then be added to the exploration.

***

### 1.2. Infrastructure for measuring exploration enjoyability
In order to ensure that students enjoy the lessons on Oppia, we need to develop a way to measure lesson "enjoyability" so that creators can see the effects of their changes. The aim of this project is to define and put in place the necessary infrastructure for this. By the end of the project, we'd like to make it possible for creators to see whether their lessons are enjoyable, as well as figure out which parts of their lessons might be frustrating/confusing/boring so that they can fix those for future learners. We'd also like to introduce a dashboard that makes it easy to see at a glance which lessons need improvement, so that they can be fixed.

In order to do this, we would need to figure out what "enjoyability" means. Here are some initial suggestions for metrics (but you are welcome to suggest your own):
* Enjoyability:
  * Did a student finish the exploration?
  * Did they carry on to the next exploration in the series?
* Possible ways to detect issues:
  * Frustration: The student submits more than two answers in a row without leaving the card.
  * Confusion: In a particular card, the same answer is submitted more than once, with at least one other answer to that card appearing between consecutive submissions.
  * Boredom: _We're not sure :) What do you think?_

**Potential mentors**: **@brianrodri** (primary), **@kevinlee12**

**Difficulty**: Medium

**Knowledge/Skills needed**
* Full stack development (Python + AngularJS)

**Suggested milestones**
1. Find a way to calculate and store the "continuation metric" (i.e. does the student continue with the next lesson in the series). Then, create a dashboard for all curated lessons that shows, for each lesson, the combined completion + continuation stats.

2. Introduce a frontend service which detects signals indicating student boredom / frustration / confusion, creates cross-sectional metrics in real-time, and sends those metrics to the backend, which stores them as aggregate metrics. Additionally, add new playthrough types to match these metrics as needed (e.g., a playthrough which demonstrates "boredom"), so that these can be used as supporting evidence when debugging the issues.

3. Show the signals detected in Milestone 2 in the statistics tab. Audit the full detection/resolution flow and fix any other issues in order to ensure that the end-to-end experience for debugging and improving lessons is fully intuitive.

**Notes**
* In Milestone 2, you may be able to reuse quite a bit of the existing infrastructure for playthroughs.

***

### 1.3. Translation infrastructure enhancements
Currently, Oppia provides a simple platform for translators to record and track the progress of audio voiceovers that are contributed to lessons. From talking to translators, we have found that there are some improvements that could be made to this platform that would make it easier to translate lessons, namely:
* Caching/storing recorded audio locally until it is saved, so that translators can easily check their work by clicking "Play" after uploading an audio file.
* Allowing users to upload multiple audio files at a time.
* Allowing multiple translators to work in parallel without losing their draft changes.

**Potential mentors**: **@DubeySandeep** (primary)

**Difficulty**: Medium

**Knowledge/Skills needed**
* Frontend development
* Good UI/UX design

**Suggested milestones**:
1. Make it possible for translators to upload multiple audio files at a time for a single card, and automatically match audio files to the correct place (or allow them to do this manually).
2. Cache recorded audio, so that translators can easily check their work by playing audio after uploading it.
3. Enable multiple translators to work in parallel without losing their draft changes.

***

### 1.4. Improvements to the editor saving flow
There are several serious issues with current workflows in the exploration editor that can occasionally cause loss of work. In particular:

* When an exploration is migrated to a newer schema version, any existing draft changelists should also be updated accordingly. Currently, draft changelists are not updated, resulting in a version mismatch and a loss of work when the exploration creator subsequently tries to apply the draft. (See #4438 for some discussion.)
* When an exploration is updated, any existing suggestions in the feedback tab should be updated accordingly. Currently, such suggestions are not updated, resulting in a version mismatch and a loss of work when the exploration creator subsequently tries to apply the suggestion.
* When changes cannot be saved to an exploration, a "lost changes" modal pops up so that the creator can make a copy of their edits and then reapply them. However, the code for this modal is not robust, and in particular it does not take into account draft changelists that were stored in an older format. Thus, when it tries to display such drafts, it breaks and ends up not showing anything.
* It is difficult to change an interaction into a slightly different one (e.g. from text input to number-with-input) without losing all the associated responses, hints and solutions. It would be nice to declare a suitable transformation that allows this data to be carried over from one interaction type to a closely-related one, and to auto-migrate as much of the responses as possible so that the creator does not lose their work.

The aim of this project is to fix any three of these issues.

**Potential mentors**: **@seanlip** (primary)

**Difficulty**: Medium

**Knowledge/Skills needed**
* Full stack development including Python and AngularJS
* Good technical design

**Suggested milestones**
Choose three of the issues above, and fix them. Fixing each issue counts as a single milestone.

**Notes**:
If you'd like to get a bit more familiar with the exploration editor, here is a simpler issue along the same lines that you might like to have a go at: When switching from a rule type to a different rule type, the inputs to the old rule type get lost, even though both rule types have the same types of inputs and it is possible to carry the inputs over.

***

### 1.5. Creating a "reviewer view" for explorations
In order to ensure a high level of quality, explorations are often reviewed by an experienced lesson creator before publication. However, this is currently a somewhat tedious process that requires lots of clicking from one state to another, which can make it difficult for the reviewer to get a sense of the main "flow" of the exploration.

It would be nice to have a more linear, scrollable view of the entire exploration which is optimized for reviewers, and which supports basic commenting functionality. The aim of this project is to build this view.

**Potential mentors**: **@aks681** (primary), **@seanlip**

**Difficulty**: Medium/Hard

**Knowledge/Skills needed**
* Python and AngularJS
* Good UI/UX design
* Good technical design
* Very good understanding of what an exploration is, and what its various components are

**Suggested milestones**
1. Implement a basic "reviewer's view" of the exploration in the editor tab. In addition to the "content" section of each card, this view should also include a representation of at least two of the following: interaction, feedback/responses, hints, solution.
1. Fully implement the reviewer's view. Implement the backend storage for reviewer comments on parts of an exploration.
1. Implement the frontend system for reviewer comments on parts of an exploration.

**Notes**
* Proposals must include clear mockups or wireframes for how the display would look. A sample exploration converted into linear view as an example would be great!
* Proposals should clearly indicate how each of the components of an exploration would be handled (interaction, hints, solutions, answer groups). Be sure to think about what makes the most sense for the reviewer -- you don't need to include everything in full detail. For example, the reviewer probably won’t need to see fully-fledged interactions that they can interact with.
* The proposal should explain how branching explorations would be handled. (Note, though, that explorations are typically fairly linear in nature, with branching used only for reviewing earlier material and/or going back to earlier cards. The reviewers' view should be strongly optimized for that use case, but there should be a clear plan for how to handle non-linear explorations.) Note that the overview graph in the exploration editor page already shows a "main trunk" for the exploration, which could serve as the basis for how to pick the cards to display in a linear view.
* In milestone 2, we recommend trying to expand the existing feedback system to allow references to specific parts of a card, rather than creating a brand-new system from scratch.
* The reviewer view should support simple threaded comments like Google Docs and the existing exploration editor feedback tab (but it doesn't need to support any form of collaborative editing).

***

### 1.6. Allow creation of parameterized questions
The addition of the upcoming questions framework allows us to create a large question bank for practice questions. However, it would be tedious for creators to create a large number of questions with similar formats but slight variations (e.g. "Add 4/5 and 3/4", "Add 2/3 and 3/5", etc.)

Instead, we would like to introduce the concept of parameterized questions, where the creator can specify parameters which can be used to generate many questions at once. (In the example given above, the question might be of the form “Add a/b + c/d”, with parameters a, b, c, d. The question creator would specify ranges of values for the parameters in order to generate questions.)

Note that parameterization might potentially extend to expressing the same question in different ways. For example, we might want to be able to treat the questions "Add a/b + c/d", "Find the sum of a/b and c/d", and "{{name}} has a/b of a cake and {{other_name}} has c/d of the same cake; what is the total amount of cake they have?" as the same.

**Potential mentors**: **@aks681** (primary), **@vinitamurthi**

**Difficulty**: Hard

**Knowledge/Skills needed**
* Full stack development
* Good technical design
* Good UX design

**Suggested milestones**
1. Make any backend changes that are necessary to allow parameter values / ranges to be stored along with a question, and implement functionality (hidden behind a flag) for specifying these values / ranges in the frontend.
2. Implement functionality that allows authors to use parameters in question content and rules.
3. Implement functionality to allow creators to audit that the parameterizations they have chosen work well in all cases, and result in sensible questions.

**Notes**
* Good technical judgement is really important for this project, particularly in ensuring that the system that is built is not too complicated. We expect a GSoC project for this idea to cover only a sub-part of what is described in the description above; figuring out a suitable scope for this subproblem (and explaining clearly how it could be extended in the future) is an important part of the proposal.
* The existing [parameters/expressions framework](http://oppia.github.io/#/Parameters) might be a useful starting point. Note that there is some existing functionality for parameters in the codebase, but it is not well-maintained. It is probably best to figure out a design for this system from scratch, and only then see whether the existing "parameter" functionality can fit well into the proposed system.
* There should be a way for creators to audit that the parameterizations they have picked work well in all cases and result in sensible questions (cf. Milestone 3). The user flow for doing this should be clearly laid out.
* Proposals should explain clearly how the rules in answer groups will handle parameters without complicating the default lesson creation experience. Perhaps there could be an "advanced view" which shows a more complicated UI only when parameters are activated in the Settings tab.
* [Bonus] Currently, Oppia lessons can be augmented with translations and voiceovers in other languages, which are very helpful for learners. It would be great if you could suggest a clean way to handle audio translations for parameterized questions -- but note that this isn't a requirement for the project!

***

### 1.7. Community-based voice-over and translation

Most of the Oppia lessons are in the English language which is used by 15-20% of the entire population in the world. To make our lessons more accessible to people around the world we need our lessons to have translations in different languages. This project focuses on making Oppia lessons more shareable and breaking the language barrier for learning new things by allowing the Oppia community to help to translate and voice-over the exploration in different languages.

The workflow for voiceovers and translations are going to be different as translations can be done incrementally whereas the voiceovers for the entire exploration needs to be done by a single contributor so that we have a consistent voice throughout the exploration. To accommodate such pattern we are thinking of having two workflows:

“Project” workflow for voiceover:
As part of their application, the translator or voice actor should submit a voiceover of the initial state. The proficient voice-artist (in that specific language) would review this and decide:
Whether to accept or reject the application and based on that the contributor will get assigned as a voice-artist for that exploration.

All translators and voice actors should only be actively assigned to one exploration at a time. Once an assignment is made, any remaining pending applications should be cancelled until that task is completed.

“Suggestion” workflow for translations:

A user may decide to suggest a few written translations to exploration, they should be redirected to the translation tab and allowed to add translation suggestion in the specified language. Once they submit a translation, a proficient translator (in that specific language) should either accept or reject the suggestion.

**Potential mentors**: **@DubeySandeep** (Primary), **@nithusha21**

**Difficulty**: Medium/Hard

**Knowledge/Skills needed**:
* Python and AngularJS
* Good UI/UX design
* Good technical design
* Good understanding of existing suggestion and review structure.

**Suggested milestones**:
1. Create a backend structure to provide points to translators/voice-artists based on their work as a translator/voice-artist. Create the backend structure for the “suggestion” workflow (including review system).

2. Create the full UI for the suggestion workflow, including functionality for contributors to see the list of explorations which they can translate/voiceover in the dashboard. Create a backend structure for the “project” workflow.
 
3. Create the full UI for the project workflow, including allowing users to see reviews of their audio-applications and respond to them.

**Related issues**: #6536

***

## Learner View Projects
### 2.1. Highlight text in a lesson as audio is played
We have found that audio voiceovers (especially in native languages) are very helpful for learners for whom English isn't a first language. However, for longer cards, it is difficult for learners to match the audio voiceover to the text on the card. It would be great for learners to be able to track the audio with the text. 

The aim of this project would be to allow lesson translators and voiceover artists to annotate textual translations and voiceover audio respectively, so that the relevant text can be highlighted in the exploration player while the corresponding audio is playing. A rough requirements doc for this project can be found [here](https://docs.google.com/document/d/1VUaXm4V0YxyPXRBz8W_YMWEC_guzcnccju8d3KWz5jw/edit).

**Potential mentors**: **@DubeySandeep** (primary)

**Difficulty**: Hard

**Knowledge/Skills needed**: 
* Full stack development
* Good UX design

**Suggested milestones**:
1. Change the backend schema for an exploration as required (in order to include annotations) and migrate existing explorations to the new schema.
1. Create a frontend UI that allows translators and voiceover artists to easily specify the correspondences between an audio voiceover (possibly in a different language), the text of the written translation in that language, and the text of the original exploration card.
1. Update the learner view to allow the corresponding text to be highlighted when the audio is playing.

**Notes**
* Proposals should include clear descriptions of the workflows for annotators (both those who are working on written translations and audio voiceovers).
* A lot of the difficulty of this project arises in handling edge cases correctly, while still ensuring that the workflow for creators is as simple as possible. Strong proposals would carefully explain how they plan to handle edge cases.

***

### 2.2. Review tests and other improvements to the questions framework
While explorations and stories help encourage a learner to continue learning, it is also useful for a learner to be able to keep track of their understanding as their learning progresses. Review tests are an upcoming feature in Oppia that aims to help learners test the skills they've learned after they have completed 2-3 lessons in a story in that topic. These review tests would be automatically presented to the learner once they have progressed up to a certain point in the story, and would need to be completed successfully in order to advance to the next part of the story.

This project aims to create the learner view for review tests, and to improve the question framework as a whole so that the experience of practising questions on Oppia (via pre-tests, review tests and practice sessions) is as effective and enjoyable as possible.

**Potential mentors**: **@vinitamurthi** (primary), **@aks681**

**Difficulty**: Medium

**Knowledge/Skills needed**
* UI/UX design
* Full-stack development (Python and AngularJS)

**Suggested milestones**
1. Implement the full user flow for review tests. After this milestone, review tests should be presented to students at the right time, making use of the existing question player component. At the end of the review test, there should be a way for the student to return to the story they were on.
1. Update the question player framework to return more information than just the score, once the learner has completed the test. Specifically, the question player framework should be able to return the score, as well as calculate and return the mastery of the skill(s) that were tested. At the end of this milestone, the question player API should return score as well as a list of skills tested along with their mastery levels.
1. Use the skill mastery information returned by the question player API in each of the tests (i.e. pre-tests, practice sessions, and review tests). Each of the tests would have to use the skill mastery levels in different ways. Pre-tests would use mastery to decide whether the learner has passed the requirements and can proceed with the lesson, whereas review tests and practice sessions would use the mastery values primarily to keep track of the learner's progress and pass on recommendations for next steps to the learner.

**Notes**
* Proposals should include user flows for what the review tests experience would look like.
* For Milestone 2, proposals should define a reasonable approach for measuring and modifying skill mastery levels (which would be represented as floating-point numbers between 0.0 and 1.0 for each skill).

***

### 2.3. Asking students why they picked a particular answer
We would like to add a feature to the lesson player that allows students to explain how they arrived at a (wrong) answer. The aim of this feature is to encourage reflection on the student's part, as well as provide (anonymized) information to creators about student misconceptions, so that the creator can improve Oppia’s feedback for future students.

**Potential mentors**: **@nithusha21** (primary), **@aks681**

Difficulty: Medium

**Knowledge/Skills needed**
* Good technical and UI/UX design
* Full stack development

**Suggested milestones**
1. Implement the backend data storage models, domain objects, services and controllers needed for this feature. Note that this feature should be whitelisted to the same set of explorations for which learner playthroughs are whitelisted.
1. Augment the learner view UI to enable learners to fill out responses.
1. Augment the editor view UI to surface these responses to creators, and complete the end-to-end feature so that the complete life-cycle functions correctly. Add e2e tests to verify the overall life-cycle.

**Notes**
* Proposals must clearly state what conditions trigger this flow. The process should not unduly obstruct the learner -- e.g, it would not be nice to surface a modal with "explain your approach" every time the learner clicks submit, and perhaps we might want to do this at most once per lesson. Proposals should also outline when and where this data is surfaced to creators.
* Proposals must clearly explain the complete lifecycle of this feature, starting from the learner's submission and proceeding all the way to the creator improving the lesson based on that feedback. Be sure to consider "non happy path" flows as well, such as when the student does not provide an explanation that the creator can understand, or does not want to provide an explanation at all.
* Proposals should include mocks for both the learner and creator user journeys.

***

### 2.4. Memorization Experience for Learners
For some topics, attention needs to be given on memorizing data (such as the names of the counting numbers, the times table, the months in a year, or the planets in the solar system). There should be an effective way for learners to do this as needed, in a topic or in an exploration. The creator should be able to specify the information that needs to be memorized, and there should be a built-in mechanism in Oppia that helps the learner commit this information to memory as quickly and accurately as possible.

**Potential mentors**: **@seanlip** (primary)

**Difficulty**: Medium/Hard. This project is somewhat open-ended. We encourage coming up with a proposal which is reasonable in scope, but which also can be backed by evidence that implementing it would lead to an effective learning experience.

**Knowledge/Skills needed**
* Full-stack development
* Good technical design
* Good UX design

**Suggested milestones**
These will depend strongly on the nature of the proposal. In general, we recommend:
1. Make all necessary backend changes for this project, working through the stack, starting from the storage models to the backend controllers.
1. Make all necessary frontend changes for the editor view to enable the creation of such experiences for learners.
1. Make all necessary frontend changes for the learner view to enable them to experience this feature.

**Notes**
* Proposals should define where this experience takes place, and why -- is this a separate experience at the topic level, or is it part of an exploration? The overall user experience for the student should be a natural one, and be defined in the proposal as clearly as possible.
* The success of this project is based on how effectively it helps students memorize a list of predetermined facts/words. The proposal should explain why the approach chosen is likely to be effective.
* For this project, simple and elegant approaches are preferred to more complex ones.

***

## Infrastructure Projects
### 3.1. Improve frontend and end-to-end tests
In order to ensure that users of Oppia have a smooth experience, we would like to ensure that all frontend functionality in Oppia is fully tested, at all times, before it goes into production.

The aim of this project is twofold: (a) to achieve 100% coverage for the frontend tests and ensure that this state is preserved in the future, as well as (b) to improve Oppia's end-to-end tests coverage and make them run faster.

**Potential mentors**: **@apb7** (primary), **@nithusha21**

**Difficulty**: Medium

**Knowledge/Skills needed**
* Familiarity with Karma and Protractor
* Basic understanding of AngularJS
* A good "testing" mentality.

**Suggested milestones**
1. Extend frontend unit tests to reach at least 75% coverage.
1. Extend frontend unit tests to reach 100% coverage and lay down guidelines/rules which ensure that this state is preserved, that is, the coverage always remains at 100%. These guidelines/rules should make it easy for future developers to incorporate the necessary tests along with their code, and prevent insufficiently-tested code from making it into the codebase.
1. Optimize the e2e tests on the following grounds (while ensuring that coverage remains at 100%):
    1. Pull out common flows from the e2e tests that run on both desktop (core/protractor_desktop) and mobile (core/protractor_mobile), and organize them in core/protractor instead.
    1. Make the tests faster by minimizing repetition of statements between different tests. (Refer to the first bullet point under Notes.)

**Related issues**: #4057

**Notes**
* A general problem observed with the end-to-end tests is the repetition of actions, in both the initial setup and the steps performed. This makes the end-to-end tests a bit inefficient and results in their taking more time to be completed. Proposals should clearly explain how they are planning to ensure that this problem is removed once and for all, and what amendments must be made to the guidelines for end-to-end tests.
* The present frontend coverage is 46.07% with respect to statements (12562 statements covered out of a total of 27266 statements). Proposals should explain a plan to reach 100% coverage and outline how this state of affairs will be preserved in the future.

***

### 3.2. Improve backend test coverage and upgrade it to support Python 3
This project aims to improve backend test coverage to 100%, and then migrate the backend codebase to be simultaneously compatible with both Python 2 and Python 3. The reason these two projects are linked is because one prerequisite for a safe migration is to have full test coverage, so it's important to make sure that the backend coverage is 100% before migrating. We would also like to standardize all scripts in the codebase to be written in Python (currently, there is a mixture of bash and Python being used).

Unfortunately, we cannot do a full migration to Python 3 at this time due to incompatibility issues with Google App Engine (GAE) dependencies. So, the current plan is to have the codebase python3 ready, so that we can easily upgrade to python3 as soon as the GAE issues are resolved.
 
**Potential mentors**: **@apb7** (primary), **@brianrodri**

**Difficulty**: Medium

**Knowledge/Skills needed**
* Python
* A good testing mentality
* Bash scripting knowledge.

**Suggested milestones**
1. Improve the coverage of the existing backend code from 89% to 100% (2314 lines missing of 21562 at the time this was written), and put automated checks and guidelines in place to ensure that no untested backend code makes it into the develop branch.
1. Convert all bash scripts to python. Update the codebase to ensure that it is compatible with both Python 2 and Python 3, while ensuring that all setup and deployment scripts continue to work fine. Make sure that all libraries we use are compatible with python 3: if not, suggest mitigation approaches and migrate the libraries accordingly.
1. Put measures in place (like lint checks) to ensure that the backend code always remains compatible with both python 2 and python 3, regardless of subsequent developer changes. Create a list of remaining steps that need to be taken for a final migration to python 3 (once a solution is found for the GAE dependency issues); this list should be as short as possible.

**Related issues**: [#6550](https://github.com/oppia/oppia/issues/6550)

**Notes** 
* See https://docs.python.org/3/howto/pyporting.html for migration instructions.
* Proposals must clearly state a plan for how to achieve the 100% coverage state from our current state.

***

### 3.3. Migrate the frontend to Angular 2
With the announcement that [AngularJS will no longer be maintained or updated](https://blog.angular.io/stable-angularjs-and-long-term-support-7e077635ee9c), we would like to upgrade our frontend to use Angular 2. The migration will need to happen step by step, while maintaining the working state of the codebase. 

**Potential mentors**: **@kevinlee12** (primary), **@bansalnitish**

Difficulty: Hard

**Knowledge/Skills needed**
* AngularJS and Angular2
* Good technical design

**Prerequisites**
This project will only be offered for GSoC if the pre-work to convert the codebase to a migratable state (and update any necessary third-party libraries) is completed before the start of GSoC. This work is tracked in the ["Angular 2 Migration" GitHub project](https://github.com/oppia/oppia/projects/32).

**Suggested milestones**:
1. Upgrade at least 40% of the codebase to Angular 2, including test files. Communicate to developers the changes that are going on, and ensure that documentation exists for them to easily set up an Angular 2 environment and get started with development using Angular 2.
1. Upgrade at least 70% of the codebase to Angular 2, including test files.
1. Upgrade the entire codebase to Angular 2, including test files.

**Notes**:
* Proposals should demonstrate a clear understanding of the upgrade process, and specify a clear plan for tackling this project that can be fully conducted during the GSoC period.
* Proposals should explain the impact of the changes on developers, and how to minimize this.
* Proposals should explain how they intend to measure progress, and how the "40%" and "70%" numbers above can be verified objectively. (Note that the number for Milestone 1 is slightly higher because we expect the easier parts of this project to be completed earlier.)
* See https://angular.io/guide/upgrade for the official upgrade instructions.

***

### 3.4. Upgrade third-party libraries
Some of the third party libraries that Oppia uses have been updated, and migrating to newer versions of these libraries might help fix some issues on the issue tracker. The aim of this project is to upgrade all third-party libraries (carefully!) to the latest stable version. 

**Potential mentors**: **@vojtechjelinek** (primary), **@bansalnitish**

**Knowledge/Skills needed**
* Bash
* Python (to understand the use cases of the library)
* Javascript (to understand the use cases of the library)

**Suggested milestones**
1. Upgrade 70% of the libraries in ./third_party, with no regressions.
1. Upgrade 100% of the libraries in ./third_party, with no regressions.
1. Upgrade Node to the latest stable version and then upgrade all libraries in ../node_modules. Upgrade all libraries in ../oppia_tools.

**Difficulty**: Easy/Medium

Notes:
* An important part of upgrading libraries is to make necessary changes to support the upgraded libraries (in case new versions introduce breaking changes or are not backward-compatible). There are several libraries in ./third_party for which this is more difficult than others. The proposal should explain which libraries these are, and describe a plan to upgrade them safely.
* Note that Milestone 3 comes last because node and ../oppia_tools are not user-facing.
* Proposals should explain how they intend to measure progress, and how the "70%" number in Milestone 1 can be verified objectively.

***

### 3.5. Static serving
Currently, Oppia serves all pages using the Jinja templating engine, which isn't very efficient -- for one thing, because pages are dynamically composed using Jinja, they can’t be cached. The aim of this project is therefore to serve as much of Oppia's pages as we can statically, and handle all dynamic content using AJAX calls. In order to do this, we'll need to get rid of the Jinja footprint in our codebase. Furthermore, we sometimes use Jinja to include static files (like header_js_libs.html or footer.html); and will therefore need to find an alternative way to include these in a Jinja-less environment (perhaps in our build process, or with ngInclude).

**Potential mentors**: **@vojtechjelinek** (primary)

**Difficulty**: Medium

**Knowledge/Skills needed**
* Full-stack development
* Technical design

**Suggested milestones**:
1. Devise a way to serve the [About page](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/pages/about/about.html) or the [Fractions landing page](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/pages/landing/topic_landing_page.html) statically (this requires getting rid of any remaining Jinja constructs on that page), using an approach that is generalizable to other pages. Identify other issues that can arise from serving the remaining pages statically.
1. Convert all mostly-static pages in Oppia, as well as at least one non-static page, to use the new framework developed in Milestone 1.
1. Serve all pages in Oppia statically.

**Related issues**:
* #4220: MusicNotesInput static images are not hash interpolated.
* #2308: Add pre-rendering and other pre improvements to Oppia pages.
* #5002: Remove GLOBALS from HTML
* #5597: Jinja replacement with angular for page title
* #3950: Replace Jinja templates in the frontend with Angular

**Notes**:
* The proposal should include a clear analysis of how to get rid of Jinja for all pages.
* This project may require some changes in the build process, because we currently sometimes use `{% include %}` just to have clearer dev processes. Good proposals will include a coherent analysis of how to deal with this issue, as well as the pros/cons of possible approaches. Some starting-point ideas are provided below, but there may be others:
    * re-build the finalized templates at release time, then serve them statically from then on (rather than try 
to re-construct them at every request). But how would we handle local development, where the changed files must be available immediately?
    * Look into stuff like ngInclude in Angular. But that might lead to too many calls to the server (even if only to retrieve static files). That said, we could cache the templates.
* This project requires the usage of some kind of module bundling (webpack). We hope to have this completed prior to GSoC -- please talk to **@vojtechjelinek** for more details.
* In order to get rid of Jinja, we need to find alternative ways to handle all the GLOBALS variables that are currently sent to the frontend using Jinja. Work on this is currently ongoing at #5002 -- please talk to **@vojtechjelinek** if you’d like to help with this.

***

### 3.6. Validate invariants between data models
We would like to validate that Oppia deployments have valid data and relationships between datastore storage models. Some sample validations include:

* All explorations have correct ExplorationRights objects defined
* All images are linked up with an existing exploration
* All audio files are linked up with an existing exploration
* All explorations in collections have corresponding model instances
* Feedback/Suggestions have corresponding explorations attached to them
* All RTE fields are correctly formatted

The aim of this project is to figure out all the invariants that should hold between Oppia storage models, and put in place an audit job to verify that they hold in a production deployment, as well as put steps in place to ensure that, if the invariants hold at a point in time, they continue to hold in perpetuity.

**Potential mentors**: **@bansalnitish** (primary), **@seanlip**

**Difficulty**: Medium

**Knowledge/Skills needed**
* Python
* Map Reduce jobs
* Good technical design
* Good eye for testing

**Suggested milestones**
1. Update the backend code to ensure that all desired invariants continue to hold in perpetuity, and create an audit job to verify that all desired invariants hold. This audit job should be run in production immediately after Milestone 1 and will produce a list of discrepancies that need to be addressed.
1. Resolve at least half of the discrepancies found during Milestone 1.
1. Resolve all the discrepancies found during Milestone 1.

**Notes**
* The above list is not representative, and we expect there to be many more such validations. The proposal should include a full list of these.
* This project ties in very closely to Oppia's release process. Make sure you are acquainted with [Oppia’s release timeline](https://github.com/oppia/oppia/wiki/Release-Schedule), as well as the [procedure for running one-off jobs in production](https://github.com/oppia/oppia/wiki/Running-jobs-in-production).

***

# Other useful information

## Dates and Deadlines
Noteworthy dates for 2019:
* **Jan 16 - Feb 7**: Mentoring organizations apply
* **Feb 27**: Mentoring organizations are announced
* **Mar 25 - Apr 9**: Student application period
* **May 6**: Accepted students are announced
* **May 6 - May 27**: Community bonding period
* **May 27 - Aug 19**: Students enjoy the summer by contributing code to their projects
* **Aug 26**: GSoC officially ends

## List of Potential Mentors

* Akshay (@aks681)
* Apurv (@apb7)
* Brian (@brianrodri)
* Kevin (@kevinlee12)
* Nithesh (@nithusha21)
* Nitish (@bansalnitish)
* Sandeep (@DubeySandeep)
* Sean (@seanlip)
* Vinita (@vinitamurthi)
* Vojta (@vojtechjelinek)

## Communication

**Chat**

Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](
https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any questions related to getting started. For project-specific questions, please direct your queries to the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).

**Email**

If you have questions pertaining to "how-to-get-started", please ask them on [Gitter](
https://gitter.im/oppia/oppia-chat), or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you.

To discuss your project ideas or share your proposal for feedback from the community, please email the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).