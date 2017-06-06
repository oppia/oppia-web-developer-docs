## Doing a code release

To release a new version of Oppia, follow the following steps. 

### Prepare for the release

1. If any changes have been made to the integrations\_dev folder or to /static/scripts/oppia-player-0.0.0.js since the last release, run the integrations release process and test these integrations. More information can be found [here](https://github.com/oppia/oppia/tree/master/integrations_dev/build_new_release.py).

1. If the terms have been updated in this release cycle, update `feconf.REGISTRATION_PAGE_LAST_UPDATED_UTC` accordingly.

1. If new contributors have contributed in this release cycle, update the `AUTHORS` and `CONTRIBUTORS` files, as well as the Credits section on `pages/about.html`. Check the results of the credits form for non-technical contributors. 

### Cut the release branch

1. Cut a `release-[VERSION_NUMBER]` branch. Test the release branch.

1. If any additional bugfixes need to happen, make a PR to `develop`, and cherry-pick any necessary commits onto the release branch. 

1. Run

   ```
     bash scripts/start.sh
   ```

   and play with the app for a while to make sure that nothing seems amiss.

### Deploying the release

1. Deploy the release. If fixes need to be made immediately after deployment, merge them into `develop` and cherry-pick onto the release branch (similar to before), then deploy again.

1. Update the `CHANGELOG` file. Use the commit message `Update the changelog.` in order to make it easier to find when compiling future changelists.

   **Note**: you can get this and other useful information for the release by running:
 
   ```
      python scripts/release_info.py
   ```

   (In the future, we should consider also tagging changes with their commit hash, similar to [this](https://github.com/angular/angular.js/blob/master/CHANGELOG.md).)

1. Tag the commit incrementing the release version on the release branch:

   ```
     git tag -a v[VERSION_NUMBER] -m 'Version [VERSION_NUMBER]'
     git push --tags

   ```
   (replacing `[VERSION_NUMBER]` with the relevant version number, e.g. `1.1.0`).

1. Draft a description of the new release on the [Releases page](https://github.com/oppia/oppia/releases/new).

1. Protect the release branch from further pushes on the admin page.

Congratulations, you've just done a release!

## Doing a hotfix
1. Make a branch off develop and make the fix, and make a PR into develop. Branch off the release branch, and cherry-pick the commits desired onto the hotfix branch.

1. Deploy the hotfix.