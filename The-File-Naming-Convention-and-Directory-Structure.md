Follow these conventions when adding frontend files. The filename checker described below is introduced by [oppia/oppia#27623](https://github.com/oppia/oppia/pull/27623); enforcement requires that PR to be merged.

## Table of contents

* [The naming convention](#the-naming-convention)
* [Filename lint checks](#filename-lint-checks)
  * [Supported filename patterns](#supported-filename-patterns)
  * [Path-specific patterns](#path-specific-patterns)
  * [Legacy exceptions and migration](#legacy-exceptions-and-migration)
  * [Extending the checker](#extending-the-checker)
* [Directory structure](#directory-structure)

## The naming convention

The conventions apply to TypeScript, HTML and CSS files under `assets/`, `core/templates/` and `extensions/`, not just `pages/`, `filters/` and `components/`. Other extensions, generated dependencies and frontend acceptance-test utilities are outside the filename checker's configured scope.


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

## Filename lint checks

The filename checker is part of the existing [[lint workflow|Lint-Checks]], through `GeneralPurposeLinter`. It reports the invalid path, the expected convention and a link to this page. It checks names only, not spelling, file contents, matching implementation/spec pairs or directory casing.

To check a specific destination after adding or renaming a file, run from the Oppia root:

```console
python -m scripts.linters.run_lint_checks --files core/templates/services/lesson-data.service.ts
```

Use `--path core/templates/services` to check a directory. The existing default changed-file selector does not include paths Git identifies as renames, so use `--files` or `--path` for renamed destinations. The lint runner also retains its existing global exclusions, including `assets/scripts/`; the filename-linter inventory test separately checks all tracked filenames, including those paths.

### Supported filename patterns

Feature names use lowercase kebab-case, starting with a letter; subsequent words may contain lowercase letters and digits. Use periods between the feature name, role, optional `spec` segment and extension. For example, `lesson-card.component.spec.ts` is valid; `LessonCard.component.ts`, `lesson-card-component.ts` and `lesson-card.services.ts` are not. Uppercase extensions do not bypass the rules.

| File type | Pattern or example |
| --- | --- |
| TypeScript implementation | `feature-name.role.ts`. |
| TypeScript unit test | `feature-name.role.spec.ts`. |
| Routing module | `feature-name.routing.module.ts` or `feature-name.routing.module.spec.ts`. |
| Integration test | `feature-name.integration.spec.ts`. |
| Type declaration | `feature-name.d.ts`. |
| HTML | `feature-name.component.html`, `.directive.html`, `.template.html` or `.mainpage.html`. |
| CSS | `feature-name.component.css` or `feature-name.directive.css`. |

The configured TypeScript roles are `component`, `constants`, `controller`, `directive`, `factory`, `filter`, `guard`, `import`, `initializer`, `model`, `module`, `pipe` and `service`. Components follow the same convention as directives: for example, `lesson-card.component.ts` and `lesson-card.component.html`.

### Path-specific patterns

Special-purpose files have narrower permissions rather than a general exception for any TypeScript, HTML or CSS name:

* Interaction entry points may use PascalCase only when the filename matches their immediate interaction directory, such as `extensions/interactions/Continue/Continue.ts`.
* Immediate files in `core/templates/utility/` may use kebab-case `.ts` and `.spec.ts` names without a role.
* Schema validators, unit-test helpers and translation infrastructure have explicitly scoped patterns in their existing directories.
* The CodeMirror `diff_match_patch.d.ts` declaration and the infrastructure entry points listed in `INFRASTRUCTURE_TYPESCRIPT_PATHS` are allowed only at their configured paths.
* The shared `footer_js_libs.html`, `header_css_libs.html` and `header_js_libs.html` templates are allowed directly under `core/templates/pages/`. The form test fixture has an exact-path exception.
* PascalCase value-generator templates are allowed under `extensions/value_generators/templates/` with the `.component.html` suffix.
* Kebab-case global CSS names are allowed directly under `core/templates/css/`. Interaction static CSS files may use underscore-separated names under `extensions/interactions/<interaction>/static/`.

Patterns match the complete basename and, where configured, the complete repository-relative path. They cannot be reused in unrelated directories. See [the checker configuration](https://github.com/oppia/oppia/blob/develop/scripts/linters/filename_linter.py) for the exact expressions and infrastructure paths after the linter PR merges.

### Legacy exceptions and migration

Existing nonconforming filenames are recorded by exact repository-relative path in `scripts/linters/filename_linter_allowlist.json`, with a reason referencing [#27577](https://github.com/oppia/oppia/issues/27577). These are migration exceptions, not examples for new files. Wildcards and copied filenames in different directories are not exceptions.

When migrating a file, rename it, update its references and remove its old allowlist entry in the same change. Tests require entries to be sorted, unique, still present and still nonconforming. An inventory test checks all tracked filenames so new names cannot silently fall outside the documented policy.

### Extending the checker

The naming configuration is separate from `check_filenames()`:

* Add an ordinary TypeScript role to `TYPESCRIPT_ROLES` to support both its implementation and unit-test filenames.
* Add a `FilenamePattern` for a different naming format. Include a path restriction when the format is specific to a directory or infrastructure file.
* Add a `FilenameRule` for a new directory scope or extension. Directory prefixes must end in `/`; extensions must be lowercase.

Patterns within a rule are alternatives. A path covered by multiple rules must satisfy each applicable rule. Add positive and negative tests, including directory-boundary cases, and update this wiki page whenever changing the policy. Existing tests demonstrate registering a resolver pattern and a separate JSON rule without changing the checker.

## Directory structure

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
