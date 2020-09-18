Sometimes, things go wrong while programming, and the reason for that is not obvious! In order to figure out what's happening, you will need to **debug** the code. This is an important skill to learn, but not an easy one to teach. On this page, we present a few examples of "debugging stories" from team members, so that you can see how other people approach tricky problems in the codebase.

_Oppia contributors: If you have other cool debugging stories to share, please feel free to add them below!_

## Google App Engine SDK Upgrade
_Contributed by Kevin Zhang_ (**@kevjumba**)

The context for this story arose when I was migrating our memcache usage to MemoryStore as part of a larger migration to the Python 3 version of App Engine. Before the migration, we were using a deprecated version of the Google App Engine (GAE) SDK, which resided in its standalone package: 'google_appengine_1.9.67'. Separately, we had installed the Google Cloud SDK in a different folder, so that we could use its 'gcloud' command line interface (CLI) utility.

However, times have changed, and Google no longer supports a standalone GAE package. Instead, the newest version of the GAE SDK is packaged within the latest version of the Google Cloud SDK. Moreover, I needed a 'VPC access connector' for the migration, and only the latest version of the GAE SDK included that.

So, I needed to update the way we use and install the GAE SDK by migrating away from the standalone package, and instead use the newest version of the Google Cloud SDK for all GAE-related operations. Unfortunately, during this upgrade, I encountered multiple errors related to incompatibilities with our old usage, detailed below. But first, some background:

### Background
1. The top level 'Google Cloud SDK' folder will be referred to as the **root** folder.
2. The `dev_appserver.py` script is a special python script provided by the Google App Engine package that allows us to start our own local development server. In the standalone Google App Engine package, `dev_appserver.py` resided in the top level directory. However, the Google Cloud SDK added a new version of the `dev_appserver.py` file in a bin folder under the **root** folder, namely `root/bin/`.
3. Oppia uses CircleCI. This software allocates certain instances of a Ubuntu VM to us so we can run tests on their Ubuntu instances whenever a PR is updated or created.

### Migration Process
1. I first replaced all the old usages of 'dev_appserver.py' with usage of the newer Google Cloud SDK version.

2. The normal development server started fine. I tested some functionality on the development server and nothing seemed out of the ordinary. However, after I submitted a PR, the CircleCI e2e tests started failing. When the dev app server tried to start on the CircleCI build, the build errored out with the message: "Permission Denied". Unfortunately, this error wasn't reproducible on my local machine and there was no indication of why the Circle CI Ubuntu instance would be different than my own UNIX instance.
   - **Initial Local Debugging:** After perusing the stack-trace, I discovered a reference to a subprocess call nested within the Google App Engine source code. The call executed a command `python -c import grpc`. Basically, this command tries to import the grpc library -- a library included in the Google Cloud SDK folder -- through the command line.
       - Furthermore, while reading the App Engine source code, I realized that the `dev_appserver.py` script in the **root** folder actually points to a `dev_appserver.py` script that was nested further within the Cloud SDK folder. At the time, I didn't realize the importance of this fact.
   - **Circle CI Instance Debugging:** In an attempt to fix the 'Permission Denied' bug, I checked out another branch on top of mine so that I could perform quick tests in the CircleCI environment by pushing new commits. To help this move faster, I temporarily deleted all the '.github/workflows' yaml configuration files, except for the '.circleci/config.yml' file that controls the tests that are run on the CircleCI instance. I edited this file so that it would only run a simple test, to enable me to debug this error using quick iterations on the CircleCI build.
       - First, I tried running `chmod -R 777` on the entire directory, but this didn't change the error message.
       - Next, I added a `subprocess` command to print out the relevant file permissions right before the development server is started, and compared this output to the permissions on my own computer. Python's default import functionality looks for the `__init__.py` file in a directory, and then checks for the specific folder to import (in this case, `grpc`). Unfortunately, the permissions on the CI instance for those specific folders/files exactly matched the ones on my local machine, which was enough evidence to confirm that file permissions weren't the issue.
       - Since the permissions seemed to match, I added `sudo` to the command to start the dev server, as a test to see whether using a root user would help. This did not change the error, therefore ruling out the possibility of a user-access bug.
      - I decided that my debugging cycles were too slow at this point, so I researched how to ssh into the CI instance for more efficient debugging. The steps to do this are as follows:
            1. Rerun a job with the button "Rerun job with SSH" on the top-right of the circle CI console.
            2. After the job finishes, expand the tab at the bottom labeled, "Enable SSH". It should provide you with details to log in to the CircleCI instance's terminal.
     - I logged into the SSH instance and tried a variety of tests.
        - I tried importing 'grpc' from the command line which resulted in the error: `ImportError: grpc/_cython/cygrpc.so: undefined symbol: PyUnicodeUCS2_DecodeLatin1`. This error is due to the fact that the Circle CI instance runs a default Python version that uses 4-character unicode. However, the included version of `grpc` was compiled using a 2-character unicode format, so the compilations don't match. I did research on whether it was possible to build CircleCI’s python docker image with a different unicode setting, but there were no known solutions to this issue.
        - I tried resetting the entire Google App Engine directory with 'chmod -R 777', just to confirm that user privileges were the issue (they were not).
        - I tried running the `dev_appserver.py` script from the terminal and got the same error.
        - Neither of these possible solutions worked, so I postulated that it's possible we weren't supposed to actually run the `dev_appserver.py` from the **root** directory in the way that we did. 

   - **Arriving at the Solution:** I remembered, from earlier, that the **root** folder 'dev_appserver.py' script actually calls a nested `dev_appserver.py` script, so I went to investigate what exactly that script did. From reading the contents, it seemed like this script provided most of the functionality that our app needed. So, I changed all of the paths to point the nested python script instead, and tried running the e2e tests. Thankfully, it finally started the development server, and the tests started running and passing!


