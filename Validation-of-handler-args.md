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
    This method normalizes the obj against its schema and raises AssertionError if any of the validation checks fail. This assertionerror is 
    represented as InvalidInputException to the users.




