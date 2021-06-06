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



