


## Overview

Angular is an app-design framework and development platform for creating efficient and sophisticated apps.

Currently, the project is in a hybrid state where we have both Angular and AngularJS. This makes our application slow and bulky. The codebase has a duplication of libraries since many of the AngularJS libraries are not compatible with Angular. This project aims to migrate the entire codebase to Angular. The benefits of doing this are:
* Improved Developer Experience: 
  * Developing when the application is a hybrid state opens us to a whole host of complicated errors which are in some cases not possible to be solved.
  * Angular is being actively maintained and comes out with a lot of new features that aid in developing new features.
* Improved User Experience:
  * When the codebase is completely migrated, the developers will focus their efforts on making new features for the website rather than fixing nasty errors that pop up because of the hybrid state.
  * Decrease in page loading times as a result of not bundling two SPA frameworks.
  * Better application performance in general.

The project plan will be iterative in nature. We will migrative the services first and then the controllers and directives. The services would be migrated in the dependency order i.e if A depends on B and B depends on C, we will migrate in the order C, B and A.

### Testing videos

**Note: Angular Migration Pull Requests must be accompanied with a video showing the before and after effects of their change to ensure that nothing is broken. This ensures faster review and lower risks of reverted PRs**

## Angular Migration Tracker

The [angular migration tracker](https://docs.google.com/spreadsheets/d/1L9Udn-XT6Lk1qaTBUySTw1AnhvQMR-30Qry4rfd-Ovg/edit?usp=sharing) holds the record of which services which are to be migrated. The issue [#8472](https://github.com/oppia/oppia/issues/8472) holds a subset of those services that can be migrated without any major blockers.

## Implementation details to migrate services

1. Import following dependencies
  
   ```
   import { downgradeInjectable } from '@angular/upgrade/static';
   import { Injectable } from '@angular/core';
   ```

2. If the services uses `$http`, import `HttpClient` as a dependency:
   ```
   import { HttpClient } from '@angular/common/http';
   ```

3. Change angularJS factory definition to Angular class definition as follows
   ```
   angular.module('oppia').factory('ServiceName',['dependency1', function(dependency1) {
   ```

   to

   ```
   import { dependency1 } from ... // to be added at the top of the file
   ..
   ..
   export class ServiceName {
   ```

4. Add decorator above the class definition
   ```
   @Injectable({
     providedIn: 'root'
   })
   export class ServiceName {
   ...
   ```

5. Add a constructor for the class and inject the dependencies
   ```
   constructor(
       private service1: Service1,
       private service2: Service2) {}
   ```

6. Change `$http.get` requests in service as follows

   (a) Change `$http.get` to `this.http.get`
   ```
   $http.get(url).then(function(response) {
     dataDict = angular.copy(response.data);
   ```
   to
   ```
   this.http.get(
      url).toPromise().then(
       (response) => {

   ```
   The `dataDict` is not required in Angular services. You can directly use the `response` variable.

   (b) Search in the  codebase where the service is used to obtain results from get requests and change 
   `response.data` to `response`.

   (c) Return the `errorCallback` (the reject function) with `errorResponse.error.error` as follows:
  
   ```
   (errorResponse) => {
     errorCallback(errorResponse.error.error);
   }
   ```

   (d) Add `$rootScope.apply()` in the controller/directive that is resolving the http request similar to how it is 
   added [here](https://github.com/oppia/oppia/pull/8427/files#diff-ecf6cefd0707bcbafeb6a0b4009aa60cR78). You can find this by doing a simple search of the function name in service where get request is handled.
      To do this, make a global search in the code-base for the function. eg. if the service is `SkillBackendApiService` and the function in which the call is made is `fetchSkill`. The search the code-base for `SkillBackendApiService.fetchSkill`. You will find instances like the following:
   ```
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

7. Change `$http.put` or `$http.post` requests as follows

   (a) Change `$http.post/put` to `this.http.post/put`
   ```
   $http.post(url).then(function(response) {
     ...
   ```
   to
   ```
   this.http.post(
     url).toPromise().then(
      (response) => {...;
   ```

   (b) Add `$rootScope.apply()` in the controller/directive that is resolving the HTTP request similar to how it is 
   added [here](https://github.com/oppia/oppia/pull/8427/files#diff-ecf6cefd0707bcbafeb6a0b4009aa60cR78). You can find this by doing a simple search of the function name in service where get request is handled.

8. If you are migrating a service that is named as `.*-backend-api.service.ts` then please return a domain object and not a dict in the `successCallback` function. For example take a look at this change [PR #9505](https://github.com/oppia/oppia/pull/9505/files#diff-05de50229b44c01bdaeac172928b514dR64), where the domain object is created via an object factory and this is sent ahead. You also need to change the piece of code where this response is used because the response is now a domain object instead of a dict. If there is no specific object factory to alter the response to a domain object, create one similar to how it is done in this [change](https://github.com/oppia/oppia/pull/9570/files#diff-09e3c3999c18dabdf2ddedf6e3e250f8R1).
Topic Domain Objects need to contain properties that are being read from the backend. So, the Topic Domain Object does not depend on the service being migrated, but the expected return value of the function. For example, in `SkillBackendApiService`, the function `fetchSkill` will clearly return a `Skill` object. Note that `SkillObjectFactory.ts` already exists, so we don't need to create it. But if there is no corresponding Object Factory, you need to create one similar to how `SkillObjectFactory` is created. So, we take the response from the backend and instead of `successCallback(response)`, we resolve `successCallback(SkillObjectFactory.createFromBackendDict(response))`. This passes the frontend `Skill` object to functions that call `fetchSkill` when the promise gets resolved.  
However, there is more to it. Since before you migrated the file, the calling functions were expecting a backend dict object, the references need to be changed as well.  
To do this, do a global search in the code-base for the function, eg. `SkillBackendApiService.fetchSkill` and refactor the code inside the resolve function to reflect that the parameter is now a `Skill` object and not a backend dict object.
Please note that interfaces/properties in Object Factories and the `.*-backend-api.service.ts` could be in snake_case, please surround them with single quotes as in `'some_property'`. Except for these two categories, all the properties inside all other files should be camel case: `someProperty`.

9. For functions in the service, add type definitions for all the arguments as well as return values. 
**Note:** For complex types or some type that is being used over functions or files we can declare interface or export interface (if it has to be imported over files). For example in the file [rating-computation.service.ts](https://github.com/oppia/oppia/blob/develop/core/templates/components/ratings/rating-computation/rating-computation.service.ts) we have an export interface to declare the type RatingFrequencies. In the same file, we also have a function named static, which is used by the functions of the class itself. 

10. For functions which are private to the service (used as helper functions) add the private keyword for those functions.

11. In  the file end add
    ```
    angular.module('oppia').factory('ServiceName', downgradeInjectable(ServiceName));
    ```



 This [pull request](https://github.com/oppia/oppia/pull/10693/files) can be used as a reference.

## Implementation details to migrate tests

1. Remove all `beforeEach()` blocks and any other service that is not needed in the test file.

2. Convert all the function keywords to () => (fat arrow functions) like
   ```
   describe('abc', function() { ... });
   ```
   to
   ```
   describe('abc', () => { .. });
   ```

3. Import TestBed in your spec file
   ```
   import { TestBed } from '@angular/core/testing';

   import { ServiceName } from ...
   ```

   If your test is for a service that makes HTTP requests, you also need to import the following
   ```
   import { HttpClientTestingModule, HttpTestingController } from
      '@angular/common/http/testing';
   import { TestBed, fakeAsync, flushMicrotasks } from '@angular/core/testing';
   ```

4. Add a beforeEach block that creates an instance of service you want to test
   ```
   beforeEach(() => {
     serviceInstance = TestBed.get(ServiceName);
   });
   ```

   (a) If your spec file needs any pipe (filters in angular), import them and add it to the providers in the 
   TestBed configuration
   ```
   beforeEach(() => {
     TestBed.configureTestingModule({
       providers: [CamelCaseToHyphensPipe, ConvertToPlainTextPipe] // Any pipe that is required
     });
     instance = TestBed.get(ServiceName);
   ```

   (b) If your spec file tests service that makes HTTP requests, you need to make a HttpClientTestingModule and 
   add afterEach statement to check there are no pending requests after each test.
   ```
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

6. If your spec file is for a service that makes HTTP requests then

   (a) Convert each individual test defined in it block as follows
   ```
   it('should ...', fakeAsync(() => {
   .
   .
   }));
   ```

   (b) Change the test to create an HTTP request via httpTestingController (taking an example from the `topic-viewer-backend-api.service.spec.ts`)
   ```
   $httpBackend.expect('GET', '/topic_data_handler/0').respond(
     sampleDataResults);
   TopicViewerBackendApiService.fetchTopicData('0').then(
     successHandler, failHandler);
   $httpBackend.flush();
   ```

   to

   ```
   topicViewerBackendApiService.fetchTopicData('0').then(
    successHandler, failHandler);
   var req = httpTestingController.expectOne(
               '/topic_data_handler/0');
   expect(req.request.method).toEqual('GET');
   req.flush(sampleDataResults);

   flushMicrotasks();
   ```

## Implementation details to migrate directives

There are two parts to this migration. (The ts file and the HTML file)
Migrating directives requires the contributor to be aware of the context

### Migrating the logic part (ts file):
Here are the steps to migrate the logic part
#### 1. Create a basic component in the directive file:
Import Component to the file.
`import { Component } from '@angular/core';`

The take a look at the directive declaration. For example if the directive is declared like this:
```
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

then add the following at the end of the file.
```
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
* The template of the directive (in 99% of the cases) exists in the same folder as the directive.ts file.

#### 2. Import and inject the dependencies:
```
controller: [
        '$scope', '$rootScope',
        'ConceptCardBackendApiService', 'ConceptCardObjectFactory',
```

The first two dependencies are interesting ones. They don't have a direct equivalent in angular. In most of the cases, you will find something like `$scope.someVariable = `, `$scope.$onDestroy`, `$scope.$onInit`, and `$rootScope.$applyAsync()`. In other cases contact your onboarding mentor or @srijanreddy98.

Now, we have the other two dependencies ('ConceptCardBackendApiService', 'ConceptCardObjectFactory'). These are called injectables as they are "injected". So these go into your constructor.

First, import these two services into the directive.

```
import { ConceptCardBackendApiService } from 'service/some-service.ts';
import { ConceptCardObjectFactory } from 'services/some-other-service.ts';
```

Create a constructor for the class you made in the previous step and add those injectables there:
```
export class ConceptCardComponent {

constructor(
  private conceptCardBackendApiService: ConceptCardBackendApiService,
  private conceptCardObjectFactory: ConceptCardObjectFactory
) {}

}
```
Sometimes, you will also see dependencies like $window, $log, $timeout etc.
`For $window`: Use `window-ref.service.ts`
In the constructor, with other dependencies, inject `WindowRef`
```
constructor(
...
private windowRef: WindowRef
) {}
```
Then instead of `window`, use `windowRef.nativeWindow`, eg `windowRef.nativeWindow.location.href` etc
Also, instead of `location` for setting urls, use `location.href`

`For $timeout`: Use `setTimeout`

`For $log`: Use `logger.service.ts`

**Notice the casing very carefully. The service is ConceptCardBackendApiService but its instance is called conceptCardBackendApiService (with a small c)**

#### 3. Adding OnInit / OnDestroy:
You will notice that in almost every directive you have `ctrl.$onInit` and/or `ctrl.$onDestroy`. The equivalent of this in angular is `ngOnInit` and `ngOnDestroy`.
First, you need to import OnInit from '@angular/core'; Then implement it in the class. So change the class declaration to this:
`export class ConceptCard implements OnInit {` and add an `ngOnInit() {}` below the constructor.
After this step the component class would look like this:

```
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

Similarly, do this for `onDestroy`

#### 4. Changing the bindToController:
If there is some value in bindToController then import `Input` from `@angular/core`;

There are four "syntaxes" that you could run into when trying to migrate bindToController:
1. `'@'`
2. `'<'`
3. `'='`
4. `'&'`

##### The syntax for `'@'` is pretty straight forward:
```
  layoutType: '@',
```
will change to
```
  @Input() layoutType: string;
```
**Note that `'@'` is always a string but `'<'` can be of any type (string, number, object or custom types).**

##### The syntax for '<'.
```
  layoutAlignType: '<',
```
changes to 
```
  @Input() layoutAlignType: string;
```
(The type of layoutAlignType being string is an example. please be aware of the type used in your case).
Take a look at the directive name (in this case it is conceptCard). Now do a global search for `<concept-card`. (Note the change to snake_case and the extra '<' at the beginning).
When you get the results, in each and every case you will find something like `layout-align-type=layoutAlign`.
**If it is an angularjs template**, change that to `[layout-align-type]=layoutAlign`.
(Notice in the component it was `layoutAlignType` but in HTML it is [layout-align-type]. The camelCase to kebab-case change is required when the template is a template of an angularjs component/directive).

**Otherwise, change it to `[layoutAlignType]=layoutAlign`.**

**If you find something like `layout-align-type="center center"`, leave it as it is, do not change it. The `[]` syntax can only be used with variables. If the attribute is not surrounded by `[]` and the attribute value is surrounded by double quotes, that means the passed value is a string.** 

##### The changes required for `'&'`:

You will find `'&'` with a syntax that looks like `getSkillIds: '&skillIds',`. This requires some significant changes so please follow the next steps very carefully:

First, change the 
```
getSkillIds: '&skillIds',
``` 
to 
```
@Input() skillIds: Array<string>,
```
Note: If the syntax looks like `skillIds: '&'`, then just change it to:
```
@Input() skillIds: Array<string>,
``` 

(Array<string> is an example. please be aware of the type used in your case).
Then change all cases of `ctrl.getSkillIds()` to `this.skillIds`. (Notice the parenthesis were also removed).

Take a look at the directive name (in this case it is conceptCard). Now do a global search for `<concept-card`. (Note the change to kebab-case and the extra '<' at the beginning).
When you get the results, in each and every case you will find something like `skill-ids=skillIds`.

**If the occurence is in an angularjs template** (i.e. the corresponding .ts file for the html has not been migrated), change that to `[skill-ids]=skillIds`.
(Notice in the component it was `skillIds` but in HTML it is [skill-ids]. The camelCase to kebab-case change is required when the template is a template of an angularjs component/directive). 

**Otherwise, change it to `[skillIds]=skillIds`.**

**Note: If you find something like `skill-type="supersonic"`, leave it as it is, do not change it. The `[]` syntax can only be used with variables. If the attribute is not surrounded by `[]` and the attribute value is surrounded by double quotes, that means the passed value is a string.** 

Understanding binding interpolation:
1.  Binding is a way to share information between different directives using variables that pass values. Variables are passed via selectors of other directives present in the HTML file of the directive we are working on
    
2.  Interpolation is simply a way to make sure we pass variables and not values in our HTML. Eg. How do we know if in `<dir-name abc=”xyz”>`, `xyz` is a string or a variable? So for variables, we use interpolation -> {{ }}. Hence, for variables, we use two methods:
	a. `<dir-name [abc]="xyz">` The `[]` assumes that the string is a variable.
	b. `<dir-name abc="{{ xyz }}">`.
	We use method `a` in all cases except if the variable is interspersed with other text. eg. `<dir-name abc="The boy has {{ count }} apples">`
    
3.  Do not use interpolation with properties marked with [prop], or events. These automatically assume that a variable is passed

##### The syntax for `=`:

In most cases, the `=` is the same as `<` when looked at from an angular2+ perspective. So just follow the steps given for `<` migration.


#### 5. Start separating the other functions:

Take a look at the directive code:
```
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
```
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

#### 6. Create class members (variables):
Till now we only looked at `ctrl.someVariable = function()`. Now we will look at all the other cases.
Looking at the directive code again:
Take a look at the directive code:
```
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
So looking at all the other `ctrl.` declaration we find:
`ctrl.numberOfWorkedExamplesShown, ctrl.currentConceptCard, ctrl.explanationIsShown, ctrl.numberOfWorkedExamplesShown++, ctrl.conceptCards, ctrl.loadingMessage`, etc.

Now we have to define them as class members. In order to do so just remove `ctrl.` in front of the variable and add them to the class above the constructor.
```
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

#### 7. Now we copy the contents of the functions:
It very simple, anything with `ctrl.` becomes `this.`.
For example:
```
ctrl.isLastWorkedExample = function() {
  return ctrl.numberOfWorkedExamplesShown ===  
    ctrl.currentConceptCard.getWorkedExamples().length;
};
```
becomes

```
isLastWorkedExample(): boolean {
  return this.numberOfWorkedExamplesShown ===
    this.currentConceptCard.getWorkedExamples().length;
}
```
**Note the dependency injections also get the `this.` prefix**
in the controller.$OnInit function we have 
```
ConceptCardBackendApiService.loadConceptCards(
              ctrl.getSkillIds()
            )
```
This will become:
```
this.conceptCardBackendApiService.loadConceptCards(
              this.skillIds
            )
```

#### 8. Add downgrade statement at the end of the file and import downgradeComponent from '@angular/upgrade/static'
   ```
   angular.module('oppia').directive(
     'conceptCard', downgradeComponent(
       {component: ConceptCardComponent}));
   ```

#### 9. Change the name of the file from `*directive|controller.ts` to `*component.ts`. Import this component into the corresponding module page and add it in the `declarations` and `entryComponents`. 
You can find the corresponding module page as follows:
For directives in the pages folder, they will be in the same subfolder as `*.module.ts`
For directives in the components folder, the module page is `shared-component.module.ts`


### Migrating the HTML file:

This is the easier part of migration but still should be migrated carefully:
Here are the migration patterns:

#### Changing `<[ ... ]>` to `{{ ... }}`

The interpolation in angular uses `{{ }}` to interpolate. So change `<[ ]>` to `{{ }}`.

`<li><[credit]></li>` becomes `<li>{{ credit }} </li>`

#### Removing $ctrl ($ctrl -> )
By default, all the variables of the class you migrated are available in HTML in angular (unlike angularjs where it was prefixed by $ctrl or had to attached to the $scope). Remove all `$ctrl.` from html.

`<li ng-if="$ctrl.credits === 0"><[$ctrl.credits]></li>` becomes `<li *ngIf="credits === 0"> {{ credit }} </li>`

#### Change ng-if -> *ngIf

`<li ng-if="$ctrl.credits === 0"><[$ctrl.credits]></li>` becomes `<li *ngIf="credits === 0"> {{ credit }} </li>`

#### Change ng-repeat to *ngFor
| AJS | ng2+ |
|-----|------|
|`<div class="oppia-about-credits-letter-groups three-col">` | `<div class="oppia-about-credits-letter-groups three-col">`|
|`<span ng-repeat-start="item in $ctrl.allCredits">`| `<div *ngFor="let credit of allCredits">`|
|`<[item.letter]></span>` | `<span>{{ credit.letter }}</span>` |
|`<ul ng-repeat-end>` | `<ul>`|
|`<li ng-repeat="credit in item.credits"><[credit]></li>` | `<li *ngFor="let name of credit.names">{{ name }}</li>`|
|`</ul>` | `</ul>`|
|`</div>`| `</div>`|

### Other tags
ng-cloak -> Remove

ng-class -> ngClass

ng-show/ng-hide -> [GeeksForGeeks](https://www.geeksforgeeks.org/what-is-the-equivalent-of-ngshow-and-nghide-in-angular-2/)

#### HTML tag attributes

If you see any HTML attribute which looks like this:
`<div editable=<[$ctrl.edit]>`, then just change it to `<div [editable]="edit">`

If you ng-src/ng-srcset, change it to [src]/[srcset] .

#### HTML events:

All the events in HTML are available in angular. Example onClick -> (click), ng-click -> (click), ng-submit -> (ngSubmit)

#### Translations:
You may come across the following:
```
<some-tag translate="I18N_VARIABLE_NAME"
	translate-values="{abc: xyz}"></some-tag>
```
Convert it like this:
```
<some-tag [innerHTML]="'I18N_VARIABLE_NAME' | translate:{abc: xyz}">
</some-tag>
```
If there are no translate-values, simply use `"'I18N_VARIABLE_NAME' | translate"`

Please note the single-quote marks around `I18N_VARIABLE_NAME`
#### CSS updates
There may be some style updates required to make sure that the pages look exactly like before.

You can find the following changes here: https://github.com/oppia/oppia/pull/9980/files#diff-1d203da36aa74eef4c39b05a27eafbaeR40-R46

Besides this, styles that contain the directive name now need to be enclosed in a `<div>` tag.

eg: Original: https://github.com/oppia/oppia/pull/9957/files#diff-25860f544f47c16a020aff8bb0c389fdL1-L3

Modified: https://github.com/oppia/oppia/pull/9957/files#diff-45cbfaec92adcc709712a85df070f455R1-R4

## Testing your Pull Request

1. Ensure your frontend tests pass
   ```
   python -m scripts.run_frontend_tests
   ```

   Note: If your migrated service involves HTTP calls and when you run the frontend test your frontend test fail for some other service (One error that might pop is `Error: No pending request to flush !`) then go ahead and migrate the failing tests for the other service too. You might have 
   guessed that in such case we have migrated a service which is now making HTTP calls in Angular using HttpClient 
   but some other service that is issuing HTTP requests to this service is still testing by making calls via 
   AngularJS HTTP module (using $httpBackend). Go through this [PR #9029](https://github.com/oppia/oppia/pull/9029/files), 
   wherein `question-creation.service` and `question-backend-api.service` are migrated to Angular and we went 
   ahead to change relevant tests in `questions-list.service.spec`.

2. Ensure there are no typescript error
   ```
   python -m scripts.typescript_checks
   ```

3. Ensure there are no linting errors
   ```
   python -m scripts.linters.pre_commit_linter
   ``
 4. Manual testing
	 See where the directive you have migrated is being used. You can do this by seeing where it's corresponding `selector` is being used. Then check whether functionality that you have implemented works as expected (like on the develop branch). Add a screen recording of the places where the directive is used when you open your PR!


## Implementation details to refactor Object Factories:

### 1. Remove the following imports:

The following imports will no longer be required.

```
import { downgradeInjectable } from '@angular/upgrade/static';	
import { Injectable } from '@angular/core';
```

### 2. Change the file overview
Change the file overview to not include the term Object Factory. Instead, replace it with the word "model".

eg:
| Before | After |
|--------|-------|
|`Factory for creating new frontend instances of ParamMetadata`|`Model class for creating new frontend instances of ParamMetadata`|

### 3. Move functions from ObjectFactory class.

Locate a class in the whose name is suffixed by ObjectFactory. Move all the functions from that ObjectFactory class (except the constructor) and add them to the other class in the file. Add static in front of all the functions you moved.

Before:
```
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
After
```
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
Remove the @Injectable and the object factory class after this.
Remove these:
```
@Injectable({
  providedIn: 'root'
})
export class ParamMetadataObjectFactory {

}
angular.module('oppia').factory(
  'ParamMetadataObjectFactory',
  downgradeInjectable(ParamMetadataObjectFactory));

```

### 4. Remove the imports and class listings/ instantiation from the following files:
- angular-service.index.ts
- oppia-angular-root.component.ts
- UgradedServices.ts

### 5. Rename the file.

The file you would be working on will be named either `*-object.factory.ts` or `*ObjectFactory.ts`. You need to remove the object factory part and add .model.ts instead. For example, `PlaythroughObjectFactory.ts` should be renamed to `playthrough-object.model.ts and `skill-summary-object.factory.ts` should be renamed to `skill-summary.model.ts`.

### 6. Change the import (as you have changed the name of the file) and its usage around the codebase.

Patterns that will change:
** Make sure to search with the function name**
For example, let one of the functions that you moved before (in step 3) be `createWithGetAction`.

#### Pattern 1. ParamMetadataObjectFactory.createWithGetAction(...);

import ParamMetadata from param-metadata.model.ts

Change `ParamMetadataObjectFactory.createWithGetAction()` to `ParamMetadata.createWithGetAction(...)`;

Do this for all functions.

Remove any other ParamMetadataObjectFactory left in the file.

#### Pattern 2. this.paramMetadataObjectFactory.createWithGetAction(...);

Make sure that ParamMetadata has been imported.

Change `this.paramMetadataObjectFactory.createWithGetAction(...)` to `ParamMetadata.createWithGetAction(...)`;

Do this for all functions.

Remove paramMetadataObjectFactory from constructor.

### 7. Changing the spec file:

Each *-object.factory.ts will have its corresponding spec file name *-object.factory.spec.ts. You will need to follow the procedure mentioned in step 6,i.e. the previous step, to refactor the spec as well. Note that in spec file ParamMetadataObjectFactory could be shortened as `pmof`. So searching by function name in the spec file will be more accurate.

**PR's for reference: [#10701](https://github.com/oppia/oppia/pull/10701/), [#10713](https://github.com/oppia/oppia/pull/10713/)**

## FAQ

**Common Issues with Migrating Services**
1. Front-end tests fail
    This can for various reasons, but the most common one is return types. You will get errors like: ‘a’ is not defined on an object of type ‘X’. Try console logging the object you are receiving actually has the property you’re calling and adjust accordingly. This will mostly happen with HttpResponse objects.

**Common Issues with Migrating Directives**

1. Error like this:
 ```
 'some-selector' is not a known element: 
 1. If 'some-selector' is an Angular component, then verify that it is part of this module. 
 2. 2. If 'some-selector' is a Web Component then add 'CUSTOM_ELEMENTS_SCHEMA' to the '@NgModule.schemas' of this component to suppress this message.
 ```
 This can occur for a couple of reasons:
	 a. The corresponding external Angular module is not yet integrated into the code-base eg. For `ngModel`, you need the `FormsModule`
	b. It is another unmigrated directive. You need to wrap it in an Angular wrapper and import it into your current module. Do it via the shared component module. Use [#9237](https://github.com/oppia/oppia/pull/9237/files) for reference
	c. The Angular module has a different selector i.e `md-card` becomes `mat-card`


**Why do we need @Injectable decorator?**

The first line is needed since our app is in hybrid state i.e half angular and half AngularJS and we need to downgrade each of our services to AngularJS so that our application runs smoothly. The second line is needed as a decorator in every service. To define a class as a service, Angular uses the @Injectable() decorator to provide the metadata that allows Angular to inject it into a component as a dependency. 
For any class that is to be used as service, we need to add the following decorator for the above reason.
When we provide the service at the root level, Angular creates a single, shared instance of the service and injects it into any class that asks for it. Registering the provider in the @Injectable() metadata also allows Angular to optimize an app by removing the service from the compiled app if it isn't used. There are two other methods for registering a service but we’ll go with the one described above.

**Why do we need `$rootScope.$applyAsync` with HTTP requests?**

As you can see in the link here, the directive updates the value when the promise is resolved.
```
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
Everything was working fine before the migration, but after migration, we noticed that all the values in the above-mentioned function were updated but not propagated to the corresponding HTML file. Searched online gave [stackoverflow](https://stackoverflow.com/a/21659051) link which mentions four points of which one is

_Yes, AngularJS's bindings are "turn-based", they only fire on certain DOM events and on calls to `$applyAsync/$digest`. There are some useful services like `$http` and `$timeout` that do the wrapping for you, but anything outside of that requires calls to either `$applyAsync` or `$digest`._
`$digest` cycle is not running after we've upgraded `$http` to `HttpClient` and adding `$rootScope.$applyAsync` to explicitly ask Angular to propagate the changes to Html is the solution that works perfectly.

**What is TestBed?**

When a service has a dependent service, DI (dependency injector) finds or creates that dependent service. And if that dependent service has its own dependencies, DI finds-or-creates them as well. From Angular docs “As a service tester, you must at least think about the first level of service dependencies but you can let Angular DI do the service creation and deal with constructor argument order when you use the TestBed testing utility to provide and create services” i.e DI will deal with a constructor argument

**Some Common Migration Queries**
1.  What are Promises? - Promises are exactly what they sound like. In the simplest words, they are a promise to the developer that things will work, what to do when they work, and also when they don’t work.
    
	 They can have three states:
	    

	1.  Resolved: The caller of the promise has executed as expected.
	    
	2.  Rejected: The caller of the promise didn’t execute as expected
	    
	3.  Pending: The caller is yet to be executed
    
	So,  then what exactly are the resolve and reject that we pass? They are simply the function calls that we pass. Eg. successCallback(abcd) will give parameter abcd to the resolve function when the promise caller is called.
	    
	How is it structured? A promise is called using a .then() statement after the function. Note that you cannot put this after any function, only one that returns a promise. Then functions follow. If there is only one function, it is the resolve function. If there are two functions, they are called resolve and reject respectively. The reject function is used mostly for error handling and unexpected behaviour
    
	  For more reading check out the [MDN Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)!
    

2. What is `rootScope`? - Angular has scopes. `$scope` is a local scope, which is bound to exactly one controller. It can local properties and functions of the controller. `$rootScope` on the other hand, is the global scope and can be accessed from everywhere.
    

	What is `$rootScope.$applyAsync()` and why do we use it? `$rootScope.$applyAsync` is used to update the global properties and variables so that the new state can be used by the function where it is called. As to why it is not updated automatically, the reason is that the Angular DOM basically runs in cycles, and apply causes the changes to be saved. Mostly this is done explicitly, but in some cases, we have to do it explicitly. This is mentioned in the Angular migration guide. Remember that this function will go in the resolve of the promise! This is because we want the variables to get to their new state in case of expected behaviour.
    
	For more reference: [Scopes](https://docs.angularjs.org/guide/scope)
    

3. How to assign types in the Angular file?
    
	Follow a trail. Some are really simple. But they all follow the same pattern. Keep following the variable through different references to see what type to assign. You can even use other references of that variable. Eg. If you wanted to assign a type to a function that returned WindowRef.nativeWindow! I went to window-ref.service file saw that nativeWindow returned the _window object which had a type Window. Just follow trails.
    
	Other times it might be obvious from the name. Eg SkillList is obviously an array of Skills. However, double-check these!
    
	The final way is to use a console log statement. This is good for complicated data types. Run the python development server and log the value where you get the return. You’ll see something of type Object with certain properties. Global search these properties in the codebase and find out what type it is!
    

4.  What is fakeAsync() and flushMicrotasks() and why do we use it? For this we need to understand why being synchronous is a problem for tests. Compilers don’t compile code line by line and instead push processes into a queue as they come and the resulting processes are pushed once these end. What this means is that a process whose parent was called earlier may be executed after another whose parent was called later due to how much time the parent processes took. To make an asynchronous function synchronous we use fakeAsync combined with flushMicrotasks. FakeAsync creates a fake asynchronous zone wherein you can control process flow. When flushMicrotasks is called, it flushes the task queues, i.e it waits for the processes to leave the queue before proceeding further. So, the tests are consistent!
    
5.  What are MockServices/FakeServices that are in the codebase? MockServices are basically just used to imitate real services and provide functionality for tests via inorganically made function copies of the service. These are faster but don’t test services so be wary of using them. The reason we use them is that we want to want to test the current service, not the other service, so we just use a small shell to use the functionality we want.

_For any queries related to angular migration, please don't hesitate to reach out to **Srijan Reddy (@srijanreddy98)**._