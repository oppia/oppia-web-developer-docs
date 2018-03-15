# Writing Tests for Custom Pylint Checkers  
Currently, we have a custom checker build using Pylint which checks that keyword arguments are named explicitly in a function call. This checker is placed at `scripts/explicit_kwargs_checker_test.py` and is run using the `scripts/backend_tests.py` script.  
It has a function named `test_finds_non_explicit_kwargs` which uses the `astroid.extract_node` function to separate the different nodes.  
Example: 
```python
func_node = astroid.extract_node("""
        def test(test_var_one, test_var_two=4, test_var_three=5, test_var_four="test_checker"): #@
            test_var_five = test_var_two + test_var_three
            return test_var_five
        """)
```
The `#@` symbol indicates the line which `extract_node` needs to make the nodes of (Here, the function definition).  
For further details, please refer to [how to write and test a checker using Pylint](https://pylint.readthedocs.io/en/latest/how_tos/custom_checkers.html).  
