While committing or pushing the changes in the code that you made, we have certain checks and tests in place that run on your changes and verify that everything is in order and good to go. So in a lot of cases you'll be unable to push your code because your changes are failing our tests and require some changes to be made. They can fail for reasons as simple as like missing a space or missing a Whiteline, or using an invalid keyword, or missing docstrings.

These tests are triggered automatically when you try to commit or push your changes, but you can trigger these tests manually also by **python -m scripts.pre_commit_linter.**

If the tests fail, you'll have this in your console.

```
--------------------
Checks Not Passed.
--------------------
```

Debugging:
Now, the reason that the tests are failing is also present in the console and are pretty straight forward to read, understand and fix. Scroll up and find the error log.

**Examples:**

**1.**
```
Users/apple/codebase/opensource/oppia/core/templates/dev/head/services/assets-backend-api.service.spec.ts
   46:1  error  This line has a length of 85. Maximum allowed is 80  max-len
```
Here, in the file **assets-backend-api.service.spec.ts**, the error is at line number **46** and the error is that the line has exceeded the max length of 80. So to fix that, this line needs to be broken down into two lines.
So I'll change this
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
core/templates/dev/head/services/assets-backend-api.service.spec.ts --> Line 30: In tests, please use 'describe' instead of 'ddescribe'or 'fdescribe'
```

Here, the fdescribe needs to be changed to describe.This
```
fdescribe('Assets Backend API Service', () => {
```
to, this
```
describe('Assets Backend API Service', () => {
```


