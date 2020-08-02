We have a certain file naming convention to be followed while naming new files.

### The Naming Convention:
This new naming convention as of now applies only to pages/, filters/ and components/ directories. 


The naming follows a general pattern:

- The filename is divided into three parts (four for spec files). The first part is the name of the functionality, the second part is the type of functionality and the third part is the file extension. The third part in case of spec files become the word “spec” and the extension becomes the fourth part.

- The different parts of the filename are joined by periods.

- If the first part of the name has multiple words then the words are joined by kebab-case, with all the letters being small.

- For eg if there is a directive file which houses a directive named stateResponses. Then the name of the file would be state-responses.directive.ts 


**Types of functionality.**

- _Directives_: A directive’s name must end with “**.directive.ts**” For example, if the name of a directive is ‘stateResponses’ then the name of the file must be “state-responses.directive.ts”.

- _Controllers_: A controller’s name must end with “**.controller.ts**” For example, if the name of a directive is ‘StoryEditor’ then the name of the file must be “story-editor.controller.ts”.

- _Filters_: A filter’s name must end with “**.filter.ts**” For example, if the name of a filter is ‘formatTimer’ then the name of the file must be “format-timer.filter.ts”.

- _Services_: A service’s name must end with “**.service.ts**” For example, if the name of a service is ‘ExplorationDataService’ then the name of the file must be “exploration-data.service.ts”.

- _Constants_: The constants of a page are to be kept in a single file. The file should be _named name-of-the-page.constants.ts_. Any new constant that needs to be added should be added to this file only and this constants.ts file should be required in the file which uses the constant. 

- _HTML files_: There are three types of HTML files:-

    - _Mainpage_: These are the pages which act as a starting point of the page. These pages are directly called from the backend. The names of these HTML files must end with “**.mainpage.html**”. For example, the main page of the exploration editor page would be named exploration-editor-page.mainpage.html.

    - _Directive_: These are the HTML files which are served by the directive files. These are the HTML files that appear in the ‘templateUrl’ of the directive. These must have their names ending with “**.directive.html**”. For example, the progress nav directive would be named progress-nav.directive.html.

    - _Template_: These are the shared HTML files which are required by various other functions like modals, jinja templating, etc.  These names are to end with "**.template.html**" 

- Import files: These are the TS files which are for the sole purpose of importing the required TS files for the HTML file. Such files are to end with “**.import.ts**”. For example if a file get-started.mainpage.html needs a script file then the file would be named “get-started.import.ts”

### Directory Structure:

The directory structure is based on the concept of single feature per folder.

- The files in a directory imply a single common feature.

- The files which are sub-ordinates of the parent directive/controller are to be made as sub-directory of the directory where the parent directive/controller resides. These sub-directories again follow the rules of the directory. If one or more sibling files relate to a similar feature, then they are to be placed in a single directory.

- For services, the services specific to a page should be located in a direct subdirectory of the mainpage directory.

- For services that are to be used across multiple pages, such are to be placed in a shared folder like domain/ or services/.

- For big pages like exploration-editor-page, services specific to a feature may be included on a subdirectory to the feature directory.

- The various template HTML files (shared HTML files not in the templateUrl of a directive, these are mostly used in modals and in ‘{% include %}’ statements) must be located in a direct sub-directory of the mainpage directory (except in big pages where they can be put under a subdirectory of feature directory).

- **Naming**: The name of the directory would be the name of the functionality in kebab-case.

    - The name of the highest directory under pages directory must be suffixed with -page

    - The name of the sub-directories are to be named after the feature they serve in kebab case. For example, if it houses a feature as "dummy feature" then the directory must be named dummy-feature.

    - The name of the directory having the various services and template HTML files would be name-of-the-parent-directory-services and name-of-the-parent-directory-templates respectively.


While adding any new files, devs are requested to kindly follow the above convention. In case of any problems or cases not covered by the above convention, you can reach out to us and we would be happy to help.

