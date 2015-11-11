Interactions provide a way for learners to submit answers to Oppia. They are implemented using custom HTML tags built with [AngularJS directives](http://seanhess.github.io/2013/10/14/angularjs-directive-design.html). Here's an example of such a tag:

```
  <oppia-interactive-text-input></oppia-interactive-text-input>
```

In the Oppia codebase, interactions live in the `extensions/interactions` directory. Each interaction is made up of four main components:

  * a Python configuration file
  * an AngularJS directive representing the tag's behavior
  * an HTML template representing the contents of the tag
  * an HTML template for rendering the learner's answer.

To add a new interaction to Oppia, here is what you need to do:

  1. Pick a descriptive id for your interaction, like `MusicPhraseInput`. For these instructions, we'll assume that the id of your interaction is `MyInteraction`.
  1. In the `extensions/interactions` directory, create a new directory called `MyInteraction`. In that directory, create the files `MyInteraction.py`, `MyInteraction.js` and `MyInteraction.html`.

Here's what each file should contain:

  1. `MyInteraction.py` provides various attributes for your interaction. These are documented in `extensions/interactions/base.py`.
    * The `display_mode` field can take one of two values:
      * `DISPLAY_MODE_INLINE` corresponds to interactions, like text and multiple choice, that are part of the learner/tutor conversation.
      * `DISPLAY_MODE_SUPPLEMENTAL` corresponds to interactions that correspond to the tutor bringing a new artifact (like a map, or a programming console) into the conversation.
    * The `_customization_arg_specs` field should be an array specifying the options that the exploration creator can set. For each option, a dict with the following keys should be provided:
      * `name`: the identifier that `MyInteraction.js` uses to refer to the customization option.
      * `description`: the description shown to an exploration creator in the interaction editor.
      * `schema`: a [[schema|Schema-Based-Forms]] that defines the customization option's type, as well as appropriate validators and UI configuration options.
      * `default_value`: a default initial/fallback value for the customization option.
    * `answer_type` is the type of object that the learner's answer should be represented as. This should be the name of one of the classes in `extensions/objects/models/objects`. When the learner submits an answer, the answer will be passed to the server and then through the object's `normalize` function. You may need to [[write new objects|Creating-Objects]] to support your interaction. This object also determines which [[rules|Creating-Rules]] are available to classify answers submitted using this interaction.
    * `_dependency_ids` argument should contain a list of strings, each of which is the name of a [[dependency|Creating-Dependencies]]. These allow you to specify code that you want to be available to your interaction as it runs or is edited. If the interaction you are implementing has a significant JavaScript component, we suggest packaging as much of the core functionality as possible into third-party JavaScript libraries that are also usable outside of Oppia, and writing a small directive that makes use of the imported JavaScript library. For an example of how to do this, see the [World Map interaction](https://github.com/oppia/oppia/tree/master/extensions/interactions/InteractiveMap/InteractiveMap.js).
  1. `MyInteraction.js` contains two directives that define the behaviour of your interaction. One of these is the view that is presented to the learner to interact with, and the other (the 'response') is the view that is shown to the learner after the interaction has taken place. Please take a look at the `*.js` files for other interactions, and/or the [AngularJS directive documentation](http://docs.angularjs.org/guide/directive), for information on how to construct a directive. In particular you will need to change the following:
    * The first argument of oppia.directive should become `oppiaInteractiveMyInteraction` or `oppiaResponseMyInteraction`, respectively.
    * The value of the `templateUrl` key should become `interaction/MyInteraction` and `response/MyInteraction`, respectively.
    * The body of `function($scope, $attrs)` should contain the JavaScript the interaction will use to run. If you have defined parameters in the python file, say with name `myParameter`, then you can reference them by `$attrs.myParameterWithValue`. (The 'WithValue' part is a legacy holdover.) Note that the parameters in $attrs are JSON-stringified, so you will need to use `oppiaHtmlEscaper.escapedJsonToObj()` to convert them back. (Do not use `JSON.parse()`, since it does not handle the necessary escaping.)
    * To post an answer to the server, call

      ```
        $scope.$parent.$parent.submitAnswer(answer);
      ```

      where `answer` is a variable containing the learner's answer.
  1. `MyInteraction.html` contains the two templates used to display the interaction's HTML, each of which is bound to the directives in `MyInteraction.js`. In the response template, you can refer to the learner's answer -- see e.g. the `NumericInput` code for details.
  1. (optional) `stats_response.html` determines how users' submissions are shown to the exploration author in the statistics. If this is omitted, the raw answer will be used.

Once you've created these files, activate your interaction in Oppia by editing the `ALLOWED_INTERACTIONS` variable in `feconf.py` (you'll need to specify its name and the location of its directory). Your interaction should then be available in the interaction repository, and can be used in explorations.

### Testing ###

We have an [[end-to-end testing framework|Writing-End-to-End-Tests]] using Protractor.js that you you are encouraged to use for your interaction. The tests mimic a user by interacting with the web-page, for example by clicking and typing, and then checking that the interaction behaves in the expected way.

To do so will require the following:
  1. Add your interaction to the dictionary of interactions in `extensions/interactions/protractor.js`.
  1. Create a `protractor.js` file in your interaction's directory and implement the following:
    * `customizeInteraction`: a function that when sent relevant arguments will choose parameters for your interaction.
    * `expectInteractionDetailsToMatch`: a function that in the player verifies the interaction is displayed correctly, including those customizations specified in the editor.
    * `submitAnswer`: a function that simulates the user submitting an answer to an interaction, for example for a numeric interaction submitting a number.
    * `submissionHandler`: The type of the returned object of the interaction; this should match the `obj_type` of the submission handler specified in the interaction's python file.
    * `testSuite`: An array of dictionaries, each of which describes a scenario in which the interaction is used and specifies how it should behave. Each entry specifies customizations for the interaction and selects and parameterizes one of the rules associated with it. The test will then move to the player, check that the interaction is displayed correctly, submit a series of correct and wrong answers, and verify that these are handled correctly.
  1. Any new [[objects|Creating-Objects]] you create must have handlers for them added to `extensions/objects/protractor.js`. You can then use these handlers when writing your `customizeInteraction` and `submitAnswer` functions. Objects that are used as rule parameters must implement a `setValue()` function that fully specifies them, and this will be used automatically when a rule is being selected. Don't forget to add the new objects both to the list of object editors and to the exports.
  1. Any new [[rules|Creating-Rules]] must be included in `extensions/rules/protractor.js` within the entry for the type of returned object the rule applies to. You just need to specify the `description` from the rule's python file.
  1. When running the tests you may want to change `describe` to `ddescribe` in the "Interactions" test class of `core/tests/protractor/editorAndPlayer.js` which will cause just the interaction-specific tests to be run. Be sure to change it back before committing!
