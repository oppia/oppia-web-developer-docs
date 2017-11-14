# Introduction
Oppia has a rich text editor (RTE), used by exploration creators to create or edit the content of their explorations. This document is an overview of usage and implementation. The code portion of the document will largely focus on how the Rich Text Components are integrated into the RTE, since that is the most complicated part of Oppia's RTE setup.

# Usage
The directive is called `text-angular-rte`, and can be used as as simply as:

    <text-angular-rte html-content="yourContentVariable">
    </text-angular-rte>

See [`schema_based_html_editor_directive.html`](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/components/forms/schema_editors/schema_based_html_editor_directive.html) for a more complicated usage example.

The directive exposes the following attributes:
* `html-content`: bind to the variable storing the content the RTE is editing
* `ui-config` (optional): used to configure the RTE. For example, you can set the placeholder text or whether to hide complex extensions.
* `label-for-focus-target` (optional): a label for the directive, which is used when programmatically setting focus onto the RTE.

# Third Party
The RTE depends on the following third party libraries, all specified in our `oppia/manifest.json`:
* [textAngular](https://github.com/textAngular/textAngular): a text editor library developed specifically for use in AngularJS projects. The RTE is largely just a wrapper around textAngular.
* Rangy: a library for handling selections and ranges, required by textAngular
* FontAwesome: provides the icons used in textAngular's toolbar

# Upgrading textAngular
As described above, the core of our RTE is the 3rd party library textAngular. If you are upgrading the textAngular version we are using, it is important to check that the new textAngular version does not cause any regressions in the RTE. After upgrading the textAngular version, use the RTE in the exploration editor to perform the following checks in both the Chrome and Firefox browsers:
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
* `<component>Preview.png` is an image representing the component, used in the RTE text area (optional)

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
## textAngularRte
`textAngularRte` is the actual RTE [directive](https://docs.angularjs.org/guide/directive), defined in [`FormBuilder.js`](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/components/forms/FormBuilder.js).
### Template
The `template` specified in the directive definition is just an instance of the `textAngular` directive, passing in various attributes usually through variables that are often set in the `controller`. Notice that the `textAngular` directive is not bound directly to `htmlContent`, but to a `tempContent` variable defined in the `controller`. This is explained more fully in the "Rich Text Components" section.
### Toolbar options
The buttons that should appear in the RTE toolbar is defined by the `toolbarOptions` array in the `controller`. This array is converted to a JSON string, which is stored in `toolbarOptionsJSON` on the `$scope`.
### Rich Text Components
Rich text components are components such as the "math" component that can be used in explorations. Each component is a directive, of the form `<oppia-noninteractive-*>`. Currently, the RTE does not have the ability to display the rich text components directly, so each component is represented in the RTE during editing by an image icon. This is why the `htmlContent` variable is not passed to the `textAngular` directive directly. Instead, the variable `tempContent` is used, which stores the processed content after each component has been replaced by an image. The reverse processing step (replacing the image icons with the components) must be done when data is saved from the RTE. The helper functions to do the processing in either direction are defined in `rteHelperService`. To summarize:
* `$scope.tempContent = rteHelperService.convertHtmlToRte($scope.htmlContent)`, where `convertHtmlToRte` replaces each component with their corresponding image icon. `$scope.tempContent` is what the actual `textAngular` directive is bound to, since as mentioned previously textAngular can only display the image icons, it can't display the components directly.
* `$scope.htmlContent = rteHelperService.convertRteToHtml($scope.tempContent)`, where `convertRteToHtml` replaces each image icon with the corresponding component.
To understand the conversion processing more fully, look at the `rteHelperService` definition in [`app.js`](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/app.js).

## sanitizeHtmlForRte
This is a custom filter defined in [`FormBuilder.js`](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/components/forms/FormBuilder.js) that does sanitization of the HTML content (it is called from the `textAngularRte` controller). Importantly, it does the sanitization in a way that specifically preserves the rich text components.

## taOptions Decorator
In [`app.js`](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/app.js) we also have a `taOptions` [decorator](https://docs.angularjs.org/guide/decorators), which allows us to modify the textAngular toolbar options to add functionality for our Rich Text Components. This allows us to provide the following custom functionality for our components: when the exploration creator clicks on the icon for a component (or inserts a new one through the toolbar), a modal opens up for the creator to edit the component.

### Registering components with textAngular
The list of component definitions is obtained by calling `rteHelperService.getRichTextComponents()`. To provide the desired functionality we iterate over this list of definitions and register each component as a tool with textAngular, using the function `taRegisterTool`. When calling `taRegisterTool` we pass in the component name and an object that specifies:
* `display`: the html of the toolbar button corresponding to that component
* `disabled`: when the component should be disabled
* `onElementSelect`: an object with properties for what to do when the component is clicked, including:
    * `action`: a function that opens the modal to edit the component that was clicked
* `action`: a function that is called when the component's button is clicked in the toolbar, it opens the modal to insert a **new** component
This description is not complete, and it recommended to read the code carefully if you are going to work with it.

### _openCustomizationModal
This a helper function for opening the modal which is used to insert new components or editing existing ones. It uses the `customizationArgSpecs` (obtained from the component definition) to know what the editable fields are for each component, which allows it to render the modal properly for any component.

# Hidden or disabled components
Sometimes, we want to disable or hide components in the RTE. There are 2 cases where this happens right now:
* "Complex" components such as tabs contain rich text content themselves, but we don't want the possibility of recursion where people can use the RTE to insert tab inside tabs inside tabs...etc. For this case, the `textAngularRte` directive controller checks the `uiConfig.hide_complex_extensions` flag. When `hide_complex_extensions` is set, complex extensions will be hidden (the user won't see them at all).
* There are cases, such as when a learner uses the RTE to submit a suggestion, where the user is not an editor and doesn't have filesystem-related permissions. For example, the learner can't upload a picture, so it makes sense to disable the functionality for inserting a new image (but images that may already be in the content should be left alone). The check for this is done in the call to `taRegisterTool`, when specifying the `disabled` property. When disabled, the toolbar button for that component becomes greyed out and unclickable.