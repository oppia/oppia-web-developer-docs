If your PR changes the properties of an exploration or state (or other structure), it should also include a migration so that existing entities in the datastore can be migrated smoothly to the new structural format. The following instructions describe how to write such a migration for states of explorations or questions.

## Steps to follow while writing state migrations
1. Make the necessary changes to the State class (or its descendant classes) to reflect the post-migration state structure.
2. Increment the CURRENT_STATE_SCHEMA_VERSION in the feconf.py file.
3. Increment the CURRENT_EXP_SCHEMA_VERSION in the exp_domain.py file and similar changes in the question_domain.py file.
4. Start with writing _convert_states_v(old_state_version)_dict_to_v(old_state_version + 1)_dict method in exp_domain.py files under Exploration class and in question_domain.py under Question class. In exp_domain.py, update the ```Exploration._migrate_to_latest_yaml_version``` method to use your conversion function (not required for question_domain.py, this is done automatically).
5. Write a conversion function _convert_states_v(old_state_version)_dict_to_v(old_state_version + 1)_dict in draft_upgrade_services.py that makes appropriate upgrades to data that resides in ExplorationChange lists. Here you have to check if the changes from your conversion function can be made to the draft_change_list available. If the changes can be made make sure to update the drafts otherwise raise `InvalidDraftConversionException` which will drop the changes in the drafts. If no changes needs to be done to the draft you can simply return the draft_change_list. You will be able to see examples for this in the previously mentioned functions.
6. Changing existing test files (Note: this list is not exhaustive. These files include tests that utilize a full state dictionary, but there are tests not listed here and tests that use a subset of state- like AnswerGroup, Interaction, etc.- that may have to be updated) :
   - Change core/tests/data/oppia-ThetitleforZIPdownloadhandlertest!-v2-gold.zip file with the updated schema.
   - Change the dict and yaml form of state in the following files wherever required:
     - core/controllers/editor_test.py
     - core/domain/exp_domain_test.py
     - core/domain/exp_services_test.py
     - core/domain/question_jobs_one_off_test.py
     - core/domain/state_domain_test.py
     - core/domain/exp_jobs_one_off_test.py
     - core/domain/interaction_jobs_one_off_test.py
     - core/domain/question_services_test.py
     - core/tests/test_utils.py (Change the VERSION_(Old_version)_STATE_DICT to a new one)
     - core/domain/QuestionObjectFactorySpec.js
     - core/templates/components/question-directives/modal-templates/question-editor-modal.controller.spec.ts
     - core/templates/components/question-directives/question-player/services/question-player-state.service.spec.ts
     - core/templates/components/state-editor/state-content-editor/state-content-editor.directive.spec.ts
     - core/templates/domain/question/question-update.service.spec.ts
     - core/templates/pages/contributor-dashboard-page/modal-templates/question-suggestion-editor-modal.controller.spec.ts
     - core/templates/pages/exploration-editor-page/editor-tab/exploration-editor-tab.component.spec.ts
     - core/templates/pages/exploration-editor-page/editor-tab/services/solution-verification.service.spec.ts
     - core/templates/pages/exploration-editor-page/editor-tab/templates/modal-templates/teach-oppia-modal.controller.spec.ts
     - core/templates/pages/exploration-editor-page/editor-tab/training-panel/training-data-editor-panel-modal.controller.spec.ts
     - core/templates/pages/exploration-editor-page/editor-tab/training-panel/training-data.service.spec.ts
     - core/templates/pages/exploration-editor-page/editor-tab/training-panel/training-modal.controller.spec.ts
     - core/templates/pages/exploration-editor-page/editor-tab/training-panel/training-panel.component.spec.ts
     - core/templates/pages/exploration-editor-page/services/exploration-states.service.spec.ts
     - core/templates/pages/exploration-editor-page/services/graph-data.service.spec.ts
     - core/templates/pages/exploration-editor-page/services/parameter-metadata.service.spec.ts
     - core/templates/pages/exploration-editor-page/services/router.service.spec.ts
     - core/templates/pages/exploration-editor-page/statistics-tab/statistics-tab.component.spec.ts
     - core/templates/pages/exploration-editor-page/translation-tab/services/translation-status.service.spec.ts
     - core/templates/pages/exploration-editor-page/translation-tab/state-translation-editor/state-translation-editor.component.spec.ts
     - core/templates/pages/exploration-player-page/services/answer-classification.service.spec.ts
     - core/templates/pages/exploration-player-page/services/audio-preloader.service.spec.ts
     - core/templates/pages/exploration-player-page/services/extract-image-filenames-from-state.service.spec.ts
     - core/templates/pages/exploration-player-page/services/image-preloader.service.spec.ts
     - core/templates/pages/exploration-player-page/services/learner-answer-info.service.spec.ts
     - core/templates/pages/skill-editor-page/services/question-creation-service.spec.ts
     - core/templates/pages/skill-editor-page/skill-preview-tab/skill-preview-tab.controller.spec.ts
     - core/templates/services/question-validation.service.spec.ts
     - core/templates/services/state-interaction-stats.service.spec.ts
     - core/templates/services/state-top-answers-stats.service.spec.ts

