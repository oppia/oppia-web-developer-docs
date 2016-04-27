Oppia is excited to be participating in [Google Summer of Code 2016](https://developers.google.com/open-source/gsoc/)! GSoC is a global program which offers post-secondary students an opportunity to discover and work with open source organizations over the course of 3 months and be paid a stipend. Students work one-on-one with a mentor of an open source organization in order to implement either a project idea by the organization or a proposal of their own.
Feel free to check out our [GSoC organization page](https://summerofcode.withgoogle.com/organizations/5631832271880192/).

The following are Oppia's 2016 GSoC project ideas:

* [Oppia usable offline with more lightweight data transfer](#making-oppia-usable-offline-and-being-more-lightweight-in-transmitting-data).
* [Learning material requests and submission](#making-it-possible-to-submit-and-prioritize-requests-for-learning-material)
* [Creator dashboard](#creator-dashboard).
* [Android app to enable learning-on-the-go](#android-app-to-enable-learning-on-the-go)
* [Applying machine learning to code interaction](#applying-machine-learning-to-code-interaction-training-and-generalizing)
* [Re-imagining the exploration editor](#re-imagining-the-exploration-editor)

We accepted the following two proposals in 2016:
* [**@gvishal**'s proposal](pdfs/GSoC2016VishalGupta.pdf) for offline/lightweight Oppia
* [**@526avijitgupta**'s proposal](pdfs/GSoC2016AvijitGupta.pdf) for the creator dashboard.


# Students
GSoC is an excellent opportunity for students to get paid to work on an open source project. If you're interested in applying as a student, you should definitely read the following resources:

- [Google Summer of Code student guide](http://write.flossmanuals.net/gsocstudentguide/what-is-google-summer-of-code/)
- [Google's list of resources](https://developers.google.com/open-source/gsoc/resources/)
- [GSoC FAQ](https://developers.google.com/open-source/gsoc/faq)

## Getting started
If you're specifically interested in applying to work with Oppia in Google Summer of Code, we recommend you follow these steps:

1. Sign up to the [oppia-gsoc-announce@](https://groups.google.com/forum/#!forum/oppia-gsoc-announce) mailing list in order to receive important notifications about Oppia's participation in GSoC.
1. Take a look at the project ideas below, and select a project you're most interested in.
1. If you're not very familiar with what Oppia is all about (or wish to become familiarized with concepts like explorations and interactions), then our [user documentation](http://oppia.github.io/#/) will be very helpful for you! Read the [developer wiki](https://github.com/oppia/oppia/wiki), and especially [Overview of the Oppia codebase](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase) to get familiar with the codebase, and start planning your project proposal.
1. (Optional) Read the [contributors' guide](https://github.com/oppia/oppia/blob/develop/CONTRIBUTING.md), set up a development instance and work on a [starter project](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22starter+project%22) to get more familiar with the Oppia codebase and the contribution process. This will also help us get to understand your skills, and get an idea of what it's like to work with you. (**Note:** If you can't find a suitable starter project, you can also pick an issue labeled "TODO: needs instructions" -- these issues require a bit more investigation, but some of them are not too difficult.)
1. Write your project proposal! If you have any questions about your project, feel free to ask on [Gitter chat](https://gitter.im/oppia/oppia-chat), or email the mentors' mailing list at oppia-gsoc-mentors@googlegroups.com. Please be specific when asking questions; this makes it easier for us to help you.

## FAQs
**Q: What technical skills do I need to work on Oppia?**

A: Familiarity with JavaScript, Python, and Google App Engine is useful and recommended for most Oppia work. In addition UI design skills is useful for frontend work. Please see the individual project ideas to determine whether these skills are recommended or required for the project in question.

**Q: How can I increase my chances of getting selected?**

A: Writing a good project proposal, engaging with the community, helping other students can all help you. Your application will be evaluated holistically, so there's no one thing you must or must not do (other than apply!) to get selected.

**Q: Can you be flexible around other my commitments in the summer?**

A: GSoC is intended to be a full-time job, so the main concern is whether you can still get the project done on time. Be upfront about your other commitments and make sure you schedule your time accordingly when creating your proposal. The proposal should be able to reflect you being able to complete the project by the end of the summer.

**Q: Why hasn't anyone responded to my question/email/PR? :\(**

A: We are pleasantly surprised at the amount of interest we have been getting :) However, we have a limited amount of manpower, and hence may take a while to get back to you. Please be patient! If we haven't responded in more than a day or two, you can try pinging us again over chat or email.

**Q: How can I get feedback on my project proposal before submitting it?**

A: Please submit a *draft* proposal at our [GSoC Organization Page](https://summerofcode.withgoogle.com/organizations/5631832271880192/) and one or more organization members will try to review and leave comments on it (through Google Docs). The earlier you submit the draft, the more likely we will be able to review it.

## GSoC Proposal Template
When proposing a project, please use the following template:

**Project**
- Project name
- Project description
- What interests you about this project?
- What areas of research will you do in this project (if applicable)?
- Outline of a project plan and implementation schedule

**Related Technical Skills**

Please outline any prior experience you have, especially where it relates to technical skills that are needed for the above project. (Depending on the complexity of the project, we may write back and request more information in this category.)

**Open Source and Education**

Why are you interested in open source development? Why education?

**Summer Plans**
- Which timezone(s) will you primarily be in during the summer?
- How much time will you be able to commit to this project?
- Please list jobs, summer classes, and other obligations you may need to work around.

**Communication**
- What is your preferred method of communication and contact information?
- How often do you plan on communicating with your mentor?

## Types of work related to Oppia projects
In order to ensure a well-rounded engineering experience, developers will do some or all of the following depending on their project:
- Meet with their mentors regularly
- Meet with other contributors related to their project area
- Receive code reviews for all code they write for their project
- Write automated tests for their projects
- Create UI mocks (if doing frontend development)
- Write design documents (if implementing large features or introducing new systems)

## Selection Criteria

In order to select students for GSoC, we will mainly be looking at two things:
- The quality of the submitted proposal
- Our prior history/experience working with the student

This is because we believe that strong performance in these two dimensions is likely to correlate well with the student having an enjoyable, fulfilling and productive experience over the summer, and successfully completing the GSoC program.

For the proposal, we will be looking for the following:
- Specific ideas that build on the original project idea, with a strong focus on creating a simple, intuitive experience for end users.
- The ability to break down a complex task into reasonable milestones, with a clear, well-defined (and, ideally, shippable) deliverable at the end of each milestone.
- Sufficient detail (e.g. references to particular files and methods) to convince us that the applicant is not hand-waving, and has a very good understanding of both the scope of the problem and the existing codebase.
- Clarity of communication.

For prior history/experience, we will take the following into consideration:
- The quality of students' previously-submitted PRs to the project (including coding ability, debugging ability, initiative, responsiveness, independence, ability to break down complex tasks, and ability to keep commitments).
- Communication skills and English language skills.
- Enthusiasm for helping others by explaining things well.

Please note that, although we are expecting many GSoC applicants this year, we are only likely to be awarded a small number of slots since this is our first year as a participant. However, please note that you don't need to be accepted to GSoC in order to become a regular contributor to the Oppia project -- this project is run by the community for the community, and we warmly welcome anyone who would like to help out!

# Dates and Deadlines
Noteworthy dates:
- **February 8-19, 2016**: Mentoring organizations apply
- **February 29, 2016**: Mentoring organizations are announced
- **March 14-25, 2016**: Student application period
- **April 22, 2016**: Accepted students announced
- **April 22-May 22, 2016**: Community bonding period
- **May 23-Aug 23, 2016**: Students enjoy the summer by programming amazing projects for open source projects
- **Aug 30, 2016**: GSoC officially ends

# Mentors

## List of Mentors

The following are definitely mentors during Google Summer of Code:
- Ben Henning (@BenHenning)
- Sean Lip (@seanlip)
- Xinyu Wu (@wxyxinyu)

The following are partial mentors (will not be assigned a student, but will help other mentors when possible):
- Allan Zhou (@AllanYangZhou)
- Bren Briggs (@bbriggs)
- Jacob Davis (@jacobdavis11)
- Madiyar Aitbayev (@maitbayev)

## Becoming a Mentor

Are you interested in mentoring in Google Summer of Code 2016 for Oppia? Mentoring can be an extremely rewarding experience, though it is a commitment and a responsibility. You can be sure you will learn a lot from your potential mentee. To better understand what mentoring entails, check out this [GSoC mentoring guide](https://flossmanuals.net/GSoCMentoring/).

Please be aware that there are no guarantees that Oppia will have enough students for all mentors to be assigned one. Nevertheless, please email oppia-gsoc-mentors@googlegroups.com if you're interested in being a mentor!

# Communication

There are several ways to communicate with us (see sections below). Please feel free to also email the organization administrators if you have additional questions and we'll be happy to help:

- Ben Henning henning(dot)benmax(at)gmail(dot)com
- Sean Lip sean(at)seanlip(dot)org

It may help to email the Google Summer of Code mailing list, as well, which is oppia-gsoc-mentors@googlegroups.com.

## Joining Oppia's Gitter

We don't have an official IRC channel, but we do have a real-time chat channel through Gitter. Joining our Gitter chat is easily. Simply head to the following link:

https://gitter.im/oppia/oppia-chat#

You can login using your GitHub account (Gitter will ask to be associated with your GitHub account for authentication) and you will then be able to talk in it.

## Oppia's Developer Mailing List

You should also join Oppia's developer mailing list: oppia-dev@googlegroups.com. You can join by going to https://groups.google.com/forum/#!forum/oppia-dev and requesting to join the group. A group manager will need to approve the request (usually happens within a couple of hours).

Nearly all contributors to Oppia (past and present) are in this mailing list, so it's a fantastic place to ask questions that the entire team will see. All developers working on Oppia are highly recommended to join this mailing list, as major announcements are listed here (including early details on future releases and major work being done across the project).

# Oppia's Project Ideas

We have several projects that will have significant impact on Oppia and we feel would make excellent Google Summer of Code projects. This is the specific list we are outlining for GSoC, but there are many more project ideas being discussed on the team.

Feel free to suggest your own or look at our various [starter projects](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22starter+project%22) to help generate ideas for new projects, if none of the below interest you. We're also happy to discuss new ideas that you'd like to implement, outside of the projects listed below or our existing starter projects.

Finally, be aware that the projects below may either seem larger than they are or will be sized down once a student is paired with one. These projects were picked because they were self-contained, high-impact projects. Most of them involve end-to-end development, which can be very hard to do within only a summer of work. We have ranked each project based on our assumed difficulty; the projects themselves should be scoped based on students' applications and discussion with the corresponding mentors once the summer begins.

Many of the projects below involve significant work in either Oppia's frontend, backend, or both. It is very helpful to look at [the overview of Oppia's codebase](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase) as a reference.



## Making Oppia usable offline and being more lightweight in transmitting data

**Difficulty**: Medium

**Potential mentor(s)**: Ben Henning (primary)

### Summary

This is a two-part project. Oppia currently requires users to be connected to the internet at all times while playing explorations. Furthermore, Oppia sends quite a lot of data across the network while playing explorations or visiting the website in general. Both of these have a negative effect on the user experience on the site, and are likely to make Oppia difficult or impossible to use for many users who are visiting it on poor connections.

The first part of this project involves allowing some explorations to be played without an internet connection. This is a multi-step problem. While playing an exploration, there are many things that happen, including:
- Statistics recording
- Answer classification
- Response selection
- State transitions

Most of these now happen in the frontend, however, there are still a few aspects of the communication between the frontend and backend that need to be changed in order to allow offline playing. Furthermore, there's no concept of persistent frontend storage at the moment (which might be needed in order to save some explorations and go back to play them without an internet connection).

The second part of this project is decreasing the amount of data Oppia sends between the backend and frontend. Oppia was not originally written with mobile or poor internet connections in mind. There have been recent efforts by contributors to concatenate and minify Oppia's CSS and JS resources, though these are just stepping stones in the longer strategy of making Oppia more efficient bandwidth-wise for users.

**Expected results**: Users will be able to play some Oppia explorations without any Internet connection. Also, there is a measurable decrease in data sent between the browser and the server when visiting any pages on Oppia.

### Required skills/knowledge
Required:
- Familiarity with AngularJS
- Familiarity with Python
- Familiarity with Google App Engine

Recommended:
- Code investigation skills
- Familiarity with frontend data storage solutions
- Understanding of RESTful APIs

Both parts of this project involve a lot of investigation, since you will need to figure out which parts of the protocol need to be adjusted in order to facilitate offline playing or how to optimize the protocol or other parts of the Oppia stack to reduce the amount of data sent across the network.


## Making it possible to submit and prioritize requests for learning material

**Difficulty**: Medium

**Potential mentor(s)**: Ben Henning (primary), Xinyu Wu (secondary)

### Summary

Currently, https://www.oppia.org serves as a repository of almost random explorations users have created. Although it's fantastic that users create these explorations, we think Oppia will be a lot more effective to both learners and exploration creators if there is some way for people to submit requests for new explorations and have creators address those requests by directly creating the corresponding exploration(s) (see [issue 490](https://github.com/oppia/oppia/issues/490)).

This project involves writing a system for creating, listing, and addressing requests for new content. Users should be able to see and search for content requests, be able to create a new request for content (including a brief description), and vote on existing requests. Creators will be able to use the same searching functionality to find top-ranked requests and address them by listing a specific exploration or collection which they feel satisfies the request. It's not yet clear what the exact flow of this should be; we will leave it up to the student's proposal to clarify how they feel learners and creators should interact when addressing content requests. Some things to consider in this area include:

- Should any creator be able to address any request (even very popular ones)?
- Should the request be closed when an exploration/collection is associated with a request?
- Should explorations and interactions even be associated with requests?
- Should requests allow back-and-forth discussion among the community?
- Should the author of the request be responsible for closing the request when an exploration/collection is made which satisfies it?

Those are just a few questions to get started thinking about the system.

**Expected results**: Users will be able to navigate to a dashboard containing existing requests for new explorations and collections. They will be able to create new requests and view their own. Creators will be able to solve these requests in some way by creating an exploration or collection and addressing a particular request or requests. The exact nature of this resolving behavior is up to the student and will be discussed as part of this project. The overall user flow and interfaces will also be up to the student.

### Required skills/knowledge

This is an end-to-end project and involves hands-on work with both frontend and backend code.

Required:
- Familiarity with Python
- Familiarity with AngularJS

Recommended:
- Familiarity with Google App Engine (which uses a NoSQL data store)
- Familiarity with creating mocks with programs such as Sketch (definitely not a requirement, but it will help)

Students will be requested to create mocks (even if they're just drawings on paper) and a design document outlining the technical changes needed in the frontend and backend for implementing this system. The mocks are expected to be a first iteration of the overall learner request system, so they will not be expected to be highly detailed or fleshed out. They should be able to express the basic UI structure and demonstrate user flow through the system. Students will also be working with people across the team since this project is multi-disciplinary.



## Creator dashboard

**Difficulty**: Medium

**Potential mentor(s)**: Sean Lip (primary), Allan Zhou (secondary)

### Summary

Oppia's approach to creating educational content is incremental -- that is, the content is not created all at once, but is improved over time based on answers and feedback from students. Analysis of these answers can help lesson creators detect and respond to common misconceptions, so that students who encounter similar issues in the future can receive better feedback from Oppia.

The purpose of this project is to implement a creator dashboard that allows lesson creators to see, at a glance, completion rates, common student misconceptions, and student-submitted feedback for their lessons -- and to make it easy for creators to take action on this information. There should also be a button on that page that allows creators to build a new exploration. A design project for this page is currently underway, and we already have some preliminary wireframes (see [issue #1366](https://github.com/oppia/oppia/issues/1366#issuecomment-198021655)), but these may undergo further iterations as we make progress on implementation and usability testing. If you are interested, we welcome your participation in the design process!

**Expected results**: A page in Oppia that displays the above information for creators in a way that is easy to understand and that also makes it easy for them to take action. Some backend computation would also be needed to aggregate the relevant data and keep it up to date.

### Required skills/knowledge

Familiarity with Python and AngularJS; ability to accurately implement UIs based on designers' mocks. Also useful (but not required): ability to create and edit design mocks (e.g. using Sketch).

Since this is a full-stack project, you might also find the [Overview of the Codebase](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase) wiki page helpful in order to get a sense of how the Oppia stack works.

## Android app to enable learning-on-the-go

**Difficulty**: Hard

**Potential mentor(s)**: Ben Henning

### Summary

The world is increasingly becoming a mobile-driven environment, with well over one billion users of smart phones. Although Oppia is a responsive website for learners, there is much to gain by having a dedicated Android app. Maintaining a responsive website is challenging and there are almost certainly going to be issues when viewing the site on different devices.

This project will introduce a dedicated mobile interface for Oppia, through either web views, targeted styling for the web application, or a native Android interface. This mobile interface will make it easier for users to access their profile, browse the gallery, and play through explorations.

**Expected results**: An Android app which allows users to access primary portions of Oppia's website (the profile page, gallery, and exploration player) and be able to play through an exploration.

### Required skills/knowledge

Required:
- Java and extensive comfort writing Java applications
- Familiarity with AngularJS: the developer working on this project will need to understand how Oppia's frontend works (which can be learned prior to the project starting)

Recommended:
- Android development experience
- Familiarity with Google App Engine (Python)
- Familiarity with RESTful APIs



## Applying machine learning to code interaction training and generalizing

**Difficulty**: Hard

**Potential mentor(s)**: Ben Henning (primary), Allan Zhou (secondary)

### Summary

Since Oppia needs to be a smart tutor which provides personalized feedback to learners, machine learning has great potential application to Oppia. There are some efforts into allowing creators to train Oppia to reply with targeted responses based on which answers a user submits when playing through an exploration. This support is not yet enabled on https://oppia.org as of the beginning of Google Summer of Code, but is being actively developed and can support the work on this project. It will also be turned on for the public to use before the end of summer.

The new functionality introduces a training interface in the exploration editor wherein creators can see previous user answers, then select which response Oppia should use if it encounters that answer again (or the creator can create a new response, instead). We then train a classifier in the background so that Oppia can hopefully place new answers in the correct response "bucket" before the creator teaches it to do so. The training interface will be available for a few interactions, but the machine learning part will only be available for text input. Although text input with machine learning is a fascinating and highly useful topic, this project focuses on applying machine learning for training our code evaluation interactions, instead.

The code evaluation interaction allows learners to type in code in order to match some sort of output, avoid an error, or match specific code. The code is evaluated in the frontend, but the learner's answer is stored in the backend. Python is the only supported language, though we will definitely be adding more languages in the future.

This project involves figuring out a way to cluster together similar pieces of code (though not exactly the same) and then use that to train a classification model that can predict which cluster a new piece of code belongs to. Originally, members of the Oppia team were considering integration with [OverCode](http://people.csail.mit.edu/elg/overcode), though there were some technical concerns with how it would integrate with Oppia. Using an existing library is completely fine for this project and even encouraged. The complexity of this project includes discovering a library, integrating it, and making sure it works well in practice.

At the end of the project, creators will be able to train Oppia to respond to certain types of code submitted by learners. Oppia will be able to encounter new pieces of code it has not yet seen, and intelligently classify them into previously learned buckets, if that new piece of code is sufficiently similar semantically to previously taught bits of code.

**Expected results**: Creators will be able to train Oppia to recognize buckets of user-submitted Python code answers using the existing training infrastructure and a new code classifier. Creators will also be able to test if a particular code sample fits within the bucket they expect, where buckets lead to Oppia providing a targeted reply based on the answer.

### Required skills/knowledge
Required:
- An understanding of machine learning concepts, including clustering and statistical classification techniques
- Experience with coding in Python

Recommended:
- Google App Engine
- NoSQL storage systems
- RESTful APIs

Students working on this project will need to write a design document explaining which library/libraries they plan on integrating, as well as an overall solution to solving the clustering problem. Some emphasis will be placed on ensuring it will work within the answer classification infrastructure, though there are many members of the Oppia team who will happily assist with explaining this to the student. Finally, there may be some emphasis also placed on solving this project in such a way that it can be extended to future languages, rather than being fixed specifically to Python.

## Re-imagining the exploration editor

**Difficulty**: Hard

**Potential mentor(s)**: Sean Lip

### Summary

The Oppia editor is powerful and feature-rich. This is good for users who desire flexibility, but not good for first-time users and people who "just want to teach online". Hence, a priority for Oppia this year is to simplify the editor to the point where it is easily accessible to first-time exploration creators.

More specifically, when someone creates an exploration for the first time, we'd like them to create something that's fairly linear (see the notes on "critical path" [here](http://oppia.github.io/#/DesignTips)). The emphasis here is on minimizing the amount of time needed for the creator to build something that they are happy with publishing and sharing; generally speaking, this should happen in 30 minutes or less, and be of similar difficulty to writing a short blog post on the subject. Note that it is totally fine for the explorations thereby created to use only a small subset of the functionality that Oppia provides -- they can always be augmented later.

This project is currently in the conceptualization/idea phase. A number of Oppia's current contributors are now working on ideas and creation UX stories (e.g., should the 'simple' experience be: "write a dialog, and then press a button to break it up into cards?"). The plan is to test these ideas with users and produce low-fidelity mocks by the end of April. The GSoC project itself will then involve building prototypes of these mocks, validating them with users, planning a suitable implementation strategy for integrating this into the current editor, and implementing the new editor.

**Expected results**: New creators discovering Oppia for the first time should, within 30 minutes, be able to successfully create and publish an exploration that they are proud of.

### Required skills/knowledge
Required:
- Strong experience coding in AngularJS.
- Strong familiarity with the existing editor codebase.
- Willingness and ability to do frequent user experience testing.

Recommended:
- Good design taste.
- Prior experience with major codebase refactoring.

Students working on this project are encouraged to submit: (a) ideas for a "simpler" editor (ideally fleshed out using concrete examples of lessons), (b) an overview of how they would plan the transition from the current editor to the simpler one.
