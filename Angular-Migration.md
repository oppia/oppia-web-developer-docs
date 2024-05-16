## Overview

Angular is an app-design framework and development platform for creating efficient and sophisticated apps.

Currently, Oppia is in a hybrid state where we have both Angular and AngularJS. This makes our application slow and bulky. The codebase has duplicate libraries since many of the AngularJS libraries are not compatible with Angular. This project aims to migrate the entire codebase to Angular. The benefits of doing this are:

* Improved Developer Experience:

  * Developing when the application is a hybrid state opens us to a whole host of complicated errors which are in some cases not solvable.
  * Angular is being actively maintained and comes out with a lot of new features that aid development.

* Improved User Experience:

  * When the codebase is completely migrated, the developers will focus their efforts on making new features for the website rather than fixing nasty errors that pop up because of the hybrid state.
  * Decreased page loading times as a result of not bundling AngularJS anymore.
  * Better application performance in general.

The project plan will be iterative in nature. We will migrate the services first and then the controllers and directives. The services will be migrated in dependency order. For example, if A depends on B and B depends on C, we will migrate in the order C, B, and then A.

### Testing videos

**Note: Angular Migration Pull Requests must be accompanied with a video showing the before and after effects of their change to ensure that nothing is broken. This ensures faster review and a lower risk of reverted PRs**

## Angular migration tracker

