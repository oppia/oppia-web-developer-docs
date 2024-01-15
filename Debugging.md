We do a lot of debugging at Oppia, whether because tests are failing on a PR or because of a tricky bug that was found during release testing. These guides will help you get started debugging and offer useful tips:

Start here if failing tests are stopping you from pushing or merging a PR:

* [[If your presubmit checks fail|If-your-presubmit-check-fails]]
* [[If CI checks fail on your PR|If-CI-checks-fail-on-your-PR]]

Unless the bug you are trying to fix is trivial, we recommend creating a debugging doc to organize your work:

* [[Debugging Docs|Debugging-Docs]]

Here are some debugging guides for particular kinds of issues you might encounter or types of tests:

* [[Interpreting GitHub Actions Results|Interpreting-GitHubActions-Results]]
* [[Finding the commit that introduced a bug|How-to-find-the-commit-which-introduced-a-bug]]
* [[Debugging end-to-end tests|Debug-end-to-end-tests]]
* [[Debugging backend tests|Debug-backend-tests]]
* [[Debugging frontend tests|Debug-frontend-tests]]
* [[Debugging lighthouse Tests|Lighthouse-Tests]]
* [[Debugging custom ESLint check tests|Debug-custom-ESLint-check-tests]]
* [[Debugging custom Pylint check tests|Debug-custom-Pylint-check-tests]]

Finally, see these debugging stories to learn more about how debugging works in practice:

* [[Debugging Stories|Debugging-Stories]]
