## Table of contents

* [Introduction](#introduction)
* [Using the rich text editor](#using-the-rich-text-editor)
* [Adding rich text components](#adding-rich-text-components)
  * [Component code](#component-code)
  * [Component registration in `rich_text_components_definitions.ts`](#component-registration-in-rich_text_components_definitionsts)
    * [`customization_arg_specs`](#customization_arg_specs)
    * [Example registration](#example-registration)
* [Implementation](#implementation)
  * [Third-Party Libraries](#third-party-libraries)
    * [Upgrading CKEditor](#upgrading-ckeditor)
  * [RTE implementation](#rte-implementation)
    * [Adding a new plugin](#adding-a-new-plugin)
    * [Adding rich text components to CKEditor](#adding-rich-text-components-to-ckeditor)
    * [Hidden components](#hidden-components)

## Introduction

Oppia has a rich text editor (RTE), used by exploration creators to create or edit the content of their explorations. This document is an overview of its usage and implementation. The code portion of the document will largely focus on how the rich text components are integrated into the RTE, since that is the most complicated part of Oppia's RTE setup.

## Using the rich text editor

The directive is called `ck-editor-4-rte`, and can be used as simply as this example from [`suggestion-modal-for-creator-view.directive.html`](https://github.com/oppia/oppia/blob/develop/core/templates/pages/creator-dashboard-page/suggestion-modal-for-creator-view/suggestion-modal-for-creator-view.directive.html):

```html
<ck-editor-4-rte [value]="suggestionData.newSuggestionHtml"
                 (value-change)="updateValue($event)">
</ck-editor-4-rte>
```

See [`schema-based-html-editor.directive.html`](https://github.com/oppia/oppia/blob/develop/core/templates/components/forms/schema-based-editors/schema-based-html-editor.directive.html) for a more complicated usage example.

The directive exposes the following attributes:

* `[value]`: Bind to the variable storing the content the RTE is editing.
* `(value-change)`: Function call that handles the user's changes to the RTE.
* `[ui-config]` (optional): Used to configure the RTE. For example, you can set the placeholder text or whether to hide complex extensions.

## Adding rich text components

Oppia explorations can have rich text components, which are custom widgets that creators can insert into their content. Note that we have two kinds of components at play here: rich text components and [Angular components](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase#component-layer). Each rich text component is an Angular component of the form `<oppia-noninteractive-*></oppia-noninteractive-*>`, with different attributes depending on the component. Examples include the Math (for inserting Latex) component, the Image component, and the Video component. This section describes how the components are defined in case you want to add your own component, or need to modify an existing one.

### Component code

The code for defining each rich text component is housed in [`extensions/rich_text_components`](https://github.com/oppia/oppia/tree/develop/extensions/rich_text_components). In this folder, each component has its own folder, with the following files and subfolders:

* `/directives` contains the TypeScript and HTML files that define the rich text component's Angular component.

  Each rich text component has one main Angular component defined by the following files:

  * `{{rich text component name}}.component.html`: Contains the HTML of the Angular component. This HTML will be inserted in place of the `<oppia-noninteractive-*>` tag.
  * `oppia-noninteractive-{{rich text component name}}.component.ts`: Defines the component logic.
  * `oppia-noninteractive-{{rich text component name}}.component.spec.ts`: Tests for the component logic.

  Some rich text components have additional Angular components like modals. These will have additional triplets of files.

* `{{rich text component name}}.png` is an icon representing the component, used in the RTE toolbar button.

* `webdriverio.js` exports two functions that are used by the end-to-end tests: `customizeComponent` configures a new instance of the component (e.g. sets the destination of a newly added Link component), and `expectComponentDetailsToMatch` checks that a component has the expected properties.

To add a new rich text component, create a new folder under `extensions/rich_text_components`. The folder name should match the name of your new component, and the folder should contain each of the files described above.

### Component registration in `rich_text_components_definitions.ts`

You also need to register your component in [`assets/rich_text_components_definitions.js`](https://github.com/oppia/oppia/blob/develop/assets/rich_text_components_definitions.ts). Each component is described there by a dictionary with the following keys:

* `backend_id`: A string used to identify this rich text component in the backend.
* `category`: The category the rich text component falls under in the repository.
* `description`: A description of the rich text component.
* `frontend_id`: The HTML tag name for the component.
* `tooltip`: The tooltip for the icon in the rich text editor.
* `icon_data_url`: URL of the component icon.
* `is_complex`: Whether the component is large enough to discourage its use when the rich text editor is intended to be lightweight.
* `requires_fs`: Whether the component requires the filesystem in some way that prevents it from being used by unauthorized users.
* `is_block_element`: Whether the component should be displayed as a block element.
* `customization_arg_specs`: Each dictionary defines a customizable option of that component. For example, the Math component has the sole customizable option `raw_latex` for the latex to be rendered. Each dictionary in the list has the form:
  * `name`: the name of the option.
  * `description`: a string describing the option, which will be displayed when the component is being edited/inserted.
  * `schema`: a [[schema|Schema-Based-Forms]] specifies type, and optionally validation rules or UI configurations.
  * `default_value`: initial value for the option.

Each rich text component must also be registered in `feconf.py` in the `ALLOWED_RTE_EXTENSIONS` variable.

#### `customization_arg_specs`

The `customization_arg_specs` property of the component definition in `rich_text_components_definitions.ts` needs a bit more explanation. Its value is a list of dictionaries, where each dictionary has the following keys:

* `name`: The name of the customization argument. This argument will be available to the component TypeScript file as `{{name}}WithValue`. For example, the Math component has a customization argument with name `math_content`. The Math component includes the line `@Input() mathContentWithValue: string;` at the top of its class definition, and the code in the class can access the argument as `this.mathContentWithValue`.

* `description`: A human-readable description of the argument.

* `schema`: The argument's [[schema|Schema-Based-Forms]].

* `default_value`: The default value for the argument. This value must match the schema.

#### Example registration

Here's an example of the Math component's registration:

```json
  "Math": {
    "backend_id": "Math",
    "category": "Basic Input",
    "description": "A math formula.",
    "frontend_id": "math",
    "tooltip": "Insert mathematical formula",
    "icon_data_url": "/rich_text_components/Math/Math.png",
    "is_complex": false,
    "requires_internet": true,
    "requires_fs": false,
    "is_block_element": false,
    "customization_arg_specs": [{
      "name": "math_content",
      "description": "The Math Expression to be displayed.",
      "schema": {
        "type": "custom",
        "obj_type": "MathExpressionContent"
      },
      "default_value": {
        "raw_latex": "",
        "svg_filename": ""
      }
    }]
  },
```

## Implementation

This section describes how Oppia's rich text editor and rich text component system are implemented. This information may be helpful if you need to modify how Oppia uses rich text components, but you don't need this section if you just want to use RTEs or add new rich text components.

### Third-Party Libraries

The RTE depends on the following third-party libraries, all specified in our `manifest.json`:

* [CKEditor 4](https://github.com/ckeditor/ckeditor4): CKEditor is a what-you-see-is-what-you-get (WYSIWYG) rich text editor. The RTE is largely just a wrapper around CKEditor. We currently use version 4.
* [SharedSpace](https://ckeditor.com/cke4/addon/sharedspace): ensures that the toolbar will always remain in one place on the page.
* [Bootstrap](https://ckeditor.com/cke4/addon/bootstrapck): provides the skin of CKEditor's toolbar.

#### Upgrading CKEditor

If you upgrade the CKEditor version that we using, it is important to check that the new CKEditor version does not cause any regressions in the RTE. After upgrading the CKEditor version, use the RTE in the exploration editor to perform the following checks in both the Chrome and Firefox browsers:

* Input some plain text and save. Ensure that the content doesn't disappear upon saving.
* Input a single rich text component (such as the Math component) and then save. Make sure it is saved properly.
* Try using backspace to delete the rich text component. Make sure it is actually deleted.
* Try copying-and-pasting a rich text component. Hit save and make sure that the component is copied properly.
* Try editing the rich text component and make sure your changes are shown correctly.
* Try editing the rich text component and then cancel your changes.  Check that the original component is preserved.
* Try dragging-and-dropping a rich text component from one place in the content to another, then saving. Make sure the component is moved properly.
* Input text with multiple paragraphs. Make sure the paragraphs are correctly spaced apart.
* Insert an Image component with a large image, and save. Make sure the image does not overflow the content boundaries.
* Insert an Image component with a small image, and save. Make sure the image is not stretched out.

### RTE implementation

This section is a code overview of how the RTE is actually implemented. This is mostly useful if you plan to modify the RTE to fix a bug or add a new feature.

`CkEditor4RteComponent` is defined in [`ck-editor-4-rte.component.ts`](https://github.com/oppia/oppia/blob/develop/core/templates/components/ck-editor-helpers/ck-editor-4-rte.component.ts)and is the Angular component behind the RTE. There we define a `ckConfig` object that configures the editor. This configuration includes the `toolbar` attribute, which specifies the order in which rich text components appear in the editor toolbar.

Near the end of the `ngAfterViewInit()` function, we use `ck.on` to specify the following callback functions:

* The callback passed to `ck.on('instanceReady', ...)` is executed when any new instance of CKEditor is ready. For example it will be executed when we click on the content of a card in the exploration editor. In the callback, we add CSS and icons to the buttons in the toolbar.
* The callback passed to `ck.on('change', ...)` is executed whenever the content of CKEditor changes. It handles user updates to the rich text.

#### Adding a new plugin

To add a new plugin, follow these steps:

1. Add the plugin to the `manifest.json` to add it as a dependency. Take a look at how we added `SharedSpace` for an example. Alternatively, define your own custom plugin like we did with `pre`.
2. Add a call to `CKEditor.plugins.addExternal` in the component's `ngAfterViewInit()` method. For example, here's how we added the `pre` plugin:

   ```ts
   CKEDITOR.plugins.addExternal(
     'pre', '/extensions/ckeditor_plugins/pre/', 'plugin.js');
   ```

3. Add this plugin to the value of `extraPlugins` in `ckConfig`. `extraPlugins` is a string of comma-separated plugin names.

#### Adding rich text components to CKEditor

Rich text components are dynamically added to CKEditor in [`ck-editor-4-widgets.initializer.ts`](https://github.com/oppia/oppia/blob/develop/core/templates/components/ck-editor-helpers/ck-editor-4-widgets.initializer.ts) as [widgets](https://docs.ckeditor.com/ckeditor4/latest/guide/widget_sdk_intro.html). We use the `getRichTextComponents()` function to obtain each rich text component and construct their respective widgets. We also have a function `isInlineComponent()` to check whether a rich text component is an inline or block component.

`componentTemplate` defines a template to wrap the rich text components. Inline components are wrapped in a span, and block components are wrapped in a div.

The plugins are added to CKEditor in the line `CKEDITOR.plugins.add(ckName, {`. The `init` function passed to `add()` is executed when the plugin is initialised and it adds a widget for each component using the line `editor.widgets.add(ckName, {`. `editor.widgets.add` is passed an object with the following attributes:

* `button`: The button label for the widget.
* `inline`: Whether the widget is an inline component or a block component. The link and the math component are inline, and the rest are block components.
* `template`: The wrapper template for the widget.
* `edit`: A function that will be executed when a widget is being edited. In this function, the default action is canceled since we have used our own edit modal. `RteHelperService._openCustomizationModal()` is a helper function for opening the modal which is used to insert new components or edit existing ones. It uses the [customizationArgSpecs from the component definition](#customization_arg_specs) to know what the editable fields are for each component. The function can then render the modal properly for any component.
* `downcast()`: A function that downcasts the widget instance by clearing the Angular rendering content and returning the rich text component without any wrapper. Downcasting a widget means removing any property which is not needed in the output's source.
* `upcast()`: A function that upcasts an element to this widget. It returns whether an element is an instance of the widget. The element will be upcasted if it is an instance of the widget. Upcasting an element means changing that element into a widget.
* `data()`: A function that will be executed every time the widget data changes. It will set the attributes of rich text components according to the change in data values.
* `init()`: A function that will be executed when initialising a widget (i.e. after a widget instance is created but before it is ready to be used). It is executed before the data function is executed. It reads and saves values from the component attributes.

#### Hidden components

Sometimes, we want to disable or hide components in the RTE. There are 2 cases where this happens right now:

* "Complex" components like tabs contain rich text content, but we don't want the possibility of recursion where people use the RTE to insert tabs inside tabs inside tabs...etc. To prevent this, the `ckEditorRte` directive [link function](http://websystique.com/angularjs/angularjs-custom-directives-link-function-guide/) checks the `uiConfig.hide_complex_extensions` flag. When `hide_complex_extensions` is set, complex extensions will be hidden from the user.
* There are cases, such as when a learner uses the RTE to submit a suggestion, where the user is not an editor and doesn't have filesystem-related permissions. For example, the learner can't upload a picture, so it makes sense to hide the functionality for inserting a new image. The check `canUseFs && componentDefn.requiresFs` in the link function ensures that the image plugin is hidden.
