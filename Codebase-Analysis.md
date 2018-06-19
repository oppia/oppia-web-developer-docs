# Understanding what a function arg means(for code without documentation):

**If you face the trouble of not understanding what any argument in a function means, when you're**
**trying to document the function, follow these guidelines for figuring it out.**

First and foremost, check whether the arg name is decipherable. A lot of information
about the arg can usually be obtained, by just reading the name. For example,
if there is an arg named 'exploration_dicts', you can reasonably establish that this arg
is a list of dictionary representations of the 'Exploration' object.

If you're at this step, the function name probably did not offer all the information
required. Now, a reasonable step to perform would be to figure out how this arg is
initialised when the function is called. For example, assume a function:

```
def func(some_arg):
    return some_arg.some_field
```

This doesn't make a lot of sense at first glance since it doesn't offer any information
about the arg. But, if you search the
file for where this function has been called,

```
some_arg = SomeObject(some_field, some_field2)
func(some_arg)
```

Now, we know that the arg to this function in this case is an object of type
'SomeObject'. So, we could traverse up to the function call to decipher the meaning
of the arg.

PS: In some cases, the function might be called from a different file completely, so
it would make sense to 'grep' through the codebase to find out instances of function
call.


***




**Now, let's go through a full example of analyzing a function for the meaning of its' args.**

There is a function defined in scripts/custom_lint_checks.py:

```
def check_single_constructor_params(self, class_doc, init_doc, class_node):
    if class_doc.has_params() and init_doc.has_params():
        self.add_message(
            'multiple-constructor-doc',
            args=(class_node.name,),
            node=class_node)
```

We are deciphering the meaning of the args 'class_doc', 'init_doc' and 'class_node'.

1. 'class_doc':

Now I search the same file for function call for 'check_single_constructor_params'.
I found this block of code:

```
class_node = checker_utils.node_frame_class(node)
      if class_node is not None:
          class_doc = docstrings_checker.docstringify(class_node.doc)
          self.check_single_constructor_params(
              class_doc, node_doc, class_node)
```

within another function 'check_functiondef_params(self, node, node_doc)'.

By looking at the line before the function call, we can understand that the
'class_doc' arg has to be the return value of the docstrings_checker.docstringify(class_node.doc)

Traversing to the docstrings_checker file and searching for the docstringify method:

```
def docstringify(docstring):
    for docstring_type in [GoogleDocstring]:
        instance = docstring_type(docstring)
        if instance.is_valid():
            return instance

    return _check_docs_utils.Docstring(docstring)
```

We understand that the return value of this function is of type _check_docs_utils.Docstring(docstring).
Now, checking the imports at the top of the page:

`from pylint.extensions import _check_docs_utils`

So, the pylint.extensions._check_docs_utils has a class called 'Docstring' defined
and this is type of class_doc (the class can be verified online, since pylint is another
open source library.)

2. 'init_doc':

Similarly, following the above reasoning, the 'init_doc' can also be reasonably
estimated to be an argument of type 'Docstring'. Since the function in concern is
titled 'check_functiondef_params', the 'init_doc' logically comes out to be "the
Docstring class instance represnting the docstrings of the constructor for a class."

3. 'class_node':

Searching around the custom_lint_checks.py file for occurences of node and a possible
type relation, we come across:

```
func_node = node.frame()
    if not isinstance(func_node, astroid.FunctionDef):
        return
```

inside function 'visit_raise()'.
This lets us know that the 'func_node' is of type 'astroid.FunctionDef'.
Hence, a reasonable estimation would be that 'class_node' is of type 'astroid.ClassDef'