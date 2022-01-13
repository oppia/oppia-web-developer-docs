## Table of Contents

-   [Getting started](#getting-started)
-   [FAQs](#faqs)
-   [Types of work related to Oppia projects](#types-of-work-related-to-oppia-projects)
-   [Selection Criteria](#selection-criteria)

Oppia is planning to participate in [Google Summer of Code 2022](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers an opportunity to discover and work with open source organizations to any non-experienced contributors and especially to post-secondary students. The contributions are supported by a stipend. Contributors work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

In order to receive updates about GSoC at Oppia, please subscribe to the [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce) mailing list.

You might be interested in our GSoC info pages from previous years: [2021](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2021), [2020](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020), [2019](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2019), [2018](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018), [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions [here](https://github.com/oppia/oppia/wiki).


# Contributors

GSoC is an excellent opportunity for new contributors to get paid to work on an open source project. If you're interested in applying as a contributor, you should definitely read the following resources:

-   [Google Summer of Code contributor guide](https://google.github.io/gsocguides/student/)
-   [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
-   [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)

## Getting started

If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. If you like, you can also sign up to the [oppia-gsoc-discuss@](https://groups.google.com/forum/#!forum/oppia-gsoc-discuss) mailing list to participate in general discussion related to Oppia's involvement in GSoC. Make sure to set your preferences correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is all about by taking a look at our [user documentation](http://oppia.github.io/#/) — this will help you become familiar with important concepts like explorations and interactions. We also recommend having a go at playing lessons on [Oppia.org](https://www.oppia.org/splash), which hosts a live instance of Oppia.

3. Read and follow the instructions in the [contributors' guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) carefully.

4. Consider taking up one or more starter projects in order to become familiar with the contribution process. This will help us get an idea of what it's like to work with you — e.g. how independent, resourceful, responsive, etc. you are. It will also help you get a better understanding of the codebase, so that you can write a good and detailed project proposal.

    - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to follow the [tips for success](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#tips-for-success) carefully, manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide), and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Once you've merged at least 2 pull requests, you will get an invitation to become a collaborator to the Oppia or Oppia-Android repository and be officially onboarded! **This step is a prerequisite to applying for GSoC.**

6. Now, you can select one or more GSoC projects that you're most interested in, and write your project proposal! This point will be elaborated more after Oppia is officialy accepted into GSoC.

<!--- 6. Now, you can select one or more GSoC projects that you're most interested in, and write your project proposal! We strongly encourage you to discuss your project ideas and share your proposal with the community, so that you can get feedback and ensure that what you're writing makes sense to others. The best way to do this is to put your proposal into a collaborative editing tool like Google Docs, allow others to comment on it, and share a link to it on the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com). You can also email this mailing list if you have any questions about a project, or would like to discuss your approach with the Oppia community and get feedback. Please be specific when asking questions, since this makes it easier for us to help you.
    - **Important note:** Please read [this oppia-gsoc-discuss@ thread](https://groups.google.com/forum/#!topic/oppia-gsoc-discuss/S6Ge3vQ3cuc) carefully for details about the recommended review process. Note that you do not need to write the entire proposal before getting your first review — see the instructions in that thread for more details. Thanks!
--->

## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: For Oppia Web, Angular 2+, Python 3.7 and Google App Engine is useful and recommended for most Oppia work; in addition, UI design skills are useful for frontend, user-facing work. For Oppia Android, you'll want to be familiar with Android development in Kotlin. Please see the individual project ideas to determine whether these skills are recommended for the project in question.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other contributors, successfully contributing, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: Yes (within reason)! This year, GSoC is going to be slightly different from previous years. The program has been restructured in a way that allows contributors to take some time off for any other commitments (such as exams etc.) [(View the timeline here)](https://developers.google.com/open-source/gsoc/timeline). Oppia will respect the same timelines as given by GSoC — the main concern is whether you can still get the project done on time. Be upfront about your other commitments and make sure you schedule your time accordingly when creating your proposal. Other commitments you should list include time when you'll be in school and will commit less time to GSoC, time when you'll be travelling and away from GSoC work, any summer jobs you need to commit to, etc. We will try to be flexible around other time commitments, as long as your proposal convinces us that you will have enough time to complete the project by the end of the GSoC coding period. On the other hand, if you do not disclose other commitments, and it turns out that you are unable to commit to what you wrote on your proposal, this is grounds for failing the program.

**Q: Which projects are most important for Oppia?**

A: All the projects we've listed here are important, and we'd be very happy to see good progress made on any of them! Projects are treated as equally important during selection. Note that the relative importance of a project to Oppia is not part of the [selection criteria](#selection-criteria). We would encourage you to pick a project that you would enjoy doing over the summer.

**Q: Can I submit more than one proposal to Oppia?**

A: Yes you can. However, we strongly recommend picking one project and writing a solid proposal for it. Splitting attention across multiple projects might not be a great idea.

**Q: How early should I start working on the proposal?**

A: As early as possible. Make sure to get feedback from mentors before finally submitting the proposal. This will help you to write a better proposal as you can refine the details based on the feedback you receive. The mentors would need some time to review your proposal, and hence it is a good idea to begin as early as possible.

**Q: I only discovered Oppia recently. Does this mean that, during selection, my application would automatically be ranked lower than those by other applicants who have a longer tenure with Oppia?**

A: Definitely not! Here are the [selection criteria](#selection-criteria) we use when selecting contributors for GSoC; note that tenure is not part of these criteria. Also, our philosophy is to consider each application based on its own merits, not relative to other applications, and we try to accept every contributor whose application "meets the bar". The only cases in which we'd need to compare applications against each other are when a project idea receives multiple applications, we receive fewer "slots" to host contributors than we originally applied for, or we don't have enough mentors to host all the projects we want to support.

**Q: What are the minimum number of PRs that one should have?**

A: There is no specific minimum number. Remember that quality is more important than quantity. It is better to submit a nontrivial PR rather than a simple bug fix. Start with starter issues, then prioritize ones that touch the area(s) of the codebase which are related to your project.

**Q: What is the total number of contributors that will be accepted?**

A: As many as we think will succeed, though the Google GSoC admins may impose quotas.

**Q: I do not have any experience in skill XYZ. Is some certification required?**

A: Try to work on good first issues and take courses online. In the field of software development, it is common to develop experience and expertise as you take up and complete projects successfully. We do not require any formal certification of particular skills.

**Q: Is it okay if I only focus on the frontend or backend?**

A: This probably depends on the project(s) you wish to apply for. However, note that the ability to be effective in both the frontend and backend will open up more opportunities for you, since projects often touch multiple layers of the stack.

**Q: The [Google GSoC FAQ](https://developers.google.com/open-source/gsoc/faq#can_someone_already_participating_in_open_source_be_a_gsoc_contributor) mentions that it is only for new contributors. I have already contributed to Oppia and I have write access, can I still participate?**

A: The GSoC program is open to new and beginner contributors to open source. Some of our contributors with write access are still beginner contributors, whereas some of our other contributors with write access will not qualify because they are experienced contributors. If you only recently received write access, or have been contributing to Oppia for less than a year, you are probably still a beginner contributor. If the previous sentence does not apply to you, and you want to know which group you fall into, please contact **@vojtechjelinek** or **@seanlip** for a decision.

<!---
## GSoC Proposal Template

When submitting a proposal, please use the provided (**TODO: fix link and update subsequent paragraphs**)[GSoC proposal template](https://docs.google.com/document/d/1fZ8yJG70zoANYGJgOv5wsIzz3arOX4Up4EJqfUU6nis/edit). We will only consider proposals submitted using this template.

You are welcome to ask mentors for reviews during the proposal preparation phase. Mentors will review proposals incrementally. That is, they will work through the Mocks section, and, only after they are satisfied with it, they will review the Technical Design section, and, similarly, only after that section looks good, they will review the Milestones section. This is meant to help ensure that later sections of the proposal are building on a solid baseline.

**Important:** Please make sure that your final proposal is self-contained. In particular, to be fair to all applicants, key components of the proposal should not be editable after the deadline, and you shouldn't assume that reviewers will follow external links.

### Tips for writing a good project plan

Here's some advice about proposals and milestone timeline planning that we collated from previous contributors and mentors:

-   Choose a project you're interested in! If you have a strong interest in your project, this will help you pick up necessary skills and tackle any unforeseen difficulties that arise during GSoC.
-   Familiarize yourself with the relevant part of the codebase for your project, especially if you haven't touched it before. It's important to think about how to integrate your project with the current Oppia structure — don't design in a vacuum.
-   Define milestones with enough detail to get a proper ETA for each milestone (so, don't just say "write e2e tests"), otherwise you run the risk of significantly underestimating the timeline.
-   Clear written communication and presentation is crucial in preparing your proposal. The proposal should show that you have a clear understanding of the codebase and the final goal of the project. Eg. In a user-facing proposal, writing about just the files that have to be changed is not enough, detailed mocks and userflows (in the form of diagrams or points) are also essential.
-   Limit proposal length. Remember a lengthy proposal is not equivalent to an excellent proposal.
-   Ensure that the problem statement is within your limits to tackle. You should make sure that what you are proposing is within your capabilities. What we have in the [project ideas section](#oppias-project-ideas-list) are suggested milestones; it is up to you to come up with a complete plan that is within your ability. i.e., contributors can propose whatever they want; it’s up to us to subsequently figure out (during selection) whether we’re happy about what’s being proposed.
-   Contributors who make the last milestone bulky normally run into issues. So, make sure that you distribute work evenly.

### What should applicants expect from mentors in a proposal review?

-   Please write your proposal on the assumption that you "own" your chosen project. From your perspective, the submitted proposal should be in as good a condition as possible before you ask for a review. Make sure you have a sufficiently good understanding of the codebase/project to find flaws in the design; don't assume that reviewers are responsible for doing this for you. Note that your proposal doesn't need to be flawless — we expect that you might make mistakes, and reviewers will be happy to guide you on how to improve. Instead, by "as good a condition as possible", we mean that your proposal should demonstrate:
    -   Your ownership of the project
    -   The research you have put into writing it
    -   Your analytical skills
    -   Your independence in making complex decisions
-   Make sure to present solutions and ask for feedback, rather than just asking for solutions. You can do this by presenting the various solutions you came up with in your proposal, and doing an analysis of their advantages & disadvantages from the end-user perspective. Finally, choose the best solution you have and explain your reasoning behind your choice. Note that this doesn't mean that you must always have multiple ideas to solve a problem, but you should instead always explain how you reached a solution, and why is it the best one from the end-user's perspective.
-   Mentor's suggestions are "suggestions", not orders (often, reviewers may not be certain whether their suggestion is correct), so, as the proposal owner, you are welcome to decide whether to accept/reject it. In either case, when you are accepting/rejecting a suggestion provided by a reviewer, explain your reasoning and the research that led to your decision. Don't use an "appeal to authority" (e.g. "I am doing it this way because XXX said so") — the rational analysis that underlies the decision is what's important.
-   We do not expect you to always agree with your reviewers. If you think that the suggestion doesn't suit your project, it is totally fine to explain your decision and provide reasons for it. It is always a good idea to have discussions when you have confusions, rather than simply agreeing. Note that this does not mean that we encourage you to disagree with your reviewers on everything — this is just a suggestion to bear in mind if you get confused.
-   Please note that your reviewer may or may not be involved in the final selection process. It is also **not** the case that you need to implement all your reviewers' suggestions/requests in order to be selected. As mentioned above, it is important that you actively take help and work together with your proposal reviewers in order to prepare a strong proposal that meets the guidelines for your chosen project.

### Sample proposals from past years

If you'd like to get a sense of what a proposal might contain, please see our [GSoC 2021 page](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020) for examples of proposals that we accepted in 2021. However, please note that the [GSoC Proposal Template](https://docs.google.com/document/d/1fZ8yJG70zoANYGJgOv5wsIzz3arOX4Up4EJqfUU6nis/edit) has been completely revamped for 2022, so please be sure to follow the 2022 template.

_**Note:** although some of the previous years proposals are a bit on the long side, there's **no** formal length requirement for your proposal. In general, the quality of what you write is much more important than the amount of text you write, and we encourage you to write shorter proposals that still convey the main aim of the project. For the actual requirements, please see the [GSoC Proposal Template](#gsoc-proposal-template) section above._

--->

## Types of work related to Oppia projects

In order to ensure a well-rounded engineering experience, contributors will do some or all of the following depending on their project:

-   Meet with their mentors regularly
-   Meet with other contributors related to their project area
-   Read and understand parts of the codebase related to their project
-   Receive code reviews for all code they write for their project
-   Write automated tests for their projects
-   Create UI mocks (if doing frontend development)
-   Write design documents (if implementing large features or introducing new systems)

We've also asked our previous GSoC contributors what they learned during previous GSoCs. Here are the collated answers:

-   Technical ability
    -   Writing clean code, while keeping in mind the requirement for the code to run in production.
    -   Working on a large codebase.
    -   Building an entire new feature in a scalable way.
    -   Reading and understanding code from other open-source organizations.
    -   Writing robust tests.
-   Technical domain knowledge
    -   I feel more confident on working with Angular. Oppia was the first time I worked with unit, e2e tests. I feel a lot more confident in writing code now whether be it making my own projects or contributing to other open-source projects.
    -   I learned lots of things about typescript and webpack.
    -   I understood how E2E tests and angular migrations worked in Oppia — this felt very rewarding.
    -   I enjoyed finding and fixing accessibility issues.
-   Technical leadership skills
    -   Apart from the project, I learnt how to manage my time well, how to achieve deadlines especially when I got evaluations from external evaluators.
    -   Reviewing others' code.
    -   Technical design skills (and validation of technical ideas).
    -   Learning how to give, respond to and understand reviews is something that I believe has improved a lot during the GSoC tenure.
-   Communication
    -   Putting forward my thoughts more systematically and deeply so that everyone can understand me well.
    -   Better communication skills.
    -   How to write a good proposal.
    -   Learning how to work with a large community like this which is spread over different time zones.

## Selection Criteria

In order to select contributors for GSoC, we will mainly be looking at three things:

-   The quality of the submitted proposal
-   The quality of the applicant's previously-submitted PRs (in order to assess their ability to code, debug, break down complex tasks, etc.). Note that quantity isn't a prerequisite in itself, though contributors who've submitted multiple PRs are likely to have had more opportunities to demonstrate the abilities needed to succeed in GSoC.
-   Our prior experience working with the contributor (do they keep commitments, communicate well, demonstrate independence/initiative/responsiveness, help others, etc.)

We believe that strong performance in these dimensions is likely to correlate well with the contributor having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the GSoC program.

For the proposal, we generally look for a clear indication that the contributor has a good, deep understanding of the project, and has broken it down sufficiently well, in a way that makes it very likely to succeed. Some indicators that could help with this include:

-   A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating a simple, intuitive experience for end users.
-   A concrete, specific breakdown of the work to be done for each milestone. Here's an [example](https://docs.google.com/document/d/1vuwXvHOYXqfM2S2B2KIWhZrAa1PL59wJRUYsqJEd67E/edit) from a previous design doc. (Note that, in the implementation plan, the author has carefully considered and listed which tests need to be written alongside the code; this is a positive indicator.)
-   Sufficient concreteness (e.g. references to particular files and methods) to demonstrate that the applicant is familiar with both the scope of the problem and the existing codebase.
-   A description, if applicable, of how the applicant plans to mitigate risks that could potentially derail the project.
-   Clear, unambiguous communication. (This is important; your proposal will be read by many mentors!)

## Oppia's Project Ideas List

_**Note:** If you're coming to this section from an external link, please make sure to scroll up and read this entire wiki page carefully, not just this section. There's a lot of useful information on the rest of the page, including a FAQ and a section describing selection criteria. Thanks!_

We will publish the projects ideas list around the start of February. We will announce this on our [Oppia GSoC Announce mailing list](https://groups.google.com/g/oppia-gsoc-announce).

<!---

The following is a list of Oppia's 2022 GSoC project ideas. (Please note that all mentor assignments listed below are provisional, and may change depending on which proposals are eventually accepted.)

You are welcome to choose among these ideas, or propose your own! However, if you're planning to propose something original, it's essential to engage with the Oppia community in order to get feedback and guidance to improve the proposal. We also recommend taking a look at [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission) and seeing if there is a natural way to tie your idea to the Oppia project's goals, otherwise it might not be a good fit at this time.

The list of project ideas is not fixed and more projects can be added. Also, please note that **the project descriptions are not final yet** — we are still working them out, and some of them may change a bit.


# Other useful information

## Dates and Deadlines

Noteworthy dates for 2022 ([Full Timeline](https://developers.google.com/open-source/gsoc/timeline)):

TODO

## List of Mentors

TODO

## Communication

**Chat**

Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any questions related to getting started. For project-specific questions, please direct your queries to the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).

**Email**

In order to receive updates about GSoC at Oppia please subscribe to [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce).

If you have questions pertaining to "how-to-get-started", please ask them on [Gitter](https://gitter.im/oppia/oppia-chat), or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you. Also, please make sure to read our ["getting started" wiki page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) before sending an email, since the answer to your question might already be contained there!

To discuss your project ideas, or share your proposal for feedback from the community, please email the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com). You can also use this list for specific questions about GSoC.

---

--->