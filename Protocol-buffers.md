## Tableof contents

* [Introduction](#introduction)
* [Support for protocol buffers](#support-for-protocol-buffers)
  * [Install proto files](#install-proto-files)
  * [Generate code from proto files](#generate-code-from-proto-files)
* [Adding your own proto files](#adding-your-own-proto-files)
* [Examples](#examples)
  * [Oppia ML](#oppia-ml)

## Introduction

At Oppia, we need to be able to store and transfer data in a language-agnostic way, for example between our frontend and backend code. We mostly use JSON, but we sometimes use [protocol buffers](https://developers.google.com/protocol-buffers/) instead. To quote from its documentation:

> Protocol buffers are a language-neutral, platform-neutral extensible mechanism for serializing structured data.

Practically speaking, this means you can define a data structure in a `*.proto` file (called a proto file). Then, you can run a command to generate code for reading and writing that data structure. The magic comes from the fact that the generated code can be in many different languages. This lets you define a data structure once and use it in both Python and JavaScript, for example. We use [buf](https://docs.buf.build) to perform this code generation.

Below, we'll discuss how we use protocol buffers at Oppia.

## Support for protocol buffers

### Install proto files

We expect proto files to be defined in their own repositories, which we download and install as dependencies. In [`manifest.json`](), the `proto` section describes how to download proto files:

```json
"proto": {
  "oppiaMlProto": {
    "version": "0.0.0",
    "downloadFormat": "zip",
    "url": "https://github.com/oppia/oppia-ml-proto/archive/0.0.0.zip",
    "rootDirPrefix": "oppia-ml-proto-",
    "targetDirPrefix": "oppia-ml-proto-"
  }
},
```

In this case `oppiaMlProto` says to download the version 0.0.0 archive of the `oppia/oppia-ml-proto` repository and unzip the contents, prefixing the unzipped folder with `oppia-ml-proto`. The folder will be placed in `third_party/` by [`scripts/install_third_party.py`](https://github.com/oppia/oppia/blob/develop/scripts/install_third_party.py).

### Generate code from proto files

Later in the process of installing Oppia's dependencies, [`install_third_party_libs`](https://github.com/oppia/oppia/blob/develop/scripts/install_third_party_libs.py) calls `buf generate` to generate Python and JavaScript code from the proto files. The `buf` command reads from two configuration files:

* [`buf.yaml`](https://github.com/oppia/oppia/blob/develop/buf.yaml) tells `buf` where to find proto files. For our example above, it would list `third_party/oppia-ml-proto-0.0.0` since that folder contains proto files. The config file would look like this:

  ```yaml
  version: v1beta1
  build:
    roots:
      - third_party/oppia-ml-proto-0.0.0
  ```

  Note that the `version` key specifies what version of the buf configuration language we are using, _not_ the version of our proto files.

* [`buf.gen.yaml`](https://github.com/oppia/oppia/blob/develop/buf.gen.yaml) tells `buf` how to generate code from our proto files. For example, suppose you want to generate Python code to `src/python` and JavaScript code to `src/javascript`. Then you could use the following configuration:

  ```yaml
  version: v1beta1
  plugins:
    - name: python
      out: src/python

    - name: js
      out: src/javascript
  ```

Assuming that we use the above configurations, let's see what code would be generated. Suppose `oppia-ml-proto-0.0.0` has two proto files: `a.proto` and `b.proto`. The following code files would be generated:

* `src/python/a_pb2.py`
* `src/python/b_pb2.py`
* `src/javascript/a.js`
* `src/javascript/b.js`

Note that for Python code, protobuf [replaces `.proto` with `_pb2.py`](https://developers.google.com/protocol-buffers/docs/reference/python-generated#invocation) to distinguish these files from those generated with protobuf version 1. For more information about how the file names of generated code are constructed, see [the protobuf documentation](https://developers.google.com/protocol-buffers/docs/reference/overview) for the programming languages you use.

## Adding your own proto files

To take advantage of Oppia's support for protocol buffers, you should follow these steps:

1. Create and publish (or find) your proto files in a dedicated repository. This doesn't necessarily have to be on GitHub, for example if you want to use someone else's proto files. See [the protobuf docs](https://developers.google.com/protocol-buffers/docs/proto3) for details on proto file syntax.
2. Add an object under the `proto` key in `manifest.json` describing how to download your proto files. For details on the syntax used by `manifest.json`, check the code in `scripts/install_third_party.py`, which parses the manifest.
3. Add the path to where your proto files will be downloaded to `buf.yaml` under the `roots` key.
4. If you need more languages than are currently in `buf.gen.yaml`, update `buf.gen.yaml` to add your languages.
5. You're done! Now you can import classes representing your data structures the from the code that buf generates.

## Examples

### Oppia ML

The primary way we use protocol buffers right now is for the [Oppia ML project](https://github.com/oppia/oppia-ml). Its proto files are defined in the [oppia/oppia-ml-proto](https://github.com/oppia/oppia-ml-proto) repository.

It uses the following `buf.gen.yaml`:

```yaml
version: v1beta1
plugins:
  - name: python
    out: proto_files

  - name: js
    out: extensions/classifiers/proto
    opt: import_style=commonjs,binary

  - name: ts
    out: extensions/classifiers/proto
```

Otherwise, the files are as in the examples above.

Then we import from this generated code like this:

* TypeScript and JavaScript:

  ```ts
  import { TextClassifierFrozenModel } from 'classifiers/proto/text_classifier';
  ```

* Python:

  ```python
  from proto_files import text_classifier_pb2
  ```

To learn how to use the generated code, check out [the protobuf tutorial for your language](https://developers.google.com/protocol-buffers/docs/tutorials).
