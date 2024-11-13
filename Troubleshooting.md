## General

Here are some general troubleshooting tips for Oppia. The platform specific tips are [Linux](#linux), [Windows](#windows), and [Mac OS](#mac-os).

# Table of Contents

- [For Jio India Users](#for-jio-india-users)
- [`[Errno 104] Connection reset by peer`](#errno-104-connection-reset-by-peer)
- [`No module named builtins`](#no-module-named-builtins)
- [No Java](#no-java)
- [Frontend Tests Stuck](#frontend-tests-stuck)
- [Selenium Server Not Killed by Ctrl-C](#selenium-server-not-killed-by-ctrl-c)
- [403 Error](#403-error)
- [MERGE\_MSG Newer than Swap File](#merge_msg-newer-than-swap-file)
- [Warnings from `start.py`](#warnings-from-startpy)
- [No Such File or Directory: Google Cloud SDK](#no-such-file-or-directory-google-cloud-sdk)
- [No module named '\_sqlite3'](#no-module-named-_sqlite3)
- [Problems Cloning from GitHub](#problems-cloning-from-github)
- [Certificate Verify Failed](#certificate-verify-failed)
- [No Module Named Scripts](#no-module-named-scripts)
- [Invalid Syntax](#invalid-syntax)
- [Java Read Past EOF](#java-read-past-eof)
- [Low RAM](#low-ram)
- [Failed to Start Server on Port XXXX](#failed-to-start-server-on-port-xxxx)
- [Failed to connect to raw.githubusercontent.com port 443](#failed-to-connect-to-rawgithubusercontentcom-port-443)
- [`./portserver.socket is not listed in the .github/CODEOWNERS file`](#portserversocket-is-not-listed-in-the-githubcodeowners-file)
- [Push fails due to connection timeout](#push-fails-due-to-connection-timeout)
- [Exception: Error compiling proto files](#exception-error-compiling-proto-files)
- [Linux](#linux)
  - [Python 2 is not available](#python-2-is-not-available)
  - [OSError: \[Errno 2\] No such file or directory](#oserror-errno-2-no-such-file-or-directory)
  - [Pip: Cannot Import Name Main](#pip-cannot-import-name-main)
  - [ENOSPC: System Limit for Number of File Watchers Reached](#enospc-system-limit-for-number-of-file-watchers-reached)
  - [No Module functools\_lru\_cache](#no-module-functools_lru_cache)
  - [No Module appengine.api](#no-module-appengineapi)
  - [ModuleNotFoundError: No module named \_bz2](#modulenotfounderror-no-module-named-_bz2)
  - [Subprocess.CalledProcessError: Command 'yarn install --pure-lockfile' returned non-zero exit status 1](#subprocesscalledprocesserror-command-yarn-install---pure-lockfile-returned-non-zero-exit-status-1)

- [Mac OS](#mac-os)
  - [Python 2 is not available](#python-2-is-not-available-1)
  - [Error: alert\_on\_exit() -\> Iterator\[None\]](#error-alert_on_exit---iteratornone)
  - [Local datastore data are not being deleted](#local-datastore-data-are-not-being-deleted)
  - [No module named '\_ctypes' on M1 Macs](#no-module-named-_ctypes-on-m1-macs)
  - [Cannot Import Name `_imaging`](#cannot-import-name-_imaging)
  - [Command cc failed with exit status 1](#command-cc-failed-with-exit-status-1)
  - [GitPython Not Installed](#gitpython-not-installed)
  - [Install Imaging](#install-imaging)
  - [No Java Runtime Present](#no-java-runtime-present)
  - [503 Error when Starting Appengine](#503-error-when-starting-appengine)
  - [SSL Wrong Version Number](#ssl-wrong-version-number)
  - [SSL Verification Issues](#ssl-verification-issues)
  - [Yarn: ESOCKETTIMEDOUT](#yarn-esockettimedout)
  - [ERROR: Cannot uninstall {Package-Name-and-version}, RECORD file not found](#error-cannot-uninstall-package-name-and-version-record-file-not-found)
- [Windows](#windows)
  - [Windows Firewall](#windows-firewall)
  - [No Such File or Directory /dev/disk/by-id](#no-such-file-or-directory-devdiskby-id)
  - [First build never completed](#first-build-never-completed)
- [Docker Setup](#docker-setup)
  - [docker-desktop : Depends: docker-ce-cli but it is not installable](#docker-desktop--depends-docker-ce-cli-but-it-is-not-installable)
  - [make commands: `Operation not permitted`](#make-commands-operation-not-permitted)
  - [Installation encounters `network timeout` or `connection error`](#installation-encounters-network-timeout-or-connection-error)
- [If the above doesn't work](#if-the-above-doesnt-work)

### For Jio India Users
It seems the Jio network is blocking the domain `raw.githubusercontent.com` which is used by Github for storage of images in this wiki and some of the dependencies while installing Opia.. If you are using Jio, you can try changing the DNS address to 8.8.8.8 (Google DNS) or 1.1.1.1 (Cloudfare DNS) from settings. Original discussion [here](https://github.com/orgs/community/discussions/42655)

### `[Errno 104] Connection reset by peer`
If after running `python -m scripts.start` you get the following lines:
```
Traceback (most recent call last):
  File "/home/vansh/.pyenv/versions/3.9.20/lib/python3.8/urllib/request.py", line 1354, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "/home/vansh/.pyenv/versions/3.9.20/lib/python3.8/http/client.py", line 1256, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/home/vansh/.pyenv/versions/3.9.20/lib/python3.8/http/client.py", line 1302, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/home/vansh/.pyenv/versions/3.9.20/lib/python3.8/http/client.py", line 1251, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/home/vansh/.pyenv/versions/3.9.20/lib/python3.8/http/client.py", line 1011, in _send_output
    self.send(msg)
  File "/home/vansh/.pyenv/versions/3.9.20/lib/python3.8/http/client.py", line 951, in send
    self.connect()
  File "/home/vansh/.pyenv/versions/3.9.20/lib/python3.8/http/client.py", line 1425, in connect
    self.sock = self._context.wrap_socket(self.sock,
  File "/home/vansh/.pyenv/versions/3.9.20/lib/python3.8/ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "/home/vansh/.pyenv/versions/3.9.20/lib/python3.8/ssl.py", line 1040, in _create
    self.do_handshake()
  File "/home/vansh/.pyenv/versions/3.9.20/lib/python3.8/ssl.py", line 1309, in do_handshake
    self._sslobj.do_handshake()
ConnectionResetError: [Errno 104] Connection reset by peer
```
Then run `pip install requests[security]`.

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

If you're unable to run frontend tests while pushing your changes due to the script getting stuck, please go to "node_modules" directory (located at the same level as that of the root directory) and delete the "webdriverio" directory present inside that folder.

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

### No module named '\_sqlite3'

If you see an error that says something along the lines of `ERROR: gcloud failed to load: No module named _sqlite3` while running `scripts.start` - then follow the steps below:

1. Uninstall Python 3.9.20 from pyenv with the command: `pyenv uninstall 3.9.20`
2. Install the packages as per the [wiki](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) to have the suggested build environment.
3. Install Python 3.9.20 from pyenv with the command: `pyenv install 3.9.20` and make sure that there are no warnings or errors in the output of the command.

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

- Be sure that libraries were installed using Python 3. If not, uninstall all Python 2 environments and reinstall everything in Python 3.
- Delete the `oppia_tools` directory and rerun the script

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

- Sometimes this happens because the service is taking a long time to start running on that port. If the service takes longer than our timeout, you'll see this message. To fix this, you can increase the timeout in `scripts/common.py` by increasing the value of `MAX_WAIT_TIME_FOR_PORT_TO_OPEN_SECS`. This can also happen when your machine is running more slowly than usual. Quitting resource-intensive applications or rebooting may help.
- Sometimes this happens because the server earlier failed to shutdown correctly. You may need to kill remaining processes. You can search for processes containing `oppia`, and `elasticsearch` like this: `ps -ax | grep <search term>`. This will show the process ID numbers, which you can pass to `kill` to kill the process like this: `kill <process ID>`.
- Some developers have found that they have to run some services manually to get Oppia to work. This is an unsupported workaround, but you may find it useful:

  - Redis (port 6379) on M1 macs:
    1. Install Rosetta 2 try [this](https://www.google.com/url?q=https://stackoverflow.com/questions/64882584/how-to-run-the-homebrew-installer-under-rosetta-2-on-m1-macbook%23:~:text%3DYou%2520can%2520run%2520Terminal%2520with,%2522Open%2520using%2520Rosetta%2522%2520option&sa=D&source=hangouts&ust=1611504651223000&usg=AFQjCNFhJysGCAFdzLswFuK5JVoxjs6CwQ)
    2. Inside Rosetta perform all the installations/prerequisites.
       Note: If `sudo easy_install pyyaml` does not work try using `pip install pyyaml`.
    3. Open the Rosetta terminal and download redis server using `pip install redis`.
    4. Run redis-server with the following cmd: `redis-server` (**Don't stop the redis server**)
    5. Open another rosetta terminal and run `python -m scripts.start`
  - Elasticsearch (port 9200):

    ```console
    $ oppia_tools/elasticsearch-<version>/bin/elasticsearch
    ```

    For some version number `<version>`.

### Failed to connect to raw.githubusercontent.com port 443

Change the DNS address to 8.8.8.8 or change your network/WiFi.

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

If the push still keeps failing due to a connection timeout, add the following lines to `~/.ssh/config` ([Reference](https://stackoverflow.com/a/65818657)):

  ```console
  Host*
    ServerAliveInterval 60
    ServerAliveCountMax 30
  ```

### Exception: Error compiling proto files

If you are getting something like this in M1 macbooks when running `python -m scripts.start`:

```
b'protoc-gen-js: program not found or is not executable\Please specify a program using absolute path or make sure the program is available in your PATH system variable\n--js_out: protoc-gen-js: Plugin failed with status code 1. Inplugin js: exit status 1\n
Traceback (most recent call last) :
   File "/Users/.../.pyenv/versions/3.9.20/lib/python3.8/runpy.py", line 193, in _run_module_as_main
      "main" mod_spec)
   File "/Users/.../.pyenv/versions/3.9.20/lib/python3.8/runpy.py", line 85, in run_code
      exec (code, run globals)
   File "/Users/.../opensource/oppia/scripts/start.py", line 32, in <module>
      install_third_party_libs.main()
   File "/Users/.../opensource/oppia/scripts/install_ third party_libs.py", line 226, in main
      compile_protobuf_files (PROTO FILES PATHS)
   File "/Users/.../opensource/oppia/scripts/install_thirdparty_libs.py",line145,in_compile_protobuf_files
      raise Exception ('Error compiling proto files at %s' % path)
   Exception: Error compiling proto files at /Users/.../opensource/oppia/third_party/oppia-ml-proto-0.0.0
```

Try searching for where protoc is installed (probably in `/opt/homebrew/bin/protoc`) and remove it and then re-run the command.

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

### ENOSPC: System Limit for Number of File Watchers Reached

If you get an error while running a local server which says something like this:

```
'watch' errored after 789 ms
Error: ENOSPC: System limit for number of file watchers reached, watch 'some filename'
```

then you will need to increase the number of system watchers by running the command:

```
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
```

Use the same command in the cases where the changes made by you to files are not being detected by the server. See https://stackoverflow.com/questions/22475849/node-js-what-is-enospc-error-and-how-to-solve/32600959#32600959 for more details.


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

If after running `python -m scripts.linters.run_lint_checks`, you get an error that contains:

```
No module named appengine.api
```

If you're not using a virtual environment, make sure that the path to the appengine lib is locatable. Also, make sure that there are no other versions of google libraries installed globally which may cause path conflict issues. Refer to [this blog](https://medium.com/@maanavshah/fixing-python-import-error-no-module-named-appengine-ebcb540e7f18) for more reference.
If this error occurs within a virtual environment, try reinstalling the libs by running clean.py followed by start.py.

### ModuleNotFoundError: No module named \_bz2

1. Install bz2 headers. Use the command `sudo apt-get install libbz2-dev` on Ubuntu.
2. Install Python 3 again so that the bz2 library gets included in `~/.pyenv/versions/3.9.20/lib/python3.8/`. Use the command `pyenv install 3.9.20`.

### Subprocess.CalledProcessError: Command 'yarn install --pure-lockfile' returned non-zero exit status 1

If you get error like this when running ``python -m scripts.start``:
```
Traceback (most recent call last):
  File "/home/hardik/.pyenv/versions/3.9.20/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/hardik/.pyenv/versions/3.9.20/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/hardik/opensource/oppia/scripts/start.py", line 33, in <module>
    install_third_party_libs.main()
  File "/home/hardik/opensource/oppia/scripts/install_third_party_libs.py", line 234, in main
    subprocess.check_call([get_yarn_command(), 'install', '--pure-lockfile'])
  File "/home/hardik/.pyenv/versions/3.9.20/lib/python3.8/subprocess.py", line 364, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['yarn', 'install', '--pure-lockfile']' returned non-zero exit status 1.
```
 - In ``opensource/`` i.e parent folder of ``oppia/``, run below commands :
 ```
sudo apt install cmdtest
```

```
npm install  yarn
```
> Note :- If the above solution doesn't work, please go through the following answered discussions and try the solution mentioned there. [oppia/oppia#17425](https://github.com/oppia/oppia/discussions/17425), [oppia/oppia#18428](https://github.com/oppia/oppia/discussions/18428), [oppia/oppia#14814](https://github.com/oppia/oppia/discussions/14814)

## Mac OS

### Python 2 is not available

If you get error like this when running `python -m scripts.start`:

```
ERROR: (dev_appserver) python2: command not found
```

you will need to install Python 2 on your platform, even though Oppia doesn't use Python 2 anymore some parts of the App Engine dev server still need it. If you have MacOS >= 12.3, please follow the steps listed [here](https://github.com/oppia/oppia/wiki/Installing-Oppia-(Mac-OS;-Python-3)#install-prerequisites) to install Python 2 on your system.

### Error: alert_on_exit() -> Iterator[None]

If after running python -m scripts.start, you get an error similar to this below:

```
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/runpy.py", line 163, in _run_module_as_main
    mod_name, _Error)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/runpy.py", line 119, in _get_module_details
    code = loader.get_code(mod_name)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pkgutil.py", line 281, in get_code
    self.code = compile(source, self.filename, 'exec')
  File "/Users/Desktop/opensource-oppia/oppia/scripts/start.py", line 85
    def alert_on_exit() -> Iterator[None]:
```

Then,

1. Open your `.bash_profile` file, and check if there are two versions of Python listed inside of it, one for Python 2.7 and other for Python 3.8. Simply remove the entry for Python 2.7. Finally, this is how your file should look like:

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Setting PATH for Python 3.10
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.10/bin:${PATH}"
export PATH
```

2. Reload the .bash_profile by doing “source .bash_profile”, and now start your Oppia server `python -m scripts.start`.

**Note:** Even if the bash_profile file doesn’t contain two entries for Python version per #1, please do #2 in order to make sure that the new version of Python is set for the virtual environment.

### Local datastore data are not being deleted

In some cases it is possible that the local datastore data are not deleted when the server is rerun, you can delete the data by running `curl -X POST http://localhost:8089/reset` when the devserver is running.

### No module named '\_ctypes' on M1 Macs

When one contributor got a `ModuleNotFoundError: No module named '_ctypes'` error when installing on an M1 Mac with Rosetta, they found that using Python 3.9.20 worked.

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

> [!NOTE]
> [Google search results]
(https://pillow.readthedocs.io/en/stable/installation.html#warnings) indicate that PIL and Pillow cannot coexist in the same environment

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

If you encounter an issue during the installation of the PIL library on MacOS Mojave V10.14.x, which includes a lot of meaningless characters and contains logs such as:

* `error: command 'cc' failed with exit status 1`

* `error: command 'clang' failed with exit status 1`

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
Command "/usr/local/opt/python@3/bin/python3.8 -u -c "import setuptools, tokenize;__file__='/private/tmp/pip-req-build-TGvu2M/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /private/tmp/pip-record-6nuoQh/install-record.txt --single-version-externally-managed --compile --home=/private/tmp/pip-target-CMgDrw" failed with error code 1 in /private/tmp/pip-req-build-TGvu2M/
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

Please download [Java](https://support.apple.com/kb/DL1572?locale=en_US) and install it.

### 503 Error when Starting Appengine

if you run into an error that looks like this when starting App Engine:

```
File "/System/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/urllib2.py", line 558, in http_error_default
    raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
HTTPError: HTTP Error 503: Service Unavailable
```

please take a look at this StackOverflow [answer](https://stackoverflow.com/a/19460147) and see if it helps.

### SSL Wrong Version Number

If you get an error with `IOError: [Errno socket error] [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:727)` at the bottom, one contributor found that the error occurred intermitently. If you rerun your command, you should get further down the list of files to download. Keep rerunning until all the downloads succeed.

### SSL Verification Issues

If all else fails, and you run into SSL related issues while installing third party libs, [here](https://stackoverflow.com/a/40857561) is what worked for one contributor. **WARNING This disables all SSL verification, so use at your own risk!**

### Yarn: ESOCKETTIMEDOUT

If you get an error like this when running `python -m scripts.start`:

```
info There appears to be trouble with your network connection. Retrying...
info There appears to be trouble with your network connection. Retrying...
info There appears to be trouble with your network connection. Retrying...
info There appears to be trouble with your network connection. Retrying...
info There appears to be trouble with your network connection. Retrying...
error An unexpected error occurred: "https://registry.yarnpkg.com/mathjs/-/mathjs-9.5.2.tgz: ESOCKETTIMEDOUT".
info If you think this is a bug, please open a bug report with the information provided in /opensource/oppia/yarn-error.log".
info Visit https://yarnpkg.com/en/docs/cli/install for documentation about this command.
```

Try running `yarn install --network-timeout 100000`, where the timeout value is in milliseconds. If that doesn’t work, try running the command with a larger network timeout value and keep increasing the timeout (e.g. adding a zero at the end of the value) until it succeeds. Then try running `python -m scripts.start` again. Note: To see if you've raised the timeout enough, you only need to run `yarn install`. You don’t need to run `python -m scripts.start` every time.

### ERROR: Cannot uninstall {Package-Name-and-version}, RECORD file not found

If you get an error like this when running `python -m scripts.start` or scripts for running checks for frontend/backend unit tests:

```
Installing collected packages: certifi
  Attempting uninstall: certifi
    WARNING: No metadata found in /Users/ash/Desktop/openSource/.direnv/python-3.9.20/lib/python3.8/site-packages
    Found existing installation: certifi 2022.12.7
ERROR: Cannot uninstall certifi 2022.12.7, RECORD file not found. You might be able to recover from this via: 'pip install --force-reinstall --no-deps certifi==2022.12.7'.

[notice] A new release of pip is available: 23.1.2 -> 24.0
[notice] To update, run: pip install --upgrade pip
Traceback (most recent call last):
  File "/Users/ash/Desktop/openSource/.direnv/python-3.9.20/bin/pip-sync", line 8, in <module>
    sys.exit(cli())
  File "/Users/ash/Desktop/openSource/.direnv/python-3.9.20/lib/python3.8/site-packages/click/core.py", line 1130, in __call__
    return self.main(*args, **kwargs)
  File "/Users/ash/Desktop/openSource/.direnv/python-3.9.20/lib/python3.8/site-packages/click/core.py", line 1055, in main
    rv = self.invoke(ctx)
  File "/Users/ash/Desktop/openSource/.direnv/python-3.9.20/lib/python3.8/site-packages/click/core.py", line 1404, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/Users/ash/Desktop/openSource/.direnv/python-3.9.20/lib/python3.8/site-packages/click/core.py", line 760, in invoke
    return __callback(*args, **kwargs)
  File "/Users/ash/Desktop/openSource/.direnv/python-3.9.20/lib/python3.8/site-packages/piptools/scripts/sync.py", line 174, in cli
    sync.sync(
  File "/Users/ash/Desktop/openSource/.direnv/python-3.9.20/lib/python3.8/site-packages/piptools/sync.py", line 244, in sync
    run(  # nosec
  File "/Users/ash/.pyenv/versions/3.9.20/lib/python3.8/subprocess.py", line 516, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/Users/ash/Desktop/openSource/.direnv/python-3.9.20/bin/python', '-m', 'pip', 'install', '-r', '/var/folders/75/00_6bzhj2yv42jzg6bk544vh0000gn/T/tmp8rdctoxc', '--require-hashes', '--no-deps']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "/Users/ash/.pyenv/versions/3.9.20/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/Users/ash/.pyenv/versions/3.9.20/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/Users/ash/Desktop/openSource/oppia/scripts/run_backend_tests.py", line 67, in <module>
    from . import install_third_party_libs
  File "/Users/ash/Desktop/openSource/oppia/scripts/install_third_party_libs.py", line 32, in <module>
    install_python_dev_dependencies.main(['--assert_compiled'])
  File "/Users/ash/Desktop/openSource/oppia/scripts/install_python_dev_dependencies.py", line 145, in main
    install_dev_dependencies()
  File "/Users/ash/Desktop/openSource/oppia/scripts/install_python_dev_dependencies.py", line 89, in install_dev_dependencies
    subprocess.run(
  File "/Users/ash/.pyenv/versions/3.9.20/lib/python3.8/subprocess.py", line 516, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['pip-sync', 'requirements_dev.txt', '--pip-args', '--require-hashes --no-deps']' returned non-zero exit status 1.
```

 Try removing the `.direnv` directory located at `{path-to-opensource-directory}/openSource/.direnv`. This directory may contain corrupted or misconfigured environment settings that could lead to installation issues. You can run `rm -rf {path-to-opensource-directory}/openSource/.direnv` to remove it. Please exercise caution when using the `rm -rf` command, as it can delete files and directories recursively without confirmation.

After removing `.direnv`, run `direnv allow` in your active directory (ensure it's `opensource`). This command applies changes to the `.direnv` configuration after manual modifications.

Next, execute `python -m scripts.start` inside your Oppia directory before running other scripts like `python -m scripts.run_frontend_tests`. The `python -m scripts.start` command automatically reinstalls all necessary python packages required for Oppia's development environment. Running other scripts before this step might result in "Module not found" errors, requiring manual reinstallation of each package using the `pip` command.

## Windows

### Windows Firewall

It's possible that Windows firewall might be preventing localhost:8181 to launch. In such a case, you should re-config the firewall by adding new inbound rule so that ports 8181 and 8000 are allowed. (Instruction about how to add inbound rules can be found [here](https://msdn.microsoft.com/en-us/library/hh168549(v=nav.90).aspx))

### No Such File or Directory /dev/disk/by-id

If you get this error

```
[OSError: [Errno 2] No such file or directory: `/dev/disk/by-id/`
```

try fixing it by adding the `--no_browser` argument to your command, e.g. `python -m scripts.start --no_browser`.

### First build never completed

If you are running on Windows with WSL2 and a relatively small amount of RAM (<16 GB), you might see this error:

```
Traceback (most recent call last):
  File "/home/user/opensource/oppia/scripts/servers.py", line 95, in managed_process
    yield popen_proc
  File "/home/user/opensource/oppia/scripts/servers.py", line 449, in managed_ng_build
    raise IOError('First build never completed')
OSError: First build never completed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/contextlib.py", line 131, in __exit__
    self.gen.throw(type, value, traceback)
  File "/home/user/opensource/oppia/scripts/servers.py", line 365, in managed_redis_server
    yield proc
  File "/home/user/opensource/oppia/scripts/start.py", line 178, in main
    stack.enter_context(servers.managed_ng_build(watch_mode=True))
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/contextlib.py", line 425, in enter_context
    result = _cm_type.__enter__(cm)
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/contextlib.py", line 113, in __enter__
    return next(self.gen)
  File "/home/user/opensource/oppia/scripts/servers.py", line 461, in managed_ng_build
    yield proc
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/contextlib.py", line 525, in __exit__
    raise exc_details[1]
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/contextlib.py", line 510, in __exit__
    if cb(*exc_details):
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/contextlib.py", line 131, in __exit__
    self.gen.throw(type, value, traceback)
  File "/home/user/opensource/oppia/scripts/servers.py", line 138, in managed_process
    raise Exception(
Exception: Process Angular Compiler(name="sh", pid=2350) exited unexpectedly with exit code 137

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/user/opensource/oppia/scripts/start.py", line 233, in <module>
    main()
  File "/home/user/opensource/oppia/scripts/start.py", line 229, in main
    dev_appserver.wait()
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/contextlib.py", line 525, in __exit__
    raise exc_details[1]
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/contextlib.py", line 510, in __exit__
    if cb(*exc_details):
  File "/home/user/.pyenv/versions/3.9.20/lib/python3.8/contextlib.py", line 382, in _exit_wrapper
    callback(*args, **kwds)
  File "/home/user/opensource/oppia/scripts/start.py", line 132, in call_extend_index_yaml
    extend_index_yaml.main()
  File "/home/user/opensource/oppia/scripts/extend_index_yaml.py", line 92, in main
    with open(WEB_INF_INDEX_XML_PATH, 'r', encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: '/home/user/opensource/oppia/../cloud_datastore_emulator_cache/WEB-INF/appengine-generated/datastore-indexes-auto.xml'
```

The error code 137 indicates that the Angular compiler ran out of memory. This happens because WSL2 only gives the host operating system (Ubuntu, in our case) 50% of the machine's RAM by default. If you have 8 GB RAM, for example, this means Ubuntu only gets 4 GB, which is insufficient to run Oppia. To fix this, you need to follow [Microsoft's instructions](https://learn.microsoft.com/en-us/windows/wsl/wsl-config) to increase the amount of RAM given to the host operating system.

## Docker Setup

### docker-desktop : Depends: docker-ce-cli but it is not installable

While installing Docker Desktop, ubuntu users might see the following error logs:
```
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:
 
The following packages have unmet dependencies:
 docker-desktop : Depends: docker-ce-cli but it is not installable
E: Unable to correct problems, you have held broken packages.
```

The cause of this error is the absence of the Docker repository installation on the system. To address this issue, a straightforward solution is to execute the following commands before installing Docker Desktop:
```
sudo apt install -y ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update -y
```
These commands are used to prepare an Ubuntu system for Docker installation. They start by installing necessary packages like ca-certificates, gnupg, and lsb-release. Then, a directory named /etc/apt/keyrings is created to store GPG keys. Next, a Docker GPG key is downloaded from the Docker repository and converted to binary format before being saved in the keyring directory. A Docker repository source is added to the APT sources list using an echo command, specifying the architecture, GPG key location, repository URL, and Ubuntu version. Finally, the package list is updated to include Docker packages from the newly added repository. These steps collectively enable secure access to Docker packages and facilitate their installation and management on the system.

Following the completion of the aforementioned commands, you can proceed with the installation of Docker Desktop.

[Reference](https://stackoverflow.com/questions/72299444/docker-desktop-doesnt-install-saying-docker-ce-cli-not-installable) for the solution stated.

### make commands: `Operation not permitted`

Some users might face the following error while running `make` commands:
```
Operation not permitted
make: *** [Makefile:14: docker] Error 1
```

To fix this, create a new user called 'docker' and include the current user in the 'docker' group. Execute the following commands to achieve this:
```
sudo groupadd docker
sudo gpasswd -a $USER docker
```

[Reference]([url](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo))

The cause of the issue is that Docker daemon binds to a unix socket by default, which is owned by root. So, when you run the make commands without admin access, it is not able to access the unix socket and hence the error is thrown.

### Installation encounters `network timeout` or `connection error`

If you encounter network timeout or connection errors during the Docker setup process, simply re-execute the `make build` command. This is necessary as the Docker setup may have been disrupted by network problems. By rerunning the command, the setup will pick up from the point of failure and continue accordingly.

### Any Installation Error in Docker Setup

If you encounter any error during the Oppia Docker setup process, please try the following steps to resolve the issue:
1. Run `make clean` to remove the existing Docker containers and images.
2. Run `make build` to rebuild the Docker containers and images.
3. Run `make run-devserver` to start the Oppia development server.

If the issue persists, try clearing the Docker cache by running the following commands:
1.  Run `make clean` to remove the existing Docker containers and images.
2.  Run `docker builder prune --all` to remove all build cache.
3.  Run `make build` to rebuild the Docker containers and images.
4.  Run `make run-devserver` to start the Oppia development server.

## If the above doesn't work

If you run into any issues with the installation process, please let us know by [filing an issue](https://github.com/oppia/oppia/issues/new?title=Describe%20your%20feature%20request%20or%20bug%20report%20succinctly&body=If%20you%27d%20like%20to%20propose%20a%20feature,%20describe%20what%20you%27d%20like%20to%20see.%20Mock%20ups%20would%20be%20great!%0A%0AIf%20you%27re%20reporting%20a%20bug,%20please%20be%20sure%20to%20include%20the%20expected%20behaviour,%20the%20observed%20behaviour,%20and%20steps%20to%20reproduce%20the%20problem.%20Console%20copy-pastes%20and%20any%20background%20on%20the%20environment%20would%20also%20be%20helpful.%0A%0AThanks!). You should use our template on [How to Ask Questions](https://github.com/oppia/oppia/wiki/Guide-on-How-to-Ask-Questions) to provide us all the necessary info. Thanks!
