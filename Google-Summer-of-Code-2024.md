**Important**: _We are making some changes to how we run GSoC for 2024. Please read this page carefully, since some things may have changed from previous years._

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

Oppia is planning to participate in [Google Summer of Code 2024](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers an opportunity to discover and work with open source organizations to post-secondary students and other non-experienced contributors. The contributions are supported by a stipend. Contributors work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

In order to receive updates about GSoC at Oppia, please subscribe to the [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce) mailing list.

This year, Oppia will follow the standard GSoC timeline: projects will have 6 weeks for each milestone, with a product demo and internal evaluation after 5 weeks. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below for more details.

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions [here](https://github.com/oppia/oppia/wiki).


## Contributors

GSoC is an excellent opportunity for new contributors to get paid to work on an open source project. If you're interested in applying as a contributor, you should definitely read the following resources:

-   [Google Summer of Code contributor guide](https://google.github.io/gsocguides/student/)
-   [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
-   [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)


## Getting started

Welcome! If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. Make sure to set your preferences correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is about:
    - Read the [user documentation](http://oppia.github.io/#/) to become familiar with important concepts like explorations and interactions.
    - Play some lessons on [Oppia.org](https://www.oppia.org/learn/math), which hosts a live instance of Oppia.

3. To get started with development, read and follow the instructions in the contributors' guide carefully ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Oppia Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)).

4. Do one or more starter projects to become familiar with the contribution process. This will help us get an idea of what it's like to work with you. It will also help you get a better understanding of the codebase and our development process, which may help with writing a good project proposal. Once you've merged at least 2 pull requests, you will get an invitation to become a collaborator to the Oppia repository and be officially onboarded! **This step is a prerequisite to applying for GSoC.**

   - **Note!** You must be onboarded to the repository to which you will contribute during GSoC. For example, to work on an Oppia Web GSoC project, you need to be onboarded to the oppia/oppia repository, which means that your 2 pull requests need to be to oppia/oppia.

   - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to read the [["getting started" guide|Contributing-code-to-Oppia]] and [[PR instructions|Make-a-pull-request]] carefully, follow the [tips for success](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#tips-for-success), manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [[style rules|Coding-style-guide]], and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Select one or more [GSoC project ideas](#oppias-project-ideas-list) that you're most interested in, and write your project proposal! You can get feedback from project mentors when you've completed a sufficient draft -- see the instructions in the [GSoC proposal template](#gsoc-proposal-template) section for details.

   We require that all general discussion about GSoC projects take place in open channels. If you have questions about a project, you can ask in [GitHub Discussions](https://github.com/oppia/oppia/discussions/categories/gsoc-2024-q-a). Please be specific when asking questions, since this makes it easier for us to help you.

   - **Pro-tip!** During the application period, your first goal should be to figure out how to become an effective contributor. Start developing your project proposal only once you have experience getting some PRs merged. This will give you a much better idea of what you want to work on, and how much you can accomplish.

   Good luck!


## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: For Oppia Web, Angular 2+, Python 3.8, Google App Engine and Apache Beam are useful and recommended for most Oppia work; in addition, UI design skills are helpful for frontend user-facing work, and experience with Docker and GitHub Actions is useful for developer workflow projects. Also, it is important to be able to write tests for the code you submit (using Karma, Webdriverio and unittest). Please see the individual project ideas to determine which skills are recommended for the project in question. Note that, although GSoC is aimed at beginner contributors to open source and at students, "beginner to open source" is **not** the same as "beginner to coding" -- the projects assume that you have proficiency with coding. For Oppia Web, you might find this [[page of learning resources|Learning-Resources]] helpful, as well as other pages on our [wiki](https://github.com/oppia/oppia/wiki) that provide guidance on Apache Beam, testing frameworks, etc.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other contributors, successfully contributing, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: Probably not. We have not had good experiences offering flexibility in previous years, so this year, Oppia will strictly adhere to the standard GSoC timeline. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below, and avoid taking up major commitments alongside GSoC; you are unlikely to be able to balance both.

**Q: Which projects are most important for Oppia?**

A: All the projects we've listed in the [Ideas List](#oppias-project-ideas-list) are important, and we'd be very happy to see good progress made on any of them! Projects are treated as equally important during selection; note that the relative importance of a project to Oppia is not part of the [selection criteria](#selection-criteria). We strongly encourage you to pick a project that you'd enjoy doing over the summer!

**Q: Can I submit more than one proposal to Oppia?**

A: Yes, you can. However, we strongly recommend picking one project and writing a solid proposal for it. Splitting attention across multiple projects might not be a great idea. (That said, GSoC is offering full-length and half-length projects, so one exception might be if you're interested in doing either the 'full version' or the 'half version' of a project idea that can support both modes. In such a case, you would be welcome to submit both the 'full version' and the 'half version' as separate applications, but, before doing so, please make sure that you'd be happy with either outcome if you are selected.)

**Q: How early should I start working on the proposal?**

A: We recommend that you first figure out how to become an effective contributor and get onboarded to the project by getting some PRs merged. Then, start developing your project proposal as early as possible after accepted mentoring organizations are announced on 21 Feb. This will give you time to get feedback from mentors and improve the proposal before submission. Make sure to follow all instructions in the [proposal template](https://docs.google.com/document/d/1yYefLkT7dJJa86MyrdWpbZtzeaWAKCi1eXZZDGUrasM/edit) (especially around sharing and access) to reduce delays in reviewing your proposal.

**Q: I only discovered Oppia recently. Does this mean that, during selection, my application would automatically be ranked lower than those by other applicants who have a longer tenure with Oppia?**

A: Definitely not! Here are the [selection criteria](#selection-criteria) we use when selecting contributors for GSoC. Note that tenure is explicitly not part of these criteria.

**Q: What are the minimum number of PRs that one should have?**

A: You should have at least 2 PRs merged, but they don't need to be large. Beyond that, remember that quality is more important than quantity. It is better to submit a non-trivial PR that tackles an important issue rather than a one-line wording change. Start with starter issues, then consider focusing on issues labelled "high priority" and priority" from the team that is offering the project you are interested in. You can see a list of these issues on the respective teams' project boards: [LaCE](https://github.com/orgs/oppia/projects/3/views/8), [Dev Workflow](https://github.com/orgs/oppia/projects/8/views/11), [Contributor Dashboard](https://github.com/orgs/oppia/projects/18/views/4), [Android CLaM](https://github.com/orgs/oppia/projects/4/views/3), [Android Dev Workflow](https://github.com/orgs/oppia/projects/10/views/1).

**Q: What is the total number of contributors that will be accepted?**

A: As many as we think will succeed, though the Google GSoC admins may impose limits based on how they decide to distribute contributor slots among the different open-source organizations.

**Q: I do not have any experience in skill XYZ. Is some certification required?**

A: No, we do not require any formal certification of particular skills. Instead, we will assess your application based on your proposal and the skills that you have demonstrated in your PRs and other interactions with the community. That said, if you are missing a skill, we recommend trying to learn it. Consider working on issues that give you a chance to develop that skill, refer to our wiki documentation, and follow tutorials from elsewhere on the Web. In the field of software development, it is common to develop experience and expertise as you take up and complete projects successfully.

**Q: Is it okay if I only focus on the frontend or backend?**

A: This probably depends on the project(s) you wish to apply for. However, note that most projects are full-stack and require ability in both the frontend and backend. We recommend becoming familiar with both of these, since this will open up more opportunities for you, as the projects we work on at Oppia often touch multiple layers of the stack.

**Q: The [Google GSoC FAQ](https://developers.google.com/open-source/gsoc/faq#can_someone_already_participating_in_open_source_be_a_gsoc_contributor) mentions that the program is only for new contributors. I have already contributed to Oppia and I have write access. Can I still participate?**

A: The GSoC program is open to students, as well as beginner contributors to open source. If you do not qualify as a student, see [this FAQ](https://developers.google.com/open-source/gsoc/faq#how_do_i_know_if_i_am_considered_a_beginner_in_open_source_development) on the GSoC website for whether you would be considered a beginner.

**Q: I'd love to contribute to open source, but I'm not sure I have enough time during the summer to do a GSoC project. Can I still help out?**

A: Yes, GSoC is probably not the best choice if you don't have enough time during the summer, since it requires focused commitment. However, you can still start contributing to Oppia by following the instructions in the contributors' guide ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Oppia Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)).

**Q: Can I use content from the project ideas list or PRD in my proposal?**

A: It is fine for proposals to draw from the GSoC idea in the wiki and any linked PRDs. However, please note that if you copy content directly from any source (even if it is an Oppia doc), **you must cite and link to the original source**. Also, remember from our [selection criteria](#selection-criteria) that when we review proposals, one of the things we look for is evidence that the applicant understands the project and existing codebase well. Strong proposals will therefore contain details that are original (e.g. that are not copied from the PRD).


## Dates and Deadlines

Noteworthy dates for 2024 (see also the [Official GSoC Timeline](https://developers.google.com/open-source/gsoc/timeline):

- **Jan 22 - Feb 6**: Mentoring organizations apply
- **Feb 21**: Mentoring organizations are announced
- **Mar 18 - Apr 2**: GSoC contributor application period
- **May 1**: Accepted GSoC contributors are announced
- **May 1 - May 26**: Community bonding ("greenlight") period
- **May 27 - Jul 8**: Milestone 1 work period for GSoC contributors
  - **Jun 28**: Milestone 1 work due for internal evaluation
  - **Jul 1 - Jul 8**: Buffer time for Milestone 1 revisions
  - **Jul 8 - Jul 12**: Official GSoC midpoint evaluation
- **Jul 12 - Aug 19**: Milestone 2 work period for GSoC contributors
  - **Aug 12**: Milestone 2 work due for internal evaluation
  - **Aug 15 - Aug 23**: Buffer time for Phase 2 revisions
  - **Aug 19 - Aug 26**: Official GSoC mentor evaluation due
- **Sep 3**: GSoC period at Oppia officially ends

**Note!** For Oppia's participation in GSoC 2024, the coding period dates are strict, and we will not be offering extensions. Please ensure that you have sufficient time during the summer to work on your projects.

## Types of work related to Oppia projects

The Oppia team is committed to making GSoC an enriching educational experience for contributors. In general, our goal for GSoC is for contributors to have a really meaningful experience, and to do something worthwhile over the summer that they can look back on with pride.

In order to ensure a well-rounded engineering experience, GSoC contributors will have the opportunity to do some or all of the following, depending on their project:

- Write design documents for technical projects
- Read and understand parts of the codebase related to their project
- Receive code reviews for all code they write for their project
- Write automated tests for their projects
- Meet regularly with other contributors on their Oppia development team (LaCE, Contributor Dashboard, Dev Workflow, Android)
- Meet 1:1 with their mentors regularly to get developmental feedback
- Give presentations and demos of their projects
- Participate in release testing and documentation initiatives

We've also asked our previous GSoC contributors what specific things they learned during their GSoC projects. Here are their collated answers:

- Technical ability and domain knowledge
  - Writing clean code, while keeping in mind that the code needs to run in production.
  - Building an entirely new feature in a scalable way.
  - Writing better automated tests.
  - The importance of testing and also following a clean architecture.
  - I feel more confident on working with Angular.
  - Apache Beam and working with GAE models.
  - I learned lots of things about typescript and webpack.
  - I can now make better design decisions, UI decisions, and technical decisions, and my understanding of overall full-stack development has increased.
- Technical leadership skills
  - How to manage my time well, and how to achieve deadlines.
  - How to properly plan a project before implementing it.
  - How to give, respond to and understand reviews.
  - How to effectively convey ideas.
  - How to write a good project proposal.
- Communication and personal development
  - How to seek help when needed and overcome challenges.
  - How to reach out to people, work with them, and help solve each other's problems.
  - How to get myself unblocked.
  - Putting forward my thoughts more systematically so that others can understand me well.
  - How to work with a large community which is spread over different time zones.
  - I feel more confident while joining online meetings.
  - I have become a better developer, not only in term of technical skills but in thinking of actual application of the built product and the edge case scenarios that the user might face.

Contributors have also told us why they continue to stay engaged with the project after GSoC ends:

- Community
  - I had a great experience with Oppia and would like to continue contributing to the project. I'd like to help newer contributors too, (for example by reviewing their code when I get the chance).
  - The organisation is active and has a strong community bond.
  - It is really an awesome experience working with some amazing folks from all around the world at Oppia.
  - The kind of support the complete community provides is extraordinary.
- Giving back
  - The main reason to stay connected is the purpose the community serves. Providing education to those who do not have access to it helps me give back to the society.
  - It makes me very happy that I'm a part of an organization which provides free education and I think the education is the biggest blessing we can give to one to make them stand on their feet.
  - I would love to be part of this org by knowing that maybe not much but yes I'm trying to make an impact and my contribution in the educational field. I really want to do this because where I come from there is not much of education.

- Growth / learning:
  - I like working in Oppia since it not only helps me improve my coding skills but also helps me grow as an individual.
  - Working with Oppia has really helped me grow as a developer and I would really like to stick around to gain even more experience of real world software development.
  - I feel my exponential growth while contributing in Oppia and got to learn many new things while getting help from mentors and other Oppia team members.
  - The kind of work that Oppia does is really inspiring and there are a lot of opportunities to improve your skills be it be technical skills or leadership skills and most of all the people at Oppia are really fun to work with :)


## GSoC Proposal Template

When submitting a proposal, please use the provided GSoC proposal template. We will only consider proposals submitted using this template. Note that, this year, there is a length limit: the proposal's technical section should fall within 8-20 pages at "Arial 11" font size.

**Note:** although some of the previous years' proposals are a bit on the long side, there's **no** formal length requirement for your proposal. The quality of what you write is much more important than the amount of text you write, and we encourage you to write shorter proposals that still convey the main aim of the project.



(**NOTE**: The link to the 2024 template will be posted soon. **It will differ from the 2023 template.** We will post instructions together with the template.)

**Some important notes:**

1. When the necessary criteria for requesting a review are met, share your proposal to gsoc-2024-mentors@oppia.org and provide them with commenting permissions. Use only this channel for proposal reviews; **do not** send proposals directly to individual GSoC mentors. All proposal-related communication should happen through the gsoc-2024-mentors@oppia.org mailing list or directly through comments in the proposal doc.

2. Your final proposal should be self-contained. In particular, to be fair to all applicants, key components of the proposal should not be editable after the deadline. Don't assume that reviewers will follow external links.

3. Your proposal must be **original** (see section 2.4 of the [Contributor Participation Agreement](https://summerofcode.withgoogle.com/terms/contributor)). During the selection process, proposals that are found to have passed off others' work as their own will automatically be disqualified. If you include any text in your proposal that is copied from the Internet or other sources, you **must** provide a link or reference back to the source, with appropriate credit. Note that you must attribute sources even if you paraphrase (i.e. re-write their content in your own words). In cases of doubt, we would encourage you to err on the side of citing your sources (since not doing so may be construed as plagiarism).


### Tips for writing a good project plan

Here's some advice about proposals and milestone timeline planning that we collated from previous contributors and mentors:

- Choose a project you're interested in! If you have a strong interest in your project, this might make it easier for you to pick up the necessary skills and tackle unforeseen difficulties that may arise during GSoC.
- Familiarize yourself with the technologies and the relevant part of the codebase for your project, especially if you haven't touched it before. It's important to think about how to integrate your project with the current Oppia structure — don't design in a vacuum.
- Define milestones with enough detail to get a proper ETA for each milestone (so, don't just say "write e2e tests"). Otherwise, you risk significantly underestimating the timeline.
- Clear written communication and presentation is crucial in preparing your proposal. The proposal should show that you have a good understanding of the codebase and the final goal of the project. For example, in a user-facing proposal, don't just make a list of files that need to be changed; you should also show detailed mocks and user flow diagrams that demonstrate a clear understanding of the requirements.
- Limit proposal length. A lengthy proposal is not necessarily better. In fact, adding large amounts of unnecessary detail can sometimes obscure the main points you are trying to get across.
- Pick a project idea that is within your limits to tackle, and make sure that what you're proposing is within your capabilities.

### What should applicants expect from mentors in a proposal review?

- Please write your proposal on the assumption that you "own" your chosen project. From your perspective, the submitted proposal should be proofread and in as good a condition as possible before you ask for a review. Make sure that you have a sufficiently good understanding of the codebase/project so that you can find and fix flaws in the design; reviewers will give you feedback but not do this for you. Note that your proposal doesn't need to be flawless — we expect that you might make mistakes, and reviewers will be happy to guide you on how to improve. Instead, by "as good a condition as possible", we mean that your proposal should demonstrate:
  - Your ownership of the project
  - The research you have put into writing it
  - Your analytical skills
  - Your independence in making complex decisions
- Make sure to present solutions and ask for feedback, rather than just asking for solutions. The proposal template contains a "key decisions" section which you can use to present the various options you came up with, analyze their advantages & disadvantages using a comparison table, and explain your proposed choice and the reasoning behind it. Note that this doesn't mean that you must always have multiple ideas to solve a problem, but you should instead always explain how you reached a solution, and why is it the best one from the end-user's perspective. Think about how you might gather data to validate your conclusions (e.g. by finding support in the peer-reviewed literature, or by showing your ideas to potential users in the target audience and asking for feedback, etc.).
- Reviewers' suggestions are _suggestions_, not mandates. We do not expect you to always agree with your reviewers! This means that, as the proposal owner, you are always welcome to decide whether to accept/reject such suggestions. In either case, when accepting/rejecting a suggestion provided by a reviewer, try to explain your reasoning and the research that led to your decision.
- If you're confused about something, try to identify the point of confusion and ask have specific discussions about it, rather than simply agreeing to whatever is proposed. Don't rely on an "appeal to authority" (e.g. "I am doing it this way because reviewer XXX said so") — the rational analysis and thought that underlie the decision are what's important, so make sure that you understand and clearly communicate the reasons behind the decisions you make.
- Note that the process Oppia uses to select GSoC contributors typically includes multiple independent reviewers, most of whom will not have looked at the earlier versions of your submitted proposal. Your initial proposal reviewers may or may not be involved in the final selection process, and it is **not** a requirement that you need to implement all your reviewer's suggestions/requests in order to be selected. Instead, please consider your reviewer as a friendly advisor who is available to help you and provide guidance, rather than the main future evaluator of your proposal.

## Selection Criteria

In order to select contributors for GSoC, we will mainly be looking at three things:

- The quality of the submitted proposal
- The quality of the applicant's PRs (in order to assess their ability to code, debug, break down complex tasks, etc.). In particular, we will be assessing whether the applicant has the necessary technical and communication skills to succeed in their chosen GSoC project.
- Our prior experience working with the contributor (do they keep commitments, communicate well, demonstrate independence/initiative/responsiveness, help others, etc.)

We believe that strong performance in these dimensions is likely to correlate well with the contributor having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the GSoC program.

For the proposal, we generally look for a clear indication that the contributor has a good, clear understanding of the project, and has broken it down sufficiently well, in a way that makes it very likely to succeed. Some indicators that could help with this include:

- Clear, unambiguous communication. (This is important; your proposal will be read by many mentors!)
- A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating a simple, intuitive experience for end users.
- A proposed solution approach which is sufficiently concrete and which demonstrates that the applicant has a good understanding of both the scope of the problem and the existing codebase.
- A description, if applicable, of how the applicant plans to mitigate risks that could potentially derail the project.
- A concrete, specific description of each milestone, together with a breakdown of the necessary work.


## Communication

If you have questions pertaining to "how to get started with Oppia" or any other queries regarding GSoC at Oppia, please ask them on **GitHub Discussions** ([Web](https://github.com/oppia/oppia/discussions)). Please be specific when asking questions; this makes it easier for us to help you. Also, please make sure to read the relevant "getting started" wiki page ([Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)) first, since the answer to your question might already exist there!

To receive important announcements and updates about GSoC at Oppia, please subscribe to the **[Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce)** mailing list.

## Oppia's Project Ideas List

_**Note:** If you're coming to this section from an external link, please make sure to scroll up and read this entire wiki page carefully, not just this section. There's a lot of useful information on the rest of the page, including a FAQ and a section describing selection criteria. Thanks!_

The following is a list of Oppia's 2024 GSoC project ideas. You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community beforehand in order to get feedback and guidance to improve the proposal. We'd also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

Please note that the list of project ideas below is not set in stone: more projects may be added later, and some project descriptions may also change a bit, so check back regularly. In addition, the mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted.

### Learner and Creator Experience (LaCE) team

1.1. [Infrastructure and navigation for multiple classrooms](#11-infrastructure-and-navigation-for-multiple-classrooms)

1.2. [Static page redesigns](#12-static-page-redesigns)

1.3. [Clean up the structure for revision cards and worked examples](#13-clean-up-the-structure-for-revision-cards-and-worked-examples)


### Contributor Dashboard team

2.1. [Show AI-powered and cached translation suggestions to translation submitters](#21-show-ai-powered-and-cached-translation-suggestions-to-translation-submitters)

2.2. [Make it possible to update translations for previously-translated content](#22-make-it-possible-to-update-translations-for-previously-translated-content)

### Developer Workflow team

3.1. [Acceptance tests](#31-acceptance-tests)

### Android team

4.1. [Code coverage support and enforcement](#41-code-coverage-support-and-enforcement)

4.2. [Multiple classrooms support](#42-multiple-classrooms-support)

4.3. [Platform parameter developer dashboard and improvements to platform parameter testing support](#43-platform-parameter-developer-dashboard-and-improvements-to-platform-parameter-testing-support)


## Learner and Creator Experience (LaCE) team

### 1.1. Infrastructure and navigation for multiple classrooms

**Project Description:**

Oppia currently has a classroom page for Math lessons, which is featured prominently and accessible via the home page, navigation bar, community library and learner dashboard. We are planning to create more classrooms for other topics.

The aim of this project is to implement the infrastructure to display these classrooms, and make it easy for learners to navigate to them.

**Size of this project:** Medium (\~175 hours)

**Difficulty**: Medium

**Potential mentors:** @Nik-09

**Product Clarifier:** @yupigummy

**Technical Clarifier:** @seanlip

**Required knowledge/skills:**
- Ability to write code in Python with unit tests.
- Ability to write code in TypeScript/Angular with unit tests.
- Ability to write end-to-end or acceptance tests.
- Effective communication using [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs).

**Suggested Milestones:**
- **Milestone 1**: Creators should be able to create new classrooms and view them at the relevant URLs. Specific deliverables:
  - In the topics and skills dashboard, topics can be filtered by classroom, and the default sorting order for topics should be by when they were last updated.
  - The topic editor page should show which classroom a topic is in.
  - Whether a classroom is visible/hidden should be configurable on the classroom admin dashboard.
  - A new "classroom index" page is implemented at www.oppia.org/learn, with e2e tests. The page is gated behind a feature flag. If there is only 1 visible classroom, this page should redirect to /learn/{{classroom-name}}. If there are more visible classrooms, it should show a list of classrooms. If there are no visible classrooms, it should show a standard error message in prod mode, and tell the user that they can create a new classroom at /classroom-admin in dev mode.
  - Implement a generalized per-subject classroom page and update the math classroom to use it, including the routing. The functionality for classrooms should be fully generalized so that there is no direct reference to “/math” in the codebase.

- **Milestone 2**: The new classrooms page should be discoverable and the learner-facing functionality should be completed so that the feature can be launched to users.
  - Update the splash page and navigation bar to point to the new classroom index page if there is more than one classroom. (The existing behaviour of the site should be preserved if there is only one classroom.) Add e2e tests for this.
  - Update the community library and learner dashboard to point to the new classroom pages, and add e2e tests for this.
  - In the topic viewer page, show which classroom the topic is in.
  - Implement the necessary analytics events for classroom usage (see the "Automatically-collected metrics" section of the PRD).
  - Work with the tech lead to add new CUJs and launch the new classrooms page functionality. Remove the feature flag once the launch is successful.

**What we are looking for in proposals:**

Here are some examples of questions to analyze:
- How will you generalize the routing to multiple classrooms? (Ideally, this is handled in the frontend.) Which parts of this solution are already implemented and which parts still need to be done?
- How will you efficiently determine which classroom (if any) a topic is in?
- What backend changes are needed in order to remove any hardcoding of "/math" and generalize it?
- What corner cases are there? Feel free to ask the product team if you need UI decisions, but you should think through and fully enumerate all the 'corner case' questions.

**Technical hints / guidance**

- Note that new classrooms are created using the dashboard at /classroom-admin. You will need curriculum admin permissions, which you can grant at /admin (see the Roles tab).
- Here are [the PRD](https://docs.google.com/document/d/1d_FUVKiHsdB8drn9ofw72mIEHztM2GAF8UhErllVMCw/edit) and [mocks](https://www.figma.com/file/CxEKn4FvaZRAAbvuqDchD1/Oppia-Multiple-Classrooms?type=design&node-id=0%3A1&mode=design&t=a3kGrOeQP0HJm0dh-1) for the project, which you can use as a reference.
- Make sure to include unit and acceptance tests to confirm both 1-classroom and multiple classrooms behaviour. In general, you'll want to test the behaviour for (a) a single /math classroom, (b) a single non-/math classroom, (c) 2+ classrooms.
- All UI updates should work fully on mobile devices and be responsive, accessible and fully internationalized.
- Make sure to handle corner cases correctly. E.g. if the learner has done no topics in the science classroom yet, then don’t show that classroom in the list of classrooms-with-topics-in-progress in the learner dashboard.


### 1.2. Static page redesigns

**Project Description:**

User research has indicated that the informational pages on the Oppia.org website could be improved, because users cannot find the information that they need from them. The aim of this project is to make these improvements.

Please refer to [this PRD](https://docs.google.com/document/d/1enceUlqh7KpaE5i_rdKE-0mZh899tYNf524vFiUYZvI/edit) (still being worked on) for the full details of this project.

**Not in scope:**
- Writing translations for the pages into other languages. You should only fill in en.json and qqq.json for any learner-facing strings, as described in our [internationalization wiki page](https://github.com/oppia/oppia/wiki/How-to-develop-for-i18n#adding-new-translation-keys).

**Size of this project:** Small (\~90 hours)

**Difficulty**: Easy

**Potential mentors:** TBD

**Product Clarifier:** @tanzhirong (tentative)

**Technical Clarifier:** TBD

**Required knowledge/skills:**
- Ability to write frontend PRs in TypeScript/Angular/HTML/CSS with unit tests. These PRs should show attention to detail and excellent judgment for responsive design.
- Ability to write and/or fix flakes in e2e/acceptance tests.
- Ability to make small backend changes in the Python code.
- Effective communication using [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs).

**Suggested Milestones:**
- **Milestone 1**: Update the acceptance tests to cover the "ideal flows" for volunteers, donors, partners, and parents/teachers with acceptance tests (see the "Product Flows and Requirements for Specific User Flows”"section). This might involve modifying some of the existing tests to make the user type more specific.

  Redesign the About page according to the given mocks, and ensure that it is fully-responsive for all device sizes, reaches a Lighthouse score of 100 for accessibility, and fully internationalizable.

  Update and simplify the navbar according to the given mocks.

- **Milestone 2**: Redesign the "Volunteering" and "For Parents/Teachers" pages according to the given mocks, and ensure that they are fully-responsive for all device sizes, reach a Lighthouse score of 100 for accessibility, and fully internationalizable. Add the necessary metrics events to these pages (see the “Automatically-collected metrics” section).

**What we are looking for in proposals:**

- Explain how you will ensure that the implemented/updated pages are (a) fully-responsive for all device sizes, (b) reach a Lighthouse score of 100 for accessibility, and (c) fully internationalizable. If possible, link to PRs that demonstrate that you have a good understanding of these areas.
- List all the events you plan to add to Oppia’s site analytics service, and provide a sample of how you would do this.
- For each element in the mocks (such as the bar graphs, timeline chart, etc.), explain how you would implement it.
- Which common components would you create, and where would those common components be used? (It is a bonus if you are able to also use them in pages outside the ones covered in this project.)
- When auditing the mocks and thinking about implementation, you might find that you need to get clarifications on various aspects of the mocks. Include, in your proposal, a list of questions that you have asked / would ask, how they affect the implementation, and the answers to those questions. You might even consider conducting some lightweight user research using the scripts provided in the PRD, but this is optional.

**Technical hints / guidance**

- Attention to detail is very important for this project – we don't want to have to revisit these pages again for several years after the GSoC project is completed. So, exhibiting good UI judgment is a particularly important skill that is required for this project. (For example, a button isn’t just a coloured rectangle – it has hover effects, it might change its size depending on the screen width, it might need accessibility support, etc.) Keep this in mind when tackling issues on Oppia, or proposing implementation strategies for this project.

- Where possible, try to make common components (like the primary-button component that is used in several static pages; see e.g. [oppia#19676](https://github.com/oppia/oppia/pull/19676)) so that you only need to implement the details once, and can more easily keep things consistent throughout the website. We suggest doing this for any UI element that you would use at least twice, and in some cases it might make sense to do it even if you use the element once (so that the component is better encapsulated)


### 1.3. Clean up the structure for revision cards and worked examples

**Project Description:**

Currently, topics in Oppia contain a list of skills that they teach, and these skills are grouped into “subtopics” (like “Adding Fractions”), each with its own revision card (or “subtopic page”). Subtopic pages were originally implemented as a single rich-text editor (RTE) component, but given their length in practice, this was a mistake since it means that they are too big to be translated easily. Additionally, skill descriptions (“concept cards”) and subtopic pages can include worked examples, but worked examples were incorrectly implemented as a field on the skill model. Experience has shown that worked examples would be better implemented as a rich-text component instead, since this gives more flexibility in where they are placed and allows them to be used in other contexts like the subtopic pages.

The aim of this project is therefore to clean up some of this incorrect modelling and fix the representation of subtopic pages and worked examples, while also ensuring that they are easily translatable.

**Not in scope:**
- Implementing new rich-text components other than "Worked Example".

**Size of this project:** Large (\~350 hours)

**Difficulty**: Hard

**Potential mentors:** @kevintab95

**Product Clarifier:** @seanlip

**Technical Clarifier:** @kevintab95

**Required knowledge/skills:**
- Ability to write code in Python with unit tests.
- Ability to write code in TypeScript/Angular with unit tests.
- Ability to write Beam jobs with tests. (This [wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) explains how to write Apache Beam jobs. You can try some issues from [this list](https://docs.google.com/document/d/1egQNvBXlgRNhSXdscUZlYOTgd48MXO9a5cPW2rVFL0Y/edit) to get experience.)
- Ability to write and/or fix flakes in e2e/acceptance tests.
- Effective communication using [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs).

**Suggested Milestones:**
- **Milestone 1**: Carry out a schema migration to split the subtitled_html field of SubtopicPageContents (also known as "revision cards") into a list of (heading: str, content: RTE) pairs – existing subtopic page content should be migrated to a single-element list, with the only item in that list having a heading that is the revision card’s title, and a body consisting of the existing RTE content.

  Store the written translations for subtopic pages in EntityTranslationsModel instead of within the SubtopicPage object, similar to the migration that was done for the correspondingly-named field in explorations a few years ago. Also, introduce a unique content ID for each translatable field, similar to explorations. (This should be a relatively easy migration because there are no translations for SubtopicPages yet, but you will need to figure out the new structure and fix the "plumbing".)

  Update the editor UI to accommodate the new structure, and the learner UI to use an improved display for the revision cards based on these mocks, with clearly-indicated headings for each of the sections.

- **Milestone 2**: Carry out a schema migration to safely deprecate the `worked_examples` field in the `skill_contents` part of the SkillModel, and remove it from the skill editor UI as well. Implement a new 'Worked Example' RTE component that appears only in the skill description and subtopic page RTEs, and add acceptance tests for its use. Ensure that this component is (in principle) translatable in the contributor dashboard.

**What we are looking for in proposals:**

- Explain how the current structure for exploration translations works, and describe, by analogy, the ideal structure for skill and subtopic card translations. For the subtopic pages, what changes exactly will you make with regards to written translations and content IDs?
- Explain in detail the steps you would take to carry out the structural migrations for subtopic pages and skills. For the former, what will the updated editor UI look like?
- Explain how you would make the new 'worked examples' component appear only in the concept card and revision card RTEs. Additionally, what will the schema of this new RTE component look like, and how will you structure the acceptance tests?
- What is the **full list** of places which use RTE components, and that will need to be updated with details for the worked example component? Explain the approach you took to find these.

**Technical hints / guidance**

- For the worked examples section, see [this PRD](https://docs.google.com/document/d/1QrqTsR1Ew3WfQvj7D83mh0k9HjW6xQ-2dpJGkbe8XqY/edit#heading=h.s68z2sezulra). There is currently no PRD for revision cards, but there are [preliminary mocks](https://www.figma.com/file/wH1RGiZ7KEvLUxeL5R16G6/Oppia-%7C-RTE?type=design&mode=design&t=vEGSCuJcR3gRtZlB-0#681559870) that you can use as a basis.
- See [this wiki page](https://github.com/oppia/oppia/wiki/Rich-Text-Editor-%28RTE%29-Overview) for details on how to implement rich-text components.
- See [this wiki page](https://github.com/oppia/oppia/wiki/Writing-state-migrations) for details on how to write state migrations. Writing migrations for other entities follows a similar process.
- We recommend taking the time to really understand how exploration translations work before you try to figure out a similar structure for subtopic pages. The original TDD for that project is here: [Infrastructure for separate storage of translations](https://docs.google.com/document/d/1ZZ6pVKpmynTlmf1_PV1I5TcccmEXPnmoFAVKXN-u2xM/edit).
- For subtopic page contents, be careful to ensure that each element in the list has its own unique content ID. Do not just base the content ID on the item's index in the list – if you have 3 elements in the list and then remove the middle one, the last element’s content ID should not change. This is why we need a counter to keep track of the "next content ID to assign".
- For "ensure that this component is (in principle) translatable in the contributor dashboard", you can temporarily enable it in exploration RTEs (e.g. in the hints RTE), and then test out the translation workflow. It's important to ensure that the new 'worked example' RTE component has behavioural parity with other RTE components in all places which refer to RTE components, even if it's not being used in the relevant contexts yet – for example, you should update the character-counting logic for hint/solution validation to handle worked-example RTE components as well, in case we decide to make this component available to explorations in the future.


## Contributor Dashboard (CD) team

### 2.1. Show AI-powered and cached translation suggestions to translation submitters

**Project Description:**

This project involves showing auto-generated suggestions in the Contributor Dashboard translation submission modal, so that translation submitters can edit-and-submit those translations rather than needing to generate completely new ones from scratch each time. These suggestions would arise from two sources: (a) previously-accepted 'canonical' translations for the same string, and (b) autogenerated translations from an automated AI-powered translation service.

The project involves implementing a system for caching translations so that each (string, language) pair is associated with both an unreviewed and approved translation. The approved translation should be populated just once, and cached for future use, and the source of the automatic translation should also be stored. The manual translation is only populated once a translation is approved by a human reviewer (possibly after edits). This cache system should then be used to generate auto-suggestions for new strings that match an existing one, when the translation submitter is asked to create a translation for a string that exactly matches one that is already in our database.

Additionally, Oppia already has a partial implementation for [computer-aided translation (CAT)](https://docs.google.com/document/d/1kJd-yLTzB9a2c3Nq7v9pzKfHwKHKGpkWfQ8B0YGf50U/edit#heading=h.24wysknhgyrz) support. This project also involves auditing that implementation and completing it, so that auto-generated translations can be suggested to translation submitters.

**Tracking issues**: [#16164](https://github.com/oppia/oppia/issues/16164), [#19680](https://github.com/oppia/oppia/issues/19680), [#19681](https://github.com/oppia/oppia/issues/19681)

**Not in scope:**
- Configuring the list of languages that are prioritized for translation
- Auto-generation of voiceovers (in any language)
- Enabling translations for concept cards, review cards, or practice questions

**Size of this project:** Large (\~350 hours)

**Difficulty**: Hard

**Potential mentors:** @chris7716, @Aakash-Jakhmola

**Product Clarifier:** @seanlip

**Technical Clarifier:** @chris7716

**Required knowledge/skills:**
- Ability to write code in Python with unit tests.
- Ability to write code in TypeScript/Angular with unit tests.
- Ability to write Beam jobs with tests. (This [wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) explains how to write Apache Beam jobs. You can try some issues from [this list](https://docs.google.com/document/d/1egQNvBXlgRNhSXdscUZlYOTgd48MXO9a5cPW2rVFL0Y/edit) to get experience.)
- Effective communication using [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs).
- Ability to write and/or fix flakes in e2e/acceptance tests.

**Suggested Milestones:**
- **Milestone 1**: The full translation caching system backend is implemented and used for auto-suggesting translations for strings that have been previously accepted. The contributor dashboard UI displays these suggestions to translation submitters and explains why they are being suggested. When a translation is accepted by a reviewer, its 'approved' entry in the datastore model is updated. If availability of translations meets the existing criteria for displaying a translated language in the exploration player, the exploration player UI displays these translations to learners, along with an indicator that the translation has not been reviewed yet (see [these mocks](https://github.com/oppia/design-team/issues/95)).

- **Milestone 2**: The full computer-aided translation (CAT) backend implementation is completed, including functionality that allows the developer team to configure the CAT service provider for each language. Admins can run a Beam job from the admin dashboard to generate auto-translations for any untranslated texts for all curated lessons in Oppia's prioritized languages (they can select 'all explorations' or a particular exploration, and they can select 'all languages' or a particular language). These auto-generated suggestions are then shown in the contributor dashboard UI when they are available, as well as the exploration player, together with the relevant context as described in Milestone 1.

**What we are looking for in proposals:**

- For the cache structure, you will probably need to hash strings for quick lookup, and also because the datastore has a [maximum limit for indexable string fields](https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/entity-property-reference#types) (1500 bytes). How will this be handled?
- If the same string can have multiple translations in different contexts, how will that be handled?
- Please provide a clear list of the remaining steps which are  required to complete the CAT project. Bear in mind that getting CAT fully ready includes:
  - Making sure that all rich-text components are handled properly, and fine-tuning the user experience to ensure that all parts of translations (e.g. alt text for images) are easily auditable by submitters before they submit.
  - Ensuring that the system is extensible so that we can specify different service providers for different languages, and each service provider should have a ‘services.py’ file in core/platform/translate. (For this project, it is fine to include the implementation for only one provider, but the framework should be extensible and there should be clear instructions in the wiki for contributors on how to do this.)

**Technical hints / guidance**

- Here is an [information sketch](https://docs.google.com/document/d/1ZZ6pVKpmynTlmf1_PV1I5TcccmEXPnmoFAVKXN-u2xM/edit#bookmark=id.d999h6434xq2) about the translation caching system. You can use it as a starting point for your technical design. Note that there are other reasons to cache beyond the one implemented in this project (e.g. we might have custom logic for auto-translation of strings that are entirely numeric) and your system should be extensible to these.
- We have filed a request for the CD mocks with the design team; you can follow [this design issue](https://github.com/oppia/design-team/issues/128) for updates. For your proposal, focus more on the technical aspects than the mocks.
- A large part (probably around \~80%) of the CAT backend work is already done (see [this doc](https://docs.google.com/document/d/1kJd-yLTzB9a2c3Nq7v9pzKfHwKHKGpkWfQ8B0YGf50U/edit#heading=h.jp6no890gjkv) for details). You might like to look at previous unfinished PRs: [#12604](https://github.com/oppia/oppia/pull/12604/files) / [#14418](https://github.com/oppia/oppia/pull/14418).
- If anything goes wrong with generating the suggestion, just don’t show the suggestion part of the submission modal. (Don’t error noisily in a way that blocks the experience for the translation submitter.)
- You will need to gate the new functionality behind [feature flags](https://github.com/oppia/oppia/wiki/Launching-new-features). The flags that would need to be added are for:
  - `SHOW_TRANSLATION_SUGGESTIONS_IN_CD`, for gating the integration of translation suggestions to the contributor dashboard
  - `SHOW_AUTOGENERATED_TRANSLATIONS_IN_LESSONS` -- for showing autogenerated translations in the exploration player
- This [related PRD](https://docs.google.com/document/d/1TeGQQNLNJWkTgvGQ1xmV6snz8zXnJ23TvuDKtK5_Tok/edit) might be a helpful reference.


### 2.2. Make it possible to update translations for previously-translated content

**Project Description:**

Sometimes, after a piece of content is translated, a small part of the original text is edited. In such cases, we should:

- Ensure that the translation counts in the exploration editor translations tab and contributor dashboard are updated correctly, and that the correct behaviour is locked in by acceptance tests.
- Make it easy for the translator to base their new translation on the original one, but just edit the part of the previous translation that has changed. (Currently, they need to submit a brand-new translation instead.) We can do this by showing the new content to be translated, the existing translation, and a diff between the new content and the previously-translated content.

**Tracking issues**: [#16163](https://github.com/oppia/oppia/issues/16163)

**Not in scope:**
- Translation caching and/or auto-generation
- Translations for concept cards, review cards and practice questions

**Size of this project:** Large (\~350 hours)

**Difficulty**: Hard

**Potential mentors:** @chris7716, @Aakash-Jakhmola

**Product Clarifier:** @seanlip

**Technical Clarifier:** @chris7716

**Required knowledge/skills:**
- Ability to write code in Python with unit tests.
- Ability to write code in TypeScript/Angular with unit tests.
- Ability to write Beam jobs with tests. (This [wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) explains how to write Apache Beam jobs. You can try some issues from [this list](https://docs.google.com/document/d/1egQNvBXlgRNhSXdscUZlYOTgd48MXO9a5cPW2rVFL0Y/edit) to get experience.)
- Effective communication using [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs).
- Ability to write and/or fix flakes in e2e/acceptance tests.
- An understanding of how to query the App Engine datastore directly, e.g. structuring queries to use 1 get-multi operation rather than N get operations.

**Suggested Milestones:**
- **Milestone 1**: Ensure that the translation counts in the exploration editor translations tab and contributor dashboard are updated correctly when translations are marked-as-stale or new translations are updated, and that the strings to re-translate show up in the CD view for submitters; write acceptance tests to cover this behaviour. Verify also that the reviewer sees the current text at the time they are reviewing, and not the text at the time of submission.

  Make the necessary backend changes for storing data about the English content of an exploration at the time the last translation for that content was accepted (note: not the English content at the time the opportunity was created), and populate this information retroactively for lessons in topics using a Beam job.

- **Milestone 2**: Show a diff view in the UI that translators can use to create the translation for the updated content. Hide this diff view behind a feature flag `SHOW_DIFF_VIEW_FOR_RETRANSLATING_UPDATED_CONTENT`.

**What we are looking for in proposals:**

- A clear analysis of how translation counts in the exploration editor translations tab and contributor dashboard are currently generated, with links to lines of code in GitHub.
- A clear description of how the end-to-end system for updating previous translations should work, and the gaps that exist in the current system for doing so.
- A description of your Beam job for regenerating the translation count data, as well as how you would validate its correctness.
- A clear description of how you would retrieve the “version when translation was last accepted” for a particular translatable string of a lesson. This might involve storing the entire string somewhere, or storing just the relevant version of the exploration and using that to retrieve the string as needed. Consider different approaches and evaluate their tradeoffs using a decision table.
- A description of how you would generalize the “diff view” component in the exploration history tab to use for the contributor dashboard as well (or if this isn’t a good idea and, if so, why).

**Technical hints / guidance**

- A request for mocks for the contributor dashboard UI has been filed with the design team; feel free to follow along at [this link](https://github.com/oppia/design-team/issues/128).
- Note that a tricky part of this project involves showing the English content at the time the previous translation was accepted. We recommend first investigating if this information is stored anywhere, or is easily retrievable. If not, you’ll need to create a separate model for it and populate it via a Beam job, and ensure that it is subsequently populated whenever a translation is approved. There is some earlier analysis in [this TDD](https://docs.google.com/document/d/1RIlefl2kmXyqwrcqTruNjJlQ6EWoiKs9DApT52Kahx8/edit) which you can use as a starting point, but you should validate whether that analysis is correct and not follow it blindly.
- You might find this information about [feature flags](https://github.com/oppia/oppia/wiki/Launching-new-features) useful.


## Developer workflow team

### 3.1. Acceptance tests

**Project Description:**

The Oppia development team is enhancing its software quality by implementing Acceptance Testing on the develop branch. These end-to-end tests are crucial for ensuring the application's functionality aligns with user expectations, with the aim of detecting and fixing bugs before release. By automating the tests for every commit, the team ensures that key user journeys remain unbroken, enhancing the reliability and user experience of the software.

A detailed documentation of user journeys and test steps is maintained to guide the testing process. This project requires both writing acceptance tests for all the user stories, as well as fixing any minor UI/UX issues that cause e2e test flakiness.

Note that one other benefit of moving to the acceptance tests is that critical user journeys (CUJs) can be more easily tracked. With a complete suite of acceptance tests, it is easier to audit whether or not a particular CUJ has been included. This makes it easier to add tests for new CUJs introduced in new features while still keeping the tests well-organized. A key goal of this project is therefore to write the acceptance tests in a maintainable way that achieves these aims.

Here is a spreadsheet detailing most of the tests that need to be written:
https://docs.google.com/spreadsheets/d/1O8EHiSAGrG0yoNUBz9E4DIwKNS8Rfsv_ffC4k1WK5jc/edit#gid=1807800085

**Tracking issue**: [#17712](https://github.com/oppia/oppia/issues/17712)

**Not in scope:**
- Building the infrastructure to write and run the acceptance tests. (Though please note that writing the acceptance tests in a maintainable way, e.g. extracting utility functions to enable code reuse or provide relevant functionality for a group of tests, is still in scope.)
- Writing acceptance tests for new features that are first introduced after April 2024.

**Size of this project:** Large (\~350 hours). Alternatively, you may pick either Milestone 1 or Milestone 2 for a medium-sized project.

**Difficulty**: Medium

**Potential mentors:** TBD

**Product Clarifier:** @seanlip

**Technical Clarifier:** @DubeySandeep

**Required knowledge/skills:**
- Ability to write non-flaky End-to-End tests, including appropriate use of WaitFor. (To demonstrate this, we recommend making at least one PR that solves a part of #17712 by covering the CUJs for at least one set of users. This PR should demonstrate the ability to comprehend and articulate acceptance test requirements.)
- Ability to diagnose and resolve issues within E2E tests, particularly flakiness. (To demonstrate this, show one or more [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs) that correctly diagnose the root cause of an e2e flake, and make at least one PR that resolves at least one E2E flakiness issue.)
- Ability to make frontend changes to fix small code issues that are found when writing the acceptance tests. (To demonstrate this, you can show 2-3 PRs that fix UI/UX issues.)
- Ability to debug changes in general and communicate issues clearly in writing. (See above note re debugging docs.)
- Participation in QA testing. This is required because, for this project, it is important to understand the app from a product perspective. If you are interested in this project, we recommend joining the release testers mailing list at oppia-release-testers@googlegroups.com and looking out for calls to help with release testing.

**Suggested Milestones:**
- **Milestone 1**: Complete the acceptance tests for creators' and contributors' user journeys, and ensure that they run on all PRs (by adding them to the "acceptance test" GitHub workflow). Remove any existing webdriverio tests whose functionality is fully covered by the new acceptance tests.

  Creators' journeys include: exploration editor, blog editor and voice artist CUJs.

  Contributors' journeys include: translation and question submitters, translation and question reviewers.

- **Milestone 2**: Complete the acceptance tests for learners' and admins' user journeys, and ensure that they run on all PRs (by adding them to the "acceptance test”"GitHub workflow). Remove any existing webdriverio tests whose functionality is fully covered by the new acceptance tests.

  Learners' journeys include: guest/anonymous users and logged-in users. Surfaces to test include the site’s static pages, the exploration player, the learner dashboard, the embedded lesson player, the newsletter email signup, and the “contact us” page.

  Admins' journeys include: curriculum admin or topic manager (topic, skill, question creation / editing), contributor dashboard admin, release coordinator (feature flags, flush cache, running a Beam job), site admin.

**What we are looking for in proposals:**

For this particular GSoC project, the proposal is less important and we are more interested in your previous PRs, as described above. We recommend focusing your efforts accordingly.

Some things you could address in your proposal:
- How will you break down this project into individual milestones? Provide a clear timeline for this.
- Explain how your tests would catch console errors that arise during execution of the user journeys.
- For each existing webdriverio test file, specify the set of CUJs which need to be covered by acceptance tests in order for it to be removed. (If you identify gaps in the spreadsheet CUJs during this audit, feel free to suggest improvements to those.)
- In the release-coordinator tab, we want to test the "running Beam jobs" CUJ. Analyze the tradeoffs of creating a separate tiny Beam job for this that runs quickly, doesn't affect the datastore, and that can be added to the list of jobs in the /release-coordinator page, versus using one of the existing Beam jobs. Describe which approach you would take and why. (Note: you can find more info on how to write Beam jobs in [this wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs).)
- Describe how you would handle specific issues that arise in acceptance tests like mobile viewports, waiting for long-running operations like Beam jobs, etc.
- Suggest any improvements to test organization that you would make, or missing CUJs that you would add. You can cross-reference the testing spreadsheet with the CUJ document that is currently used for release testing, or identify those journeys yourself. Focus only on *critical* user journeys -- you do not need to go into detail for all the edge cases.
- Include test specs for some of the journeys that are not yet covered in the spreadsheet, such as the release-coordinator and site admin user journeys. You can also do this for recently-released features or features that are about to be released (like the contributor admin dashboard, learner groups, contributor recognition project, etc.).


**Technical hints / guidance**

- Start by writing tests for just one CUJ to make sure you can do it properly. If you are able to do that well, then there is a good chance that you will be successful with this project.
- For this project, user journeys are detailed in a shared sheet, divided into distinct tabs. During the implementation phase, applicants should tackle each user journey in a structured way, leveraging lessons and code from earlier phases to inform later work. This will help streamline implementation and ensure efficient reuse of developed solutions.
- There is some buffer time built in to the project for improving the organization of tests as more tests get written. Your mentors will work with you on this.
- Note that QA coordinators can advise on CUJs and provide detail on them if any are unclear. Feel free to reach out to them once you've joined the release testing team.


## Android team

### 4.1. Code coverage support and enforcement

**Project Description:**

[Code coverage](https://en.wikipedia.org/wiki/Code_coverage) is a means of quantifying test behavioral coverage. The assumption is that higher code coverage means higher confidence in technical changes. Higher confidence means that the team can rely on more automation to drive releases which, in turn, lets us bring new features to users faster and with fewer bugs.

Historically, this has been a challenging area for the team. Past attempts (see [#2466](https://github.com/oppia/oppia-android/pull/2466) and [#2744](https://github.com/oppia/oppia-android/pull/2744)) ran into challenges with generating correct reports using Gradle. Since the team is also trying to move off of Gradle, Bazel poses its own problems in supporting JaCoCo ([bazel#12159](https://github.com/bazelbuild/bazel/issues/12159)) though rules_kotlin does seem to support it now: [rules_kotlin#508](https://github.com/bazelbuild/rules_kotlin/pull/508) (requires upgrading to a newer version of rules_kotlin which will be done as part of [#4886](https://github.com/oppia/oppia-android/pull/4886) ahead of GSoC coding period starting).

This project entails introducing support for measuring code coverage for all Kotlin files in the Android codebase, with any support gaps documented (e.g. lambdas if those still cause problems: [jacoco#654](https://github.com/jacoco/jacoco/issues/654)). It also involves introducing support for running coverage on a per-unit basis (that is, only measuring the coverage of file Example.kt when running ExampleTest.kt and no other tests), with enforcement for targeting a specific coverage percentage (that's configurable).

**Tracking issues**: [#1497](https://github.com/oppia/oppia-android/issues/1497), [#1726](https://github.com/oppia/oppia-android/issues/1726), [#1727](https://github.com/oppia/oppia-android/issues/1727), [#1728](https://github.com/oppia/oppia-android/issues/1728)

**Not in scope:**
- Adding tests for any existing code not affected by the new script functionality itself. This project is NOT intending to increase code coverage, just add instrumentation for it.
- Updating any projects outside of Oppia Android unless this is required in order to get code coverage working during proposal writing.

**Size of this project:** Medium (\~175 hours)

**Difficulty**: Hard

**Potential mentors:** @BenHenning

**Product Clarifier:** @BenHenning

**Technical Clarifier:** @BenHenning

**Required knowledge/skills:**
- Comfortable with digging into problems that may require exploring code outside of Oppia Android, and that may not have obvious solutions findable via search engines.
- Excellent technical communication skills.
- Strong familiarity with Kotlin (coroutines is a bonus as they will be used during development, but it isn’t strongly required).
- Basic familiarity with using the Bazel command line for building and running tests. Working knowledge of how Bazel targets work.
- Comfortable with performing Bazel queries (e.g. using _bazel query_) and referencing the Bazel [build encyclopedia](https://bazel.build/reference/be/overview) and [query guide](https://bazel.build/query/guide) when needed.
- Working Bazel setup in local development environment. Specifically:
  - _bazel test //scripts/..._ should pass.
  - Recommended: you have a local Android Studio project set up with the Bazel Android Studio plugin (not required, but it can greatly help with day-to-day development).

**Suggested Milestones:**

- **Milestone 1**:  Introduce a new script to compute a per-unit code coverage percentage for a single file.
  - Deliverable 1: Introduce a new scripting utility that can run code coverage for a specific Bazel test target, interpret the results, and return a proto for data processing.
  - Deliverable 2: Introduce a new utility which can, given the proto from the deliverable 1 utility, generate a rich-text code coverage report in one of three formats:
    1. Markdown (for easy copying to GitHub)
    2. HTML (for easy local viewing)
  - Deliverable 3: Update the test exemption check script & its exemption format such that each file now has two possible states:
    1. Exempt from having a test file (the current exemption behavior).
    2. An override of the code coverage to meet a specific minimum (which can be 0%).

- **Milestone 2**: Integrate code coverage checking.
  - Deliverable 1: Introduce a new script that uses the utility from deliverable 1 to perform code coverage analysis for a single target and the utility from deliverable 2 to _optionally_ generate and output a rich-text report file for the test run. This script should always output the computed code coverage for a given file, and have a configuration option to fail if it's below a specified threshold.
  - Deliverable 2: Introduce a new CI workflow which, similarly to the [existing unit test workflow](https://github.com/oppia/oppia-android/blob/3ced7e14a8bff8c3757ed15a1626b0e63c6ce14d/.github/workflows/unit_tests.yml#L16), runs a series of buckets for code coverage analysis using the new script from milestone 1. Report generation should be enabled & reports uploaded as artifacts. Code coverage should only run after tests are passing (on a per-bucket basis if possible).
  - Deliverable 3: Fix/replace the cancellation workflow to ensure re-runs of CI correctly and _quickly_ terminate all existing workflows that are running.
  - Deliverable 4: Introduce a wiki page explaining how to use the code coverage tool, provide advice on how to write tests with good behavioral coverage, and explain the limitations of the code coverage tool (i.e. all the cases it does _not_ correctly count coverage for a specific line).
  - Deliverable 5: File issues for all cases where the code coverage tool misses or incorrectly counts code coverage for future work.

**What we are looking for in proposals:**
- A **working** demonstration of running code coverage using _bazel coverage_ with a test within the Oppia Android project with correct results (it’s fine if some branches aren’t hit due to missing JaCoCo functionality). Proposals that do not include this working demonstration will be rejected as this is considered a critical prerequisite for succeeding in this project.
- All of the components outlined in the break-down Gist are expected to be fully expanded in the document and finalized, including:
  - Adding documentation strings for each proto field, class, and method being proposed.
  - Adding a dependency diagram showing how the components will be interconnected.
  - Adding a sequence diagram to show how the workflows will behave, and how different uses of the scripts will call through to different dependencies.
- That other [scripts](https://github.com/oppia/oppia-android/tree/develop/scripts) in the codebase are used as the basis for fully writing out the technical portions of the proposal.

**Technical hints / guidance**

See this [Gist](https://gist.github.com/BenHenning/4d1db014731eb9b1e5d7ba175df78962).

### 4.2. Multiple classrooms support

**Project Description:**

The app is currently limited to displaying a single list of basic numeracy topics. Together, these topics comprise what we call a 'classroom' (see https://oppia.org/learn/math for Oppia web's classroom viewer).

This project entails introducing support for more than just mathematics topics by revising the core home screen & navigation flows to support topics grouped by their classroom. Future classrooms will include science, financial literacy, and more.

**Reference document**: [PRD](https://docs.google.com/document/d/1uOiDnWBxJmDMwqej-VSRKEnDP4Been3np9y1ov6YTNA/edit)

**Not in scope:** N/A (nothing of note for this project).

**Size of this project:** Large (\~350 hours)

**Difficulty**: Medium

**Potential mentors:** @adhiamboperes

**Product Clarifier:** @moewastaken

**Technical Clarifier:** @adhiamboperes

**Required knowledge/skills:**
- Strong familiarity with how UIs are layered in Oppia Android, and with corresponding terminology: activities, fragments, presenters, listeners, and view models, and how activity and fragment navigation works.
- Good working knowledge of modifying and/or creating new layout files in Android. Ability to read mocks and apply them when creating layouts.
- At least basic familiarity with writing UI tests in Oppia Android.
- Proficiency in writing Kotlin and Android code.
- Familiarity with how DataProviders behave and are used for piping data from the domain layer to the app layer. Familiarity with Kotlin coroutines is a plus, but not required.
- Familiarity with proto files and how the app uses protos for both lesson file formats and data interchange in the app.
- Good working knowledge of the app home screen (from a UX perspective).
- Able to build the project locally using Bazel.

**Suggested Milestones:**
- **Milestone 1**: Introduce new UIs for classroom selection.
  - Deliverable 1: Introduce new feature flag for the multiple classrooms feature.
  - Deliverable 2: Update the model & domain layer to support the definition of classrooms, and specify a classroom per-topic.
  - Deliverable 3: Introduce a ClassroomController.
  - Deliverable 4: Introduce a new activity & related fragments/views/tests for a new classroom selection landing page (recommendations section should be faked out for now).
  - Deliverable 5: Introduce a new activity & related fragments/views/tests for a classroom page with topic list picker.
- **Milestone 2**:
  - Deliverable 1: Update the asset download script ([#4885](https://github.com/oppia/oppia-android/pull/4885)) to support classrooms.
  - Deliverable 2: Implement new recommendations logic & UI support for the classroom selection page (includes updating recommendation cards to include classroom information).
  - Deliverable 3: Update topic cards to include classroom & topic progress information.
  - Deliverable 4: Gated by the feature flag, hook up the new classroom selection page to replace the existing home activity upon profile login.
  - Deliverable 5: Test, iterate, and work with the tech lead to finalize and launch the feature.
  - Deliverable 6: Audit home activity/fragment & recommendation tests to ensure the new utilities cover the same behaviors. Remove the old home activity/fragment.

**What we are looking for in proposals:**

That all of the components outlined in the break-down Gist are expected to be fully expanded in the document and finalized, including:
- Adding documentation strings for each proto field, class, and method being proposed.
- Adding a dependency diagram showing how the components will be interconnected.
- Adding a sequence diagram to show how different user flows will call through to different dependencies in the project.

**Technical hints / guidance**

See this [Gist](https://gist.github.com/BenHenning/8bbc85721747a6c1d4362448b2151aec).


### 4.3. Platform parameter developer dashboard and improvements to platform parameter testing support

**Project Description:**

Feature flags are a special type of configurable [platform parameter](https://github.com/oppia/oppia-android/wiki/Platform-Parameters-&-Feature-Flags#introduction) which allows the team to stage features behind remotely configurable flags until they're ready to be launched. This allows features to be developed across multiple releases without users seeing part of the feature (or app stability issues when the feature is enabled), ensuring the team releases high-quality features and doesn't hurt the overall quality and performance of the app. Broadly, platform parameters allow the team to overall configure the app (which can be useful both for feature flags, as described above, and safety 'knobs' such as controlling rate limits to remote APIs to help reduce the chance of server outages).

This project entails two parts: (1) introduce a developer-only UI (as part of the developer options section of the app) which displays all platform parameters in the app, their current enabled/disabled status (for feature flags) or values (for regular parameters), their sync status (i.e. whether they're being synced from the server or using a local developer default), and allows an explicit manual override to force the feature on or off or override the parameter's value. And, (2) refactor the existing functionality for testing feature flags and platform parameters from using [TestPlatformParameterModule](https://github.com/oppia/oppia-android/blob/3ced7e14a8bff8c3757ed15a1626b0e63c6ce14d/testing/src/main/java/org/oppia/android/testing/platformparameter/TestPlatformParameterModule.kt#L64) to instead using an annotation-based enable/disable/value override trigger with support for multiple parameter tweaks per test, and both per-test and per-class configuration.

**Tracking issues**: [#4303](https://github.com/oppia/oppia-android/issues/4303) & [#4302](https://github.com/oppia/oppia-android/issues/4302)

**Not in scope:**
- Platform parameter and feature flag enumeration.
- Changing existing tests to specific enable/disable features (beyond migrating existing overrides).

**Size of this project:** Large (\~350 hours)

**Difficulty**: Medium

**Potential mentors:** @kkmurerwa

**Product Clarifier:** @BenHenning

**Technical Clarifier:** @kkmurerwa

**Required knowledge/skills:**
- Strong familiarity with Kotlin.
- Strong familiarity with platform parameter and feature flag system, and tests. Preferred to demonstrate working with feature flags in tests.
- Strong familiarity with how UIs are layered in Oppia Android, and with corresponding terminology: activities, fragments, presenters, listeners, and view models, and how activity and fragment navigation works.
- Good working knowledge of modifying and/or creating new layout files in Android. Ability to read mocks and apply them when creating layouts.
- Good working knowledge of different app build flavors.
- At least basic working knowledge of the in-app developer options screens.
- At least basic working knowledge of protos and textprotos, and how they’re used in the app.
- Able to build the project locally using Bazel.

**Suggested Milestones:**
- **Milestone 1**: Introduce improved testing support for platform parameters.
  - Deliverable 1: Introduce new annotations for overriding feature flags, platform parameters, and defaulting each back to normal, all targeted for test classes and methods.
  - Deliverable 2: Update OppiaTestRule to properly arrange the platform parameters and feature flags for each overridden value as indicated by the class-level and method-level annotations.
  - Deliverable 3: Update OppiaTestRule to fail if it's not the first rule run for a test, and update any tests that fail because of this.
  - Deliverable 4: Add a regex check ensuring that OppiaTestRule is always present in a test file, and update all tests that are missing the rule.
  - Deliverable 5: Migrate all old TestPlatformParameterModule usage over to the new annotations and remove the module.
- **Milestone 2**: Introduce UI for overriding platform parameters and feature flags.
  - Deliverable 1: Refactor the domain logic for platform parameters and feature flags to facilitate value updating using compile-time module configuration (i.e. production implementations should make it impossible to override platform parameters).
  - Deliverable 2: Introduce a new platform parameter to gate the override UI feature.
  - Deliverable 3: Introduce a new UI that distinctly lists:
    - Platform parameters and features (each should be distinctly indicated).
    - Both parameters & features show, for each:
      - Their name.
      - Their local default value.
      - Their remote value (if any).
      - Their current value.
      - Their sync status, that is one of: unspecified, using local value, using remote value, using override value.
    - Parameters show the values of the parameter based on type. Feature flags show based on enabled/disabled state (rather than true/false boolean values).
  - Deliverable 4: Update the UI to include support for overriding values.
    - Platform parameters provide true/false switches for boolean values, and text input for integers & strings.
    - Feature flags provide enable/disable switches.
    - Both provide a button for resetting the override (only if it’s set).
  - Deliverable 5: Update the UI to include a status indicator for whether the app needs to be restarted in order for the override to take effect, and a button to force restart the app (i.e. by crashing it and letting the user reopen it).
  - Deliverable 6: Test, iterate, and finalize (i.e. release) the new UI to developers.
  - Deliverable 7: Introduce a new wiki page demonstrating the UI and explaining how and when to use it. Add an interactive link to this page in the new UI itself.

**What we are looking for in proposals:**
- All of the components outlined in the break-down Gist are expected to be fully expanded in the document and finalized, including:
  - Adding documentation strings for each proto field, class, and method being proposed.
  - Adding a dependency diagram showing how the components will be interconnected.
  - Adding a sequence diagram to show how different user flows will call through to different dependencies in the project.
- Examples of the new feature testing API.
- Hand-created mocks for the new platform parameter dashboard (these can be rough; they just serve as the basis for development of the project).

**Technical hints / guidance**

See this [Gist](https://gist.github.com/BenHenning/93f89b9cc824e090fbcce1cfade3152e).
