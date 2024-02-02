## Important!

_We are making some changes to how we run GSoC for 2024. Please read this page carefully, since some things may have changed from previous years._

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

In order to receive updates about GSoC at Oppia, please subscribe to the [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce) mailing list and keep an eye on [GitHub Discussions](https://github.com/oppia/oppia/discussions).

This year, Oppia will follow the standard GSoC timeline: projects will have 6 weeks for each milestone, with a PM demo and internal evaluation after 5 weeks. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below for more details.

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions [here](https://github.com/oppia/oppia/wiki).


## Contributors

GSoC is an excellent opportunity for new contributors to get paid to work on an open source project. If you're interested in applying as a contributor, you should definitely read the following resources:

-   [Google Summer of Code contributor guide](https://google.github.io/gsocguides/student/)
-   [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
-   [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)


## Getting started

Welcome! If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. Also, turn on notifications for [Github Discussions](https://github.com/oppia/oppia/discussions) since announcements may be made there as well. Make sure to set your preferences for both of these correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is about:
    - Read the [user documentation](http://oppia.github.io/#/) to become familiar with important concepts like explorations and interactions.
    - Play some lessons on [Oppia.org](https://www.oppia.org/learn/math), which hosts a live instance of Oppia.

3. To get started with development, read and follow the instructions in the contributors' guide carefully ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Oppia Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)).

4. Do one or more starter projects to become familiar with the contribution process. This will help us get an idea of what it's like to work with you. It will also help you get a better understanding of the codebase and our development process, which may help with writing a good project proposal. Once you've merged at least 2 pull requests, you will get an invitation to become a collaborator to the Oppia repository and be officially onboarded! **This step is a prerequisite to applying for GSoC.**

   - **Note!** You must be onboarded to the repository to which you will contribute during GSoC. For example, to work on an Oppia Web GSoC project, you need to be onboarded to the oppia/oppia repository, which means that your 2 pull requests need to be to oppia/oppia.

   - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to read the [["getting started" guide|Contributing-code-to-Oppia]] and [[PR instructions|Make-a-pull-request]] carefully, follow the [tips for success](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#tips-for-success), manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [[style rules|Coding-style-guide]], and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Select one or more [GSoC project ideas](#oppias-project-ideas-list) that you're most interested in, and write your project proposal! You can get feedback from project mentors when you've completed a sufficient draft -- see the instructions in the [GSoC proposal template](#gsoc-proposal-template) section for details.

   We require that all general discussion about GSoC projects take place in open channels. If you have questions about a project, you can ask in [GitHub Discussions](https://github.com/oppia/oppia/discussions/categories/gsoc-2024-q-a) or email the [oppia-gsoc-discuss@](https://groups.google.com/g/oppia-gsoc-discuss) mailing list. Please be specific when asking questions, since this makes it easier for us to help you.

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
  - The organisation is active and have strong community bond.
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

To receive important announcements and updates about GSoC at Oppia, please subscribe to the **[Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce)** mailing list and turn on notifications for GitHub Discussions.

## Oppia's Project Ideas List

_**Note:** If you're coming to this section from an external link, please make sure to scroll up and read this entire wiki page carefully, not just this section. There's a lot of useful information on the rest of the page, including a FAQ and a section describing selection criteria. Thanks!_

The following is a list of Oppia's 2024 GSoC project ideas. You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community beforehand in order to get feedback and guidance to improve the proposal. We'd also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

Please note that the list of project ideas below is not set in stone: more projects may be added later, and some project descriptions may also change a bit, so check back regularly. In addition, the mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted.

### Learner and Creator Experience (LaCE) team

The LaCE team's project ideas for GSoC 2024 are still in development, and will be published shortly.

### Contributor Dashboard team

The Contributor Dashboard team's project ideas for GSoC 2024 are still in development, and will be published shortly.

### Developer workflow team

The Developer Workflow team's project ideas for GSoC 2024 are still in development, and will be published shortly.

### Android team

The Android team's project ideas for GSoC 2024 are still in development, and will be published shortly.
