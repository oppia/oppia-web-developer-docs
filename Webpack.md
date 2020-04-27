## What is webpack
Webpack is an open-source JavaScript module bundler. Webpack takes modules with dependencies and generates static assets representing those modules. It takes the dependencies and generates a dependency graph allowing web developers to use a modular approach for their web application development purposes.

## How we use webpack
We use Webpack to bundle almost all TypeScript files in our codebase into bundles for every HTML page that we have. Entry points and HTML pages are configurated in [`webpack.config.ts`](https://github.com/oppia/oppia/blob/develop/webpack.config.ts). How exactly are the files bundled is decided by webpack and the build process takes around **15 seconds**. We use webpack both for dev and prod mode, also when frontend tests and e2e tests are run. There is a section in the [Coding style guide about webpack](https://github.com/oppia/oppia/wiki/Coding-style-guide#webpack).

Later we plan to use Webpack also with dependencies and directives HTML files.

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
