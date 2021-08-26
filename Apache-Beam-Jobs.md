[Apache Beam](https://beam.apache.org/) is used by Oppia to perform large-scale
datastore operations. There are two types of operations:
-   **Batch**: Operations that are designed to be executed _once_ on the
    "current state" of the datastore.

    Examples:
    -   Count the # of models in the datastore
    -   Update the StringProperty values of all models with a specific kind
    -   Validate the relationships between models

-   **Continuous**: Operations that are designed to run _indefinitely_ by
    "reacting to updates" in the datastore.

    Examples:
    -   Updating the top `N` answers to a lesson
    -   Generating notifications for the events that users have subscribed to

If you're already familiar with Apache Beam, or are eager to start writing a new
job, then follow the [Quick Start](#quick-start).

Otherwise, if you're looking for supplemental material, you can read the entire
guide and fallback to the [Apache Beam Programming Guide][1] for more details.

Running Apache Beam Jobs
========================

Developer Environment
---------------------
![screencast of running jobs](https://user-images.githubusercontent.com/5094060/128743997-70cca5f9-0b76-4294-806e-f65f5df5be95.gif)
1. Sign in as an administrator ([instructions][3])
2. Navigate to **Admin Page > Roles Tab**
3. Add the "Release Coordinator" role to the username you are signed in with
4. Navigate to http://localhost:8181/release-coordinator, then to the **Beam Jobs tab**
5. Search for your job and then click the **Play button**

Apache Beam Job Architecture
============================

Jobs are composed of the following components:
-   [`Pipeline`s](#pipelines)
-   [`PValue`s](#pvalues)
-   [`PTransform`s](#ptransforms)
-   [`Runner`s](#runners)

## `Pipeline`s

`Pipeline`s manage a "DAG"
([directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph))
of `PValue`s and the `PTransform`s that compute them. Conceptually, `PValue`s
are the DAG's nodes and `PTransform`s are the edges.

For example:

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

Or, the equivalent Oppia code:

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

## `PValue`s

`PCollection`s are the primary input and output `PValue`s used by `PTransform`s.
They are a kind of `PValue` that represent a dataset of (virtually) any size,
including unbounded/continuous datasets.

`PBegin` and `PEnd` are "terminal" values that signal that an operation cannot
produce it or act upon it, respectively.

A `Pipeline` object is the best example of a `PBegin`, and the output of a write
operation is the best example of a `PEnd`.

## `PTransform`s

### `ParDo` and `DoFn`
`DoFn`s are the most-basic unit, and are invoked on elements of a `PCollection`
using `beam.ParDo`. It is analogous to the following code:

```python
do_fn = DoFn()
for value in pcoll:
    # NOTE: We don't use the return values directly. However, it's possible for
    # the DoFn to hold onto state in more advanced implementations.
    do_fn(value)
```

### `Map` and `FlatMap`
`beam.Map` is an operation that transforms each item in a `PCollection` into a
new value using a plain-old function. It is analogous to the following code:

```python
new_pcoll = []
for value in pcoll:
    new_pcoll.append(fn(value))
return new_pcoll
```

`beam.FlatMap` is a similar transformation, but it _flattens_ the output
`PCollection` into a single output `PCollection`. It is analogous to the
following code:

```python
new_pcoll = []
for value in pcoll:
    for sub_value in fn(value):
        new_pcoll.append(sub_value)
return new_pcoll
```

### `Filter`
`beam.Filter` reduces the elements of a `PCollection` into elements that have
returned True from a specified function. It is analogous to the following code:

```python
new_pcoll = []
for value in pcoll:
    if fn(value):
        new_pcoll.append(value)
return new_pcoll
```

### `GroupByKey`
`beam.GroupByKey` is useful when you need to perform an operation on elements
that share a common property. It is analogous to the following code:

```python
groups = collections.defaultdict(lambda: collections.defaultdict(list))
for i, pcoll in enumerate(pcolls_to_group):
    # NOTE: Each PCollection must have (key, value) pairs as elements.
    for key, value in pcoll:
        # Items from each PCollection are grouped under the same key, and
        # bucketed into their corresponding index.
        groups[key][i].append(value)
return groups
```

For example, in our validation jobs we compute two `PCollection`s:

```python
# Tuples of (ModelKey, True) for each model in the datastore that exists.
existing_models_pcoll = ...
# Tuples of (ModelKey, str) for each error message that should be reported when
# the corresponding model instance does not exist.
errors_if_missing_pcoll = ...
```

To generate a report, we use `GroupByKey` to pair the messages to the existing
models.

After this step, we can filter out the pairs where a model existed and report
the errors that are left over.

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

## `Runner`s

`Runner`s provide the run() method used to visit every node (`PValue`) in the
pipeline's DAG by executing the edges (`PTransform`s) to compute their values.
At Oppia, we use `DataflowRunner` to have our `Pipeline`s run on the Google
Cloud Dataflow service: https://cloud.google.com/dataflow.

High-level Guidelines
---------------------

-   **TL;DR**: Inherit from `base_jobs.JobBase` and override the `run()` method.

-   The `run()` method must return a `PCollection` of `JobRunResult` instances.
    -   In English, this means that **the job _must_ report _something_ about
        what was done during its execution.** This can be the errors it
        discovered, or the number of successful operations it was able to
        perform.
    -   Regardless of your needs, **jobs _must_ report _something_; empty
        results are forbidden!**
        -   If you don't think your job has any results worth reporting, then
            just print a "Success" metric with the number of models it
            processed.
    -   `JobRunResult` outputs should answer the following questions:
        -   Did the job run without any problems? How and why do I know?
        -   How much work did the job manage to do?
        -   If the job encountered a problem, what caused it?

-   When writing new jobs, prefer splitting boilerplate into new, small, and
    simple `PTransform` subclasses. Then, after unit testing them, combine them
    liberally in your job's `run()` method.
    -   Keep the job class and the `PTransform`s it uses in the same file,
        unless you plan on reusing them in future jobs. If you _do_ plan on
        reusing the job, then ask your reviewer for guidance on how to organize
        it.

-   Never modify input values. If you need to make changes to an input value,
    then [clone it first][2].

Quick Start
===========

The quick start is split into case studies of increasing complexity. Study the
one that best suits your needs.

If none of them help you implement your job, you may request a new one by adding
a comment to [#13190](https://github.com/oppia/oppia/issues/13190) with answers
to the following questions:
-   Why do I want a new case study?
-   Why are the current case studies insufficient?
-   What answers would the "perfect" case study provide?

Then we'll start write a new Case Study to help you, and future contributors,
as soon as we can (brianrodri@ will always notify you of how long it'll take).

Case study: `CountAllModelsJob`
-------------------------------

**Difficulty:** Trivial

**Key Concepts:**
-   Fetching NDB models
-   Counting elements in a `PCollection`
-   Creating `JobRunResult` values
-   Job registration

---

We'll start by writing a boilerplate `PTransform` which accepts models as input,
and returns `(kind, #)` tuples (where `kind` is the name of the model's class,
as a string).

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

Next, we'll write the job which applies the `PTransform` to every model in the
datastore. We can keep both of their implementations in the same file, since
they are so tightly coupled. Unit tests can focus on one or the other.

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

Case Study: `SchemaMigrationJob`
------------------------------

**Difficulty:** Medium

**Key Concepts:**
-   Getting and Putting NDB models
-   Partitioning one `PCollection` into many `PCollection`s.
-   Returning variable outputs from a `DoFn`

---

Let's start by listing the specification of a schema migration job:

-   The schema version of a model is in the closed range `[1, N]`, where `N` is
    the latest version.
-   All migration functions are implemented in terms of taking `n` to `n + 1`.
-   Models should only be put into storage after successfully migrating to v`N`.
-   Models that were already at v`N` should be reported separately.

A recursive function seems like an intuitive fit for this type of operation, so
let's workout what a diagram would look like in terms of
`migrate_to_next_version`.

> NOTE: In practice, an iterative approach would be more efficient. However,
> this code is concerned with teaching you how to use advanced Apache Beam
> constructs, so we'll go with the more-complicated approach against better
> judgment.
>
> In practice, finding the best patterns on your own will become easier as you
> gain experience writing jobs and working with "Functional Programming" in
> general.

> TIP: Often, when jobs are relatively complicated, it's helpful to begin by
> sketching a diagram of what you want the job to do. I recommend using pen and
> paper or a whiteboard, but in this Wiki Page we use ASCII art to keep the
> document self-contained.

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

> TIP: You don't need to know what the names of the `PTransform`s (edges) used
> in a diagram are. It's easy to look up the "perfect match" after drawing it.
>
> In this example, we could have easily replaced the edges with "plain-text"
> sentences without losing any generality.

There's a lot of complication in the outset, so let's make sure we use plenty of
`PTransform`s to write them. We'll start with the most interesting one: the loop
to migrate models to the next version.

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
> NOTE: This implementation won't work as-is, it's merely a scaffold of the key
> components we need to use to build out our diagram.



[1]: https://beam.apache.org/documentation/programming-guide/
[2]: https://github.com/oppia/oppia/blob/4d2f639869e57fbeaada414d923cae83eb0e082e/jobs/job_utils.py#L37-L63
[3]: https://github.com/oppia/oppia/wiki/Firebase-authentication#creating-an-administrator-account