## Overview

For non-python files, we run partial ci tests depending on the tests that a specific file effects. The process of determining which tests to run goes like this:

1. Generate a root files mapping which maps files to their root files.
2. Store golden files containing the page modules that a specific test uses.
3. Run a script inside the Github workflow which will map changed files in a PR to their root files using the mapping above. Afterwards, map those root files to tests by using the golden files containing the page modules that a test uses.

# Root Files Config

The root files config at `core/tests/root-files-config.json` contains all the valid root files that are generated in the root files mapping. This ensures that all files in the codebase either lead to a root file or are a root file themselves. We also have a list of root files that should run all tests, the valid root files are stored in the field `VALID_ROOT_FILES`, while the run all tests root files are stored in the field `RUN_ALL_TESTS_ROOT_FILES`. If you get an error that there is a root file not contained in these lists, please add them to one of these lists depending on the context of the file. If the specific file has a chance to break some part of the Oppia website, like `src/index.html`, please add it to the `RUN_ALL_TESTS_ROOT_FILES`, otherwise if it is a file like `README.md`, please add it to the `VALID_ROOT_FILES`.