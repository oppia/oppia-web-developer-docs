## Doing a code release

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

  **Note**: you can get this and other useful information for the release by running:

  ```
    python scripts/release_info.py
  ```

  (In the future, we should consider also tagging changes with their commit hash, similar to [this](https://github.com/angular/angular.js/blob/master/CHANGELOG.md).)

1. Do a PR from the release branch into `master`, and wait for the Travis-CI checks to turn green. **Do not squash-merge this PR.**

1. Merge the release branch into both `master` and `develop`, tag the new release, and delete the release branch:

  ```
    git checkout master
    git pull origin master
    git merge release-[VERSION_NUMBER]
    git push origin master

    git tag -a v[VERSION_NUMBER] -m 'Version [VERSION_NUMBER]'
    git push --tags

    git checkout develop
    git pull origin develop
    git merge release-[VERSION_NUMBER]
    git push origin develop

    git branch -D release-[VERSION_NUMBER]
    git push origin --delete release-[VERSION_NUMBER]
  ```

  (replacing `[VERSION_NUMBER]` with the relevant version number, e.g. `1.1.0`).

1. Draft a description of the new release on the [Releases page](https://github.com/oppia/oppia/releases/new).

Congratulations, you've just done a release!
