## Table of contents
- [Why do we need to define types?](#why-do-we-need-to-define-types-)
- [Where should the types be defined?](#where-should-the-types-be-defined-)
  * [Functions](#functions)
  * [Classes](#classes)
- [How to determine the types while migrating to Angular?](#how-to-determine-the-types-while-migrating-to-angular-)
- [Defining types for a third-party library](#defining-types-for-a-third-party-library)
- [Typescript interfaces](#typescript-interfaces)
- [Some Coding Style Conventions](#some-coding-style-conventions)
  * [Using string, number, boolean and array as types](#using-string--number--boolean-and-array-as-types)
  * [While using HTTP Client](#while-using-http-client)
  * [Declaring generic types](#declaring-generic-types)
  * [The interfaces should not begin with `I`](#the-interfaces-should-not-begin-with-i)
- [Advanced types](#advanced-types)
  * [Union Types](#union-types)
  * [Discriminated Unions](#discriminated-unions)
  * [Conditional Types](#conditional-types)
  * [Example](#example)
- [Cases encountered in Codebase:](#cases-encountered-in-oppia-codebase)

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

NOTE - You can skip adding types if the argument has default values like
```typescript
function exampleFunction(arg1 = 'test'): number {
  // Here typescript compiler assumes arg1 to be of type string.
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

## Defining types for a third-party library

First of all check if the library already has types -
- Some libraries already have types along with them. If yes, you need not do anything.
- Check if the library has types in [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped). If yes, you can just install the types using `yarn`. For example, you need types for node. You can install them using command `yarn add @types/node --dev`.


If the library doesn't have any types. You'll have to write types for the lib using the following instructions.

1.  Find the source code of the third-party library

    For adding type definitions for a js library, the first step is to find the source code of the library.

    Try to find the file that imports the js script of the library. For example **PencilCodeEmbed** is imported by the [pencilcode.html](https://github.com/oppia/oppia/blob/develop/extensions/interactions/pencilcode.html) file.

2. Create a file for the type definitions

    Create a file that will contain the type definitions in the typings directory with the name `library-name-defs.d.ts`.


3. Write the type definitions

    For writing custom definitions, existing type definitions in [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) and [this guide](http://blog.wolksoftware.com/contributing-to-definitelytyped) can be used as a reference.


Refer [this doc](https://docs.google.com/document/d/19V1d46DSRgTC9K2StZAcgUABpaRjzSzYaEVZIRo_Mlk/edit?usp=sharing) for detailed instructions & example.

Sample PRs
- [Upgrade version of wavesurfer and use type defs from DefinitelyTyped](https://github.com/oppia/oppia/pull/9831) - Here the custom types for wavesurfer were declared, but we found that there were definitions for wavesurfer in DefinitelyTyped. So, this PR deletes the custom types and uses the definitions from DefinitelyTyped.
- [Type definitions for midi, skulpt, math expressions](https://github.com/oppia/oppia/pull/9266) - In this PR the custom types for midi skulpt and math expressions libraries are declared.

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

Avoid **exporting** these kind of types unless its **necessary** to do so because other developers may be confused on how to use that generic type and what arguments does it need. So, it's better to not export these generic types.

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
You can refer [this file](https://github.com/oppia/oppia/blob/ef6f64122988057f161bde3e6fd212ed307425a9/core/templates/domain/statistics/LearnerActionObjectFactory.ts) to check an example where Discriminated Unions and Conditional Types are both used to build strict types.

In this file the `Learner Action` has an `action_type` and `action_customization_args` which are interdependent i.e. the schema of customization args depend on the action type.
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

## Why Enable Strict Mode?
We are working to enable strict mode checks for all TypeScript code in the codebase. This is because code that passes these checks has several benefits:

* The code becomes more self-documenting
* Edge cases are caught, thus reducing potential runtime errors
* The written code will be more robust 

## Cases Encountered in Oppia Codebase:

The following list illustrates some common TypeScript issues encountered in the Oppia codebase and explains how to update the code in each case, in order to support strict type-checking.

### [TS-1]:
 Variable `<variable name>` implicitly has type ‘any’ in some locations where its type cannot be determined
#### [TS-1-1]

##### Violation:
The type of variable is not defined explicitly and hence typescript assigns it an ‘any’ type. This violates the **noImplicitAny** rule of strict mode. 

```typescript
describe(‘Test winnowing preprocessing functions’, () => {
    var service; // error
    beforeEach(() => {
        service = new WinnowingPreprocessingService();
    });
...
});
```


##### Solution: 
To solve this, the variable is explicitly assigned the type it belongs to. In some cases in the Oppia codebase, we may need to import the Interface, Class or Type as it is not imported in the file before.
In this example, the service was of type `WinnowingPreprocessingService`.

```typescript
describe(‘Test winnowing preprocessing functions’, () => {
    var service: WinnowingPreprocessingService; 
    beforeEach(() => {
        service = new WinnowingPreprocessingService();
    });
...
});
```


#### [TS-1-2]
##### Violation:
The following scenario arises when we are dealing with the need to specify the type of a variable of a **constant**.

```typescript
var errors; // noImplicitAny Violation

errors = ObjectDomainConstants.NUMBER_WITH_UNIT_PARSING_ERRORS;

``` 




##### Solution:
The way we can specify the type of a constant variable is by using `typeof <constant>`.

```typescript
var: errors: typeof ObjectDomainConstants.NUMBER_WITH_UNITS_PARSING_ERRORS;

errors = ObjectDomainConstants.NUMBER_WITH_UNITS_PARSING_ERRORS;
```


### [TS-2]:
 Type null is not assignable to type `<type name>`
#### [TS-2-1]:
##### Violation:
The **strictNullChecks** rule disallows assigning `null` and `undefined` as a value until the type is explicitly marked. 
In the following example taken from the codebase, `ruleObjectFactory` is of type `RuleObjectFactory`. Since it was not explicitly assigned the type `null`, the compiler throws an error when we try to assign it the value `null`. 

```typescript
describe(‘RuleObjectFactory’. () => {
    let ruleObjectFactory: RuleObjectFactory = null; // error
...
})
```



##### Solution: 
In some cases that arise throughout the Oppia codebase as in this example, we can simply remove the `null` value assignment.

```typescript
describe(‘RuleObjectFactory’. () => {
    let ruleObjectFactory: RuleObjectFactory;
...
})
```


#### [TS-2-2]:
##### Violation:
The **strictNullChecks** rule does not pass and the value `null` or `undefined` is being passed to a function. 

```typescript
…
private savedMemento: string = null; // error
setStateNameSavedMemento(stateName: string): void {
    this.savedMemento = stateName;
}

```


##### Solution:
The first course of action to be taken is to try and refactor the code in a way that adding `null` or `undefined` may not be needed. 
We cannot refactor the code since the initial value of `savedMemento` has to be `null`. 

If refactoring may not be an option as in the example above, we can convert the type to a union and add the type `null` explicitly.

```typescript
…
private savedMemento: string | null = null;
setStateNameSavedMemento(stateName: string | null ): void {
    this.savedMemento = stateName;
}
```


### [TS-3]:
 In situations where the type can be `undefined` and cannot be refactored. The following errors can occur:

Object is possibly `undefined`.

Argument of type `<type1> | undefined` is not assignable to parameter of type `<type1>`.
#### [TS-3-1]:
##### Violation:
We would need to analyze the behavior of the code when `undefined` is actually returned.

Consider the following example:

```typescript
...
var height = shadowPreviewCard.height();
return (height > 630); // error
```


`shadowPreviewCard` is a jQuery selector and `height()` will return the height of an element and `undefined` if the element does not exist.
##### Solution:
height() will only return undefined if shadowPreviewCard Selector does not exist. 
By analyzing the code, we come to know that the css classes do exist in the directives html code and were put there for the exact purpose of checking the height of the card. Hence, the selector will be valid, and the undefined case will never occur in this part of the code.

Hence, to make sure the code behaves the way it is supposed to, we should throw an error if `height()` ever returns `undefined`.

```typescript
...
var height = shadowPreviewCard.height();
if (typeof height === undefined){
    throw new Error(“Shadow Preview Card Selector does not exist”)’;
}
return (height > 630); 
```


#### [TS-3-2]:
File: https://github.com/oppia/oppia/blob/develop/core/templates/domain/topic/topic-summary.model.ts 
##### Violation:
Using `?` before assigning values to properties makes them optional, which means that they can have type undefined alongside whichever type they were assigned.

For example, `can_edit_topic` is implicitly of type `boolean | undefined`. 

```typescript
...
  // These properties are optional because they are only present in the
  // topic summary dict of topic dashboard page.
  'can_edit_topic'?: boolean;
  'is_published'?: boolean;
  'classroom'?: string;
...
   topicSummaryBackendDict.topic_model_last_updated,
   topicSummaryBackendDict.can_edit_topic, // error
   topicSummaryBackendDict.is_published, // error
   topicSummaryBackendDict.classroom, // error
   topicSummaryBackendDict.thumbnail_filename,
   topicSummaryBackendDict.thumbnail_bg_color,
```



##### Solution:
If possible, we should try to refactor the code so that `undefined` may not be needed. 
If not, the fix to this error will be to add ` | undefined` at places where these properties have been used i.e. at the point of declaration and at return types of functions as shown below

```typescript
...
  public canEditTopic: boolean | undefined,
  public isPublished: boolean | undefined,
  public classroom: string | undefined,
...
  getClassroom(): string | undefined {
    return this.classroom;
  }
...
  isTopicPublished(): boolean | undefined {
    return this.isPublished;
  }
...
```



### [TS-4]:
 Element implicitly has an ‘any’ type because expression of type ‘string’ can’t be used to index type ‘{ }’. No index signature with a parameter of type ‘string’ was found on type ‘{ }’.
#### [TS-4-1]:
##### Violation:
This situation or a variant of it arises in a significant number of files in the Oppia codebase when working with dictionaries. The following error arises because there is no explicit type mentioned for the key-value pairs of the dictionary. Hence the type of value returned for the specific key cannot be determined and ends up implicitly with type `any` which is not allowed in typescript strict mode.

In the example, `nodeTitles` had type `{ }` with no explicit mention of the types of key-value pairs and `nodes[ ].getId()` returns a `string`. 

```typescript
...
var nodes = this._nodes;
var nodeTitles = { };
for (var i = 0; i < nodes.length; i++){
    ...
    // nodes[i].getId() -> returns string
    let title = nodeTitles[nodes[i].getId()]; //error
    ...
}
```


##### Solution:
We need to explicitly mention the type of key-value pair/s present in the dictionary. 
For simple dictionaries, this can be done by using the utility type `Record<Keys,Type>`. 

**Note:** An interface should be declared for more complicated dictionaries and anything that is used at more than one place except the following:
Native types
Maps
Utility Types (e.g. `Partial<Type>`, `Pick<Type, Keys>, Record<Keys, Type>`) -- see [this guide](https://www.typescriptlang.org/docs/handbook/utility-types.html).

```typescript
...
var nodes = this._nodes;
var nodeTitles: Record<string,string> = { };
for (var i = 0; i < nodes.length; i++){
    ...
    // nodes[i].getId() -> returns string
    let title = nodeTitles[nodes[i].getId()]; 
    ...
}
```


#### [TS-4-2]:
##### Violation:
When we use `Object.keys()` it returns type `string[ ]` and not type `<constant key>[ ]` which causes the error above whenever we try to use any of the key values where it expects a value of type `<constant key>` and instead gets type `string`.

```typescript
var keys = Object.keys(ObjectsDomainConstants.CURRENCY_UNITS);
for (var i = 0; i < keys.length; i++){
    let baseUnitValue = (
        ObjectsDomainConstants.CURRENCY_UNITS[keys[i]].base_unit); // error
    );
}
```


##### Solution:
The potential fix to this error is to explicitly identify the type of key values to be of those properties present in the constant, declare a type for it and then use it as a **type assertion** for the keys.

```typescript
type CurrencyUnitKeys = (
    keyof typeof ObjectDomainConstants.CURRENCY_UNITS)[ ];
var keys = (
     <CurrencyUnitsKeys> Object.keys(ObjectsDomainConstants.CURRENCY_UNITS)
   );
for (var i = 0; i < keys.length; i++){
    let baseUnitValue = (
        ObjectsDomainConstants.CURRENCY_UNITS[keys[i]].base_unit); 
    );
}
```


**Reference:** [PR-12642](https://github.com/oppia/oppia/pull/12643/files#diff-2d18a828071d16d44dd9131301259bef95d00247ee038b53b51e8f0cb96d77c4R185-R187)


### [TS-5]:
 Argument of type 'string[ ]' is not assignable to parameter of type 'number[ ]’

#### [TS-5-1]
##### Violation:
This error specifies that a wrong type cannot be assigned to some variable of type string[ ]. 
Using `Object.keys()` returns some value of type `string[ ]` but usage of variable for assignment at other places asks for it to be a `number[ ]`.

```typescript
var existingNumSpaces = Object.keys(numSpacesToDesiredIndentLevel);
```


##### Solution:
The fix to this error will be to check the usage of variable at certain places and `map` it to `number` as shown below.

```typescript
var existingNumSpaces = Object.keys( 
          numSpacesToDesiredIndentLevel 
).map(Number);
```



### [TS-6]:
 ‘this’ implicitly has type ‘any’ because it does not have a type annotation.
#### [TS-6-1]
##### Violation:
Considering the following code, it violates `noImplicitThis` rule.

```typescript
describe('High bounce rate task model', function() {
    beforeEach(() => {
        this.config = ( // error
        new ExplorationImprovementConfig(‘eid’, 1, true, 0.25, 0.20, 100));
    }
    ...
}
```


##### Solution:
The way to handle this is by initializing the variables and their types and removing `this` before each call to that variable.

```typescript
describe('High bounce rate task model', function() {
    let config: ExplorationImprovementsConfig;
    beforeEach(() => {
        config = (
        new ExplorationImprovementConfig(‘eid’, 1, true, 0.25, 0.20, 100));
    }
    ...
}
```


**Reference:** [#12642](https://github.com/oppia/oppia/pull/12643/files#diff-889c624b65e382805c19df5efe460414e323e9793fc5200b79ffeb61ea20e46dR28-R37)
### [TS-7]:
 Property `<PropertyName>` has no initializer and is definitely not assigned in the constructor
#### [TS-7-1]
##### Violation:
The strictPropertyInitialization rule enforces that the properties are assigned either in the constructor or with a property initializer and due to this, the following situation may occur.


```typescript
...
@Input() options: CodeMirrorMergeViewOptions; // error
@ViewChild(CodemirrorComponent) codemirrorComponent: CodemirrorComponent;  //error
codemirror: CodeMirror.Editor; // error
...
```



##### Solution:
Angular lifecycle hooks are used to populate the values inside the codebase. To solve this case, we will be using the non-null (!) assertion operator which asserts that the object is non-null and non-undefined. Adding ` | undefined` as a type will work for properties used inside components and just `( ! )` operator for properties that involve Component Interactions (like `@Input()` in this case).

```typescript
...
@Input() options!: CodeMirrorMergeViewOptions;
@ViewChild(CodemirrorComponent) codemirrorComponent: CodemirrorComponent | undefined;
codemirror: CodeMirror.Editor | undefined;
...
```


**Reference:** [#12965](https://github.com/oppia/oppia/pull/12965/files#diff-a6de57afea05cf64679a839bccd46bd637dcd287d134ad3483a3714d033a5f16R23-R29)

