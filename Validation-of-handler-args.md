## Contents 
* [Introduction](https://github.com/oppia/oppia/wiki/Validation-of-handler-args#introduction)
* [Directory Structure](https://github.com/oppia/oppia/wiki/Validation-of-handler-args#directory-structure)
    * validate_args_schema() in base.py
    * validate() method in payload_validator.py
    * normalize_against_schema() in schema_utils.py 
* [Schema keys](https://github.com/oppia/oppia/wiki/Validation-of-handler-args#schema-keys)
* [How to write schema for handler args](https://github.com/oppia/oppia/wiki/Validation-of-handler-args#how-to-write-validation-schema-for-handlers)
* [Important code pointers](https://github.com/oppia/oppia/wiki/Validation-of-handler-args#important-code-pointers)
* [Default & Optional arguments]()
* Domain object arguments.
* Extra validators
* Extra arguments
* Non-arg-receiving handlers.
* [Common Error faced](https://github.com/oppia/oppia/wiki/Validation-of-handler-args#common-error-faced)
    * NotImplementedError
    * InvalidInputException
* Example references
* [Debugging tricks](https://github.com/oppia/oppia/wiki/Validation-of-handler-args#debugging-tricks)
* [Contact](https://github.com/oppia/oppia/wiki/Validation-of-handler-args#contact)

## Introduction
All arguments passed to the GET/POST/PUT/DELETE methods of the handler classes in the Oppia controller layer need to be robustly validated before being passed to the domain layer in the backend. This can be done using the help of a Schema-Validation-System(SVS) architecture. The SVS architecture is responsible for validating the args coming from payloads or requests before passing those args into the backend structure.
## Directory structure
The following key methods are used in the validation of handler args through the SVS architecture:
validate_args_schema() in base.py
This method is defined in the BaseHandler class of base.py. 
The validate_args_schema method is responsible for raising all kinds of errors in the context of validation of handler args, like InvalidInputException and NotImplemented error. (See this section for a list of common errors that may arise.)
validate(handler_args, handler_args_schema) in payload_validator.py
handler_args: The arguments from payload/ request.
handler_args_schema: Schema from the handler class. (See this link for more information on how to write a schema).
This method is the core method for SVS functionality. It collects all the AssertionErrors raised from schema_utils.
normalize_against_schema(obj, schema) in schema_utils.py
	obj: The object which needs to be normalized.
	schema: The schema for the object.
This method normalizes the obj against its schema and raises AssertionError if any of the validation checks fail. This assertionerror is represented as InvalidInputException to the users.
## Schema Keys
Data can be validated using Oppia’s SVS by providing a schema for the data(args). A schema takes the form of a dictionary with the following fields:
type: The type of the data.
Possible values: bool, int, float, unicode, list, dict, html, custom, object_dict.
The list type has additional fields len, items in its schema (see here). 
The dict type has additional field properties in its schema. (see here)
The custom type refers to data with a defined object class in objects.py. The object class needs to be mentioned in the obj_type field of the schema (see here).
The object_dict type refers to dicts which correspond to domain object classes which already have a validate() method. The class should be passed with the object_class field of the schema (see here).
choices (optional): A list of possible values for the given type. The value entered must be equal to one of the elements in the list.
validators (optional): A list of validators to apply to the return value, in order. (see here).
default_value (optional): Either None (which indicates that the corresponding field is optional), or a value that conforms to the rest of the schema and is used to replace the object if it is missing or None. (see here)
[for type=list] items:  The schema for an item in the list.  Note to developers: The elements of all schema-validated lists should always have the same data types. If you are considering using a polymorphic list for a handler argument, please consider using a dict instead.
[for type=list] len (optional): A numeric value, representing the length of the list. The value must be greater than 0. No elements can be added or deleted.
[for type=dict] properties: A list whose elements are dicts, each representing a single field (key-value pair) of the data. Each dict in the list should have two mandatory keys:
name: The name of the field.
schema: The schema for the value corresponding to this field.
[for type=dict] description (optional): A human-readable description of the field.
[for type=custom] obj_type: The name of the class of the object, defined in objects.py.
[for type=object_dict] object class: The class of the domain object whose dictionary form this object represents. (See here)
## How to write validation schema for handlers
If you’re writing a new handler method, you’ll need to add schema validation for the handler args. To do this, follow the steps below:

List all the arguments passed to each method in the handler
Make a list of all the arguments passed to each method in the handler class. Arguments received by a handler class method can be categorized into 3 types:
URL path elements: The data which is present inside the URL are called URL path elements. Example: in url/<exploration_id>/, the exploration_id is a URL path element.
Payload arguments: The data which comes from payloads are called payload arguments. These data are typically received by PUT and POST methods.
URL query parameters: The data which comes to the handlers via the query strings in urls are called URL query parameters. Example: in url/<exploration_id>?username=nikhil, there is a single URL query parameter, with arg name “username” and value “nikhil”. URL query parameters are typically received by GET and DELETE methods.
If you face any difficulty see the debugging section or reach out to any of the persons mentioned in the contact section.
Determine the schema for each argument.
For writing schema each argument should be analysed deeply, like the use of argument in the backend structure of the code and based on the analysis, schema for the arguments should be written by following the boilerplate code.
See these links for more information on allowed schema keys, Important code pointers, and examples.
Define schemas for URL path elements in URL_PATH_ARGS_SCHEMA
The schemas for URL path elements should be written in URL_PATH_ARGS_SCHEMA.
The keys of URL_PATH_ARGS_SCHEMA should be the full set of URL path elements and the corresponding values should be the schemas for those args. If there are no URL path elements, then URL_PATH_ARGS_SCHEMA should be set to {} (an empty dict).
Examples:  Let exploration_id be a data present in the url path. Then, the schema for exploration_id should look like:

    URL_PATH_ARGS_SCHEMA = {
                'exploration_id': {
                    'type': 'unicode'
                }
            }



Define schemas for payload arguments and URL query parameter in HANDLER_ARGS_SCHEMA
The schemas for payload arguments and URL query parameters are written in HANDLER_ARGS_SCHEMA.
After writing boilerplate code for the HANDLER_ARGS_SCHEMA, the value corresponding to each request method (GET/PUT/POST/DELETE) key should contain all the payload args and URL query parameters for the corresponding method where each key represents the name of an argument and the corresponding value represents its schema.
Examples:  Let “username” be an argument passed to the delete request method of a handler class. Then, the schema for the delete request method should look like: 

    HANDLER_ARGS_SCHEMA = {
                'DELETE': {
                    'username': {
                            'type': 'unicode',
                     }
                },
       }






## Important code pointers
When adding schemas for the args of a particular handler class, some analysis is typically needed. The following points discuss the conventions adopted throughout the codebase for adding schemas to handler classes. Please read these conventions carefully:
Default & Optional arguments.
Domain object arguments.
Extra validators
Extra arguments
Non-arg-receiving handlers.

Default & Optional arguments
	If an argument is not present in a payload/request, and the schema for that argument is defined in the handler, then that argument is treated as “missing”. For missing args, schema utils will raise AssertionError which is represented as InvalidInputException by validate_args_schema() method.
Default args for a handler should therefore include a key with name “default_value”. The value for this key is the default value with which the arg will be updated to. If an argument is optional and it is not supposed to be updated with any default value, then the “default_value” key should contain None.

Example when default value is provided: Let apply_draft be an optional argument which should take the default value False if no value for that arg is provided in the request/payload. In that case, the schema for apply_draft should look like:

    {
    'GET': {
                    'apply_draft': {
                        'type': 'bool',
                        'default_value': False
                    }
                }
    }


Example when default value is not provided: Suppose make_community_owned is optional argument which should not take any default value if no value for that arg is provided in the request/payload. In that case, the schema for ‘make_community_owned’ should look like:  

    {
    'PUT':{
                    'make_community_owned': {
                        'type': 'bool',
                        'default_value': None
                    }
       }
    }


Pr link for reference: (Example)

Domain objects arguments
	Objects which are initialized by classes written in the domain layer of the codebase are called domain objects. These classes typically include methods to validate their objects.
For validating domain objects through SVS architecture, the class for that corresponding domain object should be passed into the schema. The conventional steps for writing schema for domain objects is as follows:
Add schema key “type” and its value as “object_dict”.
Add schema key “object_class” and its value as name of the domain object class.

Example:  Let change_list be a domain object, and it's validate method is written in the ExplorationChange class of exp_domain file. The schema for change_list should look like:

    'PUT': {
                'change_list': {
                    'type': 'list',
                    'items': {
                        'type': 'object_dict',
                        'object_class': exp_domain.ExplorationChange
                    }
                }
       }


Extra validators 
	By providing validators, you can increase the functionality of schema. The validators field in the schema contains the list of dicts, where each dict contains a key “id” and the value of the key should be the name of the validator. Existing validator methods can be found in _Validator class of  schema utils. Based on a particular condition, an existing validator may be used, or a new one can be written.

Example: Let us assume that language_code is a handler arg that needs to be validated in order to check whether it is a supported language code. The validator checking this is already written in schema_utils. So the schema for language code would look like:


     HANDLER_ARGS_SCHEMA = {
            'PUT': {
                'language_code': {
                    'type': 'unicode',
                    'validators': [{
                        'id': 'is_supported_language_code'
                    }]
               }   
            }
        }



Extra arguments
	Any received arguments which do not correspond to a schema in the handler class are treated as extra arguments. By default, schema_utils will raise AssertionError for extra args.
For html handlers extra args are allowed since some of the html handlers receive utm parameters which are not used by backend structure but used by Google Analytics (you can read more about utm parameters).
The conventional steps for writing the schema specially for html handlers are as follows:
List all the arguments received by the html handler class.
If the argument received is not used by the backend structure of the codebase, there is no need to write a schema for that argument.
 
Non args receiving handlers
	For handlers which do not receive any arguments from payload/request, they should only contain the boilerplate for writing schema else you will face NotImplemented Error.
Example: Boilerplate for writing schema should look like:


        URL_PATH_ARGS_SCHEMA = {}
        HANDLER_ARGS_SCHEMA = {
            'PUT': {},
            'GET': {},
            'PUT': {},
            'POST': {}  
        }

Here in HANDLER_ARGS_SCHEMA you can ignore any request method if they are not used in handler class.

## Common Error faced
When writing handler args, you may encounter NotImplementedErrors or InvalidInputException. Here is how to handle these:
NotImplementedError
Description: This error will be raised if the schema i.e, HANDLER_ARGS_SCHEMA or URL_PATH_ARGS_SCHEMA are not present in any of the handler class.
How to resolve: This error message is raised with the name of the handler which is missing a schema definition. So, by reading the error message, you can know which handler class needs schemas to be added.
InvalidInputException
Description: This error will be raised if schema validation failed for any argument. It may be due to extra args, missing args or any type mismatch.
How to resolve: This error message is raised by the validate_args_schema() method with the name of the argument for which schema validation failed. So by looking at error messages and stack traces, you can find which argument is failing the schema validation test.
Example for reference
	Examples of pr for different types is given below:
Pr link for type dict
Pr link for type list
Pr link for type object_dict
Pr link for type bool
Pr link for type int


## Debugging tricks
Most of the time, while writing schema for a handler class you need to add a couple of print statements for gaining information about the arguments coming from payload/request. In this section we will add schema step by step for ExplorationRightsHandler.
Steps:
Find the handler class.
ExplorationRightsHandler is present in the editor.py file.
Identify the request methods.
ExplorationRightsHandler contains PUT and DELETE request methods.
Make a list of all arguments.
URL path elements: exploration_id
Payload arguments: version, make_community_owned, new_member_username, new_member_role, viewable_if_private.
URL query parameters: username 
Add print statements
Add these print statements in the validate_args_schema() of the base.py. Make sure to add these print statements after their declaration in the code.


            print('\n'*3)
            print('------------'*3)
            print('Request url = ',self.request.uri)
            print('Handler class name = ',handler_class_name)
            print('Arguments = ', self.request.arguments())
            print('Iterating over arguments...')
            for j in self.request.arguments():
                print(j, self.request.get(j))
            print('URL path elements = ', self.request.route_kwargs)
            print('Request method = ',request_method)
            print('HANDLER_ARGS_SCHEMA =  ', self.HANDLER_ARGS_SCHEMA)
            print('URL_PATH_ARGS_SCHEMA = , ', self.URL_PATH_ARGS_SCHEMA)
            print('------------'*3)
            print('\n'*3)

Hit the handler through frontend.
Start the server and hit the handlers from the frontend then view terminal. For ExplorationRightsHandler, the print logs should look like:

Write schema by following the boilerplate code.
Now the schema for ExplorationRightsHandler should look like:

class ExplorationRightsHandler(EditorHandler):
    """Handles management of exploration editing rights."""

    URL_PATH_ARGS_SCHEMA = {
            'exploration_id': {
                'type': 'unicode'
            }
        }

    HANDLER_ARGS_SCHEMA = {
            'DELETE': {
                'username': {
                        'type': 'unicode'
                    }
            },
            'PUT':{
                'version': {
                    'type': 'unicode'
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


Remove print statements
Remove all the print statements and verify schema validation by again hitting the handler from the frontend.
## Contact
For any discussion please contact Rohit(@rohitkatlaa) or Vojtech(@vojtechjelinek) or Nikhil(@Nik-09).


