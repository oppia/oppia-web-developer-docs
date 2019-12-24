There are two coverage checks currently in our code-base:
1. **Code-Climate**: 
* These are the required checks and the failure of these checks would mean the PR is decreasing coverage.
* They provide coverage only for backend.
2. **Codecov**:
* These checks are not required and are only used to generate coverage reports in form of Codecov comments. Hence, the contributor should not worry if the codecov coverage checks are failing (though the code-climate checks should be passing).
* They provide coverage for frontend tests only.

The checks provided by each service (code-climate and codecov) are:
1. **total-coverage(code-climate) or project(codecov)**: This ensures that the absolute coverage of the code-base does not decrease.
2. **diff-coverage(code-climate) or patch(codecov)**: This ensures the PR is fully tested, i.e it will run coverage only on the changed/added lines.

**What to do if code-climate checks are not reporting?** 

The answer is to first look at the backend tests results.

If there are **any** backend test errors, no coverage report will be produced. Please fix those errors and push again.

If there are no backend test errors, the issue is with the coverage not at 100%. In the backend test section, scroll down to the section that looks like:

```
Name                                                                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------------------------------------------
appengine_config.py                                                                 23      0   100%
constants.py                                                                        20      0   100%
core/controllers/acl_decorators.py                                                 686      0   100%
core/controllers/admin.py                                                          304      0   100%
core/controllers/base.py                                                           258      0   100%
core/controllers/classifier.py                                                      79      0   100%
core/controllers/classroom.py                                                       39      0   100%
```

Find the file that does not have 100% cover and look at the Missing column for lines that are missing coverage.