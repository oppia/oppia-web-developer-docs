## Type Annotations
Type Annotations are a new feature added in [PEP 484](https://www.python.org/dev/peps/pep-0484/) that allow for adding type hints to variables. They give information about types of variables to someone who is reading the code. This brings a sense of statically-typed control to the dynamically typed Python. Though Python ignores these type hints during code execution, third-party libraries can be used to statically type-check the codebase. 

## Where to add type annotations
1. If a new file is added, it must have type annotations.
2. If a file is updated, then:
   - If the file already has type annotations, then the updated code must also have type annotations.
   - If the file has no type annotations, then the updated code may or may not have type annotations.

## Requirements for adding type annotations
1. Install [python3](https://www.python.org/downloads/release/python-377/).
2. Run `python -m scripts.run_mypy_checks`. This will install all the dependencies and will type check the annotated files.

## Running MyPy check script
Mypy checks script (`scripts/run_mypy_checks.py`) is the script used to run our mypy type checks.\
**Note**: This requires you to have `python3` and `mypy(v0.902)` installed on your local system.
It has two modes of running:
1. `python -m scripts.run_mypy_checks`\
This runs the type checks on all the type annotated files in the codebase.
2. `python -m scripts.run_mypy_checks --files path/file1.py path/file2.py`\
This runs the type checks on the files specified, i.e., file1 and file2.

## Adding type annotations
The method to write type annotations is to figure out types of the variables and mention them.

### Steps to add type annotation to a file:
**Note**: Type annotation to a main code file and its test file will be added together.
1. Run mypy type checks on the main code file you are trying to annotate. This will give the errors. 
2. Start solving these one by one.
3. Let’s say a function is not type annotated, you should first look at the function arguments and the return value. Try to get information of the types from the function docstring, test file, function code and function usage. Let’s say in the example given below, where we have a function to take two integers and convert them to string and return the concatenated string, you can figure out from the function code that the return type will be a string. The type of the arguments can be figured out by taking a look at the docstring, tests and usage of the functions.
   - The original example code:
		```
		def concat(x, y):
		    return str(x) + str(y)
		```
   - After adding type annotation:
		```
		def concat(x, y):
		    # type: (int, int) -> str
		    return str(x) + str(y)
		```


4. You may also get errors when Mypy is not able to infer the type of a variable, then you must specify the type of the variable. 
   - The original code example:
		```
		d = {
		  ‘a’: 1,
		  ‘b’: 2,
		  ‘c’: 3
		}
		```
   - After adding type annotation:
		```
		d = {
		  ‘a’: 1,
		  ‘b’: 2,
		  ‘c’: 3
		} # type: Dict[str, int]
		```


5. To understand what different error codes mean take a look at different Error Codes in MyPy docs.  
   - First try to find the reason behind that error. If that error can be resolved by some improvements in the codebase, then make the necessary changes. 
   - If there are no options left to resolve that error, then only go for ignoring the error. Let’s say code in a line throws [no-return-any] error and you have no other way than to suppress it, add a comment `# type: ignore[no-return-any]` to that line. 
   - Some ignored errors can be fixed in future, so make a TODO issue for them like this and write a todo in the file with the issue number of the issue created.

    **Note**: While adding `# type: ignore[code]` statements, the line length can increase beyond 80(this is our max line length limit) and this will throw lint errors. So try to split the code in multiple lines so that we don't cross the limit. If it is not possible, ignore the line-too-long error by using the pylint pragma after the type annotation like`# type: ignore[code] # pylint: disable=line-too-long`.

6. If stubs of some third party library are missing and mypy notifies it.
    Errors thrown by mypy:
	```
	utils.py:48: error: Library stubs not installed for "yaml" (or incompatible with Python 2.7)  [import]
	utils.py:48: note: Hint: "python3 -m pip install types-PyYAML"
	utils.py:48: note: (or run "mypy --install-types" to install all missing stub packages)
	utils.py:48: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
	```


   - The stubs can be downloaded using:
Running `mypy --install-types` will mention all the types/stubs to be downloaded.

		```
		Installing missing stub packages:
		/usr/bin/python3 -m pip install types-PyYAML

		Install? [yN]
		```
   - This will mention all the packages to be installed. This will ask for confirmation to download types/stubs. Press ‘N’ to decline downloading stubs using this.
   - Add all the types packages with versions in `mypy_requirements.txt`, and then run the mypy script using `python -m scripts.run_mypy_checks`. Running this script will download the packages. From the last example, we know that `types-PyYAML` needs to be downloaded. Search for the latest version of this and specify `types-PyYAMP==x.y.z` in `mypy_requirements.txt`. Then running the mypy script will download the package.
7. When the main code file has no errors, start type annotating the corresponding test file. Note that in the test file, there may be deliberate errors which are used to test that the functions should fail. These errors must be silenced using `# type: ignore[<error-code>]` where <error-code> is the code of the error to be silenced.
8. When both the main code file and its test file have been type annotated, remove both of them from the list `NOT_FULLY_COVERED_FILES` in `scripts/run_mypy_checks.py` so that these files are considered as type annotated.

For more information on adding types, refer to [Mypy Cheat Sheet(Python 2)](https://mypy.readthedocs.io/en/stable/cheat_sheet.html).

## Important Tips
### 1. Use `typing.Text` instead of `str` and `unicode`
**Reason**: `typing.Text` means `str` in python3 and `unicode` in python2. In python2, `str` is a subclass of `unicode`. So `typing.Text` won’t make it difficult to migrate to python3.
Note: Some errors like `Argument 1 to "<method-name>" has incompatible type "unicode"; expected "str"  [arg-type]` can arise due to this. 
This is because we accept `str` as `Text` in the methods and may give this value as an argument assumed to be of type `Text`(unicode or sub-class of unicode, i.e. str). So these errors should be silenced for smoother py3 migration along with types.

## Special Cases while adding Type Annotations
There are certain special cases that were encountered while adding type checks to our codebase. They are described below along with the solutions to tackle them.
### 1. Expected ‘\<type\>’ but got ’Optional[\<type\>]’
**Error explained**: If you access the attribute of a value with a union type, mypy checks that the attribute is defined for every type in that union. Otherwise the operation can fail at runtime. This also applies to optional types.
MyPy docs [link](https://mypy.readthedocs.io/en/stable/error_code_list.html#check-that-attribute-exists-in-each-union-item-union-attr) for this error.

#### a. 
##### Violation:
Dict.get(key) returns the value of the key in the dictionary or None. Thus MyPy assumes it to be Optional[<type>]


```
    @classmethod
    def _get(cls):
        # type: () -> Type[_Gae]

        return cls._PLATFORM_MAPPING.get(GAE_PLATFORM)

```



##### Solution:
To solve this, we will use Dict[key] instead of Dict.get(key). This is because the return type of Dict[key] is the value of the key in the dictionary. Make sure to handle the case that the key does not exist in the dictionary if it is required to do so.

```
    @classmethod
    def _get(cls):
        # type: () -> Type[_Gae]

        return cls._PLATFORM_MAPPING[GAE_PLATFORM]

```


### 2. Signature of "\<method_name\>" incompatible with supertype "\<ParentClass\>"
Error explained: A method in a subclass must accept all arguments that the base class method accepts, and the return type must conform to the return type in the base class.
MyPy docs [link](https://mypy.readthedocs.io/en/stable/error_code_list.html#check-validity-of-overrides-override) for this error.

#### a.
##### Violation:
Overridden methods or attributes must be compatible with the base class. Subclass method must accept all superclass method’s arguments and the return type can be a narrowed subclass.

```
class Platform(python_utils.OBJECT):

    @classmethod
    def import_models(cls):
    …

class _Gae(Platform):

    @classmethod
    def import_models(cls, model_names):
    …

```


##### Solution:
To solve this, we will change the base class method which accepts all subclass arguments. So we will add an unused argument to the base class method.


```
class Platform(python_utils.OBJECT):

    @classmethod
    def import_models(cls, unused_model_names):
    …

class _Gae(Platform):

    @classmethod
    def import_models(cls, model_names):
    …

```



### 3. Incompatible types in assignment (expression has type "\<type1\>", variable has type "\<type2\>") 
Error explained: Mypy checks whether the assigned expression is compatible with the assignment target (or targets) or not.
Mypy docs [link](https://mypy.readthedocs.io/en/stable/error_code_list.html#check-types-in-assignment-statement-assignment) for this error.


#### a.

##### Violation:

We assign variables to be of a particular type but later assign a value of different type.

We can see in the following example that `d` has different types. First it is assigned to a value of type `Dict[Text, Text[`, third assigned value is `Dict[Text, Union[Text, Dict[Text, Text]]]` and at last, it is assigned a value of type `List`.

```

def test_recursively_remove_key(self):
	# type: () -> None
	d = {'a': 'b'}
	utils.recursively_remove_key(d, 'a')
	self.assertEqual(d, {})

	d = {}
	utils.recursively_remove_key(d, 'a')
	self.assertEqual(d, {})

	d = {'a': 'b', 'c': 'd'}
	utils.recursively_remove_key(d, 'a')
	self.assertEqual(d, {'c': 'd'})

	d = {'a': 'b', 'c': {'a': 'b'}}
	utils.recursively_remove_key(d, 'a')
	self.assertEqual(d, {'c': {}})

	d = ['a', 'b', {'c': 'd'}]
	utils.recursively_remove_key(d, 'c')
	self.assertEqual(d, ['a', 'b', {}])
```

  

##### Solution:

The solution here is to break down the test into multiple smaller tests. For this, refer to point 1 [here](https://github.com/oppia/oppia/wiki/Writing-backend-tests#common-testing-scenarios). It states that if a function tests more than one behaviour, split the test into multiple parts.

  

```

    def test_recursively_remove_key_for_empty_dict(self):
        # type: () -> None
        d = {} # type: Dict[None, None]
        utils.recursively_remove_key(d, 'a')
        self.assertEqual(d, {})

    def test_recursively_remove_key_for_single_key_dict(self):
        # type: () -> None
        d = {'a': 'b'}
        utils.recursively_remove_key(d, 'a')
        self.assertEqual(d, {})

    def test_recursively_remove_key_for_multi_key_dict(self):
        # type: () -> None
        d = {'a': 'b', 'c': 'd'}
        utils.recursively_remove_key(d, 'a')
        self.assertEqual(d, {'c': 'd'})

    def test_recursively_remove_key_for_dict_with_value_dict(self):
        # type: () -> None
        d = {'a': 'b', 'c': {'a': 'b'}}
        utils.recursively_remove_key(d, 'a')
        self.assertEqual(d, {'c': {}})

    def test_recursively_remove_key_for_list(self):
        # type: () -> None
        l = ['a', 'b', {'c': 'd'}]
        utils.recursively_remove_key(l, 'c')
        self.assertEqual(l, ['a', 'b', {}])
```


## Some additional work due to python2 to python3 migration
Since we are currently using Python2, there may be some third party packages which don’t have stubs in the typeshed repository (i.e., the stubs repository which comes bundled with mypy). So there may be type check errors like:
no-untyped-call: 
Reason: Calling an untyped function is not allowed by default as per our configurations. 
Solution: We will need to ignore these errors by writing `# type: ignore[no-untyped-call]` at every place this error is thrown.
no-return-any: 
Reason: Returning a variable which mypy assumes to be of type ‘Any’ is not allowed by default as per our configurations. 
Solution: We will need to ignore these errors by writing `# type: ignore[no-return-any]` at every place this error is thrown.

We are in the process of python3 migration, and after it is complete, we won’t be using our old python2 third party libraries and with this, some of the ignores will be useless while some may still be required. Some would still be required because we won’t be having stubs for every third party library from the start. To identify type ignores that can be removed, we can leverage one peculiar functionality of  mypy - it throws errors when an ignore statement is not used and this will help us in removing extra ignore statements after python3 migration. 
Note: During the python3 migration phase, if we start seeing unused ignore errors then they would either have to be all fixed or they can be suppressed setting warn_unused_ignores as False in the mypy.ini file if needed.

