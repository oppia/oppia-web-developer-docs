_Note: If you're writing a new one-off job that needs to be run in production, please see the ["Running Jobs in Production" wiki page](https://github.com/oppia/oppia/wiki/Running-jobs-in-production) in order to understand how the deployment procedure works._

## Follow the steps below to write a new one-off job:
1. Add a new class to the `<domain-name>_jobs_one_off.py` file (Create one if it doesn't exist.)
2. Find the model which you want to map over.
3. Add `entity_classes_to_map_over` `@classmethod` which returns a list of the model you want to map over.
4. Create a static method `map` in the newly created one-off job class which will receive a model as an arg.
5. Write the job you want to perform on a model in the `map` static method, `yield` a tuple of `key and value` to log any information you want from the job like success or failure log, etc.
6. Add a `reduce` static method which will receive the `yield` produced by the `map` class after calling this method on a model. Anything you yield in the method will be logged as a report from the one-off job. (See existing one-off jobs for more info.)
7. Add your one-off job class in the [ONE_OFF_JOB_MANAGER list](https://github.com/oppia/oppia/blob/develop/core/jobs_registry.py#L44) of jobs_registry.py file.
8. Make sure to test the one-off job manually. (You can follow [these steps](https://github.com/oppia/oppia/wiki/Running-Jobs-on-Dev-Server) to test a one-off job through the admin page.)
9. If your one-off job is too slow or running on small number of model types (classes) you can try to increase the number of shards, for that you need to override the `enqueue` `@classmethod` and set the `shard_count` to some higher number (default is 8). Increasing the number too much can also break the one-off job, so you need to test it even after changing just the `shard_count`.

## Example of an one-off job:
```

class InteractionAuditOneOffJob(jobs.BaseMapReduceOneOffJobManager):
    """Job that produces a list of (exploration, state) pairs, grouped by the
    interaction they use.
    """

	@classmethod
    def enqueue(cls, job_id, additional_job_params=None):
        super(InteractionAuditOneOffJob, cls).enqueue(
			job_id, shard_count=64)

    @classmethod
    def entity_classes_to_map_over(cls):
        return [exp_models.ExplorationModel]

    @staticmethod
    def map(item):
        if item.deleted:
            return

        exploration = exp_fetchers.get_exploration_from_model(item)
        for state_name, state in exploration.states.items():
            exp_and_state_key = '%s %s' % (item.id, state_name)
            yield (state.interaction.id, exp_and_state_key)

    @staticmethod
    def reduce(key, values):
        yield (key, values)
```