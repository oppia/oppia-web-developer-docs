## Common Errors in webpack

### Module not found: Error: Can't resolve '...'
This is most likely caused due to incorrect path mentioned in import or require statements. In this case, try to look for errors like spelling mistakes in the path or ensure that a file exists in that path.

If the import statement refers to a third-party library. Running `yarn install` should fix this problem.

## What is webpack
Webpack is an open-source JavaScript module bundler. Webpack takes modules with dependencies and generates static assets representing those modules. It takes the dependencies and generates a dependency graph allowing web developers to use a modular approach for their web application development purposes.

## How we use webpack
We use Webpack to bundle almost all TypeScript files in our codebase into bundles for every HTML page that we have. Entry points and HTML pages are configurated in [`webpack.common.config.ts`](https://github.com/oppia/oppia/blob/develop/webpack.common.config.ts). We use webpack both for dev and prod mode, also when frontend tests and e2e tests are run. There is a section in the [Coding style guide about webpack](https://github.com/oppia/oppia/wiki/Coding-style-guide#webpack).

## Configuration

The common configuration settings for both dev and prod mode are located in [`webpack.common.config.ts`](https://github.com/oppia/oppia/blob/develop/webpack.common.config.ts).

### Dev mode
The configuration info for dev mode is located in [`webpack.dev.config.ts`](https://github.com/oppia/oppia/blob/develop/webpack.dev.config.ts). The bundled files are generated into `webpack_bundles` and then directly used from there in our server.

### Prod mode
The configuration info for prod mode is located in [`webpack.prod.config.ts`](https://github.com/oppia/oppia/blob/develop/webpack.prod.config.ts). The bundled files are generated into `backend_prod_files/webpack_bundles` as in dev mode, then are transferred into `build/` folder by `scripts/build.py`.

#### E2e tests
We use modified [`webpack.terser.config.ts`](https://github.com/oppia/oppia/blob/develop/webpack.terser.config.ts) configuration for running the webpack in e2e tests, this configuration is almost the same as the prod config but with the parallelization disabled.

### Frontend tests
The configuration info for frontend tests webpack is included in [`karma.conf.ts`](https://github.com/oppia/oppia/blob/develop/core/tests/karma.conf.ts). Karma handles the execution of webpack by itself and there is no need to call the webpack build ourselves.

## Overview of the config

### webpack.common.config.ts

Firstly in the `resolve` property, we define some basic things like the modules, the extensions that should be handled by webpack, the alias used by webpack. For example, we have defined the following alias

```typescript
alias: {
  '@angular/upgrade/static': (
  '@angular/upgrade/bundles/upgrade-static.umd.js')
}
```

now whenever webpack sees something like
```typescript
require('@angular/upgrade/static');
```
in the code that it's building it automatically resolves the path `@angular/upgrade/bundles/upgrade-static.umd.js`.

Btw, we need this alias for angular migration because of an issue in the `@angular/upgrade` package. Reference -> https://github.com/angular/angular/issues/13137

In the `entry` property, we define the entry files for webpack. Basically, we have a separate entry file for each page. The entry files end with `.import.ts` and present in each of the folders in `core/templates/pages/`. For example, an entry looks something like

```typescript
about: commonPrefix + '/pages/about-page/about-page.import.ts'
```

The name given to the chunk before the colon (:) i.e. `about` in this case will be used in the config later.

In the `plugins` property, we define the plugins we use with webpack. We currently use the following three plugins.

#### HtmlWebpackPlugin
This basically helps us with loading the built webpack bundles as script imports in the html files, providing meta tags for our templates, etc. We add an instance of this plugin for every page like

```typescript
new HtmlWebpackPlugin({
  chunks: ['about'],
  filename: 'about-page.mainpage.html',
  meta: {
    name: defaultMeta.name,
    description: 'With Oppia, you can access free lessons on ' +
      'math, physics, statistics, chemistry, music, history and ' +
      'more from anywhere in the world. Oppia is a nonprofit ' +
      'with the mission of providing high-quality ' +
      'education to those who lack access to it.'
  },
  template: commonPrefix + '/pages/about-page/about-page.mainpage.html',
  minify: htmlMinifyConfig,
  inject: false
}),
```

Here the `chunks` contain a chunk whose name should be the same as the name we gave to its chunk in the entry component above.

Similar to the `.import.ts` files all the pages i.e. all the folders in `core/templates/pages/` directory contain a `.mainpage.html` file that serves as the main HTML template for that page. As you can see we set the `template` and `filename` properties according to this file.

`meta` is used to include the meta tags in the HTML page. `minify` is used to provide the config for minifying the output HTML page.

`inject` property is used to inject all the assets to the output HTML. We have set it to `false` because we do this manually in our templates [here](https://github.com/oppia/oppia/blob/e088975944db1b7f44acdc88f72caeac4dd2674e/core/templates/pages/footer_js_libs.html#L5-L11).

#### CleanWebpackPlugin
This plugin is used to clean the webpack files after every successful rebuild.

#### LoaderOptionsPlugin
```typescript
new webpack.LoaderOptionsPlugin({
  options: {
    macros: {
      load: macros.load,
      loadExtensions: macros.loadExtensions
    },
  },
}),
```

This plugin is used to load the macros we defined in [webpack.common.macros.ts](#webpack.common.macros.ts).

In the `module` property we define the loaders we use for different files.
We use `cache-loader` before every loader to maximize the rebuild speed.

The `externals` property is used to define the external libs that are not included in the bundle but are required by some bundled libraries. Reference -> [https://webpack.js.org/configuration/externals/](https://webpack.js.org/configuration/externals/)

### webpack.common.macros.ts

In this file, we have defined two macros i.e. `load` and `loadExtensions`. We use these in the HTML template files for loading other HTML files.
These work like `require` statements in typescript files.

Examples where macros are used -> [load](https://github.com/oppia/oppia/blob/424c985d940951a0e5688c272c4dfa54d58db0dd/core/templates/pages/contributor-dashboard-page/contributor-dashboard-page.mainpage.html#L22), [loadExtensions](https://github.com/oppia/oppia/blob/424c985d940951a0e5688c272c4dfa54d58db0dd/extensions/interactions/dependency_html.html#L1).

### webpack.dev.config.ts

This file adds some additional config to the `webpack.common.config.ts`. In particular, the config specified in this file is

```typescript
mode: 'development',
output: {
  filename: '[name].bundle.js',
  path: path.resolve(__dirname, 'webpack_bundles')
},
devtool: 'eval',
watchOptions: {
  aggregateTimeout: 500,
  poll: 1000
}
```

As you can see we specify the build mode to development, the output files and the path, the devtool and watch options (these are used when webpack is watching the files).

This is the config that is used while running the dev server using `python -m scripts.start`.

### webpack.prod.config.ts

Similar to the `webpack.dev.config.ts` this is the config used for the production build. The config specified in this file is
```typescript
mode: 'production',
output: {
  filename: '[name].[contenthash].bundle.js',
  path: path.resolve(__dirname, 'backend_prod_files/webpack_bundles')
}
```

Here we specify the build mode i.e. production and the output config. We don't use a devtool here to make the build faster.

This is the config that is used while running the dev server using
`python -m scripts.start --prod_env`.

### webpack.prod.sourcemap.config.ts and webpack.dev.sourcemap.config.ts

These are the webpack configs that are used for building using source maps. We do not use devtools that use source maps in `webpack.dev.config.ts` and `webpack.prod.config.ts` because building using source maps is slow. More in [webpack documentation](https://webpack.js.org/configuration/devtool/).

This config is used while deploying oppia. You can also build using source maps by adding a `--source_maps` flag in the start script. Like `python -m scripts.start --source_maps`.

In these config files, we use the main config (`webpack.dev.config.ts` or `webpack.prod.config.ts`) and change the devtools used in them. For example, this is how `webpack.dev.sourcemap.config.ts` looks like.

```typescript
const { merge } = require('webpack-merge');
const dev = require('./webpack.dev.config.ts');

module.exports = merge(dev, {
  devtool: 'inline-source-map'
});
```
These are the devtools we use

| Config | Devtool |
| :------: | :-------: |
| Development | eval |
| Development + Source Maps | inline-source-map |
| Production | none |
| Production + Source Maps | source-map |

### webpack.terser.config.ts

This config was written so that it can be used in the e2e tests run on Circle CI. You can refer to this [discussion](https://discuss.circleci.com/t/build-fails-with-error-spawn-enomem/30537/10) on why it was needed. This basically disables the parallelism in the terser config.
