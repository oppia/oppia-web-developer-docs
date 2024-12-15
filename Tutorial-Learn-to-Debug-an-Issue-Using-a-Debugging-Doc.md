## Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Scenario](#scenario)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Procedure](#procedure)
    - [**Step 1: Establishing the Background and Analyzing Code Changes**](#step-1-establishing-the-background-and-analyzing-code-changes)
      - [1.1 Review the Product Requirement Document (PRD) and Key Specifications](#11-review-the-product-requirement-document-prd-and-key-specifications)
      - [1.2 Analyze the Code Changes that Introduced the Issue](#12-analyze-the-code-changes-that-introduced-the-issue)
      - [1.3 Identifying the Error](#13-identifying-the-error)
      - [Key Takeaways](#key-takeaways)
    - [Step 2: Capturing the Problem Scope](#step-2-capturing-the-problem-scope)
      - [2.1 What to Include in the Debugging Doc](#21-what-to-include-in-the-debugging-doc)
      - [2.2  Example: Filling in the Debugging Doc for Our Scenario](#22--example-filling-in-the-debugging-doc-for-our-scenario)
      - [Key Takeaways](#key-takeaways-1)
    - [Step 3: Conducting and Documenting the Initial Investigation for Affected Code and Context.](#step-3-conducting-and-documenting-the-initial-investigation-for-affected-code-and-context)
      - [Example: Applying the Code-Level Investigation Steps](#example-applying-the-code-level-investigation-steps)
      - [Key Takeaways](#key-takeaways-2)
    - [Step 4: Hypothesis Testing](#step-4-hypothesis-testing)
      - [4.1 How to Formulate Hypotheses](#41-how-to-formulate-hypotheses)
      - [4.2 Documenting Hypotheses](#42-documenting-hypotheses)
      - [4.3 Tips for Hypothesis Testing](#43-tips-for-hypothesis-testing)
      - [Key Takeaways](#key-takeaways-3)
    - [Step 5: Documenting the Solution](#step-5-documenting-the-solution)
      - [Our Case: Understanding the Fix](#our-case-understanding-the-fix)
- [Conclusion](#conclusion)
    - [Appendix](#appendix)
    - [We Value Your Feedback](#we-value-your-feedback)

## Introduction

When you encounter a challenging issue, documenting your debugging process can be incredibly helpful. A structured approach keeps your thoughts organized, helps you track the steps you’ve already tried, and makes it easier for others to collaborate with you. At Oppia, we use a "[debugging doc](https://docs.google.com/document/d/1qRbvKjJ0A7NPVK8g6XJNISMx_6BuepoCL7F2eIfrGqM/edit?tab=t.0#heading=h.ieezq05wy6da)" to achieve this.

Creating a debugging doc not only helps you stay organized but also fosters collaboration by allowing others to jump in without repeating steps. Additionally, these docs serve as invaluable learning resources for your team, capturing solutions and insights that can simplify future debugging efforts.

If you cannot find a solution within 30 minutes, we recommend documenting your progress and sharing it with your team. This allows you to reflect on your attempts while providing others an opportunity to contribute fresh perspectives.

This tutorial will guide you on how to write a debugging doc and effectively communicate your thought process to seek help or share insights.

## Scenario

This issue we are going to tackle in this tutorial arose during the development of a [**GSoC project**](https://docs.google.com/document/d/1Uh_CJRhGE4IM7c0ENdmXkoMD0YtGqFsl1ObR6vvmxdY/edit#bookmark=id.okubcuk2vtnw). The goal of the project was to implement a new filtering feature in the Topics and Skills Dashboard. To ensure that the feature could be thoroughly tested without disrupting existing workflows, it was gated behind a [feature flag](https://github.com/oppia/oppia/wiki/Launching-new-features), enabling a phased rollout and internal testing before making it available to all users. 

We introduced the feature flag, `SerialChapterLaunchCurriculumAdminView`, in [Pull Request \#18283](https://github.com/oppia/oppia/pull/18283). This flag gates the filtering functionality in `topics-and-skills-dashboard-page.service.ts`, showing the new feature options when the flag is enabled.

However, during development, a frontend test failed with the following error:

`Error: Cannot read properties of undefined (reading 'status')`

Error Log:

```typescript
TypeError: Cannot read properties of undefined (reading 'status')
    at TopicsAndSkillsDashboardPageService.getFilteredTopics (core/templates/combined-tests.spec.js:212040:31027)
    at UserContext.<anonymous> (core/templates/combined-tests.spec.js:211960:30)
    at ./node_modules/zone.js/dist/zone.js.ZoneDelegate.invoke (core/templates/combined-tests.spec.js:774051:30)
    at ./node_modules/zone.js/dist/proxy.js.ProxyZoneSpec.onInvoke (core/templates/combined-tests.spec.js:773536:43)
    at ./node_modules/zone.js/dist/zone.js.ZoneDelegate.invoke (core/templates/combined-tests.spec.js:774050:36)
    at ./node_modules/zone.js/dist/zone.js.Zone.run (core/templates/combined-tests.spec.js:773808:47)
    at runInTestZone (core/templates/combined-tests.spec.js:773091:38)
    at UserContext.<anonymous> (core/templates/combined-tests.spec.js:773106:24)
    at <Jasmine>
```

This error suggests that the `platformFeatureService` variable, which controls the feature gating, is not properly initialized in the test environment. As a result, when the code attempts to access the `status` property of `platformFeatureService`, it encounters an `undefined` error, leading to a test failure.

For more details on how feature flags and the `platformFeatureService` are set up, refer to the [Oppia Wiki on Launching New Features](https://github.com/oppia/oppia/wiki/Launching-new-features#frontend).

In the following sections, we’ll break down the debugging process step-by-step, investigating potential causes, testing hypotheses, and adjusting the test environment configuration to handle the feature flag effectively.

## Prerequisites

Before diving into this tutorial, ensure you have the following in place:

1. Make sure your development environment is properly configured. If not, follow the [Oppia Setup Instructions](https://github.com/oppia/oppia/wiki/Installing-Oppia).  
2. Understanding how the Topics and Skills dashboard works will be crucial. Refer to:  
   * [User Guide: Topics and Skills Dashboard](https://oppia-user-guide.readthedocs.io/en/latest/admins/skills.html)  
   * [How to Access Topics and Skills Pages](https://github.com/oppia/oppia/wiki/How-to-access-Oppia-webpages#topics-and-skills-pages)  
3. As this tutorial deals with feature gating, it’s important to know how new features are launched with feature flags in Oppia. Read:[Launching New Features](https://github.com/oppia/oppia/wiki/Launching-new-features)  
4. To make the most out of this tutorial, review the process and format of a debugging doc.  
   * [Oppia Debugging Docs](https://github.com/oppia/oppia/wiki/Debugging-Docs)

## Setup

Follow these steps to set up your environment for this tutorial:

1. **Check Out the Specific Commit:** To ensure consistency, we’ll be working from a specific commit. Use the following command to switch to the relevant commit:   
   `git checkout 794b5d78e88f585efadc366b767889596afccacb`  
   This ensures you are working with the same version of the code referenced in this tutorial.  
2. **Apply the Patch File:** Download the patch file from the [provided link](https://github.com/oppia/oppia-web-developer-docs/blob/develop/patchFiles/tutorial-debugging-doc-setup.patch) and apply it to your local branch: `git apply /path/to/your/patch-file.patch`  
   Replace `/path/to/your/patch-file.patch` with the actual location of the downloaded patch file on your machine.  
3. **Verify the Commit:** After applying the patch, verify that you are on the correct commit: `git log -1`   
   You should see the commit hash `794b5d78e88f585efadc366b767889596afccacb` in the output.

## Procedure

***Note:** This tutorial emphasizes documenting your debugging journey in a "debugging doc." The aim isn’t just to solve the issue independently but to record your insights and observations in a way that supports team collaboration. While we won’t dive into complete end-to-end debugging, we’ll cover essential steps to express your thought process clearly and effectively for others to build on.*

#### **Step 1: Establishing the Background and Analyzing Code Changes**

Before we start debugging, it’s essential to understand the broader context and the exact changes that might have led to this issue. This preparation helps create a well-rounded understanding of the feature itself and the new code, setting a strong foundation for effective debugging.

> [!IMPORTANT]
> **Practice 1**: Before diving into debugging, let’s ensure you have a solid understanding of the resources you’ll need. Take a moment to read through the following key documents carefully:
> - [PRD for Topics & Skills Dashboard](https://docs.google.com/document/d/1Uh_CJRhGE4IM7c0ENdmXkoMD0YtGqFsl1ObR6vvmxdY/edit?tab=t.0#bookmark=id.okubcuk2vtnw): This document covers the objectives and requirements for the new feature, providing context on the expected behavior.
> - [Oppia Feature Flag Guide](https://github.com/oppia/oppia/wiki/Launching-new-features#changing-value-of-feature-flags): Essential for understanding how to implement and toggle feature flags, which is central to this debugging scenario.
> - [Frontend Tests Wiki Page](https://github.com/oppia/oppia/wiki/Frontend-tests): A key aspect of this issue is related to the frontend testing environment. This guide provides an overview of how frontend tests are structured and executed at Oppia, which is valuable for diagnosing test-specific issues.
> - [Debugging Guide for Oppia](https://github.com/oppia/oppia/wiki/Debugging): This guide offers best practices and strategies for systematic troubleshooting within the Oppia codebase, helping you navigate common debugging challenges.
> 
> By thoroughly reviewing these resources, you’ll build a solid foundation for understanding and resolving the issue in this tutorial. Once you’re ready, continue to the next section to apply these insights!

By examining both the PRD and technical documentation, you’ll gain a comprehensive understanding of the feature requirements and the general debugging practices followed at Oppia. This knowledge will provide a foundation for identifying and resolving the error effectively.

##### 1.1 Review the Product Requirement Document (PRD) and Key Specifications

The goal of this feature is to enhance the Topics and Skills Dashboard by introducing new filtering and sorting capabilities. These improvements aim to provide users with more precise options for viewing story publication statuses and sorting by launch timelines. To ensure the feature aligns with its intended behavior, it's important to review the PRD and relevant technical documentation, which bridges the gap between the feature’s design and its implementation.

**Key Features from the PRD:**

* **Added Stories:** Displays the total count of stories associated with each topic, categorized by publication status (fully published, partially published, or unpublished). This gives users a quick way to assess content readiness.  
* **New Filtering and Sorting Options:**  
  * **Status Filter:** Enables filtering of topics based on publication status, allowing users to narrow down their view to topics that match specific criteria.  
  * **Sorting Options:** Adds sorting choices, such as "Most Upcoming Launches" and "Most Launches Behind Schedule," which prioritize topics by their launch timelines.

Understanding these features will provide insight into the intended functionality, helping us identify where any potential issues with the new filtering and sorting logic might lie.

##### 1.2 Analyze the Code Changes that Introduced the Issue

After reviewing the specifications, the next step is to analyze the code changes that introduced the error. In this case, the error seems connected to `platformFeatureService`, which appears undefined in the test environment. A helpful starting point is to identify the files impacted by recent changes. 

> [!IMPORTANT]
> **Practice 2**: Take a moment to review the modifications introduced by the patch file. This will help you see how the feature is structured and understand which parts of the codebase might be contributing to the issue. As you review the changes, make a list summarizing the key modifications. This will help you pinpoint the areas of interest. You can compare your list to the one provided in the next section to ensure you’ve captured all critical updates.
>
> **Hint**: You can run `git status` in your feature branch to view the modified files.

Running `git status` in your feature branch will show the modified files, highlighting where recent updates occurred.

Here’s a summary of the key code changes:

* In `assets/constants.ts`:  
  * Added a new constant `TOPIC_SKILL_DASHBOARD_SORTING_OPTIONS`, which includes options like "Most Upcoming Launches" and "Most Launches Behind Schedule."  
  * Updated values like `BRANCH_NAME` and `SHORT_COMMIT_HASH` for versioning.  
* In `topics-and-skills-dashboard-filter.model.ts`:  
  * Updated the `TopicsAndSkillsDashboardFilter` class to accommodate new sorting and status options.  
  * The constructor now accepts new option types to handle these additional filters.  
* In `topics-and-skills-dashboard-page.component.spec.ts`:  
  * Introduced a mock `PlatformFeatureService` for testing.  
  * This mock service simulates the `SerialChapterLaunchCurriculumAdminView` feature flag being enabled or disabled during testing.  
* In `topics-and-skills-dashboard-page.component.ts`:  
  * Added type definitions for `TopicStatusOptionsKeys` and `TopicSortingOptionsKeys`.  
  * Inject the `PlatformFeatureService` into the component’s constructor to check whether the new sorting and filtering options should be displayed.  
* In `topics-and-skills-dashboard-page.constants.ts`:  
  * Added new enums: `ETopicSortingOptions` and `ETopicStatusOptions`, which define the additional sorting and filtering options for topics.  
* In `topics-and-skills-dashboard-page.service.spec.ts`:  
  * Updated unit tests to include the new sorting and status options.  
  * Added tests for the feature flag `SerialChapterLaunchCurriculumAdminView` to ensure the functionality is properly toggled on and off during testing.  
* In `topics-and-skills-dashboard-page.service.ts`:  
  * Injected the `PlatformFeatureService` to determine whether the new filtering and sorting options should be applied.  
  * Updated the `getFilteredTopics` method to handle the new options and added conditional logic to enable them based on the feature flag.  
* In `UpgradedServices.ts`:  
  * Updated the initialization of `TopicsAndSkillsDashboardPageService` to include the `PlatformFeatureService`.

***Note:** To get a sense of how the feature behaves in practice, try enabling it on your local server. This can help verify that the core functionality is working correctly.*

##### 1.3 Identifying the Error

Now that we’ve looked at the code, let's focus on the error message:  
 `Error: Cannot read properties of undefined (reading 'status')`

> [!IMPORTANT]
> **Practice 3**: Now that you’ve reviewed the modified files, analyze the error logs generated during test execution. Look closely at the error trace to identify the exact functions and files where the issue surfaces. This will help you pinpoint areas to investigate further.
> 
> **Hint**: Debugging frontend tests can be tricky because the stack traces in Jasmine (our testing framework) often lack accurate line numbers. While improvements were considered in [#9648](https://github.com/oppia/oppia/issues/9648), Jasmine’s limitations meant we couldn’t implement a solution. To work around this, try using test names to locate the relevant code files or examine the variable or function that’s causing the error.

This error message indicates that `platformFeatureService` is undefined during testing, leading to a failure when accessing `platformFeatureService.status`. This points to a potential issue with how the service or the feature flag is being mocked in the test environment, especially in scenarios involving feature gating.

##### Key Takeaways

In this section, we’ve laid the groundwork for debugging by establishing the background and analyzing code changes. Here’s how to apply these insights more broadly:

* **Thorough Background Review**: Always review relevant PRDs, specifications, technical documentation, and linked GitHub issues. If others previously worked on this issue, try reaching out for follow-up details. Understanding the intended behavior helps you focus on specific code paths where errors might arise.  
* **Track and Analyze the Affected Code**: Identify impacted files and code by reading the error stack trace, which often leads directly to the source of the problem.  
* **Observe Feature Behavior in Different Environments**: Testing across environments—like a local server, production, CI, or pre-push hooks—can reveal configuration-specific issues. Identify where the error occurs, as it can often point to setup or dependency mismatches.

By building a strong foundation with these insights, the debugging process becomes smoother and more efficient. In the next section, we’ll explore documenting the initial investigation and preparing a comprehensive debugging doc for deeper analysis.

#### Step 2: Capturing the Problem Scope

In this step, we will outline the information that needs to be included in a debugging doc following the [Oppia template](https://docs.google.com/document/d/1qRbvKjJ0A7NPVK8g6XJNISMx_6BuepoCL7F2eIfrGqM/edit?tab=t.0#heading=h.ieezq05wy6da). This helps to structure your findings so others can quickly understand the issue’s context and progression. We’ll use our example scenario to illustrate.

> [!IMPORTANT]
> **Practice 4**: Make a copy of [Oppia’s debugging template](https://docs.google.com/document/d/1qRbvKjJ0A7NPVK8g6XJNISMx_6BuepoCL7F2eIfrGqM/edit?tab=t.0#heading=h.ieezq05wy6da) and explore its structure. Pay special attention to the text in the yellow boxes—they contain instructions on how to effectively document each section of the debugging doc.
>
> **Hint**: Start by reading through each section’s instructions to understand the type of information required. This will give you a clear framework for documenting your findings in a way that others can easily follow.

##### 2.1 What to Include in the Debugging Doc

To ensure an effective debugging doc, include the following critical components:

* **Description of the Problem**: Summarize the issue, focusing on the feature’s purpose and where the error arises. This background helps clarify the specific context and goals of the feature.  
* **Error Log**: Copy the specific error message that appears in your console or logs. Trim any extraneous details to focus on the key part of the error stack, as this will help pinpoint the issue.  
* **Where the Problem Occurred**: Indicate where the error is happening (e.g., local machine, CI environment). Knowing this context is critical for narrowing down configuration or environment-related issues.  
* **Steps to Reproduce the Error**: Document the exact steps taken to encounter the issue. This allows others to replicate the error and better understand the surrounding conditions.  
* **Reliability of the Error**: State if the error occurs consistently or intermittently. Consistent errors may indicate a clear coding issue, while intermittent ones could suggest timing or environmental factors.

##### 2.2  Example: Filling in the Debugging Doc for Our Scenario

> [!IMPORTANT]
> **Practice 5**: Using the insights gathered so far, try drafting the initial investigation and background section of your debugging doc. Focus on clearly summarizing the issue, where it occurs, and any specific error messages you’ve seen. This exercise will help you organize your findings and provide a clear foundation for troubleshooting.

Here’s how the initial investigation might look for our example scenario.

**Description of the Problem**  
The error occurs while implementing new filtering and sorting features in the Topics and Skills Dashboard. This feature uses a flag, `SerialChapterLaunchCurriculumAdminView`, to toggle sorting options. When running frontend tests, the code fails with an error indicating that `platformFeatureService` is `undefined`, which prevents the feature flag from being accessed.

The feature itself works as expected when tested manually on a local server, but the error surfaces during automated testing, suggesting an issue with the service setup or the mocking of dependencies in the test environment.

**Error Log**

```typescript
Error: Cannot read properties of undefined (reading 'status')
TypeError: Cannot read properties of undefined (reading 'status')
   at TopicsAndSkillsDashboardPageService.getFilteredTopics (core/templates/combined-tests.spec.js:212040:31027)
   at UserContext.<anonymous> (core/templates/combined-tests.spec.js:211960:30)
```

This error log shows that the `platformFeatureService.status` property cannot be accessed in the `getFilteredTopics` function, which is where the sorting and filtering options are managed based on the feature flag.

**Where the Problem Occurred**  
The issue occurs during local testing on the developer’s machine.

**Steps to Reproduce the Error**

1. Apply the patch file containing the new filtering and sorting feature changes.  
2. Implement the filtering and sorting feature in `topics-and-skills-dashboard-page.service.ts`.  
3. Run the frontend tests using `python -m scripts.run_frontend_tests`.  
4. Observe the error in the console during test execution.

**Reliability of the Error**

The error occurs consistently with each test run.

##### Key Takeaways

In this section, we’ve set up a well-documented initial investigation, providing a comprehensive overview of the issue. Here’s how to apply this approach generally:

* **Detailed Problem Context**: Always start with a concise problem summary that includes the intended feature behavior. This helps frame the issue for anyone new to it.  
* **Highlight Key Errors**: Capture and trim error logs to show only the most relevant details. This keeps focus on the main problem without distracting noise.  
* **Reproducibility**: Clear steps to reproduce the error are invaluable for collaborators. Make sure to include any specific setup or patches needed for replication.

By structuring your initial investigation carefully, you’ll have a clear foundation for diving into hypothesis testing and further debugging in the next steps.

In the following section, we’ll proceed to hypothesis testing and explore various methods to uncover the root cause systematically.

#### Step 3: Conducting and Documenting the Initial Investigation for Affected Code and Context.

With a foundational understanding of the issue, the next step is an initial code-level investigation. This stage focuses on pinpointing the exact files, functions, and dependencies related to the error. Documenting this step in your debugging doc ensures collaborators can easily follow the logic behind your findings and contribute effectively to the troubleshooting process.

In this section, address the following key questions:

* **Does the error exist only in your branch, or is it present in the main development branch as well?**  
  If the error appears in the main branch, it may indicate a recently introduced bug affecting multiple environments. If it’s specific to your branch, it’s likely due to new code introduced in your feature branch. When an error exists in the main branch, follow the steps in this [Oppia guide](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug) to trace the exact commit that introduced the issue.  
* **Where in the code does the error originate?**  
  Use the error logs to locate the precise file and function where the error is occurring. Narrowing down the error source minimizes the likelihood of investigating unrelated code paths.  
* **Which related parts of the code might be contributing to the error?**  
  Include relevant code snippets with clear annotations. This step clarifies the code context for yourself and provides collaborators with an easy entry point for investigation. Additionally, link directly to the GitHub file or section if possible, allowing for quick access to the code.

> [!IMPORTANT]
> **Practice 6**: Using the prompts above, draft your code-level investigation by documenting where the error surfaces in the code, whether it’s specific to your branch, and any related sections that may be contributing to the issue. Feel free to review and update the previous sections in your debugging doc as new insights come to light.

##### Example: Applying the Code-Level Investigation Steps

In our case, we’ve applied each of these investigative steps as follows:

**Does the error happen in the develop branch?**

No. The error is specific to our feature branch, arising during the implementation of feature gating for the new filtering functionality in `topics-and-skills-dashboard-page.service.ts`.

**Relevant Code Snippet**  
Below is the section of code where the error occurs. The code attempts to access `platformFeatureService.status` to check the status of the `SerialChapterLaunchCurriculumAdminView` feature flag. During testing, this access fails as `platformFeatureService` is undefined, leading to the observed error.

```typescript
if (filterObject.status !== EPublishedOptions.All) {
    if (this.platformFeatureService.status.SerialChapterLaunchCurriculumAdminView.isEnabled) {
        // Filtering logic...
    } else {
        // Alternate filtering logic...
    }
}
```

**Analysis and Observations**  
The error `Cannot read properties of undefined (reading 'status')` indicates that `platformFeatureService` is undefined in the test environment. This suggests a possible issue with the service initialization or setup within the test environment itself.

##### Key Takeaways

Conducting and documenting a code-level investigation is essential for targeted debugging. Here’s how these steps contribute to an efficient and collaborative debugging process:

* **Isolate the Error Source**: Pinpointing the exact file and function where the error occurs narrows the investigation to relevant code paths, helping you avoid distractions and focus on the most likely areas for bugs.  
* **Clarify Code Dependencies**: Analyzing related code and dependencies—such as services, flags, or recent changes—offers insights into possible misconfigurations or missing elements that could be causing the issue.  
* **Facilitate Collaboration**: Organizing your findings with annotated code snippets and GitHub links enables team members to jump in quickly, understand your progress, and contribute more effectively.

By documenting these findings, you lay a solid foundation for the next phase: hypothesis testing. This structured approach lets you build on your initial analysis, systematically uncovering the root cause of the issue and streamlining the debugging process. Now we know what is wrong, and it’s time to think through why and how things might have gone wrong. In the next section, we’ll cover this by exploring various possible scenarios that could be contributing to the error.

#### Step 4: Hypothesis Testing

The Hypothesis Testing stage is at the core of effective debugging. This step involves generating and systematically testing potential causes for the error, ultimately helping to isolate the root issue. By formulating clear, testable hypotheses and recording the results, you gain a deeper understanding of the problem. Additionally, your documented process allows others to follow your reasoning and contributes to a collaborative debugging effort.

> [!IMPORTANT]
> **Practice 7**: Examine the Hypothesis section in the debugging doc template to understand how hypotheses are structured. Think about potential causes for the issue based on the information gathered so far and try to create one or two clear, testable hypotheses that could explain the error.
> 
> **Hint**: Focus on isolating specific elements in the code or setup that may be contributing to the issue. Use your observations from the initial investigation as clues. For example, if the issue is only occurring in the test environment, a hypothesis could focus on differences in how services or dependencies are initialized in that environment.

##### 4.1 How to Formulate Hypotheses

Start by asking yourself: *What could be causing this problem?* With the context from the Initial Investigation, think through plausible explanations. Each hypothesis should aim to test a specific code area, dependency, or setup that could be contributing to the issue. Here are some techniques to guide you in formulating well-focused hypotheses:

* **Research Similar Errors**: Upon encountering an error, one of the first steps you should take is searching online for the exact error message. This can provide you with potential solutions, insights, or troubleshooting steps that can save time and guide you toward a resolution.  
* **Narrow the Problem’s “Surface”**: Focus on isolating potential causes by honing in on specific elements of the code, environment, or dependencies that might be malfunctioning. This approach clarifies your direction, making it easier to investigate systematically.  
* **Refer to Recent Changes**: If the feature worked previously but fails now, investigate recent modifications to the code or configurations. Often, bugs are introduced through recent changes, and comparing the “last known good state” with the current state can help identify these differences.  
* **Divide and Conquer**: Simplify the problem by gradually removing parts of the code or dependencies until the issue either disappears or becomes isolated to a specific segment. Continue refining the code until you’re left with the smallest possible section that still exhibits the problem. When dealing with newly-introduced features, consider removing bits of the recently added code to isolate the issue. For instance, you might replace complex modules with simpler stubs that simulate functionality without introducing potential bugs, allowing you to pinpoint the error more precisely.  
* **Compare Similar Implementations**: Examine how similar functionality or features are implemented elsewhere in the codebase, especially for recurring architectural patterns like feature flags or service dependencies. If the issue is specific to your implementation but not others, contrasting it with similar code can reveal subtle differences in initialization or setup that could explain the error.  
* **Analyze Patterns**: If the error isn’t consistent, try gathering data about each occurrence. Look for patterns in timing, specific setups, or environmental conditions that could shed light on the issue. However, keep in mind that not all issues exhibit clear patterns—if you don’t find any, don’t get discouraged. Instead, focus on systematically ruling out potential causes.  
* **Consider External Dependencies**: Dependencies such as third-party libraries, test configurations, or system setups can influence code behavior, particularly in testing environments. Check if an external dependency might be misconfigured, outdated, or behaving unexpectedly.

For additional guidance, consider checking out [Oppia’s Debugging Guide](https://github.com/oppia/oppia/wiki/Debugging), which covers methods and best practices for effective debugging within the Oppia codebase.

##### 4.2 Documenting Hypotheses

For each hypothesis, document it using this structured approach to ensure clarity and reproducibility:

1. **Suspected Cause**: Briefly describe the potential problem or misconfiguration you believe might be causing the issue. Explain the reasoning behind why this could be the root of the problem.  
2. **How I Tested This Hypothesis**: Outline the exact steps taken to test the hypothesis. Include any changes, observations, or checks you performed so that others can replicate the process. Make sure each step is specific to avoid ambiguity.  
3. **Status**: Conclude each hypothesis with a status label—**Confirmed**, **Rejected**, or **Untested** (if it’s a hypothesis you plan to explore). This makes it clear what has been verified and what remains to be investigated.

This structured approach to Hypothesis Testing not only enhances your own troubleshooting process but also creates a clear, reproducible path for others who may need to assist or review your work. By systematically documenting each hypothesis and its results, you establish a logical, evidence-based approach to problem-solving that can serve as a valuable reference for future debugging efforts.

**Hypothesis 1: The platformFeatureService Is Not Properly Initialized in the Test Environment**

**Suspected Cause**: The initial investigation led us to consider that the `platformFeatureService`, which controls the `SerialChapterLaunchCurriculumAdminView` feature flag, might not be set up correctly in the test environment, specifically within the `topics-and-skills-dashboard-page.service.spec.ts` test file. This service needs to be initialized properly for the feature flag to function as expected. If it isn’t, the `status` property would be undefined, which directly explains the observed error.

**Reasoning Behind This Hypothesis**: This hypothesis emerged from the error logs showing an issue with the `status` property being undefined, a property that is accessed only if `platformFeatureService` is present. Additionally, the feature worked as expected on the local server but encountered issues solely during testing, pointing to a potential test environment setup issue. Therefore, we suspected that `platformFeatureService` wasn’t being initialized correctly during testing.

> [!IMPORTANT]
> **Practice 8**: Check whether `platformFeatureService` is properly defined in both the development server environment and the test environment. If the error logs indicate that `platformFeatureService` is undefined in the test environment but works correctly in the development server or local setup, this discrepancy might point to a missing initialization process or mock setup in the test environment. Additionally, document the “How I Tested This Hypothesis” section based on the steps you followed.
>
> **Hint**: Check the console logs on your local server to see the state of `platformFeatureService`. If it is defined in the development server but undefined in the test environment, this discrepancy could indicate that the initialization process or mock setup in tests is missing essential configurations that are present in the dev server environment.

**How I Tested This Hypothesis**:

**Step 1: Check if `platformFeatureService` Is Defined During Testing**  
To confirm whether the service was accessible during test execution, I added console logs within the `getFilteredTopics` function of the `topics-and-skills-dashboard-page.service.spec.ts` file. The goal was to output the value of `platformFeatureService` when running tests, revealing whether it was initialized or remained undefined.

**Step 2: Run Tests Verbosely for Diagnostic Output**  
Next, I ran the frontend tests with verbose logging enabled, which provided detailed diagnostic output during test execution. This confirmed that `platformFeatureService` was indeed undefined in the test environment, consistent with the observed error message. This outcome suggested that the issue might be specific to the test setup, rather than to the feature flag code.

***Note**: To run frontend tests in verbose mode, use the command: `python -m scripts.run_frontend_tests --verbose`. For more on frontend test debugging, refer to [this wiki page](https://github.com/oppia/oppia/wiki/Debug-frontend-tests).*

**Step 3: Compare Local Server Output**  
I then checked the feature’s functionality in a local server environment to confirm it operated as expected outside of the test setup. Here, the feature flag appeared correctly in the browser console, confirming that the issue wasn’t in the core code or functionality but rather was specific to the test setup.

***Note**: If you need to enable feature flags on your local server, refer to the [feature flag setup wiki](https://github.com/oppia/oppia/wiki/Launching-new-features#changing-value-of-feature-flags).*

**Status**: Confirmed

***Note:** A confirmed hypothesis doesn’t always lead directly to the root cause. In this case, while we’ve narrowed the problem down to the test environment, further investigation is required to identify the exact cause and solution. This is a natural part of the debugging process.*

> [!IMPORTANT]
> **Practice 9**: Reflect on what this hypothesis reveals about the issue. Since the feature works on the local server but fails in the test environment, the problem is likely within the test configuration rather than the code itself. Based on this result, try to formulate another hypothesis for testing/debugging. 
> **Hint**: Consider aspects such as the consistency of the mock setup or test initialization steps that may differ from those in the local server environment.

Since the feature behaves correctly on the local server but fails in the test environment, this suggests that the code itself is not the issue. The error is likely due to a misconfiguration or missing initialization step specific to the frontend test setup. This confirms our hypothesis and directs us to inspect the test file configuration for potential setup issues.

**Hypothesis 2: There may be a missing dependency or import affecting the test environment for `platformFeatureService`.**

**Suspected Cause**:The `platformFeatureService` might require specific dependencies or imports to function correctly within the test environment. If any essential dependency or import is missing in the `topics-and-skills-dashboard-page.service.spec.ts` file, this could prevent the feature flag’s `status` property from being initialized correctly, resulting in the observed undefined error.

**Reasoning Behind This Hypothesis**: Given that `platformFeatureService` controls the feature flag, it’s crucial to ensure that all related dependencies are properly imported in the test file. Missing or incorrect imports could prevent the service from being correctly instantiated, especially when testing with feature flags. Furthermore, since the feature functions as expected in the local server, this points to an issue specifically related to the test setup. Examining the imports is a logical next step to ensure no essential components were left out in the test environment configuration.

> [!IMPORTANT]
> **Practice 10**: Check if the test setup is missing any dependencies or modules required for the feature flags to function correctly.
> 
> **Hint**: Compare the imports and configurations with those in similar test files that successfully use feature flags. This can help identify any missing or misconfigured elements essential for the setup.

**How I Tested This Hypothesis**:

**Step 1: Review All Imports in the Test File**  
I started by carefully reviewing the imports in `topics-and-skills-dashboard-page.service.spec.ts`, confirming that all dependencies related to `platformFeatureService` were indeed included. This included examining imports for common test dependencies, mocks, and the platform feature itself.

**Step 2: Cross-Check with Similar Test Files**  
I compared the imports in `topics-and-skills-dashboard-page.service.spec.ts` with those in similar test files, such as `story-update.service.spec.ts`, which also uses `platformFeatureService`. By cross-referencing the imports, I verified that all necessary dependencies were accounted for and that the structure was consistent with other files where the feature flag works correctly.

**Status**: Rejected

> [!IMPORTANT]
> **Practice 11**: Reflect on the findings from this hypothesis and document what you observed. 
> **Hint**: Note whether all necessary dependencies were present and if adjusting imports had any effect on the test outcome. Consider how this finding shifts focus toward potential setup or configuration issues rather than missing imports.

All dependencies were correctly imported in `topics-and-skills-dashboard-page.service.spec.ts`. Adding additional imports or adjusting existing ones did not impact the test outcome. This finding suggests that the issue isn’t due to missing or incorrect imports. Instead, it further points to the possibility of a configuration issue specific to the test setup or the way `platformFeatureService` is being initialized and mocked in this particular test file.

**Hypothesis 3: The Test Setup or Feature Flag Mocking Configuration for `platformFeatureService` May Be Incorrect**

**Suspected Cause**:  
The issue might stem from the way `platformFeatureService` is configured in the test environment of `topics-and-skills-dashboard-page.service.spec.ts`. An improper setup or a misconfiguration in how the feature flag is mocked could lead to the `status` property appearing as undefined in tests, even though it behaves as expected in the local server environment.

> [!IMPORTANT]
> **Practice 12**: Think through how you would logically test the hypothesis that the feature flag mocking configuration may be incorrect. Consider comparing the mock setup in your failing test file with other files where the feature flag service is successfully mocked. How might differences in these setups help you identify misconfigurations?
>
> **Hint**: Start by examining similar test files where platformFeatureService is mocked correctly. Look for any discrepancies in how the mock is set up and think about whether these differences could impact test outcomes.

**Reasoning Behind This Hypothesis**:  
Considering that the feature works correctly on the local server, we can infer that the root cause is likely related to the testing environment setup. From Hypothesis 1, we know that the feature flag isn’t being initialized correctly in the test environment. Since platformFeatureService needs to be mocked accurately to simulate feature flag behavior, any differences in the setup of this mock service between our test file and other files could be critical. To ensure consistency, compare the setup in `topics-and-skills-dashboard-page.service.spec.ts` with successfully configured files like `story-update.service.spec.ts`, which might provide insights into the correct mocking process.

**How I Tested This Hypothesis**:

> [!IMPORTANT]
> **Practice 13**: What approach would you take to compare the two test files effectively? Consider creating minimal versions of each test file, keeping only the essential setup and a single test case calling the affected code to highlight differences. 
> 
> **Hint**: Strip down each test file to one basic test case, ideally the one that calls the problematic code. This allows you to focus on differences in the setup without the distractions of other test cases. By isolating only the setup, you’ll be better able to spot inconsistencies that could be causing the issue.

**Step 1: Review the Mock Service Setup in the Failing Test File**  
I began by thoroughly examining `topics-and-skills-dashboard-page.service.spec.ts` to check how `platformFeatureService` was being mocked. This setup declared `MockPlatformFeatureService` with a `status` object that included `SerialChapterLaunchCurriculumAdminView`, set to `isEnabled: false`. I compared this setup with similar files that successfully mocked `platformFeatureService` to spot any discrepancies.

**Step 2: Cross-Check with Another Successful Test Configuration**  
I identified `story-update.service.spec.ts` as a similar test file where feature flagging for `platformFeatureService` was correctly configured. Upon inspection, I noticed that `story-update.service.spec.ts` had a streamlined `beforeEach` setup without manually reinitializing the service. This difference suggested that certain setup inconsistencies in our test file could be influencing the outcome.

**Step 3: Minimalist Test Setup**  
To pinpoint the impact of these setup differences, I created minimalist versions of both `topics-and-skills-dashboard-page.service.spec.ts` and `story-update.service.spec.ts` by keeping only one simplified test case. This stripped-down approach allowed me to isolate the `beforeEach` configuration from other test cases, focusing solely on how the setup affected feature flag functionality.

**Step 4: Align `beforeEach` Configurations and Re-Test**  
Following the `story-update.service.spec.ts` structure, I modified the `beforeEach` block in `topics-and-skills-dashboard-page.service.spec.ts` as follows:

* Removed the line `tsds = new TopicsAndSkillsDashboardPageService()` and allowed `TestBed.configureTestingModule` to handle the entire setup.  
* Simplified the injection of `platformFeatureService` to match the successful setup.

**Testing Outcome**:

The issue in `topics-and-skills-dashboard-page.service.spec.ts` has been resolved. By aligning the `beforeEach` setup with the successful configuration from similar files, the error was eliminated. This confirmed that the original setup in `topics-and-skills-dashboard-page.service.spec.ts` was incomplete, leading to the improper initialization of the `platformFeatureService` mock.

**Status**: Confirmed

##### 4.3 Tips for Hypothesis Testing

When working through hypothesis testing, following best practices can dramatically improve both your efficiency and accuracy in isolating the cause of an issue. Here are some key tips:

**1\. Focus on Small, Testable Changes:** Avoid changing multiple aspects at once. If you test multiple adjustments simultaneously, it becomes challenging to pinpoint which one influences the outcome. Break down the problem into smaller components, isolating one element at a time. For instance, if you’re troubleshooting a service configuration, only adjust its setup while keeping other settings constant to see if it impacts the result.

**2\. Document Observations Clearly:** Detailed documentation can be as valuable as the tests themselves. Note any unexpected behaviors, error messages, or recurring patterns. Each observation, even from a rejected hypothesis, adds to the cumulative understanding of the problem and may reveal subtle clues that guide future tests.

**3\. Use Console Logs and Breakpoints:** Console logs and breakpoints are powerful tools to watch your code in action, especially in complex environments. Logs allow you to track variables and conditions in real-time, while [breakpoints](https://github.com/oppia/oppia/wiki/Debug-backend-tests#use-the-python-debugger) help step through code execution line by line. This can reveal unexpected variable states or interactions, highlighting where the code diverges from expected behavior.

**4\. Seek Similar Code for Clues:** In large codebases, examining similar code implementations often yields valuable insights. A similar component, service, or test file that interacts with a comparable dependency may contain setup patterns or solutions that can resolve the current issue. For example, if another feature flag setup works as expected, examining its configuration can help pinpoint missing steps or misconfigurations in your current setup.

##### Key Takeaways

The **Hypothesis Testing** phase is central to diagnosing an issue effectively. By exploring possible causes and testing them systematically, you gradually isolate the root cause. Here’s how the practices in this section contribute to efficient and collaborative debugging:

* **Structured Testing**: Testing one hypothesis at a time and documenting the steps ensures a clear, logical approach, making it easier to isolate the issue.  
* **Collaboration-Ready Documentation**: Clear, thorough documentation allows others to understand and contribute to the debugging process, creating a shared knowledge base that can save time and resources in future troubleshooting efforts.  
* **Iterative Problem Solving**: Even if a hypothesis is rejected, it helps refine the problem’s scope and narrows down the next testing steps.

With these findings in hand, we’ll proceed to develop a solution that ensures consistent initialization of `platformFeatureService` within the test environment. This approach will help prevent similar issues in the future and reinforce reliable configurations across tests.

#### Step 5: Documenting the Solution

Now that we have a working solution, it’s essential to document it thoroughly. This ensures future developers can understand the issue and how to resolve similar problems. When describing the solution, include:

1. **A Clear Explanation of the Fix**: Outline what changes were made and why they work.  
2. **Analysis of the Root Cause**: Explain how the identified root cause led to the observed errors. This is critical for grasping the underlying concepts and avoiding similar mistakes.  
3. **Acknowledgment of Partial Resolutions**: If the exact root cause isn’t clear but the bug was resolved, document your debugging process up to the hypothesis stage and share it with others to collaboratively refine the solution.

> [!IMPORTANT]
> **Practice 14**: Now that you have a working solution from the hypothesis section, can you document the Solution section? Follow the tips mentioned above, which outline what should be included in the Solution section. Feel free to use the internet or any other resources to gain a better understanding of why the error was resolved.

##### Our Case: Understanding the Fix

**Root Cause Analysis:**  
The earlier setup in `topics-and-skills-dashboard-page.service.spec.ts` manually instantiated the `TopicsAndSkillsDashboardPageService` using `new` and passed it to the `TestBed`. This approach bypassed Angular's dependency injection system, which is designed to properly initialize services, mocks, and interdependencies.

The implications of this were:

1. **Improper Mock Initialization**: The manual instantiation failed to configure the `platformFeatureService` mock correctly. Specifically, the `status` property, which relies on proper initialization of the mock, remained undefined during tests. This was the direct cause of the bug in our case.  
2. **Injecting Real Services (General Implication):** While not the direct cause of this issue, manually creating a service using `new` and injecting it into the `TestBed` can lead to challenges. Real services often have complex dependencies that are difficult to create and control in isolation, making tests harder to manage and debug.  
3. **Fragmented Setup (General Implication):** Combining manual initialization (`tsds = new TopicsAndSkillsDashboardPageService()`) with `TestBed` in the `beforeEach` block created an inconsistent and fragmented setup. This inconsistency made the code harder to read, understand, and maintain, especially for new contributors.

**The Solution:**  
To address this, we aligned the `beforeEach` setup in `topics-and-skills-dashboard-page.service.spec.ts` with the pattern used in `story-update.service.spec.ts`. The changes included:

* Mocking Dependencies for Better Testing: Instead of directly injecting real services, we used Angular’s `TestBed.configureTestingModule` to manage service creation. Mock dependencies were provided to simulate real behavior, allowing for better control and isolation during testing. By replacing complex service setups with simplified dummy values or spies on service methods, we also ensured easier debugging and streamlined test cases.  
* Removing Manual Instantiation: The line `tsds = new TopicsAndSkillsDashboardPageService()` was removed. Allowing `TestBed.configureTestingModule` to manage the setup ensured that all dependencies were initialized properly.

## Conclusion

Debugging complex issues, especially within a large codebase, requires a structured approach that balances investigation with documentation. Through this tutorial, we’ve walked through the stages of a debugging doc, from initial investigation to hypothesis testing, using a real-world example of the `platformFeatureService` configuration issue.

Here are some key takeaways from this process:

* **Understanding the Issue’s Context:** Beginning with a thorough background check—like reading the PRD and analyzing the code changes—is essential. This provides context and narrows down potential causes before diving into tests.  
* **Systematic Hypothesis Testing:** Formulating and testing hypotheses in an isolated manner allows you to methodically identify the source of an error. By documenting each step, including rejected hypotheses, you build a knowledge base that can accelerate troubleshooting both now and in the future.  
* **Clear and Consistent Test Setup:** This example underscored the importance of a consistent testing setup. Ensuring that mocks, feature flags, and dependencies are properly initialized across tests is crucial for accurate results. Borrowing setup configurations from similar working tests can be an effective way to spot missing or misconfigured elements.  
* **Documenting and Sharing Findings:** Debugging documentation is not only a tool for individual problem-solving but also a collaborative asset. By documenting insights and observations, you make it easier for others to understand, reproduce, and build on your findings.

Going forward, applying these debugging strategies will not only improve your efficiency but also strengthen the codebase’s stability. Remember, each well-documented debugging session contributes to a richer, more resilient knowledge base for the entire team. Happy debugging, and don’t hesitate to share your insights—they’re invaluable to the community\!

#### Appendix

The full debugging doc for this issue can be found [here](https://docs.google.com/document/d/1_1lEoe0hBFn-gNmI1qZqF2X_Z0wqWy40Hj23Rlkp4cY/edit?tab=t.0#heading=h.ieezq05wy6da). Reviewing this document will give you insights into how the issue was debugged in the original setting. You can also read through the comments to see how conversations unfolded between team members to resolve the issue collaboratively.

#### We Value Your Feedback

Did you find this tutorial useful? Or, did you encounter any issues or find things hard to grasp? Let us know by opening a discussion on [GitHub Discussions](https://github.com/oppia/oppia/discussions/new?category=tutorial-feedback). We would be happy to help you and make improvements as needed\!