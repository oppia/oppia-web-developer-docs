## Requirements

Before a job or feature that cannot be fully tested locally can be run and deployed in production, it must first be tested on the Oppia backup server. Examples of features that require backup server testing are features that add or modify code that requires some third-party API, like Cloud Tasks, Cloud Storage, or Cloud Translate.

If your job or feature is not essential for the release and has not been fully tested by the release cut, then it is not going into the release. "Fully tested" means:
- The job or feature should run without failures on the Oppia backup server.
- The job or feature produces the expected output.
- The job or feature has the expected outcome (this must be verified by e.g. user-facing changes, or introspection of the datastore, or a validation job, or an output check, etc.).
- The job or feature should be explicitly approved by server jobs admin (currently @seanlip,  @vojtechjelinek, @kevintab95 and @DubeySandeep).

Also, in case your job is a new migration job (not an already existing migrations), there has to be an audit job accompanying it to verify that the data that you are migrating is valid in the server. **The audit job will have to be "Fully tested" before testing on the migration job can start.** 

In case there is invalid data observed, either your migration job should fix it programmatically, or the corresponding data has to be manually fixed before the migration job can be run. This is valid for both testing in the backup server and running in production.

## Instructions

### Writing your job

All jobs must adhere to the following requirements before they can be run on the test server:
- In the "success" case, the job should yield aggregate output (like the total number of files migrated).
- In all possible "failure" cases, the job should yield debug/error output (like the ID of an exploration that couldn't be migrated and the reason why).
- There must be automated backend tests in the codebase for both the success and failure cases.
- There should be a Google Doc with clear instructions on what the server jobs admin needs to do, including:
  - Additional steps that need to be taken in order to verify whether the job has succeeded or failed (such as manual testing, runs of validation jobs, inspection of datastore, checks of error logs, checks of job output, etc.)
  - The expected job output for both the pass/fail cases
  - What the server jobs admin should do with any output produced by the job
  - What the server jobs admin should do if the job run fails midway, both in terms of how to recover from the run (e.g. by running a job to delete all instances of a newly-created model class, etc.) and how to debug the job (e.g. do other jobs need to be run to provide additional information, is there error output that can be manually investigated, etc.)

### Submitting a PR with a new job or feature that requires third-party API

**If a PR introduces a new job(s) or feature(s) that requires third-party API, it can be merged only after it is tested on the backup server.** The author of the PR should submit a request using [this form](https://goo.gl/forms/XIj00RJ2h5L55XzU2) after the job is approved by all reviewers except the server admins (admins will only approve after the job or feature is verified to be working). 
> **Note**
> Please submit just a single request if multiple jobs need to be run in succession. 

The form responses go to the server jobs admins and the admins should respond to the contributor within 24 hours. The server jobs admin will send updates after running the job(s) to the job author and [oppia release team](oppia-release-team@googlegroups.com). If the job(s) runs successfully, the admin will approve the job(s) in the corresponding [spreadsheet row](https://docs.google.com/spreadsheets/d/1Wegd0rZhVOm3Q3VCIw0xMbLC7IWtRyrEahiPn61Fhoo/edit#gid=948463314&range=S:S) as well as merge the PR which introduces the job. 

> **Warning**
> Before submitting a testing request, please ensure that the job has already been tested manually on your local machine, and that all CI checks are passing in your PR on GitHub. For an existing job, make sure that you test the job locally and specify clearly, in the form, why you want to run the job.

If you are hoping to run your job in a particular release, please plan your work schedule appropriately so that you get the testing completed in time for that release. Jobs must have completed a successful run on the backup server before the [date of the relevant release cutoff](https://github.com/oppia/oppia/wiki/Release-Schedule), which is typically the first Saturday of the corresponding month.

In general, we advise doing testing on your own App Engine instance beforehand. (App Engine has a [free tier](https://cloud.google.com/free/docs/always-free-usage-limits#gae_name) that you can use for this.)

You can check the status of your job in [this spreadsheet](https://docs.google.com/spreadsheets/d/1Wegd0rZhVOm3Q3VCIw0xMbLC7IWtRyrEahiPn61Fhoo/edit). Only release coordinators and QA leads will have edit access. If you see that something is wrong, please leave a comment on the spreadsheet, or send an email to oppia-release-team@googlegroups.com . 

If you have any questions about the above or if you do not get any update within 24 hours, please send an email to oppia-release-team@googlegroups.com .

### What to do if your job or feature that requires third-party API is not approved?

* If your job or feature that requires third-party API is not approved, you will get an email from the server jobs admin explaining what went wrong. 
* You should fix the error and create a new request for running the job or feature that requires third-party API in [this form](https://goo.gl/forms/XIj00RJ2h5L55XzU2). Make sure to fill the section about what got fixed. (Note that, after previously filling out the form, you would have received an email with your form submissions; you might find this email useful as a reference.)
