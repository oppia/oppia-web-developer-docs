**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

**Note:** Installing Oppia on Windows can be **complicated**. We strongly recommend installing on [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29) or [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29) instead if you're able to do so.

**Note:** These instructions are tested to work on Windows 10. If you have some other version of windows, we strongly recommend using Linux or Mac OS, if possible. Alternatively, if you have sufficient RAM (>=6 gb), you could try installing Linux in virtualbox and then installing Oppia on the virtual Linux machine.

*For information on issues that may occasionally arise with the installation process, please see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting) page.*

# Installation using Docker on Windows 10

_These notes were kindly contributed by **@ezl-13** on 13 Aug 2019. Note though that getting the frontend (Karma) tests running may not work in a foolproof way, and we haven't figured out how to get the e2e tests running yet. This is being worked on in issues [#7355](https://github.com/oppia/oppia/issues/7355) and [#7345](https://github.com/oppia/oppia/issues/7345)._

Docker allows for an easy installation of Oppia for Windows users and a more reliable testing environment for running test scripts. The following instructions describe how to install Oppia using Docker. (If you need help with troubleshooting, please see [this section](https://github.com/oppia/oppia/wiki/Installing-Oppia-(Windows)#troubleshooting).)

## Prerequisites & Getting Docker Container Set Up (you should only need to follow these steps once)

### Start Docker

1. Download Docker Desktop for Windows:
    - Windows Enterprise and Pro: https://hub.docker.com/editions/community/docker-ce-desktop-windows
    - Windows 10 Home: https://docs.docker.com/toolbox/toolbox_install_windows/

2. Start Docker by clicking on the Docker application (a Docker icon should appear in your taskbar tray).

### Build the Docker Image

3. Build the Docker image from the Oppia root folder (note the "." at the end of the command). Make sure you have a good Internet connection when doing this step.

    If this is your first time running docker build, run:
    ```
      docker build -t {image_name} -f ubuntu_dockerfile .
    ```
    where you should replace `{image_name}` with whatever you want to call your Docker image (say `oppia_image`).

    If this is not your first time running this command, run:
    ```
      docker build -t {image_name} -f ubuntu_dockerfile . --no-cache
    ```
    where the `--no-cache` flag tells docker to rebuild from the beginning. 

    Expect up to a 2 minute delay until the first line of output is printed to the console. The total runtime for this build should be around 25-30 minutes on a good connection.
    - If successful, the output should say: `successfully tagged {image_name}:latest`. It will also give a security warning, but this is fine. You will be able to see the Docker image’s details by running: `docker images`
    - If it is not successful, it is very likely due to unstable wifi connections. Move next to a router, and retry this step. 

    Here's what a successful run looks like:

      ![Screenshot showing terminal output for a successful Docker installation.](images/dockerSuccess.png)

### Build a Docker container based on image

4. Now that the Docker image is built, create a Docker container using that image by running:

   ```
     docker run -u 0 -it -p 8181:8181 --name {container_name} {image_name}:latest bash
   ```

   where you should replace `{container_name}` with whatever you want to call your Docker container (say `oppia_container`) and `{image_name}` with the name of your Docker image (see above).

5. At this point, a container is built with your current oppia directory. Now you should have a new terminal prompt `root@...`. This is a Linux-based terminal. Everything is now set up to run scripts like start.sh and run_frontend_tests.sh. You can type `exit` to return to your Command Prompt.

## Running Oppia on a development server

### Ensure container is running

1. Run `docker ps`.
    - If this outputs a container, move on to step 3. Note: the `{container_name}` in the following steps can be found under the “NAMES” column of the output of `docker ps`.
    - If this does not output a container, move on to step 2.

2. Run `docker ps -a`
    - If this outputs names of containers, find the NAME of the most recent container and run: `docker start {container_name}`
    - If this does not output names of containers, run: `docker images` to get the name of a previously built image and follow step 4 from the prerequisite instructions. Then return to step 1 to ensure that the container is running.

### Update the files in the container with your local repo

3. Update the container to have your most recent code. Skip this step if you have not made any changes to your local repo. Note: Please keep in mind the direction of the slashes in the paths ( ‘/’ vs ‘\’).
    - If you remember what files/directories you have edited, run:
      ```
        docker cp {path\to\src} {container_name}:/home/oppia/{path/to/dest} 
      ```

      where `{path\to\src}` can be the relative path to a file or folder and `{path/to/dest}` is the path within the /home/oppia directory in the container. Example: `docker cp .\core\domain\. oppia_container:/home/oppia/core/domain/`

    - If you do not remember what files you have edited, run:
      ```
        docker cp .\. {container_name}:/home/oppia/ 
      ```
      in the oppia root directory to copy over the entire oppia/ directory into the container. Note: This will take ~10 minutes to copy over all of the files.

### Start bash and run the start script

4. Start bash in the updated Docker container: `docker exec -it {container_name} bash`

5. Now you should have a new terminal prompt`root@...`. Run the start.sh script: `bash scripts/start.sh`

The estimated runtime for this script is about 10-20 minutes. It will open a server at localhost:8181. After the terminal prints `INFO ... http://0.0.0.0:8181` or `+ 27 hidden modules`, open localhost:8181 in your local computer browser. If the Oppia server does not load, restart this step.

## Running frontend tests

**Note**: run_frontend_tests.sh might not run correctly every time, and we’re still working on figuring out why. 

1. Start bash in the Docker container (follow steps 1-4 from running Oppia on a development server).

2. Run the run_frontend_tests.sh script: `bash scripts/run_frontend_tests.sh`. The expected runtime is about 3-7 minutes. 
    - If this outputs an error ("failed before timeout of 2000ms"), continue to step 3.
    - If this runs correctly (displays "SUCCESS"), do not go onto step 3.

3. Run these two commands to manually compile the frontend tests and run the tests:
     ```
       ./node_modules/typescript/bin/tsc --project .
       ./node_modules/karma/bin/karma start ./core/tests/karma.conf.ts
     ```
   If this outputs an error, try STEP 2 again.
   If this runs correctly, you will see a SIGKILL at the end. That is okay.

## Troubleshooting

- If docker outputs: Error processing … no space left on device. 
  - Then: run docker system prune (to delete terminated docker images / containers)

- If docker outputs: docker: Error response from daemon: … port is already allocated.
  - Then: restart docker by right clicking on the icon in the taskbar and clicking Restart

- If docker outputs: unzip not found
  - Then: run bash scripts/install_prerequisites.sh inside of the Docker image (bash)

- If docker outputs: npm: no such file or directory
  - Then: run the following two commands:
       ```
         curl -sL https://deb.nodesource.com/setup_8.x | bash
         apt-get install nodejs 
       ```

# Installation using the Ubuntu terminal on Windows 10

_These notes were kindly contributed by **@varun-tandon** on 18 Feb 2019. They get Oppia working in a virtual environment on Windows, but with the caveat that the frontend (Karma) tests do not run because the Chrome browser does not open in the virtual environment. We are still looking for a fix for this._

First, start by [installing the Ubuntu terminal](https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0). Then, follow [the Ubuntu installation instructions](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), **but with the following changes**:

### After the prerequisites, but before running start.sh:

3. Set up a virtual environment (virtualenv) for your Oppia dependencies. This ensures that conflicting versions of Python, pip, or any Python modules on your machine do not result in installation issues. In `opensource/` run:
   ```
   pip2 install virtualenv
   python2 -m virtualenv env
   ```
   This creates a Python 2 virtual environment named "env" in your `opensource/` directory. Now, anytime you need to work with the Oppia code base, you should activate the virtualenv in `opensource/` by running
   ```
   source env/bin/activate
   ```
   If this is successful, the start of the terminal line will now have `(env)` at the beginning of it. The remaining steps of installation and running the development server should all be done within this virtual environment to ensure compatibility.

### When running start.sh:

Please note that the installation process can have some strange hiccups on the Windows Ubuntu subsystem. If you are installing to this subsystem and encounter errors, please restart your computer and try running the start script again. 

If you get an error that indicates that a server is already running, this is a good sign! Navigate to [https://localhost:8181](https://localhost:8181). If the Oppia homepage loads, you have successfully completed installation!
