## Table of contents

* [Introduction](#introduction)
* [Run TypeScript tests](#run-typescript-tests)

## Introduction

We use a lot of [TypeScript](https://www.typescriptlang.org/) code at Oppia, which lets us write JavaScript code that is strongly typed. We declare the types of variables, function arguments, and function return values. Then, TypeScript checks that there aren't any type errors when it compiles our code. For example, if you have a function that expects an int, TypeScript won't let you call the function with a string.

For help writing TypeScript code, check out our [[guide on defining types|Guide-on-defining-types]]. This page will focus on the TypeScript tests we run to make sure the types are correct.

## Run TypeScript tests

You can run the TypeScript tests like this:

Python:
```console
python -m scripts.run_typescript_checks --strict_check
```

Docker:
```console
make run_tests.typescript
```

These tests compile all ts files in the codebase and check for errors (including type errors) during compilation. The compiled files are put in the folder `local_compiled_js_for_test`, which is automatically deleted after the tests finish running. Note that this folder might not be deleted if you abort the tests early.

The tests pass if, at the end of the test output, you see the message:

```text
Compilation successful!
```

If the tests fail, you'll see:

```text
Errors found during compilation
```

Below this message will be errors describing what went wrong. For example, consider this error:

```text
core/templates/services/exploration-features-backend-api.service.ts(49,7): error TS2345: Argument of type 'boolean' is not assignable to parameter of type 'string'.
```

This means that on line 49 of `exploration-features-backend-api.service.ts`, you are passing a boolean to a function that expects a string.
