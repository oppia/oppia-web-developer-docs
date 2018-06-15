Any and all code that you want to get merged into Oppia, needs to be tested extensively before. This guide gives you an idea of how backend integration tests are usually structured.

All classes and tests written below are just examples, and not actual code in the codebase.

# Writing tests for Domain classes

For some Domain class, defined:

```
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

```
class ExplorationThemeDomainUnitTests(test_utils.GenericTestBase):
  """Tests for exploration theme domain class."""

  def setUp(self):
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


# Writing tests for Handlers(controllers)

For some Controller, defined:

```
class UpdateExplorationVersionHandler(base.BaseHandler):
  """Dummy handler."""

  @acl_decorators.can_edit_exploration
  def post(self, exp_id):
    exp_version = self.payload.get('exp_version')
    exploration_instance = exp_models.Exploration.get(dummy_instance_id)
    exploration_instance.exp_version = exp_version
    exploration_instance.save()
```

a test would be written like:

```
class UpdateExplorationVersionHandlerTest(test_utils.GenericTestBase):
  """Test for dummy handler.

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