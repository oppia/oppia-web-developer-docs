## What is webpack
Webpack is an open-source JavaScript module bundler. Webpack takes modules with dependencies and generates static assets representing those modules. It takes the dependencies and generates a dependency graph allowing web developers to use a modular approach for their web application development purposes.

## How we use webpack
We use webpack to bundle almost all TypeScript files in `core/templates/dev/head/` into budles for every HTML page that we have. Entry points and HTML pages are configurated in [`webpack.config.ts`](https://github.com/oppia/oppia/blob/develop/webpack.config.ts). How exactly are the files bundled is decided by webpack and the build process takes around **15 seconds**. We use webpack both for dev and prod mode, also when frontend tests and e2e tests are run. There is a section in the [Coding style guide about webpack](https://github.com/oppia/oppia/wiki/Coding-style-guide#webpack).

Later we plan to use webpack with `extensions/` folder, remaining files in `core/templates/dev/head/`, dependencies, directives HTML files.

Files that are not yet included in webpack bundles are compiled from TypeScript into JavaScript and are moved into `local_compiled_js/` folder.

### Dev mode
The configuration info for dev mode is in [`webpack.dev.config.ts`](https://github.com/oppia/oppia/blob/develop/webpack.dev.config.ts). The bundled files are generated into `core/templates/dev/head/dist/` and then directly used from there in our server.

### Prod mode
The configuration info for prod mode is in [`webpack.prod.config.ts`](https://github.com/oppia/oppia/blob/develop/webpack.prod.config.ts). The bundled files are generated into `core/templates/dev/head/dist/` as in dev mode, then are transfered into `build/` folder by `scripts/build.py`.

### Frontend tests
The configuration info for frontend tests webpack is included in in [`karma.conf.ts`](https://github.com/oppia/oppia/blob/develop/core/tests/karma.conf.ts). Karma handles the execution of webpack by itself and there is no need to call the webpack build ourselves.

## Troubleshooting
### Webpack hangs
Sometimes webpack hangs and doesn't finish properly, this usually happens after new branch is created or code is pulled from upstream.

**Solution**

Kill the process by `Ctrl+C` and run the command again.

### Frontend tests fail without reason
Frontend tests tend to fail sometimes with random errors.

**Solution**

Delete the `local_compiled_js/` directory and restart a local stack so that a new `local_compiled_js/` directory is created.