## Speeding Up Frontend Tests
_Contributed by Kevin Thomas_ (**@kevintab95**)

Around the second week of March 2020, Oppia devs reported that the frontend tests were taking too long to complete execution. The issue was investigated and fixed in [PR #8864](https://github.com/oppia/oppia/pull/8864). This writeup details the process behind the fix.

Initial inspection of the console output revealed that the "build" part of the test script took a considerable amount of time to complete, compared to the execution of the tests. However, the build process is expected to take time because all the test files need to be bundled into a large file, and the webpack build process is known to be slow. So in order to speed up the script, I figured that I would need to speed up the actual tests.

The output provided in the terminal seemed insufficient for debugging. So, to get a more verbose output and to be able to use more advanced tools, I changed the following settings in karma.conf.ts:

<p align="center"><img width="600px" src="https://user-images.githubusercontent.com/11008603/91498050-b710c480-e8dc-11ea-87e9-74c95978c2ed.png" /></p>

I also set "browser" to Chrome instead of headless Chrome, and "singleRun" to false so that the browser remains open after the tests complete execution. Running the tests on Chrome browser would allow me to leverage the built-in devtools for debugging purposes.

Running the test with these settings opened up the Chrome browser:

<p align="center"><img width="600px" src="https://user-images.githubusercontent.com/11008603/91498453-68175f00-e8dd-11ea-9452-980604768abc.gif" /></p>

To allow debugging, I enabled “DEBUG” mode by clicking on the debug button, as seen in the image above.

This showed that, in the console tab, a significant number of “response errors” were logged.

<p align="center"><img width="400px" src="https://user-images.githubusercontent.com/11008603/91498552-92691c80-e8dd-11ea-8217-94765c400906.png" /></p>

These errors occur because spec files which mock backend calls may expect resolved/rejected responses. So what could be investigated was to check whether there were any bottlenecks when those errors are logged.

The standard way to identify performance bottlenecks is to use the built-in Javascript Profiler. Once the test started to execute, I fired up devtools and used a JavaScript profiling tool to record a small segment of the test execution (e.g. 10-20 seconds).

<p align="center"><img width="600px" src="https://user-images.githubusercontent.com/11008603/91498651-c6dcd880-e8dd-11ea-929f-2fddcc0963f1.gif" /></p>

I then stopped the recording after 10-20s and exported the result as a JSON file, and stopped the remainder of the test script. I then uploaded the captured JS profile in a new browser instance.

<p align="center"><img width="600px" src="https://user-images.githubusercontent.com/11008603/91498725-ed027880-e8dd-11ea-9484-07ba6dec06c6.gif" /></p>

Searching for “responseError” in the loaded profile showed a large number of results. 

<p align="center"><img width="800px" src="https://user-images.githubusercontent.com/11008603/91498828-19b69000-e8de-11ea-85dd-7cffd82ca3a9.png" /></p>

Zooming into a few of the results indicated that the "mapStacktrace" operation was executed for every "responseError" call. Although the operation seemed to take only a short time to execute (~5ms), this seemed like a potential bottleneck because of the frequency of its occurrence, especially when it could be avoided altogether. It is an expensive operation to map the stack trace info of the bundled code to that of the individual files and, since tests are run in DEV mode, this operation seemed unnecessary.

<p align="center"><img width="800px" src="https://user-images.githubusercontent.com/11008603/91498863-2935d900-e8de-11ea-8f2a-308f83024081.png" /></p>

As a fix, I added a check to ensure that the "mapStacktrace" operation only executes if DEV_MODE is false. Subsequent test runs with this fix indicated a significant decrease in the runtime (~by half, from 8m to 4m)!

<p align="center"><img src="https://user-images.githubusercontent.com/11008603/91499014-60a48580-e8de-11ea-89c0-bda7b4e52478.png" /></p>
