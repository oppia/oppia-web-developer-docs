# Creating Interactions #

Interactions are included in HTML pages using auto-generated tags like

> `<oppia-interactive-text-input></oppia-interactive-text-input>`

They are implemented using [AngularJS directives](http://seanhess.github.io/2013/10/14/angularjs-directive-design.html), which make it easy to define reusable frontend components. A directive is a piece of JavaScript code that defines the behavior of a custom HTML tag.

In the Oppia codebase, specifications for the different interactions can be found in the `extensions/interactions` directory. Each interaction is made up of four main components:

  * a Python configuration file
  * an AngularJS directive representing the tag's behavior
  * an HTML template representing the contents of the tag
  * an HTML template for rendering the reader's answer.

To add a new interaction to a clone of the Oppia codebase, here is what you need to do:

  1. Let's say that you want to call your interaction `MyInteraction` (in practice, please pick a more descriptive name, like `MusicPhraseInput` or `TextInput`). In the `extensions/interactions` directory, create a new directory called `MyInteraction`.
  1. In the first level of the `MyInteraction` directory, create the following files: `MyInteraction.py`, `MyInteraction.js` and `MyInteraction.html`. We now consider what each file should contain.
  1. The `MyInteraction.py` file provides information including the customization options for the interaction, and the input types associated with the various answer handlers. Edit the fields to reflect the various attributes for your interaction. It is probably easiest to base this file on the corresponding `*.py` file from another interaction.
    * The `display_mode` field can take one of two values: `DISPLAY_MODE_INLINE` or `DISPLAY_MODE_SUPPLEMENTAL`. The former case corresponds to interactions like text, multiple choice and so on which can be considered transient in the context of a student/tutor conversation. The latter case corresponds to interactions that are akin to the tutor bringing a new artifact (like a map, or a programming console) into the conversation, and, in this case, the interaction will retain knowledge of previous answers to the same question. (For example, the learner's previous clicks will be shown on the interactive map.)
    * The `_customization_arg_specs` argument should be an array specifying the options that the exploration creator using this interaction is able to set. For each option, a dict with the following keys should be provided:
      * `name`: This is the identifier that is used in the `MyInteraction.js` file to refer to the customization option.
      * `description`: This is the identifier shown to an exploration creator when they edit the interaction options in the exploration editor.
      * `schema`: This defines the type of the customization option, as well as appropriate validators and UI configuration options. See [SchemaBasedFormsDesignDoc](SchemaBasedFormsDesignDoc.md) for more information about how to define schemas.
      * `default_value`: This provides a default initial/fallback value for the customization option.
    * `answer_type`: The type of object that the reader's answer should be represented as. This should be the name of one of the classes in `extensions/objects/models/objects`. When the reader submits an answer, the answer will be passed to the server and then through the object's `normalize` function. You may need to [write new objects](CreatingObjects.md) to support your interaction. This object also determines which [rules](CreatingRules.md) are available to classify answers submitted using this interaction.
    * The `_dependency_ids` arguments should contain an array of strings, each of which is the name of a [dependency](CreatingDependencies.md). These dependencies allow you to specify code, typically from external websites, that you want to be available to your interaction as it runs or is edited. If the interaction you are implementing has a significant JavaScript component, we suggest packaging as much of the core functionality as possible into third-party JavaScript libraries that are also usable outside of Oppia, and writing a small directive that makes use of the imported JavaScript library. For an example of how to do this, see the [World Map interaction](https://github.com/oppia/oppia/tree/master/extensions/interactions/InteractiveMap/InteractiveMap.js).
  1. The `MyInteraction.js` file contains two directives that define the behaviour of your interaction. One of these is the view that is presented to the learner to interact with, and the other (the 'response') is the view that is shown to the learner after the interaction has taken place. Please take a look at the `*.js` files for other interactions, and/or the [AngularJS directive documentation](http://docs.angularjs.org/guide/directive), for information on how to construct a directive. In particular you will need to change the following:
    * The first argument of oppia.directive should become `oppiaInteractiveMyInteraction` or `oppiaResponseMyInteraction`, respectively.
    * The value of the `templateUrl` key should become `interaction/MyInteraction` and `response/MyInteraction`, respectively.
    * The body of `function($scope, $attrs)` should contain the JavaScript the interaction will use to run. If you have defined parameters in the python file, say with name `myParameter`, then you can reference them by `$attrs.myParameterWithValue`. (The 'WithValue' part is a legacy holdover.) Note that the parameters in $attrs are JSON-stringified, so you will need to use `oppiaHtmlEscaper.escapedJsonToObj()` to convert them back. (Do not use `JSON.parse()`, since it does not handle the necessary escaping.)
  1. The `MyInteraction.html` file contains the two templates used to display the interaction's HTML, each of which is bound to the directives in `MyInteraction.js`. Please use <[...]> angular notation instead of {{...}} in this file. In the response template, you can refer to the learner's answer -- see e.g. the `NumericInput` code for details.
  1. (optional) You can also add a `stats_response.html` that will determine how user's submissions will be shown to the editor in the statistics. If this is omitted then just `{{answer}}` will be used.
  1. Activate your interaction in Oppia by editing the `ALLOWED_INTERACTIONS` variable in `feconf.py`. You will need to specify its name and the location of its directory.
  1. And you're done! Your interaction should now be available in the interaction repository, and can be used in explorations.

Note that, in the JS directive, you will probably want to post an answer to the server at some point. The current way to do this is to call
```
    $scope.$parent.$parent.submitAnswer(answer, handler);
```
where `answer` is a variable containing the reader's answer, and `handler` is a variable containing the event type. (Currently, it can only be `'submit'`, but we may expand it later to include other types of events, such as `'click'`, `'drag'`, etc.)

### Testing ###

We have an [integration testing framework](SettingUpTests.md) using Protractor.js that you you are encouraged to use for your interaction. The tests mimic a user by interacting with the web-page, for example by clicking and typing, and then checking that the interaction behaves in the expected way.

To do so will require the following:
  1. Add your interaction to the dictionary of interactions in `extensions/interactions/protractor.js`.
  1. Create a `protractor.js` file in your interaction's directory and implement the following:
    * `customizeInteraction`: a function that when sent relevant arguments will choose parameters for your interaction.
    * `expectInteractionDetailsToMatch`: a function that in the player verifies the interaction is displayed correctly, including those customizations specified in the editor.
    * `submitAnswer`: a function that simulates the user submitting an answer to an interaction, for example for a numeric interaction submitting a number.
    * `submissionHandler`: The type of the returned object of the interaction; this should match the `obj_type` of the submission handler specified in the interaction's python file.
    * `testSuite`: An array of dictionaries, each of which describes a scenario in which the interaction is used and specifies how it should behave. Each entry specifies customizations for the interaction and selects and parameterizes one of the rules associated with it. The test will then move to the player, check that the interaction is displayed correctly, submit a series of correct and wrong answers, and verify that these are handled correctly.
  1. Any new [objects](CreatingObjects.md) you create must have handlers for them added to `extensions/objects/protractor.js`. You can then use these handlers when writing your `customizeInteraction` and `submitAnswer` functions. Objects that are used as rule parameters must implement a `setValue()` function that fully specifies them, and this will be used automatically when a rule is being selected. Don't forget to add the new objects both to the list of object editors and to the exports.
  1. Any new [rules](CreatingRules.md) must be included in `extensions/rules/protractor.js` within the entry for the type of returned object the rule applies to. You just need to specify the `description` from the rule's python file.
  1. When running the tests you may want to change `describe` to `ddescribe` in the "Interactions" test class of `core/tests/protractor/editorAndPlayer.js` which will cause just the interaction-specific tests to be run. Be sure to change it back before committing!
