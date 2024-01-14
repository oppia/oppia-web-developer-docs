This document talks about different types of server problems that have been fixed before, and it suggests ways to stop those problems from happening again. The types of problems include issues with data, problems when lots of people are using the server, situations that don't happen very often, making sure the server works with old internet browsers, mistakes in the way the server thinks, problems when the internet is slow, and errors that don't need to be written down. For each type of problem, it gives an example and tips on how to stop it from happening.

# Categories

Detailed list can be found here.[https://docs.google.com/spreadsheets/d/1sgY2IOUP_RQf47uMYFbKjUVc3U3LnXeAAGFJ1xzjkyI/edit#gid=0]
Data related issue[https://docs.google.com/document/d/1hIQIaFNVvyNiZBcCx0X7-_2lc0r1yvjxGfn4GJMjwEs/edit#heading=h.8l65z4v3inu0]
Scalability issue[https://docs.google.com/document/d/1hIQIaFNVvyNiZBcCx0X7-_2lc0r1yvjxGfn4GJMjwEs/edit#heading=h.nw7ebo5gw1ke]
Corner cases[https://docs.google.com/document/d/1hIQIaFNVvyNiZBcCx0X7-_2lc0r1yvjxGfn4GJMjwEs/edit#heading=h.34kkz7w5mzfp]
Supporting old browsers[https://docs.google.com/document/d/1hIQIaFNVvyNiZBcCx0X7-_2lc0r1yvjxGfn4GJMjwEs/edit#heading=h.90m8kcnx5gyh]
Logic errors[https://docs.google.com/document/d/1hIQIaFNVvyNiZBcCx0X7-_2lc0r1yvjxGfn4GJMjwEs/edit#heading=h.4nsx9mmay1nn]
Race conditions / issues on slow networks[https://docs.google.com/document/d/1hIQIaFNVvyNiZBcCx0X7-_2lc0r1yvjxGfn4GJMjwEs/edit#heading=h.k0ge8xbqh3ch]
Related to an upgrade[https://docs.google.com/document/d/1hIQIaFNVvyNiZBcCx0X7-_2lc0r1yvjxGfn4GJMjwEs/edit#heading=h.8crhff8u87tk]
Errors that didn't need to be logged[https://docs.google.com/document/d/1hIQIaFNVvyNiZBcCx0X7-_2lc0r1yvjxGfn4GJMjwEs/edit#heading=h.u62qotr8my7p]

## Scalability Issue
Issues that are related to features not scaling well on production. Example: (1) Exploration state data is too large for some explorations and no further changes can be made to these explorations. (2) Suggestion models being fetched for review exceeds the query limit, so only an incomplete result is shown.
### Preventive action
* Design stage: During design doc reviews, one should ask questions about performance and scalability when dealing with large amounts of data – “how big do you expect X to get?”, “are there any limits to the size?”, “what happens when it reaches this limit and is it possible to handle it?”
* Manual testing: Having a functionality to generate dummy data for testing locally might help.

## Corner Cases
User-facing issues where certain corner case scenarios are not considered (empty list, undefined object etc.) Example: Deleting a hint that is active in the editor view caused console errors. Although these are not often serious, these issues can be tricky to debug due to lack of reproduction steps. The majority of server errors fall under this category.
### Preventive action
* Static analysis / compilation stage: Strongly typed frontend will help catch some of these issues.
* Manual testing: Developers generally test only the “happy” paths in their feature. We should encourage them to test edge cases. Adoption of template users in testing mentioned here should help uncover / test edge case scenarios.

## Supporting old browsers
Certain JS functionality may not be supported in older browsers. Example: String.prototype.match was used in the codebase but it lacked support in IE browsers. Fixes for these issues often involve adding a polyfill or swapping the relevant JS method with a more compatible one.
### Preventive action
* Static analysis / compilation stage: Fix a JS standard that we expect all clients to support and specify a “target version” in typescript so that the code will be compiled to that version / JS standard.

## Logic errors
Logical errors in the code. Example: “this” scope was referring to the global scope when it was supposed to refer to a local one (#7873). These are quite rare.
### Preventive action
* Code review: These issues need to be flagged during code reviews. Often happens when the developer is refactoring existing code but hasn’t fully tested their changes.

## Data-related Issue
Issues that resulted in corrupt or missing data on the server. Issues like this are quite hard to debug and involve complicated one-off jobs to be run. Example: Certain exploration stats models were missing on the production server, this resulted in few deferred tasks erroring often and piling up in the stackdriver logs. Fortunately, these issues are quite rare.
### Preventive action
* Manual testing:
When testing, perform destructive operations on entities that have related supplementary entities to check if the supplementary objects reflect the correct state of the original ones.
Testing with foreign / special characters (as mentioned under Template Users).

* Code: Audit jobs need to account for all instances or occurrences of the relevant item on the server. Sufficient written proof / explanation about the “thoroughness” of the audit can be added as a comment in the audit job code.

* Review phase: Reviewers should be encouraged to ask questions and ensure that the audit job is thorough.

## Race Conditions / Slow Network Issues
Some errors happen when interacting too fast with the application or when the network is too slow. Example: Clicking on the “content” tab in the translation editor before it has fully loaded (#6378).
### Preventive action
* Manual testing: For code that has a lot of “async” functionality, the authors should be encouraged to try throttling their network and/or interacting with the UI before it has completely loaded. This could be a category of “template users” mentioned here.
* Automated testing: Configure certain automated tests to run under throttled network conditions. Might be worth considering the introduction of tests where the test interacts too quickly with elements on the page and expect nothing to happen (there should be no console errors).

## Related to a migration
One-off errors from migration of libraries or frameworks e.g. missing imports in the module files.
### Preventive action
* Documentation: Record common issues in the relevant migration page when they are identified.

## Errors that didn't need to be logged
Sometimes there may be unexpected errors thrown that do not impact user actions. Such errors can be ignored on a case-by-case basis. Example: Navigating away from a page when there are pending requests or if the request timed out caused some console errors.
### Preventive action

* Code / review: When adding logging statements or throwing errors that are not handled, always consider what scenarios and how often they will get called. If the frequency is high, discuss with the server error coordinator for the month to check if there are alternatives to achieve the same (e.g. it may be possible to add logs on stackdriver interface directly in a controlled way.)