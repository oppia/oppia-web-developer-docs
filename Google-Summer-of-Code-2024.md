**Important**: _We are making some changes to how we run GSoC for 2024. Please read this page carefully, since some things may have changed from previous years._

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

This year, Oppia will be participating in [Google Summer of Code 2024](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers an opportunity to discover and work with open source organizations to post-secondary students and other non-experienced contributors. The contributions are supported by a stipend. Contributors work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

In order to receive updates about GSoC at Oppia, please subscribe to the [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce) mailing list.

This year, Oppia will follow the standard GSoC timeline: projects will have 6 weeks for each milestone, with a product demo and internal evaluation after 5 weeks. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below for more details.

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions [here](https://github.com/oppia/oppia/wiki).


## Contributors

GSoC is an excellent opportunity for new contributors to get paid to work on an open source project. If you're interested in applying as a contributor, you should definitely read the following resources:

-   [Google Summer of Code contributor guide](https://google.github.io/gsocguides/student/)
-   [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
-   [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)


## Completed Projects

The following projects (with linked proposals, contributor journals and final reports) were successfully completed as part of GSoC 2024:

* [Mohd Afzal Khan](pdfs/GSoC2024MohdAfzal.pdf): Infrastructure and navigation for multiple classrooms. Mentor: Nikita Vorobyev. [Journal link](https://medium.com/@afzl210). [Final report](https://medium.com/@afzl210/gsoc24-final-report-multiple-classrooms-8bcf3d4d10bf).
* [Akash Paloju](pdfs/GSoC2024AkashPaloju.pdf): Static Page Redesigns. Mentor: Harshvardhan Singh. [Journal link](https://add-compelling-pages.blogspot.com/). [Final report](https://gsoc-journey-akash-paloju.blogspot.com/2024/08/my-gsoc24-journey-with-oppia-foundation.html).
* [Vir Kothari](pdfs/GSoC2024VirKothari.pdf): Improvements to the exploration editor page. Mentor: Kevin Thomas. [Journal link](https://medium.com/@virkothari8). [Final report](https://medium.com/@virkothari8/gsoc-2024-final-project-report-oppia-improvements-to-the-exploration-editor-page-fb93af950d3b).
* [Akhilesh Kumar Yadav](pdfs/GSoC2024AkhileshKumar.pdf): Acceptance Tests. Mentor: Christie Ho. [Journal link](https://medium.com/@akacademic05). [Final report](https://medium.com/@akacademic05/my-google-summer-of-code24-with-oppia-foundation-2c12e796f258).
* [Justin Nguyen](pdfs/GSoC2024JustinNguyen.pdf): Make CI and pre-push hooks more efficient.  Mentor: Vojtěch Jelínek. [Journal link](https://medium.com/@jn-nguyen). [Final report](https://docs.google.com/document/d/1Ev_qaJ2yybLZBRpXAtu7WMQIjguuNamLWGKB57v3hUs/edit).
* [Ramadevi](pdfs/GSoC2024RamaDevi.pdf): Code coverage support and enforcement. Mentor: Ben Henning. [Journal link](https://medium.com/@rd4dev). [Final report](https://medium.com/@rd4dev/gsoc-24-final-report-oppia-android-code-coverage-enforcement-47089b8eb3e1).
* [Saptak Manna](pdfs/GSoC2024SaptakManna.pdf): Multiple Classrooms Support. Mentor: Adhiambo Peres. [Journal link](https://medium.com/@Mr_17). [Final report](https://medium.com/@Mr_17/my-google-summer-of-code24-journey-with-oppia-286ebcdef2fd).


## Getting started

Welcome! If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. Make sure to set your preferences correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is about:
    - Read the [user documentation](http://oppia.github.io/#/) to become familiar with important concepts like explorations and interactions.
    - Play some lessons on [Oppia.org](https://www.oppia.org/learn/math), which hosts a live instance of Oppia.

3. To get started with development, read and follow the instructions in the contributors' guide carefully ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), [Oppia Android](https://github.com/oppia/oppia-android/wiki/Contributing-to-Oppia-android)).

4. Do one or more starter projects to become familiar with the contribution process. This will help us get an idea of what it's like to work with you. It will also help you get a better understanding of the codebase and our development process, which may help with writing a good project proposal. Once you've merged at least 2 pull requests, you will get an invitation to become a collaborator to the Oppia repository and be officially onboarded! **This step is a prerequisite to applying for GSoC.**

   - **Note!** You must be onboarded to the repository to which you will contribute during GSoC. For example, to work on an Oppia Web GSoC project, you need to be onboarded to the oppia/oppia repository, which means that your 2 pull requests need to be to oppia/oppia.

   - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to read the [["getting started" guide|Contributing-code-to-Oppia]] and [[PR instructions|Rules-for-making-PRs]] carefully, follow the [tips for success](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#tips-for-success), manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [[style rules|Coding-style-guide]], and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Select one or more [GSoC project ideas](#oppias-project-ideas-list) that you're most interested in, and write your project proposal! You can get feedback from project mentors when you've completed a sufficient draft -- see the instructions in the [GSoC proposal template](#gsoc-proposal-template) section for details.

   We require that all general discussion about GSoC projects take place in open channels. If you have questions about a project, you can ask in [GitHub Web Discussions](https://github.com/oppia/oppia/discussions/categories/gsoc-2024-q-a) or [GitHub Android Discussions](https://github.com/oppia/oppia-android/discussions/categories/general-gsoc-q-a). Note that individual projects have their own categories, so please make use of those if you have project-specific questions. Please also be specific when asking questions, since this makes it easier for us to help you.

   - **Pro-tip!** During the application period, your first goal should be to figure out how to become an effective contributor. Start developing your project proposal only once you have experience getting some PRs merged. This will give you a much better idea of what you want to work on, and how much you can accomplish.

   Good luck!


## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: For Oppia Web, Angular 2+, Python 3.9, Google App Engine and Apache Beam are useful and recommended for most Oppia work; in addition, UI design skills are helpful for frontend user-facing work, and experience with Docker and GitHub Actions is useful for developer workflow projects. Also, it is important to be able to write tests for the code you submit (using Karma, Webdriverio and unittest). Please see the individual project ideas to determine which skills are recommended for the project in question. Note that, although GSoC is aimed at beginner contributors to open source and at students, "beginner to open source" is **not** the same as "beginner to coding" -- the projects assume that you have proficiency with coding. For Oppia Web, you might find this [[page of learning resources|Learning-Resources]] helpful, as well as other pages on our [wiki](https://github.com/oppia/oppia/wiki) that provide guidance on Apache Beam, testing frameworks, etc.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other contributors, successfully contributing, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: Probably not. We have not had good experiences offering flexibility in previous years, so this year, Oppia will strictly adhere to the standard GSoC timeline. Please refer to the [Dates and Deadlines](#dates-and-deadlines) section below, and avoid taking up major commitments alongside GSoC; you are unlikely to be able to balance both.

**Q: Which projects are most important for Oppia?**

A: All the projects we've listed in the [Ideas List](#oppias-project-ideas-list) are important, and we'd be very happy to see good progress made on any of them! Projects are treated as equally important during selection; note that the relative importance of a project to Oppia is not part of the [selection criteria](#selection-criteria). We strongly encourage you to pick a project that you'd enjoy doing over the summer!

**Q: Can I submit more than one proposal to Oppia?**

A: Yes, you can. However, we strongly recommend picking one project and writing a solid proposal for it. Splitting attention across multiple projects might not be a great idea. (That said, GSoC is offering projects of multiple lengths, and if you're interested in doing either the 'full version' or the 'half version' of a project idea that can support both modes, you can submit **both** the 'full version' and the 'half version' as separate applications. Just make sure that you'd be happy with either outcome if you are selected!)

**Q: I'm part of team X in Oppia. Can I submit a proposal for a project idea from a different team?**

A: Yes, you can; there are no issues with that. There is a space in the proposal template to list teams at Oppia you've participated in, and we will get feedback from members of those teams about what their experience of collaborating with you is like.

**Q: How early should I start working on the proposal?**

A: We recommend that you first figure out how to become an effective contributor and get onboarded to the project by getting some PRs merged. Then, start developing your project proposal as early as possible after accepted mentoring organizations are announced on 21 Feb. This will give you time to get feedback from mentors and improve the proposal before submission. Make sure to follow all instructions in the [proposal template](https://docs.google.com/document/d/1BIvB0Pt_KCAD17wFS1viOTfZiehBuEJOO1GeypezdkY/edit) (especially around sharing and access) to reduce delays in reviewing your proposal.

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

When submitting a proposal, please use the provided [GSoC proposal template](https://docs.google.com/document/d/1BIvB0Pt_KCAD17wFS1viOTfZiehBuEJOO1GeypezdkY/edit). We will only consider proposals submitted using this template. Note that, this year, there is a length limit: the proposal's technical "HOW" section should not exceed 20 pages at "Roboto 10" font size.

**Note:** There's **no** formal minimum length requirement for your proposal. The quality of what you write is much more important than the amount of text you write, and we encourage you to write **shorter** proposals that still convey the main aim of the project.

**Some important notes:**

1. When the necessary criteria for requesting a review are met, add gsoc-2024-mentors@oppia.org as an editor for your proposal doc. (This makes some workflows, like inviting PMs or fixing typos, etc., easier, but if you're concerned about changes to your doc, then you can [turn on notifications for edits](https://support.google.com/docs/answer/91588?hl=en&co=GENIE.Platform%3DDesktop).) After fixing the sharing settings, make a new post in the correct "proposal reviews" category in [GitHub Discussions](https://github.com/oppia/oppia/discussions) that is clearly titled with the name of the project that you are requesting a review for, and provide a link to the doc in your post.

   Please use only the above channel for proposal reviews: all proposal-related communication should happen through GitHub Discussions or directly through comments in the proposal doc. **Do not** send proposals directly to individual GSoC mentors.

   You can also request **at most one** "tech lead review" for **at most one** of your proposals during the pre-selection phase. To keep things fair, the tech lead will do only a single pass on your proposal and leave comments, but is not required to follow up on replies to those comments. Since you can only request a tech lead review once (per applicant), we recommend doing so after you have gotten feedback from mentors and completed a full draft of your proposal, but at least a week before the due date. Tech leads will process requests in the order they are received. To request a tech lead review, fill in [this Google Form](https://forms.gle/v6QCE4KrEt1vRRKv8).

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

To select contributors for GSoC, we will evaluate candidates based on a set of criteria designed to ensure we select individuals who not only possess the necessary skills but also demonstrate the ability to contribute effectively to the project. The criteria are as follows, listed in order of significance::

- **Primary Criterion: Required Skills for the Project** - This is the most critical factor in our selection process. A contributor must have the necessary skills for the project. Lack of these skills is a deal-breaker and can lead to immediate rejection of the proposal.

- **Secondary Criteria** (of equal importance):
    - **Quality of the Submitted Proposal** - This criterion helps us gauge the applicant's understanding of the project requirements. The proposal should align with project goals, and be clear, thorough, and feasible.
    - **Prior Experience Working with the Contributor** - We consider our previous interactions with the contributor, focusing on their reliability, communication skills, independence, initiative, responsiveness, and willingness to assist others. This assessment allows us to predict how well the contributor will integrate with the Oppia developer community and contribute to the project's success.

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

1.4. [Redesign the topic page](#14-redesign-the-topic-page)

1.5. [Improve the practice sessions experience](#15-improve-the-practice-sessions-experience)

1.6. [Improvements to the exploration editor page](#16-improvements-to-the-exploration-editor-page)

### Contributor Dashboard team

2.1. [Show AI-powered and cached translation suggestions to translation submitters](#21-show-ai-powered-and-cached-translation-suggestions-to-translation-submitters)

2.2. [Make it possible to update translations for previously-translated content](#22-make-it-possible-to-update-translations-for-previously-translated-content)

### Developer Workflow team

3.1. [Acceptance tests](#31-acceptance-tests)

3.2. [Make CI and pre-push hooks more efficient](#32-make-ci-and-pre-push-hooks-more-efficient)

### Android team

4.1. [Code coverage support and enforcement](#41-code-coverage-support-and-enforcement)

4.2. [Multiple classrooms support](#42-multiple-classrooms-support)


## Learner and Creator Experience (LaCE) team

### 1.1. Infrastructure and navigation for multiple classrooms

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:**

Oppia currently has a classroom page for Math lessons, which is featured prominently and accessible via the home page, navigation bar, community library and learner dashboard. We are planning to create more classrooms for other topics.

The aim of this project is to implement the infrastructure to display these classrooms, and make it easy for learners to navigate to them.

**Tracking issue**: [#19849](https://github.com/oppia/oppia/issues/19849)

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

<details>
<summary>What we are looking for in proposals:</summary>

Here are some examples of questions to analyze:

- How will you generalize the routing to multiple classrooms? (Ideally, this is handled in the frontend.) Which parts of this solution are already implemented and which parts still need to be done?

- How will you efficiently determine which classroom (if any) a topic is in?

- What backend changes are needed in order to remove any hardcoding of "/math" and generalize it?

- What corner cases are there? Feel free to ask the product team if you need UI decisions, but you should think through and fully enumerate all the 'corner case' questions.

</details>

<details>
<summary>Technical hints / guidance</summary>

- Note that new classrooms are created by curriculum admins using the dashboard at /classroom-admin. You will need curriculum admin permissions, which you can grant at /admin (see the Roles tab).

- Hidden classrooms should be viewable by curriculum admins and super admins, with a banner displayed across the top to point out that it is hidden. They should result in a 404 for all other users.

- Here are [the PRD](https://docs.google.com/document/d/1d_FUVKiHsdB8drn9ofw72mIEHztM2GAF8UhErllVMCw/edit) and [mocks](https://www.figma.com/file/CxEKn4FvaZRAAbvuqDchD1/Oppia-Multiple-Classrooms?type=design&node-id=0%3A1&mode=design&t=a3kGrOeQP0HJm0dh-1) for the project, which you can use as a reference.

- Make sure to include unit and acceptance tests to confirm both 1-classroom and multiple classrooms behaviour. In general, you'll want to test the behaviour for (a) a single /math classroom, (b) a single non-/math classroom, (c) 2+ classrooms.

- All UI updates should work fully on mobile devices and be responsive, accessible and fully internationalized.

- Make sure to handle corner cases correctly. E.g. if the learner has done no topics in the science classroom yet, then don’t show that classroom in the list of classrooms-with-topics-in-progress in the learner dashboard.

- You can assume that, from a product perspective, it's fine to require that a topic cannot be linked to more than one classroom. However, if your technical design depends upon this being true, then you should take steps to prevent this from happening (e.g. erroring and refusing to save if the user makes a change that would cause such a state to arise).

- This project includes changes to the learner dashboard. The mocks are based on the redesigned learner dashboard which is currently being worked on in [#18384](https://github.com/oppia/oppia/issues/18384). We expect the redesigned learner dashboard to be ready by the time you are ready to implement those parts, but if not, you can implement the new functionality on the existing learner dashboard instead. You do not need to tackle [#18384](https://github.com/oppia/oppia/issues/18384) directly as part of this project.
</details>


### 1.2. Static page redesigns

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:**

User research has indicated that the informational pages on the Oppia.org website could be improved, because users cannot find the information that they need from them. The aim of this project is to make these improvements.

Please refer to [this PRD](https://docs.google.com/document/d/1enceUlqh7KpaE5i_rdKE-0mZh899tYNf524vFiUYZvI/edit) (still being worked on) for the full details of this project.

**Tracking issue**: [#19850](https://github.com/oppia/oppia/issues/19850)

**Not in scope:**
- Writing translations for the pages into other languages. You should only fill in en.json and qqq.json for any learner-facing strings, as described in our [internationalization wiki page](https://github.com/oppia/oppia/wiki/How-to-develop-for-i18n#adding-new-translation-keys).

**Size of this project:** Small (\~90 hours)

**Difficulty**: Easy

**Potential mentors:** @Lawful2002

**Product Clarifier:** @melhikh, @tanzhirong (backup)

**Technical Clarifier:** @Lawful2002

**Required knowledge/skills:**
- Ability to write frontend PRs in TypeScript/Angular/HTML/CSS with unit tests. These PRs should show attention to detail and excellent judgment for responsive design.
- Ability to write and/or fix flakes in e2e/acceptance tests.
- Ability to make small backend changes in the Python code.
- Effective communication using [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs).

**Suggested Milestones:**
- **Milestone 1**: Update the acceptance tests to cover as much as possible of the "ideal flows" for volunteers, donors, partners, and parents/teachers (see the "Product Flows and Requirements for Specific User Flows" section). This might involve modifying some of the existing tests to make the user type more specific. (Then, as you subsequently redesign the pages, update these tests as needed.)

  Redesign the About page according to the given mocks, and ensure that it is fully-responsive for all device sizes, reaches a Lighthouse score of 100 for accessibility, and fully internationalizable.

  Update and simplify the navbar according to the given mocks.

- **Milestone 2**: Redesign the "Volunteering" and "For Parents/Teachers" pages according to the given mocks, and ensure that they are fully-responsive for all device sizes, reach a Lighthouse score of 100 for accessibility, and fully internationalizable. Add the necessary metrics events to these pages (see the “Automatically-collected metrics” section).

<details>
<summary>What we are looking for in proposals:</summary>

- Explain how you will ensure that the implemented/updated pages are (a) fully-responsive for all device sizes, (b) reach a Lighthouse score of 100 for accessibility, (c) support RTL layouts properly, and (d) fully internationalizable. If possible, link to PRs that demonstrate that you have a good understanding of these areas.

- List all the events you plan to add to Oppia’s site analytics service, and provide a sample of how you would do this.

- For each element in the mocks (such as the bar graphs, timeline chart, etc.), explain how you would implement it.

- Which common components would you create, and where would those common components be used? (It is a bonus if you are able to also use them in pages outside the ones covered in this project.)

- When auditing the mocks and thinking about implementation, you might find that you need to get clarifications on various aspects of the mocks. Include, in your proposal, a list of questions that you have asked / would ask, how they affect the implementation, and the answers to those questions. You might even consider conducting some lightweight user research using the scripts provided in the PRD, but this is optional.
</details>

<details>
<summary>Technical hints / guidance</summary>

- Attention to detail is very important for this project – we don't want to have to revisit these pages again for several years after the GSoC project is completed. So, exhibiting good UI judgment is a particularly important skill that is required for this project. (For example, a button isn’t just a coloured rectangle – it has hover effects, it might change its size depending on the screen width, it might need accessibility support, etc.) Keep this in mind when tackling issues on Oppia, or proposing implementation strategies for this project.

- When implementing, plan for each PR to include both desktop and mobile views (for a particular part of the mocks), as well as the necessary tests.

- Where possible, try to make common components (like the primary-button component that is used in several static pages; see e.g. [oppia#19676](https://github.com/oppia/oppia/pull/19676)) so that you only need to implement the details once, and can more easily keep things consistent throughout the website. We suggest doing this for any UI element that you would use at least twice, and in some cases it might make sense to do it even if you use the element once (so that the component is better encapsulated)
</details>

### 1.3. Clean up the structure for revision cards and worked examples

**Project Description:**

Currently, topics in Oppia contain a list of skills that they teach, and these skills are grouped into subtopics (like 'Adding Fractions'), each with its own revision card (or 'subtopic page' in the backend). Subtopic pages are currently implemented as a single rich-text editor (RTE) field, but this results in their being too long to translate, and the content doesn't look good. (For example, this is one of the revision cards in the Division topic: [link](https://www.oppia.org/learn/math/division/revision/basic-concepts).) We would like to instead split this RTE field into multiple heading/content parts, both to make it easier to translate each revision card in stages and also to improve the display for learners. In the example above, the updated revision card would have two sections: "What is division?" and "Parts of a division equation". In the subtopic page editor, each of these sections would have its own text field (for the heading) and RTE field (for the content).

Additionally, both skill explanations and subtopic pages can include worked examples, but worked examples were incorrectly implemented only as a field on the skill model. Experience has shown that worked examples would be better implemented as a rich-text component instead, since this gives more flexibility in where they are placed and allows them to be used in other contexts like the subtopic pages.

The aim of this project is therefore to clean up the incorrect modelling described above and fix the representation of subtopic pages and worked examples, while also ensuring that they are easily translatable.

**Tracking issues**: [#18305](https://github.com/oppia/oppia/issues/18305), [#19851](https://github.com/oppia/oppia/issues/19851)

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
- **Milestone 1**: Create a new `subtopic_page_sections` field in SubtopicPageContents that is a repeated JsonProperty consisting of (heading: str, content: RTE) pairs. Then, carry out a migration that converts the existing `subtitled_html` field (also known as "revision cards") into the new structure, which should be a single-element list with one item whose heading is the revision card’s title, and whose body is the existing RTE content.

  Store the written translations for subtopic pages in EntityTranslationsModel instead of within the SubtopicPage object, similar to the migration that was done for the correspondingly-named field in explorations a few years ago. Also, introduce a unique content ID for each translatable field, similar to explorations. (This should be a relatively easy migration because there are no translations for SubtopicPages yet, but you will need to figure out the new structure and fix the "plumbing".)

  Update the editor UI to accommodate the new structure, and the learner UI to use an improved display for the revision cards based on these mocks, with clearly-indicated headings for each of the sections. Finally, deprecate the old `subtitled_html` field.

- **Milestone 2**: Carry out a schema migration to safely deprecate the `worked_examples` field in the `skill_contents` part of the SkillModel, and remove it from the skill editor UI as well. Implement a new 'Worked Example' RTE component that appears only in the skill explanation and subtopic page RTEs, and add acceptance tests for its use. Ensure that this component is (in principle) translatable in the contributor dashboard.

<details>
<summary>What we are looking for in proposals:</summary>

- Explain how the current structure for exploration translations works, and describe, by analogy, the ideal structure for skill and subtopic card translations. For the subtopic pages, what changes exactly will you make with regards to written translations and content IDs?

- Explain in detail the steps you would take to carry out the structural migrations for subtopic pages and skills. For the former, what will the updated editor UI look like?

- Explain how you would make the new 'worked examples' component appear only in the concept card and revision card RTEs. Additionally, what will the schema of this new RTE component look like, and how will you structure the acceptance tests?

- What is the **full list** of places which use RTE components, and that will need to be updated with details for the worked example component? Explain the approach you took to find these.

</details>

<details>
<summary>Technical hints / guidance</summary>

- For the worked examples section, see [this PRD](https://docs.google.com/document/d/1QrqTsR1Ew3WfQvj7D83mh0k9HjW6xQ-2dpJGkbe8XqY/edit#heading=h.s68z2sezulra). There is currently no PRD for revision cards, but there are [preliminary mocks](https://www.figma.com/file/wH1RGiZ7KEvLUxeL5R16G6/Oppia-%7C-RTE?type=design&mode=design&t=vEGSCuJcR3gRtZlB-0#681559870) that you can use as a basis.

- See [this wiki page](https://github.com/oppia/oppia/wiki/Rich-Text-Editor-%28RTE%29-Overview) for details on how to implement rich-text components.

- See [this wiki page](https://github.com/oppia/oppia/wiki/Writing-state-migrations) for details on how to write state migrations. Writing migrations for JSON properties in other entities follows a similar process.

- We recommend taking the time to really understand how exploration translations work before you try to figure out a similar structure for subtopic pages. The original TDD for that project is here: [Infrastructure for separate storage of translations](https://docs.google.com/document/d/1ZZ6pVKpmynTlmf1_PV1I5TcccmEXPnmoFAVKXN-u2xM/edit).

- For subtopic page contents, be careful to ensure that each element in the list has its own unique content ID. Do not just base the content ID on the item's index in the list – if you have 3 elements in the list and then remove the middle one, the last element’s content ID should not change. This is why we need a counter to keep track of the "next content ID to assign".

- For "ensure that this component is (in principle) translatable in the contributor dashboard", you can temporarily enable it in exploration RTEs (e.g. in the hints RTE), and then test out the translation workflow. It's important to ensure that the new 'worked example' RTE component has behavioural parity with other RTE components in all places which refer to RTE components, even if it's not being used in the relevant contexts yet – for example, you should update the character-counting logic for hint/solution validation to handle worked-example RTE components as well, in case we decide to make this component available to explorations in the future.
</details>


### 1.4. Redesign the topic page

**Project Description:**

Based on user feedback, on the current topic page, users often overlook the Practice and Revision tabs completely. Additionally, the functionality in those tabs is not correlated with the available lessons, making it unclear to learners when they should review or practice those skills.

The aim of this project is to update the design of the topic page to present a more integrated view of the lessons, practice sessions, and links to revision cards (subtopic pages), so that learners can practice the skills they learned in the relevant lesson. Additionally, it is disappointing for learners to find that the languages that they would want to use for translations and voiceovers are missing only after they start the lesson, so the new design incorporates these selections within the topic page itself and follows the overall site language as a default.

Link to PRD: https://docs.google.com/document/d/1r9IEQ5z_t-eu9XAWN3eRA7iKdKuYsOQbVUjO2ZH1qKg/edit (note: only the parts of the PRD related to the topic page are relevant for this project)

**Tracking issue**: [#19614](https://github.com/oppia/oppia/issues/19614)

**Not in scope:**
- Changes in the linked PRD that relate solely to the practice questions player.
- "View skill progress" section in the mocks for showing skill progress in the topic page (we can do that when the practice questions mastery project is completed).
- Implementing the filter for viewing only lessons/practice questions, or saving the user’s preference for whether they want to see only lessons or practice cards in the list.

**Size of this project:** Medium (\~175 hours)

**Difficulty**: Medium (but requires good fluency with full-stack Web projects)

**Potential mentors:** @Nik-09

**Product Clarifier:** @seanlip

**Technical Clarifier:** @Nik-09

**Required knowledge/skills:**
- Ability to write code for full-stack features in TypeScript/Angular + Python with unit tests.
- Attention to UI detail in mocks, and good UI judgment.
- Ability to write and/or fix flakes in e2e/acceptance tests.
- Effective communication using [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs).

**Suggested Milestones:**
- **Milestone 1**: Implement a basic version of the updated topic player page (based on these [mocks](https://www.figma.com/file/pe0Q3Zx9j6Lt9cvgC7FOOV/Practice-Session-and-Topic-Page---Project-3?type=design&node-id=1318-273022&mode=design&t=B1A3jnB9OlIFBe6a-4)), and ensure that it is fully responsive for desktop and mobile portrait views. This involves the following steps:
  * Create a feature flag for the redesigned page. The new page should be implemented behind this feature flag until it is ready for launch.
  * Create a common modal component to use throughout Oppia that aligns with the designs in the mocks.
  * Create components for (a) lesson cards (which should include the learner’s progress bar and a button to play the lesson – you don’t need to customize the button text at this stage) and (b) practice cards. Use these to display the topic list in the UI.
  * Implement the “Representation of Chapter Availability” section in the mocks by updating the existing "coming soon" UI.

  Additionally, in the **topic editor** page, when applicable, display a warning in the “Canonical Stories” section that lists all subtopics and/or skills that aren’t covered by any chapter of the canonical stories. (This should not block publication of the story, but is important information for the topic manager to know, now that we are associating practice cards with lessons.)

- **Milestone 2**: Add functionality to the topic player page so that it is ready for launch:
  * Implement the text and voiceover language options for the lesson cards, based on the specs described in the mocks/PRD.
  * Implement the correct choice of terminology for start/resume/review buttons on lesson cards (based on the learner’s completion progress), and the associated modals. (This is the part that was left out from the lesson cards in Milestone 1.)
  * Implement the dialog that lists the skills within each subtopic.

  Verify that the topic page works correctly on tablet and mobile landscape views, and fix any issues that arise. Make the topic URL point to the new page, and work with the release team to launch the redesigned page.

<details>
<summary>What we are looking for in proposals:</summary>

Some questions to check that you understand the tech stack:

- How will you load the lesson in the preferred language once the user clicks on the Start button?

- How would you load the practice questions session populated with the desired subtopic ID?

- Explain how you will ensure that the implemented/updated pages are (a) fully-responsive for all device sizes, (b) reach a Lighthouse score of 100 for accessibility, (c) support RTL layouts, and (d) are fully internationalizable. If possible, link to PRs that demonstrate that you have a good understanding of these areas.

Additional things to discuss in your proposal:

- What are the APIs for the components that you will create (e.g. modal, lesson card, progress bar, practice card, and possibly others)? For each of these, provide a definition of the API interface, and an example usage of the component that is associated with a screenshot of one of its instances in the mocks.

- Show a screenshot of the existing "serial chapter launch" functionality running on your local machine, and explain the changes you would make to it to bring it into alignment with the mocks.

- Describe the algorithm that you would use to compute the warning message in the topic editor page.

- When auditing the mocks and thinking about implementation, you might find that you need to get clarifications on various aspects of the mocks. Include, in your proposal, a list of questions that you have asked / would ask, how they affect the implementation, and the answers to those questions.
</details>

<details>
<summary>Technical hints / guidance</summary>

- Note that there is a terminology mismatch between the UI and the code (see "Update 1" under "Details of the Proposed Solution" in the PRD). In your proposal, use the names in the code (skills, subtopics) to describe concepts. The only exception is when you are specifically referring to language that the end user actually sees.

- When implementing, plan for each PR to include both desktop and mobile views (for a particular part of the mocks), as well as the necessary tests.

- For how to launch new features, see this wiki page: https://github.com/oppia/oppia/wiki/Launching-new-features

- When fetching multiple entities, do a single GET-MULTI call. Avoid executing a single GET call N times in a for loop.

- Where possible, try to make common components (like the primary-button component that is used in several static pages; see e.g. oppia#19676) so that you only need to implement the details once, and can more easily keep things consistent throughout the website. We suggest doing this for any UI element that you would use at least twice, and in some cases it might make sense to do it even if you use the element once (so that the component is better encapsulated).

- Here is how to calculate where the practice cards should go in the list contained in the topic editor page. When sending data to the frontend, include all subtopic IDs for the topic and the skill IDs that each subtopic contains. Also, for each chapter, send the list of "acquired skill IDs" to the frontend (these are part of the specification for each chapter). Then, in the frontend, do the following on the fly:
  - For each subtopic, compute the list of its skill IDs that are included in at least one of the lesson chapters of the given story. If the subtopic has no skill IDs that match this criterion, omit it from the list.
  - For each subtopic, run through the list of chapters in order until all of its skills in the list above have been marked as acquired. Place the subtopic practice card immediately after the first chapter for which that condition is met.
  - When two or more subtopic practice cards fall in the same slot, order them based on the ordering of the list of subtopics in the topic editor page.

- The warning in the topic editor page should display:
  - Any subtopics that would be skipped in the first step of the algorithm above, because none of their skills were the "acquired skills" for any chapter.
  - Any skills in other subtopics that are not an acquired skill of any of the chapters within the canonical stories.

- To turn on the "coming soon" functionality, you’ll need to flip the "serial chapter launch" feature flag in the /release-coordinator page (you can give yourself permissions for that in /admin > Roles). See Rishi Kejriwal’s project in GSoC 2023 for more details about how this feature works.
</details>


### 1.5. Improve the practice sessions experience

**Project Description:**

In order to help learners develop mastery of the skills they learn, we want to make practice sessions a more core feature of the Oppia platform. Unfortunately, the current practice sessions experience doesn't encourage and motivate learners to keep practicing until they achieve mastery, and we do not properly surface this functionality in the learner dashboard.

This project aims to redesign the practice sessions experience to incorporate mastery tracking and light gamification, and motivate learners to practice more.

The Figma mocks for this project are linked [here](https://www.figma.com/file/pe0Q3Zx9j6Lt9cvgC7FOOV/Practice-Session-and-Topic-Page---Project-3?type=design&node-id=1099-59863&mode=design&t=gsj3ZOqNEojCgTkw-0) (specifically, see the sections towards the right titled "Practice Player" and "Session Results"). Note that, for this project, we will not be implementing the "Stars" part of the mocks.

Link to PRD: https://docs.google.com/document/d/1r9IEQ5z_t-eu9XAWN3eRA7iKdKuYsOQbVUjO2ZH1qKg/edit (note: only the parts of the PRD related to practice sessions are relevant for this project)

**Tracking issue**: [#19613](https://github.com/oppia/oppia/issues/19613)

**Not in scope:**
- Implementing the "stars" part of the mocks/PRD (though points and mastery are still in scope).
- Showing skill progress in the topic page.
- Adding links from other parts of the site to the practice question experience (e.g. in the learner dashboard, the topic page, and at the ends of lessons).
- Adding a classification level for each skill as trivial/simple/regular, and allowing the curriculum admin / topic manager to update this classification in the skill editor (with a default to regular).

**Size of this project:** Large (\~350 hours)

**Difficulty**: Hard

**Potential mentors:** @nikitaevg

**Product Clarifier:** @juliafalarini

**Technical Clarifier:** @seanlip

**Required knowledge/skills:**
- Ability to write code for full-stack features in TypeScript/Angular + Python with unit tests.
- Attention to UI detail in mocks, and good UI judgment.
- Ability to write and/or fix flakes in e2e/acceptance tests.
- Effective communication using [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs).

Note: Ability to [write Beam jobs](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) is a plus, but is not strictly required.

**Suggested Milestones:**
- **Milestone 1**: Track each user’s total points (this should be updated in the backend each time a learner answers a question correctly, regardless of whether they eventually complete the practice session or not), and show this total in their learner dashboard. The tracking functionality should be hidden behind a `TRACK_PRACTICE_QUESTION_POINTS` feature flag, and the display functionality should be hidden behind a `SHOW_PRACTICE_QUESTION_POINTS` feature flag.

  Implement the redesigned practice sessions UI behind a `SHOW_UPDATED_PRACTICE_SESSIONS_UI` flag, including counters and animations for showing how many points a user has earned in a practice session.

  Add functionality for tracking mastery at both the skill and subtopic levels (this includes storing information about "number correct", "total number attempted", and "results of last 100 questions attempted"). Use this to track answers for questions that are done in both lessons and practice sessions, and update the learner’s mastery scores in the backend. This functionality should be hidden behind a `TRACK_SKILL_MASTERY` feature flag.

- **Milestone 2**: Implement the redesigned practice session results UI behind a `SHOW_UPDATED_PRACTICE_SESSION_RESULTS_UI` flag. Show the total number of points, overall mastery (with an animation showing the change from 'before the session' to 'after the session'), and wrong answers.

  Update functionality for the question selection algorithm to incorporate skill mastery as well. If there aren’t enough questions to choose from, the frontend should display a message saying “sorry, there aren’t enough questions for this topic yet, please check back later” and notify the question admins by email.

<details>
<summary>What we are looking for in proposals:</summary>

Here are some parts of your proposal that we will be paying particular attention to:

- Explain carefully how you would implement the algorithms for (a) tracking mastery and (b) selecting the questions to use for a practice session. You will need to generalize these from the descriptions given in the PRD – try to understand the underlying ideas that the author is going for, and turn those into a generalized algorithm that doesn't have a lot of special-casing.

- Currently, we have approximately 5 questions per skill in the question database. This will mean that the algorithm for (b) above needs to be modified for the initial implementation. Propose how you would handle that, and what instructions the site admin / tech lead should follow to reconfigure the system when the number of questions per skill reaches a higher threshold.

- Explain how you would code the animations in the practice sessions player.

- When auditing the mocks and thinking about implementation, you might find that you need to get clarifications on various aspects of the mocks. Include, in your proposal, a list of questions that you have asked / would ask, how they affect the implementation, and the answers to those questions.
</details>

<details>
<summary>Technical hints / guidance</summary>

- Note that there is a terminology mismatch between the UI and the code (see "Update 1" under "Details of the Proposed Solution" in the PRD). In your proposal, use the names in the code (skills, subtopics) to describe concepts. The only exception is when you are specifically referring to language that the end user actually sees. Note that you should avoid doing any renaming in the backend.

- For how to launch new features, see this wiki page: https://github.com/oppia/oppia/wiki/Launching-new-features

- When implementing, each PR should include both desktop and mobile views (for a particular part of the mocks), and include the necessary tests.

- The new practice session experience should be implemented behind a feature flag until it is ready to launch.

- For questions in lessons (explorations), you only need to track mastery for that question if that question has been tagged with a skill. Points don't need to be tracked for questions within lessons.

- While the question player supports a range of question types, we don't have mocks for most of those types. For now, it is fine to use the existing UI implementations of those question types, tweaking them slightly as needed, as long as the end-user experience is playable without significant obstacles. However, please ensure that, when using shared components, that you test your changes in the other contexts in which those components are being used as well (so that you don't break anything) -- you should show proof of that in the PR descriptions.

- Note that not all sub-tasks in each milestone are of equal difficulty. In Milestone 1, the mastery tracking is straightforward and tracking the total points is easy, but implementing the redesigned practice session UI will take the longest. Plan your schedule accordingly. In Milestone 2, the practice session results UI redesign will probably take longer than the update of the question selection algorithm, since there are multiple parts to the former.
</details>


### 1.6. Improvements to the exploration editor page

**Project Description:**

The aim of this project is to provide two enhancements to the exploration editor page for lesson creators, and ensure that they are covered by acceptance tests:

(a) Allow creators to see which languages a particular part of a lesson has been translated into when editing it, and update those translations directly if appropriate. (For reference, the current user journey – just for updating images – is described [here](https://docs.google.com/document/d/1SRGKBBYdyXN_LWvnHM_Radhdg74mHgvfs27P_n8tAAk/edit), and as you can see it is somewhat convoluted! This project would help simplify steps 22-26, which involve navigating to the translation tab to edit the images there.)

(b) For cards that are tagged with skills: enable lesson creators to tag their response groups with misconceptions, and highlight any non-optional misconceptions that are missing (though this need not block saving).

For (a): in the state editor, when a change is made to a part of a card that has existing translations and this results in a “should translations be updated?” pop-up modal, the modal should also include a list of the existing languages for which that content has been translated, and the currently-saved translations for those languages. The lesson creator should be given the option to update or confirm these translations if the changes are trivial to do (e.g. the content is just numbers), and otherwise leave them alone by default. This will help to save some re-translation work for the community. Note: these translation changes should not be applied immediately – if the lesson creator subsequently discards their change before committing it to the backend, then those translation changes should also be discarded. A cancel button should be added to the main modal for this purpose.

For (b): we have run into issues with missing feedback in lessons, even in cases where we know that the skill is likely to result in specific misconceptions being caught. This is already handled in the question editor by ensuring that all (mandatory) misconceptions for skills are addressed, and we want to extend this functionality to the exploration editor. So, the aim of this project is, for cards which are tagged with a skill in the exploration editor, to show a list of non-optional misconceptions pertaining to the skill which aren’t tagged to an answer response group yet, and to provide functionality that allows the lesson creator to view the list of misconceptions for that card and tag answer response groups with misconceptions as appropriate, in a similar way as is done in the practice questions creation flow.

**Tracking issues**: [#18549](https://github.com/oppia/oppia/issues/18549), [#19852](https://github.com/oppia/oppia/issues/19852)

**Not in scope:**
- Autogenerating the translations for updated content.
- Adding validation checks in the exploration editor to ensure that all misconceptions are tagged, or that all cards are tagged with skills.

**Size of this project:** Large (\~350 hours). Alternatively, you can pick either of the sub-projects for a medium (\~175 hours) project.

**Difficulty**: Medium

**Potential mentors:** @kevintab95

**Product Clarifier:** @seanlip

**Technical Clarifier:** @seanlip

**Required knowledge/skills:**
- Ability to write code for full-stack features in TypeScript/Angular + Python with unit tests.
- Strong UI/UX and technical design skills, including the ability to follow existing design and coding patterns.
- Ability to write and/or fix flakes in e2e/acceptance tests.
- Effective communication using [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs).

Note: Ability to [write Beam jobs](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) is a plus, but is not strictly required.

**Suggested Milestones:**
- **Milestone 1**: Creators should be able to see a list of existing translations through the modal that pops up when they make changes to a published exploration, and should be able to edit those translations if the edits are easy to make.

- **Milestone 2**: Exploration creators should be able to tag answer groups in curated explorations with misconceptions.

<details>
<summary>What we are looking for in proposals:</summary>

General notes:
- Before talking about the fixes you will make, clearly describe how the existing end-to-end user flows work from a technical perspective. This is important to ensure that you have a clear understanding of the system you are modifying.
- You will need to propose a UI for each of these features that aligns with the existing design of the page. Figma prototypes might be a good way to demonstrate this.
- When fetching multiple entities, do a single GET-MULTI call. Avoid executing a single GET call N times in a for loop.

For (a):
- Explain how you would efficiently fetch the info about translations for a piece of content from the backend.
- Explain what updates your code will make to propagate the changes in the modal when the user clicks a non-Cancel button to confirm the changes.
- Outline the acceptance test specs for the intended user flows in each of the following cases: the main content, multiple-choice options, text input responses, hints, and solutions. You can follow a similar pattern as given here: [Web QA Test Matrix (arranged by user type)](https://docs.google.com/spreadsheets/d/1O8EHiSAGrG0yoNUBz9E4DIwKNS8Rfsv_ffC4k1WK5jc/edit#gid=1275148408)

For (b):
- Provide a clear technical description of the relevant parts of the existing question editor workflow, and explain how you would generalize the existing question editor components so that they can be used in the exploration editor as well.
</details>

<details>
<summary>Technical hints / guidance</summary>

The features described here are fairly standard full-stack projects that require both backend and frontend changes to add new functionality to an existing UI. In general, the most important thing to demonstrate in the proposal for this project is good technical design skills and attention to detail (e.g. correct treatment of corner cases). Strong proposals would first show a good understanding of the current system, and correctly describe the parts of it that are relevant to the relevant subproject, before suggesting the changes that would be needed in order to achieve the desired functionality.

For (a):
- The relevant modal to edit is `mark-translations-as-needing-update-modal.component.html`.
- When the modal is opened, you would need to fetch the info about translations for that piece of content from the backend; ensure that the action buttons on the modal are disabled until that happens and the creator has had a chance to audit the translations.
- When proposing mocks for this feature, ensure that consideration is given to the case where there are many translations, since they might overflow if all of them are displayed at once – you could display these in an accordion, and limit the max-height of the modal so that there is an internal scrollbar. For editing translations, you can add a second modal on top of the first one that shows the new content and the editable translation. In the main modal, the “Leave as-is” option should be changed to “Accept the translations above” or similar, and the instructional text should be amended to let creators know that they can edit the translations directly if they wish (and that their chosen option will apply to the translations for all the languages).
- Any changes made while in the context of these modals should be stored temporarily and only applied to the main change list when the modal is saved. If the user clicks Cancel then all changes, including the edit that led to the opening of the modal, should be discarded.
- Make sure to test that your functionality works correctly on a range of different types of content – the main content, multiple-choice options, text input responses, hints, solutions – and cover these journeys using acceptance tests to ensure that they do not break in the future.

For (b):
- This feature should only exist for “curated explorations”, i.e. those that are included in at least one story.
- You can use a UI here that is similar to that in the question editor. Try to reuse existing components where possible.
- Since we will need to update the misconception tags on an incremental basis for existing explorations, you don’t need to add any validation to the exploration editor for missing misconceptions. (Otherwise, this will cause a large number of already-published explorations to become unsaveable until all their misconceptions are completed.)
</details>


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

**Potential mentors:** @chris7716

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

- **Milestone 2**: The full computer-aided translation (CAT) backend implementation is completed, including functionality that allows the developer team to configure the CAT service provider for each language. Admins can run a Beam job from the admin dashboard to generate auto-translations for any untranslated texts for all curated lessons in Oppia's prioritized languages (they can select 'all explorations' or a particular exploration, and they can select 'all languages' or a particular language). Any stored auto-generated suggestions (from caching or from AI providers) are then shown in the contributor dashboard UI when they are available, as well as the exploration player, together with the relevant context as described in Milestone 1.

<details>
<summary>What we are looking for in proposals:</summary>

- For the cache structure, you will probably need to hash strings for quick lookup, and also because the datastore has a [maximum limit for indexable string fields](https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/entity-property-reference#types) (1500 bytes). How will this be handled?

- If the same string can have multiple translations in different contexts, how will that be handled?

- Please provide a clear list of the remaining steps which are  required to complete the CAT project. Bear in mind that getting CAT fully ready includes:
  - Making sure that all rich-text components are handled properly, and fine-tuning the user experience to ensure that all parts of translations (e.g. alt text for images) are easily auditable by submitters before they submit.
  - Ensuring that the system is extensible so that we can specify different service providers for different languages, and each service provider should have a ‘services.py’ file in core/platform/translate. (For this project, it is fine to include the implementation for only one provider, but the framework should be extensible and there should be clear instructions in the wiki for contributors on how to do this.)
</details>

<details>
<summary>Technical hints / guidance</summary>

- Here is an [information sketch](https://docs.google.com/document/d/1ZZ6pVKpmynTlmf1_PV1I5TcccmEXPnmoFAVKXN-u2xM/edit#bookmark=id.d999h6434xq2) about the translation caching system. You can use it as a starting point for your technical design. Note that there are other reasons to cache beyond the one implemented in this project (e.g. we might have custom logic for auto-translation of strings that are entirely numeric) and your system should be extensible to these.

- We have filed a request for the CD mocks with the design team; you can follow [this design issue](https://github.com/oppia/design-team/issues/128) for updates. For your proposal, focus more on the technical aspects than the mocks.

- A large part (probably around \~80%) of the CAT backend work is already done (see [this doc](https://docs.google.com/document/d/1kJd-yLTzB9a2c3Nq7v9pzKfHwKHKGpkWfQ8B0YGf50U/edit#heading=h.jp6no890gjkv) for details). You might like to look at previous unfinished PRs: [#12604](https://github.com/oppia/oppia/pull/12604/files) / [#14418](https://github.com/oppia/oppia/pull/14418).

- If anything goes wrong with generating the suggestion, just don’t show the suggestion part of the submission modal. (Don’t error noisily in a way that blocks the experience for the translation submitter.)

- You will need to gate the new functionality behind [feature flags](https://github.com/oppia/oppia/wiki/Launching-new-features). The flags that would need to be added are for:
  - `SHOW_TRANSLATION_SUGGESTIONS_IN_CD`, for gating the integration of translation suggestions to the contributor dashboard
  - `SHOW_AUTOGENERATED_TRANSLATIONS_IN_LESSONS` -- for showing autogenerated translations in the exploration player
In addition, it would be helpful to provide per-language configuration for showing autogenerated translations in lessons, so that we can only turn that feature on for languages where the auto-translations have proven to be sufficiently good. This can be done by using a platform parameter that contains the supported languages; we would only show the autogenerated translations if the feature flag is turned on **and** the language is in the list of supported languages.

- This [related PRD](https://docs.google.com/document/d/1TeGQQNLNJWkTgvGQ1xmV6snz8zXnJ23TvuDKtK5_Tok/edit) might be a helpful reference.
</details>


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

**Potential mentors:** @chris7716

**Product Clarifier:** @seanlip

**Technical Clarifier:** @chris7716

**Required knowledge/skills:**
- Ability to write code in Python with unit tests.
- Ability to write code in TypeScript/Angular with unit tests.
- Ability to write Beam jobs with tests. (This [wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs) explains how to write Apache Beam jobs. You can try some issues from [this list](https://docs.google.com/document/d/1egQNvBXlgRNhSXdscUZlYOTgd48MXO9a5cPW2rVFL0Y/edit) to get experience.)
- Effective communication using [debugging docs](https://github.com/oppia/oppia/wiki/Debugging-Docs).
- Ability to write and/or fix flakes in e2e/acceptance tests.

**Suggested Milestones:**
- **Milestone 1**: Ensure that the translation counts in the exploration editor translations tab and contributor dashboard are updated correctly when translations are marked-as-stale or new translations are updated, and that the strings to re-translate show up in the CD view for submitters; write acceptance tests to cover this behaviour. Verify also that the reviewer sees the current text at the time they are reviewing, and not the text at the time of submission.

  Make the necessary backend changes for storing data about the English content of an exploration at the time the last translation for that content was accepted (note: not the English content at the time the opportunity was created), and populate this information retroactively for lessons in topics using a Beam job.

- **Milestone 2**: Show a diff view in the UI that translators can use to create the translation for the updated content. Hide this diff view behind a feature flag `SHOW_DIFF_VIEW_FOR_RETRANSLATING_UPDATED_CONTENT`.

<details>
<summary>What we are looking for in proposals:</summary>

- A clear analysis of how translation counts in the exploration editor translations tab and contributor dashboard are currently generated, with links to lines of code in GitHub.

- A clear description of how the end-to-end system for updating previous translations should work, and the gaps that exist in the current system for doing so.

- A description of your Beam job for regenerating the translation count data, as well as how you would validate its correctness.

- A clear description of how you would retrieve the “version when translation was last accepted” for a particular translatable string of a lesson. This might involve storing the entire string somewhere, or storing just the relevant version of the exploration and using that to retrieve the string as needed. Consider different approaches and evaluate their tradeoffs using a decision table.

- A description of how you would generalize the “diff view” component in the exploration history tab to use for the contributor dashboard as well (or if this isn’t a good idea and, if so, why).
</details>

<details>
<summary>Technical hints / guidance</summary>

- A request for mocks for the contributor dashboard UI has been filed with the design team; feel free to follow along at [this link](https://github.com/oppia/design-team/issues/128).

- Note that a tricky part of this project involves showing the English content at the time the previous translation was accepted. We recommend first investigating if this information is stored anywhere, or is easily retrievable. If not, you’ll need to create a separate model for it and populate it via a Beam job, and ensure that it is subsequently populated whenever a translation is approved. There is some earlier analysis in [this TDD](https://docs.google.com/document/d/1RIlefl2kmXyqwrcqTruNjJlQ6EWoiKs9DApT52Kahx8/edit) which you can use as a starting point, but you should validate whether that analysis is correct and not follow it blindly.

- You might find this information about [feature flags](https://github.com/oppia/oppia/wiki/Launching-new-features) useful.

- When fetching multiple entities, do a single GET-MULTI call. Avoid executing a single GET call N times in a for loop.
</details>


## Developer workflow team

### 3.1. Acceptance tests

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

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

**Size of this project:** Large (\~350 hours). Alternatively, you may pick either Milestone 1 or Milestone 2 for a medium-sized (\~175 hours) project.

**Difficulty**: Medium

**Potential mentors:** @imchristie

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

<details>
<summary>What we are looking for in proposals:</summary>

For this particular GSoC project, the proposal is less important and we are more interested in your previous PRs, as described above. We recommend focusing your efforts accordingly.

Some things you could address in your proposal:

- How will you break down this project into individual milestones? Provide a clear timeline for this.

- Explain how your tests would catch console errors that arise during execution of the user journeys.

- For each existing webdriverio test file, specify the set of CUJs which need to be covered by acceptance tests in order for it to be removed. (If you identify gaps in the spreadsheet CUJs during this audit, feel free to suggest improvements to those.)

- In the release-coordinator tab, we want to test the "running Beam jobs" CUJ. Analyze the tradeoffs of creating a separate tiny Beam job for this that runs quickly, doesn't affect the datastore, and that can be added to the list of jobs in the /release-coordinator page, versus using one of the existing Beam jobs. Describe which approach you would take and why. (Note: you can find more info on how to write Beam jobs in [this wiki page](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs).)

- Describe how you would handle specific issues that arise in acceptance tests like mobile viewports, waiting for long-running operations like Beam jobs, etc.

- Suggest any improvements to test organization that you would make, or missing CUJs that you would add. You can cross-reference the testing spreadsheet with the [CUJ document](https://docs.google.com/document/d/1s3MG2MVh_7m7B0wIlZb7sAcoyUdY0zq7a1JEFtwYBjI/edit) that is currently used for release testing, or identify those journeys yourself through direct experimentation with the test server or your local dev setup. Focus only on *critical* user journeys -- you do not need to go into detail for all the edge cases.

- Include test specs for some of the journeys that are not yet covered in the spreadsheet, such as the release-coordinator and site admin user journeys. You can also do this for recently-released features or features that are about to be released (like the contributor admin dashboard, learner groups, contributor recognition project, etc.).
</details>

<details>
<summary>Technical hints / guidance</summary>

- Start by writing tests for just one CUJ to make sure you can do it properly. If you are able to do that well, then there is a good chance that you will be successful with this project.

- For this project, user journeys are detailed in a shared sheet, divided into distinct tabs. During the implementation phase, applicants should tackle each user journey in a structured way, leveraging lessons and code from earlier phases to inform later work. This will help streamline implementation and ensure efficient reuse of developed solutions.

- There is some buffer time built in to the project for improving the organization of tests as more tests get written. Your mentors will work with you on this.

- Note that QA coordinators can advise on CUJs and provide detail on them if any are unclear. Feel free to reach out to them once you've joined the release testing team.
</details>


### 3.2. Make CI and pre-push hooks more efficient

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:**

Optimize the pre-push hooks and CI checks so that they only run necessary tests. This is meant to speed up the developer workflow, while still maintaining a quality bar for PRs that are merged into the develop branch.

**Tracking issue**: [#20001](https://github.com/oppia/oppia/issues/20001)

**Not in scope:**
- Replacing the linter with a faster one (e.g. ruff).
- Migrating the backend tests to a different framework like pytest (so that we can use, e.g., pytest-testmon).
- Complete the implementation of frontend/backend typing so that it is sufficient to run the lint checks only for the code changed in a PR and not their callers in other files (in order to avoid mismatches in function signatures).
- Mapping backend files to the URL endpoints which they affect, so that they can be used to determine which e2e/acceptance/lighthouse tests to run.

**Size of this project:** Large (\~350 hours). Alternatively, you may pick either Milestone 1 or Milestone 2 for a medium-sized (\~175 hours) project.

**Difficulty**: Medium/Hard

**Potential mentors:** @vojtechjelinek

**Product Clarifier:** @DubeySandeep

**Technical Clarifier:** @DubeySandeep

**Required knowledge/skills:**
- For both milestones: ability to work with and configure CI workflows
- For milestone 1: ability to write or make nontrivial changes to backend and frontend unit tests
- For milestone 2: ability to write or fix flakes in e2e/acceptance tests. We also strongly recommend having experience with QA testing for this milestone (to do this, you can join the release testers mailing list at oppia-release-testers@googlegroups.com and looking out for calls to help with release testing).

**Suggested Milestones:**
- **Milestone 1**: Optimize the pre-push hook and the unit tests / lint checks.
  - Shorten the install-and-build step in the pre-push hook, and remove whichever parts can be removed safely.
  - Create a reporter that alerts on which backend unit tests take a long time to run. Refactor any long tests to avoid network/database/disk-access calls in order to shorten their runtime (while still ensuring that they test what they need to). For long backend unit tests that need to be long (e.g. because they are creating a lot of data to test scalability) add them to a “long tests” list that doesn't need to be run during pre-push.
  - In both the pre-push hook and the PR CI, run only the lint (HTML, pylint, eslint, stylelint) tests for files that have changed from the develop branch.
  - In the pre-push hook, run only the frontend and backend unit tests for files that have changed from the develop branch. (But, because the pre-push hook times out, impose a maximum limit on the number of backend unit tests to run, and ignore files that are in the “long tests” list above.) On the PR CI, run all frontend and backend unit tests.
  - In the merge queue, all lint checks and unit tests should still be run for all files in the frontend and backend.

- **Milestone 2**: Optimize the WebdriverIO/Puppeteer e2e/acceptance/lighthouse tests. To do this:
  - Create a GitHub Action that generates a dependency graph which can be used to find the modules that changed files are part of.
  - Maintain a mapping of Angular pages (“modules”) to the e2e/acceptance/lighthouse test suites they affect.
  - For PRs that include only changes to frontend files, use this mapping, together with the dependency graph above, to run only those test suites in the PR’s CI checks. For PRs that include other files, run all tests.

<details>
<summary>What we are looking for in proposals:</summary>

General:

- While CI builds on PRs do not need to run the full set of checks in some cases, the merge queue should still run the full set of checks. Explain how you would achieve that.

- If the merge queue becomes flaky, we might be forced to turn off the merge queue. In such cases, we would need a configuration flag that switches back to running all tests on PR CI builds. Explain how you would implement this flag and what instructions a core maintainer of the Oppia repository should follow if this scenario occurs in the future.

- Explain clearly how you plan to get the list of files changed since the last push, and how you plan to run only the lint checks and unit tests that relate to those files. Ensure that your proposed structure is easily maintainable.

- Explain how you would measure the impact of these optimizations on pre-push hook and CI runtimes.

Also, for this project, it is important that you are able to demonstrate familiarity with GitHub actions, since this project has a number of tasks related to it. E.g.

- Adding build resource usage information to the actions job-summary: https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#adding-a-job-summary

- Setting up different workflows for PRs in merge-queue vs develop.

- Setting up an environment flag to enable/disable whether to run only changed files on a PR.

- Setting up CI such that it can trigger which e2e suites need to be run based on the changes.

We would like to see a description in your proposal of how you'd tackle each of these, and a proof-of-concept demonstration of one of them in a personal repo that you own.

Specific questions for particular milestones:

Milestone 1:

- Find one of the longest-running backend tests, explain how you would make it quicker, and provide a time analysis of the difference.

- For frontend tests, the karma config file uses a regex check to combine all the specs that need to be tested. Explain how, for the purposes of the pre-push hook, you would safely modify that to only include the changed files. (For example, you might create a seam by separating out that regex to a different file/constant and, in the pre-push hook, substitute a custom set of filepaths instead).

- Explain how the pre-push checks will run in the Docker container – e.g. will we run multiple services in parallel, what will the output would look like, what would the order of these checks be, etc.

- What changes will you make to the install-and-build step in the pre-push hook?

Milestone 2:

- Explain how you would generate the frontend dependency graph required by Milestone 2.

</details>

<details>
<summary>Technical hints / guidance</summary>

- You can use git commands to detect which files have changed (and thus need to be tested in the pre-push hook).
- Ensure all optimizations are designed with our Docker environment in mind. In other words, consider how the overall pre-push check will run on docker containers.
</details>


## Android team

### 4.1. Code coverage support and enforcement

**Project Description:**

[Code coverage](https://en.wikipedia.org/wiki/Code_coverage) is a means of quantifying test behavioral coverage. The assumption is that higher code coverage means higher confidence in technical changes. Higher confidence means that the team can rely on more automation to drive releases which, in turn, lets us bring new features to users faster and with fewer bugs.

Historically, this has been a challenging area for the team. Past attempts (see [#2466](https://github.com/oppia/oppia-android/pull/2466) and [#2744](https://github.com/oppia/oppia-android/pull/2744)) ran into challenges with generating correct reports using Gradle. Since the team is also trying to move off of Gradle, Bazel poses its own problems in supporting JaCoCo ([bazel#12159](https://github.com/bazelbuild/bazel/issues/12159)) though rules_kotlin does seem to support it now: [rules_kotlin#508](https://github.com/bazelbuild/rules_kotlin/pull/508) (requires upgrading to a newer version of rules_kotlin which will be done as part of [#4886](https://github.com/oppia/oppia-android/pull/4886) ahead of GSoC coding period starting).

This project entails introducing support for measuring code coverage for all Kotlin files in the Android codebase, with any support gaps documented (e.g. lambdas if those still cause problems: [jacoco#654](https://github.com/jacoco/jacoco/issues/654)). It also involves introducing support for running coverage on a per-unit basis (that is, only measuring the coverage of file Example.kt when running ExampleTest.kt and no other tests), with enforcement for targeting a specific coverage percentage (that's configurable).

**Tracking issue**: [#5343](https://github.com/oppia/oppia-android/issues/5343) (**important**: make sure to subscribe to notifications to this issue if you're going to submit a proposal so that you can be notified if there are any changes to the project's requirements).

**Not in scope:**
- Adding tests for any existing code not affected by the new script functionality itself. This project is NOT intending to increase code coverage, just add instrumentation for it.
- Updating any projects outside of Oppia Android unless this is required in order to get code coverage working during proposal writing.

**Size of this project:** Medium (\~175 hours)

**Difficulty**: Hard

**Potential mentors:** @BenHenning

**Product Clarifier:** @BenHenning

**Technical Clarifier:** @BenHenning

**Required knowledge/skills:**
- Ability to write code and tests in Kotlin.
- Ability to build the app and run tests in Bazel.

**Recommended knowledge/skills:**
- Comfortable with digging into problems that may require exploring code outside of Oppia Android, and that may not have obvious solutions findable via search engines.
- Excellent technical communication skills.
- Familiarity with Kotlin coroutines.
- Understanding of how Bazel targets work.
- Comfortable with performing Bazel queries (e.g. using _bazel query_) and referencing the Bazel [build encyclopedia](https://bazel.build/reference/be/overview) and [query guide](https://bazel.build/query/guide) when needed.
- Having a local Android Studio project set up with the Bazel Android Studio plugin (not required, but it can greatly help with day-to-day development).

**Suggested Milestones:** See the project's tracking issue.

<details>
<summary>What we are looking for in proposals:</summary>

- A **working** demonstration of running code coverage using _bazel coverage_ with a test within the Oppia Android project with correct results (it’s fine if some branches aren’t hit due to missing JaCoCo functionality). Proposals that do not include this working demonstration will be rejected as this is considered a critical prerequisite for succeeding in this project.

- All of the components outlined in the break-down Gist are expected to be fully expanded in the document and finalized, including:
  - Adding documentation strings for each proto field, class, and method being proposed.
  - Adding a dependency diagram showing how the components will be interconnected.
  - Adding a sequence diagram to show how the workflows will behave, and how different uses of the scripts will call through to different dependencies.

- That other [scripts](https://github.com/oppia/oppia-android/tree/develop/scripts) in the codebase are used as the basis for fully writing out the technical portions of the proposal.
</details>

<details>
<summary>Technical hints / guidance</summary>

See tracking issue: [#5343](https://github.com/oppia/oppia-android/issues/5343).
</details>

### 4.2. Multiple classrooms support

> [!IMPORTANT]
> This is a popular project idea.
> Multiple applicants are interested in this project.

**Project Description:**

The app is currently limited to displaying a single list of basic numeracy topics. Together, these topics comprise what we call a 'classroom' (see https://oppia.org/learn/math for Oppia web's classroom viewer).

This project entails introducing support for more than just mathematics topics by revising the core home screen & navigation flows to support topics grouped by their classroom. Future classrooms will include science, financial literacy, and more.

**Tracking issue**: [#5344](https://github.com/oppia/oppia-android/issues/5344) (**important**: make sure to subscribe to notifications to this issue if you're going to submit a proposal so that you can be notified if there are any changes to the project's requirements).

**Reference document**: [PRD](https://docs.google.com/document/d/1uOiDnWBxJmDMwqej-VSRKEnDP4Been3np9y1ov6YTNA/edit)

**Not in scope:** N/A (nothing of note for this project).

**Size of this project:** Large (\~350 hours)

**Difficulty**: Medium

**Potential mentors:** @adhiamboperes

**Product Clarifier:** @moewastaken

**Technical Clarifier:** @adhiamboperes

**Required knowledge/skills:**
- Ability to write code and tests in Kotlin.
- Ability to build the app and run tests in Bazel.
- Ability to make changes & test UI code in Android, and strong familiarity with how the app layers UI components.
- Ability to work with DataProviders.
- Ability to understand and work with protos.

**Recommended knowledge/skills:**
- Ability to read UI mock-ups and apply them when creating layouts.
- Familiarity with Kotlin coroutines.
- Good working knowledge of the app home screen (from a UX perspective).

**Suggested Milestones:** See the project's tracking issue.

<details>
<summary>What we are looking for in proposals:</summary>

That all of the components outlined in the break-down Gist are expected to be fully expanded in the document and finalized, including:
- Adding documentation strings for each proto field, class, and method being proposed.
- Adding a dependency diagram showing how the components will be interconnected.
- Adding a sequence diagram to show how different user flows will call through to different dependencies in the project.

</details>

<details>
<summary>Technical hints / guidance</summary>

See tracking issue: [#5344](https://github.com/oppia/oppia-android/issues/5344).
</details>
