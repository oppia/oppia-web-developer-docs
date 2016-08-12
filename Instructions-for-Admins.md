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

1. Do a PR from the release branch into `master`, and wait for the Travis-CI checks to turn green. **DO NOT SQUASH-MERGE THIS PR.**

1. Tag the new release, and delete the release branch:

  ```
    git checkout master
    git pull origin master
    git tag -a v[VERSION_NUMBER] -m 'Version [VERSION_NUMBER]'
    git push --tags

  ```
  (replacing `[VERSION_NUMBER]` with the relevant version number, e.g. `1.1.0`).

1. Draft a description of the new release on the [Releases page](https://github.com/oppia/oppia/releases/new).

1. Deploy the release.

1. Make a PR to merge `master` into `develop`. **DO NOT SQUASH MERGE.**

Congratulations, you've just done a release!

## Doing a hotfix
1. Make a branch off `master`, and add the commits desired.

1. Do a PR from the hotfix branch into `master`, and wait for the Travis-CI checks to turn green. It's ok to squash merge this.

1. Deploy the hotfix.

1. Do a PR from `master` to `develop`. **DO NOT SQUASH MERGE.**
