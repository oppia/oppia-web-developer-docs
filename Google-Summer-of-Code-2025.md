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

The official GSoC timeline for 2025 has not been posted yet. We will update this section when that happens.

> [!NOTE]
> For Oppia's participation in GSoC 2025, the coding period dates are strict, and we will not be offering extensions. Please ensure that you have sufficient time during the summer to work on your projects.

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

   You can also request **at most one** "tech lead review" for **at most one** of your proposals during the pre-selection phase. To keep things fair, the tech lead will do only a single pass on your proposal and leave comments, but is not required to follow up on replies to those comments. Since you can only request a tech lead review once (per applicant), we recommend doing so after you have gotten feedback from mentors and completed a full draft of your proposal, but at least a week before the due date. Tech leads will process requests in the order they are received. To request a tech lead review, fill in this Google Form (**link to be added later**).

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

_The LaCE team's project ideas for GSoC 2025 are still in development, and will be published shortly._

### Contributor Dashboard team

_The Contributor Dashboard team's project ideas for GSoC 2025 are still in development, and will be published shortly._

### Developer Workflow team

_The Developer Workflow team's project ideas for GSoC 2025 are still in development, and will be published shortly._

### Android team

_The Android team's project ideas for GSoC 2025 are still in development, and will be published shortly._
