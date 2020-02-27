Oppia uses cache slugs with static resources to cut down on bandwidth requirements for a user. This requires a developer to use appropriate methods (depending on the static resource required) defined in `/core/templates/domain/utilities/UrlInterpolationServiceSpec.js`.

**Common steps to use these methods**:
1. Include/import `UrlInterpolationServiceSpec.js` in the corresponding html and controller files.
2. Expose the method to the html using `$scope`,
eg. `$scope.getStaticResourceUrl = (UrlInterpolationService.getStaticResourceUrl);`
3. Call the method using angular tags in the html,
eg. `<link rel="stylesheet" type="text/css" ng-href="<[getStaticResourceUrl('/path-to-resource')]>">`

Depending on the static resource type we have the following methods:

1. **getStaticResourceUrl(resourcePath)**:
    For css, js and extension resources.
    Usage:
        `<link rel="stylesheet" type="text/css" ng-href="<[getStaticResourceUrl('/path-to-resource')]>">`
    Example:
        `<link rel="stylesheet" type="text/css" ng-href="<[getStaticResourceUrl('/extensions/gadgets/AdviceBar/static/css/adviceBar.css')]>">`

2. **getStaticImageUrl(imagePath)**:
    This method should be used to reference image files present in `/assets/images` and `imagePath` passed in the method should be relative to `/assets/images` and start with a forward slash.
Example:
`<img ng-src="<[getStaticImageUrl('/logo/288x128_logo_white.png')]>">`

3. **getGadgetImgUrl(gadgetType)**:
This method given a gadget type, returns the complete url path to that gadget type image.
Example:
`<img ng-src="<[getGadgetImgUrl(gadgetType)]>">`

4. **getInteractionThumbnailImageUrl(interactionId)**:
This method given an interaction id, returns the complete url path to the thumbnail image for the interaction.
Example:
`<img ng-src="<[getInteractionThumbnailImageUrl(interactionId)]>">`
