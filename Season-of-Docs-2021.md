## Table of Contents
* [Getting started](#getting-started)
* [FAQ](#faq)
* [Starter projects](#starter-projects)
* [Season of Docs Proposal](#season-of-docs-proposal)
  * [Template](#template)
  * [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan)
  * [Selection criteria](#selection-criteria)
* [Project Ideas](#project-ideas)
* [Other useful information](#other-useful-information)
    * [Dates and Deadlines](#dates-and-deadlines)
    * [List of Mentors](#list-of-potential-mentors)
    * [Communication](#communication)

Oppia is participating in [Season of Docs](https://developers.google.com/season-of-docs/) program! This program provides support for open source projects to improve their documentation and gives professional technical writers an opportunity to gain experience in open source. The technical writers work closely with one or more mentors on finishing a project idea given by the organization.

Please note that acceptance into Season of Docs isn't a prerequisite for [becoming an Oppia contributor](https://github.com/oppia/oppia/wiki). The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out!

# Getting started
If you're interested in applying to work with Oppia for Season of Docs, please follow these steps:

1. Sign up to the [oppia-sod-announce@](https://groups.google.com/forum/#!forum/oppia-sod-announce) mailing list in order to receive important notifications about Oppia's participation in Season of Docs. If you like, you can also sign up to the [oppia-sod-discuss@](https://groups.google.com/forum/#!forum/oppia-sod-discuss) mailing list to participate in general discussion related to Oppia's involvement in Season of Docs. Make sure to set your mailing list preferences correctly so that you actually get the emails!

1. Get a better understanding of what Oppia is all about by taking a look at our [user documentation](http://oppia.github.io/#/) — this will help you become familiar with important concepts like explorations and interactions. We also recommend having a go at playing some of the existing lessons on [Oppia.org](https://www.oppia.org), like [these ones on Fractions](https://www.oppia.org/fractions), to get a better idea of what they look like.

1. If you think that you're familiar enough with Oppia, select one or more Season of Docs projects that you're most interested in, and write your project proposal! We strongly encourage you to discuss your project ideas and share your proposal with the community, so that you can get feedback and ensure that what you're writing makes sense to others. The best way to do this is to put your proposal into a collaborative editing tool like Google Docs, allow others to comment on it, and share a link to it on the [Season of Docs discussion mailing list](mailto:oppia-sod-discuss@googlegroups.com). You can also email this mailing list if you have any questions about a project, or would like to discuss your approach with the Oppia community and get feedback. Please be specific when asking questions, since this makes it easier for us to help you. You can also start working on one of the [starter projects](#starter-projects).

# FAQ

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other students, successfully contributing to already existing documentation  ([Technical documentation](https://github.com/oppia/oppia/wiki) and [User documentation](http://oppia.github.io/#/)), and demonstrating that you can work independently can all help you. You can also propose some more ambitious projects and changes that we might want to implement in our documentation.

# Starter projects
### _Starter projects will be added soon_

# Season of Docs Proposal
**Important**: Please make sure that your final proposal is self-contained! In particular, to be fair to all applicants, key components of the proposal should not be editable after the deadline, and you shouldn't assume that reviewers will follow external links.

## Template
When submitting a proposal, please use the following template:
#### Project Details
* Name of the project.
* Why are you interested in working with Oppia?
* What interests you about this project?
* Project plan and implementation strategy. This is the most important section of the proposal.
* The platform you want to use for hosting the documentation

#### Other Commitments
* Which timezone(s) will you primarily be in during the implementation phase?
* How much time will you be able to commit to this project?

#### Communication
* What is your contact information, and preferred method of communication?
* How often, and through which channel(s), do you plan on communicating with your mentor?

## Tips for writing a good project plan

* The plan should include **milestones** that divide your work into multiple parts. You can set monthly or weekly milestones. Strong proposals will have clear, concrete and measurable milestones, whose success can be objectively evaluated by an external observer.

* The plan should include a **breakdown** of the pages/guides/how-tos that you plan to write, possibly including rough drafts or samples. For guides, you might want to make a list of steps that the guide should include, and what files the guide should reference.

## Selection criteria

In order to select technical writers for Season of Docs, we will mainly be looking at three things:

- The quality of the submitted proposal
- The quality of the applicant's previous technical writing related work
- The quality of the applicant's starter project

We believe that strong performance in these dimensions is likely to correlate well with the technical writer having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the Season of Docs program.

For the proposal, we generally look for a clear indication that the technical writer has a good, deep understanding of the project. Some indicators that could help with this include:
- Clear, unambiguous communication.
- A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating clear and understandable documentation for users or developers.
- A concrete, specific breakdown of the work to be done for each milestone.
- A proposal that is sufficiently concrete to demonstrate that the applicant is familiar with the scope of the problem they're tackling. This may include pointers to parts of the Oppia codebase.

# Project ideas

## Guide for Oppia developers

### Problem statement
The Oppia project has a large technical community, comprising numerous open-source contributors from around the world. However, there are several development processes, principles, and practices that the team follows but which are not clearly documented anywhere. This can sometimes make it hard for newer contributors to the project to get started, since it results in their being unaware of these processes and practices, and sometimes lacking the necessary context to tackle issues successfully.

Currently, reviewers and mentors help/guide contributors with such questions. However, we do need to document these guidelines/principles in order to ensure that the project is welcoming and accessible for new contributors, and to help these developers contribute independently and effectively.
### Project’s scope
This project involves organizing the information architecture of the Oppia wiki. As part of this, several new additional short guides for Oppia developers in the form of “how-tos” will need to be written; these guides are intended to be helpful in addressing common questions asked by both new and experienced developers. The aim is to address all questions that Oppia developers regularly face in their work. This project would therefore include writing/updating documentation on the following topics:
1. How-to docs:
   * How to set-up the development environment in different[a] text editors/IDEs [Sublime, VScode, Atom]
      * How to integrate third-party linters and register custom linters.
      * How to set up the IDE to quickly run tests.
      * How to set up the environment to support easy debugging.
   * How to write and test an Apache Beam job
   * How to write a new lint check
   * How to integrate and upgrade third-party libraries
   * How to write good end-to-end tests
2. Docs that explain various structures and processes:
   * How the various extension frameworks are structured
      * rich_text_components
      * interactions
      * visualizations
      * issues and actions
      * schema-based editors
      * object editors
      * schema validations
   * How Oppia’s build process works
   * How Oppia compiles and uses protobuffers
   * How the codebase is structured (including frontend and backend), and how to write a simple full-stack change (i.e., explain how the different pieces fit together)
   * How Oppia’s storage infrastructure works and how the different entities are connected to each other:
      * images
      * explorations, skills, questions, topic
      * feedback, suggestion
      * users

#### Knowledge/Skills needed
* Technical writing experience
* Knowledge of Python
* Knowledge of Angular

# Other useful information
## Dates and Deadlines
* Feb 09 – Mar 26: Organizations apply
* Apr 16: Organizations are announced
* _Last date for submitting your proposal to be announced soon_
* Apr 16 – May 17: Technical writer hiring
* Apr 16: Doc development can officially begin

## List of Potential Mentors
* Sandeep (@DubeySandeep)
* Sean (@seanlip)

## Communication

#### Chat
Oppia has a real-time chat channel on [Gitter](https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any questions related to getting started.

#### Email
If you have questions pertaining to "how-to-get-started", please ask them on [Gitter](
https://gitter.im/oppia/oppia-chat), or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you.
