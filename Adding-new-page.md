### Webpack
When you're adding new HTML page (not directive HTML) that uses TypeScript you also need to add it to `webpack.common.config.ts`:

1. You need to define the TypeScript entry point for the page into `module.exports.entries`.
2. You need to add `new HtmlWebpackPlugin({…})` into `module.exports.plugins`.

For example when adding **pages/generic-page/generic-page.mainpage.html** with asocciated TypeScript file **pages/generic-page/generic-page.scripts.ts**, you will need to add `page: commonPrefix + '/pages/generic-page/generic-page.scripts.ts'` to `module.exports.entries` and

```javascript
new HtmlWebpackPlugin({
   chunks: ['page'],
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