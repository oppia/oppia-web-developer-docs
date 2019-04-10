## Table of Contents
* [Getting started](#getting-started)
* [Season of Docs Proposal](#season-of-docs-proposal)
  * [Template](#template)
  * [Tips for writing a good project plan](#tips-for-writing-a-good-project-plan)
  * [Selection criteria](#selection-criteria)
* [Project Ideas](#project-ideas)
* [Other useful information](#other-useful-information)
    * [Dates and Deadlines](#dates-and-deadlines)
    * [List of Mentors](#list-of-potential-mentors)
    * [Communication](#communication)

Oppia is planning to participate in first year of [Season of Docs](https://developers.google.com/season-of-docs/). The program connects open source organizations with technical writers, who then work on 3 or 6 month long projects, and then can receive a paid stipend. The technical writers work closely with two or more mentors on finishing a project idea by the organization, or a proposal of their own.

Also, please note that acceptance into Season of Docs isn't a prerequisite for [becoming an Oppia contributor](https://github.com/oppia/oppia/wiki). The Oppia project is run by the community for the community, and we warmly welcome anyone who'd like to help out!

# Getting started
If you're interested in applying to work with Oppia for Season of Docs, please follow these steps:

1. Sign up to the [oppia-sod-announce@](https://groups.google.com/forum/#!forum/oppia-sod-announce) mailing list in order to receive important notifications about Oppia's participation in Season of Docs. If you like, you can also sign up to the [oppia-sod-discuss@](https://groups.google.com/forum/#!forum/oppia-sod-discuss) mailing list to participate in general discussion related to Oppia's involvement in Season of Docs (see point 5 below, too). Make sure to set your mailing list preferences correctly so that you actually get the emails!

1. Get a better understanding of what Oppia is all about by taking a look at our [user documentation](http://oppia.github.io/#/) — this will help you become familiar with important concepts like explorations and interactions. We also recommend having a go at playing some of the existing lessons on [Oppia.org](https://www.oppia.org), like [these ones on Fractions](https://www.oppia.org/fractions), to get a better idea of what they look like.

1. If you think that you're familiar enough with Oppia, select one or more Season of Docs projects that you're most interested in, and write your project proposal! We strongly encourage you to discuss your project ideas and share your proposal with the community, so that you can get feedback and ensure that what you're writing makes sense to others. The best way to do this is to put your proposal into a collaborative editing tool like Google Docs, allow others to comment on it, and share a link to it on the [Season of Docs discussion mailing list](mailto:oppia-sod-discuss@googlegroups.com). You can also email this mailing list if you have any questions about a project, or would like to discuss your approach with the Oppia community and get feedback. Please be specific when asking questions, since this makes it easier for us to help you.

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

* **Milestones** that will divide your work into multiple parts, you can set milestones for each month or for each week. Strong proposals will have clear, concrete and measurable milestones, whose success can be objectively evaluated by an external observer.

* **Technical analysis** of the pages/guides/how-tos that you plan to write, you want to provide rough draft for each page you plan to write. For guides you might want to make a list of steps that will the guide include and what files will that guide reference.

## Selection criteria

In order to select technical writers for Season of Docs, we will mainly be looking at two things:

- The quality of the submitted proposal
- The quality of the applicant's previous technical writing related work

We believe that strong performance in these dimensions is likely to correlate well with the technical writer having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the Season of Docs program.

For the proposal, we generally look for a clear indication that the technical writer has a good, deep understanding of the project. Some indicators that could help with this include:
- A clear analysis of (and good design decisions that build on top of) the original project idea, with a strong focus on creating clear and understandable documentation for users or developers.
- A concrete, specific breakdown of the work to be done for each milestone.
- Sufficient concreteness (e.g. references to particular files and methods that will be relevant for the documentation) to demonstrate that the applicant is familiar with both the scope of the problem and the existing codebase.
- Clear, unambiguous communication. (This is important; your proposal will be read by many mentors!)

# Project ideas
### Beginners’ guide to creating stuff on Oppia
Guide for new Oppia creators about lessons/explorations, skills, lesson translations, the interface of the Oppia page. Currently our user documentation is hosted on [oppia.github.io](http://oppia.github.io) pages, but if you prefer other platform to host the documentation you can explain that in your proposal.
#### List of guides to write
* How to organize skills and create a story outline for a topic.
* How to create a lesson that fits in a story.
* How to use the "translation tab", "stats tab", "history tab" and  "feedback tab" effectively.
* How to enhance a lesson based on the information provided by stats and playthroughs
* How to translate or add voiceovers to a lesson
* How to add images to a lesson.
* How to write a lesson that is accessible.
* How to write practice questions for a skill.
* Explanation about the different roles in the exploration, including the hierarchy and the rights of each role. 
#### Knowledge/Skills needed
* technical writing experience

### Guide for Oppia developers
Guides for Oppia developers that are in the form of “how tos” and provide useful resources for new but also experienced developers. Can extend some of ours already existing wiki pages. Currently our documentation is hosted as a [GitHub Wiki](https://github.com/oppia/oppia/wiki) pages, but if you prefer other platform to host the documentation you can explain that in your proposal.
#### List of guides to write
* How to install and start Oppia
* How to deploy Oppia on Google App Engine
* How to write a backend job
* How to write, test and run a migration
* How to create a new interaction type
* How to write good backend tests
* How to write good frontend tests
* How to write good end-to-end tests
* How to write a new lint check
* How to write code that is effective and doesn’t affect the page speed
* How to upgrade third party library
* Onboarding guide for the dev workflow team
* Onboarding guide for the QA team
* Onboarding guide for the onboarding team
#### Knowledge/Skills needed
* technical writing experience
* slight knowledge of Python
* slight knowledge of Angular

### Descriptive “how it works” docs for our codebase
Documentation for our codebase, that explain the structure of our frontend and backend. Can extend some of ours already existing wiki pages. Currently our documentation is hosted as a [GitHub Wiki](https://github.com/oppia/oppia/wiki) pages, but if you prefer other platform to host the documentation you can explain that in your proposal.
#### Places in codebase to explain
* Overview of the codebase, including examples of how a request/response works (see TODO at the bottom of this page)
  * frontend
  * backend
  * build process
* How are our data stored
  * images
  * explorations, skills, questions, topic
  * feedback, suggestion
  * users
* How are various extensions structured
  * rich_text_components
  * interactions
  * visualizations
  * issues and actions
  * schema-based editors
  * object editors
#### Knowledge/Skills needed
* technical writing experience
* slight knowledge of Python
* slight knowledge of Angular

# Other useful information
## Dates and Deadlines
Mar 16 – Apr 23: Organizations apply
Apr 30: Organizations are announced
Apr 30 – Jun 28: Technical writers application period
Jul 30: Accepted technical writers are announced
Aug 1 – Sep 1: Community bonding period
Sep 2 – Nov 29: Technical writers create documentation to their projects (short-running project)
Sep 2 – Feb 21: Technical writers create documentation to their projects (long-running project)

## List of Potential Mentors
* Sandeep (@DubeySandeep)
* Sean (@seanlip)
* Vibhor (@vibhor98)
* Vojta (@vojtechjelinek)

## Communication
#### Chat
Oppia doesn't have an official IRC channel, but we do have a real-time chat channel on [Gitter](
https://gitter.im/oppia/oppia-chat)! You can log in using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it. Please feel free to use Gitter if you just want to say hi to the community or if you have any questions related to getting started.

#### Email
If you have questions pertaining to "how-to-get-started", please ask them on [Gitter](
https://gitter.im/oppia/oppia-chat), or the oppia-dev@ mailing list. Please be specific when asking questions; this makes it easier for us to help you.