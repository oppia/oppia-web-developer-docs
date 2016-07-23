Oppia uses cache slugs with static resources to cut down on bandwidth requirements for a user. This requires a developer to use appropriate methods (depending on the static resource required) defined in `/core/templates/dev/head/domain/utilities/UrlInterpolationServiceSpec.js`. 
Common steps to use these methods:
1. Include/import `UrlInterpolationServiceSpec.js` in the corresponding html and controller files.
2. Expose the method to the html using `$scope`, eg. 
    `$scope.getStaticResourceUrl = (UrlInterpolationService.getStaticResourceUrl);`
3. Call the method using angular tags in the html, eg. `<link rel="stylesheet" type="text/css" ng-href="<[getStaticResourceUrl('/path-to-resource')]>">`

Depending on the static resource type we have the following methods:

1. `getStaticResourceUrl(resourcePath)`:
    For css, js and extension resources.
    Usage: 
        * `<link rel="stylesheet" type="text/css" ng-href="<[getStaticResourceUrl('/path-to-resource')]>">`     
    Examples:
        * <link rel="stylesheet" type="text/css" ng-href="<[getStaticResourceUrl('/extensions/gadgets/AdviceBar/static/css/adviceBar.css')]>">
    