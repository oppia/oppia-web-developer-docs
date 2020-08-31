Sometimes, things go wrong while programming, and the reason for that is not obvious! In order to figure out what's happening, you will need to **debug** the code. This is an important skill to learn, but not an easy one to teach. On this page, we present a few examples of "debugging stories" from team members, so that you can see how other people approach tricky problems in the codebase.

## Google App Engine SDK Upgrade
_Contributed by Kevin Zhang_ (**@kevjumba**)

### Oppia's Previous Setup
Previously, in our setup for Google App Engine (GAE), we used a deprecated version of the Google App Engine SDK, which resided in its standalone package, namely, 'google_appengine_1.9.67'. In order to use the 'gcloud' command line interface (CLI) utility, we also had a separate download for the Google Cloud SDK.
 
### Primary Motivation
However, currently, Google no longer supports a standalone GAE package. Instead, the newest version of the GAE SDK is packaged within the latest version of the Google Cloud SDK. Moreover, the newest version of GAE SDK provides support for a 'VPC access connector' which is a requirement for one of my migrations. This forced me to update the way we use and install the GAE SDK by migrating away from the standalone package, but instead use the newest version of the Google Cloud SDK for all GAE related operations. Unfortunately during this upgrade, I encountered multiple errors related to incompatibilities with our old usage that I detail below.

### Background
1. The top level 'Google Cloud SDK' folder will be referred to as the **root** folder.
2. The 'dev_appserver.py' script is a special python script provided by the Google App Engine package that allows us to start our own local development server. In the standalone Google App Engine package, 'dev_appserver.py' resided in the top level directory. However, the Google Cloud SDK added a new version of the 'dev_appserver.py' file in a bin folder under the **root** folder, namely 'root/bin/'.
3. Oppia uses CircleCI. This software allocates certain instances of a Ubuntu VM to us so we can run tests on their Ubuntu instances whenever a PR is updated or created.

### Migration Process
1. I first replaced all of the old usages of 'dev_appserver.py' with usage of the newer Google Cloud SDK version.

2. The normal development server started fine. I tested some functionality on the development server and nothing seemed out of the ordinary. However, after making a pull request, Circle CI e2e tests started failing. When the dev app server tried to start on the Circle CI build, the build errored out with the error message: "Permission Denied". The problem was that this error refused to manifest on my local machine and there was no indication of why the Circle CI ubuntu instance would be different than my own UNIX instance.
   - After perusing the stack-trace, I was led to a reference to a subprocess call nested within the Google App Engine source code. The call was to execute a command `python -c import grpc` which was a python package included with the App Engine package. Essentially what this command does is attempt an import of the grpc library through the command line. 
       - Furthermore, I realized that the 'dev_appserver.py' script in the **root** folder actually points to a 'dev_appserver.py' script nested further inside the Cloud SDK folder.
   - In an attempt to fix the 'Permission Denied' bug, I checked out another branch on top of my branch so that I can perform quick tests on the CircleCI instance by pushing new commits. To help this along, I deleted all of the '.github/workflows' yaml files (configuration for the various github CI tests) except for the '.circleci/config.yml' file that controls the tests run on the Circle CI instance. I edited this file  so that it would only run a simple test so that I can debug the error in quick iterations on the Circle CI build.
       - I first tried to run `chmod -R 777` the entire directory but this didn’t change the error message.
       - I added a subprocess command to print out the relevant file permissions right before the development server is started and compared this output to the permissions on my own computer. Python default import functionality looks for the '__init__.py' file in a directory and then checks for the specific folder, in this case 'grpc' to import. The permissions on the CI instance for these specific folders/files were identical to the ones on my local machine which I took as enough evidence that file permissions don't seem to be the issue.
       - Since the permissions seemed to match, I changed the command to start the dev server using sudo as a test to see whether using a root user would help. This did not change the error, confirming for me that this 'Permission Denied' problem is not a user access issue but some other problem.
       - I decided that my debugging cycles were too slow to debug such a tricky problem so I researched how to ssh into the CI instance for more efficient debugging. The steps to do this are listed here:
            1. Rerun a job with the button "Rerun job with SSH" on the top right of the circle CI console.
            2. Expand the tab at the bottom labeled, "Enable SSH" after the job finishes. It should provide you with details to log in to the terminal.
     - I logged into the SSH instance and tried a variety of tests.
        - I tried importing 'grpc' from the command line which resulted in this error: "ImportError: grpc/_cython/cygrpc.so: undefined symbol: PyUnicodeUCS2_DecodeLatin1'. This error is due to the fact that the Circle CI instance runs a default Python version that uses 4-character unicode. However, the included version of 'grpc' was compiled using a 2-character unicode format so the compilations don’t match. I did research on whether it was possible to build CircleCI’s python docker image with a different unicode setting but there were no known solutions to this issue.
        - I tried resetting the entire directory of Google App Engine with 'chmod -R 777' just to make sure that user privileges were the issue (they were not).
        - I tried running the 'dev_appserver.py' script from the terminal and got the same error.
        - Neither of these possible solutions worked so I postulated that it's possible we aren't supposed to actually run the 'dev_appserver.py' from the **root** directory in the way that we did. 


   - I remembered from a previous discovery that the **root** folder 'dev_appserver.py' script actually calls a nested 'dev_appserver.py' script so I went to investigate what exactly that script does. From reading the contents, it seemed like this script provided most of the functionality that our app needed. I changed all of the paths to point the nested python script instead and tried running the e2e tests. Thankfully, it finally started the development server and started running the tests.

