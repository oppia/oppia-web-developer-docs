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

For backend validations of the data stored for these interactions, we have a custom expression parser in `core/domain/expression_parser.py`. **Note that these need to be in sync with the behavior of nerdamer's validations.** To check nerdamer's behaviour, the source code can be checked [here](https://github.com/jiggzson/nerdamer). To ensure sync, an exhaustive list of test cases (refer to the original proposal) are run on both frontend and backend validators, so these can be updated if and when required.

## FAQs
- **How is the data stored for these interactions validated?**
  - There are 2 layers of validation for all three math interactions.
    - **Frontend validations:** This is a set of validations that happen in real-time as soon as the learner/creator enters an expression into guppy. On any change to the guppy input, the input is passed to validation handlers that internally use nerdamer to run syntactic as well as logical checks on the given input. Any errors caught at this stage are displayed to the user in real-time and the submit button is disabled until they are fixed. One caveat to note here is that the checks and display of errors happen when the user clicks outside the input box and not on single-letter changes. This is intentionally done since the latter is an annoying experience. To achieve this, the validations are run when the currently active guppy instance goes out of focus, implying that the user is done typing and validations can be run. Note that these validations run anywhere a guppy instance is present so they will be run on both creator's and learner's view. **These are handled by the `core/templates/services/math-interaction-service.ts`**
    - **Backend validations:** After the first level of validations from the frontend pass, the creator's input needs to be stored in the datastore. Before this happens, we also run some backend validations on the input as a backup check for any data that gets stored. This is done to ensure that scenarios such as breakages in the frontend, direct backend calls, one-off/audit backend jobs, etc. are all handled. **These are handled by the `core/domain/expression_parser.py`**
  - Other than this there are obviously some exploration level validations for all these interactions that check exploration level validity to avoid scenarios like redundant rule input, impossible-to-reach state, etc. **These are handled by the individual validation services present in each interaction's directory.**

# Glossary
- **Syntactic checks:** Checks that ensure structural validity of an expression by checking if a valid abstract syntax tree can be formed for the given expression. For e.g. "a + b / c" is syntactically valid whereas "a + b /" is not.
- **Logical checks:** Checks that catch logical errors in an expression. A syntactically valid expression can still have logical erros. E.g. "4 + x / 0". 

## References
- [Original proposal](https://drive.google.com/file/d/1vB3vxvBUEsYivUgTiZrmUYhmReCfQPQE/view)

## Open Issues
- [ ] [Division sign customization arg acts exploration-specific instead of being state-specific.](https://github.com/oppia/oppia/issues/13689)
  - **Context:** The division sign display is Guppy config that is currently set on a global level. This needs to be changed to an instance-level config. But that config context needs to persist for all instances for a given state. Might be a little tricky, need to find a cleaner solution.
- [ ] [Unexpected error message in guppy input](https://github.com/oppia/oppia/issues/16488)
  - **Context:"** There are some modifications done to the input provided by guppy where we explicitly add parentheses to some expressions so that the nerdamer and the backend parsers understand the expression. We also have a real-time validation that checks for redundant parentheses in an expression. The modifications seem to be triggering this validation. Check `validateAlgebraicExpression` in `math-interactions.service.ts` for more info.
- [ ] [The error message "Not a prefix operator" is not clear](https://github.com/oppia/oppia/issues/16358)
  - **Context:** For showing errors on the frontend, we rely on Nerdamer's syntactic checks and we update the error message thrown by Nerdamer's validator to make it human readable. The error message can be updated to be more user friendly. Check `cleanErrorMessage` in `math-interactions.service.ts`.
- [ ] [The placeholder text for NumericExpressionInput overflows out of the box.](https://github.com/oppia/oppia/issues/11747)
  - **Context:** We allow custom placeholder for the guppy inputs so if the custom placeholder text is too long, instead of wrapping, it overflows. This seems to be a non-trivial UI issue that is native to the guppy library. Some hacks were tried to fix this, but a long term fix might be required to handle all scenarios. Check `guppy.html`.
