Sometimes we need to make urgent updates to the production server outside the normal release cycle, for example to fix a regression that's degrading our users' experiences. These urgent fixes are called hotfixes, and they follow the procedure described below.

1. Decide whether a PR really needs to be hotfixed. Hotfixing requires extra work by our release team, so we reserve it only for the PRs that really need it. Hotfixing is only for PRs that meet the following criteria:

   * The PR must fix a bug that currently exists in production.
   * The bug must be expected to significantly degrade the user experience. For example, bugs that break important features or make core functionality hard to use would qualify. Minor aesthetic issues that don't confuse users would not qualify.
   * The bug must be a regression. In other words, the broken functionality must have been working recently. If it has been broken for a long time, then the fix can wait for the normal release cycle.

2. If the PR needs to be hotfixed, fill in [this form](https://forms.gle/4CRqXovA3xS27rDLA) to notify the release team.

3. Within a couple days, you should be contacted by the release coordinator for the current release. Work with them to get your changes into production safely. If you don't hear anything, reach out to the release team, whose contact info can be found on [[their wiki page|Release-schedule-and-other-information]].
