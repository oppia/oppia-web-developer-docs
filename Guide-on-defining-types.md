## Table of contents
- [Why do we need to define types?](#why-do-we-need-to-define-types-)
- [Where should the types be defined?](#where-should-the-types-be-defined-)
  * [Functions](#functions)
  * [Classes](#classes)
- [How to determine the types while migrating to Angular?](#how-to-determine-the-types-while-migrating-to-angular-)
- [Defining types for a third party library](#defining-types-for-a-third-party-library)
  * [Check if the library already has types](#check-if-the-library-already-has-types)
  * [Find the source code of the third party library](#find-the-source-code-of-the-third-party-library)
  * [Create a file for the type definitions](#create-a-file-for-the-type-definitions)
  * [Write the type definitions](#write-the-type-definitions)
  * [Updating the version of the library](#updating-the-version-of-the-library)
- [Typescript interfaces](#typescript-interfaces)
- [Some Coding Style Conventions](#some-coding-style-conventions)
  * [Using string, number, boolean and array as types](#using-string--number--boolean-and-array-as-types)
  * [While using HTTP Client](#while-using-http-client)
  * [Declaring generic types](#declaring-generic-types)
  * [The interfaces should not begin with `I`](#the-interfaces-should-not-begin-with-i)
- [Advanced types](#advanced-types)
  * [Union Types](#union-types)
  * [Discrimated Unions](#discrimated-unions)
  * [Conditional Types](#conditional-types)
  * [Example](#example)

## Why do we need to define types?
- Earlier detection of errors which in turn speeds development
- No run-time penalty for determining the type.
- Clean code. This allows developers to write more robust code and maintain it, resulting in better, cleaner code.
- Makes it easier for fellow developers to understand and use the already written code.

## Where should the types be defined?
> NOTE: These conventions apply to the files in Angular.

### Functions
- All the arguments of the function should have a type.
- The function should have a return type.

For example - A function with types would look something like this.
```typescript
function exampleFunction(arg1: string, arg2: number): boolean {
    ...
}
```

### Classes
- The properties of the class should have a type.
- The arguments in the constructor should have a type.
- The functions specified in the class should have types as listed in the section above.

For example - A class with types would look something like this.
```typescript
class ExampleClass {
    public propertyOne: number;
    public propertyTwo: string;

    constructor(someService: SomeService) {
        ...
    }

    someFunction(arg1: string): number {
        ...
    }
}
```

## How to determine the types while migrating to Angular?

Determining types of variables is often an easy job. Most of the time, the types can be determined by a little reading of the code. However, if you're unable to determine the type of variable in a file, you can look for the places where that class or function is used.

Also, if you are working on a backend api service, you can try to look at the corresponding backend Python `controllers` file to check the response dict. The backend `controller` and `domain` layers have docstrings which clearly explain the types of data that are passed to the frontend.

## Defining types for a third party library

First of all check if the library already has types -
- Some libraries already have types along with them. If yes, you need not do anything.
- Check if the library has types in [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped). If yes, you can just install the types using `yarn`.


If the library doesn't have any types. You'll have to write types for the lib using the following instructions.

1.  Find the source code of the third party library

    For adding type definitions for a js library, the first step is to find the source code of the library.

    Try to find the file that imports the js script of the library. For example **PencilCodeEmbed** is imported by the [pencilcode.html](https://github.com/oppia/oppia/blob/develop/extensions/interactions/pencilcode.html) file.

2. Create a file for the type definitions

    Create a file that will contain the type definitions in the typings directory with the name `library-name-defs.d.ts`.


3. Write the type definitions

    For writing custom definitions, existing type definitions in [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) and [this guide](http://blog.wolksoftware.com/contributing-to-definitelytyped) can be used as a reference.


Refer [this doc](https://docs.google.com/document/d/19V1d46DSRgTC9K2StZAcgUABpaRjzSzYaEVZIRo_Mlk/edit?usp=sharing) for detailed instructions & example.

When updating the version of the library look for the difference in the code of the library compared to the present version. Update the type definitions accordingly if the arguments or return types are modified, or some new functions or variables are defined.

## Typescript interfaces
You can read the detailed documentation on interfaces [here](https://www.typescriptlang.org/docs/handbook/interfaces.html).

## Some Coding Style Conventions

### Using string, number, boolean and array as types
`string`, `number`, `boolean` and `t[]` should be used when declaring types instead of `String`, `Number`, `Boolean` and `Array<t>`. This is because the latter are javascript types for constructing those things. Reference - https://stackoverflow.com/a/14727461

### While using HTTP Client
Don't do

```typescript
this.http.get(...).toPromise().then((response: BackendDict) => {...})
```

Instead do

```typescript
this.http.get<BackendDict>(...).toPromise().then(response => {...})
```

### Declaring generic types
If there's a generic type that needs to be declared. For example

```typescript
type A<T> = {
    abc: T
};
```

Avoid **exporting** these kind of types unless its **necessary** to do so because other developers may be confused on how to use that generic type and what arugments does it need. So, it's better to not export these generic types.

### The interfaces should not begin with `I`
The interfaces should not have an extra `I`. For example `IAnswerStats` should just be `AnswerStats`.

We use them mainly in the places where we have to define types for objects or dicts. Mostly in `*backend-api.service.ts` and `*object.factory.ts` files.

## Advanced types
These are just a few example of Advanced Types that we use. For full documentaion go [here](https://www.typescriptlang.org/docs/handbook/advanced-types.html).

### Union Types
This can be used when we a variable may be of different types. In some cases Discriminated Unions (described below) may be a better option to make the types more strict.

For example, when a variable may be either string or a number. We can do
```typescript
let a: string | number;
```

But when you use this variable `a` like a string or a number, there can be typescript errors.

For example, if you try to do
```typescript
console.log(a.length);
```

An error like the following may come up.
```bash
Property 'length' does not exist on type 'string | number'.
  Property 'length' does not exist on type 'number'.
```

So, now you have two options.

The first method is to add an `if` condition checking if the `a` is a string.

```typescript
if (typeof a === 'string') {
    console.log(a.length);
}
```

The second method is typecasting. However, you should _prefer_ the first method if possible.

```typescript
console.log((<string> a).length);
```

### Discriminated Unions
You can combine singleton types, union types, type guards, and type aliases to build an advanced pattern called discriminated unions, also known as tagged unions or algebraic data types. Discriminated unions are useful in functional programming. These are very helpful in making types more strict. There are three ingredients:

1. Types that have a common, singleton type property — the discriminant.
2. A type alias that takes the union of those types — the union.
3. Type guards on the common property.

Example
```typescript
interface Square {
    kind: "square";
    size: number;
}
interface Rectangle {
    kind: "rectangle";
    width: number;
    height: number;
}
interface Circle {
    kind: "circle";
    radius: number;
}

type Shape = Square | Rectangle | Circle;

function area(s: Shape) {
    switch (s.kind) {
        case "square": return s.size * s.size;
        case "rectangle": return s.height * s.width;
        case "circle": return Math.PI * s.radius ** 2;
    }
}
```

### Conditional Types
You can also change the types in a generic type function using `extends`.

Example
```typescript
type TypeName<T> =
    T extends string ? "string" :
    T extends number ? "number" :
    T extends boolean ? "boolean" :
    T extends undefined ? "undefined" :
    T extends Function ? "function" :
    "object";

type T0 = TypeName<string>;  // "string"
type T1 = TypeName<"a">;  // "string"
type T2 = TypeName<true>;  // "boolean"
type T3 = TypeName<() => void>;  // "function"
type T4 = TypeName<string[]>;  // "object"
```

### Example
You can refer [this file](https://github.com/oppia/oppia/blob/ef6f64122988057f161bde3e6fd212ed307425a9/core/templates/domain/statistics/LearnerActionObjectFactory.ts) to check a example where Discriminated Unions and Conditional Types are both used to build strict types.

In this file the `Learner Action` has a `action_type` and `action_customization_args` which are interdependent i.e. the schema of customization args depend on the action type.
So, here first we defined a generic type that changes its type according to the type parameter.

```typescript
type ActionCustomizationArgs<ActionType> = (
  ActionType extends 'ExplorationStart' ?
  ExplorationStartCustomizationArgs :
  ActionType extends 'AnswerSubmit' ? AnswerSubmitCustomizationArgs :
  ActionType extends 'ExplorationQuit' ?
  ExplorationQuitCustomizationArgs : never);
```

 Then we built a generic interface for the learner action backend dict.

```typescript
interface LearnerActionBackendDictBase<ActionType> {
  'action_type': ActionType;
  'action_customization_args': ActionCustomizationArgs<ActionType>;
  'schema_version': number;
}
```

Then we defined the strict backend dict interfaces to avoid exporting the generic type.

```typescript
export type ExplorationStartLearnerActionBackendDict = (
  LearnerActionBackendDictBase<'ExplorationStart'>);

export type AnswerSubmitLearnerActionBackendDict = (
  LearnerActionBackendDictBase<'AnswerSubmit'>);

export type ExplorationQuitLearnerActionBackendDict = (
  LearnerActionBackendDictBase<'ExplorationQuit'>);

export type LearnerActionBackendDict = (
  ExplorationStartLearnerActionBackendDict |
  AnswerSubmitLearnerActionBackendDict |
  ExplorationQuitLearnerActionBackendDict);
```

Similarly, we can create a base class for learner action.

```typescript
class LearnerActionBase<ActionType> {
  constructor(
      public readonly actionType: ActionType,
      public actionCustomizationArgs: ActionCustomizationArgs<ActionType>,
      public schemaVersion: number) {}

  toBackendDict(): LearnerActionBackendDictBase<ActionType> {
    return {
      action_type: this.actionType,
      action_customization_args: this.actionCustomizationArgs,
      schema_version: this.schemaVersion,
    };
  }
}

export class ExplorationStartLearnerAction extends
  LearnerActionBase<'ExplorationStart'> {}

export class AnswerSubmitLearnerAction extends
  LearnerActionBase<'AnswerSubmit'> {}

export class ExplorationQuitLearnerAction extends
  LearnerActionBase<'ExplorationQuit'> {}

export type LearnerAction = (
  ExplorationStartLearnerAction |
  AnswerSubmitLearnerAction |
  ExplorationQuitLearnerAction);
```

And now, finally, the object factory can create domain objects based on the `action_type` in the backend dict.

```typescript
export class LearnerActionObjectFactory {
  createFromBackendDict(
      learnerActionBackendDict: LearnerActionBackendDict): LearnerAction {
    switch (learnerActionBackendDict.action_type) {
      case 'ExplorationStart':
        return new ExplorationStartLearnerAction(
          learnerActionBackendDict.action_type,
          learnerActionBackendDict.action_customization_args,
          learnerActionBackendDict.schema_version);
      case 'AnswerSubmit':
        return new AnswerSubmitLearnerAction(
          learnerActionBackendDict.action_type,
          learnerActionBackendDict.action_customization_args,
          learnerActionBackendDict.schema_version);
      case 'ExplorationQuit':
        return new ExplorationQuitLearnerAction(
          learnerActionBackendDict.action_type,
          learnerActionBackendDict.action_customization_args,
          learnerActionBackendDict.schema_version);
      default:
        break;
    }
    const invalidBackendDict: never = learnerActionBackendDict;
    throw new Error(
      'Backend dict does not match any known action type: ' +
      angular.toJson(invalidBackendDict));
  }
}
```

Passing invalid combinations of `action_type` and `customization_args` to the `createFromBackendDict` function would throw typescript errors, and that's what we want.