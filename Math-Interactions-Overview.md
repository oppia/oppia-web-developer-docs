There are currently three interactions that can be used for math-related questions in lessons:
- AlgebraicExpressionInput
- NumericExpressionInput
- MathEquationInput

The following third party libraries are used:
- [Guppy](https://guppy.js.org/site/): Opensource tool that provides an input widget for the math interactions. Supports WYSIWYG and provides a lot of APIs that can be used to build customizations on top of the basic tools.
- [Nerdamer](https://nerdamer.com/): Opensource javascript library for handling (validating, operating, etc) the math expressions on the frontend.

## Code structure
### Frontend
The interaction-specific files are in `extensions/interactions`. Each interaction has its own directory. The general structure of this directory would be as follows:

![interactions](https://user-images.githubusercontent.com/35144226/228078766-a0fb8b8a-a03b-4df1-add5-59725d41cdeb.PNG)

The `core/templates/services` contains the following services related to the math interactions:
- `guppy-initialization-service.ts`: Service for initializing a guppy instance. On the exploration editor page, there could be multiple guppy instances present at any given point. This service manages all of these instances and helps in initializing a new instance and finding the currently active instance.
- `guppy-configuration-service.ts`: Service for handling the global config that will be applied to all guppy instances. 
- `math-interaction-service.ts`: The core service for handling most of the math interaction-related functionalities on the frontend. This service handles:
  - All frontend validations using nerdamer.
  - Modifying the user input from guppy and transforming it such that it is compatible with nerdamer and our backend parser schema.
  - Generating error messages for various invalid scenarios.

For the custom on-screen keyboard, the functionality is handled by the component present in `core/templates/components/on-screen-keyboard`. This does not extend the custom OSK provided by guppy since customization on that is quite limited. The custom on-screen keyboard contains normal buttons that call the guppy API functions to insert characters onto the currently active guppy instance.

### Backend
There are some custom objects (e.g. `MathEquation`, `AlgebraicIdentifier`, etc.)  present in `extensions/objects/models/objects.py` that help in type checks for the objects used in these interactions. The validators (e.g. `is_valid_math_expression`, `is_valid_algebraic_expression`, etc.) for these objects are present in `core/schema_utils.py`. 

For backend validations of the data stored for these interactions, we have a custom expression parser in `core/domain/expression_parser.py`. **Note that these need to be in sync with the behavior of nerdamer's validations.** To check nerdamer's behaviour, the source code can be checked [here](https://github.com/jiggzson/nerdamer). To ensure sync, an exhaustive list of test cases (refer to the original proposal linked in the references section below) are run on both frontend and backend validators, so these can be updated if and when required. These test cases are currently present in `math-interactions.service.spec.ts` for frontend and in `expression_parser_test.py` for backend.

## FAQs
- **How is the data stored for these interactions validated?**
  - There are 2 layers of validation for all three math interactions.
    - **Frontend validations:** This is a set of validations that happen in real-time as soon as the learner/creator enters an expression into guppy. On any change to the guppy input, the input is passed to validation handlers that internally use nerdamer to run syntactic as well as logical checks on the given input. Any errors caught at this stage are displayed to the user in real-time and the submit button is disabled until they are fixed. One caveat to note here is that the checks and display of errors happen when the user clicks outside the input box and not on single-letter changes. This is intentionally done since the latter is an annoying experience. To achieve this, the validations are run when the currently active guppy instance goes out of focus, implying that the user is done typing and validations can be run. Note that these validations run anywhere a guppy instance is present so they will be run on both creator's and learner's view. **These are handled by the `core/templates/services/math-interaction-service.ts`**
    - **Backend validations:** After the first level of validations from the frontend pass, the creator's input needs to be stored in the datastore. Before this happens, we also run some backend validations on the input as a backup check for any data that gets stored. This is done to ensure that scenarios such as breakages in the frontend, direct backend calls, one-off/audit backend jobs, etc. are all handled. **These are handled by the `core/domain/expression_parser.py`**
  - Other than this there are obviously some exploration level validations for all these interactions that check exploration level validity to avoid scenarios like redundant rule input, impossible-to-reach state, etc. **These are handled by the individual validation services present in each interaction's directory.**

# Glossary
- **Syntactic checks:** Checks that ensure structural validity of an expression by checking if a valid abstract syntax tree can be formed for the given expression. For e.g. "a + b / c" is syntactically valid whereas "a + b /" is not.
- **Logical checks:** Checks that catch logical errors in an expression. A syntactically valid expression can still have logical errors. E.g. "4 + x / 0". 

## References
- [Original proposal](https://drive.google.com/file/d/1vB3vxvBUEsYivUgTiZrmUYhmReCfQPQE/view)
