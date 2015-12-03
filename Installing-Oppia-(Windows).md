**Warning: This install process may be broken. We've made a number of changes to the installation scripts, and have not upgraded the Windows installation pathway yet. If you have access to a Mac or Linux machine, we suggest using either of those instead.**

**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

These instructions outline how to install Oppia on a Windows machine and run the tests.

### Setting up a development server

1. Install Python 2.7.6 by selecting the appropriate MSI from [this page](https://www.python.org/download/releases/2.7.6/). (You can follow [these instructions](http://support.microsoft.com/kb/827218) to determine whether your computer uses the x64 or x86 architecture.) Do not install the latest Python version, 2.7.7, as it will trigger a problem in GAE. During the installation, select the option "add python.exe to path" if it exists, otherwise manually add Python to the path by going to `My Computer > Properties > Advanced System Settings > Environment Variables` and appending `"C:\Python27"` to the `PATH` environment variable.

2. Install the Python Imaging Library (PIL) 1.1.7 for Python 2.7 from [here](http://www.pythonware.com/products/pil/). If you run into issues, the following links may be helpful:
  * http://stackoverflow.com/questions/14177000/cant-install-pil-1-7
  * http://technet.microsoft.com/en-us/library/cc947813%28v=ws.10%29.aspx

3. Install [Git Bash](http://git-scm.com/download/win). During installation, select "Use Git from Git Bash only" and "Checkout Windows-style, commit Unix Style line endings". Launch a Git Bash terminal and ensure that Python 2.7.6 is on the path by typing `python` at the command line.

4. Install Python setuptools by downloading `ez\_setup.py` from https://pypi.python.org/pypi/setuptools to your home directory, and then typing `python ez_setup.py` in the Git Bash terminal.

5. Clone the oppia repository to your local machine following the instructions in the [README](https://github.com/oppia/oppia/blob/develop/README.md).

6. Go to http://nodejs.org. Click "Downloads", then "Other Releases", then "v0.10.33", then download and execute "node-v0.10.33-x86.msi". After executing this, restart your computer, in order to make "node" and "npm" accessible from the command line. More info [here](http://blueashes.com/2011/web-development/install-nodejs-on-windows/).

7. Run `bash scripts/start.sh --nojsrepl` and wait for it to complete downloading and installing all the necessary dependencies. This will start Google App Engine. Note that node.js and jsrepl will not be installed by this script; you have already installed nodejs in the previous step.

8. Open `localhost:8181` in a browser. You should see Oppia load!

### Running the backend tests

9. Open a new command prompt and type `bash scripts/run_backend_tests.sh`.

### Running the frontend tests

10. Install Chrome.

11. Run `bash scripts/run_frontend_tests.sh --nojsrepl`. The first time this runs it will install karma and other node modules.
  * During the installation of karma you may get an MSBUILD error saying it can't load the Visual C++ component "VCBuild.exe". If you see this, ignore it and re-run the script; it should work the second time.
  * If you get ENOENT errors, have a look at [this Stack Overflow answer](http://stackoverflow.com/questions/25093276/node-js-windows-error-enoent-stat-c-users-rt-appdata-roaming-npm). You may need to create an `npm` folder, and/or run the script as an admin.

12. If all goes well, Chrome will launch, and the front-end tests will complete.
