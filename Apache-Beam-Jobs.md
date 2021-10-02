## Table of contents

* [Introduction](#introduction)
* [Running Apache Beam Jobs](#running-apache-beam-jobs)
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
* [Testing Apache Beam Jobs](#testing-apache-beam-jobs)
* [Case studies](#case-studies)
  * [Case study: `CountAllModelsJob`](#case-study-countallmodelsjob)
  * [Case Study: `SchemaMigrationJob`](#case-study-schemamigrationjob)

## Introduction

[Apache Beam](https://beam.apache.org/) is used by Oppia to perform large-scale datastore operations. There are two types of operations:

* **Batch**: Operations that are designed to be executed _once_ on the current state of the datastore. Here are some examples:

  * Count the number of models in the datastore.
  * Update a property across all models.
  * Validate the relationships between models.

* **Continuous**: Operations that are designed to run _indefinitely_ by reacting to updates to the datastore. Here are some examples:

  * Updating the top 10 answers to a lesson every time a new answer is submitted.
  * Generating notifications for the events that users have subscribed to whenever those events change.

If you're already familiar with Apache Beam or are eager to start writing a new job, jump to the [case studies](#case-studies). Otherwise, you can read the whole page. If you still have questions after reading, take a look at the [Apache Beam Programming Guide][1] for more details.

## Running Apache Beam Jobs

These instructions assume you are running a local development server. If you are a release coordinator running these jobs on the production or testing servers, you should already have been granted the "Release Coordinator" role, so you can skip steps 1-3.

1. Sign in as an administrator ([instructions][3]).
2. Navigate to **Admin Page > Roles Tab**.
3. Add the "Release Coordinator" role to the username you are signed in with.
4. Navigate to http://localhost:8181/release-coordinator, then to the **Beam Jobs tab**.
5. Search for your job and then click the **Play button**.
6. Click "Start new job".

![Screen recording showing how to run jobs](https://user-images.githubusercontent.com/5094060/128743997-70cca5f9-0b76-4294-806e-f65f5df5be95.gif)

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
Notice that the return value from the `DoFn` is not used. However, it's possible for the DoFn to hold onto state in more advanced implementations.

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

> TIP: As illustrated, you don't need to know what the names of the `PTransform`s (edges) used in a diagram are. It's easy to look up the appropriate `PTransform` after drawing the diagram.

Now that we have our bearings, let's get started on implementing the job.

### 1. Subclass the `base_jobs.JobBase` class and override the `run()` method

Make sure your job class name is clear and concise, because the name is presented to release coordinators:

![image](https://user-images.githubusercontent.com/5094060/135734501-eb9c0370-e98d-4271-b41a-0bf11c25503c.png)

Job names should follow the convention: `<Verb><Noun>Job`.

-   For example:

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

-   For example:
    * `blog_validation_jobs.py`
    * `dashboard_stats_computation_jobs.py`
    * `exploration_indexing_jobs.py`
    * `exploration_stats_regeneration_jobs.py`
    * `model_validation_jobs.py`

    However, you should always prefer placing jobs in pre-existing modules if an appropriate one already exists.

For this example, we will write our job in the module: `core/jobs/batch_jobs/exploration_inspection_jobs.py`.

### 2. Override the `run()` method to operate on `self.pipeline`

As illustrated in the Architecture section, jobs are organized by `Pipeline`s, `PTransform`s, and `PCollection`s. Jobs that inherit from `JobBase` are constructed with a `Pipeline` object already accessible via `self.pipeline`. When we write our jobs, we will build them off of `self.pipeline`.

`Pipeline`s are special `PValue`s that represent the entrypoint of a job. `PTransform`s that operate on `Pipeline` are generally "producers"; that is to say, operations that produce intial `PCollection`s to work off of.

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

Note that, since pipelines are a part of every job, it's fine to leave it out of a DAG to save on complexity.

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
                exp_models.ExplorationModel.get_all(deleted=False))
        )
```

Observe that:
1. We're using `ndb_io.GetModels` rather than `get_multi`
2. We're passing a Query to `ndb_io.GetModels`

We use `ndb_io.GetModels()` because we want to work on `PCollection`s of models, not a list of models. In fact, all operations that can be taken on models (`get`, `put`, `delete`) have analogous `PTransform` interfaces defined in `ndb_io`. They are:

| NDB function           | `PTransform` analogue                        |
| ---------------------- | -------------------------------------------- |
| `models = get_multi()` | `model_pcoll = ndb_io.GetModels(Query(...))` |
| `put_multi(models)`    | `model_pcoll \| ndb_io.PutMulti()`           |
| `delete_multi(keys)`   | `key_pcoll \| ndb_io.DeleteMulti()`          |

Note that `get_multi` has the biggest change in interface, in that it takes a `Query` argument. You can get a query for any model by using the class method `get_all`.
-   **IMPORTANT:** Never use `datastore_services.query_everything()`!! Due to a limitation in Apache Beam, this operation is incredibly slow and inefficient! **You are almost certainly doing something wrong if you need this function.** Ask @brianrodri/@vojtechjelinek for help if you believe you need to use it regardless.

Why should we use these `PTransform` over the simpler `get`/`put`/`delete` functions? **Performance**. The `get`/`put`/`delete` function calls are all *synchronous*, so your job's performance will suffer greatly by waiting for the operations to complete.

`PTransform`s, on the other hand, are specially crafted to take advantage of the Apache Beam framework and guarantee better performance. In general, **you should always prefer `ndb_io` over any of the `get`/`put`/`delete` functions!** If you think you have a valid need for avoiding `ndb_io`, then speak with @brianrodri/@vojtechjelinek first.

Let's get back to implementing the job.

```python
def run(self):
    exp_model_pcoll = (
        self.pipeline
        | 'Get all ExplorationModels' >> ndb_io.GetModels(
            exp_models.ExplorationModel.get_all(deleted=False))
    )

    state_count_pcoll = (
        exp_model_pcoll
        | 'Count states' >> beam.Map(self.get_number_of_states)
    )
```

Note that we chose to use `beam.Map` here instead of `beam.ParDo`. This is mostly a stylistic choice, as `beam.Map` is just a specialized version of `ParDo`, in that `Map` simply takes each input element and "maps" it to a single output element. In our case, each `ExplorationModel` will map to a single `int`, the number of states.

Here is the implementation of `get_number_of_states`. This function transforms the model into a domain object, and then counts the number of states in the corresponding `dict`.

```python
def get_number_of_states(self, exp_model: ExplorationModel) -> int:
    exp = exp_fetchers.get_exploration_from_model(exp_model)
    return len(exp.states)
```

Finally, we need to sum all the counts together. We'll use `beam.CombineGlobally` to accomplish this, which uses an input function to combine values of a `PCollection`. It returns a `PCollection` with a single element: the result of the combination.

```python
def run(self):
    exp_model_pcoll = (
        self.pipeline
        | 'Get all ExplorationModels' >> ndb_io.GetModels(
            exp_models.ExplorationModel.get_all(deleted=False))
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



With this, our objective is complete. However, there's still more code to write!

### 3. Have the `run()` method return a `PCollection` of `JobRunResult`s

* In English, this means that **the job _must_ report _something_ about what occurred during its execution.** For example, this can be the errors it discovered or the number of successful operations it was able to perform. **Empty results are forbidden!**

  * If you don't think your job has any results worth reporting, then just print a "success" metric with the number of models it processed.

* `JobRunResult` outputs should answer the following questions:

  * Did the job run without any problems? How and why do I know?
  * How much work did the job manage to do?
  * If the job encountered a problem, what caused it?

Our job is trying to report the total number of states across all explorations, so we need to create a `JobRunResult` that holds that information. For this, we can simply use the `as_stdout` helper method:

```python
def run(self):
    exp_model_pcoll = (
        self.pipeline
        | 'Get all ExplorationModels' >> ndb_io.GetModels(
            exp_models.ExplorationModel.get_all(deleted=False))
    )

    state_count_pcoll = (
        exp_model_pcoll
        | 'Count states' >> beam.Map(self.get_number_of_states)
    )

    state_count_sum_pcoll = (
        state_count_pcoll
        | 'Sum values' >> beam.CombineGlobally(sum)
    )

    return state_count_sum_pcoll | beam.Map(job_run_result.JobRunResult.as_stdout)
```

The method maps every element in a `PCollection` into a `JobRunResult` with the stringified-value as its `stdout`.

With this, our job is fully written! Move on to the next section for instructions on _testing_ your new job.

## Testing Apache Beam Jobs

We'll assume that we've written a fully operational `CountExplorationStatesJob`, and go over the steps in ensuring the job works as intended.

### 1. Inherit from `JobTestBase` and override the class constant `JOB_CLASS`

The current convention is to name your test cases `<JobName>Tests`, but you can create better names if you want to break tests up into groups of specialized focus. For our example, we'll keep things simple.

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
        'e1', 'o1', ['D', 'E', 'F', 'G', 'H'], ['TextInput'])
    self.save_new_linear_exp_with_state_names_and_interactions(
        'e1', 'o1', ['I', 'J'], ['TextInput'])
    self.save_new_linear_exp_with_state_names_and_interactions(
        'e1', 'o1', ['K', 'L', 'M', 'N'], ['TextInput'])

    self.assert_job_output_is([
        job_run_result.JobRunResult(stdout='14'),
    ])
```

Note that `self.assert_job_output_is(...)` and `self.assert_job_output_is_empty()` do as advertised -- they run the job to completion and verify the result.

-   **IMPORTANT:** Only one `assert_job_output_is` assertion can be performed in a test body. Multiple calls will result in an exception instructing you to split the test apart.

## Case studies

The case studies are sorted in order of increasing complexity. Study the one that best suits your needs.

If none of them help you implement your job, you may request a new one by adding a comment to [#13190](https://github.com/oppia/oppia/issues/13190) with answers to the following questions:

* Why do I want a new case study?
* Why are the current case studies insufficient?
* What answers would the "perfect" case study provide?

Then we'll start write a new Case Study to help you, and future contributors, as soon as we can (@brianrodri will always notify you of how long it'll take).

### Case study: `CountAllModelsJob`

**Difficulty:** Trivial

**Key Concepts:**

* Fetching NDB models
* Counting elements in a `PCollection`
* Creating `JobRunResult` values
* Job registration

---

We'll start by writing a boilerplate `PTransform` which accepts models as input, and returns `(kind, #)` tuples (where `kind` is the name of the model's class, as a string).

```python
from jobs import job_utils
from jobs.types import job_run_result

import apache_beam as beam


class CountModels(beam.PTransform):
    """Returns the number of models after grouping them by their "kind".

    Kind is a unique identifier given to all models. In practice, the following
    always holds:

        job_utils.get_model_kind(FooModel) == 'FooModel'
    """

    def expand(self, model_pcoll):
        """Method PTransform subclasses must implement.

        Args:
            model_pcoll: PCollection[base_models.BaseModel]. The collection of
                models to count.

        Returns:
            PCollection[Tuple[str, int]]. The (kind, count) tuples corresponding
            to the input PCollection.
        """
        return (
            model_pcoll
            # "Map" every model to its kind. Analogous to the code:
            # [job_utils.get_model_kind(model) for model in model_pcoll]
            | beam.Map(job_utils.get_model_kind)
            # Built-in PTransform that reduces a collection of values into
            # (value, # discovered) tuples.
            | beam.combiners.Count.PerElement()
        )
```

Next, we'll write the job which applies the `PTransform` to every model in the datastore. We can keep both the `PTransform` and the job in the same file, since they are so tightly coupled. Unit tests can focus on one or the other.

```python
from core.platform import models
from jobs import base_jobs
from jobs.io import ndb_io

datastore_services = models.Registry.import_datastore_services()


class CountAllModelsJob(base_jobs.JobBase):
    """Counts every model in the datastore."""

    def run(self):
        query_everything = datastore_services.query_everything()
        all_models = self.pipeline | ndb_io.GetModels(query_everything)
        return (
            all_models
            | CountModels()
            # We'll convert the tuples into `JobRunResult` instances, where the
            # stdout field is used to store the tuple's value.
            | beam.Map(job_run_result.JobRunResult.as_stdout)
        )
```

Finally, we'll import this job into the registry file. Let's assume the name of
the file was `jobs/count_all_models_jobs.py`.

```diff
  # file: jobs/registry.py

  from jobs import base_jobs
  from jobs import base_validation_jobs
+ from jobs import count_all_models_jobs
```

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

* Our job should conform to the following requirements:

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
