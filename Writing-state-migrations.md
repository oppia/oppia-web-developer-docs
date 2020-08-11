If your PR changes the properties of an exploration or state (or other structure), it should also include a migration so that existing entities in the datastore can be migrated smoothly to the new structural format. The following instructions describe how to write such a migration for states of explorations or questions.

## Steps to follow while writing state migrations
1. Make the necessary changes to the State class (or its descendant classes) to reflect the post-migration state structure.
2. Make the necessary changes to the NEW_STATE_TEMPLATE in the constants.js file to reflect the post-migration state dict structure.
3. Increment the CURRENT_STATE_SCHEMA_VERSION in the feconf.py file.
4. Increment the CURRENT_EXP_SCHEMA_VERSION in the exp_domain.py file and similar changes in the question_domain.py file.
5. Start with writing _convert_states_v(old_state_version)_dict_to_v(old_state_version + 1)_dict method in exp_domain.py files under Exploration class and in question_domain.py under Question class. In exp_domain.py, update the ```Exploration._migrate_to_latest_yaml_version``` method to use your conversion function (not required for question_domain.py, this is done automatically).
6. Write a conversion function _convert_states_v(old_state_version)_dict_to_v(old_state_version + 1)_dict in draft_upgrade_services.py that makes appropriate upgrades to data that resides in ExplorationChange lists.
7. Changing existing test files:
   - Change core/tests/data/oppia-ThetitleforZIPdownloadhandlertest!-v2-gold.zip file with the updated schema.
   - Change the dict and yaml form of state in the following files wherever required:
     - core/controllers/editor_test.py
     - core/domain/exp_domain_test.py
     - core/domain/exp_services_test.py
     - core/domain/question_jobs_one_off_test.py
     - core/domain/QuestionObjectFactorySpec.js
     - core/domain/state_domain_test.py
     - core/tests/test_utils.py (Change the VERSION_(Old_version)_STATE_DICT to a new one)

8. Create a PR, if the tests fails try resolving the test issues.
9. Once your PR is finalized, file a one off job request for the ExplorationMigrationAuditJob on this [form](https://docs.google.com/forms/d/e/1FAIpQLSfvYWscAn18ok06An1oQ54h1VmBHfCX8uuuV01kIvY9WX0-Ug/viewform). The job tests a migration by making changes to the dict of existing exploration models and validating that the migration will be successful without committing the changes to the datastore.
10. Fix any issues or errors from the audit job above.
11. Get your migration PR merged.
12. Once your PR is merged, please submit a request using this [form](https://docs.google.com/forms/d/e/1FAIpQLSfvYWscAn18ok06An1oQ54h1VmBHfCX8uuuV01kIvY9WX0-Ug/viewform) to run this migration in production. Before submitting this request, please ensure that the migration has already been tested manually on your local machine, passed code review, and been merged into develop.

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