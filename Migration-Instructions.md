This page contains instructions for migrating a production instance of Oppia from one release to the next. Please note that a special migration occurred for version 2.5.0 and it's *highly recommended* that you bring your instance up to a fully upgraded version of 2.4.2, then perform the 2.4.2 → 2.5.0 migration, then continue with any other migrations after that, if needed.

### Migrating v2.4.2 → v.2.5.0 ###

Version 2.5.0 of Oppia included a migration of all answers to a new storage model. #3294 provides more context for this migration, and the steps for performing this migration are as follows:

1. Go into the admin panel after deploying v2.5.0 of the application
2. Stop all continuous computation jobs and wait for them to stop
2. Run ``ClearMigratedAnswersJob`` and ``ClearLargeAnswerBucketsJob``
3. Run the ``PurgeInconsistentAnswersJob`` and wait for it to complete
4. Run the ``SplitLargeAnswerBucketsJob``
5. Run the ``AnswersAudit`` job
6. Wait for both jobs to complete
7. Run the ``AnswerMigrationJob`` and wait for it to complete
8. Check the output of the ``AnswerMigrationJob`` for any errors.  If there are any errors follow these sub-steps:
  a. Run ``AnswerMigrationCleanupJob`` and wait for it to complete
  b. Re-run the ``AnswerMigrationJob`` and wait for it to complete
  c. Check the output of the ``AnswerMigrationJob`` for any errors. If the errors are the same as the previous time the ``AnswerMigrationJob`` was run, stop the process and investigate.  Otherwise, repeat steps (a) through (c) until the migration job no longer reports errors.
9. Start the ``AnswersAudit2`` job
10. Start the ``RuleTypeBreakdownAudit`` job
11. Wait for both to complete.  Check the output of ``RuleTypeBreakdownAudit`` to verify that all answer rule types were migrated (there should be no reports of specific exploration failing to migrate all of their rule types)
12. Optionally compare the output from ``AnswersAudit`` and ``AnswersAudit2``.  Other than some minor differences between the old and new storage models, the aggregate rule type counts should be equal for both jobs
13. Start the ``RefreshInteractionRegistryJob`` and wait for it to complete
14. Restart continuous computation jobs and start ``InteractionAnswerSummariesAggregator``
15. After the aggregator has finished running a few times, look through the answer stats for some large explorations and verify they look similar to before
16. Start the ``CleanupLargeBucketLabelsFromNewAnswersJob`` and wait for it to complete

If you are migrating a site with regular user traffic, consider enabling maintenance mode in feconf by setting the [ENABLE_MAINTENANCE_MODE](https://github.com/oppia/oppia/blob/release-2.5.0/feconf.py#L264) flag to ``True``. When maintenance mode is enabled, only the admin panel is accessible to all users, and only superadmins can access the rest of the site (you may need to refresh other pages a few times before they are accessible). Don't forget to set the flag back to ``False`` and push a new binary after the migration is complete.

If you are migrating a large number of answers, consider increasing the number of shards your mapreduce jobs use by editing ``third_party/gae-mapreduce-1.9.17.0/mapreduce/parameters.py`` and changing the ``SHARD_COUNT`` property to a value higher (we used 64 shards for steps 1-8 and 32 shards thereafter due to limitations in the app engine mapreduce pipeline). It's also highly recommended to increase your instance class to F4 or F4_1G when running the migration, as a lot of memory may be consumed. You can also upgrade your default queue to have a ``bucket_size`` of 100 and a rate of 500/s just for the migration job and follow-up audit jobs.

Please note that the above information is provided for reference, and we hope that it is helpful. However, if you perform this migration, you do so at your own risk, and we cannot guarantee any assistance if you run into problems. You might also wish to consider running through the migration beforehand on a test server.

### Migrating v2.0.0 → v2.0.1, or v2.0.0.rc.4 → v2.0.0, or v2.0.0.rc.3 → v2.0.0.rc.4 ###

After pushing the new code to the production server and upgrading the version number in the Google App Engine 'Versions' panel, do the following:

  1. Flush memcache.
  1. If necessary, stop the SearchRanker job (and any others that refer to ExplorationModel).
  1. Run the ExplorationMigrationJobManager job once, and wait for it to finish.
  1. Flush memcache (as a precaution).
  1. Restart the SearchRanker job (and any others), if needed.
  1. Play through an exploration on the site to ensure that everything works as expected.

### Migrating v2.0.0.rc.2 → v2.0.0.rc.3 ###

v2.0.0.rc.3 introduced a schema change in how explorations were stored in the backend, due to the removal of the 'special' END state. The migration process for upgrading Oppia is therefore a little more complex than usual. This page contains instructions for performing the migration after pushing the new code to the production server and upgrading the version number to 2-0-0-rc-3 in the Google App Engine 'Versions' panel.

  1. Flush memcache. (This is critical.)
  1. Go to /admin, and run the ExplorationValidityJobManager job. Ensure that its output is `[]` (i.e., all explorations are valid). **This must be done before continuing.**
  1. Run the ExplorationMigrationJobManager job once, and wait for it to finish.
  1. Run the CompletionEventsMigrator job once, and wait for it to finish.
  1. As a check, return to the Google App Engine admin panel, and verify that the explorations in the datastore all have a states\_schema\_version property and that the value of this property is 3.
  1. Flush memcache (as a precaution).
  1. Play through an exploration on the site to ensure that everything works as expected.
