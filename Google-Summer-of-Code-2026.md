**Important**: _We are making some changes to how we run GSoC for 2026. Please read this page carefully, since some things have changed from previous years._

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

This year marks the 11th year that Oppia will be participating in [Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers post-secondary students, as well as newcomers to open source, an opportunity to discover and work with open source organizations. The contributions are supported by a stipend. Contributors work closely with one or more mentors to implement either a project idea by the organization, or a proposal of their own.

In order to receive updates about GSoC at Oppia, please subscribe to the [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce) mailing list, as well as the [Developer Announcements](https://github.com/oppia/oppia/discussions/categories/developer-announcements) category on GitHub Discussions.

This year, the same as last year, Oppia plans to follow a slightly extended GSoC timeline: projects will have 7 weeks for each milestone, with an additional "holiday week" between the milestones. Each milestone includes 5 weeks of coding time, 1 week for evaluations, and 1 week for fixes, as well as a product demo session after the 4th coding week. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below for more details.

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

You might also enjoy the "weekly journals" from some of our previous contributors: **[Rd4dev](https://medium.com/@rd4dev)** and **[@hardikgoyal2003](https://medium.com/@hardikgoyal2003)**.


## Selected Projects

Check back later to see the projects selected for GSoC 2026.

## Getting started

Welcome! If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list and the [Developer Announcements](https://github.com/oppia/oppia/discussions/categories/developer-announcements) category on GitHub Discussions, so that you can receive important notifications about Oppia's participation in GSoC. Make sure to set your preferences correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is about:
    - Read the [user documentation](http://oppia.github.io/#/) to become familiar with important concepts like explorations and interactions.
    - Play some lessons on [Oppia.org](https://www.oppia.org/learn/math), which hosts a live instance of Oppia.

3. To get started with development, read and follow the instructions in the contributors' guide carefully ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Oppia Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)). If you're interested in Oppia Web, you might also find [these tutorials](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#developing-your-skills) helpful.

4. Do a few starter projects to become familiar with the contribution process. This will help us get an idea of what it's like to work with you. It will also help you get a better understanding of the codebase and our development process, which may help with writing a good project proposal. Once you've merged at least 1-2 pull requests, you will get an invitation to become a collaborator to the Oppia repository and be officially onboarded! **This step is a prerequisite to applying for GSoC.**

> [!NOTE]
> You must be onboarded to the repository to which you will contribute during GSoC. For example, to work on an Oppia Web GSoC project, you need to be onboarded to the oppia/oppia repository, which means that your pull requests need to be to oppia/oppia.

> [!TIP]
> Quality is more important than quantity, so try to contribute to high-impact issues where possible. Also, we want to see examples of your best work, so please make sure to read the [["getting started" guide|Contributing-code-to-Oppia]] and [[PR instructions|Rules-for-making-PRs]] carefully, follow the [tips for success](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#tips-for-success), manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [[style rules|Coding-style-guide]], and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Select one or more [GSoC project ideas](#oppias-project-ideas-list) that you're most interested in, and write your project proposal! You can get feedback from project mentors when you've completed a sufficient draft -- see the instructions in the [GSoC proposal template](#gsoc-proposal-template) section for details.

   We require that all general discussion about GSoC projects take place in open channels. If you have questions about a project, you can ask in [GitHub Web Discussions](https://github.com/oppia/oppia/discussions/categories/general-gsoc-2026-q-a-web) or [GitHub Android Discussions](https://github.com/oppia/oppia-android/discussions/categories/general-gsoc-q-a). Note that individual projects have their own categories, so please use those if you have project-specific questions. Please also be specific when asking questions, since this makes it easier for us to help you.

> [!TIP]
> During the application period, your first goal should be to figure out how to become an effective contributor. Start developing your project proposal only once you have experience getting some PRs merged. This will give you a much better idea of what you want to work on, and how much you can accomplish.
>
> You might also want to ensure that you have the required skills for your chosen project. For guidance on how to do this, see the relevant section in the [GSoC proposal template](#gsoc-proposal-template) document and our [FAQs](#faqs).

Good luck!


## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: Please see the individual project ideas to determine which skills are recommended for the project in question. Also, in general:

   - For Oppia Web, Angular 2+, Python 3.10, Google App Engine and Apache Beam are useful and recommended, and experience with GitHub Actions is useful for developer workflow projects. Also, it is important to be able to write tests for the code you submit (using Karma, Puppeteer and unittest). You might also find this [[page of learning resources|Learning-Resources]] helpful, as well as other pages on our [wiki](https://github.com/oppia/oppia/wiki) that provide guidance on Apache Beam, testing frameworks, etc.

   - For Oppia Android, you will need to know how to program in Kotlin, and have experience with Android development. Knowledge of Bazel may also be helpful for some projects.

   - Note that, although GSoC is aimed at both students and beginner contributors to open source, "beginner to open source" is **not** the same as "beginner to coding" -- the projects do assume that you have some proficiency with coding. The fact that GSoC projects produce high-quality code that solves real problems for open-source projects does make GSoC challenging, but this is also part of what makes GSoC such a valuable experience for our contributors.

**Q: How can I increase my chances of getting selected?**

A: The most important thing is to ensure that you have the required skills for the project -- see the "Required Skills" section of the [proposal template](#gsoc-proposal-template) for more details. Aside from that, writing a good project proposal with a solid solution approach, engaging with the community, helping other contributors, successfully contributing PRs for high-priority issues, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](#selection-criteria) we'll be using this year.

**Q: Which projects are most important for Oppia? Can you advise which project I should pick?**

A: All the projects we've listed in the [Ideas List](#oppias-project-ideas-list) are treated as equally important during selection, and we'd be very happy to see good progress made on any of them! Note that the relative importance of a project to Oppia is not part of the [selection criteria](#selection-criteria). In general, we recommend that you pick a project based on whether you already have (or will be able to learn) the skills required for it, and that you'd enjoy doing over the summer!

**Q: I do not have any experience in skill XYZ. What should I do?**

A: If you are missing a skill that is needed for a project, we recommend trying to learn it -- in software development, it is common to develop experience and expertise as you take up and complete projects successfully. Some ways to do this include working on issues that give you a chance to develop that skill, referring to our wiki documentation, and following tutorials from elsewhere on the Web. Please note that, in general, we are unlikely to accept applicants who lack the required skills for a project, since this tends to result in significant difficulties during the coding phase.

**Q: How will you assess whether I have the required skills for a project?**

We will assess your application based on your proposal and the skills that you have demonstrated in your PRs and other interactions with the community. Please see the guidance in the "Required Skills" section of the [proposal template](#gsoc-proposal-template), which explains how to demonstrate that you have the required skills for a project, and provides pointers on how to develop those skills.

**Q: Is it okay if I only focus on the frontend or backend?**

A: This probably depends on the project(s) you wish to apply for; check their "required skills" sections. However, note that most projects are full-stack and require ability in both the frontend and backend. We recommend becoming familiar with both of these, since this will open up more opportunities for you, as the projects we work on at Oppia often touch multiple layers of the stack.

**Q: What is the minimum number of PRs that one should have?**

A: You should have at least 2 merged PRs. Beyond that, remember that quality is more important than quantity, so consider taking some high-priority or ["impact: high"](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22Impact%3A+High%22) issues if you're able to, since those fixes are more valuable. You can find a list of high-priority issues on the respective teams' project boards: [LEAP](https://github.com/orgs/oppia/projects/3/views/8), [Dev Workflow](https://github.com/orgs/oppia/projects/8/views/11), [CORE](https://github.com/orgs/oppia/projects/18/views/4), [Android CLaM](https://github.com/orgs/oppia/projects/4/views/3), [Android Dev Workflow](https://github.com/orgs/oppia/projects/10/views/1). Additionally, you'll also want to demonstrate that you have the required skills to successfully complete your chosen project; please see the guidance in the "Required Skills" section of the [proposal template](#gsoc-proposal-template), which explains how to do this.

**Q: Will I be penalized during selection if I ask for help while contributing?**

A: Not at all! Asking for help when you need it is part of the learning process, and the Oppia open-source community is more than happy to help and onboard new members. Please just ensure that your questions are well-formed and that you (a) have read the relevant docs on the wiki, (b) provide the necessary information (such as a [debugging doc](https://github.com/oppia/oppia/wiki/Debugging-Docs)) to help responders understand what you've figured out so far and where you are stuck.

**Q: I only discovered Oppia recently. Does this mean that, during selection, my application would automatically be ranked lower than those by other applicants who have a longer tenure with Oppia?**

A: Definitely not! Here are the [selection criteria](#selection-criteria) we use when selecting contributors for GSoC. Note that tenure with Oppia is explicitly not part of these criteria.

**Q: How early should I start working on the proposal?**

A: We recommend developing your project proposal and engaging with the community via GitHub Discussions as early as possible, so that you have enough time to get feedback from mentors and improve the proposal before the submission deadline. Make sure to follow all instructions in the [proposal template](#gsoc-proposal-template) (especially around sharing and access) to reduce delays in reviewing your proposal. That said, it's important to note that the proposal is only one part of the application process, and it is probably more important to figure out how to become an effective contributor by getting some PRs merged and demonstrating that you have the required skills for the project.

**Q: Can I submit more than one proposal to Oppia?**

A: Yes, you can. However, we strongly recommend picking one project and writing a solid proposal for it. Splitting attention across multiple projects might not be a great idea.

**Q: If I only submit a proposal, without making any code contributions, will my application be considered?**

A: No. See our [selection criteria](#selection-criteria) for more details.

**Q: Can I use content from the project ideas list or PRD in my proposal?**

A: It is fine for proposals to draw from the GSoC idea in the wiki and any linked PRDs. However, please note that if you copy content directly from any source (even if it is an Oppia doc), **you must cite and link to the original source**. Also, remember from our [selection criteria](#selection-criteria) that when we review proposals, one of the things we look for is evidence that the applicant understands the project and existing codebase well. Strong proposals will therefore contain details that are original (e.g. that are not copied from the PRD).

**Q: I'm part of team X in Oppia. Can I submit a proposal for a project idea from a different team?**

A: Yes, you can; there are no issues with that. There is a space in the proposal template to list teams at Oppia you've participated in, and we will get feedback from members of those teams about what their experience of collaborating with you has been like.

**Q: What is the total number of contributors that will be accepted?**

A: We generally request slots for as many projects as we think will succeed. However, the Google GSoC admins may impose limits based on how they decide to distribute contributor slots among the different open-source organizations.

**Q: The [Google GSoC FAQ](https://developers.google.com/open-source/gsoc/faq#can_someone_already_participating_in_open_source_be_a_gsoc_contributor) mentions that the program is only for new contributors. I have already contributed to Oppia and I have write access. Can I still participate?**

A: The GSoC program is open to students, as well as beginner contributors to open source. If you do not qualify as a student, see [this FAQ](https://developers.google.com/open-source/gsoc/faq#how_do_i_know_if_i_am_considered_a_beginner_in_open_source_development) on the GSoC website for whether you would be considered a beginner.

**Q: Can you be flexible around my other summer commitments?**

A: Probably not. We have not had good experiences offering flexibility in previous years, so this year, Oppia will strictly adhere to the Oppia GSoC timeline. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below, and avoid taking up major commitments alongside GSoC. Experience from previous years suggests that you will be unlikely to successfully balance both.

**Q: I'd love to contribute to open source, but I'm not sure I have enough time during the summer to do a GSoC project. Can I still help out?**

A: Yes, GSoC is probably not the best choice if you don't have enough time during the summer, since it requires focused commitment. However, you can still start contributing to Oppia by following the instructions in the contributors' guide ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Oppia Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)).

**Q: What are Oppia's rules for contributors using artificial intelligence (AI) models?**

A: You are welcome to use AI when contributing to Oppia, but you are still responsible for what you contribute. For example, we expect you to double-check any AI-generated code to make sure that it is correct, high-quality, and complies with our guidelines. If AI generates buggy code, it's your job to fix the bugs before you open a PR. Similarly, if you use AI to craft prose (e.g. comments on PR threads), we still expect you to communicate clearly, effectively, and constructively. In our experience, AI tends to generate prose that is too long and verbose, which can be frustrating for other people to read. You are also responsible for ensuring that you are legally allowed to contribute your work to Oppia (e.g. that AI hasn't copied it from a restrictively-licensed source). Finally, remember that GSoC is about learning, so make sure you don't come to rely on AI in place of developing your own skills.

## Dates and Deadlines

Noteworthy dates for 2026 (see also the [Official GSoC Timeline](https://developers.google.com/open-source/gsoc/timeline)):

- **Jan 19 - Feb 3**: Mentoring organizations apply
- **Feb 19**: Mentoring organizations are announced
- **Feb 21 16:00 UTC**: GSoC Q&A session with Oppia
  - Video call link: https://meet.google.com/ffg-vbts-rqd
- **Mar 16 - Mar 31**: GSoC contributor application period
- **Apr 30**: Accepted GSoC contributors are announced
- **Apr 30 - May 24**: Community bonding ("greenlight") period
  - **TBD**: Briefing for accepted GSoC contributors (mandatory)
- **May 25 - Jul 10**: Milestone 1 work period for GSoC
  - **Jun 26**: Milestone 1 work due for internal evaluation
  - **Jun 27 - Jul 3**: Testing of the milestone 1 work product
  - **Jul 4 - Jul 10**: Buffer time for Milestone 1 revisions
  - **Jul 13 - Jul 17**: Official GSoC midpoint evaluation
- **Jul 18 - Sep 2**: Milestone 2 work period for GSoC
  - **Aug 19**: Milestone 2 work due for internal evaluation
  - **Aug 20 - Aug 26**: Testing of the milestone 2 work product
  - **Aug 27 - Sept 2**: Buffer time for Phase 2 revisions
  - **Sept 7 - Sept 14**: Official GSoC mentor evaluation due
- **Sep 15**: GSoC period at Oppia officially ends

**Note!** For Oppia's participation in GSoC 2026, the coding period dates are strict, and we will not be offering extensions. Please ensure that you have sufficient time during the summer to work on your projects.



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

When submitting a proposal, please use the provided [GSoC 2026 proposal template](https://docs.google.com/document/d/1C1ZhKaShWSSIAtiFLd-lcQyjfQbMRNl3bIf-kQv2KNw/edit?tab=t.0). We will only consider proposals submitted using this template. Note that there is a length limit: the proposal's technical "HOW" section should not exceed 20 pages at "Roboto 10" font size.

> [!IMPORTANT]
> The 2026 template differs from the 2025 template. Please make sure that you are using the 2026 one. Proposals must follow our template and instructions exactly, or they will be dismissed without review as spam.

**Note:** There's **no** formal minimum length requirement for your proposal. The quality of what you write is much more important than the amount of text you write, and we encourage you to write **shorter** proposals that still convey the main aim of the project.

> [!CAUTION]
> While large language models have become quite capable recently, we caution you against relying on them too much. In contrast to the verbosity typical of AI-generated text, strong proposals will need to be dense and succinct to convey the deep technical analysis we expect within the proposal length limit.


**Some important notes:**

1. Your proposal must be **original** (see section 2.4 of the [Contributor Participation Agreement](https://summerofcode.withgoogle.com/terms/contributor)). During the selection process, proposals that are found to have passed off others' work as their own will automatically be disqualified. If you include any text in your proposal that is copied from the Internet or other sources (even if it is an Oppia doc), you **must** provide a link or reference back to the source. Note that you must attribute sources even if you paraphrase (i.e. re-write their content in your own words). In cases of doubt, we would encourage you to err on the side of citing your sources (since not doing so may be construed as plagiarism).

2. When the necessary criteria for requesting a review are met, add gsoc-2026-mentors@oppia.org as an editor for your proposal doc. (This makes some workflows, like inviting PMs or fixing typos, etc., easier, but if you're concerned about changes to your doc, then you can [turn on notifications for edits](https://support.google.com/docs/answer/91588?hl=en&co=GENIE.Platform%3DDesktop).) After fixing the sharing settings, make a new post in the correct "proposal reviews" category in [GitHub Discussions](https://github.com/oppia/oppia/discussions) that is clearly titled with the name of the project that you are requesting a review for, and provide a link to the doc in your post.

   Please use only the above channel for proposal reviews: all proposal-related communication should happen through GitHub Discussions or directly through comments in the proposal doc. **Do not** send proposals directly to individual GSoC mentors.

   You can also request **at most one** "tech lead review" for **at most one** of your proposals during the pre-selection phase. To keep things fair, the tech lead will do only a single pass on your proposal and leave comments, but is not required to follow up on replies to those comments. Since you can only request a tech lead review once (per applicant), we recommend doing so after you have gotten feedback from mentors and completed a full draft of your proposal, but at least a week before the due date. Tech leads will process requests in the order they are received. To request a tech lead review, fill in [this Google Form](https://forms.gle/GzQ2sAPPBALhnbRx9).

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
 
> [!IMPORTANT]
> Communication quality is very important to us. We've noticed a number of new contributors leaving irrelevant, unclear, or otherwise low-quality comments that appear to have been generated by AI tools. This kind of behavior will reflect poorly on you during selection. While you are welcome to use AI (see our FAQ for details), you remain responsible for the quality of your communications. In general, we have found AI-generated text to be frustratingly long and verbose, so we encourage you to practice communicating clearly and concisely without relying on AI.

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

The following is a list of Oppia's 2026 GSoC project ideas. You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community beforehand in order to get feedback and guidance to improve the proposal. We'd also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

Please note that the list of project ideas below is not set in stone: more projects may be added later, and some project descriptions may also change a bit, so check back regularly. In addition, the mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted. (If you want to see what changes have been made to this page since you last viewed it, you can use the [History tab](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2026/_history).)

If you need clarification on any of these ideas, feel free to open a thread in GitHub Discussions following the process in [this guide](https://docs.google.com/document/d/1jt8_pKcrbsc0xHgUEa0Wh8i6imxYmZiB_2QjDmH7ODg/edit?tab=t.0).

### Learners, Educators, Allies, and Parents (LEAP) team

- [1.1. Web user feedback](#11-web-user-feedback)
- [1.2. Learner assessments](#12-learner-assessments)
- [1.3. Re-design the topic page](#13-re-design-the-topic-page)

### Creators, Operations, Reviewers, and Editors (CORE) team

- [2.1. Automatic translation suggestions](#21-automatic-translation-suggestions)
- [2.2. Extend translation infrastructure to exploration metadata and skills](#22-extend-translation-infrastructure-to-exploration-metadata-and-skills)

### Developer Workflow team

- [3.1. Improve acceptance test infrastructure](#31-improve-acceptance-test-infrastructure)
- [3.2. Consolidate entity migration jobs](#32-consolidate-entity-migration-jobs)
- [3.3. Standardize and validate domain objects and storage models](#33-standardize-and-validate-domain-objects-and-storage-models)

### Android team

- [4.1 Support for Lesson Progress, Study Guides, and Worked Examples](#41-support-for-lesson-progress-study-guides-and-worked-examples)
- [4.2 Streamlining Release Automation](#42-streamlining-release-automation)

## Learners, Educators, Allies, and Parents (LEAP) team

### 1.1. Web user feedback

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:** Learners (and other relevant users) should have an easy way to report issues with the platform so that we can quickly catch and resolve these issues in a scalable manner.

Links to PRD and mocks:

- PRD: https://docs.google.com/document/d/1ZUD7nktZrl5ZyxcXfLAqJqb6wI40U9rdg-2vHHWUZ1g/edit?usp=sharing

**Tracking issues**:

- https://github.com/oppia/oppia/issues/24716

**Not in scope:**

- Feedback Recategorization: Workflows for admins to move feedback between categories (e.g., changing "Lesson" to "Platform").
- Auto-Translation: Automatic translation of non-English feedback.

**Size:** Large (\~350 hours)

**Difficulty**: Moderate

**Potential mentors:** @mon4our

**Product/technical clarifiers:** @U8NWXD (product), @mon4our (technical)

**Discussion forum:** https://github.com/oppia/oppia/discussions/categories/gsoc-q-a-1-leap-projects

**Required knowledge/skills:**

- Figure out the root cause of an issue and communicate it well using a debugging doc.
- Debug and fix CI failures/flakes.
- Write Python code with unit tests.
- Write TS + Angular code with unit tests.
- Write or modify e2e/acceptance tests.
- Write or modify Beam jobs.

**Related issues:** We don't have a set of particularly related issues for you to start with since this will be a brand new feature. To gain experience with the required knowledge and skills, look for relevant issues with the [LEAP](https://github.com/orgs/oppia/projects/3), [CORE](https://github.com/orgs/oppia/projects/18), and [dev workflow](https://github.com/orgs/oppia/projects/8) teams depending on which skills you need to practice or demonstrate.

**Suggested Milestones:**

- **Milestone 1**: Implement the feedback entry point and modal using the pre-existing image uploader component for screenshots. Develop the logic to programmatically capture user session data (logs, metadata) upon opt-in and persist all data to the backend. **Important steps**: Integrating the existing image uploader, implementing a method to share user’s session data, CAPTCHA integration (to prevent spam feedback by bots, might not be necessary), implementing the acceptance tests for the user flows and backend schema design.

- **Milestone 2**: Create the admin-facing dashboard to retrieve and view feedback. **Important steps**: Creating the Dashboard UI, implementing fetching from the backend data, writing the acceptance tests for the admin flows.

<details>
<summary>Org-admin/tech-lead commentary/advice</summary>

In this project, you will be building a new, fairly self-contained feature from the ground up, including some creative design work. If you are excited by the prospect of owning a feature from start to finish and the challenge of overcoming unexpected problems, then this might be a good project for you. Strong debugging, technical design, and planning skills will be essential.
</details>

<details>
<summary>What we are looking for in proposals</summary>

The proposal must explain technically how you intend to capture "session data". What will be the database schema for the new Feedback Models that will store the feedback in the database? How will the frontend fetch the feedback data from the backend? How will you integrate the existing image uploader modal into the feedback form? Consider how to protect the feedback submitter’s privacy. Include mocks for the new admin dashboard (for viewing the submitted feedback). Since these are not external-facing, the design can be a little rougher.
</details>

<details>
<summary>Technical hints / guidance</summary>

- Frontend-backend communication: You will need to implement a new API endpoint (e.g., /api/feedback_dashboard) to serve the admin dashboard. This endpoint should support server-side pagination and filtering (e.g., fetching feedback by category or date range) to handle potential future scale.
- On the frontend, create a dedicated FeedbackBackendApiService to handle these requests and manage the type definitions for the feedback objects.
- Image uploader: Check the current implementation for the Image Upload RTE component in the topic/subtopic modals to get an idea of how to use the image uploader modal in the feedback form.
- Would we need to differentiate between logged in and logged out users? Explain why. How would we implement the system in either case?
- To protect the privacy of those submitting feedback, create a cron job (search for `cron` in our codebase to see examples) to automatically erase feedback after 6 months. Viewing feedback should be restricted to admins, and admins should also be able to delete particular pieces of feedback early in case they see something sensitive.

</details>

<details>
<summary>Suggested PM demo points</summary>

Milestone 1:

- User is able to open the feedback modal from any page on the site
- User is able to rate the experience and provide text feedback.
- Demonstrate the integration of the image uploader component.
- Show the "Include session info" checkbox (unchecked by default).
- The feedback is stored as expected on the backend
- CAPTCHA integration
- All applicable frontend, backend, and acceptance tests have been written and pass robustly.

Milestone 2:

- User submitted feedback shows up on the admin dashboard
- Dashboard is legible and easy to use
- Admins can dismiss feedback
- Admins can delete feedback
- Feedback is automatically deleted every 6 months
- All applicable frontend, backend, and acceptance tests have been written and pass robustly.

</details>

### 1.2. Learner assessments

**Project Description:** We want to celebrate and recognize learners’ achievements as they progress through our curriculum to help motivate them. We currently do this at the exploration (also known as a “lesson”) level, but we want to also celebrate longer-term learning across multiple lessons. To do so, this project introduces assessments that cover groups of skills. At any time, learners can choose to take the assessment to test what they’ve learned. In the future (out of scope for this project), we plan to give learners certificates for passing assessments so they can share the certificate with others. Even without this certificate feature, learners will be able to show their passing score page to others to celebrate their achievement.

This project includes:

- Creating the backend infrastructure needed to:
  - Store the certificate assessment offerings available for learners to take
  - Given a certificate assessment offering, generate an assessment by randomly selecting from a pool of questions
  - Record the results from a learner’s certificate assessment attempt
- Building the frontend experience for learners to:
  - Discover the available assessment offerings
  - Take an assessment
  - See the results of their assessment attempt
  - See their history of assessment attempts
- Building the frontend experience for our lessons team to create and configure assessment offerings

Our product team has put a lot of work into specifying the learner’s experience, so the frontend for learners and the backend infrastructure are pretty well-defined. You will have more freedom (and responsibility) to design the frontend experience for the lessons team.

Links to PRD and mocks:

- PRD: [Assessment Construction and Mastery for Certificates](https://docs.google.com/document/d/19Qm6YPInNMFgqihJP-zL1qtW1BsLRDdLgWHuRr7XtRE/edit?usp=sharing)
- PRD: [Certificates #28 (Logged-in Student Experience, Web)](https://docs.google.com/document/d/1j5hHvh_WrEngnty5I2RR3EMGBsUHHARJWqnC_ABwYUo/edit)

**Tracking issues**:

- https://github.com/oppia/oppia/issues/24717

**Not in scope:**

- The Skill Mastery PRD (linked-to from the Certification Assessment PRD)
- Mastery measures that aggregate across multiple certification assessments
- Generating the certificate document. For now, we will let learners take assessments and screenshot their score page to share their achievement with others.
- Translations. The questions surfaced in the assessment are currently un-translated, so to keep the scope of this project manageable, we will add translation support in a later project.

**Size:** Large (\~350 hours)

**Difficulty**: Hard

**Potential mentors:** @brianrodri @masterboy376

**Product/technical clarifiers:** @U8NWXD (product), @brianrodri (technical)

**Discussion forum:** https://github.com/oppia/oppia/discussions/categories/gsoc-q-a-1-leap-projects

**Required knowledge/skills:**

- Figure out the root cause of an issue and communicate it well using a debugging doc.
- Debug and fix CI failures/flakes.
- Write Python code with unit tests.
- Write TS + Angular code with unit tests.
- Write or modify e2e/acceptance tests.
- Basic user interface design skills will be important for creating the lesson team’s interface for creating certificate assessment offerings. Note that the functionality and usability of this interface is more important than its aesthetics since it is not exposed to external users.
  - To demonstrate this skill, you can include in your proposal draft mocks for the asessment creation interface.
- Creating user interfaces that follow provided mocks. In particular, you should be comfortable using HTML, CSS, and Angular to create new user interface elements to match mocks.
  - To demonstrate this skill, take a look at feature requests for the [CORE](https://github.com/orgs/oppia/projects/18/views/4) and [LEAP](https://github.com/orgs/oppia/projects/3) teams.
- Working with Oppia’s full-stack infrastructure. You should be familiar with how data flows between the layers of Oppia’s stack from the frontend all the way through to storage models and back to the frontend.
  - To demonstrate this skill, take a look at full-stack feature requests or bug fixes for the [CORE](https://github.com/orgs/oppia/projects/18/views/4) and [LEAP](https://github.com/orgs/oppia/projects/3) teams.

**Related issues:** Take a look at issues for the [CORE](https://github.com/orgs/oppia/projects/18/views/4) and [LEAP](https://github.com/orgs/oppia/projects/3) teams, particularly but not exclusively [those related to questions](https://github.com/orgs/oppia/projects/18/views/4?sliceBy%5Bvalue%5D=%5BProject%5D+Fix+issues+affecting+question+submitter+workflows).

**Suggested Milestones:**

- **Milestone 1**: The frontend experience for the lessons team has been created, allowing them to create, edit, view, and delete certificate assessment offerings. This interface enforces validation checks to prevent the creation of invalid assessment offerings (e.g. attaching skills that don’t have enough questions, leaving the description blank) and gives the user feedback about whether changes were successfully saved. The associated backend infrastructure has also been created to store the configured offerings.

- **Milestone 2**: The frontend experience for learners has been created, allowing them to discover, take, and see results of assessments. Learners can also see their history of assessment attempts. The associated backend infrastructure has been built to support this experience, including the generation of new assessments and recording the results of assessments taken.

<details>
<summary>Org-admin/tech-lead commentary/advice</summary>

This is a complex, full-stack project that develops a new feature and includes some design work. You should have good familiarity with Oppia’s full-stack infrastructure and be prepared to tackle unexpected issues. Debugging skills will be essential! If the challenge of implementing a whole feature end-to-end excites you, then this is a great project to consider.
</details>

<details>
<summary>What we are looking for in proposals</summary>

- Mocks for the frontend experience for the lessons team
- Detailed plans for the backend infrastructure you will build. What endpoints will you create or change? What storage models will you create, and what will each model look like? Be specific.
- Sketch out the logic (for example with pseudocode) you will use generate assessments, store assessment attempt results, and compute the metrics to display on the assessment results page.
- How will you use feature flags to stage the release of the feature?
- How will you compute the metrics requested in the PRDs? Note that while we need to be able to get these metrics, they don’t need to be surfaced in a dashboard. For example, a beam job that we can run to calculate metrics is acceptable (though if you go this route you need to show you can write beam jobs).
- Make sure to account for writing frontend, backend, and acceptance tests for your project! These should be included in your timeline, and you should provide evidence that you know how to write them.

</details>

<details>
<summary>Technical hints / guidance</summary>

There are substantial technical details in the PRDs, particularly with regards to storing assessment attempt results, so please review those carefully. In brief, we envision you creating the backend storage models for the following:

- Certificate assessment offerings. Should store configuration parameters like attached skills, time limit, name, description, and associated classroom. This needs to be versioned so that if an assessment offering is changed, we can recover the assessment offering version that the learner actually attempted.
- Assessment attempts. Should store a versioned reference to the offering attempted, the start and end times, references to response objects for each question in the attempt (including questions not answered), and a learner identifier.
- Assessment question responses. Should store a version reference to the associated assessment attempt object, a versioned reference to the question presented, the user’s selected answer (or an indication that the question wasn’t answered), whether the learner got the answer correct, and a versioned reference to the skill tested.

We already have backend storage models for questions, topics, skills, and classrooms. You should plan to use those existing models and describe in your proposal any changes you will need to make to them. For example, we will need to modify the classroom model to store references to certificate offerings so that we can control the order in which offerinigs are displayed to the user.

There is also prior work in the codebase that you can learn from. For example, at the end of a practice session, users are currently shown a breakdown of their score that is similar to what we want to show at the end of an assessment in this project.

</details>

<details>
<summary>Suggested PM demo points</summary>

Milestone 1:

- Certificate assessment offerings can be created, viewed, edited, and deleted.
- Validation checks prevent the creation of invalid assessment offerings.
- Changes made through the frontend are persisted to storage models in the backend.
- All applicable frontend, backend, and acceptance tests have been written and pass robustly.

Milestone 2:

- Learners can discover, take, and see results from assessments.
- Learners can see their history of assessment attempts.
- Learner assessment results are persisted to the backend.
- Assessments are correctly generated.
- All applicable frontend, backend, and acceptance tests have been written and pass robustly.

</details>

### 1.3. Re-design the topic page

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:** Based on user feedback, on the current topic page, users often overlook the Practice and Revision tabs completely. Additionally, the functionality in those tabs is not correlated with the available lessons, making it unclear to learners when they should review or practice those skills.

The aim of this project is to update the design of the topic page to present a more integrated view of the lessons, practice sessions, and links to revision cards (subtopic pages), so that learners can practice the skills they learned in the relevant lesson. Additionally, it is disappointing for learners to find that the languages that they would want to use for translations and voiceovers are missing only after they start the lesson, so the new design incorporates these selections within the topic page itself and follows the overall site language as a default.

Links to PRD and mocks:

- [PRD: Practice Sessions Experience and Topic Page](https://docs.google.com/document/d/1r9IEQ5z_t-eu9XAWN3eRA7iKdKuYsOQbVUjO2ZH1qKg/edit?tab=t.0)
  - Note that this PRD describes a redesign of both the topic page and the practice session experience. This GSoC project only covers redesigning the topic page. The PRD’s mocks are also out of date; please refer to [these mocks](https://www.figma.com/design/1wjdVilWcZs9znEj6tFyFC/Project--107-Add-visual-cues-to-guide-learners-to-their-next-steps-on-the-topic-page?node-id=1-51&p=f) instead. You may find it useful to start by reviewing the mocks, since they only cover the parts of the PRD relevant to this GSoC project.

**Tracking issues**:

- https://github.com/oppia/oppia/issues/19614

**Not in scope:** Changes in the linked PRD that relate solely to the practice questions player.

**Size:** Medium (\~175 hours)

**Difficulty**: Moderate

**Potential mentors:** @HardikGoyal2003

**Product/technical clarifiers:** @HardikGoyal2003 (product), @HardikGoyal2003 (technical)

**Discussion forum:** https://github.com/oppia/oppia/discussions/categories/gsoc-q-a-1-leap-projects

**Required knowledge/skills:**

- Figure out the root cause of an issue and communicate it well using a debugging doc.
- Debug and fix CI failures/flakes.
- Write Python code with unit tests.
- Write TS + Angular code with unit tests.
- Write or modify e2e/acceptance tests.
- User interface creation, particularly familiarity with CSS and screen-size-responsive design

**Related issues:**

- https://github.com/orgs/oppia/projects/3/views/8?sliceBy%5Bvalue%5D=%5BProject%5D+Fix+issues+relating+to+the+topic%2Fclassroom+pages
- https://github.com/orgs/oppia/projects/3/views/8?sliceBy%5Bvalue%5D=%5BProject%5D+Fix+all+acceptance+test+failures
- https://github.com/orgs/oppia/projects/3/views/8?sliceBy%5Bvalue%5D=%5BProject%5D+Fix+issues+with+checkpoints%2Fprogress
- https://github.com/orgs/oppia/projects/3/views/8?sliceBy%5Bvalue%5D=%5BProject%5D+Fix+issues+with+RTL+support

**Suggested Milestones:**

- **Milestone 1**: Implement a basic version of the updated topic player page (based on these mocks), and ensure that it is fully responsive for desktop and mobile portrait views. This involves the following steps:
  - Use the feature flag introduced in this PR: https://github.com/oppia/oppia/pull/20406, and also verify that the feature flag has been properly introduced in that PR.
  - Display the topic name and description prominently, along with the associated story name and description.
  - Include a link to the study skills page from the topic page, ensuring the page is accessible and properly styled.
  - Filterable, scrollable sequence of lessons and practices.
    - Displayed the count of lessons and practices
    - Practices should be interspersed in the correct order
    - Correctly suggest what item to work on next. This suggestion should be the default when the page loads and indicated with a green arrow.
    - Dynamic scroll arrow visibility
    - Correct scroll distance
    - Selecting a lesson or practice shows details and links to start, resume, study, or practice, as appropriate
    - Filter status is remembered the next time the user loads the page
  - Maintain a uniform UI consistent with the topic editor page and ensure full responsiveness for both desktop and mobile portrait views.

- **Milestone 2**:
  - Show progress indicators on lessons and practice sessions
  - Show pop-ups when a user returns to an in-progress or completed lesson
  - Implement the “Representation of Chapter Availability” section in the mocks by updating the existing "coming soon" UI and new tag on the chapters.
  - Support secondary language selection, enforced with pop-ups when necessary
  - Persist secondary language choices. At this point, the full language selection algorithm should be implemented

<details>
<summary>Org-admin/tech-lead commentary/advice</summary>

This project is primarily a frontend project, so contributors should be comfortable with Oppia’s frontend stack. This project is a good fit for contributors interested in building a full, user-facing frontend that will directly impact the learner experience.
</details>

<details>
<summary>What we are looking for in proposals</summary>

Consider: 

- How will you support showing multiple stories in the topic page?
- How will you build the new topic page while keeping the old design intact, and how will you make it easy to deprecate the old design and switch over to the new design when needed? Hint: use feature flags!

Some questions to check that you understand the tech stack:

- How will you load the lesson in the preferred language once the user clicks on the Start button?
- Explain how you will ensure that the implemented/updated pages are (a) fully-responsive for all device sizes, (b) reach a Lighthouse score of 100 for accessibility, (c) support RTL layouts, and (d) are fully internationalizable. If possible, link to PRs that demonstrate that you have a good understanding of these areas.

Additional things to discuss in your proposal:

- What are the APIs for the components that you will create (e.g., modal, lesson card, progress bar, practice card, and possibly others)? For each of these, provide a definition of the API interface and an example usage of the component that is associated with a screenshot of one of its instances in the mocks.
- Show a screenshot of the existing "serial chapter launch" functionality running on your local machine, and explain the changes you would make to it to bring it into alignment with the mocks.
- When auditing the mocks and thinking about implementation, you might find that you need to get clarifications on various aspects of the mocks. Include, in your proposal, a list of questions that you have asked / would ask, how they affect the implementation, and the answers to those questions.

</details>

<details>
<summary>Technical hints / guidance</summary>

- For implementing the language and audio on the lesson card, check the approach used in the new lesson player.
- For implementing the progress bar for the lesson card, check the new lesson player’s checkpoint bar.
- To implement the skill progress circle or to determine whether the skill has been completed or not, check the new learner dashboard’s progress tab. In that, skills are implemented that show the progress.
- When fetching multiple entities, do a single GET-MULTI call. Avoid executing a single GET call N times in a for loop.
- To turn on the "coming soon" functionality, you’ll need to flip the "serial chapter launch" feature flag in the /release-coordinator page (you can give yourself permissions for that in /admin > Roles). See Rishi Kejriwal’s project in GSoC 2023 for more details about how this feature works.

</details>

<details>
<summary>Suggested PM demo points</summary>

Milestone 1:

- The overall topic page design has been implemented
- Clicking the study skills link, either from the story header or from a practice, leads to the study skills page. From there, selecting a concept leads to the concept revision page.
- Lessons and practices are shown in the correct order. The user can scroll through them. Check that scroll distances and scrolling availability are correct, given the number of items and screen size.
- Lessons and practices can be selected to show more details.
- Lessons and practices can be filtered, and the state of this filter is remembered the next time the user loads the page.
- All applicable frontend, backend, and acceptance tests have been written and pass robustly.

Milestone 2:

- Progress indicators are displayed, and progress is calculated correctly, for both lessons and practices.
- Users are shown pop-ups when loading in-progress or completed lessons.
- Languages are selected correctly for lessons. This includes secondary language selection and pop-ups.
- All applicable frontend, backend, and acceptance tests have been written and pass robustly.

</details>

## Creators, Operations, Reviewers, and Editors (CORE) team

### 2.1. Automatic translation suggestions

**Project Description:** The lesson content in Oppia is primarily written in English, and the current translation workflow follows a review-and-approval model. Contributors who are familiar with their native language can submit translation suggestions through the contributor dashboard. These suggestions are then reviewed and approved by a translator admin, after which the translated content is stored in the datastore for the respective entities.

This project aims to simplify the contribution process by automatically providing AI-based translation suggestions. Contributors will have the option to accept the suggested translation (and edit it if needed) or reject it. If the AI suggestion is rejected, contributors can add the translation manually, following the existing workflow.

Links to PRD and mocks:
* [Mocks](https://www.figma.com/design/l5CN6GOxtqlZYKrOYBK88p/Automatic-translation-UI?node-id=0-1&t=mKCsNeEwEK1SOsev-1) with the following tweaks:
  * You don't need to highlight the parts of the auto-generated translation that the user changes.
  * To submit the translation, require that the user have looked at the translated alt text for each image. Currently we require this by forcing translators to click on images, which opens a modal showing the alt text, to copy the images into the translation, but that mechanism won't work for automated translations.

**Tracking issues**:

- https://github.com/oppia/oppia/issues/24714

**Not in scope:** This project does not aim to automate the entire translation pipeline. Specifically, when the main content of an entity is modified, translations will not be regenerated automatically. This is intentional, as we want to retain the review-and-approval model in the translation infrastructure so that only approved translations are shown to end users.

Automating the translation pipeline could be explored as a future project, depending on how effective and successful this project proves to be.

**Size:** Medium (\~175 hours)

**Difficulty**: Moderate

**Potential mentors:** @Nik-09

**Product/technical clarifiers:** @U8NWXD (product), @Nik-09 (technical)

**Discussion forum:** https://github.com/oppia/oppia/discussions/categories/gsoc-q-a-2-core-projects

**Required knowledge/skills:**

- Figure out the root cause of an issue and communicate it well using a debugging doc.
- Debug and fix CI failures/flakes.
- Write Python code with unit tests.
- Write TS + Angular code with unit tests.
- Write or modify e2e/acceptance tests.
- (maybe, depending on your technical approach) Write or modify Beam jobs.

**Related issues:**

- Contributors can work on something from this list to understand the translation workflow: https://github.com/orgs/oppia/projects/18/views/4?sliceBy%5Bvalue%5D=%5BProject%5D+Fix+issues+in+the+main+translator%2Fquestion+opportunities+dashboard
- Full-stack related issues: https://github.com/oppia/oppia/issues?q=state%3Aopen%20label%3Afull-stack
- https://github.com/oppia/oppia/issues/16837

**Suggested Milestones:**

- **Milestone 1**:
  - Build backend infrastructure to generate automatic translations for entities. The infrastructure should be flexible enough to support adding or removing languages used for translation generation.
  - Build the backend infrastructure to store the generated translations in a cache model to avoid multiple translation generations of the same content in a language.
  - The translations should be generated on the fly while contributors add translation suggestions from the Contributor Dashboard. Please have a look at the Figma mocks for more clarity.
  - Use the Azure Translator SDK ([reference](https://learn.microsoft.com/en-us/azure/ai-services/translator/text-translation/quickstart/client-library-sdk?pivots=programming-language-python)) to generate translations for Oppia content. The translation configuration should be flexible and language-specific, allowing us to define which service is used for each supported language.
  - This design should make it easy to onboard additional third-party translation providers in the future (for example, GCP), with minimal code changes. A JSON-based configuration can be used to map languages to translation platforms such as Azure or GCP.
  - Develop full-stack functionality to enable the addition and removal of languages from the translator admin page (the UI will be very similar to the existing voiceover admin page), supporting automatic translation generation.


- **Milestone 2**: Contributors should be able to view AI-based translation suggestions in the Contributor Dashboard. They should be able to submit translations by fully accepting the suggested AI translation, accepting it after making edits, or rejecting it entirely and providing a manual translation instead. If translators don't click the "Auto-Translate" button, everything should work as it did before the auto-translation project.

<details>
<summary>Org-admin/tech-lead commentary/advice</summary>

This project implements a full-stack, largely self-contained feature that has the potential to immediately improve the translator experience. The selected contributor will likely work with the translation team to get feedback, so this project is great for those who value seeing the impact of their work quickly. This project has a little of everything, from backend architecture design to frontend UI work.

</details>

<details>
<summary>What we are looking for in proposals</summary>

- A structured and extensible design that supports multiple translation services in the future, beyond the current Azure-based implementation, with the ability to configure translation providers on a per-language basis.
- Comprehensive examples demonstrating successful translations using Azure for Oppia content, including math, images, and other Oppia interactions.
- A detailed end-to-end implementation plan, covering the process from generating translations using the Azure Translator SDK to surfacing translation suggestions in the frontend UI.

</details>

<details>
<summary>Technical hints / guidance</summary>

Caching automatic translation: 
- Each piece of content is translated in the backend and displayed on the CD dashboard when the user submits a translation. Instead of calling the third-party service (Azure, in this case) every time, we can store the generated translations in the datastore.
- This way, if another exploration — or even the same exploration — contains identical content, we can reuse the previously generated translation instead of sending a new request to the external service. This approach reduces both processing time and cost.
- To implement this, we can:
  - Generate a hash of the original English content.
  - Store the hash along with the original content, target language code, and the generated translation in the datastore.
  - When a new translation request is received, first check whether a matching hash entry already exists.
  - If a match is found, reuse the stored translation instead of calling the third-party API.
  - Ensure proper handling of potential hash collisions.
- This optimization improves efficiency, reduces redundant API calls, and lowers overall operational costs.


How to make changing third-party translation provider easy
- There are multiple ways to implement this. The simplest approach would be to maintain a JSON configuration file in the codebase that maps each language to the third-party provider used for automatic translation regeneration. Then create backend objects or functions that handle querying the third-party provider and present a common interface to the rest of our backend code so we can easily swap them out.
- A similar approach has already been implemented for automatic voiceover regeneration. You can refer to the autogeneratable_language_accent_list.json file in the assets directory of the codebase as a reference.

</details>

<details>
<summary>Suggested PM demo points</summary>

Milestone 1:

- The translation admin page should successfully support adding and removing languages for automatic translations, enabling/disabling the overall translation suggestions functionality.
- The translation admin page should support changing the automatic translation service used for any language. 
- Should be able to show the generated translations for selected entities and log the output either in the console or terminal. 
- Additionally, the quality of the generated translations must be reviewed and approved by the translation team to ensure they meet the standards of the existing content translation in the respective language.
- All applicable frontend, backend, and acceptance tests have been written and pass robustly.

Milestone 2:

- Demonstrate the complete end-to-end workflow, showing how AI-based translation suggestions are generated, modified, and accepted by contributors, followed by how translator reviewers approve the suggested translations without altering the existing review flow.
- All applicable frontend, backend, and acceptance tests have been written and pass robustly.

</details>

### 2.2. Extend translation infrastructure to exploration metadata and skills

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:** Currently, we have two main mechanisms for translating content at Oppia: translatewiki and the contributor dashboard. Translatewiki handles content that is not user-generated, for example the text on the homepage at oppia.org. The goal of this project is to extend the contributor dashboard to handle other kinds of user-generated content in our curated curriculum, specifically the following:

- exploration metadata (e.g. titles and tags)
- skill (concept card) content

The finished product should also be easily extended to other kinds of content in the future, for example:

- topic metadata
- story metadata
- study guide content

At a high level, this project consists of:

- Displaying all translatable opportunities of the new entities in the contributor dashboard.
- Displaying all reviewable translated suggestions in the reviewer dashboard.
- Displaying translated contents to learners when a language other than English is selected.

Links to PRD and mocks: We have a full TDD instead of a PRD: docs.google.com/document/d/1cFJ6weoOWPopLFpRf2lw4RRPPNFVJ4QVLqdxb_WsLyY/edit. You are welcome to draw inspiration from the TDD, but you should not assume that its suggested approach is best. We expect you to critically evaluate it and suggest deviations when appropriate.

**Tracking issues**:

- https://github.com/oppia/oppia/issues/22793
- https://github.com/oppia/oppia/issues/24933

**Not in scope:** 

- Supporting translation of content outside our curated curriculum, for example user profiles or explorations that aren’t connected to a topic.
- Supporting translation of entities besides exploration metadata and skill content.
- Actually doing the translations. This project is just about creating the infrastructure and interface that will support the translation team in doing the actual translations.

**Size:** Large (\~350 hours)

**Difficulty**: Hard

**Potential mentors:** @chris7716 and @masterboy376

**Product/technical clarifiers:** @chris7716 (product), @chris7716 (technical)

**Discussion forum:** https://github.com/oppia/oppia/discussions/categories/gsoc-q-a-2-core-projects

**Required knowledge/skills:**

- Figure out the root cause of an issue and communicate it well using a debugging doc.
- Debug and fix CI failures/flakes.
- Write Python code with unit tests.
- Write TS + Angular code with unit tests.
- Write or modify e2e/acceptance tests.
- Write or modify Beam jobs.
- Architecting extensible code infrastructure

**Related issues:**

- Bugs in https://github.com/orgs/oppia/projects/18/views/4?sliceBy%5Bvalue%5D=%5BProject%5D+Expand+translation%2Fvoiceover+opportunities+to+include+all+user-created+content
- Translation issues in https://github.com/orgs/oppia/projects/18/views/4?sliceBy%5Bvalue%5D=%5BProject%5D+Fix+issues+for+translation%2Fquestion+coordinators
https://github.com/orgs/oppia/projects/18/views/4?sliceBy%5Bvalue%5D=%5BProject%5D+Fix+issues+affecting+translation+reviewer+workflows

**Suggested Milestones:**

- **Milestone 1**: Build the extensible translation infrastructure and migrate the translations currently supported by the contributor dashboard (i.e. exploration non-metadata content) to use it.

- **Milestone 2**: Exploration metadata and skill content can be translated through the contributor dashboard, and all legacy code related to the old translation system has been removed.

<details>
<summary>Org-admin/tech-lead commentary/advice</summary>

This is a complicated project that primarily consists of backend changes, plus some changes to the frontend code to keep it compatible with the new backend. We expect minimal changes to the user interface. Contributors skilled in the creation of modular, extensible frameworks will likely be particularly well-suited for this project. The first milestone, implementing the extensible framework, is the most critical and the trickiest. Mistakes here will lead to problems extending the framework to other entity types in the second milestone. We think most of the technical issues have been thought through and solved already, which both reduces the amount of planning and design work required of the contributor, and also may help avoid technical issues derailing the project.

</details>

<details>
<summary>What we are looking for in proposals</summary>

A TDD has already been drafted for this project, so we’ll be looking for evidence that applicants deeply understand the proposed approach and have critically evaluated it. Read the TDD closely, consider whether you think the approach makes sense, and reach out to us with questions and alternative ideas. The solution in the TDD might not actually be the best, and pointing out issues with the TDD is a great way to show you really understand it. Further, the TDD gives a rather high-level explanation of some parts of the project, for example what changes will be required to show translations of the newly-translated entities to users. Your proposal should delve into the details of these parts. We've also had a number of issues with keeping translation counts up-to-date (see https://github.com/oppia/oppia/issues/21878), so you should address how you plan to avoid similar issues in your project.

</details>

<details>
<summary>Technical hints / guidance</summary>

We’ve already put a good amount of thought into the technical details. See the TDD for our proposed plan.

</details>

<details>
<summary>Suggested PM demo points</summary>

Milestone 1:

- The contributor dashboard works like it did before. Opportunities are surfaced for translators, translators can submit translations, reviewers can review them, and accepted translations are displayed to users.
- Topic filtering for translators and reviewers works.
- While the contributor dashboard user experience hasn’t changed, it is now implemented using an extensible infrastructure that we can easily extend to the rest of the user-generated content in our curated curriculum.
- All applicable frontend, backend, and acceptance (unlikely to change much) tests have been written and pass robustly.

Milestone 2:

- Opportunities for user-generated content in the curated curriculum are surfaced for translators, translators can submit translations, reviewers can review them, and accepted translations are displayed to users. Check that the following kinds of content can be translated:
  - exploration metadata (e.g. titles and tags)
  - skill (concept card) content
- Translators and reviewers can filter by topic
- All applicable frontend, backend, and acceptance (unlikely to change much) tests have been written and pass robustly.
- The translation infrastructure is extensible to easily support new kinds of content.

</details>

## Developer Workflow Team

### 3.1. Improve acceptance test infrastructure

**Project Description:** [Acceptance tests](https://github.com/oppia/oppia/wiki/Acceptance-Tests) are end-to-end tests organized by Critical User Journeys (CUJs). However, these tests are not as stable as we are expecting them to be. This project aims to improve the infrastructure of the acceptance tests to make it more stable and easy to manage. This includes but is not limited to migrating to Playwright from Puppeteer to reduce test flakiness, adding workflows to easily update snapshots, and documentation updates. Further, we expect using Playwright to reduce test flakiness, but some flakes will likely persist. This project includes fixing these persistent flakes. To limit the scope of this part of the project, you won't be expected to fix more than 10 persistent flakes (i.e. flakes that aren't fixed by the migration and weren't introduced by your changes). All of the acceptance test infrastructure issues can be found [here](https://github.com/orgs/oppia/projects/8/views/11?sliceBy[value]=[Project]+Fix+infrastructure+issues+in+the+acceptance+tests).

**Tracking issues**:

- Finish removing webdriverio tests: https://github.com/oppia/oppia/issues/23871
- Migrate to Playwright: https://github.com/oppia/oppia/issues/24715
- Document how to debug acceptance tests:
  - https://github.com/oppia/oppia/issues/16136
  - https://github.com/oppia/oppia/issues/22319
  - https://github.com/oppia/oppia-web-developer-docs/issues/422
- Infrastructure issues:
  - Jest not exiting on time: https://github.com/oppia/oppia/issues/22251
  - Assert expected console errors are present: https://github.com/oppia/oppia/issues/12770
  - Give better error message when an element isn't clickable: https://github.com/oppia/oppia/issues/20142
  - Method overriding issue in UserFactory: https://github.com/oppia/oppia/issues/22539
  - Detect server errors: https://github.com/oppia/oppia/issues/21644
  - Browser disconnecting: https://github.com/oppia/oppia/issues/22193
  - We should not fast-fail on snapshot mismatches: https://github.com/oppia/oppia/issues/23776
  - Capture screen recordings on CI for mobile tests: https://github.com/oppia/oppia/issues/23155
- Flakes (which flakes are problematic may change over time):
  - https://github.com/oppia/oppia/issues/22174
  - https://github.com/oppia/oppia/issues/23106

**Not in scope:** Writing new acceptance tests to increase coverage.

**Size:** Medium (\~175 hours)

**Difficulty**: Easy

**Potential mentors:** @jayam04

**Product/technical clarifiers:** @U8NWXD (product), @jayam04 (technical)

**Discussion forum:** https://github.com/oppia/oppia/discussions/categories/gsoc-q-a-3-dev-workflow-projects

**Required knowledge/skills:**

- Figure out the root cause of an issue and communicate it well using a debugging doc.
- Debug and fix CI failures/flakes.
- Make changes to GitHub Actions workflows.
- Write Python code with unit tests.
- Write or modify e2e/acceptance tests.
- Fixing acceptance test flakes.

**Related issues:**

- https://github.com/oppia/oppia/issues/23871

**Suggested Milestones:**

- **Milestone 1**: Initialize and set up Playwright infrastructure to work in parallel with Puppeteer tests. Migrate all acceptance tests (described in our CUJ trackers for [internal](https://docs.google.com/spreadsheets/d/1DIZ0_Gmf9uhjTbhuDpA495PTjYZW9ZE97r6urS-iXwg/edit) and [external](https://docs.google.com/spreadsheets/d/1IrxN13IC5xwWdAFnGMu_4p3FU1ADL4QO-eLZIuTowIA/edit) users) to the Playwright framework. You may find the [Playwright team's official migration guide](https://playwright.dev/docs/puppeteer) helpful. Remove puppeteer infrastructure by ensuring python scripts and CI run every test using Playwright, and remove unused dependencies. Fix method overriding issue in UserFactory. Additionally, if webdriverio tests are not removed by GSoC start date, contributors will need to migrate webdriverio tests to Playwright in place of some infrastructure issues.

- **Milestone 2**: Update test to not fast-fail on snapshot mismatch but complete the test steps before failing. Fix screen-recording failing in mobile tests. Add a guide for debugging flaky acceptance tests. Fix 10 acceptance test flakes.

<details>
<summary>Org-admin/tech-lead commentary/advice</summary>

This project is straightforward, however some level of CI understanding is required. Thus, folks with experience in Acceptance tests (writing and/or debugging) will be a good fit. There are a lot of tests, so folks taking shorter time in repetitive tasks will benefit.
</details>

<details>
<summary>What we are looking for in proposals</summary>

For this particular GSoC project, the proposal is less important and we are more interested in your previous PRs. In particular, each of the following can significantly enhance your application:

- Tackling at least one PR that solves a part of #23871.
- Fixing some issues on acceptance tests infrastructure in the [Improve workflow for updating acceptance test screenshots](https://github.com/orgs/oppia/projects/8/views/11?sliceBy[value]=[Project]+Improve+workflow+for+updating+acceptance+test+screenshots) and [Fix infrastructure issues in acceptance tests](https://github.com/orgs/oppia/projects/8/views/11?sliceBy%5Bvalue%5D=%5BProject%5D+Fix+infrastructure+issues+in+the+acceptance+tests) themes on the dev workflow project board.
- Showing at least one debugging doc that correctly diagnoses the root cause of an e2e/acceptance flake.
- Making at least one PR that resolves at least one E2E/acceptance flakiness issue (many of these are collected here).

Some things you should address in your proposal:

- How will you support the Playwright and Puppeteer framework simultaneously? Explain changes you will make in python scripts and the config file ([`acceptance.json`](https://github.com/oppia/oppia/blob/develop/core/tests/ci-test-suite-configs/acceptance.json)).
- Important parts of code that you need to take care of while migrating from Puppeteer to Playwright. E.g., Changing usage of ElementHandle to Locator.
- How will you break down this project into individual sub-milestones? Provide a clear timeline for this.
- How will you set up your debugging cycle so that you can easily figure out what is going wrong with a test, or fix a flake in it? Explain this for both (a) local development, and (b) getting a test to pass in the CI environment.
</details>

<details>
<summary>Technical hints / guidance</summary>

- Create a separate directory for Playwright tests, then migrate tests from Puppeteer to Playwright. In doing so, the contributor needs to make sure that the common code is always in sync. There can be conflicts - for instance when a function is used by tests in both Puppeteer and Playwright frameworks, changes to the function in any will create conflicts when we migrate remaining tests. This can be prevented by simply not allowing any function modification once we start migrating.
- Update and use “Stress test (Acceptance test)” workflow to ensure that every new test is flake free.
- Contributors should migrate to Playwright with as few changes as possible first. Then, once Puppeteer is completely removed, they can work on critical parts such as replacing all `ElementHandle` instances with `Locator`.
- Initially, edit the `acceptance.json` config file to specify whether each test should be run under Puppeteer or Playwright. This will allow CI to run smoothly without requiring extensive changes as everything will be handled by Python script.
</details>

<details>
<summary>Suggested PM demo points</summary>

Milestone 1:

- Running an acceptance test using python -m scripts.run_acceptance_tests should run acceptance tests in the Playwright framework. No acceptance test should use Puppeteer framework, and all the unused Puppeteer dependencies must be removed (i.e. Puppeteer Video Recording package).
- CI should run all acceptance tests using Playwright framework and Internal User journeys using Puppeteer framework
- Method overriding in UserFactory should throw an error.

Milestone 2:

- Every mobile acceptance test should record a complete test. (Can be verified by stress testing an acceptance test).
- Running a test with snapshot mismatch, the test should take all steps after comparison and throw a snapshot mismatch error at the end. Test should also upload new snapshot taken as artifact.
- We should have complete documentation on acceptance tests including updating screenshots, etc.
- 10 acceptance test flakes have been resolved, and their tests now pass robustly.

</details>

### 3.2. Consolidate entity migration jobs

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:**

The Oppia codebase includes several different versioned entities which store learning material: explorations, skills, stories, subtopic pages, questions, topics, and collections. The infrastructure to maintain each of these versioned entities has been developed separately, and is a bit patchy (for example, migrations of old snapshots have not been implemented for some of the entities). This is making it difficult to remove some of the old version upgrade functions in the codebase which are no longer needed.

The aim of this project is to standardize these migration jobs so that there is a single, standard way to migrate and upgrade versioned models. This will (a) ensure that all the versioned models can be easily updated on a periodic basis, (b) let us delete the code for upgrading from old versions once all the entities of that version have been upgraded, and (c) simplify the remaining version upgrade code.

**Tracking issues**: [#22023](https://github.com/oppia/oppia/issues/22023)

**Size:** Medium (\~175 hours)

**Difficulty**: Moderate

**Potential mentors:** @kevintab95

**Product/technical clarifiers:** @U8NWXD (product), @kevintab95 (technical)

**Discussion forum:** https://github.com/oppia/oppia/discussions/categories/gsoc-q-a-3-dev-workflow-projects

**Required knowledge/skills:**
- Figure out the root cause of an issue and communicate it well using a [debugging doc](https://github.com/oppia/oppia/wiki/Debugging-Docs).
- Write Python code with unit tests.
- Write or modify Beam jobs, with tests.

Additionally, strong technical design skills and a good sense of code architecture are helpful.

**Related issues:**

- [#16556](https://github.com/oppia/oppia/issues/16556) is a good issue to look into, since it will help you become familiar with the migration job infrastructure.
- [Issues related to Beam jobs](https://github.com/oppia/oppia/labels/Beam%20jobs) are also good ones to look at.


**Suggested Milestones:**
- **Milestone 1**: Create a BaseVersionedDomainObject which specifies object member mappings to storage model properties in a declarative way, and also specifies the "schema version field" corresponding to each JsonProperty-related field. Add tests to ensure that all JsonProperties are accounted for. Then, replace all existing domain objects for versioned models with subclasses of BaseVersionedDomainObject. Additionally, ensure that all functions that convert storage models to domain objects also migrate domain objects to the latest schema version.

- **Milestone 2**: Create BaseMigrateVersionedModelJob and BaseMigrateVersionedModelSnapshotsJob classes with the core logic for upgrading models and snapshots to the latest schema versions, respectively. Use these to build both job and audit job subclasses for all versioned models (explorations, skills, stories, subtopic pages, questions, topics, collections) with proper logging and error reporting (e.g. if a migration fails, the model that could not be migrated should be logged for debugging). Test these jobs on production data to ensure that they work correctly, and fix any issues that arise. Finally, run all the jobs in all our production environments, so that all the models and snapshots on the server are upgraded to the latest schema versions, then remove the old jobs and the old conversion functions for all 7 versioned models, as well as the methods they call (similar to what was done in https://github.com/oppia/oppia/pull/12256/files).


<details>
<summary>Org-admin/tech-lead commentary/advice</summary>

This project requires a very good understanding of how our migration pipeline works, and a solid grasp of technical architecture so that you can make good design decisions for how the base classes and their subclasses are structured. However, once that is well-understood, it should not be too difficult to implement. You will probably find deleting all the old code at the end quite satisfying!
</details>

<details>
<summary>What we are looking for in proposals</summary>

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

- There are existing jobs and audit jobs in the codebase for migrating models and snapshots (e.g. MigrateExplorationJob, ExpSnapshotsMigrationAuditJob, etc.). All these should be deleted at the end of the project. This old wiki page with instructions for writing schema migrations might also provide some useful background: https://github.com/oppia/oppia/wiki/Writing-state-migrations

- The bulk of the logic for all the new jobs should be in the two base classes, BaseMigrateVersionedModelJob and BaseMigrateVersionedModelSnapshotsJob. In general, if some functionality is common to all versioned models, it should be included in the base class, otherwise it should be defined in the relevant subclass(es). Ideally, the subclasses would just point to the relevant storage models / domain object classes and not include any custom logic – see `SNAPSHOT_METADATA_CLASS` in `ExplorationModel` for an example of this. The corresponding audit jobs for these two jobs should be trivial subclasses of the main jobs with `DATASTORE_UPDATES_ALLOWED = False`. (Look at the usage of `DATASTORE_UPDATES_ALLOWED` in the codebase for more information.)

- Part of this project includes standardizing the infrastructure for migrating JSON properties. Here is a more detailed technical sketch for how this could be done:

  - Create a BaseVersionedDomainObject whose subclasses declaratively specify a mapping from any versioned field to its corresponding schema version field. (These fields correspond to `JsonProperty` in the datastore's storage model.) Un-versioned fields of type `Dict` or `List[Dict]`` should be explicitly declared as un-versioned. Subclasses must also reference constants in feconf.py that specify the minimum and maximum version of each field.

  - Write backend tests that:
    - Identify all subclasses of BaseVersionedDomainObject in the codebase and verify that every `Dict` or `List[Dict]`` field contained in the object is either included in the mapping mentioned above or included in a list of un-versioned fields. This ensures that all versioned domain objects have the necessary infrastructure for performing schema upgrades for their respective JsonProperties.
    - Ensure that the relevant migration functions for each upgradable field are present in the corresponding domain object class with the function signatures (including type hints). Specifically, each conversion function should accept one parameter of the same type as the versioned field and should return one value of the same type. The migration functions can be named using a standard scheme, e.g. `_convert_{{field_name}}_v{{x}}_dict_to_v{{x+1}}_dict`, and the backend test can check for that. This test should also use the minimum and maximum schema versions to check that upgrade functions from the minimum up to the maximum version are present.

  - Add a `migrate_to_latest_schema_versions` function to BaseVersionedDomainObject to handle schema upgrades in a generalized way across all domain objects.
  - Ensure that all the different getter functions in the _services/fetchers.py files that convert storage models to domain objects also use `migrate_to_latest_schema_versions` to translate that object’s fields to use the latest schema versions.
  - Replace all domain objects corresponding to VersionedModels with the new BaseVersionedDomainObject.

- Here's a schematic depiction of a possible end state for versioned domain models:

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
</details>

<details>
<summary>Suggested PM demo points</summary>

- Milestone 1: At least one domain object is using BaseVersionedDomainObject, and all the get/save functionality works correctly. All applicable frontend, backend, and acceptance tests have been written and pass robustly.

- Milestone 2: All jobs run correctly on the backup server. All applicable frontend, backend, and acceptance tests have been written and pass robustly.
</details>


### 3.3. Standardize and validate domain objects and storage models

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:**

Oppia's production data is organized using [NDB storage models](https://github.com/oppia/oppia/wiki/Storage-models#storage-model-concepts), which in simple terms can be thought of as objects having different properties. For instance, data related to a user can be stored in a UserSettingsModel with properties like username, user ID, etc.

Different inter-model relationships exist as well, corresponding to relationships between prod data. For instance, a story includes a list of explorations. So, a StoryModel might include the IDs of all the ExplorationModels it is composed of.

For proper functioning of the Oppia application, it is important to ensure that all the models are internally consistent and that the relationships between models are valid. The aim of this project is therefore to ensure that all production data is valid by:

  - Ensuring that domain objects exist for all prod models, and that they have full `validate()` functions.

  - Implementing Beam jobs that audit production data and flag any errors. These jobs should validate the model properties as well as inter-model relationships. After these jobs are run, any errors should be investigated, and checks should be implemented to ensure that such problems don’t reoccur in the future with new data.

**Tracking issues**:
- [#21970](https://github.com/oppia/oppia/issues/21970)
- [#21905](https://github.com/oppia/oppia/issues/21905)
- [#21869](https://github.com/oppia/oppia/issues/21869)

**Not in scope:** Migrating existing datastore data to address the validation issues found in the first milestone.

**Size:** Large (\~350 hours)

**Difficulty**: Moderate

**Potential mentors:** @ankita240796

**Product/technical clarifiers:** @U8NWXD (product), @ankita240796 (technical)

**Discussion forum:** https://github.com/oppia/oppia/discussions/categories/gsoc-q-a-3-dev-workflow-projects

**Required knowledge/skills:**
- Figure out the root cause of an issue and communicate it well using a [debugging doc](https://github.com/oppia/oppia/wiki/Debugging-Docs).
- Write Python code with unit tests.
- Write or modify Beam jobs, with tests.


**Related issues:**

- https://github.com/oppia/oppia/issues/21970
- https://github.com/oppia/oppia/issues/21905
- https://github.com/oppia/oppia/issues/21869
- The first checkbox item from any of the following:
  - https://github.com/oppia/oppia/issues/14968
  - https://github.com/oppia/oppia/issues/14967
  - https://github.com/oppia/oppia/issues/14969
  - https://github.com/oppia/oppia/issues/14971
  - https://github.com/oppia/oppia/issues/14972


**Suggested Milestones:**

- **Milestone 1**: Domain objects exist for all storage models, and include validate() methods that fully validate the domain object's internal consistency and correctness. The usage of storage models in the domain layer is restricted to the interfaces for getting and saving datastore models, and they are not passed further around the codebase. 50% of the validation jobs for the storage models are implemented and run successfully. For each validation error found, an issue is filed with clear action steps for (a) stopping the error from happening for new data, and (b) migrating old data to fix the error.

- **Milestone 2**: All remaining validation jobs for the storage models are implemented and run successfully, and issues are filed for all validation errors as described in Milestone 1. All root causes of the validation issues found in Milestones 1 and 2 are identified and fixed, so that the error no longer happens for new data. (This corresponds to part (a) of each issue in Milestone 1.)


<details>
<summary>Org-admin/tech-lead commentary/advice</summary>

This project is relatively straightforward if you can identify the validation checks correctly and are able to analyze the codebase to figure out why incorrect data is being written. The [design brief](https://docs.google.com/document/d/1u45oC6igsaTvQl4oNd8VvDiZe3JqeY3m_5n4QZ6d4rA/edit?usp=sharing) provided in the technical hints should help provide a lot of the necessary structure. Note that the validation requirements for the different models can vary greatly in terms of difficulty.
</details>

<details>
<summary>What we are looking for in proposals</summary>

For your proposal, please include the following:

  - A complete list of all storage models, with “validity” clearly defined for (a) the corresponding domain objects, (b) the models themselves (including inter-model relationships).

  - How you would structure the sub-milestones to enable you to run jobs efficiently on the server in batches.

  - A worked example of how you would do each part of the project (domain-object creation, only using storage models in get/put, writing a validation job, filing the GitHub issue, fixing the root cause). You can link to sample PRs if you like. For the purposes of this illustration, we suggest that you pick one or two "average" or "hard" examples – try not to pick a trivial model.

  - Any complicated cases you identify for any of the above steps, and an explanation of how you would tackle them. (For example, customization arg validation for interactions.)

  - An explanation of how you would ensure/verify that storage models are not used beyond the get and save functions in the `*_services.py` file. (For example, you might come up with a standard pattern for get/save that you can implement universally to make that verification easy to do, or you might analyze import statements that involve to the storage layer, or you might add a backend test to ensure that ndb.Model instances are not passed beyond specific functions.)


We also recommend taking up at least one checkbox item from each of the following, in order to confirm that this project is a good fit for you:
  - https://github.com/oppia/oppia/issues/21970
  - https://github.com/oppia/oppia/issues/21869
  - The first checkbox from any of the following (to demonstrate ability to “identify the root cause of an error and stop it from happening”):
    - https://github.com/oppia/oppia/issues/14968
    - https://github.com/oppia/oppia/issues/14967
    - https://github.com/oppia/oppia/issues/14969
    - https://github.com/oppia/oppia/issues/14971
    - https://github.com/oppia/oppia/issues/14972

</details>

<details>
<summary>Technical hints / guidance</summary>

- Please go through the following guides in the Oppia wiki:

  - [Storage models](https://github.com/oppia/oppia/wiki/Storage-models#storage-model-concepts)
  - [Testing jobs and other features on production](https://github.com/oppia/oppia/wiki/Testing-jobs-and-other-features-on-production)
  - [Debugging datastore locally](https://github.com/oppia/oppia/wiki/Debugging-datastore-locally)
  - [Apache Beam Jobs](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) · oppia/oppia Wiki · GitHub
    - Note that, in general, any Beam jobs you write should be **idempotent**, i.e., running them twice should result in the same outcome as running them once. This allows us to just rerun them if a job fails for some reason (e.g. due to an internal Beam error).

- See [this design brief](https://docs.google.com/document/d/1u45oC6igsaTvQl4oNd8VvDiZe3JqeY3m_5n4QZ6d4rA/edit?usp=sharing) for a design approach that you can follow for the validation jobs.

- To understand how validation jobs work, you might like to take a look at the existing [audit and validation jobs](https://github.com/oppia/oppia/tree/develop/core/jobs/batch_jobs). Some examples:
  - https://github.com/oppia/oppia/blob/develop/core/jobs/batch_jobs/user_validation_jobs.py
  - https://github.com/oppia/oppia/blob/develop/core/jobs/batch_jobs/blog_validation_jobs.py
</details>

<details>
<summary>Suggested PM demo points</summary>

- Milestone 1: Validation jobs for at least 5 prod models are written & run, and errors arising from those jobs have been filed as issues on GitHub. All applicable frontend, backend, and acceptance tests have been written and pass robustly.

- Milestone 2: A full list of errors is compiled with clear action items. All applicable frontend, backend, and acceptance tests have been written and pass robustly.
</details>

## Android team

### 4.1 Support for Lesson Progress, Study Guides, and Worked Examples

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:**
This project is two smaller user-facing improvements combined into a single project.

The first part is completing the work that began in https://github.com/oppia/oppia-android/pull/5388 to address https://github.com/oppia/oppia-android/issues/4652. The Android app supports users exiting a lesson early and resuming where they left off later. However, they are unable to monitor their progress through the lesson and this has come up repeatedly in user feedback. As mentioned in [this discussion thread](https://github.com/oppia/oppia-android/pull/5388#discussion_r1593148545) the Oppia web platform already supports annotating exploration states with a property for whether the [card is a checkpoint](https://github.com/oppia/oppia/blob/5ebbb3d369532a22ee1638a810d597ffb9719594/core/domain/state_domain.py#L3615). This is crucial because showing progress isn't as simple as counting the number of cards the user completed and representing that out of the total number of cards: explorations are dynamic. Users may go down diverging pathways through their lesson experience since the lesson may have a branch with multiple cards to review a concept that the user doesn't fully understand. Instead, we need to provide a means of showing progress that accounts for this dynamic structure using the checkpoints as key points.

Note that one aspect of this that's a bit challenging is that the exact mocks are not defined for how this screen should look. 

The second part of this project is introducing support for study guides and worked examples, both of which the Oppia web platform now supports. In particular:
- Study guides are a change to the existing 'revision cards' in the app that introduce multiple sections with section headers.
- Worked examples are rich text components that are meant to provide a collapsible box with a "question" and "answer" that the user can view if they want to see an example.

In Android, we want to implement study guides in a way that looks similar to Oppia web (see [this Figma project](https://www.figma.com/design/xVkmX0xZdNCpj9CP7ec6pG/Learner-View-of-Revision-Card?node-id=0-1&t=Lt8v5o8bmEg0X1ct-1)).

Worked examples, however, are quite challenging to implement in the way that Oppia web does because the app currently translates custom rich text components to Android `Spannable`s (see [`HtmlParser`](https://github.com/oppia/oppia-android/blob/191e15dafcc073061941ce64fdd7b999363064e9/utility/src/main/java/org/oppia/android/util/parser/html/HtmlParser.kt#L75)), and interactive spannables are very difficult to implement without substantial accessibility problems. The team assumes that this can only be solved with a complete reworking of how HTML tags are handled which is outside the scope of this project. Instead, this project will require introducing a new in-app tag handler that inlines the worked example question and answer in a way that matches how lesson authors represented this before and in a way that's translatable and works for RTL languages like Arabic. Essentially, a worked example with the tag `<oppia-noninteractive-workedexample question-with-value="&amp;quot;&amp;lt;pre&amp;gt;&amp;lt;p&amp;gt;lorem ipsum&amp;lt;/p&amp;gt;&amp;lt;/pre&amp;gt;&amp;quot;" answer-with-value="&amp;quot;lorem ipsum&amp;quot;"></oppia-noninteractive-workedexample>` would be rendered into two lines with block spacing:

```html
<p>
<strong>Question</strong>:
<br>
<pre><p>lorem ipsum</p></pre>
</p>
<p>
<string>Answer</strong>:
<br>
lorem ipsum
</p>
```

Some important things to note for both projects:
- The lesson progress does not have exact mocks defined yet. Proposals need to include mocks and, if accepted, these will be refined durnig the community bonding period in collaboration with the product and Android UX design teams.
- Study guides do not have exact mocks and the implementation will be based off of the mobile web mocks. This means that extra time should be baked into implementation for UI adjustments that are suggested during the code review and evaluation periods.
- Worked example questions and answers can themselves include HTML which then needs to be interpreted into spans and properly inlined. There are no other tags supported by the Android app that can embed HTML in this way.
- All of this functionality must be gated behind feature flags (three in total for each feature).

**Tracking issue**: https://github.com/oppia/oppia-android/issues/6104

**Not in scope:**
- Implementing the full box-like UI and collapsible sections that Oppia web has for worked examples.
- Updating checkpointing to use state checkpoints rather than storing progress at each step in the exploration.

**Size:** Medium (\~175 hours)

**Difficulty**: Moderate-Easy (not quite 'Easy' because the product specification is not 100% defined so there's some uncertainty)

**Potential mentors:** @MohitGupta121

**Product/technical clarifiers:** @BenHenning (product & technical), @MohitGupta121 (technical)

**Discussion forum:** https://github.com/oppia/oppia-android/discussions/categories/gsoc-q-a-4-android-projects

**Required knowledge/skills:**
- Figure out the root cause of an issue and communicate it well using a [debugging doc](https://github.com/oppia/oppia/wiki/Debugging-Docs).
- Build the app and install it on a local device or emulator. Then verify that you can:
  - (a) build a non-test library target locally
  - (b) run a unit test locally
  - (c) play through the app locally
- Write new Kotlin code with unit tests.
- Change Android UIs, write tests for them, and manually verify that they work.

**Related issues:**
- https://github.com/oppia/oppia-android/issues/5039
- https://github.com/oppia/oppia-android/issues/4235
- https://github.com/oppia/oppia-android/issues/4742
- https://github.com/oppia/oppia-android/issues/4754
- https://github.com/oppia/oppia-android/issues/6019

**Suggested Milestones:**

- **Milestone 1**:
  - Introduction of three new feature flags: lesson progress visualization, study guides, and worked examples.
  - Support for lesson progress visualization gated behind the feature flag.
  - Support for the new study guides experience, gated behind the study guides feature flag.
  - Completed QA testing for both features with all bugs triaged (see below for note on launch readiness).

- **Milestone 2**:
  - Support for worked examples, gated behind the worked examples feature flag.
  - Completed QA testing for the worked examples feature (see below for note on launch readiness).
  - Bugs fixed for all three features.
  - Launch all three features.
 
**Important** note on launch readiness: we want this project to include fully launching all three features which means the milestones must be scheduled such that there's sufficient time for QA testing (which will require 2 weeks time), fixing bugs, and completing product reviews of the features early enough for the features to be completed before the next app release is cut. Exceptions cannot be made for late work here because the release process may be automated by this point in the summer (milestone 2).

<details>
<summary>Org-admin/tech-lead commentary/advice</summary>

This is a really nice project for building general familarity with some typical and some atypical Android development in the Oppia Android codebase. It involves building three features basically from scratch and seeing them completely to launch. This is possible only because all three features are individually small, so it's a unique opportunity to learn and see the end-to-end completion process of a full feature three times over.

All three features also touch on critical learning pathways but also aren't 100% defined from a product or UX perspective. This means the contributor will actually get to have a say in how the features should each behave (with guidance from other team members).

</details>

<details>
<summary>What we are looking for in proposals</summary>

- A description for how lesson progress will be represented in both the UI and what dataflow changes will be required (in `EphemeralState` and `ExplorationProgressController`).
- An explanation for how the new study guide structure will be represented in the UI (using a `RecyclerView` conformant to other patterns used in the app).
- An explanation for how the custom worked examples handler will both handled the fact that answer & question text can itself be HTML, and how the generated spannables will then be reinserted into the final outer HTML string with the required format mentioned above and in a way that supports translations and RTL layouts.
- Details on which test lesson assets will be changed and how in order to test all three features.
- Details on all test plans (lists of actual test names that will be added and which test suites are being changed).
- A sequence diagram showing the dataflow for lesson progress and how the `card_is_checkpoint` property is processed all the way from the lesson structure through to the final property that indicates the user's progress in the lesson in the UI.

</details>

<details>
<summary>Technical hints / guidance</summary>

- General changes overview:
  - Since the new functionality is gated behind feature flags the easiest way to implement some of the features is to introduce entire new versions of the affected files. In other cases it's easier to just gate in single places. Specifically:
    - Study guides will be easier to implement as an entirely new package (also partly because they're being renamed to 'Study Guides' from 'Revision Cards').
    - Lesson progress and worked examples will be easier to gate, though worked examples are slightly tricky because they need to be completely ignored when the feature is off (which means introducing two different handlers).
  - Test lessons will need to be updated. It's recommended to specifically update:
    - [`test_exp_id_2.textproto`](https://github.com/oppia/oppia-android/blob/develop/domain/src/main/assets/test_exp_id_2.textproto) to have `card_is_checkpoint` set at a few points (at least 3) so that lesson progress can be demonstrated for the test lesson.
    - [`test_topic_id_0_1.textproto`](https://github.com/oppia/oppia-android/blob/develop/domain/src/main/assets/test_topic_id_0_1.textproto) to include both worked examples and to use the new revision card structure.
- UI changes:
  - A new package: `app/topic/studyguide` which largely copies from [`app/topic/revisioncard`](https://github.com/oppia/oppia-android/tree/develop/app/src/main/java/org/oppia/android/app/topic/revisioncard) except that it will use a `RecyclerView` and `BindableAdapter` with two model types: heading and content. Note that:
    - New UI layout files will be introduced.
    - Using Jetpack Compose is okay but not mandated. Jetpack Compose should not be used for worked examples or lesson progress.
    - There may be new strings needed for the 'Study Guide' terminology (the app should match the web platform when the feature is enabled).
  - Possibly multiple files under [`app/player/state`](https://github.com/oppia/oppia-android/tree/develop/app/src/main/java/org/oppia/android/app/player/state) to support lesson progress, but in particular: [`StatePlayerRecyclerViewAssembler`](https://github.com/oppia/oppia-android/blob/develop/app/src/main/java/org/oppia/android/app/player/state/StatePlayerRecyclerViewAssembler.kt) since this is the primary consumer of `EphemeralState` from `ExplorationProgressController`.
    - A new feature will need to be added to the assembler to support lesson progress.
    - This feature will only be enabled for explorations (via [`StateFragmentPresenter.createRecyclerViewAssembler`](https://github.com/oppia/oppia-android/blob/191e15dafcc073061941ce64fdd7b999363064e9/app/src/main/java/org/oppia/android/app/player/state/StateFragmentPresenter.kt#L252C15-L252C42)), _not_ questions, and only when the flag is enabled.
    - The current concept mock has the progress indicator next to the navigation buttons. This can only be done by modifying three different layouts: `continue_interaction_item.xml`, `continue_navigation_button_item.xml`, and `next_button_item.xml` which should be hidden in each unless specifically enabled via the respective view models through `StatePlayerRecyclerViewAssembler`.
- Domain changes:
  - [`ExplorationProgressController`](https://github.com/oppia/oppia-android/blob/191e15dafcc073061941ce64fdd7b999363064e9/domain/src/main/java/org/oppia/android/domain/exploration/ExplorationProgressController.kt) in order to compute the current state progress and pass it through `EpehemeralState`. However, [`StateDeck`](https://github.com/oppia/oppia-android/blob/191e15dafcc073061941ce64fdd7b999363064e9/domain/src/main/java/org/oppia/android/domain/state/StateDeck.kt) is the utility actually responsible for calculating `EphemeralState`, and [`StateGraph`](https://github.com/oppia/oppia-android/blob/191e15dafcc073061941ce64fdd7b999363064e9/domain/src/main/java/org/oppia/android/domain/state/StateGraph.kt) will also be necessary for making this work.
  - `StateDeck`:
    - Suggest adding a helper method to compute the checkpoint count at the current state. This should be as simple as counting the number of states with `card_is_checkpoint` set plus 1 since the initial state is considered a checkpoint.
    - `getCurrentEphemeralState` will need to be updated to take a parameter for the total number of checkpoints that will be passed from `ExplorationProgressController`.
    - `getCurrentEphemeralState` should not populate the corresponding fields if the feature is disabled or if the provided count is null (which may happen--see below).
  - `StateGraph`:
    - Suggest adding a new API property `checkpointCount: Int?` which is lazy initialized by calling a new helper: `fun computeCheckpointCount(): Int?` which returns `null` if the exploration has zero states marked as `card_is_checkpoint` (indicating that it doesn't support checkpoints). Note that the lazy initialization is to memoize the value since it will not be trivial to compute and will be needed many times throughout playing an exploration (and isn't expected to change).
    - For actual behavior: `computeCheckpointCount` needs to perform a pathfind through the state graph from the initial state (whose name will need to be passed into `StateGraph`'s constructor) to all terminal states (using the same terminal checker passed into `StateDeck` which will need to be passed into `StateGraph`'s constructor). Specific details:
      - The function should first check that there's exactly one terminal state. If there's more than one then log a warning and return null. This drastically simplifies the algorithm to a pathfind just between two points in the graph.
      - From the starting to ending state follow the main linear path: this is done by going through the `AnswerGroup`s of each state one-by-one and following to the state corresponding to the answer marked using [`labelled_as_correct`](https://github.com/oppia/oppia-android/blob/191e15dafcc073061941ce64fdd7b999363064e9/model/src/main/proto/exploration.proto#L216). There can be more than one answer marked as correct. All correct answers will eventually lead to the terminal state.
      - This is a good application for Dijkstra's algorithm which should yield a single path even if there's more than one correct answer in a state.
      - The single path that's found can then be walked to count all of the `card_is_checkpoint` states and return that count plus 2 (for the initial and terminal states).
      - Note: complex exploration arrangements including multiple correct answers in a single state going to diverging pathways that eventually meet back to the main path should be included in the tests for `StateGraph`. These do not need to be represented in the test exploration.
  - Note that the learner progress functionality must work with all of the following:
    - Lesson checkpoint saving and restoring.
    - Flashbacks.
    - Navigating backward/forward in the state deck (i.e. the progress should count down if the user navigates back to a state previous to the current completed checkpoint count).
- Utility changes:
  - [`HtmlParser`](https://github.com/oppia/oppia-android/blob/develop/utility/src/main/java/org/oppia/android/util/parser/html/HtmlParser.kt) to support a new tag handler for worked examples.
    - See `computeCustomTagHandlers` and the other custom tag handlers for an idea on the implementation.
    - Note that being able to parse arbitrary HTML inside a tag handler isn't currently supported. As such [`CustomContentHtmlHandler.CustomTagHandler`](https://github.com/oppia/oppia-android/blob/191e15dafcc073061941ce64fdd7b999363064e9/utility/src/main/java/org/oppia/android/util/parser/html/CustomHtmlContentHandler.kt#L195C13-L195C29) specifically `handleTag` and `handleTagForContentDescription` will need to be updated to take a new interface `CustomHtmlParser` which takes an html `String` and returns a `Spannable`. A default implementation of this interface can be provided via a call to [`CustomContentHtmlHandler.fromHtml`](https://github.com/oppia/oppia-android/blob/191e15dafcc073061941ce64fdd7b999363064e9/utility/src/main/java/org/oppia/android/util/parser/html/CustomHtmlContentHandler.kt#L320-L324).
- Model changes:
  - `exploration.proto`'s `EphemeralState` should be updated to include new fields: `CheckpointProgress checkpoint_progress` which is not set if the functionality is disdabled. This new proto will need two fields: `int32 completed_checkpoint_count` and `int32 total_checkpoint_count`.

</details>

<details>
<summary>Suggested PM demo points</summary>

- Milestone 1:
  - Lesson progress works correctly for production assets when the feature is enabled including: back navigation, checkpointing, configuration changes, and flashbacks. Progress should not show when the feature is disabled and for explorations that don't have marked checkpoint states. Some visual bugs are okay since milestone 2 includes time to fix issues.
  - The new study guide view shows when the flag is enabled and hides when it's disabled. Some visual bugs/needed improvements are okay since milestone 2 includes time to fix issues.

- Milestone 2:
  - Worked examples show correctly when the corresponding flag is enabled and are completely hidden when the flag is disabled. The visual correctness should be nearly production ready (i.e. small problems are okay but large problems are not).
  - Lesson progress and study guide functionality is fully production ready (i.e. all major design and UX feedback from milestone 1 has been addressed).
  - Both features need to be launch ready.
</details>

### 4.2 Streamlining Release Automation

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:**
The Oppia Android team currently needs to follow a manual, 17-page release process that is both incomplete and has out-of-date instructions, for each release of the app. This highly error-prone and complex manual process leads to multiple hours needing to be spent every time the team wants to ship a new release to end users. This project aims to significantly reduce the burden on the development team to conduct releases by:
- Cleaning up and modernizing the release process to be a wiki page rather than a private Google document.
- Introducing a variety of scripts and GitHub Actions tooling to reduce most of the steps of the process to simple "one-click" deployments to eliminate most of the complexity and time-consuming nature of the existing release process.

One important note for this project is that the team currently only deploys to the Google Play Store. This project will include, as part of its deployment scripts, introducing support for deploying testable builds to [Firebase App Distribution](https://firebase.google.com/docs/app-distribution) to solve a very big headache that currently exists for the QA team: actually installing the correct version of the app. There's well-known synchronization issue wih Play Store that makes it difficult to actually guarantee testers get the correct build at the correct time, and it has caused multiple testers in the past to outright not be able to help with QA for past releases. Firebase App Distribution is expected to fully mitigate this problem and provide QA even more control over testing (such as by being able to switch between multiple release flavors rather than only being limited to a single flavor as is the case for the Play Store's Internal Testing release channel).

Please also note the difficulty of this project. We are assuming most of the deployment steps will require small, custom Kotlin scripts (in-line with other scripts in the codebase) and are not solvable with existing deployment solutions. It may be the case that there are such solutions possible, but the team's own research suggests that we almost certainly have to build out this tooling from scratch due to the prerequisite for Bazel integration. We do expect existing libraries and tooling to be used for directly integrating with Play Store and Firebase.

Here is an explanation for how the release process should work within this project:
- Once per month a release coordinator do the following steps:
  - Start a release:
    - Cut a new release branch for the current version in [`version.bzl`](https://github.com/oppia/oppia-android/blob/develop/version.bzl) since this denotes the _next_ version of the app to release. 'Cutting' simply means checking the latest alpha tag and creating a new branch following the `release-<minor>.<major>` scheme.
    - Send a PR on `develop` to update the minor vrersion in `version.bzl`.
      - Note that merging this PR will kick off an automated script that will generate a PR for generating a new changelog for the _previous_ version.
      - If the script fails, the release coordinator needs to manually create a changelog description for the newly cut release.
      - Changelogs always live in the `develop` branch.
    - Once the branch exists and the changelog exists in `develop`, the coordinator will run the GitHub workflows to build and deploy the beta and GA versions to QA for testing (Firebase deployment only).
    - Other manual steps needed (such as emailing marketing and creating & updating the release document).
  - (Ongoing) monitor QA's progress and make sure that release blocking issues are assigned and fixed in a timely manner.
  - Launch the app (when QA has completed testing the app):
    - Run the GitHub workflow to deploy the app to beta (25% rollout initially; may go up if most users switch to production after GA is first launched).
    - Run the GitHub workflow to deploy the app to GA (25% rollout initially; may go down as the population grows).
    - Wait for Google to review and approve the changes, then publish them.
  - Complete the rollout ~1 week after the 25% deployments go live after checking app health & crash metrics to make sure the app looks healthy:
    - Run the GitHub workflow to deploy the app to beta 100%.
    - Run the GitHub workflow to deploy the app to GA 100%.
    - Wait for Google to review and approve the changes, then publish them.
  - Finish the release and ensure that the team is set up properly for the next release and release coordinator.
- Once per week a release coordinator will need to:
  - Check for alpha releases that are ready to be deployed after Google approval.
  - Check for changelog updates that need to be reviewed (PR) or deployed after Google approval.
  - Check for updated pinned version PRs to review and merge.
  - Check for updated TranslateWiki PRs to review and merge.
- The following crons will run regularly:
  - Once per week: run a workflow to generate a new pinned versions `textproto` file and generate a PR to merge it into `develop`.
  - Once per week: build and deploy an alpha version of the app:
    - Scan all commits to `develop` as compared to the ongoing tag `latest-alpha`. Find the latest commit that has passing CI. If there's none, end the workflow in one of two ways:
      - If there are commits but none have passing CI, fail with an error to surface to repository maintainers that the alpha channel is blocked on CI flakiness.
      - If there are no commits then log this and let the workflow end without failing since there's not actually anything to release.
    - 'Cut' a new alpha release by simply updating `latest-alpha` to the newly selected commit.
    - Kick off two deployment scripts:
      - Upload alpha to Firebase.
      - Upload alpha to Play Console.
- Additional detail:
  - If the changelog is ever updated then it should kick off a script to redeploy it to the Play Console for the corresponding release.

**Changes on March 17**: Some additional details that could be helpful:
- The GitHub CLI tool (`gh`) can actually generate the changelog that GitHub supports through its releases flow. See: https://cli.github.com/manual/gh_release_create. However, that tool is for creating the actual release on GitHub which we don't want to do, we just want the notes. Instead, it's possible to directly call the GitHub API for generating these. See:
    ```sh
    gh api --method POST -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" /repos/oppia/oppia-android/releases/generate-notes -f tag_name='v1.0.0' -q .body
    ```
    It may not be beneficial to use this vs. just generating the description entirely from logs (since more context will probably be useful to the LLM), however it's worth surfacing this in case it can help simplify anything. It is not a requirement to use this.
- GitHub environments can require reviewers to approve the workflow before they run. We should absolutely be enabling this for release workflows. See this [corresponding GitHub documentation](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments#creating-an-environment).

**Tracking issue**: https://github.com/oppia/oppia-android/issues/6106

**Not in scope:** Cron jobs to fully automate the beta & GA launches, or changelog translations (since the team plans to rely on automated translations for these). The steps for creating the release on GitHub, emailing the marketing team, and creating a GitHub discussion are all also not part of the project.

**Size:** Large (\~350 hours)

**Difficulty**: Hard

**Potential mentors:** @adhiamboperes

**Product/technical clarifiers:** @BenHenning (product & technical), @adhiamboperes (technical)

**Discussion forum:** https://github.com/oppia/oppia-android/discussions/categories/gsoc-q-a-4-android-projects

**Required knowledge/skills:**
- Figure out the root cause of an issue and communicate it well using a [debugging doc](https://github.com/oppia/oppia/wiki/Debugging-Docs).
- Build the app and install it on a local device or emulator. Then verify that you can:
  - (a) build a non-test library target locally
  - (b) run a unit test locally
  - (c) play through the app locally
  - (d) build _each_ flavor of the app: dev, alpha, beta, GA.
- Write new Kotlin code with unit tests.
- Familiarity with how the team uses Kotlin scripts (recommended to have actually written or changed one, but this isn't a strong requirement).
- Familiarity with GitHub Actions and a strong concept of how cron jobs work.

**Related issues:**
- https://github.com/oppia/oppia-android/issues/4971
- https://github.com/oppia/oppia-android/issues/4985
- https://github.com/oppia/oppia-android/issues/3620
- https://github.com/oppia/oppia-android/issues/5570
- https://github.com/oppia/oppia-android/issues/4594
- https://github.com/oppia/oppia-android/issues/2542
- https://github.com/oppia/oppia-android/issues/5847
- https://github.com/oppia/oppia-android/issues/2641

**Suggested Milestones:**

- **Milestone 1**:
  - Introduce support for maintaining a checked-in version of the app changelog. Specifically, this changelog should:
    - Provide a historical record of changes that goes into each release, mapped to their `major.minor` release version.
    - Be used as default for every flavor of the app unless that flavor has an override and a custom changelog to use (which needs to be supported).
  - Support for the following new GitHub actions that can be manually triggered through the GitHub web interface:
    - Build and sign release and upload it to the team's binary archive.
    - Deploy to Firebase App Distribution.
    - Deploy to Play Store.
    - Upload the changelog to Play Store.
  - Specific notes on each of the new actions above:
    - The deployment actions need to:
      - Work for each of the alpha, beta, and GA flavors of the app, and upload to the correct corresponding track.
      - Be one action for all of the flavors (selecting the flavor should be an input).
      - Take the specific release branch being deployed as an input. They should fail if the coordinator tries releasing a previously released branch, a version lower than the one currently deployed on the track (using the version name, not version codes), and always try to deploy the latest commit of the release branch.
      - Work correctly for the changelog, meaning the correct changelog (version & flavor) is selected and is uploaded to the correct release track along with the binary. If the changelog, for whatever reason, doesn't exist at the time the workflow is run then it should fail. A changelog must be included.
    - In the case of the changelog workflow, this is only run when the changelog is modified not when it's first generated. Also, it must fail if it it corresponds to a release that isn't actually _live_ on the Play Console. We cannot change old versions of the changelog, and we cannot change a changelog that hasn't yet been released (since it can cause a race condition against deploying the corresponding release). It _is_ allowed to change a changelog and re-run the deployment script (which will likely need to happen on occasion if a mistake is made in the changelog).
    - Note that building and deployment are separate. The idea here is that the coordinator can build a signed release (with release assets) one time for a given flavor and release version, and upload that to the team's shared release archive. Deployment scripts can then download the correct verrsion from this archive (or fail if they're missing) for deployments to Firebase and Play Console. This ensures precisely the same binary that's tested is also the one eventually deployed to end users (and allows for repeatability of select steps like deployment).

- **Milestone 2**:
  - Rewrite the existing release documentation and publish it as multiple wiki pages, also accounting for release features. The following pages should be added as a new 'Releasing' top-level section:
    - An overview of the binary & feature release process.
    - A high-level playbook for release coordinators detailing the steps they need to take for creating a new release and releasing it. These will mostly be using the new automation introduced in milestone 1. It also will need to account for the new release process that happens once https://github.com/oppia/oppia-android/issues/5033 is addressed.
    - A more detailed playbook that provides detailed steps for manually performing each step necessary (for cases when GitHub Actions is broken or unavailable). Parts of this page will be linked to from the previous page so that it's easy to jump to manual instructions if needed.
    - A playbook for developers adding new features and guiding them through the release process.
  - Introduction of automatic generation for the following release artifacts:
    - Changelogs: each time the minor version of the app is updated (a la [version.bzl](https://github.com/oppia/oppia-android/blob/develop/version.bzl)), a script should kick off to generate a new changelog for that version and automatically propose a PR to make the change. Specific requirements:
      - The branch must be directly on the repository so that team members can edit it.
      - The changelog should be sourced from all merged PRs and referenced issues since the last release (which is how GitHub generates its automated changelog for new releases).
      - Changelogs are always checked into `develop` and `develop` is the source of truth for the latest changes (since the entire changelog archive is included on there).
      - An LLM should be invoked using the above source material to provide a suggested, brief description of changes geared towards end users.
      - The PR description for the proposed changelog should contain links to all of the reference material so that team members can choose to alter the context provided by the LLM.
      - **Important**: The changelog is always for the _previous_ version (i.e. if we update the version from 1.1 to 1.2, then 1.1's changelog is what needs to be generated since 1.2 is now the unreleased developer build and 1.1 is soon to be released). Note that this is a difference from the past when the major/minor version represented the previous release.
    - Lesson pinning: the lesson download script relies on a generated textproto file that contains all of the lesson IDs and versions to download. This file will soon be checked into `develop`, so a new cron job should be introduced that periodically (weekly to start) re-runs the download script that produces the pinned version file and introduces a PR for it. Specific requirements:
      - Every week, run the script to generate a new pinned lesson textproto and propose a PR to update it.
      - The same branch is used each time, similar to the Translatewiki model.
      - If the branch already has an open PR, force push the changes (in general, always run against latest `develop` and force push the proposed changes into the branch).
  - Introduce automated release cron for alpha: a new cron job that automatically pushes new alpha flavors of the app to their corresponding channels. Specific requirements:
    - The cron should run weekly (i.e. we never push alpha more than once per week).
    - The cron finds the most recent commit to `develop` with passing CI checks and compares it against the rolling alpha version of the app (which is denoted using the tag `latest-alpha`).
    - If the commits are different, `latest-alpha` is updated to the latest passing CI `develop` commit and that version of the app is built and automatically deployed to both Firebase and Play Console.
    - Note that this should be done in two steps: a workflow that performs all of the alpha detection and build kick-off work, and a cron that runs it. The former should be able to be manually started, as well.

<details>
<summary>Org-admin/tech-lead commentary/advice</summary>

This is a challenging project that essentially builds out all of the necessary critical components for automating Oppia Android releases, significantly streamlining the release process by minimizing the current burdens and time-consuming tasks needed for each release. This will save time both for release coordinators and for QA. It is **crucial** that you have a deep understanding of the existing release process. There is very little time in this project for things to go off track which means misunderstandings have a very high chance of leading to project failure. Make sure that you clarify all doubts and uncertainties before the coding period begins.

This project will expose the developer to substantial automation processes and multi-service deployments. This is a very strong release engineering project and aligns well with individuals interested in learning more about developer operations. There's also a potentially interesting opportunity to leverage an LLM (if it ends up being feasible) for automatic changelog generation which could be a novel opportunity since the team hasn't deeply explored incorporating LLMs into any automation workflows yet.

Particularly challenging aspects of this project:
- The proposed process is actually a change to the way releases are currently managed. This is because the long-term plan is to eventually move Android releases over to a pipeline where code automatically goes from `develop` to `alpha` to `beta` and then finally to `ga`. The full scope is too large for this project (and has a bunch of other complexities to manage), so the only piece of complete automation being done is just the `alpha` bit to start. In order to make that streamlined we will be introducing a `latest-alpha` tag which is not used for the app today.
- Signing the app is done using a locked-down private key that's in a locked-down private repository. That's not a compatible workflow with the automation being built in this project so a new solution needs to be introduced using `jsign` and Google Cloud [KMS](https://cloud.google.com/security/products/security-key-management).

</details>

<details>
<summary>What we are looking for in proposals</summary>

- An explanation (not actual code) of every GitHub action workflow that is needed for the project.
- A technical break-down of every script that needs to be introduced.
- A description of every new third party dependency and service needed and why. Dependencies need confirmation on compatibility with the team's current versions of Kotlin, Java, and Bazel.
- Details on all test plans (lists of actual test names that will be added and which test suites are being changed).
- An explanation of the high-level steps of the Oppia Android release process, and why each step is needed.
  - Note that it's crucial to be very detailed about the specific steps that are being replaced with automation. It's expected that the steps not being automated will be kept at a higher level.
  - It's fine to link back to the public documentation but the explanations should be your own.
  - Particular scrutiny will be placed on the start-to-finish flow for a new binary build, particularly the signing and deployment steps as these are completely new.
- **Important**: an explanation for how you plan to test all of the changes both manually and automatically since we can't provide you with access to the actual production environments or signing key.
  - The best practice for this is to conduct a "dry-run" though you'll need to research how this can be done with each of the integration touch points.
  - In some cases you may need to use a personal Google Cloud project (e.g. for testing the signing flow), or we can provide one during the summer for specifically this purpose.
  - At some point you will need someone with access to perform the actual steps to validate that everything is working. This will require very clear instructions on what needs to be set up in Google Cloud, Firebase, and Play Console plus the actual steps for testing.
  - For automated tests, only the new scripts and utilities need tests but not all of the APIs may be testable. If they have dry-run support then that could also be used for automatic tests, otherwise you'll need to use their testing libraries or abstract them so that we can introduce change detector tests (to make sure we're calling the APIs correctly).
- An explanation for the security aspects of the workflows: how do we make sure that only authorized individuals can access sensitive information?
  - Note that most of this is solved by avoiding having sensitive information like the signing key in GitHub to begin with, but it also needs to be considered for the authentication used for Google Cloud, Firebase, and Play Console.
  - It's very important to understand how the following work since they are critical security components:
    - HSM-backed keystore signing.
    - Workflow Identity Federation keyless authentication.
    - GitHub environments and how they relate to authentication.
- Sequence diagrams covering:
  - The end-to-end lifecycle of alpha, beta, and GA flavors of the app including their deployments to their respective platforms and the manual user steps needed in each (i.e. for final deployment or user installations for testing or end usage). Include how cron fits into this.
  - The end-to-end lifecycle for changelogs including the steps for manually editing them and approving deployments to update the listing on the Play Store. Include how cron fits into this.
  - The end-to-end lifecycle for the pinned lesson version textproto file. Include how cron fits into this.

</details>

<details>
<summary>Technical hints / guidance</summary>

High-level thoughts (that need to be expanded):
- General changes overview:
  - This project is essentially:
    - Breaking down the entire release process (making sure not to miss anything).
    - Identifying the key steps.
    - Building workflows and sometimes new scripts to automate pieces of those steps.
    - Updating environment configurations to work with these new automations.
    - Piecing the entire thing together.
  - Much of the work can be done with existing actions, though in some cases a custom script is necessary. There are no end-to-end solutions that the team is aware of to solve full chunks of the release process which is partly why this GSoC project description is so detailed.
- New directory structure setups:
  - For changelogs: `config/changelogs/<major.minor>.md` which can be overridden using `<major.minor>_<flavor>.md`.
  - For the binary storage buckets in Google Cloud Storage:
    - `gs://<bucket_name>/<major>.<minor>/RC<rc_num>/<fully_qualified_binary_name>.aab`
    - `bucket_name` is one of `oppia-android-alpha-releases`, `oppia-android-beta-releases`, or `oppia-android-prod-releases` as described in the environment setup notes.
    - Example: `gs://oppia-android-beta-releases/0.16/RC01/oppia-android-0.16-rc01-beta-5f3e75afa7.aab`.
- Environment setup details:
  - We need to check in the public PEM certificate (X.509) for the signing key to the main repository in plaintext. This can go in `config/certificate`.
  - We need to set up a Google Cloud GitHub environment for Oppia Android in order to use Workflow Identity Federation (WIF): `oppia-android-release-env`.
    - This will be locked to the pattern `release-*` for release branches and the `latest-alpha` tag for alpha releases.
    - We also need to include the GCP project ID as a secret here since it's needed for the Vertex AI integration.
  - We need to set up new Google Cloud Storage buckets for release binaries:
    - One bucket for alpha releases that has automatic deletion turned on for 90 days (i.e. items auto delete after 90 days). Old alpha versions aren't important: `oppia-android-alpha-releases`.
    - One bucket for beta releases that has automatic archiving after 90 days and automatic deletion after 365 days: `oppia-android-beta-releases`. **Important**: automatic deletion should be filed as a TODO issue and not actually done initially since it must wait until after the GA launch of the app.
    - One bucket for production releases that never auto-deletes and automatically archives after 90 days: `oppia-android-prod-releases`.
  - We need to set up keyless authentication for signing in Google Cloud using WIF: https://cloud.google.com/blog/products/identity-security/enabling-keyless-authentication-from-github-actions. This should be set up to only grant access by satisfying all of the following strict attribute conditions:
    - `attribute.repository == "oppia/oppia-android"`
    - `attribute.environment == "oppia-android-release-env"`
    - `attribute.ref.startsWith("refs/heads/release-") || attribute.ref == "refs/tags/latest-alpha"` (to match the branch protection pattern and support tags--note that this is intentionally redundant with the environment configuration as a means of "defense in depth")
  - We need to set up the following service accounts in Google Cloud to impersonate via WIF for different steps in the process:
    - Account for signing the app.
    - Account for uploading and downloading archives to the Google Cloud Storage buckets.
    - Account for uploading to Play Console (will also need to be invited to Play Console and be given the correct permissions).
    - Account for uploading to Firebase App Distribution (will also need to be added to Firebase with the "Firebase App Distribution Admin" role).
    - Account for accessing Vertex AI for LLM content generation (will need the `roles/aiplatform.user` role).
  - Note that these service accounts and the unique identity for WIF can both be directly in workflow files in plaintext.
  - We need to set up private key signing through Google Cloud Keystore (https://docs.cloud.google.com/kms/docs/hsm) which **MUST NOT** be single tenant (regular HSM is fine).
- New actions workflows:
  - `build_and_sign.yml` (takes a flavor input as one of `alpha`, `beta`, or `ga`, and an input of source ref which is either going to be `latest-alpha` or a `release-*` matching branch).
    - Validates the inputs are correct (especially the source ref).
    - Builds the corresponding version of the app using `bazel build` with optimizations turned on, caching disabled, and production assets embedding turned on.
    - Signs the build using Google Cloud Keystore with a new custom script (which requires using WIF to impersonate the service account with signing privileges).
    - Uploads the build to the correct GCS bucket (which requires using WIF to impersonate the service account with archiving privileges). This can be done with the existing `google-github-actions/upload-cloud-storage` action. This should be configured such that it fails if the build already exists.
      - Note that this is slightly tricky because of the version and release candidate pathing so there's some version extraction from the AAB and string manipulation that needs to be done here.
    - Can be manually run (i.e. `workflow_dispatch`).
  - `deploy_to_firebase.yml` (takes a flavor input as one of `alpha`, `beta`, or `ga`, and an input of source ref which is either going to be `latest-alpha` or a `release-*` matching branch).
    - Validates the inputs are correct (especially the source ref).
    - Runs a new custom script to derive the exact expected binary release name based on the provided flavor and source ref (which should resolve to a commit hash).
    - Downloads the release AAB from the corresponding GCS bucket (which requires using WIF to impersonate the service account with archiving privileges).\*
    - Uses the `firebase` CLI tool (`appdistribution:distribute` command) to upload the AAB to the track corresponding to the provided flavor (which requires using WIF to impersonate the service account with Firebase deployment privileges).
    - Can be manually run (i.e. `workflow_dispatch`).
  - `deploy_to_play_console.yml` (takes flavor input as one of `alpha`, `beta`, or `ga`, an input of source ref which is either going to be `latest-alpha` or a `release-*` matching branch, and takes a rollout percentage from 1 to 100).
    - Validates the inputs are correct (especially the source ref).
    - Runs a new custom script to derive the exact expected binary release name based on the provided flavor and source ref (which should resolve to a commit hash).
    - Downloads the release AAB from the corresponding GCS bucket (which requires using WIF to impersonate the service account with archiving privileges).\*
    - Runs a new custom script for actually performing the upload to Play Console bits (which requires using WIF to impersonate the service account with Play Console privileges).
    - Can be manually run (i.e. `workflow_dispatch`).
  - `deploy_updated_changelog.yml`
    - Run automatically when one of the changelog files changes (i.e. `on` `push` `paths`).
    - Runs a new custom script for specifically uploading the changelog since additional verifications are needed (which requires using WIF to impersonate the service account with Play Console privileges). This script will essentially decide what changelog updates to upload and how (see description below).
    - Can be manually run (i.e. `workflow_dispatch`).
  - `generate_changelog.yml`
    - Run automatically when `version.yml` is updated (i.e. `on` `push` `paths`).
    - Runs a new custom script to automatically generate changelogs for all releases missing them, create a PR with the changes, and submit the PR for review (using existing actions).
      - See the explanation of this script below for more specifics.
      - Note that the PR description should include the base information used to generate the actual suggested changelog lines.
      - Note that this will require using WIF to impersonate the service account with Vertex AI privileges.
    - Can be manually run (i.e. `workflow_dispatch`).
  - `pull_latest_lesson_versions.yml`
    - Run automatically once per week (i.e. using `schedule`).
    - Run the `//scripts:download_lesson_list` script to regenerate the `config/pinned_download_list_versions.textproto` file, create a new PR, and send it for review (the latter of which can be done with existing actions).
    - Can be manually run (i.e. `workflow_dispatch`).
  - `auto_release_alpha.yml`
    - Runs automatically once per week (i.e. using `schedule`).
    - Tries to update `latest-alpha` to a new version or fails/exits early if there isn't a viable candidate.
    - Kicks off `build_and_sign.yml` for the updated `latest-alpha` tag.
    - Kicks off both `deploy_to_firebase.yml` and `deploy_to_play_console.yml` for the alpha release (Play Console will roll out to 100% by default for alpha releases).
    - Can be manually run (i.e. `workflow_dispatch`).
  - \* There isn't an existing action for downloading from GCS buckets (only uploading), so `google-github-actions/setup-gcloud` will need to be used in conjunction with `gcloud storage cp gs://<bucket_name>/path/to/name-of.aab ./path-to.aab` in order to download it.
  - In general, all of the workflows should work just fine when using WIF in combination with Google's `google-github-actions/auth` action since it populates an environment variable that's used for identity authentication. The main difference is that workflows will need to use different service accounts when authenticating depending on what, precisely, they're doing. Reauthentication may also be necessary if a workflow needs to access multiple service accounts.
- New scripts (need to figure out the new script utilities needed):
  - `SignReleaseBinary`
    - Responsible for actually interacting with Google Cloud Keystore to securely sign a release AAB.
    - See [this Gist](https://gist.github.com/BenHenning/fa2a3f26df872ab32ead5461edcef3c7#file-secureandroidreleasesigningexample-kt) for an initial code example for how this might look, though changes will definitely be necessary.
  - `DeriveVersionNameForCommit`
    - Uses the strategy outlined in https://github.com/oppia/oppia-android/issues/5033 to generate the exact version name corresponding to the provided commit with backward compatibility for old versions.
    - Note that this may end up being able to use or refactor the solution for https://github.com/oppia/oppia-android/issues/5033 (which wasn't completed at the time of these technical notes being written).
  - `UploadBinaryToPlayConsole`
    - Responsible for uploading a binary and its changelog (sourced from the `develop`, not current, branch) to the Play Console with the provided rollout percentage.
    - Specifically, this script must fail if any of the following are not met:
      - A changelog exists for the binary on the `develop` branch.
      - A release is already pending for the current track (either not yet reviewd by Google or not yet deployed by the release coordinator).
      - The existing release on the target track is larger in `<major>.<minor>` than the release being deployed (e.g. trying to deploy version 1.2 when 1.3 is already on the track should fail).
      - The existing flavor would create a version code inversion, that is: after this release goes out the version codes much match: ga < beta < alpha. Note that this must account for pending releases for other tracks since multiple tracks can be deployed simultaneously.
    - [This Gist](https://gist.github.com/BenHenning/fa2a3f26df872ab32ead5461edcef3c7#file-uploadtoplaystoreexample-kt) can be used as an initial example, but it's far from complete.
  - `UploadChangelogToPlayConsole`
    - Responsible for auditing the existing release tracks and checking if their changelogs have changed as compared to what's checked into the current `develop` branch. Only the latest changelog is considered.
    - If there are differences, this script will upload the changelogs to Play Console but only if there's not already a pending release (pending releases should cause the script to fail to avoid a race condition between updating the changelog and deploying the binary).
    - If the latest release is older than the changelog version then this script should also fail. This means there's a new release going out but it hasn't been deployed yet. `UploadBinaryToPlayConsole` is responsible for the initial release of a changelog, this script only handles incremental updates.
  - `GenerateChangelogs`
    - Responsible for generating 2-3 user-facing sentences that explain what was added to a release. The suggestion is to do the following:
      - Fetch the previous and new versions. This should be done by sorting release branches lexicographically and picking the two largest (newest) ones.
        - This should also be spot-checked against `version.bzl`. The version in that file must be newer (larger) than the newest release branch.
      - Check if a changelog even needs to be generated for the previous version (i.e. that one doesn't already exist in the changelogs directory).
      - Calculate the start and end commits that are being considered (which can be done by using the release branch merge bases with `develop`--cherry-picks aren't considered here).
      - Collect all commits between the start and end: these represent the changes for the previous release (note again that the current version in `version.bzl` is the _next_ release version whereas this script is trying to generate changelogs for the previous release).
      - Collect all issue titles and descriptions that were fully fixed as part of this release (by inspecting which issues were marked as fixed in the commit descriptions--this may be slightly error-prone but that's fine).
      - Feed all of the merged PR commit bodies, issue titles, and issue descriptions into an LLM with a prompt to generate a 2-3 sentence description explaining what's new in this version of the Oppia Android app. The prompt should include an instruction to emphasize new features first, high priority bug fixes second, and should ignore developer-oriented changes.
    - Note that some iteration will probably be needed to find a good prompt to use.
    - This script should generate the new changelog file for human review using the output from the LLM.
    - The PR that ends up being generated from the output of this script should also include:
      - The before-and-after versions and release branches being referenced.
      - The exact commits for the commit range.
      - A bullet list of all of the commits considered.
      - A bullet list of all of the determined fixed issues used to generate the prompt.
    - The LLM integration can happen through [Vertex AI](https://cloud.google.com/vertex-ai) using the Vertex AI service account defined above and the same WIF process used elsewhere. [This Gist](https://gist.github.com/BenHenning/fa2a3f26df872ab32ead5461edcef3c7#file-vertexaiintegrationexample-kt) has a very rough starting example for how this integration may look.
- Other script utility changes
  - There may need to be changes in `GitClient` for some of the changelog generation.
  - As mentioned for `DeriveVersionNameForCommit` there may be some benefits to refactoring existing version name computation logic into a common utility.
  - Some of the Play Console integration logic might be worth putting in a common utility to simplify `UploadBinaryToPlayConsole` and `UploadChangelogToPlayConsole` but it isn't clear how much can be done there.
  - **Important**: some of these endpoints might not have testing libraries. In such cases they will definitely need to be abstracted using an interface with real and mockable or fake implementations (depending on what's being tested).
- New wiki pages:
  - New page under "Developing Oppia": App & Feature Release Process
    - Includes high-level diagrams and explanations for the lifecycle of a release and feature.
    - Specifically this page should explain how features go from development to users and the how-to steps for developers:
      - Feature changes are merged into `develop` but gated behind a feature flag.
      - Features, once code completed, are enabled for testing in alpha builds and are requested for product review.
      - When product finishes reviewing, any iterations are completed by the developer and then the feature requested for QA review.
      - Once QA finishes testing, all found bugs are fixed by the developer and then the feature is requested for final approval from the team lead.
      - In some cases larger features may be staged in beta separately.
      - With team lead sign-off, the feature can be made ready to be enabled in production (for now this is turning on the feature and it going out with the next release).
      - It's important to note how changes to a release flag corresponds to a specific release so the developer must also understand the release binary lifecycle.
      - Once a feature has been deployed it can then be cleaned up in the next release (i.e. its gating logic can be removed along with any deprecated codepaths that it replaces).
    - The binary release lifecycle should be explained which shows when specific changes actually reach users directly:
      - Alpha: this is automatically deployed to both team members via Firebase and end-users via Play Console once per week. Alpha users can opt into changes through the feature flag dashboard (once https://github.com/oppia/oppia-android/issues/6058 is addressed).
      - Beta & GA\*: these are manually deployed once per month to end users via Play Console. Beta users can opt into changes through the feature flag dashboard (once https://github.com/oppia/oppia-android/issues/6058 is addressed).
      - \* Note that GA isn't launched yet.
    - There is existing documentation to reference for releases, Android features, and [adding new feature flags](https://github.com/oppia/oppia-android/wiki/Platform-Parameters-&-Feature-Flags).
  - New section under "Developer Reference": "Release Coordination". Under this section there should be two new pages:
    - Release Playbook
      - This will provide the exact step-by-step instructions for how to complete an entire release and all of the responsibilities along the way.
      - There is existing documentation for Oppia Android releases that should act as the baseline for these instructions.
      - These instructions should lean heavily on the new automation being built. Ideally there are very few manual steps to actually run.
      - The playbook should link back to both the release overview described above and the in-depth reference described below. The former teaches new coordinators how releases work and the latter provides a safety net if one of the automation steps fails. This means the Playbook just focuses on exactly the minimum steps that the coordinator needs to complete in order to keep the release cycle running and when.
    - In-Depth Release Reference
      - This will be a section-by-section outline of the exact instructions to perform each step in the release process, including: building the app, uploading it to Play Console, uploading it to Firebase App Distribution, signing it, uploading it to the archive, etc.
      - This is not to be a process but, rather, a look-up reference on how to manually complete a particular step if that part of the automation fails. Ideally this guide should never be used but it is crucial if something breaks down to avoid stalling the entire release process.
      - This will also need to include a section explaining necessary permissions since many of the steps require privileged access.

</details>

<details>
<summary>Suggested PM demo points</summary>

- Milestone 1: Demonstrating each of the new actions works with a test-only version of the app.

- Milestone 2: Walk through the new wiki pages to demonstrate their content. Demonstration of the automatic changelog and lesson pinning crons running. Demonstration of the alpha cron automatically running.
</details>
