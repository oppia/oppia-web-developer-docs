Oppia uses lots of forms, and it's tiresome to have to write each one from scratch each time. To get around this, we have built a schema-based form framework that allows such forms to be built declaratively. Each schema contains information about:
  * **The type of the form field.** E.g.: should the value being input be text, numeric, or boolean?
  * **Validation.** What additional restrictions need to be placed on the input? E.g.: is between -180 and 180.
  * **UI niceties.** How should the form field be displayed? E.g.: should a placeholder be provided? how wide should the text input field be?

Note that this framework isn't meant to be exhaustive; it is meant to simplify form creation for the more common cases. Custom forms can still be written using the methods referenced in [[Creating Objects|Creating-Objects]].

In the frontend, the `components/forms/` directory contains a form builder which takes a schema and generates a form whose return value satisfies the schema. The schema can be annotated with UI configuration options to tell the form how to display itself. A developer can use the formBuilder or create his/her own custom form; the only requirement is that the return type matches that defined by the schema.

## Schema description

Each schema has a top-level field `type`, which is one of `bool`, `int`, `float`, `unicode`, `list`, `dict`, `html`. The `list` and `dict` types have additional fields in their schemas (see below). In addition to these fields, there are three optional top-level fields:
  * `validators`: a list of validators to apply to the return value, in order. This validation should also be applied automatically in the frontend.
  * `choices`: a list of values of the given type. The value entered must be equal to some element of this list.
  * `ui_config`: a dict of configuration parameters for the UI. See below for more details on this field.

### Additional fields for lists and dicts
For lists, there are two possible additional fields:
  * `items`: required. The schema for an item in the list. Note that polymorphic lists are not allowed at this time.
  * `len`: optional. If present, the length of the list; must be an integer greater than 0. No elements can be added or deleted.

For dicts, there are two possible additional fields:
  * `properties`: required. This is a list whose elements are dicts. The list specifies the order in which the fields for the dict are displayed in the editor view. Each dict has two mandatory keys:
    * `name`: the name of the field
    * `schema`: the schema for the value corresponding to this field.
  * `description`: optional. If present, this gives a human-readable description of the field.

### UI configuration

The 'ui_config' field in a schema is a dict of keys and values. All the keys are optional. The allowed keys, and the circumstances in which they are allowed, are as follows:
  * `rows`: only allowed for type `unicode`; if specified, must be a positive integer. If this value is omitted, the unicode field is displayed as a regular `<input>` field. Otherwise, it is displayed as a textarea with the given number of rows.
  * `placeholder`: only allowed for type `unicode`; if specified, must be a string. It represents the placeholder for the input field.
  * `coding_mode`: only allowed for type `unicode`; if specified, must be either `none` or `python`. If this value is specified, a CodeMirror instance with the appropriate syntax highlighting is used as the input area, and the `rows` and `placeholder` properties above are ignored.
  * `add_element_text`: only allowed for type `list`; if specified, must be a unicode string. If this value is omitted, no changes are made to the 'Add element' button; otherwise, the default 'Add element' text is replaced with the given value.
  * `size`: only allowed for type `html`; if specified, must be either 'small' or 'large'. If 'small', a 2-line RTE is shown; if large, a 10-line RTE is shown.
