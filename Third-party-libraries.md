## Table of contents

* [Introduction](#introduction)
* [Unmanaged development dependencies](#unmanaged-development-dependencies)
* [Managed dependencies](#managed-dependencies)
  * [`start.py`](#startpy)
  * [`install_third_party_libs.py`](#install_third_party_libspy)
    * [Python packages](#python-packages)
    * [Node modules](#node-modules)
    * [Protobuf](#protobuf)
  * [`install_third_party.py`](#install_third_partypy)
    * [Manifest files](#manifest-files)
    * [Redis and Elasticsearch](#redis-and-elasticsearch)
  * [`install_backend_python_libs.py`](#install_backend_python_libspy)
* [Security](#security)
* [Upgrade dependencies](#upgrade-dependencies)
  * [Upgrade backend libraries](#upgrade-backend-libraries)
    * [Upgrade production, backend libraries](#upgrade-production-backend-libraries)
    * [Upgrade development, backend libraries](#upgrade-development-backend-libraries)
  * [Upgrade frontend libraries](#upgrade-frontend-libraries)
    * [Upgrade frontend libraries installed from npm](#upgrade-frontend-libraries-installed-from-npm)
    * [Upgrade frontend libraries not installed from npm](#upgrade-frontend-libraries-not-installed-from-npm)
* [Add dependencies](#add-dependencies)
  * [Add a backend library](#add-a-backend-library)
    * [Add a backend, production library from pip](#add-a-backend-production-library-from-pip)
    * [Add a backend, development library from pip](#add-a-backend-development-library-from-pip)
    * [Add a library that cannot be installed from pip](#add-a-library-that-cannot-be-installed-from-pip)
  * [Add a frontend library](#add-a-frontend-library)
    * [Add a frontend library from npm](#add-a-frontend-library-from-npm)
    * [Add a frontend library from outside npm](#add-a-frontend-library-from-outside-npm)

## Introduction

At Oppia we have a lot of dependencies, and we have many different ways of managing them. Some of these dependencies are required for our production application, while others are only used for development. Below, we will discuss how all these dependencies are managed.

## Unmanaged development dependencies

Oppia has some development dependencies that the user has to manage themselves. These are:

* Python 3.9
* Google Chrome
* git
* Tools commonly found on Linux and MacOS systems like bash

In our [[setup instructions|Installing-Oppia]], we walk developers through installing these.

## Managed dependencies

The rest of Oppia's development and production dependencies are managed by the Oppia code. These dependencies are installed to the following places:

* `oppia_tools/` stores development tools that aren't used in production. This folder is a sibling of the repository root (`oppia/`), so if you are in the root of the repository, this folder is at `../oppia_tools/`. However, we'll use `oppia_tools/` here for simplicity.
* `third_party/python_libs` stores our production Python dependencies.
* `third_party/static` stores the production Node.js dependencies that aren't installed from npm. These dependencies are downloaded and compiled by our own code.
* `node_modules` stores the production Node.js dependencies that we install from npm. On developer machines, it also stores development dependencies. These dependencies are downloaded by yarn and compiled by webpack.
* `third_party/` also stores some other production dependencies like protobuf files.

When you run `python -m scripts.start`, a chain of scripts installs and/or upgrades dependencies as necessary:

```mermaid
flowchart TD
first("start.py") -->|"calls install_third_party_libs.main() when start.py is executed or imported"| ITPL("install_third_party_libs.py")
ITPL -->|"main() calls install_third_party.main()"|ITP("install_third_party.py")
ITPL -->|"calls install_python_dev_dependencies.main() when executed or imported"| IPDD("install_python_dev_dependencies.py")
ITP -->|"main() calls install_python_prod_dependencies.main()"| IPPD("install_python_prod_dependencies.py")
```

We'll look at each of these scripts below.

### `start.py`

When you start a development server, you execute `scripts/start.py`. This file does not itself install any dependencies, but it contains a call to `install_third_party_libs.main()` that will be executed whenever `start.py` is executed, or even imported.

### `install_third_party_libs.py`

#### Python packages

Whenever `install_third_party_libs.py` is executed or imported, it calls `install_python_dev_dependencies.main()` to install Python development dependencies to the active virtual environment. These dependencies are listed in `requirements_dev.txt`, which `install_python_dev_dependencies.py` asserts matches what would be produced by compiling `requirements_dev.in`. If this assertion fails, the script goes ahead and does the compilation but then fails to make sure you commit the updated `requirements_dev.txt` file.

#### Node modules

This script installs the frontend dependencies from `package.json` using `yarn`. The versions of all these Node.js modules are pinned by `yarn.lock`, and they get installed to `node_modules/`.

#### Protobuf

We also install the protoc and buf tools for protobuf (these versions are pinned). By the time we install those tools, we've already called `install_third_party.main()`, so we have downloaded the proto files. We use buf to generate code from those proto files (i.e. compile the proto files).

### `install_third_party.py`

#### Manifest files

We use a `dependencies.json` file to specify other dependencies that we have but which aren't Python packages or Node.js modules. This file has a `dependencies` key, under which it has the following keys:

* `proto`: Files here are installed to `third_party/`
* `frontend`: Files here are installed to `third_party/static/`
* `oppiaTools`: Files here are installed to `oppia_tools/`

Under each of these keys is a collection of key-value pairs where each key is a dependency name and each value is an object describing how to download and install the dependency. We support three types of dependencies:

* Zip archives of files. The zip archive must expand to a single file or folder. The following keys are required in the object describing this dependency:

  * `version`: The dependency's version string.
  * `url`: The full URL to the zip archive.
  * `downloadFormat`: Must be set to `zip`.

  The object must specify one of the following keys:

  * `rootDir`: The base name of the expanded file or folder.
  * `rootDirPrefix`: The prefix of the base name of the expanded file or folder. The prefix concatenated with the version string should produce the full base name.

  The object must also specify one of the following keys:

  * `targetDir`: The base name to which the expanded file or folder should be renamed.
  * `targetDirPrefix`: The prefix of the base name to which the expanded file or folder should be renamed. The prefix concatenated with the version string should produce the full base name.

* Collections of files. The following keys are required in the object describing this dependency:

  * `version`: The dependency's version string.
  * `url`: The prefix of the URL to the files.
  * `downloadFormat`: Must be set to `files`.
  * `files`: List of the files to download. Each file will be downloaded from the URL formed by joining `url` with the item in `files`, using a slash (`/`) as a delimiter. Files are not renamed after they are downloaded.
  * `targetDirPrefix`: A string which, when suffixed with `version`, yields the base name of the folder to which each file will be downloaded.

* Tar archives of files. These work just like zip archives, except that there are no optional keys. Instead of the `rootDir`, `rootDirPrefix`, `targetDir`, and `targetDirPrefix` keys, these two keys are required:

  * `tarRootDirPrefix`: Same as `rootDirPrefix` for zip files.
  * `targetDirPrefix`: Same as `targetDirPrefix` for zip files.

New dependencies should not be added to `dependencies.json`, as we are trying to remove this method of installing dependencies. Instead, you should use the [node modules](#node-modules) method.

#### Redis and Elasticsearch

We download and install the Redis CLI and Elasticsearch development server. We pin the versions of these dependencies that we install, but we don't automatically upgrade old versions. Specifically, we try to execute the Redis and Elasticsearch binaries. If the binaries execute successfully, then we don't install anything.

### `install_backend_python_libs.py`

This script uses pip to install the Python dependencies we need in production to `third_party/python_libs`. We define these dependencies using `requirements.in`, which lists the libraries we depend on directly. Then `install_backend_python_libs.py` generates `requirements.txt`, which lists those direct dependencies, plus all the packages that our direct dependencies need, and so on. Both `requirements.in` and `requirements.txt` specify versions, so `requirements.txt` is analogous to `yarn.lock` in that it pins all the versions of all the Python packages we use in production.

## Security

All dependencies we add to our projects introduce risks. These include security risks (an attacker could inject malicious code into Oppia if they control one of our dependencies) and maintainability risks (if a dependency isn't well-maintained, its bugs could break Oppia). To mitigate these risks, we should do the following:

1. **Minimize** the number of dependencies we have and the extent to which we rely on them. Especially for small dependencies, it may be better to implement them ourselves. That said, for security-related operations (especially cryptographic ones), relying on a trusted library may be better than rolling our own and possibly making mistakes.
2. **Vet** any dependencies we do have. This means checking that we trust the maintainer not to add malicious code, maintain security measures to stop someone else from adding malicious code, and maintain the dependency by fixing bugs. For small dependencies, this may mean reviewing their code manually. For larger ones, we may have to rely on reputation.
3. **Pin** dependencies to a specific, immutable version. Here are some examples of types of dependencies we use often:
   * PyPI: Use `==` to specify a particular version number, e.g. `my_dependency==1.0.5`.

     > [!WARNING]
     > Do not use `=>`, which will tell `pip` to automatically install the latest version of a package without our involvement.

   * NPM: Use `yarn.lock` to pin dependency versions (this happens automatically for all NPM dependencies handled by yarn).
   * GitHub Actions: Use a commit hash ("SHA value" in the [docs](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions#using-release-management-for-your-custom-actions)) when specifying a third-party dependency. For example: `- uses: actions/javascript-action@172239021f7ba04fe7327647b213799853a9eb89`.
4. **Hash** dependencies using a hashing algorithm [approved by NIST](https://csrc.nist.gov/projects/hash-functions) and compare that hash to a list of the values we expect. In most cases, we should take advantage of package managers' built-in functionality to verify checksums. This ensures that even if someone manages to change the code of a supposedly immutable dependency version (for example, there are ways to do this in PyPI where packages can be provided either as source code or as binaries), we won't install the malicious dependency.
5. **Upgrade** dependencies every month to ensure we benefit from any security fixes.

Ideally, we'd also constrain dependencies to limit the damage they can do, but that isn't really supported by any of the dependency ecosystems we use yet. Also note that not all of these measures are in place yet. Work on implementing them is tracked in [oppia/oppia#16991](https://github.com/oppia/oppia/issues/16991).

## Upgrade dependencies

### Upgrade backend libraries

Before upgrading any backend dependencies, you should check for any breaking changes between the currently installed version and the new version you want to upgrade the library to. You should:

* Check the library's changelog for breaking changes.
* **Important:** Test that everything works correctly after you install the upgraded version (see below).

Note that we don't have an automatic way to detect outdated backend dependencies, so to upgrade all outdated backend dependencies, you have to look up each library online to find its latest version and compare that to the version currently specified in our code. We explain where our code specifies version numbers below.

#### Upgrade production, backend libraries

A production library (these are listed in `requirements.in`) can be upgraded as follows:

1. Update the library's version number in `requirements.in`.
2. Run `scripts/start.py` to update `requirements.txt` based on the new `requirements.in`.

#### Upgrade development, backend libraries

1. Update the library's version number in `requirements_dev.in`.
2. Run `scripts/start.py` to update `requirements_dev.txt` based on the new `requirements_dev.in`.

Backend libraries that are not installed using pip also have their versions specified in `install_third_party_libs.py`, but they use custom code for each library. You should read the code to find the section for your library.

### Upgrade frontend libraries

#### Upgrade frontend libraries installed from npm

You can update all frontend libraries that we install from npm as follows. Note that `<yarn version>` specifies the currently-installed version of yarn (there should only be one version in `oppia_tools`). Also, all commands should be run from the repository root.

1. Run `../oppia_tools/yarn-<yarn version>/bin/yarn upgrade` to upgrade libraries that should not have any breaking changes.
2. Run `../oppia_tools/yarn-<yarn version>/bin/yarn outdated` to show outdated libraries whose newer versions might have breaking changes.
3. Check for breaking changes in the outdated libraries from the previous step. You should:

   * Check the library's changelog for breaking changes.
   * **Important:** Test that everything works correctly after you install the upgraded version.

4. Manually update the versions in `package.json` for all packages you decide to upgrade.
5. Run `../oppia_tools/yarn-<yarn version>/bin/yarn install`

#### Upgrade frontend libraries not installed from npm

Other frontend libraries are specified in `dependencies.json`. You can upgrade these libraries as follows:

1. Check for breaking changes in the libraries you want to upgrade. You should:

   * Check the library's changelog for breaking changes.
   * Test that after you install the upgraded version (see below), everything works correctly.

2. Change the version in `dependencies.json` to the new version you want to install.

Note that we don't have an automatic way to detect outdated libraries in `dependencies.json`, so to upgrade all such libraries, you have to check each version manually.

Note that we don't have an automatic way to detect outdated libraries in `dependencies.json`, so to identify outdated dependencies, you have to look up each library online to find its latest version and compare that to the version specified in `dependencies.json`.

## Add dependencies

Note that all dependencies must be compatible with our Apache 2 license. All additions must also be approved by @vojtechjelinek.

### Add a backend library

Note that if a library is needed both for development and in production, then it should be added according to both of the following sets of instructions.

#### Add a backend, production library from pip

Here's how to add a backend, production library that can be installed from pip:

1. Add the library to `requirements.in` in the form `<package-name>==<version>`.
2. Generate `requirements.txt` from `requirements.in` by running `scripts/start.py`.

#### Add a backend, development library from pip

1. Add the library to `requirements_dev.in` in the form `<package-name>==<version>`.
2. Generate `requirements_dev.txt` from `requirements_dev.in` by running `scripts/start.py`.

#### Add a library that cannot be installed from pip

If a library cannot be installed from pip, you'll have to add custom code to `scripts/install_third_party_libs.py` to handle installation.

### Add a frontend library

#### Add a frontend library from npm

If the library is available from npm, you can install it like this:

1. Add it to `package.json`. If the dependency is needed in production, add it under `"dependencies"`. Otherwise, add it under `"devDependencies"`. If a dependency is needed in both production and for development, only add it under `"dependencies"`.
2. Run `../oppia_tools/yarn-<yarn version>/bin/yarn install` from the repository root. Note that `<yarn version>` specifies the version of yarn.

#### Add a frontend library from outside npm

If your library is not available from npm, you can add it to `dependencies.json`. However, you should check with @vojtechjelinek first as we are trying to move away from `dependencies.json`.
