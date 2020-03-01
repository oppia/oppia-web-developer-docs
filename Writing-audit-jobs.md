Audit jobs are a type of one-off jobs that are to be run in production in order to investigate/modify certain aspects of entities like explorations, collections, interactions, topics, stories, questions, skills, etc. Now, as the dataset can be enormous, we use a MapReduce job to perform such audits, efficiently.

The following instructions describe how to write a one-off MapReduce job to audit entities.

## Steps to follow while writing audit jobs

 1. Depending on the entity you’re going to be working on, you’ll write your audit job in the corresponding *_jobs_one_off.py file. (for eg, exp_jobs_one_off.py has all one-off jobs that operate on explorations).
 2. The job will usually comprise of 3 functions:
	 - `entity_classes_to_map_over`: This function should return a list of datastore class references to map over. These can be imported from models registry in core/platform.
	 - `map`: Here you need to implement the map function for this job. This function would take in the entity that needs to be audited, *_model (for eg, exploration_model) and state what operations need to be performed on that entity. Based on the necessary conditions, this function should return a generator (with `yield`) that can then be reduced to form the final output.
	 - `reduce`: This function should aggregate all the mapped results into an output with the required format.
 3. The tests for the job should be written in the *_jobs_one_off_test.py. The tests should at least have functions that would validate that the job runs only for the desired entities and that the job does not run for deleted entities. Beyond this, you may have to add more tests based on your particular use-case.
 4. Lastly, add an entry to core/jobs_registry to mention the new job that you wrote.

After writing the job with appropriate tests, follow instructions [here](https://github.com/oppia/oppia/wiki/Running-jobs-in-production) in order to run your job in production.

For reference, let’s walk through one example. Consider [this](https://github.com/oppia/oppia/blob/5eda7cd1bab85730e4feefbd5833ba19329c0979/core/domain/exp_jobs_one_off.py#L338) Audit Job which outputs a list of private explorations that are viewable. Following the aforementioned steps, notice that 3 functions have been implemented. Let’s take a brief overview of each of them.

 - `entity_classes_to_map_over`: This returns a list of datastore class references containing the exploration model.
 - `map`: This function takes in an “item” which is the exploration_model that needs to be operated upon. Here, the condition for privacy and viewability is checked, and if the condition is matched, that particular exploration’s id and title are generated.
 - `reduce`: The reduce function here, simply aggregates the mapped generations and returns (id, title) pairs of the explorations that are private, yet viewable.

Now, let’s take a look at the tests for this job, [here](https://github.com/oppia/oppia/blob/5eda7cd1bab85730e4feefbd5833ba19329c0979/core/domain/exp_jobs_one_off_test.py#L1389).

After setting up with dummy values for email, username, exploration ids, and titles, 3 kinds of tests have been written.

 - `test_output_contains_only_viewable_private_explorations`: This tests if the job outputs only viewable explorations. The way this works is, dummy explorations are created and then the job is run on these explorations. An instance of the job is created by calling the create_new() method, which returns a job_id, which is then enqueued and eventually processed. In this case, two explorations are created. One is private and viewable and the other is not. The job is run on both explorations. A null output is expected from the 2nd exploration and an (id, title) pair is expected from the job when it’s run on the 1st exploration.
 - `test_no_action_is_performed_when_exploration_rights_is_none`: Similar procedure as mentioned above with the sample exploration being private and viewable but the exploration rights model is deleted. So the output of the job should yield an empty list.
 - `test_no_action_is_performed_for_deleted_exploration`: Here a sample exploration, private and viewable, is created and then deleted. A generic function to test that the job yields empty output for deleted explorations, run_job_for_deleted_exp, is run on that exploration.
