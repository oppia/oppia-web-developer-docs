If your PR changes the properties of an exploration or state (or other structure), it should also include a migration so that existing entities in the datastore can be migrated smoothly to the new structural format. The following instructions describe how to write such a migration for states of explorations or questions.

## Steps to follow while writing state migrations
1. Make the necessary changes to the State class (or its descendant classes) to reflect the post-migration state structure.
2. Make the necessary changes to the NEW_STATE_TEMPLATE in the constants.js file to reflect the post-migration state dict structure.
3. Increment the CURRENT_STATE_SCHEMA_VERSION in the feconf.py file.
4. Increment the CURRENT_EXP_SCHEMA_VERSION in the exp_domain.py file and similar changes in the question_domain.py file.
5. Start with writing _convert_states_v(old_state_version)_dict_to_v(old_state_version + 1)_dict method in exp_domain.py files under Exploration class and in question_domain.py under Question class.
6. Changing existing test files:
   - Change core/tests/data/oppia-ThetitleforZIPdownloadhandlertest!-v2-gold.zip file with the updated schema.
   - Change the dict and yaml form of state in the following files wherever required:
     - core/controllers/editor_test.py
     - core/domain/exp_domain_test.py
     - core/domain/exp_services_test.py
     - core/domain/question_jobs_one_off_test.py
     - core/domain/QuestionObjectFactorySpec.js
     - core/domain/state_domain_test.py
     - core/tests/test_utils.py (Change the VERSION_(Old_version)_STATE_DICT to a new one)

7. Create a PR, if the tests fails try resolving the test issues.
8. Once your PR is finalized, create a new one-off job (ExplorationMigrationValidationJob) which will make changes to the dict of existing exploration model and validates that the migration will be successful.
9. Once the one-off job PR gets merged and the job result is successful, try updating your migration PR and deleting the one-off job (as this will not be required anymore).
10. Get your migration PR merged.
11. Once your PR is merged, please submit a request using this [form](https://docs.google.com/forms/d/e/1FAIpQLSeI_hrDEM_hsddJIw77HLC_C3pemB5zBXuPpuEJS6FSXQU0iA/viewform?usp=sf_link) to run this migration in production. Before submitting this request, please ensure that the migration has already been tested manually on your local machine, passed code review, and been merged into develop.

**Note:** These steps are for the migration where one is changing the schema of all existing states, depending on the changes your migration is going to make the steps will be less as you’ll have to change very fewer test files.

If you find new test files where changes needed to be required, try updating the list.

**Links to relevant PRs:**
 - Migration related to changing state schema for all possible states: [#6249](https://github.com/oppia/oppia/pull/6249)

 - Migration related to changing specific interaction schema: [#6177](https://github.com/oppia/oppia/pull/6177)
 - One-off job related to migration: [#6249](https://github.com/oppia/oppia/pull/6249)

## Testing state migration locally:

- Checkout develop.
- Start the server and go to the admin page.
- Load all demo exploration.
- Create a new exploration, make some changes and save them.
- Checkout the feature branch which contains state migration.
- Go to 0.0.0.0:8000 and flush existing Memcache from the Memcache tab.
- Go to the Jobs tab of admin page.
- Run ExplorationMigrationJobManager and wait for the job to get completed.
- Check the output of the job and post the screen-shot in your PR.
- Go to the exploration you have created lately, check whether it's working as expected.
- Check demo exploration (note demo exploration ids are 0, 1, 2, etc.)
- Add a report in your migration PR. 