# Tutorial: Learn How to Figure Out the Reproduction Steps for a Server Error

## Introduction

This tutorial will guide you through debugging a server error that is challenging to reproduce locally. Specifically, we will investigate and fix a `TypeError` related to certificate generation for contributors.

### Skills Covered:

- Codebase Navigation
- Identifying and Analyzing Error Logs
- Debugging Techniques
- Reproducing Server Errors Locally

### Scenario:

One of the server admins has reported the following error logs. Your task is to investigate the issue and determine how and why it is occurring.

> **Note:** The primary goal of this tutorial is not to find a solution, but to guide you through the process of investigating and understanding the workflow of debugging server errors. In this tutorial, you will follow the steps a developer might take to investigate this server error.

```plaintext
TypeError: expected string or bytes-like object 

Exception raised: expected string or bytes-like object 
Traceback (most recent call last): 
  File "/layers/google.python.pip/pip/lib/python3.8/site-packages/webapp2.py", line 604, in dispatch 
    return method(*args, **kwargs) 
  File "/workspace/core/controllers/acl_decorators.py", line 4788, in test_can_fetch_all_contributor_dashboard_stats 
    return handler(self, username, **kwargs) 
  File "/workspace/core/controllers/contributor_dashboard.py", line 1062, in get 
    response = suggestion_services.generate_contributor_certificate_data(
  File "/workspace/core/domain/suggestion_services.py", line 3870, in generate_contributor_certificate_data 
    data = _generate_translation_contributor_certificate_data(
  File "/workspace/core/domain/suggestion_services.py", line 3945, in _generate_translation_contributor_certificate_data 
    plain_text = _get_plain_text_from_html_content_string(
  File "/workspace/core/domain/suggestion_services.py", line 1408, in _get_plain_text_from_html_content_string 
    html_content_string_with_rte_tags_replaced = re.sub(
  File "/layers/google.python.runtime/python/lib/python3.8/re.py", line 210, in sub 
    return _compile(pattern, flags).sub(repl, string, count) 
TypeError: expected string or bytes-like object
```

## Procedure:

The following steps illustrate how a developer might tackle this issue. Try following this tutorial step-by-step on your local machine! This will give you a better sense of how to tackle other similar issues in the codebase. If you get stuck with a step in this tutorial, raise an issue in GitHub Discussions to get help.

**Important**: When you see a “practice question box”, stop and try to figure out the answer on your own before reading ahead. You will learn more if you try to figure out your own answer to the question first!

#### Setup:

