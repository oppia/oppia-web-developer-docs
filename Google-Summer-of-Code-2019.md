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

Oppia is planning to participate in [Google Summer of Code 2019](https://developers.google.com/open-source/gsoc/)! GSoC is a global program which offers post-secondary students an opportunity to discover and work with open source organizations over the course of 3 months, while being paid a stipend. Students work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

You might be interested in our GSoC info pages from previous years: [2018](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018), [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

Also, please note that acceptance into GSoC isn't a prerequisite for [becoming an Oppia contributor](https://github.com/oppia/oppia/wiki). The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out!

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

If you'd like to get a sense of what a proposal might contain, here are some examples of student proposals that we accepted: <To be added> 

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

The following is a list of Oppia's 2019 GSoC project ideas. You are welcome to choose among these ideas, or propose your own! However, if you are proposing something original, it's essential to engage with the Oppia community in order to get feedback and guidance to improve the proposal, as well as to make sure that it fits in with the team's overall plans.

Please note that all mentor assignments are provisional, and that they may change depending on which proposals are eventually accepted.

This year, the Oppia team is offering three types of projects: infrastructure projects, projects that improve the learner experience, and projects that improve the creator experience. Some of the project ideas are annotated with notes and suggestions from the mentors, but please bear in mind that the main purpose of these notes is simply to suggest ideas or possible starting points; they aren't meant to be prescriptive. You'd also be welcome to include discussions of other relevant aspects (that aren't mentioned in the notes) to your proposal. For more information, see: [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan).

1. [Creator Experience Projects](#creator-experience-projects)
     1. Building a Lesson Artist Dashboard
     1. Define and Implement Continuous Real-Time Effectiveness Metric for Explorations 
     1. Translation infrastructure enhancement
     1. Allow exporting an exploration to a linear view for easy review/improvement 
     1. Improvements to the editor flow, including
     1. Allow creation of parameterized questions

1. [Learner View Projects](#learner-view-projects)
    1. Highlight words as audio is played.
    1. Functionality for asking students why they picked a particular answer 
    1. Memorization Experience for Learners
    1. Review tests and improvements to the questions framework

1. [Infrastructure Projects](#infrastructure-projects)
    1. Improve frontend test coverage (to 100%) and optimize e2e test suite
    1. Improve backend test coverage (to 100%) and making sure the codebase follows python 3 syntax, and is ready for migration. 
    1. Upgrade Angular dependencies and migrate to Angular 2
    1. Upgrade third-party libs
    1. Static serving
    1. Validate production data

## "Creator Experience" Projects
### 1.1. Building a Lesson Artist Dashboard
Art and graphics form an integral part of most explorations on Oppia, and is especially important in making lessons learner-friendly. Typically, art is used for illustrative images, decorative images, or images for questions or answers. We have developed a standardized process for creating lessons, and are currently working on creating lessons in relevant subject areas that are as good as possible. However, one major blocker for getting lessons out fast to learners is the lack of designers/artists, and we would like to have a framework that enables artists to contribute to lessons as easily as developers can contribute to GitHub repositories.

The idea behind this project is to enable two things. Firstly, add functionality to have dedicated artists for explorations: this will allow creators to assign artist roles, and allow the art development workflow to happen in parallel with other creative work. Secondly, implement a way to crowdsource these graphics (using the existing suggestions framework). For this, all open image requests should be surfaced to non-editors/artists of the exploration, and they should be allowed to suggest an image. This will be reviewed by the editors/artists, and once approved, can be added to the lesson. 

**Potential mentors**: @nithusha21 (primary)

**Difficulty**: Medium

**Knowledge/Skills needed**
* Good technical design 
* UX design
* Full stack development

**Suggested milestones**
1. Implement an “image placeholder” component in rich-text editor fields for an exploration, and implement a new role for artists that gives them permissions to contribute images to these image placeholders (or replace existing images).
1. Implement a single common view for all explorations that lists all open image requests. The creator of the exploration should be able to flip a setting, which would either enable or disable image placeholders within their exploration to be displayed in the common view. This common view must be accessible to all, and should be easily reachable from the creator/learner dashboards. Suggestions for images would happen through this view.
1. Implement a suggestion-based approach to suggest an image for a placeholder. This will enable all users to contribute an image to the lesson. The suggested images should appear on the feedback tab of the exploration creation page (this is exploration specific, and should not be reachable by all). The artists/editors of the exploration should be able to review the suggestion, and if the image is accepted, the suggested image should be added to the exploration.

***

### 1.2. Real-Time Measurement of Exploration Effectiveness
We want to provide creators meta-analysis for the improvements they make to their explorations. This gives them confidence in following through with our suggested improvements, and allows them to quantitatively understand the effectiveness of their explorations.

**Open Questions**:
* How do we "prove" explorations have improved for learners?
* What kind of data can we collect to argue an exploration has improved?
* Can they be anonymized?
* How will we intuitively show these metrics to creators?

**Potential mentors**: @brianrodri (primary), @kevinlee12

**Difficulty**: Medium

**Knowledge/Skills needed**
* Full stack development
* Python
* Angular JS

**Suggested milestones**
_To be decided_

**Related issues**
* Define and Implement Continuous Real-Time Effectiveness Metric for Explorations (#5801)

**Notes**
* Proposals must:
    * Suggest 2-3 well-defined metrics to be monitored, and why/how they will determine effectiveness.
    * Mock of the directive which shows the metrics.
    * Define all domain objects +tests, services +tests, directives +tests, backend schemas/models + tests which will be implemented.

***

### 1.3. Audio project: Making fully feature audio translation tab.
Currently, Oppia provides a simple platform for translators for recording and tracking audio translations work. This platform mostly covers the managerial part for audio translation like checking audio translation coverage at a single glance for any language, we had few interaction with oppia translators and we found that we improve the platform in many ways to make the translation process easy and simple. We have enlisted few important features which can be integrated to the translation structure:
* Caching/storing recorded audio locally until they are saved.
* Allowing users to upload multiple audio files at a time.
* Allowing multiple translators to work in parallel without losing their draft changes.

**Potential mentors**: @DubeySandeep (primary)

**Difficulty**: Medium

**Knowledge/Skills needed**
* Frontend development
* Good UI/UX design

**Suggested milestones**:
1. In the first milestone, you can work on backend structure to implement “Allowing multiple translators to work in parallel without losing their draft changes.”
1. In the second milestone, try to cover the usability of translation tab, i.e, caching recorded audio so that translator can easily navigate in translation tab without losing any recorded audio. Allowing translators to upload multiple files at a time and automatically (or allowing them to select) locate audio files to the correct place.
1. In the third milestone, you can implement a functionality to allow translators to upload multiple audio files at a time.

***

### 1.4. Creating a “Reviewer View” for Explorations
In order to ensure a high level of quality, explorations are often reviewed by an experienced lesson creator before publication. However, this is currently a somewhat tedious process that requires lots of clicking from one state to another, which can make it difficult for the reviewer to get a sense of the main “flow” of the exploration.

It would be nice to have a more linear, scrollable view of the entire exploration which is optimized for reviewers, and which supports basic commenting functionality. The aim of this project is to build this view.

**Potential mentors**: @1995YogeshSharma (primary), @seanlip

**Difficulty**: Hard

**Knowledge/Skills needed**
* Python and AngularJS
* Good UI/UX design
* Good technical design
* Very good understanding of what an exploration is, and what its various components are

**Suggested milestones**
1. Implement a basic “reviewer’s view” of the exploration in the editor tab. In addition to the “content” section of each card, this view should also include a representation of at least two of the following: interaction, feedback/responses, hints, solution.
1. Fully implement the reviewer’s view. Implement the backend storage for reviewer comments on parts of an exploration (in a way that involves expanding the existing feedback system to allow reference to specific parts of a card, rather than creating a brand-new sibling system from scratch).
1. Implement the frontend system for reviewer comments on parts of an exploration.

**Notes**
* Proposals must include clear mockups or wireframes for how the display would look. A sample exploration converted into linear view as an example would be great!
* Proposals should clearly indicate how each of the components of an exploration would be handled (interaction, hints, solutions, answer groups). Be sure to think about what makes the most sense for the reviewer -- you don’t need to include everything in full detail. For example, the reviewer probably won’t need to see fully-fledged interactions that they can interact with. The user flow for a reviewer should be clearly laid out.
* The proposal should explain how branching explorations would be handled. (Note, though, that explorations are typically fairly linear in nature, with branching used only for reviewing earlier material and/or going back to earlier cards. The reviewers’ view should be optimized for that use case, but there should be some reasonable way to handle non-linear explorations.)
* The view should support comments like Google Docs. Proposals should give examples about what this would look like and how it would work.  

***

### 1.5. Improvements to the Editor Saving Flow
There are a number of serious issues with current workflows in the exploration editor that can occasionally cause loss of work. In particular:

* When an exploration is migrated to a newer schema version, any existing draft changelists should also be updated accordingly. Currently, draft changelists are not updated, resulting in a version mismatch and a loss of work when the exploration creator subsequently tries to apply the draft. (See #4438 for some discussion.)
* When an exploration is updated, any existing suggestions in the feedback tab should be updated accordingly. Currently, such suggestions are not updated, resulting in a version mismatch and a loss of work when the exploration creator subsequently tries to apply the suggestion.
* When changes cannot be saved to an exploration, a “lost changes” modal pops up so that the creator can make a copy of their edits and then reapply them. However, the code for this modal is not robust, and in particular it does not take into account draft changelists that were stored in an older format. Thus, when it tries to display such drafts, it breaks and ends up not showing anything.
* It is difficult to change an interaction into a slightly different one (e.g. from text input to number-with-input) without losing all the associated responses, hints and solutions. It would be nice to declare a suitable transformation that allows this data to be carried over from one interaction type to a closely-related one, and to auto-migrate as much of the responses as possible so that the creator does not lose their work.

The aim of this project is to fix any three of these issues.

**Potential mentors**: @vibhor98 @1995YogeshSharma 

**Difficulty**: Medium

**Knowledge/Skills needed**
* Full stack development including Python and AngularJS
* Good technical design

**Suggested milestones**
Choose three of the issues above, and fix them. Fixing each issue counts as a single milestone.

**Notes**:
If you would like to get a bit more familiar with the exploration editor, here is a simpler issue along the same lines that you might like to have a go at: When switching from a rule type to a different rule type, the inputs to the old rule type get lost, even though both rule types have the same types of inputs and it is possible to carry the inputs over.

***

### 1.6. Allow creation of parameterized questions
With the addition of the questions framework, there is potential to create a large question bank for practice questions. However, it would be tedious for creators to create a large number of questions with similar formats but slight variations (e.g. “Add ⅘ and ¾”, “Add ⅔ and ⅗”, etc.)

Instead, we would like to introduce the concept of parameterized questions, where the creator can specify parameters which can be used to generate many questions at once. (In the example given above, the question might be of the form “Add a/b + c/d”, with parameters a, b, c, d. The question creator would specify ranges of values for the parameters in order to generate questions.)

Note that parameterization might also extend to expressing the same question in different ways. For example, we might want to be able to treat the questions “Add a/b + c/d”, “Find the sum of a/b and c/d”, and “{{name}} has a/b of a cake and {{other_name}} has c/d of the same cake; what is the total amount of cake they have?” as the same.

**Potential mentors**: @aks681, @vinitamurthi

**Difficulty**: Hard

**Knowledge/Skills needed**
* Full stack development
* Good technical design
* Good UX design

**Suggested milestones**
* Make any backend changes that are necessary to allow parameter values / ranges to be stored along with a question, and implement functionality (hidden behind a flag) for specifying these values / ranges in the frontend.
* Implement functionality that allows authors to use parameters in question content and rules.
* Implement functionality to allow creators to audit that the parameterizations they have chosen work well in all cases, and result in sensible questions.

**Notes**
* Good technical judgement is really important for this project, particularly in ensuring that the system that is built is not too complicated. We expect a GSoC project for this idea to cover only a sub-part of what is described in the description above; figuring out a suitable scope for this subproblem (and explaining clearly how it could be extended in the future) is an important part of the proposal.
* The existing parameters/expressions framework might be a useful starting point. Note that there is some existing functionality for parameters in the codebase, but it is not well-maintained. It is probably best to figure out a design for this system from scratch, and only then see whether the existing parameter functionality can fit well into the proposed system.
* There should be a way for creators to audit that the parameterizations they have picked work well in all cases and result in sensible questions. The user flow for doing this should be clearly laid out.
* Proposals should explain clearly how the rules in answer groups will handle parameters without complicating the default lesson creation experience.
* [Stretch] Suggest a way to handle audio translations for parameterized questions.

***

## Learner View Projects
### 2.1. Highlight text in a lesson as audio is played
We have found that audio voiceovers (especially in native languages) are very helpful for learners for whom English is not a first language. However, for longer cards, it is difficult for learners to match the audio voiceover to the text on the card. It would be great for learners to be able to track the audio with the text. 

The aim of this project would be to allow lesson translators and voiceover artists to annotate textual translations and voiceover audio respectively, so that the relevant text can be highlighted in the exploration player while the corresponding audio is playing. A rough requirements doc for this project can be found here.

**Potential mentors**: @DubeySandeep

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

***

### 2.2. Functionality for asking students why they picked a particular answer
We would like to add a feature to the lesson player that allows students to explain how they arrived at a (wrong) answer. The aim of this feature is to encourage reflection on the student’s part, as well as provide (anonymized) information to creators about student misconceptions, so that the creator can improve Oppia’s feedback for future students.

**Potential mentors**: @vibhor98 (primary), @aks681

Difficulty: Medium

**Knowledge/Skills needed**
* Good technical and UI/UX design
* Full stack development

**Suggested milestones**
1. Implement the backend data storage models, domain objects, services and controllers needed for this feature. Note that this feature should be whitelisted to the same set of explorations for which learner playthroughs are whitelisted.
1. Augment the learner view UI to enable learners to fill out responses.
1. Augment the editor view UI to surface these responses to creators, and complete the end-to-end feature so that the complete life-cycle functions correctly. Add e2e tests to verify the overall life-cycle.

**Notes**
* Proposals must clearly state when this information must be recorded. The process should not unduly obstruct the learner -- e.g, it would not be nice to surface a modal with “explain your approach” every time the learner clicks submit. Proposals should also outline when and where this data is surfaced to creators. 
* Proposals must clearly state the complete lifecycle of this feature, starting from the learner’s submission and proceeding all the way to the creator improving the lesson based on that feedback. Be sure to consider “non happy path” flows as well, such as when the student does not provide an explanation that the creator can understand. The proposal should also include mocks for both the learner and creator views.

***

### 2.3. Memorization Experience for Learners
For some topics, attention needs to be given on memorizing data (such as the names of the counting numbers, the times table, the months in a year, or the planets in the solar system). There should be an effective way for learners to do this as needed, in a topic or in an exploration. The creator should be able to specify the information that needs to be memorized, and there should be a built-in mechanism in Oppia that helps the learner commit this information to memory as quickly and accurately as possible.

**Potential mentors**: @seanlip (primary)

**Difficulty**: Medium/Hard. This project is somewhat open-ended. We encourage coming up with a proposal which is reasonable in scope, but which also can be backed by evidence that implementing it would lead to an effective learning experience.

**Knowledge/Skills needed**
* Full stack development
* Good technical design
* Good UX design

**Suggested milestones**
These will depend strongly on the nature of the proposal. In general, we recommend:
1. Make all necessary backend changes for this project, working through the stack, starting from the storage models to the backend controllers.
1. Make all necessary frontend changes for the editor view to enable the creation of such experiences for learners.
1. Make all necessary frontend changes for the learner view to enable them to experience this feature.

**Notes**
* Proposals should define where this experience takes place, and why -- is this a separate experience at the topic level, or is it part of an exploration? The user experience for the student should be a natural one, and be defined in the proposal as clearly as possible.
* The success of this project is based on how effectively it helps students memorize a list of predetermined facts/words. The proposal should explain why the approach chosen is likely to be effective.

***

### 2.5. Review tests and other improvements to the questions framework
While explorations and stories help encourage a learner to continue learning, it is also useful for a learner to be able to keep track of their understanding as the learning progresses. Review tests are an upcoming feature in Oppia that aims to help learners test the skills they’ve learned after they have completed 2-3 lessons in a story in that topic. These review tests would be automatically presented to the learner once they have progressed up to a certain point in the story, and would need to be completed successfully in order to advance to the next part of the story.

This project aims to create the learner view for review tests, and to improve the question framework as a whole so that the experience of practising questions on Oppia (via pre-tests, review tests and practice sessions) is as effective and enjoyable as possible.

**Potential mentors**: @vinitamurti (primary), @aks681

**Difficulty**: Medium

**Knowledge/Skills needed**
* UI/UX design
* Python (backend development)
* Angular JS (frontend development)

**Suggested milestones**
1. Implement the full user flow for review tests. After this milestone, review tests should be presented to students at the right time, making use of the existing question player component. At the end of the review test, there should be a way for the student to return to the story they were on.
1. Update the question player framework to return more information than just the score, once the learner has completed the test. Specifically, the question player framework should be able to return the score, as well as calculate and return the mastery of the skill(s) that were tested. At the end of this milestone, the question player API should return score as well as a list of skills tested along with their mastery levels. Note, the proposal should define  mastery levels as well.
1. Use the skill mastery information returned by the question player API in each of the tests (i.e. pre-tests, practice sessions, and review tests). Each of the tests would have to use the skill mastery levels in different ways. Pre-tests would use mastery to decide whether the learner has passed the requirements and can proceed with the lesson, whereas review tests and practice sessions would use the mastery values primarily to pass on the information to the learner and keep track of their progress.

**Notes**
* Proposals should include user flows for what the review tests experience would look like.
* Proposals should include a clear definition of how to measure the effectiveness of the questions framework.

***

## Infrastructure Projects

# Other useful information

## Dates and Deadlines
Noteworthy dates for 2019:
* **Jan 16 - Feb 7**: Mentoring organizations apply
* **Feb 27**: Mentoring organizations are announced
* **Mar 25 - Apr 9**: Student application period
* **May 6**: Accepted students are announced
* **May 6 - May 27**: Community bonding period
* **May 27 - Aug 19**: Students enjoy the summer by contributing code to their projects
* **Aug 26*: GSoC officially ends

## List of Mentors

## Communication

**Chat**

Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](
https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any questions related to getting started. For project-specific questions, please direct your queries to the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).

**Email**

If you have questions pertaining to "how-to-get-started", please ask them on [Gitter](
https://gitter.im/oppia/oppia-chat), or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you.

To discuss your project ideas or share your proposal for feedback from the community, please email the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).