### Migrating a production instance of Oppia from v2.0.0.rc.2 to v2.0.0.rc.3 ###

v2.0.0.rc.3 introduced a schema change in how explorations were stored in the backend, due to the removal of the 'special' END state. The migration process for upgrading Oppia is therefore a little more complex than usual. This page contains instructions for performing the migration after pushing the new code to the production server and upgrading the version number to 2-0-0-rc-3 in the Google App Engine 'Versions' panel.

  1. Flush memcache. (This is critical.)
  1. Go to /admin, and run the ExplorationValidityJobManager job. Ensure that its output is `[]` (i.e., all explorations are valid). **This must be done before continuing.**
  1. Run the ExplorationMigrationJobManager job once, and wait for it to finish.
  1. Run the CompletionEventsMigrator job once, and wait for it to finish.
  1. As a check, return to the Google App Engine admin panel, and verify that the explorations in the datastore all have a states\_schema\_version property and that the value of this property is 3.
  1. Flush memcache (as a precaution).
  1. Play through an exploration on the site to ensure that everything works as expected.

### Migrating a production instance of Oppia from v2.0.0.rc.3 to v2.0.0.rc.4 ###

v2.0.0.rc.4 introduced another schema change in how explorations were stored in the backend, due to the redesign of the rules/feedback system. This page contains instructions for performing the migration after pushing the new code to the production server and upgrading the version number to 2-0-0-rc-4 in the Google App Engine 'Versions' panel.

  1. Flush memcache.
  1. Run the ExplorationMigrationJobManager job once, and wait for it to finish.
  1. Flush memcache (as a precaution).
  1. Play through an exploration on the site to ensure that everything works as expected.