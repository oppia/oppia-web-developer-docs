## Requirements

Before a MapReduce job can be run in production, it must first be tested on the Oppia backup server.

If your job is not essential for the release and has not been fully tested by the release cut, then it is not going into the release. "Fully tested" means:
- The job should run without failures on the Oppia backup server.
- The job produces the expected output.
- The job has the expected outcome (this must be verified by e.g. user-facing changes, or introspection of the datastore, or a validation job, or an output check, etc.).
- The job should be explicitly approved by server jobs admin (currently @seanlip).

## Instructions

### Writing your job

All jobs must adhere to the following requirements before they can be run on the test server:
- In the "success" case, the job should yield aggregate output (like the total number of files migrated).
- In all possible "failure" cases, the job should yield debug/error output (like the ID of an exploration that couldn't be migrated and the reason why).
- There must be automated backend tests in the codebase for both the success and failure cases.
- There should be a Google Doc with clear instructions on what the release coordinator needs to do, including:
  - Additional steps that need to be taken in order to verify whether the job has succeeded or failed (such as manual testing, runs of validation jobs, inspection of datastore, checks of error logs, checks of job output, etc.)
  - The expected job output for both the pass/fail cases
  - What the release coordinator should do with any output produced by the job
  - What the release coordinator should do if the job run fails midway, both in terms of how to recover from the run (e.g. by running a job to delete all instances of a newly-created model class, etc.) and how to debug the job (e.g. do other jobs need to be run to provide additional information, is there error output that can be manually investigated, etc.)

### Submitting a PR with a new job

If a PR introduces a new job, it can be merged only after it is tested on the backup server. The author of the PR should submit a request using [this form](https://goo.gl/forms/XIj00RJ2h5L55XzU2) as soon as the PR is approved by all the reviewers. The form responses should go to the server jobs admin (currently **@seanlip**) and the admin should run the job and respond to the contributor within 48 hours. The server jobs admin should send updates after running the job to the job author and [oppia release team](oppia-release-team@googlegroups.com). If the job runs successfully, the admin should approve the job for release in the corresponding [spreadsheet row](https://docs.google.com/spreadsheets/d/1Wegd0rZhVOm3Q3VCIw0xMbLC7IWtRyrEahiPn61Fhoo/edit#gid=948463314&range=S:S) as well as merge the PR which introduces the job. 

**Note**: If you do not get any update within 48 hours, please send a mail to oppia-release-team@googlegroups.com with a link to your job.

### Running your job on the backup server (and possibly in production)

In order to test a job, please submit a request using [this form](https://goo.gl/forms/XIj00RJ2h5L55XzU2). Before submitting a testing request, please ensure that the job has already been tested manually on your local machine, passed code review, and been merged into develop.  For an existing job, make sure that you test the job locally and specify clearly in the form that why you want to run the job.

If you are hoping to run your job in a particular release, please plan your work schedule appropriately so that you get the testing completed in time for that release. Jobs must have completed a successful run on the backup server before the [date of the relevant release cutoff](https://github.com/oppia/oppia/wiki/Release-Schedule), which is typically the first Saturday of the corresponding month. Note backup test server jobs will be run on Weekends. (More specifically, the release coordinator will run the job during the weekend after the job request is submitted, and results will come back within 24 hours after that.)

In general, we advise allowing 1-2 weeks for the backup server testing process, and doing testing on your own App Engine instance beforehand. (App Engine has a [free tier](https://cloud.google.com/free/docs/always-free-usage-limits#gae_name) that you can use for this.)

You can check the status of your job in [this spreadsheet](https://docs.google.com/spreadsheets/d/1Wegd0rZhVOm3Q3VCIw0xMbLC7IWtRyrEahiPn61Fhoo/edit). Only release coordinators and QA leads will have edit access. If you see that something is wrong, please leave a comment on the spreadsheet, or send an email to oppia-release-team@googlegroups.com . 

If you have any questions about the above, please send an email to oppia-release-team@googlegroups.com .