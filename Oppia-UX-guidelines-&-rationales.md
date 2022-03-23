### Oppia's Design Guide

You can find all of Oppia's design guidelines [here](https://xd.adobe.com/view/e54eaf14-243c-4cf4-8b9e-d8ff8c6933cc-b01d/grid/). Note that this is a living document, so it will be updated over time and some sections may be incomplete right now (as of 24 Mar 2022).


### Guidelines for Modals
#### Throughout Oppia we follow three patterns for modal closing:
1. Modal with form(s) inside it.
     - It should only get closed if the user clicks the dedicated close button or by pressing the ESC key.
     - Example: 
         ![image](https://user-images.githubusercontent.com/16653571/52317691-164f7100-29e7-11e9-8da3-7a512e227183.png)

2. Modals with warnings or suggestions.
     - It should get closed through the dedicated close button or just by clicking outside the modal i.e, in the background or by pressing ESC key.
     - Example: 

        ![image](https://user-images.githubusercontent.com/16653571/52317811-983f9a00-29e7-11e9-9422-bbc56d7aa4e6.png)

3. Modals which don't have a close button.
     - It should not get closed by users through any process.
     - Example: 

        ![image](https://user-images.githubusercontent.com/16653571/52318097-dbe6d380-29e8-11e9-95d7-b2ebea58362a.png)