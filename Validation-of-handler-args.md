## Contents 

* [Introduction](#introduction)
* [Directory Structure](#directory-structure) 
* [Schema keys](#schema-keys)
* [How to write schema for handler args](#how-to-write-validation-schema-for-handlers)
* [Important code pointers](#important-code-pointers)
    * [Default & Optional arguments](#default--optional-arguments)
    * [Domain object arguments](#domain-objects-arguments)
    * [Extra validators](#extra-validators)
    * [Extra arguments](#extra-arguments)
    * [Non-args-receiving handlers](#handlers-with-no-arguments)
    * [Post schema operations](#post-schema-operations)
* [Common Error faced](#common-error-faced)
* [Example references](#example-for-reference)
* [Debugging tricks](#debugging-tricks)
* [Contact](#contact)

## Introduction

All arguments passed to the GET/POST/PUT/DELETE methods of the handler classes in the Oppia controller layer need to be robustly validated before being passed to the domain layer in the backend. This can be done using the help of a Schema-Validation-System(SVS) architecture. The SVS architecture is responsible for validating the args coming from payloads or requests before passing those args into the backend structure.

## Directory Structure

The following key methods are used in the validation of handler args through the SVS architecture:
- **validate_args_schema()** in base.py  
This method is defined in the BaseHandler class of base.py.  
The validate_args_schema method is responsible for raising all kinds of errors in the context of validation of handler args, like - 
**InvalidInputException** and **NotImplemented** error. (See [this section](#common-error-faced) for a list of common errors that may arise.)
- **validate(handler_args, handler_args_schemas)** in payload_validator.py  
**handler_args**: The arguments from payload/ request.  
**handler_args_schemas**: Schema from the handler class.(See [this link](#how-to-write-validation-schema-for-handlers) for more information on how to write a schema).  
 This method is the core method for SVS functionality. It collects all the AssertionErrors raised from schema_utils.
- **normalize_against_schema(obj, schema)** in schema_utils.py  
**obj**: The object which needs to be normalized.  
**schema**: The schema for the object.  
This method normalizes the obj against its schema and raises AssertionError if any of the validation checks fail. This assertionerror is 
represented as InvalidInputException to the users.

## Schema Keys

Data can be validated using Oppia’s SVS by providing a schema for the data(args). A schema takes the form of a dictionary with the following fields:
- **type**: The type of the data.
    - Possible values: bool, int, float, string, unicode, list, dict, html, custom, object_dict.
       - The list type has additional fields len, items in its schema.
       - The dict type has additional field properties in its schema.
       - The custom type refers to data with a defined object class in objects.py. The object class needs to be mentioned in the obj_type field of the schema.
       - The object_dict type refers to dicts which correspond to domain object classes which already have a validate() method. The schema type ‘object_dict’ accepts any one of the following keys.
            - object_class
            - validation_method  
For more understanding [see here](#domain-objects-arguments).
- **choices** (optional): A list of possible values for the given type. The value entered must be equal to one of the elements in the list.
- **validators** (optional): A list of validators to apply to the return value, in order. ([See here](#extra-validators))
- **default_value** (optional): Either None (which indicates that the corresponding field is optional), or a value that conforms to the rest of the schema and is used to replace the object if it is missing or None. ([See here](#default--optional-arguments))
- [for type=list] **items**: The schema for an item in the list.  Note to developers: The elements of all schema-validated lists should always have the same data types. If you are considering using a polymorphic list for a handler argument, please consider using a dict instead.
- [for type=list] **len** (optional): A numeric value, representing the length of the list. The value must be greater than 0. No elements can be added or deleted.
- [for type=dict] **properties**: A list whose elements are dicts, each representing a single field (key-value pair) of the data. Each dict in the list should have two mandatory keys:
    - **name**: The name of the field.
    - **schema**: The schema for the value corresponding to this field.
- [for type=dict] **description** (optional): A human-readable description of the field.
- [for type=custom] **obj_type**: The name of the class of the object, defined in objects.py.
- [for type=object_dict] **object_class** (optional): The class of the domain object whose dictionary form this object represents. ([See here](#case-1))
- [for type=object_dict] **validation_method** (optional): Name of the method written in domain_objects_validator file, which directly calls the validate method for the domain objects. ([See here](#case-2))

## How to write validation schema for handlers

If you’re writing a new handler method, you’ll need to add schema validation for the handler args. To do this, follow the steps below:
1. **List all the arguments passed to each method in the handler**  
Make a list of all the arguments passed to each method in the handler class. Arguments received by a handler class method can be categorized into 3 types:
    - **URL path elements** : The data which is present as a part of the URL are called URL path elements. Example: in ```url/<exploration_id>/```, the exploration_id is a URL path element.
    - **Payload arguments**: The data which comes from payloads are called payload arguments. These data are typically received by PUT and POST methods.
    - **URL query parameters**: Query parameters are a defined set of parameters attached to the end of a url. They are extensions of the URL that are used to help define specific content or actions based on the data being passed. Example: in ```url/<exploration_id>?username=nikhil```, there is a single URL query parameter, with arg name “username” and value “nikhil”. URL query parameters are typically received by GET and DELETE methods.  
If you face any difficulty see the [debugging section](#debugging-tricks) or 
    reach out to any of the persons mentioned in the [contact section](#contact).

2. **Determine the schema for each argument**  
For writing schema each argument should be analysed deeply, like the use of argument in the backend structure of the code and based on the analysis, schema for the arguments should be written by following the [boilerplate code](#handlers-with-no-arguments). See these links for more information on [allowed schema keys](#schema-keys), [Important code pointers](#important-code-pointers), and 
[examples](#example-for-reference).

3. **Define schemas for URL path elements in URL_PATH_ARGS_SCHEMAS**  
    - The schemas for URL path elements should be written in URL_PATH_ARGS_SCHEMAS in the handler class.  
    - The keys of URL_PATH_ARGS_SCHEMAS should be the full set of URL path elements and the corresponding values should be the schemas for those args. If there are no URL path elements, then URL_PATH_ARGS_SCHEMAS should be set to {} (an empty dict).  
Examples:  Let ```exploration_id``` be a data present in the url path. Then, the schema for exploration_id should look like:

```python
URL_PATH_ARGS_SCHEMAS = {
    'exploration_id': {
        'type': 'unicode'
    }
}
```

4. **Define schemas for payload arguments and URL query parameter in HANDLER_ARGS_SCHEMAS**  
    - The schemas for payload arguments and URL query parameters are written in HANDLER_ARGS_SCHEMAS in the hnadler class.
    - After writing [boilerplate code](#handlers-with-no-arguments) for the HANDLER_ARGS_SCHEMAS, the value corresponding to each request method key (GET/PUT/POST/DELETE) should contain all the payload args and URL query parameters for the corresponding method where each key represents the name of an argument and the corresponding value represents its schema. **Note**: While writing boilerplate code, make sure to remove the request keys which do not correspond to any request method in the handler class.  
Examples:  Let ```username``` be an argument passed to the delete request method of a handler class. Then, the schema for the delete request method should look like: 
```python
HANDLER_ARGS_SCHEMAS = {
    'DELETE': {
        'username': {
            'type': 'unicode'
        }
    }
}
```

## Important code pointers

When adding schemas for the args of a particular handler class, some analysis is typically needed. The following points discuss the conventions adopted throughout the codebase for adding schemas to handler classes. **Please read these conventions carefully**. 
  
### Default & Optional arguments

If an argument is not present in a payload/request, and the schema for that argument is defined in the handler, then that argument is treated as “missing”. For missing args, schema utils will raise AssertionError which is represented as InvalidInputException by validate_args_schema() method.  
To provide default args for a handler, include a key with the name ```default_value``` in the schema. The value for this key is the default value with which the arg will be updated if no value for that arg is provided in the request. If an argument is optional and it is not supposed to be updated with any default value, then the “default_value” key should contain None. 
 
**Example when default value is provided**: Let ```apply_draft``` be an optional argument which should take the default value False if no value for that arg is provided in the request/payload. In that case, the schema for "apply_draft" should look like:
```python
{
    'GET': {
        'apply_draft': {
            'type': 'bool',
            'default_value': False
        }
    }
}
```
**Example when default value is not provided**: Suppose ```make_community_owned``` is an optional argument which should not take any default value if no value for that arg is provided in the request/payload. In that case, the schema for "make_community_owned" should look like:
```python
{
    'PUT':{
        'make_community_owned': {
            'type': 'bool',
            'default_value': None
        }
    }
}
```
For more understanding [refer to examples](#example-for-reference).

### Domain objects arguments

Objects which are represented by classes written in the domain layer of the codebase are called domain objects. These classes typically include methods to validate their objects.
For validating domain objects through SVS architecture, there are two preferred solutions, each for their unique cases.

#### Case 1: 

The data coming from the payloads/requests is in the dict format and many of the domain objects do not get initialized with the dictionary form of the data so they must be initialized by using the from_dict() method of the same domain class. In this case class is directly passed into the schema with a schema key named ‘object_class’. Schema for these cases should have the two keys as follows: 
1. **type**: 'object_dict'
2. **object_class**: class written in the domain layer of the codebase for the corresponding argument.

**Example**: Let new_rules is the list of dicts where each dict item is a representation of the PlatformParameterRule domain object in the platform_parameter_domain file. The schema for new_rules should look like:
```python
HANDLER_ARGS_SCHEMAS = {
    'POST': {
        'new_rules': {
            'type': 'list',
            'items': {
                'type': 'object_dict',
                'object_class': (
                    platform_parameter_domain.PlatformParameterRule)
            }
        }
    }
}
```

#### Case 2:

The cases for which validate method is written in domain classes but they are designed differently like in some domain class, validate_dict() method is present which validates the dictionary form of the data directly and in some cases validate method needs some extra arguments like a flag for strict validation. Since there is no general way to handle these cases, a separate method should be written for each such argument in the domain_objects_validator file which calls each validate method uniquely.  
The newly written method of the domain_objects_validator file should be directly passed into the schema with a schema key named ‘validation_method’. Schema for these cases should have the two keys as follows: 
1. **type**: 'object_dict'
2. **validation_method**: method written in domain_objects_validator for calling validate method from domain class directly.

**Example**:  Let change_list be a list of dicts where each dict item is a representation of the ExplorationChange domain object in the exp_domain file. The schema for change_list should look like:
```python
HANDLER_ARGS_SCHEMAS = {
    'PUT': {
        'change_list': {
            'type': 'list',
            'items': {
                'type': 'object_dict',
                'validation_method': (
                    domain_objects_validator.validate_exploration_change)
            }
        }
    }
}
```
Here validate_exploration_change is a method and it should be defined in domain_objects_validator file.  
For more understanding [refer to examples](##example-for-reference).

### Extra validators

By providing validators, you can increase a schema’s functionality. The `validators` field in the schema contains a list of dicts, where each dict contains a key “id” whose value is the name of the validator. Existing validator methods can be found in _Validator class of  schema utils. You can use the existing validators, or write new ones.  
**Example**: Let us assume that ```language_code``` is a handler arg that needs to be validated in order to check whether it is a supported language code. The validator checking this is already written in schema_utils. So the schema for language code would look like:
```python
HANDLER_ARGS_SCHEMAS = {
    'PUT': {
        'language_code': {
            'type': 'unicode',
            'validators': [{
                'id': 'is_supported_language_code'
            }]
        }   
    }
}
```

### Extra arguments

Any received arguments which do not correspond to a schema in the handler class are treated as extra arguments. By default, schema_utils will raise AssertionError for extra args. However, for html handlers, extra args are allowed (to accommodate e.g. utm parameters which are not used by the backend but needed for analytics -- see [this link](https://support.google.com/analytics/answer/1033863?hl=en#zippy=%2Cin-this-article) for an explanation). Note that the schema for HTML handlers can be written in the usual way. (The functionality for allowing extra arguments in HTML handlers is already handled by the schema validation infrastructure.)

### Handlers with no arguments

Handlers with no request arguments still need a schema defined, otherwise you will face NotImplemented Error.  
In this case, the schema should look like the following (note that the keys for HANDLER_ARGS_SCHEMAS depend on which handler methods are present):
```python
        URL_PATH_ARGS_SCHEMAS = {}
        HANDLER_ARGS_SCHEMAS = {
            'PUT': {},
            'GET': {},
            'PUT': {},
            'POST': {}  
        }
```

### Post schema operations

After writing schemas for a handler class, make sure to update the request methods for using the normalized value after schema validation, also remove the checks which are already performed during the schema validation process.  
**Example**: Replace the ```request``` keyword in the backend with ```normalized_request``` keyword, so that the normalized value obtained after schema validation can be used in the backend.
```python
self.request.get(‘version’) ----> self.normalized_request.get(‘version’)
```


## Common Error faced

When writing handler args, you may encounter NotImplementedErrors or InvalidInputException. Here is how to handle these:
1. **NotImplementedError**
    - **Description**: This error will be raised if any necessary schemas (i.e, HANDLER_ARGS_SCHEMAS or URL_PATH_ARGS_SCHEMAS) are not present in the corresponding handler class.
    - **How to resolve**: This error message is raised with the name of the handler which is missing a schema definition. So, by reading the error message, you can know which handler class needs schemas to be added.
2. **InvalidInputException**
    - **Description**: This error will be raised if schema validation failed for any argument. It may be due to extra args, missing args or any type mismatch.
    - **How to resolve**: This error message is raised by the validate_args_schema() method with the name of the argument for which schema validation failed. So by looking at error messages and stack traces, you can find which argument is failing the schema validation test.

## Example for reference

Examples of pr for different types is given below:
- [Sample pr 1](https://github.com/oppia/oppia/pull/13223)
- [Sample pr 2](https://github.com/oppia/oppia/pull/13224)
- [Sample pr 3](https://github.com/oppia/oppia/pull/13225)
## Debugging tricks

When writing the schema for a handler class, you will often need to add a couple of print statements to gain information about the arguments coming from payload/request. In this section we will add a schema step by step for ExplorationRightsHandler.  
**Steps**:
1. **Find the handler class.**  
ExplorationRightsHandler is present in the editor.py file.
2. **Identify the request methods.**  
ExplorationRightsHandler contains PUT and DELETE request methods.
3. **Make a list of all arguments.**  
    - URL path elements: exploration_id
    - Payload arguments: version, make_community_owned, new_member_username, 
    new_member_role, viewable_if_private.
    - URL query parameters: username
4. **Add print statements**  
Add these print statements in the validate_args_schema() of the base.py. Make sure to add these print statements after their declaration in the code.
```python
        print('\n'*3)
        print('------------'*3)
        print('Request url = ',self.request.uri)
        print('Handler class name = ',handler_class_name)
        print('handler_args = ',handler_args)
        print('Arguments = ', self.request.arguments())
        print('Iterating over arguments...')
        for j in self.request.arguments():
            print(j, self.request.get(j))
        print('URL path elements = ', self.request.route_kwargs)
        print('Request method = ',request_method)
        print('HANDLER_ARGS_SCHEMAS =  ', self.HANDLER_ARGS_SCHEMAS)
        print('URL_PATH_ARGS_SCHEMAS = , ', self.URL_PATH_ARGS_SCHEMAS)
        print('GET_HANDLER_ERROR_RETURN_TYPE', self.GET_HANDLER_ERROR_RETURN_TYPE)
        print('------------'*3)
        print('\n'*3)
```
5. **Hit the handler through frontend**  
Start the server and hit the handlers from the frontend then view terminal. For "ExplorationRightsHandler", the print logs should look like:
```

------------------------------------
(u'Request url = ', 'http://localhost:8181/createhandler/rights/QuWbhgRTovXr')
(u'Handler class name = ', 'ExplorationRightsHandler')
(u'Arguments = ', ['csrf_token', 'payload', 'source'])
Iterating over arguments...
('csrf_token', u'1622997677/wOV5q43bIZf1cvOhCB4vrQ==')
('payload', u'{"version":1,"new_member_role":"owner","new_member_username":"nikhil"}')
('source', u'http://localhost:8181/create/QuWbhgRTovXr#/settings')
(u'URL path elements = ', {u'exploration_id': 'QuWbhgRTovXr'})
(u'Request method = ', 'PUT')
(u'HANDLER_ARGS_SCHEMAS =  ', {u'DELETE': {u'username': {u'type': u'unicode'}}, u'PUT': {u'make_community_owned': {u'default_value': None, u'type': u'bool'}, u'new_member_role': {u'default_value': None, u'type': u'unicode'}, u'new_member_username': {u'default_value': None, u'type': u'unicode'}, u'viewable_if_private': {u'default_value': None, u'type': u'bool'}, u'version': {u'type': u'int'}}})
(u'URL_PATH_ARGS_SCHEMAS = , ', {u'exploration_id': {u'type': u'unicode'}})
------------------------------------


```
6. **Write schema by following the boilerplate code**  
Writing the schema is the most crucial part, and it is important to get this correct. The print logs from the previous step can help you get started, but please be sure to dig into the backend and frontend code, and follow calls to methods/functions to see how the incoming data is used. This will help you avoid making errors. In particular:  
**For the backend**: Try to read code as well as docstrings of all the methods which use the arguments from payload/request.  
**For the frontend**: Try to read the functions which are associated with an url.  
The eventual schema for ExplorationRightsHandler should look like:
```python
class ExplorationRightsHandler(EditorHandler):
    """Handles management of exploration editing rights."""

    URL_PATH_ARGS_SCHEMAS = {
        'exploration_id': {
            'type': 'unicode'
        }
    }

    HANDLER_ARGS_SCHEMAS = {
        'DELETE': {
            'username': {
                    'type': 'unicode'
                }
        },
        'PUT':{
            'version': {
                'type': 'int'
            },
            'make_community_owned': {
                'type': 'bool',
                'default_value': None
            },
            'new_member_username': {
                'type': 'unicode',
                'default_value': None
            },
            'new_member_role': {
                'type': 'unicode',
                'default_value': None
            },
            'viewable_if_private': {
                'type': 'bool',
                'default_value': None
            }
        }
    }

```
7. Remove print statements  
Remove all the print statements and verify schema validation by again hitting the handler from the frontend.

## Contact
For any discussion please contact Rohit(@rohitkatlaa) or Vojtech(@vojtechjelinek) or Nikhil(@Nik-09).



