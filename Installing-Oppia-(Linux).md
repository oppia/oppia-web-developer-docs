**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

*These installation instructions were last tested on 22 Feb 2016. For more information on issues that may occasionally arise with the installation process, please see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29#troubleshooting) section below.*

## Prerequisites ##

*The following instructions will install Oppia on your local machine. If you would like to run it in a virtual machine instead, we recommend the [Vagrant instructions](https://github.com/oppia/oppia/wiki/Installing-Oppia%28Vagrant%29).*

Oppia relies on a number of programs and third-party libraries. Many of these libraries are downloaded automatically for you when you run the `start.sh` script provided with Oppia. However, there are some things that you will need to do beforehand:

1. Ensure that you have [Python 2.7](http://www.python.org/download/releases/2.7/) installed.

2. Make sure you have curl (used to download third-party libraries), setuptools (needed for installing coverage, which checks test coverage for the Python code), git (which allows you to store the source in version control), python-dev (which is used for the numpy installation), python-pip (which is also used for the numpy installation) and pyyaml (which is used to parse YAML files):

  ```
    sudo apt-get install curl python-setuptools git python-dev python-pip python-yaml
  ```

Alternatively, if you are on Debian/Ubuntu, you can use the `install_prerequisites.sh` script to install these. From the oppia directory:

```
bash scripts/install_prerequisites.sh
```

## Running Oppia on a development server ##

1. Download Oppia by following the instructions in the [README](https://github.com/oppia/oppia#oppia).

2. In a terminal, navigate to `oppia/` and run:

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

3. The `start.sh` script will start a development server at http://localhost:8181. It should look something like this:

  ![Image showing the default splash page.](images/defaultDevPage.png)

  You can also view the App Engine admin console at http://localhost:8000.

4. *Loading the demo explorations.* The default Oppia installation comes with a set of [demo explorations](https://github.com/oppia/oppia/tree/master/data/explorations). On startup, none of these are loaded. To load them, log in to your server as an admin, then click your username in the top-right corner and choose 'Admin Page'. This will open the admin page, from which you can load the demo explorations.

5. *Shutting down the development server.* When you're done, you can shut down the development server by typing Ctrl+C into the terminal.

## Tips and tricks

  * To preserve the contents of the local datastore between consecutive runs, use the `--save_datastore` argument when starting up the dev server:

  ```
    bash scripts/start.sh --save_datastore
  ```

## Notes on installation on Arch Linux systems

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

Once this step is done, run `bash scripts/start.sh` to install other necessary files such as node modules and static js libraries and google app engine. Even after downloading everything server will fail to start and show errors. If you don’t see any errors then you have successfully setup Oppia in Arch and don’t have to execute following steps but it is highly likely that server won’t work.

### Fixing Python

In Arch, the `python` command refers to python 3 (in contrast to Ubuntu, where `python` refers to python 2). This has to be fixed. There are two ways to do so. One is to modify the python files and other is to modify system links.
1. Modify python (.py) files: two files have to be modified slightly here. First is dev_appserver.py file of the google app engine. Go to ‘oppia_tools/google_appengine_1.9.50/google_appengine’ and open ‘dev_appserver.py’ file. On the first line replace ‘python’ with ‘python2’. Secondly go to the ‘oppia/.git/hooks/prepush.py’ file and open it. On the very first line replace ‘python’ with ‘python2’.
2. Modify system links: go to the /usr/bin and type following command.
```
	# ln -sf python2 python
```

### Fix Google App Engine

Note: make sure you have already executed ‘bash scripts/start.sh’ before doing this step and all the necessary files were downloaded by the script. Basically at this point your Oppia server should start showing logs (error logs) in the terminal but you won’t be able to access Oppia in browser.

One of the highlights of Arch is that it is always up to date from linux to all packages. That is also the case with python2. Arch uses latest version of the python 2 which is 2.7.14. This version is incompatible with Google App Engine v1.9.50, currently used by Oppia. To fix this go to ‘oppia_tools/google_appengine_1.9.50/google_appengine/google/appengine/dist27’ and open ‘socket.py’ file. In this file go to the line 73 (or, alternatively, search for ‘RAND_egd’) and remove import of ‘RAND_egd’ from that line.

## Troubleshooting

  * If you get an error that ends with:

    ```
      fancy_urllib.InvalidCertificateException?: Host appengine.google.com returned
      an invalid certificate (ssl.c:507: error:14090086:SSL
      routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed):
    ```

    try removing the `cacerts.txt` and `urlfetch_cacerts.txt` files as described [here](http://stackoverflow.com/questions/13899530/gae-sdk-1-7-4-and-invalidcertificateexception) and [here](http://stackoverflow.com/questions/17777994/why-cant-i-launch-my-app-from-the-shell).

  * If you get an error that ends with:

    ```
    ssl.PROTOCOL_SSLv3: OpenSSL.SSL.SSLv3_METHOD,
    AttributeError: 'module' object has no attribute 'PROTOCOL_SSLv3'
    ```

    try commenting out the line

    ```
      '../oppia_tools/google_appengine_1.9.19/google_appengine/lib/requests/requests/packages/urllib3/contrib/pyopenssl.py:70': (ssl.PROTOCOL_SSLv3: OpenSSL.SSL.SSLv3_METHOD,)
    ```
    as described [here](https://code.google.com/p/googleappengine/issues/detail?id=11539#c2).

  * If you get an error that ends with:

    ```
      File "numpy/setup.py", line 5, in configuration
        config = Configuration('numpy',parent_package,top_path)
      File "/tmp/pip-build-4rsvws0b/numpy/build/py3k/numpy/distutils/misc_util.py", line 743, in __init__
        raise ValueError("%r is not a directory" % (package_path,))
    ValueError: 'build/py3k/numpy' is not a directory
    Converting to Python3 via 2to3...
    ```
    make sure that your default `pip` is using Python 2, not Python 3. See [#1742](https://github.com/oppia/oppia/issues/1742).

  * If you get an error that looks something like this:

    ```
    error: can't combine user with prefix, exec_prefix/home, or install_(plat)base

    ----------------------------------------
    Cleaning up...
    Command /usr/bin/python -c "import setuptools, tokenize;__file__='/tmp/pip-build-xiOWdq/numpy/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /tmp/pip-t7c_y1-record/install-record.txt --single-version-externally-managed --compile --user --home=/tmp/tmpP9jGIf failed with error code 1 in /tmp/pip-build-xiOWdq/numpy
    Traceback (most recent call last):
      File "/usr/bin/pip", line 9, in <module>
        load_entry_point('pip==1.5.6', 'console_scripts', 'pip')()
      File "/usr/lib/python2.7/dist-packages/pip/__init__.py", line 248, in main
        return command.main(cmd_args)
      File "/usr/lib/python2.7/dist-packages/pip/basecommand.py", line 161, in main
        text = '\n'.join(complete_log)
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 72: ordinal not in range(128)
    ```
    try updating the version of pip to v8.1.2 (as described in [this comment](https://github.com/oppia/oppia/issues/1580#issuecomment-218423065)).

  * If you get an error that ends with either:

    ```
    File "/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/command/install.py", line 264, in finalize_options
    "must supply either home or prefix/exec-prefix -- not both"
    DistutilsOptionError: must supply either home or prefix/exec-prefix -- not both
    ```

    or

    ```
    ImportError: No module named _ctypes
    ```

    please ensure that you are using Python 2. Also, if your system already has numpy installed, please ensure that its version is 1.6.1 (since that is the only one compatible with Google App Engine). For more details, see [this issue](https://github.com/oppia/oppia/issues/1545).

  * If you get an error that ends with:

    ```
    File "/oppia_tools/google_appengine_1.9.50/google_appengine/google/appengine/dist27/socket.py", line 73, in 
    from _ssl import RAND_add, RAND_egd, RAND_status, SSL_ERROR_ZERO_RETURN, SSL_ERROR_WANT_READ, SSL_ERROR_WANT_WRITE, SSL_ERROR_WANT_X509_LOOKUP, SSL_ERROR_SYSCALL, SSL_ERROR_SSL, SSL_ERROR_WANT_CONNECT, SSL_ERROR_EOF, SSL_ERROR_INVALID_ERROR_CODE
    ImportError: cannot import name RAND_egd
    ```
    go to `oppia_tools/google_appengine_1.9.50/google_appengine/google/appengine/dist27` and open the `socket.py` file. In this file go to the line 73 (or, alternatively, search for ‘RAND_egd’) and remove import of ‘RAND_egd’ from that line.

  * If you get 403 error while serving oppia locally:

    go to `oppia_tools/google_app_engine_1.9.XX/google_appengine/google/appengine/tools` and open the `appengine_rpc.py` file. Comment the following line in it. `opener.add_handler(fancy_urllib.FancyProxyHandler())` . Run the server again.
 [Resource](https://stackoverflow.com/questions/16698621/google-app-engine-error-httperror/17522082)
    