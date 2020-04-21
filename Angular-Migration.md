## Overview

Angular is an app-design framework and development platform for creating efficient and sophisticated apps. Angular has numerous benefits over AngularJS like (some of which are listed here):
1. Angular is faster than AngularJS.
2. AngularJS uses JavaScript but Angular 2 and later versions (clubbed together as Angular 2+ for the sake of discussions) use TypeScript. TypeScript is the superset of JavaScript and provides static typing during the development process. Static typing not just improves performance but avoids many runtime pitfalls that were making AngularJS difficult to use for larger and complex applications.
3. AngularJS does not provide mobile development support but Angular does.

This project aims to migrate the entire codebase from AngularJS to Angular. The project plan will be iterative in nature. We will migrative the services first and then the controllers and directives. The services would be migrated in the dependency order i.e if A depends on B and B depends on C, we will migrate in the order C, B and A.

We have a script named [create_topological_sort_of_all_services](https://github.com/oppia/oppia/blob/develop/scripts/create_topological_sort_of_all_services.py) which generates all the services in the dependency order. The codebase has about 340 services as of now, out of which 220 are migrated to Angular and remaining 120 are to be migrated. Some files slipped in even without having all the require statements which has affected the output of the script. The plan would be to go in the order of the files that script generates. If the current service that is in order could be migrated -- migrate it, else add missing require statements. We will re-run the script during the second pass and fix the left ones then.

## Angular Migration Tracker

The [angular migration tracker](https://docs.google.com/spreadsheets/d/1L9Udn-XT6Lk1qaTBUySTw1AnhvQMR-30Qry4rfd-Ovg/edit?usp=sharing) holds the record of which services have been migrated and which are to be migrated. The order of services mentioned in the tracker is in dependency order i.e if serviceA depends on serviceB and serviceB depends on serviceC, then the order of services written in the tracker would be serviceC, serviceB followed by serviceA.

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
      url, { observe: 'response' }).toPromise().then(
       (response) => {this.dataDict = cloneDeep(response.body);
   ```
   and import clonedeep like this:
   ```
   import cloneDeep from 'lodash/cloneDeep';
   ```

   (b) Search in the  codebase where the service is used to obtain results from get requests and change 
   `response.data` to `response.body`.

   (c) Add `$rootScope.apply()` in the controller/directive that is resolving the http request similar to how it is 
   added [here](https://github.com/oppia/oppia/pull/8427/files#diff-ecf6cefd0707bcbafeb6a0b4009aa60cR78). You can 
   find this by doing a simple search of the function name in service where get request is handled.

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

   (b) Add `$rootScope.apply()` in the controller/directive that is resolving the http request similar to how it is 
   added [here](https://github.com/oppia/oppia/pull/8427/files#diff-ecf6cefd0707bcbafeb6a0b4009aa60cR78). You can 
   find this by doing a simple search of the function name in service where get request is handled.

8. For functions in the service, add type definitions for all the arguments as well as return values. 
**Note:** For complex types or some type that is being used over functions or files we can declare interface or export interface (if it has to be imported over files). For example in the file [rating-computation.service.ts](https://github.com/oppia/oppia/blob/develop/core/templates/components/ratings/rating-computation/rating-computation.service.ts) we have an export interface to declare the type IRatingFrequencies. In the same file we also have a function named static, which is used by the functions of the class itself. 

9. For functions which are private to the service (used as helper functions), add private keyword for those functions.

10. In  the file end add
    ```
    angular.module('oppia').factory('ServiceName', downgradeInjectable(ServiceName));
    ```

11. Add the service to the [UpgradedServices.ts](https://github.com/oppia/oppia/blob/develop/core/templates/dev/head/services/UpgradedServices.ts) as it is done for all other upgraded services.

Take a look as to how the topic-viewer-backend-api.service is migrated in this [pull request](https://github.com/oppia/oppia/pull/8427/files).

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

   If your test is for a service that makes http requests, you also need to import the following
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

   (b) If your spec file tests service that makes http requests, you need to make a HttpClientTestingModule and 
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

6. If your spec file is for a service that makes http requests then

   (a) Convert each individual test defined in it block as follows
   ```
   it('should ...', fakeAsync(() => {
   .
   .
   }));
   ```

   (b) Change the test to create a http request via httpTestingController (taking an example from the `topic-viewer-backend-api.service.spec.ts`)
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

## Testing your Pull Request

1. Ensure your frontend tests pass
   ```
   python -m scripts.run_frontend_tests
   ```

   Note: If your migrated service involves http calls and when you run the frontend test your frontend test fail 
   for some other service then go ahead and migrate the failing tests for the other service too. You might have 
   guessed that in such case we have migrated a service which is now making http calls in Angular using HttpClient 
   but some other service that is issuing http requests to this service is still testing by making calls via 
   AngularJS http module (using $httpBackend). Go through this [PR #9029](https://github.com/oppia/oppia/pull/9029/files), 
   wherein `question-creation.service` and `question-backend-api.service` are migrated to Angular and we went 
   ahead to change relevant tests in `questions-list.service.spec`.

2. Ensure there are no typescript error
   ```
   python -m scripts.typescript_checks
   ```

3. Ensure there are no linting errors
   ```
   python -m scripts.linters.pre_commit_linter
   ```

## FAQ

**Why do we need @Injectable decorator?**

The first line is needed since our app is in hybrid state i.e half angular and half AngularJS and we need to downgrade each of our service to AngularJS so that our application runs smoothly. The second line is needed as a decorator in every service. To define a class as a service, Angular uses the @Injectable() decorator to provide the metadata that allows Angular to inject it into a component as a dependency. 
For any class that is to be used as service we need to add the following decorator for the above reason.
When we provide the service at the root level, Angular creates a single, shared instance of the service and injects it into any class that asks for it. Registering the provider in the @Injectable() metadata also allows Angular to optimize an app by removing the service from the compiled app if it isn't used. There are two other methods for registering a service but we’ll go with the one described above.

**Why do we need $rootScope.$apply with http requests?**

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
Everything was working fine before the migration, but after migration we noticed that all the values in the above mentioned function were updated but not propagated to the corresponding html file. Searched online gave [stackoverflow](https://stackoverflow.com/a/21659051) link which mentions four points of which one is

_Yes, AngularJS's bindings are "turn-based", they only fire on certain DOM events and on calls to $apply/$digest. There are some useful services like $http and $timeout that do the wrapping for you, but anything outside of that requires calls to either $apply or $digest._
`$digest` cycle is not running after we've upgraded `$http` to `HttpClient` and adding `$rootScope.$apply` to explicitly ask Angular to propagate the changes to Html is the solution that works perfectly.

**What is TestBed?**

When a service has a dependent service, DI (dependency injector) finds or creates that dependent service. And if that dependent service has its own dependencies, DI finds-or-creates them as well. From Angular docs “As a service tester, you must at least think about the first level of service dependencies but you can let Angular DI do the service creation and deal with constructor argument order when you use the TestBed testing utility to provide and create services” i.e DI will deal with constructor argument

_For any queries related to angular migration, please don't hesitate to reach out to **Nitish Bansal (@bansalnitish)**._