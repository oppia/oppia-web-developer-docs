**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

*These installation instructions were last tested on 22 Feb 2016. For more information on issues that may occasionally arise with the installation process, please see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting) page.*

**Note:** Be careful about trying to install Oppia if you have the Python [Anaconda platform](https://www.anaconda.com/) installed. We've received a bunch of reports that installation is tricky in that environment (there are lots of small things that get in the way), and that the solution is to use the standard python installation (via e.g. homebrew) instead.

## Prerequisites ##

*The following instructions will install Oppia on your local machine. If you would like to run it in a virtual machine instead, we recommend the [Vagrant instructions](https://github.com/oppia/oppia/wiki/Installing-Oppia%28Vagrant%29).*

Oppia relies on a number of programs and third-party libraries. Many of these libraries are downloaded automatically for you when you run the `start.sh` script provided with Oppia. However, there are some things that you will need to do beforehand:

1. Ensure that you have [Python 2.7](http://www.python.org/download/releases/2.7/) installed (Note: you can check this by running `python --version`).

2. Install setuptools (which is needed to install coverage, which checks test coverage for the Python code), pip (which is needed to install numpy) and pyyaml (which is needed to parse YAML files). To do this, open the terminal and run:

  ```
    sudo easy_install setuptools
    sudo easy_install pip
    sudo easy_install pyyaml
  ```

3. Download [git](http://git-scm.com/download/mac), then run the package and follow instructions. This allows you to store the source in version control.


## Running Oppia on a development server ##

1. In a terminal, navigate to `oppia/` and run:

  ```
     bash scripts/start.sh
  ```

  The first time you run this script, it will take a while (about 5 - 10 minutes when we last tested it in Feb 2014, though this depends on your Internet connection). Subsequent runs should be much faster. The `start.sh` script downloads and installs the required dependencies (such as Google App Engine) if they are not already present, and sets up a development server for you to play with. The development server logs are then output to this terminal, so you will not be able to enter further commands in it until you disconnect the server.

  **Note**: The script will create two folders that are siblings of the `oppia/` root directory: `oppia_tools` and `node_modules`. This is done so that these two folders will not be uploaded to App Engine when the application is deployed to the web.

  **Note**: If you run into errors while installing Oppia, please try deleting the directories

  ```
    ../oppia_tools/
    ../node_modules/
    third_party/
    core/templates/prod/
  ```

  and running `start.sh` again.

  **Note**: Oppia uses the npm tool to install some packages. This tool accesses both ~/tmp and ~/.npm, and has been known to occasionally encounter permissions issues with those directories. You may need to either delete these directories and all their contents (if they do not contain anything else that needs to be preserved), or change their permissions so that they are owned by you, which you can do by running

  ```
    sudo chown -R {{YOUR_USERNAME}} ~/tmp
    sudo chown -R {{YOUR_USERNAME}} ~/.npm
  ```

  where `{{YOUR_USERNAME}}` should be replaced by your username.

2. The `start.sh` script will start a development server at http://localhost:8181. (If this doesn't happen automatically, try navigating directly to http://localhost:8181 in a browser once stuff stops being printed to the terminal.) It should look something like this:

  ![Image showing the default splash page.](https://res.cloudinary.com/dozmja9ir/image/upload/v1538254601/home_page.png)

  You can also view the App Engine admin console at http://localhost:8000.

3. *Loading the demo explorations.* The default Oppia installation comes with a set of [demo explorations](https://github.com/oppia/oppia/tree/master/data/explorations). On startup, none of these are loaded. To load them, log in to your server as an admin, then click your username in the top-right corner and choose 'Admin Page'. This will open the admin page, from which you can load the demo explorations.

4. *Shutting down the development server.* When you're done, you can shut down the development server by typing Ctrl+C into the terminal.

## Tips and tricks

  * To preserve the contents of the local datastore between consecutive runs, use the `--save_datastore` argument when starting up the dev server:

  ```
    bash scripts/start.sh --save_datastore
  ```

