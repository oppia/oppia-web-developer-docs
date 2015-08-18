# Creating New Rules #

This page is an introduction to creating new Oppia rules. An Oppia rule takes a reader's response, normalizes it, and evaluates it against a predicate. A card's interaction will correspond to a set of rules, and the first rule that is triggered by the response determines what Oppia will display to the reader next.

## Where To Look ##

Rules are categorized by the type of input they evaluate. For example, a SetRule that tests for equality with an existing set would expect to be given a set as its input.

All the rule definitions can be found in the extensions/rules directory of the Oppia source tree. In this directory, there are a bunch of Python files of the form `[INPUT_TYPE].py`; each of these files contains all the rules that are used to evaluate inputs whose type is `INPUT_TYPE`. Each rule is represented by a single Python class.

In addition, the directory also contains files of the form `[INPUT_TYPE]_test.py`; these files contain tests for the rules. These tests are run as part of the standard test suite:
`bash scripts/test.sh`

(Note, also, that each of the different object types used in Oppia has a class in `extensions/objects/models/objects.py` which provides a `normalize()` function to convert it to its canonical form.)

## Adding a New Rule ##

If you have just [created a new object](CreatingObjects.md), say `MyObject` and now want to define the rules associated with it:
  1. In `extensions/rules/base.py` add a `MyObjectRule` class, and give its `subject_type` as `objects.MyObject`.
  1. In `extensions/rules` create `my_object.py`, and for each rule you want to create add an appropriate class, deriving it from `base.MyObject`. This class should contain the following entries, which are described in more detail below:
    * `description`
    * `is_generic`: This specifies whether the rule will accept a wide range of different input, and helps determine how user statistics are shown to the exploration creator. For example a rule checking for equality with a given string would not be generic, but one checking if the answer contains a given string might be.
    * `_evaluate`
    * (optional) `_validate_params`
  1. Create `extensions/rules/my_object_test.py` containing tests of the classes just defined. You are strongly encouraged to do this for any new rule that you create, so that you can ensure that the rule works properly and returns the correct results on a variety of inputs.

If you simply want to add a new rule for a pre-existing object, say `MyObject`, then you only need to add a new class within `MyObject.py` as in (2), and associated tests as in (3).

### Rule Description ###

Here is an example of a rule description:

```
   is between {{a|NonnegativeInt}} and {{b|Real}}
```

This means that, when the rule is first created, it expects to be given a non-negative integer, `a`, and a real number, `b`. This all happens before any input is passed to the rule to be evaluated. If you which your parameters to be of a specialised type you can [create](CreatingObjects.md) it.

You will need to write such a description for your rule, following the syntax above.

This rule will create new attributes in the Rule class corresponding to the parameter names. In this case, the attributes `a` and `b` will be created. These can be used in the evaluation function, which we turn to next.

### Evaluation Function ###

You will need to define a function called `_evaluate(self, subject)` that evaluates the subject and returns a Boolean value (True if the rule is satisfied, False otherwise). Note the underscore at the beginning of the function name; this must be preserved.

This function has access to `subject`, as well as any parameters defined in the rule description string. In the previous example, the parameters `a` and `b` can be accessed using `self.a` and `self.b`. Here is an example of what the corresponding evaluation function might look like:

```
    def _evaluate(self, subject):
        return self.a <= subject <= self.b
```

The evaluation function may not use any other external parameters (such as the reader's current card, and so on) to compute its result; everything must be passed in through the subject or be defined when the rule is first initialized.

### Parameter-Checking Function ###

Optionally, you may want run checks on the parameters when the rule is initialized. This can be done by writing a function `_validate_params(self)`; as before, the function has access to the parameters used to define the rule. The function should raise an Exception if these parameters are invalid.

**TODO**: These exceptions should be shown to the exploration creator.

If the function is not present, no checks will be carried out (except for ensuring that the parameters are of the correct type).

## Contributing to Oppia ##

If you would like to contribute a rule to Oppia, please feel free to do so, but we recommend that you talk to us first! This helps ensure that work is not duplicated, and that the added rules are as useful as they can be. We also actively welcome suggestions for new rules.