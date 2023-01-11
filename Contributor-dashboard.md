# Contributor dashboard

## Overview
The [contributor dashboard page](https://www.oppia.org/contributor-dashboard) on the Oppia site allows users to submit content suggestions (currently translations and practice questions) directly to lessons. These suggestions are then reviewed, and either accepted, or sent back for revision. See the [user docs](https://oppia-user-guide.readthedocs.io/en/latest/contributor/contribute.html) for step-by-step instructions how to contribute content suggestions.

## How items for contribution are populated

### Translate text tab
Every list item on the "Translate Text" tab corresponds to a particular lesson and all of its pieces of text content. In the codebase, we refer to each of these list items as _opportunities_. The contributor dashboard automatically shows a translation opportunity for a lesson when the following are true:

1. The lesson (also called an _exploration_) corresponds to a _chapter_ in a _story_ of a published classroom subject, e.g. "Decimals" (also called a _topic_). See the [user docs](https://oppia-user-guide.readthedocs.io/en/latest/keyconcepts.html) for an overview of these terms.
1. Every piece of text content in the lesson does not yet have an accepted translation.

### Submit question tab
Every list item on the "Submit Question" tab corresponds to a particular _skill_, e.g. "Adding Decimals", in a topic. The contributor dashboard automatically shows a question opportunity for a skill when the following are true:

1. The skill is part of a published classroom topic.
1. The skill does not yet have 10 accepted practice questions.

## Additional feature behavior
- Unlike with submitting translation suggestions, users need to be allowlisted by an admin before being able to submit question suggestions. Until then, the user will not see the "Submit Question" tab on the contributor dashboard page:

  ![Alt text](https://oppia-user-guide.readthedocs.io/en/latest/_images/submit_question.png "a title")

- Users cannot review their own suggestions.
- Users must be allowlisted by an admin to be able to review translation suggestions in a particular language or to review question suggestions.
- Reviewers can edit a suggestion and accept the edited version.
- Only subjects/topics associated with a classroom, e.g. Math, are surfaced in the topic/subject selector of the "Translate Text" tab.

## Admin page
There exists a separate admin page for the contributor dashboard at /contributor-dashboard-admin. There, an admin user can:

1. allowlist a user to submit question suggestions
1. allowlist a user to review translation suggestions in a particular language
1. allowlist a user to review question suggestions
1. remove rights from a user for any of the above

See [this](https://docs.google.com/document/d/1VqNiJttq85YyR6cQkd8M9lGGkOP8OlUlkI37Xw6SovM/edit) doc for step-by-step admin instructions. This may be useful for developing locally as a coder as well.

## Local development
Some setup is usually required when developing locally for the contributor dashboard since before a user can submit a content suggestion to a lesson, a lesson needs to exist. Additionally, the requirements outlined in [How items for contribution are populated](#how-items-for-contribution-are-populated) must be satisfied. See [this](https://docs.google.com/document/d/1JYX4nvTcblaVVYAlTi7rApE0lWSBx0v_ZCCr_8WW4Wc/edit#) doc for step-by-step instructions on how to populate test data when running a local server.

## Appendix
1. [Contributor dashboard overview](https://docs.google.com/document/d/1wM9cQzq1-3nbEhZliRlpnGDXbM_HspNkY16CYnA6lWg/edit#): More in-depth developer focused overview of the backend structure of the contributor dashboard.