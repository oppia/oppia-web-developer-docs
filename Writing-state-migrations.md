If your PR changes the properties of an exploration or state (or other structure), it should also include a migration so that existing entities in the datastore can be migrated smoothly to the new structural format. The following instructions describe how to write such a migration for states of explorations or questions.

## Steps to follow while writing state migrations
1. Make the necessary changes to the State class (or its descendant classes) to reflect the post-migration state structure.
2. Increment the `CURRENT_STATE_SCHEMA_VERSION` in the _feconf.py_ file.
3. Increment the `CURRENT_EXP_SCHEMA_VERSION` in the _exp_domain.py_ file and similar changes in the _question_domain.py_ file.
4. Start with writing `_convert_states_v{old_state_version}_dict_to_v{old_state_version + 1}_dict` method in _exp_domain.py_ files under `Exploration` class and in _question_domain.py_ under `Question` class. In _exp_domain.py_, update the `Exploration._migrate_to_latest_yaml_version` method to use your conversion function (not required for _question_domain.py_, this is done automatically).
5. Write a conversion function `_convert_states_v{old_state_version}_dict_to_v{old_state_version + 1}_dict` in _draft_upgrade_services.py_ that makes appropriate upgrades to data that resides in `ExplorationChange` lists. Here you have to check if the changes that you do in your conversion function affect the `draft_change_list`, if yes, then make sure to update the drafts or raise `InvalidDraftConversionException` which will drop the changes in the drafts (this needs to be done in cases where changes to drafts would be too complicated). If no changes need to be done to drafts you can simply return the `draft_change_list`.
6. You would require to make some changes to the existing test files according to the changes you are doing in your conversion function. You have to edit the test functions present for the previous conversion functions in the `exp_domain_test.py` file to update the latest schema version. Also you have to update the schema of core/tests/data/oppia-ThetitleforZIPdownloadhandlertest!-v2-gold.zip file.

7. Create a PR. If the tests fail, try resolving the test issues.
8. Once your PR is finalized, file a one request for the `AuditExplorationMigrationJob` and `MigrateExplorationJob` using this [form](https://docs.google.com/forms/d/e/1FAIpQLSfvYWscAn18ok06An1oQ54h1VmBHfCX8uuuV01kIvY9WX0-Ug/viewform). The job tests a migration by running your conversion function on the dicts of existing exploration models and validating that the migration will be successful. Make sure to mention to only run `MigrateExplorationJob` when the `AuditExplorationMigrationJob` is successful. The audit job does not commit changes to the datastore. After successful testing you can get you PR merged.

**Note:** These steps are for the migration where one is changing the schema of all existing states, depending on the changes your migration is going to make the steps will be less as you’ll have to change very fewer test files.

If you find new test files where changes needed to be required, try updating the list.

**Links to relevant PRs:**
 - Deprecate math interactions' unsupported rules and update cust arg name: [#15271](https://github.com/oppia/oppia/pull/15271)
 - Add state migration for new customization_arg catchMisspellings: [#16077](https://github.com/oppia/oppia/pull/16077). Please note that in the PR changes are done in several files and those are done according to the requirements.

## Important note:

- Make sure to add a thorough test for the migration function covering each possible case. Check the PR [#11466](https://github.com/oppia/oppia/pull/11466/files) for reference. Please note that while you are writing tests in the `exp_domain_test.py` file you should use `swap` function to swap the CURRENT_STATE_SCHEMA_VERSION to the schema version you are writing, This way in case you have several tests the next person who will write the schema tests do not have to change `states_schema_version` of every test present. We currently do not have any specific reference to this change, the above PR does not include this as we recently decided to go ahead with this decision. You can always take reference of `swap` function in the codebase to see the usage.

## Testing state migration locally:

- Checkout develop.
- Start the server and go to the admin page.
- Load all demo exploration.
- Create a new exploration, make some changes and save them.
- Checkout the feature branch which contains state migration.
- Go to 0.0.0.0:8000 and flush existing Memcache from the Memcache tab.
- Go to the admin page and assign yourself the role of "release coordinator".
- Go to the Misc tab of /release-coordinator page and flush the cache.
- Run `AuditExplorationMigrationJob` and wait for the job to get completed. This job will not make any changes to the exploration as this is simply an audit job. We run this job before the actual migration job so that in case anything fails we do not make changes to the datastore.
- Run `MigrateExplorationJob` and wait for the job to get completed. This will make changes to exploration.
- Check the output of the job and post the screen-shot in your PR.
- Go to the exploration you have created lately, check whether it's working as expected.
- Check demo exploration (note demo exploration ids are 0, 1, 2, etc.)