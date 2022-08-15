## Table of Contents

- [Getting started](#getting-started)
- [FAQs](#faqs)
- [Dates and Deadlines](#dates-and-deadlines)
- [Types of work related to Oppia projects](#types-of-work-related-to-oppia-projects)
- [GSoC proposal template](#gsoc-proposal-template)
  - [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan)
  - [What should applicants expect from mentors in a proposal review?](#what-should-applicants-expect-from-mentors-in-a-proposal-review)
  - [Sample proposals from past years](#sample-proposals-from-past-years)
- [Selection Criteria](#selection-criteria)
- [Communication](#communication)
- [Oppia's Project Ideas List](#oppias-project-ideas-list)
  - [Learner and Creator Experience (LaCE) team](#learner-and-creator-experience-lace-team-1)
  - [Contributor Dashboard team](#contributor-dashboard-team-1)
  - [Angular team](#angular-team-1)
  - [Backend team](#backend-team-1)
  - [Developer workflow team](#developer-workflow-team-1)
  - [Android team](#android-team-1)

This year, Oppia will be participating in [Google Summer of Code 2022](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers non-experienced contributors (and, historically, post-secondary students) the opportunity to discover and work with open-source organizations. The contributions are supported by a stipend. Contributors work closely with one or more mentors from an open-source organization to implement either a project idea by the organization, or a proposal of their own. You might be interested in our GSoC info pages from previous years: [2021](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2021), [2020](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020), [2019](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2019), [2018](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018), [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

In order to receive updates about GSoC at Oppia, please subscribe to the [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce) mailing list.

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions [here](https://github.com/oppia/oppia/wiki).


## Accepted Proposals:
- The projects we've accepted are:
  * [Anshuman Maurya's proposal](pdfs/GSoC2022AnshumanMaurya.pdf): Achieve 100% Per-File Branch and Line Coverage for the Frontend and the Backend. Mentor: Chris Skalnik
    * **Milestone 1:** Ensure that all backend files (except for test data files) have an associated test file. Ensure that every backend file has an associated test file so that coverage checks are guaranteed to be triggered for all files. Calculate backend branch coverage on CI and use a temporary denylist to ensure that the backend branch coverage does not regress. Achieve 100% line coverage for all backend files.
    * **Milestone 2:** Achieve 100% line coverage of all frontend files (except for test files and unit-test-utils.ts and schema-based-list-viewer.directive.ts, since those will be removed by the Angular Migration). Achieve 100% backend branch coverage and 100% per-file backend line coverage except for the files in core/domain/. Remove the temporary denylist for backend branch coverage.
  * [Ch Vishnu Nithin Reddy's proposal](pdfs/GSoC2022ChVishnuNithinReddy.pdf): Celebrating learners' accomplishments. Mentor: Kevin Thomas
    * **Milestone 1:** Celebrate lesson completion in a meaningful, actionable, and rewarding way for the learner.
    * **Milestone 2:** Celebrate checkpoint completion in a meaningful, rewarding way for the learner that encourages them to continue progressing.
  * [Harshvardhan Singh's proposal](pdfs/GSoC2022HarshvardhanSingh.pdf): Making the Contributor Dashboard UI responsive. Mentor: Vojtěch Jelínek
    * **Milestone 1:** Implement a fully-responsive UI for the contributor dashboard landing page (this includes the overall navigation, the review workflow, and the views of the user’s review/submission history).
    * **Milestone 2:** Implement a fully-responsive UI for the translation and question submission pages (this includes both the list of opportunities and the submission workflow).
  * [Hasitha Kaushan's proposal](pdfs/GSoC2022HasithaKaushan.pdf): Contributor recognition infrastructure. Mentor: Sagang Wee
    * **Milestone 1:** All backend infrastructure for the project is completed, up to and including the HTTP request endpoints.
    * **Milestone 2:** Contributors can see their stats and badges in a new stats tab on their logged-in Contributor Dashboard (on both desktop and mobile devices). This also includes contributor certificate generation.
  * Hitesh Tomar's proposal (to be added): Fix validation errors. Mentor: Eric Lou
  * [Jeevesh Garg's proposal](pdfs/GSoC2022JeeveshGarg.pdf): Improve Frontend Type System. Mentor: Mridul Setia
    * **Milestone 1:** Change the TypeScript config file so that all newly-added files need to be strictly typed. Introduce strict typing for 280 frontend files (this number also can include test files).
    * **Milestone 2:** Introduce strict typing for 280 additional frontend files in the codebase that were not covered in Milestone 1 (again, this number also can include test files).
Remove the "unknown" type from all frontend files in the codebase, and add a lint check to prevent usage of "unknown" in the future.
  * [Jishnu Goyal's proposal](pdfs/GSoC2022JishnuGoyal.pdf): Interactive Onboarding Flow. Mentor: Ben Henning
    * **Milestone 1:** Make fixes to address the most pressing user onboarding issues (listed below), and manually verify all the new onboarding fixes to ensure that UI elements are functioning as expected. Also, introduce the necessary domain functionality for introducing spotlights in M2.
      * Change the icon for initiating voiceovers to a headphones icon
      * Add an animation to the continue button on the lessons page during the initial user experience, so that they are less likely to get stuck because of not knowing where to click next.
      * Hide the info tab and make the lessons tab the default topic landing tab.
      * Make the home screen have a clearer CTA (achieved by hiding the promoted story list for the first time a user enters the app – this section is made visible when the user enters everytime after).
      * Redesign the topic lessons tab to have a clearer CTA, and expand the lessons list of the first story by default.
      * Add appropriate placeholder texts for all text based interactions in the app.
      * In the revision screen, change the toolbars to have an orange color. Also, at the end of the revision cards, add "next" and "previous" chapter image views to navigate between cards.
    * **Milestone 2:** 
      * Add spotlights for the audio voiceover play and language buttons; the exploration exit button; the Lessons and Revision tabs; the first chapter of a story; the home-screen promoted stories; and the onboarding screen's 'next' button. Add RTL functionality to spotlights. Manually test all the spotlight flows to ensure that they are behaving as expected. Write wiki documentation for how to add a new spotlight for features in the future.
      * For Talkback users: suspend the spotlight; add content descriptions to Lesson Tab, Revision Tab and Exit buttons on the exploration screen; reword the content descriptions for the Voiceover icon and voiceover language option; and add a forced announcement for the hint bar (when it gets visible).
  * [Manan Rathi's proposal](pdfs/GSoC2022MananRathi.pdf): Helping learners when they get stuck. Mentor: Prayush Dawda
    * **Milestone 1:** Allow creators to provide a destination state for the case where a learner is really stuck. Prohibit lesson creators from sending the learner more than 2-3 cards back in the lesson.
    * **Milestone 2:** Detect when a learner is stuck and provide appropriate real-time assistance based on (a) proactively showing concept cards or hints, (b) redirection to the alternative destination state, and (c) providing the solution as the last resort (the solution will be made mandatory for each state). Detect small misspellings and provide the learner with appropriate help.
  * [Nikhil Agarwal's proposal](pdfs/GSoC2022NikhilAgarwal.pdf): Learner diagnostic tests. Mentor: Sean Lip
    * **Milestone 1:** Curriculum admins should be able to use a “classroom administration” page to configure details of each classroom, enter the dependencies between topics in that classroom, and enter details for the diagnostic test. A comprehensive suite of backend integration test cases that convincingly should demonstrate that the recommendation system entered by the curriculum admin works correctly.
    * **Milestone 2:** Learners should be able to visit the Math Classroom page and take an adaptive diagnostic test that surfaces 0, 1 or 2 topic recommendations for them to pursue.
  * [Pankaj Prajapati's proposal](pdfs/GSoC2022PankajPrajapati.pdf): Learner groups MVP. Mentor: Akshay Anand
    * **Milestone 1:** Facilitators can, from a teacher dashboard page, create a
learning group and its syllabus and see all learner groups created by them. They should also be able to view the learner group’s homepage (which
contains the details of the learning group, its syllabus and the list of
learners and their progress).
    * **Milestone 2:** Facilitators should be able to invite learners to join the group via username. Learners should be able to join the group, set their preferences (or edit them later), and see the group homepage (which contains their progress, as well as triggers for starting recommended activities from the syllabus).
  * [Rijuta Singh's proposal](pdfs/GSoC2022RijutaSingh.pdf): Blog integration. Mentor: Praneeth Gangavarapu
    * **Milestone 1:** Create the blog homepage and individual blog post pages (but hide them behind a feature flag for now). Blog editors should be able to create a new blog post (using the existing blog post creation infrastructure) and have it appear on the new blog page.
    * **Milestone 2:** All blog posts from Medium should be moved to the Oppia.org blog page, and should look nice and display correctly for readers. The Oppia navbar and footer should have links that point to the new blog. Implement a blog statistics page that shows the total number of views and reads for each post, author, and the overall blog.
  * [Sahil Jhangar's proposal](pdfs/GSoC2022SahilJhangar.pdf): Make backend code typed. Mentor: Aasif Faizal
    * **Milestone 1:** Fully type core/domain, core/tests, and core/jobs. Put measures in place to ensure that the files in these folders have full backend typing in perpetuity, to Oppia’s standards (i.e. not using "Any", casts, and objects, and only using a narrow, fully-documented subset of type-ignore pragmas).
    * **Milestone 2:** Fully type the entire backend codebase, including schema validation for all handlers. Drop typeinfo from all docstrings and add new docstring lint checks to ensure that docstrings adhere to the new format in perpetuity. Also, ensure that measures are in place to prevent backend typing coverage from regressing in the codebase.
  * [Shivam Chaudhary's proposal](pdfs/GSoC2022ShivamChaudhary.pdf): Angular migration. Mentor: Ashutosh Chauhan
    * **Milestone 1:** Fully migrate the following directives/pages from AngularJS to Angular 11: state-editor, state-directives, question-directives, version-diff-visualization, contributor-dashboard-page.
    * **Milestone 2:** Fully migrate the exploration-editor page, the review test page, the practice session page, from AngularJS to Angular 11. Migrate the relevant files in the codebase to use AngularCDK DragAndDrop instead of uiSortable, and ngxJoyride instead of ngJoyride. Remove uiSortable and ngJoyride completely from the codebase.
  * [Shivam Jha's proposal](pdfs/GSoC2022ShivamJha.pdf): Migrate Away From Protractor. Mentor: Md Shahbaz Alam
    * **Milestone 1:** Set up WebdriverIO with Github Actions. Document how we use it, including adding a step-by-step guide to the developer wiki on “how to debug e2e tests” (which should be kept up-to-date and address any issues that devs face). Add eslint rules to ensure the code quality. Add a lint check to ensure that the union of suites present in both versions of the e2e tests is the complete list of e2e suites. Fully migrate 20 test suites to WebdriverIO.
    * **Milestone 2:** Fully migrate all remaining e2e test suites to WebdriverIO, and remove all references to Protractor from the codebase and the developer wiki.
  * [Soumyajyoti Dey's proposal](pdfs/GSoC2022SoumyajyotiDey.pdf): Improving the lesson creation experience. Mentor: Kevin Thomas
    * **Milestone 1:** Enable creators to see changes in the exploration metadata by clicking a button in the history tab. Make all the necessary backend changes (up to and including the controller layer) for users to be able to navigate through the version history of a state (and the exploration metadata) in an exploration. Also, create the backend api service in the frontend for fetching the version history data.
    * **Milestone 2:** Make all the other required frontend changes so that users can navigate through the version history of a state and the exploration metadata.
  * [Vraj Desai's proposal](pdfs/GSoC2022VrajDesai.pdf): Accessibility Improvements. Mentor: Rajat Talesra
    * **Milestone 1:** All screens in the Android app can be fully used by screenreader users (using e.g. Talkback), with the exclusion of (a) Exploration player, (b) Question Player, (c) dark mode and (d) focus shifting to the start of the screen if an item changes (for screens with recyclerviews). Users should also be able to use the ImageClickInput regions interaction easily using screen-readers.
    * **Milestone 2:** All screens in the Android app can be fully used by screenreader users (using e.g. Talkback), with the exclusion of (a) dark mode and (b) focus shifting to the start of the screen if an item changes (for screens with recyclerviews).
  

# Contributors

GSoC is an excellent opportunity for new contributors to get paid to work on an open source project. If you're interested in applying as a contributor, you should definitely read the following resources:

-   [Google Summer of Code contributor guide](https://google.github.io/gsocguides/student/)
-   [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
-   [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)


## Getting started

Welcome! If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. If you like, you can also sign up to the [oppia-gsoc-discuss@](https://groups.google.com/forum/#!forum/oppia-gsoc-discuss) mailing list to participate in general discussion related to Oppia's involvement in GSoC. Make sure to set your preferences correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is about:
    - Read the [user documentation](http://oppia.github.io/#/) to become familiar with important concepts like explorations and interactions. 
    - Play some lessons on [Oppia.org](https://www.oppia.org/learn/math), which hosts a live instance of Oppia.
 
3. To get started with development, read and follow the instructions in the contributors' guide carefully ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Oppia Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)).

4. Do one or more starter projects to become familiar with the contribution process. This will help us get an idea of what it's like to work with you. It will also help you get a better understanding of the codebase and our development process, which may help with writing a good project proposal. Once you've merged at least 2 pull requests, you will get an invitation to become a collaborator to the Oppia or Oppia-Android repository and be officially onboarded!

   - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to follow the [tips for success](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#tips-for-success), manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide), and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Select one or more [GSoC project ideas](#oppias-project-ideas-list) that you're most interested in, and write your project proposal! We strongly encourage you to discuss your project ideas and share your proposal with the community, so that you can get feedback and ensure that what you're writing makes sense to others. Please follow the instructions in the [GSoC proposal template](#gsoc-proposal-template) section to do this. 

    If you have any questions about a project, or would like to discuss your approach with the Oppia community and get feedback, you can also email the [oppia-gsoc-discuss@](https://groups.google.com/g/oppia-gsoc-discuss) mailing list. Please be specific when asking questions, since this makes it easier for us to help you.

    Good luck!

## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: For Oppia Web, Angular 2+, Python 3.7 and Google App Engine is useful and recommended for most Oppia work; in addition, UI design skills are useful for frontend, user-facing work. For Oppia Android, you'll want to be familiar with Android development in Kotlin. Please see the individual project ideas to determine whether these skills are recommended for the project in question.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other contributors, successfully contributing, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: Yes (within reason)! This year, GSoC is going to be a bit different from previous years. The program has been restructured in a way that allows contributors to take some time off for any other commitments such as exams. ([View the timeline here.](https://developers.google.com/open-source/gsoc/timeline)) Oppia will respect the same timelines that are given by GSoC; the main concern is whether you can still get the project done on time. Be upfront about your other commitments and make sure you schedule your time accordingly when creating your proposal. Other commitments you should list include time when you'll be in school and will commit less time to GSoC, time when you'll be travelling and away from GSoC work, any summer jobs you need to commit to, etc. We will try to be flexible around other time commitments, as long as your proposal convinces us that you will have enough time to complete the project by the end of the GSoC coding period. On the other hand, if you do not disclose other commitments, and it turns out that you are unable to commit to what you wrote on your proposal, this is grounds for failing the program.

**Q: Which projects are most important for Oppia?**

A: All the projects we've listed in the [Ideas List](#oppias-project-ideas-list) are important, and we'd be very happy to see good progress made on any of them! Projects are treated as equally important during selection; note that the relative importance of a project to Oppia is not part of the [selection criteria](#selection-criteria). We strongly encourage you to pick a project that you'd enjoy doing over the summer!

**Q: Can I submit more than one proposal to Oppia?**

A: Yes, you can. However, we strongly recommend picking one project and writing a solid proposal for it. Splitting attention across multiple projects might not be a great idea. (That said, since this is the first year GSoC is offering full-length and half-length projects, one exception might be if you're interested in doing either the 'full version' or the 'half version' of a project idea that can support both modes. In such a case, you would be welcome to submit both the 'full version' and the 'half version' as separate applications, but, before doing so, please make sure that you'd be happy with either outcome if you are selected.) 

**Q: How early should I start working on the proposal?**

A: As early as possible. Make sure to get feedback from mentors before finally submitting the proposal. This will help you to write a better proposal, as you can refine the details based on the feedback you receive. Mentors will need some time to review your proposal, so it's a good idea to begin as early as possible. Make sure to follow all instructions in the [proposal template](https://docs.google.com/document/d/1yYefLkT7dJJa86MyrdWpbZtzeaWAKCi1eXZZDGUrasM/edit) (especially around sharing and access) to reduce delays in reviewing your proposal.

**Q: I only discovered Oppia recently. Does this mean that, during selection, my application would automatically be ranked lower than those by other applicants who have a longer tenure with Oppia?**

A: Definitely not! Here are the [selection criteria](#selection-criteria) we use when selecting contributors for GSoC. Note that tenure is explicitly not part of these criteria.

**Q: What are the minimum number of PRs that one should have?**

A: You should have at least 2 PRs merged, but they don't need to be large. Beyond that, remember that quality is more important than quantity. It is better to submit a non-trivial PR rather than a one-line wording change. Start with starter issues, then prioritize ones that touch the area(s) of the codebase which are related to your project.

**Q: What is the total number of contributors that will be accepted?**

A: As many as we think will succeed, though the Google GSoC admins may impose limits based on how they decide to distribute contributor slots among the different open-source organizations.

**Q: I do not have any experience in skill XYZ. Is some certification required?**

A: Try to work on good first issues and take courses online. In the field of software development, it is common to develop experience and expertise as you take up and complete projects successfully. We do not require any formal certification of particular skills.

**Q: Is it okay if I only focus on the frontend or backend?**

A: This probably depends on the project(s) you wish to apply for. However, note that the ability to be effective in both the frontend and backend will open up more opportunities for you, since projects often touch multiple layers of the stack.

**Q: The [Google GSoC FAQ](https://developers.google.com/open-source/gsoc/faq#can_someone_already_participating_in_open_source_be_a_gsoc_contributor) mentions that the program is only for new contributors. I have already contributed to Oppia and I have write access. Can I still participate?**

A: The GSoC program is open to new and beginner contributors to open source. Some of our contributors with write access are still beginner contributors, whereas some of our other contributors with write access will not qualify because they are experienced contributors. If you have only recently received write access, or have been contributing to Oppia for less than a year, you are probably still a beginner contributor. If the previous sentence does not apply to you, and you want to know which group you fall into, please contact **@vojtechjelinek** or **@seanlip** for a decision.

## Dates and Deadlines

Noteworthy dates for 2022 ([Full Timeline](https://developers.google.com/open-source/gsoc/timeline)):

- **Feb 7 - Feb 21**: Mentoring organizations apply
- **Mar 7**: Mentoring organizations are announced
- **Apr 4 - Apr 19**: GSoC contributor application period
- **May 20**: Accepted GSoC contributors are announced
- **May 20 - Jun 12**: Community bonding period
- **Jun 13 - Sep 12**: GSoC contributors enjoy the summer by contributing code to their projects
- **Sep 12 - Nov 21**: Extension period for GSoC coding (for projects with extended deadlines)

## Types of work related to Oppia projects

The Oppia team is committed to making GSoC an enriching educational experience for contributors. In order to ensure a well-rounded engineering experience, GSoC contributors will have the opportunity to do some or all of the following, depending on their project:

-   Meet with their mentors regularly
-   Meet with other contributors related to their project area
-   Read and understand parts of the codebase related to their project
-   Receive code reviews for all code they write for their project
-   Write automated tests for their projects
-   Create UI mocks (if doing frontend development)
-   Give presentations and demos of their projects
-   Contribute to community initiatives, such as release testing and documentation
-   Write design documents (if implementing large features or introducing new systems)

We've also asked our previous GSoC contributors what they learned during previous GSoCs. Here are their collated answers:

-   Technical ability
    -   Writing clean code, while keeping in mind the requirement for the code to run in production.
    -   The quality of code that I write now is much improved. Also, I got the experience of working with a team.
    -   Building an entirely new feature in a scalable way.
    -   Writing robust tests.
    -   Working on a large codebase.
    -   Reading and understanding code from other open-source organizations.
    -   I am now more confident in my skills as a developer.
-   Technical domain knowledge
    -   I feel more confident on working with Angular. Oppia was the first time I worked with unit and e2e tests. 
    -   I feel a lot more confident in writing code now, whether it be making my own projects or contributing to other open-source projects.
    -   I learned lots of things about typescript and webpack.
    -   I understood how E2E tests and angular migrations worked in Oppia — this felt very rewarding.
    -   I enjoyed finding and fixing accessibility issues.
    -   I learned the importance of testing and also following a clean architecture.
-   Technical leadership skills
    -   How to manage my time well, how to achieve deadlines especially when I got evaluations from external evaluators.
    -   How to properly plan a project before implementing it.
    -   Technical design skills (and validation of technical ideas).
    -   How to give, respond to and understand reviews.
-   Communication and personal development
    -   Putting forward my thoughts more systematically and deeply so that everyone can understand me well.
    -   Better communication skills.
    -   How to write a good proposal.
    -   How to work with a large community like this which is spread over different time zones.
    -   How to reach out to people, work with them, and solve each other's problems.

## GSoC Proposal Template

When submitting a proposal, please use the provided [GSoC proposal template](https://docs.google.com/document/d/1yYefLkT7dJJa86MyrdWpbZtzeaWAKCi1eXZZDGUrasM). We will only consider proposals submitted using this template.

You are welcome to ask mentors for reviews during the proposal preparation phase. We recommend getting the WHAT section reviewed before doing substantial work on the HOW section, and getting the first part of the HOW section reviewed before doing work on the second part. This is meant to help ensure that later sections of the proposal build on a solid baseline, and avoid wasted work.

**Some important notes:** 
1. Your proposal should be shared as "anyone with the link can leave comments" and sent to oppia-gsoc-discuss@. Do not send proposals directly to individual GSoC mentors. Mentors have been instructed not to respond to proposals that are not shared publicly, and we take a negative view on restricting access to proposals after feedback is provided. This is because, in the spirit of open-source, we would like to keep the discussions open, so it is intentional that everyone (including non-mentors) should be able to see your proposal and leave comments and suggestions on it.

2. Your final proposal should be self-contained. In particular, to be fair to all applicants, key components of the proposal should not be editable after the deadline. Don't assume that reviewers will follow external links.

3. Your proposal must be **original** (see section 2.4 of the [Contributor Participation Agreement](https://summerofcode.withgoogle.com/terms/contributor)). During the selection process, proposals that are found to have passed off others' work as their own will automatically be disqualified. If you include any text in your proposal that is copied from the Internet or other sources, you should make it clear that you are doing so, and **provide a link or reference back to the source, with appropriate credit**. In cases of doubt, we would encourage you to err on the side of giving credit (since not doing so may be construed as plagiarism).


### Tips for writing a good project plan

Here's some advice about proposals and milestone timeline planning that we collated from previous contributors and mentors:

-   Choose a project you're interested in! If you have a strong interest in your project, this might make it easier for you to pick up the necessary skills and tackle unforeseen difficulties that may arise during GSoC.
-   Familiarize yourself with the relevant part of the codebase for your project, especially if you haven't touched it before. It's important to think about how to integrate your project with the current Oppia structure — don't design in a vacuum.
-   Define milestones with enough detail to get a proper ETA for each milestone (so, don't just say "write e2e tests"). Otherwise, you run the risk of significantly underestimating the timeline.
-   Clear written communication and presentation is crucial in preparing your proposal. The proposal should show that you have a good understanding of the codebase and the final goal of the project. For example, in a user-facing proposal, don't just make a list of files that need to be changed; it is also important to show detailed mocks and user flow diagrams that demonstrate a clear understanding of the requirements.
-   Limit proposal length. A lengthy proposal is not necessarily a better proposal; adding large amounts of unnecessary detail can sometimes obscure the main points you are trying to get across.
-   Ensure that the problem statement is within your limits to tackle, and make sure that what you're proposing is within your capabilities. The [Project Ideas section](#oppias-project-ideas-list) contains some suggested milestones, but it is up to you to come up with a complete plan that is within your ability. In other words, contributors can propose whatever they want; it’s up to the Oppia team to subsequently figure out (during selection) whether we’re happy about what’s being proposed.
-   Contributors who make the last milestone bulky normally run into issues. So, make sure that you distribute work evenly.

### What should applicants expect from mentors in a proposal review?

-   Please write your proposal on the assumption that you "own" your chosen project. From your perspective, the submitted proposal should be in as good a condition as possible before you ask for a review. Make sure that you have a sufficiently good understanding of the codebase/project so that you can find and fix flaws in the design; don't assume that reviewers are responsible for doing this for you. Note that your proposal doesn't need to be flawless — we expect that you might make mistakes, and reviewers will be happy to guide you on how to improve. Instead, by "as good a condition as possible", we mean that your proposal should demonstrate:
    -   Your ownership of the project
    -   The research you have put into writing it
    -   Your analytical skills
    -   Your independence in making complex decisions
-   Make sure to present solutions and ask for feedback, rather than just asking for solutions. You can do this by presenting the various solutions you came up with within your proposal, and doing an analysis of their advantages & disadvantages from the end-user perspective using a comparison table. Finally, choose the best solution you have, and explain the reasoning for how you arrived at your choice. Note that this doesn't mean that you must always have multiple ideas to solve a problem, but you should instead always explain how you reached a solution, and why is it the best one from the end-user's perspective. Think about how you might gather some data to validate your conclusions (e.g. by finding support in the peer-reviewed literature, or by showing your ideas to potential users in the target audience and asking for feedback, etc.).
-   Mentors' suggestions are _suggestions_, not mandates (often, reviewers may not be certain whether their suggestion is correct). We do not expect you to always agree with your reviewers! This means that, as the proposal owner, you are always welcome to decide whether to accept/reject such suggestions. In either case, when you are accepting/rejecting a suggestion provided by a reviewer, try to explain your reasoning and the research that led to your decision.
-   If you're confused about something, try to identify the point of confusion and ask have specific discussions about it, rather than simply agreeing to whatever is proposed. Don't rely on an "appeal to authority" (e.g. "I am doing it this way because reviewer XXX said so") — the rational analysis and thought that underlie the decision are what's important, so make sure that you understand and clearly communicate the reasons behind the decisions you make.
-   Note that the process Oppia uses to select GSoC contributors typically includes multiple independent mentors, most of whom will not have looked at the earlier versions of your submitted proposal. Your reviewer may or may not be involved in the final selection process, and it is definitely **not** the case that you need to implement all your reviewer's suggestions/requests in order to be selected. We recommend considering your reviewer as a friendly advisor who is available to help you and provide guidance, rather than the main future evaluator of your proposal.

### Sample proposals from past years

If you'd like to get a sense of what a proposal might contain, please see our [GSoC 2021 page](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2021) for examples of proposals that we accepted in 2021. However, please note that the [GSoC Proposal Template](#gsoc-proposal-template) has been completely revamped for 2022, so please be sure to follow the 2022 template.

**Note:** although some of the previous years' proposals are a bit on the long side, there's **no** formal length requirement for your proposal. The quality of what you write is much more important than the amount of text you write, and we encourage you to write shorter proposals that still convey the main aim of the project.

## Selection Criteria

In order to select contributors for GSoC, we will mainly be looking at three things:

-   The quality of the submitted proposal
-   The quality of the applicant's previously-submitted PRs (in order to assess their ability to code, debug, break down complex tasks, etc.). Note that quantity isn't a prerequisite in itself, though contributors who've submitted multiple PRs are likely to have had more opportunities to demonstrate the abilities needed to succeed in GSoC.
-   Our prior experience working with the contributor (do they keep commitments, communicate well, demonstrate independence/initiative/responsiveness, help others, etc.)

We believe that strong performance in these dimensions is likely to correlate well with the contributor having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the GSoC program.

For the proposal, we generally look for a clear indication that the contributor has a good, clear understanding of the project, and has broken it down sufficiently well, in a way that makes it very likely to succeed. Some indicators that could help with this include:

-   Clear, unambiguous communication. (This is important; your proposal will be read by many mentors!)
-   A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating a simple, intuitive experience for end users.
-   A proposed solution approach which is sufficiently concrete and which demonstrates that the applicant has a good understanding of both the scope of the problem and the existing codebase.
-   A description, if applicable, of how the applicant plans to mitigate risks that could potentially derail the project.
-   A concrete, specific breakdown of the work to be done for each milestone.


## Communication

If you have questions pertaining to "how to get started with Oppia", please ask them on **GitHub Discussions** ([Web](https://github.com/oppia/oppia/discussions), [Android](https://github.com/oppia/oppia-android/discussions)). Please be specific when asking questions; this makes it easier for us to help you. Also, please make sure to read the relevant "getting started" wiki page ([Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)) first, since the answer to your question might already exist there!

For GSoC-project-specific questions, please direct your queries to the **[GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com)**. You can also use this mailing list to discuss your project ideas, ask specific questions about GSoC, or share your proposal for feedback from the community. All of this year's GSoC mentors are already members of that mailing list.

To receive important announcements and updates about GSoC at Oppia, please subscribe to the **[Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce)** mailing list.

Finally, Oppia has a real-time chat channel at [Gitter](https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any general questions (though, for the latter, GitHub Discussions is probably better).

## Oppia's Project Ideas List

_**Note:** If you're coming to this section from an external link, please make sure to scroll up and read this entire wiki page carefully, not just this section. There's a lot of useful information on the rest of the page, including a FAQ and a section describing selection criteria. Thanks!_

The following is a list of Oppia's 2022 GSoC project ideas. You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community beforehand in order to get feedback and guidance to improve the proposal. We'd also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

Please note that the list of project ideas below is not set in stone: more projects may be added later, and some project descriptions may also change a bit, so check back regularly. In addition, the mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted.

### Learner and Creator Experience (LaCE) team

1.1. [Learner diagnostic tests](#11-learner-diagnostic-tests)

1.2. [Implementing the “Needs Guiding Responses” section of the lesson analytics dashboard](#12-implementing-the-needs-guiding-responses-section-of-the-lesson-analytics-dashboard)

1.3. [Helping learners when they get stuck](#13-helping-learners-when-they-get-stuck)

1.4. [Celebrating learners' accomplishments](#14-celebrating-learners-accomplishments)

1.5. [Learner Groups MVP](#15-learner-groups-mvp)

1.6. [Improving some math interactions](#16-improving-some-math-interactions)

1.7. [Blog integration](#17-blog-integration)

1.8. [Improving the lesson creation experience](#18-improving-the-lesson-creation-experience)

1.9. [Onboarding improvements](#19-onboarding-improvements)

### Contributor Dashboard team

2.1. [Contributor recognition infrastructure](#21-contributor-recognition-infrastructure)

2.2. [Making the Contributor Dashboard UI responsive](#22-making-the-contributor-dashboard-ui-responsive)

2.3. [Adding a Contributor Dashboard Stats page](#23-adding-a-contributor-dashboard-stats-page)

### Angular team

3.1. [Migrate the exploration editor page to Angular, and move the entire frontend to the Angular CLI](#31-migrate-the-exploration-editor-page-to-angular-and-move-the-entire-frontend-to-the-angular-cli)

### Backend team

4.1. [Make backend code typed](#41-make-backend-code-typed)

4.2. [Improve the frontend type system](#42-improve-the-frontend-type-system)

4.3. [Fix validation errors](#43-fix-validation-errors)

4.4. [Move and fix data in Google Cloud Storage](#44-move-and-fix-data-in-google-cloud-storage)

### Developer workflow team

5.1. [Achieve 100% Per-File Branch and Line Coverage for the Frontend and the Backend](#51-achieve-100-per-file-branch-and-line-coverage-for-the-frontend-and-the-backend)

5.2. [Migrate away from Protractor](#52-migrate-away-from-protractor)

### Android team

6.1. [Android release automation](#61-android-release-automation)

6.2. [Interactive onboarding flow](#62-interactive-onboarding-flow)

6.3. [Accessibility improvements](#63-accessibility-improvements)


## Learner and Creator Experience (LaCE) team

### 1.1. Learner Diagnostic Tests

**Project Description:**

We have heard that, when visiting the Oppia Classroom, learners are sometimes not sure which lesson(s) to start with. The aim of this project is to streamline the “getting started” experience for learners, as well as provide a way for them to test themselves and get personalized recommendations for what lesson(s) to work on next.

Specifically, learners should see an option in the Math Classroom page (located at /learn/math) to take a diagnostic test. This test should be a set of questions covering multiple topics. Ideally, it would be adaptive in nature, and have no more than 10-15 questions (possibly ending earlier if the learner's topic can be determined with fewer questions). When a recommendation is made, the learner should understand the rationale for the recommendation. It is fine to make 0, 1 or 2 recommendations (with 0 being the case if they seem to have understood everything).

Curriculum admins should be able to “program” this test. They would specify the key skills for each topic that would be tested, and how the learner’s performance on the tested skills maps to the decision of which topic to recommend. A simple way to model this is for the curriculum admin to provide up to 3 key skills for each topic (in the order that these are taught within that topic), as well as some representation of the dependencies between topics. The diagnostic test should “binary search” using this data to find the “earliest” topic that the learner would benefit from learning. (This is a high-level sketch, and more detail should be supplied within the proposal.)

**Size of this project:** large (~350 hours)

**Potential Mentors:** @krishita30j, @aks681

**Knowledge/Skills Recommended:** 

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Some understanding of UI/UX design
* Good technical design skills

**Suggested Milestones:**

* **Milestone 1:** Create a “classroom administration” page for curriculum admins. Move the "classroom details" config property from the "Admin > Config" page to this new page. Additionally, on this page, add a section which allows curriculum admins to enter details for the diagnostic test and the inter-topic dependencies for each classroom page. The learner UI doesn’t need to exist at this point, but there should at least be a comprehensive suite of backend integration test cases that convincingly shows that the recommendation system entered by the curriculum admin works correctly.
* **Milestone 2:** The full learner UI for diagnostic tests should be built. New learners should be able to visit the Math Classroom page and take an adaptive diagnostic test that would then surface 0, 1 or 2 topic recommendations for them to pursue. 

**Dependency on Release Schedule:** None.

**Proposal notes:**

* This project will require some UI/UX design skills. The proposal should include mocks for the learner and creator (i.e. curriculum admin) experiences.
* The proposal should explain how to handle the case where a learner makes an error in the diagnostic tests that is not due to a misunderstanding of the topic, but more due to a typo or computation error. Do we give them another chance to submit the right answer, or do we give them a second question on that skill, or something else?
* You may be able to reuse large parts of the existing practice question player infrastructure in the learner view of the diagnostic test. If you do, please explain in the proposal which specific top-level component(s) you will be reusing, and what (if any) modifications need to be made to it to support both the existing and new use cases. Try to keep these modifications minimal.
* In the future, we’d like to reuse this infrastructure for topic-level diagnostic tests that would help the learner figure out which lesson in a topic they should start from. Implementing these topic-level tests is out of scope for this GSoC project. However, when designing the infrastructure, please keep this use case in mind, since we would like to extend the project to support it in the future.
* (For information only) Oppia has a learner feedback team which uses the Oppia lessons to conduct sessions with learners. They will be one of the stakeholders for this project, since they would use it to help learners figure out which topic they’d like to learn at the start of a learner feedback session. During the GSoC project, you will have the opportunity to get feedback from them on what you’re building!

**Useful resources:**
* [PRD for this feature](https://docs.google.com/document/d/1GrVORe_oMrFOt6SN_JyfIr06f_TlwfwvOVMYfqT4gZY/edit). Note that this PRD might have some omissions, or be incomplete. If you see gaps, feel free to fill them in! You can also leave comments directly on the PRD if you have questions about what is written there.


### 1.2. Implementing the “needs guiding responses” section of the lesson analytics dashboard

**Project Description:**

Oppia has, for each exploration, an “improvements tab” that shows common wrong answers to a question. This allows lesson creators to subsequently improve the lessons. (For example, if a particular wrong answer isn’t addressed well by the existing feedback, and is being submitted regularly, then we can detect this and update the lesson.) This is important for ensuring that learners don’t get stuck.

Unfortunately, the existing stats dashboard is somewhat unwieldy and not well-suited for easily taking action to update lessons. A new [improvements tab](https://drive.google.com/file/d/1GOrwZhVKCunSmOgbvMDaGFU2LSjT_MOf/view) that is more editor-friendly has already been (mostly) designed. This improvements tab shows improvements that can be made to the exploration, categorized by bounce rate, incomplete learning, and specific wrong answers for cards.

The aim of this project is to implement the part of the improvements tab that covers “Card-Level Improvements > Needs Guiding Responses”. (The other parts are out of scope for this project.) 

The main challenge for this project is surfacing the necessary data for this view correctly and quickly. In order to do this, the data needs to be grouped and arranged properly in the backend for easy retrieval. This data should be kept up-to-date using Apache Beam jobs that are regularly run using a cron scheduler, but since there is a lot of data, there should be some aggregation and archival strategy so that the cron jobs do not need to perform computations on the full historical dataset each time. The aim of this project is thus to build out this data pipeline and ensure that it is robust, and display its output in an easy-to-understand way in the exploration editor improvements tab.

**Size of this project:** large (~350 hours)

**Potential Mentors:** @seanlip, @vojtechjelinek

**Knowledge/Skills Recommended:** 

* Knowledge and understanding of Python
* Ability to write Beam jobs
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Strong technical design skills

**Suggested Milestones:**

* **Milestone 1:** Implement the data pipeline for answer statistics. This should include (a) generating one-off archival models for historical data that can be queried quickly, (b) creating “realtime” models for each exploration/state that store the most recent set of answer data, (c) adding a trigger to update the archival model via a deferred job once the realtime model exceeds a certain number of distinct answers or storage size, (d) implementing the necessary queries and controllers to provide the “top wrong answers” data to the frontend. These jobs should work correctly in production.

* **Milestone 2:** Implement the UI for the “Card-Level Improvements > Needs Guiding Responses” section of the improvements tab. This section should correctly display answers for the various different types of interactions (note that the mock in the “Useful Resources” section only shows one such type, which is TextInput answers). It should also display an “Address Answers” call-to-action which, when clicked, brings the user to the relevant part of the main exploration editor tab, which would also open the “Add Response” dialog box with a reminder of the wrong answers they still need to address, so that they can add new answer groups and feedback for them (see more details [here](https://docs.google.com/document/d/1qQbW9Z_cgJ1mwU0hzBpPVS_4WLT_l_08ZixLR1G2bvQ/edit#heading=h.c63b1rerczu8)).

**Dependency on Release Schedule:**  Since this project involves a step to generate archival models, the timeline should be arranged so that this step can be run and verified during the appropriate release cycle. 

**Proposal notes:**

* One thing to consider when designing the data structure is versioning, and how to tell whether a set of answers is “still useful” for a given exploration version. A simple rule of thumb that could be used is whether the card still uses the same interaction type. Additionally (or alternatively), each wrong answer surfaced could include the date when it was last seen, and this can be used to filter wrong answers that have become obsolete. (Note that these are just ideas for you to consider, and it is fine if you decide not to go with these or have alternative suggestions. You may want to compare and contrast different approaches.)
* It's also worth thinking about how to handle the fact that answers may be submitted in different languages, now that we have the functionality for lessons to be played entirely in other languages. 
* We recommend taking a look at the existing codebase. Some good places to start are event_services.py, StateAnswersModel, and the stats_domain.py and stats_services.py files. Although these models and functionality may not be optimally implemented, they should be useful for getting a sense of what exists today.
* Note that an existing infrastructure for stats computations relied on a “continuous-computation” infrastructure in our codebase, which was deprecated some time ago (though you can see it in older versions of the codebase, in jobs.py). This infrastructure also relied on MapReduce jobs, which became obsolete after the recent migration to Python 3. Additionally, the previous infrastructure didn’t really handle versioning correctly. Thus, we would advise revisiting the infrastructure questions afresh and coming up with a clear technical design (that doesn’t assume that what exists in the codebase is already optimal).
* In general, we recommend that the proposal should examine the existing stats pipeline, describe how it works, and identify problems with it. It should then propose a technical design that would satisfy the criteria mentioned in this project (and explain in detail how statistics should be computed, archived, and surfaced), and describe how we would move from the existing pipeline to this new design. It is important to compare multiple alternative approaches to doing this (for example, there may be pros/cons associated with building an independent “realtime model” from scratch, vs making light modifications to the existing models).


**Useful resources:**
* UI mocks: [link](https://drive.google.com/file/d/1GOrwZhVKCunSmOgbvMDaGFU2LSjT_MOf/view?usp=sharing)
* How to write Apache Beam jobs: [wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) 
* Here is a somewhat outdated and incomplete [design doc](https://docs.google.com/document/d/1qQbW9Z_cgJ1mwU0hzBpPVS_4WLT_l_08ZixLR1G2bvQ/edit#heading=h.ylvrrqipsjif) that overlaps a bit with this project. Most of the doc is out of scope for the project, but you might find it interesting reading for context. The most relevant section is [this one](https://docs.google.com/document/d/1qQbW9Z_cgJ1mwU0hzBpPVS_4WLT_l_08ZixLR1G2bvQ/edit#bookmark=id.3fmayg4aifoi) in the "product design" part of the doc. Note that you do not need to follow the approach in the technical design section of that document (since, on reflection, it looks like the storage and display approach for NGR tasks would likely need to be handled differently from other tasks in the dashboard).
* Release schedule: [wiki page](https://github.com/oppia/oppia/wiki/Release-schedule-and-other-information) 

### 1.3. Helping learners when they get stuck
**Project Description:**

One core principle of Oppia lessons is that we never want the learner to get stuck, even if they’re working through the lessons on their own – i.e. without the assistance of a teacher, tutor, or parent. The aim of this project is to implement several improvements to the core learner experience to support this. Specifically, this entails:
- Adding a `dest_if_really_stuck` field to the Outcome structure in an answer group, and a way for creators to specify it (if they want to). This allows a creator to specify a separate state to go to if the learner is really stuck. Having this field would allow creators to provide a light hint in the feedback, and then provide a more dedicated step-by-step learning path if the learner subsequently needs further help.
- Detecting when a learner is stuck because the initial feedback they received isn’t clear/helpful enough for them (e.g. submitting too many wrong answers, or submitting the same or similar answers repeatedly), and then helping them using some combination of the following:
  - Providing the concept card pertaining to the linked skill ID, and recommending that they read it for a refresher and/or examples.
  - Taking them to the `dest_if_really_stuck` state, or proactively offering a hint, if either of those exists.
  - If the learner repeatedly submits the same wrong answer: saying something like “no, sorry, that’s really not the answer. Why don’t you try reading this and seeing if it helps?”, and pointing them to the linked concept card for the state so that they can learn more.
- Prohibiting lesson creators from sending the learner more than 2-3 cards back in the lesson due to a wrong answer, since this is discouraging for the learner. Lesson creators should instead be encouraged to refer the learner to a concept card, or implement a separate “revision pathway” using the `dest_if_really_stuck` field. Long “send-back paths” should result in a validation error in the exploration editor that should be fixed before the exploration can be saved.
- For TextInput interactions, if the learner's answer has an [edit distance](https://en.wikipedia.org/wiki/Edit_distance) of 1-2 characters from an answer that is marked correct (and isn't an exact match with a specific creator-defined wrong answer), say something along the lines of: "you're very close, you understand the concept, just check the spelling of word XXX" and let the learner retry it, rather than telling them "wrong answer" or redirecting them elsewhere. (Also, for the purpose of practice sessions and skill mastery, we should just note this response as a typo, and not count it as an error when recording stats in the backend.)

**Size of this project:** medium (~175 hours)

**Potential Mentors:** @kevintab95, @EricZLou

**Knowledge/Skills Recommended:** 

* Full-stack development: Python, Angular, TypeScript, HTML/CSS
* Learning design
* UX design

**Suggested Milestones:**
* **Milestone 1:** Allow creators to provide a destination state for the case where a learner is really stuck. Prohibit lesson creators from sending the learner more than 2-3 cards back in the lesson.
* **Milestone 2:** Detect when a learner is stuck and provide appropriate real-time assistance based on redirection to concept cards, the alternative destination state mentioned above, or proactive hinting. Detect small misspellings and provide the learner with appropriate help.

**Dependency on Release Schedule:** None.

**Proposal notes:**

* You can assume that learners won't get stuck on multiple-choice questions (mainly because there are a very limited number of possible answers).
* Your proposal should be clear about what triggers you are using to detect “stuck”-ness, and why. For example, you might write something like:
    * If the learner makes 3 incorrect responses, or has been on the question for 2.5 minutes, whichever is earlier: then, nudge them to look at the concept card.
    * Once the learner has actually looked at the concept card: if they then make 3 more incorrect responses that are _different_ from each other, or have been on the question for 2.5 more minutes, whichever is earlier: then, take them to the `dest_if_really_stuck` state if it exists, otherwise proactively offer the next hint if it exists, otherwise do nothing.
   (The above is just an example, but illustrates the specificity that would be needed. Additionally, you should justify the decision you make about how this system should ideally behave.)
* In your technical design, we would advise making the constants – such as 3 and 2.5 – easily parameterizable, so that they can be tweaked in the future.
* For the "catch misspellings" functionality, try to support multiple options for the text of this feedback so that it doesn't feel robotic. We would also need a way to translate this feedback into different languages, in a similar way to how we do this for the rest of the site.
* Creators might need to be able to turn off the "catch misspellings" functionality on a card-based level, since some language-learning explorations may explicitly want to test/teach spelling.
* You may have other ideas about how to improve the core learning experience on Oppia. These are welcome – feel free to include these in your proposal when fleshing out the product design section! In particular, there may be some potential in this project to teach learners metacognitive skills for how to deal with “being stuck”. There is a lot of research on this topic that can be found on the Internet. Proposals which demonstrate an understanding of this, and address this in a holistic way, will be viewed more favourably.

**Useful resources:**

* [PRD for this feature](https://docs.google.com/document/d/1TErYOB7aTg1cpalRhruH5L_TZCrvhUjbqlwHB5hReyA/edit). Note that this PRD might have some omissions, or be incomplete. If you see gaps, feel free to fill them in! You can also leave comments directly on the PRD if you have questions about what is written there.


### 1.4. Celebrating learners' accomplishments

**Project Description:**

We want learners to have an enjoyable experience when playing Oppia’s explorations, and to receive positive reinforcement whenever they reach an appropriate milestone. This project therefore involves:



* Celebrating the learner's completion of a lesson very overtly. This should happen when the learner reaches an “EndExploration” card. Specifically, we should make sure to recognize what the learner has learned, celebrate their accomplishment, and make it clear what the next recommendation for them would be (e.g. practice the skills they learned in a practice session or start learning the next lesson).
* Celebrating the learner's achievement (perhaps a bit less overtly) when they finish a streak of questions within a lesson. For simplicity, this can be considered to be just before they reach a new checkpoint. 

**Size of this project:** medium (~175 hours)

**Potential Mentors:** @kevintab95, @iamprayush

**Knowledge/Skills Recommended:** 



* Frontend development: Angular, TypeScript, HTML/CSS
* Animations in Angular
* Graphic design
* Game design
* Teaching experience (not strictly needed, but likely to be useful for coming up with a proposal)

**Suggested Milestones:**



* **Milestone 1:** Celebrate lesson completion in a meaningful, actionable, and rewarding way for the learner.  
* **Milestone 2:** Celebrate checkpoint/milestone completion in a meaningful, rewarding way for the learner that encourages them to continue progressing.

**Dependency on Release Schedule:** None.

**Proposal notes:**



* This is a fairly open-ended project, and a lot of its difficulty is in the design. Although the coding is likely to be relatively straightforward, the crux is whether the resulting implementation achieves the goal of motivating learners to continue learning.
* The proposal should therefore include designs for how these experiences should look, and explain, as objectively as possible, why these will serve the desired purpose. You may wish to refer to game design techniques and design frameworks in your justification.
* From a technical perspective, you may need to explain how you will vary the feedback so that it remains meaningful and doesn’t become stale (or justify why the repetition is a good idea). Can you find a way to relate it more directly to what the learner has just accomplished? This might involve building some creator-facing components. 
* It is worth paying attention to providing _meaningful_ recognition that is rooted in good pedagogy and that helps learners develop a growth mindset. Ideally, learners will become more confident in their skills to tackle challenges, rather than viewing their abilities as fixed and beyond their control. Proposals which demonstrate an understanding of this, and address it in a holistic way, will be viewed more favourably.


**Useful resources:**

* Here is a link to a [design doc](https://docs.google.com/document/d/1eWHs46cOHcm7NuQl8pM9Dada9nTgg3GoCQLgQJSNmIY/edit) for the checkpoints functionality mentioned in Milestone 2.


### 1.5. Learner Groups MVP 

**Project Description:**

We would like to make it possible for teachers, tutors, and parents to support students who are using Oppia to learn. We are therefore planning to introduce Learner Groups, a feature which allows facilitators to provide recommendations and goals to help guide learners, and which allows learners to optionally share their progress so that facilitators can provide them with additional support.

The aim of this project is to add functionality for learning facilitators to guide and monitor a group of learners directly in the Oppia platform. Specifically, facilitators should be able to create learner groups and invite learners to join them, and learners should be able to sign up for these groups. Facilitators should be able to monitor the progress of learners in their learning group and identify opportunities to help them.

This project should cover the following:

* Allow facilitators to create, access, and manage their learning groups in a new “Teacher Dashboard” that any user can access, but that users can specifically select as their home page in their account Preferences page. 
* Allow facilitators to create a learning group and its associated syllabus, and see the details of their learning group (as well as the list of individual learners and their progress).
* Allow facilitators to invite learners to their learning group (via username), and enable those learners to join the learning group and set their sharing preferences. (For now, learners would need to remember the URL or store it somewhere – adding a “learner groups” page to the learner dashboard is out of scope for this project.)
* Allow learners to see the homepage(s) for the learning group(s) they’ve joined, which includes progress, preferences, and buttons to start practice question sessions and lessons (as recommended by the facilitator through the learning group’s syllabus).

**Size of this project:** large (~350 hours)

**Potential Mentors:** @aks681, @krishita30j

**Knowledge/Skills Recommended:** 

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Attention to detail (in terms of UI)

**Suggested Milestones:**

* **Milestone 1:** Facilitators can, from a teacher dashboard page, create a learning group and its syllabus, and view its homepage (which contains the details of the learning group, its syllabus, and the list of learners and their progress). 

* **Milestone 2:** Facilitators should be able to invite learners to join the group via username. Learners should be able to join the group, set their preferences (or edit them later), and see the group homepage (which contains their progress, as well as triggers for starting recommended activities from the syllabus).

**Dependency on Release Schedule:** None.

**Proposal notes:**
* As part of this project, applicants should propose the design for the new Teacher dashboard.
* The technical design should allow for the possibility of learning groups having more than one facilitator in the future (though you don’t need to implement this functionality as part of the current project).
* Milestone 1 involves the facilitator being able to see the list of learners and their progress in a learner group. However, since the functionality for joining a learner group will only be implemented in milestone 2, you will need an alternative way to simulate this scenario in milestone 1 so that the facilitator view can be validated. One way to do this is to temporarily add a button (perhaps with an input field for an existing username) to the admin dashboard that simulates a learner joining the group and making some progress; this button should only be visible in the Activities tab and should only be usable in development mode. You can subsequently remove this button once the necessary functionality has been implemented in Milestone 2. 


**Useful resources:**

* Here is a link to [some mocks](https://www.figma.com/file/lSYstyhrwf9whM29mFxc8E/Learner-Group?node-id=2%3A9680) for the learner group functionality: 

* Here is the [full PRD](https://docs.google.com/document/u/1/d/1GMkU_Vxi7Y69ZI4gRfxLaDpX-sWfaMZsGQdXasdeELQ/edit) for learner groups. Note that this GSoC project only covers **part of** the scope of this PRD – in particular, the following requirements are not in scope for this GSoC project:
Allow learners to see the learning groups they are a part of in their learner dashboard. (would access directly via link for now)
Allow learners to join by an “open link”.
Allow facilitators to see statistical information about the group’s progress.
Allow learners to block/report spammy facilitator invitations.



### 1.6. Improving some math interactions

**Project Description:**

The aim of this project is to update the existing interactions to support three use cases: (a) allowing learners to submit an answer using a number line, (b) allowing learners to submit an answer in the form of a percentage, and (c) for math interactions where learners enter input through a keyboard, making it easier for learners who are new to keyboards/computers to easily input characters which use the Shift key (such as +, %) or which are hard to find on a regular keyboard (such as ×, ÷).

This support is needed because (a) creators currently implement number lines using the ImageClickInput interaction, which results in a lot of fiddly work on the part of the creator and occasional bugs when a learner clicks between the regions defined by the creator; (b) creators are currently forced to use TextInput fields in order for learners to submit an answer in the form of a percentage, but this makes it hard to do “greater than / less than” answer validations; (c) learners who are new to using a keyboard sometimes get stuck when they need to type an expression like "6 + 4" because they don't know how to type a "+" character.

More details for the number line interaction:

* Lesson creators should be able to input the start and ending integers of the number line, as well as the desired interval length. The generated number line should then equally space out the marks along the number line between the starting and ending numbers. The creator should not be able to select an option where there are more than 10 or fewer than 3 points along the number line.
* Creators should then be able to specify the feedback the learner receives based on how they answer along different points in the number line. Care should be taken to correctly handle the case when the number line parameters subsequently change – a warning should be displayed to the creator if the corresponding rule becomes invalid.
* On seeing this interaction, learners should be able to select and drag their answer along the number line, with the cursor automatically “snapping” to the demarcated lines along the number line. Once they are satisfied with the location on the number line, the learner should be able to confirm their selection and receive feedback.


**Size of this project:** medium (~175 hours)

**Potential Mentors:** @iamprayush, @nithusha21

**Knowledge/Skills Recommended:** 

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Attention to detail (in terms of UI, including writing good UI documentation and error messages)

**Suggested Milestones:**

* **Milestone 1:** Implement the Number Line interaction (creator and learner views).

* **Milestone 2:** Implement a way to input percentages (creator and learner views). Also, make it really easy for learners to type symbols in the existing numeric/algebraic expression input interactions on both desktop and mobile.

**Dependency on Release Schedule:** None.

**Proposal notes:**
* It is important that the Number Line interaction works on all types of devices (mobile, desktop, tablet). The proposal should explain how the learner view will be made responsive to these different views. If the entire interaction can’t fit within the viewport, the proposal should explain how the user will still be able to easily drag or scroll to their desired answer along the number line.
* For the percentage interaction, there are two choices for implementation. One approach is to have it be a customization to the existing NumericInput interaction. The other is to implement a brand-new PercentageInput interaction. The proposal should compare both these options, and explain which one to go with and why (using a comparison table).
* For math symbol input, probably the simplest way to handle this (at least on desktop) would be to add buttons with individual type-able symbols below the input field. The proposal should clearly describe which math symbols will be shown in which circumstances. (You might want to take a look at the individual lessons on www.oppia.org/learn/math to get a sense of how the question-answering experience works for the current mathematics lessons, so that you can get a better sense for what needs to be improved on both mobile and desktop.)

**Useful resources:**

* [Extension overview](https://github.com/oppia/oppia/wiki/Extensions-Overview) wiki page
* [Creating new interactions](https://github.com/oppia/oppia/wiki/Creating-Interactions) wiki page
* While not necessarily directly useful for this project, you might find these blog posts from previous GSoC learners interesting reading: [Prayush’s math expression interactions](https://medium.com/@ThePegasus/google-summer-of-code-2020-with-oppia-7542804bb9e9); [Pulkit’s interaction implementations on Android](https://gist.github.com/aggarwalpulkit596/84c23a09cd4244624092f2967b0eae38).
* [PRD for this feature](https://docs.google.com/document/d/1cha8e5H4Dfb7t8cLL2VZYi02Ysk2YEdyyalY1dDqPXE/edit). Note that this PRD might have some omissions, or be incomplete. If you see gaps, feel free to fill them in! You can also leave comments directly on the PRD if you have questions about what is written there.


### 1.7. Blog integration

**Project Description:**

Last year, we built a [blog editor interface](https://medium.com/@rijuta_s/google-summer-of-code-2021-with-oppia-43e7a90c907b) in order to allow blog post editors to create and publish blog posts directly within the Oppia site. The aim of this GSoC project is to complete the viewer interface for the blog, and migrate all the posts from Oppia’s Medium blog page to it, so that we can use the new blog on the Oppia website going forward. We would also like to complete the statistics functionality in the blog editor page that would allow blog editors to see the number of views/impressions their blog posts receive, as well as any other features that may be useful.

For the viewer interface, the project entails creating a blog page at oppia.org/blog that displays published blog posts. Users should be able to:

* Quickly and easily view previews of all of our previous blog posts in chronological order, based on their original publication date
* Click on a blog post preview to view a full version of the blog post
* Filter/Search blog posts based on tags associated with each post, or keywords in blog post titles

The project also involves moving all existing blog posts from Medium to this new blog page. This can be done using any reasonable approach, as long as the blog posts are successfully migrated and look good on the new page. Once all blog posts are successfully migrated, a link to the blog page should be made accessible in the Oppia website’s navbar and footer. 

**Size of this project:** medium (~175 hours)

**Potential Mentors:** @gp201, @DubeySandeep

**Knowledge/Skills Recommended:** 

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Attention to detail (in terms of UI)

**Suggested Milestones:**

* **Milestone 1:** Create the blog homepage and individual blog post pages (but hide them behind a “development mode” flag for now). Blog editors should be able to create a new blog post (using the existing blog post creation infrastructure) and have it appear on the new blog page.
* **Milestone 2:** Migrate all blog posts from Medium to the blog page on Oppia.org, and ensure that all the blog posts look nice and display correctly for readers. Add a link to the Oppia navigation bar and footer that points to the new blog. Implement a page (or pages) that surface blog statistics showing the total number of views and reads for each post, author, and the overall blog.

**Dependency on Release Schedule:** Since migration of the blog posts needs to be done on the production server, the timeline for this project should be planned carefully so that the necessary functionality is deployed by the time the blog posts need to be migrated.

**Proposal notes:**

* Care should be taken to ensure that the blog page is accessible, and displays well in both desktop and mobile views. 
* You are welcome to suggest additional features in your proposal which would be useful for the blog, but if you do so, please justify why these are worth implementing from the user's perspective.

**Useful resources:**

* Mocks for the blog-related pages: [link](https://xd.adobe.com/view/9bb82409-cdca-432a-b11c-88324643e2c0-ceeb/grid). (You might also wish to see pages 6 and 11+ of [Rijuta’s GSoC proposal](https://github.com/oppia/oppia/wiki/pdfs/GSoC2021RijutaSingh.pdf) from 2021, which describe the intended product designs for these pages.)
* Mobile mocks for the blog: [link](https://www.figma.com/file/k960aiD0UXm3vajxm4M0kr/Blog-Integration?node-id=224%3A0)
* Release schedule: [wiki page](https://github.com/oppia/oppia/wiki/Release-schedule-and-other-information) 


### 1.8. Improving the lesson creation experience

**Project Description:**

The aim of this project is to provide three enhancements to the exploration editor page for lesson creators: (a) showing the history of metadata changes to an exploration; (b) showing the history of changes to a specific card and allowing that history to be browsed through; (c) allowing creators to see which languages a particular part of a lesson has been translated into when editing it, and to update those translations if appropriate.

(**Note**: If desired, you may submit a proposal for a <span style="text-decoration:underline;">half-size project</span> covering EITHER both options (a) and (b), OR option (c). If you do this, please label your proposal accordingly with “parts (a) + (b)” or “part (c)” in the title.)

For (a): The current exploration history tab allows comparison between each “state card”, but doesn’t include details of the exploration metadata. An additional box containing these details should be added to the comparison graph.

For (b): In the state editor, it should be possible to see a “Last edited by XXX at version YYY” annotation (excluding translation commits) at the bottom right. Clicking this should open a pop-up modal that shows the changes made to the card in that last edit, and a further link at the bottom right saying “Previously edited by XXX at version YYY” which, when clicked, advances the modal to the previous change, and so on. (This is intended to function a little bit like “git blame” in the GitHub UI.)

For (c): In the state editor, when a change is made to a part of a card and this results in a “should translations be updated?” pop-up modal, the modal should also include a list of the existing languages for which that content has been translated, and the currently-saved translations for those languages. The lesson creator should be asked to update these translations if the changes are trivial to do (e.g. the content is just numbers), and otherwise leave them alone by default. This will help to save some re-translation work for the community. **Note**: these translation changes should not be applied immediately – if the lesson creator subsequently discards their change before committing it to the backend, then those translation changes should also be discarded.

**Size of this project:** large (~350 hours); can be reduced to medium (~175 hours) if desired (see description)

**Potential Mentors:** @nithusha21, @kevintab95

**Knowledge/Skills Recommended:** 

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Ability to write Beam jobs
* Technical design skills
* (Ideally) Some UI/UX design skills

**Suggested Milestones:**

* **Milestone 1:** Creators should be able to see changes to an exploration’s metadata in the comparison view in the history tab. They should also be able to navigate through all the historical changes to a particular state (excluding changes that solely affect translations). 
* **Milestone 2:** Creators should be able to see a list of existing translations through the modal that pops up when they make changes to a published exploration, and should be able to edit those if the edits are easy to make.

**Dependency on Release Schedule:** Some sections of this proposal may entail writing Beam jobs to update existing server data. The timeline should be arranged so that such jobs can be run and verified during the appropriate release cycle.

**Proposal notes:**

* The main thing that is important to demonstrate in the proposal for this project is good technical design skills. Strong proposals would first show a good understanding of the current system, and correctly describe the parts of it that are relevant to the relevant subproject, before suggesting the minimal changes that would be needed in order to achieve the desired functionality. 
* For (b), some precomputation may be needed in order to retrieve the version of the "previous change" quickly.
* For (b), it would be useful to generalize the system so that one can go forward/back from any given state. This would allow additional useful functionality like clicking on a state in a particular version when it's shown in the history tab, and moving forward/back through its history. Be sure to handle state additions, deletions and renames correctly!

**Useful resources:**

* How to write Apache Beam jobs: [wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs)
* Release schedule: [wiki page](https://github.com/oppia/oppia/wiki/Release-schedule-and-other-information) 


### 1.9. Onboarding improvements

**Project Description:**

Oppia’s mission is to provide learners with an engaging and effective learning experience. However, today, when someone enters the site for the first time, they’re given little to no information about what Oppia is and how it works. This makes it difficult for learners, especially those who are new to using technology and the internet, to effectively use Oppia as a learning resource.

The aim for this project is to ensure that any learner, regardless of their previous familiarity (or lack thereof) with online learning platforms, is able to quickly and easily become familiar with Oppia and the lesson player.

This project will involve two major parts:
* Update the sign-in and preferences pages to allow users to self-identify as a learner, teacher, and/or contributor. (See [mocks](https://www.figma.com/file/rmE2w7UzcICchhX4RBAnYY/Nav-%26-Library-(Copy)?node-id=201%3A578_).) After a user logs in, they should be shown the relevant dashboard based on the homepage they chose in the signup process.
  * New users should default to only being learners, though they can change this in the sign-in page (and subsequently in their preferences page). Existing users should be migrated as follows:
    * If they have their default_dashboard set to “creator”, tick the creator checkbox
    * If they have their default_dashboard set to “learner”, tick the learner checkbox
    * If they’ve made any translation or practice question contributions, tick the contributor checkbox
  * After a new user signs up and creates a profile: if the user self-identifies as a learner, present a screen (or screens) explaining how they can use Oppia to learn effectively (specifically: learn new topics in the Classroom, practice the skills they learn with practice sessions, and refer to previously-learned skills using revision cards).
    * Note: The applicant is responsible for proposing mocks for this.
  * In the release in which this feature is launched, show a one-time dismissable notification to existing users (when they log in) saying that they can change their self-identification settings and providing them with an easy link to do so.

* Adding various prompts throughout the onboarding experience. **Note:** Each of these applies both to logged-in and logged-out users. For logged-in users, all of these should trigger at the account level (when the logged-in user visits the page for the first time). For logged-out users, all of these should trigger at the device level (when the user of the device visits the page for the first time).
  * When any user first enters the site, present them with a prompt to let them know that they can adjust the site language using the language picker in the top navigation bar. (Learners who are unfamiliar with similar practices on other websites often miss this, and we want to ensure that language is not a barrier for learners.)
  * On entering the Classroom page for the first time, after a short period of time to allow them to explore the page, present the learner with a prompt to let them know that they can begin learning or reviewing any topic by clicking on one of the cards.
  * When a learner enters a lesson for the first time, show them a very brief walkthrough of the main lesson player features – namely, the lesson card, audio player, and (when such a button is available and they haven’t clicked on it with 20 seconds) the “CONTINUE” (or similar) button. In the case where the first card’s interaction type isn’t a Continue button, the walkthrough should only include the lesson card and audio player; then, once the button to move to the next card appears, Oppia should show a helper tooltip if the learner hasn’t clicked that button within 10 seconds.

* Adding similar prompts as described above to onboard learners to the Learner Dashboard (which is their home page when they log in).

**Size of this project:** medium (~175 hours)

**Potential Mentors:** @krishita30j, @seanlip

**Knowledge/Skills Recommended:** 

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Ability to write Beam jobs
* UI/UX design skills

**Suggested Milestones:**

* **Milestone 1:** Make it possible for new and existing users to change their self-identification, and migrate existing users so that their self-identification fields are populated. Explain to new learners how they can use Oppia to learn effectively.
* **Milestone 2:** Add prompts throughout the onboarding experience so that learners can discover the language picker, classroom cards, and lesson player features. Add support for onboarding new users to the learner dashboard.

**Dependency on Release Schedule:** A Beam job will need to be run in order to populate the self-identification information for existing users. The timeline should be arranged so that this job can be run and verified during the appropriate release cycle.

**Proposal notes:**

* The proposal should propose mocks for how each of these requirements should look (unless mocks have already been provided). When proposing these mocks, please take care to ensure that the wording used is simple and easily understandable by a new visitor to the site, and doesn’t use terminology or jargon that won’t be clear.
  * It’s probably a good idea to get feedback from others on your proposed mocks, especially from people who aren’t familiar with Oppia, so that you can improve them. You will probably want to repeat this process until you’re certain that your proposed onboarding flow achieves the aims that you want it to.
* For the learner dashboard onboarding flow, it is up to you to propose what you want the onboarding experience to look like. You can use ideas similar to the ones for general onboarding, or come up with others, as long as what you propose is intuitive for new users.


**Useful resources:**

* [Onboarding mocks](https://www.figma.com/file/rmE2w7UzcICchhX4RBAnYY/Nav-%26-Library-(Copy)?node-id=201%3A578) (for self-identification)
* Release schedule: [wiki page](https://github.com/oppia/oppia/wiki/Release-schedule-and-other-information) 

---


## Contributor Dashboard Team

### 2.1. Contributor Recognition Infrastructure

**Project Description:**

The Oppia Contributor Dashboard (oppia.org/contributor-dashboard) allows users to submit suggestions for translations and practice questions, which are then reviewed and accepted/rejected. These contributions are important for making Oppia’s lessons accessible and useful for learners around the world, and we would like to recognize and credit users who have made significant contributions in this area. 

One idea we are interested in pursuing is to build a system that shows users their “impact”, modeled using points for completing tasks that ultimately provide value to learners (such as successfully submitting practice questions/translations and reviewing user-generated suggestions). We would like to use this system for the following use cases:



1. **Celebrating user milestones in their profile page.** This can be simply a list of “achievements/badges”, e.g. “Submitted 1/3/5/10/etc. translations!”, “Reviewed X translations (Y words total)!” accompanied by icons. This would be a nice way to thank users for their many contributions. We will probably also want some mechanism for notifying a user by email each time they achieve a milestone. 
2. **Allowing users to generate a “badge”/”certificate” from their main Contributor Dashboard page.** Frequently, student volunteers need to show proof of their contributions with data such as translated word counts. We would like to enable contributors to generate a record of their submission stats, along with their name and contribution dates. This can simply be shown as a table or image which the contributor can then screenshot (and share on social media, if they wish). Alternatively, a button could be shown that, when clicked, will result in a “certificate” file being downloaded to the user’s computer.

For this GSoC project, you should implement this system and surface it to users for the above 2 cases.

**Size of this project:** large (~350 hours)

**Potential Mentors:** @sagangwee, @bhavukJain

**Knowledge/Skills Recommended:** 



* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Some knowledge about game design might be useful

**Suggested Milestones:**



* **Milestone 1:** Complete the backend infrastructure. This includes adding data models (or updating existing ones) and writing methods to update them when a submission/acceptance/rejection action takes place, as well as writing one-off Beam jobs to initialize these scores/counters based on previous contributor actions (if possible). Additionally, the URL endpoints for surfacing data for the 2 use cases above should be added in the controller layer.
* **Milestone 2:** Implement the necessary frontend services to retrieve the impact scores, and update the relevant UIs to display contribution milestones and generate contributor stats for the 2 use cases above.

**Dependency on Release Schedule:** None.

**Proposal notes:** 



* Your proposal should clearly outline the scoring algorithm and different scoring “buckets” you plan to use, and the reasons supporting it. (Note that additionally maintaining separate fields with the raw data makes it possible to change how we display the summary data to users in the future.) You are welcome to use the following ideas as a baseline (but make sure to think through the various corner cases, e.g. what should we do, in principle, if the original content gets deleted/modified after a translation suggestion has been made):  
    * For translation submissions: points should probably correlate in some way to the length/difficulty of the translation. One idea is to add (M * translation word count) to a user’s “translation submission in language L” score if the submission is accepted (where M is a multiplier to be determined), and subtract a small constant amount if a submission is rejected. This score change is only applied when the submission is accepted, not at the time of submission (to avoid the user seeing their score go up and then down) – though it might be interesting to show users their “potential score increase if accepted” for translations that are still awaiting review.
        * An alternative approach could be to maintain separate counters for “number of translations submitted/accepted”, “word count of submitted/accepted translations”, etc.
        * If you decide to go with an approach like the above, please describe how you would handle the calculation of the “translation word count” for cases where the translation includes images, alt text, or math formulae.
    * For practice question submissions: similar to above, but probably adding a constant value for each practice question instead.
    * For translation reviews: 
        * If the reviewer accepts a submission as-is, add 1 to their “number of accepted translations in language L” score. 
        * If the reviewer edits the submission and then accepts it, add 1 to their “number of fixed-and-submitted translations in language L” score.
        * If the reviewer rejects a submission, add 1 to their “number of rejected translations in language L” score.
        * If the reviewer accepts/rejects a submission, additionally add the number of words in the submission to their “number of words reviewed” score.
    * For practice question reviews: similar to above.
* Your proposal should provide a clear explanation of how these scores and relevant contribution metadata (e.g. milestones reached) will be represented, stored and updated, so that they can be retrieved **quickly** when the user loads the relevant page in the frontend. (You might want to consider the pros/cons of storing milestone completions explicitly, vs. computing them on the fly.) 

**Useful resources:**



* [User documentation for contributor dashboard](https://oppia-lesson-creator-documentation.readthedocs.io/en/latest/contributor/contribute.html)
* [Contributor Dashboard Design Overview](https://docs.google.com/document/d/1wM9cQzq1-3nbEhZliRlpnGDXbM_HspNkY16CYnA6lWg/edit)
* [Populating test data in the contributor dashboard](https://docs.google.com/document/d/1JYX4nvTcblaVVYAlTi7rApE0lWSBx0v_ZCCr_8WW4Wc/edit?usp=sharing)
* [https://github.com/oppia/oppia/wiki/Storage-models](https://github.com/oppia/oppia/wiki/Storage-models) 


### 2.2. Making the Contributor Dashboard UI Responsive

**Project Description:**

The Oppia Contributor Dashboard (oppia.org/contributor-dashboard) allows users to submit suggestions for translations and practice questions, which are then reviewed and accepted/rejected. Unfortunately, the existing contributor dashboard has only been developed with a focus on desktop/laptop users. Many of our contributors don’t necessarily have easy access to desktops/laptops, and we would also like users of mobile devices to have a seamless experience when submitting translations and practice questions.

The aim of this project is therefore to implement a responsive UI for the contributor dashboard page and related user flows, based on these [mid-fidelity](https://www.figma.com/file/FNA3qSJP2dLmQMMnjgMLQI/Contributor-Dashboard-(final-draft)?node-id=0%3A1) and [high-fidelity mocks](https://xd.adobe.com/view/8eeae0ca-4aaa-4b6e-84e2-a80796089530-dbb9/?fullscreen). (Please use these mocks as a reference – you shouldn’t be creating your own mocks from scratch for this project!)

**Size of this project:** medium (~175 hours) 

**Potential Mentors:** @DubeySandeep, @sagangwee

**Knowledge/Skills Recommended:** 



* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Responsive design
* Attention to detail (in terms of UI)

**Suggested Milestones:**

* **Milestone 1:** Implement the mobile UI for the contributor dashboard landing page (this includes the overall navigation, as well as the user’s review/submission history).
* **Milestone 2:** Implement the mobile UI for the translation and question submission pages (this includes both the list of opportunities and the submission workflow)

**Dependency on Release Schedule:** None.

**Proposal notes:** 

* We encourage you to explore ways to make the user experience on mobile devices as intuitive as possible. If you see any improvements you can make to the flow, please feel free to suggest them. (Optionally, if you like, you can also register to help translate lessons through the [volunteer interest form](https://docs.google.com/forms/d/e/1FAIpQLSc5_rwUjugT_Jt_EB49_zAKWVY68I3fTXF5w9b5faIk7rL6yg/viewform) – this may help you get a sense of the workflow, but please only sign up if you are proficient in the language in question and are actually interested in helping out in this way.)
* When writing your proposal, please explain how you plan to keep the responsive CSS easy to maintain. We recommend that you follow an approach that is consistent with other parts of the codebase, rather than inventing something brand-new just for the Contributor Dashboard. 

**Useful resources:**

* [User documentation for contributor dashboard](https://docs.google.com/document/d/17jMFtfHVWtJYrzyGQUKdsRXgky7lWv76sGYLOxSbA5w/edit)
* [Contributor Dashboard Design Overview](https://docs.google.com/document/d/1wM9cQzq1-3nbEhZliRlpnGDXbM_HspNkY16CYnA6lWg/edit)
* [Populating test data in the contributor dashboard](https://docs.google.com/document/d/1JYX4nvTcblaVVYAlTi7rApE0lWSBx0v_ZCCr_8WW4Wc/edit?usp=sharing)


### 2.3. Adding a Contributor Dashboard Stats page

**Project Description:**

Oppia has a contributor dashboard that allows contributors to submit translations for lessons (i.e., explorations), as well as practice questions for skills. However, it is currently not straightforward for translation and practice question coordinators to see the status of translation and practice question completions. We would like to create a public page, located at the URL /contributor-dashboard-stats, to display the translation/practice-question progress for each topic/skill for everyone to see.

This page should be designed to serve the following use cases (these are described for translators only, but similar use cases should also be handled for practice question coordinators, though with skills instead of lessons):



* Make it easy for translation coordinators to see which languages are nearly completed, so that they can (a) make plans for filling up the gaps, and (b) let the relevant country teams know when the lessons will be ready.
* Make it easy for translation coordinators to see the recent rate of progress in a particular language, so that they can bring on more translators for languages which need attention.
* Make it easy for translation coordinators (and anyone else who’s interested) to understand the overall status of translations for a particular language, so that they can project when Oppia’s lessons will be fully available in their language. 
* Make it easy for practice question coordinators to do the analogous things represented by the 3 bullet points above. 

Note that translation and practice question coordinators will typically be interested in whether all lessons for a particular topic have been translated into a particular language, and whether all skills in a particular topic have sufficient practice questions, respectively. Although the completion of translations for a particular lesson (or questions for a particular skill) is important, that is only a secondary metric since, e.g., we cannot launch a topic in a particular language if only half the lessons are translated.  

**Size of this project:** medium (~175 hours) 

**Potential Mentors:** @bhavukJain, @DubeySandeep

**Knowledge/Skills Recommended:** 



* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Responsive design

**Suggested Milestones:**



* **Milestone 1:** _Backend_: Write jobs to compute and aggregate the necessary data. Create the necessary API endpoint controller methods to surface this data to frontend clients.
* **Milestone 2:** _Frontend_: Implement the frontend services and UI for the /_contributor-dashboard-stats_ page. Add any necessary affordances to ensure that translation and practice question coordinators can easily answer their questions. Demo this dashboard to the PM and translation coordinator teams, and get explicit confirmation that it fully meets their needs.

**Dependency on Release Schedule:** None.

**Proposal notes:** 



* It is important that this page loads fast. Thus, unless you can find an easy way to generate all these statistics on-the-fly, you might want to consider performing the stats computation in a daily Apache Beam batch job, and storing the results for quick retrieval. This [wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) has more details on how to write batch jobs.

**Useful resources:**



* [User documentation for contributor dashboard](https://docs.google.com/document/d/17jMFtfHVWtJYrzyGQUKdsRXgky7lWv76sGYLOxSbA5w/edit)
* [Contributor Dashboard Design Overview](https://docs.google.com/document/d/1wM9cQzq1-3nbEhZliRlpnGDXbM_HspNkY16CYnA6lWg/edit)
* [Populating test data in the contributor dashboard](https://docs.google.com/document/d/1JYX4nvTcblaVVYAlTi7rApE0lWSBx0v_ZCCr_8WW4Wc/edit?usp=sharing)
* [Writing Apache Beam jobs](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs)
* [Contributor Stats Design Doc](https://docs.google.com/document/d/1JEDiy-f1vnBLwibu8hsfuo3JObBWiaFvDTTU9L18zpY/edit#heading=h.xktwhwyu0mji)


---


## Angular team


### 3.1. Migrate the exploration editor page to Angular, and move the entire frontend to the Angular CLI

**Project Description:**

The Oppia team has been working on a migration of the entire codebase from AngularJS – which is now deprecated – to Angular. This project aims to do two things: (a) migrate the exploration editor page (one of the last pages to be migrated) and all its subcomponents to AngularJS, and (b) move all the pages in Oppia from the current Webpack build system to the Angular CLI with ahead-of-time (AOT) compilation, so that all pages are precompiled and load faster when requested by users. (This would also mean that we don’t need to serve the Angular compiler to users, thus reducing bandwidth requirements as well.) 

Please note that moving all the pages to the Angular router is a prerequisite for moving to the Angular CLI.  (However, this should be straightforward, and in fact has already been done for most pages.) Additionally, this project also entails removing Webpack as a separate standalone dependency after the migration of the build system to Angular CLI is complete.

**Size of this project:** large (~350 hours)

**Potential Mentors:** @ashutoshc8101, @srijanreddy98

**Knowledge/Skills Recommended:** 



* Having a good understanding of the Angular router
* Having an in-depth understanding of Angular CLI and the Angular build system
* PRs related to the Angular migration project that demonstrates your ability to migrate from AngularJS to Angular 2+

**Suggested Milestones:**



* **Milestone 1:** Remove AngularJS from the exploration editor page.
* **Milestone 2:** Move all pages to use the Angular router and use ahead-of-time compilation with Angular CLI. Remove Webpack completely from the codebase.

**Dependency on Release Schedule:** None, though this project would also require some test runs on the prod server to make sure the new build system works well.

**Proposal notes:**



* The proposal should include a breakdown of the exploration editor migration project into conceptual sub-parts, with a description of any potential blockers and how you plan to overcome them. You don’t need to go into detail about how you would migrate specific files beyond the above; it is sufficient to include links to existing Angular migration PRs you’ve made in order to demonstrate familiarity with the domain.
* The proposal should show that the new angular config works well with dev builds (preserving auto-rebuild when files change), production builds, e2e test runs and unit test runs.

**Useful resources:**

* [CLI Overview and Command Reference](https://angular.io/cli)
* [Angular Migration Wiki Page](https://github.com/oppia/oppia/wiki/Angular-Migration)
* [How to test features on production](https://github.com/oppia/oppia/wiki/Testing-jobs-and-other-features-on-production)

---


## Backend team


### 4.1. Make backend code typed

Last year, we introduced MyPy (Python typing) into the codebase. This year, we want to fully type all remaining parts of the backend codebase. Also, as part of this, we would like to remove the existing docstring typeinfo annotations (and update the docstring lint checks accordingly) so that there is no duplicate type information.

Please make sure that when typing the files in _core/controllers_ all the handlers in the file have schema validation enabled, if not then also add a schema validation.

After this project is finished, all Python files in the Oppia codebase should be typed, and there should be no typeinfo in the docstrings.

**Size of this project:** large (~350 hours)

**Potential Mentors:** @aasiffaizal, @vojtechjelinek

**Knowledge/Skills Recommended:** 



* Knowledge and understanding of MyPy, preferably not only basic typing structures but also more advanced concepts like literals, generics and overloads.
* Knowledge of Python and also our backend tests, since refactors may be needed in some places.

**Suggested Milestones:**



* **Milestone 1:** Fully type core/domain and core/jobs.
* **Milestone 2:** Fully type core/controllers and other remaining files.

**Dependency on Release Schedule:** None

**Proposal notes:** 



* Your proposal should include details of the order in which you want to handle the typing of files, and an explanation of why you picked that order. Also, please explain how you plan to handle the removal of typing info from docstrings.
* You may omit the following sections from your proposal:
    * Additions/Changes to Web Server Endpoint Contracts
    * Calls to Web Server Endpoints
    * UI Screens/Components
    * Data Handling and Privacy
    * [Web only] Storage Model Layer Changes
    * [Web only] Web frontend changes

**Useful resources:**



* [Backend Type Annotations wiki page](https://github.com/oppia/oppia/wiki/Backend-Type-Annotations) 
* [MyPy documentation](https://mypy.readthedocs.io/en/stable/) 


### 4.2. Improve the frontend type system

Our frontend codebase is fully typed, but our typing doesn’t yet pass strict TypeScript checks. In this project, you should firstly change the strict TypeScript config file so that all newly-added files need to be strictly typed, and then introduce strict typing for around 280 twins of files and tests for those files (so 560 files altogether). 

In your work, you should make sure that no more `unknown` type is used and also remove all the usage of `unknown` type from the newly strictly typed files. There can be rare exceptions where `unknown` is needed (like in error handling), there should be appropriate runtime checks and it should be supplemented with proper comments.

**Size of this project:** large (~350 hours)

**Potential Mentors:** @mridul-netizen, @srijanreddy98

**Suggested Milestones:**



* **Milestone 1:** Change the TypeScript config file so that all newly-added files need to be strictly typed. Introduce typing for 140 twins of files and tests for those files (so, 280 files altogether).
* **Milestone 2:** Introduce typing for 140 twins of files and tests for those files (280 files altogether).

**Knowledge/Skills Recommended:** 



* Knowledge and understanding of TypeScript typing, preferably not only basic typing structures but also more advanced concepts like literals, generics or overloads.
* Knowledge of frontend tests, since in some places refactors to tests might be needed.

**Dependency on Release Schedule:** None

**Proposal notes:** 

* Your proposal should include an explanation of how you plan to introduce the TS config change so that all newly-added files by other developers are forced to be strictly typed before they can be merged into develop. Also, you should explain in what order you plan to type the files, and an explanation of why you picked that order.
* You may omit the following sections from your proposal:
    * Additions/Changes to Web Server Endpoint Contracts
    * Calls to Web Server Endpoints
    * UI Screens/Components
    * Data Handling and Privacy
    * [Web only] Storage Model Layer Changes
    * [Web only] Web frontend changes

**Useful resources:**



* [Guide on defining frontend types](https://github.com/oppia/oppia/wiki/Guide-on-defining-types)
* [TypeScript documentation](https://www.typescriptlang.org/docs/handbook/) 
* [Frontend tests wiki page](https://github.com/oppia/oppia/wiki/Frontend-tests)


### 4.3. Fix validation errors

We are currently in the process of introducing Beam jobs for validating datastore models. These will enable us to validate various attributes of our models and fix any consistency errors that are detected. 

We are already aware of some existing issues with our data that can be fixed as part of this project. These include:


* Task set 1
  * Removing traces of ‘cloned from’ from old versions of some explorations ([#10828](https://github.com/oppia/oppia/issues/10828))
  * Fixing datetime fields in `LearnerPlaylistModel`, `CompletedActivitiesModel`, `UserSubscriptionsModel`,  and `UserSettingsModel`  ([#11616](https://github.com/oppia/oppia/issues/11616), [#12120](https://github.com/oppia/oppia/issues/12120))
  * Adding more validation checks for datetimes ([#12121](https://github.com/oppia/oppia/issues/12121))
  * Implementing a process to ensure that external storage models linked to a storage model are updated in case of storage model deletion ([#10809](https://github.com/oppia/oppia/issues/10809))
  * Fixing `CompletedActivitiesModel` and `IncompleteActivitiesModel` to only reference existing and public explorations ([#14968](https://github.com/oppia/oppia/issues/14968))
  * Fixing `GeneralFeedbackThreadModel` entities with missing related `GeneralSuggestionModel` entities ([#11736](https://github.com/oppia/oppia/issues/11736)) 
* Task set 2
  * Handling deprecated commands ([#10807](https://github.com/oppia/oppia/issues/10807), [#10820](https://github.com/oppia/oppia/issues/10820))
  * Fixing `UnsentFeedbackEmailModel` entities with missing `GeneralFeedbackThreadModel`s and `GeneralFeedbackMessageModel`s ([#14966](https://github.com/oppia/oppia/issues/14966))
  * Fixing `GeneralSuggestionModel` entities that are marked as rejected but are missing their final reviewer ID ([#14967](https://github.com/oppia/oppia/issues/14967))
  * Fixing `ExpUserLastPlaythroughModel` has a few validation issues ([#14972](https://github.com/oppia/oppia/issues/14972))
  * Fixing `GeneralFeedbackMessageModel.feedback_thread_ids` to only reference existing `GeneralFeedbackThreadModel` ([#14971](https://github.com/oppia/oppia/issues/14971))
  * Fixing `UserSubscriptionsModel` ([#14969](https://github.com/oppia/oppia/issues/14969))

Note that this project **will not** entail writing new validation jobs from scratch, though in some cases it might require small modifications to the existing validation jobs. (For example, we might decide that, in some model property, we want to allow more values, and thus need to modify the validation job to account for that.) However, it does require writing jobs to fix production data (based on known validation issues), running those jobs on a test instance, and then running those jobs in production.

**Size of this project:** medium (~175 hours) or large (~350 hours). <span style="text-decoration:underline;">Note</span>: We would recommend taking up this project as a longer-term one (e.g. until November) with fewer hours per week, since it can take time to verify the validations on a server with production data.

**Potential Mentors:** @EricZLou, @ankita240796

**Suggested Milestones:**



* **Medium project:**
    * **Milestone 1:** Fix 3 tasks from _Task set 1_ or _Task set 2_.
    * **Milestone 2:** Fix the 3 remaining tasks from the set you picked in _Milestone 1_.
* **Large project:**
    * **Milestone 1:** Fix 6 tasks from _Task set 1_.
    * **Milestone 2:** Fix 6 tasks from _Task set 2_.

**Knowledge/Skills Recommended:** 

* Good knowledge of Apache Beam
* Ability to write Beam jobs
* A good understanding of the storage layer of the Oppia codebase 

**Dependency on Release Schedule:** There is some dependency on the [release schedule](https://github.com/oppia/oppia/wiki/Release-schedule-and-other-information), as Beam jobs are a critical part of this project and these are run on the prod server only once a month. Although we can run these jobs at any time on a test server, they will ultimately need to be run in production, so we suggest organizing your milestones and timelines around which jobs you would like to finalize by each of the release dates.

**Proposal notes:** 

* Make sure to provide example code for a Beam job that you will use to fix one of the issues. We will not judge you on its correctness. We just want to make sure that you've read the Beam job documentation and generally understand how to write Beam jobs.
* In your proposal, please explain how you plan to tackle the tasks from the list above. There are usually two parts to this: (a) making sure that we fix the current issues in our datastore, and (b) ensuring that those issues don’t reoccur in the future (which often requires doing a careful audit to prove that all possible “loopholes” that would allow them to occur have been plugged).
* When designing the Beam jobs to fix existing issues in our datastore, make sure that those jobs only make modifications that are strictly necessary. Be especially careful with updates or deletions, since it is important to avoid any data loss or corruption. For each task, you should specify how you would manually verify (on a test server) that the job has done the right thing after it is run, and what the rollback procedure for the job is (if something goes wrong while running it). 
* Also, note that, in general, the jobs you write should be designed to be **idempotent**. That is, running them twice should result in the same outcome as running them once (since this allows us to just rerun them if an error happens within the Beam framework).
* Make sure that you account for possible delays in the job testing procedure (when you submit job for testing on the backup server it might take up to 48 hours before it is tested.
* You can omit the following sections from your proposal:
    * Additions/Changes to Web Server Endpoint Contracts
    * Calls to Web Server Endpoints
    * UI Screens/Components
    * [Web only] Web frontend changes

**Useful resources:**

* ["Testing jobs and other features on production" wiki page](https://github.com/oppia/oppia/wiki/Testing-jobs-and-other-features-on-production) 
* ["Release schedule and other information" wiki page](https://github.com/oppia/oppia/wiki/Release-schedule-and-other-information) 
* [Apache Beam Jobs wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) 


### 4.4. Move and fix data in Google Cloud Storage

This project aims to make sure that our image and audio files in GCS (Google Cloud Storage) have the correct MIME types, and also aims to migrate the profile images from UserSettingsModel to GCS.

The project has three main parts:



* Introduce GCS IO for Beam jobs (should be placed in _core/jobs/io_), which will allow Beam jobs to work with files in GCS. (This is a prerequisite for the other parts of the project.)
* Validate that existing files in GCS have the correct MIME types ([#13480](https://github.com/oppia/oppia/issues/13480)), and fix those types if needed.
* Migrate profile images from UserSettingsModel to GCS and start using WebP for profile images ([Move user profile images to GCS](https://docs.google.com/document/d/1PXg3MJOnjmdIc3gN0faiii6Lzrecc-rGOVY9sL-wOWs/edit#heading=h.yq3m92owb3zz))

The GCS IO mentioned in the first part should offer the following interactions with GCS:



* Reading from files
* Writing into files
* Allow modifying file metadata
* Deleting files
* Getting the list of files in a folder

**Size of this project:** medium (~175 hours)

**Potential Mentors:** @vojtechjelinek, @aasiffaizal

**Knowledge/Skills Recommended:** 



* Good knowledge of Apache Beam
* Ability to write Beam jobs
* Knowledge of both Python and TypeScript, as this project has a full-stack component.

**Suggested Milestones:**



* **Milestone 1:** Introduce a new GCS IO for Beam jobs. Validate and fix MIME types in our GCS files.
* **Milestone 2:** Migrate profile images from UserSettingsModel to GCS and start using WebP for profile images

**Dependency on Release Schedule:** There is some dependency on the [release schedule](https://github.com/oppia/oppia/wiki/Release-schedule-and-other-information), as Beam jobs are a critical part of this project and these are run on the prod server only once a month. Although we can run these jobs at any time on a test server, they will ultimately need to be run in production, so we suggest organizing your milestones and timelines around which jobs you would like to complete by each of the release dates.

**Proposal notes:** 



* When designing the Beam jobs to fix existing issues in our datastore, make sure that those jobs only make modifications that are strictly necessary. Be especially careful with updates or deletions, since it is important to avoid any data loss or corruption. Specify how you would manually verify (on a test server) that the job has done the right thing after it is run, and what the rollback procedure for the job is (if something goes wrong while running it). 
* Also, note that, in general, the jobs you write should be designed to be **idempotent**. That is, running them twice should result in the same outcome as running them once (since this allows us to just rerun them if an error happens with the Beam framework).

**Useful resources:**



* ["Testing jobs and other features on production" wiki page](https://github.com/oppia/oppia/wiki/Testing-jobs-and-other-features-on-production) 
* ["Release schedule and other information" wiki page](https://github.com/oppia/oppia/wiki/Release-schedule-and-other-information) 
* [Apache Beam Jobs wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) 
* [Apache Beam GCS IO](https://beam.apache.org/releases/pydoc/2.36.0/apache_beam.io.gcp.gcsio.html)


---


## Developer workflow team


### 5.1. Achieve 100% Per-File Branch and Line Coverage for the Frontend and the Backend

**Project Description:**

Good test coverage is important for helping prevent regressions in the codebase. Currently, we have ~96% frontend line coverage, ~80% frontend branch coverage, ~99% backend branch coverage, and 100% backend line coverage. 

We want to achieve 100% per-file branch and line coverage for both the frontend and the backend. “Per-file” means that a given non-test file is fully covered by its associated test file. The goal of this project would be to (1) achieve 100% per-file branch and line coverage and (2) implement the testing infrastructure to ensure that this coverage is maintained.

**Size of this project:** medium (~175 hours)

**Potential mentors**: @U8NWXD, @gp201

**Knowledge/Skills Recommended:** 

* Experience using Karma to write frontend tests 
* Experience using unittest to write backend tests

**Suggested Milestones:**



* **Milestone 1:** Implement testing infrastructure and add 45% of the required tests.
* **Milestone 2:** Add the remaining 55% of required tests.

**Dependency on Release Schedule:** None.

**Proposal Notes:**



* In the “Testing Plan” section of the proposal, you should describe how you will confirm that the testing infrastructure that you set up works correctly. However, you don’t need to describe specific user journeys or end-to-end tests there.
* There may be some other contributors currently assigned to achieve 100% test coverage on some files, but please don't count on those files being finished before GSoC starts.

**Useful resources:**



* Karma’s coverage preprocessor has an option to apply coverage checks on a per-file basis ([docs](https://github.com/karma-runner/karma-coverage/blob/master/docs/configuration.md#check)), but we’ll probably need to stop combining tests into a single spec “file” at runtime for this option to work.
* We use coverage to calculate backend test coverage, and this tool has an option to check branch coverage ([docs](https://coverage.readthedocs.io/en/latest/branch.html)).


### 5.2. Migrate away from Protractor

**Project Description:**

The Angular team plans to [halt Protractor development at the end of 2022](https://github.com/angular/protractor/issues/5502). We need to move towards a new E2E testing framework. Ideally, we want a framework that:

1. Supports all existing Oppia functionality (e.g. some tools don't support opening new tabs)
2. Supports taking screenshots and videos. This doesn’t have to be supported natively (e.g. with protractor we use ffmpeg for screen recordings), but it should be possible to do.
3. Supports simulating mobile devices, slow connections, and offline mode.
4. Is easy to write tests for.
5. Is easy for us to migrate to.
6. Is fast and has low memory usage.

Most likely, no tool will excel in all of these areas, so we’ll need to find a tool that balances these goals. The aim of this project is to complete the migration of the existing e2e tests to this new tool.

**Size of this project:** large (~350 hours)

**Potential Mentors:** @SAEb-ai, @U8NWXD

**Knowledge/Skills Recommended:** 



* Familiar with protractor and whatever end-to-end testing tool you propose.

**Suggested Milestones:**



* **Milestone 1:** Set up the new tool with Github Actions, and migrate half of the existing e2e test suites. At this stage, we will probably have two scripts for running the e2e tests: one for Protractor suites and another for the migrated suites. On GitHub Actions, we will need to run both.
* **Milestone 2:** Migrate the other half of the suites, and remove all references to Protractor from the codebase. Document how we use the new tool.

**Dependency on Release Schedule:** None.

**Proposal Notes:**



* The Google team suggested six alternatives to Protractor: Cypress, Playwright, Puppeteer,  Selenium-webdriver, Testcafe and WebdriverIO. As Cypress has limited support for iframes and no support for new tab creation, and as Puppeteer does not have a proper migration guide, we have narrowed this list down to four frameworks which best suit Oppia: **Playwright**, **Selenium-webdriver**, **Testcafe** and **WebdriverIO**. (Even though a proper migration guide doesn’t exist for Selenium-webdriver, we’ve included it because it’s very similar to protractor in terms of APIs. Also, Protractor uses Selenium-Webdriver under the hood.)
* We recommend that you propose a e2e testing framework from one of the above four frameworks. However, if you know of some other framework which would suit Oppia better, you are welcome to propose that and support your choice by showing why it’s the best way to meet Oppia’s needs. In either case, we recommend showing a comparison table of available testing frameworks against the different criteria listed above.
* In the “Testing Plan” section of your proposal, you should describe how you will confirm that the testing infrastructure you set up works correctly. However, you don’t need to describe specific user journeys or end-to-end tests there.
* Your proposal should include a plan for how to seamlessly transition to the new end-to-end testing tool. For example, you might describe how we will run both Protractor and the new framework while the migration is in progress.

**Useful resources:**

* [Migrating from Protractor to Playwright - Official documentation](https://playwright.dev/docs/protractor). 
* [Migrating from Protractor to WebdriverIO - Official documentation. ](https://webdriver.io/docs/protractor-migration/)
* [Migrating from Protractor to TestCafe - Official documentation.](https://testcafe.io/documentation/403554/recipes/migration/migrate-tests-from-protractor-to-testcafe)
* [Future of Angular E2E & Plans for Protractor - Google's official issue announcing deprecation](https://github.com/angular/protractor/issues/5502): This includes some suggested alternatives from the Protractor team

---

## Android team

### 6.1. Android release automation

**Project Description:**

As the Oppia team prepares to establish regular releases of the Android app, having release automation is essential to ensure releases consistently launch without avoidable delays. This project introduces fundamental automation tools in order to support rapid and nearly fully automatic releases of the app.

The app release process this automation will support is as follows:

- Introduce scripts necessary to eliminate the major manual steps that occur during the production build process:
  - Incrementing the app versions such that version code, minor version, and major version are correctly updateable on the Oppia Android repository (since these need to be centralized to [one file](https://github.com/oppia/oppia-android/blob/develop/version.bzl)).
  - Cutting a new release branch and ensuring that it has the correct versions (and that the develop branch subsequently has the correct versions to avoid version reuse).
  - Verifying that a particular release is ready to be cut based on the following criteria:
    - Alpha: select test suites are passing on develop.
    - Beta: all tests are passing for the branch (including end-to-end tests which don't currently run in CI), and the release has been approved for beta by a TL via a message on a pinned issue corresponding to that release.
  - Patching the release for production use.
  - Replacing the third-party licenses by leveraging the third-party license extraction script.
  - Replacing the app assets with production assets for embedding using an asset downloader script (for security reasons, this script would need to be pulled from a private repository which we will provide).
  - Securely signing the app with the team's production key (this must be done in a way where the key cannot be leaked and will likely require proxying through a private GitHub repository).
  - Automatically uploading releases to the Play Store and launching them to a specific track.

- Once per day
  - Cut a new release per the criteria mentioned above
  - Automatically upload the alpha flavor of the release to the 'feature testing' internal testing release track of the app
  - Automatically upload the production (release) flavor of the app to the 'alpha' closed testing release track of the app

- Once per week
  - Try to create a new beta release:
    - Check the latest alpha release against the beta criteria mentioned above, and if they succeed then push the release flavor of the app to the 'QA' internal testing track
  - Try to promote the latest beta release:
    - Check that the latest beta channel has an approved beta confirmation from a TL per its stickied issue (based on app version) and, if it does, push the beta flavor of the app to the 'beta' open testing release track of the app

- Built releases will need to be outputted in a way that makes them easy to archive and upload to GitHub for when the specific version is released publicly.

Note that most of the development of this project will need to be on a separate repository with a separate Play Store app since the Oppia Android app would require production access. Team members with this access will help verify each individual milestone with the real app repository and Play Store project.

**Size of this project:** large (~350 hours)

**Potential Mentors:** @ankita240796, @BenHenning

**Knowledge/Skills Recommended:** 

* Familiarity with Bazel and Oppia Android scripts is highly recommended as many of the same patterns will be leveraged here (these scripts must be written in Kotlin with full automated testing).
* Familiarity with GitHub Actions or other CI frameworks will likely be extremely beneficial as the entirety of this project will be demonstrated via CI automation.
* Familiarity with build or release processes would help, but isn't necessarily a prerequisite.


**Suggested Milestones:**

* **Milestone 1:** Scripts exist to automate all manual parts of the release process as enumerated in the project description.
* **Milestone 2:** Releases are automatically cut and promoted based on the schedule described in the project description.

**Dependency on Release Schedule:** None.

**Proposal Notes:**

* The proposal's 'end-to-end' testing section should include details on how you will verify the new scripts and actions correctness manually (we don't write automated end-to-end tests for scripts). Note that we still expect thorough automated unit tests to be written for all scripts and their constituent components.
* Note that we're specifically looking for a proposal that demonstrates a well-explained design and implementation plan to fully automate Oppia Android's releases for alpha and beta.

**Useful resources:**

* [Android documentation](https://developer.android.com/studio/publish). 
* [Oppia Android Release Process](https://docs.google.com/document/d/1XAoXnQkn2oIAFkd6vY90tn_SSW3J9Eia0_4RhXhJSxQ/edit?usp=sharing)
* The [Bazel rule](https://github.com/oppia/oppia-android/blob/develop/oppia_android_application.bzl#L288) used to build deployable AABs

### 6.2. Interactive onboarding flow

**Project Description:**

The team has received user feedback that the app's current onboarding flow isn't clearly explaining how to use the app. This project fixes these gaps by introducing a more interactive onboarding experience to help users build intuitive context as they navigate throughout the app, and understand more precisely how to actually use it ([PRD](https://docs.google.com/document/d/1o9yiFhNmPTF1Hl1zJxXp8Mv4Q1hoc5Os_SrvE4sUpQg/edit)).

This project will introduce an in-the-moment “spotlight” for key interactive components of the app. A **spotlight** is a visual highlighting of a particular element on the screen, with text explaining what it is or how to use it. These spotlights should be implemented using [this](https://github.com/TakuSemba/Spotlight) or a comparable library. They should highlight the following key app functionality:

- Onboarding screen
  - In the first slide of the initial onboarding presentation seen by new users, show how to navigate to the next slide
- Profile page screen
  - An overview of the profile selection screen
  - Creating a profile (both admin and user profiles)
  - Setting a PIN
- Home screen
  - An overview of the home screen
  - Selecting a topic from the home screen
- Topic screen
  - The different icons of the topic screen
  - Selecting a lesson to play it from the lessons tab of the topic screen
- Exploration screen
  - An overview of the lesson screen, including lesson content and how to submit an answer
  - Playing/pausing audio
  - Changing the audio voiceover's language
  - Showing a hint to explain hints and solutions (note that this will likely require forcing a "dummy" hint to be shown since there may not be a guarantee that an actual valid hint can be shown in-context)
  - Explaining that the user can always quit via the back button and that their progress will be saved so that they can take a break and resume later

Note that each of these experiences may lead to multiple parts of the UI being highlighted, and should follow a predefined linear flow (i.e., for a particular screen, we would show the highlights in a specific order in the initial “walkthrough”). There should be an option to cancel out of the flow, and the app should not show it again if the flow is either canceled or completed. The app should show the onboarding flow the first time the user experiences whichever screen contains the interactive elements that should be explained. 

Also, please note that, users need to have an option in their profiles to reset their tutorial progress in case they want to revisit any tutorial instructions. The project also needs to include analytics (per the PRD) to ensure the feature is being used as expected once it's launched. Furthermore, all highlighted features should only be highlighted the first time the user encounters them (this is a reactive walkthrough experience), including those that are part of the exploration flow.

**Size of this project:** large (~350 hours)

**Potential Mentors:** @BenHenning, @rt4914

**Knowledge/Skills Recommended:** 

* Familiarity with Android UI development and automated testing, particularly in Oppia Android, will be a major help in writing a clear proposal. Understanding how persistence works in Oppia Android will also be important for writing the proposal.
* The applicant should also build familiarity with the linked [Spotlight](https://github.com/TakuSemba/Spotlight) library (or any reasonable alternative library that can meet the project requirements) and include clear details in the project proposal for how the chosen library will be integrated.


**Suggested Milestones:**

* **Milestone 1:** 
  * A platform parameter feature flag should be introduced to gate all user-facing functionality for this project (everything should be locked behind this flag).
  * The necessary domain components to represent the full, per-screen tutorial state with persistence should be implemented, with thorough testing.
  * The onboarding screen and profile page screens should be fully implemented and thoroughly tested, with a particular emphasis placed on demonstrating that profiles who've already seen the tutorials don't see them again, and that partial completion of a single segment of the tutorial re-prompts the full part of that tutorial upon reentry into the activity.

* **Milestone 2:**
  * The tutorials for the home, topic, and exploration screens are fully implemented and thoroughly tested.
  * A new end-to-end test suite, that mimics the journey that a new user would take, should be written to go through the entire tutorial flow.


**Dependency on Release Schedule:** None.

**Proposal Notes:**

* Note that we're specifically looking for a detailed explanation of the planned UI changes in your proposal. In particular, you should include visual mocks and diagrams to demonstrate the user experience in detail.
* We're also especially looking for a well-thought out technical design from the domain layer to the UI as this project will affect the full app stack.

**Useful resources:**

* See [this PRD](https://docs.google.com/document/d/1o9yiFhNmPTF1Hl1zJxXp8Mv4Q1hoc5Os_SrvE4sUpQg/edit) for a more detailed description of the planned functionality.
* You might find it useful to look at the [Lightweight Checkpointing proposal](https://docs.google.com/document/d/1YI4DtA5vbdJaoiL4tIBErgOvRm9fiIxfyDB6vr7zdQA/edit) from GSoC 2021, since it was also a full-app user-facing project and was well-organized.



### 6.3. Accessibility Improvements

**Project Description:**

We would like to ensure that the Oppia Android app is fully accessible to screen readers, and have identified a number of areas in which the experience could be improved. The aim of this project is to fix these issues so that the overall experience of using the app for such users is as smooth and intuitive as possible.

Specifically, this project entails the following parts:

- Ensuring that screens with similar UI components have a consistent UX throughout, for both sighted and non-sighted users. Here, “consistent” means two things: (a) sighted and non-sighted users have the same experience, (b) a user’s experience across different screens is the same (in cases where the screens use the same or similar components).
  - An example of (a): The flow for screen-reader users should be consistent with that of sighted users. For example, sighted users for left-to-right languages normally read a screen from the top-left and then start moving towards the right and then to the bottom. Similarly, the screen-reader should also start from the top-left and move to the next item in the same way. The experience should be adjusted appropriately for right-to-left languages such as Arabic.
  - An example of (b): Common components such as EditTexts and buttons should work the same way across all screens; all back-button icons on the top left should have the same  labels and content descriptions; etc. 
- Ensuring that the app is fully accessible for any combination of settings in the Android OS (such as magnified screens, large text, bed-time mode, night-light mode, lack of visible screen (with Talkback), etc.) and with different accessibility services. For all these combinations of settings, the app should pass the [Accessibility Scanner](https://support.google.com/accessibility/android/answer/6376570?hl=en) checks. (Note that “dark mode” support is being tackled as a separate effort and isn’t included in this GSoC project.)
- Ensuring that data persists when transitioning from portrait to landscape mode, and vice-versa. Basically – suppose the normal flow for a user is to do action X and action Y in sequence. Then, if a screen rotation happens after action X, the only action needed after that screen rotation should be action Y (without doing action X again). Some examples:
  - If any text is typed in an EditText and the screen is then rotated, the string should still be available.
  - If the user has selected a couple of options in an ItemSelectionInteraction, then, on rotation, those selections should persist.

**Size of this project:** medium (~175 hours)

**Potential Mentors:** @rt4914, @BenHenning

**Knowledge/Skills Recommended:** 

* Familiarity with accessibility programming techniques in Android.
* Familiarity with Android UI development and automated testing, particularly in Oppia Android, will be a major help in writing a clear proposal. Understanding how persistence works in Oppia Android will also be important for writing the proposal.

**Suggested Milestones:**

* **Milestone 1:** Ensure that screens with similar UI components have a consistent UX throughout, for both sighted and non-sighted users. Ensure that the app is fully accessible for any combination of settings in the Android OS.

* **Milestone 2:** Ensure that data always persists on screen rotations.

**Dependency on Release Schedule:** None.

**Proposal Notes:**

* Strong proposals would include specific documentation of user flows (specifically, pictures and an explanation of the flows) from an accessibility perspective (i.e. swipe navigation & textual, rather than visual, read-out) as part of the audit to clearly define both what the current user experience is, as well as what we want it to be, for all key flows in the app. This should demonstrate a consistent and cohesive accessibility flow, per the project description.

**Useful resources:**

* Oppia Android accessibility guide: [wiki page](https://github.com/oppia/oppia-android/wiki/Accessibility-(A11y)-Guide)
* List of accessibility tests we need to pass (note that this GSoC project is basically helping to audit and fix some of these): [spreadsheet](https://docs.google.com/spreadsheets/d/1lFQo2XE0dSGZcMvr7paxdL3zXB3FVcRnZOqD70DT3a4/edit#gid=0)
* Similar issues (to give some ideas of the types of challenges we face with accessibility): https://github.com/oppia/oppia-android/projects/13#column-15114947
* Some issues related to the "configuration changes" part of the project:
  * https://github.com/oppia/oppia-android/issues/1592
  * https://github.com/oppia/oppia-android/issues/1737
  * https://github.com/oppia/oppia-android/issues/1468
