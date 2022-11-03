## Table of Contents

* [Macs with M1 chips](#macs-with-m1-chips)
* [Install prerequisites](#install-prerequisites)
* [Clone Oppia](#clone-oppia)
* [Setup a virtual environment](#setup-a-virtual-environment)
* [Running Oppia on a development server](#running-oppia-on-a-development-server)
* [Tips and tricks](#tips-and-tricks)

**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

*These installation instructions were last tested on 24 July 2021. For more information on issues that may occasionally arise with the installation process, please see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting) page.*

**Note:** Be careful about trying to install Oppia if you have the Python [Anaconda platform](https://www.anaconda.com/) installed. We've received a bunch of reports that installation is tricky in that environment (there are lots of small things that get in the way), and that the solution is to use the standard python installation (via e.g. homebrew) instead.

## Macs with M1 chips

To check whether your Mac has an M1 chip, navigate to the Apple menu and select "About This Mac." In the window that opens, check for a "Chip" section. If it says "Apple M1" then you have an M1 chip. Otherwise, you should see an Intel processor listed in the "Processor" section. [This article](https://www.howtogeek.com/706226/how-to-check-if-your-mac-is-using-an-intel-or-apple-silicon-processor/) explains in more detail with screenshots if you have trouble.

If your Mac has an M1 chip, follow these instructions instead:

1. If not yet installed, install Rosetta 2 with the following command:  `softwareupdate --install-rosetta`. Rosetta 2 translates Intel-based apps to run on Apple silicon Macs.

2. Next, we will create a Rosetta terminal that emulate the *Intel* architecture. To do so, open a new terminal and run the following command (change "bash" to "zsh" if you're using a zsh terminal):
    ```shell
    $ env /usr/bin/arch -x86_64 /bin/bash --login
    ``` 
    This switches the architecture from Mac M1's *ARM* architecture to the emulated *Intel* architecture for the current session. To verify this, run `arch` in the terminal and you should see `i386` being printed. Proceed with step `3` and `4` using this terminal.
3. Inside the Rosetta terminal (i386) perform the Downloading and prerequisites steps (**Note:** If `sudo easy_install pyyaml` does not work try using `pip3 install pyyaml`).

4. Open the rosetta terminal (from step 2) and run `python -m scripts.start`

## Install prerequisites

Oppia relies on a number of programs and third-party libraries. Many of these libraries are downloaded automatically for you when you first run the `start.py` script provided with Oppia. However, there are some things that you will need to do beforehand:

1. [**If you have Mac OS >= 12.3**] Ensure that you have Python 2.7 available on your system. (This is needed because App Engine's `dev_appserver.py` [requires Python 2.7 to be installed](https://cloud.google.com/appengine/docs/standard/python3/tools/local-devserver-command).) If Python 2.7 is not installed, please follow the following steps: 

    * Download MacOS [Python 2.7 installer](https://www.python.org/downloads/release/python-2716/) (depending on whether your system is 32bit/64bit). Once you have downloaded it, please install Python 2.7 using the installer.

    * Add pip for Python 2.7

    ```console
    $ curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip2.py
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                   Dload  Upload   Total   Spent    Left  Speed
     100 1863k  100 1863k    0     0  16.7M      0 --:--:-- --:--:-- --:--:-- 18.1M
    ```

    * Add the following to the `$PATH` variable on your Mac: `/Library/Frameworks/Python.framework/Versions/2.7/bin`

    * Download `plistlib.py`

   ```console
   $ curl https://raw.githubusercontent.com/python/cpython/2.7/Lib/plistlib.py -o 
   /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plistlib.py
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
   100 15185  100 15185    0     0  44274      0 --:--:-- --:--:-- --:--:-- 45193
   ```
    * Now try doing `python --version` on your command-line, and you should see version `2.7` printed.

2. Ensure that you have [Python 3.7](https://www.python.org/downloads/release/python-3711/) installed (Note: you can check this by running `python3 --version`). If Python 3.7 is not installed, download and run the latest Python 3.7 installer from https://www.python.org/downloads/mac-osx/.

3. Download [git](http://git-scm.com/download/mac), then run the package and follow instructions. This allows you to store the source in version control.

**Note:** While #1 above is only for those having MacOS >= 12.3, #2 and #3 should be done by everyone using a Mac for setting up Oppia. 

## Clone Oppia

1. Create a new, empty folder that will hold your Oppia work. Here, we call the folder `opensource`.

2. Navigate to the folder (`cd opensource/`).

3. Navigate to https://github.com/oppia/oppia and click on the `fork` button. It is placed on the right corner opposite the repository name `oppia/oppia`.

   ![Screenshot with the fork button](images/install/fork.png)

   You should now see Oppia under your repositories. It will be marked as forked from `oppia/oppia`.

   ![Screenshot of repository list with Oppia](images/install/repositoryList.png)

   For more information on forking, see [GitHub's documentation](https://help.github.com/articles/fork-a-repo/).

4. Clone the repository to your local computer (replacing the values in `{{}}`):

   ```console
   $ git clone https://github.com/{{GITHUB USERNAME}}/oppia.git
   Cloning into 'oppia'...
   remote: Enumerating objects: 203313, done.
   remote: Total 203313 (delta 0), reused 0 (delta 0), pack-reused 203313
   Receiving objects: 100% (203313/203313), 179.26 MiB | 3.12 MiB/s, done.
   Resolving deltas: 100% (155851/155851), done.
   Updating files: 100% (4199/4199), done.
   ```

   Note that you will see slightly different output because the numbers change as Oppia grows.

5. Now your `origin` remote is pointing to your fork (`{{GITHUB USERNAME}}/oppia`). To stay up to date with the main `oppia/oppia` repository, add it as a remote called `upstream`. You'll first need to move into the `oppia` directory that was created by the clone operation.

   ```console
   $ cd oppia
   $ git remote add upstream https://github.com/oppia/oppia.git
   $ git remote -v
   origin     https://github.com/{{GITHUB USERNAME}}/oppia.git (fetch)
   origin     https://github.com/{{GITHUB USERNAME}}/oppia.git (push)
   upstream   https://github.com/oppia/oppia.git (fetch)
   upstream   https://github.com/oppia/oppia.git (push)
   ```

   The `git remote -v` command at the end shows all your current remotes.

   Now you can pull in changes from `oppia/oppia` by running `git pull upstream {{branch}}` and push your changes to your fork by running `git push origin {{branch}}`.

   We have established a clean setup now. We can make any changes we like and push it to this forked repository, and then make a pull request for getting the changes merged into the original repository. Here's a nice picture explaining the process ([image source](https://github.com/Rafase282/My-FreeCodeCamp-Code/wiki/Lesson-Save-your-Code-Revisions-Forever-with-Git)).

   ![Diagram of the fork-and-clone workflow](images/install/forkCloneWorkflow.png)

   For making any changes to original repository, we first sync our cloned repository with original repository. We merge develop with `upstream/develop` to do this. Now we make a new branch, do the changes on the branch, push the branch to forked repository, and make a PR from Github interface. We use a different branch to make changes so that we can work on multiple issues while still having a clean version in develop branch.

## Setup a virtual environment

For your vitual environment, we recommend you use [pyenv](https://github.com/pyenv/pyenv). Here are some instructions for doing so, but you can use another virtual environment tool if you wish:

1. **Make sure you install the Python build dependencies for your operating system. These are specified [here](https://github.com/pyenv/pyenv/wiki#suggested-build-environment). If you don't do this it might lead to problems further on.**

2. Install pyenv. Note that if you use zsh as your shell (check by running `echo $SHELL`) you should replace `bash` with `zsh` below:

   ```console
   $ curl pyenv.run | bash
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
   100   270  100   270    0     0    630      0 --:--:-- --:--:-- --:--:--   632
   Cloning into '/home/user/.pyenv'...
   ...
   WARNING: seems you still have not added 'pyenv' to the load path.
   ...
   ```

   If you see the warning at the end, add the following lines to your `.bash_profile` (or `~/.zshrc` if you use zsh):

   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"

   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   ```

2. Reload your shell or open a new terminal window to load your updated `~/.bash_profile` or `~/.zshrc`.

3. If you have MacOS >= 12.3, install Python 3.7.13, otherwise install Python 3.7.10 and the associated pip using the command below: 

    `pyenv install <version>`, where `version` could be `3.7.13` (MacOS >= 12.3) or `3.7.10` (otherwise).
 
    This is how it looks like:  

   ```console
   $ pyenv install 3.7.10
   Downloading Python-3.7.10.tar.xz...
   -> https://www.python.org/ftp/python/3.7.10/Python-3.7.10.tar.xz
   Installing Python-3.7.10...
   Installed Python-3.7.10 to /home/user/.pyenv/versions/3.7.10
   ```

4. Create a virtual environment for oppia depending on the python version installed using the command below: 

    `pyenv virtualenv <python-version> oppia`, where `python-version` could be `3.7.13` or `3.7.10`

     This is how it looks like: 

   ```console
   $ pyenv virtualenv 3.7.10 oppia
   ...
   $ pyenv versions
   ...
   oppia
   ...
   ```

   In the cloned `oppia` folder, run

   ```console
   pyenv local oppia
   ```

   Now whenever you are within the `oppia` folder, the virtual environment will be active.

5. Install the Python dependencies:

   ```console
   $ pip install pyyaml setuptools
   Requirement already satisfied: setuptools in /home/user/.pyenv/versions/3.7.18/envs/oppia-tmp/lib/python2.7/site-packages (44.1.1)
   Collecting pyyaml
     Downloading PyYAML-5.4.1-cp27-cp27mu-manylinux1_x86_64.whl (574 kB)
        |████████████████████████████████| 574 kB 2.3 MB/s
   Installing collected packages: pyyaml
   Successfully installed pyyaml-5.4.1
   ```

6. If you want to run backend tests and check coverage, please install these 2 pip libraries globally (or in your venv).

   ```console
   pip install coverage configparser
   ```

## Running Oppia on a development server

1. In a terminal, navigate to `oppia/` and run:

   ```console
   python -m scripts.start
   ```

   The first time you run this script, it will take a while (about 5 - 10 minutes when we last tested it in Dec 2018, though this depends on your Internet connection). Subsequent runs should be much faster. The `start.py` script downloads and installs the required dependencies (such as Google App Engine) if they are not already present, and sets up a development server for you to play with. The development server logs are then output to this terminal, so you will not be able to enter further commands in it until you disconnect the server.

   **Note**: **Please don't use `sudo` while installing.** It's not required, and using it may cause problems later. If you face permissions issues, ensure that you have the necessary permissions for the directory in which you're trying to set up Oppia. If you run into any other installation problems, please read [[these notes|Issues-with-installation?]]

   **Note**: The script will create a number of files and folders that are siblings of the `oppia/` root directory (e.g. `oppia_tools`). This is done so that these two folders will not be uploaded to App Engine when the application is deployed to the web.

   **Note**: If you run into errors while installing Oppia, please try running `python -m scripts.clean` and then running `start.py` again.

   **Note**: Oppia uses the npm tool to install some packages. This tool accesses both ~/tmp and ~/.npm, and has been known to occasionally encounter permissions issues with those directories. You may need to either delete these directories and all their contents (if they do not contain anything else that needs to be preserved), or change their permissions so that they are owned by you, which you can do by running

   ```console
   sudo chown -R {{YOUR_USERNAME}} ~/tmp
   sudo chown -R {{YOUR_USERNAME}} ~/.npm
   ```

   where `{{YOUR_USERNAME}}` should be replaced by your username.

2. The `start.py` script will start a development server at http://localhost:8181. (If this doesn't happen automatically, try navigating directly to http://localhost:8181 in a browser once stuff stops being printed to the terminal.) It should look something like this:

   ![Image showing the default splash page.](https://res.cloudinary.com/dozmja9ir/image/upload/v1538254601/home_page.png)

   You can also view the App Engine admin console at http://localhost:8000.

   **Note:** There may be a few warnings that appear after running `start.py`. Don’t worry about these so long as you see the page once you go to http://localhost:8181. The script should continue to run so long as the development server is on (you’ll see a lot of lines that start with "INFO") and you’re able to navigate to the page.

3. When you're done, you can shut down the development server by typing Ctrl+C into the terminal. **Then wait for a command prompt to appear.** Oppia has to shut down all the services it's started, and if you abort the graceful shutdown steps (e.g. by typing Ctrl+C many times), you may have trouble re-starting the server.

   <details>
   <summary>Example of shutdown output</summary>

   ```text
   ^CINFO     2021-07-17 21:50:08,043 shutdown.py:50] Shutting down.
   INFO     2021-07-17 21:50:08,043 stub_util.py:377] Applying all pending transactions and saving the datastore
   INFO     2021-07-17 21:50:08,044 stub_util.py:380] Saving search indexes

   i  emulators: Received SIGINT (Ctrl-C) for the first time. Starting a clean shutdown.
   i  emulators: Please wait for a clean shutdown or send the SIGINT (Ctrl-C) signal again to stop right now.
   i  Automatically exporting data using --export-on-exit "/opensource/oppia/../firebase_emulator_cache" please wait for the export to finish...


   Servers are shutting down, please wait for them to end gracefully!


   i  Found running emulator hub for project dev-project-id at http://localhost:4400
   i  Creating export directory /opensource/firebase_emulator_cache
   i  Exporting data to: /opensource/firebase_emulator_cache
   i  emulators: Received export request. Exporting data to /opensource/firebase_emulator_cache.
   ✔  emulators: Export complete.
   ✔  Export complete
   i  emulators: Shutting down emulators.
   i  ui: Stopping Emulator UI
   ⚠  Emulator UI has exited upon receiving signal: SIGINT
   i  auth: Stopping Authentication Emulator
   i  hub: Stopping emulator hub
   i  logging: Stopping Logging Emulator
   Stopping Web Browser(name="open", pid=29306)...
   Stopping GAE Development Server(name="python2.7", pid=29289)...
   Stopping Webpack Compiler(name="node", pid=29234)...
   Stopping Firebase Emulator(name="node", pid=29216)...
   Stopping ElasticSearch Server(name="java", pid=29148)...
   Stopping Redis Server(name="redis-server", pid=29147)...


   Done! Thank you for waiting.


   Traceback (most recent call last):
     File "/Users/user/.pyenv/versions/3.7.10/lib/python3.7/runpy.py", line 174, in _run_module_as_main
       "__main__", fname, loader, pkg_name)
     File "/Users/user/.pyenv/versions/3.7.10/lib/python3.7/runpy.py", line 72, in _run_code
       exec code in run_globals
     File "/opensource/oppia/scripts/start.py", line 205, in <module>
       main()
     File "/opensource/oppia/scripts/start.py", line 201, in main
       dev_appserver.wait()
     File "/opensource/oppia/../oppia_tools/psutil-5.7.3/psutil/__init__.py", line 1350, in wait
       ret = super(Popen, self).wait(timeout)
     File "/opensource/oppia/../oppia_tools/psutil-5.7.3/psutil/__init__.py", line 1259, in wait
       self._exitcode = self._proc.wait(timeout)
     File "/opensource/oppia/../oppia_tools/psutil-5.7.3/psutil/_psosx.py", line 342, in wrapper
       return fun(self, *args, **kwargs)
     File "/opensource/oppia/../oppia_tools/psutil-5.7.3/psutil/_psosx.py", line 550, in wait
       return _psposix.wait_pid(self.pid, timeout, self._name)
     File "/opensource/oppia/../oppia_tools/psutil-5.7.3/psutil/_psposix.py", line 115, in wait_pid
       retpid, status = os.waitpid(pid, flags)
   KeyboardInterrupt
   ```

   </details>

## Tips and tricks

* To preserve the contents of the local datastore between consecutive runs, use the `--save_datastore` argument when starting up the dev server:

  ```console
  python -m scripts.start --save_datastore
  ```

* The default Oppia installation comes with a set of [demo explorations](https://github.com/oppia/oppia/tree/61f19354098669bcb408ef7b65fa50d92c076488/data/explorations). On startup, none of these are loaded. To load them, log in to your server as an admin, then click your username in the top-right corner and choose 'Admin Page'. This will open the admin page, from which you can load the demo explorations.
