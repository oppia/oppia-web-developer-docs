## Table of contents

* [Introduction](#introduction)
* [Merge conflicts](#merge-conflicts)
* [Network problems](#network-problems)
* [Failing tests](#failing-tests)

## Introduction

If your PR build fails, do not despair! Scroll down to the bottom of the PR thread until you see the results of the continuous integration (CI) tests that ran:

![Screenshot of PR CI results](images/prCiResults.png)

The failure may be due to one of the following things:

* If you see a warning that your PR has a merge conflict, then see the [merge conflicts section](#merge-conflicts) below.
* If your issue is not a merge conflict, then click on the "Details" link next to any failing builds and inspect the logs.

  * If you see an error when installing third-party libraries, then there was probably a network issue. See the [network problems](#network-problems) section below.
  * If you see from the logs that a test is failing, see the [failing tests section](#failing-tests) below.

## Merge conflicts

You can fix merge conflicts by following the "merge from develop" instructions in  [step 5 of our instructions for making a pull request](https://github.com/oppia/oppia/wiki/Make-a-pull-request#step-5-address-review-comments-until-all-reviewers-approve). Then when you push the merge commit to your feature branch on GitHub, the merge conflict message will disappear.

## Network problems

If the error has a message like the one below, then it is due to a network error and is unrelated to your PR. Please reach out to a code owner or Core Maintainer to restart your test.

```text
Installing Node.js
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/runpy.py", line 174, in _run_module_as_main
    "__main__", fname, loader, pkg_name)
  File "/usr/local/lib/python2.7/runpy.py", line 72, in _run_code
    exec code in run_globals
  File "/home/circleci/oppia/scripts/install_third_party_libs.py", line 311, in <module>
    main()
  File "/home/circleci/oppia/scripts/install_third_party_libs.py", line 236, in main
    setup.main(args=[])
  File "scripts/setup.py", line 158, in main
    download_and_install_node()
  File "scripts/setup.py", line 120, in download_and_install_node
    outfile_name)
  File "scripts/setup.py", line 81, in download_and_install_package
    python_utils.url_retrieve(url_to_retrieve, filename=filename)
  File "python_utils.py", line 289, in url_retrieve
    return urllib.urlretrieve(source_url, filename=filename)
  File "/usr/local/lib/python2.7/urllib.py", line 98, in urlretrieve
    return opener.retrieve(url, filename, reporthook, data)
  File "/usr/local/lib/python2.7/urllib.py", line 289, in retrieve
    "of %i bytes" % (read, size), result)
urllib.ContentTooShortError: retrieval incomplete: got only 7372553 out of 18638507 bytes

Exited with code exit status 1
```

If you see a different error while installing third-party libraries, please file an issue and mention @automated-qa-reviewers to notify the Automated QA team.

## Failing tests

If you see that a test is failing, there are two possibilities: your code could be wrong, or the test could be flaky. There is no easy way to tell whether a particular failure is a flake, but here are some guidelines:

* Flakes mostly occur in the end-to-end (E2E) tests. Sometimes we see flakes in the lighthouse or frontend tests, but the backend tests and linters almost never flake.
* Consider whether your changes could have plausibly caused the failure. For example, if you just updated the README, then there's no way that you could have broken an E2E test. However, be careful to consider that changes in one part of the code can have unintended effects in apparently unrelated code. For example, if you add an E2E test that creates an exploration with the same name as an exploration created by another E2E test, you could break that other E2E test, even if it's testing completely unrelated code.
* Check whether the error message you see matches a known flake. For E2E tests, look for a green message in the log like this:

  ```text
  E2E logging server says test flaky: {{true/false}}
  ```

  This message is based on a list of known flakes maintained by the Automated QA team. Note however that this list may be incomplete, so a test could be flaking even if this message says `false`.

If your code is wrong, then you'll need to fix it just as you would [respond to reviewer comments](https://github.com/oppia/oppia/wiki/Make-a-pull-request#step-5-address-review-comments-until-all-reviewers-approve). You may also want to review the documentation on our various CI checks to help you debug:

* [[Lint Checks|Lint-Checks]]
* [[Backend tests|Backend-tests]]
* [[Frontend tests|Frontend-unit-tests-guide]]
* [[End-to-end tests|End-to-End-Tests]]
* [[Lighthouse Tests|Lighthouse-Tests]]

Note that all our CI checks except for the backend tests merge from the upstream `develop` branch before running, so you may need to merge from `develop` locally to reproduce the failure.

If the test is flaky, ask one of your reviewers to restart the test for you.

Following these instructions should result in PRs that are green and ready to merge by the time a reviewer looks at them, thus shortening the review cycle! If you are still unable to resolve the issues yourself, please follow our instructions to [[get help|Get-help]] from other developers.