**Install Oppia on Your Local Machine**  
To begin, you'll need to have Oppia installed on your local machine. If you haven't done so already, please follow the installation steps provided in this [wiki page](https://github.com/oppia/oppia/wiki).

**Check Out the Specific Commit**  
To ensure that you are working with the same version of the code as this tutorial, navigate to your local Oppia directory and check out the specific commit: 

```bash
git checkout 192f0a9a4866debac160015bc949130aaae6a7fe
```

**Verify the Commit:**  
You can verify that you are on the correct commit by running:

```bash
git log -1
```

The output should display the commit ID `192f0a9a4866debac160015bc949130aaae6a7fe`.

#### Debugging Process:

When faced with a server error, developers at Oppia typically follow these steps:

**Analyze the Error Logs to Locate the Affected Code:** Start by reviewing the error logs to find a stack trace that indicates where the error occurred. Pinpoint the relevant file, function, or line number where the problem originated.

**Examine the Affected Code:** Open the identified file(s) and examine the specific code blocks related to the error. Understand the intended functionality of the code and check for any immediate errors or inconsistencies.

**Investigate Potential Causes by Exploring the Code in Depth:** Consider possible reasons for the error, such as incorrect data types, missing conditions, edge cases, or unexpected inputs. Dive deeper into the code, focusing on sections that are most likely causing the issue. Look for logic errors, unhandled cases, or data processing problems that align with your initial suspicions.

**Reproduce the Error:** Set up an environment to recreate the conditions that led to the error. Use test data or modify unit tests to replicate the issue and confirm your hypotheses about its cause.

**Document Your Findings:** Once you've identified and confirmed the cause of the error, document your findings in detail on the original GitHub issue. Provide a summary of the error, clear steps to reproduce it, and any relevant observations or logs to support your conclusions.

### Stage 1: Analyze the Error Logs to Locate the Affected Code
> **Objective**: Identify where the error occurred in the code.
 
> **Note**: This tutorial focuses on server errors, which are typically reported by server admins and come with error logs. For other issues, such as user-reported bugs, error logs might not always be available. In these cases, it is essential to ask users for "steps to reproduce the bug." If this information is not provided, we can contact the user to request additional details that will help us understand the issue better.

Here is the error log we need to investigate:

```python
TypeError: expected string or bytes-like object 

Exception raised: expected string or bytes-like object 
Traceback (most recent call last): 
  File "/layers/google.python.pip/pip/lib/python3.8/site-packages/webapp2.py", line 604, in dispatch
    return method(*args, **kwargs) 
  File "/workspace/core/controllers/acl_decorators.py", line 4788, in test_can_fetch_all_contributor_dashboard_stats 
    return handler(self, username, **kwargs) 
  File "/workspace/core/controllers/contributor_dashboard.py", line 1062, in get 
    response = suggestion_services.generate_contributor_certificate_data(
  File "/workspace/core/domain/suggestion_services.py", line 3870, in generate_contributor_certificate_data 
    data = _generate_translation_contributor_certificate_data(
  File "/workspace/core/domain/suggestion_services.py", line 3945, in _generate_translation_contributor_certificate_data 
    plain_text = _get_plain_text_from_html_content_string(
  File "/workspace/core/domain/suggestion_services.py", line 1408, in _get_plain_text_from_html_content_string 
    html_content_string_with_rte_tags_replaced = re.sub(
  File "/layers/google.python.runtime/python/lib/python3.8/re.py", line 210, in sub 
    return _compile(pattern, flags).sub(repl, string, count) 
TypeError: expected string or bytes-like object
```

#### Understanding the Stack Trace:

A **stack trace** is a report of the active stack frames at a certain point in time during the execution of a program. It shows the call sequence leading to the point where the error occurred. Each line provides the file name, line number, and function where the error occurred.

- The stack trace is read **from the bottom up** to understand the sequence of function calls leading to the error.
- The bottom-most lines generally point to standard library or third-party code (in this case, `re.py` from Python's standard library).
- Moving upward, you start seeing calls within the project codebase, which is where we should focus.
- The key is to find the first instance where **Oppia's code interacts with the point of failure**.


>[!IMPORTANT]
> Practice 1: Locate the specific line in the stack trace where Oppia's code is directly involved in causing the failure. This is the point where the error is most likely to originate within the Oppia codebase.
> 
> **Hint**: Look for the first occurrence (from the bottom of the stack trace upward) where the stack trace shows a line of code from the Oppia codebase. This line represents the entry point in the Oppia code that led to the failure. Identifying this line will help you trace the error back to its origin in the code.


In this stack trace, the relevant line is:

```python
File "/workspace/core/domain/suggestion_services.py", line 1408, in _get_plain_text_from_html_content_string html_content_string_with_rte_tags_replaced = re.sub(
```


This line indicates that the error originated in the `_get_plain_text_from_html_content_string` function within the `suggestion_services.py` file.

You have identified the error location in the codebase and gathered initial clues about what might have gone wrong.

Next Step: Pinpoint the specific part of the code causing the error.

>[!IMPORTANT]
> Practice 2: Locate the `_get_plain_text_from_html_content_string` function in the `suggestion_services.py` file.
> 
> **Hint**: To locate the function, you can make use of search functionalities of your code editor. [Tips for Common IDEs](https://github.com/oppia/oppia/wiki/Tips-for-common-IDEs)

```python
File "/workspace/core/domain/suggestion_services.py", line 1408, in _get_plain_text_from_html_content_string html_content_string_with_rte_tags_replaced = re.sub( File "/layers/google.python.runtime/python/lib/python3.8/re.py", line 210, in sub return _compile(pattern, flags).sub(repl, string, count) TypeError: expected string or bytes-like object
```

Based on the error logs, the issue arises because the argument passed to the re.sub() function in the _get_plain_text_from_html_content_string method is not of the expected data type (a string or bytes-like object).

You have now pinpointed the exact file, function, and line where the issue originated and are ready to dive deeper into the problem area.

### Stage 2: Examine the Affected Code
> **Objective**: Analyze the affected code to understand its intended behavior and determine what might have gone wrong.

Examine the _get_plain_text_from_html_content_string function to understand its purpose and the specific operation where the error occurs.

<details>
  <summary>Here's the function:</summary>

```python
def _get_plain_text_from_html_content_string(html_content_string: str) -> str:
   """Retrieves the plain text from the given html content string. RTE element
   occurrences in the html are replaced by their corresponding rte component
   name, capitalized in square brackets.
   eg: <p>Sample1 <oppia-noninteractive-math></oppia-noninteractive-math>
       Sample2 </p> will give as output: Sample1 [Math] Sample2.
   Note: similar logic exists in the frontend in format-rte-preview.filter.ts.

   Args:
       html_content_string: str. The content html string to convert to plain
           text.

   Returns:
       str. The plain text string from the given html content string.
   """

   def _replace_rte_tag(rte_tag: Match[str]) -> str:
       """Replaces all of the <oppia-noninteractive-**> tags with their
       corresponding rte component name in square brackets.

       Args:
           rte_tag: MatchObject. A matched object that contains the
               oppia-noninteractive rte tags.

       Returns:
           str. The string to replace the rte tags with.
       """
       # Retrieve the matched string from the MatchObject.
       rte_tag_string = rte_tag.group(0)
       # Get the name of the rte tag. The hyphen is there as an optional
       # matching character to cover the case where the name of the rte
       # component is more than one word.
       rte_tag_name = re.search(
           r'oppia-noninteractive-(\w|-)+', rte_tag_string)
       # Here, rte_tag_name is always going to exists because the string
       # that was passed in this function is always going to contain
       # `<oppia-noninteractive>` substring. So, to just rule out the
       # possibility of None for mypy type checking. we used assertion here.
       assert rte_tag_name is not None
       # Retrieve the matched string from the MatchObject.
       rte_tag_name_string = rte_tag_name.group(0)
       # Get the name of the rte component.
       rte_component_name_string_list = rte_tag_name_string.split('-')[2:]
       # If the component name is more than word, connect the words with spaces
       # to create a single string.
       rte_component_name_string = ' '.join(rte_component_name_string_list)
       # Captialize each word in the string.
       capitalized_rte_component_name_string = (
           rte_component_name_string.title())
       formatted_rte_component_name_string = ' [%s] ' % (
           capitalized_rte_component_name_string)
       return formatted_rte_component_name_string

   # Replace all the <oppia-noninteractive-**> tags with their rte component
   # names capitalized in square brackets.
   html_content_string_with_rte_tags_replaced = re.sub(
       r'<oppia-noninteractive-[^>]+>(.*?)</oppia-noninteractive-[^>]+>',
       _replace_rte_tag, html_content_string)
   # Get rid of all of the other html tags.
   plain_text = html_cleaner.strip_html_tags(
       html_content_string_with_rte_tags_replaced)
   # Remove trailing and leading whitespace and ensure that all words are
   # separated by a single space.
   plain_text_without_contiguous_whitespace = ' '.join(plain_text.split())
   return plain_text_without_contiguous_whitespace
```

</details>

> [!IMPORTANT]
> Practice 3: Locate the lines which are causing the error in the above mentioned function.
>
> **Hint**: Review the error logs. In a real debugging scenario, the stack trace would help you pinpoint this specific line as the source of the error.

In this stack trace, the relevant line is:

```python
File "/workspace/core/domain/suggestion_services.py", line 1408, in _get_plain_text_from_html_content_string html_content_string_with_rte_tags_replaced = re.sub(
```

This line indicates that the error originated in the `_get_plain_text_from_html_content_string` function within the `suggestion_services.py` file at line number 1408. Let’s take a look at that line:

```python
html_content_string_with_rte_tags_replaced = re.sub(     r'<oppia-noninteractive-[^>]+>(.*?)</oppia-noninteractive-[^>]+>',
       _replace_rte_tag, html_content_string)
```

Note that the third parameter, `html_content_string`, is being passed to the `re.sub` function and that this parameter is the argument of the function `_get_plain_text_from_html_content_string`.

The `re.sub` function is used to replace certain HTML tags. According to the Python documentation for `re.sub`, it expects the first argument to be a pattern, the second argument to be a replacement string, and the third argument to be the string to be searched and replaced.

Even though the re.sub [documentation](https://docs.python.org/3/library/re.html#re.sub) doesn't explicitly mention the TypeError, we can infer the following:
- **TypeError Convention**: In Python, TypeError is conventionally raised to indicate that an operation or function received an argument of an inappropriate type. This means that if re.sub expects a string or bytes-like object but receives a different type, it raises a TypeError.
- **Error Message**: The error message "expected string or bytes-like object" indicates that re.sub was given an argument that wasn't a string or bytes-like object, which is why it raised a `TypeError`.

> [!IMPORTANT]
> **Practice 4**: Determine where the `html_content_string` is coming from.
>
> **Hint**: Review the error logs carefully. Pay close attention to the lines mentioned in the stack trace, especially the one that is calling the `_get_plain_text_from_html_content_string` function. This will give you a clue about where the `html_content_string` originates.

According to the error log, this function is called in `suggestion_services.py` within the `_generate_translation_contributor_certificate_data` function.

```python
# Retrieve the html content that is emphasized on the
# Contributor Dashboard pages. This content is what stands
# out for each suggestion when a user views a list of
# suggestions.
get_html_representing_suggestion = (
    SUGGESTION_EMPHASIZED_TEXT_GETTER_FUNCTIONS[
        Suggestion.suggestion_type]
    )
plain_text = _get_plain_text_from_html_content_string(
get_html_representing_suggestion(suggestion))
```

As we can see, we are passing the output of the function, `get_html_representing_suggestion(suggestion)` as the input to the function  `_get_plain_text_from_html_content_string`.

Let’s take a closer look at the method `get_html_representing_suggestion(suggestion)`. This method handles different types of suggestions and retrieves the corresponding HTML content based on the type of suggestion.

In the context of this method, two lambda functions are defined to extract HTML content based on the `suggestion_type`:

**For translation suggestions:**
```python
SUGGESTION_TRANSLATE_CONTENT_HTML: Callable[
    [suggestion_registry.SuggestionTranslateContent], str
] = lambda suggestion: suggestion.change_cmd.translation_html
```
This lambda function is used when the suggestion type is related to translating content. It retrieves the translation_html property from the change_cmd attribute of the suggestion object.

**For question suggestions:**
```python
SUGGESTION_ADD_QUESTION_HTML: Callable[
    [suggestion_registry.SuggestionAddQuestion], str
] = lambda suggestion: suggestion.change_cmd.question_dict[
    'question_state_data']['content']['html']
```

This lambda function is used when the suggestion type involves adding a question. It retrieves the `html` property from the `question_state_data` dictionary inside the `question_dict` of the suggestion object.

> [!IMPORTANT]
> Practice 5: Based on the code provided and the context of the lambda functions, what could potentially go wrong with the data being accessed? Specifically, think about the structure of the suggestion.change_cmd.question_dict['question_state_data']['content']['html'] and suggestion.change_cmd.translation_html fields. What potential data type or structure issues could arise here?

One possible issue is that the `html` property of the `question_dict` or the `translation_html` field might not always be a string as expected. It could be `None` or another data type entirely, which would cause issues when the `_get_plain_text_from_html_content_string` function tries to process it. If the function is expecting a string but receives a different type (such as `None` or a more complex object), it could result in a `TypeError`. This could explain why the error indicates that a string or bytes-like object was expected but something else was provided.

In this case, the issue is likely that either `suggestion.change_cmd.translation_html` or `suggestion.change_cmd.question_dict['question_state_data']['content']['html']` is not always a string, leading to the observed error when passed to the `re.sub()` function.

> You now understand the purpose and expected behavior of the affected code and have identified areas where discrepancies may have occurred.