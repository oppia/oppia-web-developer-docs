_NB: For details on **running** the backend tests, see https://github.com/oppia/oppia/wiki/Running-Tests#server-side-tests._

All code that you want to merge into Oppia must be supported by a strong set of unit tests. Tests are important because they can help catch bugs, provide an entry-point for newcomers to understand the code, and ensure that your changes won’t get broken by other developers in the long run.

This guide aims to give you an idea of how Oppia’s backend tests are structured. (We also have separate pages for [frontend tests](https://github.com/oppia/oppia/wiki/Frontend-unit-tests-guide) and [end-to-end tests](https://github.com/oppia/oppia/wiki/End-to-End-Tests).)

# Generating Coverage Reports

We use a simple tool, called *code coverage*, to check that all of Oppia’s backend code is fully covered by at least one test. Coverage reports specify which lines of each file have not been used in any test, and the overall coverage percentage of each file. Currently, Oppia has achieved **100% backend coverage**; please help us maintain this going forward!

When writing a test for a function or class, you can generate a coverage report to verify that all the lines of the function/class have been included in the tests. To do this, simply add the `--generate_coverage_report` flag to the `run_backend_tests` command:

        python -m scripts.run_backend_tests --generate_coverage_report

If there are **any** backend test errors, no coverage report will be produced. Please fix those errors and then re-run the above command.

Otherwise, the resulting coverage report lists each backend file, along with the lines in it which are not covered by tests (as in the example below). Use this info to add new tests that cover those lines.

```
Name                                                                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------------------------------------------
appengine_config.py                                                                 23      0   100%
constants.py                                                                        20      0   100%
core/controllers/acl_decorators.py                                                 686      0   100%
core/controllers/admin.py                                                          304      0   100%
core/controllers/base.py                                                           258      0   100%
core/controllers/classifier.py                                                      79      0   100%
core/controllers/classroom.py                                                       39      0   100%
```


**Important note:** Getting to 100% coverage is a necessary, but not sufficient, indicator of the quality of your tests. You'll also need to ensure that your tests are sufficiently robust, and in particular, that your tests are written based on figuring out what **behaviour** you want to check. The following guidelines will help you write better tests that will lead to more maintainable code.

# Guidelines for writing good tests

1. **Each test method should test only a single behaviour.** This helps both with naming the test, and ensuring that the test doesn't fail for unrelated code changes.

   - When naming a test, start by writing a full sentence that clearly describes its behaviour. Try not to abbreviate if possible, but, if you need to do so in order to fit within the 80-character limit, make sure that the resulting test name is still meaningful and easy to understand.

   - We recommend that test names follow the format:

            test_{{action}}_{{withCondition1}}_{{withCondition2}}_{{hasExpectedOutcome}}`

      where `{{action}}`, `{{withCondition}}` and `{{hasExpectedOutcome}}` are replaced with appropriate descriptions in snake_case. Put the outcome at the end, so that it's easy to compare consecutive tests that have slightly different conditions with divergent outcomes. 

   - Here are some examples of good test names:
       - `test_get_by_auth_id_with_invalid_auth_method_name_is_none`
       - `test_get_by_auth_id_for_unregistered_auth_id_is_empty_list`

      These names are good because it's easy to see what the differences between the tests are: one tests an invalid auth, and the other tests an unregistered auth. Correspondingly, these conditions lead to different outcomes ('name is none' vs. 'auth ID is empty list').

2. Tests should use the following general structure:
   * **Setup** - this is where you prepare any inputs/environment needed for the test.
   * **Baseline verification** - check the values without performing any action. This step is only needed if your action is state-changing (i.e., if the same assert statement would lead to one result at baseline, and a different result at endline). Use the same assertion here that you would use at endline.
   * **Action** - perform the action or function call that leads to the expected change.
   * **Endline verification** - check that the values in the baseline verification have changed accordingly.

3. **Test the interface**, not the implementation. That is, treat the function as a black box and test its functionalities. This will help you design a better API from an external user’s perspective.

4. Keep tests **simple**. Don't include any logic in the test. Write the test as a series of straightforward, descriptive and meaningful commands (also known in programming circles as "DAMP"). It's fine if there's some repetition, as long as the tests are easy to read.

5. **Don't use what you don't need.** By default, prefer to inherit from `unittest.TestCase` when writing tests. Only use `test_utils.GenericTestCase` when you need to interact with models or the app itself. This helps keep our tests lean and fast.

   As a general rule, if the only thing your test needs to do is run a function and assert something about its return value, then `unittest.TestCase` is good enough. See https://github.com/oppia/oppia/pull/10869/files for an example of where both kinds of tests were necessary.

6. When building your suite of tests, try to include a range of possible behaviours, such as:
     * "Happy path" cases
     * Boundary/edge cases
     * Failure cases
     * Ambiguous cases

    Also, try testing multiple contrasting behaviours in order to ensure that the test is correct. E.g. if you are checking that an exception is raised under a certain criterion, also add a test to ensure that the exception is not raised when the criterion is not satisfied.

7. For **test outputs**, follow these guidelines:
     * Test each output as exactly and completely as possible. E.g. it's better to compare equality for an entire dict, rather than just checking that a particular value has changed.
     * Use `assertTrue()` / `assertFalse()` instead of `assertEqual(value, True/False)`.
     * Use `assertIsNone` instead of `assertEqual(value, None)`.

8. If you create a new test module (a `*_test.py` file), you will need to add it to a shard in [`oppia/scripts/backend_test_shards.json`](https://github.com/oppia/oppia/blob/develop/scripts/backend_test_shards.json). See the section on shards below.

### Sharded Backend Tests

#### How Sharding Works

We shard the backend tests into many smaller jobs that run in parallel on GitHub Actions. In your PRs, you'll see something like this:

![Display of backend test jobs on a pull request](https://user-images.githubusercontent.com/19878639/109242853-ddd78700-77a9-11eb-9cae-da5cece9ab26.png)

The jobs named like `Run backend tests (ubuntu-18.04, i)` are running the sharded jobs, each with its own number `i`. The last job, `Check combined backend test coverage`. All these jobs are defined in [`.github/workflows/backend_tests.yml`](https://github.com/oppia/oppia/blob/develop/.github/workflows/backend_tests.yml).

The shards are defined in [`scripts/backend_test_shards.json`](https://github.com/oppia/oppia/blob/develop/scripts/backend_test_shards.json). Here's what that top of file looks like:

```json
{
    "1": [
        "core.controllers.base_test",
        "core.controllers.collection_editor_test",
```

Each shard is identified by a name, in this case `1`. You could run this shard with `python -m scripts.run_backend_tests --test_shard 1`. The shards are then defined by a list of test modules. For example, the module name for `core/controllers/base_test.py` is `core.controllers.base_test`. Notice that there is no `.py` at the end!

#### Common Errors

Whenever you run a shard of backend tests, the `run_backend_tests.py` script checks to make sure the test modules on the filesystem and the modules in the shards file are exactly the same. If you add a module to a shard that isn't in the filesystem, you'll get a `Modules ... in shards not found` error. This often happens if the module name is incorrect. On the other hand, if there is a module on the filesystem that's not in the shards, you'll get a `Modules ... not in shards` error. This often happens because you forgot to add a new test to the shards.

#### Adding New Tests to Shards

The point of sharding the backend tests is to speed up test runs on PRs. When the backend tests run in parallel, we spread the tests out across the multiple machines available to us on GitHub Actions. This means it's important for the tests to remain evenly distributed across the shards. To help with that, please **add any new tests to the shard with the shortest runtime.** Further, **make sure that all shards run in under 30 minutes.** If all the shards are taking close to 30 minutes, create a new shard in the JSON file.

## Common testing scenarios

1. If a function tests **more than one behaviour**, split the test into multiple parts. E.g. if you have a single test that looks like this:

     ```
     * Setup
     * Action 1
     * Assertion 1
     * Action 2
     * Assertion 2
     ```

      then split it into two tests as follows:

     ```
     * Setup
     * Action 1
     * Assertion 1

     * Setup + Action 1 (where 'action 1' now represents part of the arrangement)
     * Action 2
     * Assertion 2
     ```

2. If the function under test **depends on some other function**, you can use self.swap() to swap the second function with a simple "mock" function whose output you can define.

3. For assertions that **check errors** (e.g. self.assertRaises or self.assertRaisesRegexp), keep the part of the code enclosed in self.assertRaises as small as possible, so that you can be sure that the error is actually being caused by that part of the code (and not, say, by the setup code).

4. **Guidelines for testing private methods/functions**: Tests should only be written to verify the behaviour of **public** methods/functions. Here are some suggestions for what to do in specific cases involving private functions (if this doesn't help for your particular case and you're not sure what to do, please talk to **@BenHenning**):
   * If you’re trying to access hidden information, consider getting that information from one level below instead (e.g. datastore).
   * If you want to test code within a private method/function, test it by instead calling a public function that makes use of that function, or move it to a utility (if it's general-purpose) where it becomes public. Avoid testing private APIs since that may lead to brittle tests in unexpected situations (such as when the implementation of the API changes, but the behaviour remains the same).


## Example: Writing unit tests for domain classes

Things to keep in mind when writing a unit test:

* For each method defined in the domain class, a separate test function to test the method should be implemented.
* Define a setUp method in the test if functionality and variables are going to be reused between tests.
* If there are multiple possibilities within a method, make sure that all parts of the function are tested in its own test function.

For some Domain class, defined:

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

a test would be written like:

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

## Example: Writing integration tests for handlers (controllers)

Things to keep in mind when writing an integration test:

* After understanding completely what the controller does, cover all the cases with a test of its own.

For some Controller, defined:

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

a test would be written like:

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
    self.post_json(
      '/explorehandler/update_exp_version/%s' % (self.exp_id),
      {'exp_version': 123})
      
    self.exploration = exp_services.get_exploration_by_id(self.exp_id)

    self.assertEqual(exploration.version, 123)
```
