## Table of contents

* [Introduction](#introduction)
* [Actions](#actions)
* [Issues](#issues)
* [Using actions and issues](#using-actions-and-issues)

## Introduction

As a user plays through an exploration, we want to track their progress to identify any problems. If we do find problems with the exploration, we can raise those to the exploration creator. For example, if a user gets stuck in a cycle of cards or submits many incorrect answers to an interaction, the exploration could probably be improved.

We store the steps a user takes through an exploration as _actions_, and we create _issues_ to keep track of the problems that these actions indicate. Both actions and issues are defined as [[schemas|Schemas]].

## Actions

There are three actions defined at [`extensions/actions/`](https://github.com/oppia/oppia/tree/develop/extensions/actions):

* `ExplorationStart`: This action is recorded when a learner starts an exploration. It stores the name of the state (i.e. card) they start at.

* `AnswerSubmit`: This action is recorded when a learner submits a response to an interaction. It stores the ID of the interaction, the name of the state with the interaction, the answer that the learner submitted, the exploration's feedback for that answer, the next state they transition to, and how long the learner spent in the state. Note that the interaction ID is just its name, for example `ItemSelectionInput`.

* `ExplorationQuit`: This action is recorded when a learner leaves an exploration. It stores the name of the state at which the learner quit and how long the user spent in the last state they visited.

These actions are recorded using the functions provided by the [stats reporting service](https://github.com/oppia/oppia/tree/develop/core/templates/pages/exploration-player-page/services/stats-reporting.service.ts). For example, when a learner transitions into a terminal state (a card that ends the exploration), the [conversation skin directive](https://github.com/oppia/oppia/blob/develop/core/templates/pages/exploration-player-page/learner-experience/conversation-skin.component.ts) calls `StatsReportingService.recordExplorationCompleted()`.

When a learner's journey through an exploration goes smoothly, we don't store the actions anywhere; however, when we detect a problem in a learner's journey, then we create an issue that stores the associated actions. Note that at no point during this process do we store or process any information about the learner's identity.

## Issues

We define three different issues at [`extensions/issues/`](https://github.com/oppia/oppia/tree/develop/extensions/issues):

* `MultipleIncorrectSubmissions`: This issue is recorded when a user submits 3 or more incorrect answers to an interaction. It stores the name of the state where the user provided incorrect answers and the number of incorrect answers that they submitted.

  The logic determining whether to file this issue lives in the `MultipleIncorrectAnswersTracker` class in the [playthrough service](https://github.com/oppia/oppia/tree/develop/core/templates/services/playthrough.service.ts).

* `CyclicStateTransitions`: This issue is recorded when a user repeats a cycle of states 3 times in a row. Note that our cycle detection isn't particularly clever. As soon as we detect a cycle, we check whether it's equal to the most recent cycle we detected earlier. If it matches, we increment a counter. Otherwise, we reset the counter to 1. Here are some examples:

  * `A -> B -> A -> B -> A -> B -> A`: An issue would be filed because the cycle `A -> B -> A` happened 3 times.
  * `A -> B -> A -> C -> A -> B -> A -> C -> A -> B -> A -> C -> A`: An issue would _not_ be filed even though the cycle `A -> B -> A -> C -> A` repeats 3 times. The reason is that we will only detect the smaller `A -> B -> A` and `A -> C -> A` cycles, which alternate. Since they alternate, we keep resetting our counter to 1 and so never reach 3 consecutive cycles.

  The logic behind this cycle detection lives in the `CyclicStateTransitionsTracker` class in the [playthrough service](https://github.com/oppia/oppia/tree/develop/core/templates/services/playthrough.service.ts).

  This issue stores a list of the state names that make up the cycle.

* `EarlyQuit`: This issue is recorded whenever a user quits an exploration after fewer than 300 seconds. It records the name of the state where the user quit and the time they spent on the exploration.

  The logic behind this cycle detection lives in the `EarlyQuitTracker` class in the [playthrough service](https://github.com/oppia/oppia/tree/develop/core/templates/services/playthrough.service.ts).

## Using actions and issues

Right now, neither issues nor their associated actions are surfaced to exploration creators. They used to be available through the improvements tab of the exploration editor, but that tab has been removed. We are currently working on building a new improvements tab.
