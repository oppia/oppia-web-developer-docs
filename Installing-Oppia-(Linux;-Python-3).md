**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

*These installation instructions were last tested on 24 July 2021. For more information on issues that may occasionally arise with the installation process, please contact _vojtech.jelinek@hey.com_ or see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting) page (but that page is not yet updated for Python 3).*

## Downloading Oppia ##

1. Create a new, empty folder called `oppia/` in your computer's home folder. If you already use `oppia/` for Python 2 Oppia feel free to use some different folder name. 

1. Navigate to it (`cd oppia`), then [fork and clone](https://help.github.com/articles/fork-a-repo/) ([why?](https://github.com/oppia/oppia/wiki/Why-fork-and-clone-Oppia%3F)) the Oppia repo so that it gets downloaded into `oppia/oppia`. 

1. Navigate to this folder (`cd oppia`) and run `git remote add upstream https://github.com/oppia/oppia.git` (or, if you're using SSH, use `git@github.com:oppia/oppia.git`) to add an `upstream` remote that's linked to Oppia's main repository. (This will be necessary when submitting PRs later.)


## Prerequisites ##

_The following instructions will install Oppia on your local machine._

Oppia relies on a number of programs and third-party libraries. Many of these libraries are downloaded automatically for you when you first run the `start.py` script provided with Oppia (see step 1 in the next section). However, there are some things that you will need to do beforehand:

1. We heavily recommend usage of virtual environment for working with Oppia. Here is a short guide for using [direnv](https://direnv.net/):
    
    1. Install direnv for you OS using this [installation guide](https://direnv.net/docs/installation.html).
    2. Hook direnv into your shell using this [setup guide](https://direnv.net/docs/hook.html).
    3. Install pyenv by using [this guide](https://github.com/pyenv/pyenv-installer#install).
        - **Do not install pyenv using snap as it can lead to problems.**
    4. Install Python 3.7.10 by running `pyenv install 3.7.10`.
        - In some cases there might be some problems installing the versions and you might need to prepare your guild environment first, to do so follow this [guide from pyenv](https://github.com/pyenv/pyenv/wiki#suggested-build-environment).
        - **Make sure that "BUILD FAILED" is not in the output of `pyenv install 3.7.10`. If it is look at other errors in the output and consult [pyenv wiki](https://github.com/pyenv/pyenv/wiki/Common-build-problems).**
    5. Verify that Python 3.7.10 was installed by running `pyenv versions`, the 3.7.10 should be listed there.
    5. Run this command to download .direnvrc `curl https://gist.githubusercontent.com/vojtechjelinek/104017176ecf2507f7e0e303b09e00d4/raw/841ff41a12791fa1a1d8621a4639bd3c9931404b/.direnvrc > ~/.direnvrc`.
    6. In `oppia/` folder (NOT `oppia/oppia`) add a file named .envrc and add this line into it `use python 3.7.10`.
    7. Run `direnv allow`.
    8. Now you should have a virtual environment that will be enabled when you enter the oppia folder.

2. Make sure you have curl (used to download third-party libraries), setuptools (needed for installing coverage, which checks test coverage for the Python code), git (which allows you to store the source in version control), python-dev (which is used for the numpy installation), python-pip (which is also used for the numpy installation) and pyyaml (which is used to parse YAML files):

  ```
    sudo apt-get install curl openjdk-8-jre python3-setuptools git python3-dev python3-pip python3-yaml unzip python-matplotlib python3-matplotlib
  ```

Alternatively, if you are on Debian/Ubuntu, you can use the `install_prerequisites.sh` script to install these. From the oppia directory:

```
bash scripts/install_prerequisites.sh
```


3. If you want to run backend tests and check coverage, please install these 2 pip libraries globally (or in your venv).
```
pip install coverage configparser
```
## Running Oppia on a development server ##

1. In a terminal, navigate to `oppia/` and run:

  ```
     python -m scripts.start
  ```

  The first time you run this script, it will take a while -- about 5 - 10 minutes when we last tested it in Sep 2020, though this depends on your Internet connection. (It might also hang after "Checking if pip is installed on the local machine" due to the grpcio build being slow -- just give it some time, and it should finish.) Subsequent runs should be much faster. The `start.py` script downloads and installs the required dependencies (such as Google App Engine) if they are not already present, and sets up a development server for you to play with. The development server logs are then output to this terminal, so you will not be able to enter further commands in it until you disconnect the server.

  **Note**: **Please don't use `sudo` while installing.** It's not required, and using it may cause problems later. If you face permissions issues, ensure that you have the necessary permissions for the directory in which you're trying to set up Oppia. If you run into any other installation problems, please read [these notes](https://github.com/oppia/oppia/wiki/Issues-with-installation%3F).

  **Note**: The script will create two folders that are siblings of the `oppia/` root directory: `oppia_tools` and `node_modules`. This is done so that these two folders will not be uploaded to App Engine when the application is deployed to the web.
  
  **Note**: If you run into errors while installing Oppia, please try running `python -m scripts.clean` and running `start.py` again.

  **Note**: Oppia uses the npm tool to install some packages. This tool accesses both ~/tmp and ~/.npm, and has been known to occasionally encounter permissions issues with those directories. You may need to either delete these directories and all their contents (if they do not contain anything else that needs to be preserved), or change their permissions so that they are owned by you, which you can do by running

  ```
    sudo chown -R {{YOUR_USERNAME}} ~/tmp
    sudo chown -R {{YOUR_USERNAME}} ~/.npm
  ```

  where `{{YOUR_USERNAME}}` should be replaced by your username.

2. The `start.py` script will start a development server at http://localhost:8181. It should look something like this:

  ![Image showing the default splash page.](https://res.cloudinary.com/dozmja9ir/image/upload/v1538254601/home_page.png)

  You can also view the App Engine admin console at http://localhost:8000.

  **Note:** There may be a few warnings that appear after running `start.py`. Don’t worry about these so long as you see the page above once you go to http://localhost:8181. The script should continue to run so long as the development server is on (you’ll see a lot of lines that start with “INFO”) and you’re able to navigate to the page. 

3. *Loading the demo explorations.* The default Oppia installation comes with a set of [demo explorations](https://github.com/oppia/oppia/tree/master/data/explorations). On startup, none of these are loaded. To load them, log in to your server as an admin, then click your username in the top-right corner and choose 'Admin Page'. This will open the admin page, from which you can load the demo explorations.

4. *Shutting down the development server.* When you're done, you can shut down the development server by typing Ctrl+C into the terminal.

## Tips and tricks

  * To preserve the contents of the local datastore between consecutive runs, use the `--save_datastore` argument when starting up the dev server:

  ```
    python -m scripts.start --save_datastore
  ```

## Notes on installation on Arch Linux systems

**THIS PART IS NOT UPDATED FOR PYTHON 3!**

_The following notes are thanks to Prasanna Patil (@prasanna08). They come with no guarantees, and may change some settings on your local machine, so please make sure you fully understand their ramifications before following them!_

### Installation prerequisites

Arch uses pacman as package manager, so the install_prerequisites.sh script is not going to work and all of the prerequisites have to be installed manually using pacman. Just type the following command in the shell (notation: # denotes sudo access while $ denotes normal user access):

```
   # pacman -Sy python2 python2-pip python2-setuptools curl jre7-openjdk unzip git python2-yaml
```

Also, note that pacman doesn't support google chrome in the default package manager (which is needed to run frontend and e2e tests). However, you can use the chromium package instead; this is an open-source fork of google chrome. Here's how to do it -- install the chromium browser, and then create a soft link from the google-chrome command to chromium:

```
   # pacman -Sy chromium
   # cd /usr/bin
   # ln -sf chromium google-chrome
```

If you do want to use google chrome instead, you could also use the third-party repository AUR (with the help of yaourt).

### Install 3rd party libraries

Arch uses the pip command for pip 3 (which installs libraries for python 3) and pip2 command for python 2, so we have to install all necessary (python’s) 3rd party libraries manually. For this go to the ‘oppia_tools’ directory and open a terminal and type following commands (note: make sure that you are in oppia_tools folder).

```
  $ pip2 install pylint==1.7.1 --target="./pylint-1.7.1"
  $ pip2 install numpy==1.6.1 --target="./numpy-1.6.1"
  $ pip2 install browsermob-proxy==0.7.1 --target="./browsermob-proxy-0.7.1"
  $ pip2 install selenium==2.53.2 --target="./selenium-2.53.2"
  $ curl -o webtest-download.zip -L https://github.com/Pylons/webtest/archive/1.4.2.zip
  $ unzip webtest-download.zip -d .
  $ rm webtest-download.zip
  $ touch ./pylint-1.7.1/backports/__init__.py
```

Once this step is done, run `python -m scripts.start` to install other necessary files such as node modules and static js libraries and google app engine. Even after downloading everything server will fail to start and show errors. If you don’t see any errors then you have successfully setup Oppia in Arch and don’t have to execute following steps but it is highly likely that server won’t work.

### Fixing Python

In Arch, the `python` command refers to python 3 (in contrast to Ubuntu, where `python` refers to python 2). This has to be fixed. There are two ways to do so. One is to modify the python files and other is to modify system links.
1. Modify python (.py) files: two files have to be modified slightly here. First is dev_appserver.py file of the google app engine. Go to ‘oppia_tools/google_appengine_1.9.50/google_appengine’ and open ‘dev_appserver.py’ file. On the first line replace ‘python’ with ‘python2’. Secondly go to the ‘oppia/.git/hooks/prepush.py’ file and open it. On the very first line replace ‘python’ with ‘python2’.
2. Modify system links: go to the /usr/bin and type following command.
```
	# ln -sf python2 python
```

### Fix Google App Engine

Note: make sure you have already executed ‘python -m scripts.start’ before doing this step and all the necessary files were downloaded by the script. Basically at this point your Oppia server should start showing logs (error logs) in the terminal but you won’t be able to access Oppia in browser.

One of the highlights of Arch is that it is always up to date from linux to all packages. That is also the case with python2. Arch uses latest version of the python 2 which is 2.7.14. This version is incompatible with Google App Engine v1.9.50, currently used by Oppia. To fix this go to ‘oppia_tools/google_appengine_1.9.50/google_appengine/google/appengine/dist27’ and open ‘socket.py’ file. In this file go to the line 73 (or, alternatively, search for ‘RAND_egd’) and remove import of ‘RAND_egd’ from that line.

   