## Speeding Up Frontend Tests
_Contributed by Kevin Thomas_ (**@kevintab95**)

Around the 2nd week of March 2020, Oppia devs reported that the frontend tests were taking too long to complete execution. The issue was investigated and fixed in #8864. This document details the process behind the fix.

An initial inspection of the console output revealed that the “build” part of the test script took a considerable amount of time to complete compared to the execution of the tests. The build process is expected to take time because all the test files need to be bundled into a large file and it is known the webpack build process is slow. So in order to speed up the script, one would have to speed up the actual tests.

The output provided in the terminal seemed insufficient to debug. So, to get a more verbose output and to be able to use more advanced tools, the following settings in karma.conf.ts were changed:

<p align="center"><img width="600px" src="https://user-images.githubusercontent.com/11008603/91498050-b710c480-e8dc-11ea-87e9-74c95978c2ed.png" /></p>

The “browser” was set to Chrome instead of headless Chrome and “singleRun” was set to false so that the browser remains open after the tests complete execution. Running the tests on Chrome browser, will allow leveraging the built-in devtools for debugging purposes.

Running the test with these settings opens up the Chrome browser:

<p align="center"><img width="600px" src="https://user-images.githubusercontent.com/11008603/91498453-68175f00-e8dd-11ea-9452-980604768abc.gif" /></p>

To allow debugging, “DEBUG” mode is enabled by clicking on the debug button as seen in the image above.

In the console tab, a significant number of “response errors” were logged.

<p align="center"><img width="400px" src="https://user-images.githubusercontent.com/11008603/91498552-92691c80-e8dd-11ea-8217-94765c400906.png" /></p>

These errors occur because spec files mock backend calls may expect resolved/rejected responses. So what could be investigated was to check if there were any bottlenecks when these errors are logged. Standard way to identify performance bottlenecks is to use the  built-in Javascript Profiler.

Once the test has started to execute, devtools can be fired up and a javascript profiling tool can be used to record a small segment of the test execution (e.g. 10-20 seconds).

<p align="center"><img width="600px" src="https://user-images.githubusercontent.com/11008603/91498651-c6dcd880-e8dd-11ea-929f-2fddcc0963f1.gif" /></p>

The recording is stopped after 10-20s and the result is exported as a JSON and the remainder of the test script is stopped.

In a new browser instance, the captured JS profile is uploaded.

<p align="center"><img width="600px" src="https://user-images.githubusercontent.com/11008603/91498725-ed027880-e8dd-11ea-9484-07ba6dec06c6.gif" /></p>

Searching for “responseError” in the loaded profile, showed a large number of results. 

<p align="center"><img width="800px" src="https://user-images.githubusercontent.com/11008603/91498828-19b69000-e8de-11ea-85dd-7cffd82ca3a9.png" /></p>

Zooming into a few of the results indicated that the “mapStacktrace” operation was executed for every “responseError” call. Although the operation seemed to take only a short time to execute (~5ms), this seemed like a potential bottleneck because of the frequency of its occurrence when it could be avoided altogether. It is an expensive operation to map the stack trace info of the bundled code to that of the individual files and since tests are run in DEV mode, this operation seemed unnecessary.

<p align="center"><img width="800px" src="https://user-images.githubusercontent.com/11008603/91498863-2935d900-e8de-11ea-8f2a-308f83024081.png" /></p>

As a fix, a check was added such that the “mapStacktrace” operation only executes if DEV_MODE is false.

Subsequent test runs with this fix indicated a significant decrease in the runtime (~by half, from 8m to 4m).

<p align="center"><img src="https://user-images.githubusercontent.com/11008603/91499014-60a48580-e8de-11ea-89c0-bda7b4e52478.png" /></p>

