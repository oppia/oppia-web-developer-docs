# Creating New Objects #

This page explains how to create new types of objects that a user's submission to an interaction might be converted into, or that could be used as a parameter in a rule. You will typically want to create such objects when [creating a new interaction](CreatingInteractiveWidgets.md). Each object that some interaction submits should have [rules](CreatingRules.md) associated with it that an exploration creator can select from to determine which card the user will proceed to next.

Let's suppose you're creating a new object called `MyObject` (in practice you should use a more descriptive name).
  1. In `extensions/objects/models/objects.py` create a new object, with either `BaseObject` or one of the other existing objects as its superobject. The class should have the following attributes:
    * `description`: A string describing the object.
    * (optional) `edit_html_filename`: The name of the file in (3) below, if it exists.
    * (optional) `edit_js_filename`: The name of the file in (4) below, if it exists.
    * `normalize`: A function that is given an instance of the object in question and is responsible for validating and normalizing it. The supplied instance is a native Python object.
  1. In `extensions/objects/models/objects_test.py` add new tests to the `ObjectNormalizationUnitTests` class; these will be run automatically with the other tests.
  1. (optional) In `extensions/objects/templates` add a file `my_object_editor.html` specifying an interface in which objects of this type can be submitted. This is only necessary if editors will be entering parameters that use this object type.
  1. (optional) In `extensions/objects/templates`, create `myObjectEditor.js`, the JavaScript directive associated with `my_object_editor.html`. You should base this (and the HTML file) on one of the pre-existing ones.