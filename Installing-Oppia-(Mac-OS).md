**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

*The installation instructions on this page were last tested on 2 Feb 2016. For more information on issues that may occasionally arise with the installation process, please see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29#troubleshooting) section below.*

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

1. Follow the instructions in the [README](https://github.com/oppia/oppia#oppia).

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

## Troubleshooting

  * If you get an error that ends with:

    ```
      fancy_urllib.InvalidCertificateException?: Host appengine.google.com returned
      an invalid certificate (ssl.c:507: error:14090086:SSL
      routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed):
    ```

    try removing the `cacerts.txt` and `urlfetch_cacerts.txt` files as described [here](http://stackoverflow.com/questions/13899530/gae-sdk-1-7-4-and-invalidcertificateexception) and [here](http://stackoverflow.com/questions/17777994/why-cant-i-launch-my-app-from-the-shell).

  * If you get an error that includes:

    ```
    clang: error: invalid argument '-faltivec' only allowed with 'ppc/ppc64/ppc64le'
    clang: error: invalid argument '-faltivec' only allowed with 'ppc/ppc64/ppc64le'
    clang: error: invalid argument '-faltivec' only allowed with 'ppc/ppc64/ppc64le'
    clang: error: invalid argument '-faltivec' only allowed with 'ppc/ppc64/ppc64le'
    error: Command "gcc -fno-strict-aliasing -fno-common -dynamic -arch x86_64 -arch i386 -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -fwrapv -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE -arch x86_64 -arch i386 -pipe -DNO_ATLAS_INFO=3 -Inumpy/core/blasdot -Inumpy/core/include -Ibuild/src.macosx-10.10-intel-2.7/numpy/core/include/numpy -Inumpy/core/src/private -Inumpy/core/src -Inumpy/core -Inumpy/core/src/npymath -Inumpy/core/src/multiarray -Inumpy/core/src/umath -Inumpy/core/include -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -Ibuild/src.macosx-10.10-intel-2.7/numpy/core/src/multiarray -Ibuild/src.macosx-10.10-intel-2.7/numpy/core/src/umath -c numpy/core/blasdot/_dotblas.c -o build/temp.macosx-10.10-intel-2.7/numpy/core/blasdot/_dotblas.o -faltivec -I/System/Library/Frameworks/vecLib.framework/Headers" failed with exit status 1
    ```

  please see the instructions in [issue #1179](https://github.com/oppia/oppia/issues/1179) for a fix.

  * If you get an error that includes:

   ```
   GitPython is not installed for Python 2.x
   The 'dist' command will not work without it. Get it using pip or easy_install
   ```
   please install [GitPython](http://gitpython.readthedocs.io/en/stable/intro.html#installing-gitpython) before proceeding further.

  * If you get an error that includes:

   ```
   No Java runtime present, requesting install.
   closure-compiler failed.
   ```
   please download [Java](https://support.apple.com/kb/DL1572?locale=en_US) and install it.

  * if you get an error that includes:
   
   ```
   Checking whether Skulpt is installed in third_party
   cp: /Users/sdawson/opensource/oppia_tools/skulpt-0.10.0/skulpt/dist/*: No such file or directory
   ```
   please remove the below mentioned directories and try running `start.sh` again:
   ```
   ../oppia_tools/
   ../node_modules/
   third_party/
   core/templates/prod/
   ```
   
  * if you run into issues while installing numpy, and the error message looks something like this:

   ```
   Collecting numpy==1.6.1
  Downloading numpy-1.6.1-cp27-none-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.whl (11.6MB)
    100% |████████████████████████████████| 11.6MB 104kB/s 
Installing collected packages: numpy
Exception:
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/site-packages/pip/basecommand.py", line 215, in main
    status = self.run(options, args)
  File "/usr/local/lib/python2.7/site-packages/pip/commands/install.py", line 317, in run
    prefix=options.prefix_path,
  File "/usr/local/lib/python2.7/site-packages/pip/req/req_set.py", line 742, in install
    **kwargs
  File "/usr/local/lib/python2.7/site-packages/pip/req/req_install.py", line 831, in install
    self.move_wheel_files(self.source_dir, root=root, prefix=prefix)
  File "/usr/local/lib/python2.7/site-packages/pip/req/req_install.py", line 1032, in move_wheel_files
    isolated=self.isolated,
  File "/usr/local/lib/python2.7/site-packages/pip/wheel.py", line 247, in move_wheel_files
    prefix=prefix,
  File "/usr/local/lib/python2.7/site-packages/pip/locations.py", line 153, in distutils_scheme
    i.finalize_options()
  File "/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/command/install.py", line 264, in finalize_options
    "must supply either home or prefix/exec-prefix -- not both"
DistutilsOptionError: must supply either home or prefix/exec-prefix -- not both
   ```
   this StackOverflow [answer](http://stackoverflow.com/a/24357384) provides a possible fix.