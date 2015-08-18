# Overview of the Oppia codebase #

Oppia is primarily written as a [Google App Engine](https://developers.google.com/appengine/docs/whatisgoogleappengine) application. The Oppia backend is written in Python, and is connected to a frontend built mostly with [AngularJS](http://angularjs.org/).

## The core ##

Most of the functionality of Oppia is in the core/ directory. This directory is arranged as follows:

<img src='https://raw.githubusercontent.com/oppia/oppia/wiki/images/codebaseOverview.png' width='380'>


<h2>Back-end</h2>

One way to understand what this diagram means is to look at the lifecycle of a typical request. A user makes a request to the Oppia server by performing some action (like clicking a button) that causes some JavaScript code to issue a POST request. This request is made to a particular URL, which main.py matches to a handler in the <code>core/controllers</code> directory.<br>
<br>
Each controller is meant to be a thin layer that understands and validates the request, and then calls methods in <code>core/domain</code> to actually make the computation, change the state of the data on the server, or perform a query. The files in <code>core/domain</code> constitute the core functionality of Oppia and are where most of the logical operations occur.<br>
<br>
In <code>core/domain</code>, there are generally two types of files: those whose names end in <code>_domain.py</code>, and those whose names end in <code>_services.py</code>. The rough dichotomy between these two types of files is as follows: files of the form <code>*_services.py</code> are mostly comprised of functions that act on data, whereas files of the form <code>*_domain.py</code> define transient classes that represent Oppia objects (like explorations, states/cards, and so on). These classes are generally initialized using data from persistent storage, and are then operated on by functions in the <code>*_services.py</code> files.<br>
<br>
Methods in the domain layer often need to access storage, memcache and other services provided by the application framework. All framework-dependent code (such as anything with a dependency on ndb or google.appengine) should go in core/platform. The <a href='https://github.com/oppia/oppia/tree/master/core/platform/models.py'>platforms/models.py</a> class provides an interface to these services and refers to the correct classes based on what the underlying framework is at runtime. All files in the templates, controllers and domain layers are expected to work independently of which framework is used.<br>
<br>
The backend codebase is heavily tested. Tests are generally contained in <code>*_test.py</code> files next to the Python module they test. This naming convention allows them to be automatically detected and compiled into a test suite by Python's <code>unittest</code> module. For more information, see the documentation for tests on the wiki [TODO: add link].<br>
<br>
<br>
<h2>Front-end</h2>

The developer version of the front-end code is contained in <code>core/templates/dev/head</code>. When pushing to a server (Google App Engine) then a <code>core/templates/prod/head</code> directory is also produced that contains minified versions of the code, but this is not generally of concern during development. There are the following sub-directories:<br>
<br>
<ul><li><code>admin</code>: This provides the /admin page which exposes admin controls, for example for adding new moderators.<br>
</li><li><code>components</code>: This provides certain components, mostly for the editor. In particular there are <code>rule_editor.html</code> for the rule editor and <code>visualizations.html</code> for the state graph.<br>
</li><li><code>css</code>: Site-wide css. There are other blocks of css within individual HTML files.<br>
</li><li><code>dashboard</code>
</li><li><code>editor</code>: The editor; this constitutes by far the largest and most complex section of code.<br>
</li><li><code>error</code>: Pages to display when a page cannot be loaded (e.g. due to unauthorised access).<br>
</li><li><code>expressions</code>: Code to parse and evaluate expressions used within an interaction, for example those using parameters.<br>
</li><li><code>forms</code>: Certain standard objects are used in various places throughout the website; for example rich text, lists and dictionaries. Code used to display editors for these objects is collected here.<br>
</li><li><code>galleries</code>
</li><li><code>moderator</code>: The /moderator page provided functionality for moderators.<br>
</li><li><code>pages</code>: Various static pages, for example the site guidelines.<br>
</li><li><code>player</code>
</li><li><code>profile</code>: Used when a new user registers, and to display usernames for logged-in users.<br>
</li><li><code>services</code>: JavaScript handling the embedding of explorations in other websites, user warnings and other matters.</li></ul>


Files generally come in pairs of the form <code>state_editor.html</code> and <code>StateEditor.js</code> in which the latter provides the JavaScript for the former. Within the HTML file sections of the DOM are bound to particular controllers in the JavaScript file. However there are some JavaScript files that cover multiple HTML files, and others that provide general services and so have no HTML file. There are also files of the form <code>StateEditorSpec.js</code> containing <a href='SettingUpTests.md'>karma unit tests</a> for the corresponding js file.<br>
<br>
<h2>Extensions</h2>

Oppia has a number of extension points that allow developers to augment its functionality. For example, developers can create new rules and interactions. All these extension points are located in the <code>extensions/</code> folder.<br>
<br>
There are currently five types of extensions:<br>
<br>
<ul><li>objects. These represent object types that Oppia recognizes, such as NonnegativeInt, UnicodeString and Filepath. In general, they each come with an editor view, a readonly view, and a normalizer which tries to convert a Python object to the given type.<br>
</li><li>rules. These allow learner answers to be classified, so that Oppia can provide appropriate feedback in response.<br>
</li><li>skins. The intention of this directory is to allow different types of skins for the Oppia learner view. <i>It is not fully developed yet.</i>
</li><li>value generators. This is a fancy name for functions which take some inputs and produces a single output. They are used when defining parameter changes: for example, they allow an exploration author to specify an exact value for the parameter, or a range of values, one of which is selected at random.<br>
</li><li>rich-text-editor extensions. These provide additional functionality for content that is shown to the learner, but that does not send any data to the Oppia server. These include videos, images, links, LaTeX math expressions, and others. The extensions are accessed via control buttons in the rich-text editor toolbar.<br>
</li><li>interactions. These allow the learner to submit an answer which is sent to the server and classified. Examples include interactive maps and numeric input. You can make your own, too!</li></ul>


<h2>Other files and folders</h2>

<ul><li><code>feconf.py</code> contains various constants that are referred to by other backend files in the app.<br>
</li><li>The <code>data/explorations</code> folder contains sample explorations that are bundled with the Oppia distribution.<br>
</li><li>The <code>scripts/</code> folder contains several utility scripts that automate processes like starting a development server, running tests, and deploying a copy of Oppia to a production server. More information on how to use these scripts can be found on the documentation pages for deploying Oppia and for running tests (TODO: add link).
