_NB: For details on **running** the backend tests, see https://github.com/oppia/oppia/wiki/Running-Tests#server-side-tests._

Any and all code that you want to get merged into Oppia, needs to be tested extensively before. This guide gives you an idea of how backend integration tests are usually structured.

All classes and tests written below are just examples, and not actual code in the codebase.

# Generating Coverage Reports

This is a a really useful tool while writing backend tests. Coverage reports specify which lines of each file have not been used in any test, and the overall coverage percentage of each file. So, while writing a test for some function or a class, a coverage report can be generated to verify that all lines of the function/class have been included in the tests.

**The ultimate goal is to achieve 100% backend coverage.**

To generate backend coverage, a flag should be added to the command that runs backend tests.

`python -m scripts.run_backend_tests --generate_coverage_report`

The report lists each backend file along with the lines missing coverage in tests.

# Guidelines for writing good tests

1. Tests should use the following general pattern:
   * setup - this is where you prepare any inputs/environment needed for the test.
   * baseline verification - check the values without performing any action.
   * action - perform the action or function call that leads to the expected change.
   * endline verification - check that the values in the baseline verification have changed accordingly.

1. Each test method should only test a single behavior, as that helps both with naming the test, and ensuring that tests don't fail for unrelated changes to the corresponding production code. Test names should follow this format:

    `test_{{action}}_{{withCondition1}}_{{withCondition2}}_{{hasExpectedOutcome}}`

   where `{{action}}`, `{{withCondition}}` and `{{hasExpectedOutcome}}` are replaced with appropriate descriptions in snake_case. Put the outcome at the end of the name, so that you and others can easily compare consecutive tests of the same method that have slightly different conditions with divergent outcomes. Here are some examples of good test names:
   - ``test_get_by_auth_id_with_invalid_auth_method_name_is_none``
   - ``test_get_by_auth_id_for_unregistered_auth_id_is_empty_list``

   These are good test names because it's quickly clear what the differences are between the tests: one is testing an invalid auth versus an unregistered auth. Correspondingly, these conditions lead to different outcomes ('name is none' vs. 'auth ID is empty list').

   In general, when naming a test you should start with a full sentence and only abbreviate if needed to fit within the 80 column character limit. Prefer to not abbreviate, and be careful when abbreviating to avoid important meaning being taken away from the test name.

1. If a function is testing more than one behaviour and you are not able to name the function according to the above pattern, split the test into multiple parts. E.g. if you have a single test that looks like this:
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

1. Keep tests simple. Don't include any logic in the test. If you have to test more than one behavior in a function, write a separate test for each specific behavior (see above).

1. Test the interface and not the implementation. That is, treat the function as a black box and test its functionalities.

1. Try testing multiple contrasting behaviours in order to ensure that the test is correct. E.g. if you are checking that an exception is raised under a certain criterion, also add a test to ensure that the exception is not raised when the criterion is not satisfied.

1. If the function under test depends on some other function, you can use self.swap() to swap the second function with a simple "mock" function whose output you can define.

1. Use:
   * `assertTrue() / assertFalse()` instead of `assertEqual(value, True/False)`
   * `assertIsNone` instead of `assertEqual(value, None)`

1. Test the output of each function as exactly and completely as possible. E.g. it's better to compare equality for an entire dict rather than just checking that a particular value has changed.

1. **Guidelines for testing private methods/functions**: Tests should only be written to verify the behaviour of **public** methods/functions. Private functions should not be used in behavioural tests. Here are some suggestions for what to do in specific cases (if this doesn't help for your particular case and you're not sure what to do, please talk to **@BenHenning**):
   * If you want to test code execution a private method/function, test it through public interface, or move it to a utility (if it's general-purpose) where it becomes public. Avoid testing private APIs since that may lead to brittle test in unexpected situations (such as when the implementation of the API changes, but the behaviour remains the same).
   * If you’re trying to access hidden information, consider getting that information from one level below instead (e.g. datastore).

1. For assertions that check errors (e.g. self.assertRaises or self.assertRaisesRegexp), keep the part of the code enclosed in self.assertRaises as small as possible, so that you can be sure that the error is actually being caused by that part of the code (and not, say, by the setup code).


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
class ExplorationThemeDomainUnitTests(test_utils.GenericTestBase):
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
