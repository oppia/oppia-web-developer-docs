## Table of Contents
* [Completed Projects](#completed-projects)
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

Oppia has been selected to participate in [Google Summer of Code 2020](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers post-secondary students an opportunity to discover and work with open source organizations over the course of 3 months, while being paid a stipend. Students work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

You might be interested in our GSoC info pages from previous years: [2019](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2019), [2018](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018), [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions [here](https://github.com/oppia/oppia/wiki).

## Completed Projects:

The following projects were fully completed during GSoC 2020:

- [Abhith Krishna's proposal](pdfs/GSoC2020AbhithKrishna.pdf) and [final blog post](https://medium.com/@abyk476/google-summer-of-code20-with-oppia-1c5bd87ad9d7): Generate images for LaTeX expressions. Mentor: Sandeep Dubey.

    - **Milestone 1**: All RTE math expressions have a new “SVG filename” attribute in addition to the LaTeX value. For existing expressions, this filename will be an empty string. For newly-created expressions other than expressions created in suggestions, the filename will be non-empty and the corresponding SVG file is guaranteed to exist on the server (but will not be used for display yet).
    - **Milestone 2**: All RTE math expressions in the server (in explorations, questions, topics, skills, question/translation suggestions, and any other RTEs) include a non-empty SVG filename that points to a valid file. There is a validation job that can be used to audit this, and that validation job runs to completion successfully on existing production data.
    - **Milestone 3**: 
       - All math expressions are displayed using SVGs in the learner view. 
       - MathJax is fully removed from the learner view.

- [Anshul Hudda's proposal](pdfs/GSoC2020AnshulHudda.pdf) and [final blog post](https://medium.com/@anshulhudda.ssap/google-summer-of-code20-with-oppia-60208850be57): Fix the linter and implement all the lint checks. Mentor: Nitish Bansal.

    - **Milestone 1**: In non-verbose mode, the linter has less verbose output, and raises an exception if there is any error due to the operation of the linter script. All existing lint checks have tests written for them. The linter handles all general and CSS lint errors except for at most one CSS check, and the linter script has 100% test coverage.
    - **Milestone 2**: The linter fully handles all Python checks. All JS/TS lint checks are fully implemented, except for at most 11.
    - **Milestone 3**: The linter fully handles all JS/TS lint checks and CSS lint checks.

- [James James's proposal](pdfs/GSoC2020JamesJames.pdf) and [final blog post](https://medium.com/@jamesjay4199/google-summer-of-code-20-at-oppia-foundation-b2b39c3ebde7): Make Oppiabot more useful. Mentor: Ankita Saxena.

    - **Milestone 1**: All issue-related Checks and the following "PR creation" checks are fully operational:
       - WIP PR checks
       - PR branch name check
       - PR job check
    - **Milestone 2**: All Oppiabot checks that should run on PR creation, PR labelling, and force pushes are fully operational.
    - **Milestone 3**: All Oppiabot checks that should run on PR reviews, PR review comments, merge conflicts, and CI result publication are fully operational. In addition, the following periodic checks are implemented:  PR's aren't stale, issues are associated with a project.

- [Jim Zhan's proposal](pdfs/GSoC2020JimZhan.pdf) and [final blog post](https://medium.com/@jimz_89254/google-summer-of-code-20-with-oppia-a1a366d03aea): Ensure that Oppia is Fully Accessible. Mentor: Sagang Wee.

    - **Milestone 1**:
       - Set up LightHouse CI for automated testing
       - For the following web pages: Admin, Classroom, About, Collection_editor, Collection_player, Contact, Console_errors, Creator_dashboard, Community_dashboard, Delete_account, Donate, Email_dashboard, Email_dashboard_Result
          - Achieve Google Chrome Lighthouse audit report scores of 100
          - Complete manual accessibility review ([Review Checklist](https://docs.google.com/document/d/1UQpNSqVi2sSoj3nUiArdq5KgK0NPYuTbQrnSXAe5X-w/edit))
       - Develop and refine a robust manual testing methodology to catch accessibility issues that cannot be checked automatically by Lighthouse, and create documentation for this, so that the QA process includes a full suite of manual tests for accessibility starting from July onwards.
    - **Milestone 2**:
       - For all web pages listed above in M1, as well as: Error, Exploration_Editor, Exploration_Player, Get_Started, Landing, Learner_Dashboard, Library, Maintenance, Moderator, Notifications_Dashboard, Pending_Account_Deletion, Practice_session, Privacy.
          - Achieve Google Chrome Lighthouse audit report scores of 100
          - Complete manual accessibility review ([Review Checklist](https://docs.google.com/document/d/1UQpNSqVi2sSoj3nUiArdq5KgK0NPYuTbQrnSXAe5X-w/edit))
       - Users can use keyboard shortcuts to navigate to all critical pages (Get Started, Library, Creator Dashboard, Learner Dashboard, Profile, Notification, Preferences)
       - Users can use keyboard shortcuts for critical actions on the Library page and Exploration Viewer. Users also have a way of discovering these keyboard shortcuts
    - **Milestone 3**: 
       - For all web pages in the Oppia web application, including all webpages listed above in M1 and M2, as well as: Preferences, Profile, Review_Test, Signup, Skill_Editor, Splash, Stewards, Story_Editor, Story_Viewer, Subtopic_Viewer, Teach, Terms, Thanks, Topic_Editor, Topics_and_Skills_Dashboard, Topic_Viewer, and any other pages.
          - Achieve Google Chrome Lighthouse audit report scores of 100
          - Complete manual accessibility review ([Review Checklist](https://docs.google.com/document/d/1UQpNSqVi2sSoj3nUiArdq5KgK0NPYuTbQrnSXAe5X-w/edit))

- [Mariana Zangrossi's proposal](pdfs/GSoC2020MarianaZangrossi.pdf) and [final blog post](https://medium.com/@mari.zangue/my-journey-through-gsoc20-with-oppia-9eb6b27e7a02): Frontend testing of controllers and directives. Mentor: Nithesh Hariharan.

    - **Milestone 1**:  Achieve 100% coverage of non-inline controllers and fully cover 33 out of 69 inline controllers.
    - **Milestone 2**: Achieve 100% coverage of inline controllers and 87.5% coverage of files in /core/templates/pages/exploration-editor-page folder.
    - **Milestone 3**: Achieve 100% on some /core/templates/pages folders:
       - /exploration-editor-page
       - /subtopic-viewer-page
       - /profile-page
       - /library-page
       - /story-viewer-page
       - /review-test-page
       - /classroom-page
       - /community-dashboard-page
       - /learner-dashboard-page

- [Mohamed Medhat's proposal](pdfs/GSoC2020MohamedMedhat.pdf) and [final blog post](https://medium.com/@mohamed.medhat0298/gsoc-2020-oppia-foundation-ef9ecaf69903): Support tablet interfaces. Mentor: Rajat Talesra.

    - **Milestone 1**: Review and provide suggestions for all tablet mocks. Implement low-fidelity & high-fidelity code for tablet UI in the Onboarding Flow, HomeFragment , ProfileChooser, NavigationDrawer, and RecentlyPlayedStoryList.
    - **Milestone 2**: Implement low-fidelity & high-fidelity code for tablet UI in following screens: Topic including all Tabs, ExplorationPlayer, Hints & Solution, QuestionPlayer and Concept Card.
    - **Milestone 3**: 
        - Implement low-fidelity & high-fidelity code for tablet UI in following screens: 
           - Admin Controls
           - Options and its 3 child screens(Audio Selection, Language Selection and StoryTextSize Selection). 
        - Create an API in android which can take a screenshot in the test case and the image should be accessible for comparison.


- [Nishant Mittal's proposal](pdfs/GSoC2020NishantMittal.pdf) and [final blog post](https://www.nishantwrp.com/posts/google-summer-of-code-2020-with-oppia/): Solve all typescript and webpack issues in the codebase. Mentor: Vojtěch Jelínek.

    - **Milestone 1**:
       - All third-party libraries have type definitions.
       - All HTTP requests are made by backend-api-services. (Only in files migrated to angular).
       - There are less than 20 files in the codebase with ‘any’ under the issue # 7176.
    - **Milestone 2**:
       - There are no occurrences of ‘any’ in the codebase, except for the AngularJS constants $uibModalInstance, $uibModal, $rootScope and $translate (if these are not yet upgraded).
       - No PRs that reach the review stage have ‘any’ defined.
       - All backend api services migrated to angular return camelCase objects.
       - There is proper documentation on adding type definitions.
       - No PRs that reach the review stage have any typescript errors.
    - **Milestone 3**: 
       - There will be no generated third_party.js file.
       - All *scripts.ts files have been renamed to *import.ts
       - There will be no script imports,  except for jQuery, MathJax, and PencilCode embed.
       - The webpack compile speed will be reduced to under 30s for dev and under 120s for production (locally).
       - We may be using Webpack 5.0 (if a non-beta release is made by 15 August and it is compatible with our webpack config).
       - There will be documentation on:
          - Dealing with different types of typescript errors.
          - How our webpack config works.
          - How to deal with some common errors in webpack.

- [Prayush Dawda's proposal](pdfs/GSoC2020PrayushDawda.pdf) and [final blog post](https://medium.com/@ThePegasus/google-summer-of-code-2020-with-oppia-7542804bb9e9): Revamping Math Interactions. Mentor: Akshay Anand.

    - **Milestone 1**:
       - The Algebraic Expression Input and Math Equation Input interactions will be ready for lesson creators to use with the following two rules:
          - MatchesExactlyWith
          - IsEquivalentTo.
       - The old Math Expression Input interaction will be disabled (will not be visible in the Choose Interaction modal) in order to disallow any new explorations from using it.
       - An audit job will be merged and ready to run on production that will output the validity and type of inputs present in the explorations that use the old MathExpressionInput interaction. This will help in the migration of these explorations to the new interactions.
    - **Milestone 2**:
       - The Numeric Expression Input interaction will be ready to use with all its rules implemented.
       - A customized OSK will be added for mobile friendliness of the guppy editor.
       - A migration job will be merged and ready to be run on production that will appropriately upgrade the explorations that use the old math interaction based on the output of the audit job that would have been merged in Milestone 1.
    - **Milestone 3**: 
       - The migration job from M2 will be run on prod and no exploration on the production server will use the old MathExpressionInput interaction.
       - The following rules will be added to the Algebraic Expression Input and Math Equation Input interaction:
          - ContainsSomeOf
          - OmitsSomeOf
          - MatchesWithGeneralForm
       - The old Math Expression Input interaction will be stably deprecated and all related code will be removed from the codebase.

- [Pulkit Aggarwal's proposal](pdfs/GSoC2020PulkitAggarwal.pdf) and [final blog post](https://gist.github.com/aggarwalpulkit596/84c23a09cd4244624092f2967b0eae38): Additional Interaction Types. Mentor: Ben Henning.

    - **Milestone 1**: Fully implement the drag-and-drop sorting interaction in the Android app.
    - **Milestone 2**:
       - Fully implement the image region interaction in the Android app.
       - Implement backend support for ratio input.
    - **Milestone 3**: Fully implement the ratio input interaction in the Android app.

- [Rishabh Rawat's proposal](pdfs/GSoC2020RishabhRawat.pdf) and [final blog post](https://medium.com/@coolrishabhrawat/google-summer-of-code-20-at-oppia-foundation-944359e027fe): Editor Page Redesigns. Mentor: Sean Lip.

    - **Milestone 1**: Complete the Topics-and-Skills dashboard, Topic Editor page, and Skill Editor page redesigns (both mobile and desktop).
    - **Milestone 2**:
       - Redesign the Subtopic Editor(Desktop and mobile view)
       - Redesign the Story Editor(Desktop and mobile view)
       - Redesign the Chapter Editor(Desktop and mobile view)
    - **Milestone 3**:
       - Redesign the Question Editor(Desktop and mobile view)
       - Redesign the Exploration Editor(Desktop and mobile view)

- [Rohit Katlaa's proposal](pdfs/GSoC2020RohitKatlaa.pdf) and [final blog post](https://medium.com/@rohitkatlaa/my-work-with-oppia-during-gsoc20-8adf72de92bd?sk=573e4fe56ea30a4d9cee72aec541ed51): Adding SVG editor to RTE. Mentor: Kevin Thomas.

    - **Milestone 1**:
       - All required backend changes and validations will be in place.
       - It is possible to create and save the diagrams, but the UI for doing so will be hidden behind a flag variable (to be turned on for the public in Milestone 2). Saved diagrams will be displayed in the card content.
    - **Milestone 2**:
       - All E2E tests for the svg editor will be completed.
       - The flag variable is removed and the UI is fully available for creators.
       - The user will be able to use the pie chart tool to add pie charts to the editor.
    - **Milestone 3**: 
       - The user will be able to use the arc tool to draw arcs.
       - The user will be able to use the import image tool to import the required image into the editor.

- [Sarthak Agarwal's proposal](pdfs/GSoC2020SarthakAgarwal.pdf) and [final blog post](https://medium.com/@agarwal.sarthak262012/google-summer-of-code-2020-oppia-f7a71dba5506): Analytics Support. Mentor: Vinita Murthi.

    - **Milestone 1**: When a crash or an event arises, the corresponding crash report or event report is uploaded to the Firebase console when there is network connectivity. A full suite of unit tests will be written for both the crashlytics logging wrapper and the event analytics logging wrapper.
    - **Milestone 2**: In the absence of network connectivity, event analytics stats are stored offline. Logs will be stored in disk, with the maximum size of the files determined by a constant specified in the code. If the max size is reached, logs will be removed based on their priority and their recency (i.e. timestamp). This functionality will be achieved via a log persistence class. A full suite of unit tests will be written for the log persistence functionality.
    - **Milestone 3**: In the absence of network connectivity, crash reports are stored offline. In the presence of network connectivity, these offline records of crashes/events are uploaded to the firebase console using a work manager. There will be a full suite of unit tests for this work manager. In addition, event stats for the following 5 views of the oppia application can be analysed via the Firebase analytics dashboard: the home screen, and the 4 tabs of the topic page (i.e. info, lessons, practice, and revision). There is also clear documentation for how to create similar dashboards in the future for other views.

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

A: GSoC is intended to be a full-time commitment, so the main concern is whether you can still get the project done on time. Be upfront about your other commitments and make sure you schedule your time accordingly when creating your proposal. Other commitments you should list include time when you'll be in school and will commit less time to GSoC, time when you'll be travelling and away from GSoC work, any summer jobs you need to commit to, etc. We will try to be flexible around other time commitments, as long as your proposal convinces us that you will have enough time to complete the project by the end of the summer. On the other hand, if you do not disclose other commitments, and it turns out that you are unable to commit to what you wrote on your proposal, this is grounds for failing the program.

**Q: Which projects are most important for Oppia?**

A: All the projects we've listed here are important, and we'd be very happy to see good progress made on any of them! Projects are treated as equally important during selection. Note that the relative importance of a project to Oppia is not part of the [selection criteria](#selection-criteria). We would encourage you to pick a project that you would enjoy doing over the summer.

**Q: Can I submit more than one proposal to Oppia?**

A: Yes you can. However, we strongly recommend picking one project and writing a solid proposal for it. Splitting attention across multiple projects might not be a great idea. 

**Q: How early should I start working on the proposal?**

A: As early as possible. Make sure to get feedback from mentors before finally submitting the proposal. This will help you to write a better proposal as you can refine the details based on the feedback you receive. The mentors would need some time to review, and hence it is a good idea to begin as early as possible.

**Q: I only discovered this project recently. Does this mean that, during selection, my application would automatically be ranked lower than those by other applicants who have a longer tenure with Oppia?**

A: Definitely not! Here are the [selection criteria](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020#selection-criteria) we use when selecting students for GSoC; note that tenure is not part of these criteria. Also, our philosophy is to consider each application based on its own merits, not relative to other applications, and we try to accept every student whose application "meets the bar". The only cases in which we'd need to compare applications against each other are when a project idea receives multiple applications, or we receive fewer "slots" to host students than we originally applied for.

**Q: What are the minimum number of PRs that one should have?**

A: There is no specific minimum number. Remember that quality is more important than quantity. It is better to submit a nontrivial PRs rather than a simple bug fix. Start with starter issues, then prioritize ones that are related to your project.

**Q: What is the total number we'll accept?**

A: As many as we think we'll succeed, though GSoC admins may impose quotas.

**Q: I do not have any experience in some XYZ skill. Is some certification required?**

A: Try to work on good first issues and take courses online. You develop experience & expertise once you start working. We do not need any certification.

**Q: Is it okay to focus only on the frontend or backend?**

A: This depends on your project. Focus on the project's goals.

## GSoC Proposal Template

When submitting a proposal, please use the provided [GSoC proposal template](https://docs.google.com/document/d/1C6OgWa5I2wTWYPLTOqoZMVvWrVQ10BGXbe4SNEBMu-s/edit). We will only consider proposals submitted using this template.

You are welcome to ask mentors for reviews during the proposal preparation phase. Mentors will review proposals incrementally. That is, they will work through the Mocks section, and, only after they are satisfied with it, they will review the Technical Design section, and, similarly, only after that section looks good, they will review the Milestones section. This is meant to help ensure that later sections of the proposal are building on a solid baseline.

**Important:** Please make sure that your final proposal is self-contained. In particular, to be fair to all applicants, key components of the proposal should not be editable after the deadline, and you shouldn't assume that reviewers will follow external links.

### Tips for writing a good project plan

Here's some advice about proposals and milestone timeline planning that we collated from previous students and mentors:

- Choose a project you're interested in! If you have a strong interest in your project, this will help you pick up necessary skills and tackle any unforeseen difficulties that arise during GSoC.
- Familiarize yourself with the relevant part of the codebase for your project, especially if you haven't touched it before. It's important to think about how to integrate your project with the current Oppia structure -- don't design in a vacuum.
- Define milestones with enough detail to get a proper ETA for each milestone (so, don't just say "write e2e tests"), otherwise you run the risk of significantly underestimating the timeline.
- Clear written communication and presentation is crucial in preparing your proposal. The proposal should show that you have a clear understanding of the codebase and the final goal of the project. Eg. In a user-facing proposal, writing about just the files that have to be changed is not enough, detailed mocks and userflows (in the form of diagrams or points) are also essential.
- Limit proposal length. Remember a lengthy proposal is not equivalent to an excellent proposal.
- Ensure that the problem statement is within your limits to tackle. You should make sure that what you are proposing is within your capabilities. What we have in the [project ideas section](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020#oppias-project-ideas-list) are suggested milestones; it is up to you to come up with a complete plan that is within your ability. i.e., students can propose whatever they want; it’s up to us to subsequently figure out (during selection) whether we’re happy about what’s being proposed.
- Students who make milestone 3 bulky normally run into issues. So, make sure that you distribute work evenly.

### What should applicants expect from mentors in a proposal review?
* Please write your proposal on the assumption that you "own" your chosen project. From your perspective, the submitted proposal should be in as good a condition as possible before you ask for a review. Make sure you have a sufficiently good understanding of the codebase/project to find flaws in the design; don't assume that reviewers are responsible for doing this for you. Note that, by "as good a condition as possible", we don't mean that your proposal needs to be flawless -- we expect that you might make mistakes, and reviewers will be happy to guide you on how to improve. Instead, by "as good a condition as possible", we mean that your proposal should demonstrate:
  * Your ownership of the project
  * The research you have put into writing it
  * Your analytical skills
  * Your independence in making complex decisions
* Make sure to present solutions and ask for feedback, rather than just asking for solutions. You can do this by presenting the various solutions you came up with in your proposal, and doing an analysis of their advantages & disadvantages from the end-user perspective. Finally, choose the best solution you have and explain your reasoning behind your choice. Note that this doesn't mean that you must always have multiple ideas to solve a problem, but you should instead always explain how you reached a solution, and why is it the best one from the end-user's perspective.
* Mentor's suggestions are "suggestions", not orders (often, reviewers may not be certain whether their suggestion is correct), so, as the proposal owner, you are welcome to decide whether to accept/reject it. In either case, when you are accepting/rejecting a suggestion provided by a reviewer, explain your reasoning and the research that led to your decision. Don't use an "appeal to authority" (e.g. "I am doing it this way because XXX said so") -- the rational analysis that underlies the decision is what's important.
* We do not expect you to always agree with your reviewers. If you think that the suggestion doesn't suit your project, it is totally fine to explain your decision and provide reasons for it. It is always a good idea to have discussions when you have confusions, rather than simply agreeing. Note that this does not mean that we encourage you to disagree with your reviewers on everything -- this is just a suggestion to bear in mind if you get confused.
* Please note that your reviewer may or may not be involved in the final selection process. It is also **not** the case that you need to implement all your reviewers' suggestions/requests in order to be selected. As mentioned above, it is important that you actively take help and work together with your proposal reviewers in order to prepare a strong proposal that meets the guidelines for your chosen project.

### Sample proposals from past years

If you'd like to get a sense of what a proposal might contain, please see our [GSoC 2019 page](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2019) for examples of proposals that we accepted in 2019. Note that the [GSoC Proposal Template](https://docs.google.com/document/d/1C6OgWa5I2wTWYPLTOqoZMVvWrVQ10BGXbe4SNEBMu-s/edit) was only created in 2020, so although it may seem like none of the previous proposals follow the template, please be sure to follow it this year.

_**Note:** although some of these proposals are a bit on the long side, there's **no** formal length requirement for your proposal. In general, the quality of what you write is much more important than the amount of text you write, and we encourage you to write shorter proposals that still convey the main aim of the project. For the actual requirements, please see the [GSoC Proposal Template](#gsoc-proposal-template) section above._

## Types of work related to Oppia projects
In order to ensure a well-rounded engineering experience, developers will do some or all of the following depending on their project:
- Meet with their mentors regularly
- Meet with other contributors related to their project area
- Read and understand parts of the code base related to their project
- Receive code reviews for all code they write for their project
- Write automated tests for their projects
- Create UI mocks (if doing frontend development)
- Write design documents (if implementing large features or introducing new systems)

**[NEW!]** We asked our previous students what they learned during GSoC. Here are the collated answers:
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

## Oppia's Project Ideas List

_**Note:** If you're coming to this section from an external link, please make sure to scroll up and read this entire wiki page carefully, not just this section. There's a lot of useful information on the rest of the page, including a FAQ and a section describing selection criteria. Thanks!_

The following is a list of Oppia's 2020 GSoC project ideas. (Please note that all mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted.)

You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community in order to get feedback and guidance to improve the proposal. We also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

This year, the Oppia team is offering projects in four categories: Full-stack, Backend, Frontend and Android. Some of the project ideas are annotated with notes and suggestions from the mentors, but please bear in mind that the main purpose of these notes is simply to suggest ideas or possible starting points; they aren't meant to be prescriptive. You'd also be welcome to include discussions of other relevant aspects (that aren't mentioned in the notes) in your proposal. Also, please note that the suggested milestones are only suggestions. You are welcome to divide up the project in an appropriate way based on how you plan to approach it, as long as each milestone has a concrete deliverable and the timeline makes sense. For more information, see: [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan).


### Full-stack Projects

1.1. [Fix Exploration Saving Flows](#11-fix-exploration-saving-flows)

1.2. [Generate Images for LaTeX expressions](#12-generate-images-for-latex-expressions)

1.3. [Bulk Upload of Voiceovers](#13-bulk-upload-of-voiceovers)

1.4. [Add an SVG Diagram Editor to the RTE](#14-add-an-svg-diagram-editor-to-the-rte)

1.5. **[WITHDRAWN]** ~~[Provide an easy, lightweight way for students to log in to save progress](#15-provide-an-easy-lightweight-way-for-students-to-log-in-to-save-progress)~~

1.6. [Improvements to TextClassifier for ML based response to student inputs](#16-improvements-to-textclassifier-for-ml-based-responses-to-student-inputs)

1.7. [Image contributions](#17-image-contributions)

### Frontend Projects

2.1. [Editor Page Redesigns](#21-editor-page-redesigns)

2.2. [Solve all typescript and webpack issues in the codebase](#22-solve-all-typescript-and-webpack-issues-in-the-codebase)

2.3. [Frontend testing of controllers and directives](#23-frontend-testing-of-controllers-and-directives)

2.4. [Ensure that Oppia is fully accessible](#24-ensure-that-oppia-is-fully-accessible)

### Backend Projects

3.1. [Simplify the Oppia build process](#31-simplify-the-oppia-build-process)

3.2. [Validate data invariants between storage models](#32-validate-data-invariants-between-storage-models)

3.3. [Fix the linter and implement all lint checks](#33-fix-the-linter-and-implement-all-lint-checks)

3.4. [Make Oppiabot more useful](#34-make-oppiabot-more-useful)

### Android Projects

4.1. [Support tablet interfaces](#41-support-tablet-interfaces)

4.2. [Analytics Support](#42-analytics-support)

4.3. [Additional interaction types](#43-additional-interaction-types)

## Full-stack Projects

### 1.1. Fix Exploration Saving Flows

There are several serious issues with current saving/migration workflows in the exploration editor that can occasionally cause loss of work. In particular:
* When an exploration is updated, any existing suggestions in the feedback tab should be updated accordingly. Currently, such suggestions are not updated, resulting in a version mismatch and a loss of work when the exploration creator subsequently tries to apply the suggestion.
* When changes cannot be saved to an exploration, a "lost changes" modal pops up so that the creator can make a copy of their edits and then reapply them. However, the code for this modal is not robust, and in particular it does not take into account draft changelists that were stored in an older format. Thus, when it tries to display such drafts, it breaks and ends up not showing anything.
* Each model type (topic, story, exploration, etc.) currently has its own migration system, and all these systems are similar. We would like to consolidate this by having the migration functionality come "out of the box" when creating a new model type. This involves implementing a generalized migration system for all model types, and moving the migration methods to their own files.
* It's currently hard to tell the difference between a commit to an exploration that is a small typo fix, or a large content change. We would like to add support for creators to indicate whether changes to explorations are major/minor, in order to provide signal to inform Android app users when they might want to update their lessons.
* It is difficult to change an interaction into a slightly different one (e.g. from text input to number-with-input) without losing all the associated responses, hints and solutions. It would be nice to declare a suitable transformation that allows this data to be carried over from one interaction type to a closely-related one, and to auto-migrate as much of the responses as possible so that the creator does not lose their work.

The aim of this project is to fix any three of these issues.

**Team**: Learner and Creator Experience

**Potential Mentors**: @seanlip (primary), @kevintab95, @aks681

**Consider taking up this project if you...**

* Enjoy debugging and tracing through Python and JavaScript code to find out how something works
* Are familiar with the flow of logic between the Oppia backend and frontend
* Have good analytical and technical design skills

**Suggested Milestones**

Choose three of the issues above, and fix them. Fixing each issue counts as a single milestone.

**Notes**

Your proposal should include clear explanations for how you plan to solve each of the problems you decide to tackle. (This may entail repeating the sections suggested in the proposal template three times, since this GSoC project is essentially made up of three separate mini-projects.)

### 1.2. Generate images for LaTeX expressions

This project aims to introduce SVG rendering for all LaTeX expressions in explorations, so that MathJax can be removed as a dependency from the learner pages (which has the nice side effect of making the explorations load faster).

**Team**: Learner and Creator Experience

**Potential Mentors**: @kevintab95 (primary), @aks681

**Consider taking up this project if you...**

* Enjoy full-stack development (Python and Angular).
* Have good technical design skills.

**Suggested Milestones**

1. Extend the current "math expression" rich-text editor component to include an SVG field. The image for this field should be auto-generated for newly-created math expressions.
2. Migrate all existing expressions on the server to populate the SVG field, and validate that all SVG fields are populated.
3. Use the SVG image instead of the LaTeX when showing the formula to the user. Remove MathJax libraries from the frontend pages.

**Notes**
- The proposal should explain the convention for how the SVG files will be stored. (The rich-text editor component would only include a reference that can be used to compute the URL at which to retrieve the image.) Note that there is already a system for storing images in explorations, and we recommend reading the code to understand how it works so that you can implement something similar here.
- Proposals should include a clear explanation of how to carry out the migration procedure, as well as how to carry out an audit in order to ensure that the procedure has been performed correctly.

### 1.3. Bulk Upload of Voiceovers

Voiceover recording is an important feature for making lessons accessible in more than one language. As one of the most used features for creators, there are 2 ways voiceovers can be added to the platform: recording and uploading files. 

Recently there was a concern raised with the workflow for uploading files. The current workflow that exists for uploads is to update one section of the lesson at a time, which is quite time-consuming. The main aim of this project is to address this by providing voice artists and creators the ability to bulk upload files and give them improved control of assigning the individual audio files to desired sections of the lesson. This will streamline the process and reduce the time needed for adding voiceovers to the lessons.

**Team**: Audio and Translations

**Potential Mentors**: @mzaman07 (primary), @DubeySandeep

**Consider taking up this project if you...**

* Enjoy designing UI and care about UX.
* Want to expand on your frontend development skills (Angular).
* Have strong analytical and technical design skills.

**Suggested Milestones**

1. Implement a bulk upload function for audio files. Create a form that will take the resulting file upload(s). Cache all the files in the browser. Provide a way for the user to empty/refresh the cache.
2. Implement functionality that will allow the user to see all the cached files, play them as a preview, and assign files (or selections of files) to a lesson card. Ensure that the whole file upload process doesn't require refreshing the page, and is efficient in terms of network performance. Get confirmation from voiceover artists that the implemented workflow is a significant improvement over the previous one.
3. Apply minor cosmetic indicators to show that the file has been uploaded to Oppia. Display its byte size, duration, and mime type. If certain browser(s) have niche constraints, indicate that to the user.

**Notes**

- The main goal of this project is to improve the workflow for the voiceover artists. This requires careful consideration towards figuring out the correct UX design for the voiceover flow, so please make sure that you think carefully about the design and make it as intuitive as possible. Remember that voiceover artists will be using this flow a lot (there are perhaps 150 audio clips per exploration, typically), so it should not be cumbersome. The proposal should clearly explain the design and how it improves the experience. 

- You may need to do some research on the constraints of saving raw audio file data on different browsers. Each browser may have different constraints.

### 1.4. Add an SVG Diagram Editor to the RTE

The aim of this project is to introduce an SVG diagram editor in the rich-text editor (RTE). Creators can use this to create custom diagrams for their lessons in the browser itself. The images produced would then be stored as SVGs for use in the lesson.

**Team**: Learner and Creator Experience

**Potential Mentors**: @kevintab95 (primary), @aks681

**Consider taking up this project if you...**

* Enjoy debugging and tracing JavaScript code to find out how something works
* Are familiar with the flow of logic between the Oppia backend and frontend
* Have good analytical and technical design skills

**Suggested Milestones**

* Milestone 1: Complete the backend changes for introducing literallycanvas, svgedit or a similar editor to the RTE framework (eg. saving/retrieving SVG data).
* Milestone 2: Complete the frontend changes for the SVG editor.
* Milestone 3: Add at least 2 custom controls for standard types of diagrams (such as geometrical shapes for mathematics lessons) to the SVG editor. These should build on the existing editor and show that the editor can be customized easily to include new types of diagrams for specific types of lessons.

**Notes**

Your proposal should contain a detailed plan for each of the milestones. It should also include mocks for how the SVG editor would look like once it has been integrated into the RTE.

### 1.5. Provide an easy, lightweight way for students to log in to save progress

**(Update 19 Mar 2020) We are withdrawing this project because we've learned that having two login systems is likely to cause user confusion. Sorry for the inconvenience!**

Currently, the only way for a user to save their progress in an exploration is to log in with a Google account, which not every person may have or know how to create. The aim of this project is to create a lightweight and intuitive way to signup and login without having a google account, by just asking the user for a username, password, and optional email / mobile number, and then allowing them to login using these. Here, the username, email and mobile number (if provided) should be validated to be unique. (If a mobile number / email is provided, this can subsequently be used for profile recovery if the password is lost.)

This project also aims to add functionality in the corresponding user's profile page to support the upgrading of "lightweight accounts" into "full accounts" later on, if the user wants to link a google account to it and gain, e.g. editing privileges.

**Team**: Learner and Creator Experience

**Potential Mentors**: @aks681 (primary), @seanlip

**Consider taking up this project if you...**

* Are familiar with the flow of logic between the Oppia backend and frontend
* Are interested in creating an end-to-end user flow
* Have good technical design skills

**Suggested Milestones**

1. Finish the backend for signup/login using lightweight accounts, and implement the migration to add the mobile number field to the user model. Also, make sure that the email and mobile number fields are optional in the user model.
2. Create the signup and login page frontend that communicates with the backend that was created in the previous milestone.
3. Integrate these pages into the main website by editing the Signup button on the top right to show 2 options when clicked. Make sure login with redirect URL works as well. Also, write e2e tests for this functionality.

**Notes**
- The proposal should discuss the following design decision: is it better to build profiles on top of the existing UserModels or should there be a separate LightweightUserModel created instead? It is useful, when making this decision, to think through all the possible workflows (e.g. if we decide to use two separate models, would the lightweight model get deleted when linked to an account?).

### 1.6. Improvements to TextClassifier for ML-based responses to student inputs

Oppia provides several ways to interact with students when they are going through an exploration. Text input interaction is one such interaction, in which students provide their answer as a text string. Currently, Oppia uses "hard" rules such as ‘answer contains xyz’, ‘answer starts with abc’ etc… to figure out proper response to student inputs. Providing a proper response is very important, because an improper response may confuse students and lead to them leaving the lesson. These rules are created by the creators of the exploration. However, it is hard for them to enumerate all possible conditions. 

Recent advances in machine learning / deep learning could prove to be very useful here. The creator simply labels student inputs with proper responses which could be treated as training data in order to train an ML model. The goal of this project is to research and implement a machine learning model which can be used to provide appropriate responses to textual user inputs. This is a classification problem: based on training data, the model should predict the appropriate class which would map to a response that should be used by Oppia for the given answer.

Currently, Oppia has already implemented a naive version of such a classifier, which uses a Bag-of-Words and SVM model. The aim is to use techniques from recent advances in distributed representational learning in order to improve upon the current model.

**Team**: Machine learning

**Potential Mentors**: @prasanna08 (primary)

**Consider taking up this project if you...**

* Are excited about recent research in the NLP community (especially deep learning based models such as BERT, GPT).
* Enjoy reading deep learning research papers, critically analysing them, and implementing state-of-the-art models for your own experiments.
* Enjoy applying cutting-edge ML techniques to real-world, production environment specifications.
* Have a fair amount of experience with implementing models in Python (note that Oppia currently uses Python 2.7).
* Have experience coding in AngularJS or Angular.

**Suggested Milestones**

1. **Literature review**: Compile relevant research papers. Explore their methodologies, and implement them (possibly adapting code published by researchers), then test your implementations on the proposed datasets and compare the results with 1-2 baselines. Provide working implementations and a report of the results for at least the initially-proposed idea and the baselines. Submit a list of at least 4 ideas that you would like to try in the next month.
2. **Experiment and build a classifier**: Experiment with the ideas proposed in the previous milestone, and provide a report on the results, including a clear specification of the model you are going to implement in Oppia, as well as a full list of changes that are required to implement the classifier using the current ML pipeline. The performance of the final classifier must be adequate (compared to state-of-the-art performance on the proposed datasets), and it must satisfy the constraints in the “notes” section below. You will need to provide sufficient evidence to show that the classifier meets these criteria. 
3. **Implement and test**: Implement the final classifier in the Oppia code base, and create a dummy exploration on which it can be tested. Note that the responses that end up being given by the classifier in manual testing are the primary success criterion here (rather than the reports that were created in earlier milestones). Also, depending upon the model you propose, you might need to make some changes to the existing ML pipeline.

**Notes**

The ML pipeline implemented in Oppia performs the classification in the browser of a learner's machine. The models are trained by a backend server called “Oppia-ML”, and then they are transferred to the frontend where prediction is carried out in the browser in JavaScript. Hence, there are several constraints on the model which need to be adhered to:
1. The model must be small, i.e., it should fit within a few MBs. 
2. Inference must be fast on a machine with nominal specifications (4GB RAM, i3 process, no GPUs).
3. It must be possible to implement the inference code in JavaScript in the frontend. The backend could be anything Python-based (e.g. tensorflow, pytorch), but the inference code has to be implemented in JavaScript.
4. The model must have reasonably good performance (compared to state-of-the-art benchmarks) on natural language inference datasets (e.g. SNLI or equivalent).

The student proposal should focus on the following points. (**Important:** While preparing your proposal, please use [this](https://docs.google.com/document/d/1RiOlOKcztnjv69wyhUI-n17lmSN81Y2jKLpnna39bPs/edit?usp=sharing) template instead of the default one for the “Project Details” section of the proposal.)
* **Selection of promising techniques**. Start by providing a list of at least 3 deep learning / NLP / ML techniques that could potentially be used to address this problem. From this list, pick the most promising options and explain why you think they are the most promising; also, explain why the rejected options are not worth pursuing. Develop the promising options into initial ideas that (i) can be implemented and tested quickly and (ii) could form baselines for further experiments that you will do during GSoC. (These ideas do not need to be complex.)
* **Baselines**. Provide baseline models that you are going to compare against, and specify which metrics you will be using for comparison. Student should propose an ambitious baseline, rather than something simple such as “SVM with tf-idf”. (It may happen that, at the end of your experiments, your baseline turns out to perform the best; that is OK.)
* **Datasets**. Specify the datasets on which the classifier will be tested. One such example is SNLI, but you can use any dataset you wish, as long as you give an explanation on why that particular dataset would be a good choice.
* Prior experience. Provide details of any previous experience you may have with researching such models.

### 1.7. Image contributions

Art and graphics form an integral part of most explorations on Oppia, and are especially important for making lessons learner-friendly and communicating key concepts to learners, especially since good graphics can transcend language barriers. However, one major blocker when creating lessons is the lack of an easy way for designers/artists to add images to lessons. We would like to enable artists to contribute art to lessons as easily as developers can contribute code to GitHub repositories.

**Team**: Contributor Experience team

**Potential Mentors**: @DubeySandeep (primary), @sagangwee

**Consider taking up this project if you...**

* Are familiar with the flow of logic between the Oppia backend and frontend
* Are familiar with the state migration functionality
* Are familiar with the rich-text editor workflow 
* Have good technical design skills

**Suggested Milestones**

1. Build a separate section for images in different backend entities. Write migrations (if required) to populate these sections. Allow owners and editors of explorations to add placeholder images specifying what art is needed there.
2. Add new models for opportunities to contribute art to explorations, and present the available opportunities in the Community Dashboard page.
3. Allow contributors to submit a suggestion for available opportunities, and reviewers to review these suggestions.

**Notes**

A few things should be considered while writing the design doc:
- There should be a separate section in the state object which should have reference to images. (Similar to RecordedVoiceover and WrittenTranslation.) This will help establish a specific section in the backend objects which contributors can edit.
- While designing the workflow for the rich-text editor, please note that this editor is used in several different places (stories, topics, etc.). Currently, we aren't implementing the image suggestion workflow for those other places, but we might do so in the future. So, when designing the infrastructure for this project, it would be a good idea to think about how the functionality (such as any necessary changes to the RTE) can be reused in other places.
 
## Frontend Projects

### 2.1. Editor Page Redesigns

The aim of this project is to redesign the topic, exploration, story and skill editor pages so they are more visually appealing and work better on mobile, while retaining all of their features. Some initial mocks that we created visualizing these changes can be found here ([desktop](https://xd.adobe.com/view/3940de63-c416-4008-4b32-a73dc43fd7a1-4f71/), [mobile](
https://xd.adobe.com/view/84eb3b8d-3d19-4971-7e79-9ff756b25c83-f2da/grid)); please note that these mocks will be updated over time as we finalize the design. (Feel free to suggest changes to the mocks if you think that would enhance the creator experience, or ask any questions on the oppia-gsoc-discuss@ mailing list.)

**Team**: Learner and Creator Experience

**Potential Mentors**: @aks681 (primary), @kevintab95

**Consider taking up this project if you...**

* Are interested in UI/UX design
* Enjoy debugging and tracing JavaScript (and Typescript) code to find out how something works

**Suggested Milestones**

1. Complete the topic and skill editor pages redesign.
2. Complete the story editor page redesign.
3. Complete the exploration editor page redesign.

**Notes**

* The mocks for these editor pages will be provided. The goal of this project is to implement them.
* The proposal should explain the files that would be changed and briefly explain the nature of the changes to be made.
* The proposal review will be based on whether the student understands the codebase well enough, as well as past PRs related to the editor (or other user-facing) pages, with emphasis on attention to detail in the UI.

### 2.2. Solve all typescript and webpack issues in the codebase

The aim of this project is to complete all remaining typescript and webpack tasks in order to ensure a smooth development workflow. In particular:

* Remove all custom typings for typescript
* Remove "any" types for third-party libraries
* Remove all "any" types from the codebase
* Replace third_party and remaining `<script>` imports with webpack
* Reduce the overall time for webpack compilation (under 8s for develop and 60s for production builds)
* Add documentation on all typescript and webpack errors and solutions on how to fix them.
 
**Related issues**: 7601, 7434, 6431, 6351

**Team**: Dev Workflow

**Potential Mentors**: @vojtechjelinek (primary), @ankita240796

**Consider taking up this project if you...**

* Want to work with TypeScript and Webpack.
* Are fine with working mainly on the build process and not the final product.
* Enjoy making processes simpler and easier to understand.

**Suggested Milestones**

1. Remove all custom typings for typescript. "Custom typings" denotes the extra typing files that we have for jQuery, HTML element and scope defs. We have custom type definitions for third party libraries [here](https://github.com/oppia/oppia/tree/develop/typings). We need to remove these and add our own typedefs for third party libraries instead of defining them as "any".
2. Remove "any" types for third-party libraries. Remove all "any" types from the codebase. (Here, "any" types denotes all the declarations which do not have a type specified, or where the type specified is `any`.)
3. Replace third_party and remaining `<script>` tags with webpack. Reduce the overall time for webpack compilation. Add documentation on all typescript and webpack errors, and solutions on how to fix them.

**Notes**

* This project should simplify the TypeScript and Webpack part of the build process as much as possible for the ordinary developer. Always keep this aim in mind.


### 2.3. Frontend testing of controllers and directives

This project aims at improving the frontend test coverage of controllers and directives to reach 100%.

**Team**: QA Team

**Potential Mentors**: @nithusha21 (primary)

**Consider taking up this project if you...**

* Are interested in testing (since most of the project would involve writing unit tests).
* Have the ability to read through someone else’s code, in order to understand what needs to be tested. (This project will involve reading through a lot of Oppia's source code.)
* Like to handle technical challenges! It is very likely that you'll run into problems while trying to test the code as is, and you will almost certainly need to research and come up with solutions to test certain constructs.

**Suggested Milestones**

1. Develop a pattern for testing controllers and directives and implement it for about 20% of the files.
2. Fully cover 60% of the controllers and directives.
3. Fully cover 100% of the controllers and directives.

**Notes**
1. Currently we don't have a way to test controllers and directives in the codebase. The applicant would need to research suggested methods and pick one such strategy to implement the tests in Oppia (this should be a part of the proposal). A proof of concept pull request would be great. 
2. Please checkout our wiki page for best practices while writing frontend tests. It outlines standard guidelines which need to be followed while writing frontend tests. 
3. The project would involve applying the testing template to a large number of controllers and directives. The proposals must contain a concrete plan (preferably as a table) which outlines which file will be worked out at what time. 

### 2.4. Ensure that Oppia is Fully Accessible

Ensure that the entire Oppia website is fully accessible to screen readers (i.e., all pages should score 100% on the Chrome browser’s inbuilt Accessibility audit tool), and that automated tests are put in place to ensure this is the case going forward.

**Team**: Learner and Creator Experience

**Potential Mentors**: @kevintab95 (primary), @aks681

**Consider taking up this project if you...**

* Enjoy debugging and tracing JavaScript code to find out how something works.
* Have good technical design skills.

**Suggested Milestones**

* Milestone 1: 
  * The following pages should score 100% in both Chrome and manual accessibility audits:
    * Learner dashboard
    * Creator dashboard
    * Topics and Skills dashboard
    * Classroom page
    * Exploration editor page
  * Ensure that automated tests are put in place (eg. [axe-core](https://github.com/dequelabs/axe-core), [protractor-accessiblity-plugin](https://github.com/angular/protractor-accessibility-plugin/), [lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci/blob/master/docs/getting-started.md)) to ensure that this score is maintained, going forward.
* Milestone 2:
  * The following pages should score 100% in the accessibility audit: 
    * Editor page (stats, history, feedback)
    * Topics editor
    * Skills editor
  * Complete the "Keyboard navigation" feature (eg. [Facebook's shortcuts](https://www.facebook.com/help/156151771119453)):
    * Keyboard shortcuts for navigation across Oppia (eg. moving to a particular section of the same page, navigating to a new page).
    * Must include an easy to access "quick reference".
* Milestone 3: 
  * The following pages should score 100% in the accessibility audit: 
    * Story editor
    * Preferences
    * Profile
    * Library
    * Splash and remaining pages.

**Notes**:
- A good proposal would evaluate how accessible Oppia is currently and describe clearly how it can be improved.
- Evaluate relevant automated tools that can be used and how they can be introduced into the project.
- Explain in detail how the "Keyboard navigation" feature will be introduced.

## Backend Projects

### 3.1. Simplify the Oppia build process

The build process that Oppia uses to prepare the files for reliably serving the site was changed quite a lot in the last few months: we introduced webpack, changed our build scripts from bash to Python, and also upgraded some libraries. Since a lot of these changes affected the build process and sometimes weren’t accounted for, the build process is now clunky and quite hard to understand. 

This project’s aim is to simplify the build process, making it easy for developers to work with it and unifying the multiple entry points that need to build some files (backend tests, e2e tests, frontend tests, local dev server) as much as possible. After the project is complete, all the build-related stuff should be handled exclusively with either Python or webpack.

**Related issues**: 7061, 5676, 6369, 6866, 7601, 6988

**Team**: Speed Team

**Potential Mentors**: @vojtechjelinek (primary)

**Consider taking up this project if you...**

* Want to critically analyze and then propose a new architecture for our build process.
* Enjoy refactoring previously-written code.

**Suggested Milestones**

1. Remove gulp build (#5676). Simplify directory structure (#6369). Replace Java yuicompressor minification of CSS by some npm or webpack alternative.
2. Refactor the production build process to only move and build the files that are actually needed.
3. Tidy up various scripts that developers use so that they’re more self-explaining. Currently, there's usually one big (hundreds of lines) main method that does everything; this should be replaced with multiple smaller methods. Document the updated build process either in a separate document, or together with the code. 

**Notes**

While writing your proposal, please make sure to keep in mind that a key aim of this project is to simplify the Python part of the build process as much as possible for the ordinary developer. Proposals should demonstrate an understanding of the current build process and explain clearly what the eventual build process (after the refactor) should look like. Clarity of thought and expression is important here.

### 3.2. Validate data invariants between storage models

The storage models for Oppia's datastore have audit jobs implemented in core/domain/prod_validation_jobs_one_off.py. Run the audit jobs for all storage models and perform a migration to bring them to a valid state. Add tests for all these migration jobs to ensure that they work correctly. Update the existing models to ensure that they remain in a valid state, and complete all [remaining TODOs](https://github.com/oppia/oppia/issues/8510) in the storage models.

**Team**: Server Team

**Potential Mentors**: @ankita240796 (primary), @bansalnitish

**Consider taking up this project if you...**

* Enjoy debugging and fixing validation issues.
* Enjoy analyzing errors and finding their root cause, as well as fixing the pipeline by eliminating the sources of error.

**Suggested Milestones**

1. Select half of the storage models in the codebase. Run the validation jobs for them, diagnose the errors, find ways to fix them, and write a migration job to bring all the models to a valid state (as well as make code modifications to ensure that they continue to be in a valid state henceforth).
2. Do the same thing as in Milestone 1 for the rest of the model classes in the codebase.
3. Complete all remaining TODOs defined in core/storage/. See [this issue](https://github.com/oppia/oppia/issues/8510) for details.

**Notes**

This project follows the following pipeline for a model. This is explained with an example for [ExplorationModel](https://github.com/oppia/oppia/blob/develop/core/storage/exploration/gae_models.py#L43):
* Understand our [release schedule](https://github.com/oppia/oppia/wiki/Release-Schedule) and the way to [make a request to run a job](https://github.com/oppia/oppia/wiki/Running-jobs-in-production).
* Run the [validation job for ExplorationModel](https://github.com/oppia/oppia/blob/develop/core/domain/prod_validation_jobs_one_off.py#L5199) on a backup prod server (you can ask an admin to help you with this).
* If the job fails, collect all the cases which are produced as job output, and analyze the root cause for these invalid cases. Write a migration job to fix these issues and run it on the backup prod server. Also, fix the code to ensure that such cases do not occur in future. Repeat this step until the validation job passes.

We recommend that you try to run a complete pipeline for at least one model before GSoC, and include, in your proposal, the details on how the pipeline was implemented and run.


### 3.3. Fix the linter and implement all lint checks

The Oppia development workflow uses lint checks to help detect style errors before they reach the review phase. This project aims to implement the remaining lint checks in the codebase and make the linting process more robust by adding tests (since we've had some cases in the past where the linter happily let everything through, and this wasn't detected until several months later!)

**Team**: Development Workflow

**Potential Mentors**: @bansalnitish (primary), @ankita240796

**Consider taking up this project if you...**

* Enjoy debugging and fixing issues
* Enjoy refactoring a process and increasing its efficiency
* Have a good sense for how the linting process works for different programming languages

**Suggested Milestones**

1. Refactor the linter to make it more robust, and implement tests for it. Specifically:
- Refactor it to split it up into two (if this makes sense).
- Make the lint output cleaner and less verbose.
- Handle errors correctly.
- Make the code simpler.
- Make sure that verbose mode does the right thing.

2+3. Writing new lint checks. See the master list: [#8423](https://github.com/oppia/oppia/issues/8423)

**Notes**

- The proposal should include a detailed plan in the format of a table which mentions which new lint checks will be added along with the timeline. It should include code samples for implementing at least 2 new checks (if you like, these can be done by linking to PRs that you have previously submitted to the codebase).
- Milestones 2 and 3 should be separately defined by the student in their proposal.
- The proposal should also include implementation details for the refactor process, as well as a clear description of the "end state" and an explanation of how this refactoring will improve the linter. 
- Mentors will examine proposals for this project to see whether the applicant has a good understanding of the existing linting process, as well as organizational clarity (i.e. do they have a good understanding of the "big picture" and a clear vision for how these and future lint checks should be implemented so as to fit into a standard organizational structure).


### 3.4. Make Oppiabot more useful

This project aims to add more functionality to [Oppiabot](https://github.com/oppia/oppiabot) to make the overall developer workflow smoother. The doc with the required functionality is [here](https://docs.google.com/spreadsheets/d/1hFSfl6eQs14m-eLPDCTfwWAZazmFUyTbHwDox15qoW8/edit?usp=sharing).

**Team**: Development workflow

**Potential Mentors**: @ankita240796 (primary), @bansalnitish

**Consider taking up this project if you...**

* Enjoy automating stuff
* Enjoy adding new features to an existing framework
* Have a good understanding of GitHub APIs

**Suggested Milestones**

All the rows in the doc mentioned in the project description above should be completed by the end of the 3 GSoC milestones. It is up to the student how to split this work between the 3 milestones, though we recommend grouping related functionality into the same milestone.

**Notes**

We recommend implementing at least two of the rows mentioned in the [functionalities doc](https://docs.google.com/spreadsheets/d/1hFSfl6eQs14m-eLPDCTfwWAZazmFUyTbHwDox15qoW8/edit?usp=sharing) and explaining your implementation in the proposal. The proposal should also include details of how you would implement the remaining functionality, along with mocks to illustrate what Oppiabot does in the various situations that occur.
 
Use the following [technical design template](https://docs.google.com/document/d/1DdQVdTkGShIbqdz2TTQ9UAKJSoeJ7ut_9jnKFvXnUdc/edit?usp=sharing) for describing technical design of each task mentioned in the [functionalities doc](https://docs.google.com/spreadsheets/d/1hFSfl6eQs14m-eLPDCTfwWAZazmFUyTbHwDox15qoW8/edit?usp=sharing).


## Android Projects

### 4.1. Support Tablet Interfaces

Currently, the Oppia Android app is designed for Android Phones only. This design can be scaled to Android Tablets to increase the application user domain. The project also aims to add screendiff/screenshot testing to validate the UI designs so that no regressions occur.

**Team**: Android

**Potential Mentors**: @rt4914 (primary), @BenHenning, @vinitamurthi

**Consider taking up this project if you...**

* Enjoy working on the user interface of the Android application (Kotlin/Java & XML).
* Can design new screens based on existing screens in the application.
* Are able to use design software (such as Adobe XD) to design mocks.
* Have experience with writing UI-based test cases.

**Suggested Milestones**

1. Introduce screen-diff/screenshot testing to the application, and write test cases to cover the current (mobile phone) UI. This framework should also be used in subsequent milestones to validate the tablet UI and ensure that no regressions occur.
2. Create designs for all tablet screens. Implement high-fidelity code for tablet UI in the HomeFragment, Navigation Drawer and TopicTabs screens.
3. Implement high-fidelity code for tablet UI in all remaining screens (ExplorationPlayer, QuestionPlayer, Settings, Help, Feedback, Profile, Revision and any other screens present in the application).

**Notes**
- Your proposal should include the approach for screenshot testing and how the tablet layout will be introduced in the current codebase. Also, add designs/mocks for at least 3 screens from any of the following: HomeFragment, Navigation Drawer, TopicTabs, ExplorationPlayer, QuestionPlayer, Revision.
- It is fine to switch around the tasks in milestones 2 and 3. The above is just a rough breakdown of work items based on the assumption that the more important ones should be done first.

### 4.2. Analytics Support

Analytics support needs to be built in the Android app so that it is possible to reliably send usage data to a central location while ensuring that no sensitive information leaves the phone. The aim of this project is to:
- Collect & upload crash scenarios
- Collect & upload app health metrics (e.g. memory, CPU usage, etc.)
- Collect & upload key usage events (e.g. activities & dialogs being opened, button clicks, etc.), and ensure these can be tested
- Ensure logs can be uploaded offline, potentially months later for users who have infrequent internet access

**Team**: Android

**Potential Mentors**: @vinitamurthi (primary), @rt4914, @BenHenning

**Consider taking up this project if you...**

* Are interested in using Firebase in an Android app.
* Are interested in working on system usage tracking and analytics.

**Suggested Milestones**

1. Integrate with Firebase to track crashes (all crashes in the app, including ANRs), and app health metrics:
   * App battery usage (distinguishing between foreground/background app usage isn't necessary)
   * App memory usage (this doesn't need to be broken down by memory type; total_pss is sufficient)
   * App CPU usage (this doesn't need to be broken down by threads)
   * App network/bandwidth usage (aggregated data is sufficient; this doesn't need to be broken down by request)
   * Disk usage (doesn't need to be broken down by cache/app storage; total storage is fine. Should include APK install size, if possible)
   * Other performance metrics are optional and should only be considered if they're trivial to implement, otherwise they can be implemented by the team later
2. Analytics tracking with Firebase for usage events like certain activities opening, dialogs opening/closing, key buttons being pressed, expensive operations starting/finishing, and errors being detected. The dimensions for this data in Firebase should have parity with the existing dimensions we track with Google Analytics for Oppia Web (i.e. geography, device information, and language of the user). This milestone includes introducing testing infrastructure to verify that such events are logged (see the notes section below). Your project should outline a list of these events. Consider analyzing the following in the codebase in order to build this list:
   * Each screen in the app (including both activities & dialogs)
   * Each button in the app
   * Cases when the UI requests to load data and when that data loads/fails
   * Other failure cases in service code (e.g. domain controllers)
3. The Oppia Android app is being designed to support users who may go months without internet connectivity. For this reason, an additional solution needs to be built to ensure all of the stats from (1) and (2) can be uploaded later after the user reconnects to the internet. It's not expected that Firebase can solve this out of the box, and that additional work will be needed. The following should additionally be considered when outlining the work for this milestone:
   * How should we retain performance, crash, and usage statistics for potentially months after they initially occurred & upload them later?
   * How should we ensure the timestamps on submitted data stays correct?
   * How should we handle limited space on devices? We probably can't retain stats in perpetuity, and therefore need to clean up old stats
   * How do we ensure data is correctly associated with a specific user? Locally, the user's app profile ID can be used for this purpose. Stats shouldn't be associated with a specific user when uploaded, only with generic information about their device, geography, etc. so that these stats can be aggregated and analyzed later.

**Notes:**
- Your proposal should include how Firebase will be introduced in the application.
- Your proposal should include how the team can access collected stats to create graphs to monitor app health over time.
- You should also focus on mentioning the approach for saving the stats/analytics/logs offline and uploading these analytics once the user is online (keep in mind that users may go weeks or months without internet connectivity).
- Your project should consider device constraints (such as lack of consistent internet connectivity, internet connectivity failures when uploading stats, short bursts of available time to upload stats due to the app being frequently killed by the system, battery considerations (e.g. no wakelocks), and storage consumption).
- Please consider how each of the stats measurements will be associated with other measurements from the same user/device/play session. App health statistics shouldn't be associated with a user, but they do need to be tied to country/locale/device so that we can perform aggregated analyses on these stats.
- Milestone 2 includes introducing test infrastructure so that we can verify that specific usage events are logged at the correct time in automated tests. To keep this simple, we suggest describing in your proposal a class that provides a way to verify that a specific usage event was logged, was not logged, and logged N times. You should describe how this will be hooked up. No additional testing infrastructure work is needed beyond this.

### 4.3. Additional interaction types

Oppia Android currently includes a subset of the interactions (i.e., question types) from the web app. Some additional interactions can be implemented in the Android app, since they are likely to be useful for the mathematics lessons that will be released on it. These interactions include:

* Image Region Selection
* Ratio Input
* Drag and Drop Sort

**Team**: Android

**Potential Mentors**: @rt4914 (primary), @benhenning, @vinitamurthi

**Consider taking up this project if you...**

* Enjoy debugging and tracing through the Oppia web/backend codebase (which is written using Python and Angular).
* Have good analytical and technical design skills
* Are interested in introducing both UI and service functionality in the Android app.

**Suggested Milestones**

1. Add an interaction for Image Region Selection.
2. Add an interaction for Ratio input. This includes changing Oppia's web backend, too.
3. Add an interaction for Drag and Drop Sort.

**Notes:**
- Your proposal should focus on the best approach for introducing these interactions in such a way that they can be used anywhere throughout the application easily.
- Going through the Oppia web codebase and knowing how the interaction has been implemented on the web can help you write a better approach for the Android app. Note that there are already quite a few examples of existing interactions in the Web codebase, and some documentation on the wiki for how to create new ones.
- We're specifically looking for how the interactions will be developed in both codebases (note that some of these are already implemented in Oppia's backend/web codebase).
- Introducing interactions also includes introducing support for classifying answers for each, which in turn may require additional Oppia Android/web work (see how other rule classifiers are implemented in both of these codebases). Proposals should demonstrate understanding of how interactions are structured, rendered, represented in schemas, and how they interact with the rest of the Oppia system, especially answer classification. A good understanding of this is key to coming up with a feasible plan for implementing new interactions, and porting over existing ones.


# Other useful information

## Dates and Deadlines

Noteworthy dates for 2020:
* **Jan 15 - Feb 6**: Mentoring organizations apply
* **Feb 21**: Mentoring organizations are announced
* **Mar 16 - Mar 31**: Student application period
* **Apr 27**: Accepted students are announced
* **Apr 27 - May 18**: Community bonding period
* **May 18 - Aug 10**: Students enjoy the summer by contributing code to their projects
* **Aug 25**: GSoC officially ends

## List of Mentors

* Akshay (@aks681)
* Ankita (@ankita240796)
* Ben (@BenHenning)
* Kevin Thomas (@kevintab95)
* Nithesh (@nithusha21)
* Nitish (@bansalnitish)
* Prasanna (@prasanna08)
* Rajat (@rt4914)
* Sagang (@sagangwee)
* Sandeep (@DubeySandeep)
* Sean (@seanlip)
* Vinita (@vinitamurthi)
* Vojta (@vojtechjelinek)
* Zaman (@mzaman07)

## Communication

**Chat**

Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](
https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any questions related to getting started. For project-specific questions, please direct your queries to the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).

**Email**

If you have questions pertaining to "how-to-get-started", please ask them on [Gitter](
https://gitter.im/oppia/oppia-chat), or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you. Also, please make sure to read our ["getting started" wiki page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) before sending an email, since the answer to your question might already be contained there!

To discuss your project ideas, or share your proposal for feedback from the community, please email the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com). You can also use this list for specific questions about GSoC.