Oppia's translation infrastructure was originally built for explorations only. It has since been
generalised so that any user-generated content, such as skills and exploration metadata, can be
translated through the same contributor dashboard flow and shown to learners in their own
language. This page explains what "translatable" means in code, and walks through everything you
need to change to add a new entity type end to end.

## Table of contents

- [Background: the four pieces](#background-the-four-pieces)
- [Step 1: register the entity type](#step-1-register-the-entity-type)
- [Step 2: declare the content types](#step-2-declare-the-content-types)
- [Step 3: make the domain object translatable](#step-3-make-the-domain-object-translatable)
- [Step 4: give every translatable field a stable content ID](#step-4-give-every-translatable-field-a-stable-content-id)
- [Step 5: hook up the opportunity lifecycle](#step-5-hook-up-the-opportunity-lifecycle)
- [Step 6: always recompute counts, never increment them](#step-6-always-recompute-counts-never-increment-them)
- [Step 7: support suggestions](#step-7-support-suggestions)
- [Step 8: serve translations to learners](#step-8-serve-translations-to-learners)
- [Step 9: expose it in the contributor dashboard](#step-9-expose-it-in-the-contributor-dashboard)
  - [Grouping the items in the translation modal](#grouping-the-items-in-the-translation-modal)
- [Step 10: backfill existing entities](#step-10-backfill-existing-entities)
- [Step 11: make translated content searchable](#step-11-make-translated-content-searchable)
- [Step 12: roll out behind a feature flag](#step-12-roll-out-behind-a-feature-flag)
- [Step 13: tests](#step-13-tests)
- [Checklist](#checklist)
- [Gotchas](#gotchas)

## Background: the four pieces

Translation in Oppia is built from four fairly independent parts. It helps to keep them separate
in your head, because a new entity type has to be registered with each one.

**Translatable content.** A domain object declares which of its fields can be translated by
extending `translation_domain.BaseTranslatableObject` and implementing
`get_translatable_contents_collection()`. Every translatable field is identified by a stable
string called a content ID.

**Stored translations.** Accepted translations live in `EntityTranslationsModel`, keyed by entity
type, entity ID, entity version, and language code. Nothing in that model is specific to
explorations, so it works for a new entity type as soon as the type is registered.

**Opportunities.** `TranslationOpportunityModel` is what makes an entity appear in the
contributor dashboard as something available to translate. Its ID is always
`{entity_type}.{entity_id}`, and it holds the topics the entity belongs to, how many pieces of
translatable content it has, and how many are translated per language.

**Suggestions.** A contributor's translation is a `translate_content` suggestion carrying a
`target_type` and `target_id`. Accepting one writes to `EntityTranslationsModel` and updates the
opportunity's counts.

## Step 1: register the entity type

Everything starts in `core/feconf.py`.

If your entity does not already have one, add an `ENTITY_TYPE_<NAME>` constant. Then add the type
to:

- `TranslatableEntityType`, the enum used by the translation services and storage layer.
- `TRANSLATABLE_ENTITY_TYPES`, the list validated in `TranslationOpportunityModel._pre_put_hook`.
  If you skip this, saving an opportunity raises `Invalid entity_type`.
- `SUGGESTION_TARGET_TYPE_CHOICES`, if contributors will submit translation suggestions for the
  entity. Suggestion validation rejects target types that are not listed.

## Step 2: declare the content types

Add an entry to `translation_domain.ContentType` for each kind of field you are making
translatable. Skills added `SKILL_DESCRIPTION`, `SKILL_EXPLANATION` and `MISCONCEPTION_FEEDBACK`.
Exploration metadata added `METADATA`.

Use a specific content type rather than reusing `CONTENT`. The content type is what tells the UI
and the stats layer what the translator is actually looking at.

## Step 3: make the domain object translatable

Have your domain class extend `translation_domain.BaseTranslatableObject` and implement
`get_translatable_contents_collection()`. `Skill` in `core/domain/skill_domain.py` is the
clearest reference implementation:

```python
def get_translatable_contents_collection(
    self,
    **kwargs: Any,
) -> translation_domain.TranslatableContentsCollection:
    translatable_contents_collection = (
        translation_domain.TranslatableContentsCollection()
    )

    translatable_contents_collection.add_translatable_field(
        feconf.SKILL_DESCRIPTION_CONTENT_ID,
        translation_domain.ContentType.SKILL_DESCRIPTION,
        translation_domain.TranslatableContentFormat.UNICODE_STRING,
        self.description,
    )

    translatable_contents_collection.add_translatable_field(
        self.skill_contents.explanation.content_id,
        translation_domain.ContentType.SKILL_EXPLANATION,
        translation_domain.TranslatableContentFormat.HTML,
        self.skill_contents.explanation.html,
    )

    for misconception in self.misconceptions:
        translatable_contents_collection.add_translatable_field(
            f'misconception_{misconception.id}_feedback',
            translation_domain.ContentType.MISCONCEPTION_FEEDBACK,
            translation_domain.TranslatableContentFormat.HTML,
            misconception.feedback,
        )

    return translatable_contents_collection
```

Two things to get right.

Pick the correct `TranslatableContentFormat`. Use `UNICODE_STRING` for plain text such as a
title or description, and `HTML` for rich text. Getting this wrong gives the translator the
wrong editor.

If your object contains child objects that are themselves translatable, use
`add_fields_from_translatable_object()` rather than listing their fields by hand. `Exploration`
does this to pull in every state.

Some entities expose content that should only be translated behind a flag. Exploration metadata
is gated this way, which is why `Exploration.get_translatable_contents_collection()` takes an
`override_metadata_feature_flag` keyword. Follow that pattern if your content is being rolled
out gradually.

## Step 4: give every translatable field a stable content ID

This is the part that causes the most trouble, because fields that were never translated often
have no ID at all.

Rich text fields usually already carry one, because `SubtitledHtml` has a `content_id`. Plain
string fields normally do not, and you have two options:

- Use a constant when there is exactly one such field on the object. A skill has one
  description, so it uses `feconf.SKILL_DESCRIPTION_CONTENT_ID`.
- Derive a synthetic ID when the field belongs to a repeated child. Misconception feedback uses
  `f'misconception_{misconception.id}_feedback'`.

Content IDs must be unique within the entity and stable across edits. If an ID changes, existing
translations for it are orphaned, because `EntityTranslationsModel` looks them up by ID.

## Step 5: hook up the opportunity lifecycle

An entity nobody can find is not translatable in practice. Opportunities are managed in
`core/domain/opportunity_services.py`. The functions you will use are
`create_translation_opportunity`, `update_translation_opportunity_with_accepted_suggestion`,
`remove_topic_from_translation_opportunities` and `delete_translation_opportunities`.

Work out every event that changes whether your entity should be translatable, and call the right
function from the service that owns that event. For skills this is driven from
`topic_services.py` and `skill_services.py`, because a skill becomes translatable when it is
assigned to a topic.

The rule to apply separates three different events, and the difference between them matters more
than it first appears:

- **The entity becomes reachable.** Create the opportunity. For a skill this is assignment to a
  topic, published or unpublished. Do not require the topic to be published. Curriculum work
  happens in draft topics, and waiting for publication would leave that content untranslatable
  for as long as it is being written.
- **The entity stops being reachable, but still exists.** Keep the opportunity and update what
  changed. Unassigning a skill from a topic calls
  `remove_topic_from_translation_opportunities`, which removes that topic ID and leaves the model
  in place with an empty `topic_ids`. Do not delete anything, and do not touch pending
  suggestions. A translator's accepted work and a reviewer's queue both survive, which is the
  point: a temporary curriculum change should not throw away contributor effort.
- **The entity is deleted.** Now delete the opportunity with `delete_translation_opportunities`
  and auto reject every pending translation suggestion, because the target no longer exists.
  `skill_services.delete_skill` does both.

An earlier draft of this design deleted the opportunity and rejected suggestions as soon as a
skill left its last topic, and auto rejected on topic unpublication too. That was changed
deliberately during review. If you are adding a new entity type, follow the three-way split
above rather than tying deletion to reachability.

One consequence worth knowing when you test this. The dashboard query only filters on
`topic_ids` when a specific topic is selected, so an entity whose `topic_ids` is empty still
appears under the "All" topic filter and disappears under any named one.

## Step 6: always recompute counts, never increment them

This one is worth its own step because it caused a bug that went unnoticed for over two years
(issue #21878).

`translation_counts` and `content_count` must always be recomputed from the source of truth,
which is `EntityTranslationsModel` and `get_translatable_contents_collection()`. Never increment
or decrement a stored count in place. Incrementing drifts under concurrent acceptances and, once
wrong, stays wrong forever. Recomputing gives eventual consistency and makes it impossible for a
count to exceed the real number of translations.

The same rule applies in the backfill job in step 10.

## Step 7: support suggestions

`SuggestionTranslateContent` in `core/domain/suggestion_registry.py` carries a `target_type`, so
much of this is already generic. What you need to make work:

- `pre_accept_validate()` resolves the target entity, then validates the content ID against the
  entity's translatable contents. For explorations it also validates the state name. Validate
  both independently, since a valid state name does not imply a valid content ID.
- `accept()` calls `translation_services.add_new_translation()` with the right
  `TranslatableEntityType`, entity version, language code, and content ID.
- `/suggestionhandler` (POST) accepts your `target_type` for `translate_content`.
- `/suggestionactionhandler/<suggestion_type>/<suggestion_id>` (PUT) dispatches accept and reject
  for your entity and updates contribution and review stats.

Contribution and review stats are recorded per topic, so resolve the topic ID from the entity's
translation opportunity rather than defaulting it. Stats should be updated for every entity type,
not only explorations.

If a field has a constraint that only makes sense for that field, validate it in
`SuggestionTranslateContent.validate()` keyed on the content ID, and mirror the check in the
translation modal so the contributor sees it before submitting rather than after. An exploration
title is capped at 36 characters this way, because that is what a lesson tile can display.
Backend validation alone would reject the work after the translator had already done it.

Images inside a translation are copied at submission time, based on the suggestion's own
`target_type` and `image_context`, so this generally needs no per-entity work.

## Step 8: serve translations to learners

Give the learner-facing handler for your entity an optional `language_code` query parameter,
validated with the existing `is_supported_audio_language_code` schema validator rather than a
hand-written list of codes. When it is present and not English, look up `EntityTranslationsModel`
and substitute translated values into the response. Always fall back to English for anything
untranslated, and never fail a learner request because a translation is missing.

Use `translation_services.get_up_to_date_translation` to read a value. It returns the translation
only when one exists and is not flagged `needs_update`, which is what keeps a learner from seeing
a translation that is stale relative to an edited English source. Do not write your own version
of that check; three separate copies of it appeared across different pull requests before it was
made a shared helper.

If the response is cached on the frontend, key the cache by language. A cache keyed only by
entity ID will serve the previous language's content after the learner switches.

Handlers already following this pattern:

- `/libraryindexhandler` and `/explorationsummarieshandler/data` for exploration title, objective
  and tags.
- `/concept_card_handler/<selected_skill_ids>` for skill description and explanation.
- `/entity_translations_handler/<entity_type>/<entity_id>/<version>/<language_code>` for fetching
  a specific entity's translations directly.

A useful property of this design is that most learner-facing components need no changes, because
they already render whatever JSON the handler returns. Usually the only frontend change is
passing the learner's language code through.

## Step 9: expose it in the contributor dashboard

The dashboard talks to the v2 endpoints, which all take an `entity_type` parameter:

- `/opportunitieshandlerv2` for available opportunities, taking `entity_type` as a query
  parameter.
- `/getreviewableopportunitieshandlerv2` for opportunities the user can review, also taking
  `entity_type`.
- `/gettranslatablecontentshandlerv2` for the translatable fields of one entity, taking
  `entity_type` and `entity_id`.

The suggestion lists are not versioned. They take the entity type as a URL path argument instead:
`/getreviewablesuggestions/<target_type>/<suggestion_type>` and
`/getsubmittedsuggestions/<target_type>/<suggestion_type>`. Both accept the sentinel value `all`
as the target type, which returns suggestions of every entity type in one response, so each
suggestion has to be rendered from its own target type rather than from the request's.

On the frontend, add your type to the entity type selector on the Translate and Review tabs, and
make sure the opportunity card renders something meaningful. Labels such as story and chapter
titles do not apply to every entity type, so a skill shows its description instead. Take an
opened opportunity's entity type from the opportunity itself rather than from the dashboard
filter, because the filter can be set to "all" and cannot tell you which card was clicked.

If your entity can be pinned, `PinnedOpportunityModel` needs an `entity_type` so pinned skills do
not collide with pinned explorations. Be aware that the write path and the read path are separate
work: the v2 opportunity path does not currently look a saved pin back up, so pinning has to be
implemented on both sides for it to survive a page reload.

### Grouping the items in the translation modal

`/gettranslatablecontentshandlerv2` returns each translatable item with a `grouping_key`, which
the modal uses to keep related items together as the contributor pages through them. An
exploration sets it to the state name, so a lesson is translated card by card.

There is no requirement to supply one. Items with no grouping key fall into a single default
group, labelled by `DEFAULT_SUGGESTION_STATE_NAME` in `assets/constants.ts`. Skills use this, and
so does exploration metadata, since metadata belongs to no state.

Set a grouping key only if your entity has a real internal structure that a translator would
recognise. Inventing one produces group names that mean nothing to the person translating.

## Step 10: backfill existing entities

Opportunity models are only written when the lifecycle hooks fire, so entities that already exist
will not appear until something touches them. Write an Apache Beam job under
`core/jobs/batch_jobs/` and register it in `core/jobs/registry.py`.

The job must compute `content_count` from the entity's `get_translatable_contents_collection()`
and `translation_counts` from `EntityTranslationsModel`. Do not copy counts across from an older
model, because the old values predate the new completion criterion and are the exact source of
the drift described in step 6.

Beam jobs that write production data need a testing doc and a successful run on the backup server
before they can be merged, so plan for that lead time. See [[Apache Beam Jobs|Apache-Beam-Jobs]].

## Step 11: make translated content searchable

If your entity has fields that feed the Community Library search index, translations should be
searchable too. This takes three changes, and missing any one of them leaves the feature silently
half working.

**Index the translated values.** In `core/domain/search_services.py`, add a field to the search
document for each translatable field, and fill it by reading every `EntityTranslation` for the
entity and collecting the up to date values. Explorations use `translated_titles`,
`translated_objectives` and `translated_tags`. Skip any translation flagged `needs_update`, using
`translation_services.get_up_to_date_translation`, so a translation that is stale relative to the
edited English source is never returned.

**Add the new fields to the query.** This is the step that is easy to miss. Indexing a field does
not make it searchable: the query in `core/platform/search/elastic_search_services.py` lists the
fields it matches against, and anything absent from that list is never consulted no matter what
is in the document. Give the translated fields the same boosts as their English counterparts so
that English ranking does not change.

The cost of forgetting this is not hypothetical. `tags` had been indexed for years and was never
in the query list, so no lesson was ever findable by its tags in any language until that was
noticed while adding the translated fields.

**Reindex when a translation is accepted.** Entities are normally reindexed when they are
published or edited, which never happens on translation acceptance. Add a hook in
`suggestion_services.accept_suggestion` so a newly accepted translation becomes searchable
immediately. Existing translations accepted before your change are not covered by that hook, so
they need a backfill job of their own.

## Step 12: roll out behind a feature flag

New endpoints are added alongside the old ones using a `v2` suffix, and the frontend chooses
between them based on a feature flag, currently
`ENABLE_TRANSLATION_OPPORTUNITIES_WITH_NEW_OPP_MODELS`. This keeps the old path available for
rollback.

Once the flag has been enabled in production and the new path is stable, a cleanup change removes
the old endpoints and models, removes the flag checks, and renames the `v2` endpoints to drop the
suffix so they do not confuse future developers. Plan for that cleanup rather than leaving both
paths in place indefinitely.

## Step 13: tests

Oppia requires 100 percent line coverage on new and changed code, backend and frontend. Cover:

- The domain method, including every content type it can emit.
- Each lifecycle hook, especially the removal paths, since those are the easiest to forget.
- Suggestion creation, validation failures, acceptance, and rejection.
- The learner-facing handler both with and without a translation present.
- The Beam job, including entities that already have an opportunity.

While developing:

```
python -m scripts.run_backend_tests --test_target <dotted.module.path>
```

Note that CI combines coverage across five shards, so a single module run locally can report
lines as uncovered that another module actually covers.

## Checklist

- [ ] `ENTITY_TYPE_<NAME>` exists in `feconf`
- [ ] Added to `TranslatableEntityType` and `TRANSLATABLE_ENTITY_TYPES`
- [ ] Added to `SUGGESTION_TARGET_TYPE_CHOICES` if contributors translate it
- [ ] New `ContentType` values added
- [ ] Domain object extends `BaseTranslatableObject` and implements
      `get_translatable_contents_collection()`
- [ ] Every translatable field has a stable, unique content ID
- [ ] Opportunity created when the entity becomes reachable, kept when it stops being reachable,
      deleted only when the entity itself is deleted
- [ ] Pending suggestions auto rejected only on entity deletion
- [ ] Counts recomputed from source of truth, never incremented
- [ ] Suggestion validation checks state name and content ID independently
- [ ] Accept path writes to `EntityTranslationsModel` and updates stats with the right topic
- [ ] Learner-facing handler serves translations with an English fallback
- [ ] Entity type selectable in the contributor dashboard, and the card renders sensibly
- [ ] `PinnedOpportunityModel` handles the entity type, if pinning applies
- [ ] Backfill Beam job written, registered, with a testing doc and a backup server run
- [ ] Translated values indexed for search, added to the query field list, and reindexed on
      acceptance, if the fields are searchable
- [ ] Rolled out behind the feature flag, with the cleanup planned
- [ ] Tests at 100 percent coverage, and lint, mypy and black are clean

## Gotchas

**Not every domain object is translatable.** Only `Exploration` and `Skill` extend
`BaseTranslatableObject` today. `Story` and `Topic` do not, so any code calling
`get_translatable_contents_collection()` on a value that could be one of those needs an
`isinstance` guard. mypy will insist on it.

**Opportunity IDs are structured.** `TranslationOpportunityModel` IDs are always
`{entity_type}.{entity_id}`, produced by `_generate_id` and validated in `_pre_put_hook`. Do not
write fallback code that infers the entity type some other way, because it is unreachable.

**Fetchers cannot take a variable `strict`.** Functions such as `get_skill_by_id` use `@overload`
declarations keyed on `Literal[True]` and `Literal[False]`, so a plain `bool` cannot be forwarded
through a wrapper. Prefer letting the fetcher raise rather than adding a `strict` parameter for a
single call site.

**A valid state name does not imply a valid content ID.** They are independent. Checking only the
state name lets invalid content IDs through validation and into the accept path.

**Entity versions matter.** Translations are stored against a specific entity version. When you
read translations back, use the version consistently with how they were written, or the lookup
silently returns nothing.
