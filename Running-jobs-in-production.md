# Instructions for getting jobs into production

## Running your job on the test server

Before a MapReduce job can be run in production, it must first be tested on the Oppia test server.

In order to test a job, please submit a request using [this form](https://goo.gl/forms/XIj00RJ2h5L55XzU2). Before submitting a testing request, please ensure that the job has already been tested manually on your local machine, passed code review, and been merged into develop.

### Requirements for running a job in production

**Important**: If your job is not essential for the release and has not been fully tested by the release cut, then it is not going into the release. "Fully tested" means:
- The job should run without failures on oppiatestserver.
- The job produces the expected output.
- The job has the expected outcome (this must be verified by e.g. user-facing changes, or introspection of the datastore, or a validation job, or an output check, etc.).

## Submitting a job to production

Once your job has been fully tested on oppiatestserver, please submit a request using [this form](https://goo.gl/forms/6pNveYNJat9nSBRm1) to get it run on the main production server. Requests must be in by the [date of the relevant release cutoff](https://github.com/oppia/oppia/wiki/Release-Schedule), which is typically the first Saturday of the corresponding month.

You can check the status of your job in [this spreadsheet](https://docs.google.com/spreadsheets/d/1PAVWMxu7w-tOuJEzbixHRQL4GO34uHggbgQCcH1AXJg/edit#gid=0). Only release coordinators and QA leads will have edit access. If you see that something is wrong, please leave a comment on the spreadsheet, or send an email to oppia-release-team@googlegroups.com . 