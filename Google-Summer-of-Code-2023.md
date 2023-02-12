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

This year, Oppia will be participating in [Google Summer of Code 2023](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers students and non-experienced contributors the opportunity to discover and work with open-source organizations. The contributions are supported by a stipend. Contributors work closely with one or more mentors from an open-source organization to implement either a project idea by the organization, or a proposal of their own. You might be interested in our GSoC info pages from previous years: [2022](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2022), [2021](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2021), [2020](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020), [2019](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2019), [2018](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018), [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

In order to receive updates about GSoC at Oppia, please subscribe to the [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce) mailing list.

Oppia will be giving an automatic extension to all the projects i.e, all the projects will have 8 weeks for each milestone, with an internal evaluation after 6 weeks. The coding period dates are strict and intended to balance offering flexibility to contributors with the need on the org admin side to have a streamlined process and a more time-bounded GSoC period. Contributors may opt for a shorter timeline if desired.
Therefore, there will not be any additional extensions. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below.

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions [here](https://github.com/oppia/oppia/wiki).


# Contributors

GSoC is an excellent opportunity for new contributors to get paid to work on an open source project. If you're interested in applying as a contributor, you should definitely read the following resources:

-   [Google Summer of Code contributor guide](https://google.github.io/gsocguides/student/)
-   [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
-   [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)


## Getting started

Welcome! If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. If you like, you can also turn on notifications for [Github Discussions](https://github.com/oppia/oppia/discussions) to participate in general discussion related to Oppia's involvement in GSoC. Make sure to set your preferences correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is about:
    - Read the [user documentation](http://oppia.github.io/#/) to become familiar with important concepts like explorations and interactions.
    - Play some lessons on [Oppia.org](https://www.oppia.org/learn/math), which hosts a live instance of Oppia.

3. To get started with development, read and follow the instructions in the contributors' guide carefully ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up)).
    - **Note!** Oppia Android won't be offering GSoC projects in 2023, but will be doing so again from 2024 onwards.

4. Do one or more starter projects to become familiar with the contribution process. This will help us get an idea of what it's like to work with you. It will also help you get a better understanding of the codebase and our development process, which may help with writing a good project proposal. Once you've merged at least 2 pull requests, you will get an invitation to become a collaborator to the Oppia repository and be officially onboarded! **This step is a prerequisite** to applying for GSoC.

   - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to read the [["getting started" guide|Contributing-code-to-Oppia]] and [[PR instructions|Make-a-pull-request]] carefully, follow the [tips for success](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#tips-for-success), manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide), and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Select one or more [GSoC project ideas](#oppias-project-ideas-list) that you're most interested in, and write your project proposal! We strongly encourage you to discuss your project ideas and share your proposal with the community, so that you can get feedback and ensure that what you're writing makes sense to others. Please follow the instructions in the [GSoC proposal template](#gsoc-proposal-template) section to do this.

    If you have any questions about a project, or would like to discuss your approach with the Oppia community and get feedback, you can also email the [oppia-gsoc-discuss@](https://groups.google.com/g/oppia-gsoc-discuss) mailing list. Please be specific when asking questions, since this makes it easier for us to help you.
    - **Pro-tip!** 75% of the accepted proposals had begun their work at least 4 weeks prior to the deadline. Hence, we strongly recommend that the contributors start writing proposals as early as possible.

    Good luck!


## FAQs

**Q: Is Oppia Android a part of this year's GSoC?**

A: Oppia Android won't be able to participate in GSoC this year. Note that this is a one-off, and Oppia Android hopes to be back in 2024 when we have better processes and documentation to help contributors get onboarded more smoothly.

**Q: What technical skills do I need to work on Oppia?**

A: For Oppia Web, Angular 2+, Python 3.8 and Google App Engine are useful and recommended for most Oppia work; in addition, UI design skills are useful for frontend, user-facing work. Please see the individual project ideas to determine whether these skills are recommended for the project in question.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other contributors, successfully contributing, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: No, Oppia will strictly adhere to GSoC timeline and will usually not be able to provide any additional extensions. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below.

**Q: Which projects are most important for Oppia?**

A: All the projects we've listed in the [Ideas List](#oppias-project-ideas-list) are important, and we'd be very happy to see good progress made on any of them! Projects are treated as equally important during selection; note that the relative importance of a project to Oppia is not part of the [selection criteria](#selection-criteria). We strongly encourage you to pick a project that you'd enjoy doing over the summer!

**Q: Can I submit more than one proposal to Oppia?**

A: Yes, you can. However, we strongly recommend picking one project and writing a solid proposal for it. Splitting attention across multiple projects might not be a great idea. (That said, GSoC is offering full-length and half-length projects, so one exception might be if you're interested in doing either the 'full version' or the 'half version' of a project idea that can support both modes. In such a case, you would be welcome to submit both the 'full version' and the 'half version' as separate applications, but, before doing so, please make sure that you'd be happy with either outcome if you are selected.)

**Q: How early should I start working on the proposal?**

A: As early as possible. Make sure to get feedback from mentors before finally submitting the proposal. This will help you to write a better proposal, as you can refine the details based on the feedback you receive. Mentors will need some time to review your proposal, so it's a good idea to begin as early as possible. Make sure to follow all instructions in the [proposal template](https://docs.google.com/document/d/1yYefLkT7dJJa86MyrdWpbZtzeaWAKCi1eXZZDGUrasM/edit) (especially around sharing and access) to reduce delays in reviewing your proposal. Please note that 75% of the accepted proposals for last year had begun their work at least 4 weeks prior to the deadline. Hence, we strongly recommend that the contributors start writing proposals as early as possible.

**Q: I only discovered Oppia recently. Does this mean that, during selection, my application would automatically be ranked lower than those by other applicants who have a longer tenure with Oppia?**

A: Definitely not! Here are the [selection criteria](#selection-criteria) we use when selecting contributors for GSoC. Note that tenure is explicitly not part of these criteria.

**Q: What are the minimum number of PRs that one should have?**

A: You should have at least 2 PRs merged, but they don't need to be large. Beyond that, remember that quality is more important than quantity. It is better to submit a non-trivial PR rather than a one-line wording change. Start with starter issues, then move ahead with prioritized issues from the team that is offering the project you are interested in.
Here are the boards of the respective teams: [LaCE Quality](https://github.com/orgs/oppia/projects/3/views/8), [Developer Workflow](https://github.com/orgs/oppia/projects/8/views/11), [Contributor Experience](https://github.com/orgs/oppia/projects/18/views/4).

**Q: What is the total number of contributors that will be accepted?**

A: As many as we think will succeed, though the Google GSoC admins may impose limits based on how they decide to distribute contributor slots among the different open-source organizations.

**Q: I do not have any experience in skill XYZ. Is some certification required?**

A: Try to work on good first issues and take courses online. In the field of software development, it is common to develop experience and expertise as you take up and complete projects successfully. We do not require any formal certification of particular skills.

**Q: Is it okay if I only focus on the frontend or backend?**

A: This probably depends on the project(s) you wish to apply for. However, note that the ability to be effective in both the frontend and backend will open up more opportunities for you, since projects often touch multiple layers of the stack.

**Q: The [Google GSoC FAQ](https://developers.google.com/open-source/gsoc/faq#can_someone_already_participating_in_open_source_be_a_gsoc_contributor) mentions that the program is only for new contributors. I have already contributed to Oppia and I have write access. Can I still participate?**

A: The GSoC program is open to new and beginner contributors to open source and to students. Some of our contributors with write access are still beginner contributors, whereas some of our other contributors with write access will not qualify because they are experienced contributors. If you have only recently received write access, or have been contributing to Oppia for less than a year, you are probably still a beginner contributor. If the previous sentence does not apply to you, and you want to know which group you fall into, please contact **@srijanreddy98**, **@U8NWXD** or **@aasiffaizal** for a decision.

**Q: I'd love to contribute to open source, but I'm not sure I have enough time during the summer to do a GSoC project. Can I still help out?**

A: Yes, GSoC might not be the best choice if you don't have enough time during the summer. However, you can start contributing to Oppia by following the instructions in the contributors' guide ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Oppia Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)).

**Q: Why doesn't Oppia provide difficulty levels for projects?**

A: Difficulty can vary from person to person depending on the skills required which is why we list all the prerequisite skills for each project.

## Dates and Deadlines

Noteworthy dates for 2023 ([Full Timeline](https://developers.google.com/open-source/gsoc/timeline)):

- **Jan 23 - Feb 7**: Mentoring organizations apply
- **Feb 22**: Mentoring organizations are announced
- **Mar 20 - Apr 4**: GSoC contributor application period
- **May 4**: Accepted GSoC contributors are announced
- **May 4 - May 28**: Community bonding period
- **May 29 - Jul 26**: Standard Milestone 1 work period for GSoC contributors
- **Jul 31 - Sep 27**: Standard Milestone 2 work period for GSoC contributors
- **Oct 6**: GSoC period at Oppia officially ends

**Note!** The coding period dates are strict and intended to balance offering flexibility to contributors with the need on the org admin side to have a streamlined process and a more time-bounded GSoC period.

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

- Technical ability
    -   Writing clean code, while keeping in mind the requirement for the code to run in production.
    -   The quality of code that I write now is much improved. Also, I got the experience of working with a team.
    -   Building an entirely new feature in a scalable way.
    -   Writing robust tests.
    -   Working on a large codebase.
    -   Reading and understanding code from other open-source organizations.
    -   I gained a lot of technical knowledge, learned how to write automated tests better, got better at communicating and getting myself unblocked, among other things.
- Technical domain knowledge
    -   I feel more confident on working with Angular. Oppia was the first time I worked with unit and e2e tests.
    -   I feel a lot more confident in writing code now, whether it be making my own projects or contributing to other open-source projects.
    -   I learned lots of things about typescript and webpack.
    -   The biggest improvement is that now I can make better design decisions, UI decisions, and technical decisions, and my understanding of the overall full-stack development has increased.
    -   I enjoyed finding and fixing accessibility issues.
    -   I learned the importance of testing and also following a clean architecture.
- Technical leadership skills
    -   How to manage my time well, how to achieve deadlines especially when I got evaluations from external evaluators.
    -   How to properly plan a project before implementing it.
    -   Technical design skills (and validation of technical ideas).
    -   How to give, respond to and understand reviews.
- Communication and personal development
    - Putting forward my thoughts more systematically and deeply so that everyone can understand me well.
    - My conversation skills have surely improved and I feel more confident while joining online meetings. Also, I am more mindful of the deadlines and enjoyed solving challenges faced in this project.
    - How to write a good proposal.
    - How to work with a large community like this which is spread over different time zones.
    - How to reach out to people, work with them, and solve each other's problems.
    - I have become a better developer, not only in term of technical skills but in thinking of actual application of the product build and the edge case scenarios the user might face. Another major learning has been to speak up and ask for help or anything required which I previously was not too confident of.
- Why contributors want to stay
    - Community
      - I had a great experience with Oppia and would like to continue contributing to the project. I'd like to help newer contributors too, (for example by reviewing their code when I get the chance).
      - The organisation is active and have strong community bond.
      - It is really an awesome experience working with some amazing folks from all around the world at Oppia.
      - The kind of support the complete community provides is extra-ordinary.
    - Giving back
      - "Everybody wants to do some good work but lets be honest, it is maybe the lazyness or the time issue that you are not able to do the type of work you always wanted to do, what can be a good way to give back to the community than to contributing here.
      - It makes me very happy that I'm a part of an organization which provides free education and I think the education is the biggest blessing we can give to one to make them stand on their feet.
      - I would love to be part of this org by knowing that maybe not much but yes I'm trying to make an impact and my contribution in the educational field. I really want to do this because where I come from there is not much of education.
      - Also the main reason to stay connected is the purpose the community serves. Providing education to those who do not have access to it helps me give back to the society.
    - Growth / learning:
      - Working with Oppia has really helped me grow as a developer and I would really like to stick around to gain even more experience of real world software development.
      - The kind of work that Oppia does is really inspiring and there are a lot of opportunities to improve your skills be it be technical skills or leadership skills and most of all the people at Oppia are really fun to work with :)
      - I like working in Oppia since it not only helps me improve my coding skills but also helps me grow as an individual.



## GSoC Proposal Template

When submitting a proposal, please use the provided [GSoC proposal template](https://docs.google.com/document/d/1ZZEJXCFgqPgPDuImKAW6EB9SMOS8cICPI2uCsVLww8w/edit#). We will only consider proposals submitted using this template.

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

If you'd like to get a sense of what a proposal might contain, please see our [GSoC 2022 page](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2022) for examples of proposals that we accepted in 2022. However, please note that the [GSoC Proposal Template](#gsoc-proposal-template) has been slightly updated for 2023, so please be sure to follow the 2023 template.

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

If you have questions pertaining to "how to get started with Oppia" or any other queries regarding GSoC at Oppia, please ask them on **GitHub Discussions** ([Web](https://github.com/oppia/oppia/discussions)). Please be specific when asking questions; this makes it easier for us to help you. Also, please make sure to read the relevant "getting started" wiki page ([Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up)) first, since the answer to your question might already exist there!

To receive important announcements and updates about GSoC at Oppia, please subscribe to the **[Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce)** mailing list.

## Oppia's Project Ideas List

_**Note:** If you're coming to this section from an external link, please make sure to scroll up and read this entire wiki page carefully, not just this section. There's a lot of useful information on the rest of the page, including a FAQ and a section describing selection criteria. Thanks!_

The following is a list of Oppia's 2023 GSoC project ideas. You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community beforehand in order to get feedback and guidance to improve the proposal. We'd also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

Please note that the list of project ideas below is not set in stone: more projects may be added later, and some project descriptions may also change a bit, so check back regularly. In addition, the mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted.

### Learner and Creator Experience (LaCE) team

1.1. [Implementing the “Needs Guiding Responses” section of the lesson analytics dashboard](#11-implementing-the-needs-guiding-responses-section-of-the-lesson-analytics-dashboard)

1.2. [Improving the lesson creation experience](#12-improving-the-lesson-creation-experience)

1.3 [Serial chapter launch](#13-serial-chapter-launch)

1.4 [Learner dashboard redesign](#14-learner-dashboard-redesign)

1.5 [Improvement to math interactions](#15-improvements-to-math-interactions)

1.6 [Accessibility improvements](#16-improve-accessibility)

### Contributor Dashboard team

2.1. [Contributor Dashboard Admin Stats Table](#21-contributor-dashboard-admin-stats-table)

2.2. [Prioritized Translation Languages and Auto-Translations](#23-improvements-for-translation-reviewer-experience)

### Data validation team

3.1 [Fix validation errors](#31-fix-validation-errors)

### Developer workflow team

4.1. [Dockerize Oppia](#41-dockerize-oppia)

4.2. [Developer Workflow Release Dashboard](#42-developer-workflow-release-dashboard)

4.3. [Developer Workflow Telemetry Dashboard](#43-developer-workflow-telemetry-dashboard)

4.4. [Make CI faster](#44-make-ci-faster)

4.5. [Normalize Usage of Feature Flags](#45-normalize-usage-of-feature-flags)

## Learner and Creator Experience (LaCE) team

### 1.1. Implementing the “needs guiding responses” section of the lesson analytics dashboard

**Project Description:**

Oppia has, for each exploration, an “improvements tab” that shows common wrong answers to a question. This allows lesson creators to subsequently improve the lessons. (For example, if a particular wrong answer isn’t addressed well by the existing feedback, and is being submitted regularly, then we can detect this and update the lesson.) This is important for ensuring that learners don’t get stuck.

Unfortunately, the existing stats dashboard is somewhat unwieldy and not well-suited for easily taking action to update lessons. A new [improvements tab](https://drive.google.com/file/d/1GOrwZhVKCunSmOgbvMDaGFU2LSjT_MOf/view) that is more editor-friendly has already been (mostly) designed. This improvements tab shows improvements that can be made to the exploration, categorized by bounce rate, incomplete learning, and specific wrong answers for cards.

The aim of this project is to implement the part of the improvements tab that covers “Card-Level Improvements > Needs Guiding Responses”. (The other parts are out of scope for this project.)

The main challenge for this project is surfacing the necessary data for this view correctly and quickly. In order to do this, the data needs to be grouped and arranged properly in the backend for easy retrieval. This data should be kept up-to-date using Apache Beam jobs that are regularly run using a cron scheduler, but since there is a lot of data, there should be some aggregation and archival strategy so that the cron jobs do not need to perform computations on the full historical dataset each time. The aim of this project is thus to build out this data pipeline and ensure that it is robust, and display its output in an easy-to-understand way in the exploration editor improvements tab.

**Size of this project:** large (~350 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

* Knowledge and understanding of Python
* Ability to write Beam jobs
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Strong technical design skills

**Suggested Milestones:**

* **Milestone 1:** Implement the data pipeline for answer statistics. This should include (a) generating one-off archival models for historical data that can be queried quickly, (b) creating “realtime” models for each exploration/state that store the most recent set of answer data, (c) adding a trigger to update the archival model via a deferred job once the realtime model exceeds a certain number of distinct answers or storage size, (d) implementing the necessary queries and controllers to provide the “top wrong answers” data to the frontend. These jobs should work correctly in production.

* **Milestone 2:** Implement the UI for the “Card-Level Improvements > Needs Guiding Responses” section of the improvements tab. This section should correctly display answers for the various different types of interactions (note that the mock in the “Useful Resources” section only shows one such type, which is TextInput answers). It should also display an “Address Answers” call-to-action which, when clicked, brings the user to the relevant part of the main exploration editor tab, which would also open the “Add Response” dialog box with a reminder of the wrong answers they still need to address, so that they can add new answer groups and feedback for them (see more details [here](https://docs.google.com/document/d/1qQbW9Z_cgJ1mwU0hzBpPVS_4WLT_l_08ZixLR1G2bvQ/edit#heading=h.c63b1rerczu8)).

**Dependency on Release Schedule:**  Since this project involves a step to generate archival models, the timeline should be arranged so that this step can be run and verified during the appropriate release cycle. Note that releases can be delayed by up to a month, and you should account for such delays in your timeline.

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

### 1.2. Improving the lesson creation experience

**Project Description:**

The aim of this project is to provide three enhancements to the exploration editor page for lesson creators: (a) showing the history of metadata changes to an exploration; (b) showing the history of changes to a specific card and allowing that history to be browsed through; (c) allowing creators to see which languages a particular part of a lesson has been translated into when editing it, and to update those translations if appropriate.

(**Note**: If desired, you may submit a proposal for a <span style="text-decoration:underline;">half-size project</span> covering EITHER both options (a) and (b), OR option (c). If you do this, please label your proposal accordingly with “parts (a) + (b)” or “part (c)” in the title.)

For (a): The current exploration history tab allows comparison between each “state card”, but doesn’t include details of the exploration metadata. An additional box containing these details should be added to the comparison graph.

For (b): In the state editor, it should be possible to see a “Last edited by XXX at version YYY” annotation (excluding translation commits) at the bottom right. Clicking this should open a pop-up modal that shows the changes made to the card in that last edit, and a further link at the bottom right saying “Previously edited by XXX at version YYY” which, when clicked, advances the modal to the previous change, and so on. (This is intended to function a little bit like “git blame” in the GitHub UI.)

For (c): In the state editor, when a change is made to a part of a card and this results in a “should translations be updated?” pop-up modal, the modal should also include a list of the existing languages for which that content has been translated, and the currently-saved translations for those languages. The lesson creator should be asked to update these translations if the changes are trivial to do (e.g. the content is just numbers), and otherwise leave them alone by default. This will help to save some re-translation work for the community. **Note**: these translation changes should not be applied immediately – if the lesson creator subsequently discards their change before committing it to the backend, then those translation changes should also be discarded.

**Size of this project:** large (~350 hours); can be reduced to medium (~175 hours) if desired (see description)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS
* Ability to write Beam jobs
* Technical design skills
* (Ideally) Some UI/UX design skills

**Suggested Milestones:**

* **Milestone 1:** Creators should be able to see changes to an exploration’s metadata in the comparison view in the history tab. They should also be able to navigate through all the historical changes to a particular state (excluding changes that solely affect translations).
* **Milestone 2:** Creators should be able to see a list of existing translations through the modal that pops up when they make changes to a published exploration, and should be able to edit those if the edits are easy to make.

**Dependency on Release Schedule:** Some sections of this proposal may entail writing Beam jobs to update existing server data. The timeline should be arranged so that such jobs can be run and verified during the appropriate release cycle. Note that releases can be delayed by up to a month, and you should account for such delays in your timeline.

**Proposal notes:**

* The main thing that is important to demonstrate in the proposal for this project is good technical design skills. Strong proposals would first show a good understanding of the current system, and correctly describe the parts of it that are relevant to the relevant subproject, before suggesting the changes that would be needed in order to achieve the desired functionality.
* For (b), some precomputation may be needed in order to retrieve the version of the "previous change" quickly.
* For (b), it would be useful to generalize the system so that one can go forward/back from any given state. This would allow additional useful functionality like clicking on a state in a particular version when it's shown in the history tab, and moving forward/back through its history. Be sure to handle state additions, deletions and renames correctly!

**Useful resources:**

* How to write Apache Beam jobs: [wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs)
* Release schedule: [wiki page](https://github.com/oppia/oppia/wiki/Release-schedule-and-other-information)

### 1.3. Serial chapter launch

**Project Description:**

Currently, it takes a very long time to publish lessons as it requires the entire topic to be published. Therefore, the broad aim of this project is to create a system that allows for individual lessons to be published as they are created.
This project involves the following steps:
1. Allow curriculum admins to create a pipeline/queue of unpublished chapters on the story editor page by assigning each lesson one of three labels: Draft, Ready to Publish and Published.
2. Allow curriculum admins to set up planned dates for publication for the lessons currently in the queue. These dates should be used to notify the curriculum admins about upcoming or behind schedule launches.
3. Create a system that sends weekly emails to curriculum admins notifying them about upcoming or missed deadlines.
4. Notify learners about recently published lessons on the learner dashboard and the classroom page, and about upcoming ones on the chapter end card.
5. Allow learners to opt to receive email notifications when new lessons are published.

**Link to PRD:** [Serial Chapter Launch](https://docs.google.com/document/d/1Uh_CJRhGE4IM7c0ENdmXkoMD0YtGqFsl1ObR6vvmxdY/edit)

**Size of this project:** medium (~175 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS

**Suggested Milestones:**

* **Milestone 1:** Create a system that allows curriculum admins to add lessons to the pipeline and mark them with appropriate labels and deadline dates, which is then used to send appropriate notifications to the admins once a week via email.
* **Milestone 2:** Implement the learner-facing part of this project that involves pushing notifications to the learner dashboard and the classroom pages when new topics are published. Also notify learners about upcoming topics when they reach the chapter end card. Learners should also be able to sign up to receive email notifications when new lessons are published. 

**Proposal notes:**

* Hide this feature behind a feature flag until the entire project is complete.

**Useful resources:**

### 1.4. Learner Dashboard Redesign

**Project Description:**

The Learner Dashboard is the “home page” for signed-in learners. This is the place where they can get a broad understanding of their progress and quickly be able to pick up where they left off or start something new.

In its current state, the architecture of the learner dashboard is inconsistent and unintuitive. Therefore this project aims to fix various issues plaguing the learner dashboard. Broadly, the contributor is expected to the following:

1. Move the “Feedback Updates” tab out of the learner dashboard to the profile pic dropdown. There should also be an indicator that appears when there are updates to show, and the overall feedback-update flow (including sending and receiving messages in feedback threads) should work smoothly.
2. Update the learner dashboard to have the following architecture:
   - Home
     - “Continue where you left off” section 
       1. CTA to start any lessons (from Classroom or community library) that are in progress
       2. CTA to start next suggested lesson for any goals they’ve set (if any) 
       3. CTA to start next suggested lesson to complete for any learner groups they’ve joined (if any) 
     - Learn something new section
       1. Show topics in classroom and CTA to view the topic pages
       2. CTA to start any lessons that haven’t been started that are in their Play Later list (if any)
       3. CTA to go to Math Classroom (“Browse All Math lessons”) 
       4. Lesson search box
     - Learner Groups section
       1. Show any invitations that are not yet responded to for learner groups
       2. Include CTAs to show more info, accept, or decline invitation
       3. Include a CTA to view any learner groups they’ve already joined (should navigate to the associated learner group page) 
     - Review section
       1. If they’ve completed any previous topics from the classroom, suggest CTAs for up to 3 relevant review cards 
     - Goals
       1. CTAs to set or remove any goals (can only have up to 5 goals set at a time)
       2. Can view current goals and progress towards completing those goals
       3. Can view previously completed goals
       4. CTA to start next suggested item to move forward their goal (i.e. next lesson in the topic they need to complete) 
     - Progress
       1. Can view all lessons (Classroom and Community Library) that are currently in progress 
          - CTA to continue any of these lessons 
       2. Can view all skills they’ve started learning or mastering (i.e. via Practice sessions) and the level of mastery 
          - CTA to start practice session with that skill (will be directed to practice session tab for that topic with that skill pre-selected) 
          - CTA to view relevant review card for that skill
       3. Can view all completed lessons (Classroom and Community Library) 
3. Make sure the new architecture and UI is responsive and has all the necessary accessibility labels (like aria, tag etc)


**Link to PRD:** [Learner Dashboard IA Redesign Project Primer](https://docs.google.com/document/d/1PIs9QaEF_Itbj_H8lLWe-NsP18QSNY0f_JLsZW2e_PQ/edit)

**Size of this project:** medium (~175 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

* Knowledge and understanding of TypeScript, Angular, HTML, and CSS

**Suggested Milestones:**

* **Milestone 1:** Move the feedback tab out of the learner dashboard and add it in the profile pic dropdown menu and add an indicator to notify the user when there updates to show and update the architecture for the home tab. Verify that the feedback flow is working fully end-to-end.
* **Milestone 2:** Update the architecture for the Goals and Progress tabs.

**Proposal notes:**

**Useful resources:**

### 1.5. Improvements to Math Interactions

**Project Description:**

In the current system,
- There is no interaction that takes percentages as a response. Currently,  TextInput fields are used to take input in the form of percentages. 
- Learners use their physical keyboards on laptops or desktops to give input to math explorations. This may create confusion and can slow down or hinder learners' progress. For example, users may not identify * as the symbol for multiplication, they may instead provide “x” as the symbol for multiplication in their response, which will be recorded as a wrong answer.

The proposed solution to this problem is to:

1. Introduce clickable keys to solve math interactions.
   1. For algebraic expression, numeric expression and algebraic equation input, clickable buttons with special characters will show up below the input field on desktop/mobile. Each button contains a single character (like ‘+’, ‘-’, ‘×’, ‘÷’, ‘(‘, ‘)’, ‘=’), and when clicked it will “type” that character in the input field. 
   2. Lesson creators will be able to customize which of these buttons are shown. 
   3. Learners should be able to use both these keys and their standard keyboard when submitting their solution.
2. Allow learners to submit answers in the form of percentages and allow curriculum admins to convert the responses from text input fields to percentage.
   1. Introduce a percentage interaction with a ‘%’ button below it.
   2. Provide a utility, gated behind a feature flag, for curriculum admins to convert existing text input fields to percentage input. Curriculum admins should be able to transform text input to percent input with the click of a button, and the system will accept that change and perform the necessary updates if it is able to validate that the update can be done successfully for that exploration card. The effect of the button should be to perform the standard actions that would be needed to do the update manually, but without losing any of the existing answer groups, translations, and voiceovers. 

**Link to PRD:** [Improvements to Math Interactions PRD](https://docs.google.com/document/d/1cha8e5H4Dfb7t8cLL2VZYi02Ysk2YEdyyalY1dDqPXE/edit#heading=h.rpq25vez37fp)

**Size of this project:** medium (~175 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, HTML, and CSS

**Suggested Milestones:**

* **Milestone 1:** Implementation of percentage interaction
* **Milestone 2:** Implementation of text to percentage conversion utility and virtual math keys

**Proposal notes:**

Math symbol input:
- In order to allow the lesson creator to customize which buttons are shown, a new customization arg will be needed for the interactions. This entails a change in the schema to the explorations, so an exploration migration will be needed. Sensible default values for this customization arg should be chosen – e.g. all arithmetic operation symbols and parentheses – but the creator should be able to turn these off if needed (e.g. in a lesson about division, many of the other symbols will not be relevant).


**Useful resources:**

### 1.6. Improve Accessibility

**Project Description:**

Oppia aims to provide a good and fruitful learning experience to all people. This includes people with certain conditions like poor vision, hearing loss etc. Certain tools like Lighthouse grade pages based on their accessibility and assign a score from 0 to 1 (inclusive). As of now not all pages on Oppia have an accessibility score of 1, which can make it difficult for some learners to use Oppia which is not ideal.

Therefore, the aim of this project is to improve the accessibility of all learner facing pages on Oppia, i.e. getting the Lighthouse scores of all these pages to 1.0. Under this project, the contributor is expected to fix all [the accessibility issues](https://github.com/oppia/oppia/issues?q=is%3Aissue+is%3Aopen+label%3Aa11y+) that have already been filed and run Lighthouse tests on all learner facing pages and bring their scores to 1.0, if that isn’t already the case.

**Link to PRD:** [Improvements to Math Interactions PRD](https://docs.google.com/document/d/1cha8e5H4Dfb7t8cLL2VZYi02Ysk2YEdyyalY1dDqPXE/edit#heading=h.rpq25vez37fp)

**Size of this project:** medium (~175 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

* Knowledge and understanding of TypeScript, Angular, HTML, and CSS

**Suggested Milestones:**

* **Milestone 1:** Fix all the [accessibility issues](https://github.com/oppia/oppia/issues?q=is%3Aissue+is%3Aopen+label%3Aa11y+) already filed on Oppia’s github repository.
* **Milestone 2:** Bring the Lighthouse Accessibility scores of all learner facing pages to 1.

**Proposal notes:**

Run [Lighthouse tests](https://developer.chrome.com/docs/lighthouse/overview/#devtools) in the browser


**Useful resources:**

## Contributor Dashboard team

### 2.1. Contributor Dashboard Admin Stats Table

**Project Description:**

Contributor dashboard admin page revamp. Table view of contributors with key stats, e.g. number of translations/questions submitted/reviewed. Each row represents a contributor and is actionable, allowing an admin to add or remove contribution rights.

**Size of this project:** medium (~175 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, basic HTML, and CSS

**Suggested Milestones:**

* **Milestone 1:** Complete the backend changes:
  - Introduce language coordinator admin role
  - Modify contributor dashboard admin controller to allow adding or removing language coordinators
  - Add new endpoint to contributor dashboard admin controller for fetching contributor stats

* **Milestone 2:** Complete the frontend changes:
  - Display contributor stats table on contributor dashboard admin page
  - Show different available admin actions depending on user admin role
  - Add support for sorting by table column (will require some backend query changes)
  - Implement table pagination


**Dependency on Release Schedule:**

**Proposal notes:**

* For contributor stats, you can query the existing stats models in core/storage/suggestion/gae_models.py, e.g. `TranslationContributionStatsModel`.
* To support sorting by table column, we’ll need to add a sort key for each attribute. The sort key will be used in the storage query. See PR [#1653](https://github.com/oppia/oppia/pull/16534) for an example.
* Pagination is hard. See PR [#16289](https://github.com/oppia/oppia/pull/16289) to see how pagination was added to the existing contributor stats tables.


**Useful resources:**

### 2.2. Prioritized Translation Languages and Auto-Translations

**Project Description:**

Support the marking of languages as “prioritized” for translation. Prioritized languages will have their remaining untranslated lesson text content auto-translated to make the lessons available in the language as quickly as possible. Auto-translated content will appear with a note explaining the auto-translation. Non-prioritized languages will also be auto-translated after a threshold of translation, e.g. 95%.

Additionally, finish adding [computer-aided translation (CAT)](https://docs.google.com/document/d/1kJd-yLTzB9a2c3Nq7v9pzKfHwKHKGpkWfQ8B0YGf50U/edit#heading=h.24wysknhgyrz) support when submitting translation suggestions.

**Size of this project:** medium (~175 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

* Knowledge and understanding of Python
* Knowledge and understanding of TypeScript, Angular, basic HTML, and CSS

**Suggested Milestones:**

* **Milestone 1:** Complete the backend framework for prioritized languages:
  - Add notion of prioritized language in backend storage schemas
  - Store list of prioritized languages
  - Create beam job to auto-translate remaining text content for a prioritized language


* **Milestone 2:** Surface prioritized languages in the UI and add CAT support:
  - Enable the adding of a prioritized language in the contributor dashboard admin page
  - Add note to lesson text content that has been auto-translated
  - Auto-translate non-prioritized language once translation threshold has been achieved (95%)
  - Add computer-aided translation capability to translation contribution modal



**Dependency on Release Schedule:** Some sections of this proposal may entail writing Beam jobs to update existing server data. The timeline should be arranged so that such jobs can be run and verified during the appropriate release cycle. Note that releases can be delayed by up to a month, and you should account for such delays in your timeline.

**Proposal notes:**

* We’ll likely write a beam job to populate the auto-translations for a language. See the [wiki](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) for more details.
* Maybe ~80% of the CAT work is already done, including all of the backend changes. We just need to hook it up in the frontend, e.g. see working PR: [#12624](https://github.com/oppia/oppia/pull/12604/files) and related issue [#11434](https://github.com/oppia/oppia/issues/11434).
  - See Computer Aided Translations (CAT) backend milestone PRs.
* The CAT backend utilizes the Google Translate API for auto-translations. We can re-use that work here for auto-translations. Alternatively, we can investigate other translate APIs that may offer better translations, e.g. Oppia has done studies in the past that have shown Microsoft to produce preferred translations.


**Useful resources:**


## Data validation team

### 3.1. Fix validation errors

**Project Description:**

The aim of this project is to fix various problems with data in our existing models. In order to do that, usually you’ll write a Beam job that takes the existing models and fixes them.

Task set 1
- Implementing a process to ensure that external storage models linked to a storage model are updated in case of storage model deletion ([#10809](https://github.com/oppia/oppia/issues/10809)) 
- Removing traces of ‘cloned from’ from old versions of some explorations ([#10828](https://github.com/oppia/oppia/issues/10808))
- Fixing datetime fields in `LearnerPlaylistModel`, `CompletedActivitiesModel`, `UserSubscriptionsModel`,  and `UserSettingsModel`  ([#11616](https://github.com/oppia/oppia/issues/11616), [#12120](https://github.com/oppia/oppia/issues/12120)) 
- Fixing `CompletedActivitiesModel` and `IncompleteActivitiesModel` to only reference existing and public explorations ([#14968](https://github.com/oppia/oppia/issues/14968)) 
- Fixing `GeneralFeedbackThreadModel` entities with missing related `GeneralSuggestionModel` entities ([#11736](https://github.com/oppia/oppia/issues/11736)) 

Task set 2
- Handling deprecated commands ([#10807](https://github.com/oppia/oppia/issues/10807), [#10820](https://github.com/oppia/oppia/issues/10820)) 
- Fixing `UnsentFeedbackEmailModel` entities with missing `GeneralFeedbackThreadModel`s and `GeneralFeedbackMessageModel`s ([#14966](https://github.com/oppia/oppia/issues/14966)) 
- Fixing `GeneralSuggestionModel` entities that are marked as rejected but are missing their final reviewer ID ([#14967](https://github.com/oppia/oppia/issues/14967)) 
- Fixing `ExpUserLastPlaythroughModel` has a few validation issues ([#14972](https://github.com/oppia/oppia/issues/14972)) 
- Fixing `GeneralFeedbackMessageModel.feedback_thread_ids` to only reference existing `GeneralFeedbackThreadModel` ([#14971](https://github.com/oppia/oppia/issues/14971)) 

**Size of this project:** large (~350 hours)

**Potential Mentors:**  TBA

**Knowledge/Skills Recommended:**

- Apache Beam jobs
- Python
- Responsibility with schedules and good communication, because you will need to coordinate with the Oppia release team to conduct test runs on the backup server, and this can delay the project if not handled responsibly

**Suggested Milestones:**

* **Milestone 1:** Fix all tasks from Task set 1.

* **Milestone 2:** Fix all tasks from Task set 2.

**Dependency on Release Schedule:** The timeline should be arranged so that such jobs can be run and verified during the appropriate release cycle. Note that releases can be delayed by up to a month, and you should account for such delays in your timeline.

**Proposal notes:**

- Make sure to provide example code for a Beam job that you will use to fix one of the issues. We just want to make sure that you've read the Beam job documentation and generally understand how to write Beam jobs.
- You need to have at least one PR that either creates some Beam job or fixes some existing Beam job.
- In your proposal, please explain how you plan to tackle each task from the list above. There are usually two parts to this: (a) making sure that we fix the current issues in our datastore, and (b) ensuring that those issues don’t reoccur in the future (which often requires doing a careful audit to prove that all possible “loopholes” that would allow them to occur have been plugged).
- When designing the Beam jobs to fix existing issues in our datastore, make sure that those jobs only make modifications that are strictly necessary. Be especially careful with updates or deletions, since it is important to avoid any data loss or corruption. For each task, you should also write a verification Beam job that verifies that the changes were correct. You should also manually verify (on a test server) that the job has done the right thing after it is run. Make sure to also explain what the rollback procedure for the job is (if something goes wrong while running it).
- Also, note that, in general, the jobs you write should be designed to be **idempotent**. That is, running them twice should result in the same outcome as running them once (since this allows us to just rerun them if an error happens within the Beam framework).
- In your timeline, make sure that you account for possible delays in the job testing procedure. In particular, note that when you submit the job for testing on the backup server, it might take up to 48 hours to get the results

**Useful resources:**

## Developer workflow team

### 4.1. Dockerize Oppia

**Project Description:**

We want to package Oppia as a Docker container so that new contributors can get started by running `docker-compose up -d` after cloning the repository to install all the dependencies and start the local development server. This will be much easier than the current installation process, which is often painful to troubleshoot. Docker will also let us speed up test runs on GitHub Actions by caching the Docker image.

Requirements:
* Setup should be quick and easy. For example, a user might need to:
  - Install Docker
  - Clone oppia/oppia
  - Run `docker-compose up -d`
* The setup should be independent of the OS or platform it is run on.
* The setup should not exceed the 8GB RAM requirement for Oppia on any platform for which we have supported installation instructions.
* It should be easy for a user to update their installation to the current dependency versions.
* It should be easy to reset the environment, for example if the internet connection fails and so a dependency is only partly installed.
* Developers should be able to run tests, use git (e.g. switch branches, push changes, and checkout commits), and use all the other development tools we document in the wiki. The interface for doing so should undergo only minimal changes.
* Maintainers should be able to easily upgrade Oppia’s dependencies (e.g. change requirements.in to specify updated versions) and check that the local server still works. When those updates are merged into develop, all developers should be smoothly upgraded to the new versions.
* All dependencies must be pinned to a specific version and come from a trustworthy source. We should also verify dependency checksums before installing them.
* All installations should happen via Docker or standard command-line tools.
* Should use Docker compose V2 (since compose V1 has been [deprecated](https://www.docker.com/blog/announcing-compose-v2-general-availability/)).

**Size of this project:** large (~350 hours)

**Potential Mentors:**  TBA

**Knowledge/Skills Recommended:** Applicants should be familiar with Python and have some exposure to Docker.

**Suggested Milestones:**

* **Milestone 1:** The server launch should be successful and all Oppia pages should be functioning correctly.

* **Milestone 2:** All tests should be executed locally and the migration of GitHub actions to utilize docker, including caching of docker images, should be completed.

**Dependency on Release Schedule:** None.

**Proposal notes:**

**Useful resources:**


### 4.2. Developer Workflow Release Dashboard

**Project Description:**

The aim of this project is to create a dashboard for release testers and team leads on the Oppia developer team. The dashboard should be built as a standard App Engine app that supports login. It should show a list of all commits in develop. For each commit, it should show the status of the release candidate (RC) that was built for that commit:
* A link to the RC (note: you can find links at the bottom of runs, e.g. https://github.com/oppia/release-scripts/actions/runs/3987166674).
* Did that RC pass acceptance testing, fail acceptance testing, or get skipped?
* For all RCs that pass acceptance testing:
  - **Prod server**. Show a button next to the deployable RC (if present) to deploy it to prod. An RC is deployable if it is strictly newer (here “newer” refers to commit order, not the timestamp on the commit) than the currently-deployed RC, all CI tests are passing, all acceptance tests are passing, no newer RC meets the preceding deployability requirements (i.e. only the newest RC with passing tests is deployable). Deploying should be restricted to members of the team-leads-and-release-coordinators Google Group or allowlist; when clicked, it should notify that mailing list. The deployed version should be formatted on App Engine as {{tag}}-{{commithash}}, where {{tag}} is the release version (e.g. “3.2.1”).
  - **Test server**.
    - If the RC is currently provisioned on a test server, show a link to that test server.
    - If not, show a button to provision a test server on BrowserStack with this RC. This button should be restricted to members of the release-testers Google Group or allowlist. Once provisioned, it should send an email to the requester and the status in the dashboard should be updated. The deployed version should be formatted as {{tag}}-{{commithash}}, where {{tag}} is the release version (e.g. “3.2.1”).

(Note that the team-leads-and-release-coordinators Google Group will be a member of the release-testers Google Group.)

Pagination should be included to allow paging through multiple pages of commits (50 per page), but it is fine not to go back more than 300 commits or so.

Include full documentation on how to update code, test, and deploy new releases of this app. The app will also need unit tests and linting, and to support easy developer setup.

**Size of this project:** large (~350 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

* Frontend development (probably Angular, but we don’t require that)
* Backend development (probably Python, but we don’t require that)


**Suggested Milestones:**

* **Milestone 1:** Create a new repo for the release dashboard and include setup, update, test and deployment instructions, as well as CI checks that run all the tests and ensure that all code is 100% tested before an update can be merged to develop. The release dashboard should show a table with a paginated list of commits, their release candidates, and their acceptance test statuses.

* **Milestone 2:** For the appropriate release candidates, the release dashboard should have buttons that support deploy-to-prod-server and deploy-to-test-server functionality. These buttons should be correctly access-controlled and should send the appropriate notification emails when clicked.

**Dependency on Release Schedule:**  None.

**Proposal notes:**

Follow existing Oppia design patterns and app conventions, so that the app is easy for the team to maintain. In particular, for authentication, we suggest using Firebase authentication in a similar way to the main Oppia.org app, rather than rolling out a custom username/password system. You should also take care to avoid any security vulnerabilities (e.g. XSS, CSRF). Following Oppia design patterns and conventions will help here, but whether or not you borrow from Oppia, you should make clear what patterns and conventions you will use, and why they are important.

Your app should be independent of the production Oppia deployment at https://oppia.org. This is because if Oppia is broken, we need to be able to access the release dashboard to fix it.

Most important things for the proposal:
- Make a table showing types of notification events received, when they’re triggered, where they’re sent from, what their format is and what the app will do with them.
- Check that you’re able to do the following from an App Engine app, and describe how you would do so in detail. As a bonus, show proof of a working prototype for these that someone can experiment with:
- Receive a notification from GitHub
- Send an email to a given address (can follow what Web does with Mailgun)
- Send a request to trigger a GItHub Action.
- Send a request to provision BrowserStack.
- Get current status from BrowserStack.

Note that this dashboard could also optionally link to, or iframe, [the proposed telemetry dashboard](#43-developer-workflow-telemetry-dashboard), so that team leads have a single point of reference.

The dashboard does not need to meet accessibility guidelines.


**Useful resources:**

### 4.3. Developer Workflow Telemetry Dashboard

**Project Description:**

The aim of this project is to create a public dashboard that anyone on the Oppia developer team can view. This dashboard should show summaries of the following metrics (these are known as the DORA metrics or “Four Keys”), supplemented by charts. In all cases, the horizontal axis represents time, and the options should support both grouping by day and by week.

The following graphs should be shown:
- Failure recovery time (how long it takes us to recover from a failing build in develop – note that this is a bit different from the more standard “how long it takes us to recover from a failing deploy to production”)
- Deploy frequency (how often we cut and deploy a new release to Oppia.org)
- Change failure rate (how often we get a defect in develop)
- Lead time for changes: (how long it takes for a commit to get deployed to Oppia.org)

You can see an example of what this dashboard might look like in the visualization here, but there is no requirement that you use this [library](https://github.com/GoogleCloudPlatform/fourkeys#dashboard).

Also, include full documentation on how to update code, test, and deploy new releases of this app. The app will also need unit tests and linting, and to support easy developer setup.

**Size of this project:** medium (~175 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

**Suggested Milestones:**

* **Milestone 1:** Create a new repo for the telemetry dashboard and include setup, update, test and deployment instructions, as well as CI checks that run all the tests and ensure that all code is 100% tested before an update can be merged to develop. The telemetry dashboard should show at least one chart and summary statistic (of your choice) of the four that are given.

* **Milestone 2:** The telemetry dashboard should show all four metrics, and be added to the Oppia team’s wiki and broadcast to the dev team.

**Dependency on Release Schedule:**  None.

**Proposal notes:**

When coding, try to follow existing Oppia design patterns so it’s easy for other folks on the team to maintain the app in the future.

Most important things for the proposal:
- Would be good to see a comparison of technical options. One of them is [fourkeys](https://github.com/GoogleCloudPlatform/fourkeys) but there may be others (including building from scratch). Note that you can use a library like ApexCharts for the graphs.
- Make a table showing types of notification events received, when they’re triggered, where they’re sent from, what their format is and what the app will do with them.
- If you can, try to show proof of a sample prototype set up and working with data from some other repository. This would be helpful since the documentation for how to get these metrics (e.g. in the fourkeys [README](https://github.com/GoogleCloudPlatform/fourkeys/blob/main/README.md)) is already pretty good (though we still ask that you explain your approach clearly so that we can check that you understand what you’re doing).

**Useful resources:**

### 4.4. Make CI faster

**Project Description:**

The broad aim of this project is to get the CI tests to run in under 1 hour so that PRs can be merged into develop quicker. This entails several steps:

- Get the pre-push tests (that run on the developer’s local machine) to run in under 5 minutes:
  - Audit backend unit tests to see which ones take a long time, and refactor those to avoid network/database/disk-access calls in order to shorten their runtime (while still testing what they need to).
  - For long backend unit tests that need to be long because they are creating a lot of data to test scalability, add them to a “scalability” list of tests that doesn’t need to get run during pre-push.
  - Run only the lint, MyPy, and typescript checks; karma tests; and backend unit tests that were affected by files changed since the last push.
  - (If possible) On pre-push, shorten the build step or remove it altogether.
- Get the CI checks to run in under 1 hr wall time (i.e. including parallelization):
  - Create a single environment at the start that gets used for all other tests. (In particular we currently seem to be running the “install third party deps” step repeatedly, so it might be good to cache folders like oppia_tools.)
  - Create a build artifact that gets reused in all workflows. (Currently, build artifacts can’t be persisted across workflows, but this GitHub action for uploading to GCS might be helpful.)
  - Run the full versions of all pre-push tests (mentioned above) first, and block other tests on these. (If any of the pre-push tests fail, then do not run the other CI checks.)
  - For long-running tests:
    - If the test is essential, find a way to make it shorter.
    - If it is not, remove it from CI and put it in an acceptance layer that only runs on some release-candidate builds (see below).
- Split off less-important long-running tests into acceptance tests:
- Create a GitHub Action that, at regular time intervals, takes the latest release-candidate build on develop that passes all CI checks, runs the acceptance tests on them. Builds that pass all acceptance tests should have a public, machine-readable indication that they did, and builds that cause an acceptance test failure should result in an email or chat notification to the CI Stability team.

**Size of this project:** large (~350 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:**

* Familiarity with GitHub Actions and workflows.
Clear understanding of the current Oppia pre-push and CI pipeline.

**Suggested Milestones:**

* **Milestone 1:** CI checks run in under an hour. Less important tests are split off into an acceptance layer.

* **Milestone 2:** Pre-push checks run in under 5 minutes.

**Dependency on Release Schedule:**  None.

**Proposal notes:**

* See the [GSoC idea doc](https://docs.google.com/document/d/1pIAu06LJS39BUeRyPZVWFYSW9aIKDrA_z7uoNtzoe9I/edit#) and the PRD linked there for more details.

**Useful resources:**

### 4.5. Normalize Usage of Feature Flags

**Project Description:**

The aim of this project is to normalize the usage of feature flags (implemented using [platform parameters](https://github.com/oppia/oppia/wiki/Developing-new-features-with-feature-gating)) in Oppia’s deployment process. At the end of the project:

- The feature flags dashboard should be moved from /admin to /release-coordinator, and be made more intuitive. (The current UI is not intuitive at all – it’s quite unclear what to do.) The common case of switching a boolean flag on and off should be easy for developers to do.
- Feature flags should support rollbacks. There seems to be an [issue](https://github.com/oppia/oppia/issues/16416) with rollbacks not being correctly captured that should be diagnosed and fixed.
- Extend the current functionality to allowlist specific usernames for external trusted tester programs.
- Ensure the documentation is sufficiently complete so that developers are used to creating feature flags for new features, and have no questions about how to do so.

**Size of this project:** medium (~175 hours)

**Potential Mentors:** TBA

**Knowledge/Skills Recommended:** Python and TypeScript

**Suggested Milestones:**

* **Milestone 1:** The feature flags dashboard is moved from /admin to /release-coordinator. It is also made more intuitive; in particular, the common case of switching a boolean flag on and off is easy for developers to do.  Feature flags support rollbacks (see [#16416](https://github.com/oppia/oppia/issues/16416)).

* **Milestone 2:** Feature flags support allowlisting specific user IDs for external trusted tester programs. The documentation for handling feature flags is fully complete and developers use feature flags as a matter-of-course, without any issues.

**Dependency on Release Schedule:** None (unless you propose using beam jobs).

**Proposal notes:**

See "launching new features" page on wiki:
- [Launching new features](https://github.com/oppia/oppia/wiki/Launching-new-features)
- [Developing new features with feature gating](https://github.com/oppia/oppia/wiki/Developing-new-features-with-feature-gating)

In general, features should start out in the DEV FeatureStage. When the functionality is complete, they should be moved to the TEST FeatureStage (and the test servers, but not oppia.org, should accept features in the TEST FeatureStage). When release testing completes and the feature is cleared for full launch, a single PR should be created to flip the TEST flag to PROD, which will enable it to run on oppia.org in the next prod release of the app.

The feature flags UI is typically used for (a) boolean feature flags on Web, (b) platform parameters needed to give signals to the Android app. It may be worth having different simplified UIs for these two common cases as well as the more generic UI at the very bottom, all of which should work the same way “under the hood”.

Issue #16416 might be due to a caching issue where feature flags aren’t properly cleared from users’ caches when reset.

For supporting specific user IDs for external trusted tester programs, it should be possible to define groups of users (managed by username, but stored in the datastore using user IDs) and then have the flag be something like “if the user is in this group, enable the feature”.

**Useful resources:**
