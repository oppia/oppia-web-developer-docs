This page is an introduction to creating new Oppia rules. An Oppia rule takes a reader's response, normalizes it, and evaluates it against a predicate. A card's interaction will correspond to a set of rules, and the first rule that is triggered by the response determines what Oppia will display to the reader next.

## Where To Look ##

Rules are categorized by the type of input they evaluate. For example, a SetRule that tests for equality with an existing set would expect to be given a set as its input.

All the rule definitions can be found in the extensions/interaction/rules.json file of the Oppia source tree. This file contains a bunch of JSON dictionaries; each of these dictionaries contains all the rules that are used to evaluate inputs whose type is `INPUT_TYPE`. Each rule is represented by a single key-value pair inside the dictionary corresponding to that particular `INPUT_TYPE`.

(Note, also, that each of the different object types used in Oppia has a class in `extensions/objects/models/objects.py` which provides a `normalize()` function to convert it to its canonical form.)

## Adding a New Rule ##

If you have just [created a new interaction](Creating-Interactions), say `MyInteraction` and now want to define the rules associated with it:
  1. In [extensions/interactions/rules.json](https://github.com/oppia/oppia/blob/develop/extensions/interactions/rules.json) add a `MyInteraction` dictionary.
  2. For each rule you want to create add an appropriate key (this is the “rule name”). The corresponding value should contain a single key, `description`, whose value is described in the Rule Description section.
  3. Add a corresponding evaluation function, as described in the [Evaluation Function](#evaluation-function) section.
  4. Add tests for the evaluation function, as described in the [Adding Tests](#adding-tests) section.

Note that, if you simply want to add a new rule for a pre-existing interaction, say `MyInteraction`, then you only need to add a new key to the existing dictionary as in (2).

### Rule Description ###

Here is an example of a rule description:

```
   is between {{a|NonnegativeInt}} and {{b|Real}}
```

This means that, when the rule is first created, it expects to be given a non-negative integer, `a`, and a real number, `b`. This all happens before any input is passed to the rule to be evaluated.

### Evaluation Function ###

You will need to define a factory service called `myInteractionRulesService` (in `MyInteraction.js`) that contains functions to evaluate rules and returns a Boolean value (`True` if the rule is satisfied, `False` otherwise). Note that the name of the function must be the same as the key used in step 2 of [Adding a New Rule](#adding-a-new-rule) section.

This function has access to `answer`, as well as any parameters defined in the rule description string. In the previous example, the parameters `a` and `b` can be accessed using `inputs.a` and `inputs.b`. Here is an example of what the corresponding evaluation function might look like:

```
    ruleName: function(answer, inputs) {
        return inputs.a <= answer <= inputs.b
    }
```

The evaluation function may not use any other external parameters (such as the reader's current card, and so on) to compute its result; everything must be passed in through the subject or be defined when the rule is first initialized.

## Adding Tests ##

You will need to create a `MyInteractionRulesServiceSpec.js` file containing tests for rules defined in the `myInteractionRulesService` factory service. Create a separate test for each rule and check the various corner cases to make sure that rules are defined correctly. You are strongly encouraged to do this for any new rule that you create, so that you can ensure that the rule works properly and returns the correct results on a variety of inputs.

## Contributing New Rules ##

If you would like to contribute a rule to Oppia, please feel free to do so, but we recommend that you talk to us first! This helps ensure that work is not duplicated, and that the added rules are useful for creators and learners. We also welcome suggestions for new rules.
