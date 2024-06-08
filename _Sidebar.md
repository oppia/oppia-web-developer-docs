**Core documentation**
  * [Oppia's mission](Oppia's-Mission)
  * [Code of Conduct](https://github.com/oppia/oppia/blob/develop/.github/CODE_OF_CONDUCT.md)
  * **[[Get involved!|Home]]**
    * [Coders](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up)
    * [[Instructional designers|Teaching-with-Oppia]]
      * [[Create a Lesson!|Lesson-Creation-Guide]]
    * [[UX researchers|Conducting-research-with-students]]
    * [[Voice artists | Instructions-for-voice-artists]]
    * [[Designers and artists|Contributing-to-Oppia's-design]]
  * [[How to report a bug|How-to-file-a-bug-report]]
  * [[Google Summer of Code 2024|Google-Summer-of-Code-2024]]
---
**Developing Oppia**
  * [[FAQs|Frequently-Asked-Questions]]
  * [[How to get help|Get-help]]
    * [[Troubleshooting|Troubleshooting]]
  * Getting started with the project
    * **[['Getting started' guide|https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up]]**
    * [[Installing Oppia|Installing-Oppia]]
      * [[Set up your development tools|Tips-for-common-IDEs]]
    * [[How to access Oppia webpages|How-to-access-Oppia-webpages]]
      * [[Glossary of terms|Glossary-of-terms]]
      * [User documentation](https://oppia.github.io/)
    * [[Populating data on local server|Populating-data-on-local-server]]
    * Team onboarding guides
      * [[LaCE Team|LaCE-onboarding-guide]]
      * [[Contributor Dashboard Team|Contributor-dashboard]]
  * [[How the codebase is organized|Overview-of-the-Oppia-codebase]]
  * Making your first PR
    * **[[Good first issues|https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22]]**
    * [[Finding the commit that introduced a bug|How-to-find-the-commit-which-introduced-a-bug]]
    * [[Tips for finding the right code to change|Find-the-right-code-to-change]]
      * [[Tips for analyzing the codebase|Analyzing-the-codebase]]
    * [[Learning resources for developers|Learning-Resources]]
    * [[Make a pull request|Make-a-pull-request]]
      * [[Common pull request workflows|Common-pull-request-workflows]]
      * [[Coding style guide|Coding-style-guide]]
      * [[Formatters|Formatters]]
      * [[Bytes and string handling in Python 3|Bytes-and-string-handling-in-Python-3]]
  * [[Debugging|Debugging]]
    * [[Debugging Docs|Debugging-Docs]]
    * [[If your presubmit checks fail|If-your-presubmit-check-fails]]
    * [[If CI checks fail on your PR|If-CI-checks-fail-on-your-PR]]
      * [[Interpreting GitHub Actions Results|Interpreting-GitHubActions-Results]]
      * [[Debugging end-to-end tests|Debug-end-to-end-tests]]
      * [[Debugging backend tests|Debug-backend-tests]]
      * [[Debugging frontend tests|Debug-frontend-tests]]
      * [[Debugging custom ESLint check tests|Debug-custom-ESLint-check-tests]]
      * [[Debugging custom Pylint check tests|Debug-custom-Pylint-check-tests]]
    * [[Debugging datastore locally|Debugging-datastore-locally]]
    * [[Debug frontend code|Debug-frontend-code]]
    * [[Debugging Stories|Debugging-Stories]]
    * [[Testing email functionality|Testing-email-functionality]]
  * Testing
      * [[Backend tests|Backend-tests]]
      * [[Frontend tests|Frontend-tests]]
      * [[End-to-end tests|End-to-End-Tests]]
      * [[Acceptance Tests|Acceptance-Tests]]
      * [[Lighthouse Tests|Lighthouse-Tests]]
  * Codebase policies and processes
    * **[[Guidelines for launching new features|Launching-new-features]]**
    * **[[Guidelines for making an urgent fix (hotfix)|Making-an-urgent-fix-(hotfix)]]**
    * **[[Testing jobs and other features on production|Testing-jobs-and-other-features-on-production]]**
    * [[Guidelines for Developers with Write Access to oppia/oppia|Guidelines-for-Developers-with-Write-Access-to-oppia-oppia]]
    * [[Release schedule and other information|Release-schedule-and-other-information]]
    * [[Revert and Regression Policy|Revert-and-Regression-Policy]]
    * [[Privacy aware programming|Privacy-aware-programming]]
    * Code review:
      * [[Instructions for Reviewers|Instructions-for-Reviewers]]
      * [[Oppia's code owners and checks to be carried out by developers|Oppia's-code-owners-and-checks-to-be-carried-out-by-developers]]
    * Project organization:
      * [[Triaging Process|Triaging-process]]
    * QA Testing:
      * [[Guide for release testers|Release-testing-quickstart-guide]]
      * [[Instructions for QA coordinators|Instructions-to-QA-coordinators]]
    * Design docs:
      * [[How to write design docs|Writing-design-docs]]
  * Team-Specific Guides
    * LaCE/CD:
      * 👣 [[Make a simple UI change|Making-a-simple-UI-change]]
      * [[Testing for Accessibility|Testing-for-Accessibility]]
      * [[Release accessibility checklist|Release-accessibility-checklist]]
      * [[Apache Beam Jobs|Apache-beam-jobs]]
      * Translations:
        * [[Adding new translations|Adding-new-translations-for-i18n]]
        * [[How to develop for i18n|How-to-develop-for-i18n]]
      * Server errors:
        * [[Server errors and solutions|Server-errors-and-solutions]]
    * Developer Workflow:
      * [[Instructions for making PR passes|Instructions-for-making-PR-passes]]
      * [[Lint Checks|Lint-Checks]]
        * [[Custom Pylint checks|Custom-Pylint-checks]]
        * [[Custom ESLint checks|Custom-ESLint-checks]]
      * [[Wiki infrastructure|Wiki]]
        * [[Wiki style guide|Wiki-style-guide]]

---
**Developer Reference**

  * [[Oppiabot|Oppiabot]]
  * [[Git cheat sheet|Git-cheat-sheet]]
  * Frontend
    * [[How to write frontend type definitions|Guide-on-defining-types]]
      * [[TypeScript tests|TypeScript-tests]]
    * [[Frontend file naming conventions|The-File-Naming-Convention-and-Directory-Structure]]
    * [[Angular Migration|Angular-Migration]]
    * [[UX guidelines|Oppia-UX-guidelines-&-rationales]]
    * [[Writing style guide|Writing-style-guide]]
    * [[Schemas|Schemas]]
  * Backend
    * [[Backend Type Annotations|Backend-Type-Annotations]]
    * [[Writing state migrations | Writing-state-migrations]]
    * [[Calculating statistics|Calculating-statistics]]
    * [[Storage models|Storage-models]]
    * [[Coding for speed in GAE | Coding-for-speed-in-GAE]]
    * [[Adding a new page|Adding-new-page]]
    * [[Adding static assets|Adding-static-assets]]
    * [[Wipeout Implementation|Wipeout-Implementation]]
    * [[Notes on NDB Datastore transactions|Notes-on-NDB-Datastore-Transactions]]
    * [[How to handle merging of change lists for exploration properties|Guide-to-handle-merging-of-change-lists-for-exploration-properties]]
    * [[Instructions for editing roles or actions|Instructions-for-editing-roles-or-actions]]
    * [[Protocol buffers|Protocol-buffers]]
  * [[Webpack|Webpack]]
  * [[Third-party libraries|Third-party-libraries]]
  * [[Extension frameworks|Extensions-Overview]]
    * [[Rich Text Components|Rich-Text-Editor-(RTE)-Overview]]
    * [[Interactions|Creating-Interactions]]
      * [[Math Interactions Overview | Math-Interactions-Overview]]
    * [[Rules|Creating-Rules]]
    * [[Objects|Creating-Objects]]
    * [[Dependencies|Creating-Dependencies]]
    * [[Value generators|Creating-Value-Generators]]
    * [[Actions and issues|Actions-and-issues]]
  * [[Oppia-ml Extension|Oppia-ml-Extension]]
  * [[Mobile development|Mobile-development]]
  * [[Performance testing|Performance-Testing]]
  * [[Build process|Build-process]]
  * [[Best practices for leading Oppia teams|Leading-Oppia-Teams]]
  * Past Events
    * Google Summer of Code: [[2023|Google-Summer-of-Code-2023]], [[2022|Google-Summer-of-Code-2022]], [[2021|Google-Summer-of-Code-2021]], [[2020|Google-Summer-of-Code-2020]], [[2019|Google-Summer-of-Code-2019]], [[2018|Google-Summer-of-Code-2018]], [[2017|Google-Summer-of-Code-2017]], [[2016|Google-Summer-of-Code-2016]]
    * Hacktoberfest: [[2023|Hacktoberfest-2023]], [[2022|Hacktoberfest-2022]], [[2021|Hacktoberfest-2021]], [[2020|Hacktoberfest-2020]], [[2019|Hacktoberfest-2019]], [[2018|Hacktoberfest-2018]], [[2017|Hacktoberfest-2017]], [[2016|Hacktoberfest-2016]]
    * GHC Open Source Day: [[2019|GHC-Open-Source-Day-2019]], [[2018|GHC-Open-Source-Day]]
    * Season of Docs: [[2024|Season-of-Docs-2024]], [[2021|Season-of-Docs-2021]], [[2019|Season-of-Docs-2019]]
    * DSC-SLoP (Semester Long Project): [[2022|SLoP-2022]], [[2020|SLoP-2020]]
    * Outreachy: [[Dec 2021 to Mar 2022|Outreachy-Dec-2021-to-Mar-2022]]
