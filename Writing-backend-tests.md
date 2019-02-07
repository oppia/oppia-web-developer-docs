_NB: For details on **running** the backend tests, see https://github.com/oppia/oppia/wiki/Running-Tests#server-side-tests._

Any and all code that you want to get merged into Oppia, needs to be tested extensively before. This guide gives you an idea of how backend integration tests are usually structured.

All classes and tests written below are just examples, and not actual code in the codebase.

# Generating Coverage Reports

This is a a really useful tool while writing backend tests. Coverage reports specify which lines of each file have not been used in any test, and the overall coverage percentage of each file. So, while writing a test for some function or a class, a coverage report can be generated to verify that all lines of the function/class have been included in the tests.

**The ultimate goal is to achieve 100% backend coverage.**

To generate backend coverage, a flag should be added to the command that runs backend tests.

`bash scripts/run_backend_tests.sh --generate_coverage_report`

The report lists each backend file along with the lines missing coverage in tests.

# Writing tests for Domain classes - Unit tests

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


# Writing tests for Handlers(controllers) - Integration tests

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

### Some general guidelines for writing good tests:
1. You should test the interface and not the implementation. That is, treat the function as a black box and test its functionalities.
2. Keep the tests simple. Don't put any logic in the test. If you have to test more than one thing in a function, use separate test for each of them.
3. Try testing multiple contrasting behaviours as it helps strengthen that the test is correct.
For instance: if you are checking that an exception is raised under a certain criteria, also add a test to ensure that the exception is not raised when the criteria is not fulfiled.
4. Each method only tests a single behavior, as that helps both with naming the test, and ensuring tests don't fail for unrelated changes to the corresponding production code. Beyond that, consider using the following format when naming tests: 
    `test_action_withCondition_withAnotherCondition_hasExpectedOutcome`

   * Try following the same consistent style for naming all the functions.
   * Split functions into multiple parts if they are testing more than one behaviour and you are not able to name the function according to the above pattern. For instance:

     Instead of a single test of following format:
     ```
     * Arrange
     * Act 1
     * Assert 1
     * Act 2
     * Assert 2
     ```
     Split into two test as follows:
     ```
     * Arrange
     * Act 1
     * Assert 1
     * Arrange + Act 1 (where 'act 1' now represents part of the arrangement)
     * Act 2
     * Assert 2
     ```
   * Put the outcome at the end of the name as it can help easily compare consecutive tests of the same method that have slightly different conditions to indicate the variety of potential outcomes.
5. If some part of function depends on some other function to make decision, use self.swap() to swap that function with a simple function whose output you can define.
6. Tests should follow a general pattern:
   * setup() - this is where you build inputs/ environment required by function.
   * test baseline case - check the values without performing any action.
   * do the action that leads to a change.
   * test the end line case - check whether the value has changed correctly.
7. Test the function as exactly and completely as possible. Eg - if you need to check the change in a key in the dict, compare for the equality of whole dict.
8. **Guidelines for testing private methods/functions**: Tests should never refer to private methods/functions in all cases. All tests should happen through the public interface. Here are some suggestions for what to do in specific cases (if this doesn't help for your particular case and you're not sure what to do, please talk to **@BenHenning**):
   * If you want to test code execution a private method/function, test it through public interface, or move it to a utility (if it's general-purpose) where it becomes public. Avoid testing private API since that may lead to brittle test in unexpected situations (such as when the implementation of API changes but the behaviour remains same).
   * If you’re trying to access hidden information, consider getting that information from one level below instead (e.g. datastore).
9. Use:
   * `assertTrue() / assertFalse()` instead of `assertEqual(value, True/False)`
   * `assertIsNone` instead of `assertEqual(value, None)`
10. For assertion errors, try using regex to remove the part of the error message that relies on some specific variable (like a name relying on any id or key). This will prevent the test from breaking when the naming strategy is changed.


    