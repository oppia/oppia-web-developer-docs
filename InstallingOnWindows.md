The following instructions outline how to install Oppia on a Windows machine and run the tests. Note that the resulting Oppia installation will omit the code interaction, which depends on a library called jsrepl that we have not figured out how to install in Windows yet. If you would like to help with fixing this, please add a comment to [issue 100](https://github.com/oppia/oppia/issues/100) -- thanks!

### First we'll get a development server up and running. ###

1. Install Python 2.7.6 by selecting the appropriate MSI from [this page](https://www.python.org/download/releases/2.7.6/). (You can follow [these instructions](http://support.microsoft.com/kb/827218) to determine whether your computer uses the x64 or x86 architecture.) Do not install the latest Python version, 2.7.7, as it will trigger a problem in the GAE. During the installation, select the option "add python.exe to path" (if you see this option). If you do not see this option, manually add Python to the path by going to `
My Computer > Properties > Advanced System Settings > Environment Variables` and appending "C:\Python27" to the PATH environment variable.

2. Install the Python Imaging Library (PIL) 1.1.7 for Python 2.7 from here: http://www.pythonware.com/products/pil/ . If you run into issues, the following links may be helpful:
  * http://stackoverflow.com/questions/14177000/cant-install-pil-1-7
  * http://technet.microsoft.com/en-us/library/cc947813%28v=ws.10%29.aspx

3. Install Git Bash from here: http://git-scm.com/download/win . During the installation, select "Use Git from Git Bash only" and "Checkout Windows-style, commit Unix Style line endings". Launch a Git Bash terminal and ensure that python 2.7.6 is on the path by typing "python" at the command line.

4. Install Python setuptools by downloading ez\_setup.py from https://pypi.python.org/pypi/setuptools, putting ez\_setup.py in your home directory and, in the Git Bash terminal, typing `python ez_setup.py`.

5. Clone the oppia repository to your local machine. [TODO: link to steps]

_The rest of these instructions assume that you are working on the latest revision of the `develop` branch. To get to this revision, ensure you're in the `oppia/` root folder, and run:_

```
    git pull
    git checkout develop
    git pull origin develop
```

6. Go to http://nodejs.org. Click "Downloads", then "Other Releases", then "v0.10.33", then download and execute "node-v0.10.33-x86.msi". After executing this, restart your computer, in order to make "node" and "npm" accessible from the command line. (See [here](http://blueashes.com/2011/web-development/install-nodejs-on-windows/) for more info.)

7. Run `bash scripts/start.sh --nojsrepl` and wait for it to complete downloading and installing all the necessary dependencies. This will start the GAE. Note that node.js and jsrepl will not be installed by this script; you have already installed nodejs in the previous step.

8. Open `localhost:8181` in a browser. You should see Oppia load!

### Next, we'll run the backend tests. ###

9. Open a new command prompt, or kill the GAE if necessary to get the prompt back -- then, run the back end tests by typing `bash scripts/test.sh`. Note that killing the GAE will shut down the local server.

### Finally, we'll run the frontend tests. ###

10. Install Chrome.

11. Run `bash scripts/run_js_tests.sh --nojsrepl`. The first time this runs it will install karma and other node modules.
  * During the installation of karma you may get an MSBUILD error saying it can't load the Visual C++ component "VCBuild.exe". If you see this, ignore it and re-run the script; it should work the second time.
  * If you get ENOENT errors, have a look at [this stackoverflow answer](http://stackoverflow.com/questions/25093276/node-js-windows-error-enoent-stat-c-users-rt-appdata-roaming-npm). You may need to create an `npm` folder, and/or run the script as an administrator.

12. If all goes well, Chrome will launch, and the front-end tests will complete.

# Doing programming work on Windows #

## Configuring your GitHub username and password ##

At some point you will need to submit code to GitHub, which requires you to provide login information. See [this link](https://help.github.com/articles/set-up-git/#next-steps-authenticating-with-github-from-git) for instructions on how to set things up so you don't have to do this manually each time.
