## Table of Contents

* [Introduction](#introduction)
* [Testing philosophy](#testing-philosophy)
  * [Unit tests](#unit-tests)
    * [Writing comprehensive tests](#writing-comprehensive-tests)
    * [Mocking](#mocking)
  * [Integration tests](#integration-tests)
  * [Unit versus integration tests at Oppia](#unit-versus-integration-tests-at-oppia)
  * [When to mock](#when-to-mock)
* [Run backend tests](#run-backend-tests)
  * [Identifying whether the tests passed](#identifying-whether-the-tests-passed)
  * [Coverage reports](#coverage-reports)
    * [Warning: full coverage does not mean your tests are comprehensive](#warning-full-coverage-does-not-mean-your-tests-are-comprehensive)
* [Write backend tests](#write-backend-tests)
  * [Backend test structure](#backend-test-structure)
  * [Guidelines for writing good tests](#guidelines-for-writing-good-tests)
  * [Sharding backend tests](#sharding-backend-tests)
    * [How sharding works](#how-sharding-works)
    * [Common errors](#common-errors)
    * [Adding new tests to shards](#adding-new-tests-to-shards)
  * [Common testing scenarios](#common-testing-scenarios)
  * [Examples](#examples)
    * [Example: Writing unit tests for domain classes](#example-writing-unit-tests-for-domain-classes)
    * [Example: Writing integration tests for handlers (controllers)](#example-writing-integration-tests-for-handlers-controllers)

## Introduction

All code in Oppia's backend must be thoroughly tested because tests help catch bugs, help new contributors understand our backend code, and ensure that our code doesn't get broken by other developers in the future.

This guide covers Oppia’s backend tests. We also have separate pages for [[frontend tests|Frontend-tests]] and [[end-to-end tests|End-to-End-Tests]].

## Testing philosophy

Let's begin by explaining some testing philosophy. This will help you design your tests; we'll talk about how to actually write them later. There are two main kinds of tests that we use in the backend: unit tests and integration tests.

### Unit tests

Unit tests check that a small unit of code, usually a function or a class, works correctly. By testing only a small piece of code at a time, we can write very thorough tests. For example, it would be a lot harder to write comprehensive test cases for all of Oppia than it would be to write comprehensive test cases for a small utility function that checks whether a username is valid.

#### Writing comprehensive tests

Let's consider what test cases we might write for such a utility. Suppose we only want to allow usernames that are between 1 and 7 characters (inclusive), and that include only English letters and Arabic numerals. These test cases would not be comprehensive:

* `'abc123'`: Valid
* `'aBc'`: Valid
* `'1'`: Valid
* `'abc_123'`: Invalid
* `'abc123de'`: Invalid

**Exercise:** Take a moment to think about what test cases are missing.

Here's an example implementation of our utility function that is incorrect but passes these test cases:

```python
ALLOWED_USERNAME_CHARACTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
]
MAX_USERNAME_LENGTH= 7

def check_is_username_valid(username):
    if not len(username) <= USERNAME_LENGTH_RANGE[1]:
        return False
    for character in username:
        if character not in ALLOWED_USERNAME_CHARACTERS:
            return False
    return True
```

Why is this code incorrect? Consider the case where `username = ''`. The function will return True even though this username is fewer than 1 character long. Our tests would be more thorough if we added a test with an empty string:

* `''`: Invalid

**Tests should cover the full range of inputs that the code being tested might be given. Remember to test error cases where the function is used incorrectly.**

#### Mocking

Most functions are quite a bit more complicated than our `check_is_username_valid()` example above. Often, they make calls to other functions that perform complicated operations we don't want to test. For example suppose we have a function `download(url)` that downloads the HTML code at `url` and returns it as a string. Now consider the following function that we want to test:

```python
def get_current_time_utc():
    response = download('https://worldtimeapi.org/api/timezone/Etc/UTC.txt')
    for line in response.split('\n'):
        if line.startswith('datetime: '):
            return line.lstrip('datetime: ')
    return None
```

Note that https://worldtimeapi.org/api/timezone/Etc/UTC.txt returns text like this:

```text
abbreviation: UTC
client_ip: <redacted>
datetime: 2021-08-26T00:38:19.941464+00:00
...
week_number: 34
```

When testing `get_current_time_utc()`, we don't want to actually query worldtimeapi.org because we don't want our tests to fail just because we lose our network connection or the worldtimeapi.org servers go down. Instead, we want to replace `download()` with a fake function that we control. This function is called a _mock_ or _stub_, and the process of introducing such a function is called _mocking_ or _stubbing_.

To return to our earlier example, we might replace `download()` with this mock function:

```python
def mock_download(url):
    return '\n'.join([
        'abbreviation: UTC',
        'client_ip: 127.0.0.1',
        'datetime: 2021-08-26T00:38:19.941464+00:00',
        ...
        'week_number: 34',
    ])
```

That way our tests still check that we can handle responses from worldtimeapi.org, but we don't have to worry about our test results depending on a network query to an external server.

### Integration tests

Unit tests have a major failing: even when each small unit of your code is correct, your program as a whole can be incorrect if you don't put those units together correctly. For example, consider the two functions below:

```python
def search_for_substring(string_to_search, substring):
    return substring in string_to_search

def get_search_args_for_illegal_usernames(username):
    return 'admin', username


if __name__ == '__main__':
    print(search_for_substring(*get_search_args_for_illegal_usernames('i_am_an_admin')))
```

If you run this code, you'll see `False` printed even though the username contains the substring `admin`. The problem is that `get_search_args_for_illegal_usernames()` returns the substring first and the string to search (the username) second, but `search_for_substring()` expects the arguments to be in the opposite order. In this case the code units are fine. The bug arises when we integrate those units together.

We use integration tests to catch bugs like these. These tests are actually written just like our unit tests. The only difference is that we mock less in integration tests.

### Unit versus integration tests at Oppia

At Oppia, we don't distinguish clearly between unit and integration tests. Many of our backend unit tests end up being a lot like integration tests just because we don't bother to mock everything. However, the distinction is important because we do sometimes write integration tests on purpose, so you'll see some test code described that way.

### When to mock

We just saw how the difference between unit and integration tests largely comes down to how much mocking we do, but that raises a question: "When should you mock?" There is no hard rule, but we generally encourage developers to mock only when doing so makes the tests easier to write. Don't bother mocking every function call your unit of code makes.

In fact, too many mocks can be a problem because when someone changes the code you've mocked, they have to remember to change your mock too. This introduces opportunities for errors that cause the mock code to diverge from the code being mocked, which can let bugs slip past the tests undetected.

## Run backend tests

You can run backend tests like this:

```console
python -m scripts.run_backend_tests
```

Alternatively, you can run just a single test module like this:

```console
python -m scripts.run_backend_tests --test_target=core.controllers.editor_test
```

The argument to `--test_target` can be as specific as you like. For example:

* Run a class of tests: `--test_target=core.controllers.editor_test.BaseEditorControllerTests`
* Run a single test: `--test_target=core.controllers.editor_test.BaseEditorControllerTests.test_editor_page`

If you also want to see the output of `print` statements and error logs in the terminal, use `--verbose` like this:

```console
python -m scripts.run_backend_tests --test_target=core.controllers.editor_test --verbose
```

For more information about `--test_target` and other flags, run:

```console
python -m scripts.run_backend_tests --help
```

Note that while the tests are running, you may see the word `ERROR` show up in the test logs. This does not necessarily mean that an error has occurred; it happens because some tests actually expect an error to be raised.

### Identifying whether the tests passed

The tests pass if, at the end of the test output, you see the message:

```text
All tests pass.
```

Every line representing a test class will also start with `SUCCESS`.

However, one or more tests failed if you get something like this instead:

```text
Ran 326 tests in 47 test classes.
(1 ERRORS, 0 FAILURES)
```

You can find more information about the exact errors by scrolling up and looking through the error log for tests marked `FAILED` (indicating that an assertion in the test failed) and `ERROR` (indicating that an exception was raised by the test).

Note that you might see a bunch of lines that just contain `[datastore]`. While annoying, this is normal. We just haven't figured out how to get rid of them yet. You can follow [#14239](https://github.com/oppia/oppia/issues/14239) to track our progress in fixing this.

### Coverage reports

#### Overall coverage

We use a simple tool called *code coverage* to check that all of Oppia’s backend code is fully covered by at least one test. Coverage reports specify which lines of each file have not been executed in any test, and they report what percentage of each file (branches and lines) is covered by the tests. Currently, Oppia has achieved **100% backend line coverage**. We require that all changes maintain this full coverage.

When writing a test for a function or class, you can generate a coverage report to verify that all the lines of the function/class have been included in the tests. To do this, simply add the `--generate_coverage_report` flag to the `run_backend_tests` command:

```console
python -m scripts.run_backend_tests --generate_coverage_report
```

If there are **any** backend test errors, no coverage report will be produced. Please fix those errors and then re-run the above command. If the tests all pass, a coverage report will be printed that lists each backend file, along with the lines not covered by tests. Here is an example of a coverage report:

```text
Name                                                                             Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------------------------------------------------
core/android_validation_constants.py                                                23      0      0      0   100%
core/constants.py                                                                   32      1      2      1    94%   3, 5->4
core/controllers/access_validators.py                                               80      0     10      0   100%
```

Notice that `constants.py` has only 94% code coverage because line 3 and the branch `5->4` were not covered. This means that none of the tests executed line 3. It also means that a branch in the code causes execution to jump from line 5 to line 4, and none of the tests executed this branch. Here's an example of such a branch:

```text
1 for elem in lst:
2    if elem == 0:
3        continue
4    pass
```

If we find an element in `lst` that is `0`, then we will hit the `continue` statement, and execution will jump from line 3 to line 1. This would be denoted in the coverage report as a branch `3->1`. We currently require that all files have full line coverage, and files not in the `scripts/backend_tests_incomplete_coverage.txt` exclusion list are also required to have full branch coverage. This means that you might see an overall coverage of less than 100% on your PR--that's okay so long as all the missing coverage is coming from branches in files that are in the exclusion list.

#### Warning: full coverage does not mean your tests are comprehensive

To see how tests that produce 100% coverage can still not be comprehensive, consider the following pseudocode:

```text
1 # Compute the absolute value of a number
2 function absoluteValue(number) {
3   if number <= 0 {
4     return -number
5   } else {
6     return number
7   }
8 }
```

Now consider the following sets of test cases:

* `absoluteValue(1)` and `absoluteValue(5)`: These test cases are not comprehensive because they only test positive numbers. Code coverage is also not 100% because line 4 is never executed.
* `absoluteValue(0)` and `absoluteValue(1)`: These test cases are not comprehensive because they do not test negative numbers, and it's important for an absolute value function to correctly handle negative inputs. However, the code coverage is 100% because both blocks of the `if` statement are executed.
* `absoluteValue(-1)`, `absoluteValue(0)`, and `absoluteValue(1)`: These test cases are comprehensive, and code coverage is 100%. Note that even though line 1 doesn't execute, coverage is 100% because line 1 is not executable.

This example illustrates something very important about code coverage: **Code coverage less than 100% implies that the tests are not comprehensive, but code coverage of 100% does NOT imply that tests are comprehensive.** Therefore, while code coverage is a useful tool, you should primarily think about whether your tests cover all the possible behaviors of the code being tested. In other words, you should have a behavior-first perspective. Don't just think about which lines are covered.

#### Associated test files

We require that every backend file have an associated test file. For example, if you create a file `new_file.py`, you will also need to create a test file `new_file_test.py`. We have a CI check (defined by `.github/workflows/backend_associated_test_file_check.yml`) that will fail if any test files are missing.

#### Per-file coverage

Above, we discussed overall coverage, which measures how much of our code runs when all the tests run. Per-file coverage is similar, but it measures only how much of a file runs when that file's associated test file runs. We are working to achieve full per-file coverage, but since that work is incomplete, we currently allow files in the exclusion list `scripts/backend_tests_incomplete_coverage.txt` to have incomplete per-file line and branch coverage (though they must still have 100% overall line coverage).

If your changes result in incomplete per-file coverage of a file not in the exclusion list, you'll see an error like this:

```text
 INCOMPLETE COVERAGE (95.0%): scripts.run_lighthouse_tests_test
Name                              Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------------
scripts/run_lighthouse_tests.py     118      5     34      3    95%   107->116, 111-113, 114->107, 117-118
-----------------------------------------------------------------------------
TOTAL                               118      5     34      3    95%
```

If you want to check that you've fixed the per-file coverage issue without running all the tests, you can use `--test_target` to run only the test file associated with the file whose coverage you want to check. Then in the overall coverage report, check the line for your file to see if it's 100%. Note that most other files in the codebase will show as being incompletely covered since you didn't run all the tests, and that's okay.

## Write backend tests

### Backend test structure

We write our backend tests with Python's [unittest framework](https://docs.python.org/3/library/unittest.html). You should familiarize yourself with that framework by reading through the ["basic example" in its documentation](https://docs.python.org/3/library/unittest.html#basic-example). You should also take a look at what [assertion functions](https://docs.python.org/3/library/unittest.html#unittest.TestCase) are available.

Backend test files live alongside the backend code files they test. For example, alongside `core/controllers/base.py` you'll find `core/controllers/base_test.py`. That `_test.py` suffix is important. It's how we identify which files have tests to run. Note that each file is entirely code or entirely tests. No file mixes code and tests.

Inside test files, tests are organized into classes whose names end in `Tests`. Test cases are methods of these classes, and the method names begin with `test_`. Note that only methods beginning with `test_` and inside classes that inherit from `unittest.TestCase` are executed as tests. Here is an example of a test from `base_test.py`:

```python
class HelperFunctionTests(test_utils.GenericTestBase):

    def test_load_template(self):
        oppia_root_path = os.path.join(
            'core', 'templates', 'pages', 'oppia-root')
        with self.swap(feconf, 'FRONTEND_TEMPLATES_DIR', oppia_root_path):
            self.assertIn(
                '"Loading | Oppia"',
                base.load_template('oppia-root.mainpage.html'))
```

Notice that the test class inherits from `test_utils.GenericTestBase`, which provides a few functions you may want to use:

* `GenericTestBase` inherits from `unittest.TestCase`, so all the normal unittest functions are available. In particular, we use the unittest assertion functions.

* The base class provides two swap functions for mocking:

  * `swap(object, attribute_to_mock, mock)`: `attribute_to_mock` is the name of the thing you want to mock (it can be a variable, a function, or even a class). `object` is the object that has `attribute_to_mock` as an attribute, and `mock` is the mock value you want to substitute in for `attribute_to_mock`. For example suppose you want to mock the constant `DEV_MODE` in the module `constants` with `True`. You would call `swap(constants, 'DEV_MODE', True)`.

  * `swap_with_checks(object, attribute_to_mock, mock, expected_args=None, expected_kwargs=None, called=True)`: The first three arguments are the same as `swap()`. However, this function also lets you assert that your mock function is called in particular ways.

    `expected_args` takes a list of tuples, where each tuple contains a group of expected positional arguments. The test will assert that the function is called once with each group of expected arguments, in the order in which you specify the groups. Note that the order of the arguments within each group must match the order in which the arguments are passed to the function.

    `expected_kwargs` accepts a list of dictionaries. Each dictionary specifies keyword arguments as key-value pairs, and the test will assert that your function is called once with each group of keyword arguments you specify, in the same order as the dictionaries appear in the list.

    If `expected_args` is `None`, then no assertions are made about the positional arguments that the mock function receives. The same is true of `expected_kwargs`.

    Lastly, `called` specifies whether we expect the mock function to have been called. The test will fail if this assertion is not met.

    Consider this example:

    ```python
    self.swap_with_checks(
        subprocess, 'Popen', mock_popen,
        expected_args=[(['python'],), (['python2'],)],
        expected_kwargs=[{'shell': True}, {'shell': False}])
    ```

    This code will assert that `mock_popen` receives the following calls in order:

    ```python
    mock_popen(['python'], shell=True)
    mock_popen(['python2'], shell=False)
    ```

  These swap functions each return a context where the mocking has been performed. You'll see this called a `swap` in the code. You can use the swap like this:

  ```python
  my_func_swap = self.swap(module, 'my_func', mock_my_func)

  with my_func_swap:
      func_being_tested()
  ```

  If you have a lot of swaps, the `with` statements can get pretty burdensome. You can use `GenericTestBase.exit_stack.enter_context` instead like this:

  ```python
  my_func_swap = self.swap(module, 'my_func', mock_my_func)

  self.exit_stack.enter_context(my_func_swap)

  func_being_tested()
  ```

  There are also other swap functions you can use. They are defined and documented in [`core/tests/test_utils.py`](https://github.com/oppia/oppia/blob/develop/core/tests/test_utils.py).

### Guidelines for writing good tests

1. **Each test method should test only a single behaviour.** This helps both with naming the test and with ensuring that the test doesn't fail for unrelated code changes.

   * When naming a test, start by writing a full sentence that clearly describes its behaviour. Try not to abbreviate if possible, but, if you need to do so in order to fit within the 80-character limit, make sure that the resulting test name is still meaningful and easy to understand.

   * We recommend that test names follow the format:

     ```text
     test_{{action}}_with_{{with_condition}}_{{has_expected_outcome}}
     ```

     where `{{action}}`, `{{with_condition}}`, and `{{has_expected_outcome}}` are replaced with appropriate descriptions. Put the outcome at the end, so that it's easy to compare consecutive tests that have slightly different conditions and divergent outcomes. Here are some examples that follow this format:

     * `test_get_by_auth_id_with_invalid_auth_method_name_is_none`
     * `test_get_by_auth_id_for_unregistered_auth_id_is_empty_list`

     These names are good because it's easy to see the differences between the tests: one tests an invalid auth method, and the other tests an unregistered auth. Correspondingly, these conditions lead to different outcomes (`name_is_none' vs. 'id_is_empty_list').

2. Tests should use the following general structure:

   * **Setup** - this is where you prepare any inputs/environment needed for the test.
   * **Baseline verification** - check the values without performing any action. This step is only needed if your action is state-changing (i.e. if the same assert statement would lead to one result at the baseline and a different result at the endline). Check the same values here as you check at the endline.
   * **Action** - perform the action or function call that leads to the expected change.
   * **Endline verification** - check that the values from the baseline verification have changed accordingly.

3. **Test the interface, not the implementation.** That is, treat the function as a black box and test its behavior. Don't test that the function uses a particular implementation. This will help you design a better API from an external user’s perspective. For example, consider the following function:

   ```python
   def absolute_value(number):
       return abs(number)
   ```

   Let's forget for the moment that this function is pointless and just focus on thinking about how to test it. We should test the function by providing some values, some positive and some negative, and checking that their absolute values are returned. We should _not_ test it by mocking `abs()` and making sure it was called correctly, as that would be testing the implementation instead of the interface. Remember that we want to test that the function behaves correctly, and we can demonstrate this most clearly by providing numbers to our function and checking that the function returns absolute values.

   You can check whether you're following this principle by imagining what would happen if you changed the function. For example, say you implemented `absolute_value()` differently:

   ```python
   def absolute_value(number):
       if number < 0:
           return -number
       return number
   ```

   After changing the implementation, your tests should all still pass. In our example, our tests that provide various numbers would still pass. Our test that mocked `abs()` would not.

4. Keep tests **simple**. Don't include any logic in the test. Write the test as a series of straightforward, descriptive and meaningful commands (also known in programming circles as "DAMP"). It's fine if there's some repetition, as long as the tests are easy to read.

5. **Don't use what you don't need.** By default, prefer to inherit from `unittest.TestCase` when writing tests. Only use `test_utils.GenericTestBase` when you need to interact with models or the app itself, or when you need the mocking capabilities that `GenericTestBase` provides. This helps keep our tests lean and fast.

   As a general rule, if the only thing your test needs to do is run a function and assert something about its return value, then `unittest.TestCase` is good enough. See https://github.com/oppia/oppia/pull/10869/files for an example of where both kinds of tests were necessary.

6. When building your suite of tests, try to include a range of possible behaviours, such as:

   * "Happy path" cases where the tested code was used correctly.
   * Failure cases where the tested code was used improperly.
   * Ambiguous cases that are on the edge between happy path cases and failure cases.
   * Boundary/edge cases that stress the function's capabilities. Think of these as the test cases you'd use if you were trying to break the code. For example, checking how an absolute value function handles `math.nan` or a string.

   Also, try writing contrasting tests. For example, if you are checking that an exception is raised under a certain criterion, also add a test to ensure that the exception is not raised when the criterion is not satisfied.

7. For **test outputs**, follow these guidelines:

   * Test each output as exactly and completely as possible. For example, it's better to compare equality for an entire dict rather than just checking that a particular value has changed.
   * Use `assertTrue(value)` or `assertFalse(value)` instead of `assertEqual(value, True)` or `assertEqual(value, False)`.
   * Use `assertIsNone(value)` instead of `assertEqual(value, None)`.

8. If you create a new test module (a `*_test.py` file), you will need to add it to a shard in [`oppia/scripts/backend_test_shards.json`](https://github.com/oppia/oppia/blob/develop/scripts/backend_test_shards.json). See the [section on shards below](#sharding-backend-tests).

### Common testing scenarios

1. If a function tests **more than one behaviour**, split the test into multiple parts. For example, if you have a single test that looks like this:

   * Test:

     * Setup
     * Action 1
     * Assertion 1
     * Action 2
     * Assertion 2

   then split it into two tests as follows:

   * Test 1:

     * Setup
     * Action 1
     * Assertion 1

   * Test 2:

     * Setup + Action 1
     * Action 2
     * Assertion 2

2. For assertions that **check errors** (e.g. self.assertRaises or self.assertRaisesRegexp), keep the part of the code enclosed in self.assertRaises as small as possible so that you can be sure that the error is actually being caused by that part of the code (and not, say, by the setup code).

3. **Guidelines for testing private methods/functions**: Tests should only be written to verify the behaviour of **public** methods/functions. Here are some suggestions for what to do in specific cases involving private functions (if this doesn't help for your particular case and you're not sure what to do, please talk to **@BenHenning**):

   * If you’re trying to access hidden information, consider getting that information from one level below instead (e.g. the datastore).
   * If you want to test code within a private method/function, test it by instead calling a public function that makes use of that function, or move it to a utility (if it's general-purpose) where it becomes public. Avoid testing private APIs since that may lead to brittle tests in unexpected situations (such as when the implementation of the API changes but the behaviour remains the same).

4. **For unit tests:**

   * You should test each method of a class individually, with one or more test cases for each method.
   * Define a `setUp()` method in the test if functionality or variables are going to be reused between tests.

5. **For integration tests:**

   Begin by defining the section of code you want to test and considering how it's supposed to behave. Then design test cases to check that it behaves correctly. You should write one test for each test case you design.

### Sharding backend tests

#### How sharding works

We shard the backend tests into many smaller jobs that run in parallel on GitHub Actions. In your PRs, you'll see something like this:

![Display of backend test jobs on a pull request](https://user-images.githubusercontent.com/19878639/109242853-ddd78700-77a9-11eb-9cae-da5cece9ab26.png)

The jobs named like `Run backend tests (ubuntu-18.04, i)` are running the sharded jobs, each with its own number `i`. The last job, `Check combined backend test coverage`, checks that the code coverage is 100%. All these jobs are defined in [`.github/workflows/backend_tests.yml`](https://github.com/oppia/oppia/blob/develop/.github/workflows/backend_tests.yml).

The shards are defined in [`scripts/backend_test_shards.json`](https://github.com/oppia/oppia/blob/develop/scripts/backend_test_shards.json). Here's what the top of that file looks like:

```json
{
    "1": [
        "core.controllers.base_test",
        "core.controllers.collection_editor_test",
```

Each shard is identified by a name, in this case `1`. You could run this shard with `python -m scripts.run_backend_tests --test_shard 1`. The shards are then defined by a list of test modules. For example, the module name for `core/controllers/base_test.py` is `core.controllers.base_test`. Notice that there is no `.py` at the end!

#### Common errors

Whenever you run a shard of backend tests, the `run_backend_tests.py` script checks to make sure the test modules on the filesystem and the modules in the shards file are exactly the same. If a shard has a module that isn't in the filesystem, you'll get a `Modules ... in shards not found` error. This often happens if the module name is incorrect. On the other hand, if there is a module on the filesystem that's not in the shards, you'll get a `Modules ... not in shards` error. This often happens because you forgot to add a new test to the shards.

#### Adding new tests to shards

The point of sharding the backend tests is to speed up test runs on PRs. When the backend tests run in parallel, we spread the tests out across the multiple machines available to us on GitHub Actions. This means it's important for the tests to remain evenly distributed across the shards. To help with that, please **add any new tests to the shard with the shortest runtime.** Further, **make sure that all shards run in under 30 minutes.** If all the shards are taking close to 30 minutes, create a new shard in the JSON file. You can find a shard's runtime from the test runs on your PR:

![Display of backend test jobs on a pull request](https://user-images.githubusercontent.com/19878639/109242853-ddd78700-77a9-11eb-9cae-da5cece9ab26.png)

### Examples

#### Example: Writing unit tests for domain classes

Suppose we have the following domain class:

```python
class ExplorationTheme(object):
  """Domain object representing a theme for an exploration."""

  def __init__(self, exp_id, theme_str):
    """Constructs an ExplorationTheme domain object.

    Args:
      exp_id: str. ID of the exploration.
      theme_str: str. Theme of the exploration.
    """
    self.exp_id = exp_id
    self.theme_str = theme_str

  def to_dict(self):
    return {
      'exp_id': self.exp_id,
      'theme_str': self.theme_str
    }

  def from_dict(cls, exp_theme_dict):
    return cls(
      exp_theme_dict['exp_id'], exp_theme_dict['theme_str'])
```

We can write unit tests for the class like this:

```python
class ExplorationThemeDomainUnitTests(unittest.TestCase):
  """Tests for exploration theme domain class."""

  def setUp(self):
    # Please remember to explicitly call the setUp method with the super class.
    super(ExplorationThemeDomainUnitTests, self).setUp()

    self.exp_theme = exp_domain.ExplorationTheme('exp_id1', 'theme1')

  def test_to_dict(self):
    self.assertEqual(
      self.exp_theme.to_dict(),
      {
        'exp_id': 'exp_id1',
        'theme_str': 'theme1'
      }
    )

  def test_from_dict(self):
    exp_theme_dict = {
      'exp_id': 'exp_id1',
      'theme_str': 'theme1'
    }
    new_exp_theme = exp_domain.ExplorationTheme.from_dict(exp_theme_dict)
    self.assertEqual(new_exp_theme.exp_id, 'exp_id1')
    self.assertEqual(new_exp_theme.theme_str, 'theme1')
```

#### Example: Writing integration tests for handlers (controllers)

Suppose we have the following controller:

```python
class UpdateExplorationVersionHandler(base.BaseHandler):
  """Handler that updates an exploration version."""

  @acl_decorators.can_edit_exploration
  def post(self, exp_id):
    exp_version = self.payload.get('exp_version')
    exploration_instance = exp_models.Exploration.get(exp_id)
    exploration_instance.exp_version = exp_version
    exploration_instance.save()
```

We can write test cases like this:

```python
class UpdateExplorationVersionHandlerTest(test_utils.GenericTestBase):
  """Test for handler that updates the version of an exploration.

  The URL for this handler is: '/explorehandler/update_exp_version/<exploration_id>'
  """

  def setUp(self):
    super(UpdateExplorationVersionHandlerTest, self).setUp()

    self.exp_id = '15'

    self.login(self.VIEWER_EMAIL)
    self.signup(self.VIEWER_EMAIL, self.VIEWER_USERNAME)
    exp_services.load_demo(self.exp_id)

  def test_version_gets_updated_correctly(self):
    exploration = exp_services.get_exploration_by_id(self.exp_id)
    # The exploration is loaded at version 1.
    self.assertEqual(exploration.version, 1)

    self.post_json(
      '/explorehandler/update_exp_version/%s' % (self.exp_id),
      {'exp_version': 123})

    exploration = exp_services.get_exploration_by_id(self.exp_id)
    self.assertEqual(exploration.version, 123)
```