7. Create a PR. If the tests fail, try resolving the test issues.
8. Once your PR is finalized, file a one off job request for the `AuditExplorationMigrationJob` and `MigrateExplorationJob` using this [form](https://docs.google.com/forms/d/e/1FAIpQLSfvYWscAn18ok06An1oQ54h1VmBHfCX8uuuV01kIvY9WX0-Ug/viewform). The job tests a migration by running your conversion function on the dicts of existing exploration models and validating that the migration will be successful. Make sure to mention to only run `MigrateExplorationJob` when the `AuditExplorationMigrationJob` is successfull. The audit job does not commit changes to the datastore.
9. Fix any issues or errors from the audit job above.
10. Get your migration PR merged.
11. Once your PR is merged, please submit a request using this [form](https://docs.google.com/forms/d/e/1FAIpQLSfvYWscAn18ok06An1oQ54h1VmBHfCX8uuuV01kIvY9WX0-Ug/viewform) to run this migration in production. Before submitting this request, please ensure that the migration has already been tested manually on your local machine, passed code review, and been merged into develop.

**Note:** These steps are for the migration where one is changing the schema of all existing states, depending on the changes your migration is going to make the steps will be less as you’ll have to change very fewer test files.

If you find new test files where changes needed to be required, try updating the list.

**Links to relevant PRs:**
 - Deprecate math interactions' unsupported rules and update cust arg name: [#15271](https://github.com/oppia/oppia/pull/15271)
 - Add state migration for new customization_arg catchMisspellings: [#16077](https://github.com/oppia/oppia/pull/16077). Please note that in the PR changes are done in several files and those are done according to the requirements.

## Important note:

- Make sure to add a thorough test for the migration function covering each possible case. Check the PR [#11466](https://github.com/oppia/oppia/pull/11466/files) for reference. Please note that while you are writing tests in the `exp_domain_test.py` file you should use `swap` function to swap the CURRENT_STATE_SCHEMA_VERSION to the schema version you are writing, This way in case you have several tests the next person who will write the schema tests do not have to change `states_schema_version` of every test present. We currently do not have any specefic reference to this change, the above PR does not include this as we recently decided to go ahead with this decission. You can always take reference of `swap` function in the codebase to see the usage.

## Testing state migration locally:

- Checkout develop.
- Start the server and go to the admin page.
- Load all demo exploration.
- Create a new exploration, make some changes and save them.
- Checkout the feature branch which contains state migration.
- Go to 0.0.0.0:8000 and flush existing Memcache from the Memcache tab.
- Go to admin page and assign yourself the role of `release coordinator`.
- Go to the Misc tab of release-coordinator page and flush cache.
- Run AuditExplorationMigrationJob and wait for the job to get completed. This job will not make any changes to the exploration as this is simply an audit job. We run this job before the actual migration job so that in case anything fails we do not make changes to the datastore.
- Run MigrateExplorationJob and wait for the job to get completed. This will make changes to exploration.
- Check the output of the job and post the screen-shot in your PR.
- Go to the exploration you have created lately, check whether it's working as expected.
- Check demo exploration (note demo exploration ids are 0, 1, 2, etc.)
- Add a report in your migration PR.