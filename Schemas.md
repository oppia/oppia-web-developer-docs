## Introduction

At Oppia, we often want to describe the possible structure of some data. This data could be as simple as the boolean value of a checkbox in a user's preferences, or it could be more complex like the valid arguments to one of our backend API controllers. We use describe these data using _schemas_.

Schemas describe the structure of data in a machine-readable format so that generic utility functions can operate on arbitrary data so long as the data comes with a schema. For example, schemas let us:

* Validate provided data to make sure it conforms to the expected schema.
* Automatically generate forms that let a user provided data in a form specified by a schema.

## Write a schema

A schema is just a dictionary that takes the form described below:

* Required keys:

  * `type`: The type of the data. Must be one of the following types. Unless otherwise stated, the type corresponds to the Python type of the same name.

    * `bool`
    * `int`
    * `float`
    * `basestring`: A type that includes both the `bytes` and `str` types in Python 3. Normalization will _not_ decode the data, even if a `bytes` object is provided.
    * `unicode`: The `str` type in Python 3, which was the `unicode` type in Python 2. This type also accepts a `bytes` object, which will be automatically decoded according to UTF-8 during normalization.
    * `list`
    * `dict`
    * `html`: A string (`bytes` or `str` in Python 3) with HTML code. When normalized, the HTML code will be sanitized by `core.domain.html_cleaner.clean()`. A `bytes` object may also be provided, which will be automatically decoded acording to UTF-8 during normalization.
    * `custom`: A custom object type defined in `extensions/objects/models/objects.py`.
    * `object_dict`: A dictionary that corresponds to a domain object (an object whose class is defined in the domain layer).
    * `unicode_or_none`: Accepts data of type `unicode` or `None`. If the data is not `None`, it is normalized as if it were of type `unicode`.

* Optional keys:

  * `choices`: A list of possible values. The data must exactly match one of the choices.
  * `validators`: A list of dictionaries, each of which has a sole key `id` that maps to the name of a validation function. The validation functions are defined as static methods of `schema_utils._Validators`. To conform to the schema, data must pass all validators.
  * `ui_config`: A dictionary of configuration parameters for how the data should be displayed. Note that this key only applies when the schema data is being displayed as a form. The dictionary may contain any of the following keys:

    * `rows`: Only allowed for type `unicode`. If specified, the value must be a positive integer. If this value is omitted, the unicode field is displayed as a regular `<input>` field. Otherwise, it is displayed as a textarea with the given number of rows.
    * `placeholder`: Only allowed for type `unicode`. If specified, the value must be a string, which will be the placeholder for the input field.
    * `coding_mode`: Only allowed for type `unicode`. If specified, the value must be a string equal to either `none` or `python`. If this value is specified, a CodeMirror instance with the appropriate syntax highlighting is used as the input area, and the `rows` and `placeholder` properties above are ignored.
    * `add_element_text`: Only allowed for type `list`. If specified, the value must be a unicode string. If this value is omitted, no changes are made to the 'Add element' button; otherwise, the default 'Add element' text is replaced with the given value.
    * `size`: Only allowed for type `html`. If specified, the value must be a string equal to either `small` or `large`. If `small`, a 2-line RTE is shown; if `large`, a 10-line RTE is shown.

* Keys for certain types:

  * If the type is `object_dict`, the schema must also include exactly one of the following keys:

    * `object_class`: If this key is provided, the value should be the domain object class. During normalization, the data will be passed to the class's `from_dict` method to construct the object, and then the object's `validate()` class will be called.

    * `validation_method`: If this key is provided, its value should be a function that can validate the provided dictionary. During normalization, the function will be called on the data, and then the data will be returned. Note that any return value from the validation function will be ignored.

  * If the type is `list`, the following keys apply:

    * `len` (optional): The required length of the list. Normalization will fail if the list length differs from the value of this key.
    * `items` (required): A schema that describes each object in the list. Normalization will recursively normalize each of the list elements according to this schema.

  * If the type is `dict`, the following keys apply:

    * `properties` (required): A list of dictionaries. Each dictionary describes a key-value pair in the data and has exactly two keys:

      * `name`: The key in the dictionary that the schema describes.
      * `schema`: A schema describing the associated value.

      For example, suppose we want to describe a dictionary with a single key, `version`, whose value is an integer. We could do so with the following schema:

      ```json
      {
        "type": "dict",
        "properties": [
          {
            "name": "version",
            "schema": {
              "type": "int"
            }
          }
        ]
      }
      ```

      In an editor, the fields for the properties will appear in the same order as they appear in the list.

    * `description` (optional): A human-readable description.

## Uses for schemas in Oppia

### Schema-based forms

Oppia uses lots of forms, and it's tiresome to have to write each one from scratch each time. To get around this, we have built a schema-based form framework that allows such forms to be built declaratively. From each schema, we know the type of the form field, what restrictions we want to impose on user input (from the validators), and how the form should be displayed (from the `ui_config` key).

Note that this framework isn't meant to be exhaustive; it is meant to simplify form creation for the more common cases. Custom forms can still be written using the methods referenced in [[Creating Objects|Creating-Objects]].

In the frontend, the `components/forms/schema-based-editors/` directory contains the `schema-based-editor` component which takes a schema and generates a form whose return value satisfies the schema. The schema can be annotated with UI configuration options to tell the form how to display itself. You can also use FormBuilder to create a custom form; the only requirement is that the return type matches that defined by the schema.

For example, the [`story-node-editor` component](https://github.com/oppia/oppia/blob/develop/core/templates/pages/story-editor-page/editor-tab) includes a schema-based editor with the following HTML:

```html
<schema-based-editor id="storyNodeOutline"
                     schema="OUTLINE_SCHEMA"
                     local-value="editableOutline">
</schema-based-editor>
```

The `OUTLINE_SCHEMA` constant in the component's TypeScript file like this:

```ts
$scope.OUTLINE_SCHEMA = {
  type: 'html',
  ui_config: {
    startupFocusEnabled: false,
    rows: 100
  }
};
```

The result is a form where a user can provide an outline with some basic HTML markup:

![Screenshot of a chapter outline editor](images/schemaBasedEditor.png)
