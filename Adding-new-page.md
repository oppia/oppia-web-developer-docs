
## When adding a new learner-facing page…

1.  Get an approval from Diana ([diana@oppia.org](mailto:diana@oppia.org)) and Sean ([sean@oppia.org](mailto:sean@seanlip.org)) regarding the Page Title and the Page Meta tag content that will be used by the new page before creating a PR.
    
2.  In the PR that introduces the new page, make sure that it handles the page title and meta tag changes. If it is a public user-facing page, the sitemap should also be updated.
    

	- For static pages, the HTML should contain `<title>` and `<meta>` tags. Example:
       ```html
       <title itemprop="name">Title of the page.</title>
       <meta charset="UTF-8">
       <meta name="referrer" content="no-referrer">
       <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=yes">
       <meta name="description" content="Meta tag content goes here.">
       <meta itemprop="name" content="Title of the page.">
       <meta property="og:title" content="Title of the page.">
       <meta property="og:type" content="article">
       <meta property="og:site_name" content="Oppia">
       <meta property="og:description" content="Meta tag content goes here.">
      ```

    - For dynamic pages, follow this example:

      https://github.com/oppia/oppia/blob/dacde388ab3a8eac535a1a848afaed24b9ffc7b6/core/templates/pages/story-viewer-page/story-viewer-page.component.ts#L158-L161
    

4.  In the PR description, explain the following in detail:
    

    - Is the page learner facing and public?
    
    - How can it be accessed i.e. the user journey to get to the new page?
    
    - A clear description of the contents of the page.
    
    - What is the page title and meta tag content that will be used in the new page?
    
    - Does the sitemap.xml need to be updated?
    

4.  Add @dchen97 and @seanlip as reviewers for the PR.

## Technical part

### Files

* _generic-page.import.ts_ — imports necessary for the page initialization
* _generic-page.mainpage.html_ — the main HTML
* _generic-page.module.ts_ — Angular module definition 

### Webpack
When you're adding new HTML page (not directive HTML) that uses TypeScript you also need to add it to `webpack.common.config.ts`:

1. You need to define the TypeScript entry point for the page into `module.exports.entries`.
2. You need to add `new HtmlWebpackPlugin({…})` into `module.exports.plugins`.

For example when adding **pages/generic-page/generic-page.mainpage.html** with asocciated TypeScript file **pages/generic-page/generic-page.scripts.ts**, you will need to add `page: commonPrefix + '/pages/generic-page/generic-page.scripts.ts'` to `module.exports.entries` and

```javascript
new HtmlWebpackPlugin({
  chunks: ['page'],
  meta: { // if default meta is used this can be ommited
    name: 'name',
    description: 'description'
  },
  filename: 'generic-page.mainpage.html',
  template: commonPrefix + '/pages/generic-page/generic-page.mainpage.html',
  minify: htmlMinifyConfig,
  inject: false
})
```
into `module.exports.plugins`.

### Lighthouse

The new page should be added both to the _.lighthouserc.js_ and _.lighthouserc-accessibility.js_. The page URL should be added to `ci.collect.url` and in the _.lighthouserc.js_
```javascript
{
  'matchingUrlPattern': 'http://[^/]+/url',
  'assertions': {
    'uses-webp-images': [
      'error', {'maxLength': 0, 'strategy': 'pessimistic'}      
    ],
    'uses-passive-event-listeners': ['error', {'minScore': 1}],
    'deprecations': ['error', {'minScore': 1}]
  }
}
```
into `ci.collect.assert.assertMatrix`.