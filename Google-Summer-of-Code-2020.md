## Table of Contents
* [Getting started](#getting-started)
* [FAQs](#faqs)
* [GSoC Proposal Template](#gsoc-proposal-template)
  * [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan)
  * [Sample proposals from past years](#sample-proposals-from-past-years)
* [Types of work related to Oppia projects](#types-of-work-related-to-oppia-projects)
* [Selection Criteria](#selection-criteria)
* [Oppia's Project Ideas](#oppias-project-ideas)
* [Other useful information](#other-useful-information)
    * [Dates and Deadlines](#dates-and-deadlines)
    * [List of Mentors](#list-of-mentors)
    * [Communication](#communication)

Oppia is planning to participate in [Google Summer of Code 2020](https://summerofcode.withgoogle.com/)! GSoC is a global program which offers post-secondary students an opportunity to discover and work with open source organizations over the course of 3 months, while being paid a stipend. Students work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

You might be interested in our GSoC info pages from previous years: [2019](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2019), [2018](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018), [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017), [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

Also, please note that acceptance into GSoC isn't a prerequisite for becoming an Oppia contributor. The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out!

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

## GSoC Proposal Template

When submitting a proposal, please use the provided [GSoC proposal template](https://docs.google.com/document/d/1C6OgWa5I2wTWYPLTOqoZMVvWrVQ10BGXbe4SNEBMu-s/edit). We will only consider proposals submitted using this template.

**Important:** Please make sure that your final proposal is self-contained. In particular, to be fair to all applicants, key components of the proposal should not be editable after the deadline, and you shouldn't assume that reviewers will follow external links.

### Tips for writing a good project plan

Here's some advice about proposals and milestone timeline planning that we collated from previous students and mentors:

- Choose a project you're interested in! If you have a strong interest in your project, this will help you pick up necessary skills and tackle any unforeseen difficulties that arise during GSoC.
- Familiarize yourself with the relevant part of the codebase for your project, especially if you haven't touched it before. It's important to think about how to integrate your project with the current Oppia structure -- don't design in a vacuum.
- Define milestones with enough detail to get a proper ETA for each milestone (so, don't just say "write e2e tests"), otherwise you run the risk of significantly underestimating the timeline.

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

## Oppia's project ideas

TBD

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

TBD

## Communication

**Chat**

Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](
https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any questions related to getting started. For project-specific questions, please direct your queries to the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).

**Email**

If you have questions pertaining to "how-to-get-started", please ask them on [Gitter](
https://gitter.im/oppia/oppia-chat), or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you. Note that full instructions for getting started with Oppia can also be found at [this wiki page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up), and we recommend that you read it before sending an email.

To discuss your project ideas, or share your proposal for feedback from the community, please email the [GSoC discussion mailing list](mailto:oppia-gsoc-discuss@googlegroups.com).