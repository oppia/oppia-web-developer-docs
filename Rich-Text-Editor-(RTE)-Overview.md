# Introduction
Oppia has a rich text editor (RTE), used by exploration creators to create or edit the content of their explorations. This document is an overview of how this is implemented. The code portion of the document will largely focus on how the Rich Text Components are integrated into the RTE, since that is the most complicated part of Oppia's RTE setup.
# Third Party
The RTE depends on the following third party libraries, all specified in our `oppia/manifest.json`:
* [textAngular](https://github.com/textAngular/textAngular): a text editor library developed specifically for use in AngularJS projects. The RTE is largely just a wrapper around textAngular.
* Rangy: a library for handling selections and ranges, required by textAngular
* FontAwesome: provides the icons used in textAngular's toolbar

# Usage
The directive is called `text-angular-rte`, and can be used as as simply as:

    <text-angular-rte html-content="yourContentVariable">
    </text-angular-rte>

See `oppia/core/templates/dev/head/components/forms/schema_editors/schema_based_html_editor_directive.html` for a more complicated usage example.

The directive exposes the following attributes:
* `html-content`: bind to the variable storing the content the RTE is editing
* `ui-config` (optional): used to configure the RTE. For example, you can set the placeholder text or whether to hide complex extensions.
* `label-for-focus-target` (optional): a label for the directive, which is used when programmatically setting focus onto the RTE.

# Code
## textAngularRte
`textAngularRte` is the actual RTE [directive](https://docs.angularjs.org/guide/directive), defined in [`FormBuilder.js`](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/components/forms/FormBuilder.js).
### Template
The `template` specified in the directive definition is just and instance of the `textAngular` directive, passing in various attributes usually through variables that are often set in the `controller`. Notice that the `textAngular` directive is not bound directly to `htmlContent`, but to a `tempContent` variable defined in the `controller`. This is explained more fully in the "Rich Text Components" section.
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
* There are cases, such as when a learner uses the RTE to submit a suggestion, where the user is not an editor and doesn't have filesystem-related permissions. For example, the learner can't upload a picture, so we would want to disable the image component. The check for this is done in the call to `taRegisterTool`, when specifying the `disabled` property. When disabled, the toolbar button for that component becomes greyed out and unclickable.