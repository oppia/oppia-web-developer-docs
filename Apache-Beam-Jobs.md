## Table of contents

* [Introduction](#introduction)
* [Apache Beam Job Architecture](#apache-beam-job-architecture)
  * [`Pipeline`s](#pipelines)
  * [`PValue`s](#pvalues)
  * [`PTransform`s](#ptransforms)
    * [`ParDo` and `DoFn`](#pardo-and-dofn)
    * [`Map` and `FlatMap`](#map-and-flatmap)
    * [`Filter`](#filter)
    * [`GroupByKey`](#groupbykey)
    * [Example of using `GroupByKey`,`Filter`, and `FlatMap`](#example-of-using-groupbykeyfilter-and-flatmap)
  * [`Runner`s](#runners)
* [Writing Apache Beam Jobs](#writing-apache-beam-jobs)
  * [1. Subclass the `base_jobs.JobBase` class and override the `run()` method](#1-subclass-the-base_jobsjobbase-class-and-override-the-run-method)
  * [2. Override the `run()` method to operate on `self.pipeline`](#2-override-the-run-method-to-operate-on-selfpipeline)
  * [3. Have the `run()` method return a `PCollection` of `JobRunResult`s](#3-have-the-run-method-return-a-pcollection-of-jobrunresults)
  * [4. Add the job module to `core/jobs/registry.py`](#4-add-the-job-module-to-corejobsregistrypy)
* [Testing Apache Beam Jobs](#testing-apache-beam-jobs)
  * [1. Inherit from `JobTestBase` and override the class constant `JOB_CLASS`](#1-inherit-from-jobtestbase-and-override-the-class-constant-job_class)
  * [2. Run assertions using a `assert_job_output_is_*` method](#2-run-assertions-using-a-assert_job_output_is_-method)
* [Running Apache Beam Jobs](#running-apache-beam-jobs)
  * [Local Development Server](#local-development-server)
  * [Production Server](#production-server)
* [Beam guidelines](#beam-guidelines)
  * [Do not use NDB put/get/delete directly](#do-not-use-ndb-putgetdelete-directly)
  * [Use `get_package_file_contents` for accessing files](#use-get_package_file_contents-for-accessing-files)
* [Common Beam errors](#common-beam-errors)
  * [`'_UnwindowedValues' object is not subscriptable` error](#_unwindowedvalues-object-is-not-subscriptable-error)
  * [`_namedptransform is not iterable` error](#_namedptransform-is-not-iterable-error)
* [Case studies](#case-studies)
  * [Case Study: `SchemaMigrationJob`](#case-study-schemamigrationjob)

## Introduction

[Apache Beam](https://beam.apache.org/) is used by Oppia to perform large-scale datastore operations. We use Apache Beam jobs mostly as batch operation jobs, examples can be:

  * Count the number of models in the datastore.
  * Update a property across all models.
  * Delete all models that are no longer needed.
  * Delete all models that belong to one user.
  * Create stats models from other models.

Jobs can be triggered manually or automatically. Manually this can be done through the release coordinator page. Automatically jobs can be run through code, this is used together with CRON to schedule jobs to be run at a specific date and time.

If you're already familiar with Apache Beam or are eager to start writing a new job, jump to the [case studies](#case-studies). Otherwise, you can read the whole page. If you still have questions after reading, take a look at the [Apache Beam Programming Guide][1] for more details.

## Apache Beam Job Architecture

Conceptually, an Apache Beam job is just a bunch of steps, each of which transforms some input data into some output data. For example, if you wanted to count how many interactions are in all of Oppia's explorations, you could break that task down into a series of transformations:

    .--------------. Count interactions .--------. Sum .-------.
    | Explorations | -----------------> | Counts | --> | Total |
    '--------------'                    '--------'     '-------'

For more complicated tasks, Apache Beam supports tasks whose transformations form a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph), or "DAG." These are just graphs with no cycles. For example, if you wanted to find the ratio of interactions to cards, you could use this DAG:

    .--------------. Count interactions .-------. Sum .------------------.
    | Explorations | -----------------> | Count | --> | Num Interactions |
    '--------------'                    '-------'     '------------------'
           |                                                    |
           |                                                    |
           |                                                    |
           | Count cards .-------. Sum .-----------.            |
           '-----------> | Count | --> | Num Cards |------------+
                         '-------'     '-----------'            |
                                                                |
                                .----------------------. Divide |
                                | Interactions / Cards | <------'
                                '----------------------'

Note that the first example we saw, while linear, is still a DAG!

In Apache Beam, all jobs are represented as these DAGs. The nodes are represented as [`PValue`](#pvalues) objects, and the edges are represented as [`PTransform`](#ptransforms) objects. [`Pipeline`](#pipelines) objects manage the DAGs, and [`Runner`](#runners) objects actually execute the jobs.

Next, we'll look at each of these components in more detail.

### `Pipeline`s

`Pipeline`s manage the "DAG" of `PValue`s and the `PTransform`s that compute them.

For example, here's a schematic representation of a `Pipeline` that counts the number of occurrences of every word in an input file and writes those counts to an output file:

    .------------. io.ReadFromText(fname) .-------. FlatMap(str.split)
    | Input File | ---------------------> | Lines | -----------------.
    '------------'                        '-------'                  |
                                                                     |
       .----------------. combiners.Count.PerElement() .-------.     |
    .- | (word, count)s | <--------------------------- | Words | <---'
    |  '----------------'                              '-------'
    |
    | MapTuple(lambda word, count: '%s: %d' % (word, count)) .------------.
    '------------------------------------------------------> | "word: #"s |
                                                             '------------'
                                                                    |
                             .-------------. io.WriteToText(ofname) |
                             | Output File | <----------------------'
                             '-------------'

Here's the code for this job:

```python
class WordCountJob(base_jobs.JobBase):
    def run(self, fname, ofname):
        return (
            self.pipeline
            | 'Generate Lines' >> beam.io.ReadFromText(fname)
            | 'Generate Words' >> beam.FlatMap(str.split)
            | 'Generate (word, count)s' >> beam.combiners.Count.PerElement()
            | 'Generate "word: #"s' >> (
                beam.MapTuple(lambda word, count: '%s: %d' % (word, count)))
            | 'Write to Output File' >> beam.io.WriteToText(ofname)
        )
```

You might be wondering what's going on with the `|` and `>>` operators. In Python, objects can change how operators apply to them. Apache Beam has changed what the `|` and `>>` operators do, so `|` doesn't perform an OR operation anymore. Instead, `|` is a synonym for calling a `PCollection`'s `.apply()` method with a `PTransform` to create a new `PCollection`. `>>` lets you name a `PTransform` step, which helps document your job. Note that at the very beginning, we also use `|` between the pipeline object and a `PTransform` to start building the job.

### `PValue`s

`PCollection`s are the primary input and output `PValue`s used by `PTransform`s. They are a kind of `PValue` that represent a dataset of (virtually) any size, including unbounded and continuous datasets.

`PBegin` and `PEnd` are "terminal" `PValue`s that signal that the value cannot be produced by an operation (`PBegin`) or that no operation can act on the value (`PEnd`). For example, a `Pipeline` object is a `PBegin`, and the output of a write operation is a `PEnd`.

### `PTransform`s

Recall that `PTransform`s represent the "edges" of the DAG and convert `PValue`s into other `PValue`s.

#### `ParDo` and `DoFn`

`ParDo` is the most flexible `PTransform`. It accepts `DoFn`s, which are simple functions, as arguments and applies them to all elements of the input `PCollection` in parallel. It also accepts functions and lambda functions as arguments. It is analogous to the following code:

```python
do_fn = DoFn()
for value in pcoll:
    do_fn(value)
```
Notice that the return value from the `DoFn` is not used. However, it's possible for the `DoFn` to hold onto state in more advanced implementations.

#### `Map` and `FlatMap`

`beam.Map` is an operation that transforms each item in a `PCollection` into a new value using a plain-old function. It is analogous to the following code (where `fn` is the transformation function):

```python
new_pcoll = []
for value in pcoll:
    new_pcoll.append(fn(value))
return new_pcoll
```

`beam.FlatMap` is a similar transformation, but it _flattens_ the output `PCollection` into a single output `PCollection`. It is analogous to the following code (where `fn` is the transformation function):

```python
new_pcoll = []
for value in pcoll:
    for sub_value in fn(value):
        new_pcoll.append(sub_value)
return new_pcoll
```

#### `Filter`

`beam.Filter` returns a new `PCollection` with all the elements of an input `PCollection`, so long as calling a specified filtering function on the element returned True. It is analogous to the following code (for filtering function `fn`):

```python
new_pcoll = []
for value in pcoll:
    if fn(value):
        new_pcoll.append(value)
return new_pcoll
```

#### `GroupByKey`

`beam.GroupByKey` is useful when you need to perform an operation on elements that share a common property. It takes an input `PCollection` of `(key, value)` elements and returns a mapping from each `key` to all the `values` that were associated with that `key`. It is analogous to the following code:

```python
groups = collections.defaultdict(lambda: collections.defaultdict(list))
for i, pcoll in enumerate(pcolls_to_group):
    # NOTE: Each PCollection must have (key, value) pairs as elements.
    for key, value in pcoll:
        # Items from each PCollection are grouped under the same key and
        # bucketed into their corresponding index.
        groups[key][i].append(value)
return groups
```

#### Example of using `GroupByKey`,`Filter`, and `FlatMap`

For example, in our validation jobs we compute two `PCollection`s:

```python
# Tuples of (ModelKey, True) for each model in the datastore that exists.
existing_models_pcoll = ...
# Tuples of (ModelKey, str) for each error message that should be reported when
# the corresponding model instance does not exist.
errors_if_missing_pcoll = ...
```

To generate a report, we use `GroupByKey` to pair the messages to the existing models.

After this step, we can filter out the pairs where a model existed and report the errors that are left over.

```python
error_pcoll = (
    (
        # A PCollection of Tuple[ModelKey, bool]. A ModelKey identifies an
        # individual model in the datastore.
        existing_models_pcoll,
        # A PCollection of Tuple[ModelKey, str]. Each item corresponds to an
        # error that should be reported when the corresponding instance does not
        # exist.
        errors_if_missing_pcoll,
    )
    # Returns a PCollection of Tuple[ModelKey, Tuple[List[bool], List[str]]].
    | beam.GroupByKey()
    # Discards ModelKey from the PCollection.
    | beam.Values()
    # Only keep groupings that indicate that the model is missing.
    | beam.Filter(lambda (exist_bools, _): not any(exist_bools))
    # Discard the bools and flatten the results into a PCollection of strings.
    | beam.FlatMap(lambda (_, errors): errors)
)
```

### `Runner`s

`Runner`s provide the `run()` method used to visit every node (`PValue`) in the pipeline's DAG by executing the edges (`PTransform`s) to compute their values.  At Oppia, we use `DataflowRunner` to have our `Pipeline`s run on the [Google Cloud Dataflow service](https://cloud.google.com/dataflow).

## Writing Apache Beam Jobs

For this section, we'll walk through the steps of implementing a job by writing one: `CountExplorationStatesJob`.

It's helpful to begin by sketching a diagram of what you want the job to do. We recommend using pen and paper or a whiteboard, but in this wiki page we'll use ASCII art to keep the document self-contained.

Here's a diagram for the `CountExplorationStatesJob`:

    .--------------. Count states .--------. Sum .-------.
    | Explorations | -----------> | Counts | --> | Total |
    '--------------'              '--------'     '-------'

> **TIP**: As illustrated, you don't need to know what the names of the `PTransform`s (edges) used in a diagram are. It's easy to look up the appropriate `PTransform` after drawing the diagram.

Now that we have our bearings, let's get started on implementing the job.

### 1. Subclass the `base_jobs.JobBase` class and override the `run()` method

Make sure your job class name is clear and concise, because the name is presented to release coordinators:

![Screenshot of the Release Coordinator page with a list of job names visible](https://user-images.githubusercontent.com/5094060/135734501-eb9c0370-e98d-4271-b41a-0bf11c25503c.png)

Job names should follow the convention: `<Verb><Noun>Job`.

* For example:

    ```python
    class WeeklyDashboardStatsComputationJob(base_jobs.JobBase):
        """BAD: Name does not begin with a verb."""

        def run(self):
            ...


    class ComputeStatsJob(base_jobs.JobBase):
        """BAD: Unclear what kind of stats are being computed."""

        def run(self):
            ...


    class CountExplorationStatesJob(base_jobs.JobBase):
        """GOOD: Name starts with a verb and "exploration states" is unambiguous."""

        def run(self):
            ...
    ```

Module names should follow the convention: `<noun>_<operation>_jobs.py`.

* For example:
  * `blog_validation_jobs.py`
  * `dashboard_stats_computation_jobs.py`
  * `exploration_indexing_jobs.py`
  * `exploration_stats_regeneration_jobs.py`
  * `model_validation_jobs.py`

    However, you should always prefer placing jobs in preexisting modules if an appropriate one already exists.

For this example, we will write our job in the module: `core/jobs/batch_jobs/exploration_inspection_jobs.py`.

### 2. Override the `run()` method to operate on `self.pipeline`

As illustrated in the Architecture section, jobs are organized by `Pipeline`s, `PTransform`s, and `PCollection`s. Jobs that inherit from `JobBase` are constructed with a `Pipeline` object already accessible via `self.pipeline`. When we write our jobs, we will build them off of `self.pipeline`.

`Pipeline`s are special `PValue`s that represent the entry-point of a job. `PTransform`s that operate on `Pipeline` are generally "producers"; that is to say, operations that produce initial `PCollection`s to work off of.

We can represent this in our DAG by adding a special `Pipeline` node.

      ____________
     /           /\
    |  Pipeline |  |
     \___________\/
            |
            | GetModels()
            v
    .--------------. Count states .--------. Sum .-------.
    | Explorations | -----------> | Counts | --> | Total |
    '--------------'              '--------'     '-------'

> **NOTE**: since pipelines are a part of every job, it's fine to leave it out of a DAG to save on complexity.

Now, let's see how this would translate into code, starting with the Explorations.

```python
from core.jobs import base_jobs
from core.jobs.io import ndb_io
from core.platform import models

(exp_models,) = models.Registry.import_models([models.NAMES.exploration])


class CountExplorationStatesJob(base_jobs.JobBase):

    def run(self):
        exp_model_pcoll = (
            self.pipeline
            | 'Get all ExplorationModels' >> ndb_io.GetModels(
                exp_models.ExplorationModel.get_all())
        )
```

Observe that:
1. We're using `ndb_io.GetModels` rather than `get_multi`
2. We're passing a `Query` to `ndb_io.GetModels`

We use `ndb_io.GetModels()` because we want to work on `PCollection`s of models, not a list of models. In fact, all operations that can be taken on models (`get`, `put`, `delete`) have analogous `PTransform` interfaces defined in `ndb_io`. They are:

| NDB function           | `PTransform` analogue                        |
| ---------------------- | -------------------------------------------- |
| `models = get_multi()` | `model_pcoll = ndb_io.GetModels(Query(...))` |
| `put_multi(models)`    | `model_pcoll \| ndb_io.PutMulti()`           |
| `delete_multi(keys)`   | `key_pcoll \| ndb_io.DeleteMulti()`          |

Note that `get_multi` has the biggest change in interface, in that it takes a `Query` argument. You can get a query for any model by using the class method `get_all`.
> **IMPORTANT:** Never use `datastore_services.query_everything()`!! Due to a limitation in Apache Beam, this operation is incredibly slow and inefficient! **You are almost certainly doing something wrong if you need this function.** Ask @brianrodri/@vojtechjelinek for help if you believe you need to use it regardless.

Why should we use these `PTransform` over the simpler `get`/`put`/`delete` functions? **Performance**. The `get`/`put`/`delete` function calls are all *synchronous*, so your job's performance will suffer greatly by waiting for the operations to complete.

`PTransform`s, on the other hand, are specially crafted to take advantage of the Apache Beam framework and guarantee better performance. In general, **you should always prefer `ndb_io` over any of the `get`/`put`/`delete` functions!** If you think you have a valid need for avoiding `ndb_io`, then speak with @brianrodri/@vojtechjelinek first.

Let's get back to implementing the job.

```python
def run(self):
    exp_model_pcoll = (
        self.pipeline
        | 'Get all ExplorationModels' >> ndb_io.GetModels(
            exp_models.ExplorationModel.get_all())
    )

    state_count_pcoll = (
        exp_model_pcoll
        | 'Count states' >> beam.Map(self.get_number_of_states)
    )
```

Note that we chose to use `beam.Map` here instead of `beam.ParDo`. This is mostly a stylistic choice, as `beam.Map` is just a specialized version of `ParDo`, in that `Map` simply takes each input element and "maps" it to a single output element. In our case, each `ExplorationModel` will map to a single `int`, the number of states.

Here is the implementation of `get_number_of_states`. This function transforms the model into a domain object, and then counts the number of states in the corresponding `dict`.

```python
def get_number_of_states(self, model: ExplorationModel) -> int:
    exploration = exp_fetchers.get_exploration_from_model(model)
    return len(exploration.states)
```

Finally, we need to sum all the counts together. We'll use `beam.CombineGlobally` to accomplish this, which uses an input function to combine values of a `PCollection`. It returns a `PCollection` with a single element: the result of the combination.

```python
def run(self):
    exp_model_pcoll = (
        self.pipeline
        | 'Get all ExplorationModels' >> ndb_io.GetModels(
            exp_models.ExplorationModel.get_all())
    )

    state_count_pcoll = (
        exp_model_pcoll
        | 'Count states' >> beam.Map(self.get_number_of_states)
    )

    state_count_sum_pcoll = (
        state_count_pcoll
        | 'Sum values' >> beam.CombineGlobally(sum)
    )
```

> **IMPORTANT**: We take special care to pass very simple objects (like ints and models) in between `PTransform`s. This is intentional, complex objects cannot be serialized without special care (TL;DR: objects must be [picklable](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled)). When passing objects between `PTransform`s in your jobs, use simple data structures and simple types as much as possible.

With this, our objective is complete. However, there's still more code to write!

### 3. Have the `run()` method return a `PCollection` of `JobRunResult`s

* In English, this means that **the job _must_ report _something_ about what occurred during its execution.** For example, this can be the errors it discovered or the number of successful operations it was able to perform. **Empty results are forbidden!**

  * If you don't think your job has any results worth reporting, then just print a "success" metric with the number of models it processed.

* `JobRunResult` has two fields: `stdout` and `stderr`. They are analogous to a program's output, and should be used in a similar capacity for jobs -- put problems encountered by the job in `stderr` and informational outputs in `stdout`.

* `JobRunResult` outputs should answer the following questions:

  * Did the job run without any problems? How and why do I know?
  * How much work did the job manage to do?
  * If the job encountered a problem, what caused it?

Our job is trying to report the total number of states across all explorations, so we need to create a `JobRunResult` that holds that information. For this, we can use the `as_stdout` helper method:

```python
def run(self):
    exp_model_pcoll = (
        self.pipeline
        | 'Get all ExplorationModels' >> ndb_io.GetModels(
            exp_models.ExplorationModel.get_all())
    )

    state_count_pcoll = (
        exp_model_pcoll
        | 'Count states' >> beam.Map(self.get_number_of_states)
    )

    state_count_sum_pcoll = (
        state_count_pcoll
        | 'Sum values' >> beam.CombineGlobally(sum)
    )

    return (
        state_count_sum_pcoll
        | 'Map as stdout' >> beam.Map(job_run_result.JobRunResult.as_stdout)
    )
```

The method maps every element in a `PCollection` to a `JobRunResult` with their stringified-values as its `stdout`.

### 4. Add the job module to `core/jobs/registry.py`

To have your job registered and acknowledged by the front-end, make sure to import the module in the corresponding section of `core/jobs/registry.py`:
https://github.com/oppia/oppia/blob/973f777a6c5a8c3442846bda839e63856dfddf72/core/jobs/registry.py#L33-L50

---

With this, our job is finally completed!

Here is the cleaned-up implementation of our job:

```python
from core.domain import exp_fetchers
from core.jobs import base_jobs
from core.jobs.io import ndb_io
from core.platform import models

import apache_beam as beam

(exp_models,) = models.Registry.import_models([models.NAMES.exploration])


class CountExplorationStatesJob(base_jobs.JobBase):

    def run(self) -> beam.PCollection[job_run_result.JobRunResult]:
        return (
            self.pipeline
            | 'Get all ExplorationModels' >> ndb_io.GetModels(
                exp_models.ExplorationModel.get_all())
            | 'Count states' >> beam.Map(self.get_number_of_states)
            | 'Sum values' >> beam.CombineGlobally(sum)
            | 'Map as stdout' >> beam.Map(job_run_result.JobRunResult.as_stdout)
        )

    def get_number_of_states(self, model: exp_models.ExplorationModel) -> int:
        exploration = exp_fetchers.get_exploration_from_model(model)
        return len(exploration.states)
```

## Testing Apache Beam Jobs

First and foremost, you should follow our guidelines for [writing backend tests](https://github.com/oppia/oppia/wiki/Backend-tests#write-backend-tests). This includes naming your test cases (`test_{{action}}_with_{{with_condition}}_{{has_expected_outcome}}`) and our general test case structure ("Setup", "Baseline verification", "Action", "Endline verification").

There are two base classes dedicated to testing our Apache Beam jobs: `PipelinedTestBase` and `JobTestBase`.

`PipelinedTestBase` (and its subclass, `JobTestBase`) exposes two special assertion methods: `assert_pcoll_equal` and `assert_pcoll_empty`.

The class operates by first, in `setUp()`, entering the context of a `Pipeline` object (accessible via `self.pipeline`). Upon exiting the context, the `Pipeline` will execute any operations attached to it. Running the `assert_pcoll_*` methods will add a "verification" `PTransform` to the input `PCollection`, and then close the context (thus running it immediately). For this reason, **only _one_ `assert_pcoll_*` method may be called in a test case!** If you want to run multiple assertions on a `PCollection`, then create a separate test case for that purpose.

> **NOTE**: The verification `PTransform` will also run type checks on all inputs/outputs generated by the `PTransform`s under test!

Here's an example:
```python
def test_validate_model_id_with_invalid_model_id_reports_an_error(self):
    # Setup.
    invalid_id_model = base_models.BaseModel(
        id='123@?!*',
        created_on=self.YEAR_AGO,
        last_updated=self.NOW)

    # Action.
    output = (
        self.pipeline
        | beam.Create([invalid_id_model])
        | beam.ParDo(base_validation.ValidateBaseModelId())
    )

    # Endline verification.
    self.assert_pcoll_equal(output, [
        base_validation_errors.ModelIdRegexError(
            invalid_id_model,
            base_validation.BASE_MODEL_ID_PATTERN),
    ])
```

For testing _jobs_, you should follow the following steps (we'll use `CountExplorationStatesJob` as an example):

### 1. Inherit from `JobTestBase` and override the class constant `JOB_CLASS`

The current convention is to name your test cases `<JobName>Tests`, but you can create better names if you want to break tests up. For our example, we'll keep things simple.

```python
class CountExplorationStatesJobTests(test_jobs.JobTestBase):

    JOB_CLASS = CountExplorationStatesJob
```

### 2. Run assertions using a `assert_job_output_is_*` method

When testing a job, we should aim to cover behavior and common edge cases. For this job, we'll have 3 main tests:
1. When there are no Explorations in the datastore.
2. When there is exactly 1 Exploration in the datastore.
3. When there are many Explorations in the datastore.

```python
def test_empty_datastore(self):
    # Don't add any explorations to the datastore.
    self.assert_job_output_is_empty()

def test_single_exploration(self):
    self.save_new_linear_exp_with_state_names_and_interactions(
        'e1', 'o1', ['A', 'B', 'C'], ['TextInput'])

    self.assert_job_output_is([
        job_run_result.JobRunResult(stdout='3'),
    ])

def test_many_explorations(self):
    self.save_new_linear_exp_with_state_names_and_interactions(
        'e1', 'o1', ['A', 'B', 'C'], ['TextInput'])
    self.save_new_linear_exp_with_state_names_and_interactions(
        'e2', 'o1', ['D', 'E', 'F', 'G', 'H'], ['TextInput'])
    self.save_new_linear_exp_with_state_names_and_interactions(
        'e3', 'o1', ['I', 'J'], ['TextInput'])
    self.save_new_linear_exp_with_state_names_and_interactions(
        'e4', 'o1', ['K', 'L', 'M', 'N'], ['TextInput'])

    self.assert_job_output_is([
        job_run_result.JobRunResult(stdout='14'),
    ])
```

Note that `self.assert_job_output_is(...)` and `self.assert_job_output_is_empty()` do as advertised -- they run the job to completion and verify the result.

> **IMPORTANT:** Only one `assert_job_output_is` assertion can be performed in a test body. Multiple calls will result in an exception instructing you to split the test apart.

Just because a job passes in unit tests does not guarantee it will pass in production. This is because workers, which execute the pipeline code, are run in a special environment where the code base is configured differently. While Oppia's jobs team works to resolve the differences, be careful about using complex and/or confusing objects. The simpler your job, the greater chance it'll work in production!

## Running Apache Beam Jobs

### Local Development Server

These instructions assume you are running a local development server. If you are a release coordinator running these jobs on the production or testing servers, you should already have been granted the "Release Coordinator" role, so you can skip steps 1-3.

1. Sign in as an administrator ([instructions][3]).
2. Navigate to **Admin Page > Roles Tab**.
3. Add the "Release Coordinator" role to the username you are signed in with.
4. Navigate to http://localhost:8181/release-coordinator, then to the **Beam Jobs tab**.
5. Search for your job and then click the **Play button**.
6. Click "Start new job".

![Screen recording showing how to run jobs](https://user-images.githubusercontent.com/5094060/128743997-70cca5f9-0b76-4294-806e-f65f5df5be95.gif)

### Production Server

Before a job can be run and deployed in production, it must first be tested on the Oppia backup server.

If your job is not essential for the release and has not been fully tested by the release cut, then it is not going into the release. "Fully tested" means:
- The job should run without failures on the Oppia backup server.
- The job produces the expected output.
- The job has the expected outcome (this must be verified by e.g. user-facing changes, or a validation job, or an output check, etc.).
- The job should be explicitly approved by the server jobs admin (currently @seanlip and @vojtechjelinek).

Also, in case your job changes data in the datastore, there has to be a validation job accompanying it to verify that the data that you are changing is valid in the server. **The validation job will have to be "Fully tested" before testing on the migration job can start.**

In case there is invalid data observed, either your migration job should fix it programmatically, or the corresponding data has to be manually fixed before the migration job can be run. This is valid for both testing in the backup server and running in production.

For a full overview of the process to get your job tested on the Oppia backup server, refer to the corresponding [wiki page](https://github.com/oppia/oppia/wiki/Testing-jobs-and-other-features-on-production).

#### Instruction for job testers

There are two ways to perform the testing of the Beam jobs, both of these need to be done by a person that has deploy access to the backup server.

##### Deploy to backup server

This way provides full testing of the job.

1. Deploy branch containing the job to the backup server
2. Run the job through the [release coordinator page](https://oppiaserver-backup-migration.appspot.com/release-coordinator)
3. If the job fails you can check the details of the error on the Google Cloud Console in the Dataflow section


##### Run the job on backup server through the local dev server

The downside of this approach is that you cannot get the job output, you can only verify that it works.

In order to run jobs through the local dev server you need to have JSON key that will provide access to the backup server. The key can be generated according to step 4 and step 5 of the [Quickstart for Python](https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python).

1. Have the JSON key ready
2. Add `GOOGLE_APPLICATION_CREDENTIALS: "<absolute path to JSON key>"` to `env_variables` in _app_dev.yaml_
3. In _core/domain/beam_job_services.py_ change value of `run_synchronously` to `False`
4. In _core/feconf.py_
  1. Change the value of `OPPIA_PROJECT_ID` to `'oppiaserver-backup-migration'`
  1. Change the value of `DATAFLOW_TEMP_LOCATION` to `'gs://oppiaserver-backup-migration-beam-jobs-temp/'`
  1. Change the value of `DATAFLOW_STAGING_LOCATION` to `'gs://oppiaserver-backup-migration-beam-jobs-staging/'`
5. Start the dev server and run the job through the release coordinator page
6. If the job fails you can check the details of the error on the Google Cloud Console in the Dataflow section

## Beam guidelines

### Do not use NDB put/get/delete directly

Even though it is possible to use NDB functions directly, they should not be used because they are slow and we have Beam compliant alternatives from them. All these alternatives are located in _core/jobs/io/ndb_io.py_.

- Instead of using `get`, `get_multi`, `get_by_id`, etc. you should use `GetModels`, and you should pass a query to it, `GetModels` will execute the query and return a `PCollection` of the models that were returned by the query. 
- Instead of using `put`, `put_multi`, etc. you should use `PutModels`, and you just pipe a `PCollection` of models to it and they will be put into the datastore.
- Instead of using `delete`, `delete_multi`, etc. you should use `DeleteModels`, and you just pipe a `PCollection` of models to it and they will be deleted from the datastore.

All of the aforementioned classes are already used in the codebase so you can look for examples.

### Use `get_package_file_contents` for accessing files

If you need to access a file in a Beam job, please use `get_package_file_contents` (from _core/constants.py_) instead of `open` or `open_file` (from _core/utils.py_). Also, make sure that the file is included in the _assets_ folder or is listed in _MANIFEST.in_ explicitly.

#### Example

When we have a function that is used in a Beam pipeline, like:

```python
@staticmethod
def function_used_in_beam_pipeline():
    file = utils.open_file('assets/images/about/cc.svg', 'rb')
    return file.read()
```

it needs to be replaced with something like:

```python
@staticmethod
def function_used_in_beam_pipeline():
    return constants.get_package_file_contents(
        'assets', 'images/about/cc.svg', binary_mode=True
    )
```

## Common Beam errors

### `'_UnwindowedValues' object is not subscriptable` error

This error usually happens when you attempt to access an element in what you expect is a list, but Beam actually didn't convert it to a list. The solution usually is to transform the element to list explicitly using `list()`. **Some comments on the internet might suggest a usage of `SessionWindow` or similar stuff, but since all our jobs are batch jobs that process some final list of elements this solution won't work.**

#### Example

```python
new_user_stats_models = (
    {
        'suggestion': suggestions_grouped_by_target,
        'opportunity': exp_opportunities
    }
    | 'Merge models' >> beam.CoGroupByKey()
    | 'Get rid of key' >> beam.Values()  # pylint: disable=no-value-for-parameter
    | 'Generate stats' >> beam.ParDo(
        lambda x: self._generate_stats(
            x['suggestion'][0] if len(x['suggestion']) else [],
            x['opportunity'][0][0] if len(x['opportunity']) else None
        ))
)
```
The code above throws this error `'_UnwindowedValues' object is not subscriptable [while running 'Generate stats']`, we know that the issue is in the last part of the code ('Generate stats' part). After some debugging, we discover that the code needs to be changed to.
```python
| 'Generate stats' >> beam.ParDo(
    lambda x: self._generate_stats(
        x['suggestion'][0] if len(x['suggestion']) else [],
        list(x['opportunity'][0])[0] if len(x['opportunity']) else None
    ))
```

### `_namedptransform is not iterable` error

This error sometimes happens when you forget to add a label for some operation (the strings of code before `>>`). The solution is to add a label for all operations. 

#### Example

```python
some_values = (
    some_models
    | beam.Values()
)
```
The code above might return `'_namedptransform is not iterable` in the job output. We can fix this by adding an appropriate label.
```python
some_values = (
    some_models
    | 'Get values' >> beam.Values()
)
```

## Case Studies

The case studies are sorted in order of increasing complexity. Study the one that best suits your needs.

If none of them help you implement your job, you may request a new one by adding a comment to [#13190](https://github.com/oppia/oppia/issues/13190) with answers to the following questions:

* Why do I want a new case study?
* Why are the current case studies insufficient?
* What answers would the "perfect" case study provide?

Then we'll start write a new Case Study to help you, and future contributors, as soon as we can (@brianrodri will always notify you of how long it'll take).

### Case Study: `SchemaMigrationJob`

**Difficulty:** Medium

**Key Concepts:**

* Getting and Putting NDB models
* Partitioning one `PCollection` into many `PCollection`s.
* Returning variable outputs from a `DoFn`

---

Let's start by listing the specification of a schema migration job:

* We can assume:

  * The schema version of a model is in the closed range `[1, N]`, where `N` is the latest version.
  * All migration functions are implemented in terms of taking `n` to `n + 1`.

- Our job should conform to the following requirements:

  * Models should only be put into storage after successfully migrating to v`N`.
  * Models that were already at v`N` should be reported separately.

        .--------------. Partition(lambda model: model.schema_version)
        | Input Models | ---------------------------------------------.
        '--------------'                                              |
                                                     .-----------.    |
                            .----------------------- | Model @v1 | <--|
                            |                        '-----------'    |
                            |                                         |
                            | ParDo(MigrateToNextVersion())           |
                             >-----------------------------.          |
                            |                              |          |
                            |                              v          |
                            |                        .-----------.    |
                            '----------------------- | Model ... | <--'
                                                     '-----------'
                                                           |
                                                           v
                                                     .-----------.
                                                     | Model @vN |
                                                     '-----------'
                                                           |
                         .-----------.  ndb_io.PutModels() |
                         | Datastore | <-------------------'
                         '-----------'

There's a lot of complexity here, so we'll need many `PTransform`s to write our job. We'll focus on the most interesting one: the loop to migrate models to the next version.

```python
class MigrateToNextVersion(beam.DoFn):

    def process(self, input_model):
        if input_model.schema_version < ExplorationModel.LATEST_SCHEMA_VERSION:
            model = job_utils.clone_model(input_model)
            exp_services.migrate_to_next_version(model)
            yield model


class MigrateToLatestVersion(beam.PTransform):
    """Diagram:

    .--------------. Partition(lambda model: model.schema_version)
    | Input Models | ---------------------------------------------.
    '--------------'                                              |
                                                 .-----------.    |
                        .----------------------- | Model @v1 | <--|
                        |                        '-----------'    |
                        |                                         |
                        | ParDo(MigrateToNextVersion())           |
                         >-----------------------------.          |
                        |                              |          |
                        |                              v          |
                        |                        .-----------.    |
                        '----------------------- | Model ... | <--'
                                                 '-----------'
                                                       |
                                                       v
                                                 .-----------.
                                                 | Model @vN |
                                                 '-----------'
    """

    def expand(self, exp_model_pcoll):
        models_by_schema_version = (
            exp_model_pcoll
            | beam.Partition(
                lambda model, _: model.schema_version - 1,
                ExplorationModel.LATEST_SCHEMA_VERSION)
        )

        do_fn = MigrateToNextVersion()
        results = [models_by_schema_version[0] | beam.Map(do_fn)]

        for models_at_ith_version in models_by_schema_version[1:-1]:
            models_to_migrate = (
                (results[-1].updated_models, models_at_ith_version)
                | beam.Flatten()
            )
            results.append(models_to_migrate | beam.FlatMap(do_fn))
```

Note that this implementation won't work as-is since we focused on the step where we upgrade the models. To get this fully working, we'd need to write a `Pipeline` that handles loading in the models and writing the upgraded models back to the datastore.

[1]: https://beam.apache.org/documentation/programming-guide/
[2]: https://github.com/oppia/oppia/blob/4d2f639869e57fbeaada414d923cae83eb0e082e/jobs/job_utils.py#L37-L63
[3]: https://github.com/oppia/oppia/wiki/How-to-access-Oppia-webpages#log-in-as-a-super-administrator
