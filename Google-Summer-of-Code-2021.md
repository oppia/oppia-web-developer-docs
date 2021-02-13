## Table of Contents
* [Getting started](#getting-started)
* [FAQs](#faqs)
* [GSoC Proposal Template](#gsoc-proposal-template)
  * [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan)
  * [What should applicants expect from mentors in a proposal review?](#what-should-applicants-expect-from-mentors-in-a-proposal-review)
  * [Sample proposals from past years](#sample-proposals-from-past-years)
* [Types of work related to Oppia projects](#types-of-work-related-to-oppia-projects)
* [Selection Criteria](#selection-criteria)
* [Oppia's Project Ideas List](#oppias-project-ideas-list)
* [Other useful information](#other-useful-information)
    * [Dates and Deadlines](#dates-and-deadlines)
    * [List of Mentors](#list-of-mentors)
    * [Communication](#communication)


Oppia has applied to participate in [Google Summer of Code 2021](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers post-secondary students an opportunity to discover and work with open source organizations over the course of 3 months, while being paid a stipend. Students work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

You might be interested in our GSoC info pages from previous years: [2020](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020),  [2019](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2019), [2018](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018), [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions [here](https://github.com/oppia/oppia/wiki).

# Students
GSoC is an excellent opportunity for students to get paid to work on an open source project. If you're interested in applying as a student, you should definitely read the following resources:

* [Google Summer of Code student guide](https://google.github.io/gsocguides/student/)
* [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
* [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)

## Getting started

If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. If you like, you can also sign up to the [oppia-gsoc-discuss@](https://groups.google.com/forum/#!forum/oppia-gsoc-discuss) mailing list to participate in general discussion related to Oppia's involvement in GSoC (see point 6 below, too). Make sure to set your preferences correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is all about by taking a look at our [user documentation](http://oppia.github.io/#/) -- this will help you become familiar with important concepts like explorations and interactions. We also recommend having a go at playing lessons on [Oppia.org](https://www.oppia.org/splash), which hosts a live instance of Oppia.

3. Read and follow the instructions in the [contributors' guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) carefully.

4. Consider taking up one or more starter projects in order to become familiar with the contribution process. This will help us get an idea of what it's like to work with you -- e.g. how independent, resourceful, responsive, etc. you are. It will also help you get a better understanding of the codebase, so that you can write a good, detailed project proposal.
    - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to follow the [dev workflow](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#instructions-for-making-a-code-change) carefully, manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide), and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Once you've merged at least 2 pull requests, you will get an invitation to become a collaborator to the Oppia repository and be officially onboarded! **This step is a prerequisite** to applying for GSoC.

6. Now, you can select one or more GSoC projects that you're most interested in, and write your project proposal! We strongly encourage you to discuss your project ideas and share your proposal with the community, so that you can get feedback and ensure that what you're writing makes sense to others. The best way to do this is to put your proposal into a collaborative editing tool like Google Docs, allow others to comment on it, and share a link to it on the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com). You can also email this mailing list if you have any questions about a project, or would like to discuss your approach with the Oppia community and get feedback. Please be specific when asking questions, since this makes it easier for us to help you.
   * **Important note:** Please read [this oppia-gsoc-discuss@ thread](https://groups.google.com/forum/#!topic/oppia-gsoc-discuss/S6Ge3vQ3cuc) carefully for details about the recommended review process. Note that you do not need to write the entire proposal before getting your first review -- see the instructions in that thread for more details. Thanks!

## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: Familiarity with AngularJS (v1), Angular8, Python 2.7 and Google App Engine is useful and recommended for most Oppia work. In addition, UI design skills are useful for frontend, user-facing work. Please see the individual project ideas to determine whether these skills are recommended for the project in question.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other students, successfully contributing patches, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: This year, GSoC is going to be slightly different. The program has been restructured in way that allow students to take some time off for any other commitments (such as exams etc) [(View the timeline here)](https://developers.google.com/open-source/gsoc/timeline). Oppia will respect the same timelines as given by GSoC, the main concern is whether you can still get the project done on time. Be upfront about your other commitments and make sure you schedule your time accordingly when creating your proposal. Other commitments you should list include time when you'll be in school and will commit less time to GSoC, time when you'll be travelling and away from GSoC work, any summer jobs you need to commit to, etc. We will try to be flexible around other time commitments, as long as your proposal convinces us that you will have enough time to complete the project by the end of the summer. On the other hand, if you do not disclose other commitments, and it turns out that you are unable to commit to what you wrote on your proposal, this is grounds for failing the program.

**Q: Which projects are most important for Oppia?**

A: All the projects we've listed here are important, and we'd be very happy to see good progress made on any of them! Projects are treated as equally important during selection. Note that the relative importance of a project to Oppia is not part of the [selection criteria](#selection-criteria). We would encourage you to pick a project that you would enjoy doing over the summer.

**Q: Can I submit more than one proposal to Oppia?**

A: Yes you can. However, we strongly recommend picking one project and writing a solid proposal for it. Splitting attention across multiple projects might not be a great idea. 

**Q: How early should I start working on the proposal?**

A: As early as possible. Make sure to get feedback from mentors before finally submitting the proposal. This will help you to write a better proposal as you can refine the details based on the feedback you receive. The mentors would need some time to review, and hence it is a good idea to begin as early as possible.

**Q: I only discovered this project recently. Does this mean that, during selection, my application would automatically be ranked lower than those by other applicants who have a longer tenure with Oppia?**

A: Definitely not! Here are the [selection criteria](#selection-criteria) we use when selecting students for GSoC; note that tenure is not part of these criteria. Also, our philosophy is to consider each application based on its own merits, not relative to other applications, and we try to accept every student whose application "meets the bar". The only cases in which we'd need to compare applications against each other are when a project idea receives multiple applications, or we receive fewer "slots" to host students than we originally applied for.

**Q: What are the minimum number of PRs that one should have?**

A: There is no specific minimum number. Remember that quality is more important than quantity. It is better to submit a nontrivial PRs rather than a simple bug fix. Start with starter issues, then prioritize ones that are related to your project.

**Q: What is the total number we'll accept?**

A: As many as we think we'll succeed, though GSoC admins may impose quotas.

**Q: I do not have any experience in some XYZ skill. Is some certification required?**

A: Try to work on good first issues and take courses online. You develop experience & expertise once you start working. We do not need any certification.

**Q: Is it okay to focus only on the frontend or backend?**

A: This depends on your project. Focus on the project's goals.

## GSoC Proposal Template

When submitting a proposal, please use the provided [GSoC proposal template](https://docs.google.com/document/d/1fZ8yJG70zoANYGJgOv5wsIzz3arOX4Up4EJqfUU6nis/edit). We will only consider proposals submitted using this template.

You are welcome to ask mentors for reviews during the proposal preparation phase. Mentors will review proposals incrementally. That is, they will work through the Mocks section, and, only after they are satisfied with it, they will review the Technical Design section, and, similarly, only after that section looks good, they will review the Milestones section. This is meant to help ensure that later sections of the proposal are building on a solid baseline.

**Important:** Please make sure that your final proposal is self-contained. In particular, to be fair to all applicants, key components of the proposal should not be editable after the deadline, and you shouldn't assume that reviewers will follow external links.

### Tips for writing a good project plan

Here's some advice about proposals and milestone timeline planning that we collated from previous students and mentors:

- Choose a project you're interested in! If you have a strong interest in your project, this will help you pick up necessary skills and tackle any unforeseen difficulties that arise during GSoC.
- Familiarize yourself with the relevant part of the codebase for your project, especially if you haven't touched it before. It's important to think about how to integrate your project with the current Oppia structure -- don't design in a vacuum.
- Define milestones with enough detail to get a proper ETA for each milestone (so, don't just say "write e2e tests"), otherwise you run the risk of significantly underestimating the timeline.
- Clear written communication and presentation is crucial in preparing your proposal. The proposal should show that you have a clear understanding of the codebase and the final goal of the project. Eg. In a user-facing proposal, writing about just the files that have to be changed is not enough, detailed mocks and userflows (in the form of diagrams or points) are also essential.
- Limit proposal length. Remember a lengthy proposal is not equivalent to an excellent proposal.
- Ensure that the problem statement is within your limits to tackle. You should make sure that what you are proposing is within your capabilities. What we have in the [project ideas section](#oppias-project-ideas-list) are suggested milestones; it is up to you to come up with a complete plan that is within your ability. i.e., students can propose whatever they want; it’s up to us to subsequently figure out (during selection) whether we’re happy about what’s being proposed.
- Students who make the last milestone bulky normally run into issues. So, make sure that you distribute work evenly.

### What should applicants expect from mentors in a proposal review?
* Please write your proposal on the assumption that you "own" your chosen project. From your perspective, the submitted proposal should be in as good a condition as possible before you ask for a review. Make sure you have a sufficiently good understanding of the codebase/project to find flaws in the design; don't assume that reviewers are responsible for doing this for you. Note that your proposal doesn't need to be flawless -- we expect that you might make mistakes, and reviewers will be happy to guide you on how to improve. Instead, by "as good a condition as possible", we mean that your proposal should demonstrate:
  * Your ownership of the project
  * The research you have put into writing it
  * Your analytical skills
  * Your independence in making complex decisions
* Make sure to present solutions and ask for feedback, rather than just asking for solutions. You can do this by presenting the various solutions you came up with in your proposal, and doing an analysis of their advantages & disadvantages from the end-user perspective. Finally, choose the best solution you have and explain your reasoning behind your choice. Note that this doesn't mean that you must always have multiple ideas to solve a problem, but you should instead always explain how you reached a solution, and why is it the best one from the end-user's perspective.
* Mentor's suggestions are "suggestions", not orders (often, reviewers may not be certain whether their suggestion is correct), so, as the proposal owner, you are welcome to decide whether to accept/reject it. In either case, when you are accepting/rejecting a suggestion provided by a reviewer, explain your reasoning and the research that led to your decision. Don't use an "appeal to authority" (e.g. "I am doing it this way because XXX said so") -- the rational analysis that underlies the decision is what's important.
* We do not expect you to always agree with your reviewers. If you think that the suggestion doesn't suit your project, it is totally fine to explain your decision and provide reasons for it. It is always a good idea to have discussions when you have confusions, rather than simply agreeing. Note that this does not mean that we encourage you to disagree with your reviewers on everything -- this is just a suggestion to bear in mind if you get confused.
* Please note that your reviewer may or may not be involved in the final selection process. It is also **not** the case that you need to implement all your reviewers' suggestions/requests in order to be selected. As mentioned above, it is important that you actively take help and work together with your proposal reviewers in order to prepare a strong proposal that meets the guidelines for your chosen project.

### Sample proposals from past years

If you'd like to get a sense of what a proposal might contain, please see our [GSoC 2020 page](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020) for examples of proposals that we accepted in 2020. Note that the [GSoC Proposal Template](https://docs.google.com/document/d/1fZ8yJG70zoANYGJgOv5wsIzz3arOX4Up4EJqfUU6nis/edit) was edited for 2021, so please be sure to follow the 2021 template.

_**Note:** although some of the previous years proposals are a bit on the long side, there's **no** formal length requirement for your proposal. In general, the quality of what you write is much more important than the amount of text you write, and we encourage you to write shorter proposals that still convey the main aim of the project. For the actual requirements, please see the [GSoC Proposal Template](#gsoc-proposal-template) section above._

## Types of work related to Oppia projects
In order to ensure a well-rounded engineering experience, developers will do some or all of the following depending on their project:
- Meet with their mentors regularly
- Meet with other contributors related to their project area
- Read and understand parts of the code base related to their project
- Receive code reviews for all code they write for their project
- Write automated tests for their projects
- Create UI mocks (if doing frontend development)
- Write design documents (if implementing large features or introducing new systems)

We asked our previous students what they learned during GSoC 2020. Here are the collated answers:
- Technical ability
  - Writing clean code, while keeping in mind the requirement for the code to run in production.
  - Working on a large codebase.
  - Reading and understanding code from other open source organizations.
  - Automated testing
- Technical domain knowledge
  - I feel more confident on working with Angular. Oppia was the first time I worked with unit, e2e tests. I feel a lot more confident in writing code now whether be it making my own projects or contributing to other open source projects. 
  - I learned lots of things about typescript and webpack. 
  - I understood how E2E tests and angular migrations worked in Oppia -- this felt very rewarding.
  - I enjoyed finding and fixing accessibility issues. 
- Technical leadership skills
  - How to improve in planning.
  - Reviewing others' code
  - Technical design skills (and validation of technical ideas)
  - Organizing work flow, meetings management
- Communication
  - Putting forward my thoughts more systematically and deeply so that everyone can understand me well.
  - Better communication skills.
  - How to write a good proposal.
- I've become more independent and confident over the course of this project. This is not just due to my improvement in the technical aspect, but more importantly, I now know how to start, work through and successfully finish a large scale project. I feel like I can independently and confidently work on more big projects in the future and the fear of "being lost" that I had, has now significantly been reduced.

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

## Oppia's Project Ideas List
_**Note:** If you're coming to this section from an external link, please make sure to scroll up and read this entire wiki page carefully, not just this section. There's a lot of useful information on the rest of the page, including a FAQ and a section describing selection criteria. Thanks!_

The following is a list of Oppia's 2021 GSoC project ideas. (Please note that all mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted.)

You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community in order to get feedback and guidance to improve the proposal. We also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

The list of project ideas is not fixed and more projects can be added. Also, please note that **the project descriptions are not final yet** -- we are still working them out, and some of them may change a bit.


## Data and stability team

### Implement schema validators for the handler params

We would like to robustly validate all arguments passed to GET/POST/DELETE handlers and immediately raise a 400 error if an invalid argument is passed. Currently, the handler params are being verified only in some specific cases and there is no unified way to parse more complicated structures like lists and dicts. 

This project should add the framework for adding schema validation to all handlers, lint checks ensuring that for newly added handlers schema must be added, and documentation about the schema validation. Then the schema validation should be enabled on at least a part of our current handlers.

The schema validation should be implemented based on schema_utils.py (possibly with additional extensions) or through some third party library. Some changes to frontend code might also be required in order to unify how we send data between backend and frontend.

**Potential Mentors:** @vojtechjelinek, @rohitkatlaa

**Difficulty:** Intermediate

**Consider taking up this project if you:**

*   Know how to code in Python
*   Have knowledge of how different HTTP methods work
*   Know how to code a bit in TypeScript and Angular

**What we're looking for in the proposal:** 

*   Comparison of the pros/cons of using third-party library or schema_utils.py for the schema validation.

**Dependency on Release Schedule:** None, although it would be useful to implement most of the stuff before the August release so that the changes are tested.

**Suggested Milestones:**

*   Milestone 1: Implement a framework for schema validation on handlers, add lint checks for new handlers, add documentation about schema validators. Implement schema validators on handlers in 
    *   _admin.py_
    *   _classifier.py_
    *   _classroom.py_
*   Milestone 2: Implement schema validators on handlers in
    *   _collection_editor.py_
    *   _collection_viewer.py_
    *   _concept_card_viewer.py_
    *   _contributor_dashboard.py_
    *   _creator_dashboard.py_
    *   _cron.py_
    *   _custom_landing_pages.py_
    *   _editor.py_
    *   _email_dashboard.py_
    *   _features.py_
    *   _feedback.py_
    *   _improvements.py_
    *   _incoming_emails.py_
    *   _learner_dashboard.py_
    *   _learner_playlist.py_
    *   _library.py_
    *   _moderator.py_
    *   _pages.py_
    *   _platform_feature.py_
    *   _practice_sessions.py_

---

### Make backend code typed

In the frontend, we have fully-typed TypeScript code in place (although there we still need to finish the implementation of strict typing). In the backend, we should also start using types. 

This project should first add Python 3 type checking into the pre-push checks and CI checks (although the current codebase is in Python 2, it will be migrated to Python 3 before GSoC), add documentation about adding types and make sure that types need to be defined for newly added files and code. As for the next part, the assets/constants.ts (constants that are used both in frontend and backend) file should be transformed to protobuf format so that we can leverage typing for our constants too. The last part of this project should implement types for files in core/storage, core/platform, and root folder (feconf.py, utils.py, etc.). In some places we currently use lists of allowed values, these should be transformed to enums.

The checking of type annotations should be done with mypy (or any other typing alternative that implements [PEP484](https://www.python.org/dev/peps/pep-0484/), like pytype or Pyre) checks, preferably we should also implement strict mypy checks, or subset of strict checks that could work even if only a part of the codebase is typed.

**Potential Mentors:** @vojtechjelinek, @rohitkatlaa

**Difficulty:** Intermediate

**Consider taking up this project if you:**

*   Know to work with types in Python 3 and how to use even more complicated typing constructs like `Optional` or `Union` 

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

*   Milestone 1: Implement Python type checking into the pre-push checks and CI checks. Replace assets/constants.ts with protobuf and implement transforming protobuf file to TypeScript and Python constants.
*   Milestone 2: Implement types for the core/storage, core/platform, and root folder.

---

### Simplify the Oppia build process
The build process that Oppia uses to prepare the files for reliably serving the site was changed quite a lot in the last years: we introduced webpack, changed our build scripts from bash to Python, and also upgraded some libraries. Since a lot of these changes affected the build process and sometimes weren’t accounted for, the build process is now clunky and quite hard to understand.

This project’s aim is to simplify the build process, making it easy for developers to work with it and unifying the multiple entry points that need to build some files (backend tests, e2e tests, frontend tests, local dev server) as much as possible. After the project is complete, all the build-related stuff should be handled exclusively with the Angular CLI. **Note: This has a dependency on angular migration being complete. Incase migration looks like it might go well beyond the start of GSoC, please consider applying for a project that removes AngularJS from the codebase and introduces angular router.**

**Potential Mentors:** @vojtechjelinek, @seanlip, @dubeysandeep, @srijanreddy98

**Difficulty:** Hard

**What we're looking for in the proposal:**

*   Having a good understanding of the Angular router.
*   Having in depth understanding of Angular cli and the angular build system.
*   Brownie points for having PRs related to angular migration that demonstrate your ability to migrate from AngularJS to Angular 2+

**Consider taking up this project if you:**

*   Want to critically analyze and then propose a new architecture for our build process.
*   Enjoy refactoring previously-written code.

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

*   Milestone 1: Introduce the angular router, auth guards.
*   Milestone 2: Move to build process to angular-cli.

---

### Improve frontend type system

Our frontend codebase is almost fully typed. However there are some inconsistencies in the frontend and backend. This project will have the following tasks:

*   Convert Object Factories to Model.ts files and keep the entire typings in a folder.
*   Write a lint check to keep the HTTP request and response types in the frontend and backend synced. I.e. if a new field is added in the response from the backend, the frontend should also have the field added, otherwise the linter should pick up on that.
*   In the frontend, there are a lot of repeated types (eg. LostChanges and ExplorationChange). Properly extend/ implement types and create a program to generate a graph that shows the relationship between types.

**Potential Mentors:** @vojtechjelinek, @rohitkatlaa, @dubeysandeep

**Difficulty:** Hard

**Consider taking up this project if you:**

*   Enjoy coming up with cool patterns to simplify development workflow.
*   Are interested in critically analysing various solutions to a single problem.

**Dependency on Release Schedule:** None

**Suggested Milestones:**

*   Milestone 1: Create a robust system for types. Create lint checks so that no type can exist outside the system. Change ~60% of the existing types to follow the system.
*   Milestone 2: Modify the remaining types and write lint checks to keep the HTTP request and response types in the frontend and backend synced.

---

## Automated QA team

### Write Frontend Tests for Services

This project aims to write frontend tests to fully cover each service. When you begin, some services may have tests that incompletely cover the service, while others may have no tests at all. Much of the past work writing frontend tests has been tracked by [oppia/oppia#4057](https://github.com/oppia/oppia/issues/4057). This is a good reference, as is our [wiki page](https://github.com/oppia/oppia/wiki/Frontend-unit-tests-guide). It outlines best practices and standard guidelines you should follow.

The project will involve writing tests for many (around 80 as of January 2021) services. The proposals must contain a concrete plan (preferably as a table) that specifies when each file will be fully covered by tests.

**Potential Mentors:** @kevintab95, @aks681, @iamprayush

**Difficulty:** Intermediate

**Consider taking up this project if you:**

*   Are interested in testing (since most of the project will involve writing unit tests).
*   Have the ability to read through someone else’s code, in order to understand what needs to be tested. (This project will involve reading through a lot of Oppia's source code.)
*   Like to handle technical challenges! It is very likely that you'll run into problems while trying to test the code as is, and you will almost certainly need to research and come up with solutions to test certain constructs.

**What we're looking for in the proposal:**

*   Links to one or more PRs in which you added tests for services. Overall, these PRs should show you adding tests to fully cover at least two services.

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

*   Milestone 1: Fully cover half of the remaining services.
*   Milestone 2: Fully cover all of the services.

---

### Write Frontend Tests for Directives and Components

This project aims to write frontend tests to fully cover each directive/component. Note that “directives” and “components” serve the same role (“directive” is the AngularJS term while “component” is the Angular term). When you begin, some directives/components may have tests that incompletely cover them, while others may have no tests at all. A 2020 GSoC student began work on this, and their [blog post](https://mari-zangue.medium.com/my-journey-through-gsoc20-with-oppia-9eb6b27e7a02) may be a helpful reference. You should also reference our [wiki page](https://github.com/oppia/oppia/wiki/Frontend-unit-tests-guide). It outlines best practices and standard guidelines you should follow.

The project will involve writing tests for many (around 80) directives/components. The proposals must contain a concrete plan (preferably as a table) that specifies when each file will be fully covered by tests.

**Potential Mentors:** @kevintab95, @aks681, @iamprayush

**Difficulty:** Intermediate

**Consider taking up this project if you:**

*   Are interested in testing (since most of the project will involve writing unit tests).
*   Have the ability to read through someone else’s code, in order to understand what needs to be tested. (This project will involve reading through a lot of Oppia's source code.)
*   Like to handle technical challenges! It is very likely that you'll run into problems while trying to test the code as is, and you will almost certainly need to research and come up with solutions to test certain constructs.

**What we're looking for in the proposal:**

*   Links to one or more PRs in which you added tests for directives or components. Overall, these PRs should show you adding tests to fully cover at least two directives or components.

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

We are looking for 4 students to work on this project. Below, we specify the milestones for each student:

*   Student 1 (90 directives/components)
    *   Tasks: Fully cover all the directives/components in the following directories:
        *   ./core/templates/base-components/
        *   ./core/templates/components/button-directives/
        *   ./core/templates/components/ck-editor-helpers/
        *   ./core/templates/components/common-layout-directives/
        *   ./core/templates/components/concept-card/
        *   ./core/templates/components/forms/
        *   ./core/templates/components/keyboard-shortcut-help/
        *   ./core/templates/components/on-screen-keyboard/
        *   ./core/templates/components/oppia-angular-root.component.ts
        *   ./core/templates/components/profile-link-directives/
        *   ./core/templates/components/question-difficulty-selector/
        *   ./core/templates/components/question-directives/
        *   ./core/templates/components/ratings/
        *   ./core/templates/components/review-material-editor/
        *   ./core/templates/components/rubrics-editor/
        *   ./core/templates/components/score-ring/
        *   ./core/templates/components/skill-mastery/
        *   ./core/templates/components/skill-selector/
        *   ./core/templates/components/skills-mastery-list/
        *   ./core/templates/components/state-directives/
        *   ./core/templates/components/state-editor/
        *   ./extensions/rich_text_components
    *   Milestones
        *   Milestone 1: Fully cover half of the assigned components/directives.
        *   Milestone 2: Fully cover all of the assigned components/directives.
*   Student 2 (94 components/directives)
    *   Tasks: Fully cover all the directives/components in the following directories:
        *   ./core/templates/components/state-editor/
        *   ./core/templates/components/statistics-directives/
        *   ./core/templates/components/summary-tile/
        *   ./core/templates/components/version-diff-visualization/
        *   ./core/templates/directives/
        *   ./core/templates/domain/
        *   ./core/templates/pages/about-page/
        *   ./core/templates/pages/admin-page/
        *   ./core/templates/pages/classroom-page/
        *   ./core/templates/pages/collection-player-page/
        *   ./core/templates/pages/contributor-dashboard-page/
        *   ./core/templates/pages/creator-dashboard-page/
        *   ./core/templates/pages/delete-account-page/
        *   ./core/templates/pages/donate-page/
        *   ./core/templates/pages/email-dashboard-pages/
        *   ./core/templates/pages/error-pages/
        *   ./core/templates/pages/exploration-editor-page/
    *   Milestones
        *   Milestone 1: Fully cover half of the assigned components/directives.
        *   Milestone 2: Fully cover all of the assigned components/directives.
*   Student 3 (88 components/directives)
    *   Tasks: Fully cover all the directives/components in the following directories:
        *   ./core/templates/pages/exploration-player-page/
        *   ./core/templates/pages/landing-pages/
        *   ./core/templates/pages/learner-dashboard-page/
        *   ./core/templates/pages/library-page/
        *   ./core/templates/pages/maintenance-page/
        *   ./core/templates/pages/moderator-page/
        *   ./core/templates/pages/notifications-dashboard-page/
        *   ./core/templates/pages/practice-session-page/
        *   ./core/templates/pages/preferences-page/
        *   ./core/templates/pages/profile-page/
        *   ./core/templates/pages/review-test-page/
        *   ./core/templates/pages/signup-page/
        *   ./core/templates/pages/skill-editor-page/
        *   ./core/templates/pages/splash-page/
        *   ./core/templates/pages/story-editor-page/
        *   ./core/templates/pages/story-viewer-page/
        *   ./core/templates/pages/subtopic-viewer-page/
        *   ./core/templates/pages/teach-page/
        *   ./core/templates/pages/terms-page/
        *   ./core/templates/pages/thanks-page/
        *   ./core/templates/pages/topic-editor-page/
        *   ./core/templates/pages/topic-viewer-page/
        *   ./core/templates/pages/topics-and-skills-dashboard-page/
        *   ./extensions/value_generators/
        *   ./extensions/visualizations/
    *   Milestones
        *   Milestone 1: Fully cover half of the assigned components/directives.
        *   Milestone 2: Fully cover all of the assigned components/directives.
*   Student 4 (105 components/directives)
    *   Tasks: Fully cover all the directives/components in the following directories:
        *   ./extensions/interactions
        *   ./extensions/objects
    *   Milestones
        *   Milestone 1: Fully cover half of the assigned components/directives.
        *   Milestone 2: Fully cover all of the assigned components/directives.

---

## Learner and Creator Experience team

### Integrating the Oppia blog with Oppia.org

Today’s Oppia.org blog is currently hosted on a separate site, Medium. We would prefer to have the blog page directly on Oppia.org so that it is directly connected to the rest of the site. The aim of this project is to add a “blog” page hosted on Oppia.org, and implement a simple interface for editing it.

**Potential Mentors:** @aks681

**Difficulty:** Intermediate

**Consider taking up this project if you:**

*   Like working with the full stack, which includes creating storage models and frontend views.
*   Owning a specific section of the codebase.
*   Like to create new user flows and UX.
*   Are interested in working with Python, Angular (Typescript) and HTML.

**What we're looking for in the proposal:** 

*   There should be plans to handle both the backend and frontend of the blog integration.
*   Should provide a view to transfer existing blogs from Medium to this. This can be a manual transfer, though it should be possible.

**Dependency on Release Schedule:** Yes, M2 would need to be tested in release as that includes the addition of new pages.

**Suggested Milestones:**

*   Milestone 1: Create the storage model and complete the backend for storing the blog post and author data.
    *   Model should store the publishing date.
    *   Blog posts should be searchable via their titles.
    *   Each blog should have tags that can be added by the user.
    *   There should be separate “Save Draft” and “Publish” functionalities.
    *   HTML meta tags can also be added to each blog post.
*   Milestone 2: The frontend editor UI is done which should allow moving the Medium blogs to Oppia (so, any visible fields that Medium has should be handled as well).
    *   The “blog dashboard” should be accessible from the navbar/profile dropdown.

---

## Contributor Experience team

### Contributor Dashboard Mobile UI [wiki]

The Contributor Dashboard allows users to submit suggestions for translations and practice questions which are then reviewed and accepted/rejected. Currently, the dashboard has only been developed with a desktop view in mind. We want users to have a smooth experience on any platform/device.

In this project, you will work with designers to flesh out the design and UX experience of the contributor dashboard on mobile devices. Once the mocks are complete, you will then implement the new mobile UI for the entire contributor dashboard page and related user flows. 

**Potential Mentors:** @seanlip

**Difficulty:** Intermediate

**Consider taking up this project if you:**

*   Like to work collaboratively with others in different domains, working together to create a complete engineering product
*   Are interested in working on the frontend with Angular, Typescript, HTML, CSS
*   Respect the user and are committed to debugging and tweaking in response to feedback

**Dependency on Release Schedule:** Yes. Mobile UI changes will need to be pushed to test or production servers to be tested more widely in order to catch edge cases in user journeys.

**Suggested Milestones:**

*   Milestone 1: Implement the mobile UI for the contributor dashboard landing page and translation suggestion flow
*   Milestone 2: Implement the mobile UI for the question suggestion flow

---

## Android team

### Static Analysis Checks + Improvements

One key part in ensuring a development team reaches optimal efficiency is by ensuring there are reasonable checks in place to avoid regressing previous fixes, reducing trivial verification during code reviews, and ensuring that team members are utilizing best practices. A popular way to achieve this is with static analysis tools like linters. While the Oppia Android team has linters & automated tests implemented, we'd like to fill in some of the gaps in our static analysis tooling by providing ways to enforce best practices & further simplify code reviews.

Potential checks:

*   Verify activities have accessibility labels
*   Verify all files have a corresponding test file
*   Ensure activities/fragments/views can't be used outside of the app module, or in testing
*   Ensure KDocs are present for every non-private class, method, and field (even trivial ones)
*   Ensure we can easily add future checks on file names or file contents using RegEx
*   All non-test activities always have a label assigned. (important for A11y)

In particular, we're looking for static analysis improvements in a few areas:

*   Syntax verification improvements
    *   XML: verifying that our XML files are consistently formatted & follow our Android style guide for layout files
    *   Kotlin: providing style enforcement for KDoc comments in Kotlin files
*   Best practices enforcements
    *   Involves introducing a general-purpose framework that allows us to easily define prohibited regular expression patterns that match either contents of targeted files, or filenames themselves to trigger a blocking CI failure
    *   Involves collecting a list of best practices that can be enforced with this system & populating a list of prohibited patterns to enforce these patterns
    *   Involves introducing a check to ensure every new file has a corresponding test file, and that test file has a Bazel target defined for it (this may require whitelisting files that do not require tests, such as modules or Dagger component classes)

**Potential Mentors:** @BenHenning, @aggarwalpulkit596

**Difficulty:** Intermediate

**Consider taking up this project if you...**

*   Like really clean code & want to keep it that way
*   Want to help other developers reduce mistakes that could cost the team valuable development time, or in the worst case cause issues for users
*   Want to make code development & reviewing easier

**Knowledge/Skills Recommended:**

*   Familiarity with style guides is helpful, though the student will need to become familiar with the team's style guide in order to make progress
*   Ability to collect requirements & turn them into code (in particular, identifying best practice checks to enforce from our best practices lists, style guides, and from interviewing team members)
*   Familiarity with GitHub Actions will help
*   Understanding of regular expressions strongly recommended
*   Knowledge of scripting, particularly using JavaScript & Kotlin

**Dependency on Release Schedule:** No

**Suggested Milestones:**

*   Milestone 1: Introduce infrastructure for enforcing file content & name patterns in CI. Implement checks that enforce 10-20+ of team best practices.
*   Milestone 2: Introduce XML linter with Android style enforcement. Add Ktlint extension to check for KDoc formatting. Add check to ensure new files have tests.

---

### Improved Code Coverage & CI Support

The Oppia Android strongly values testing new code, and ensuring that these tests are thorough. Tests are a key way to protect new code from breaking in the future, something that everyone on the team appreciates. However, the team does not currently have a way to measure or enforce code coverage. This leads to gaps and missed behaviors that could break in the future. We need infrastructure that can record code coverage for existing tests & report the coverage in an easy-to-consume way. Further, this project involves establishing processes to improve the actual code coverage in the app and make the overall project more robust.

Note: This project will require additional onboarding work to take an existing test that is lacking some test coverage & work to fill in the gaps with new tests.

For reference, see this [Codacy report](https://app.codacy.com/gh/anandwana001/oppia-android/dashboard) of Akshay’s Oppia Android fork for an idea on nice code coverage reporting.

**Potential Mentors:** @anandwana001, @BenHenning

**Difficulty:** Intermediate

**Consider taking up this project if you...**

*   Want to understand how to write very clean tests
*   Want to help other team members learn how to write clean tests
*   Want to understand how to turn missing lines of code into new tests
*   Want to help improve the team's confidence when writing code (e.g. due to having better test coverage)

**Knowledge/Skills Recommended:**

*   Kotlin
*   Familiarity with writing tests; a key part of this project is finding the gaps in existing code coverage & writing tests to fill in the gaps
*   Excellent English writing skills since this project will involve writing documentation that the rest of the team will follow
*   Good troubleshooting skills since early analyses have revealed challenges in setting up JaCoCo

**Dependency on Release Schedule:** No

**Suggested Milestones:**

*   Milestone 1: Ensure code coverage documentation is thorough; set up code coverage support in CI with Gradle & JaCoCo. Set up Codacy. Successfully improve the code coverage for 1 class/component to 100% test coverage.
*   Milestone 2: Bring at least 10 different classes/components totalling at least 10k test LOC to 100% test coverage (all of these should be starting at less than 80% code coverage). 

---

### End-to-End Testing Support

Oppia Android's current testing corpus includes unit tests using the Robolectric testing framework & integration tests using the Espresso testing framework (to ensure that the app operates as expected on real Android). The current tests have a few limitations: they do not correctly facilitate cross-activity navigation flows which actual users will be triggering, and they do not verify that the app can interact with Oppia's backend correctly.

To prepare for the global launch of the app, we need end-to-end tests that:

*   Verify that the app works as a user would expect by playing through select critical user journeys
*   Verify that the app operates as expected when interacting with a local developer instance of the Oppia backend server

We expect that the tests will be written using UiAutomator & are set up for interacting with a local development server (see [relevant documentation](https://developer.android.com/studio/run/emulator-networking.html)).

Note that this project requires running Linux with virtualization support (in order to run an Android emulator). Some machines support running VMs that in turn can virtualize software--you should verify this. We will be checking this during the application period.

**Potential Mentors:** @anandwana001, @BenHenning

**Difficulty:** Hard

**Consider taking up this project if you...**

*   Enjoy thinking like a user or QA tester, and want to ensure the user's experience is well-protected by excellent end-to-end tests
*   Want to get a good understanding of how the cross-stack integrations between the Android app and web backend work
*   Want to learn how to write instrumentation tests (particularly with UiAutomator), or understand what's involved to write end-to-end tests

**Knowledge/Skills Recommended:**

*   Kotlin
*   Python (this project will involve changing Oppia's backend)
*   Bazel may help (the end-to-end tests must be written using Bazel--they won't have Gradle support)
*   Android testing (especially Espresso and/or UiAutomator), or other end-to-end testing (such as Protractor)

**Dependency on Release Schedule:** No (since the backend changes are only needed for developer runs of the app)

**Suggested Milestones:**

*   Milestone 1: Introduce developer-only functionality in the Oppia backend to prepopulate test topics, stories, chapters, explorations, revision cards, skills, and questions. Set up infrastructure for end-to-end testing using UiAutomator & Bazel (which will include some remodularization of the app to ensure the app can run in a mode that allows connecting to a local server). Write 1 basic end-to-end test demonstrating functionality.
    *   Note that the test data does not need to be sensible, it just needs to be able to ensure key test scenarios can be tested in the app
    *   Note that the test explorations can leverage the existing test explorations [bundled](https://github.com/oppia/oppia/tree/develop/data/explorations) with the backend, but it's recommended the student create a test exploration that has proper compatibility with the Oppia app (see [Android's test explorations](https://github.com/oppia/oppia-android/tree/develop/domain/src/main/assets) for an idea on exploration compatibility)
    *   Note that the initial test does not need to verify anything important, it just needs to demonstrate that the tests can work
*   Milestone 2: Write end-to-end tests for critical user journeys from the following packages:
    *   Create a profile & log into it
    *   Download a topic
    *   Play through one exploration

---

### Implement feature flags & platform parameters

With a large scale system like Oppia, we sometimes have features that contain several points of integration in the codebase, and/or require additional data priming or migrations ahead of the feature being released. These features often span multiple releases and thus require feature flags to gate integration points to ensure that the feature is not partially released ahead of schedule. Moreover, these features often require migrations which need to be run in specific releases due to new versions being made in irreversible data structures (e.g. explorations).

In order to release these types of features in a smooth manner, we want to be able to put these features behind feature flags that are enabled in specific builds (compile-time) and can be enabled dynamically (at runtime). This project aims to introduce compile-time & runtime feature gating for the Android app, leveraging existing runtime gating functionality supported on Oppia web.

Note that this project actually involves introducing what are called platform parameters. These are parameters that can be one of several data types (e.g. strings, integers, booleans). We plan to use the boolean types for gating features as described above, but the other parameters are essential in order to ensure the app is reasonably configurable for many different circumstances (include deprecations). The work difference between specifically supporting booleans & other data types is expected to be small.

**Potential Mentors:** @vinitamurthi, @Sarthak2601, @BenHenning

**Difficulty:** Hard

**Consider taking up this project if you...**

*   Are interested in understanding how to release large scale features in a production system
*   Would like to work on a project that touches several layers of the system. This means that you would get a greater understanding of how all the pieces of the app fit together and how they work with the backend too!

**Knowledge/Skills Recommended:**

*   Kotlin
*   Python
*   Architectural design, especially when it comes to writing test doubles/fakes

**Dependency on Release Schedule:** No

**Suggested Milestones:**

*   Milestone 1: Introduce a platform parameter system that initially has support for compile-time definitions (e.g. using Dagger modules). A major component of this milestone includes writing test infrastructure that can be used to enable features via JUnit annotations for select tests so that the team can write tests specifically for certain features being enabled/disabled.
*   Milestone 2: Introduce runtime parameter support by hooking up to Oppia backend's platform parameter API & connecting these flags back to the predefined compile-time parameters. Note that the lifecycle of these parameters need to be carefully managed: they should not be applied until the app restarts. This part of the project will include caching results from the server, and introducing a lightweight synchronization mechanism so that the app periodically verifies that its copies of the parameters are up-to-date.

---

## Oppiabot team

### Making Oppiabot Better

Oppiabot is a GitHub bot that helps automate the process of contributing to the Oppia and Oppia Android repository.

This project involves adding a couple of new features and making the currently available features better.

**Available Features:**

1. Setup a cron job to ping code owners who have been assigned to PRs but have not reviewed the PR within 24 hours.
2. Enforcing TODOs. See [#163](https://github.com/oppia/oppiabot/issues/163).
3. Introduce a pre-commit linter for oppiabot.
4. Update contributors about pending PRs. See [#129](https://github.com/oppia/oppiabot/issues/129).
5. Alert onboarding team based on contributor activity. See [#134](https://github.com/oppia/oppiabot/issues/134)
6. Close stale branches. See [#87](https://github.com/oppia/oppiabot/issues/87)
7. Update code owner check to use codeowner file for assigning code owners.
8. Be more proactive towards new contributors. See [#166](https://github.com/oppia/oppiabot/issues/166)

**Potential Mentors:** @jameesjohn, @vojtechjelinek

**Difficulty:** Intermediate

**Consider taking up this project if you:**

*   Want to help improve the experience of contributors
*   Interested in designing the flow of a contributor from when a pull request is made till it gets merged.
*   Are interested in working with JavaScript (NodeJS).

**What we're looking for in the proposal:** 

1. Links to one or more PRs showing contribution to the oppiabot project.
2. Deep understanding and concern for the developer experience.

**Dependency on Release Schedule:** None

**Suggested Milestones:**

*   Milestone 1: Fix half of the issues available.
*   Milestone 2: Fix remaining half of the issues.

# Other useful information

## Dates and Deadlines

Noteworthy dates for 2021 ([Full Timeline](https://developers.google.com/open-source/gsoc/timeline)):
* **Jan 15 - Feb 19**: Mentoring organizations apply
* **Mar 9**: Mentoring organizations are announced
* **Mar 29 - Apr 13**: Student application period
* **May 17**: Accepted students are announced
* **May 17 - Jun 7**: Community bonding period
* **Jun 7 - Aug 23**: Students enjoy the summer by contributing code to their projects
* **Aug 31**: GSoC officially ends

## List of Mentors
_Please come back to this section at the end of Jan/early Feb 2021 for the final list of mentors!_

## Communication

**Chat**

Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](
https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any questions related to getting started. For project-specific questions, please direct your queries to the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).

**Email**

If you have questions pertaining to "how-to-get-started", please ask them on [Gitter](
https://gitter.im/oppia/oppia-chat), or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you. Also, please make sure to read our ["getting started" wiki page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) before sending an email, since the answer to your question might already be contained there!

To discuss your project ideas, or share your proposal for feedback from the community, please email the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com). You can also use this list for specific questions about GSoC.