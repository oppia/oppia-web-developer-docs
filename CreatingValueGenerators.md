# Creating New Value Generators #

Parameters that are included within an exploration (both at the exploration level and the interactive widget level) must each specify both a value generator and an [object type](CreatingObjects.md). The object type specifies the type of the parameter, while the value generator is responsible (via its `generate_value` function) for providing an object of the given type when the widget runs. For example, it might simply return a copy of an object given to it (`Copier`), or it might randomly select an object from a given list (`RandomSelector`).

Let's suppose you want to create a new value generator called `MyValueGenerator` (though in practice you should use a more descriptive name).
  1. In `extensions/value_generators/models/generators.py` add a class `MyValueGenerator` that derives from `value_generators_domain.BaseValueGenerator`. It should contain a `generate_value` function that takes the `customization_args` provided by the widget for the parameter in question, and returns an object of the type the widget specifies for this parameter.
  1. In `extensions/value\_generators/models/generators\_test.py add tests for your class.
  1. In `extensions/value_generators/templates/`, add a file `my_value_generator.html` that will be used to display the form for editing parameters. The html from the relevant object's template will have been automatically compiled into a `object-editor` html tag which you should use here.
  1. Add a companion `MyValueGenerator.js` javascript file.

### References ###

[Value generators design document](ParametersDesignDoc.md)