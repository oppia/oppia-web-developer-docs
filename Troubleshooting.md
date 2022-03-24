## General

Here are some general troubleshooting tips for Oppia. The platform specific tips are [[Linux|Troubleshooting#linux]], [[Windows|Troubleshooting#windows]], and [[Mac OS|Troubleshooting#mac-os]].

### `No module named builtins`

If after running `python -m scripts.start` you get the following lines:
```
Traceback (most recent call last):
File "/usr/lib/python2.7/runpy.py", line 174, in _run_module_as_main
   "__main__", fname, loader, pkg_name)
File "/usr/lib/python2.7/runpy.py", line 72, in _run_code
   exec code in run_globals
File "/home/user/oppia/oppia/scripts/start.py", line 30, in <module>
  import python_utils
File "python_utils.py", line 36, in <module>
  import builtins  # isort:skip
ImportError: No module named builtins
```

Then run `pip install future`.

### No Java

If running `which java` on the terminal does not return any output, you do not have java installed. You can install it by running `sudo apt install openjdk-7-jre-headless`. Note that this command might vary for your local machine.

### Frontend Tests Stuck

If you're unable to run frontend tests while pushing your changes due to the script getting stuck, please go to "node_modules" directory (located at the same level as that of the root directory) and delete the "protractor" directory present inside that folder.

### Selenium Server Not Killed by Ctrl-C

If the selenium server is not killed on pressing Ctrl-C and you get an error something like this:

```
  LocalError: Either another browserstack local client is running on your machine or some server is
  listening on port 45691
```

You can kill the process manually by `sudo lsof -t -i:45691` or `sudo kill $(sudo lsof -t -i:45691)`.
These commands can be used anywhere to kill a running process on any port by using the appropriate port number.

### 403 Error

If you get 403 error while serving Oppia locally, this can be because you are working behind a proxy.

go to `oppia_tools/google-cloud-sdk-XXX.X.X/google-cloud-sdk/platform/google_appengine/google/appengine/tools/` and open the `appengine_rpc.py` file. Comment the following line in it. `opener.add_handler(ProxyHandler())`. Run the server again.

[Resource for outdated version of the App Engine.](https://stackoverflow.com/questions/16698621/google-app-engine-error-httperror/17522082)

### MERGE_MSG Newer than Swap File

If you’re seeing issues when trying to merge from upstream/develop that say something like `While opening file “/Users/….../oppia/.git/MERGE_MSG” dated: ….. NEWER than swap file!` then try following the given instructions in the error message (more info [here](https://stackoverflow.com/questions/13361729/found-a-swap-file-by-the-name/13361874)). If that doesn’t work, your forked repo may be out of sync with Oppia’s. Make sure your develop branch does NOT have any changes or commits that aren’t present on the original Oppia repo.

### Warnings from `start.py`

**Note:** There may be a few warnings that appear after running `start.py`. Don’t worry about these so long as you see the Oppia home page once you go to http://localhost:8181. The script should continue to run so long as the development server is on (you’ll see a lot of lines that start with “INFO”) and you’re able to navigate to the page.

### No Such File or Directory: Google Cloud SDK

If you see an error that says something along the lines of `OSError: [Errno 2] No such file or directory: '/.../opensource/oppia_tools/google-cloud-sdk-XXX.X.X/google-cloud-sdk/platform/google_appengine/google/appengine'` while running `scripts.start` - then try deleting the `../oppia_tools` directory and then running `scripts.start` again.

### No module named '_sqlite3'

If you see an error that says something along the lines of `ERROR: gcloud failed to load: No module named _sqlite3` while running `scripts.start` - then follow the steps below:

1. Uninstall Python 3.7.10 from pyenv with the command: `pyenv uninstall 3.7.10`
2. Install the packages as per the [wiki](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) to have the suggested build environment.
3. Install Python 3.7.10 from pyenv with the command: `pyenv install 3.7.10` and make sure that there are no warnings or errors in the output of the command.

### Problems Cloning from GitHub

If you have issues cloning the GitHub repository, make sure of the following:

1. That you’ve already [forked](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) the Oppia repository
2. That you’re making sure to [clone](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo#keep-your-fork-synced) from your own fork (making sure to replace `YOUR_USERNAME` in `git clone https://github.com/YOUR-USERNAME/oppia.git` with your GitHub username)
3. If you have two-factor authentication (which you should), that you’re typing in your [access token](https://webkul.com/blog/github-push-with-two-factor-authentication/) as your password when prompted (rather than your GitHub password).

### Certificate Verify Failed

If you see an error that says something like, `IOError: [Errno socket error] [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` then try applying the fix detailed in [this StackOverflow question](https://stackoverflow.com/questions/49183801/ssl-certificate-verify-failed-with-urllib).

### No Module Named Scripts

If you see an error that contains `No module named scripts` when trying to run any of our scripts, then make sure that you’re currently in the correct folder (i.e. the directory called `oppia` that directly contains the `scripts` directory). Note that, in general, all scripts should be run from oppia/ (and not from scripts/ or other directories). You can find more information about how to navigate folders using the command line [here](https://www.macworld.com/article/2042378/master-the-command-line-navigating-files-and-folders.html).

### Invalid Syntax

If you repeatedly get errors with `SyntaxError: invalid syntax` for a module or class that you didn’t edit and/or is part of a third party library, then try doing either of the following…

* Be sure that libraries were installed using Python 3. If not, uninstall all Python 2 environments and reinstall everything in Python 3.
* Delete the `oppia_tools` directory and rerun the script

### Java Read Past EOF

If you run into the following error when running `start.py`, you can follow the answer [here](https://stackoverflow.com/a/55885634), which says to run `../oppia_tools/elasticsearch-7.10.1/bin/elasticsearch-keystore create` (run it from opensource/oppia/). When prompted, confirm to manually overwrite the key already created.

```
Exception in thread "main" java.io.EOFException: read past EOF: SimpleFSIndexInput(path="/home/[user]/opensource/oppia_tools/elasticsearch-7.10.1/config/elasticsearch.keystore")
```

### Low RAM

Oppia does not work well on machines with little available memory. Contributors have reported problems running on machines with less than 4 GB of RAM that were resolved when switching to a machine with 8 GB of RAM. You may also experience problems if your computer has memory-intensive tasks running. See [#12098](https://github.com/oppia/oppia/issues/12098) for an example of how this problem can manifest.

For possible workarounds, see [[Failed to Start Server on Port XXXX|Troubleshooting#failed-to-start-server-on-port-xxxx]].

### Failed to Start Server on Port XXXX

If you see `Failed to start server on port XXXX, exiting ...` here are some possible solutions:

* Sometimes this happens because the service is taking a long time to start running on that port. If the service takes longer than our timeout, you'll see this message. To fix this, you can increase the timeout in `scripts/common.py` by increasing the value of `MAX_WAIT_TIME_FOR_PORT_TO_OPEN_SECS`. This can also happen when your machine is running more slowly than usual. Quitting resource-intensive applications or rebooting may help.
* Sometimes this happens because the server earlier failed to shutdown correctly. You may need to kill remaining processes. You can search for processes containing `oppia`, and `elasticsearch` like this: `ps -ax | grep <search term>`. This will show the process ID numbers, which you can pass to `kill` to kill the process like this: `kill <process ID>`.
* Some developers have found that they have to run some services manually to get Oppia to work. This is an unsupported workaround, but you may find it useful:
  * Redis (port 6379) on M1 macs:
    1. Install Rosetta 2 try [this](https://www.google.com/url?q=https://stackoverflow.com/questions/64882584/how-to-run-the-homebrew-installer-under-rosetta-2-on-m1-macbook%23:~:text%3DYou%2520can%2520run%2520Terminal%2520with,%2522Open%2520using%2520Rosetta%2522%2520option&sa=D&source=hangouts&ust=1611504651223000&usg=AFQjCNFhJysGCAFdzLswFuK5JVoxjs6CwQ)
    2. Inside Rosetta perform all the installations/prerequisites.
       Note: If `sudo easy_install pyyaml` does not work try using `pip install pyyaml`.
    3. Open the Rosetta terminal and download redis server using `pip install redis`.
    4. Run redis-server with the following cmd: `redis-server` (**Don't stop the redis server**)
    5. Open another rosetta terminal and run `python -m scripts.start`
  * Elasticsearch (port 9200):

    ```console
    $ oppia_tools/elasticsearch-<version>/bin/elasticsearch
    ```
    For some version number `<version>`.

### `./portserver.socket is not listed in the .github/CODEOWNERS file`

Just delete the `./portserver.socket` file. It's generated automatically by the end-to-end tests and is supposed to be cleaned up automatically. However, if your tests don't exit cleanly, the file can get left behind, which causes lint failures. The file is just a socket for communication between processes, so it's safe to delete once the tests exit.

### Push fails due to connection timeout

If you use SSH for your GitHub remote URL, you may find that when you run `git push` and the tests pass, your commits don't show up on GitHub. When this happens, the end of the terminal output after `git push` will look like this:

```text
...
Done!
------------------------------------
All Frontend Coverage Checks Passed.
------------------------------------
Already on ...
```

Notice that there is no output showing that commits were pushed. To fix this, use an HTTPS remote URL for GitHub as specified in our [[installation instructions|Installing-Oppia]].

You can check your remote URLs like this:

```console
$ git remote -v
origin     https://github.com/{{GITHUB USERNAME}}/oppia.git (fetch)
origin     https://github.com/{{GITHUB USERNAME}}/oppia.git (push)
upstream   https://github.com/oppia/oppia.git (fetch)
upstream   https://github.com/oppia/oppia.git (push)
```

If you see SSH URLs, fix them like this:

```console
$ git remote set-url origin https://github.com/{{GITHUB USERNAME}}/oppia.git
$ git remote set-url upstream https://github.com/oppia/oppia.git
```

Once you've fixed this, you should see this at the end of your output from `git push`:

```text
...
Done!
------------------------------------
All Frontend Coverage Checks Passed.
------------------------------------
Already on ...
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 986 bytes | 986.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:{{GITHUB USERNAME}}/oppia.git
   cfb1f9e..e3f8d66  cleanup -> cleanup
```

Note that the output above will look somewhat different for you since it's specific to what data you're pushing.

## Linux

### Python 2 is not available

If you get error like this when running `python -m scripts.start`:
```
ERROR: (dev_appserver) python2: command not found
```
you will need to install Python 2 on your platform, even though Oppia doesn't use Python 2 anymore some parts of the App Engine dev server still need it. If you are on Ubuntu, you should be able to fix this using `sudo apt install python2`. 


### OSError: [Errno 2] No such file or directory

If you get an error like this
```
  File "/home/…/oppia/oppia_tools/google-cloud-sdk-335.0.0/google-cloud-sdk/platform/google_appengine/google/appengine/tools/devappserver2/module.py", line 231, in _create_instance_factory
    module_configuration=module_configuration)
  File "/home/…/oppia/oppia_tools/google-cloud-sdk-335.0.0/google-cloud-sdk/platform/google_appengine/google/appengine/tools/devappserver2/python/instance_factory.py", line 148, in __init__
    self._SetupVirtualenvFromConfiguration()
  File "/home/…/oppia/oppia_tools/google-cloud-sdk-335.0.0/google-cloud-sdk/platform/google_appengine/google/appengine/tools/devappserver2/python/instance_factory.py", line 193, in _SetupVirtualenvFromConfiguration
    self._venv_dir, requirements_file.name)
  File "/home/…/oppia/oppia_tools/google-cloud-sdk-335.0.0/google-cloud-sdk/platform/google_appengine/google/appengine/tools/devappserver2/python/instance_factory.py", line 278, in _SetupVirtualenv
    cls._RunPipInstall(venv_dir, requirements_file_name)
  File "/home/…/oppia/oppia_tools/google-cloud-sdk-335.0.0/google-cloud-sdk/platform/google_appengine/google/appengine/tools/devappserver2/python/instance_factory.py", line 262, in _RunPipInstall
    pip_proc = subprocess.Popen(pip_cmd, stdout=pip_out)
  File "/usr/lib/python2.7/subprocess.py", line 394, in __init__
    errread, errwrite)
  File "/usr/lib/python2.7/subprocess.py", line 1047, in _execute_child
    raise child_exception
OSError: [Errno 2] No such file or directory
```
please follow the instructions mentioned in [#13672](https://github.com/oppia/oppia/issues/13672) to fix it.

### Pip: Cannot Import Name Main

If you get an error while running install_third_party.py which ends with:
```
Traceback (most recent call last):
File "/usr/bin/pip", line 9, in <module>
from pip import main
ImportError: cannot import name main
```
Try running `$ python -m pip uninstall pip` followed by running `$ python -m scripts.install_third_party` (source: [SO thread](https://stackoverflow.com/questions/49964093/file-usr-bin-pip-line-9-in-module-from-pip-import-main-importerror-canno)).


### System Limit for Number of File Watchers Reached

If you get an error while running a local server which says something like this:

```
'watch' errored after 789 ms
Error: ENOSPC: System limit for number of file watchers reached, watch 'some filename'
```

then you will need to increase the number of system watchers by running the command:
```
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
```
Use the same command in the cases where the changes made by you to files are not being detected by the server.


### No Module functools_lru_cache

If you get an error of the format:
```
ImportError: No module named functools_lru_cache
```

First check the directory `../oppia_tools/pylint-1.9.4` and if it is empty, re-install the missing prerequisites by running:
```
python -m scripts.start
```

If the directory is not empty and you still get the same error, try installing matplotlib by running the following command:
```
sudo apt-get install python3-matplotlib
```


### No Module appengine.api

If after running `python -m scripts.linters.pre_commit_linter`, you get an error that contains:
```
No module named appengine.api
```
If you're not using a virtual environment, make sure that the path to the appengine lib is locatable. Also, make sure that there are no other versions of google libraries installed globally which may cause path conflict issues. Refer to [this blog](https://medium.com/@maanavshah/fixing-python-import-error-no-module-named-appengine-ebcb540e7f18) for more reference.
If this error occurs within a virtual environment, try reinstalling the libs by running clean.py followed by start.py.



### ModuleNotFoundError: No module named _bz2
1. Install bz2 headers. Use the command `sudo apt-get install libbz2-dev` on Ubuntu.
2. Install Python 3 again so that the bz2 library gets included in `~/.pyenv/versions/3.7.10/lib/python3.7/`. Use the command `pyenv install 3.7.10`.



## Mac OS

### Python 2 is not available 

If you get error like this when running `python -m scripts.start`:

```
ERROR: (dev_appserver) python2: command not found
```

you will need to install Python 2 on your platform, even though Oppia doesn't use Python 2 anymore some parts of the App Engine dev server still need it. If you have MacOS >= 12.3, please follow the steps listed [here](https://github.com/oppia/oppia/wiki/Installing-Oppia-(Mac-OS;-Python-3)#install-prerequisites) to install Python 2 on your system. 


### Local datastore data are not being deleted

In some cases it is possible that the local datastore data are not deleted when the server is rerun, you can delete the data by running `curl -X POST http://localhost:8089/reset` when the devserver is running.

### No module named '_ctypes' on M1 Macs

When one contributor got a `ModuleNotFoundError: No module named '_ctypes'` error when installing on an M1 Mac with Rosetta, they found that using Python 3.9 worked.

### Cannot Import Name `_imaging`

After running `python -m scripts.start`, if you get an error around the following lines:

```
     File "/opensource/oppia/core/platform/models.py", line 176, in import_gae_image_services
         from core.platform.image import gae_image_services
     File "/opensource/oppia/core/platform/image/gae_image_services.py", line 20, in <module>
         from PIL import Image
     File "/opensource/oppia_tools/Pillow-6.2.2/PIL/Image.py", line 93, in <module>
         from . import _imaging as core
   ImportError: cannot import name _imaging
```
 (note: [Google search results](https://pillow.readthedocs.io/en/stable/installation.html#warnings) indicate that PIL and Pillow cannot coexist in the same environment)

First stop the script running with Ctrl + C (or Command-period on a MAC).
Try uninstalling PIL:
```
  $ pip uninstall PIL
```

Then, uninstall and reinstall Pillow
```
  $ pip uninstall pillow
  $ pip install pillow
```

Finally, try running the `python -m scripts.start` script again.


### Command cc failed with exit status 1

If, on MacOS Mojave V10.14.x, you get an issue arises while installing PIL library that has a lot of gibberish and that includes stuff like:

  `error: command 'cc' failed with exit status 1`

  `error: command 'clang' failed with exit status 1`

then try running this command on terminal ([reference](https://github.com/python-pillow/Pillow/issues/3438)):

```
  sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```


### GitPython Not Installed

If you get an error that includes:

```
GitPython is not installed for Python 3.x the 'dist' command will not work without it. Get it using pip or easy_install
```

please install [GitPython](http://gitpython.readthedocs.io/en/stable/intro.html#installing-gitpython) before proceeding further.


### Install Imaging

If you get an error that includes:

```
Command "/usr/local/opt/python@3/bin/python3.7 -u -c "import setuptools, tokenize;__file__='/private/tmp/pip-req-build-TGvu2M/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /private/tmp/pip-record-6nuoQh/install-record.txt --single-version-externally-managed --compile --home=/private/tmp/pip-target-CMgDrw" failed with error code 1 in /private/tmp/pip-req-build-TGvu2M/
```

please run the following comands:-

```
export CFLAGS=-Qunused-arguments
export CPPFLAGS=-Qunused-arguments
pip install http://effbot.org/downloads/Imaging-1.1.7.tar.gz
```

For more details look up the following [link](https://answers.ros.org/question/145856/having-trouble-installing-pil-in-mac-osx/?answer=146471#post-id-146471)


### No Java Runtime Present

If you get an error that includes:

```
No Java runtime present, requesting install.
closure-compiler failed.
```
please download [Java](https://support.apple.com/kb/DL1572?locale=en_US) and install it.


### 503 Error when Starting Appengine

if you run into an error that looks like this when starting App Engine:

```
File "/System/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib2.py", line 558, in http_error_default
    raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
HTTPError: HTTP Error 503: Service Unavailable
```

please take a look at this StackOverflow [answer](https://stackoverflow.com/a/19460147) and see if it helps.


### SSL Wrong Version Number

If you get an error with `IOError: [Errno socket error] [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:727)` at the bottom, one contributor found that the error occurred intermitently. If you rerun your command, you should get further down the list of files to download. Keep rerunning until all the downloads succeed.


### SSL Verification Issues

If all else fails, and you run into SSL related issues while installing third party libs, [here](https://stackoverflow.com/a/40857561) is what worked for one contributor. **WARNING This disables all SSL verification, so use at your own risk!**


## Windows

### Windows Firewall

It's possible that Windows firewall might be preventing localhost:8181 to launch. In such a case, you should re-config the firewall by adding new inbound rule so that ports 8181 and 8000 are allowed. (Instruction about how to add inbound rules can be found [here](https://msdn.microsoft.com/en-us/library/hh168549(v=nav.90).aspx))


### No Such File or Directory /dev/disk/by-id

If you get this error
```
[OSError: [Errno 2] No such file or directory: `/dev/disk/by-id/`
```
try fixing it by adding the `--no_browser` argument to your command, e.g. `python -m scripts.start --no_browser`.



## If the above doesn't work

If you run into any issues with the installation process, please let us know by [filing an issue](https://github.com/oppia/oppia/issues/new?title=Describe%20your%20feature%20request%20or%20bug%20report%20succinctly&body=If%20you%27d%20like%20to%20propose%20a%20feature,%20describe%20what%20you%27d%20like%20to%20see.%20Mock%20ups%20would%20be%20great!%0A%0AIf%20you%27re%20reporting%20a%20bug,%20please%20be%20sure%20to%20include%20the%20expected%20behaviour,%20the%20observed%20behaviour,%20and%20steps%20to%20reproduce%20the%20problem.%20Console%20copy-pastes%20and%20any%20background%20on%20the%20environment%20would%20also%20be%20helpful.%0A%0AThanks!). You should use our template on [How to Ask Questions](https://github.com/oppia/oppia/wiki/Guide-on-How-to-Ask-Questions) to provide us all the necessary info. Thanks!
