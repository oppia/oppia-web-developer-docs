## Table of Contents

-   [Completed Projects](#completed-projects)
-   [Getting started](#getting-started)
-   [FAQs](#faqs)
-   [GSoC Proposal Template](#gsoc-proposal-template)
    -   [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan)
    -   [What should applicants expect from mentors in a proposal review?](#what-should-applicants-expect-from-mentors-in-a-proposal-review)
    -   [Sample proposals from past years](#sample-proposals-from-past-years)
-   [Types of work related to Oppia projects](#types-of-work-related-to-oppia-projects)
-   [Selection Criteria](#selection-criteria)
-   [Oppia's Project Ideas List](#oppias-project-ideas-list)
    -   [Developer Experience Team](#developer-experience)
    -   [Data and Stability Team](#data-and-stability-team)
    -   [Automated QA Team](#automated-qa-team)
    -   [Learner and Creator Experience Team](#learner-and-creator-experience-team)
    -   [Contributor Experience Team](#contributor-experience-team)
    -   [Android Team](#android-team)
    -   [Oppiabot Team](#oppiabot-team)
-   [Other useful information](#other-useful-information)
    -   [Dates and Deadlines](#dates-and-deadlines)
    -   [List of Mentors](#list-of-mentors)
    -   [Communication](#communication)

Oppia has been selected to participate in [Google Summer of Code 2021](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers post-secondary students an opportunity to discover and work with open source organizations over the course of 3 months, while being paid a stipend. Students work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

In order to receive updates about GSoC at Oppia please subscribe to [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce).

You might be interested in our GSoC info pages from previous years: [2020](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020), [2019](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2019), [2018](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018), [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions [here](https://github.com/oppia/oppia/wiki).

## Completed Projects:
The following projects were fully completed during GSoC 2021:
* [Abhay Garg's proposal](pdfs/GSoC2021AbhayGarg.pdf) and [final blog post](https://medium.com/@prayutsu/google-summer-of-code-2021-oppia-7cb7588667ec): Introduce support for displaying copyright licenses in the app. Mentor: Rajat Talesra
   * **Milestone 1:** Introduce a script for generating a list of dependencies using a reverse-deps lookup of Oppia Android's //third_party Maven dependencies. Introduce a script for converting the dependency list to actual license content files.
   * **Milestone 2:** Introduce & hook-up a UI to properly display all of the licenses included in the app. Introduce a GitHub Actions check to verify that the list of dependencies is kept up-to-date over time. Introduce extra checks to ensure that generations of the license files can't be accidentally checked into the repository.


* [Aditya Dubey's proposal](pdfs/GSoC2021AdityaDubey.pdf) and [final blog post](https://docs.google.com/document/d/1SK-n2Av8yb6rPPZh5XkyLarV-3GLNpr0JaH6rLTGat4/edit?usp=sharing): Move custom JS\TS lint checks to eslint. Mentor: Anshul Hudda
   * **Milestone 1:** Migrate all JS/TS lint checks to custom Eslint checks (#10816). Implement 3 E2E lint checks from #8423.
   * **Milestone 2:** Implement remaining 1 E2E lint check from #8423 and move all BAD_PATTERNS_JS_AND_TS_REGEXP from general_purpose_linter.py to custom eslint checks.

* [Aishwary Saxena's proposal](pdfs/GSoC2021AishwarySaxena.pdf) and [final blog post](https://aishwary023.github.io/gsoc-2021-oppia/): Write frontend tests. Mentor: Kevin Thomas
  * **Milestone 1:** Fully cover half of the assigned code.
  * **Milestone 2:** Fully cover all of the assigned code.
  * List of Files for Aishwary: [Link](https://docs.google.com/spreadsheets/d/1tky4jE7uxLQTp0MWE3L9USnPvy3PbtGYpMgP7b0bicw/edit#gid=2101159169)

* [Apoorv Srivastava's proposal](pdfs/GSoC2021ApoorvSrivastava.pdf) and [final blog post](https://medium.com/@MaskedCarrot/google-summer-of-code-2021-oppia-d2e346508bb9): Implement lightweight checkpointing. Mentor: Pulkit Aggarwal
  * **Milestone 1:** Implement domain layer changes for creating, checking and restoring checkpoints. Checkpoints should also be automatically expired on a least-recently-used policy basis if more than 2MB of space are consumed by checkpoints (per profile). 
  * **Milestone 2:** Implement the UI changes needed to represent checkpoints that are in progress, changes to existing notices, and proper UI/domain layer support for automatically expiring checkpoints when the user has been away from the app for too long or if the app has decided to automatically expire a checkpoint to save space.


* [Arjun Gupta's proposal](pdfs/GSoC2021ArjunGupta.pdf) and [final blog post](https://medium.com/@arjupta/google-summer-of-code-2021-with-oppia-23758362d710): Implement feature flags & platform parameters. Mentor: Vinita Murthi
  * **Milestone 1:** Introduce platform parameter system that has support for compile-time definitions (i.e. using Dagger modules and dagger constants). The resulting platform parameter support should be built such that we can easily combine the compile-time gating with runtime parameters. Introduce an integration test that verifies the compile-time feature.
  * **Milestone 2:** Introduce runtime parameter support by hooking up to Oppia backend's platform parameter API & connecting these flags back to the predefined compile-time parameters. The lifecycle of these parameters need to be carefully managed: they should not be applied until the app restarts. This part of the project will include caching results from the server, and introducing a lightweight synchronization mechanism so that the app periodically verifies that its copies of the parameters are up-to-date. When the device is offline or the flag fetching fails, the flags should have appropriate defaults for the runtime parameters. Enhance the previous integration test in M1, to demonstrate the usage of runtime flags.


* [Aryaman Gupta's proposal](pdfs/GSoC2021AryamanGupta.pdf) and [final blog post](https://atpug22.medium.com/google-summer-of-code-2021-with-oppia-d61fb8c848ca): Improve Exploration save flow: Syncing edits in the background. Mentor: Kevin Thomas
  * **Milestone 1:** Introduce functionality such that edits made to an exploration by a user are propagated to all clients. More specifically, an editor’s changes should be applied to the saved exploration if their changes are unrelated to existing edits that had been committed since their last draft was started. Otherwise, the user should be informed of the merge conflict and be given a suitable way to handle it.
  * **Milestone 2:** Enable exploration editing to work offline in case of connectivity issues.

* [Ashutosh Chauhan's proposal](pdfs/GSoC2021AshutoshChauhan.pdf) and [final blog post](https://gist.github.com/ashutoshc8101/4fa89e4f437c97df21ac91ddd0736440#file-gsoc-md): Angular migration. Mentor: Srijan Reddy Vasa
  * **Milestone 1:** Migrate the following files (and their corresponding test + HTML files, if already present) to use angular: 
      * admin-page.directive.ts
      * admin-roles-tab.directive.ts
      * admin-misc-tab.directive.ts
      * admin-config-tab.directive.ts
      * classroom-page.component.ts
      * search-bar.component.ts
      * OppiaFooter.ts
      * i18nFooter.ts
      * topic-summary-tile.directive.ts
      * base-content.directive.ts
      * preferences-page.component.ts
      * edit-profile-picture-modal.controller.ts
      * profile-page.component.ts
      * topic-editor-state.service.ts
      * topic-editor-routing.service.ts
      * subtopic-validation.service.ts
      * topic-editor-navbar-breadcrumb.directive.ts
      * question-difficulty-selector.directive.ts
      * subtopic-preview-tab.component.ts
      * topic-preview-tab.component.ts
      * preview-thumbnail.component.ts
  * **Milestone 2:** Introduce angular router (including route guards) and migrate all pages to it. (Note: "frontend routing services" part  -- i.e. the sub-tabs in pages like the admin page and the topic, skill, exploration editors -- is not a requirement for this milestone.)

* [Eesha Arif's proposal](pdfs/GSoC2021EeshaArif.pdf) and [final blog post](https://gist.github.com/EeshaArif/53016604eae2abb89355b8725f914c0a): Improve frontend type system. Mentor: Vojtěch Jelínek
  * **Milestone 1:**
      * Introduce strict typing into 108 files (spec files count as normal files) that contain at least one strict typing error.
      * Files that do not contain strict typing errors need to be added to the tsconfig-strict.ts too.
  * **Milestone 2:** 
      * Introduce strict typing into 132 files (spec files count as normal files) that contain at least one strict typing error.
      * Files that do not contain strict typing errors need to be added to the tsconfig-strict.ts too.
  * List of files for Eesha: [Link](https://docs.google.com/spreadsheets/d/1LqifUvMfLvx7IlGnwPwAXb6GTVi-gA6mz701qFFtolk/edit?ts=60a2b76c#gid=0)

* [Farees Hussain Syed's proposal](pdfs/GSoC2021FareesHussain.pdf) and [final blog post](https://farees-hussain.medium.com/google-summer-of-code-2021-oppia-b3776dbdd5ec): End-to-End testing support. Mentor: Akshay Nandwana
  * **Milestone 1:** Remodularize the necessary parts of the app to support connecting to a developer instance of the Oppia backend for both lesson and image data. Create a new test exploration for the Oppia backend (via YAML) and dummy topic data (via AssetDevHandler) that covers all existing interactions supported by the Android app and use that in the test.
    * Note that the test data does not need to actually make sense, it just needs to be able to ensure key test scenarios can be tested in the app
    * The exploration should contain at least one image in some interaction
  * **Milestone 2:** Set up infrastructure for end-to-end testing using UiAutomator & Bazel. Write an end-to-end test for downloading & playing through one exploration.


* [Gangavarapu Praneeth's proposal](pdfs/GSoC2021GangavarapuPraneeth.pdf) and [final blog post](https://medium.com/@praneethg/google-summer-of-code-2021-at-oppia-foundation-a1f7542eaa2a): Write frontend tests. Mentor: Nithesh Hariharan
  * **Milestone 1:** Fully cover half of the assigned code.
  * **Milestone 2:** Fully cover all of the assigned code.
  * List of Files for Praneeth: [Link](https://docs.google.com/spreadsheets/d/1tky4jE7uxLQTp0MWE3L9USnPvy3PbtGYpMgP7b0bicw/edit#gid=633157043)

* [Hardik Katehara's proposal](pdfs/GSoC2021HardikKatehara.pdf) and [final blog post](https://hardikkatehara.medium.com/google-summer-of-code21-with-oppia-88076053621c): Make backend code typed. Mentor: Sajal Asati
  * **Milestone 1:**  Implement pre-push and CI checks for Python type-checking. Add support for typing assets/constants.ts using protobuf. Add documentation for how to run type checks and how to add type annotations. Cover all Python files (including test files) in the root folder with annotations and create an issue covering type annotation for the other files.
  * **Milestone 2:** Cover all Python files (including test files) in core/storage and core/platform with type annotations.

* [Krishita Jain's proposal](pdfs/GSoC2021KrishitaJain.pdf) and [final blog post](https://medium.com/@jainkrishita15/google-summer-of-code-2021-with-oppia-2ef3bf652883): Redesigning and updating the learner dashboard. Mentor: Akshay Anand
  * **Milestone 1:** Add Goals and Community Lessons tabs to the learner dashboard page. The Goals tab will be hidden behind a flag and the existing functionality on the learner dashboard will go into the new Community Lessons and Feedback Updates tabs. All backend and frontend work for these three tabs should be completed.
  * **Milestone 2:** Add Home and Progress tabs to the learner dashboard page. All backend and frontend work for these two tabs should be completed. The Goals tab from Milestone 1 should be made fully available to users.

* [Mridul Setia's proposal](pdfs/GSoC2021MridulSetia.pdf) and [final blog post](https://gist.github.com/mridul-netizen/e732dfeae3b1201cdbbb23377467a6bd): Improve frontend type system. Mentor: Srijan Reddy Vasa
  * **Milestone 1:**
      * Introduce strict typing into 120 files (spec files count as normal files) that contain at least one strict typing error.
      * Files that do not contain strict typing errors need to be added to the tsconfig-strict.ts too.
  * **Milestone 2:** 
      * Introduce strict typing into 120 files (spec files count as normal files) that contain at least one strict typing error.
      * Files that do not contain strict typing errors need to be added to the tsconfig-strict.ts too.
  * List of files for Mridul: [Link](https://docs.google.com/spreadsheets/d/1LqifUvMfLvx7IlGnwPwAXb6GTVi-gA6mz701qFFtolk/edit?ts=60a2b76c#gid=0)

* [Nikhil Agarwal's proposal](pdfs/GSoC2021NikhilAgarwal.pdf) and [final blog post](https://docs.google.com/document/d/1GDfd8QUuXq2Kub_grZ3o7s9PmtZEQ0LveC3f4J5as5Y/edit): Implement schema validators for the handler params. Mentor: Rohit Katlaa
   * **Milestone 1:** Implement a framework for schema validation for handlers, add lint checks for new handlers, and add documentation about schema validators. Create starter issues for new contributors for remaining handlers. Implement schema validators for all handlers in
      * admin.py
      * classifier.py
      * classroom.py
      * collection_editor.py
      * collection_viewer.py
      * concept_card_viewer.py
      * contributor_dashboard.py
      * cron.py
   * **Milestone 2:** Implement schema validators for all handlers in
      * creator_dashboard.py
      * custom_landing_pages.py
      * editor.py
      * email_dashboard.py
      * features.py
      * feedback.py
      * improvements.py
      * incoming_emails.py
      * learner_dashboard.py
      * learner_playlist.py
      * library.py
      * moderator.py
      * pages.py
      * platform_feature.py
      * practice_sessions.py

* [Radesh Kumar's proposal](pdfs/GSoC2021RadeshKumar.pdf) and [final blog post](https://medium.com/@imradesh/migrating-angularjs-components-and-writing-frontend-tests-gsoc-2020-oppia-16e8209778c): Write frontend tests. Mentor: Nithesh Hariharan
  * **Milestone 1:** Fully cover half of the assigned code.
  * **Milestone 2:** Fully cover all of the assigned code.
  * List of Files for Radesh: [Link](https://docs.google.com/spreadsheets/d/1tky4jE7uxLQTp0MWE3L9USnPvy3PbtGYpMgP7b0bicw/edit#gid=44144901)

* [Rijuta Singh's proposal](pdfs/GSoC2021RijutaSingh.pdf) and [final blog post](https://medium.com/@rijuta_s/google-summer-of-code-2021-with-oppia-43e7a90c907b): Integrating the Oppia blog with Oppia.org. Mentor: Prayush Dawda
  * **Milestone 1:** Complete the backend functionality for blog posts (for editors and viewers). This includes storage models (BlogPostModel, BlogPostSummaryModel, BlogPostRightsModel) and all services/controllers pertaining to the blog dashboard and blog homepage (including ‘Save Draft’ and ‘Publish’ functionalities for editors). Add new ‘Blog Editor’ and ‘Blog Admin’ roles, where Blog Admins can manage the list of Blog Editors as well as the list of custom tags for blog posts.
  * **Milestone 2:** Complete the ‘blog dashboard’ frontend, which includes the ‘blog-editor’ interface and blog post card preview functionality. Tags assigned to a blog post should also be used as meta tags, and the RTE in the blog post editor will support adding headers. Write end-to-end tests for the blog dashboard. Fully migrate at least 2 Medium blog posts to the new Oppia blog.

* [Sparsh Agrawal's proposal](pdfs/GSoC2021SparshAgrawal.pdf) and [final blog post](https://medium.com/@sparshagrawal1212/google-summer-of-code-2021-oppia-8a7011828f26): Static analysis checks + Improvements. Mentor: Ben Henning
  * **Milestone 1:** Introduce check to validate KDoc is present for all non-private components of a Kotlin file (classes, constructors, fields, methods, functions, and constants) with the exception of the default class constructor and companion objects. Introduce check to verify all layout files are syntactically valid XML. Introduce support for custom RegExp checks for file names & contents with an initial check that verifies activities are defined with accessibility labels. All of these checks should run in GitHub Actions.
  * **Milestone 2:** Add a GitHub Actions check to verify that production files have corresponding test files. Introduce TODO verification as a check which should be run in GitHub Actions and triggered both for PRs and for issue changes where failures in the latter should automatically reopen the issue.


* [Yash Raj's proposal](pdfs/GSoC2021YashRaj.pdf) and [final blog post](https://medium.com/@yashrajprime/google-summer-of-code-2021-oppia-599e915c2755): Developer options menu. Mentor: Sarthak Agarwal
  * **Milestone 1:** Introduce the initial UI & an option to crash the app as a proof-of-concept. This menu should be disabled by default in non-developer builds of the app. This should use a compile-time solution (like Dagger or Bazel build targets) rather than a runtime solution (like an if-check). Add the following two features: marking specific topics/stories/chapters completed, and viewing event logs.
  * **Milestone 2:** Add support for the following two features: forcing connectivity type, and forcing hints/solutions to automatically show. The functionality used elsewhere in the app to support this should be built in such a way where it's not included in production builds of the app, and in a way that doesn't "punch holes" in the app. 



# Students

GSoC is an excellent opportunity for students to get paid to work on an open source project. If you're interested in applying as a student, you should definitely read the following resources:

-   [Google Summer of Code student guide](https://google.github.io/gsocguides/student/)
-   [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
-   [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)

## Getting started

If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. If you like, you can also sign up to the [oppia-gsoc-discuss@](https://groups.google.com/forum/#!forum/oppia-gsoc-discuss) mailing list to participate in general discussion related to Oppia's involvement in GSoC (see point 6 below, too). Make sure to set your preferences correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is all about by taking a look at our [user documentation](http://oppia.github.io/#/) -- this will help you become familiar with important concepts like explorations and interactions. We also recommend having a go at playing lessons on [Oppia.org](https://www.oppia.org/splash), which hosts a live instance of Oppia.

3. Read and follow the instructions in the [contributors' guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) carefully.

4. Consider taking up one or more starter projects in order to become familiar with the contribution process. This will help us get an idea of what it's like to work with you -- e.g. how independent, resourceful, responsive, etc. you are. It will also help you get a better understanding of the codebase, so that you can write a good, detailed project proposal.

    - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to follow the [dev workflow](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#instructions-for-making-a-code-change) carefully, manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide), and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Once you've merged at least 2 pull requests, you will get an invitation to become a collaborator to the Oppia repository and be officially onboarded! **This step is a prerequisite** to applying for GSoC.

6. Now, you can select one or more GSoC projects that you're most interested in, and write your project proposal! We strongly encourage you to discuss your project ideas and share your proposal with the community, so that you can get feedback and ensure that what you're writing makes sense to others. The best way to do this is to put your proposal into a collaborative editing tool like Google Docs, allow others to comment on it, and share a link to it on the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com). You can also email this mailing list if you have any questions about a project, or would like to discuss your approach with the Oppia community and get feedback. Please be specific when asking questions, since this makes it easier for us to help you.
    - **Important note:** Please read [this oppia-gsoc-discuss@ thread](https://groups.google.com/forum/#!topic/oppia-gsoc-discuss/S6Ge3vQ3cuc) carefully for details about the recommended review process. Note that you do not need to write the entire proposal before getting your first review -- see the instructions in that thread for more details. Thanks!

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

-   Choose a project you're interested in! If you have a strong interest in your project, this will help you pick up necessary skills and tackle any unforeseen difficulties that arise during GSoC.
-   Familiarize yourself with the relevant part of the codebase for your project, especially if you haven't touched it before. It's important to think about how to integrate your project with the current Oppia structure -- don't design in a vacuum.
-   Define milestones with enough detail to get a proper ETA for each milestone (so, don't just say "write e2e tests"), otherwise you run the risk of significantly underestimating the timeline.
-   Clear written communication and presentation is crucial in preparing your proposal. The proposal should show that you have a clear understanding of the codebase and the final goal of the project. Eg. In a user-facing proposal, writing about just the files that have to be changed is not enough, detailed mocks and userflows (in the form of diagrams or points) are also essential.
-   Limit proposal length. Remember a lengthy proposal is not equivalent to an excellent proposal.
-   Ensure that the problem statement is within your limits to tackle. You should make sure that what you are proposing is within your capabilities. What we have in the [project ideas section](#oppias-project-ideas-list) are suggested milestones; it is up to you to come up with a complete plan that is within your ability. i.e., students can propose whatever they want; it’s up to us to subsequently figure out (during selection) whether we’re happy about what’s being proposed.
-   Students who make the last milestone bulky normally run into issues. So, make sure that you distribute work evenly.

### What should applicants expect from mentors in a proposal review?

-   Please write your proposal on the assumption that you "own" your chosen project. From your perspective, the submitted proposal should be in as good a condition as possible before you ask for a review. Make sure you have a sufficiently good understanding of the codebase/project to find flaws in the design; don't assume that reviewers are responsible for doing this for you. Note that your proposal doesn't need to be flawless -- we expect that you might make mistakes, and reviewers will be happy to guide you on how to improve. Instead, by "as good a condition as possible", we mean that your proposal should demonstrate:
    -   Your ownership of the project
    -   The research you have put into writing it
    -   Your analytical skills
    -   Your independence in making complex decisions
-   Make sure to present solutions and ask for feedback, rather than just asking for solutions. You can do this by presenting the various solutions you came up with in your proposal, and doing an analysis of their advantages & disadvantages from the end-user perspective. Finally, choose the best solution you have and explain your reasoning behind your choice. Note that this doesn't mean that you must always have multiple ideas to solve a problem, but you should instead always explain how you reached a solution, and why is it the best one from the end-user's perspective.
-   Mentor's suggestions are "suggestions", not orders (often, reviewers may not be certain whether their suggestion is correct), so, as the proposal owner, you are welcome to decide whether to accept/reject it. In either case, when you are accepting/rejecting a suggestion provided by a reviewer, explain your reasoning and the research that led to your decision. Don't use an "appeal to authority" (e.g. "I am doing it this way because XXX said so") -- the rational analysis that underlies the decision is what's important.
-   We do not expect you to always agree with your reviewers. If you think that the suggestion doesn't suit your project, it is totally fine to explain your decision and provide reasons for it. It is always a good idea to have discussions when you have confusions, rather than simply agreeing. Note that this does not mean that we encourage you to disagree with your reviewers on everything -- this is just a suggestion to bear in mind if you get confused.
-   Please note that your reviewer may or may not be involved in the final selection process. It is also **not** the case that you need to implement all your reviewers' suggestions/requests in order to be selected. As mentioned above, it is important that you actively take help and work together with your proposal reviewers in order to prepare a strong proposal that meets the guidelines for your chosen project.

### Sample proposals from past years

If you'd like to get a sense of what a proposal might contain, please see our [GSoC 2020 page](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020) for examples of proposals that we accepted in 2020. Note that the [GSoC Proposal Template](https://docs.google.com/document/d/1fZ8yJG70zoANYGJgOv5wsIzz3arOX4Up4EJqfUU6nis/edit) was edited for 2021, so please be sure to follow the 2021 template.

_**Note:** although some of the previous years proposals are a bit on the long side, there's **no** formal length requirement for your proposal. In general, the quality of what you write is much more important than the amount of text you write, and we encourage you to write shorter proposals that still convey the main aim of the project. For the actual requirements, please see the [GSoC Proposal Template](#gsoc-proposal-template) section above._

## Types of work related to Oppia projects

In order to ensure a well-rounded engineering experience, developers will do some or all of the following depending on their project:

-   Meet with their mentors regularly
-   Meet with other contributors related to their project area
-   Read and understand parts of the code base related to their project
-   Receive code reviews for all code they write for their project
-   Write automated tests for their projects
-   Create UI mocks (if doing frontend development)
-   Write design documents (if implementing large features or introducing new systems)

We asked our previous students what they learned during GSoC 2020. Here are the collated answers:

-   Technical ability
    -   Writing clean code, while keeping in mind the requirement for the code to run in production.
    -   Working on a large codebase.
    -   Reading and understanding code from other open source organizations.
    -   Automated testing
-   Technical domain knowledge
    -   I feel more confident on working with Angular. Oppia was the first time I worked with unit, e2e tests. I feel a lot more confident in writing code now whether be it making my own projects or contributing to other open source projects.
    -   I learned lots of things about typescript and webpack.
    -   I understood how E2E tests and angular migrations worked in Oppia -- this felt very rewarding.
    -   I enjoyed finding and fixing accessibility issues.
-   Technical leadership skills
    -   How to improve in planning.
    -   Reviewing others' code
    -   Technical design skills (and validation of technical ideas)
    -   Organizing work flow, meetings management
-   Communication
    -   Putting forward my thoughts more systematically and deeply so that everyone can understand me well.
    -   Better communication skills.
    -   How to write a good proposal.
-   I've become more independent and confident over the course of this project. This is not just due to my improvement in the technical aspect, but more importantly, I now know how to start, work through and successfully finish a large scale project. I feel like I can independently and confidently work on more big projects in the future and the fear of "being lost" that I had, has now significantly been reduced.

## Selection Criteria

In order to select students for GSoC, we will mainly be looking at three things:

-   The quality of the submitted proposal
-   The quality of the applicant's previously-submitted PRs (in order to assess their ability to code, debug, break down complex tasks, etc.). Note that quantity isn't a prerequisite in itself, though contributors who've submitted multiple PRs are likely to have had more opportunities to demonstrate the abilities needed to succeed in GSoC.
-   Our prior experience working with the student (do they keep commitments, communicate well, demonstrate independence/initiative/responsiveness, help others, etc.)

We believe that strong performance in these dimensions is likely to correlate well with the student having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the GSoC program.

For the proposal, we generally look for a clear indication that the student has a good, deep understanding of the project, and has broken it down sufficiently well, in a way that makes it very likely to succeed. Some indicators that could help with this include:

-   A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating a simple, intuitive experience for end users.
-   A concrete, specific breakdown of the work to be done for each milestone. Here's an [example](https://docs.google.com/document/d/1vuwXvHOYXqfM2S2B2KIWhZrAa1PL59wJRUYsqJEd67E/edit) from a previous design doc. (Note that, in the implementation plan, the author has carefully considered and listed which tests need to be written alongside the code; this is a positive indicator.)
-   Sufficient concreteness (e.g. references to particular files and methods) to demonstrate that the applicant is familiar with both the scope of the problem and the existing codebase.
-   A description, if applicable, of how the applicant plans to mitigate risks that could potentially derail the project.
-   Clear, unambiguous communication. (This is important; your proposal will be read by many mentors!)

## Oppia's Project Ideas List

_**Note:** If you're coming to this section from an external link, please make sure to scroll up and read this entire wiki page carefully, not just this section. There's a lot of useful information on the rest of the page, including a FAQ and a section describing selection criteria. Thanks!_

The following is a list of Oppia's 2021 GSoC project ideas. (Please note that all mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted.)

You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community in order to get feedback and guidance to improve the proposal. We also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

The list of project ideas is not fixed and more projects can be added. Also, please note that **the project descriptions are not final yet** -- we are still working them out, and some of them may change a bit.

## Developer Experience

### Solving dev-workflow issues

This project will focus on tackling some of the interesting issues in the Oppia development workflow. There are 2 parts in the project:

-   The first part of the project focuses on restructuring the existing lint checks. We want to move the existing custom lint scripts to pylint.
-   The second part of the project focuses on automating the task of code ownership transfer in Oppia Org. The current process of transferring code ownership is quite manual, and also lacks flexibility in terms of the options that it provides to the codeowners, so the aim is to come up with a design to overcome those shortcomings.

**Potential Mentors:** @sajalasati, @DubeySandeep

**Consider taking up this project if you:**

1. Know how to code in Python, Javascript.
2. Enjoy refactoring code.
3. Enjoy the system designing process to come up with a solution based on requirements that covers all test cases.

**What we're looking for in the proposal:**

-   Link to one or more PRs showing contribution to the linter project or other dev-workflow issues.
-   The second part of the project is open for design, so we expect the proposed design to:
    -   cover all the edge cases of problem,
    -   be usable for codeowners to use,
    -   meet all the listed requirements.

**Dependency on Release Schedule:** None

**Suggested Milestones:**

-   Milestone 1: Ensure all the Python related lint checks are in Pylint. This includes:
    -   Moving all checks from _BAD_PATTERNS_PYTHON_REGEXP_ in `general_purpose_linter.py` to pylint, and
    -   Moving the lint check _check_that_all_jobs_are_listed_in_the_job_registry_file_ from `python_linter.py` to backend tests.
    -   Remove the PythonLintChecksManager class from the `python_linter.py file.`
-   Milestone 2: Implement the complete flow for Automating Code Ownership transfer. The design has to meet the following requirements:
    -   Allow code owners to define their future unavailability, and collect enough info from them in advance so that the ownership is automatically transferred and restored back on specified dates.
    -   Allow code owners to define custom availability for each day of the week.
    -   Each code owner could be assigned to multiple code files, so make sure we properly assign new code owners for each of those files.
        -   The expectation here is to come up with an intelligent approach for doing so, such that it’s least cumbersome and also error-prone and feasible.
    -   Ensure PR authors have proper expectations for when a code review will take place.
    -   Though the primary task here is to design the flow for temporary ownership transfer, keep the design open to also consider the possibility of permanent transfer (one-time transfer).

To understand the current flow of making a code ownership transfer and get ideas for implementing the project, please see [this doc](https://docs.google.com/document/d/1xXXjUVd0dHXWrUTGw5k1Rpsr6w4oLqDtRzBFP7hkMxw/edit?usp=sharing).

---

### Move custom JS\TS lint checks to eslint

The Oppia development workflow uses lint checks to help detect style errors before they reach the review phase. This project aims to migrate the JS\TS checks from python to eslint checks and implement the remaining E2E lint checks in the codebase.

**Potential Mentors:** @Hudda, @DubeySandeep

**Consider taking up this project if you:**

1. Know how to code in Python, JavaScript.
2. Enjoy refactoring code.

**What we're looking for in the proposal:**

-   Link to one or more PRs implementing custom eslint checks.

**Dependency on Release Schedule:** None

**Suggested Milestones:**

-   Milestone 1: Migrate JS\TS lint checks to custom Eslint checks [#10816](https://github.com/oppia/oppia/issues/10816). Migrate some of the _BAD_PATTERNS_JS_AND_TS_REGEXP_ to custom eslint checks from _general_purpose_linter.py_.
-   Milestone 2: Implement 4 E2E lint checks from [#8423](https://github.com/oppia/oppia/issues/8423) and move remaining _BAD_PATTERNS_JS_AND_TS_REGEXP_ to custom eslint checks.

---

## Data and stability team

### Implement schema validators for the handler params

We would like to robustly validate all arguments passed to GET/POST/DELETE handlers and immediately raise a 400 error if an invalid argument is passed. Currently, the handler params are being verified only in some specific cases and there is no unified way to parse more complicated structures like lists and dicts.

This project should add the framework for adding schema validation to all handlers, lint checks ensuring that for newly added handlers schema must be added, and documentation about the schema validation. Then the schema validation should be enabled on at least a part of our current handlers.

The schema validation should be implemented based on schema_utils.py (possibly with additional extensions) or through some third party library. You can take a look at a [list of possible third-party libraries](https://docs.google.com/document/d/1s_nVczNVGgwO8-Jo2JNcoVla2x0-QYuwPmA2u0w9UsQ/edit?usp=sharing) for inspiration. Some changes to frontend code might also be required in order to unify how we send data between backend and frontend.

**Potential Mentors:** @vojtechjelinek, @rohitkatlaa

**Consider taking up this project if you:**

-   Know how to code in Python
-   Have knowledge of how different HTTP methods work
-   Know how to code a bit in TypeScript and Angular

**What we're looking for in the proposal:**

-   Comparison of the pros/cons of using third-party library or schema_utils.py for the schema validation.
-   An explanation on how you want to introduce the schema validators to the codebase.

**Dependency on Release Schedule:** None, although it would be useful to implement most of the stuff before the August release so that the changes are tested.

**Suggested Milestones:**

-   Milestone 1: Implement a framework for schema validation on handlers, add lint checks for new handlers, add documentation about schema validators. Implement schema validators on handlers in
    -   _admin.py_
    -   _classifier.py_
    -   _classroom.py_
-   Milestone 2: Implement schema validators on handlers in
    -   _collection_editor.py_
    -   _collection_viewer.py_
    -   _concept_card_viewer.py_
    -   _contributor_dashboard.py_
    -   _creator_dashboard.py_
    -   _cron.py_
    -   _custom_landing_pages.py_
    -   _editor.py_
    -   _email_dashboard.py_
    -   _features.py_
    -   _feedback.py_
    -   _improvements.py_
    -   _incoming_emails.py_
    -   _learner_dashboard.py_
    -   _learner_playlist.py_
    -   _library.py_
    -   _moderator.py_
    -   _pages.py_
    -   _platform_feature.py_
    -   _practice_sessions.py_

---

### Make backend code typed

In the frontend, we have fully-typed TypeScript code in place (although there we still need to finish the implementation of strict typing). In the backend, we should also start using types.

This project should first add Python 3 type checking into the pre-push checks and CI checks (although the current codebase is in Python 2, it will be migrated to Python 3 before GSoC), add documentation about adding types and make sure that types need to be defined for newly added files and code. As for the next part, the assets/constants.ts (constants that are used both in frontend and backend) file should be transformed to protobuf format so that we can leverage typing for our constants too. The last part of this project should implement types for files in core/storage, core/platform, and root folder (feconf.py, utils.py, etc.). In some places we currently use lists of allowed values, these should be transformed to enums.

The checking of type annotations should be done with mypy (or any other typing alternative that implements [PEP484](https://www.python.org/dev/peps/pep-0484/), like pytype or Pyre) checks, preferably we should also implement strict mypy checks, or subset of strict checks that could work even if only a part of the codebase is typed.

**Potential Mentors:** @vojtechjelinek, @rohitkatlaa

**Consider taking up this project if you:**

-   Know to work with types in Python 3 and how to use even more complicated typing constructs like `Optional` or `Union`

**What we're looking for in the proposal:**

-   An explanation on how you want to introduce the typing to the codebase.
-   An explanation on how you want to introduce the protobuf for the constants.

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1: Implement Python type checking into the pre-push checks and CI checks. Replace assets/constants.ts with protobuf and implement transforming protobuf file to TypeScript and Python constants.
-   Milestone 2: Implement types for the core/storage, core/platform, and root folder.

---

### Angular Migration

#### Note: This project can change a lot based on the progress of migration made till the community bonding period. We will try our best to make sure that the project doesn't change. That said, if such last-minute changes are troublesome for you, please consider applying to other projects.

The build process that Oppia uses to prepare the files for reliably serving the site was changed quite a lot in the last years: we introduced webpack, changed our build scripts from bash to Python, and also upgraded some libraries. Since a lot of these changes affected the build process and sometimes weren’t accounted for, the build process is now clunky and quite hard to understand.

This project’s aim is to simplify the build process by migrating to Angular-CLI, making it easy for developers to work with it and unifying the multiple entry points that need to build some files (backend tests, e2e tests, frontend tests, local dev server) as much as possible. After the project is complete, all the build-related stuff should be handled exclusively with the Angular CLI.

**Note: If the migration of all directives and services is not complete before the start of GSoC, the student may have to migrate the remaining files. Based on the number of files left, we might remove the requirement of the migration to Angular-CLI (if the student is ok with the project be downsized). Hence, there could be a case that you research a lot about Angular-CLI and may not want to/ get to work on it during GSoC. Please consider these before applying to the angular migration project.**

**Potential Mentors:** @vojtechjelinek, @seanlip, @dubeysandeep, @srijanreddy98

**Consider taking up this project if you:**

-   Want to critically analyze and then propose a new architecture for our build process.
-   Enjoy refactoring previously-written code.

**What we're looking for in the proposal:**

-   Having a good understanding of the Angular router.
-   Having an in-depth understanding of Angular CLI and the angular build system.
-   PRs related to angular migration that demonstrates your ability to migrate from AngularJS to Angular 2+

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1: Unify the entry points by using the angular router and have only one entry point in the webpack config file. Specifics of the previously existing entry points should be handled by the angular router. The strategy for top-level routing should be lazy loading.
-   Milestone 2: Move the frontend build process from webpack to angular-cli.

---

### Improve frontend type system

Our frontend codebase is fully typed, but our typing doesn’t pass strict TypeScript checks. In this project you should firstly change the strict TypeScript config file so that all newly added files need to be strictly typed and then you should introduce strict typing for around 120 twins of files and tests for those files (so 240 files all together). You can get the files that should be handled from the [UpgradedServices.ts](https://github.com/oppia/oppia/blob/develop/core/templates/services/UpgradedServices.ts), you should start with files from the lower topological level and then move up.

**Potential Mentors:** @vojtechjelinek, @rohitkatlaa, @dubeysandeep

**Consider taking up this project if you:**

-   Enjoy coming up with cool patterns to simplify development workflow.
-   Are interested in critically analysing various solutions to a single problem.

**What we're looking for in the proposal:**

-   Links to one or more PRs in which you added types for TypeScript files. Overall, these PRs should show you adding tests to fully cover at least four TypeScript files.

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1: Change the TypeScript config file so that all newly added files need to be strictly typed, introduce typing for 55 twins of files and tests for those files (so 110 files all together).
-   Milestone 2: Introduce typing for 65 twins of files and tests for those files (so 130 files all together).

---

## Automated QA team

### Write Frontend Tests

This project aims to write frontend tests to fully cover each service, directive, and component. When you begin, some files may have tests that incompletely cover the code, while others may have no tests at all. Many of the files you write tests for will contain directives, which you will need to convert to components first. Much of the past work writing frontend tests has been tracked by [oppia/oppia#4057](https://github.com/oppia/oppia/issues/4057). You should also look at the [blog post](https://mari-zangue.medium.com/my-journey-through-gsoc20-with-oppia-9eb6b27e7a02) by a GSoC student last year who worked on a similar project. This is a good reference, as is our [wiki page](https://github.com/oppia/oppia/wiki/Frontend-unit-tests-guide). It outlines best practices and standard guidelines you should follow.

The project will involve writing a lot of tests. The proposals must contain a concrete plan for how you will cover all of your assigned code in the allotted time. For your reference, here are the line counts as of March 8, 2020:

|           | Total Lines | Covered Lines | Uncovered Lines |
| --------- | ----------- | ------------- | --------------- |
| Component | 7646        | 7254          | 392             |
| Directive | 10794       | 2658          | 8136            |
| Other     | 9828        | 9028          | 800             |
| Service   | 11636       | 10247         | 1389            |

These line counts are calculated from the `karma_coverage_reports/lcov.info` file generated by our frontend test coverage checks. You can parse this file using the functions in `scripts/check_frontend_coverage.py`. For this project, we won’t be worrying about the “Other” files, so we have 9,917 lines to cover in total.

**Potential Mentors:** @kevintab95, @aks681, @iamprayush

**Consider taking up this project if you:**

-   Are interested in testing (since most of the project will involve writing unit tests).
-   Have the ability to read through someone else’s code, in order to understand what needs to be tested. (This project will involve reading through a lot of Oppia's source code.)
-   Like to handle technical challenges! It is very likely that you'll run into problems while trying to test the code as is, and you will almost certainly need to research and come up with solutions to test certain constructs.

**What we're looking for in the proposal:**

-   Links to one or more PRs in which you added tests for the frontend code. Overall, these PRs should show you adding tests to fully cover at least one service. They should also show you migrating at least one directive to a component and then testing that component.
-   A clear demonstration that you can migrate any directive and write tests for any service component. We won’t be assigning specific files until after we have selected students because the files that need to be covered are changing constantly. Therefore, it is critical that you show us you can handle any code we assign you.

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

We are looking for 1-3 students to work on this project. Each student will work on covering approximately 3,300 lines of frontend code. You are free to let us know if you have any preferences for what code to work on, but we may not be able to honor your requests.

-   Milestone 1: Fully cover half of the assigned code.
-   Milestone 2: Fully cover all of the assigned code.

---

## Learner and Creator Experience team

### Generalised migration flow for all models using JsonProperty fields

Each model type (topic, story, exploration, etc.) currently has its own migration system, and all these systems are similar. We would like to consolidate this by having the migration functionality come "out of the box" when introducing a new JsonProperty field for any model. This involves implementing a generalized migration system for all model types, and moving the migration methods to their own files.

**Potential Mentors:** @kevintab95, @aks681, @iamprayush

**Consider taking up this project if you:**

-   Like to learn about how schema migrations are done.
-   Enjoy consolidating repeated logic and making it easier for developers to write code.

**What we're looking for in the proposal:**

-   A clear plan for how the existing migration logic can be refactored.
-   How to enforce that any model with a JsonProperty field uses the new migration system?

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1:
    -   Introduce the generalised migration system for all models that may need migration.
    -   Write backend tests for the new code.
-   Milestone 2:
    -   Write a linter to ensure that all models that require a migration flow uses the newly introduced migration system.

---

### Handling Exploration updates in suggestions and ‘lost changes’ improvements

There are several serious issues with current saving/migration workflows in the exploration editor that can occasionally cause loss of work. In particular:

-   When an exploration is updated, any existing suggestions in the feedback tab should be updated accordingly. Currently, such suggestions are not updated, resulting in a version mismatch and a loss of work when the exploration creator subsequently tries to apply the suggestion.
-   When changes cannot be saved to an exploration, a "lost changes" modal pops up so that the creator can make a copy of their edits and then reapply them. However, the code for this modal is not robust, and in particular it does not take into account draft changelists that were stored in an older format. Thus, when it tries to display such drafts, it breaks and ends up not showing anything.

**Potential Mentors:** @kevintab95, @aks681, @iamprayush

**Consider taking up this project if you:**

-   Like to learn about how schema migrations are done.
-   Interested in writing MapReduce jobs to handle existing data on the server.
-   Enjoy full-stack development.

**What we're looking for in the proposal:**

-   Detailed plan for handling existing data on the server including how to handle incompatible or invalid suggestions.
-   Describe in detail the scenarios where the “Lost changes” modal might break and provide a plan to handle this.

**Dependency on Release Schedule:** Yes, since the features affect the editor flows directly they need to be properly tested and issues can arise in the release.

**Suggested Milestones:**

-   Milestone 1
    -   Handle changes to existing suggestions when exploration is updated.
    -   Write a job to handle existing old suggestions on the server.
-   Milestone 2
    -   Fix ‘lost changes’ modal breaking when draft changes are of an older format.

---

### Improve Exploration save flow: Syncing edits in the background

-   When multiple creators try to edit an exploration at the same time, a case may arise where some changes are not saved because the exploration version in the browser and server don’t match. It would be good to have the changes synced in the background, especially if the changes are unrelated (often creators work on different parts of the exploration and it may not intersect). When there are no merge conflicts it should be possible to merge.
-   Autosaving fails when there is no connectivity. Have a way for creators to continue work on their explorations even if they are offline or the connection is flaky and then save their progress automatically when they have reliable network access.

**Potential Mentors:** @kevintab95, @aks681, @iamprayush

**Consider taking up this project if you:**

-   Enjoy full-stack development.
-   Interested in exploring technologies that enable offline functionality.
-   Are excited about enabling real-time collaboration between creators within the application.

**What we're looking for in the proposal:**

-   Detailed plan for syncing exploration changes and handling merge conflicts.
-   Include user journeys and mocks for all user-facing changes.

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1
    -   Introduce functionality such that edits made by a user should be propagated to all clients. The changes should be applied if the changes are unrelated or else the user should be informed of the merge conflict (and a suitable way to handle it should be offered).
-   Milestone 2
    -   Enabling the exploration to work offline in case of connectivity issues.

---

### Enhancing the Skill functionality

This is a collection of Github issues that are related to the Skill functionality.

1. Skills list in the concept card editor takes too long to load [#10822](https://github.com/oppia/oppia/issues/10822)
    1. Maybe we can use the filter from the dashboard. See also: Implement a reusable sort/filter list view for skills [#5670](https://github.com/oppia/oppia/issues/5670) ([#5670](https://github.com/oppia/oppia/issues/5670))
2. Add validation for `MAX_SKILLS_PER_QUESTION` when creating questions and add question skill links [#6956](https://github.com/oppia/oppia/issues/6956)
3. Allow bulk assigning skills to a topic in the topics + skills dashboard [#10668](https://github.com/oppia/oppia/issues/10668)
4. Edits lost on Topic page when adding skills [#10599](https://github.com/oppia/oppia/issues/10599)
5. While creating skill/topic- A blank tab is opened and loads after few seconds which misleads user [#9807](https://github.com/oppia/oppia/issues/9807)
6. Topics and Skills Dashboard Does Not Show Total Number of Skills [#10278](https://github.com/oppia/oppia/issues/10278)
7. Long skill names in the skills list in the subtopic editor seems to break alignment [#10892](https://github.com/oppia/oppia/issues/10892). May need to be handled in other areas in the editor as well.

**Potential Mentors:** @kevintab95, @aks681, @iamprayush

**Consider taking up this project if you:**

-   Enjoy full-stack development.
-   Interested in owning and improving one of the core functionalities used by curated lessons at Oppia.

**What we're looking for in the proposal:**

-   Detailed explanation for speed-related improvements should be provided.
-   Include mocks for all user-facing changes.

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1: Complete 1–3.
-   Milestone 2: Complete 4–7.

---

### Integrating the Oppia blog with Oppia.org

Today’s Oppia.org blog is currently hosted on a separate site, Medium. We would prefer to have the blog page directly on Oppia.org so that it is directly connected to the rest of the site. The aim of this project is to add a “blog” page hosted on Oppia.org, and implement a simple interface for editing it.
Mocks for the new pages can be found [here](https://xd.adobe.com/view/9bb82409-cdca-432a-b11c-88324643e2c0-ceeb/grid).

**Potential Mentors:** @aks681

**Consider taking up this project if you:**

-   Like working with the full stack, which includes creating storage models and frontend views.
-   Owning a specific section of the codebase.
-   Like to create new user flows and UX.
-   Are interested in working with Python, Angular (Typescript) and HTML.

**What we're looking for in the proposal:**

-   There should be plans to handle both the backend and frontend of the blog integration.
-   Should provide a view to transfer existing blogs from Medium to this. This can be a manual transfer, though it should be possible.

**Dependency on Release Schedule:** Yes. M2 would need to be tested in release as that includes the addition of new pages.

**Suggested Milestones:**

-   Milestone 1: Create the storage model and complete the backend for storing the blog post and author data.
    -   Model should store the publishing date.
    -   Blog posts should be searchable via their titles.
    -   Each blog should have tags that can be added by the user.
    -   There should be separate “Save Draft” and “Publish” functionalities.
    -   HTML meta tags can also be added to each blog post.
-   Milestone 2: The frontend editor UI is done which should allow moving the Medium blogs to Oppia (so, any visible fields that Medium has should be handled as well).
    -   The “blog dashboard” should be accessible from the navbar/profile dropdown.

---

### Redesigning and updating the learner dashboard

Update the learner dashboard to incorporate planning and recommendation of topics, stories and skills to the learners. The following features should be added as part of the project (design for the new pages can be found [here](https://xd.adobe.com/view/b54892aa-dbe6-49cf-bc4f-9bb8c77de619-e01b/grid). NOTE: in the to-do list, this project aims to only add the "Learn" section and tracking stories. The "Mastery" related goal items need not be done.):

-   A customizable todo list, which would consist of the next incomplete story in topics that the learner has selected (selected in the goal editor below).
-   The ‘edit’ button for the above todo list would lead to a ‘goal editor'; where the learner can choose which all topics to track their progress on, and the next incomplete story in those topics will be filled in the todo list (mentioned above).
-   A separate progress tab in the learner dashboard where the learner can track their progress across topics. In each topic, it should show their mastery in the various subtopics and the progress in the stories in the topic. The mocks for this page will be given.

**Potential Mentors:** @aks681

**Consider taking up this project if you:**

-   Are interested in thinking critically and designing a full user flow from scratch, by thinking from the user's perspective.
-   Like working with the full stack, which includes creating storage models and frontend views.
-   Owning a specific section of the codebase.
-   Are interested in working with Python, Angular (Typescript) and HTML.

**What we're looking for in the proposal:**

-   Any new storage model/modifications to existing storage models is explained.
-   How you’ll handle the features mentioned in the description.

**Dependency on Release Schedule:** Yes, would depend on release for both milestones, since major frontend changes would be there for both.

**Suggested Milestones:**

-   Milestone 1: Redesign the learner dashboard except the todo list and goals section. So, the progress tab and its related backend changes (if any) should also be done in this milestone, or justified, if moved to the next milestone.
-   Milestone 2: The backend model, services and domain changes and the corresponding frontend changes for adding the todo list and goal editor is done.

---

### Customize difficulty for practice sessions

Currently, in the Practice tab in the topic viewer page, a learner can choose the subtopics to practice and practice questions on them. This project aims to add more customizability where the learner can fine tune the difficulty on which the questions are asked, from each subtopic that they want to practice. Following are main objectives:

-   Mastery should be calculated at the subtopic level, as the average of mastery of all skills in the subtopic and should be displayed in the topic viewer page.
-   Practice sessions should be made more independent and it’s difficulty level also customizable, in the sense that the learner can set the difficulty range of questions that would be asked in the practice session, at a subtopic level.
-   These should also be represented by cards. So, in the topic viewer’s Practice tab, there are some cards that we recommend (eg: Easy Questions on Subtopic A, Hard Questions on Subtopic B etc.), which the learner can click to quickly start a session or they can fine tune difficulty per subtopic themselves and start a session as well.
-   These cards should be shown based on a learner’s mastery in a subtopic. For example, if a learner has < 50% mastery in a subtopic, we should only show Easy and Easy/Medium practice cards and not Hard etc.

**Potential Mentors:** @aks681

**Consider taking up this project if you:**

-   Are interested in thinking critically and modifying an existing user flow to better suit the learners.
-   Like working with the full stack, which includes creating storage models and frontend views.
-   Owning a specific section of the codebase.
-   Are interested in working with Python, Angular (Typescript) and HTML.

**What we're looking for in the proposal:**

-   Any new storage model/modifications to existing storage models is explained.
-   How you’ll handle the features mentioned in the description.

**Dependency on Release Schedule:** Yes, would depend on release for M2, since the full product would be launched then.

**Suggested Milestones:**

-   Milestone 1: Complete the backend and frontend domain and other infrastructure changes to handle different practice sessions customizable by the learner based on difficulty.
-   Milestone 2: Add the topic viewer changes and cards, as mentioned in the description so that the full practice session user flow is done.

---

## Contributor Experience team

### Contributor Dashboard Responsive UI

The Contributor Dashboard (oppia.org/contributor-dashboard) allows users to submit suggestions for translations and practice questions which are then reviewed and accepted/rejected. Currently, the dashboard has only been developed with a desktop view in mind. We want users to have a smooth experience on any platform/device.

In this project, you will be given design mocks for which to implement a responsive UI for the contributor dashboard page and related user flows. You will not need to create the mocks yourself. The mid-fidelity mocks can be found [here](https://www.figma.com/file/FNA3qSJP2dLmQMMnjgMLQI/Contributor-Dashboard-(final-draft)?node-id=0%3A1). The high-fidelity mocks can be found [here](https://xd.adobe.com/view/8eeae0ca-4aaa-4b6e-84e2-a80796089530-dbb9/?fullscreen).

#### Contributor Dashboard Resources
* See the [creator documentation](https://oppia-lesson-creator-documentation.readthedocs.io/en/latest/contributor/contribute.html) for a tutorial on contributing translations and practice questions via the contributor dashboard.
* See the [Admin Playbook](https://docs.google.com/document/d/1VqNiJttq85YyR6cQkd8M9lGGkOP8OlUlkI37Xw6SovM/edit?usp=sharing) for instructions on enabling the contributor dashboard on a local dev server. 
* See [this](https://docs.google.com/document/d/1JYX4nvTcblaVVYAlTi7rApE0lWSBx0v_ZCCr_8WW4Wc/edit?usp=sharing) doc for instructions on populating sample data on a local dev server.

The UI elements that need to be updated are as follows.

#### Landing Page

-   Page tab navigation bar (for navigating between the "My Contribution", "Translate Text", and "Submit Question" tabs)
-   User header with review rights details
-   Side navigation bar for reviewers and contributors
-   Review modals for question and translation suggestions
-   Submitted contribution modals
-   Opportunity card pagination

#### Translate Text Tab

-   User header with translation language selection
-   Translation opportunity card elements
-   Translation modal

#### Submit Question Tab

-   User header
-   Question opportunity card elements
-   Question editor in question suggestion modal

**Potential Mentors:** @kevintab95, @aks681

**Consider taking up this project if you:**

-   Like to work collaboratively with others in different domains, working together to create a complete engineering product
-   Are interested in working on the frontend with Angular, Typescript, HTML, CSS
-   Respect the user and are committed to debugging and tweaking in response to feedback

**What we're looking for in the proposal:**
- A plan for minimizing code duplication, e.g. if we're planning on writing a lot of the same CSS across files, how can we structure the code in such a way so that we only write it once?
- A short summary of the proposed changes for each frontend component. Most of the changes will likely be static style changes, but if say you need to introduce new Angular components or files, then outline these changes with justifications for why they are needed.
- Some consideration on testing—is there a way to automate testing of the responsive design?
- The milestones broken down into clear tasks with PR open/merge time estimates.
- Clear, concise, organized writing. See https://developers.google.com/tech-writing/overview for technical writing tips. 

**Dependency on Release Schedule:** Yes. Mobile UI changes will need to be pushed to test or production servers to be tested more widely in order to catch edge cases in user journeys.

**Suggested Milestones:**

-   Milestone 1: Implement the mobile UI for the contributor dashboard landing page
-   Milestone 2: Implement the mobile UI for the translation and question pages

---

## Android team

### Developer Options Menu

The Oppia-Android application needs a developer options menu so that developers can alter app settings or stored data in real time. This is important because during PR reviews and testing there are cases where we need to create data like finishing a topic crashing the app, and doing this manually takes up a lot of time (or even isn't possible) and therefore having a developer menu where we can do these database related changes easily will make development and testing process easier. Note that a core requirement of this project is to ensure any implemented options do not "punch holes" in the existing app (e.g. if a user is using the production version of the app, it should not contain any code pertaining to the developer menu including the functionality needed to enable the debug functionality).

This option should be visible as a top-level navigation item in the navigation drawer for all profiles, but only if the running app is a `Debug` flavor of the app. It's expected that this feature will only work on Bazel versions of the app and not Gradle since the former lets us properly exclude functionality from certain builds.

The options/functionality that should be implemented are:

-   The ability to mark each of the following completed with all versions of each as available options (note that this will require validation to make sure the app doesn't end in a broken state):
    -   Topics
    -   Stories
    -   Chapters
-   View analytic event logs
-   App-wide behavior changes
    -   Force all hints/solutions on by default (as a toggle)
    -   Force app to run in wifi/cellular/no network cases irrespective of the actual state on the phone (though we need to take care to make sure impossible cases don't happen, such as forcing wifi/cellular when there is no connectivity at all)
-   An action to crash the app (for investigation & logging purposes)

We have mocks ready for this project, you can view them [here.](https://xd.adobe.com/view/e8aa4198-3940-47f9-514a-f41cc54457f6-9e9b/screen/5ced965e-1a0a-48cf-85dd-f28ba68f0b99/)

**Potential Mentors:** @Sarthak2601, @anandwana001, @rt4914, @BenHenning

**Consider taking up this project if you:**

-   Want to gain exposure to implementing new Android UIs
-   Like to dig into large systems & write code with clean separation
-   Want to learn about the Bazel build system
-   Want to support other developers by making their lives easier

**What we're looking for in the proposal:**

-   Proof that you can build the entire project on Bazel.
-   Some PRs related to UI related work and test cases in app layer.
-   A logically organized document written in a way that's easy to understand, and doesn't make any assumptions about what the reader knows or doesn't know (e.g. make sure any implied context is specifically called out)

**Knowledge/Skills Recommended:**

-   Familiarity with Android development (esp. UI), particularly using Kotlin
-   Strong capacity to read/understand existing code
-   Good sense for modularizing code since that will be a key part of making sure this project does not interfere with the existing app structure
-   Familiarity with Bazel will help, but it's not expected students will know Bazel ahead of time

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1: Introduce the initial UI & an option to crash the app as a proof-of-concept. This menu should be disabled by default in non-developer builds of the app. We suggest using Bazel modules & Dagger for this purpose. Add features that will not require broad changes in the codebase: marking specific topics/stories/chapters completed, and viewing event logs.
-   Milestone 2: Add support for features that require broader changes: forcing connectivity type, and forcing hints/solutions to automatically show. Note that the functionality used elsewhere in the app to support this should be built in such a way where it's not included in production builds of the app, and in a way that doesn't "punch holes" in the app. We suggest considering how staging is done in milestone 1 as a baseline for determining how to approach the work for this milestone.

---

### Static Analysis Checks + Improvements

One key part in ensuring a development team reaches optimal efficiency is by ensuring there are reasonable checks in place to avoid regressing previous fixes, reducing trivial verification during code reviews, and ensuring that team members are utilizing best practices. A popular way to achieve this is with static analysis tools like linters. While the Oppia Android team has linters & automated tests implemented, we'd like to fill in some of the gaps in our static analysis tooling by providing ways to enforce best practices & further simplify code reviews.

Suggested checks to add (note that these are picked to provide a wide variety of static analysis support so that the team can add many more checks in the future):

-   Verify activities have accessibility labels
-   Verify that TODOs correspond to current, open issues on GitHub. We should also run this particular analysis check when an issue changes so that we can detect if issues are closed before their TODOs are addressed & then reopen the issue.
-   Verify all production files have a corresponding test file
-   Ensure activities/fragments/views can't be used outside of the app module, or in testing
-   Ensure KDocs are present for every non-private class, method, and field (even trivial ones). We expect that this will require an extension to ktlint.
-   Ensure we can easily add future checks on file names or file contents using RegEx (note that both checks should be able to be matched against filepath patterns, e.g. we may want to verify that all layout XML files don't use marginLeft)
-   Ensure all XML files follow our XML style guide

**Potential Mentors:** @rt4914, @anandwana001


**Consider taking up this project if you:**

-   Like really clean code & want to keep it that way
-   Want to help other developers reduce mistakes that could cost the team valuable development time, or in the worst case cause issues for users
-   Want to make code development & reviewing easier

**What we're looking for in the proposal:**

-   A good demonstrated foundation for GitHub Actions (either via PRs or strong explanations & references go existing documentation)
-   Solid explanations for each check that we want to implement & well-reasoned justifications for why each one is important (e.g. what its expected impact is/what sorts of situations it will prevent the team from running into)
-   A logically organized document written in a way that's easy to understand, and doesn't make any assumptions about what the reader knows or doesn't know (e.g. make sure any implied context is specifically called out)

**Knowledge/Skills Recommended:**

-   Familiarity with style guides is helpful, though the student will need to become familiar with the team's style guide in order to make progress
-   Familiarity with GitHub Actions will help
-   Understanding of regular expressions strongly recommended
-   Knowledge of scripting, particularly using Kotlin

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1: Introduce improved linter support: KDoc & XML style enforcement. These checks should be run in GitHub Actions. Introduce support for custom RegExp checks for file names & contents that runs in GitHub Actions with a check that verifies activities are defined with accessibility labels.
-   Milestone 2: Add a GitHub Actions check to verify that production files have corresponding test files. Introduce TODO verification. This check should be run in GitHub Actions and triggered both for PRs and for issue changes where failures in the latter should automatically reopen the issue.

---

### End-to-End Testing Support

Oppia Android's current testing corpus includes unit tests using the Robolectric testing framework & integration tests using the Espresso testing framework (to ensure that the app operates as expected in a real Android environment). The current tests have a few limitations: they do not correctly facilitate cross-activity navigation flows which actual users will be triggering, and they do not verify that the app can interact with Oppia's backend correctly.

To prepare for the global launch of the app, we need end-to-end tests that:

-   Verify that the app works as a user would expect by playing through select critical user journeys
-   Verify that the app operates as expected when interacting with a local developer instance of the Oppia backend server

We expect that the tests will be written using UiAutomator & are set up for interacting with a local development server (see [relevant documentation](https://developer.android.com/studio/run/emulator-networking.html)).

Note that this project requires running Linux with virtualization support (in order to run an Android emulator). You will need to make sure your computer supports [KVM](https://help.ubuntu.com/community/KVM/Installation) and is running Linux.

**Potential Mentors:** @anandwana001, @BenHenning

**Consider taking up this project if you:**

-   Enjoy thinking like a user or QA tester, and want to ensure the user's experience is well-protected by excellent end-to-end tests
-   Want to get a good understanding of how the cross-stack integrations between the Android app and web backend work
-   Want to learn how to write instrumentation tests (particularly with UiAutomator), or understand what's involved to write end-to-end tests

**What we're looking for in the proposal:**

-   Submitted Android PRs that include app module tests with Espresso actions (to demonstrate familiarity with writing these tests)
-   Verification (e.g. a screenshot) that you can build the app with Bazel locally & run app module tests
-   Verification that your local development machine is running Linux & supports KVM (e.g. by running [kvm-ok](http://manpages.ubuntu.com/manpages/bionic/man1/kvm-ok.1.html) and including a screenshot of the output)
-   A clear plan on what type of test data support needs to be added to the backend, and how this will be done in a way where it can be loaded from outside the server (i.e. via a parameter passed to `start.py`)
-   A logically organized document written in a way that's easy to understand, and doesn't make any assumptions about what the reader knows or doesn't know (e.g. make sure any implied context is specifically called out)

**Knowledge/Skills Recommended:**

-   Kotlin
-   Python (this project will involve changing Oppia's backend)
-   Bazel may help (the end-to-end tests must be written using Bazel--we don't plan to use Gradle)
-   Android testing (especially Espresso and/or UiAutomator), or other end-to-end testing (such as Protractor)

**Dependency on Release Schedule:** None, since the backend changes are only needed for developer runs of the app.

**Suggested Milestones:**

-   Milestone 1: Introduce developer-only functionality in the Oppia backend to prepopulate test topics, stories, chapters, explorations, revision cards, skills, and questions. Remodularize the necessary parts of the app to support connecting to a developer instance of the Oppia backend.
    -   Note that the test data does not need to actually make sense, it just needs to be able to ensure key test scenarios can be tested in the app
    -   Note that the test explorations can leverage the existing test explorations [bundled](https://github.com/oppia/oppia/tree/develop/data/explorations) with the backend, but it's recommended the student create a test exploration that has proper compatibility with the Oppia app (see [Android's test explorations](https://github.com/oppia/oppia-android/tree/develop/domain/src/main/assets) for an idea on exploration compatibility)
-   Milestone 2: Set up infrastructure for end-to-end testing using UiAutomator & Bazel. Write end-to-end tests for downloading & playing through one exploration

---

### Implement feature flags & platform parameters

With a large scale system like Oppia, we sometimes have features that contain several points of integration in the codebase, and/or require additional data priming or migrations ahead of the feature being released. These features often span multiple releases and thus require feature flags to gate integration points to ensure that the feature is not partially released ahead of schedule. Moreover, these features often require migrations which need to be run in specific releases due to new versions being made in irreversible data structures (e.g. explorations).

In order to release these types of features in a smooth manner, we want to be able to put these features behind feature flags that are enabled in specific builds (compile-time) and can be enabled dynamically (at runtime). This project aims to introduce compile-time & runtime feature gating for the Android app, leveraging existing runtime gating functionality supported on Oppia web.

Note that this project actually involves introducing what are called platform parameters. These are parameters that can be one of several data types (e.g. strings, integers, booleans). We plan to use the boolean types for gating features as described above, but the other parameters are essential in order to ensure the app is reasonably configurable for many different circumstances (include deprecations). The work difference between specifically supporting booleans & other data types is expected to be small.

**Potential Mentors:** @vinitamurthi, @Sarthak2601, @BenHenning

**What we are looking for in the proposal:**

-   An overall system design for reading, storing, and providing feature flag values to the Android app
-   A clearly defined solution for organizing platform parameters at compile-time (e.g. using Dagger modules)
-   A solution to fetch the Oppia backend’s platform parameters at runtime
-   A logically organized document written in a way that's easy to understand, and doesn't make any assumptions about what the reader knows or doesn't know (e.g. make sure any implied context is specifically called out)

**Consider taking up this project if you:**

-   Are interested in understanding how to release large scale features in a production system
-   Would like to work on a project that touches several layers of the system. This means that you would get a greater understanding of how all the pieces of the app fit together and how they work with the backend too!

**Knowledge/Skills Recommended:**

-   Kotlin
-   Python
-   Architectural design
-   Dagger/dependency injection

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1: Introduce platform parameter system that initially has support for compile-time definitions (e.g. using Dagger modules, Dagger constants, ). The resulting platform parameter support should be built such that we can easily combine the compile-time gating with runtime parameters.
-   Milestone 2: Introduce runtime parameter support by hooking up to Oppia backend's platform parameter API & connecting these flags back to the predefined compile-time parameters. Note that the lifecycle of these parameters need to be carefully managed: they should not be applied until the app restarts. This part of the project will include caching results from the server, and introducing a lightweight synchronization mechanism so that the app periodically verifies that its copies of the parameters are up-to-date. When the device is offline, the flags should have appropriate defaults for the runtime parameters. (See the [design doc of Dynamic Feature Gating](https://docs.google.com/document/d/1FjbG2Cb0OnDVuE36jzux2Sn0sybMQozkk3hjkfeMoC0/edit#heading=h.c6v1d3lnu8sd) for a [definition of default platform parameter values](https://docs.google.com/document/d/1FjbG2Cb0OnDVuE36jzux2Sn0sybMQozkk3hjkfeMoC0/edit#heading=h.ko3wdifj5byi)

---

### Implement lightweight checkpointing

Oppia's lessons can require between 15 minutes and an hour of time depending on a number of factors from learners: understanding of the material, literacy capabilities, and general focus. One potential behavior in the app is that we don't save the user's progress if they navigate away from an exploration (lesson) which, given how long lessons can take, is expected to be a frustrating experience. To mitigate this, we'd like to introduce support for a lightweight checkpointing system wherein users' saved state is fully retained if they navigate away from a lesson & back.

This project is actually part of a larger & broader project happening both in Android & web codebases to introduce the idea of checkpointing: letting learners save their progress at specific points & return to those points. Note that lightweight checkpointing is different than this:

-   Lightweight checkpointing is an Android-only feature
-   Lightweight checkpointing involves saving progress & resuming _wherever_ the learner stops playing (rather than being taken to a specific moment in the lesson)

This project is being spec'd out currently in a [PRD](https://docs.google.com/document/d/1d8yjwz76mngtsPRxC7fubgLKg8mfA7kG1sWRWdbiaVw/edit#) (product requirement document). The expectation is that the student's proposal will summarize the product requirements for the lightweight checkpointing part of this feature, and specify the entirety of how it should be built.

**Potential Mentors:** @BenHenning, @aggarwalpulkit596, @rt4914

**What we are looking for in the proposal:**

-   A clean & consistently layered design that outlines a plan to save & restore lesson state across app instances, accounting for potential changes in the lesson proto structure
-   Utilizing existing technologies in the codebase rather than solutions typically found in blogs or stack overflow (e.g. the proposal should use PersistentCacheStore rather than SharedPreferences or Room)
-   Clear solutions for handling all edge cases in this project (e.g. cases when upgrades fail, or crashes)
-   An analysis for how much disk space each individual checkpoint will take
-   A logically organized document written in a way that's easy to understand, and doesn't make any assumptions about what the reader knows or doesn't know (e.g. make sure any implied context is specifically called out)

**Consider taking up this project if you:**

-   Want to work on a user-facing problem that is quite likely to make users happy (even if they won't be aware of the alternative)
-   Want to better understand data pipelining & persistence in larger scale Android apps

**Knowledge/Skills Recommended:**

-   Kotlin
-   Android UI development
-   Architectural design may help
-   Dagger/dependency injection may help

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1: Implement domain layer checking whether a checkpoint is saved for a lesson, support for creating a new checkpoint at the domain layer, and support for restoring the checkpoint. Checkpoints should also be automatically expired on a least-recently-used policy basis if more than 2MB of space are consumed by checkpoints (per profile). This milestone should involve extensive testing.
-   Milestone 2: Implement the UI changes needed to represent checkpoints that are in progress, changes to existing notices, and proper UI/domain layer support for automatically expiring checkpoints when the user has been away from the app for too long or if the app has decided to automatically expire a checkpoint to save space. Implement success metrics for the feature.

---

### Introduce support for displaying copyright licenses in the app

It's important for software to properly attribute all dependencies on which it depends, and to display the specific copyright licenses for those dependencies. Beyond being the right thing to do, fulfilling this in a way that can scale across future dependencies can be difficult. In fact, Oppia Android already has nearly 100 transitive (direct + indirect) dependencies, each of which has its own license.

This project aims to introduce the necessary functionality to collect third party licenses, build a UI (via the 'Help' menu) to display those licenses (similar to , and add CI checks to ensure future changes don't break baseline expectations. Note that due to the difficulty of this problem, this project is being scoped down to specific focus on Maven dependencies that we can more easily look up. There will be additional work for the team to complete after this project is done to ensure _all_ dependencies are being considered.

This project will behave similarly to Google's Play Services [version of the feature](https://developers.google.com/android/guides/opensource). Also, please note that this is a Bazel-only feature (which is why we can't use the Gradle plugin linked earlier).

We recommend that you approach this project as follows:

-   Utilize a Kotlin script to compile the actual list of dependencies & their versions (+ a link to their license file). This list will actually be explicitly checked into the codebase.
-   Introduce a GitHub CI check to verify that the list above is kept up-to-date for every code change (which lets us easily audit when indirect dependencies are added).
-   Introduce a UI that reads from an asset list file & strings to populate the list of libraries, their versions, and their licenses. These files can be checked into git, but when they are changed (see next step) their changes should never be checked into git. Measures should be taken to prevent this.
-   Introduce a Kotlin script that, when run, populates the UI files using the dependencies list. This script should fail if the dependencies list is missing any actual new dependencies.

We have mocks ready for this project, you can view them [here.]( https://xd.adobe.com/view/e8aa4198-3940-47f9-514a-f41cc54457f6-9e9b/screen/0f94055a-c5f7-45a2-8bf5-9dcfdf1c7dce/)

**Potential Mentors:** @BenHenning, @anandwana001, @Sarthak2601

**What we are looking for in the proposal:**

-   A well thought-out system for collecting, embedding, and displaying copyright licenses from both current & future dependencies. The proposal should include dataflow & sequence diagrams to clearly explain the steps involved, and specifics on how each step will work.
-   Excellent explanations for when each piece of data will be available, and how. For example, the actual licenses themselves should never be copied into the repository. This means that we will need a script that can collect the licenses themselves. That being said, we should be building this in a way where we can easily verify via CI whether a new dependency properly interops with the system as expected.
-   An explicit example (e.g. screenshot & Gist link) that you can reverse-look up all of Oppia Android's Maven dependencies using bazel query
-   A logically organized document written in a way that's easy to understand, and doesn't make any assumptions about what the reader knows or doesn't know (e.g. make sure any implied context is specifically called out)

**Consider taking up this project if you:**

-   Are interested in understanding how to build Kotlin scripts
-   Are interested in understanding how to leverage a scalable build system like Bazel to manage dependencies
-   Would like to work on a project that involves a more-complicated-than-usual data pipeline

**Knowledge/Skills Recommended:**

-   Kotlin
-   Android UI development
-   Bazel will be a big help; the scripts themselves should be written in Kotlin + Bazel to simplify work, and Bazel will be used for queries
-   GitHub Actions will help

**Dependency on Release Schedule:** None.

**Suggested Milestones:**

-   Milestone 1: Introduce a script for generating a list of dependencies using a reverse-deps lookup of Oppia Android's //third_party Maven dependencies. Introduce a script for converting the dependency list to actual license content files.
-   Milestone 2: Introduce & hook-up a UI to properly display all of the licenses included in the app. Introduce a GitHub Actions check to verify that the list of dependencies is kept up-to-date over time. Introduce extra checks to ensure that generations of the license files can't be accidentally checked into the repository.

---

## Oppiabot team

### Making Oppiabot Better

Oppiabot is a GitHub bot that helps automate the process of contributing to the Oppia and Oppia Android repository.

This project involves adding a couple of new features and making the currently available features better. If some of the available features get fixed before GSoC, you can find replacement issues which you would love to work on from https://github.com/oppia/oppiabot/issues.

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

-   Want to help improve the experience of contributors
-   Interested in designing the flow of a contributor from when a pull request is made till it gets merged.
-   Are interested in working with JavaScript (NodeJS).

**What we're looking for in the proposal:**

1. Links to one or more PRs showing contribution to the oppiabot project.
2. Deep understanding and concern for the developer experience.

**Dependency on Release Schedule:** None

**Suggested Milestones:**

-   Milestone 1: Fix half of the issues available.
-   Milestone 2: Fix remaining half of the issues.

# Other useful information

## Dates and Deadlines

Noteworthy dates for 2021 ([Full Timeline](https://developers.google.com/open-source/gsoc/timeline)):

-   **Jan 15 - Feb 19**: Mentoring organizations apply
-   **Mar 9**: Mentoring organizations are announced
-   **Mar 29 - Apr 13**: Student application period
-   **May 17**: Accepted students are announced
-   **May 17 - Jun 7**: Community bonding period
-   **Jun 7 - Aug 23**: Students enjoy the summer by contributing code to their projects
-   **Aug 31**: GSoC officially ends

## List of Mentors

-   Sandeep Dubey
-   Srijan Reddy
-   Kevin Thomas
-   Akshay Anand
-   Vojta Jelínek
-   Sean Lip
-   Rohit Katlaa
-   Vinita Murthi
-   Rajat Talesra
-   Ben Henning
-   Akshay Nandwana
-   Pulkit Aggarwal
-   Sarthak Agarwal
-   Prayush Dawda
-   Sajal Asati
-   Anshul Hudda
-   James James
-   Nithesh Hariharan
-   Sagang Wee

## Communication

**Chat**

Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any questions related to getting started. For project-specific questions, please direct your queries to the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).

**Email**

In order to receive updates about GSoC at Oppia please subscribe to [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce).

If you have questions pertaining to "how-to-get-started", please ask them on [Gitter](https://gitter.im/oppia/oppia-chat), or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you. Also, please make sure to read our ["getting started" wiki page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) before sending an email, since the answer to your question might already be contained there!

To discuss your project ideas, or share your proposal for feedback from the community, please email the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com). You can also use this list for specific questions about GSoC.

---
