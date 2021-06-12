## General notes on team structure

The Oppia team is a distributed team of contributors from all over the world. In order to ensure that the project is as stable as possible, we have a number of infrastructure teams devoted to maintaining the health of various aspects of the development workflow. We also have an onboarding team who helps new contributors get started with the project, as well as project leads who are in charge of specific initiatives or sections of the Oppia project.

This wiki page explains the different teams in Oppia and their composition.

## Infrastructure teams

### Core Maintainers

The core maintainers team is accountable to the Oppia developer community with regards to preserving the stability of the entire Oppia codebase, by ensuring that the following things are true at all times for the "develop" branch on GitHub:

- It is free of serious bugs that adversely impact the end user experience.
- It passes the CI checks.
- It has no security issues.

Because this group understands the "big picture" of Oppia, other contributors are expected to take their advice seriously, especially when members of this group are acting in an incident-response capacity.

The current members of this group are:

- Ben Henning (who also leads the efforts on Oppia Android)
- Brian Rodriguez
- Chris Skalnik
- Nithesh Hariharan (who also serves as release coordination lead)
- Kevin Thomas
- Sandeep Dubey (who also serves as dev workflow team lead)
- Sean Lip
- Srijan Reddy Vasa
- Vojtěch Jelínek (who also serves as release coordination lead)

Membership of this group is decided by appointment, by a committee made up of the currently-serving core maintainers.

Contributors should notify the Core Maintainers when they see major bugs or security vulnerabilities (general or npm). The Core Maintainers group can be contacted via the **@oppia/core-maintainers** alias or at oppia-core-maintainers@googlegroups.com.

### Release process team

(Currently led by Vojtěch Jelínek and Nithesh Hariharan.)

This team is responsible for ensuring that Oppia releases happen smoothly, correctly, and on time. Long-term projects include:
- Streamlining the release process, and automating as many parts as possible, in order to reduce the chance of human error.
- Adding automatic safeguards to ensure the correctness of releases.
- Organizing the release coordinator rotation.

### QA team

(Currently led by Nithesh Hariharan.)

This team is responsible for ensuring that the Oppia codebase and releases are bug-free. Long-term projects include:

- Deciding on strategy for maintaining test coverage.
- Improving test coverage to 100%.
- Reducing the StackDriver error count to 0.
- Organizing the QA and bugfixing teams for each release.
- Fix any known bugs in Oppia (especially user-facing ones).

### Development workflow team

(Currently led by Sandeep Dubey.)

Ensures that the Oppia development process is smooth, stable and enjoyable, by ensuring that the following always hold:
- There are no issues with codebase setup (especially for new contributors).
- Automated checks work as intended and not unduly burdensome on both contributor’s machines and CI servers.
- The technical documentation on the wiki is well-arranged, useful, and correct.
- There are no security issues relating to npm dependencies.
- The review process is speedy and streamlined.

Long-term projects include:
- Working with the Onboarding team to identify areas where new contributors get stuck during the onboarding process, and taking steps to fix those issues.
- Streamlining the code review flow by: (a) adding pre-submit checks for common errors, (b) enabling Oppiabot to automatically handle review/code-owner assignments, (c) speeding up the CI processes.

## Onboarding Team

(Currently led by Sandeep Dubey.)

The onboarding team aims to welcome new contributors and answer their questions.

The current members of this group are:

- Akshay Anand
- Ankita Saxena
- Brian Rodriguez
- Chris Skalnik
- Nithesh Hariharan
- Nitish Bansal
- Rajat Talesra
- Rishabh Rawat
- Sandeep Dubey


## Project Leads and Code Owners

In order to streamline development efforts, many of the major projects in Oppia are organized as small development teams containing 2-5 members. The projects are listed in the [Projects](https://github.com/oppia/oppia/projects) page, and each team has a team lead who is responsible for the success of the project. 

A team lead is a position of responsibility in the Oppia project, and it involves coordinating the efforts of a small team in order to improve a part of the site. This is a good way to get some experience in technical leadership. The duties of a team lead are as follows:

- Own the main design doc(s) for your project, and figure out how to break your project into subprojects that can be worked on independently.
- Be the point of contact for new contributors who'd like to help with your project, and suggest things that they can do.
- Keep the GitHub project page organized.
- Assist core maintainers in debugging major bugs that fall within their code ownership when necessary.

In general, project leads also serve as code owners. They take ownership of sections of the codebase by performing code owner reviews.
