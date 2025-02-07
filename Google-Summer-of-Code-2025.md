**Important**: _We are making some changes to how we run GSoC for 2025. Please read this page carefully, since some things have changed from previous years._

## Table of Contents

- [Getting started](#getting-started)
- [FAQs](#faqs)
- [Dates and Deadlines](#dates-and-deadlines)
- [Types of work related to Oppia projects](#types-of-work-related-to-oppia-projects)
- [GSoC proposal template](#gsoc-proposal-template)
  - [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan)
  - [What should applicants expect from mentors in a proposal review?](#what-should-applicants-expect-from-mentors-in-a-proposal-review)
- [Selection Criteria](#selection-criteria)
- [Communication](#communication)
- [Oppia's Project Ideas List](#oppias-project-ideas-list)

Oppia is planning to participate in [Google Summer of Code 2025](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers post-secondary students, as well as newcomers to open source, an opportunity to discover and work with open source organizations. The contributions are supported by a stipend. Contributors work closely with one or more mentors to implement either a project idea by the organization, or a proposal of their own.

In order to receive updates about GSoC at Oppia, please subscribe to the [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce) mailing list, as well as the [Developer Announcements](https://github.com/oppia/oppia/discussions/categories/developer-announcements) category on GitHub Discussions.

This year, based on previous years' feedback, Oppia plans to follow a slightly extended GSoC timeline: projects will have 7 weeks for each milestone, with an additional "holiday week" between the milestones. Each milestone includes 5 weeks of coding time, 1 week for evaluations, and 1 week for fixes, as well as a product demo session after the 4th coding week. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below for more details.

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by a global community dedicated to making meaningful social change, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions here ([Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)).


## Contributors

GSoC is an excellent opportunity for new contributors to get paid to work on an open source project. If you're interested in applying as a contributor, we strongly recommend reading this entire wiki page, including our [FAQ](#faqs) which answers many of the common questions we receive.

You should also definitely read the following resources:
  - [Google Summer of Code contributor guide](https://google.github.io/gsocguides/student/)
  - [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
  - [Google's GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)

Furthermore, note that GSoC isn't just about code -- it's also about communication and interaction with the open source community! Hear what some of our previous contributors have to say:

  - _I learnt a lot from this organisation -- tackling a huge codebase, writing clean and efficient code and communication._
  - _I learn a lot of things in Oppia which I didn't learn in my school and college. It's not necessary that only a software engineer can contribute, anyone can contribute to Oppia with his/her skill._
  - _I like the fact that the maintainers are so sincere in their work and are very responsive._
  - _Oppia Foundation is really awesome and I get to interact with amazing people and learn a lot. The best part is that everything is organised really well and that makes it easy to solve my issues._
  - _The Oppia Foundation excelled in fostering a supportive and inclusive environment for contributors. The responsiveness of the mentors and the community was remarkable, making it easy to seek guidance and get help whenever needed. The clear communication, structured processes, and well-documented codebase greatly helped my learning and development throughout GSoC._
  - _I really enjoyed the process, and the feeling of owning a feature end-to-end is fantastic, even with the challenges. Over the past three months, I've learned a lot about feature testing, release testing, PM demos, and more._

You might also enjoy the "weekly journals" from some of our previous contributors: **[Rd4dev](https://medium.com/@rd4dev)** and **[@theMr17](https://medium.com/@Mr_17)**.


## Getting started

Welcome! If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list and the [Developer Announcements](https://github.com/oppia/oppia/discussions/categories/developer-announcements) category on GitHub Discussions, so that you can receive important notifications about Oppia's participation in GSoC. Make sure to set your preferences correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is about:
    - Read the [user documentation](http://oppia.github.io/#/) to become familiar with important concepts like explorations and interactions.
    - Play some lessons on [Oppia.org](https://www.oppia.org/learn/math), which hosts a live instance of Oppia.

3. To get started with development, read and follow the instructions in the contributors' guide carefully ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Oppia Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)). If you're interested in Oppia Web, you might also find [these tutorials](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#developing-your-skills) helpful.

4. Do a few starter projects to become familiar with the contribution process. This will help us get an idea of what it's like to work with you. It will also help you get a better understanding of the codebase and our development process, which may help with writing a good project proposal. Once you've merged at least 2 pull requests, you will get an invitation to become a collaborator to the Oppia repository and be officially onboarded! **This step is a prerequisite to applying for GSoC.**

> [!NOTE]
> You must be onboarded to the repository to which you will contribute during GSoC. For example, to work on an Oppia Web GSoC project, you need to be onboarded to the oppia/oppia repository, which means that your 2 pull requests need to be to oppia/oppia.

> [!TIP]
> Quality is more important than quantity, so try to contribute to high-impact issues where possible. Also, we want to see examples of your best work, so please make sure to read the [["getting started" guide|Contributing-code-to-Oppia]] and [[PR instructions|Rules-for-making-PRs]] carefully, follow the [tips for success](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#tips-for-success), manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [[style rules|Coding-style-guide]], and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Select one or more [GSoC project ideas](#oppias-project-ideas-list) that you're most interested in, and write your project proposal! You can get feedback from project mentors when you've completed a sufficient draft -- see the instructions in the [GSoC proposal template](#gsoc-proposal-template) section for details.

   We require that all general discussion about GSoC projects take place in open channels. If you have questions about a project, you can ask in [GitHub Web Discussions](https://github.com/oppia/oppia/discussions/categories/gsoc-2025-q-a) or [GitHub Android Discussions](https://github.com/oppia/oppia-android/discussions/categories/general-gsoc-q-a). Note that individual projects have their own categories, so please use those if you have project-specific questions. Please also be specific when asking questions, since this makes it easier for us to help you.

> [!TIP]
> During the application period, your first goal should be to figure out how to become an effective contributor. Start developing your project proposal only once you have experience getting some PRs merged. This will give you a much better idea of what you want to work on, and how much you can accomplish.

Good luck!


## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: Please see the individual project ideas to determine which skills are recommended for the project in question. Also, in general:

   - For Oppia Web, Angular 2+, Python 3.9, Google App Engine and Apache Beam are useful and recommended, and experience with Docker and GitHub Actions is useful for developer workflow projects. Also, it is important to be able to write tests for the code you submit (using Karma, Webdriverio and unittest). You might also find this [[page of learning resources|Learning-Resources]] helpful, as well as other pages on our [wiki](https://github.com/oppia/oppia/wiki) that provide guidance on Apache Beam, testing frameworks, etc.

   - For Oppia Android, you will need to know how to program in Kotlin, and have experience with Android development. Knowledge of Bazel may also be helpful for some projects.

   - Note that, although GSoC is aimed at both students and beginner contributors to open source, "beginner to open source" is **not** the same as "beginner to coding" -- the projects do assume that you have some proficiency with coding. The fact that GSoC projects produce high-quality code that solves real problems for open-source projects does make GSoC challenging, but this is also part of what makes GSoC such a valuable experience for students.

**Q: How can I increase my chances of getting selected?**

A: The most important thing is to ensure that you have the required skills for the project -- see the "Required Skills" section of the [proposal template](#gsoc-proposal-template) for more details. Aside from that, writing a good project proposal with a solid solution approach, engaging with the community, helping other contributors, successfully contributing PRs for high-priority issues, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: Probably not. We have not had good experiences offering flexibility in previous years, so this year, Oppia will strictly adhere to the Oppia GSoC timeline. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below, and avoid taking up major commitments alongside GSoC. Experience from previous years suggests that you will be unlikely to successfully balance both.

**Q: I do not have any experience in skill XYZ. What should I do?**

A: If you are missing a skill that is needed for a project, we recommend trying to learn it -- in software development, it is common to develop experience and expertise as you take up and complete projects successfully. Some ways to do this include working on issues that give you a chance to develop that skill, referring to our wiki documentation, and following tutorials from elsewhere on the Web. Please note that, in general, we are unlikely to accept applicants who lack the required skills for a project, since this tends to result in significant difficulties during the coding phase.

**Q: How will you assess whether I have the required skills for a project?**

We will assess your application based on your proposal and the skills that you have demonstrated in your PRs and other interactions with the community. Please see the guidance in the "Required Skills" section of the [proposal template](#gsoc-proposal-template), which explains how to demonstrate that you have the required skills for a project, and provides pointers on how to develop those skills.

**Q: Is it okay if I only focus on the frontend or backend?**

A: This probably depends on the project(s) you wish to apply for. However, note that most projects are full-stack and require ability in both the frontend and backend. We recommend becoming familiar with both of these, since this will open up more opportunities for you, as the projects we work on at Oppia often touch multiple layers of the stack.

**Q: What is the minimum number of PRs that one should have?**

A: You should have at least 2 merged PRs. Beyond that, remember that quality is more important than quantity, so consider taking some high-priority or ["impact: high"](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22Impact%3A+High%22) issues if you're able to, since those fixes are more valuable. You can find a list of high-priority issues on the respective teams' project boards: [LaCE](https://github.com/orgs/oppia/projects/3/views/8), [Dev Workflow](https://github.com/orgs/oppia/projects/8/views/11), [Contributor Dashboard](https://github.com/orgs/oppia/projects/18/views/4), [Android CLaM](https://github.com/orgs/oppia/projects/4/views/3), [Android Dev Workflow](https://github.com/orgs/oppia/projects/10/views/1). Additionally, you'll also want to demonstrate that you have the required skills to successfully complete your chosen project; please see the guidance in the "Required Skills" section of the [proposal template](#gsoc-proposal-template), which explains how to do this.

**Q: Will I be penalized during selection if I ask for help while contributing?**

A: Not at all! Asking for help when you need it is part of the learning process, and the Oppia open-source community is more than happy to help and onboard new members. Please just ensure that your questions are well-formed and that you (a) have read the relevant docs on the wiki, (b) provide the necessary information (such as a [debugging doc](https://github.com/oppia/oppia/wiki/Debugging-Docs)) to help responders understand what you've figured out so far and where you are stuck.

**Q: I only discovered Oppia recently. Does this mean that, during selection, my application would automatically be ranked lower than those by other applicants who have a longer tenure with Oppia?**

A: Definitely not! Here are the [selection criteria](#selection-criteria) we use when selecting contributors for GSoC. Note that tenure is explicitly not part of these criteria.

**Q: How early should I start working on the proposal?**

A: We recommend developing your project proposal and engaging with the community as early as possible, so that you have enough time to get feedback from mentors and improve the proposal before the submission deadline. Make sure to follow all instructions in the [proposal template](https://docs.google.com/document/d/1BIvB0Pt_KCAD17wFS1viOTfZiehBuEJOO1GeypezdkY/edit) (especially around sharing and access) to reduce delays in reviewing your proposal. That said, it's important to note that the proposal is only one part of the application process, and it is probably more important to figure out how to become an effective contributor by getting some PRs merged and demonstrating that you have the required skills for the project.

**Q: Can I submit more than one proposal to Oppia?**

A: Yes, you can. However, we strongly recommend picking one project and writing a solid proposal for it. Splitting attention across multiple projects might not be a great idea. (That said, GSoC is offering projects of multiple lengths, and if you're interested in doing either the 'full version' or the 'half version' of a project idea that can support both modes, you can submit **both** the 'full version' and the 'half version' as separate applications. Just make sure that you'd be happy with either outcome if you are selected!)

**Q: Can I use content from the project ideas list or PRD in my proposal?**

A: It is fine for proposals to draw from the GSoC idea in the wiki and any linked PRDs. However, please note that if you copy content directly from any source (even if it is an Oppia doc), **you must cite and link to the original source**. Also, remember from our [selection criteria](#selection-criteria) that when we review proposals, one of the things we look for is evidence that the applicant understands the project and existing codebase well. Strong proposals will therefore contain details that are original (e.g. that are not copied from the PRD).

**Q: I'm part of team X in Oppia. Can I submit a proposal for a project idea from a different team?**

A: Yes, you can; there are no issues with that. There is a space in the proposal template to list teams at Oppia you've participated in, and we will get feedback from members of those teams about what their experience of collaborating with you has been like.

**Q: What is the total number of contributors that will be accepted?**

A: We generally request slots for as many projects as we think will succeed. However, the Google GSoC admins may impose limits based on how they decide to distribute contributor slots among the different open-source organizations.

**Q: Which projects are most important for Oppia?**

A: All the projects we've listed in the [Ideas List](#oppias-project-ideas-list) are important, and we'd be very happy to see good progress made on any of them! Projects are treated as equally important during selection; note that the relative importance of a project to Oppia is not part of the [selection criteria](#selection-criteria). We strongly encourage you to pick a project that you'd enjoy doing over the summer!

**Q: The [Google GSoC FAQ](https://developers.google.com/open-source/gsoc/faq#can_someone_already_participating_in_open_source_be_a_gsoc_contributor) mentions that the program is only for new contributors. I have already contributed to Oppia and I have write access. Can I still participate?**

A: The GSoC program is open to students, as well as beginner contributors to open source. If you do not qualify as a student, see [this FAQ](https://developers.google.com/open-source/gsoc/faq#how_do_i_know_if_i_am_considered_a_beginner_in_open_source_development) on the GSoC website for whether you would be considered a beginner.

**Q: I'd love to contribute to open source, but I'm not sure I have enough time during the summer to do a GSoC project. Can I still help out?**

A: Yes, GSoC is probably not the best choice if you don't have enough time during the summer, since it requires focused commitment. However, you can still start contributing to Oppia by following the instructions in the contributors' guide ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Oppia Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)).



## Dates and Deadlines

Noteworthy dates for 2025 (see also the [Official GSoC Timeline](https://developers.google.com/open-source/gsoc/timeline)):

- **Jan 27 - Feb 11**: Mentoring organizations apply
- **Feb 27**: Mentoring organizations are announced
- **Mar 1**: [GSoC Q&A session with Oppia](https://calendar.app.google/5jPfYs3oaoy2o8zx8)
- **Mar 24 - Apr 8**: GSoC contributor application period
- **May 8**: Accepted GSoC contributors are announced
- **May 8 - June 1**: Community bonding ("greenlight") period
- **June 2 - Jul 18**: Milestone 1 work period for GSoC
  - **Jul 4**: Milestone 1 work due for internal evaluation
  - **Jul 5 - Jul 11**: Testing of the milestone 1 work product
  - **Jul 12 - Jul 18**: Buffer time for Milestone 1 revisions
  - **Jul 19 - Jul 25**: Official GSoC midpoint evaluation
- **Jul 26 - Sept 12**: Milestone 2 work period for GSoC
  - **Aug 27**: Milestone 2 work due for internal evaluation
  - **Aug 28 - Sept 3**: Testing of the milestone 2 work product
  - **Sept 4 - Sept 10**: Buffer time for Phase 2 revisions
  - **Sept 15 - Sept 22**: Official GSoC mentor evaluation due
- **Sep 23**: GSoC period at Oppia officially ends

**Note!** For Oppia's participation in GSoC 2025, the coding period dates are strict, and we will not be offering extensions. Please ensure that you have sufficient time during the summer to work on your projects.



## Types of work related to Oppia projects

The Oppia team is committed to making GSoC an enriching educational experience for contributors. In general, our goal for GSoC is for contributors to have a really meaningful experience, and to do something worthwhile over the summer that they can look back on with pride.

In order to ensure a well-rounded engineering experience, GSoC contributors will have the opportunity to do some or all of the following, depending on their project:

- Write design documents for technical projects
- Read and understand parts of the codebase related to their project
- Receive code reviews for all code they write for their project
- Develop user-focused, responsive and internationalized UIs.
- Write automated tests for their projects
- Meet regularly with other contributors on their Oppia development team (LaCE, Contributor Dashboard, Dev Workflow, Android)
- Meet 1:1 with their mentors regularly to get developmental feedback
- Give presentations and demos of their projects
- Get personalized feedback on their project from the product team or a technical lead
- Learn how to do code reviews

We've also asked our previous GSoC contributors what specific things they learned during their GSoC projects. Here are their collated answers:

- Technical ability and domain knowledge
  - Writing maintainable and readable code.
  - Building an entirely new feature in a scalable way.
  - Writing better automated tests.
  - More confidence working with Angular.
  - Making better design, UI and technical decisions.
  - Getting a better understanding of overall full-stack development.
  - Enhanced ability to debug and resolve technical issues.
- Technical leadership skills
  - How to manage my time well, and how to achieve deadlines.
  - Improved skills in managing and executing projects.
  - How to give, respond to and understand reviews.
  - How to effectively convey ideas.
  - How to write a good project proposal.
  - Becoming a better developer, not only in terms of technical skills, but also in thinking of actual application of the built product and the edge case scenarios that the user might face.
- Communication and personal development
  - How to seek help when needed and overcome challenges.
  - How to reach out to people, work with them, and help solve each other's problems.
  - How to get myself unblocked.
  - Putting forward my thoughts more systematically so that others can understand me well.
  - Feeling more confident while joining online meetings.

Contributors have also told us why they continue to stay engaged with the project after GSoC ends:

- Community
  - It is really an awesome experience working with some amazing folks from all around the world at Oppia.
  - The organisation is active and has a strong community bond.
  - The kind of support the complete community provides is extraordinary.
- Giving back
  - The main reason to stay connected is the purpose the community serves. Providing education to those who do not have access to it helps me give back to the society.
  - It makes me very happy that I'm part of an organization which provides free education and I think the education is the biggest blessing we can give to one to make them stand on their feet.
  - I would love to be part of this org by knowing that maybe not much but yes I'm trying to make an impact and my contribution in the educational field. I really want to do this because where I come from there is not much of education.

- Growth / learning:
  - I like working in Oppia since it not only helps me improve my coding skills but also helps me grow as an individual.
  - Working with Oppia has really helped me grow as a developer and I would really like to stick around to gain even more experience of real world software development.
  - I feel my exponential growth while contributing in Oppia and got to learn many new things while getting help from mentors and other Oppia team members.
  - The kind of work that Oppia does is really inspiring and there are a lot of opportunities to improve your skills be it be technical skills or leadership skills and most of all the people at Oppia are really fun to work with :)


## GSoC Proposal Template

When submitting a proposal, please use the provided GSoC proposal template. We will only consider proposals submitted using this template. Note that there is a length limit: the proposal's technical "HOW" section should not exceed 20 pages at "Roboto 10" font size.

**Note:** There's **no** formal minimum length requirement for your proposal. The quality of what you write is much more important than the amount of text you write, and we encourage you to write **shorter** proposals that still convey the main aim of the project.

(**NOTE:** The link to the 2025 template will be posted soon. **It will differ from the 2024 template.** We will post instructions together with the template.)

**Some important notes:**

1. Your proposal must be **original** (see section 2.4 of the [Contributor Participation Agreement](https://summerofcode.withgoogle.com/terms/contributor)). During the selection process, proposals that are found to have passed off others' work as their own will automatically be disqualified. If you include any text in your proposal that is copied from the Internet or other sources (even if it is an Oppia doc), you **must** provide a link or reference back to the source. Note that you must attribute sources even if you paraphrase (i.e. re-write their content in your own words). In cases of doubt, we would encourage you to err on the side of citing your sources (since not doing so may be construed as plagiarism).

2. When the necessary criteria for requesting a review are met, add gsoc-2025-mentors@oppia.org as an editor for your proposal doc. (This makes some workflows, like inviting PMs or fixing typos, etc., easier, but if you're concerned about changes to your doc, then you can [turn on notifications for edits](https://support.google.com/docs/answer/91588?hl=en&co=GENIE.Platform%3DDesktop).) After fixing the sharing settings, make a new post in the correct "proposal reviews" category in [GitHub Discussions](https://github.com/oppia/oppia/discussions) that is clearly titled with the name of the project that you are requesting a review for, and provide a link to the doc in your post.

   Please use only the above channel for proposal reviews: all proposal-related communication should happen through GitHub Discussions or directly through comments in the proposal doc. **Do not** send proposals directly to individual GSoC mentors.

   You can also request **at most one** "tech lead review" for **at most one** of your proposals during the pre-selection phase. To keep things fair, the tech lead will do only a single pass on your proposal and leave comments, but is not required to follow up on replies to those comments. Since you can only request a tech lead review once (per applicant), we recommend doing so after you have gotten feedback from mentors and completed a full draft of your proposal, but at least a week before the due date. Tech leads will process requests in the order they are received. To request a tech lead review, fill in [this Google Form](https://forms.gle/oGnj56rHNbNCWmBr6).

3. Your final proposal should be self-contained. In particular, to be fair to all applicants, key components of the proposal should not be editable after the deadline. Don't assume that reviewers will follow external links.


### Tips for writing a good project plan

Here's some advice about proposals and milestone timeline planning that we collated from previous contributors and mentors:

- **Choose a project you're interested in!** If you have a strong interest in your project, this might make it easier for you to pick up the necessary skills and tackle unforeseen difficulties that may arise during GSoC.
- **Familiarize yourself with the technologies for your project and the relevant part of the codebase.** Reviewers will want to see that you understand how to integrate your project with the current Oppia structure — don't design in a vacuum.
- **Define milestones with enough detail to get a proper ETA.** For example, don't just say "write e2e tests", otherwise you risk significantly underestimating the timeline.
- **Communicate and present your ideas clearly.** Your proposal should show that you have a good understanding of the codebase and the final goal of the project. For example, in a user-facing proposal, don't just make a list of files that need to be changed; you should also show detailed mocks and user flow diagrams that demonstrate a clear understanding of the requirements.
- **Limit proposal length.** A lengthy proposal is not necessarily better. In fact, adding large amounts of unnecessary detail can sometimes obscure the main points you are trying to get across.
- **Pick a project idea that is within your limits to tackle.** Make sure that what you're proposing is within your capabilities.

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

To select contributors for GSoC, we will evaluate candidates based on a set of criteria designed to ensure we select individuals who not only possess the necessary skills but also demonstrate the ability to contribute effectively to the project. The criteria are as follows, listed in order of significance::

- **Primary Criterion: Required Skills for the Project** - This is the most critical factor in our selection process. A contributor must have the necessary skills for the project. Lack of these skills is a deal-breaker and can lead to immediate rejection of the proposal.

- **Secondary Criteria** (of equal importance):
    - **Quality of the Submitted Proposal** - This criterion helps us gauge the applicant's understanding of the project requirements. The proposal should align with project goals, and be clear, thorough, and feasible.
    - **Prior Experience Working with the Contributor** - We consider our previous interactions with the contributor, focusing on their reliability, communication skills, independence, initiative, responsiveness, and willingness to assist others. This assessment allows us to predict how well the contributor will integrate with the Oppia developer community and contribute to the success of the project.

We believe that strong performance in these dimensions is likely to correlate well with the contributor having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the GSoC program.

For the proposal, we generally look for a clear indication that the contributor has a good, clear understanding of the project, and has broken it down sufficiently well, in a way that makes it very likely to succeed. Some indicators that could help with this include:

- Clear, unambiguous communication. (This is important; your proposal will be read by many mentors!)
- A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating a simple, intuitive experience for end users.
- A proposed solution approach which is sufficiently concrete and which demonstrates that the applicant has a good understanding of both the scope of the problem and the existing codebase.
- A description, if applicable, of how the applicant plans to mitigate risks that could potentially derail the project.
- A concrete, specific description of each milestone, together with a breakdown of the necessary work.


## Communication

If you have questions pertaining to "how to get started with Oppia" or any other queries regarding GSoC at Oppia, please ask them on **[GitHub Discussions](https://github.com/oppia/oppia/discussions)**. Please be specific when asking questions; this makes it easier for us to help you. Also, please make sure to read the relevant "getting started" wiki page ([Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)) first, since the answer to your question might already exist there!

To receive important announcements and updates about GSoC at Oppia, please subscribe to the **[Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce)** mailing list, and the [Developer Announcements](https://github.com/oppia/oppia/discussions/categories/developer-announcements) category on GitHub Discussions.

## Oppia's Project Ideas List

_**Note:** If you're coming to this section from an external link, please make sure to scroll up and read this entire wiki page carefully, not just this section. There's a lot of useful information on the rest of the page, including a FAQ and a section describing selection criteria. Thanks!_

The following is a list of Oppia's 2025 GSoC project ideas. You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community beforehand in order to get feedback and guidance to improve the proposal. We'd also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

Please note that the list of project ideas below is not set in stone: more projects may be added later, and some project descriptions may also change a bit, so check back regularly. In addition, the mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted. (If you want to see what changes have been made to this page since you last viewed it, you can use the [History tab](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2025/_history).)

If you need clarification on any of these ideas, feel free to open a thread in GitHub Discussions following the process in [this guide](https://docs.google.com/document/d/1jt8_pKcrbsc0xHgUEa0Wh8i6imxYmZiB_2QjDmH7ODg/edit?tab=t.0).

### Learner and Creator Experience (LaCE) team

1.1. [Clean up the structure for study guides and worked examples](#11-clean-up-the-structure-for-study-guides-and-worked-examples)

1.2. [Fix the most common server errors](#12-fix-the-most-common-server-errors)

1.3. [Lesson player redesign](#13-lesson-player-redesign)

### Contributor Dashboard team

2.1. [Show AI-powered translation suggestions to translation submitters](#21-show-ai-powered-translation-suggestions-to-translation-submitters)

### Developer Workflow team

3.1. [Acceptance tests](#31-acceptance-tests)

3.2. [Consolidate entity migration jobs](#32-consolidate-entity-migration-jobs)

3.3. _This project idea is still in development and will be added shortly._

### Android team

4.1. [Flashbacks](#41-flashbacks)

4.2. [Platform parameters dashboard](#42-platform-parameters-dashboard)

4.3. _This project idea is still in development and will be added shortly._


## Learner and Creator Experience (LaCE) team

### 1.1. Clean up the structure for study guides and worked examples

**Project Description:**

Currently, topics in Oppia contain a list of skills to teach. These skills are grouped into subtopics (like ['Basic Concepts of Division'](https://www.oppia.org/learn/math/division/revision/basic-concepts)), each with its own study guide (or 'subtopic page' in the backend; note that these were previously known as “revision cards”). Subtopic pages are currently implemented as a single rich-text editor (RTE) field, but this results in their being too lengthy to translate, and the content doesn't look good.

We would like to instead split this RTE field into multiple heading/content parts, both to make it easier to translate each subtopic page in stages and also to improve the display for learners. In the example above, the updated subtopic page would have two sections: "What is division?" and "Parts of a division equation". In the subtopic page editor, each of these sections would have its own text field (for the heading) and RTE field (for the content).

Additionally, both skill explanations and subtopic pages should be able to include worked examples, but worked examples were incorrectly implemented as an explicit subfield of the SkillContents object that is contained in the Skill model. Experience has shown that worked examples would be better implemented as a general rich-text component instead, since this gives more flexibility in where they are placed and allows them to be used in other contexts like the subtopic pages.

The aim of this project is therefore to clean up the incorrect modelling described above and fix the representation of subtopic pages and worked examples, while also ensuring that they can be easily translated. We should also ensure that the user flows for creating and learning from subtopic pages and worked examples are solid, following the proposed [design mocks](https://www.figma.com/design/1e1pq5PSoiULZqM4zvVNY0/Oppia-%23136-Incorporate-worked-examples-in-the-learning-experience?node-id=0-1&p=f&t=a47Jd68ycVXdkjdM-0).

Links to PRD and mocks:
- For subtopic pages (study guides): https://www.figma.com/design/qIT6EvVeyLo2dDuQyR5xzC/Oppia-_-RTE?node-id=0-1&p=f&t=bfOaBMxVrGuWd7mF-0
- For worked examples: [PRD: Incorporate worked examples in the learning experience](https://docs.google.com/document/d/1QrqTsR1Ew3WfQvj7D83mh0k9HjW6xQ-2dpJGkbe8XqY/edit#heading=h.s68z2sezulra)
- Design thread for subtopic pages: https://github.com/oppia/design-team/issues/60
- Design thread for concept cards and worked examples: https://github.com/oppia/design-team/issues/136

**Tracking issues**: [#18305](https://github.com/oppia/oppia/issues/18305), [#19851](https://github.com/oppia/oppia/issues/19851)

**Not in scope:**
- Implementing new rich-text components other than "Worked Example".
- Implementing the "Words to know!" and "Otter Tip!" sections in the [revision card Figma mocks](https://www.figma.com/design/qIT6EvVeyLo2dDuQyR5xzC/Oppia-_-RTE?node-id=0-1&p=f&t=bfOaBMxVrGuWd7mF-0).
- Enabling the use of worked examples in hints and feedback. (We will do this later once we have tried out the functionality in subtopic pages and skill descriptions.)
- Implementing the more detailed validation described in the PRD (for limiting the number of worked examples to 2 if there are no images, or limiting them to 3 if there are images). For now, we will go with a general limit of 2.

**Size of this project:** Large (\~350 hours)

**Difficulty**: Moderate/Hard

**Potential mentors:** @kevintab95

**Product Clarifier:** @seanlip

**Technical Clarifier:** @kevintab95

**Required knowledge/skills:**
- General
  - Figure out the root cause of an issue and communicate it well using a debugging doc.
  - Debug and fix CI failures/flakes.
- Web:
  - Write Python code with unit tests.
  - Write TS + Angular code with unit tests.
  - Write or modify e2e/acceptance tests.
  - Write or modify Beam jobs, with tests.

**Related issues:**
- [RTE-related issues](https://github.com/orgs/oppia/projects/3/views/8?sliceBy%5Bvalue%5D=Creators%3A+RTE+bugs)
- [Validation (backend + frontend)](https://github.com/orgs/oppia/projects/3/views/8?sliceBy%5Bvalue%5D=Data+validation)
- [Translation-related issues](https://github.com/orgs/oppia/projects/18/views/4)

**Suggested Milestones:**
- **Milestone 1**: Create a new `study_guide_sections` field in SubtopicPageContents that is a repeated JsonProperty consisting of (heading: str, content: RTE) pairs. Then, carry out a migration that converts the existing `subtitled_html` field into the new structure, which should be a single-element list with one item whose heading is the revision card’s title, and whose body is the existing RTE content.

  Store the written translations for subtopic pages in EntityTranslationsModel instead of within the SubtopicPage object, similar to the migration that was done for the correspondingly-named field in explorations a few years ago. Also, introduce a unique content ID for each translatable field, similar to explorations. (This should be a relatively easy migration because there are no translations for SubtopicPages yet, but you will need to figure out the new structure and fix the "plumbing".)

  Update the editor UI for subtopic pages to accommodate the new structure, and the learner UI to use an improved display for the revision cards based on [these mocks](https://www.figma.com/design/qIT6EvVeyLo2dDuQyR5xzC/Oppia-_-RTE?node-id=0-1&p=f&t=bfOaBMxVrGuWd7mF-0), with clearly-indicated headings for each of the sections. Finally, deprecate the old `subtitled_html` field.

  Suggested PM demo points:
  - Editor UI for revision cards is complete
  - Learner UI is complete

- **Milestone 2**: After verifying that the existing `worked_examples` fields are empty in production, carry out a schema migration to safely deprecate the `worked_examples` field in the `skill_contents` part of the SkillModel, and remove it from the skill editor UI as well.

  Implement a new 'Worked Example' RTE component that appears only in the skill explanation and subtopic page RTEs, and add acceptance tests for its use. Verify that the learner and creator user flows involving this RTE component are working smoothly and that the user experience aligns with [these mocks](https://www.figma.com/design/1e1pq5PSoiULZqM4zvVNY0/Oppia-%23136-Incorporate-worked-examples-in-the-learning-experience?node-id=0-1&p=f&t=a47Jd68ycVXdkjdM-0). Forbid skill descriptions from having more than 2 "worked example" components. Ensure that this component is translatable in the contributor dashboard, and update the [translation guide](https://docs.google.com/document/d/17jMFtfHVWtJYrzyGQUKdsRXgky7lWv76sGYLOxSbA5w/edit?tab=t.0#heading=h.5mvcuwerfyif) to include an explanation of how to translate worked examples.

  Suggested PM demo points:
  - A worked example RTE component can be created, and used within a broader context (such as a study guide section or a skill explanation).


**Org-admin/tech-lead commentary/advice:**

This is an interesting and high-impact project that “has a little bit of everything”, and that should give you a good understanding of the overall Oppia stack. There is very little in the way of completely new functionality here; almost all the parts of the project have some existing precedent in the codebase.

If you tackle it, it is important to have a good understanding of the systems involved. Make sure you are familiar with Beam jobs, since these will be important.

<details>
<summary>What we are looking for in proposals:</summary>

- Almost all parts of this project have some precedent in the existing codebase, and it is important to maintain consistency with the existing implementations. Thus, in your proposal, when describing your technical approach, please also point to the existing parts of the codebase that already use a similar approach.

- Explain how the current structure for exploration translations works, and describe, by analogy, the ideal structure for skill and subtopic card translations. For the subtopic pages, what changes exactly will you make with regards to written translations and content IDs?

- Explain in detail the steps you would take to carry out the structural migrations for subtopic pages and skills. For the former, what will the updated editor UI look like?

- Explain how you would make the new 'worked examples' component appear only in the concept card and revision card RTEs.

- Explain how you would structure the acceptance tests for both parts of the project, and the behaviours you would test.

- What is the full list of places in the codebase which list functionality for the different RTE components, and which will need to be updated with details for the worked example component? Explain the approach you took to find these.

</details>

<details>
<summary>Technical hints / guidance</summary>

- This project combines many concepts that already exist in the Oppia codebase, and understanding (and following) existing precedent is important. You will need to have a good understanding of the following in order to tackle this project:
  - The relationship between the different models (topics, skills, subtopics, etc.)
  - How to perform a (safe) schema migration (perhaps try doing a sample migration on your local machine). See [this wiki page](https://github.com/oppia/oppia/wiki/Writing-state-migrations) for details on how to write exploration state migrations; writing migrations for JSON properties in other entities follows a similar process.
  - How to create an RTE component (perhaps try creating a test component on your local machine). See [this wiki page](https://github.com/oppia/oppia/wiki/Rich-Text-Editor-%28RTE%29-Overview) for details on how to implement rich-text components.
  - How to control which RTE components appear in which RTEs, and validate that the RTE content is valid (i.e. doesn’t include any invalid components)
  - How translations work for existing entities, like explorations. (The original TDD for that project is here: [Infrastructure for separate storage of translations](https://docs.google.com/document/d/1ZZ6pVKpmynTlmf1_PV1I5TcccmEXPnmoFAVKXN-u2xM/edit), and you can examine the code related to the Contributor Dashboard for how the translation opportunities are generated and displayed.)

- For subtopic page contents, be careful to ensure that each element in the list has its own unique content ID. Do not just base the content ID on the item's index in the list – if you have 3 elements in the list and then remove the middle one, the last element’s content ID should not change. This is why we need a counter to keep track of the "next content ID to assign".

- For "ensure that this component is translatable in the contributor dashboard", you can temporarily enable it in exploration RTEs (e.g. in the hints RTE), and then test out the translation workflow. It's important to ensure that the new 'worked example' RTE component has behavioural parity with other RTE components in all places which refer to RTE components, even if it's not being used in the relevant contexts yet – for example, you should update the character-counting logic for hint/solution validation to handle worked-example RTE components as well, in case we decide to make this component available to explorations in the future.

- **@chris7716** is currently looking into a project that involves updating the translation structure for concept cards, topic descriptions, etc. You might want to sync with him in order to ensure that your plan for introducing the necessary translation fields aligns with his work.

</details>



### 1.2. Fix the most common server errors

**Project Description:**

We currently see a number of unaddressed [server errors](https://github.com/oppia/oppia/labels/server%20errors) on hosted instances of Oppia. Many server errors relate to user-facing bugs, and are a good clue that something is problematic in the application. Furthermore, frequently occurring errors result in the server logs getting noisy, to the point that they are no longer treated as alerts because the volume of errors is too high.

The aim of this project is to address the 15 most common server errors, so that we can have relatively clean logs. This would also make it easier to catch new issues during test deployments, and reduce the overall error rate of the app.

Addressing a server error entails the following:

- Find a set of setup steps and actions that reliably reproduce the error on a local machine (see [this tutorial](https://github.com/oppia/oppia/wiki/Tutorial-Learn-to-Figure-Out-the-Reproduction-Steps-for-a-Server-Error)). If more insight is needed, it is also fine to add some logging and do another deployment to get more information.
- Identify the root cause of the error.
- Confirm the expected behaviour with the product/tech leads, if needed.
0 Fix the error and add tests (which could be frontend, backend, or full-stack) to ensure that the error does not happen again. Some of the other steps listed in this [wiki page](https://github.com/oppia/oppia/wiki/Server-errors-and-solutions) might also be of interest. Note that some errors may be due to data issues, in which case a migration job or direct editing might be required, as well as stricter typing/validation to ensure that the issue doesn’t reoccur.

Throughout this process, it is also important to be able to:

- Write clear [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs) if you run into any issues, so that you can get help and suggestions from other team members.
- Improve and clarify the logging, where needed, to make errors easier to debug.


Link to PRD:
- N/A. For the most part, this issue is purely technical. Any clarifications of behaviour should be discussed in individual issue threads and in the project proposal.


**Tracking issues**: _(To be updated.)_

**Size of this project:** Medium (\~175 hours)

**Difficulty**: Moderate

**Potential mentors:** @Nik-09

**Product Clarifier:** @kevintab95

**Technical Clarifier:** @Nik-09

**Required knowledge/skills:**
- General
  - Figure out the root cause of an issue and communicate it well using a debugging doc.
- Web:
  - Write Python code with unit tests.
  - Write TS + Angular code with unit tests.
  - Write or modify e2e/acceptance tests.
  - Write or modify Beam jobs, with tests. (This is because you might need to write audit jobs for debugging certain errors.)
  - Figure out repro steps based on info from server logs.

**Related issues:**

Consider taking up issues like [#21807](https://github.com/oppia/oppia/issues/21807), [#21841](https://github.com/oppia/oppia/issues/21841) and/or [#21872](https://github.com/oppia/oppia/issues/21872) to make errors easier to reproduce / debug.

You might also want to try some issues from [this list]((https://github.com/oppia/oppia/labels/server%20errors)) to see whether this project is a good fit for you. In any issues you attempt, try to demonstrate your ability to (a) reproduce server errors deterministically, (b) write a debugging doc to narrow down the source of an error if you can’t pinpoint it in one go, (c) find the clear root cause of an error, and (d) prevent the error from happening in the future. Where possible, we recommend trying to do a mixture of issues that cover backend code, frontend code, and Beam jobs.

If you like, you can also suggest other improvements to the logging infrastructure that would make it easier to fix "server error" issues. (It is fine to file issues for these improvements and get assigned to them in the usual way. However, you should have tried to tackle at least one server error with a debugging doc, and the improvements you suggest should help address the problems you ran into while trying to figure out what caused the error.)

**Suggested Milestones:**
- **Milestone 1**: Fix the 7 most common server errors, and improve the logging for server errors as needed.

  Suggested PM demo points:
  - Demonstrate fixes for any server errors with a user-facing behaviour component.

- **Milestone 2**: Fix the 8 next-most common server errors.

  Suggested PM demo points:
  - Demonstrate fixes for server errors with a user-facing behaviour component.


**Org-admin/tech-lead commentary/advice:**

This is a slightly unusual GSoC project that requires very good debugging skills. You will be exposed to a mix of server errors, some of which are very easy to solve, and others which will require a lot more investigation. Along the way, look for improvements to the infrastructure that would make the debugging process easier (ideally to the point that server errors can be tackled as easily as regular issues).

Laying out your work in a [debugging doc](https://github.com/oppia/oppia/wiki/Debugging-Docs) is a very important skill for this project, since you will sometimes need to get help and it is important to provide responders with the context needed to do so.

<details>
<summary>What we are looking for in proposals:</summary>

For the proposal, we recommend that you focus on identifying around 15 issues tagged as “server errors”, correctly outline their root cause, and propose a fix. These should include most of the ones from the list in the project description, as well as additional ones of your choice. You may also link to reproduction instructions (with video proof) and public debugging docs that you have already added to the corresponding issue threads.

Also, please note that, for this project, the proposal itself is a bit less important. The ability to solve some actual [server errors](https://github.com/oppia/oppia/labels/server%20errors) is better evidence that the project will be a good fit.

</details>

<details>
<summary>Technical hints / guidance</summary>

All applicants for this project should read [this tutorial](https://github.com/oppia/oppia/wiki/Tutorial-Learn-to-Figure-Out-the-Reproduction-Steps-for-a-Server-Error) on how to fix server errors. Note that, for this project, reading and understanding what the code is doing is very important, and so is writing debugging docs to explain what you know. The code fix is often simple, but the analysis to figure out which fix to make can be harder.

When attempting to fix a server error, first find a set of deterministic reproduction steps and add that to the issue. You will need to do this before you can be assigned that issue to fix. (Doing this investigation might result in linking the server error to a different existing issue that is already filed on GitHub, so general experience with bug-fixing is good to have as well.)

Note that **@kevintab95** and **@lkbhitesh07** have access to the server logs. Please correspond with Kevin Thomas and the server admins team if you want to run debugging jobs on the server.
</details>


### 1.3. Lesson player redesign

**Project Description:**

The aim of this project is to redesign the lesson player according to [these mocks](https://www.figma.com/file/YWe7SqfUVjxlJLKTUn0UZa/Project-2?type=design&node-id=7076-365949&mode=design&t=v3mhfxAkI0l9V53z-0), which were created based on feedback that we received from learners. The goals of the redesign are to make the lesson player intuitive to navigate, easy to add features to in the future, and more engaging for younger audiences. All features of the lesson player must work well on mobile, desktop and tablet device sizes, and all features should work in all languages (including both RTL and LTR languages).

The new functionality should be developed behind the /lesson URL (which should, for now, redirect to the same backend handlers as /explore), and be gated behind a feature flag. Once the lesson player is ready to launch, all /explore URLs should be redirected to /lesson instead, and the new lesson player should be used for all lessons.

Note that parts of the lesson player functionality is reused in the exploration editor preview tab, practice sessions, and diagnostic test. Care should be taken to ensure that the new functionality is properly gated and does not break these other interfaces.

Links to PRD and mocks:
- Mini-PRD: [Oppia Lesson Player Redesign Project Mini-PRD](https://docs.google.com/document/u/1/d/1922aE9_TEFTbHyA3jrXy9cTxo2JgvjfEvKHlxqxG-Rw/edit)
- Mocks: https://www.figma.com/file/YWe7SqfUVjxlJLKTUn0UZa/Project-2?type=design&node-id=7076-365949&mode=design&t=v3mhfxAkI0l9V53z-0

**Tracking issues**: [#19217](https://github.com/oppia/oppia/issues/19217)

**Not in scope:**
- Implementing the speed adjuster in the voiceover toolbar
- Implementing the “Get Help” control in the sidebar and the tutorials within it

**Size of this project:** Large (\~350 hours)

**Difficulty**: Hard

**Potential mentors:** @amyyeung17

**Product Clarifier:** @seanlip

**Technical Clarifier:** @amyyeung17

**Required knowledge/skills:**
- General
  - Figure out the root cause of an issue and communicate it well using a debugging doc.
  - Debug and fix CI failures/flakes.
- Web:
  - Write Python code with unit tests.
  - Write TS + Angular code with unit tests.
  - Write or modify e2e/acceptance tests.

**Related issues:**

These include any non-backlog issues in the “Lesson Player CUJs” section of the [LaCE project board](https://github.com/orgs/oppia/projects/3/views/8?sliceBy%5Bvalue%5D=Lesson+player%3A+CUJ+bugs) (try to choose ones that relate specifically to the exploration player interface).

Also, see the guidance in the last part of the “What we’re looking for in proposals” section below.

**Suggested Milestones:**
- **Milestone 1**: Within `core/templates/pages/exploration-player-page`, move all non-UI-specific logic from component.ts files to service.ts files in the `services/`` folder, so that such logic can be reused in both the existing and new exploration player layouts. Organize that folder to have just 3 subdirectories: a current-player-components folder with the Angular components for the existing experience, a new-player-components folder with the Angular components for the new experience, and a services folder for the services that both experiences have in common. Add a README to the root of the exploration-player-page folder explaining the layout. At the end of this process:

    - There should be no duplication of code logic throughout any of the files in `/exploration-player-page` – each piece of functionality should be specified in exactly one location, with no copy-pasting.
    - The only dependencies between files in the three root subfolders should be from current-player-components to services, and from new-player-components to services. No other inter-subfolder dependencies are allowed.
    - No further adjustments should be needed to files in `current-player-components/` for the rest of this project.

  Build the following parts of the new exploration player page:

    - The overall layout of the page (sub-navbar, main player area, sidebar, footer, audio bar). Note that the buttons in these components do not need to work yet, except for the back-and-forth navigation and "Continue" buttons in the footer.
    - The main "conversation flow" UI (including all interactions)
    - The confetti and "correct answer" pop-up on getting a correct answer

  By the end of this milestone, it should be possible to play any Oppia exploration via the `/lesson/{{exploration_id}}` URL (if the feature flag is turned on), submit and view wrong answers, and page back-and-forth through the lesson, on both desktop and mobile, and in both LTR and RTL layouts. However, it is not a requirement that the buttons in the main navbar, audio sub-navbar, etc. do anything yet when clicked (except for the navigation and “Continue” buttons in the footer). Also, the exploration editor preview tab, practice questions page and diagnostic test pages should show the new UI if the flag is turned on, and the old UI if it is not. Finally, if the flag is turned on, the /explore URL should redirect to the corresponding `/lesson` page.

  Suggested PM demo points:
  - The overall structural layout for the exploration player is in place on both desktop and mobile.
  - A simple Oppia exploration (with just Continue, Multiple Choice and NumericInput) is playable in the new lesson UI.
  - An Oppia exploration with all interactions is playable in the new lesson UI.

- **Milestone 2**: Implement the following UI components fully (using the services that you isolated in Milestone 1 where appropriate). The resulting functionality should work well in desktop, mobile and tablet UIs, as well as in LTR and RTL languages:

    - Hints, solutions and concept card pop-ups
    - The "exit lesson" flow in the top sub-navbar
    - The voiceover player sub-navbar
    - The Share, Feedback and Report buttons in the sidebar
    - The progress bar visualization in the footer
    - The save-lesson-progress and checkpoints flow
    - The end-of-lesson next steps (rate lesson, see new lesson, practice, etc.)

  Write acceptance tests, or edit the existing ones, to verify that all of the above functionality works correctly (including in the exploration editor preview tab, the practice questions page, and the diagnostic test page).

  Launch the new lesson player in production, and remove the code for the old lesson player.

  Suggested PM demo points:
  - All the controls in both sub-navbars and the sidebar are fully functional.
  - All the controls in the footer are fully functional.


**Org-admin/tech-lead commentary/advice:**

This is not an easy project. Although it primarily involves UI, it still requires quite a strong understanding of Angular and "layered architecture".

The most important part is the very first part, which involves refactoring the existing UI (in a way that doesn't make any changes to functionality) so that the “services” code is properly separated from "UI" code. To do this properly, you will need to have a very good understanding of how the different pieces of the UI connect together in the new implementation, and be able to write that down as a specification.

After the service code is properly isolated, the rest of the implementation should be fairly straightforward. However, there are a number of subparts and constraints to keep track of, so it will be important to plan the work in an organized way.


<details>
<summary>What we are looking for in proposals:</summary>

For the proposal, we would like to see answers to the following questions:

  - Give a detailed explanation of how you would identify and split out the “service” parts of conversation-skin.component.ts.
  - Give a broad, high-level overview of how you would implement the UI, paying attention to how you would do this in a maintainable way. In particular:
    - What is the final structure of the three subfolders in core/templates/pages/exploration-player-page?
    - For each component in the new exploration player, specify its API fully, including the types and descriptions of each of the component’s inputs.
    - For each component, is there a reusable component implemented elsewhere in the app that you can reuse? If so, describe which one, and how you would refactor it (if needed) to support the new "exploration player page" use case.
  - Specify the naming convention system you would use for the CSS. (It needs to be consistent and predictable.)
  - How will you use feature flags to ensure that the old lesson player page (at /explore) remains intact while the new player functionality is being developed, and that the exploration editor preview tab, practice questions page and diagnostic test pages “behave correctly”? (In your proposal, please also specify what you believe the correct behaviour to be.)
  - How will you connect the code for each of the interactions to the new exploration player? If you are making custom versions of each interaction for the new learner view, how will you ensure that the old code is used when the feature flag is turned off, and the new code is used when the feature flag is turned on?
  - How will you handle "supplemental interactions" (see the "Technical hints" section below)?
  - For each component you create, how will you ensure that it is accessible?
What is the full list of CUJs that you will write acceptance tests for? (This should be covered in the "Testing Plan" section of your proposal.)

While developing your proposal, you might find parts of the mocks that you would like clarification on. Please ask these questions in [GitHub Discussions](https://github.com/oppia/oppia/discussions) or leave comments directly on the [Figma mock](https://www.figma.com/design/YWe7SqfUVjxlJLKTUn0UZa/Project-2?node-id=7641-377168&t=UsCnBHgweFqwGCwR-0). If your technical plan relies on the answers to these questions, link to them (where appropriate) in the proposal you submit.

In addition to the proposal, the following is optional, but would significantly enhance your application if it is done well:
  - Create 1-2 PRs that focus on a specific lesson player sub-component. For this sub-component, move the shared logic between the old and new implementations to the services/ folder, and implement the “new lesson player” version of that sub-component with Karma unit tests. Demonstrate that, with your PR, the old versions of the lesson player still work correctly (including in the exploration editor preview page, the practice questions page, and the diagnostic test page, where applicable).
</details>

<details>
<summary>Technical hints / guidance</summary>

- Here is some guidance on how to [launch new features](https://github.com/oppia/oppia/wiki/Launching-new-features#how-do-you-as-a-developer-use-feature-flags), which also goes into detail on how to use feature flags.
- The most important part of this project to get right (and also the hardest) is the first part of Milestone 1. If this is done properly then the rest of the project will be a lot more straightforward. To do this, make sure that you have a clear understanding, in your new implementation, of the list of services, list of components, and which components use which services (and how they do so) – this should all be specified clearly in your proposal. Then you can look at the existing services/components (for the old implementation) and figure out what modifications are needed to bring them in line with your proposal, and establish the right boundaries between UI and "domain logic" code.
- After the code is organized, it is important to be really careful when modifying services, as doing so would impact both the new and old functionality.
- The new exploration player will also need to handle "supplemental" interactions (like image click, music notes, etc.), where the interaction is a "canvas" that the learner enters answers in, and that doesn’t reset when Oppia gives feedback. Mocks do not exist for this case, but you can use the approach taken in the existing lesson player (e.g., for desktop view, show the "canvas" on the right of the screen and the conversation on the left side).
- When developing the new UI, it is important to make sure that the new UI works for both mobile/desktop and also for RTL/LTR languages. Don't leave handling these till the end – take care to develop them properly as you go.
- When developing the new UI components, keep CSS scoped to each of those components. There is a lot of “global CSS” in the old exploration player, but we do not want to repeat that pattern.
- When developing the new UI components, it is fine to repeat UI code from the old components (if that matches the “new lesson player experience”), since we will be deleting the entire folder of old components at the end of the project.
- In general, the old lesson player may not conform to best practices. You do not need to repeat those mistakes in the new implementation! If you are not sure whether an existing practice in the old lesson player UI code should be followed in the new UI implementation, feel free to ask about that on GitHub Discussions, and we can give you advice.

</details>


## Contributor Dashboard team

### 2.1. Show AI-powered translation suggestions to translation submitters

**Project Description:**

This project involves showing auto-generated suggestions in the Contributor Dashboard translation submission modal, so that translation submitters can edit and submit those translations, rather than needing to generate completely new ones from scratch each time. These suggestions would arise from autogenerated translations from an AI-powered translation service.

The project involves implementing a system for updating `EntityTranslationsModel` to associate each (content_id, language) pair with both a “manual” and “auto” translation (see `VoiceoverType` in feconf.py, which does something similar for voiceovers). The manual translation should only be populated once a translation is approved by a human reviewer (possibly after edits), and this translation is what is shown to the learner when playing lessons. On the other hand, automatic translations will only be shown as suggestions to translation submitters via the contributor dashboard. To understand the effectiveness of the AI suggestions, the contributor admin dashboard will also display information about how many times the AI suggestions were used as-is, without any edits.

There should be a button in the /admin panel that is able to bulk-generate auto-translations via a Beam job. This job should be run to populate the initial auto-translations once the pipeline is ready. Subsequently, any additions/edits to a curated entity (lesson, topic, skill, etc.) should trigger a full auto-translation of the added/edited content, and publishing a curated entity should trigger a full auto-translation of all strings in the entity. In general, the auto-translations should always be up-to-date with the English strings in the current version of the entity.


Link to PRD: [Language Management and Lesson Auto-Translation PRD](https://docs.google.com/document/d/1TeGQQNLNJWkTgvGQ1xmV6snz8zXnJ23TvuDKtK5_Tok/edit?usp=sharing) (a bit out of date)

**Tracking issues**: [#16164](https://github.com/oppia/oppia/issues/16164) (part), [#19681](https://github.com/oppia/oppia/issues/19681)

**Not in scope:**
- Configuring the list of prioritized languages for translation
- Auto-generation of voiceovers (in any language)
- Enabling translations for concept cards, review cards, or practice questions
- Showing auto-generated translations in the learner view (see https://github.com/oppia/oppia/issues/16164 for more information).

**Size of this project:** Large (\~350 hours)

**Difficulty**: Hard

**Potential mentors:** @chris7716

**Product Clarifier:** @seanlip

**Technical Clarifier:** @chris7716

**Required knowledge/skills:**
- General
  - Figure out the root cause of an issue and communicate it well using a debugging doc.
  - Debug and fix CI failures/flakes.
- Web:
  - Write Python code with unit tests.
  - Write TS + Angular code with unit tests.
  - Write or modify e2e/acceptance tests.
  - Write or modify Beam jobs, with tests.

**Related issues:**

Issues related to translation submitters are good ones to tackle: https://github.com/orgs/oppia/projects/18/views/4?sliceBy%5Bvalue%5D=Translation+submitters


**Suggested Milestones:**
- **Milestone 1**: The full computer-aided translation (CAT) backend implementation is completed, including functionality that allows the developer team to configure the CAT service provider for each language. All rich-text fields, including those that use components like images, videos, skill links, math expressions, and so on, are handled properly, and there is validation to ensure that the autotranslated string has the same number and type of rich-text components as the original string.

  A new `exactly_matches_ai_suggestion` boolean field, which defaults to False, is added to the GeneralSuggestionModel. This is used to increment new `submitted_ai_translations_exact_match_count` fields in `TranslationContributionStatsModel` and `TranslationSubmitterTotalContributionStatsModel` when a contributor’s translation suggestion is exactly the same as the auto-AI suggestion stored in `EntityTranslationsModel`, and this new count is displayed in the relevant table of the Contributor Admin dashboard. Any Beam backfill jobs that regenerate these statistics should also be updated as needed.

  The storage models are updated to support the storage of autogenerated translations, and admins can run a Beam job from the admin dashboard to generate auto-translations for any untranslated texts for all curated lessons in Oppia's prioritized languages (they can select 'all entities', ‘all entities of a specific type’, or a specific entity; and they can select 'all languages' or a particular language). The wiki pages are also updated to explain how to add new translation providers for specific languages.

  Suggested PM demo points:
  - Translation autogeneration works properly for rich-text content with different components (skill links, images, etc.).
  - A Beam job allows generation of all autotranslations.

- **Milestone 2**: When any additions/edits are made to a curated entity (lesson, topic, skill, etc.), these should trigger a full auto-translation of the added/edited content. When a curated entity is published, this should trigger a full auto-translation of all strings in the entity that don’t have translations yet.

  Auto-generated translations are shown in the contributor dashboard UI, together with the relevant context that states where they come from.

  Suggested PM demo points:
  - Autogenerated translation suggestions are shown in the contributor dashboard UI.


**Org-admin/tech-lead commentary/advice:**

This is a difficult project that involves building and completing a pipeline that can greatly reduce the effort needed to internationalize lessons. It is also the only project we are offering this year that makes use of AI.

The main things to be prepared for are Beam jobs and working with an external translation service. When planning your milestones, try and do the Beam testing as early as possible so that you have enough time to debug any issues that arise. For the translation service, it is essential to have a quick way to test it, because you will likely need to fine-tune how you send the strings to the service. Getting that set up can involve some registration/activation steps, so it's worth getting familiar with the pipeline to ensure that you will have a good development environment to iterate in.


<details>
<summary>What we are looking for in proposals:</summary>

Please explain the following clearly in your proposal:

  - Details of all the Beam jobs you plan to write for this project.
  - What is your plan for translating each of the rich-text component types, and how will you handle this when sending the string to the third-party system for translation? How will you validate that the correct number and type of rich-text fields are preserved between the original and the translated content?
  - How will you structure the system so that different service providers can be specified for different languages, with each service provider having a ‘services.py’ file in core/platform/translate? (For this project, it is fine to include the implementation for only one provider, but the framework should be extensible and there should be clear instructions in the wiki for contributors on how to add a new provider.)
  - What are the different tasks that need to be completed for this project, and in what order should they be done?
  - What transformations need to be done to the content before it is sent to the cloud translation service, and what transformations need to be done to the received translation before it is saved in the datastore (so that it can be presented directly to translation submitters, without further edits)?
  - What is your plan for setting up a quick-debugging loop that helps you fine-tune what you send to the cloud translation service? (It would be a good idea to try and get a proof-of-concept set up on your machine that shows you are able to do effective testing with a cloud translation service while developing locally.)
  - What is the updated schema for the storage models, and (if necessary) how will you handle the migration of the existing models to the new structure?
  - What updates you will make to the Contributor Admin dashboard files, and what modifications you will make to the Beam backfill statistics-regeneration jobs, to add a new statistic for submitted translations which match the AI ones.

</details>

<details>
<summary>Technical hints / guidance</summary>

- You will need to gate the new functionality behind a `SHOW_TRANSLATION_SUGGESTIONS_IN_CD` [feature flag](https://github.com/oppia/oppia/wiki/Launching-new-features) that gates the integration of translation suggestions to the contributor dashboard. We will only turn on this feature flag once the feature testing process has been completed.
- This [design issue](https://github.com/oppia/design-team/issues/128) tracks the progress of the mocks for showing translation suggestions on the contributor dashboard, and you can follow it for updates. That said, for your proposal, please focus more on the technical aspects than the mocks – in general, anything that contributor dashboard submitters can reasonably understand and make use of is fine.
- The technical approach we are taking involves pre-generating the auto-translations, to reduce latency at the time of translating. There should therefore be no need to generate auto-translations “in the moment” while a volunteer is submitting a translation via the contributor dashboard. If, for some reason, a stored auto-translation is not available for a piece of content, it is fine to just not show that part of the submission modal. (Don’t error noisily in a way that blocks the experience for the translation submitter.)
- The list of languages for which to auto-generate translations can be derived from the information stored in VoiceoverAutogenerationPolicyModel, which contains language codes as keys. This list is currently shown on the /voiceover-admin page.
- A fair amount of the computer-aided translation (CAT) backend work has already been done (see [this doc](https://docs.google.com/document/d/1kJd-yLTzB9a2c3Nq7v9pzKfHwKHKGpkWfQ8B0YGf50U/edit#heading=h.jp6no890gjkv) for details). You might like to look at previous unfinished PRs: #12604 / #14418. However, please bear in mind that the translations system has evolved significantly since those PRs were created.
- If you need to migrate JSON properties, following the approach used for migrating the states in the Exploration domain object might help (i.e. introduce a schema version field and use that to perform the migration safely).
- To enable the (new version of the) Contributor Admin dashboard, go to /release-coordinator and turn the `cd_admin_dashboard_new_ui` flag on.
- Note that, although we are adding `submitted_ai_translations_exact_match_count` to the `TranslationContributionStatsModel`, we don’t need to show it in the contributor’s “Contribution Stats” dashboard. The reason we add it here is so that it is easy to backfill the `TranslationSubmitterTotalContributionStatsModel` from it if needed (note that this is how the other attributes are backfilled if that stats model needs to be regenerated). However, if `TranslationContributionStatsModel` needs to be backfilled, then we would need to do so based on the suggestions and entity translations.

</details>


## Developer Workflow Team

### 3.1. Acceptance tests

**Project Description:**

In order to streamline releases, we are planning to ensure that all critical user journeys (CUJs) on the Oppia web application are covered by acceptance tests. This is important because it will provide assurance that, on the merge of every PR, these critical user journeys still function correctly, which means that no major breakages will result if the develop branch gets deployed to production. Additionally, having a complete set of acceptance tests that are organized by CUJ makes it easier to audit whether or not a particular CUJ has been included, and it also helps developers add tests for new CUJs while still keeping the tests well-organized.

This project includes:

  - Writing acceptance tests for the as-yet-uncovered CUJs in a way that keeps the tests organized and maintainable. This might also include small updates to the acceptance test framework, e.g. extracting utility functions to enable code reuse or providing relevant functionality for a group of tests.
  - Tightening all page utility functions to have pre/post checks (in the form of “wait” statements) and proper error messaging, so that it is easier to debug flakes. The pre-check wait ensures that the conditions are good for performing the action, and the post-check wait ensures that the action has fully completed.
  - Deleting e2e tests whose functionality has been fully replaced by the acceptance tests.

Relevant documents:
- Current CUJ tracker: [Critical User Journeys v2](https://docs.google.com/document/d/1s3MG2MVh_7m7B0wIlZb7sAcoyUdY0zq7a1JEFtwYBjI/edit?tab=t.0#heading=h.gs2e2lh85so7)
- Spreadsheet that details most of the tests that need to be written: [Web QA Test Matrix (arranged by user type)](https://docs.google.com/spreadsheets/d/1O8EHiSAGrG0yoNUBz9E4DIwKNS8Rfsv_ffC4k1WK5jc/edit#gid=1807800085)

**Tracking issues**: [#21646](https://github.com/oppia/oppia/issues/21646)

**Not in scope:**
- Configuring the list of prioritized languages for translation
- Auto-generation of voiceovers (in any language)
- Enabling translations for concept cards, review cards, or practice questions
- Showing auto-generated translations in the learner view (see https://github.com/oppia/oppia/issues/16164 for more information).

**Size of this project:** Large (\~350 hours)

**Difficulty**: Easy / Moderate

**Potential mentors:** @imchristie

**Product Clarifier:** @seanlip

**Technical Clarifier:** @imchristie

**Required knowledge/skills:**
- General
  - Figure out the root cause of an issue and communicate it well using a debugging doc.
  - Debug and fix CI failures/flakes.
- Web:
  - Write TS + Angular code with unit tests.
  - Write or modify e2e/acceptance tests.

**Related issues:**

Acceptance test infrastructure: https://github.com/orgs/oppia/projects/8/views/11?sliceBy%5Bvalue%5D=Acceptance+Tests


**Suggested Milestones:**
- **Milestone 1**: Tighten all existing page utility functions in `core/tests/puppeteer-acceptance-tests` to have appropriate pre/post checks.

  Complete all remaining acceptance tests (as specified in [#21646](https://github.com/oppia/oppia/issues/21646)) for exploration creators, logged-out users, and logged-in users, and ensure that they run on all PRs by adding them to the "acceptance test" GitHub workflow. Remove any existing webdriverio tests whose functionality is fully covered by the new acceptance tests.

  Suggested PM demo points:
  - Acceptance tests for the exploration creator user journeys have been written.

- **Milestone 2**: Complete all other remaining acceptance tests (as specified in [#21646](https://github.com/oppia/oppia/issues/21646)), and ensure that they run on all PRs by adding them to the "acceptance test" GitHub workflow. Remove any existing webdriverio tests whose functionality is fully covered by the new acceptance tests.

  If any webdriverio tests remain after this step, translate them into CUJs and work with the QA team to make them part of the CUJ document. Implement the corresponding acceptance tests.

  Finally, remove the webdriverio and e2e test framework completely.

  Suggested PM demo points:
  - Acceptance tests for the contributor dashboard user journeys have been written.


**Org-admin/tech-lead commentary/advice:**

This is not a difficult project, since a lot of the infrastructure has been written and there are lots of examples that you can follow. The most important thing is to set up a good development cycle so that you can debug issues with tests quickly.

It is important that you are able to get the tests running on your machine, so that you can pause them when needed and investigate to see what is going wrong.


<details>
<summary>What we are looking for in proposals:</summary>

For this particular GSoC project, the proposal is less important and we are more interested in your previous PRs. In particular, each of the following can significantly enhance your application:

  - Tackling at least one PR that solves a part of #21646.
  - Showing at least one debugging doc that correctly diagnoses the root cause of an e2e/acceptance flake.
  - Making at least one PR that resolves at least one E2E/acceptance flakiness issue (many of these are collected here).

Some things you could address in your proposal:

  - How will you break down this project into individual sub-milestones? Provide a clear timeline for this.
  - How will you set up your debugging cycle so that you can easily figure out what is going wrong with a test, or fix a flake in it? Explain this for both (a) local development, and (b) getting a test to pass in the CI environment.
  - Do an audit of which page-level functions are missing pre- or post-checks. List these in your proposal. You might also consider making a PR to fix them for at least one of those files, to demonstrate that you know how to add the checks correctly and to get feedback from reviewers.
  - For each existing webdriverio test file, specify the set of CUJs which need to be covered by acceptance tests in order for it to be removed. (If you identify gaps in the spreadsheet CUJs during this audit, feel free to suggest additions/updates to those.)
  - Suggest any improvements that you would make to how the tests are currently organized. How would you make it easy for the QA team to verify whether a particular CUJ is covered by acceptance tests? Also, how would you make it easy for developers to figure out which CUJ they need to update (or if they need to add a completely new one)?
  - Suggest any missing CUJs that you would add. You can cross-reference the testing spreadsheet with the [CUJ document](https://docs.google.com/document/d/1s3MG2MVh_7m7B0wIlZb7sAcoyUdY0zq7a1JEFtwYBjI/edit) that is currently used for release testing, or identify those journeys yourself through direct experimentation with the test server or your local dev setup. Focus only on critical user journeys -- you do not need to go into detail for all the edge cases. When suggesting missing CUJs, include test specs for the corresponding user journeys (there is a format for this in the GSoC proposal template).

</details>

<details>
<summary>Technical hints / guidance</summary>

- Start by writing tests for just one CUJ to make sure you can do it properly. If you are able to do that well, then there is a good chance that you will be successful with this project.
- For this project, user journeys are detailed in a shared sheet, divided into distinct tabs. During the implementation phase, applicants should tackle each user journey in a structured way, leveraging lessons and code from earlier phases to inform later work. This will help streamline implementation and ensure efficient reuse of developed solutions.
- You might want to join the [Release Testing team](https://groups.google.com/g/oppia-release-testers) to help out with testing releases and becoming familiar with the application. The QA team, who coordinates the release testing team, can also advise on CUJs and provide detail on them if any are unclear. Feel free to reach out to them if you have questions.
- The acceptance tests ultimately need to pass in the CI environment, which is different from the local environment. How will you set up your debugging workflow so that you can test things on CI quickly? (One approach might be to temporarily comment out the other tests/workflows so that, when you make a push, only the acceptance test you are interested in runs. You might want to try this out for yourself and elaborate on what you did in your proposal.)
- The QA team owns the [CUJ document](https://docs.google.com/document/d/1s3MG2MVh_7m7B0wIlZb7sAcoyUdY0zq7a1JEFtwYBjI/edit). If you need to clarify CUJs, feel free to work directly with them on this.

</details>


### 3.2. Consolidate entity migration jobs

**Project Description:**

The Oppia codebase includes several different versioned entities which store learning material: explorations, skills, stories, subtopic pages, questions, topics, and collections. The infrastructure to maintain each of these versioned entities has been developed separately, and is a bit patchy (for example, migrations of old snapshots have not been implemented for some of the entities). This is making it difficult to remove some of the old version upgrade functions in the codebase which are no longer needed.

The aim of this project is to standardize these migration jobs so that there is a single, standard way to migrate and upgrade versioned models. This will (a) ensure that all the versioned models can be easily updated on a periodic basis, (b) let us delete the code for upgrading from old versions once all the entities of that version have been upgraded, and (c) simplify the remaining version upgrade code.

Specifically, we would like to do the following:

  - Have a BaseMigrateVersionedModelJob and a BaseMigrateVersionedModelSnapshotsJob, and refactor the jobs and audit jobs for migrating models and snapshots (like MigrateExplorationJob, ExpSnapshotsMigrationAuditJob, etc.) to be subclasses of these two jobs. The bulk of the logic for all of these jobs should be in the two base classes, with the subclasses just pointing to the relevant storage models / domain object classes and having no custom logic – see `SNAPSHOT_METADATA_CLASS` in `ExplorationModel` for an example of this.
  - Run all the jobs in production so that all the models and snapshots on the server are upgraded to use the latest schema versions.
  - Clean out all the old conversion functions and the methods they call (see https://github.com/oppia/oppia/pull/12256/files for an example).

We would also like to standardize the infrastructure for migrating JSON properties. This entails the following:

  - Create a BaseVersionedDomainObject whose subclasses declaratively specify a mapping from any versioned field to its corresponding schema version field. (These fields correspond to `JsonProperty` in the datastore's storage model.) Un-versioned fields of type `Dict` or `List[Dict]`` should be explicitly declared as un-versioned. Subclasses must also reference constants in feconf.py that specify the minimum and maximum version of each field.

  - Write backend tests that:
    - Identify all subclasses of BaseVersionedDomainObject in the codebase and verify that every `Dict` or `List[Dict]`` field contained in the object is either included in the mapping mentioned above or included in a list of un-versioned fields. This ensures that all versioned domain objects have the necessary infrastructure for performing schema upgrades for their respective JsonProperties.
    - Ensure that the relevant migration functions for each upgradable field are present in the corresponding domain object class with the function signatures (including type hints). Specifically, each conversion function should accept one parameter of the same type as the versioned field and should return one value of the same type. The migration functions can be named using a standard scheme, e.g. `_convert_{{field_name}}_v{{x}}_dict_to_v{{x+1}}_dict`, and the backend test can check for that. This test should also use the minimum and maximum schema versions to check that upgrade functions from the minimum up to the maximum version are present.

  - Add a `migrate_to_latest_schema_versions` function to BaseVersionedDomainObject to handle schema upgrades in a generalized way across all domain objects.
  - Ensure that all the different getter functions in the _services/fetchers.py files that convert storage models to domain objects also use `migrate_to_latest_schema_versions` to translate that object’s fields to use the latest schema versions.
  - Replace all domain objects corresponding to VersionedModels with the new BaseVersionedDomainObject.

Here's a schematic depiction of a possible end state for versioned domain models:

```
class BaseVersionedDomainObject:
  - Class Variables:
     - schema_versioned_attributes = {}
  - Methods:
    - def migrate_to_latest_schema_versions():
      - Use the versioned_attributes map to find versioned fields. Then call update functions on each of those until the entire domain object is fully upgraded.

class Exploration(BaseVersionedDomainObject:
  - Class Variables:
    -  schema_versioned_attributes: {
        "states_dict": {
          "version_field": "states_schema_version",
          "version_min": feconf.MIN_STATE_SCHEMA_VERSION (e.g. 5),
          "version_max": feconf.CURRENT_STATE_SCHEMA_VERSION (e.g. 10)
        }
      }
  - Methods:
    - def _convert_states_v5_dict_to_v6_dict
    - ...
    - def _convert_states_v9_dict_to_v10_dict
```

**Tracking issues**: [#21646](https://github.com/oppia/oppia/issues/21646)

**Size of this project:** Medium (\~175 hours)

**Difficulty**: Moderate

**Potential mentors:** @U8NWXD

**Product Clarifier:** @seanlip

**Technical Clarifier:** @U8NWXD

**Required knowledge/skills:**
- General
  - Figure out the root cause of an issue and communicate it well using a debugging doc.
- Web:
  - Write Python code with unit tests.
  - Write or modify Beam jobs, with tests.

Additionally, strong technical design skills and a good sense of code architecture are helpful.

**Related issues:**

- [#16556](https://github.com/oppia/oppia/issues/16556) is a good issue to look into, since it will help you become familiar with the migration job infrastructure.
- [Issues related to Beam jobs](https://github.com/oppia/oppia/labels/Beam%20jobs) are also good ones to look at.


**Suggested Milestones:**
- **Milestone 1**: Create a BaseVersionedDomainObject which specifies object member mappings to storage model properties in a declarative way, and also specifies the “schema version field” corresponding to each JsonProperty-related field. Add tests to ensure that all JsonProperties are accounted for. Then, replace all existing domain objects for versioned models with subclasses of BaseVersionedDomainObject.

  Also, ensure that all functions that convert storage models to domain objects also migrate domain objects to the latest schema version.

  Suggested PM demo points:
  - At least one domain object is using BaseVersionedDomainObject, and all the get/save functionality works correctly.

- **Milestone 2**: Create BaseMigrateVersionedModelJob and BaseMigrateVersionedModelSnapshotsJob classes with the core logic for upgrading models and snapshots to the latest schema versions, respectively. Use these to build both job and audit job subclasses for all versioned models (explorations, skills, stories, subtopic pages, questions, topics, collections) with proper logging and error reporting (e.g. if a migration fails, the model that could not be migrated should be logged for debugging). Test these jobs on production data to ensure that they work correctly, and fix any issues that arise. Delete the old jobs.

  Finally, run all the jobs in all our production environments, so that all the models and snapshots on the server are upgraded to the latest schema versions. Then, clean out the old conversion functions for all 7 versioned models and the methods they call (similar to what was done in https://github.com/oppia/oppia/pull/12256/files).

  Suggested PM demo points:
  - All jobs run correctly on the backup server.


**Org-admin/tech-lead commentary/advice:**

This project requires a very good understanding of how our migration pipeline works, and a solid grasp of technical architecture so that you can make good design decisions for how the base classes and their subclasses are structured.

However, once that is well-understood, it should not be too difficult to implement. You will probably find deleting all the old code at the end quite satisfying!


<details>
<summary>What we are looking for in proposals:</summary>

In addition to your implementation approach, please also:

  - Analyze the jobs for the existing entities to understand and catalogue their differences. Then, for each of those differences, make a proposal for how you plan to standardize it, and explain the implementation of each of the resulting base job and audit job classes for migrating entities and entity snapshots.
  - Describe what error reporting or logging you would add to the Beam job to make it easy for you or server admins to detect/debug issues when it is run.
  - Describe how you would name the new jobs. Try to use a standard naming convention that is easily extended to versioned models that are introduced in the future.
  - For each entity type, list the functions/constants that you plan to delete (in addition to the conversion methods) after you have confirmed that all models are using the latest schema versions. Describe how you determined that this is the complete list of orphaned functions/constants.
  - Provide a full example of how you would set up the BaseVersionedDomainObject with declarative definitions for at least one of the existing versioned models. Clarify what goes into the base domain object and what goes into the subclasses.
  - List the validation checks that the versioned domain object classes must satisfy, and describe how your backend tests will automatically pick up all the versioned domain object classes in the codebase when new ones are added.

</details>

<details>
<summary>Technical hints / guidance</summary>

  - When designing the Beam jobs, note that audit jobs should be trivial subclasses of the main jobs with `DATASTORE_UPDATES_ALLOWED = False`. (Look at the usage of `DATASTORE_UPDATES_ALLOWED` in the codebase for more information.)
  There is an old wiki page with instructions for writing schema migrations that might provide some useful background: https://github.com/oppia/oppia/wiki/Writing-state-migrations
  In general, if some functionality is common to all versioned models, it should be included in the base class. Otherwise, it should be defined in the relevant subclass(es).

</details>


### 3.3. TBD

_This project idea is still in development and will be added shortly.


## Android team

### 4.1. Flashbacks

**Project Description:**

When learners make a mistake on a concept they have previously demonstrated in an earlier part of a lesson, it often makes sense to redirect them back (or to a parallel flow) to try and reinforce earlier concepts that the learner may have not fully understood. However, with the current implementation, learners subsequently need to re-answer all the cards between the earlier state and the state they had reached, which is frustrating.

This project aims to provide a new feature called ‘flashbacks’ which helps to bring the benefits of earlier redirection (i.e. reviewing an earlier concept that directly ties to the misconception) without the frustrating part of having to redo the old questions before returning back to the question that originally caused the learner to become stuck.

Additionally, this project also includes improving the general look-and-feel of submitted answers for both multiple choice and item selection interactions as these both currently rely on HTML generation rather than having a cleaner, natively rendered experience. This will also allow them to be displayed properly in the “flashback” experience.

Links to PRD and mocks:
- [PRD](https://docs.google.com/document/d/1NpWgRN6BgvlutWXTYkz997ft36nRMYCbxSO7RYy2iV8/edit?tab=t.0) (note that this is incomplete)
- Design tracking issue for mocks: [oppia/design-team#50](https://github.com/oppia/design-team/issues/50). Specific notes on mocks:
  - The mocks don't include explicit changes for multiple choice and item selection.
  - The mocks don't quite represent the correct ‘inline’ experience that needs to be introduced for the ‘Learn Again’ button (which should be part of the answer & response section of the incorrect answer that is prompting for a revisit).
  - Only the mocks with the orange toolbars are actually correct and need to be implemented (except for the otter, and the return button should be part of the flow rather than overlaid).

**Tracking issues**: _To be updated._

**Size of this project:** Medium (\~175 hours)

**Difficulty**: Moderate

**Potential mentors:** @adhiamboperes

**Product Clarifier:** @seanlip

**Technical Clarifier:** @BenHenning

**Required knowledge/skills:**
- General
  - Figure out the root cause of an issue and communicate it well using a debugging doc.
- Android:
  - Build the app and install it on a local device or emulator. Then verify that you can (a) build a non-test library  target locally, (b) run a unit test locally, and (c) play through the app locally.
  - Write new Kotlin code with unit tests.
  - Change Android UIs, write tests for them, and manually verify that they work.

**Related issues:**

Key issue: [#5572](https://github.com/oppia/oppia-android/issues/5572). This tracks introducing a short-term solution of the broader problem this GSoC project aims to solve.

_(Note: Additional issues will be added soon.)_

**Suggested Milestones:**
- **Milestone 1**: The new flashback dialog is implemented and hooked up to the existing soft redirection button. (The in-line flow does not need to work at this stage.)

  Suggested PM demo points:
  - Trigger a “user is soft redirected” state to demonstrate the flashback dialog.

- **Milestone 2**: The flashback dialog is hooked up with the learner flow to have an in-line view (i.e. the 'Learn Again' button is attached to the incorrect answer that led to the flashback), and relevant UI tests are added. Also, the new designs for multiple choice and item selection interactions are implemented.

  Suggested PM demo points:
  - Demonstrate the "user is soft-redirected" flashback with the in-line "Learn Again" button along with the new item selection and multiple choice interaction views (for submitted answers).


**Org-admin/tech-lead commentary/advice:**

This project involves a lot of very gritty coding work in the most critical code pathways in the app: the core learner flow. These are not simple areas of the app as Oppia's core lesson flow is fundamentally complex, but fortunately there are dozens of past projects and changes that have changed these coding areas (which may act as good references) and the codepath has generally excellent test coverage (which means we can be confident when we make changes to these areas).

Making changes to the core lesson flow may be a combination of feeling like a lot of progress is being made (when adding some of the fairly substantial boilerplate involved in adding views to the lesson flow), and other times where it can take a while just to add a few lines of code (due to the surrounding area being particularly complex, such as for the actor-based [ExplorationProgressController](https://github.com/oppia/oppia-android/blob/4f58be9d399c70e1d1cd241495280ae913afbf07/domain/src/main/java/org/oppia/android/domain/exploration/ExplorationProgressController.kt#L106)). It may be very difficult to fully grok the full dependency and data flow for explorations, but it's usually straightforward to jump in and start making changes that in turn show up in the lesson viewer frontend.


<details>
<summary>What we are looking for in proposals:</summary>

- An explanation for how the new functionality will be gated behind a [feature flag](https://github.com/oppia/oppia-android/wiki/Platform-Parameters-&-Feature-Flags) to ensure that changes don't get shipped to end users before the feature is completed.
- A list of test names that will be added (we generally add automated tests for every code change).
- Multiple diagrams, particularly:
  - A dependency diagram showing how different components (i.e. classes) of the implementation call into each other.
  - A flow diagram to show how user interactions flow into different state changes in code.

</details>

<details>
<summary>Technical hints / guidance</summary>

_This will be added soon._

</details>


### 4.2. Platform parameters dashboard

**Project Description:**

Feature flags are a special type of configurable [platform parameter](https://github.com/oppia/oppia-android/wiki/Platform-Parameters-&-Feature-Flags#introduction) which allows the team to stage features behind remotely configurable flags until they're ready to be launched. This allows features to be developed across multiple releases without users seeing part of the feature (or app stability issues when the feature is enabled), ensuring the team releases high-quality features and doesn't hurt the overall quality and performance of the app. Broadly, platform parameters allow the team to overall configure the app (which can be useful both for feature flags, as described above, and safety 'knobs' such as controlling rate limits to remote APIs to help reduce the chance of server outages).

This project entails introducing a developer-only UI (as part of the developer options section of the app) which displays all platform parameters and feature flags in the app, their current enabled/disabled status (for feature flags) or values (for platform parameters), their sync status (i.e. whether they're being synced from the server or using a local developer default), and allows an explicit manual override to force the feature on or off or to override the platform parameter's value.

**Tracking issues**: [#5345](https://github.com/oppia/oppia-android/issues/5345) (note that this issue presently includes testing work that may well be completed by [#5565](https://github.com/oppia/oppia-android/pull/5565)).

**Size of this project:** Medium (\~175 hours)

**Difficulty**: Moderate

**Potential mentors:** @Rd4dev

**Product Clarifier:** @BenHenning

**Technical Clarifier:** @BenHenning

**Required knowledge/skills:**
- General
  - Figure out the root cause of an issue and communicate it well using a debugging doc.
- Android:
  - Build the app and install it on a local device or emulator. Then verify that you can (a) build a non-test library  target locally, (b) run a unit test locally, and (c) play through the app locally.
  - Write new Kotlin code with unit tests.
  - Change Android UIs, write tests for them, and manually verify that they work.

**Related issues:**

_(Note: Specific issues will be added soon.)_

**Suggested Milestones:**
- **Milestone 1**: Key deliverables:
   - Display a developer options-only list of platform parameters and feature flags along with their current values and sync statuses.
   - Set up initial tests to demonstrate that the UI displays correctly.

  Suggested PM demo points:
  - The new UI correctly shows all platform parameters and feature flags, and their correct value and sync statuses.

- **Milestone 2**: Key deliverables:
  - Support for overwriting platform parameters and feature flags, including force-restarting the app upon navigating away from the menu (so that the changes can take effect).
  - Updated UI tests for the new functionality.

  Suggested PM demo points:
  - The new screen fully supports overriding various platform parameters and feature flag values.


**Org-admin/tech-lead commentary/advice:**

This project involves introducing a new, isolated user interface that only affects developers (and possibly testers or user study facilitators in the future) which means it doesn't require the same level of gating as regular learner-facing features. It's often nice to work on brand new UIs, as well, since everything is starting in a fresh, clean state rather than building on existing complexity and tests.

The domain side of platform parameters isn't trivial to understand, but it's straightforward to explain and analyze the dataflow. This is expected to be a straightforward project that balances domain and frontend work (with a majority of the work being UI-related).


<details>
<summary>What we are looking for in proposals:</summary>

- A strong understanding of:
  - Feature flags and platform parameters, including their complete lifecycle for both production and tests.
  - Dagger dependency gating and how dependencies can differ based on the flavor of the app being built, and whether it's a test environment.
- A list of test names that will be added (we generally add automated tests for every code change).
- Multiple diagrams, particularly:
  - A dependency diagram showing how different components (i.e. classes) of the implementation call into each other.
  - A flow diagram to show how user interactions flow into different state changes in code.

</details>

<details>
<summary>Technical hints / guidance</summary>

_This will be added soon._

</details>


### 4.3. TBD

_This project idea is still in development and will be added shortly.
