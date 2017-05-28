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
`textAngularRte` is the actual RTE [directive](https://docs.angularjs.org/guide/directive), defined in `oppia/core/templates/dev/head/components/forms/FormBuilder.js`.
### Template
The `template` specified in the directive definition is just and instance of the `textAngular` directive, passing in various attributes usually through variables that are often set in the `controller`. Notice that the `textAngular` directive is not bound directly to `htmlContent`, but to a `tempContent` variable defined in the `controller`. This is explained more fully in the "Rich Text Components" section.
### Toolbar options
The buttons that should appear in the RTE toolbar is defined by the `toolbarOptions` array in the `controller`. This array is converted to a JSON string, which is stored in `toolbarOptionsJSON` on the `$scope`.
### Rich Text Components
Rich text components are components such as the "math" component that can be used in explorations. Each component is a directive, of the form `<oppia-noninteractive-*>`. Currently, the RTE does not have the ability to display the rich text components directly, so each component is represented in the RTE during editing by an image icon. This is why the `htmlContent` variable is not passed to the `textAngular` directive directly. Instead, the variable `tempContent` is used, which stores the processed content after each component has been replaced by an image. The reverse processing step (replacing the image icons with the components) must be done when data is saved from the RTE. The helper functions to do the processing in either direction are defined in `rteHelperService`. To summarize:
* `$scope.tempContent = rteHelperService.convertHtmlToRte($scope.htmlContent)`, where `convertHtmlToRte` replaces each component with their corresponding image icon. `$scope.tempContent` is what the actual `textAngular` directive is bound to, since as mentioned previously textAngular can only display the image icons, it can't display the components directly.
* `$scope.htmlContent = rteHelperService.convertRteToHtml($scope.tempContent)`, where `convertRteToHtml` replaces each image icon with the corresponding component.
To understand the conversion processing more fully, look at the `rteHelperService` definition in `oppia/core/templates/head/app.js`.
## taOptions Decorator
In `app.js` we also have a `taOptions` [decorator](https://docs.angularjs.org/guide/decorators), which allows us to modify the textAngular toolbar options to add functionality for our Rich Text Components. This allows us to provide the following custom functionality for our components: when the exploration creator clicks on the icon for a component (or inserts a new one through the toolbar), a modal opens up for the creator to edit the component.

To provide this functionality we register each component as a tool with textAngular using `taRegisterTool`. With this call we specify things such as the tool name, the action to take on click, and when the tool should be disabled. The actual behavior of the editing modal is largely defined in `_openCustomizationModal.` A lot of functionality of the tool for each component is dependent on the component definition, which includes things such as the name and `customizationArgSpecs` (specifies how the component can be customized, which is important for the editing modal). The list of component definitions is obtained by calling `rteHelperService.getRichTextComponents()`. 

## sanitizeHtmlForRte
This is a custom filter defined in `FormBuilder.js` that does sanitization of the HTML content (it is called from the `textAngularRte` controller). Importantly, it does the sanitization in a way that specifically preserves the rich text components.