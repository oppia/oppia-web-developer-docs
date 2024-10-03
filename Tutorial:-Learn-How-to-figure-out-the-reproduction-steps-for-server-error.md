## Introduction

This tutorial will guide you through debugging a server error that is challenging to reproduce locally. Specifically, we will investigate and fix a TypeError related to certificate generation for contributors.


## Skills Covered

- Codebase Navigation
- Identifying and Analyzing Error Logs
- Debugging Techniques
- Reproducing Server Errors Locally


## Scenario

One of the server admins has reported the following error logs. Your task is to investigate the issue and determine how and why it is occurring.

> **Note:** The primary goal of this tutorial is not to find a solution, but to guide you through the process of investigating and understanding the workflow of debugging server errors. In this tutorial, you will follow the steps a developer might take to investigate this server error.

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

## Prerequisites

Before you begin, make sure you have:

- Set up your development environment. (If you haven't, follow the [Oppia setup instructions](https://github.com/oppia/oppia/wiki/Installing-Oppia).)
- Familiarize yourself with [Debugging at Oppia wiki page.](https://github.com/oppia/oppia/wiki/Debugging).
- Before starting this tutorial, it is important to have a basic understanding of the following key concepts:
  - **Exploration**: Familiarize yourself with explorations by reviewing the [Oppia User Documentation on Explorations](https://oppia.github.io/#/KeyConceptsInOppia).
  - **Topic**: Learn about topics by visiting the [relevant wiki page](https://github.com/oppia/oppia/wiki/How-to-access-Oppia-webpages#overview-of-entities).
  - These concepts are fundamental to understanding how content is structured in Oppia, and they will help you follow the steps in this tutorial more easily.

## Procedure

> The following steps illustrate how a developer might tackle this issue. Try following this tutorial step-by-step on your local machine! This will give you a better sense of how to tackle other similar issues in the codebase. If you get stuck with a step in this tutorial, raise an issue in (GitHub Discussions)[https://github.com/oppia/oppia/discussions/categories/tutorial-feedback] to get help.

> **Important:** When you see a “practice question box”, stop and try to figure out the answer on your own before reading ahead. You will learn more if you try to figure out your own answer to the question first!



## Stage 1: Understand the Architecture of Beam Jobs at Oppia

Beam jobs at Oppia are typically structured in a modular fashion, where the main components include:

- **Pipeline Definition**: This is where you define the structure of your Beam pipeline.
- **Transforms**: These are the processing steps that operate on the data.
- **IO**: Input and output operations to read from and write to data sources.
- **Testing**: Unit tests to ensure the job is correct.

Refer to the [Beam Jobs at Oppia documentation](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs#writing-apache-beam-jobs) for a detailed overview.

## Stage 2: Understand the Models

> [!IMPORTANT]
> **Practice 1: Locate the definition of `TopicModel` and `TopicSummaryModel`.**  
> You can utilize the quick search functionality of your code editor to facilitate this process.  
> **Hint**: Take a look at this wiki page on [Tips for common IDEs](https://github.com/oppia/oppia/wiki/Tips-for-common-IDEs#visual-studio-code).

Before diving into the implementation, it's crucial to understand the models we will be working with.

<details>
<summary><b>Topic Model (oppia/core/storage/topic/gae_models.py)</b></summary>

```python
class TopicModel(base_models.VersionedModel):
    """Model for storing Topics.
    This class should only be imported by the topic services file and the topic model test file.
    """
```
</details>

The TopicModel is used for storing detailed information about topics. This model inherits from Versioned Model and thus is versioned, meaning it maintains a history of changes made to each instance. If you are curious about how versions are maintained and want to take a proper look, take a look at the VersionedModel definition in file oppia/core/storage/base_model/gae_models.py.

<details>
<summary><b>Topic Summary Model (oppia/core/storage/topic/gae_models.py)</b></summary>

```python
class TopicSummaryModel(base_models.BaseModel):
    """Summary model for an Oppia Topic.
    This should be used whenever the content blob of the topic is not needed (e.g. search results, etc).
    The key of each instance is the topic id.
    """

```
</details>

The TopicSummaryModel provides a summarized view of a topic, which is useful for scenarios where the full details of a topic’s contents are not required, such as search results. Each TopicSummaryModel instance is identified by the topic id.

## Stage 3: Draft the Directed Acyclic Graph (DAG)

Before we write any code, let's visualize the workflow of our Beam job as a Directed Acyclic Graph (DAG). This will help us understand the sequence of operations and the flow of data through the pipeline.

#### What is a DAG?
Like all graphs, a directed acyclic graph (DAG) consists of nodes connected by edges. In this case, the nodes are steps in the job, and the edges indicate the order in which to complete the steps. The edges are thus directional (hence "directed"), and the graph isn't allowed to have any cycles (hence "acyclic"). In other words, it should be impossible to start at one node and follow the edges back to the same node, as this would create an infinite loop in our job.

For more detailed information about DAGs, you can refer to the [DAG Wikipedia](https://en.wikipedia.org/wiki/Directed_acyclic_graph) page.

Visualizing our Beam job as a DAG helps in planning the structure and flow of our data processing pipeline. It provides a clear picture of how data moves from one step to another, ensuring that all necessary operations are performed in the correct order.

### Step 3.1:  Define the Job's Objective

> [!IMPORTANT]
> Practice 2: Take a notebook and try drafting a rough workflow of what our job would do, using boxes for the steps and arrows to connect different steps.
> Hint:
> - Read Everything First: Start by reading all the necessary data at the beginning of the job. This ensures that you have all the required information before performing any operations.
> - Process Data in Steps: Break down the job's functionality into simpler steps, such as filtering, transforming, and aggregating the data. Each step should be a separate node in your DAG.
> - Write Everything Last: Ensure that all writing operations, such as saving results or updating models, are performed at the end of the job. This helps in maintaining data consistency and avoids incomplete writes.

The job's objective is to validate that each topic model in the datastore has a corresponding topic summary model. The workflow can be broken down into the following steps:

- **Read Topic Models**: Read all the topic models from the datastore.
- **Validate Topic Models**:  For each topic model, check if there is a corresponding topic summary model.
- **Output Results**: Write the validation results to an output sink (e.g., a text file).

### Step 3.2: Draw the Directed Acyclic Graph (DAG)

Here's a simple representation of the DAG for our Beam job:

![DAG for Beam Job](images/TutorialDebuggingServerError/DAG.jpg)

In this DAG:

- **ReadTopicModels**: Reads topic models from the datastore and extracts their IDs.
- **ReadTopicSummaries**: Reads topic summary models from the datastore and extracts their IDs.
- **ValidateTopicModels**: Processes each topic model ID to check for a corresponding topic summary model ID, identifying any missing topic summary models.
- **WriteResults**: Writes the validation results to an output sink, including:
   - The count of total topic models.
   - The count of missing topic summary models.
   - Necessary details about each missing topic summary model.

#### Data Flow:

- The **ReadTopicModels** step outputs the IDs of the topic models.
- The **ReadTopicSummaryModels** step outputs the IDs of the topic summary models.
- The **ValidateTopicModels** step identifies missing topic summary models.
- The **WriteResults** step generates reports based on the validation.

#### Batch I/O vs Incremental I/O

An alternative workflow you might think of could involve iterating over each model and, while iterating over a specific model, validating it and adding the results to a log.
Before diving into different approaches, it's important to understand whether incremental reads and writes are feasible within Apache Beam.

#### Beam's Batch Processing Model:

Apache Beam generally operates on a batch processing model, where data is read all at once, processed, and then written out. The idea of interleaving reads and writes within each loop iteration—reading, validating, and then writing one model at a time—isn't supported in this model. While Beam does offer windowing for processing data in chunks, this approach adds complexity and isn't currently used in Oppia's workflows.

Since incremental I/O isn’t feasible in Beam’s batch model, the batch approach is both necessary and more effective. Here’s why:

- **Efficiency**: Batch I/O allows for optimized, parallel processing, making it faster than processing one item at a time, which would otherwise slow down due to constant I/O operations.
- **Data Consistency**: Writing all results at the end ensures consistency, avoiding issues like incomplete logs or partial data that could occur with incremental writes, even if they were possible.
- **Simplicity**: Separating reading, processing, and writing into distinct stages makes the workflow clearer and easier to debug. Mixing these steps would only complicate the process, making troubleshooting more difficult.

## Stage 4: Writing the Beam Job

With the DAG in mind, we can now proceed to implement the Beam job. Let’s create a new file for our job in the `oppia/core/jobs/batch_jobs` directory. 

> [!IMPORTANT]
> **Practice 3: Decide on suitable names for the module and job.**  
> Hint: Follow the conventions mentioned in the [Apache Beam Jobs Wiki](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs#testing-apache-beam-jobs).

Per the Oppia documentation for Beam Jobs:

- The name of the file follows the format `<noun>_<operation>_jobs.py`. In this case, we can use something like `topic_validation_jobs.py`.
- The name of the job follows the convention: `<Verb><Noun>Job`. In this case, we can name the job as `ValidateTopicModelsJob`.

Let’s first understand the part where we need to fetch the `TopicModels`:

<details>
<summary><b>Code for Fetching Topic Models</b></summary>

```python
topic_models_pcoll = (
    self.pipeline
    | 'Get all TopicModels' >> (
        ndb_io.GetModels(topic_models.TopicModel.get_all()))
    | 'Extract topic model ids' >> beam.Map(
        lambda model: model.id)
)
```
</details>

In the above code, self.pipeline is the starting point of our Beam pipeline. ndb_io.GetModels(topic_models.TopicModel.get_all()) fetches all TopicModel entities from the datastore. beam.Map(lambda model: model.id) extracts the id from each TopicModel entity. We only need the IDs to check for corresponding TopicSummaryModel entities.

> [!IMPORTANT]
> Practice 4: Based on the previous step where we fetched all the topic models, can you try writing the code for fetching topic summary models?
> Hint: Refer to the code snippet for fetching TopicModel entities and apply a similar approach.

<details> <summary><b>Code for Fetching Topic Summary Models</b></summary>

```python
topic_summary_models_pcoll = (
    self.pipeline
    | 'Get all TopicSummaryModels' >> (
        ndb_io.GetModels(topic_models.TopicSummaryModel.get_all()))
    | 'Extract topic summary model ids' >> beam.Map(
        lambda model: model.id)
)
```
</details>

Similar to the previous step, this code fetches all TopicSummaryModel entities and extracts their IDs. This step ensures we have a list of all summary models to compare against our topic models.

> [!IMPORTANT]
> Practice 5: Now that we have the IDs of both TopicModels and TopicSummaryModels, we need to compare them. If a TopicModel ID > is not present in the TopicSummaryModel IDs, we need to store it so that we can report it later in the next stage.
> Hint: Use the beam.Filter transform to filter out the IDs that are not present in the list of TopicSummaryModel IDs.
> Note that the beam.Filter transform works with a lambda function that returns True for items you want to keep and False for those you want to exclude.
> You might need to use the beam.Map transform to extract the IDs before using beam.Filter.
> For more details, you can also refer to the [Apache Beam Jobs Wiki on PTransforms](https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs#ptransforms).

<details> <summary><b>Code for Identifying Missing Topic Summary Models</b></summary>

```python
missing_topic_summary_models_pcoll = (
    topic_models_pcoll
    | 'Identify missing TopicSummaryModels' >> beam.Filter(
        lambda topic_id: topic_id not in topic_summary_models_pcoll)
)
```
</details>

beam.Filter(lambda topic_id: topic_id not in topic_summary_models_pcoll) filter checks if each TopicModel ID has a corresponding TopicSummaryModel ID.
This step helps us identify all topic models that lack corresponding summary models, which is the main goal of our validation job.


### Planning Reports and Logs

Logging and reporting are crucial for understanding the outcome of the Beam job and for debugging. In our validation job, we need to consider what specific information is essential to log and report, along with the purpose of each.

#### What to Log and Report:

- **Total Number of Topic Models**:  
  **Purpose**: This value helps verify that the Beam job is processing the expected number of topic models. If the number is lower or higher than anticipated, it can indicate an issue with reading the data from the datastore, such as missing or duplicated topic models.  
  **Details Logged**: The total count of topic models successfully read from the datastore.

- **Total Number of Missing Topic Summary Models**:  
  **Purpose**: This provides a quick overview of how many topic models are missing corresponding summary models, indicating potential data inconsistencies. Although this information can be derived from point 3, reporting it separately serves as a quick sanity check for admins or developers. If the total number is non-zero, it signals an issue that needs further investigation.  
  **Details Logged**: The total count of topic models that do not have corresponding topic summary models.

- **Report Topic IDs with Missing Topic Summary Models**:  
  **Purpose**: While the total number (logged in point 2) provides a high-level summary, this log provides the specific IDs of the topic models that are missing their summary models. This aids in identifying which exact models need attention and allows for detailed investigation and debugging.  
  **Details Logged**: A list of the topic model IDs that do not have corresponding topic summary models.

#### Cross-Consistency Checking

Reporting both the total number of missing summary models and the specific IDs serves a dual purpose:

- **Summary for Monitoring**: The total count is useful as a quick sanity check. If it’s non-zero, it signals that there's an issue needing attention.
- **Detailed Debugging**: The list of IDs is critical for detailed debugging and fixing the issues. Developers can use this detailed report to correct the specific inconsistencies in the data.

By logging and reporting both the high-level totals and the detailed lists, we ensure that the Beam job provides comprehensive information for both quick assessments and in-depth debugging.

> [!IMPORTANT]
> **Practice 6: Next, we need to generate reports.**  
> We have the IDs of all `TopicModels`, the IDs of all `TopicSummaryModels`, and the IDs of the `TopicSummaryModels` that are missing. Let's write the code to generate the following reports:  
> - The total number of `TopicModels`.  
> - The total number of missing `TopicSummaryModels`.  
> - Inform which `TopicModel` is missing a `TopicSummaryModel`.  
> **Hint(s)**:  
> Use the `job_result_transforms.CountObjectsToJobRunResult` transform to count the number of `TopicModels` and the number of missing `TopicSummaryModels`.  
> Remember that this transform will convert the count into a `JobRunResult` with a message indicating the success of the count.  
> For reporting the missing `TopicSummaryModels`, use the `beam.Map` transform to create a `JobRunResult` with a message for each missing `TopicSummaryModel`.  
> To understand the syntax of the above-mentioned transforms, take a look at how these transforms are used in other jobs at Oppia’s codebase.  
> **References for code examples**:  
> - [User Stats Computation Jobs](https://github.com/oppia/oppia/blob/f7d88f1dcf90a30eee1dbddca2a2eb5b46d087f1/core/jobs/batch_jobs/user_stats_computation_jobs.py#L49): Example - Look at how the `CountObjectsToJobRunResult` transform is applied to count objects and convert the result into a `JobRunResult`.  
> - [User Validation Jobs](https://github.com/oppia/oppia/blob/f7d88f1dcf90a30eee1dbddca2a2eb5b46d087f1/core/jobs/batch_jobs/user_validation_jobs.py#L41): Example - Here, the `beam.Map` transform is used to generate `JobRunResult` messages. Review this to see how the transform processes data and produces detailed logging or reporting.

With the IDs of both `TopicModels` and `TopicSummaryModels` and the identified missing `TopicSummaryModels`, we can now proceed to generate the reports. This will include the total number of topic models, the total number of missing topic summary models, and detailed information about each missing topic summary model.
Here's one approach to generating the reports:
<details>
<summary><b>Code for Generating Reports</b></summary>

```python
number_of_topic_models_report = (
    topic_models_pcoll
    | 'Report count of TopicModels' >> (
        job_result_transforms.CountObjectsToJobRunResult(
            'CountTotalTopicModels'))
)

number_of_missing_topic_summary_models_report = (
    missing_topic_summary_models_pcoll
    | 'Report count of missing TopicSummaryModels' >> (
        job_result_transforms.CountObjectsToJobRunResult(
            'CountMissingTopicSummaryModels'))
)

missing_topic_summary_models_report = (
    missing_topic_summary_models_pcoll
    | 'Report missing TopicSummaryModels' >> beam.Map(
        lambda topic_id: job_run_result.JobRunResult.as_stderr(
            'TopicModel with id %s is missing a corresponding TopicSummaryModel' % topic_id)
    )
)
```
</details>

**Report Total Topic Models**: This reports the count of all TopicModel entities.
**Report count of missing TopicSummaryModels**: This reports the count of TopicModel entities that do not have corresponding TopicSummaryModel entities.
**Report missing TopicSummaryModels**: This logs detailed information about each missing summary model.

<details><summary>Here's one approach to do that</summary>

```python
return (
    (
        number_of_topic_models_report,
        number_of_missing_topic_summary_models_report,
        missing_topic_summary_models_report,
    )
    | 'Combine reported results' >> beam.Flatten()
)
```
</details>

This combines all the reports into a single output to give a comprehensive result of our validation job.

<details> <summary><b>Here is the complete code with all the above steps: </b></summary>

```python
from core.jobs import base_jobs
from core.jobs.io import ndb_io
from core.jobs.transforms import job_result_transforms
from core.jobs.types import job_run_result
from core.platform import models

import apache_beam as beam

MYPY = False
if MYPY: # pragma: no cover
    from mypy_imports import topic_models

(topic_models,) = models.Registry.import_models([models.Names.TOPIC])

class ValidateTopicModelsJob(base_jobs.JobBase):
    """Job that validates TopicModel and TopicSummaryModel consistency."""

    def run(self) -> beam.PCollection[job_run_result.JobRunResult]:
        # Fetch all TopicModels
        topic_models_pcoll = (
            self.pipeline
            | 'Get all TopicModels' >> (
                ndb_io.GetModels(topic_models.TopicModel.get_all()))
            | 'Extract topic model ids' >> beam.Map(
                lambda model: model.id)
        )

        # Fetch all TopicSummaryModels
        topic_summary_models_pcoll = (
            self.pipeline
            | 'Get all TopicSummaryModels' >> (
                ndb_io.GetModels(topic_models.TopicSummaryModel.get_all()))
            | 'Extract topic summary model ids' >> beam.Map(
                lambda model: model.id)
        )

        # Identify missing TopicSummaryModels
        missing_topic_summary_models_pcoll = (
            topic_models_pcoll
            | 'Identify missing TopicSummaryModels' >> beam.Filter(
                lambda topic_id: topic_id not in topic_summary_models_pcoll)
        )

        # Generate reports
        number_of_topic_models_report = (
            topic_models_pcoll
            | 'Report count of TopicModels' >> (
                job_result_transforms.CountObjectsToJobRunResult(
                    'CountTotalTopicModels'))
        )

        number_of_missing_topic_summary_models_report = (
            missing_topic_summary_models_pcoll
            | 'Report count of missing TopicSummaryModels' >> (
                job_result_transforms.CountObjectsToJobRunResult(
                    'CountMissingTopicSummaryModels'))
        )

        missing_topic_summary_models_report = (
            missing_topic_summary_models_pcoll
            | 'Report missing TopicSummaryModels' >> beam.Map(
                lambda topic_id: job_run_result.JobRunResult.as_stderr(
                    'TopicModel with id %s is missing a corresponding TopicSummaryModel' % topic_id)
            )
        )

        # Combine reports
        return (
            (
                number_of_topic_models_report,
                number_of_missing_topic_summary_models_report,
                missing_topic_summary_models_report,
            )
            | 'Combine reported results' >> beam.Flatten()
        )
```
</details>

To have your job registered and acknowledged by the front-end, make sure to import the module in the corresponding section of `core/jobs/registry.py`

> Practice 7: Try importing the module in core/jobs/registry.py. Then check out the release coordinator page to verify that the job has been registered.
> Hint: Follow the steps mentioned here in the wiki https://github.com/oppia/oppia/wiki/Apache-Beam-Jobs#local-development-server

With this, our job is finally completed!

## Stage 5: Testing the Beam Job

Let's create unit tests for our `ValidateTopicModelsJob`.The objective of this stage is to ensure that our `ValidateTopicModelsJob` works correctly under different scenarios. We will create unit tests to verify the behavior of our job. Effective testing involves considering various cases, such as:

- **Null Case**: Ensure the job produces no output when there are no models.
- **Standard Case**: Ensure the job correctly processes typical data.
- **Error Case**: Ensure the job handles unexpected or incorrect data gracefully.

When drafting test cases for your Beam job, consider the following:

- **Null Case:**
  - **Scenario**: There are no `TopicModels` and `TopicSummaryModels` in the datastore.
  - **Expected Outcome**: The job should complete without producing any output, indicating that there are no missing or inconsistent models to report. The output should be an empty list or a specific log message like "No TopicModels found."

- **Standard Case:**
  - **Scenario**: The datastore contains a typical set of `TopicModels` and corresponding `TopicSummaryModels` with correct relationships between them.
  - **Expected Outcome**: The job should successfully process the models and report that all models are consistent. For example, "All TopicModels have corresponding TopicSummaryModels," or a success result with counts showing no missing models.

- **Error Case - Missing Summary Models:**
  - **Scenario**: The datastore contains `TopicModels` without corresponding `TopicSummaryModels` or contains corrupted/incomplete data.
  - **Expected Outcome**: The job should correctly identify and report the IDs of the `TopicModels` that are missing `TopicSummaryModels`. Additionally, the job should handle any corrupted data gracefully by logging a warning or error message without crashing. The output could include messages like "TopicModel with ID X is missing a corresponding TopicSummaryModel."

> [!IMPORTANT]
> **Practice 8:** Try to draft the test cases for our Beam jobs. Think of what are the cases that you would like to cover for your Beam job.
>
> **Hint:** Take a look at test files of other jobs to understand how it’s being done.

Here are the specific cases we will cover:

1. **Empty Storage:** Ensure the job produces no output when there are no models.
2. **Topic Model without Summary Model:** Ensure the job correctly identifies a topic model without a corresponding summary model.
3. **Topic Model with Summary Model:** Ensure the job does not report an issue when the topic model has a corresponding summary model.
4. **Multiple Topic Models with and without Summary Models:** Test a mix of topic models with and without corresponding summary models.

To start, we need to create a test class that inherits from `job_test_utils.JobTestBase` and defines our job class. We will also define some constants for the topic IDs we will use in our tests.

> **General Advice:** When writing unit tests for your Beam job, a common approach involves creating mock data that mimics real-world scenarios. This allows you to simulate how the job would process data in a live environment. To make your tests effective, consider the following workflow:
>
> 1. **Set Up Mock Data:** Create mock versions of the models that your Beam job will process, such as `TopicModel` and `TopicSummaryModel`. These mock objects should reflect realistic data that might be encountered during production.
> 2. **Simulate User or Functionality Flows:** Structure your tests to reflect how the job processes data, including different scenarios like valid data, missing data, or inconsistent data between models.
> 3. **Use Setup Methods:** These methods prepare the datastore and other necessary components before running your tests. This involves creating sample models and ensuring they are correctly loaded into the testing environment.

Below is an example of how you can apply this advice to create the necessary setup and test cases for our Beam job. This example sets up a test environment by creating a single `TopicModel` along with its associated `TopicRightsModel`.

<details>
<summary><b>Example Test Setup</b></summary>

```python
from __future__ import annotations

from core import feconf
from core.jobs import job_test_utils
from core.jobs.batch_jobs import topic_validation_jobs
from core.jobs.types import job_run_result
from core.platform import models
from core.domain import topic_domain

import datetime
from typing import Final, Type

MYPY = False
if MYPY:
   from mypy_imports import topic_models

(topic_models,) = models.Registry.import_models([models.Names.TOPIC])

class ValidateTopicModelsJobTests(job_test_utils.JobTestBase):

   JOB_CLASS: Type[topic_validation_jobs.ValidateTopicModelsJob] = topic_validation_jobs.ValidateTopicModelsJob

   TOPIC_ID: Final = 'topic_id'
   story_id_1: Final = 'story_id_1'
   story_id_2: Final = 'story_id_2'
   story_id_3: Final = 'story_id_3'

   def setUp(self) -> None:
       # Set up common attributes for TopicModel and TopicRightsModel.
       super().setUp()
       self.CANONICAL_NAME = 'canonical_name'
       self.LANGUAGE_CODE = 'en'
       self.NAME = 'name'
       self.NEXT_SUBTOPIC_ID = 1
       self.PAGE_TITLE_FRAGMENT_FOR_WEB = 'page_title_fragment_for_web'
       self.STORY_REFERENCE_SCHEMA_VERSION = 1
       self.SUBTOPIC_SCHEMA_VERSION = 1
       self.URL_FRAGMENT = 'url_fragment'

   def create_topic_model(self, id, **kwargs):
       """Creates a mock TopicModel with realistic data for testing."""
       # Default values for the mock TopicModel.
       default_kwargs = {
           'canonical_name': self.CANONICAL_NAME,
           'language_code': self.LANGUAGE_CODE,
           'name': self.NAME,
           'next_subtopic_id': self.NEXT_SUBTOPIC_ID,
           'page_title_fragment_for_web': self.PAGE_TITLE_FRAGMENT_FOR_WEB,
           'story_reference_schema_version': self.STORY_REFERENCE_SCHEMA_VERSION,
           'subtopic_schema_version': self.SUBTOPIC_SCHEMA_VERSION,
           'url_fragment': self.URL_FRAGMENT,
       }
       default_kwargs.update(kwargs)
       # Create the mock TopicModel.
       topic_model = self.create_model(topic_models.TopicModel, id=id, **default_kwargs)
       topic_model.update_timestamps()

       # Create and commit the associated TopicRightsModel.
       first_topic_rights_model = self.create_model(
           topic_models.TopicRightsModel,
           id=id,
           topic_is_published=False
       )
       first_topic_rights_model.commit(
           feconf.SYSTEM_COMMITTER_ID,
           'Create topic rights',
           [{'cmd': topic_domain.CMD_CREATE_NEW}]
       )

       # Commit the TopicModel.
       topic_model.commit(
           feconf.SYSTEM_COMMITTER_ID,
           'Create topic rights',
           [{'cmd': topic_domain.CMD_CREATE_NEW}]
       )
```
</details>

Here are tests for the first two cases. Take a look at them and make sure that you understand how they work.

<details>
<summary><b>Test Case: Empty Storage</b></summary>

```python
def test_empty_storage(self) -> None:
    # Ensure the job produces no output when there are no models
    self.assert_job_output_is_empty()
```
</details>

<details>
<summary><b>Test Case: Topic Model without Summary Model</b></summary>

```python
def test_topic_model_without_summary_model(self) -> None:
    # Create a topic model without a corresponding summary model
    self.create_topic_model(self.TOPIC_ID)

    # Run the job and assert expected output
    self.assert_job_output_is([
        job_run_result.JobRunResult(
            stdout='',
            stderr='Invalid TopicModel with id: %s' % self.TOPIC_ID
        ),
        job_run_result.JobRunResult(
            stdout='CountInvalidTopicModels SUCCESS: 1',
            stderr=''
        )
    ])
```

</details>

> [!IMPORTANT]
> Practice 9: Based on the above test cases, try to write the remaining cases on your own:
>
> Topic Model with Summary Model: Ensure that the job does not report an issue when the topic model has a corresponding summary model.
> Multiple Topic Models with and without Summary Models: Test a mix of topic models that have and do not have corresponding summary models.

<details>
<summary><b>Test Case: Topic Model with Summary Model</b></summary>

```python
def test_topic_model_with_summary_model(self) -> None:
    # Create a TopicSummaryModel for the existing TopicModel
    topic_summary_model = self.create_model(
        topic_models.TopicSummaryModel,
        id=self.TOPIC_ID,
        canonical_name=self.CANONICAL_NAME,
        name=self.NAME,
        language_code=self.LANGUAGE_CODE,
        url_fragment=self.URL_FRAGMENT,
        description='dummy description',
        canonical_story_count=0,
        additional_story_count=0,
        total_skill_count=0,
        total_published_node_count=0,
        uncategorized_skill_count=0,
        subtopic_count=0,
        version=1,
        published_story_exploration_mapping={
            self.story_id_1: [],
            self.story_id_2: [],
            self.story_id_3: []
        },
        topic_model_last_updated=datetime.datetime.utcnow(),
        topic_model_created_on=datetime.datetime.utcnow()
    )

    # Update timestamps and store the model
    topic_summary_model.update_timestamps()
    self.put_multi([topic_summary_model])
    self.create_topic_model(self.TOPIC_ID)

    # Run the job and assert expected output
    self.assert_job_output_is([
        job_run_result.JobRunResult(
            stdout='CountValidTopicModels SUCCESS: 1'
        )
    ])
```

</details>

<details>
<summary><b>Test Case: Multiple Topic Models with and without Summary Models</b></summary>

```python
def test_multiple_topic_models_with_and_without_summary_models(self) -> None:
    """Test a mix of topic models with and without corresponding summary models."""
    # Create a topic model without a summary model
    self.create_topic_model(self.TOPIC_ID + '_1')

    # Create a topic model with a summary model
    self.create_topic_model(self.TOPIC_ID + '_2')
    topic_summary_model_2 = self.create_model(
        topic_models.TopicSummaryModel,
        id=self.TOPIC_ID + '_2',
        canonical_name=self.CANONICAL_NAME,
        name=self.NAME,
        language_code=self.LANGUAGE_CODE,
        url_fragment=self.URL_FRAGMENT,
        description='dummy description',
        canonical_story_count=0,
        additional_story_count=0,
        total_skill_count=0,
        total_published_node_count=0,
        uncategorized_skill_count=0,
        subtopic_count=0,
        version=1,
        published_story_exploration_mapping={
            self.story_id_1: [],
            self.story_id_2: [],
            self.story_id_3: []
        },
        topic_model_last_updated=datetime.datetime.utcnow(),
        topic_model_created_on=datetime.datetime.utcnow()
    )
    topic_summary_model_2.update_timestamps()

    # Create another topic model with a summary model
    self.create_topic_model(self.TOPIC_ID + '_3')
    topic_summary_model_3 = self.create_model(
        topic_models.TopicSummaryModel,
        id=self.TOPIC_ID + '_3',
        canonical_name=self.CANONICAL_NAME,
        name=self.NAME,
        language_code=self.LANGUAGE_CODE,
        url_fragment=self.URL_FRAGMENT,
        description='dummy description',
        canonical_story_count=0,
        additional_story_count=0,
        total_skill_count=0,
        total_published_node_count=0,
        uncategorized_skill_count=0,
        subtopic_count=0,
        version=1,
        published_story_exploration_mapping={
            self.story_id_1: [],
            self.story_id_2: [],
            self.story_id_3: []
        },
        topic_model_last_updated=datetime.datetime.utcnow(),
        topic_model_created_on=datetime.datetime.utcnow()
    )
    topic_summary_model_3.update_timestamps()
    self.put_multi([topic_summary_model_2, topic_summary_model_3])

    # Run the job and assert expected output
    self.assert_job_output_is([
        job_run_result.JobRunResult(
            stderr='Invalid TopicModel with id: %s' % (self.TOPIC_ID + '_1')
        ),
        job_run_result.JobRunResult(
            stdout='CountInvalidTopicModels SUCCESS: 1'
        ),
        job_run_result.JobRunResult(
            stdout='CountValidTopicModels SUCCESS: 2'
        )
    ])
```

</details>

<details>
<summary><b>Here is the complete code for the unit tests:</b></summary>

```python
"""Unit tests for jobs.batch_jobs.topic_validation_jobs."""

from __future__ import annotations

from core import feconf
from core.jobs import job_test_utils
from core.jobs.batch_jobs import topic_validation_jobs
from core.jobs.types import job_run_result
from core.platform import models
from core.domain import topic_domain

import datetime

from typing import Final, Type

MYPY = False
if MYPY:
   from mypy_imports import topic_models

(topic_models,) = models.Registry.import_models([models.Names.TOPIC])


class ValidateTopicModelsJobTests(job_test_utils.JobTestBase):

   JOB_CLASS: Type[topic_validation_jobs.ValidateTopicModelsJob] = topic_validation_jobs.ValidateTopicModelsJob

   TOPIC_ID: Final = 'topic_id'
   story_id_1: Final = 'story_id_1'
   story_id_2: Final = 'story_id_2'
   story_id_3: Final = 'story_id_3'

   def setUp(self) -> None:
       super().setUp()
       self.CANONICAL_NAME = 'canonical_name'
       self.LANGUAGE_CODE = 'en'
       self.NAME = 'name'
       self.NEXT_SUBTOPIC_ID = 1
       self.PAGE_TITLE_FRAGMENT_FOR_WEB = 'page_title_fragment_for_web'
       self.STORY_REFERENCE_SCHEMA_VERSION = 1
       self.SUBTOPIC_SCHEMA_VERSION = 1
       self.URL_FRAGMENT = 'url_fragment'

   def create_topic_model(self, id, **kwargs):
       default_kwargs = {
           'canonical_name': self.CANONICAL_NAME,
           'language_code': self.LANGUAGE_CODE,
           'name': self.NAME,
           'next_subtopic_id': self.NEXT_SUBTOPIC_ID,
           'page_title_fragment_for_web': self.PAGE_TITLE_FRAGMENT_FOR_WEB,
           'story_reference_schema_version': self.STORY_REFERENCE_SCHEMA_VERSION,
           'subtopic_schema_version': self.SUBTOPIC_SCHEMA_VERSION,
           'url_fragment': self.URL_FRAGMENT,
       }
       default_kwargs.update(kwargs)
       topic_model = self.create_model(topic_models.TopicModel, id=id, **default_kwargs)
       topic_model.update_timestamps()

       first_topic_rights_model = self.create_model(
           topic_models.TopicRightsModel,
           id=id,
           topic_is_published=False
       )
       first_topic_rights_model.commit(
           feconf.SYSTEM_COMMITTER_ID,
           'Create topic rights',
           [{'cmd': topic_domain.CMD_CREATE_NEW}]
       )

       topic_model.commit(
           feconf.SYSTEM_COMMITTER_ID,
           'Create topic rights',
           [{'cmd': topic_domain.CMD_CREATE_NEW}]
       )

   def test_empty_storage(self) -> None:
       self.assert_job_output_is_empty()

   def test_topic_model_without_summary_model(self) -> None:
          # Create a topic model without a corresponding summary model
          self.create_topic_model(self.TOPIC_ID)

          # Run the job and assert expected output

          self.assert_job_output_is([
          job_run_result.JobRunResult(
                     stdout='',
                     stderr='Invalid TopicModel with id: %s' % self.TOPIC_ID
          ),
          job_run_result.JobRunResult(
                     stdout='CountInvalidTopicModels SUCCESS: 1',
                     stderr=''
          )
          ])

   def test_topic_model_with_summary_model(self) -> None:
       topic_summary_model = self.create_model(
           topic_models.TopicSummaryModel,
           id=self.TOPIC_ID,
           canonical_name=self.CANONICAL_NAME,
           name=self.NAME,
           language_code=self.LANGUAGE_CODE,
           url_fragment=self.URL_FRAGMENT,
           description='dummy description',
           canonical_story_count=0,
           additional_story_count=0,
           total_skill_count=0,
           total_published_node_count=0,
           uncategorized_skill_count=0,
           subtopic_count=0,
           version=1,
           published_story_exploration_mapping={
               self.story_id_1: [],
               self.story_id_2: [],
               self.story_id_3: []
           },
           topic_model_last_updated=datetime.datetime.utcnow(),
           topic_model_created_on=datetime.datetime.utcnow()
       )

       topic_summary_model.update_timestamps()
       self.put_multi([topic_summary_model])
       self.create_topic_model(self.TOPIC_ID)

       self.assert_job_output_is([
       job_run_result.JobRunResult(
           stdout='CountValidTopicModels SUCCESS: 1'
       )
   ])

   def test_multiple_topic_models_with_and_without_summary_models(self) -> None:
       self.create_topic_model(self.TOPIC_ID + '_1')
       self.create_topic_model(self.TOPIC_ID + '_2')
       topic_summary_model_2 = self.create_model(
           topic_models.TopicSummaryModel,
           id=self.TOPIC_ID + '_2',
           canonical_name=self.CANONICAL_NAME,
           name=self.NAME,
           language_code=self.LANGUAGE_CODE,
           url_fragment=self.URL_FRAGMENT,
           description='dummy description',
           canonical_story_count=0,
           additional_story_count=0,
           total_skill_count=0,
           total_published_node_count=0,
           uncategorized_skill_count=0,
           subtopic_count=0,
           version=1,
           published_story_exploration_mapping={
               self.story_id_1: [],
               self.story_id_2: [],
               self.story_id_3: []
           },
           topic_model_last_updated=datetime.datetime.utcnow(),
           topic_model_created_on=datetime.datetime.utcnow()
       )
       topic_summary_model_2.update_timestamps()
       self.create_topic_model(self.TOPIC_ID + '_3')
       topic_summary_model_3 = self.create_model(
           topic_models.TopicSummaryModel,
           id=self.TOPIC_ID + '_3',
           canonical_name=self.CANONICAL_NAME,
           name=self.NAME,
           language_code=self.LANGUAGE_CODE,
           url_fragment=self.URL_FRAGMENT,
           description='dummy description',
           canonical_story_count=0,
           additional_story_count=0,
           total_skill_count=0,
           total_published_node_count=0,
           uncategorized_skill_count=0,
           subtopic_count=0,
           version=1,
           published_story_exploration_mapping={
               self.story_id_1: [],
               self.story_id_2: [],
               self.story_id_3: []
           },
           topic_model_last_updated=datetime.datetime.utcnow(),
           topic_model_created_on=datetime.datetime.utcnow()
       )
       topic_summary_model_3.update_timestamps()
       self.put_multi([topic_summary_model_2, topic_summary_model_3])

       self.assert_job_output_is([
           job_run_result.JobRunResult(
               stderr='Invalid TopicModel with id: %s' % (self.TOPIC_ID + '_1')
           ),
           job_run_result.JobRunResult(
               stdout='CountInvalidTopicModels SUCCESS: 1'
           ),
           job_run_result.JobRunResult(
               stdout='CountValidTopicModels SUCCESS: 2'
           )
       ])
```

</details>

## Stage 6: Run and Validate the Job

Now let’s try running the job on our local server.

1. Sign in as an administrator ([instructions](https://github.com/oppia/oppia/wiki/How-to-access-Oppia-webpages#log-in-as-a-super-administrator)).
2. Navigate to Admin Page > Roles Tab.
3. Add the "Release Coordinator" role to the username you are signed in with.
4. Navigate to [http://localhost:8181/release-coordinator](http://localhost:8181/release-coordinator), then to the Beam Jobs tab.
5. Search for your job and then click the Play button.
6. Click "Start a new job."

For the above step, we didn’t create any dummy data; thus, it covers a scenario similar to our first unit test. Let’s create dummy data and see how our job works for that. Generate dummy data by following the steps mentioned in this wiki page: [Populating data on local server](https://github.com/oppia/oppia/wiki/Populating-data-on-local-server#maths-classroom-page).

> **Practice 10:** Now let's create dummy data to see how our job works with different scenarios.
>
> Follow the steps mentioned in this [wiki page](https://github.com/oppia/oppia/wiki/Populating-data-on-local-server#maths-classroom-page) to generate dummy data on your local server.  
> Re-run the job following the same steps as before.

The beam job doesn’t report any topic ID with missing topic summary models. That is because, by default, all the topic models are accompanied by their corresponding `TopicSummaryModel`.

> **Practice 11:** To test the job's ability to identify missing `TopicSummaryModel`:
>
> - Set up a local datastore using DSAdmin by following [these instructions](https://github.com/oppia/oppia/wiki/Debugging-datastore-locally).
> - Manually delete one of the `TopicSummaryModel` entries.  
> - Re-run the job to check if it correctly identifies the missing `TopicSummaryModel`.

The beam job will report the topic ID for which you deleted the topic-summary model this time.

> **Practice 12:** Now that you have a good understanding of Beam jobs at Oppia, let's add one more case to cover. Your job should also report any `TopicSummaryModel` that lacks a corresponding `TopicModel`.
>
> **Hint:** You'll need to adjust the job logic to include a check for `TopicSummaryModel` entries without corresponding `TopicModel` entries. Ensure that the unit tests also cover this scenario. Test the job by manually creating or deleting entries in your local datastore to mimic this scenario.

## Conclusion

Congratulations! You've written a Beam job that validates the consistency between `TopicModel` and `TopicSummaryModel`. You have also learned how to test your job with various scenarios to ensure its correctness.

For further reading and more complex scenarios, refer to the [Apache Beam documentation](https://beam.apache.org/documentation/) and [Oppia's developer guides](https://github.com/oppia/oppia/wiki).

### Additional Steps for Production Deployment

> **Note:** If you want to get this job run and deployed in production, there are additional steps to follow. These steps ensure that your job runs smoothly in a live environment and produces the expected results.

Before a job can be run and deployed in production, it must first be tested on the Oppia backup server. Here are the requirements for a job to be considered "fully tested":

- **No Failures:** The job should run without failures on the Oppia backup server.
- **Expected Output:** The job produces the expected output.
- **Expected Outcome:** The job has the expected outcome, which must be verified by user-facing changes, a validation job, or an output check.
- **Approval:** The job should be explicitly approved by the server jobs admin.

To understand the full process of testing Beam jobs at Oppia, please refer to the [Oppia Wiki on Testing Jobs](https://github.com/oppia/oppia/wiki/Testing-jobs-and-other-features-on-production). This wiki page includes detailed instructions and a template for submitting your job for production deployment. The template provides a structured way to request testing and approval, and the linked doc shows how to fill it out specifically for this job.

By following these steps, you'll ensure that your Beam job is ready for production and can be deployed to help maintain the integrity and consistency of data in Oppia.

## We Value Your Feedback

Did you find this tutorial useful? Or, did you encounter any issues or find things hard to grasp? Let us know by opening a discussion on [GitHub Discussions](https://github.com/oppia/oppia/discussions/new?category=tutorial-feedback). We would be happy to help you and make improvements as needed!
