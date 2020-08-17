Sometimes, things go wrong while programming, and the reason for that is not obvious! In order to figure out what's happening, you will need to **debug** the code. This is an important skill to learn, but not an easy one to teach. On this page, we present a few examples of "debugging stories" from team members, so that you can see how other people approach tricky problems in the codebase.

## Google App Engine SDK Upgrade
_Contributed by Kevin Zhang_ (**@kevjumba**)

### Oppia's Previous Setup
Previously, in our setup for Google App Engine, we would download a deprecated version of the Google App Engine package, namely google_appengine_1.9.67 with all of the required utilities needed for Oppia operation. We would also have a separate download for an old version of the Google Cloud SDK that performs certain gcloud utility operations. 

### Primary Motivation
Google App Engine has since deprecated the separation of the Google App Engine package from the regular Google Cloud SDK. The latest version of the Google Cloud SDK contains within it, similar but upgraded functionality of Google App Engine so the need for the older individual Google App Engine package no longer exists. Furthermore, the newer version of Google App Engine contained within Google Cloud SDK version 304.0.0 provides support for VPC access connector functionality.

### Debug Log
During the upgrade, I encountered many errors related to the upgrade and incompatibilities with our old usage. This is documentation of my debugging process and certain things I’ve learned that may be able to help future developers.

### Debug Process
1. To replace the dev_appserver.py functionality, which is the python script provided to start a development application server of Google App Engine for local development testing, I found a dev_appserver.py script on the top level of the Google Cloud SDK directory (the old dev_appserver.py was also on the top level in the old setup) and replaced all paths to that script with the new Google Cloud SDK path.

1. The normal development server started fine but after making a pull request, Circle CI e2e tests started failing. When the dev app server tried to start, the build errored out with the error message: Permission Denied. 
   - After perusing the stack-trace, I was led to a reference to a subprocess call. The call was to execute a command `python -c import grpc` which was a python package nested within the cloud sdk directory. Essentially the command was to import grpc through the command line. 
       - Further, the dev_appserver.py script on the top level of the Google Cloud SDK folder actually points to a dev_appserver.py nested inside the directory. 
   - In an attempt to fix the bug, I set up another branch on top of my branch and deleted all of the .github/workflows yaml files and left the .circleci/config.yml file. I edited the circleci config so that it would only run a simple test so that I can debug the error in quick iterations on the Circle CI build.
       - I first tried to chmod with `chmod -R 777` the entire directory but this didn’t work.
       - I added a subprocess command to print out the file permissions right before the dev_appserver is started and compared the permissions to the permissions of my own directory and they seemed similar or at least the same where it counted (I researched what files Python touches when an import happens and made sure that those files in the grpc folder matched with mine).
       - Since the permissions seemed to match, I changed the command to start the dev server to use sudo as a test of whether or not it is actual user permissions. Since the error still occurred, I realized it’s probably some other issue.
       - I decided I need to ssh into the instance for more debugging. In order to do this, rerun a job with the button "Rerun job with SSH" on the top right of the circle ci console and expand the tab at the bottom labeled, "Enable SSH". It should provide you with details to log in to the terminal.
     - I logged into the SSH instance and tried a variety of tests.
        - Tried importing grpc from the command line. Resulted in an error shown below. This error is due to the fact that the Circle CI instance runs Ubuntu which has a default Python that uses 4 character unicode. However, the downloaded version of grpc uses a 2 character unicode compilation so the compilations don’t match. I did research on whether it was possible to build CircleCI’s python docker image with a different unicode setting but this was not possible.
        - Tried resetting the entire directory of Google App Engine to have max privileges. (Didn’t work)
        - Tried running the dev_appserver.py script from the terminal. (Didn’t work)
   - Finally, by pure coincidence, I decided to run the nested dev_appserver.py script by itself instead of relying on the top level script. This turns out to have a similar configuration to the older version of the dev_appserver so the errors finally went away. 