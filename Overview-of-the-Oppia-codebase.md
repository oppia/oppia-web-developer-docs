Oppia is built with [Google App Engine](https://developers.google.com/appengine/docs/whatisgoogleappengine). Its backend is written in Python, and its frontend is written using [AngularJS](http://angularjs.org/).

## The core

Most of Oppia's functionality is in the `core/` directory, which is arranged as follows:

  ![Schematic diagram showing the layout of the codebase.](images/codebaseOverview.png)

### Backend

One way to understand what this diagram means is to look at the lifecycle of a typical request. A user makes a request to the Oppia server by performing some action (like clicking a button) that causes some JavaScript code to issue a POST request. This request is made to a particular URL, which `main.py` matches to a handler in the `core/controllers` directory.

Each controller is meant to be a thin layer that understands and validates the request, and then calls methods in `core/domain` to actually perform the computation/query, or change the state of the data on the server. The files in `core/domain` constitute the core functionality of Oppia and are where most of the logical operations occur.

In `core/domain`, there are generally two types of files: those whose names end in `_domain.py`, and those whose names end in `_services.py`. Files of the form `*_services.py` are mostly comprised of functions that act on data. On the other hand, files of the form `*_domain.py` define transient classes that represent Oppia objects (like explorations, states/cards, and so on); these classes are generally initialized using data from persistent storage, and are then operated on by functions in the `*_services.py` files.

Methods in the domain layer often need to access storage, memcache and other services provided by the application framework. All framework-dependent code (such as anything with a dependency on ndb or google.appengine) should go in core/platform. The [platforms/models.py](https://github.com/oppia/oppia/tree/master/core/platform/models.py) class provides an interface to these services, and refers to the correct classes based on what the underlying framework is at runtime. All files in the templates, controllers and domain layers should be independent of the underlying framework.

The backend codebase is heavily tested. Tests are contained in `*_test.py` files next to the Python module they test. This naming convention allows them to be automatically detected and compiled into a test suite by Python's `unittest` module. For more information, see [[Running Tests|Running-Tests]].

### Frontend

The developer version of the frontend code is contained in `core/templates/dev/head`. (When Oppia is deployed, a `core/templates/prod/head` directory is also produced that contains minified versions of the code, but this is not generally of concern during development.) The frontend code contains the following sub-directories:

  * `admin`: This provides the /admin page which exposes admin controls, e.g. for adding new moderators.
  * `components`: This provides certain components, mostly for the editor. In particular there are `rule_editor.html` for the rule editor and `visualizations.html` for the state graph.
  * `css`: Site-wide CSS. There may be other CSS blocks within individual HTML files.
  * `dashboard`: The per-user notifications dashboard.
  * `editor`: The editor; this constitutes by far the largest and most complex section of code.
  * `error`: Pages to display when a page cannot be loaded (e.g. due to unauthorised access).
  * `expressions`: Code to parse and evaluate expressions (which may use parameters).
  * `forms`: Certain standard objects are used in various places throughout the website, such as rich text, lists and dictionaries. Code used to display editors for these objects is collected here.
  * `galleries`: The gallery page that allows users to browse explorations.
  * `moderator`: The /moderator page that provides functionality for moderators.
  * `pages`: Various static pages, such as the site guidelines.
  * `player`: Services for the learner view. (The actual learner view templates are in `extensions/skins`.)
  * `profile`: Used when a new user registers, and to display usernames for logged-in users.
  * `services`: JavaScript handling the embedding of explorations in other websites, user warnings and other matters.

Files generally come in triples of the form `state_editor.html`, `StateEditor.js` and `StateEditorSpec.js`. The spec file contains [[Karma unit tests|Running-Tests]] for the JavaScript file.

In general, within the HTML file, sections of the DOM are bound to particular JavaScript controllers. However, some JavaScript files cover multiple HTML files, and others provide general services and so have no HTML file.

## Extensions

Oppia has a number of extension points that allow developers to augment its functionality, all of which are located in the `extensions/` folder.

There are several different types of extensions:
  * **Objects** represent object types that Oppia recognizes, such as NonnegativeInt, UnicodeString and Filepath. In general, they each come with an editor view, a readonly view, and a normalizer which tries to convert a Python object to the given type.
  * **Rules** allow learner answers to be classified, so that Oppia can provide appropriate feedback in response.
  * **Skins** provide different user interfaces for the Oppia learner view.
  * **Value generators** are essentially functions which take some inputs and produce a single output. They are used when defining parameter changes: for example, they allow an exploration author to specify an exact value for the parameter, or a range of values, one of which is selected at random.
  * **Rich-text-editor extensions** provide additional functionality for content that is shown to the learner. They are accessed via control buttons in the rich-text editor toolbar, and include things like videos, images, links and LaTeX math expressions.
  * **Interactions**, such as interactive maps and numeric input, allow the learner to submit an answer, which is then sent to the server for Oppia to respond to.


## Other files and folders

  * `feconf.py` contains various constants that are referred to by other backend files in the app.
  * The `data/explorations` folder contains sample explorations that are bundled with the Oppia distribution.
  * The `scripts/` folder contains several utility scripts that automate processes like starting a development server, running tests, and deploying a copy of Oppia to a production server.


***

*TODO:* in the boxes in the diagram, consider giving a concrete example of a controller, domain model, etc. and walk up and down through the stack, maybe pointing to code examples. (This may be useful for new contributors who are not familiar with the codebase.)
