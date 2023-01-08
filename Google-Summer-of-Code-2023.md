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

This year, Oppia will be participating in [Google Summer of Code 2023](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers non-experienced contributors (and, historically, post-secondary students) the opportunity to discover and work with open-source organizations. The contributions are supported by a stipend. Contributors work closely with one or more mentors from an open-source organization to implement either a project idea by the organization, or a proposal of their own. You might be interested in our GSoC info pages from previous years: [2022](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2022), [2021](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2021), [2020](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2020), [2019](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2019), [2018](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018), [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

In order to receive updates about GSoC at Oppia, please subscribe to the [Oppia GSoC Announce](https://groups.google.com/g/oppia-gsoc-announce) mailing list.

Oppia will strictly adhere to GSoC timeline and will not be able to provide any additional extensions. Please refer to 
the [Dates and Deadlines](#dates-and-deadlines) section below.

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out! You can get started by following the instructions [here](https://github.com/oppia/oppia/wiki).


# Contributors

GSoC is an excellent opportunity for new contributors to get paid to work on an open source project. If you're interested in applying as a contributor, you should definitely read the following resources:

-   [Google Summer of Code contributor guide](https://google.github.io/gsocguides/student/)
-   [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
-   [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)


## Getting started

Welcome! If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC. If you like, you can turn on the notification for github discussions to  participate in general discussion related to Oppia's involvement in GSoC. Make sure to set your preferences correctly so that you actually get the emails!

2. Get a better understanding of what Oppia is about:
    - Read the [user documentation](http://oppia.github.io/#/) to become familiar with important concepts like explorations and interactions.
    - Play some lessons on [Oppia.org](https://www.oppia.org/learn/math), which hosts a live instance of Oppia.

3. To get started with development, read and follow the instructions in the contributors' guide carefully ([Oppia Web](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up)).

4. Do one or more starter projects to become familiar with the contribution process. This will help us get an idea of what it's like to work with you. It will also help you get a better understanding of the codebase and our development process, which may help with writing a good project proposal. Once you've merged at least 2 pull requests, you will get an invitation to become a collaborator to the Oppia or Oppia-Android repository and be officially onboarded!

   - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to follow the [tips for success](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#tips-for-success), manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide), and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

5. Select one or more [GSoC project ideas](#oppias-project-ideas-list) that you're most interested in, and write your project proposal! We strongly encourage you to discuss your project ideas and share your proposal with the community, so that you can get feedback and ensure that what you're writing makes sense to others. Please follow the instructions in the [GSoC proposal template](#gsoc-proposal-template) section to do this.

    If you have any questions about a project, or would like to discuss your approach with the Oppia community and get feedback, you can also email the [oppia-gsoc-discuss@](https://groups.google.com/g/oppia-gsoc-discuss) mailing list. Please be specific when asking questions, since this makes it easier for us to help you.
    - **Pro-tip!** 75% of the accepted proposals had begun their work at least 4 weeks prior to the deadline. Hence, we strongly recommend that the contributors start writing proposals as early as possible.

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

**Q: Is Oppia Android a part of this year's GSoC?**

A: Oppia Android won't be able to participate in GSoC this year. Note that this is a one-off, and Oppia Android hopes to be back in 2024 when we have better processes and documentation to help contributors get onboarded more smoothly.

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

Noteworthy dates for 2023 ([Full Timeline](https://developers.google.com/open-source/gsoc/timeline)):

- **Jan 23 - Feb 7**: Mentoring organizations apply
- **Feb 22**: Mentoring organizations are announced
- **Mar 20 - Apr 4**: GSoC contributor application period
- **May 4**: Accepted GSoC contributors are announced
- **May 4 - May 28**: Community bonding period
- **May 29 - Nov 6**: GSoC contributors enjoy the summer by contributing code to their projects
- **Nov 13**: GSoC officially ends

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
- Why students want to stay
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
      - Yes, the kind of work that Oppia does is really inspiring and there are a lot of opportunities to improve your skills be it be technical skills or leadership skills and most of all the people at Oppia are really fun to work with :)
      - I like working in Oppia since it not only helps me improve my coding skills but also helps me grow as an individual.



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

If you'd like to get a sense of what a proposal might contain, please see our [GSoC 2022 page](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2022) for examples of proposals that we accepted in 2021. However, please note that the [GSoC Proposal Template](#gsoc-proposal-template) has been completely revamped for 2022, so please be sure to follow the 2022 template.

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

