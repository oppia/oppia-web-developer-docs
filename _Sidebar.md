**Core documentation**
  * [Oppia's mission](https://github.com/oppia/oppia/wiki/Oppia's-Mission)
  * [Code of Conduct](https://github.com/oppia/oppia/blob/develop/.github/CODE_OF_CONDUCT.md)
  * **[[Get involved!|Home]]**
    * [Coders](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up)
    * [[Instructional designers|Teaching-with-Oppia]]
      * [[Create a Lesson!|https://github.com/oppia/oppia/wiki/Lesson-Creation-Guide]]
    * [[UX researchers|Conducting-research-with-students]]
    * [[Voice artists | Instructions-for-voice-artists]]
    * [[Designers and artists|Contributing-to-Oppia's-design]]
  * **[[Google Summer of Code 2021|Google-Summer-of-Code-2021]]**
  * **[[Season of Docs 2021|Season-of-Docs-2021]]**
  * **[[Hacktoberfest 2021|Hacktoberfest-2021]]**
  * **[[Outreachy Dec 2021 to Mar 2022|Outreachy-Dec-2021-to-Mar-2022]]**

---
**Developing Oppia**
  * [[FAQs|Frequently-Asked-Questions]]
  * [[Installing Oppia|https://github.com/oppia/oppia/wiki/Installing-Oppia]]
  * [[Tips for common IDEs|Tips-for-common-IDEs]]
  * [[Make a pull request|Make-a-pull-request]]
  * [[Common pull request workflows|Common-pull-request-workflows]]
  * [[How to get help|Get-help]]
  * [[Learning resources for developers|Learning-Resources]]
  * [[Git cheat sheet|Git-cheat-sheet]]
  * [[Codebase Overview|Overview-of-the-Oppia-codebase]]
    * [[Glossary of terms|Glossary-of-terms]]
    * [[Apache Beam Jobs|Apache-beam-jobs]]
    * [[Tips for analyzing the codebase|Analyzing-the-codebase]]
    * [[Tour of Oppia webpages|How-to-access-Oppia-webpages]]
    * [[How to find the right code to change|Find-the-right-code-to-change]]
    * [User documentation](https://oppia.github.io/)
  * [[List of current projects|https://github.com/oppia/oppia/projects]]
  * **[[Good first issues|https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22]]**
  * Coding Guidelines
    * [[Coding style guide|Coding-style-guide]]
    * [[Guidelines for creating new files|The-File-Naming-Convention-and-Directory-Structure]]
    * [[How to add a new page|Adding-new-page]]
    * [[How to write type definitions|Guide-on-defining-types]]
    * [[How to write design docs|Writing-design-docs]]
    * [[Revert and Regression Policy|Revert-and-Regression-Policy]]
    * [[Debugging|Debugging]]
      * [[If your presubmit checks fail|If-your-presubmit-check-fails]]
      * [[If CI checks fail on your PR|If-CI-checks-fail-on-your-PR.md]]
      * [[Interpreting CircleCI Results | Interpreting CircleCI Results]]
      * [[Debugging Docs|Debugging-Docs]]
      * [[Debugging end-to-end tests|Debug-end-to-end-tests]]
      * [[Debugging backend tests|Debug-backend-tests]]
      * [[Debugging frontend tests|Debug-frontend-tests]]
      * [[Debug frontend code|Debug-frontend-code]]
      * [[Debugging custom ESLint check tests|Debug-custom-ESLint-check-tests]]
      * [[Debugging custom Pylint check tests|Debug-custom-Pylint-check-tests]]
      * [[Debugging Stories|Debugging-Stories]]
    * **[[Guidelines for launching new features|Launching-new-features]]**
    * [[Feature Gating|Developing-new-features-with-feature-gating]]
    * [[Lint Checks|Lint-Checks]]
      * [[Custom Pylint checks|Custom-Pylint-checks]]
      * [[Custom ESLint checks|Custom-ESLint-checks]]
    * [[Oppia's code owners and checks to be carried out by developers|Oppia's-code-owners-and-checks-to-be-carried-out-by-developers]]
    * [[Privacy aware programming|Privacy-aware-programming]]
    * [[Backend Type Annotations|Backend-Type-Annotations]]
    * [[Bytes and string handling in Python 3|Bytes-and-string-handling-in-Python-3]]
    * [[Guidelines for Developers with Write Access to oppia/oppia|Guidelines-for-Developers-with-Write-Access-to-oppia-oppia]]
  * Testing
    * [[Automated tests|Tests]]
      * [[TypeScript tests|TypeScript-tests]]
      * [[Backend tests|Backend-tests]]
      * [[Frontend tests|Frontend-tests]]
      * [[End-to-end tests|End-to-End-Tests]]
      * [[Lighthouse Tests|Lighthouse-Tests]]
    * Manual tests
      * [[Testing for Accessibility|Testing-for-Accessibility]]
      * [[Release accessibility checklist|Release-accessibility-checklist]]
  * Release Process
    * [[Release schedule|Release-schedule-and-other-information]]
    * [[Testing jobs and other features on production|Testing-jobs-and-other-features-on-production]]
    * [[Release testing quickstart guide|Release-testing-quickstart-guide]]

---
**Developer Reference**

  * [[Oppiabot|Oppiabot]]
  * Frontend
    * [[Angular Migration | Angular-Migration]]
    * [UX guidelines](https://github.com/oppia/oppia/wiki/Oppia-UX-guidelines-&-rationales)
    * [[Writing style guide|Writing-style-guide]]
    * [[Schemas|Schemas]]
    * [[Editor pages|Editor-pages]]
  * Backend
    * [[Writing state migrations | Writing-state-migrations]]
    * [[Writing audit jobs|Writing-audit-jobs]]
    * [[Writing new one-off MapReduce jobs|Writing-new-one-off-jobs-using-map-reduce]]
    * [[Calculating statistics|Calculating-statistics]]
    * [[Storage models|Storage-models]]
    * [[Writing validators for storage models | Writing-Validators-for-storage-models]]
    * [[Coding for speed in GAE | Coding-for-speed-in-GAE]]
    * [[Adding static assets|Adding-static-assets]]
    * [[Wipeout Implementation|Wipeout-Implementation]]
    * [[Notes on NDB Datastore transactions|Notes-on-NDB-Datastore-Transactions]]
    * [[How to handle merging of change lists for exploration properties|Guide-to-handle-merging-of-change-lists-for-exploration-properties]]
    * [[Instructions for editing roles or actions|Instructions-for-editing-roles-or-actions]]
    * [[Protocol buffers|Protocol-buffers]]
  * Translations
    * [[Adding new translations|Adding-new-translations-for-i18n]]
    * [[How to develop for i18n|How-to-develop-for-i18n]]
  * [[Webpack|Webpack]]
  * [[Third-party libraries|Third-party-libraries]]
  * [[Extension frameworks|Extensions-Overview]]
    * [[Rich Text Components|Rich-Text-Editor-(RTE)-Overview]]
    * [[Interactions|Creating-Interactions]]
    * [[Rules|Creating-Rules]]
    * [[Objects|Creating-Objects]]
    * [[Dependencies|Creating-Dependencies]]
    * [[Value generators|Creating-Value-Generators]]
    * [[Actions and issues|Actions-and-issues]]
  * [[Oppia-ml Extension|Oppia-ml-Extension]]
  * [[Mobile development|Mobile-development]]
  * [[Mobile device testing|Mobile-device-testing]]
  * [[Performance testing|Performance-Testing]]
  * [[Build process|Build-process]]
  * [[Team structure|Team-Structure]]
  * Playbooks
    * [[Instructions for making PR passes|Instructions-for-making-PR-passes]]
    * [[Instructions for Reviewers|Instructions-for-Reviewers]]
    * [[Instructions for QA coordinators|Instructions-to-QA-coordinators]]
    * [[Leading Oppia Teams|Leading-Oppia-Teams]]
  * Past Events
    * Google Summer of Code: [[2020|Google-Summer-of-Code-2020]], [[2019|Google-Summer-of-Code-2019]], [[2018|Google-Summer-of-Code-2018]], [[2017|Google-Summer-of-Code-2017]], [[2016|Google-Summer-of-Code-2016]]
    * Hacktoberfest: [[2020|Hacktoberfest-2020]], [[2019|Hacktoberfest-2019]], [[2018|Hacktoberfest-2018]], [[2017|Hacktoberfest-2017]], [[2016|Hacktoberfest-2016]]
    * GHC Open Source Day: [[2019|GHC-Open-Source-Day-2019]], [[2018|GHC-Open-Source-Day]]
    * Season of Docs: [[2019|Season-of-Docs-2019]]
    * DSC-SLoP (Semester Long Project): [[2020|SLoP-2020]]
---
**Fun**
* [Events Team](https://github.com/oppia/oppia/wiki/Events-Team)
