## Table of Contents

* [Introduction](#introduction)
* [Scenario](#scenario)
* [Prerequisites](#prerequisites)
* [Procedure](#procedure)
  + [WHAT](#what)
    - [Key User Tasks and Stories](#key-user-tasks-and-stories)
    - [Testing Plan](#testing-plan)
    - [Technical Requirements](#technical-requirements)
      * [API (Application Programming Interfaces) Endpoints](#api-application-programming-interfaces-endpoints)
      * [Database Changes](#database-changes)
      * [New or Changes to Frontend Components](#new-or-changes-to-frontend-components)
  + [HOW](#how)
    - [Key High-Level and Architectural Decisions](#key-high-level-and-architectural-decisions)
    - [Evaluation Criteria](#evaluation-criteria)
    - [Implementation Approach](#implementation-approach)
      * [Storage Model Layer Changes](#storage-model-layer-changes)
      * [User Flows (Controllers and Services)](#user-flows-controllers-and-services)
  + [Implementation Plan](#implementation-plan)
* [Conclusion](#conclusion)
  + [We Value Your Feedback](#we-value-your-feedback)

## Introduction

In this tutorial, we will walk through the process of writing a Technical Design Document (TDD) at Oppia. The primary goal of the TDD is to plan out a new or updated feature on paper first, helping you identify potential problems before investing significant effort. It also serves as a way to get feedback and approval from stakeholders, ensuring concerns (like privacy issues) are addressed early on.

The tutorial will guide you through the key sections of the TDD, highlighting what information is needed and why. You'll learn how to document architectural decisions, propose API changes, and understand the potential impact on the overall system. Ultimately, the TDD is a tool for making decisions and getting approval, ensuring that the approach is well-researched and aligned with the project’s goals before any code is written.

## Scenario

The product team at Oppia has laid the groundwork for a new feature aimed at enhancing the learner's experience. This feature will let learners add private notes to various parts of a lesson.

The Lesson Annotation Feature has a significant impact on user experience, so to manage its development effectively and reduce potential risks, it's important to create a Technical Design Document (TDD). This document will act as a roadmap, steering the feature from its initial concept through its final implementation.

For a better grasp of what this feature entails, please review the ["Key User Stories and Tasks \- Lesson Annotation Feature"](https://docs.google.com/document/d/1AOJVSzGAqiHtgM5A2UWRgyOJxlEyZ7_nQ2r050ZgcZU/edit?tab=t.0#heading=h.x6677awl9ob4) document. The goal of drafting a detailed TDD is to specify the technical needs and formulate a comprehensive plan for integrating this new feature into the existing Oppia codebase. This approach ensures that the development team is synchronized and that every aspect of the feature is thoroughly planned before beginning the coding process.

## Prerequisites

Before you begin, ensure you have:

* Set up your development environment. If you haven't done so, follow the [Oppia setup instructions](https://github.com/oppia/oppia/wiki/Setup-Oppia) to install all necessary tools and dependencies.  
* A solid understanding of both frontend and backend development, particularly with Angular and Python, as these are the core technologies used in Oppia.  
* Familiarize yourself with the Oppia codebase and its file structure. If you're new to the platform, review the [Oppia Codebase Overview](https://github.com/oppia/oppia/wiki/Codebase-overview) to understand how the components are organized and interact.  
* Resolved at least a couple of issues related to both the backend and frontend in the Oppia project. This experience will give you practical insight into our coding practices and typical challenges you might encounter.  
* Familiarize yourself with Oppia's Exploration Page and its key components, such as topics, stories, skills, subtopics, explorations, cards, content, and interactions \- [Key Concepts in Oppia](https://oppia.github.io/#/KeyConceptsInOppia).  
* Spent some time with the Exploration Editor Page and its sub-tabs to understand the functionalities currently available and how they might interact with or be impacted by the new annotation features.  
* Completed the tutorial on how to make frontend changes: [Implement UI Improvements Tutorial](https://github.com/oppia/oppia/wiki/Tutorial-Learn-how-to-Implement-UI-Improvements).  
* Completed the tutorial on how to make backend changes: [Backend Changes Tutorial](https://github.com/oppia/oppia/wiki/Tutorial-Learn-how-to-debug-a-backend-bug)   
* Completed the tutorial on how to plan and implement a small full-stack feature: [Full-Stack Feature Tutorial](https://github.com/oppia/oppia/wiki/Tutorial-Learn-to-implement-a-new-full-stack-feature).

## Procedure

First, let's delve into what a Technical Design Document (TDD) is and its role at Oppia, especially for substantial projects. TDDs ensure that we comprehensively consider all potential aspects of a project before we begin implementation. This thorough planning and review process helps streamline implementation, reducing confusion and minimizing the likelihood of project delays or blockages.

To start working with Oppia's Technical Design Document (TDD), first access the current [TDD template](https://docs.google.com/document/d/1mnz8f708DZIa6BpUyRmbb0gCT6EKO3wIvWa_3rOEOYs/edit?tab=t.0#heading=h.rpq25vez37fp). You'll need to make a personal copy of this template to begin outlining your design for a new feature. You should start with understanding the template's structure, particularly the guidance highlighted in yellow boxes. These instructions are crucial as they detail what information each section should contain and how it should be presented.

It’s important to recognize that while this tutorial discusses the current format of the TDD, the template may undergo future revisions. However, the fundamental purpose of the TDD will remain consistent: to ensure that any proposed solution is thoroughly considered, well-researched, and has broad consensus on its architectural and API design decisions.

> [!IMPORTANT]
> **Practice 1**: Review Oppia's TDD template. Based on your review of Oppia’s TDD template, describe the purpose of each of the three primary sections: WHAT, HOW, and IMPLEMENTATION PLAN.
> - WHAT: What does this section focus on, and what kind of details should you include here?
> - HOW: What does this section explain about the implementation process, and why is it important?
> - IMPLEMENTATION PLAN: What is the role of this section in the TDD, and how does it guide the coding and deployment process?
> - **Tip**: Pay special attention to the yellow-highlighted instructions in each section, which describe how to complete each part of the TDD. Understanding these details will help you effectively fill out each section of a TDD for your projects at Oppia.

The TDD is structured into three primary sections: WHAT, HOW, and IMPLEMENTATION PLAN:

* **WHAT**: Outlines the feature's requirements and user stories, detailing what needs to be accomplished.  
* **HOW**: Describes the details of how the feature requirements from the WHAT section will be implemented  
* **IMPLEMENTATION PLAN**: Details the steps for coding, testing, and deploying the feature.

Each section is designed to walk you through a clear and logical development path, ensuring that both technical specifications and user-centric considerations are well addressed.

*Note: The goal of this tutorial is not specifically to teach you how to add the Annotation feature but rather to instill an understanding of the thought process behind designing such features. We will explore key areas of the TDD, focusing on the content documented at each stage and the context behind it.*

*Writing an effectiveTDD for any feature at Oppia hinges on a deep understanding of the product and thorough research. While it's okay not to know all the answers immediately, showing a dedication to in-depth research is important. This demonstrates that you are not merely posing questions but are actively seeking out solutions and understanding, which is important  for the development of robust and effective features.*

### WHAT

The "WHAT" section of the Technical Design Document (TDD) outlines the high-level plan for the project. This includes detailing user stories, defining any new APIs needed for implementation, specifying database model changes, and describing new UI components. This foundational section is important because it requires a thorough understanding of the project's objectives and its potential impact on users. Before delving into the technical specifics of implementation, it's essential to document this part thoroughly to ensure the implementation details in the HOW section provide the correct functionality.

#### Key User Tasks and Stories

This subsection is derived directly from the Product Requirements Document (PRD) and highlights user journeys, illustrating how users will interact with the new feature. At Oppia, our development is driven by user needs, whether they be learners, exploration creators, or Oppia developers. Understanding and empathizing with user experiences is important, and this section helps developers grasp the practical applications of their work.

For larger, user-facing projects, you will generally receive a detailed PRD from the product team containing all necessary project details. However, for this tutorial, we've created a mock-up table titled "[Key User Stories and Tasks \- Lesson Annotation Feature](https://docs.google.com/document/d/1AOJVSzGAqiHtgM5A2UWRgyOJxlEyZ7_nQ2r050ZgcZU/edit?tab=t.0#heading=h.x6677awl9ob4)." This table is designed to help you comprehend the full spectrum of the user journey. Please review this table thoroughly to ensure you fully understand the intended user interactions and the feature's functionality.

>[!IMPORTANT]
> **Practice 2**: Examine the document "[Key User Stories and Tasks - Lesson Annotation Feature](https://docs.google.com/document/d/1AOJVSzGAqiHtgM5A2UWRgyOJxlEyZ7_nQ2r050ZgcZU/edit?tab=t.0#heading=h.x6677awl9ob4)" to grasp the new user flow associated with this feature. 
>
> **Hint**: To deepen your understanding, start your local server and visit the relevant pages on the Oppia platform. As you navigate, visualize the user flow described in the document, considering how users will interact with the new features. This practical exploration will help you better comprehend how the changes will affect the user experience.

#### Testing Plan

For user-facing projects, it's important to outline a comprehensive testing plan that covers all [key user stories](https://docs.google.com/document/d/1mnz8f708DZIa6BpUyRmbb0gCT6EKO3wIvWa_3rOEOYs/edit#bookmark=id.dylm3arizux1) identified in the PRD to prevent regressions. Here's how you can structure your testing plan effectively:

**Automated vs. Manual Testing**

* **Automated Acceptance Tests**: These tests should be reserved for "Must Have" user flows, where any disruption could significantly affect user functionality. Automated tests are limited by our capacity to maintain them, so it's crucial to prioritize critical user flows.  
* **Manual CUJ Tests**: Manual testing is required for important core user journeys (CUJs) that cannot be easily automated. While rare for user-facing projects, this is common in developer workflow projects — for example, ensuring that a linter correctly fails when code violates a lint rule. Some important CUJs must therefore be tested manually.

Ensure that your tests are specific and completely unambiguous. CUJs should include not only the exact steps a user would follow, but also the specific setup required before running the test. For example, if the test involves a translation reviewer named `reviewer1`, make sure that `reviewer1` is created in the setup section and consistently referenced throughout the test. See [this spreadsheet](https://docs.google.com/spreadsheets/d/1O8EHiSAGrG0yoNUBz9E4DIwKNS8Rfsv_ffC4k1WK5jc/edit?pli=1#gid=0) for examples: note how each row includes concrete details such as the email used to sign up, the exact page to navigate to, and the specific tag to add. Avoid using generic placeholders—everything should align with the setup defined earlier in the test.

> [!IMPORTANT]
> **Practice 3**: Create detailed test steps for the user flows outlined in the "[Key User Stories and Tasks \- Lesson Annotation Feature](https://docs.google.com/document/d/1AOJVSzGAqiHtgM5A2UWRgyOJxlEyZ7_nQ2r050ZgcZU/edit?tab=t.0#heading=h.x6677awl9ob4)" document.  
> 
> **Hint**: Use the "[Web QA Test Matrix (arranged by user type)](https://docs.google.com/spreadsheets/d/1O8EHiSAGrG0yoNUBz9E4DIwKNS8Rfsv_ffC4k1WK5jc/edit?pli=1#gid=0)" spreadsheet as a reference to understand how to structure each test step clearly and concisely, ensuring that each step leads to a defined expected result.

**Example User Flow Test**

Let's detail a user journey from the "Key User Tasks" section, focusing on adding notes during a lesson:

**User Journey**: As a learner, I want to add notes alongside the lesson to instantly record my thoughts while learning.

**Setup**:

* **Create Users and Content**:  
  * Sign up as a user for content creation: `exploration-creator@example.com`.  
  * Navigate to the creator dashboard: `http://localhost:8181/creator-dashboard`.  
  * Create an exploration with at least one state, and publish it. Record the exploration ID for later.  
  * Sign up two additional users who will act as learners: `exploration-learner1@example.com` and `exploration-learner2@example.com`.

**Testing Steps**:

1. **Initial Setup**:

   * Ensure the exploration is ready and accessible.  
   * Log in as `exploration-learner1@example.com`.  
2. **Add a Note**:

   * Navigate to the exploration page: `/explore/<exploration_id>.`(replace \<exploration\_id\> with the ID recorded during setup)  
   * Click the "Add Notes" button within the right column of the exploration player.  
   * Enter text into the notes section and submit the note by clicking the submit button.

**Test Expectations**:

* The note should be visible within the scrollable notes section of the modal alongside the exploration.  
* The content of the note should reflect what was entered.  
* The note should persist after reloading the page.  
* The note should still be visible after logging out and logging back in as the same user.

Check out this page to understand more about acceptance tests:[https://github.com/oppia/oppia/wiki/Acceptance-Tests](https://github.com/oppia/oppia/wiki/Acceptance-Tests)

#### Technical Requirements

The "Technical Requirements" subsection within the "WHAT" section addresses the engineering aspects necessary to implement the solution. This part of the TDD is dynamic and may undergo several revisions as you progress through the document and gain a clearer understanding of the project's scope and technical specifics.

At this stage, it’s important to outline our initial thoughts on the engineering requirements, even though these may evolve. Here we discuss three main areas:

1. **API (Application Programming Interfaces) Endpoints**: Identify any new APIs required or existing APIs that need modifications. This is crucial as APIs are the conduits through which our frontend components communicate with the backend services, and ensuring they are well-defined from the start helps in creating a seamless integration.  
2. **Database Changes**: Specify any modifications or additions to the database schema. This includes new schemas, changes to existing schemas, or even updates to data retrieval methods. Understanding these changes is essential for ensuring data integrity and efficiency of data operations.  
3. **New or Changes to Frontend Components**: Detail any new user interface components or updates to existing ones. This involves describing the visual and functional changes that will enhance user interactions or facilitate new feature functionalities.

*By clearly outlining the technical requirements from the outset, we establish a definitive roadmap for the project. It's crucial to regularly revisit this section throughout the Technical Design Document (TDD) process. This iterative review allows us to refine our strategies based on the feedback we receive and any deeper insights we gain as we delve further into the project's requirements. Additionally, if multiple approaches are viable for any of the outlined sections, document these alternatives and why the chosen approach is better in the "Key High-Level and Architectural Decisions" section. You can temporarily bypass detailing those specific subsections until a finalized approach is chosen.*

##### API (Application Programming Interfaces) Endpoints 

APIs act like conduits that facilitate data transfer between the frontend and backend layers of an application. For those new to APIs, they can be thought of as the means by which our frontend sends data to and requests data from the backend. For a more formal definition, you might want to check out [this Wikipedia page](https://en.wikipedia.org/wiki/API).

As developers, we start backend development by working from the user experience inward. This means evaluating the needs of the frontend first and then shaping our backend accordingly. By understanding the user-facing flow, we can design APIs that serve those needs directly. This user-centric approach naturally leads us to prioritize API design before database or other backend components, ensuring a development process that is both efficient and aligned with the actual product experience.

**Key Questions for API Analysis**

> [!IMPORTANT]
> **Practice 4**: Investigate and draft a high-level plan for API support needed for the Notes feature. Based on your understanding of the frontend requirements, answer the following: 
> - What specific data does the frontend need that it doesn't currently receive?
> - Is that data already available in existing API responses or will it need to be added? 
> - Can an existing API be updated, or will a new endpoint be cleaner or more appropriate? 
> - Are there any current data fetches that can be pruned as part of this change?

To properly design or adjust APIs, consider these critical questions:

1. **What new data does the frontend need?** Identify the specific data required to support the new feature. This helps define the API's responsibilities clearly.  
2. **Which existing APIs provide related data?** Reviewing current endpoints can reveal opportunities for reuse or extension.  
3. **Can existing APIs be extended to include new data?** If the change is minimal and aligns well with an existing endpoint's purpose, extending it may be the most efficient approach.  
4. **If extension isn't practical, what new APIs are needed?** When extending an API would violate separation of concerns or lead to unclear logic, a new endpoint is justified  
5. **Is there any redundant or unused data currently being returned?**While not directly part of API *design*, reviewing existing responses for unnecessary payloads can lead to more efficient APIs and reduce frontend parsing overhead.

###### *Research*

To begin, focus on how data is currently managed and fetched for **explorations** in Oppia. Since the notes feature will be tied to the exploration player, understanding the existing exploration-related endpoints is key. This involves:

**Identifying Existing Endpoints**: Observe API calls in your development environment while navigating through different states of an exploration. This will show you which endpoints are currently used and what data they handle.

**Evaluating API Responses**: Analyze the data structures returned by these endpoints. This will guide the design of the new endpoints for the notes feature.

Navigate to [Oppia's exploration player](https://www.oppia.org/explore/K645IfRNzpKy) and open the developer tools to the network tab. Here, examine the APIs triggered during the exploration interaction.

Upon analysing the endpoints you will note the following things,

- **Endpoint Patterns and Data Handling**: Exploration-related API endpoints typically follow a pattern like `/explorehandler/<verb>/<exploration_id>`. For example, `/explorehandler/init/<exploration_id>` fetches all relevant data for an exploration in a single response, including information for every state.  
  Once this data is loaded, the frontend displays one state at a time without making further API calls. The `"states"` field in the response contains a nested dictionary where each state is keyed by its name.

	Now that we have gathered all the necessary information, let's move forward.

Focusing on our specific requirements, we need to establish several API endpoints to manage notes effectively:

- **Add a New Note**: Users should be able to add notes tied to specific states within an exploration. To create a note, the client must provide the `exploration_id`, the `state_name`, and the note `content`. The backend will then generate a unique `note_id` and associate the note with the specified state and exploration.  
- **Edit/Delete a Note**: Each note will have a unique `note_id` generated by the backend during note creation. This `note_id` will be used for updating a note via a `PUT` request or removing it via a `DELETE` request.  
- **Get Notes**: To retrieve notes, we’ll need an endpoint that returns all notes associated with an exploration, grouped by state. The ideal response format is a nested dictionary: each state name maps to another dictionary of notes, where each note is keyed by its `note_id`. These notes will be sorted by their `created_at` timestamp, making it easy for the frontend to display them in  chronological order within each state.

With this high-level plan established, let's proceed to refine these ideas and document the specific details in the following subsection.

###### *Documenting*

> [!IMPORTANT]
> **Practice 5**: Summarize your research findings and document your conclusions under the "Additions/Changes to the Web Server Interface" section of the [Technical Design Document (TDD)](https://docs.google.com/document/d/1mnz8f708DZIa6BpUyRmbb0gCT6EKO3wIvWa_3rOEOYs/edit?tab=t.0#bookmark=id.jvebxvpfn5tn). 
> 
> Use a table format, as recommended in the template, to clearly present the proposed API changes, including the endpoint paths, request methods, expected payloads, and response formats.  
> 
> Note: Although the TDD template recommends a table format, for this project we will describe API changes in bullet points instead. This is because Markdown tables do not handle multi-line entries (like detailed request/response formats) very well.

**Adding a New Note**

* **Endpoint**: `POST /explorehandler/notes/<exploration_id>`  
* **Payload**:  
  * **State Name**: Specifies the state within the exploration against which the note is being taken.  
  * **Content**: The content (i.e. text) of the note.

**Editing a Note**

* **Endpoint**: `PUT /explorehandler/notes/<exploration_id>`  
* **Payload**:  
  * **Note ID**: The unique identifier of the note to be updated.  
  * **Content**: The new content for the note, which cannot be empty. ~~It is the client's responsibility~~Although the frontend is expected to validate that the note content is non-empty before sending the request, the backend will also enforce this check to ensure data integrity

**Deleting a Note**

* **Endpoint**: `DELETE /explorehandler/notes/<exploration_id>`  
* **Payload**:  
  * **Note ID**: The unique identifier of the note to be deleted.

**Fetching the Notes**

* **Endpoint**: `GET /explorehandler/notes/<exploration_id>`  
* **Response**: A structured format where each state name within the exploration serves as a key. Each key points to another dictionary detailing the notes associated with that state, organized by their creation timestamps:

```json
{
  "State Name": {
    "Note_id_1": {
      "Created_at": "datetime",
      "Content": "text"
    },
    "Note_id_2": {
      "Created_at": "datetime",
      "Content": "text"
    }
  },
// Other states continue in similar structure
}
```


##### Database Changes

In this section, we delve into database models, which are essentially representations of database schemas. For a more detailed understanding of models and how they fit into the broader architecture of Oppia's codebase, you might want to consult the [Architecture documentation](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase).

Before proceeding with modifications or additions to the database models, consider the following essential questions:

1. **Do we need to store any new data in the models?** Identify if the feature addition, such as notes, necessitates storing new types of data.  
2. **Do we need to deprecate any previously stored data?** Determine if there's data that's no longer relevant or needed due to the new feature implementation.  
3. **Can the new data be incorporated into an existing table, or is a new table required?** Evaluate whether the new data fits logically within existing structures or if creating a new table would be more appropriate.  
4. **Is there a need for data migration jobs to ensure integrity among existing data?** Sometimes, introducing new data or changing data structures requires running scripts or jobs to update and validate existing data to maintain database integrity.

To effectively address these questions, review the current database schema. Understand how different tables are linked and what specific data they store. This understanding will help in making informed decisions about where and how to integrate new data for features.

###### *Research*

> [!IMPORTANT]
> **Practice 6**: Analyze potential ways to store exploration notes in the datastore. 
> - Can existing models (like `ExplorationModel`) be extended to store notes, or would this create coupling issues or bloated payloads?
> - Would it be more appropriate to create a separate model to keep notes modular and manageable? 
> - How is similar user-generated content stored elsewhere in Oppia (e.g., feedback threads or suggestions)?
> - Are there privacy considerations for notes, especially if they're tied to user accounts or sensitive inputs? 
> - What are the expected read/write patterns — will notes be frequently updated, loaded in bulk, or retrieved per state?

For our new feature, it is essential to determine how notes, linked to specific states within an exploration, should be stored in the datastore. This decision hinges on whether existing data models can accommodate the notes or if a new model needs to be created.

Upon reviewing the database structure, we identified the `ExplorationModel` within `oppia/core/storage/exploration/gae_models.py`, which represents an exploration. This model includes several properties relevant to our needs:

```python
# The version of the states blob schema.
states_schema_version = datastore_services.IntegerProperty(
     required=True, default=0, indexed=True)
# The name of the initial state of this exploration.
init_state_name = (
     datastore_services.StringProperty(required=True, indexed=True))
# A dict representing the states of this exploration. This dict should
# not be empty.
 states = datastore_services.JsonProperty(default={}, indexed=False)
```

- `states_schema_version`: An integer indicating the version of the states blob schema.  
- `init_state_name`: A string property that names the initial state of the exploration.  
- `states`: A JSON property that holds a dictionary representing the exploration's states. This dictionary is key to our decision, as it contains the states but is not suited for extending with note properties due to its structure.

At first glance, it might seem possible to add a `notes` key to each state inside the `states` dictionary. However, this approach has a few problems:

1. **The exploration model is meant to represent a public object**, while notes are private to each user. Storing user-specific data inside a public model mixes responsibilities and makes the data model harder to manage.  
2. **Multiple users can view the same exploration**, and each can have their own notes. If we store all user notes in the same exploration model, the data will quickly grow in size. This could slow things down and make the model hard to update or query.  
3. **The state property is already a JSON field**, and adding dynamic user data to it would make it even harder to maintain or validate.

Because of these reasons, it’s better not to extend the existing `states` dictionary with a `notes` key. However, each state has a unique name within an exploration, which provides a pathway for linking notes to specific states. 

Now that we have an idea on how to link the notes to an exploration and to a notes. We can proceed with designing the Model Schema. For storing notes, we may have more than one approach. So we can bypass filling in the model changes for now and we will first discuss the various approaches and once we are given green from the reviewers, we can fill this section again.

##### New or Changes to Frontend Components

In this section, we'll discuss the UI changes necessary for implementing the new notes feature. We will determine whether to introduce new components or modify existing ones to accommodate this functionality.

> [!IMPORTANT]
> **Practice 7**: Review the Figma design for the Annotation Feature here: [Annotation Feature \- Tutorial Mocks](https://www.figma.com/design/o3nHA8WzztTh2Me3Vh8aYy/Annotation-Feature---Tutorial-Mocks?node-id=0-1&p=f). 
> - List the frontend changes required to implement the new design. 
> - Examine the current UI in the codebase and compare it with the new UI design in the Figma mockup. What are the key differences? 
> 
> Use this analysis to understand the scope of frontend development needed for this feature. 
> 
> Note: In most cases, Figma designs will be provided by the design team to guide implementation.

According to the provided Figma designs, which can be viewed [here](https://www.figma.com/design/o3nHA8WzztTh2Me3Vh8aYy/Annotation-Feature---Tutorial-Mocks?node-id=0-1&p=f), we will introduce a new component adjacent to the existing exploration player component. This new component will be a scrollable modal that displays all notes associated with a given state. It will also include an 'Add' button and a text box to enable users to input new notes directly within this modal.

Additionally, we will develop another component specifically designed to represent an individual note. This modular approach allows us to encapsulate the structure, styling, and logic for each note in a single, reusable unit. It ensures consistent formatting across all notes, simplifies future enhancements (such as adding timestamps, edit/delete options, or metadata), and improves readability by keeping the modal component focused solely on layout and container-level behavior. This separation of concerns makes the codebase cleaner, easier to test, and more maintainable.

Changes will also be made to the parent component that currently renders the exploration player to integrate these new components seamlessly. 

Since notes are user-generated and their content will vary based on the user’s input language, internationalization (I18n) is not required for the note content itself. However, any static UI text within the modal—such as the "Add a Note" button label and any placeholder or instructional text—will be internationalized to ensure consistency with the rest of the application and to support users across different locales.

In summary, two new components will be created for the notes feature (one for the modal and one for individual notes), and modifications will be made to the existing parent component to support their integration.

### HOW

In this section, we will delve into the technical specifics required to implement the solution effectively. Understanding the problem we are addressing and the architecture of Oppia's codebase is crucial for making informed architectural decisions. We will list and analyze key architectural decisions, evaluating different alternatives and selecting the optimal approach based on thorough analysis.

#### Key High-Level and Architectural Decisions

For each architectural decision, we will:

* **List Alternatives**: Present the possible solutions we should consider.  
* **Comparative Analysis Table**: Create a table comparing the alternatives across various factors, using a color-coded system (green for favorable, yellow for caution, and red for unfavorable) for clarity.  
* **Chosen Approach**: Outline the approach we plan to adopt, supported by detailed analysis. This analysis will be fleshed out further once the comparative table is reviewed.

#### **Evaluation Criteria**

The criteria for comparing different approaches may include:

* **Performance Considerations:** Evaluate how each approach performs under expected workloads, both in terms of responsiveness and scalability:  
  * **Datastore Query Complexity**: Assess how many datastore operations (e.g., GET, PUT, GET\_BY\_ID) are needed for each user action. Focus on the cost and effort of implementing these access patterns, not on theoretical computational complexity. (e.g., creating a note should ideally require just one PUT call, not multiple GET+PUT operations.)  
  * **Time Complexity**: Analyze the algorithmic complexity of operations, especially those that could degrade performance (e.g., O(N²), O(N³) operations). (e.g., avoid checking every note against every other note when only one lookup is needed.)  
  * **API Performance**: Estimate the impact on the response times of API handlers.  
  * **Scalability**: Consider how well the approach handles increasing data volumes and concurrent usage. (e.g., will it still work if an exploration has 10,000 notes?)  
* **Datastore Model Sizes**: Assess potential risks of unbounded growth in model sizes, considering the 1MB limit per model instance in the datastore.  
* **Migration Needs**: Determine if the solution requires migrating existing datastore entities or assets. While Oppia supports background migration jobs that avoid disrupting the user experience, such migrations can introduce extra complexity and workload for developers.  
* **Refactoring Requirements**: Consider the extent of refactoring needed and the potential for regressions.  
* **Consistency with Codebase Patterns**: Evaluate how well the solution aligns with existing codebase practices.  
* **Maintainability and Readability**: Evaluate the ease of maintaining and reading the code.  
* **Third-party Libraries**: Identify whether the approach requires introducing any new third-party libraries. If yes, please read about how we manage third-party libraries at Oppia in [this wiki](https://github.com/oppia/oppia/wiki/Third-party-libraries).  
* **Impact on Other Teams**: Consider how the solution affects other Oppia teams.  
* **Platform Compatibility**: Ensure that the proposed solution works reliably across all platforms Oppia supports.

With this in mind let’s move forward. For our scenario, we have to make the following decisions.

- **Model Schema for Storing Notes**: Should we create a new model, or are there viable alternatives that utilize existing structures?  
- **Handling Stale Notes**: How do we address scenarios where notes become irrelevant because the corresponding states in a lesson have been modified?

We will systematically approach each of these questions to ensure the chosen solutions are optimal, keeping in mind both the technical feasibility and the overall user experience. Once a final decision is reached and approved by reviewers, it may be necessary to update the "What" section accordingly to reflect these decisions.

##### Decision 1: Storing Notes for an Exploration

When considering how to store notes effectively for an exploration, it's important to understand the operations that notes will undergo, which include creation, deletion, updating, and fetching. Each note needs to contain specific properties to ensure it functions correctly within the system:

* **User ID**: Identifies the user who created the note.  
* **Exploration ID**: Specifies the exploration to which the note is linked.  
* **State Name**: Indicates the specific state within the exploration that the note references.  
* **Content**: Holds the textual content of the note.

> [!IMPORTANT]
> **Practice 8**: Brainstorm potential approaches for storing notes within Oppia's data architecture. 
> Think about both extending existing models (like `ExplorationModel`) and creating entirely new models. For each approach you come up with, briefly outline: 
> - What data would be stored and where. 
> - How notes would be linked to specific explorations and states. 
> - Any immediate pros or cons you can think of (without needing to finalize anything yet). 
> 
> At this stage, the goal is not to choose the best option — just to surface all reasonable ones before evaluating them in depth.

Let’s talk about the ways we can do this,

1. Implement a new model specifically for notes. Each note would be an instance of this model, identified by a unique `note_id`. Notes for a specific state could be retrieved using a combination of `user_id`, `exploration_id`, and `state_name`.  
2. Create a Model per Exploration per User. Each user-exploration pair gets its model, which includes an `exploration_id`, `user_id`, and a JSON property to store notes structured by state.  
```JSON
{
  State_name_1: {
    Note_id_1: {
      Content: 
    },
    // Other notes for this state
  },
  // Other states
}

```

*Note: If you could think of more approaches, feel free to add them to the list and do the comparison on your own. The purpose of this tutorial is not to come up with the perfect implementation plan for this mock scenario but to teach folks the aspects a developer should think about while making technical decisions.*

> [!IMPORTANT]
> **Practice 9**: Compare the storage options you've identified in Practice 8. Evaluate these options based on criteria relevant to database design and application requirements. Consider referencing the “Evaluation Criteria” section to guide your analysis. You might examine factors such as the complexity of queries required to fetch notes for an exploration, the scalability of each solution, and their impact on performance and data privacy. 
> 
> As you analyze each option, think about practical aspects like ease of implementation, consistency with existing data models, and long-term maintainability.

***Note:** The "GET", "PUT", and "DELETE" operations mentioned below refer to backend interactions with the storage layer (datastore), **not** frontend-to-backend API calls. This table focuses on how the backend will manage data internally.*

| Criteria | Option 1: One Model per Note | Option 2: One Model per Exploration per User |
| :---- | :---- | :---- |
| Description | Each note is stored in its own model object. | A single model object stores all notes for an exploration for a user using a JSON field. |
| Size per model | Smaller, as it contains only one note. | Larger, as it includes all notes for an exploration. |
| Number of Individual Models | Higher, due to one model per note. | Fewer, with one model per user per exploration. |
| Query to create a new note | One PUT call with `exploration_id`, `user_id`, and `state_name` | Requires a GET\_BY\_ID to check for an existing model, then a PUT to create a new model if it does not exist. Notes are added to a JSONB field, requiring handling of nested dictionaries. |
| Query to update an existing note | Direct PUT call using `note_id`. | GET to retrieve the model, then update the note within the JSON field. Involves 1 GET \+ 1 PUT. |
| Query to delete an existing note | Straightforward DELETE call using `note_id` | GET to fetch the model, then remove the note from the JSON field, then a PUT call to save the updated model. |
| Query to fetch notes | GET\_MULTI call due to multiple models per exploration. | Single GET\_BY\_ID call as there is one model per exploration per user. |
| Implementation Efforts | Relatively easier to implement and manage | More complex, especially in managing creation, deletion, and update logic within nested dictionaries. |
| Scalability | More scalable with increasing note entries; each note is a separate model, so growth is distributed. | Potential challenges as all notes for a user-exploration pair are stored in one model. While explorations are also stored as single models, user-generated notes can grow less predictably—especially in high-usage cases. This could lead to bloated models and performance issues in edge cases (e.g., 1000+ notes). |

**Analysis and Recommendation**

* **Option 1: One Model per Note**  
  * Pros: Better scalability, simpler CRUD (Create, Read, Update, and Delete) operations, and smaller data size per model make this option more manageable and efficient.  
  * Cons: More models overall, which may slightly increase datastore operations when loading all notes for a user in one go.  
* **Option 2: One Model per Exploration per User**  
  * Pros: Reduces the number of models by aggregating notes into a single model per user per exploration.  
  * Cons: Managing nested dictionaries within a JSONB field can complicate CRUD operations and scalability, especially as the amount of data grows.

Given these considerations, **Option 1** is preferable due to its simplicity in CRUD operations, scalability, and the ability to manage data growth effectively without compromising performance.

> [!IMPORTANT]
> **Practice 10**: Consider why each note model is assigned a unique ID, despite being retrievable by a combination of exploration_id, user_id, and state_name.

**Key Design Rationale:**

* **User Privacy**: Including the `User_id` ensures that notes are private and visible only to the user who created them. This is important for maintaining user privacy and personalization of the notes feature.  
* **Uniqueness and Retrieval**: The combination of `Exp_id`, `State_name`, and `User_id` allows for efficient querying of notes. The unique `Id` for each note lets users have multiple notes per state. 

##### Decision 2: Handling Stale Notes

When thinking about how to mark notes as stale in Oppia, one idea that comes up is tracking changes at the state level—that is, marking a note as stale only if the specific state it refers to has changed. This would offer fine-grained precision, ensuring users are only alerted when relevant content has been updated. However, given that states are currently stored as nested fields within the exploration model (rather than as separate entities), implementing state-level change tracking would require significant additional complexity—such as maintaining separate timestamps or diffing logic for each state.

Instead of tracking each state individually, we could simplify by marking all notes as stale whenever the entire exploration is updated. This broader approach reduces complexity but will overestimate the staleness of notes.

**UI Indications**: How we indicate staleness to the user can vary:

* Display a text warning next to each note.  
* Use color coding to highlight stale notes.  
* Introduce an icon in the notes section, which, upon hovering, indicates that updates to the exploration have been made since the notes were last edited.

In practice, decisions that affect user interaction and UI should be discussed with the product team or tech lead. For the sake of this tutorial, let's proceed with the scenario where the tech lead approves marking notes as stale based on updates to the entire exploration rather than individual states. We will use an icon in the notes section to signal that the exploration has received updates since the notes were initially created. This subtle yet clear indicator maintains user interface cleanliness while providing essential information.

To support staleness detection, each note will include an `updated_at` timestamp that records the last time it was modified. While retrieving notes (`explorationNotes`), we’ll compare this timestamp against the `updated_at` timestamp of the corresponding exploration. Since notes may also be edited, using `updated_at` provides a more reliable basis for detecting whether a note might be outdated than relying on `created_at`

In the backend’s response to the frontend's request for fetching exploration notes, include an `is_stale` flag. This flag will help the frontend determine and display whether the content of a note might be outdated. This method ensures that users are alerted to review and potentially update or remove notes that may no longer be accurate due to changes in the exploration.

#### Implementation Approach

This section is designed to guide developers through a structured approach to implementing new features within Oppia. It focuses on explaining the rationale behind each step, ensuring that developers understand not only what to do but also why these steps are important. This approach helps in maintaining consistency, predictability, and high quality in the development process.

For our case, let’s mention how to implement changes layer by layer, i.e from Model all the way to Controllers.

##### Storage Model Layer Changes

> [!IMPORTANT]
> **Practice 11**: Now that a model schema has been selected, detail the implementation plan for this model. Consider the guidance in the TDD's yellow box to determine what specific information to include. Address the following points in your response: 
> - What is the name of the model?
> - What is the unique identifier for the model?
> - Are any columns being indexed for more efficient queries?
> - What functions will be implemented in the storage layer to manage this model?

After deciding on the architectural approach for storing annotations, we now detail how the chosen model will be constructed, and how it will be accessed and modified by backend services.

**Model Name**: `ExplorationAnnotations` 

**File Location**: `core/storage/users/gae_models.py`

**Fields**:

* **id (str)**: Unique ID for the note, which will be randomly generated~~. UUID.~~  
* **exploration\_id (str)**: The exploration linked to the note.  
* **state\_name (str)**: The state within the exploration related to the note.  
* **user\_id (str)**: ID of the user who created the note.  
* **content (text)**: Text content of the note.  
* **created\_at**: Timestamp when the note was created.  
* **updated\_at**: Timestamp when the note was last updated.

**Key Functions**:

* **create**: Initializes a new note.  
  * **Args**: user\_id, exploration\_id, state\_name, content  
* **get\_by\_id**: Retrieves a note by its ID.  
  * **Args**: id  
* **get\_by\_exploration\_id\_user\_id**: Fetches notes for a specific exploration and user.  
  * **Args**: exploration\_id, user\_id

*Note \- Updates to the notes are managed in the service layer of Oppia, rather than directly within the storage layer, in line with our coding conventions. Specifically, when a note needs updating, we utilize the `get_by_id` function to retrieve the note's model, after which we update the `content` and `updated_at` properties accordingly in the service layer. This approach helps centralize business logic in the service layer.*


> [!IMPORTANT]
> **Practice 12**: Consider the takeout and wipeout policies for the new model you're introducing. Reference Oppia's [Wipeout Implementation](https://github.com/oppia/oppia/wiki/Wipeout-Implementation) and [Privacy-aware Programming](https://github.com/oppia/oppia/wiki/Privacy-aware-programming) guidelines. Address the following questions in your response: 
> - How does the new model handle user data?
> - What steps are necessary to ensure compliance with wipeout policies? 
> - How will the takeout functionality be incorporated into this model?

**Data Management \- Takeout and Wipeout Functionalities:** Oppia places a strong emphasis on responsible data management. Since our feature involves storing user-related data (`ExplorationNotes`), it's essential to integrate support for **wipeout** and **takeout** functionalities.

* **Wipeout**: In compliance with privacy regulations, if a user decides to delete their account, all associated data must also be permanently deleted. This ensures the security and privacy of user information. Further details on Oppia's wipeout policies and procedures can be found in our [Wipeout Implementation Guide](https://github.com/oppia/oppia/wiki/Wipeout-Implementation).

* **Takeout**: Users have the right to access and export their data. The takeout feature enables users to download their information, ensuring they can retrieve all data associated with their profiles whenever needed.

Oppia's infrastructure includes robust systems for managing these data privacy operations, primarily utilizing Beam jobs to automate the processes effectively. For new models like `ExplorationAnnotations`, necessary methods must be implemented within the storage layer to support these features. This setup ensures that our implementations are consistent with established patterns and maintain high standards for data management and privacy.

For developers looking to understand how these functionalities are integrated into new models, reviewing the changes made in [this pull request](https://github.com/oppia/oppia/pull/18873/files) can provide valuable insights. The pull request demonstrates how takeout and wipeout were adapted for a newly introduced model related to user data, offering a practical example of applying these policies in our codebase.

By following these guidelines and implementing the necessary functionalities, we ensure that our platform remains secure, user-friendly, and compliant with all relevant data protection laws. 

##### User Flows (Controllers and Services)

In this section, we will delve into the controllers and services essential for implementing the annotation feature within Oppia. This involves defining the API endpoints that will handle , editing, deleting, and retrieving notes.

**Adding a New Note**

* **Endpoint**: `POST /explorehandler/notes/<exploration_id>`  
* **Payload**:  
  * **State Name**: Specifies the state within the exploration against which the note is being taken.  
  * **Content**: The textual content of the note.

**Editing a Note**

* **Endpoint**: `POST /explorehandler/notes/`  
* **Payload**:  
  * **Note ID**: The unique identifier of the note to be updated.  
  * **Content**: The new content for the note, which cannot be empty. This field **must not be empty**, and while the client should perform basic validation before sending the request, the **backend is responsible for enforcing this validation** to ensure data integrity and prevent accidental or malicious updates.

**Deleting a Note**

* **Endpoint**: `DELETE /explorehandler/notes/`  
* **Payload**:  
  * **Note ID**: The unique identifier of the note to be deleted.

**Fetching the Notes**

* **Endpoint**: `GET /explorehandler/notes/<exploration_id>`  
* **Response**: A structured format where each state name within the exploration serves as a key. Each key points to another dictionary detailing the notes associated with that state, organized by their creation timestamps:

**Controller Layer Implementation \- oppia/core/controllers/reader.py**

As part of implementing the annotation feature for Oppia's exploration learner view, we will integrate a new handler within the `oppia/core/controllers/reader.py` file. This location is chosen because it already manages handlers associated with routes beginning with `/explorehandler/`, and the purpose of the file aligns well with the functionality of managing exploration notes.

**File Location**: `oppia/core/controllers/reader.py`

**Handler Description**: The `ExplorationNotesHandler` will facilitate operations related to the notes feature, encompassing the creation, retrieval, and deletion of notes within the learner's exploration view.

**Methods**:

1. **GET Method**  
   * **Purpose**: Retrieves all notes associated with a specific state within an exploration.  
   * **Response Format**

```JSON
{
  "state_name_1": {
    "note_id_1": {
      "created_at": "2025-04-13T10:23:00Z",
      "updated_at": "2025-04-13T10:24:00Z",
      "content": "Note text here",
      "is_stale": false
    },
    "note_id_2": {
      "created_at": "2025-04-13T10:30:00Z",
      "updated_at": "2025-04-13T10:35:00Z",
      "content": "Another note",
      "is_stale": true
    }
  },
  "state_name_2": {
    ...
  }
}
```

2. **POST Method**:  
   * **Purpose**: Handles both the creation of new notes and the editing of existing notes. This method determines the intended action based on the presence of a note ID in the request.  
   * **Input Validation**: Checks for the necessary fields depending on whether a note is being created or edited.   
     * For creation:  
       * `exploration_id` (required)  
       * `state_name` (required)  
       * `content` (required and must not be empty)  
     * For editing:  
       * `note_id` (required)  
       * `content` (required and must not be empty)  
     * The backend ensures all required fields are present and valid, and that the user has permission to perform the operation.  
   * Error Handling:  
     * `400 Bad Request`: Missing required fields or empty content.  
     * `404 Not Found`: Provided `exploration_id` does not exist.  
     * `403 Forbidden`: User is not allowed to modify the note.  
   * Response Format:

```JSON
{
  "note": {
    "id": "note_id_123",
    "exploration_id": "exp1",
    "state_name": "Intro",
    "content": "Updated note",
    "user_id": "user_abc",
    "created_at": "2025-04-13T10:23:00Z",
    "updated_at": "2025-04-13T10:35:00Z",
    "is_stale": false
  }
}

```

3. **DELETE Method**:  
   * **Purpose**: Facilitates the deletion of a note identified by its unique ID.  
   * **Validation**:   
     * Ensures the `note_id` corresponds to an existing note.  
     * Confirms that the `exploration_id` is valid.  
     * Checks that the logged-in user is the owner of the specified note.  
   * Error Handling:  
     * **400 Bad Request:** Invalid request. Note ID or Exploration ID is missing or malformed.  
     * **404 Not Found:** Note not found or associated exploration does not exist.  
     * **403 Forbidden:** You do not have permission to delete this note.  
   * Response Format:

```JSON
{
  "success": true,
  "message": "Note deleted successfully."
}
```

**Basic Validation for Each Method**

Each method within the `ExplorationNotesHandler` performs basic validation to ensure the integrity of the requests:

* **Existence Checks**: Ensures the referenced exploration and states exist before performing any operation.  
* **Data Completeness**: For creation/editing, all required fields (`state_name`, `content`, etc.) are validated both on the frontend and again in the backend for security.

**Service Layer Implementation \- oppia/core/domain/exp\_services.py**

* **Fetching Notes**:  
  * **Function**: `get_exploration_notes_by_user_id`  
  * **Arguments**: `exploration_id`, `user_id`  
  * **Logic**: This function calls the storage layer to retrieve all notes for the specified user and exploration.  
* **Creating & Editing Notes**:  
  * **Function**: `upsert_exploration_note`  
  * **Arguments**: `user_id`, `exploration_id`, `state_name`, `note_id`, `content` (Note: fields are optional depending on the context)  
  * **Logic**:  
    * If `user_id`, `exploration_id`, `state_name` are provided, it indicates a creation operation.  
    * If `note_id` is provided, it indicates an update operation.  
  * This unified function handles both create and update operations, streamlining the logic and reducing code duplication.  
* **Deleting Notes**:  
  * **Function**: `delete_exploration_note_by_id`  
  * **Arguments**: `note_id`  
  * **Logic**: This function deletes a note based on the provided `note_id`.

**Note:** Once approval is secured for the previously discussed sections, we transition to the "Implementation Plan." This section outlines the project's execution timeline and the breakdown of tasks across different Pull Requests (PRs). It’s important to establish an organized approach to ensure smooth development and deployment.

### Implementation Plan

**Strategies for Implementation:**

1. **Single PR Approach:** For smaller projects or tightly coupled changes, you might opt to consolidate all changes into a single PR. This approach is straightforward but requires careful handling to manage the complexity and ensure nothing is overlooked during reviews. For example, a single PR that both introduces a new lint check and fixes all existing code issues flagged by that check is a tightly coupled change that makes sense to be submitted together.   
   However, for larger projects, this approach has significant downsides—reviews become harder to manage, and the likelihood of frequent merge conflicts increases as more contributors work on overlapping areas of the codebase.  
2. **Breaking Projects Across Multiple PRs:** For medium to large projects, it's often beneficial to split the implementation across multiple pull requests. This approach helps streamline reviews, isolate bugs, and minimize merge conflicts.  
   One common strategy is dividing by architectural layers if it’s a full stack project:  
   * Storage Layer PR: Introduce changes to the database schema or storage models. This is typically the foundation upon which other layers build.  
   * Service Layer PR: Add the core business logic that uses the storage layer to implement functionality.  
   * Controller Layer PR: Expose the service layer functionality via API endpoints.  
   * Frontend PR: Consume the APIs and reflect changes in the user interface.

Alternatively, splitting backend and frontend changes into separate PRs is another practical approach, especially when the UI is being developed after the backend is finalized. This separation makes it easier to test and review each part in isolation.

**Feature Gating:**

* **Introduction of Feature Gates:** Before rolling out new functionalities, it's wise to implement feature gating. This strategy allows you to control the release of features and ensure they are thoroughly tested on staging servers before becoming available on production. Since our annotation feature is user-facing and requires thorough testing, we will introduce a new feature flag to hide our feature from users until it’s ready. This ensures that we can test the functionality in controlled environments and selectively enable it as needed. For more details on feature gating and how it's handled in Oppia, refer to the [Oppia Feature Gating Wiki page](https://github.com/oppia/oppia/wiki/Feature-Gating).

**Planning for Complex Projects:**

* If your project involves multiple features, prioritize and schedule them based on their importance and the resources required. This prioritization will help in planning a milestone table and effectively managing the project timeline.

## Conclusion

In this tutorial, you learned how to design and implement a backend feature for lesson annotations in Oppia. You explored how to approach the creation of a feature by writing a detailed Technical Design Document (TDD) to clarify requirements and technical decisions, ensuring a structured development process. You identified key user stories, broke down the user flow, and determined the necessary API changes for storing, editing, and deleting notes.

Additionally, you examined various model design approaches, analyzed how to handle stale notes, and created a testing plan for the feature. You also covered essential considerations like takeout and wipeout policies, and how to ensure the proper handling of user data in compliance with privacy regulations.

By completing this tutorial, you’ve gained practical experience in:

* Writing a thorough TDD that addresses technical requirements, implementation plans, and user stories.  
* Identifying necessary backend changes and how to organize tasks for development.  
* Understanding how to design and implement data storage and retrieval solutions.  
* Analyzing and making decisions on data models, stale data handling, and feature gating.  
* Preparing and conducting comprehensive testing, both automated and manual, to ensure the feature meets requirements.  
* Implementing data privacy policies in accordance with Oppia’s guidelines.

These skills will help you efficiently plan, implement, and test backend changes for new features at Oppia, ensuring that development processes are clear, systematic, and aligned with product goals.

### We Value Your Feedback

Did you find this tutorial useful? Or, did you encounter any issues or find things hard to grasp? Let us know by opening a discussion on [GitHub Discussions](https://github.com/oppia/oppia/discussions/new?category=tutorial-feedback). We would be happy to help you and make improvements as needed\!