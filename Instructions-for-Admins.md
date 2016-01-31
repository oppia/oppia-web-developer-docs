## Doing a release

To release a new version of Oppia, follow the following steps. This assumes that a `release-[VERSION_NUMBER]` branch has already been cut.

1. If any changes have been made to the integrations\_dev folder or to /static/scripts/oppia-player-0.0.0.js since the last release, run the integrations release process and test these integrations. More information can be found [here](https://github.com/oppia/oppia/tree/master/integrations_dev/build_new_release.py).

1. If the terms have been updated in this release cycle, update `feconf.REGISTRATION_PAGE_LAST_UPDATED_UTC` accordingly.

1. If new contributors have contributed in this release cycle, update the `AUTHORS` and `CONTRIBUTORS` files, as well as the Credits section on `pages/about.html`.

1. Run

  ```
    bash scripts/start.sh
  ```

  and play with the app for a while to make sure that nothing seems amiss.

1. Bump the version number by editing `app.yaml`, and update the `CHANGELOG` file. Use the commit message `Bump the version number to [VERSION_NUMBER] and update the changelog.` in order to make it easier to find when compiling future changelists.

  **Note**: a handy way to get a summary of the most recent changes is:

  ```
    git log --pretty=format:"%h - %an, %ar : %s"
  ```

  (In the future, we should consider also tagging changes with their commit hash, similar to [this](https://github.com/angular/angular.js/blob/master/CHANGELOG.md).)

1. Merge the release branch into both `master` and `develop`, and tag the new release:

  ```
    git checkout master
    git pull origin master
    git merge release-[VERSION_NUMBER]
    bash scripts/run_tests.sh
    git push origin master

    git tag -a v[VERSION_NUMBER] -m 'Version [VERSION_NUMBER]' master
    git push --tags

    git checkout develop
    git pull origin develop
    git merge release-[VERSION_NUMBER]
    git push origin develop
  ```

  (replacing `[VERSION_NUMBER]` with the relevant version number, e.g. `1.1.0`).

1. Delete the release branch.

  ```
    git branch -D release-[VERSION_NUMBER]
    git push origin --delete release-[VERSION_NUMBER]
  ```

1. Draft a description of the new release on the [Releases page](https://github.com/oppia/oppia/releases/new).

1. Checkout the master branch.

  ```
    git checkout master
  ```

1. If you want emails to be sent to the admin on job failures, specify a valid email address in feconf.ADMIN\_EMAIL\_ADDRESS and set feconf.CAN\_SEND\_EMAILS\_TO\_ADMIN to True. If you are planning to send emails to users in general, you may also wish to edit feconf.SYSTEM\_EMAIL\_ADDRESS, feconf.CAN\_SEND\_EMAILS\_TO\_USERS and feconf.DEFAULT\_EMAIL\_UPDATES\_PREFERENCE. Finally, you may also wish to edit cron.yaml and queue.yaml to change the times at which jobs are executed and the rate of job processing; if in doubt, use the default values. [**TODO**: make all these into deploy\_data settings.]

1. If there is a migration, you may want to change the default rate of jobs in queue.yaml from 3/m to 5/s to speed up the exploration migration job.

1. Update the test app at oppiatestserver.appspot.com by running

  ```
    python scripts/deploy.py --app_name=oppiatestserver
  ```

  Note that you'll need to change the version number in the App Engine console.

1. If the `index.yaml` file has changed since the last update, update only the indexes on oppia.org by running

  ```
    ../oppia_tools/google_appengine_1.9.19/google_appengine/appcfg.py update_indexes . --oauth2
  ```

  Wait for the indexes to finish uploading before proceeding with the next step.

1. Update the live server at oppia.org by running

  ```
    python scripts/deploy.py --app_name=oppiaserver
  ```

  For this you will need the oppia.org deploy\_data folder, for which you should ask an Oppia administrator. Once the update has been completed, update the version number in the App Engine console and flush memcache to remove stale data.

1. If the exploration schema version has changed in this release, you may need to run a schema migration. Follow the instructions [here](https://github.com/oppia/oppia/wiki/Migration-Instructions).

1. If you changed the default rate of queue.yaml above, needed an exploration migration, and the migration job has finished, you will want to reset the rate at which the jobs are running by making sure queue.yaml has a 5/m default rate and then execute the command:

  ```
    ../oppia_tools/google_appengine_1.9.19/google_appengine/appcfg.py update_queues . --oauth2
  ```

1. Announce the release in the [discussion forum](https://groups.google.com/forum/?fromgroups#!aboutgroup/oppia) and the oppia-announce@ mailing list.

Congratulations, you've just made a release!
