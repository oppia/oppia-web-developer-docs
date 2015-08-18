# Installing Oppia on Linux #

**Note: if you would like to create explorations, we have a hosted server at https://www.oppia.org. Please note that all published explorations on this server are world-viewable.**

The installation instructions on this page were last tested on 25 Feb 2014 with Linux Ubuntu 12.04 LTS and Linux Fedora 19.

## Prerequisites ##

Oppia relies on a number of programs and third-party libraries. Many of these libraries are downloaded automatically for you when you run the `start.sh` script provided with Oppia. However, there are some things that you will need to do beforehand:

1. Ensure that you have [Python 2.7](http://www.python.org/download/releases/2.7/) and Java installed. (Java is needed for the code interaction.) If in doubt then, in a terminal run:
```
    sudo apt-get install default-jre
```

2. Make sure you have curl (which is used by the start.sh script for downloading third-party libraries), setuptools (which is needed to install coverage, which checks test coverage for the Python code) and git (which allows you to store the source in version control):
```
    sudo apt-get install curl python-setuptools git
```

## Running Oppia on a development server ##

1. Download Oppia by following the instructions in the [README](https://github.com/oppia/oppia#oppia).

2. In a terminal, navigate to the `oppia/` root directory and run:
```
     bash scripts/start.sh
```

The first time you run this script, it will take a while (about 5 - 10 minutes when we last tested it in Feb 2014, though this depends on your Internet connection). Subsequent runs should be much faster. The `start.sh` script downloads and installs the required dependencies (such as Google App Engine) if they are not already present, and sets up a development server for you to play with. The development server logs are then output to this terminal, so you will not be able to enter further commands in it until you disconnect the server.

**Note**: The script will create two folders that are siblings of the `oppia/` root directory: `oppia_tools` and `node_modules`. This is done so that these two folders will not be uploaded to App Engine when the application is deployed to the web.

**Note**: If you run into errors while installing Oppia, please try deleting the directories
```
     ../oppia_tools/
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

3. The `start.sh` script also opens up a development server at http://localhost:8181. At this address, you should see the welcome page and be able to play with your local version of Oppia. It should look something like this:

<img src='https://raw.githubusercontent.com/oppia/oppia/wiki/images/defaultDevPage.png' width='300'>

You can also view the App Engine admin console at http://localhost:8000.

4. *Loading the demo explorations.* The default installation of Oppia comes with a set of [demo explorations](https://github.com/oppia/oppia/tree/master/data/explorations). On startup, none of these are loaded. To load the demo explorations, log in to your server as an admin, then click your username in the top-right corner and choose the 'Admin Page' option. This will open a new admin page which will allow you to load the demo explorations individually.


5. *Shutting down the development server.* When you are done, you can shut down the development server by typing Ctrl+C into the terminal.

## Troubleshooting

  * If you get an error that ends with:
    ```
      fancy_urllib.InvalidCertificateException?: Host appengine.google.com returned an invalid certificate (ssl.c:507: error:14090086:SSL
      routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed):
    ```
    try removing the `cacerts.txt` and `urlfetch_cacerts.txt` files as described [here](http://stackoverflow.com/questions/13899530/gae-sdk-1-7-4-and-invalidcertificateexception) and [here](http://stackoverflow.com/questions/17777994/why-cant-i-launch-my-app-from-the-shell).
