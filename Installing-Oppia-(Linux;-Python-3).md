## Table of Contents

* [Install prerequisites](#install-prerequisites)
* [Clone Oppia](#clone-oppia)
* [Setup a virtual environment](#setup-a-virtual-environment)
* [Running Oppia on a development server](#running-oppia-on-a-development-server)
* [Tips and tricks](#tips-and-tricks)
* [Notes on installation on Arch Linux systems](#notes-on-installation-on-arch-linux-systems)
  * [Changes to installation prerequisites](#changes-to-installation-prerequisites)
  * [Changes to the virtual environment setup](#changes-to-the-virtual-environment-setup)

**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

*These installation instructions were last tested on 8 January 2024. For more information on issues that may occasionally arise with the installation process, see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting) page or ask in the [GitHub Discussions](https://github.com/oppia/oppia/discussions).*

## Install prerequisites

Oppia relies on a number of programs and third-party libraries. Many of these libraries are downloaded automatically for you when you first run the `start.py` script provided with Oppia (see step 1 in the next section). However, there are some things that you will need to do beforehand:

1. Update your package list to the latest version by running:

```
sudo apt-get update
```

2. Make sure you have curl (used to download third-party libraries), setuptools (needed for installing coverage, which checks test coverage for the Python code), git (which allows you to store the source in version control), python-dev (which is used for the numpy installation), python-pip (which is also used for the numpy installation), pyyaml (which is used to parse YAML files) and libbz2-dev (used by Apache Beam):

```
sudo apt-get install python3-pip python3-setuptools curl openjdk-8-jre git python3-dev python3-yaml python3-matplotlib unzip libbz2-dev
```

Alternatively, if you are on Debian/Ubuntu, you can use the `install_prerequisites.sh` script to install these. From the oppia directory:

```
bash scripts/install_prerequisites.sh
```

3. Make sure that you have **Python 2** installed, it is needed for the dev server to run. On Ubuntu 20 you can install it using `sudo apt install python2`. On Ubuntu 18 you can install it using `sudo apt install python-minimal`. If both of these commands do not work, try using `sudo apt install python2-minimal`.

4. Install Chrome from [Google's website](https://www.google.com/chrome). You'll need this to run tests.

## Clone Oppia

1. Create a new, empty folder that will hold your Oppia work. Here, we call the folder `opensource`.

2. Navigate to the folder (`cd opensource/`). Next, we'll [fork and clone](https://help.github.com/articles/fork-a-repo/) the Oppia repository.

3. Navigate to https://github.com/oppia/oppia and click on the `fork` button. It is placed on the right corner opposite the repository name `oppia/oppia`.

   ![Screenshot with the fork button](images/install/fork.png)

   You should now see Oppia under your repositories. It will be marked as forked from `oppia/oppia`.

   ![Screenshot of repository list with Oppia](images/install/repositoryList.png)

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

   For developers who are using SSH to push to their git repository, please change the SSH config at `~/.ssh/config` to ensure that the git pre-push hook doesn't time out at 5 minutes. In order to do this, add the following lines to `~/.ssh/config` ([Reference](https://stackoverflow.com/a/65818657)):

   ```console
   Host*
      ServerAliveInterval 60
      ServerAliveCountMax 30
   ```

   Now you can pull in changes from `oppia/oppia` by running `git pull upstream {{branch}}` and push your changes to your fork by running `git push origin {{branch}}`.

   We have established a clean setup now. We can make any changes we like and push it to this forked repository, and then make a pull request for getting the changes merged into the original repository. Here's a nice picture explaining the process ([image source](https://github.com/Rafase282/My-FreeCodeCamp-Code/wiki/Lesson-Save-your-Code-Revisions-Forever-with-Git)).

   ![Diagram of the fork-and-clone workflow](images/install/forkCloneWorkflow.png)

   For making any changes to original repository, we first sync our cloned repository with original repository. We merge develop with `upstream/develop` to do this. Now we make a new branch, do the changes on the branch, push the branch to forked repository, and make a PR from Github interface. We use a different branch to make changes so that we can work on multiple issues while still having a clean version in develop branch.

## Setup a virtual environment

For your virtual environment, we recommend you use [pyenv](https://github.com/pyenv/pyenv). Here are some instructions for doing so, but you can use another virtual environment tool if you wish:
   > [NOTE!]
   > The commands below can be executed in any directory, as they are not path-specific.
1. **Make sure you install the Python build dependencies for your operating system. These are specified [here](https://github.com/pyenv/pyenv/wiki#suggested-build-environment). If you don't do this it might lead to problems further on.** The build dependencies for Ubuntu/Debian are


   ```
   sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
   ```

2. Install pyenv:

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

   If you see the warning at the end, add the following lines to your ``>> ~/.bashrc`` (if you are using bash) or ``>> ~/.zshrc`` (if you are using zsh).

   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"

   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   ```

   > [!WARNING]
   > Be careful with using graphical editors like Notepad in Windows. These can add carriage returns (`\r`) that confuse our Linux-based development tools. Instead, we recommend using editors designed for programming or command-line text editors.

3. Reload your shell or open a new terminal window to load your updated `~/.bashrc` or `~/.zshrc`.
```bash
exec "$SHELL"
```
4. Now you can install Python 3.9.20 and the associated pip like this:

   ```console
   $ pyenv install 3.9.20
   installing python-3.9.20...
   installed python-3.9.20 to /home/user/.pyenv/versions/3.9.20
   ```

5. Install direnv

   ```sh
   sudo apt install direnv
   ```

6. Setup direnv into your shell.  
   If you are using bash:

   ```bash
   eval "$(direnv hook bash)" >> ~/.bashrc
   ```
   If you are using zsh:

   ```bash
   eval "$(direnv hook zsh)" >> ~/.zshrc
   ``` 
   > [!WARNING]
   > Be careful with using graphical editors like Notepad in Windows. These can add carriage returns (`\r`) that confuse our Linux-based development tools. Instead, we recommend using editors designed for programming or command-line text editors.

7. Add new file called `.direnvrc` into your home (`~`) folder with this content:
   ```bash
   use_python() {
     local python_root=$(pyenv root)/versions/$1
     load_prefix "$python_root"
     if [[ -x "$python_root/bin/python" ]]; then
       layout python "$python_root/bin/python"
     else
       echo "Error: $python_root/bin/python can't be executed."
       exit
     fi
   }
   ```

   > [!WARNING]
   > Be careful with using graphical editors like Notepad in Windows. These can add carriage returns (`\r`) that confuse our Linux-based development tools. Instead, we recommend using editors designed for programming or command-line text editors.

8. Create a virtual environment for oppia by adding file named `.envrc` into the parent folder of the oppia repository
   with this content:

    ```console
    use python 3.9.20
    ```

    Then run this command in the same folder:

    ```sh
    direnv allow
    ```

    Now whenever you are within the `oppia` folder, the virtual environment will be active.

9. Install the Python dependencies:

    ```console
    $ pip install pyyaml setuptools
    Requirement already satisfied: setuptools in /home/user/.pyenv/versions/2.7.18/envs/oppia-tmp/lib/python2.7/site-packages (44.1.1)
    Collecting pyyaml
      Downloading PyYAML-5.4.1-cp27-cp27mu-manylinux1_x86_64.whl (574 kB)
         |████████████████████████████████| 574 kB 2.3 MB/s
    Installing collected packages: pyyaml
    Successfully installed pyyaml-5.4.1
    ```

    Note that you don't need to install pyyaml if you were able to install python-yaml with your package manager earlier.

10. If you want to run backend tests and check coverage, please install these 2 pip libraries:

    ```console
    pip install coverage configparser
    ```

## Running Oppia on a development server

1. In a terminal, navigate to `oppia/` and run:

   ```console
   python -m scripts.start
   ```

   > [[!IMPORTANT]
   > If you are using **Windows**, you will need to run `python -m scripts.start --no_browser` instead. This is because Windows does not support the `xdg-open` command that the script uses to open a browser window.

   The first time you run this script, it will take a while -- about 5 - 10 minutes when we last tested it in Sep 2020, though this depends on your Internet connection. (It might also hang after "Checking if pip is installed on the local machine" due to the grpcio build being slow -- just give it some time, and it should finish.) Subsequent runs should be much faster. The `start.py` script downloads and installs the required dependencies (such as Google App Engine) if they are not already present, and sets up a development server for you to play with. The development server logs are then output to this terminal, so you will not be able to enter further commands in it until you disconnect the server.

   > [!CAUTION]
   > **Please don't use `sudo` while installing.** It's not required, and using it may cause problems later. If you face permissions issues, ensure that you have the necessary permissions for the directory in which you're trying to set up Oppia. If you run into any other installation problems, please read [these notes](https://github.com/oppia/oppia/wiki/Issues-with-installation).

   > [!NOTE]
   > The script will create a number of files and folders that are siblings of the `oppia/` root directory (e.g. `oppia_tools`). This is done so that these files and folders will not be uploaded to App Engine when the application is deployed to the web.

   > [!TIP]
   > If you run into errors while installing Oppia, please try running `python -m scripts.clean` and running `start.py` again.

   > [!NOTE]
   > Oppia uses the npm tool to install some packages. This tool accesses both ~/tmp and ~/.npm, and has been known to occasionally encounter permissions issues with those directories. You may need to either delete these directories and all their contents (if they do not contain anything else that needs to be preserved), or change their permissions so that they are owned by you, which you can do by running

   ```console
   sudo chown -R {{YOUR_USERNAME}} ~/tmp
   sudo chown -R {{YOUR_USERNAME}} ~/.npm
   ```

   where `{{YOUR_USERNAME}}` should be replaced by your username.

2. The `start.py` script will start a development server at http://localhost:8181. It should look something like this:

   ![Image showing the default splash page.](https://user-images.githubusercontent.com/57531197/213922682-5ce66f8f-6a5d-493f-8f7c-fa1a566bb6f9.png)

   You can also view the App Engine admin console at http://localhost:8000.

   **Note:** There may be a few warnings that appear after running `start.py`. Don’t worry about these so long as you see the page above once you go to http://localhost:8181. The script should continue to run so long as the development server is on (you’ll see a lot of lines that start with "INFO") and you’re able to navigate to the page.

3. When you're done, you can shut down the development server by typing Ctrl+C into the terminal. **Then wait for a command prompt to appear.** Oppia has to shut down all the services it's started, and if you abort the graceful shutdown steps (e.g. by typing Ctrl+C many times), you may have trouble re-starting the server.

   <details>
   <summary>Example shutdown output</summary>

   ```text
   ^CINFO     2021-07-19 00:31:32,627 shutdown.py:50] Shutting down.
   INFO     2021-07-19 00:31:32,627 stub_util.py:377] Applying all pending transactions and saving the datastore
   INFO     2021-07-19 00:31:32,628 stub_util.py:380] Saving search indexes

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
   Stopping Web Browser(name="xdg-open", pid=14416)...
   Stopping GAE Development Server(name="sh", pid=14405)...
   Stopping Webpack Compiler(name="sh", pid=14338)...
   Stopping Firebase Emulator(name="sh", pid=14311)...
   Stopping ElasticSearch Server(name="sh", pid=14060)...
   Stopping Redis Server(name="sh", pid=14045)...


   Done! Thank you for waiting.


   Traceback (most recent call last):
     File "/home/user/.pyenv/versions/2.7.18/lib/python2.7/runpy.py", line 174, in _run_module_as_main
       "__main__", fname, loader, pkg_name)
     File "/home/user/.pyenv/versions/2.7.18/lib/python2.7/runpy.py", line 72, in _run_code
       exec code in run_globals
     File "/opensource/oppia/scripts/start.py", line 202, in <module>
       main()
     File "/opensource/oppia/scripts/start.py", line 198, in main
       dev_appserver.wait()
     File "/opensource/oppia/../oppia_tools/psutil-5.7.3/psutil/__init__.py", line 1350, in wait
       ret = super(Popen, self).wait(timeout)
     File "/opensource/oppia/../oppia_tools/psutil-5.7.3/psutil/__init__.py", line 1259, in wait
       self._exitcode = self._proc.wait(timeout)
     File "/opensource/oppia/../oppia_tools/psutil-5.7.3/psutil/_pslinux.py", line 1517, in wrapper
       return fun(self, *args, **kwargs)
     File "/opensource/oppia/../oppia_tools/psutil-5.7.3/psutil/_pslinux.py", line 1725, in wait
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

* The default Oppia installation comes with a set of [demo explorations](https://github.com/oppia/oppia/tree/master/data/explorations). On startup, none of these are loaded. To load them, log in to your server as an admin, then click your username in the top-right corner and choose 'Admin Page'. This will open the admin page, from which you can load the demo explorations.

## Notes on installation on Arch Linux systems

_The following notes are thanks to @ashish-patwal. They come with no guarantees, and may change some settings on your local machine, so please make sure you fully understand their ramifications before following them!_

### Changes to installation prerequisites

Arch uses pacman as its package manager, so the `install_prerequisites.sh` script is not going to work. Instead, all of the prerequisites have to be installed manually using pacman. Just type the following command in the shell (notation: `#` denotes sudo access while `$` denotes normal user access):

```console
# pacman -Sy curl jre8-openjdk python-setuptools git python-pip python-yaml unzip python-matplotlib
```

Also, note that pacman doesn't support Google Chrome (which is needed to run frontend and end-to-end tests) in the default package manager. However, you can use the chromium package instead; chromium is the open-source core of Google Chrome. Install the chromium browser and then create a soft link from the google-chrome command to chromium:

```console
# pacman -Sy chromium
# cd /usr/bin
# ln -sf chromium google-chrome
```

### Changes to the virtual environment setup

On Arch Linux, you should follow these instructions to set up your virtual environment:

1. **Make sure you install the Python build dependencies for your operating system. These are specified [here](https://github.com/pyenv/pyenv/wiki#suggested-build-environment). If you don't do this it might lead to problems further on.**

2. Install pyenv (notation: `#` denotes sudo access while `$` denotes normal user access):

   ```console
   # pacman -S pyenv
   ```

   Install pyenv-virtualenv either with `yay` or `pacaur`:

   ```console
   $ yay -S pyenv-virtualenv
   ```

   ```
   $ pacaur -S pyenv-virtualenv
   ```

   **Bash / Zsh**

   Add the following lines to your `~/.bashrc` or `.zshrc`

   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"

   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   ```

   **Fish**

   Execute this interactively :

   ```bash
   set -Ux PYENV_ROOT $HOME/.pyenv
   set -U fish_user_paths $PYENV_ROOT/bin $fish_user_paths
   ```

   And add this to `~/.config/fish/config.fish`

   ```bash
   status is-interactive; and pyenv init --path | source
   pyenv init - | source
   eval "$(pyenv virtualenv-init -)"
   ```

3. Reload your shell or open a new terminal window to load your updated `.bashrc`, `.zshrc`, or `config.fish`

4. Now you can install Python 3.9.20 and the associated pip like this:

   ```console
   $ pyenv install 3.9.20
   installing python-3.9.20...
   patching file misc/news.d/next/build/2021-10-11-16-27-38.bpo-45405.isfdw5.rst
   patching file configure
   patching file configure.ac
   installed python-3.9.20 to /home/user/.pyenv/versions/3.8.1
   ```

5. Create a virtual environment for oppia:

   ```console
   $ pyenv virtualenv 3.9.20 oppia
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

6. Install the Python dependencies:

   ```console
   $ pip install pyyaml setuptools
   Requirement already satisfied: setuptools in /home/user/.pyenv/versions/2.7.18/envs/oppia-tmp/lib/python2.7/site-packages (44.1.1)
   Collecting pyyaml
     Downloading PyYAML-5.4.1-cp27-cp27mu-manylinux1_x86_64.whl (574 kB)
        |████████████████████████████████| 574 kB 2.3 MB/s
   Installing collected packages: pyyaml
   Successfully installed pyyaml-5.4.1
   ```

   **Note that you don't need to install pyyaml if you were able to install python-yaml with your package manager earlier.**

7. If you want to run backend tests and check coverage, please install these 2 pip libraries:

   ```console
   pip install coverage configparser
   ```
