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
**Objective**: Identify where the error occurred in the code.
 
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
