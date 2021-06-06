## Contents 
* [Introduction](#introduction)
* [Directory Structure](#directory-structure)
    * [validate_args_schema in base.py()](#validate_args_schema-in-base.py)
    * [validate method in payload_validator.py](#validate-method-in-payload_validator.py)
    * [normalize_against_schema in schema_utils.py](#normalize_against_schema-in-schema_utils.py) 
* [Schema keys](#schema-keys)
* [How to write schema for handler args](#how-to-write-schema)
* [Important code pointers](#important-code-pointers)
    * [Default & Optional arguments](#default-&-optional-arguments)
    * [Domain object arguments](#domain-object-arguments)
    * [Extra validators](#extra-validators)
    * [Extra arguments](#extra-arguments)
    * [Non-args-receiving handlers](#non-args-receiving-handlers)
* [Common Error faced](#common-error-faced)
    * [NotImplementedError](#notimplementederror)
    * [InvalidInputException](#invalidinputexception)
* [Example references](#example-references)
* [Debugging tricks](#debugging-tricks)
* [Contact](#contact)

## Introduction

All arguments passed to the GET/POST/PUT/DELETE methods of the handler classes in the Oppia controller layer need to be robustly validated before being passed to the domain layer in the backend. This can be done using the help of a Schema-Validation-System(SVS) architecture. The SVS architecture is responsible for validating the args coming from payloads or requests before passing those args into the backend structure.

## Directory Structure

The following key methods are used in the validation of handler args through the SVS architecture:
- validate_args_schema() in base.py  
    This method is defined in the BaseHandler class of base.py.  
    The validate_args_schema method is responsible for raising all kinds of errors in the context of validation of handler args, like - 
    InvalidInputException and NotImplemented error. (See this section for a list of common errors that may arise.)
- validate(handler_args, handler_args_schema) in payload_validator.py  
    handler_args: The arguments from payload/ request.
    handler_args_schema: Schema from the handler class. (See this link for more information on how to write a schema).
    This method is the core method for SVS functionality. It collects all the AssertionErrors raised from schema_utils.
- normalize_against_schema(obj, schema) in schema_utils.py  
    obj: The object which needs to be normalized.
    schema: The schema for the object.
    This method normalizes the obj against its schema and raises AssertionError 
    if any of the validation checks fail. This assertionerror is 
    represented as InvalidInputException to the users.

## Schema Keys

Data can be validated using Oppia’s SVS by providing a schema for the data(args). A schema takes the form of a dictionary with the following fields:
- **type**: The type of the data.
    - Possible values: bool, int, float, unicode, list, dict, html, custom, object_dict.
       - The list type has additional fields len, items in its schema (see here).
       - The dict type has additional field properties in its schema. (see here)
       - The custom type refers to data with a defined object class in objects.py. The 
         object class needs to be mentioned in the obj_type field of the schema (see here).
       - The object_dict type refers to dicts which correspond to domain object classes 
         which already have a validate() method. The class should be passed with the 
         object_class field of the schema (see here).
- **choices** (optional): A list of possible values for the given type. The value entered 
  must be equal to one of the elements in the list.
- **validators** (optional):  list of validators to apply to the return value, in order. (see here).
- **default_value** (optional): Either None (which indicates that the corresponding field 
  is optional), or a value that conforms to the rest of the schema and is used to replace 
  the object if it is missing or None. (see here)
- [for type=list] **items**: The schema for an item in the list.  Note to developers: The 
  elements of all schema-validated lists should always have the same data types. If you are 
  considering using a polymorphic list for a handler argument, please consider using a dict 
  instead.
- [for type=list] **len** (optional): A numeric value, representing the length of the list. 
  The value must be greater than 0. No elements can be added or deleted.
- [for type=dict] **properties**: A list whose elements are dicts, each representing a 
  single field (key-value pair) of the data. Each dict in the list should have two 
  mandatory keys:
    - **name**: The name of the field.
    - **schema**: The schema for the value corresponding to this field.
- [for type=dict] **description** (optional): A human-readable description of the field.
- [for type=custom] **obj_type**: The name of the class of the object, defined in 
  objects.py.
- [for type=object_dict] **object_class**: The class of the domain object whose dictionary 
  form this object represents. (See here)

## How to write validation schema for handlers

If you’re writing a new handler method, you’ll need to add schema validation for the handler args. To do this, follow the steps below:
1. **List all the arguments passed to each method in the handler**
  Make a list of all the arguments passed to each method in the handler class. Arguments 
  received by a handler class method can be categorized into 3 types:
    - **URL path elements** : The data which is present inside the URL are called URL path elements. Example: in ```url/<exploration_id>/```, the exploration_id is a URL path element.
    - Payload arguments: The data which comes from payloads are called payload 
    arguments. These data are typically received by PUT and POST methods.
    - URL query parameters: The data which comes to the handlers via the query strings in urls are called URL query parameters. Example: in ```url/<exploration_id>?username=nikhil```, there is a single URL query parameter, with arg name “username” and value “nikhil”. URL query parameters are typically received by GET and DELETE methods.  
If you face any difficulty see the debugging section or reach out to any of the persons mentioned in the contact section.
2. **Determine the schema for each argument**
    For writing schema each argument should be analysed deeply, like the use of 
   argument in the backend structure of the code and based on the analysis, 
   schema for the arguments should be written by following the boilerplate code.
   See these links for more information on allowed schema keys, Important code 
   pointers, and examples.
3. **Define schemas for URL path elements in URL_PATH_ARGS_SCHEMA**
The schemas for URL path elements should be written in URL_PATH_ARGS_SCHEMA.
The keys of URL_PATH_ARGS_SCHEMA should be the full set of URL path elements and the corresponding values should be the schemas for those args. If there are no URL path elements, then URL_PATH_ARGS_SCHEMA should be set to {} (an empty dict).
Examples:  Let exploration_id be a data present in the url path. Then, the schema for exploration_id should look like:
```URL_PATH_ARGS_SCHEMAS = {
            'exploration_id': {
                'type': 'unicode'
            }
        }
```
4. **Define schemas for payload arguments and URL query parameter in HANDLER_ARGS_SCHEMAS**
    - The schemas for payload arguments and URL query parameters are written in 
    HANDLER_ARGS_SCHEMAS.
    - After writing boilerplate code for the HANDLER_ARGS_SCHEMA, the value 
    corresponding to each request method key (GET/PUT/POST/DELETE) should contain 
    all the payload args and URL query parameters for the corresponding method 
    where each key represents the name of an argument and the corresponding value 
    represents its schema.
    Note: While writing boilerplate code, make sure to remove the request keys 
    which do not correspond to any request method in the handler class. 
    Examples:  Let “username” be an argument passed to the delete request method 
    of a handler class. Then, the schema for the delete request method should 
    look like: 
```
HANDLER_ARGS_SCHEMAS = {
            'DELETE': {
                'username': {
                        'type': 'unicode',
                 }
            }
   }
```

## Important code pointers
When adding schemas for the args of a particular handler class, some analysis is typically needed. The following points discuss the conventions adopted throughout the codebase for adding schemas to handler classes. **Please read these conventions carefully**:
    * [Default & Optional arguments](#default-&-optional-arguments)
    * [Domain object arguments](#domain-object-arguments)
    * [Extra validators](#extra-validators)
    * [Extra arguments](#extra-arguments)
    * [Non-args-receiving handlers](#non-args-receiving-handlers)
### Default & Optional arguments
If an argument is not present in a payload/request, and the schema for that argument is defined in the handler, then that argument is treated as “missing”. For missing args, schema utils will raise AssertionError which is represented as InvalidInputException by validate_args_schema() method.  
To provide default args for a handler, include a key with the name “default_value” in the schema. The value for this key is the default value with which the arg will be updated if no value for that arg is provided in the request. If an argument is optional and it is not supposed to be updated with any default value, then the “default_value” key should contain None. 
 
**Example when default value is provided**: Let apply_draft be an optional argument which should take the default value False if no value for that arg is provided in the request/payload. In that case, the schema for apply_draft should look like:
```
{
'GET': {
                'apply_draft': {
                    'type': 'bool',
                    'default_value': False
                }
            }
}
```
**Example when default value is not provided**: Suppose make_community_owned is an optional argument which should not take any default value if no value for that arg is provided in the request/payload. In that case, the schema for ‘make_community_owned’ should look like:
```
{
'PUT':{
                'make_community_owned': {
                    'type': 'bool',
                    'default_value': None
                }
   }
}
```
















