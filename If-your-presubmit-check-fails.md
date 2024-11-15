### How the presubmit checks work

When you commit code changes or push to GitHub, we have certain checks that run on your changes to verify that everything is in order. If these checks fail, you must fix the errors **before** pushing your code. Do not bypass them, otherwise your code will fail checks on GitHub and this will delay the code review process.

Typically, these checks are for small things, like missing a space or a newline, using an invalid keyword, or missing docstrings. They might also fail due to [insufficient test coverage](https://github.com/oppia/oppia/wiki/Frontend-tests#generating-coverage-reports). They should be straightforward to fix, after looking at the logs to see what caused the failure.

If the tests fail, you'll see the following in your terminal:

```
--------------------
Checks Not Passed.
--------------------
```

To see the reason for the failing tests, **scroll up** in your terminal, and read and understand the logs to figure out what caused the failure. After fixing the issues, make another commit (or use `git add .` and then `git commit --amend`) to stage your changes before trying to re-push to GitHub.

### Examples

Here are some examples for how to fix a presubmit failure:

**1.**
```
Users/apple/codebase/opensource/oppia/core/templates/services/assets-backend-api.service.spec.ts
   46:1  error  This line has a length of 85. Maximum allowed is 80  max-len
```
Here, in the file **assets-backend-api.service.spec.ts**, the error is at line number **46**. The issue is that the line has exceeded the max length of 80. So to fix that, this line needs to be broken down into two lines.

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

Here, the `fdescribe` needs to be changed to `describe`. So, you would find line 30 in the given file, and change it from:

```
fdescribe('Assets Backend API Service', () => {
```

to this instead:
```
describe('Assets Backend API Service', () => {
```
