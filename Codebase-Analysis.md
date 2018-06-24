## Understanding what a function arg means

_If you're not sure what any argument in a function means, the following guidelines may help you figure it out._

First, check whether the arg name is decipherable. A lot of information about the arg can often be obtained by just reading the name. For example, if there is an arg named 'exploration_dicts', you can reasonably establish that this arg is a list of dictionary representations of the 'Exploration' object.

If that didn't work, another thing you could try would be to figure out how this arg is initialised when the function is called. For example, assume a function:

```
def func(some_arg):
    return some_arg.some_field
```

This doesn't make a lot of sense at first glance since it doesn't offer any information about the arg. But, if you search the file for where this function has been called:

```
some_arg = SomeObject(some_field, some_field2)
func(some_arg)
```

this tells us that the arg to this function in this case is an object of type 'SomeObject'. This, and other contextual clues, can help us decipher the meaning of the argument.

Note that, in some cases, the function might be called from a different file entirely, so it would also be a good idea to 'grep' through the codebase to find out where the function is being called from. You can do this by `grep "thing-to-grep" . -r --exclude-dir=third_party --exclude_dir=build --exclude-dir=backend_prod_files` (replace "thing-to-grep" with the phrase that you want to search for).

***

**Now, let's go through a full example of analyzing a function for the meaning of its args.**

There is a function defined in scripts/custom_lint_checks.py:

```
def check_single_constructor_params(self, class_doc, init_doc, class_node):
    if class_doc.has_params() and init_doc.has_params():
        self.add_message(
            'multiple-constructor-doc',
            args=(class_node.name,),
            node=class_node)
```

We want to decipher the meaning of the args 'class_doc', 'init_doc' and 'class_node'.

### 'class_doc'

It's unclear what this means from the name, so let's search the same file for function call for `check_single_constructor_params`. We find this block of code:

```
class_node = checker_utils.node_frame_class(node)
      if class_node is not None:
          class_doc = docstrings_checker.docstringify(class_node.doc)
          self.check_single_constructor_params(
              class_doc, node_doc, class_node)
```

within another function `check_functiondef_params(self, node, node_doc)`.

By looking at the line before the function call, we can understand that the `class_doc` arg has to be the return value of `docstrings_checker.docstringify(class_node.doc)`.

Traversing to the `docstrings_checker.py` file and searching for the `docstringify` method:

```
def docstringify(docstring):
    for docstring_type in [GoogleDocstring]:
        instance = docstring_type(docstring)
        if instance.is_valid():
            return instance

    return _check_docs_utils.Docstring(docstring)
```

This tells us that the return value of this function is of type `_check_docs_utils.Docstring(docstring)`. Now, checking the imports at the top of the page shows:

`from pylint.extensions import _check_docs_utils`

So, the pylint.extensions._check_docs_utils has a class called `Docstring` defined, and this is the type of `class_doc`. (This can be verified by looking at the pylint source code, since pylint is an open source library).

### 'init_doc':

Similarly, following the above reasoning, the `init_doc` can also be reasonably estimated to be an argument of type `Docstring`. Since the function in question is titled `check_functiondef_params`, the `init_doc` logically comes out to be "the Docstring class instance that represents the docstrings of the constructor for a class."

### 'class_node':

Searching around the custom_lint_checks.py file for occurrences of node and a possible type relation, we come across:

```
func_node = node.frame()
    if not isinstance(func_node, astroid.FunctionDef):
        return
```

inside the function 'visit_raise()'. This tells us that the 'func_node' is of type `astroid.FunctionDef`. Hence, we can infer that `class_node` is of type `astroid.ClassDef`.