The [angular migration tracker](https://docs.google.com/spreadsheets/d/1L9Udn-XT6Lk1qaTBUySTw1AnhvQMR-30Qry4rfd-Ovg/edit?usp=sharing) holds the record of which services are to be migrated. The issue [#8472](https://github.com/oppia/oppia/issues/8472) holds a subset of those services that can be migrated without any major blockers.

## Implementation details to migrate services

1. Import the following dependencies:

   ```js
   import { downgradeInjectable } from '@angular/upgrade/static';
   import { Injectable } from '@angular/core';
   ```

2. If the services uses `$http`, import `HttpClient` as a dependency, also import:

   ```js
   import { HttpClient } from '@angular/common/http';
   ```

3. Change the AngularJS factory definition to and Angular class definition as follows:

   ```js
   angular.module('oppia').factory('ServiceName',['dependency1', function(dependency1) {
   ```

   to

   ```js
   import { dependency1 } from ... // to be added at the top of the file
   ..
   ..
   export class ServiceName {
   ```

4. Add a decorator above the class definition:

   ```js
   @Injectable({
     providedIn: 'root'
   })
   export class ServiceName {
   ...
   ```

5. Add a constructor for the class and inject the dependencies:

   ```js
   constructor(
       private service1: Service1,
       private service2: Service2) {}
   ```

6. Change `$http.get` requests in the service as follows:

   (a) Change `$http.get` to `this.http.get`:

   ```js
   $http.get(url).then(function(response) {
     dataDict = angular.copy(response.data);
   ```

   to

   ```js
   this.http.get(
      url).toPromise().then(
       (response) => {
   ```

   The `dataDict` is not required in Angular services. You can directly use the `response` variable.

   (b) Search in the  codebase for where the service is used to obtain results from get requests and change `response.data` to `response`.

   (c) Return the `errorCallback` (the reject function) with `errorResponse.error.error` as follows:

   ```js
   (errorResponse) => {
     errorCallback(errorResponse.error.error);
   }
   ```

   (d) Add `$rootScope.$applyAsync()` in the controller/directive that is resolving the HTTP request similar to how it is added [here](https://github.com/oppia/oppia/pull/8427/files#diff-ecf6cefd0707bcbafeb6a0b4009aa60cR78). To do so, perform a global search in the codebase for the function with the HTTP request. For example, if the service is `SkillBackendApiService` and the function in which the HTTP request is made is `fetchSkill`, then search the codebase for `SkillBackendApiService.fetchSkill` and add `$rootScope.$applyAsync()` as follows:

   ```js
   SkillBackendApiService.fetchSkill(...).then((...) => {
       //resolve function
       ...
       $rootScope.$applyAsync() //add here
    }, (...) => {
       ...
       //reject function
    }
   );
   ```

   Do this for all functions that have `http` calls.

7. Change `$http.put` or `$http.post` requests as follows:

   (a) Change `$http.post/put` to `this.http.post/put`

   ```js
   $http.post(url).then(function(response) {
     ...
   ```

   to

   ```js
   this.http.post(
     url).toPromise().then(
      (response) => {...;
   ```

   (b) Add `$rootScope.$applyAsync()` wherever the function with the HTTP request is used. For example, see the changes [here](https://github.com/oppia/oppia/pull/8427/files#diff-ecf6cefd0707bcbafeb6a0b4009aa60cR78). You can find usages of the function just like you found usages when migrating `$http.get` calls in the previous step.


8. If you are migrating a service that is named as `.*-backend-api.service.ts`, then please return a domain object and not a dict in the `successCallback` function. For example take a look at [PR #9505](https://github.com/oppia/oppia/pull/9505/files#diff-05de50229b44c01bdaeac172928b514dR64), where the domain object is created via an object factory. You also need to change the piece of code where this response is used because the response is now a domain object instead of a dict. If there is no specific object factory to alter the response to a domain object, create one similar to how it is done in this [change](https://github.com/oppia/oppia/pull/9570/files#diff-09e3c3999c18dabdf2ddedf6e3e250f8R1).

   Topic domain objects need to contain properties that are being read from the backend. Therefore, the topic domain object does not depend on the service being migrated, but rather the expected return value of the function. For example, in `SkillBackendApiService`, the function `fetchSkill` will clearly return a `Skill` object. Note that `SkillObjectFactory.ts` already exists, so we don't need to create it. But if there is no corresponding Object Factory, you need to create one similar to how `SkillObjectFactory` is created. Next, we take the response from the backend and instead of `successCallback(response)`, we resolve `successCallback(SkillObjectFactory.createFromBackendDict(response))`. This passes the frontend `Skill` object to functions that call `fetchSkill` when the promise gets resolved.

   Since before you migrated the file, the calling functions were expecting a backend dict object, the references need to be changed as well. To do this, do a global search in the code-base for the function, e.g. `SkillBackendApiService.fetchSkill` and refactor the code inside the resolve function to reflect that the parameter is now a `Skill` object and not a backend dict object.

   Please note that interfaces/properties in Object Factories and the `.*-backend-api.service.ts` could be in snake_case. If that is the case, please surround them with single quotes as in `'some_property'`. Except for these two categories, all the properties inside all other files should be camel case, e.g. `someProperty`.

9. For functions in the service, add type definitions for all the arguments as well as return values.

   **Note:** For complex types or some type that is being used over functions or files we can declare an interface. For example in the file [rating-computation.service.ts](https://github.com/oppia/oppia/blob/develop/core/templates/components/ratings/rating-computation/rating-computation.service.ts) we have an export interface to declare the type `RatingFrequencies`. In the same file, we also have a function named static, which is used by the functions of the class itself.

10. For functions which are private to the service (used as helper functions), add the private keyword.

11. At the end of the file, add:

    ```js
    angular.module('oppia').factory('ServiceName', downgradeInjectable(ServiceName));
    ```

For an example of migrating a service, see [this pull request](https://github.com/oppia/oppia/pull/10693/files).

## Implementation details to migrate tests

1. Remove all `beforeEach()` blocks and any other service that is not needed in the test file.

2. Convert all the function keywords to fat arrow functions like this:

   ```js
   describe('abc', function() { ... });
   ```

   to

   ```js
   describe('abc', () => { .. });
   ```

3. Import TestBed in your spec file

   ```js
   import { TestBed } from '@angular/core/testing';

   import { ServiceName } from ...
   ```

   If your test is for a service that makes HTTP requests, you also need to import the following:

   ```js
   import { HttpClientTestingModule, HttpTestingController } from
      '@angular/common/http/testing';
   import { TestBed, fakeAsync, flushMicrotasks } from '@angular/core/testing';
   ```

4. Add a beforeEach block that creates an instance of service you want to test:

   ```js
   beforeEach(() => {
     serviceInstance = TestBed.get(ServiceName);
   });
   ```

   (a) If your spec file needs any pipes (filters in angular), import them and add it to the providers in the TestBed configuration

   ```js
   beforeEach(() => {
     TestBed.configureTestingModule({
       providers: [CamelCaseToHyphensPipe, ConvertToPlainTextPipe] // Any pipe that is required
     });
     instance = TestBed.get(ServiceName);
   ```

   (b) If your spec file tests a service that makes HTTP requests, you need to make an `HttpClientTestingModule` and add an `afterEach` statement to check there are no pending requests after each test. For example:

   ```js
   beforeEach(() => {
     TestBed.configureTestingModule({
       imports: [HttpClientTestingModule],
     });
     httpTestingController = TestBed.get(HttpTestingController);
     instance = TestBed.get(ServiceName);
   });

   afterEach(() => {
     httpTestingController.verify();
   });
   ```

5. For each test, replace the name of the service with the instance name that is created above using TestBed.

6. If your spec file is for a service that makes HTTP requests then:

   (a) Convert each individual test defined in it block as follows:

   ```js
   it('should ...', fakeAsync(() => {
   .
   .
   }));
   ```

   (b) Change the test to create an HTTP request via httpTestingController. Here's an example from `topic-viewer-backend-api.service.spec.ts`:

   ```js
   $httpBackend.expect('GET', '/topic_data_handler/0').respond(
     sampleDataResults);
   TopicViewerBackendApiService.fetchTopicData('0').then(
     successHandler, failHandler);
   $httpBackend.flush();
   ```

   to

   ```js
   topicViewerBackendApiService.fetchTopicData('0').then(
    successHandler, failHandler);
   var req = httpTestingController.expectOne(
               '/topic_data_handler/0');
   expect(req.request.method).toEqual('GET');
   req.flush(sampleDataResults);

   flushMicrotasks();
   ```

## Implementation details to migrate directives

There are two parts to this migration: the TS file and the HTML file.

### Migrating the logic part (ts file)

Here are the steps to migrate the logic part.

#### 1. Create a basic component in the directive file

Import `Component` to the file:

```js
import { Component } from '@angular/core';
```

Then take a look at the directive declaration. For example if the directive is declared like this:

```js
angular.module('oppia').directive('conceptCard', [
  'UrlInterpolationService', function(UrlInterpolationService) {
    return {
      restrict: 'E',
      scope: {},
      bindToController: {
        getSkillIds: '&skillIds',
        index: '='
      },
      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(
        '/components/concept-card/concept-card.directive.html'),
      controllerAs: '$ctrl',
      controller: [
        '$scope', '$filter', '$rootScope',
        'ConceptCardBackendApiService', 'ConceptCardObjectFactory',
```

then add the following at the end of the file:

```js
@Component({
  selector: 'concept-card',
  templateUrl: './concept-card.directive.html',
  styleUrls: []
})
export class ConceptCardComponent {}
```

Some points to note:

* Please keep in mind the name of the directive declared. In this case, it is 'conceptCard'.
* The directive name converted to kebab-case is the selector (conceptCard -> concept-card).
* The name of the class is in CamelCase (note the first letter is capital) suffixed with "Component". So conceptCard -> ConceptCardComponent.
* The template of the directive (in 99% of cases) exists in the same folder as the directive.ts file.

#### 2. Import and inject the dependencies

Suppose the AngularJS code has the following dependencies:

```js
controller: [
        '$scope', '$rootScope',
        'ConceptCardBackendApiService', 'ConceptCardObjectFactory',
```

The first two dependencies are interesting ones. They don't have a direct equivalent in Angular. In most cases, you will find something like `$scope.someVariable = `, `$scope.$onDestroy`, `$scope.$onInit`, and `$rootScope.$applyAsync()`. In other cases, contact @srijanreddy98.

Next, consider the other two dependencies ('ConceptCardBackendApiService', 'ConceptCardObjectFactory'). These are called injectables as they are "injected". These go into your constructor like this:

1. Import these two services into the directive.

   ```js
   import { ConceptCardBackendApiService } from 'service/some-service.ts';
   import { ConceptCardObjectFactory } from 'services/some-other-service.ts';
   ```

2. Create a constructor for the class you made in the previous step and add those injectables there:

   ```js
   export class ConceptCardComponent {

   constructor(
     private conceptCardBackendApiService: ConceptCardBackendApiService,
     private conceptCardObjectFactory: ConceptCardObjectFactory
   ) {}

   }
   ```

Sometimes, you will also see dependencies like $window, $log, $timeout etc.

* For `$window`: Use `window-ref.service.ts`. In the constructor, with other dependencies, inject `WindowRef`:

  ```js
  constructor(
  ...
  private windowRef: WindowRef
  ) {}
  ```

  Then instead of `window`, use `windowRef.nativeWindow`, e.g. `windowRef.nativeWindow.location.href`. Also, instead of `location` for setting URLs, use `location.href`.

* `For $timeout`: Use `setTimeout`

* `For $log`: Use `logger.service.ts`

**Notice the casing very carefully. The service is ConceptCardBackendApiService but its instance is called conceptCardBackendApiService (with a small c)**

#### 3. Adding OnInit / OnDestroy

You will notice that in almost every directive you have `ctrl.$onInit` and/or `ctrl.$onDestroy`. The equivalent of this in angular is `ngOnInit` and `ngOnDestroy`.

First, you need to import OnInit from '@angular/core'; Then implement it in the class by changing the class declaration to `export class ConceptCard implements OnInit {` and adding an `ngOnInit() {}` below the constructor.  After this step the component class would look like this:

```js
import { Component, OnInit } from '@angular/core';
...
export class ConceptCardComponent implements OnInit {

  constructor(
    private conceptCardBackendApiService: ConceptCardBackendApiService,
    private conceptCardObjectFactory: ConceptCardObjectFactory
  ) {}

  ngOnInit(): void {
	  ...
  }
}
```

Do the same for `onDestroy`.

#### 4. Changing the bindToController

If there is some value in bindToController, then import `Input` from `@angular/core`;

There are four "syntaxes" that you could run into when trying to migrate bindToController:

1. `'@'`
2. `'<'`
3. `'='`
4. `'&'`

##### The syntax for `'@'`

```js
  layoutType: '@',
```

will change to

```js
  @Input() layoutType: string;
```

**Note that `'@'` is always a string but `'<'` can be of any type (string, number, object or custom types).**

##### The syntax for '<'

```js
  layoutAlignType: '<',
```

changes to

```js
  @Input() layoutAlignType: string;
```

(The type of layoutAlignType being string is an example. please be aware of the type used in your case).

Take a look at the directive name (in this case it is conceptCard). Now do a global search for e.g. `<concept-card` (note the change to snake_case and the extra '<' at the beginning). In each search result, you should find something like `layout-align-type=layoutAlign`.

* If the search result is in an AngularJS template: Change `layout-align-type=layoutAlign` to `[layout-align-type]=layoutAlign`. Notice in the component it was `layoutAlignType` but in HTML it is [layout-align-type]. The camelCase to kebab-case change is required when the template is a template of an AngularJS component/directive.

Otherwise: Change `layout-align-type=layoutAlign` to `[layoutAlignType]=layoutAlign`.

**If you find something like `layout-align-type="center center"`, leave it as it is, do not change it. The `[]` syntax can only be used with variables. If the attribute is not surrounded by `[]` and the attribute value is surrounded by double quotes, that means the passed value is a string.**

##### The syntax for `'&'`

You will find `'&'` with a syntax that looks like `getSkillIds: '&skillIds',`. This requires some significant changes so please follow the next steps very carefully:

First, change the

```js
getSkillIds: '&skillIds',
```

to

```js
@Input() skillIds: Array<string>,
```

Note: If the syntax looks like `skillIds: '&'`, then just change it to:

```js
@Input() skillIds: Array<string>,
```

(`Array<string>` is an example. please be aware of the type used in your case).

Next, change all cases of `ctrl.getSkillIds()` to `this.skillIds`. (Notice the parentheses were also removed.)

Take a look at the directive name (in this case it is conceptCard). Now do a global search for e.g. `<concept-card`. (Note the change to kebab-case and the extra '<' at the beginning). In each search result, you should find something like `skill-ids=skillIds`, which you should change to:

* If the search result is in an AngularJS template (i.e. the corresponding .ts file for the HTML has not been migrated): `[skill-ids]=skillIds`. (Notice that in the component it was `skillIds` but in HTML it is [skill-ids]. The camelCase to kebab-case change is required when the template is a template of an AngularJS component/directive).

* Otherwise: `[skillIds]=skillIds`.

**Note: If you find something like `skill-type="supersonic"`, leave it as it is, do not change it. The `[]` syntax can only be used with variables. If the attribute is not surrounded by `[]` and the attribute value is surrounded by double quotes, that means the passed value is a string.**

Understanding binding interpolation:

1. Binding is a way to share information between different directives using variables that pass values. Variables are passed via selectors of other directives present in the HTML file of the directive we are working on.
2. Interpolation is simply a way to make sure we pass variables and not values in our HTML. For example, how do we know if in `<dir-name abc=”xyz”>`, `xyz` is a string or a variable? To clarify this ambiguity, we use interpolation for variables. Interpolation has 2 forms:

	 * `<dir-name [abc]="xyz">` (The `[]` indicates that the string is a variable)
	 * `<dir-name abc="{{ xyz }}">`

	 We use the first method in all cases except when the variable is interspersed with other text. e.g. `<dir-name abc="The boy has {{ count }} apples">`

3. Do not use interpolation with properties marked with [prop], or events. These automatically assume that a variable is passed.

##### The syntax for `=`

In most cases, the `=` is the same as `<` when looked at from an Angular2+ perspective, so just follow the steps given for `<` migration.

#### 5. Start separating the other functions

Take a look at this example directive code:

```js
var ctrl = this;
ctrl.isLastWorkedExample = function() {
  return ctrl.numberOfWorkedExamplesShown ===
    ctrl.currentConceptCard.getWorkedExamples().length;
};

ctrl.showMoreWorkedExamples = function() {
  ctrl.explanationIsShown = false;
  ctrl.numberOfWorkedExamplesShown++;
};

ctrl.$onInit = function() {
  ctrl.conceptCards = [];
  ctrl.currentConceptCard = null;
  ctrl.numberOfWorkedExamplesShown = 0;
  ctrl.loadingMessage = 'Loading';
  ConceptCardBackendApiService.loadConceptCards(
    ctrl.getSkillIds()
  ).then(function(conceptCardObjects) {
    conceptCardObjects.forEach(function(conceptCardObject) {
      ctrl.conceptCards.push(conceptCardObject);
    });
    ctrl.loadingMessage = '';
    ctrl.currentConceptCard = ctrl.conceptCards[ctrl.index];
    ctrl.numberOfWorkedExamplesShown = 0;
    if (ctrl.currentConceptCard.getWorkedExamples().length > 0) {
      ctrl.numberOfWorkedExamplesShown = 1;
    }
    // TODO(#8521): Remove when this directive is migrated to Angular.
    $rootScope.$applyAsync();
  });
};
```

Look at all lines matching the pattern `ctrl.someVariable = function(...) {...`.

In the component you made in step one, just create those functions without the `ctrl` and `= function`:

```js
export class ConceptCardComponent implements OnInit {

constructor(
  private conceptCardBackendApiService: ConceptCardBackendApiService,
  private conceptCardObjectFactory: ConceptCardObjectFactory
) {}

  ngOnInit() {
  }

  isLastWorkedExample() {
  }

  showMoreWorkedExamples() {
  }

}
```

#### 6. Create class members (variables)

Till now we only looked at `ctrl.someVariable = function()`. Now we will look at all the other cases. Take a look at this directive code:

```js
var ctrl = this;
ctrl.isLastWorkedExample = function() {
  return ctrl.numberOfWorkedExamplesShown ===
    ctrl.currentConceptCard.getWorkedExamples().length;
};

ctrl.showMoreWorkedExamples = function() {
  ctrl.explanationIsShown = false;
  ctrl.numberOfWorkedExamplesShown++;
};

ctrl.$onInit = function() {
  ctrl.conceptCards = [];
  ctrl.currentConceptCard = null;
  ctrl.numberOfWorkedExamplesShown = 0;
  ctrl.loadingMessage = 'Loading';
  ConceptCardBackendApiService.loadConceptCards(
    ctrl.getSkillIds()
  ).then(function(conceptCardObjects) {
    conceptCardObjects.forEach(function(conceptCardObject) {
      ctrl.conceptCards.push(conceptCardObject);
    });
    ctrl.loadingMessage = '';
    ctrl.currentConceptCard = ctrl.conceptCards[ctrl.index];
    ctrl.numberOfWorkedExamplesShown = 0;
    if (ctrl.currentConceptCard.getWorkedExamples().length > 0) {
      ctrl.numberOfWorkedExamplesShown = 1;
    }
    // TODO(#8521): Remove when this directive is migrated to Angular.
    $rootScope.$applyAsync();
  });
};
```

Looking at all the other `ctrl.` declarations we find `ctrl.numberOfWorkedExamplesShown`, `ctrl.currentConceptCard`, `ctrl.explanationIsShown`, `ctrl.numberOfWorkedExamplesShown++``, `ctrl.conceptCards`, `ctrl.loadingMessage`, etc.

Now we have to define them as class members. In order to do so just remove `ctrl.` from the front of the variable and add them to the class above the constructor. For example:

```js
export class ConceptCardComponent implements OnInit {
numberOfWorkedExamplesShown: number = 0;
currentConceptCard: ConceptCard;
explanationIsShown: boolean = false;
conceptCards: Array<ConceptCard>;
loadingMessage: string = '';

constructor(
  private conceptCardBackendApiService: ConceptCardBackendApiService,
  private conceptCardObjectFactory: ConceptCardObjectFactory
) {}

  ngOnInit() {
  }

  isLastWorkedExample() {
  }

  showMoreWorkedExamples() {
  }

}
```

#### 7. Copy the contents of the functions

Anything with `ctrl.` becomes `this.`. For example:

```js
ctrl.isLastWorkedExample = function() {
  return ctrl.numberOfWorkedExamplesShown ===
    ctrl.currentConceptCard.getWorkedExamples().length;
};
```

becomes

```js
isLastWorkedExample(): boolean {
  return this.numberOfWorkedExamplesShown ===
    this.currentConceptCard.getWorkedExamples().length;
}
```

**Note the dependency injections also get the `this.` prefix.**

In the controller.$OnInit function we have:

```js
ConceptCardBackendApiService.loadConceptCards(
              ctrl.getSkillIds()
            )
```

This will become:

```js
this.conceptCardBackendApiService.loadConceptCards(
              this.skillIds
            )
```

#### 8. Add downgrade statement

Import downgradeComponent from '@angular/upgrade/static'. Then add the following downgrade statement to the end of the file:

```js
angular.module('oppia').directive(
  'conceptCard', downgradeComponent(
    {component: ConceptCardComponent}));
```

#### 9. Change the name of the file

Rename the file from `*directive|controller.ts` to `*component.ts`. Import this component into the corresponding module page and add it in the `declarations` and `entryComponents`. You can find the corresponding module page as follows:

* For directives in the pages folder, they will be in the same sub-folder as `*.module.ts`
* For directives in the components folder, the module page is `shared-component.module.ts`


### Migrating an HTML file

This is the easier part of migration but still should be migrated carefully. Here are the migration patterns:

#### Changing `<[ ... ]>` to `{{ ... }}`

The interpolation in angular uses `{{ }}` to interpolate. So change `<[ ]>` to `{{ }}`. For example, `<li><[credit]></li>` becomes `<li>{{ credit }} </li>`.

#### Removing `$ctrl`

By default in Angular, all the variables of the class you migrated are available in HTML (unlike AngularJS where variables were prefixed by $ctrl or had to attached to the $scope). Remove all `$ctrl.` from HTML. For example, `<li ng-if="$ctrl.credits === 0"><[$ctrl.credits]></li>` becomes `<li *ngIf="credits === 0"> {{ credit }} </li>`.

#### Change `ng-if` to `*ngIf`

For example, `<li ng-if="$ctrl.credits === 0"><[$ctrl.credits]></li>` becomes `<li *ngIf="credits === 0"> {{ credit }} </li>`.

#### Change `ng-repeat` to `*ngFor`

| AngularJS | Angular2+ |
|-----|------|
|`<div class="oppia-about-credits-letter-groups three-col">` | `<div class="oppia-about-credits-letter-groups three-col">`|
|`<span ng-repeat-start="item in $ctrl.allCredits">`| `<div *ngFor="let credit of allCredits">`|
|`<[item.letter]></span>` | `<span>{{ credit.letter }}</span>` |
|`<ul ng-repeat-end>` | `<ul>`|
|`<li ng-repeat="credit in item.credits"><[credit]></li>` | `<li *ngFor="let name of credit.names">{{ name }}</li>`|
|`</ul>` | `</ul>`|
|`</div>`| `</div>`|

### Other tags

* `ng-cloak`: Remove.

* `ng-class`: Change to `ngClass`.

* `ng-show`/`ng-hide`: Follow [GeeksForGeeks](https://www.geeksforgeeks.org/what-is-the-equivalent-of-ngshow-and-nghide-in-angular-2/).

#### HTML tag attributes

If you see any HTML attribute which looks like `<div editable=<[$ctrl.edit]>`, then just change it to `<div [editable]="edit">`.

If you `ng-src`/`ng-srcset`, change it to `[src]`/`[srcset]`.

#### HTML events

All the events in HTML are available in angular. Example `onClick` becomes `(click)`, `ng-click` becomes `(click)`, and `ng-submit` becomes `(ngSubmit)`.

#### Translations

You may come across the following:

```html
<some-tag translate="I18N_VARIABLE_NAME"
	translate-values="{abc: xyz}"></some-tag>
```

Convert it like this:

```html
<some-tag [innerHTML]="'I18N_VARIABLE_NAME' | translate:{abc: xyz}">
</some-tag>
```

If there are no translate-values, simply use `"'I18N_VARIABLE_NAME' | translate"`

Please note the single-quote marks around `I18N_VARIABLE_NAME`.

#### CSS updates

There may be some style updates required to make sure that the pages look exactly like before. You can find the changes here: https://github.com/oppia/oppia/pull/9980/files#diff-1d203da36aa74eef4c39b05a27eafbaeR40-R46. Besides this, styles that contain the directive name now need to be enclosed in a `<div>` tag. For example compare [this code from before migration](https://github.com/oppia/oppia/pull/9957/files#diff-25860f544f47c16a020aff8bb0c389fdL1-L3) to the [migrated code](https://github.com/oppia/oppia/pull/9957/files#diff-45cbfaec92adcc709712a85df070f455R1-R4).

## Testing your Pull Request

1. Ensure your frontend tests pass

   Python:
   ```console
   python -m scripts.run_frontend_tests
   ```
   
   Docker:
   ```console
   make run_tests.frontend
   ```

   Note: If your migrated service involves HTTP calls and when you run the frontend test your frontend test fail for some other service (One error that might pop is `Error: No pending request to flush !`) then go ahead and migrate the failing tests for the other service too. You might have guessed that in such a case we have migrated a service which is now making HTTP calls in Angular using HttpClient but some other service that is issuing HTTP requests to this service is still testing by making calls via AngularJS HTTP module (using $httpBackend). Go through this [PR #9029](https://github.com/oppia/oppia/pull/9029/files), wherein `question-creation.service` and `question-backend-api.service` are migrated to Angular and we went ahead to change relevant tests in `questions-list.service.spec`.

2. Ensure there are no typescript errors:

   Python:
   ```console
   python -m scripts.typescript_checks
   ```

    Docker:
    ```console
    make run_tests.typescript
    ```

3. Ensure there are no linting errors:

   Python:
   ```console
   python -m scripts.linters.run_lint_checks
   ```
   
    Docker:
    ```console
    make run_tests.lint
    ```

4. Test manually. See where the directive you have migrated is being used. You can do this by seeing where it's corresponding `selector` is being used. Then check whether functionality that you have implemented works as expected (like on the develop branch). Add a screen recording of the places where the directive is used when you open your PR!

## Implementation details to refactor Object Factories

### 1. Remove certain imports

The following imports will no longer be required:

```js
import { downgradeInjectable } from '@angular/upgrade/static';
import { Injectable } from '@angular/core';
```

### 2. Change the file overview

Change the file overview to not include the term Object Factory. Instead, replace it with the word "model".

For example:

| Before | After |
|--------|-------|
|`Factory for creating new frontend instances of ParamMetadata`|`Model class for creating new frontend instances of ParamMetadata`|

### 3. Move functions from ObjectFactory class

Locate the class in the file whose name is suffixed by ObjectFactory. Move all the functions from that ObjectFactory class (except the constructor) and add them to the other class in the file. Add `static` in front of all the functions you moved.

Before:

```js
export class ParamMetadata {
  action: string;
  paramName: string;
  source: string;
  sourceInd: string;
  constructor(
      action: string, paramName: string, source: string, sourceInd: string) {
    this.action = action;
    this.paramName = paramName;
    this.source = source;
    this.sourceInd = sourceInd;
  }
}

@Injectable({
  providedIn: 'root'
})
export class ParamMetadataObjectFactory {
  createWithSetAction(
      paramName: string, source: string, sourceInd: string): ParamMetadata {
    return new ParamMetadata(
      ExplorationEditorPageConstants.PARAM_ACTION_SET, paramName, source,
      sourceInd);
  }

  createWithGetAction(
      paramName: string, source: string, sourceInd: string): ParamMetadata {
    return new ParamMetadata(
      ExplorationEditorPageConstants.PARAM_ACTION_GET, paramName, source,
      sourceInd);
  }
}
```

After:

```js
export class ParamMetadata {
  action: string;
  paramName: string;
  source: string;
  sourceInd: string;
  constructor(
      action: string, paramName: string, source: string, sourceInd: string) {
    this.action = action;
    this.paramName = paramName;
    this.source = source;
    this.sourceInd = sourceInd;
  }

  static createWithSetAction(
      paramName: string, source: string, sourceInd: string): ParamMetadata {
    return new ParamMetadata(
      ExplorationEditorPageConstants.PARAM_ACTION_SET, paramName, source,
      sourceInd);
  }

  static createWithGetAction(
      paramName: string, source: string, sourceInd: string): ParamMetadata {
    return new ParamMetadata(
      ExplorationEditorPageConstants.PARAM_ACTION_GET, paramName, source,
      sourceInd);
  }
}

@Injectable({
  providedIn: 'root'
})
export class ParamMetadataObjectFactory {

}
```

Next, remove the @Injectable and the object factory class. Specifically, remove the code that looks like this:

```js
@Injectable({
  providedIn: 'root'
})
export class ParamMetadataObjectFactory {

}
angular.module('oppia').factory(
  'ParamMetadataObjectFactory',
  downgradeInjectable(ParamMetadataObjectFactory));

```

### 4. Remove the imports and class listings / instances

Remove any references to the object factory from:

- angular-service.index.ts
- oppia-angular-root.component.ts
- UgradedServices.ts

### 5. Rename the file

The file you are working on will be named either `*-object.factory.ts` or `*ObjectFactory.ts`. You need to remove the object factory part and add .model.ts instead. For example, `PlaythroughObjectFactory.ts` should be renamed to `playthrough-object.model.ts and `skill-summary-object.factory.ts` should be renamed to `skill-summary.model.ts`.

### 6. Change the import (as you have changed the name of the file) and its usage around the codebase.

**Make sure to search the codebase for the function name to make sure you find all usages.**

For example, let one of the functions that you moved before (in step 3) be `createWithGetAction`.

#### Pattern 1: ParamMetadataObjectFactory.createWithGetAction(...)

First, make sure `ParamMetadata` has been imported:

```js
import ParamMetadata from param-metadata.model.ts
```

Next, change `ParamMetadataObjectFactory.createWithGetAction()` to `ParamMetadata.createWithGetAction(...)`. Do this for all functions, and then remove any other `ParamMetadataObjectFactory` references left in the file.

#### Pattern 2. this.paramMetadataObjectFactory.createWithGetAction(...)

Make sure that ParamMetadata has been imported. Then change `this.paramMetadataObjectFactory.createWithGetAction(...)` to `ParamMetadata.createWithGetAction(...)`. Do this for all functions, and remove `paramMetadataObjectFactory` from the constructor.

### 7. Changing the spec file

Each ``*-object.factory.ts` will have its corresponding spec file named `*-object.factory.spec.ts`. You will need to follow the procedure mentioned in step 6 (the previous step), to refactor the spec as well. Note that in spec file `ParamMetadataObjectFactory` could be shortened to `pmof`, so searching by the function name in the spec file will be more accurate.

**PRs for reference: [#10701](https://github.com/oppia/oppia/pull/10701/), [#10713](https://github.com/oppia/oppia/pull/10713/).**

## FAQ

### Common Issues with Migrating Services

1. Front-end tests fail. This can for various reasons, but the most common one is return types. You will get errors like: ‘a’ is not defined on an object of type ‘X’. Try console logging the object you are receiving actually has the property you’re calling and adjust accordingly. This will mostly happen with HttpResponse objects.

### Common Issues with Migrating Directives

1. Error like this:

   ```text
   'some-selector' is not a known element:
   1. If 'some-selector' is an Angular component, then verify that it is part of this module.
   2. 2. If 'some-selector' is a Web Component then add 'CUSTOM_ELEMENTS_SCHEMA' to the '@NgModule.schemas' of this component to suppress this message.
   ```

   This can occur for a couple of reasons:

   * The corresponding external Angular module is not yet integrated into the codebase, e.g. For `ngModel`, you need `FormsModule`.
   * It is another un-migrated directive. You need to wrap it in an Angular wrapper and import it into your current module. Do it via the shared component module. Use [#9237](https://github.com/oppia/oppia/pull/9237/files) for reference
   * The Angular module has a different selector i.e `md-card` becomes `mat-card`

### Why do we need @Injectable decorator?

There are two reasons:

* Our app is in hybrid state i.e. half Angular and half AngularJS, and we need to downgrade each of our services to AngularJS so that our application runs smoothly.
* To define a class as a service, Angular uses the @Injectable() decorator to provide the metadata that allows Angular to inject it into a component as a dependency. When we provide the service at the root level, Angular creates a single, shared instance of the service and injects it into any class that asks for it. Registering the provider in the @Injectable() metadata also allows Angular to optimize an app by removing the service from the compiled app if it isn't used.

### Why do we need `$rootScope.$applyAsync` with HTTP requests?

As you can see in the example here, the directive updates the value when the promise is resolved:

```js
TopicViewerBackendApiService.fetchTopicData(ctrl.topicName).then(
  function(topicDataDict) {
    ctrl.topicId = topicDataDict.topic_id;
    ctrl.canonicalStoriesList = topicDataDict.canonical_story_dicts;
    ctrl.degreesOfMastery = topicDataDict.degrees_of_mastery;
    ctrl.skillDescriptions = topicDataDict.skill_descriptions;
    ctrl.subtopics = topicDataDict.subtopics;
    $rootScope.loadingMessage = '';
    ctrl.topicId = topicDataDict.id;
```

Everything was working fine before the migration, but after migration, we noticed that all the values in the above-mentioned function were updated but not propagated to the corresponding HTML file. Searching online yielded [a Stack Overflow post](https://stackoverflow.com/a/21659051) which mentions that:

> Yes, AngularJS's bindings are "turn-based", they only fire on certain DOM events and on calls to `$applyAsync/$digest`. There are some useful services like `$http` and `$timeout` that do the wrapping for you, but anything outside of that requires calls to either `$applyAsync` or `$digest`._

The `$digest` cycle is not running after we've upgraded `$http` to `HttpClient`, so we add `$rootScope.$applyAsync` to explicitly ask Angular to propagate the changes to our HTML.

### What is TestBed?

When a service has a dependent service, DI (dependency injector) finds or creates that dependent service. And if that dependent service has its own dependencies, DI finds or creates them as well. To quote from the Angular docs, "As a service tester, you must at least think about the first level of service dependencies but you can let Angular DI do the service creation and deal with constructor argument order when you use the TestBed testing utility to provide and create services."

### Some Common Migration Queries

1. What are Promises?

   Promises are exactly what they sound like. In the simplest words, they are a promise to the developer that things will work, what to do when they work, and also when they don’t work.

	 They can have three states:

	 * Resolved: The caller of the promise has executed as expected.
	 * Rejected: The caller of the promise didn’t execute as expected
	 * Pending: The caller is yet to be executed

	 What exactly are the `resolve` and `reject` that promises accept? They are simply function calls. For example, `successCallback(abcd)` will give parameter `abcd` to the resolve function when the promise caller is called.

	 How is it structured? A promise is called using a `.then()` statement after the function. Note that you cannot put this after any function, only one that returns a promise. Then functions follow. If there is only one function, it is the resolve function. If there are two functions, they are called resolve and reject, respectively. The reject function is used mostly for error handling and unexpected behaviour

	 For more reading check out the [MDN Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)!


2. What is `rootScope`?

   Angular has scopes. `$scope` is a local scope, which is bound to exactly one controller. It can local properties and functions of the controller. `$rootScope` on the other hand, is the global scope and can be accessed from everywhere.

	What is `$rootScope.$applyAsync()` and why do we use it? `$rootScope.$applyAsync` is used to update the global properties and variables so that the new state can be used by the function where it is called. As to why it is not updated automatically, the reason is that the Angular DOM basically runs in cycles, and apply causes the changes to be saved. Mostly this is done automatically, but in some cases, we have to do it explicitly. Remember that this function will go in the resolve of the promise! This is because we want the variables to get to their new state in case of expected behaviour.

	For more reference, see [the AngularJS docs on scopes](https://docs.angularjs.org/guide/scope).


3. How do I assign types in the Angular file?

	 Follow a trail. Some are really simple, but they all follow the same pattern. Keep following the variable through different references to see what type to assign. You can even use other references of that variable. For example, if you wanted to assign a type to a function that returned `WindowRef.nativeWindow`, you would go to the `window-ref.service` file and see that `nativeWindow` returned the `_window` object which had a type `Window`.

	Other times it might be obvious from the name. For example, `SkillList` is obviously an array of Skills. However, double-check these!

	The final way is to use a console log statement. This is good for complicated data types. Run the local development server and log the value whose type you want to know. You’ll see something of type Object with certain properties. Search for these properties in the codebase to find out what type it is!

4. What are fakeAsync() and flushMicrotasks() and why do we use them?

   For this we need to understand why being synchronous is a problem for tests. Compilers don’t compile code line by line. Instead, they push processes into a queue as they come and the resulting processes are pushed once the first processes end. What this means is that a process whose parent was called earlier may be executed after another whose parent was called later due to how much time the parent processes took. To make an asynchronous function synchronous we use fakeAsync combined with flushMicrotasks. FakeAsync creates a fake asynchronous zone wherein you can control process flow. When flushMicrotasks is called, it flushes the task queues, i.e it waits for the processes to leave the queue before proceeding further. Then, the tests are consistent!

5. What are MockServices/FakeServices that are in the codebase?

   MockServices are basically just used to imitate real services and provide functionality for tests via inorganically-made function copies of the service. These are faster but don’t test services, so be wary of using them. The reason we use them is that we want to want to test the current service, not the other service, so we just use a small shell to provide the functionality we want.

6. How can I have constants shared across Angular and AngularJS code?

   The Angular 2+ constants file is named _*.constants.ts_ whereas the AngularJS equivalents of those constants must be in a separate file named _*.constants.ajs.ts_. The constants must be first declared in the Angular constants file and then be declared in the corresponding AngularJS constants file by importing the constants class from the Angular constants file and using that class's properties to declare the AngularJS equivalents. Then import the AngularJS constants class in the module and add it to the `providers` list of the `NgModule`.

   For example, if there is a constant named `SKILL_EDITOR_CONSTANT` that needs to be used in skill editor, then add that constant to the `SkillEditorConstants` class of the file _skill-editor-page.constants.ts_ like this:

   ```js
   export class SkillEditorPageConstants {
     ...
     public static SKILL_EDITOR_CONSTANT = 'constant_value';
     ...
   }
   ```

   Now, add the constant to the AngularJS file as well:

   ```js
   import { SkillEditorPageConstants } from
     'pages/skill-editor-page/skill-editor-page.constants.ts';

   ...
   oppia.constant('SKILL_EDITOR_CONSTANT', SkillEditorPageConstants.SKILL_EDITOR_CONSTANT);
   ...
   ```

   And now you can use the constant in both your AngularJS as well as Angular parts of the code!

## Contact

For any queries related to angular migration, please don't hesitate to reach out to **Srijan Reddy (@srijanreddy98)**.
