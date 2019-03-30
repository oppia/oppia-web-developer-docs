## Why would you want to run a Job on your dev server?
- If you are writing a Job yourself and want to test how would it work.
- If you are working on an issue related to a Job.
- If you are looking through the code of a Job and want to see what it does.

### Some examples of the one off jobs

* **Migration one off jobs** - These jobs are used for migrating from one schema version to other. If you are creating a new schema version for any model, make sure to run the migration job and check if the migration works as expected. One of the examples is `ExplorationMigrationJobManager` which is used for migration of explorations to the latest version.

* **Feedback Continuous Computation one off jobs** - These jobs are used for continuously computing feedback analytics and updating them. You can run these jobs when you are making changes to the feedback system and check if the analytics are computed and updated correctly.

* **Validation One off jobs** - These jobs can be used to validate the exploration data. One such example is the `ExplorationContentValidationJobForCKEditor` which validates if the html is in correct format for ckeditor. You can run this job to find invalid html content in an exploration which does not fit the ckeditor schema. Any validation job can be used to find the cases which violate the required schema.

* **Audit One off jobs** - These jobs can be used to audit various properties related to a model. One such example is `HintsAuditOneOffJob` which is used to find number of hints used in each state of an exploration. These jobs can be run if you need to audit any property associated with any model.

 
## How to run a Job on your dev server?
1.) Start the dev server and log in as admin.

![Login as admin](https://i.imgur.com/f7U0lTl.png)
![Enter your name](https://i.imgur.com/fLkBF7m.png)

2.) Hover over the user avatar and select the Admin Page.

![Hover over the avatar](https://i.imgur.com/XV43Piz.png)

3.) Select the Jobs tab and start it from the list. Note that your job will run on the explorations that are present on the server, the job is being run on. Say, if you are running on local host to check how your job is performing you need to have some explorations created on the local server. You could also take a look at the activites tab, there we have some already available explorations. You could just click on `reload` and that corresponding exploration will be made available on your server then (you could browse through your library and you'll see the particular exploration).

![Select the job](https://i.imgur.com/oj6mS6a.png)

## How to find what a Job does?
- go to `core/domain/`
- Find the file related to the Job and see its documentation to know what it does.