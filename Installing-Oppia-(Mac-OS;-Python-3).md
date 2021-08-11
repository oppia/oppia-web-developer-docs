**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).
 
*These installation instructions were last tested on 3 Dec 2018. For more information on issues that may occasionally arise with the installation process, please see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting) page. Thanks to Varun Tandon for updating these instructions!* **These instructions are not up-to-date with Python 3 that Oppia now uses. Please consult the [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-(Linux;-Python-3)) instructions and try to modify them for Mac.**
 
**Note:** Be careful about trying to install Oppia if you have the Python [Anaconda platform](https://www.anaconda.com/) installed. We've received a bunch of reports that installation is tricky in that environment (there are lots of small things that get in the way), and that the solution is to use the standard python installation (via e.g. homebrew) instead.

## Note: Mac with M1 chips ##

1. [Install](https://stackoverflow.com/a/64883440) Rosetta 2
2. Inside Rosetta perform the Downloading and prerequisites steps
   (**Note:** If `sudo easy_install pyyaml` does not work try using `pip3 install pyyaml`).
3. Open the rosetta terminal and run `python -m scripts.start`

## Downloading Oppia ##

1. Create a new, empty folder called `opensource/` in your computer's home folder. 

1. Navigate to it (`cd opensource`), then [fork and clone](https://help.github.com/articles/fork-a-repo/) ([why?](https://github.com/oppia/oppia/wiki/Why-fork-and-clone-Oppia%3F)) the Oppia repo so that it gets downloaded into `opensource/oppia`. 

1. Navigate to this folder (`cd oppia`) and run `git remote add upstream https://github.com/oppia/oppia.git` (or, if you're using SSH, use `git@github.com:oppia/oppia.git`) to add an `upstream` remote that's linked to Oppia's main repository. (This will be necessary when submitting PRs later.) 

 
## Prerequisites ##
 
*The following instructions will install Oppia on your local machine.*
 
Oppia relies on a number of programs and third-party libraries. Many of these libraries are downloaded automatically for you when you first run the `start.py` script provided with Oppia. However, there are some things that you will need to do beforehand:
 
1. Ensure that you have [Python 3.7](https://www.python.org/downloads/release/python-3711/) installed (Note: you can check this by running `python --version`). If Python 3.7 is not installed, download and run the latest Python 3.7 installer from https://www.python.org/downloads/mac-osx/.
 
2. Install setuptools (which is needed to install coverage, which checks test coverage for the Python code) and pyyaml (which is needed to parse YAML files). To do this, open the terminal and run:
 
    ```
    sudo easy_install setuptools
    sudo easy_install pyyaml
    ```
 
3. Download [git](http://git-scm.com/download/mac), then run the package and follow instructions. This allows you to store the source in version control.
 
4. Set up a virtual environment (virtualenv) for your Oppia dependencies. This ensures that conflicting versions of Python, pip, or any Python modules on your machine do not result in installation issues.

    In the `opensource/` folder (**note**: this is the **parent directory** of oppia/) run:

    ```
    pip2 install virtualenv
    python2 -m virtualenv env
    ```
    This creates a Python 2 virtual environment named "env" in your `opensource/` directory. Now, anytime you need to work with the Oppia code base, you should activate the virtualenv in `opensource/` by running
    
    ```
    source env/bin/activate
    ```
    
    If this is successful, the usual `YOURMACBOOK-NAME:directory$` at the start of the terminal line will be replaced with `(env) YOURMACBOOK-NAME:directory$`
    
    The following steps of installation and running the development server should all be done within this virtual environment to ensure compatibility.


## Running Oppia on a development server ##
 
1. In a terminal, navigate to `oppia/` and run:
 
  ```
     python -m scripts.start
  ```
 
  The first time you run this script, it will take a while (about 5 - 10 minutes when we last tested it in Dec 2018, though this depends on your Internet connection). Subsequent runs should be much faster. The `start.py` script downloads and installs the required dependencies (such as Google App Engine) if they are not already present, and sets up a development server for you to play with. The development server logs are then output to this terminal, so you will not be able to enter further commands in it until you disconnect the server.

  **Note**: **Please don't use `sudo` while installing.** It's not required, and using it may cause problems later. If you face permissions issues, ensure that you have the necessary permissions for the directory in which you're trying to set up Oppia.

  **Note**: The script will create two folders that are siblings of the `oppia/` root directory: `oppia_tools` and `node_modules`. This is done so that these two folders will not be uploaded to App Engine when the application is deployed to the web.
 
  **Note**: If you run into errors while installing Oppia, please try deleting the directories
 
  ```
    ../oppia_tools/
    node_modules/
    third_party/
  ```
 
  and running `start.py` again.
 
  **Note**: Oppia uses the npm tool to install some packages. This tool accesses both ~/tmp and ~/.npm, and has been known to occasionally encounter permissions issues with those directories. You may need to either delete these directories and all their contents (if they do not contain anything else that needs to be preserved), or change their permissions so that they are owned by you, which you can do by running
 
  ```
    sudo chown -R {{YOUR_USERNAME}} ~/tmp
    sudo chown -R {{YOUR_USERNAME}} ~/.npm
  ```
 
  where `{{YOUR_USERNAME}}` should be replaced by your username.

2. The `start.py` script will start a development server at http://localhost:8181. (If this doesn't happen automatically, try navigating directly to http://localhost:8181 in a browser once stuff stops being printed to the terminal.) It should look something like this:
 
  ![Image showing the default splash page.](https://res.cloudinary.com/dozmja9ir/image/upload/v1538254601/home_page.png)
 
  You can also view the App Engine admin console at http://localhost:8000.

  **Note:** There may be a few warnings that appear after running `start.py`. Don’t worry about these so long as you see the page once you go to http://localhost:8181. The script should continue to run so long as the development server is on (you’ll see a lot of lines that start with “INFO”) and you’re able to navigate to the page. 
 
3. *Loading the demo explorations.* The default Oppia installation comes with a set of [demo explorations](https://github.com/oppia/oppia/tree/61f19354098669bcb408ef7b65fa50d92c076488/data/explorations). On startup, none of these are loaded. To load them, log in to your server as an admin, then click your username in the top-right corner and choose 'Admin Page'. This will open the admin page, from which you can load the demo explorations.
 
4. *Shutting down the development server.* When you're done, you can shut down the development server by typing Ctrl+C into the terminal.

5. If you want to run backend tests and check coverage, please install these 2 pip libraries globally (or in your venv).
```
pip install coverage configparser
```


## Tips and tricks
 
  * To preserve the contents of the local datastore between consecutive runs, use the `--save_datastore` argument when starting up the dev server:
 
  ```
    python -m scripts.start --save_datastore
  ```