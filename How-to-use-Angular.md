With the introduction of Angular 2+ to our codebase, there are a few things one should keep in mind so that there is consistency in the style.
Note that the codebase is in a hybrid state with both Angular 2+ and AngularJS running side-by-side. Therefore the general pattern followed is that there needs to be a downgrade of the component that is upgraded so that it is available to the AngularJS part of the codebase.

## Constants
The Angular 2+ constants file to be named _*.constants.ts_ whereas the AngularJS equivalents of those constants must be in a separate file named _*.constants.ajs.ts_. The constants must be first declared in the Angular constants file and then be declared in the corresponding AngularJS constants file by importing the constants class from the Angular constants file and using that class's properties to declare the AngularJS equivalents. Import the constants class in the module and add it to the `providers` list of the `NgModule`.

For example:
If there is a constant named `SKILL_EDITOR_CONSTANT` that needs to be used in skill editor, then add that constant to the `SkillEditorConstants` class of the file _skill-editor-page.constants.ts_ as such:

```
export class SkillEditorPageConstants {
  ...
  public static SKILL_EDITOR_CONSTANT = 'constant_value';
  ...
}
```

Now, add the constant to the AngularJS file as well:

```
import { SkillEditorPageConstants } from
  'pages/skill-editor-page/skill-editor-page.constants.ts';

...
 oppia.constant('SKILL_EDITOR_CONSTANT', SkillEditorPageConstants.SKILL_EDITOR_CONSTANT);
...
```

And now you can use the constant in both your AngularJS as well as Angular parts of the code!