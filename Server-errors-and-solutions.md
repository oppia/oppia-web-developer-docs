This page discusses different types of server problems that have been fixed before, and it suggests ways to stop those problems from happening again. For each type of problem, it gives an example and tips on how to stop it from happening.

## Table of contents

* [Scalability issue](#scalability-issue)
* [Corner cases](#corner-cases)
* [Supporting old browsers](#supporting-old-browsers)
* [Logic errors](#logic-errors)
* [Data related issue](#data-related-issue)
* [Race conditions / Slow network issues](#race-conditions--slow-network-issues)
* [Related to migration](#related-to-migration)
* [Errors that didn't need to be logged](#errors-that-didnt-need-to-be-logged)

## Scalability issue

Issues that are related to features not scaling well on production. Example: (1) Exploration state data is too large [#12547](https://github.com/oppia/oppia/pull/12719) for some explorations and no further changes can be made to these explorations. (2) Suggestion models being fetched for review exceeds the query limit, so only an incomplete result is shown.

### Preventive action

1. __Design stage__: During design doc reviews, one should ask questions about performance and scalability when dealing with large amounts of data – "how big do you expect X to get?", "are there any limits to the size?", "what happens when it reaches this limit and is it possible to handle it?".
2. __Manual testing__: Having some functionality to generate dummy data for testing locally might help.

## Corner cases

User-facing issues where certain corner case scenarios are not considered (e.g. empty list or undefined object). Example: Deleting a hint that is active in the editor view caused console errors. Although these are not often serious, these issues can be tricky to debug due to lack of reproduction steps. The majority of server errors fall under this category. Other examples of errors include: [#7907](https://github.com/oppia/oppia/pull/7907), [#7342](https://github.com/oppia/oppia/pull/7342), [#6523](https://github.com/oppia/oppia/pull/6523) (didn't account for changes to interaction type), [#5457](https://github.com/oppia/oppia/pull/5457).

### Preventive action

1. __Static analysis / compilation stage__: Having strong typing in the frontend will help catch some of these issues.
2. __Manual testing__: Developers generally test only the "happy" paths in their feature. We should encourage them to test edge cases. Adoption of template users in testing mentioned [here](https://docs.google.com/document/d/1ktMagEKvUA6A0UmM_2CoENZPelqmjLmRjV7tWeo6w54/edit#heading=h.y3evobat23c5) should help uncover / test edge case scenarios.

## Supporting old browsers

Certain JS functionality may not be supported in older browsers. Example: String.prototype.match was used in the codebase but it lacked support in IE browsers. Fixes for these issues often involve adding a polyfill or swapping the relevant JS method with a more compatible one. Other examples of errors include: [#6909](https://github.com/oppia/oppia/pull/6909), [#6174](https://github.com/oppia/oppia/pull/6174), [#7926](https://github.com/oppia/oppia/pull/7926).

### Preventive action

1. __Static analysis / compilation stage__: Fix a JS standard that we expect all clients to support and specify a "target version" in typescript so that the code will be compiled to that version / JS standard.

## Logic errors
Logical errors in the code. Example: The "this" scope was referring to the global scope when it was supposed to refer to a local one ([#7873](https://github.com/oppia/oppia/pull/7873)). These are quite rare. Other examples of errors include: [#7872](https://github.com/oppia/oppia/issues/7872)(incorrect scope of "this"), [#7927](https://github.com/oppia/oppia/pull/7927).

### Preventive action

1. __Code review__: These issues need to be flagged during code reviews. They often happen when a developer is refactoring existing code but hasn’t fully tested their changes.

## Data-related issue

Issues that result in corrupt or missing data on the server. Issues that result in corrupt or missing data on the server. Issues like this are quite hard to debug and involve running complicated one-off jobs. Example: Certain exploration stats models were missing on the production server, which resulted in a few deferred tasks erroring often and piling up in the StackDriver logs. Fortunately, these issues are quite rare. Other examples of errors include: [#6159](https://github.com/oppia/oppia/pull/6159), [#9632](https://github.com/oppia/oppia/pull/9632), [#7440](https://github.com/oppia/oppia/pull/7440).

### Preventive action

1. __Manual testing__: When testing, perform destructive operations on entities that have related supplementary entities to check if the supplementary objects reflect the correct state of the original ones.
2. Testing with foreign / special characters (as mentioned under [Template Users](https://docs.google.com/document/d/1FYShgUHI0GM2I6eWe5B78PAQLvPxZxMFVjTivVoBrTg/edit#)).

3. __Code__: Audit jobs need to account for all instances or occurrences of the relevant item on the server. Sufficient written proof / explanation about the "thoroughness" of the audit can be added as a comment in the audit job code.

4. __Review phase__: Reviewers should be encouraged to ask questions and ensure that the audit job is thorough.

## Race conditions / Slow network issues

Some errors happen when interacting too fast with the application or when the network is too slow. Example: Clicking on the "content" tab in the translation editor before it has fully loaded (#6378[https://github.com/oppia/oppia/issues/6378]). Other examples of errors include: [#6161](https://github.com/oppia/oppia/issues/6161), [#13087](https://github.com/oppia/oppia/pull/13087), [#8181](https://github.com/oppia/oppia/issues/8181).

### Preventive action

1. __Manual testing__: For code that has a lot of "async" functionality, the authors should be encouraged to try throttling their network and/or interacting with the UI before it has completely loaded. This could be a category of "template users" mentioned [here](https://docs.google.com/document/d/1ktMagEKvUA6A0UmM_2CoENZPelqmjLmRjV7tWeo6w54/edit#heading=h.y3evobat23c5).

2. __Automated testing__: Configure certain automated tests to run under throttled network conditions. Might be worth considering the introduction of tests where the test interacts too quickly with elements on the page and expect nothing to happen (there should be no console errors).

## Related to migration

One-off errors from migration of libraries or frameworks e.g. missing imports in the module files.

### Preventive action

1. __Documentation__: Record common issues in the relevant migration page when they are identified.

## Errors that didn't need to be logged

Sometimes there may be unexpected errors thrown that do not impact user actions. Such errors can be ignored on a case-by-case basis. Example: Navigating away from a page when there are pending requests or if the request timed out caused some console errors. Other examples of errors include: [#5793](https://github.com/oppia/oppia/issues/5793), [#6500](https://github.com/oppia/oppia/issues/6500), [#8761](https://github.com/oppia/oppia/issues/8761), [#7563](https://github.com/oppia/oppia/issues/7563).

### Preventive action

1. __Code / review__: When adding logging statements or throwing errors that are not handled, always consider what scenarios these arise in and how often they will get called. If the frequency is high, discuss with the server error coordinator for the month to check if there are alternatives to achieve the desired logging behaviour (e.g. it may be possible to add logs on StackDriver interface directly in a controlled way.)