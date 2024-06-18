## Introduction

Our CI process has a workflow, `check_ci_test_suites_to_run`, that determines which test suites to run for a given PR based on the files that the PR modified.
If your PR fails due to the `check_ci_test_suites_to_run` workflow, please look at the error log and depending on the error, do the following:

* If you see an error about the root files config, then see the [root files config section](#root-files-config) below.

## Overview of Partial CI Tests Structure

For non-python files, we run partial CI tests depending on the tests that a specific file affects. Running partial tests like this allows PRs to be checked faster using the tests that a PR actually modifies. This faster test speed allows developers to get feedback faster and frees up CI resources. The process of determining which tests to run goes like this:

1. Generate a root files mapping which maps files to their root files. This file is generated at the start of every PR check run and is stored at `root-files-mapping.json`.
2. Store golden files containing the page modules that a specific test uses. These golden files are stored at `core/tests/test-modules-mappings/{{test-type}}/{{test-name}}`.
3. Run the script, `scripts/check_ci_test_suites_to_run.py` inside the Github workflow which will map changed files in a PR to their root files using the mapping above. Afterwards, map those root files to tests by using the golden files containing the page modules that a test uses.

# Root Files Config

The root files config at `core/tests/root-files-config.json` contains all the valid root files that are generated in the root files mapping. This ensures that all files in the codebase either lead to a root file or are a root file themselves. We also have a list of root files that should run all tests. The valid root files are stored in the field `VALID_ROOT_FILES`, while the run all tests root files are stored in the field `RUN_ALL_TESTS_ROOT_FILES`.
If you get an error that there is a root file not contained in these lists, please add them to one of these lists depending on the context of the file:

* If the specific file has a chance to break some part of the Oppia website, like `src/index.html`, please add it to the `RUN_ALL_TESTS_ROOT_FILES`.
* If it is a file like `README.md` which doesn't affect any test, please add it to the `VALID_ROOT_FILES`.