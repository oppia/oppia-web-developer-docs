# Introduction
Oppia has a rich text editor (RTE), used by exploration creators to create or edit the content of their explorations. This document is an overview of usage and implementation. The code portion of the document will largely focus on how the Rich Text Components are integrated into the RTE, since that is the most complicated part of Oppia's RTE setup.

# Usage
The directive is called `ck-editor-rte`, and can be used as as simply as:

    <ck-editor-rte ng-model="$parent.localValue">
    </ck-editor-rte>

See [`schema_based_html_editor_directive.html`](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/components/forms/schema_editors/schema_based_html_editor_directive.html) for a more complicated usage example.

The directive exposes the following attributes:
* `ng-model`: bind to the variable storing the content the RTE is editing
* `ui-config` (optional): used to configure the RTE. For example, you can set the placeholder text or whether to hide complex extensions.

# Third Party
The RTE depends on the following third party libraries, all specified in our `oppia/manifest.json`:
* [CKEditor](https://github.com/ckeditor/ckeditor-dev): CKEditor is a WYSIWYG rich text editor. The RTE is largely just a wrapper around CKEditor.
* [SharedSpace](https://ckeditor.com/cke4/addon/sharedspace): ensures that the toolbar will always remain in one designated place on the page. 
* [Bootstrap](https://ckeditor.com/cke4/addon/bootstrapck): provides the skin of CKEditor's toolbar.

# Upgrading CKEditor
As described above, the core of our RTE is the 3rd party library CKEditor. If you are upgrading the CKEditor version we are using, it is important to check that the new CKEditor version does not cause any regressions in the RTE. After upgrading the CKEditor version, use the RTE in the exploration editor to perform the following checks in both the Chrome and Firefox browsers:
* Input some plaintext and save. Ensure that the content doesn't disappear upon save.
* Input a single Rich Text Component (such as the Math component) and then save. Make sure it is saved properly.
* Try using backspace to delete the Rich Text Component. Make sure it is actually deleted.
* Try copy and pasting a Rich Text Component. Hit save and make sure that the component is copied properly.
* Try drag and dropping a Rich Text Component from one place in the content to another, then saving. Make sure the component is moved properly.
* Input text with multiple paragraphs. Make sure the paragraphs are correctly spaced apart.
* Insert an Image component with a large image, and save. Make sure the image does not overflow the content boundaries.
* Insert an Image component with a small image, and save. Make sure the image is not stretched out.

# Rich Text Components
Oppia explorations can have Rich Text Components, which are custom widgets creators can insert into their content. Each component is an Angular directive, of the form `<oppia-noninteractive-*></oppia-noninteractive-*>`, with different attributes depending on the component. Examples include the Math (for inserting Latex) component, the Image component, and the Video component. This section describes how the components are defined in case you want to add your own component, or need to modify an existing one.

The code for defining the Rich Text Components are housed in [`oppia/extensions/rich_text_components`](https://github.com/oppia/oppia/tree/develop/extensions/rich_text_components). In this folder each component has its own folder, with the following files and subfolders:
* `/directives` contains files (JS, HTML) for directives used by the component one Angular directive is master directive for that component. In the directive controller, the component attributes are processed and saved onto the scope to be used by the template. In some cases this is as simple as using `oppiaHtmlEscaper.escapedJsonToObj` to parse each attribute into an object, but a more complicated example is in [`VideoDirective.js`](https://github.com/oppia/oppia/blob/develop/extensions/rich_text_components/Video/directives/VideoDirective.js).
* `<component>.png` is an icon representing the component, used in the RTE toolbar button

The properties of components are specified in `/assets/rich_text_components_specs.js`. Each component is described by the following properties:
* `backend_id`: A string used to identify this rich-text component in the backend.
* `category`: The category the rich-text component falls under in the repository.
* `description`: A description of the rich-text component.
* `frontend_id`: The HTML tag name for the component.
* `tooltip`: The tooltip for the icon in the rich-text editor.
* `icon_data_url`: URL of the component icon.
* `preview_url_template`: URL of the component representation (can contain properties, see [preview_url_template of Video component](https://github.com/oppia/oppia/blob/develop/assets/rich_text_components_specs.js#L189)).
* `is_complex`: Whether the component is large enough to discourage its use when the rich-text editor is intended to be lightweight.
* `requires_fs`: Whether the component requires the filesystem in some way that prevents it from being used by unauthorized users.
* `is_block_element`: Whether the component should be displayed as a block element.
* `customization_arg_specs`: Each dictionary defines a customizable option of that component. For example, the `Math` component has the sole customizable option `raw_latex` for the latex to be rendered. Each dictionary in the list has the form:
    * `name`: the name of the option
    * `description`: a string describing the option, which will be displayed when the component is being edited/inserted
    * `schema`: a [schema](https://github.com/oppia/oppia/wiki/Schema-Based-Forms) specifies type, and optionally other things such as validators for the data
    * `default_value`: initial value for the option

# Code
This section is a code overview of how the RTE is actually implemented. This is mostly useful if you plan to modify the RTE when fixing a bug or adding a new feature.

## ckEditorRte
`ckEditorRte` is the actual RTE [directive](https://docs.angularjs.org/guide/directive), defined in [CkEditorRteDirective.js](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/components/CkEditorRteDirective.js).

### Template
The [template](https://docs.angularjs.org/guide/directive#template-expanding-directive)is a syntax to express the dynamic part of the html. It basically defines a view for the component. Here we have used this to render the `ckeditor` directive where it contains `contenteditable="true"` so that div is editable and a class `oppia-rte` for styling purpose.

### Toolbar
The buttons that should appear in the RTE toolbar is defined by the `toolbar` array of dictionaries in the `CKEDITOR.inline`. 
The order that will be present in this `toolbar` will account for how it looks on the site.

### Adding new plugin
To add the new plugin you need to follow these steps:
1. Add the plugin to the `manifest.json` to download it. `SharedSpace` can be looked as an example.
2. Add `CKEditor.plugins.addExternal` function corresponding to this plugin and specify its name and location.
3. Add this plugin to `extraPlugins` in CKEditor.inline function.

You can also create a custom plugin if the plugin is not available in CKEditor. `pre` is one custom plugin that is a custom plugin we have used.

### CKEditor is ready
The `ck.on('instanceReady', function)` function is executed when any new instance of CKEditor is ready. For example it will be executed when we click on the content of a card, for each option that we have for multiple choice options etc. Here we can add the css and icons to the buttons in the toolbar.

### Bind ngmodel with text in CKEditor
The `ck.on('change', function)` function is executed whenever the content of CKEditor changes. It binds the value of ng-model to the content written in the editor.

### Adding Rich Text Components to CKEditor
These rich text components are added to CKEditor in [app.js](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/app.js). The components are dynamically added to CKEditor as [widgets](https://docs.ckeditor.com/ckeditor4/latest/guide/widget_sdk_intro.html).

#### RteHelperService.getRichTextComponents()
`getRichTextComponents` is a helper function to obtain all the rich text components. A loop is then run which iterates through each component and adds it as a plugin to CKEditor.
#### RteHelperService.isInlineComponent()
`isInlineComponent` is a helper function to check whether a rich text component is inline component or block component. Link and Math are inline components whereas Video, Image, Collapsible and Tabs are block components.
#### componentTemplate
`componentTemplate` defines a template to wrap the rich text components. Inline components are wrapped in span and block components are wrapped in a div.
The plugins are added to CKEditor in the line `CKEDITOR.plugins.add(ckName, {`. The `init` function is executed when the plugin is initialized and it adds a widget for each component in the line `editor.widgets.add(ckName, {`. The widget definition in detail is ad follows:
#### button
Specifies a button label for the widget.
#### inline
Specifies whether the widget is an inline component or block component. The link and the math component are inline and the rest are declared block components.
#### template
It specifies the wrapper template for the widget.
#### edit function
This method will be executed when a widget is being edited. In this function the default action is canceled since we have used our own edit modal. `RteHelperService._openCustomizationModal()`is a helper function for opening the modal which is used to insert new components or editing existing ones. It uses the customizationArgSpecs (obtained from the component definition) to know what the editable fields are for each component, which allows it to render the modal properly for any component.
#### downcast
This function is used to downcast the widget instance by clearing the angular rendering content and returning the rich text component without any wrapper.
#### upcast function
This function is used to upcast an element to this widget. It returns whether an element is an instance of the widget. The element will be upcasted if it is an instance of the widget.
#### data function
This function will be executed every time the widget data changes. It will set the attributes of rich text components according to the change in data values.
#### init function
This function is executed while initialising a widget, after a widget instance is created, but before it is ready. It is executed before the first time when data function is exceuted. It reads values from component attributes and saves them.

# Hidden components
Sometimes, we want to disable or hide components in the RTE. There are 2 cases where this happens right now:
* "Complex" components such as tabs contain rich text content themselves, but we don't want the possibility of recursion where people can use the RTE to insert tab inside tabs inside tabs...etc. For this case, the `ckEditorRte` directive [link](http://websystique.com/angularjs/angularjs-custom-directives-link-function-guide/) function checks the `uiConfig.hide_complex_extensions` flag. When `hide_complex_extensions` is set, complex extensions will be hidden (the user won't see them at all).
* There are cases, such as when a learner uses the RTE to submit a suggestion, where the user is not an editor and doesn't have filesystem-related permissions. For example, the learner can't upload a picture, so it makes sense to hide the functionality for inserting a new image (but images that may already be in the content should be left alone). The check `canUseFs && componentDefn.requiresFs` in the link function ensures that the image plugin is hidden.