### How the presubmit checks work

While committing or pushing the changes in the code that you made, we have certain checks and tests in place that run on your changes and verify that everything is in order and good to go. This means that, sometimes, you'll be unable to push your code because your changes are failing our tests and require some changes to be made. They can fail for reasons as simple as like missing a space or missing a newline, or using an invalid keyword, or missing docstrings. They might also fail due to [insufficient test coverage](https://github.com/oppia/oppia/wiki/Frontend-unit-tests-guide#generating-coverage-reports).

These tests are triggered automatically when you try to commit or push your changes, but you can also trigger these tests manually by running the command **python -m scripts.pre_commit_linter.** (See the top of scripts/pre_commit_linter.py for instructions on command-line args you can use to customize this script.)

If the tests fail, you'll see the following in your terminal:

```
--------------------
Checks Not Passed.
--------------------
```

The reason for the failing tests will also be present in the console, and it should generally be fairly straightforward to read, understand and fix the errors. You may need to scroll up in order to see the full error log. After fixing the issues, make another commit (or use `git add` and then `git commit --amend`) to stage your changes before trying to re-push to GitHub.

**Important:** Please make sure to fix the errors *before* you push to GitHub. Do not bypass these checks, otherwise it will lead to delays in the code review process.


### Examples

**1.**
```
Users/apple/codebase/opensource/oppia/core/templates/services/assets-backend-api.service.spec.ts
   46:1  error  This line has a length of 85. Maximum allowed is 80  max-len
```
Here, in the file **assets-backend-api.service.spec.ts**, the error is at line number **46** and the error is that the line has exceeded the max length of 80. So to fix that, this line needs to be broken down into two lines.

So, you would change this
```
    fileDownloadRequestObjectFactory = TestBed.get(FileDownloadRequestObjectFactory);
```
to
```
    fileDownloadRequestObjectFactory = TestBed.get(
        FileDownloadRequestObjectFactory);
```
**2.**
```
core/templates/services/assets-backend-api.service.spec.ts --> Line 30: In tests, please use 'describe' instead of 'ddescribe'or 'fdescribe'
```

Here, the `fdescribe` needs to be changed to `describe`. You would find the relevant line of code in the file, and change this:

```
fdescribe('Assets Backend API Service', () => {
```

to this instead:
```
describe('Assets Backend API Service', () => {
```


