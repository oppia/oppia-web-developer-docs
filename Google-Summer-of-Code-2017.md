Oppia is excited to be participating in [Google Summer of Code 2017](https://developers.google.com/open-source/gsoc/)! GSoC is a global program which offers post-secondary students an opportunity to discover and work with open source organizations over the course of 3 months and be paid a stipend. Students work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

(NB: acceptance into GSoC is not a prerequisite for [becoming an Oppia contributor](https://github.com/oppia/oppia/wiki). The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out!)

The following are Oppia's 2017 GSoC project ideas:

* [Self-service playtesting](#self-service-playtesting)
* [Improving the feedback flow](#improving-the-feedback-flow)
* [Applying machine learning to the code interaction](#applying-machine-learning-to-the-code-interaction)
* [Learner dashboard](#learner-dashboard)
* [Replace fallbacks with hints](#replace-fallbacks-with-hints)
* [Translation console](#translation-console)
* [New question types](#new-question-types)
* [Code interaction with test suites](#code-interaction-with-test-suites)
* [Sitewide ACL refactor](#site-wide-acl-refactor)
* [Achievement system](#achievement-system)

For more information on the projects that were completed in GSoC 2017, please see the [official GSoC page](https://summerofcode.withgoogle.com/organizations/4875267966238720/) for the Oppia Foundation.

# Students
GSoC is an excellent opportunity for students to get paid to work on an open source project. If you're interested in applying as a student, you should definitely read the following resources:

- [Google Summer of Code student guide](http://write.flossmanuals.net/gsocstudentguide/what-is-google-summer-of-code/)
- [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
- [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)

## Getting started

If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC.

1. Get a better understanding of what Oppia is all about by taking a look at our [user documentation](http://oppia.github.io/#/) -- this will help you become familiar with important concepts like explorations and interactions. We'd also recommend having a go at playing/creating lessons on [Oppia.org](https://www.oppia.org), which hosts a live instance of Oppia.

1. Read and follow the instructions in the [contributors' guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), including signing the CLA and setting up a local development instance. Also, please read the [Oppia codebase overview](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase) and the [coding style guide](https://github.com/oppia/oppia/wiki/Coding-style-guide).

1. Work on one or more [starter issues](https://github.com/oppia/oppia/issues?q=is%3Aopen+label%3A%22TODO%3A+code%22+milestone%3A%22Recommended+projects%22) in order to become familiar with the contribution process. This will help us get an idea of what it's like to work with you -- e.g. how independent, resourceful, responsive, etc. you are. It will also help you get a better understanding of the codebase, so that you can write a good, detailed project proposal.
  - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to follow the [dev workflow](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#instructions-for-making-a-code-change) carefully, manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide), and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

1. When you've done enough starter projects to get a good understanding for the "lay of the land", select one or more GSoC projects that you're most interested in from the list below (or propose your own), and write your project proposal! If you have any questions about a project, feel free to ask on [Gitter](https://gitter.im/oppia/oppia-chat) or email the [mentors' mailing list](mailto:oppia-gsoc-mentors-17@googlegroups.com). Please be specific when asking questions, since this makes it easier for us to help you.

## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: Familiarity with AngularJS (v1), Python, and Google App Engine is useful and recommended for most Oppia work. In addition, UI design skills are useful for frontend, user-facing work. Please see the individual project ideas to determine whether these skills are recommended for the project in question.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other students, successfully contributing patches, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: GSoC is intended to be a full-time commitment, so the main concern is whether you can still get the project done on time. Be upfront about your other commitments and make sure you schedule your time accordingly when creating your proposal. Other commitments you should list include time where you'll be in school and will commit less time to GSoC, time you will be travelling and away from GSoC work, any summer jobs you need to commit to etc. We will try to be flexible around other time commitments, as long as we are convinced by your proposal that you will have enough time to complete the project by the end of the summer. On the other hand, if you do not disclose other commitments, and it turns out you are unable to commit to what you wrote on your proposal, this is grounds for failing the program.

## GSoC Proposal Template
When proposing a project, please use the following template:

**Project Details**
- Project name
- Why are you interested in working with Oppia?
- What interests you about this project? Why is it worth doing?
- Prior experience (especially with regards to technical skills that are needed for the project)
- Links to 1-5 PRs you've made that showcase your best work, especially any Oppia ones. The list should include at least one Oppia PR, but you can also include some other PRs from major open-source projects if you like.
- Project plan and implementation strategy.

**Summer Plans**
- Which timezone(s) will you primarily be in during the summer?
- How much time will you be able to commit to this project?
- What jobs, summer classes, and other obligations might you need to work around? Please be upfront about any existing commitments you may have.

**Communication**
- What is your contact information, and preferred method of communication?
- How often do you plan on communicating with your mentor?

### Notes on the project plan

The project plan is the most important section of the proposal, since it outlines what you'll be doing during the summer. Here's some guidance on what the mentors and organization admins will be looking for in this section:

- **Three clear milestones** explaining the deliverables to be achieved by the end of each of the three GSoC coding periods. Strong proposals will have clear, concrete and well-defined milestones, whose success can be readily evaluated by an external observer. It's OK to break up a milestone into smaller milestones over smaller timescales, but individual milestones should represent *concrete* deliverables that can be merged into the "develop" branch. Please try to be realistic when setting milestones, and don't over-promise.

- **A technical design and implementation plan**. The project ideas below are annotated with some notes from the mentors, but please bear in mind that these notes are not exclusive and shouldn't serve as a substitute for thinking carefully and critically about the project from first principles -- their main purpose is to suggest ideas or possible starting points. If, in your thinking, you find aspects not mentioned in the notes, feel free to include a discussion of these aspects in your proposal. (For example, certain projects may require a migration of existing production data, and this needs to be accounted for in the project plan.) Strong proposals will demonstrate familiarity with the codebase, a realistic implementation plan, and attention to detail.

- **Mocks or wireframes**, if appropriate. For user-facing projects, we strongly favour proposals that demonstrate an empathy for the user. If you're proposing frontend design mocks, we suggest showing your ideas to your friends and getting their critical feedback, so that you can be confident that others find them intuitive as well. Note that you do not need to make your mocks pixel-perfect, but they should illustrate the primary user journeys clearly enough for us to understand exactly what you're proposing. Also, bear in mind that more is not necessarily better -- an important aspect of user-focused design is deciding what _not_ to do.

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
- The quality of the applicant's previously-submitted PRs (in order to assess their ability to code, debug, break down complex tasks, etc.). Note that quantity in itself isn't a prerequisite, though contributors who've submitted multiple PRs are likely to have had more opportunities to demonstrate the abilities needed to succeed in GSoC.
- Our prior experience working with the student (e.g. do they keep commitments, communicate well, demonstrate independence/initiative/responsiveness, help others, etc.)

We believe that strong performance in these dimensions is likely to correlate well with the student having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the GSoC program.

For the proposal, we generally look for a clear indication that the student has a good, deep understanding of the project, and has broken down the project sufficiently well, in a way that makes it very likely to succeed. Some indicators that could help with this include:
- A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating a simple, intuitive experience for end users.
- A concrete, specific breakdown of the work to be done for each milestone. Here's an [example](https://docs.google.com/document/d/1vuwXvHOYXqfM2S2B2KIWhZrAa1PL59wJRUYsqJEd67E/edit#heading=h.ci6rc1u061yj) from a previous design doc. (Note that, in this example, the author has carefully considered and listed which tests need to be written alongside the code; this is a positive indicator.)
- Sufficient concreteness (e.g. references to particular files and methods) to demonstrate that the applicant is familiar with both the scope of the problem and the existing codebase.
- A description, if applicable, of how the applicant plans to mitigate risks that could potentially derail the project.
- Clear, unambiguous communication. (This is important; your proposal will be read by many mentors!)

# Oppia's Project Ideas

This year, the Oppia team aims to create a cohesive set of lessons on basic mathematics, and run pilots with students in developing countries (such as rural India and parts of Africa) who lack access to teachers and textbooks, but who do have mobile devices (albeit with limited bandwidth). We really want the students to enjoy the learning experience, and we also want these lessons to improve continuously based on student feedback. Thus, the team's technical priorities for 2017 include improving the core learner experience, and building in feedback loops that make it easy for lessons to become better over time.

We believe that the following project ideas will have significant impact on Oppia, and would make excellent Google Summer of Code projects. That said, feel free to suggest your own projects -- we'd be happy to discuss new ideas that you'd like to implement!

## Self-service playtesting

**Aim:** In order to help creators improve their lessons, we depend heavily on student playtests and feedback. However, exploration playtesting currently happens via an external form (see instructions on this [wiki page](https://github.com/oppia/oppia/wiki/Playtesting-explorations)), and the overall experience is pretty clunky. The aim of this project is to seamlessly integrate playtesting within the site, so that students and teachers who want to give more detailed feedback on an exploration can do so in a structured way.

**Skills/knowledge required**:
- UX design
- Full-stack development
- Finding a concrete solution to an ambiguous problem

**Difficulty**: Medium

**Suggested milestones**:

1. Complete a full, implementation-ready spec that includes mocks, corner cases and tests. Implement all the necessary datastore and backend logic.

1. Implement and launch the playtesting frontend. At least three user playtests should have been completed using the new system.

1. Implement and launch functionality for showing the playtest data to the exploration authors, so that they can use it to improve the exploration. Gather feedback from exploration authors and make further improvements as needed.

**Notes**:
- How can we make it easy for students to start the process of playtesting an exploration? One avenue might be the learner dashboard, but perhaps there should also be an in-exploration way to do this (or a good argument for why not).
- Would it be possible to get feedback from students who do not complete an exploration? In any case, we should make it easy for learners to report that they're stuck or feeling lost on a particular card (and explain why).
- Here are some ideas for other things that might be worth considering. Note that these are just ideas; they should be evaluated based on how useful the data would be to the exploration authors versus how much of an additional burden they impose on the playtester. Feel free to incorporate other ideas of your own that are not listed here, too.
  - At the outset, perhaps we could ask the user for the context in which they're playtesting this (e.g., are they a teacher, or are they part of a classroom working with the Oppia team, or did they randomly stumble across the exploration while browsing the site), since doing so might provide useful information for exploration authors. 
  - Perhaps we could give students the opportunity to link to a "Let's play" video of their experience on YouTube.
  - Perhaps we could track additional statistics of explorations played under playtesting (e.g. the number of times the playtester submitted an answer to a particular card, or the amount of time spent at each card) and include that alongside the playtest report.

A good proposal should discuss these issues and describe an appropriate UX. It's important to pay attention to details of the playtester’s critical user journey, as well as to think through exactly what information would be useful for the exploration author, and be very concrete about what you intend to do. Privacy considerations should also be taken into account.


## Improving the feedback flow

**Aim:** Currently, learners can provide exploration authors with free-form feedback through the site, or via dedicated playtesting of lessons. We want to make it easy for this feedback to get integrated back into the lesson. A possible way to do this is to have a page that surfaces such feedback for all featured explorations, so that any logged-in user can take a piece of free-form feedback and turn it into a suggested edit for that exploration that the original author can subsequently approve/reject (similar to how a GitHub user can take an issue and turn it into a PR). The aim of this project is to build this page.

**Skills/knowledge required**:
- UX design
- UI design
- Full-stack development
- Technical design

**Difficulty**: Hard

**Suggested milestones**:

1. Generalize the existing suggestions functionality to enable logged-in users to also suggest edits to the RTE content in answer groups and fallbacks.

1. Design and implement a new page that lists unresolved learner feedback for explorations that are featured on the site. (It’s fine if it's read-only at this stage, as long as the necessary information is displayed.)

1. Add functionality enabling any logged-in user to take a piece of feedback on this page, and address it by creating a suggested edit to the corresponding exploration.

**Notes**:
- Currently, logged-in users can only make suggestions to the "content" parts of a state. We need to make it possible for them to make suggestions to the free-form text that the author includes in the "answer group feedback" and "fallback" sections, too, and find a clean way to expose this in the exploration player UI.
- It might be a good idea to use this mainly for community-editable explorations at the outset, since those don't currently have an assigned owner.
- It might be helpful to think of the existing "feedback" functionality as analogous to GitHub issues, and the existing "suggestions" functionality as analogous to GitHub PRs.


## Applying machine learning to the code interaction

**Aim:** We want to give students useful feedback when they get stuck. For this, we need to understand the answers they submit -- e.g., in coding problems, we'd like to understand when the user incorrectly initializes a variable, or makes some other common mistake, so that we can address it. Currently, we are working on building an extensible machine learning framework and a training interface for classifying free-form answers. The proposed code classifier for this project will be built on top of this framework, and would allow learners to type in code in order to match some sort of output, avoid an error, or match specific code. The project itself involves figuring out a way to cluster similar pieces of code, and then using that to train a classification model that can predict which feedback cluster ("answer group") a new piece of code should belong to. Lesson creators will then be able to create a training set and assign responses to a set of similar code submissions using the training interface. 

**Skills/knowledge required**:
- Machine learning
- Back-end development

**Difficulty**: Hard

**Suggested milestones (rough outline)**:

1. Implement all necessary updates to existing datastore (if any), any necessary backend logic changes, and any changes required for the training interface. Build/generate a dataset for training the classifier, do any necessary data processing, and fully integrate and test any specific library that needs to be used in the project.
2. Build the model using the training data, and implement end-to-end tests. Evaluate the model on the test data using cross validation and, if possible, do a [spot-check](http://machinelearningmastery.com/why-you-should-be-spot-checking-algorithms-on-your-machine-learning-problems/). Check the performance of the model against a baseline (typically using another classification algorithm).
3. Improve the speed and accuracy of the model to the point where the classification functionality is sufficiently good and can be released to end users. Document the different approaches tried and the speed/accuracy achieved with each. Deploy the new model in production.

**Notes**:
- We will be looking carefully at the technical design section of the proposal in order to evaluate the feasibility of the proposed approach. A strong proposal will demonstrate a good understanding of Oppia’s existing classification system, and clearly explain how the proposed classifier will interface with it.
- If code evaluation is needed, this should happen in the frontend (although the results and the learner's code will be stored in the backend). For security reasons, we can't execute arbitrary Python scripts in the backend. 
- The proposal should discuss an effective strategy to build/generate datasets for training the classifier.
- The classification algorithm used should be pluggable into the existing classification framework (so that it's easy to upgrade the algorithm in the future, if needed).
- The exact milestones for this project would depend somewhat on the technical approach used; the ones above are meant only as suggestions. The proposer should feel free to use alternate milestones that lead to a production deployment by the end of the third milestone, but please ensure that each milestone is very concrete and that it can be delivered by the end of the corresponding month of GSoC. If your milestones significantly deviate from the ones above, we encourage you to get feedback from the mentoring team before submitting your proposal.
- For reference, it might be worth looking at the [GitHub project page](https://github.com/oppia/oppia/projects/4), which contains a list of open issues and a link to the design document for the existing machine learning framework. 


## Learner dashboard

**Aim:** In order to learn effectively, learners should be able to keep track of what they've learned and what they’re in the middle of. The aim of this project is to create a place on the site where learners can keep track of the lessons they’ve done, the lessons they’ve partially completed, the list of creators they are subscribed to, and any feedback threads they need to read or respond to.

**Skills/knowledge required**:
- UX design
- UI design
- Full-stack development (mostly frontend)

**Difficulty**: Medium

**Suggested milestones**:

1. Implement progress tracking for lessons. Complete and launch a basic "learner dashboard" page, including functionality for:
  - keeping track of completed and partially-completed lessons (both explorations and collections)
  - keeping track of subscriptions
2. Conduct user studies for the version of the dashboard implemented in milestone 1. Add functionality for keeping track of feedback threads that need a reply from the student, and make it possible for the student to reply to these threads from their learner dashboard.
3. Based on the results of the user studies conducted in milestone 2, implement a further project of your choice. (For example, you could show recommendations for lessons to playtest, or new lessons that would be useful for the student, or new creators that they might want to subscribe to -- or perhaps add functionality for bookmarking explorations that the student wants to play next, but doesn't have the time to at the moment.)

**Notes**:
- For milestone 2, note that the app currently behaves as follows: students can submit feedback to explorations, and exploration authors can respond to this feedback (e.g., by asking a question of clarification). However, at present, there is no way for the student to reply to this thread.
- Proposals should address how a learner gets to their dashboard, as well as any general site changes that might be needed. It’s important to think holistically about the learner user journey and ensure that it's as intuitive as possible, whilst keeping in mind that learners can also be creators.
- Proposals should also suggest a suitable design/layout for the dashboard. It's important that this design is intuitive, and easy for a learner to understand. The implementation of the dashboard should also follow good accessibility practices (e.g., it should support students who use screen readers).
- Currently, a logged-in user is taken to the creator dashboard by default, which serves as their "logged-in homepage". One could argue that the learner dashboard should play this role for a user who comes to the site mainly to learn. How should we reconcile these factors into a coherent user experience?


## Replace fallbacks with hints

**Aim:** In order to help learners successfully complete lessons, exploration creators can specify "fallbacks", which provide a particular piece of feedback if the student is stuck on a particular card for too long. However, these fallbacks can sometimes cause students to receive hints or full solutions when they're not yet ready for them. We want to replace this with a student-initiated hint system instead, so that the student has control over when they receive a hint. In addition, we want to make it compulsory for creators to specify, in each card, at least a final hint that explains how to solve the problem and helps the learner progress to the next part of the lesson, so that they don't get completely stuck midway through the exploration.

**Skills/knowledge required**:
- Strong technical design skills
- Full-stack development

**Difficulty**: Medium

**Suggested milestones**:

1. Finalize full technical plan (including UI mocks) explaining how the fallbacks-to-hints recharacterization will be carried out. Implement any necessary datastore and backend logic changes, as well as all necessary migrations.
2. Implement any necessary UI changes. Iterate on the UI until we have evidence (from user testing) that students find the hints functionality intuitive, and that creators are aware that they need to specify hints and find it easy to do so. Complete and launch the frontend.
3. Based on the feedback gathered in milestone 2, find other ways to help or encourage learners to complete the explorations they start, and implement at least one of these.

**Notes**:
- Proposals should give a very concrete description of how hints will work (e.g. what is the trigger for when they’re displayed), and what the frontend UI/UX for the learner will look like. (We suggest taking a look at how your favourite puzzle games handle this sort of thing; you might find some inspiration there!) Proposals should also explain clearly how exploration creators will specify hints, with an eye towards making it as convenient as possible for them to do so.
- Stronger proposals will discuss multiple possible approaches, make reasoned arguments for and against them, and use these to come up with an informed decision.
- Proposals should give some ideas for possible projects in milestone 3.


## Translation console

**Aim:** We want good lessons to be easily translatable into other languages, so that they're accessible to students whose first language is not necessarily English. The aim of this project is to make it as easy as possible for contributors to take an existing exploration, and translate it to another language.

**Skills/knowledge required**:
- UX design
- UI design
- Technical design
- Full-stack development

**Difficulty**: Hard

**Suggested milestones**:

1. Full spec with mocks, corner cases and tests thought out. Implement any necessary datastore + backend logic changes, and perform any necessary migrations.
2. Complete and launch the frontend. At least one exploration should have been translated by a user (possibly you, but ideally someone else) using the new system.
3. Add a tab in the exploration editor that shows creators of translated explorations any updates that happened to the original exploration since it was last translated, as well as a diff of the change. Make it easy for creators to use this information to bring their translated exploration up to date.

**Notes**:
- Although the default UX should be as convenient as possible for the author, the newly-created exploration should not be publishable until all translations are completed. The newly-created exploration should also be structurally similar to the old one, otherwise we might end up with "translated" explorations that aren't really related to each other.
- In the backend, we should keep track of what exploration has been translated from what, since this is useful for, e.g., maintaining a list of explorations that have been "derived" from a given one.
- Some major design questions:
  - Should we go with a side-by-side view (of original + translation), or inline "annotations" for translators?
  - What if students study in English, but need different (more local) examples, or a different currency unit?
  - Would it actually be better for explorations to contain more than one language? For example, students in Tanzania learn in Swahili in primary school, but in English in secondary school. If we translate all the lessons to Swahili, they are likely to still struggle with the English versions of the lessons. However, if the derived lessons displayed mainly in English with Swahili available on-demand (by tapping words/phrases/cards), this would give the student practice reading and answering questions in English, and referring to the Swahili only when they need to.

A good proposal should discuss these issues, note arguments for and against different approaches, make an informed decision, and describe an appropriate UX. It's important to pay attention to details of the translator's and learner's critical user journeys.


## New question types

**Aim:** This year, one of Oppia's main aims is to create a really good set of basic mathematics lessons. The aim of this project is to create some of the new question types (called "interactions" in the Oppia codebase) that are required for these lessons, as well as to implement a few other commonly-requested interactions.

**Skills/knowledge required**:
- UI design
- Full-stack development (mostly frontend)

**Difficulty**: Medium

**Suggested milestones**:

1. Implement [existing designs](https://docs.google.com/document/d/1g5OgnYjNQ0qgQvmHSX_ivujxHU2ERGSnav7VzkseBBw/edit#) (by Prasanna) for the (a) fractions interaction, (b) the number-with-units interaction.
2. Spec out, design and implement a new interaction for drag/drop matching of items in two lists.
3. Spec out, design and implement a new interaction for entering answers in the form of ordered lists. Note that this may entail some refactoring of the core interactions framework, since some questions may require lists of strings, others may require lists of numbers, and yet others may require lists of music notes (for example).

**Notes**:
- Proposals should demonstrate familiarity with Oppia’s interactions framework, and outline the full backend specification, rules, frontend designs, and examples of use for each of the interactions. Note that coming up with a good backend specification is not easy, and some technical judgment will likely be required.
- All interactions need to work on both desktop and mobile devices.
- The third milestone is not easy. We suggest getting early feedback from the mentoring team on your technical proposal.

## Code interaction with test suites

**Aim:** Oppia currently has two coding interactions, but they are somewhat limited, and pass on a large chunk of the work to the exploration creator. We would like to improve the existing coding interaction by extending it to include functionality for the creator to specify unit test suites, and using the "signature" of the test results to provide feedback to the student.

As a stretch goal, we would also like to make it easier for the coding interaction to automatically detect and respond to things like syntax errors, so that the exploration creator does not have to manually specify rules to catch every possible error. (This may intersect with the machine learning system that is currently being developed for answer classification.)

**Skills/knowledge required**:
- UI design
- Technical design
- Full-stack development (mostly frontend)

**Difficulty**: Hard

**Suggested milestones**:

1. Finish the spec for the revised coding interaction; this should include a complete backend specification, frontend design, examples of use and tests. Ask creators for feedback on the spec, and what additional features they would like in the code interaction. Create some initial prototypes and try these out with users.
2. Fully implement and launch the new coding interaction. At least one exploration should make use of this interaction in a non-trivial way.
3. Conduct a further project of your choice based on exploration creators' feedback. This may be the stretch goal mentioned above, or something else.

**Notes**:
- The proposal should include at least one idea for the project in the 3rd milestone.
- For the frontend, the most important part to explain is how to present the interface for the creators. E.g., how should creators specify test cases? Can they do so in addition to matching parts of the code?
- Should learners be able to see the test cases that their code failed on?

## Site-wide ACL refactor

**Aim:** The current ACLs in Oppia were written for an older version of the site with slightly different aims, and the needs of the project have changed over time. We have recently come up with a new, simplified structure for site permissions, which is detailed in this [document](https://docs.google.com/document/d/1-JsPVIr1u4LQxpTBFi-VSUpbuIoF8CxgzN9ExCKlyYs/edit#heading=h.qj2574amxs00). The aim of this project is to devise a safe way to implement this, and bring the site up-to-date with the new ACLs.

**Skills/knowledge required**:
- Technical design
- Backend development

**Difficulty**: Medium/Hard

**Suggested milestones**:

1. Finish the technical spec for the new permissions system, including:
  - New domain objects and services being introduced
  - New storage models needed
  - New tests that need to be added
  - A list of all permissions that need to be added
  - A plan for migrating the current system to the new one, including any testing that needs to be done to ensure nothing breaks.

  Implement the new storage layer, domain objects, services, and tests.

2. Perform an audit on all existing rights and permissions to ensure there are adequate tests covering each one to prevent regressions. Begin migrating permissions over to the new system, focusing only on new permissions that need to be added (not replacing the current ``rights_manager`` and tests).
3. Migrate all permissions associated with ``rights_manager`` over to the new system, removing the old code once the migration is complete. Ensure all the old ``rights_manager`` tests are included in the tests for the new system.

**Notes**:
- It's important for the proposal to be explicit on which permissions are being added and how they will be tested to ensure no behavior regressions happen. A regression in this area of code can result in serious security and privacy problems. The student needs to convince their mentor that the student's approach will prevent security and privacy vulnerabilities from being introduced.
- The student is responsible for designing the system that will replace ``rights_manager``, but we've already decided from a technical perspective that we're changing the way rights works from being pseudo-role-based to being action-based, where permissions grant allowance of certain actions and are inherited by roles. For example, rather than explicitly checking the config whitelist to determine if a user can access the collection editor, the code should ask the new permissions system whether the user has permission to 'access_collection_editor', where some other place in code populates the permission value by checking the whitelist. This indirection offers a lot more flexibility and leads to code being more readable both in production code and in tests.
- The student is responsible for using the [ACL document](https://docs.google.com/document/d/1-JsPVIr1u4LQxpTBFi-VSUpbuIoF8CxgzN9ExCKlyYs/edit#heading=h.qj2574amxs00) above and their own analysis to derive the list of permissions based on primary user actions. Only backend permissions are needed here, and we want to implement a system to last into the future (with roles and groups, where groups can inherit from other groups). However, the current application of this system needs to satisfy the ACL document wherein roles 'cascade' their permissions currently -- i.e., 'logged in users' receive all permissions guests are allowed, collection editor users inherit all from the 'logged in users' group, etc.


## Achievement system

**Aim:** We want to encourage learners and creators to contribute to the community in ways that matter, such as by playtesting explorations or resolving student feedback. Oppia has a nice new profile page which could contain achievements like badges, but no current system in place to award such achievements.

**Skills/knowledge required**:
- UX design
- Visual design
- Full-stack development
- Technical design

**Difficulty**: Hard

**Suggested milestones**:

1. Finish the spec for the end-to-end badge system, including mocks for each achievement and for UI changes to the profile page. Implement the backend storage, domain objects, services and tests for badges.
2. Implement the profile backend controller, the frontend badge system (including any new frontend domain objects, services, tests, and backend API services), and the frontend profile page to support badges. Implement the visual indicator that appears in real time when a user earns a new badge due to an action they perform, and the backend system for detecting when a user has earned a new badge. Use the above to implement and launch the end-to-end experience for 1 real badge.
3. Implement any new storage models or jobs needed among all badges, and update the badge award system to send an email to the user when they earn a badge offline. Implement the remaining badges using the system created in the previous milestones.

**Notes**:
- The student's proposal should:
  - Clarify the concept of an achievement (within the context of Oppia).
  - Describe which key user actions are worth receiving achievements, the criteria for unlocking each achievement, and an indication of how achievements are tiered.
  - Define the new domain layer for badges (domain objects and services, and also tests), as well as the storage layer needed for badges.
  - Define the general system for detecting when a new badge has been earned. For example, should this be a deferred job, or something computed in real-time?
  - For each badge, identify:
    - The statistics that need to be recorded for that badge
    - Jobs that need to be written or reused in order to collect those statistics
- Note that when a user earns a badge due to an action they did, the notification should appear in the UI in real time. However, when a user earns a badge due to an action that someone else did, they should receive an email.
- The student should work with the UI/UX team to design icons for each badge.

# Other useful information

## Dates and Deadlines
Noteworthy dates for 2017:
- **Jan 19 - Feb 9**: Mentoring organizations apply
- **Feb 27**: Mentoring organizations are announced
- **Mar 20 - Apr 3**: Student application period
- **May 1**: Accepted students announced
- **May 1 - May 30**: Community bonding period
- **May 30 - Aug 29**: Students enjoy the summer by contributing code to their projects
- **Sep 6**: GSoC officially ends

## List of Mentors

The following individuals will be serving as mentors during GSoC 2017:
- Allan Zhou (@AllanYangZhou)
- Anmol Shukla (@anmolshkl)
- Jared Silver (@jaredsilver)
- Joshua Cano (@joshuacano)
- Kevin Lee (@kevinlee12)
- Rachel Chen (@rachelwchen)
- Sean Lip (@seanlip)
- Tony Jiang (@tjiang11)
- Xinyu Wu (@wxyxinyu)

We would also like to thank Kristin Anthony (@anthkris) and Mark Halpin (@markhalpin) for their help in reviewing proposals for GSoC 2017.

## Communication

**Chat**

Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](
https://gitter.im/oppia/oppia-chat#)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it.

**Email**

If you have questions, please ask them on Gitter, or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you.

If you want your question to be read only by the mentors, you can instead send it to the Oppia GSoC mentors mailing list at oppia-gsoc-mentors-17@googlegroups.com. However, note that open communication means that more people are likely to be able to help you (and is more in line with the spirit of an open source project), and you can also get feedback from the community at large. For similar reasons, we recommend not pinging individual mentors personally -- it's better to use the GSoC mentors mailing list.