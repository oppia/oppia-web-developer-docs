In 2018, Oppia plans to apply to participate in [Google Summer of Code](https://developers.google.com/open-source/gsoc/). GSoC is a global program which offers post-secondary students an opportunity to discover and work with open source organizations over the course of 3 months, while being paid a stipend. Students work closely with one or more mentors from an open source organization in order to implement either a project idea by the organization, or a proposal of their own.

Since GSoC mentoring organizations are typically not announced until February or March of the year in question, it is not yet known whether Oppia will be participating in Google Summer of Code 2018. This page will be updated accordingly once it is known whether Oppia is participating. You might also be interested in the GSoC info pages from [2017](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2017) and [2016](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2016).

Please note, however, that acceptance into GSoC isn't a prerequisite for [becoming an Oppia contributor](https://github.com/oppia/oppia/wiki). The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out!

# Students
GSoC is an excellent opportunity for students to get paid to work on an open source project. If you're interested in applying as a student, you should definitely read the following resources:

- [Google Summer of Code student guide](http://write.flossmanuals.net/gsocstudentguide/what-is-google-summer-of-code/)
- [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
- [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)

## Getting started

If you're interested in applying to work with Oppia for GSoC, please follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC.

1. Get a better understanding of what Oppia is all about by taking a look at our [user documentation](http://oppia.github.io/#/) -- this will help you become familiar with important concepts like explorations and interactions. We'd also recommend having a go at playing/creating lessons on [Oppia.org](https://www.oppia.org), which hosts a live instance of Oppia.

1. Read and follow the instructions in the [contributors' guide](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) carefully.

1. Consider taking up one or more starter projects in order to become familiar with the contribution process. This will help us get an idea of what it's like to work with you -- e.g. how independent, resourceful, responsive, etc. you are. It will also help you get a better understanding of the codebase, so that you can write a good, detailed project proposal.
    - **Pro-tip!** Quality is more important than quantity; we want to see examples of your best work. So, please make sure to follow the [dev workflow](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#instructions-for-making-a-code-change) carefully, manually test your code before submitting (to ensure it does what you want it to and doesn't break anything else), ensure that your code conforms to the [style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide), and pay attention to small details. These are good skills to learn when developing software in general, and they will also help you build credibility as a responsible developer who can be trusted to be a good steward of the Oppia codebase.

1. When you've done enough starter projects to get a good understanding for the "lay of the land", select one or more GSoC projects that you're most interested in (after they're announced in January), and write your project proposal! If you have any questions about a project, feel free to ask on [Gitter](https://gitter.im/oppia/oppia-chat) or email the [mentors' mailing list](mailto:oppia-gsoc-mentors-17@googlegroups.com). Please be specific when asking questions, since this makes it easier for us to help you.

## FAQs

**Q: What technical skills do I need to work on Oppia?**

A: Familiarity with AngularJS (v1), Python, and Google App Engine is useful and recommended for most Oppia work. In addition, UI design skills are useful for frontend, user-facing work. Please see the individual project ideas to determine whether these skills are recommended for the project in question.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other students, successfully contributing patches, and demonstrating that you can work independently can all help you. We've also compiled some notes below on the [selection criteria](https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2018#selection-criteria) we'll be using this year.

**Q: Can you be flexible around my other commitments in the summer?**

A: GSoC is intended to be a full-time commitment, so the main concern is whether you can still get the project done on time. Be upfront about your other commitments and make sure you schedule your time accordingly when creating your proposal. Other commitments you should list include time where you'll be in school and will commit less time to GSoC, time you will be travelling and away from GSoC work, any summer jobs you need to commit to etc. We will try to be flexible around other time commitments, as long as we are convinced by your proposal that you will have enough time to complete the project by the end of the summer. On the other hand, if you do not disclose other commitments, and it turns out you are unable to commit to what you wrote on your proposal, this is grounds for failing the program.

## GSoC Proposal Template
When proposing a project, please use the following template:

**Project Details**
- Project name
- Why are you interested in working with Oppia?
- What interests you about this project? Why is it worth doing?
- Prior experience (especially with regards to technical skills that are needed for the project)
- Links to 1-5 PRs you've made that showcase your best work, especially any Oppia ones. The list should include at least one Oppia PR, but you can also include some other PRs from major open-source projects if you like.
- Project plan and implementation strategy.

**Summer Plans**
- Which timezone(s) will you primarily be in during the summer?
- How much time will you be able to commit to this project?
- What jobs, summer classes, and other obligations might you need to work around? Please be upfront about any existing commitments you may have.

**Communication**
- What is your contact information, and preferred method of communication?
- How often do you plan on communicating with your mentor?

### Notes on the project plan

The project plan is the most important section of the proposal, since it outlines what you'll be doing during the summer. Here's some guidance on what the mentors and organization admins will be looking for in this section:

- **Three clear milestones** explaining the deliverables to be achieved by the end of each of the three GSoC coding periods. Strong proposals will have clear, concrete and well-defined milestones, whose success can be readily evaluated by an external observer. It's OK to break up a milestone into smaller milestones over smaller timescales, but individual milestones should represent *concrete* deliverables that can be merged into the "develop" branch. Please try to be realistic when setting milestones, and don't over-promise.

- **A technical design and implementation plan**. The project ideas below are annotated with some notes from the mentors, but please bear in mind that these notes are not exclusive and shouldn't serve as a substitute for thinking carefully and critically about the project from first principles -- their main purpose is to suggest ideas or possible starting points. If, in your thinking, you find aspects not mentioned in the notes, feel free to include a discussion of these aspects in your proposal. (For example, certain projects may require a migration of existing production data, and this needs to be accounted for in the project plan.) Strong proposals will demonstrate familiarity with the codebase, a realistic implementation plan, and attention to detail.

- **Mocks or wireframes**, if appropriate. For user-facing projects, we strongly favour proposals that demonstrate an empathy for the user. If you're proposing frontend design mocks, we suggest showing your ideas to your friends and getting their critical feedback, so that you can be confident that others find them intuitive as well. Note that you do not need to make your mocks pixel-perfect, but they should illustrate the primary user journeys clearly enough for us to understand exactly what you're proposing. Also, bear in mind that more is not necessarily better -- an important aspect of user-focused design is deciding what _not_ to do.

## Types of work related to Oppia projects
In order to ensure a well-rounded engineering experience, developers will do some or all of the following depending on their project:
- Meet with their mentors regularly
- Meet with other contributors related to their project area
- Receive code reviews for all code they write for their project
- Write automated tests for their projects
- Create UI mocks (if doing frontend development)
- Write design documents (if implementing large features or introducing new systems)

## Selection Criteria

In order to select students for GSoC, we will mainly be looking at three things:

- The quality of the submitted proposal
- The quality of the applicant's previously-submitted PRs (in order to assess their ability to code, debug, break down complex tasks, etc.). Note that quantity in itself isn't a prerequisite, though contributors who've submitted multiple PRs are likely to have had more opportunities to demonstrate the abilities needed to succeed in GSoC.
- Our prior experience working with the student (e.g. do they keep commitments, communicate well, demonstrate independence/initiative/responsiveness, help others, etc.)

We believe that strong performance in these dimensions is likely to correlate well with the student having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the GSoC program.

For the proposal, we generally look for a clear indication that the student has a good, deep understanding of the project, and has broken down the project sufficiently well, in a way that makes it very likely to succeed. Some indicators that could help with this include:
- A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating a simple, intuitive experience for end users.
- A concrete, specific breakdown of the work to be done for each milestone. Here's an [example](https://docs.google.com/document/d/1vuwXvHOYXqfM2S2B2KIWhZrAa1PL59wJRUYsqJEd67E/edit#heading=h.ci6rc1u061yj) from a previous design doc. (Note that, in this example, the author has carefully considered and listed which tests need to be written alongside the code; this is a positive indicator.)
- Sufficient concreteness (e.g. references to particular files and methods) to demonstrate that the applicant is familiar with both the scope of the problem and the existing codebase.
- A description, if applicable, of how the applicant plans to mitigate risks that could potentially derail the project.
- Clear, unambiguous communication. (This is important; your proposal will be read by many mentors!)

# Oppia's Project Ideas

Around January 2018, the Oppia team will select and publish a list project ideas that we believe would have significant impact on Oppia, and would make excellent Google Summer of Code projects. Check this space later on for more details!

# Other useful information

## List of Mentors

TBD

## Communication

**Chat**

Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](
https://gitter.im/oppia/oppia-chat#)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it.

**Email**

If you have questions, please ask them on Gitter, or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you.

If you want your question to be read only by the mentors, you can instead send it to the Oppia GSoC mentors mailing list at oppia-gsoc-mentors-18@googlegroups.com. However, note that open communication means that more people are likely to be able to help you (and is more in line with the spirit of an open source project), and you can also get feedback from the community at large. For similar reasons, we recommend not pinging individual mentors personally -- it's better to use the GSoC mentors mailing list.