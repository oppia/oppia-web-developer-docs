## Table of contents

* [How rules work](#how-rules-work)
  * [Rule templates](#rule-templates)
  * [Rule descriptions](#rule-descriptions)
  * [Evaluation functions](#evaluation-functions)
* [Adding a New Rule](#adding-a-new-rule)

This page is an introduction to creating new Oppia rules. An Oppia rule takes a reader's response, normalizes it, and evaluates it against a predicate. A card's interaction will correspond to a set of rules, and the first rule that is triggered by the response determines what Oppia will display to the reader next.

## How rules work

### Rule templates

Rules are listed in [`extensions/interactions/rule_templates.json`](https://github.com/oppia/oppia/blob/develop/extensions/interactions/rule_templates.json), where they are grouped by interaction. For example, here are the rules for the `MathEquationInput` interaction:

```json
{
  ...
  "MathEquationInput": {
    "MatchesExactlyWith": {
      "description": "matches exactly with {{x|MathEquation}} {{y|PositionOfTerms}}"
    },
    "IsEquivalentTo": {
      "description": "is equivalent to {{x|MathEquation}}"
    },
    "ContainsSomeOf": {
      "description": "contains at least one of the terms present in {{x|MathEquation}} {{y|PositionOfTerms}}"
    },
    "OmitsSomeOf": {
      "description": "omits at least one of the terms present in {{x|MathEquation}} {{y|PositionOfTerms}}"
    },
    "MatchesWithGeneralForm": {
      "description": "matches the form of {{x|MathEquation}} with placeholders {{y|SetOfAlgebraicIdentifier}}"
    }
  },
  ...
}
```

### Rule descriptions

Rule descriptions can specify rule inputs with curly braces. For an input `p` of type `Type`, the description would include `{{p|Type}}`. The types are defined as classes in [`extensions/objects/models/objects.py`](https://github.com/oppia/oppia/blob/develop/extensions/objects/models/objects.py), and each class provides a `normalize` method that transforms the input into a canonical form.

### Evaluation functions

Each rule is implemented in the interaction's rules service as a method (evaluation function). In [`extensions/interactions/MathEquationInput/directives/math-equation-input-rules.service.ts`](https://github.com/oppia/oppia/blob/develop/extensions/interactions/MathEquationInput/directives/math-equation-input-rules.service.ts), the `MathEquationInputRulesService` class defines a `MatchesExactlyWith` method, an `IsEquivalentTo` method, and so on. Each method takes exactly two arguments: `answer`, which is the correct answer, and `inputs`, an object with the rule inputs as attributes. For example the `inputs` argument to the `MatchesWithGeneralForm` method of `MathEquationInputRulesService` would have two attributes: `x` and `y`. The types for these inputs are defined in [`extensions/interactions/rule-input-defs.ts`](https://github.com/oppia/oppia/blob/develop/extensions/interactions/rule-input-defs.ts) and [`extensions/interactions/answer-defs.ts`](https://github.com/oppia/oppia/blob/develop/extensions/interactions/answer-defs.ts).

The return value from a rule is always a boolean that describes whether `answer` and `inputs` obey the rule. For example, the `IsEquivalentTo` rule returns whether the user's inputs are equivalent to the creator-configured answer.

For example, suppose we have a rule `IsBetweenInclusive` with the description `is at least {{x|Real}} and at most {{y|Real}}`. Then our evaluation function could be:

```ts
export class MyInteractionRulesService {
  IsBetweenInclusive(
      answer: MyInteractionAnswer,
      inputs: MyInteractionInputs): boolean {
    return inputs.x <= answer <= inputs.y
  }
}
```

Note that the evaluation function must not use any external information, for example the reader's current card. The `inputs` and `answer` must be sufficient to determine whether the rule is satisfied.

## Adding a New Rule

Suppose you have just [[created a new interaction|Creating-Interactions]], say `MyInteraction`, and now you want to define the rules associated with it. To do so, follow these steps:

1. In `extensions/interactions/rule_templates.json`, add a dictionary under the key `MyInteraction`. You can skip this step if you are adding a rule to an existing interaction.
2. For each rule you want to create add an appropriate key that names the rule. The corresponding value should be a dictionary with a single key, `description`, whose value is a string describing the rule. The string should contain rule inputs as substrings of the form `{{inputName|InputType}}`. See the [descriptions section above](#rule-descriptions) for details.
3. Add a corresponding evaluation function to the interaction's rules service, as described in the [evaluation functions section above](#evaluation-functions).
4. Add tests for the evaluation function by creating a `*.spec.ts` file for the rules service. Create a separate test for each rule and check the various corner cases to make sure that rules are defined correctly. You must do this for any new rule that you create so that you can ensure that the rule works properly and returns the correct results on a variety of inputs.

If you would like to contribute a rule to Oppia, please feel free to do so, but we recommend that you talk to us first! This helps ensure that work is not duplicated, and that the added rules are useful for creators and learners. We also welcome suggestions for new rules.
