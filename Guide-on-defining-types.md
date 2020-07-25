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
- No run-time penalty for determining type.
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

Determining types of variables is often an easy job. Most of the time, the types can be determined by a little reading of the code.

However, if you're unable to determine the type of variable in a file, you can look for the places where that class or function is used.

Also, if you are working on a backend api service, you can try to look at the corresponding backend Python `controllers` file to check the response dict. The backend `controller` and `domain` layers have docstrings which clearly explain the types of data that are passed to the frontend.

## Defining types for a third party library

### Check if the library already has types
- Some libraries already have types along with them.
- Check if the library has types in [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped).

### Find the source code of the third party library

For adding type definitions for a js library, the first step is to find the source code of the library.

Try to find the file that imports the js script of the library. For example **PencilCodeEmbed** is imported by the [pencilcode.html](https://github.com/oppia/oppia/blob/develop/extensions/interactions/pencilcode.html) file.

### Create a file for the type definitions

Create a file which will contain the type definitions in the typings directory with name `library-name-defs.d.ts`.


### Write the type definitions

For writing custom definitions, existing type definitions in [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) and [this guide](http://blog.wolksoftware.com/contributing-to-definitelytyped) can be used as a reference.


### Updating the version of the library

- Look for the difference in the code of the library compared to the present version.

- Update the type definitions accordingly if the arguments or return types are modified or some new functions or variables are defined.


Refer [this doc](https://docs.google.com/document/d/19V1d46DSRgTC9K2StZAcgUABpaRjzSzYaEVZIRo_Mlk/edit?usp=sharing) for detailed instructions & example.

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

Avoid **exporting** these kind of types unless its **necessary** to do so.

### The interfaces should not begin with `I`
The interfaces should not have an extra `I`. For example `IAnswerStats` should just be `AnswerStats`.

We use them mainly in the places where we have to define types for objects or dicts. Mostly in `*backend-api.service.ts` and `*object.factory.ts` files.

## Advanced types
These are just a few example of Advanced Types that we use. For full documentaion go [here](https://www.typescriptlang.org/docs/handbook/advanced-types.html).

### Union Types
This can be used when we a variable may be of different types. In some cases Discriminated Unions (described below) may be a better option to make the types more strict.

For example when a variable may be either string or a number. We can do
```typescript
let a: string | number;
```

But when you use this variable `a` like a string or a number there can be typescript errors.

For example if you try to do
```typescript
console.log(a.length);
```

An error like the following may come up.
```bash
Property 'length' does not exist on type 'string | number'.
  Property 'length' does not exist on type 'number'.
```

So, now you have two options.

The first method is to add a `if` condition checking if the `a` is a string.

```typescript
if (typeof a === 'string') {
    console.log(a.length);
}
```

The second method is type casting. Although you should _prefer_ the first method if possible.

```typescript
console.log((<string> a).length);
```

### Discrimated Unions
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
TypeScript 2.8 introduces conditional types which add the ability to express non-uniform type mappings.

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
You can refer [this file](https://github.com/oppia/oppia/blob/develop/core/templates/domain/statistics/LearnerActionObjectFactory.ts) to check a example where Discriminated Unions and Conditional Types are both used to build strict types.