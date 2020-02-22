**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

**Note:** Installing Oppia on Windows can be **complicated**. We strongly recommend installing on [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29) or [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29) instead if you're able to do so.

**Note:** These instructions are tested to work on Windows 10. If you have some other version of windows, we strongly recommend using Linux or Mac OS, if possible.

*For information on issues that may occasionally arise with the installation process, please see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting) page.*

There follow instructions for 3 different ways to install Oppia on Windows: using VirtualBox, using Docker, and using the Ubuntu terminal. You only need to follow one of the three.

# Installation in VirtualBox on Windows 10

Last tested by **@jkoj25** on Windows 10 in January of 2020. Frontend and backend tests worked at that point.

_For this method, a machine with at least 8 GB RAM (prefereably 16 GB) and at least a dual core processor (preferably quad core) is recommended._

With VirtualBox, we run an Ubuntu 18.04 VM, with some minor changes to the VM config. With this installation, the terminal and editor for the codebase will be in VM, while the development site itself can be accessed on the Windows host. This is done so that at least some memory usage can be reduced on VM for better performance.

##  Set up VM in VirtualBox (any VM manager is fine, but the instructions here are specific to VirtualBox)

1. Install VirtualBox from [here](https://www.virtualbox.org/wiki/Downloads).
2. Open VirtualBox and click New.
3. Select Type as "Linux", Version "Ubuntu 64bit" and give some name for the VM.
4. In the next page, select an appropriate amount of RAM for the VM (can be changed later). The whole dev environment is verified to work smoothly at 6 GB RAM. At least 4 GB is recommended.
5. In the next page, select "Create a virtual hard disk now" and click Create.
6. Select VDI as the file type.
7. Depending on free space on the machine, either dynamically allocated or static can be chosen here.
8. Select the amount of storage that is needed (around 20 GB should be fine) and select a location on the machine with enough free space to host the VM and click create.

## Install Ubuntu 18 ISO

1. Download the Ubuntu 18.04 64bit ISO from [here](https://ubuntu.com/download/desktop).
2. Select the newly created VM in virtual box and click Start.
3. Here, a window pops up where you have to link the downloaded ISO file. Click the folder icon and select the ISO from your machine.
4. Now, go through the normal Ubuntu installation steps, you can do the following the specific steps:
 * Select "Minimal Installation", and check both checkboxes below it.
 * Select "Erase disk and install Ubuntu". Don't worry, no data in your host machine will be affected :).
5. Once, Ubuntu is running and everything is done installing, exit from VM.

## Setup VirtualBox config (optional, but recommended)
_The following has to be done after exiting from VM. Also, the following need only be done if you want the browser on host to have access to the server running in VM. If you allocated enough RAM to handle the browser instance as well in VirtualBox, then you are done and can use the VM as a complete dev environment!_

1. Select the newly created VM in VirtualBox and click Settings.
2. Go to 'System'. Here, you can change the amount of RAM allocated to the VM, and in the 'Processor' tab, you can change the amount of cores as well. At least 2 cores are recommended, it is verified to work smoothly at 4 cores.
2. Go to 'Network' tab. Here, Adapter 1 should be 'NAT', leave it at that.
3. Go to 'Adapter 2' and enable it. Select the first dropdown to 'Bridged Adapter' and name to whatever is the network adapter that you are using now.
4. Then, in 'Advanced', set the MAC address to your active adapter's MAC address (Check it out [here](https://kb.netgear.com/1005/How-do-I-find-my-device-s-MAC-address)).

It should look something like this: [Screenshot](https://drive.google.com/file/d/1E06mh-6zlOXbJIBOjjsCJDB7cytFS1hI/view?usp=sharing)

Now, you can open the VM. After that, clone and install the Oppia repository from GitHub following the [Ubuntu installation instructions](https://github.com/oppia/oppia/wiki/Installing-Oppia-(Linux)#downloading-oppia) in order to setup Oppia in the VM. 

If you have done the optional steps, then every time before running `python -m scripts.start` to start the dev server, change [this](https://github.com/oppia/oppia/blob/c60361e4ef32f01b0da126c24aba4174b99634f5/scripts/start.py#L143) line in start.py to `'8000 --host 0.0.0.0 --port %s --enable_host_checking=False --skip_sdk_update_check true %s' % (`.

Once, this is done, whenever you run the dev server in the VM, you can go to your browser on the Windows host and go to:
http://<your_vm's_local_ip>:8181 to access the dev server. You can find your VM's local IP address by running `ifconfig`in a terminal in the VM. It should be the `inet` address of the second adapter shown there.

The change mentioned in start.py has to be done everytime before running start.py for this to work, you can revert it after the server has started, i.e site is accessible on host.

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

    Expect up to a 2 minute delay until the first line of output is printed to the console. The total runtime for this build should be around 25-30 minutes on a good connection.
    - If successful, the output should say: `successfully tagged {image_name}:latest`. It will also give a security warning, but this is fine. You will be able to see the Docker image’s details by running: `docker images`
    - If it is not successful, it is very likely due to unstable wifi connections. Move next to a router, and retry this step. 

    Here's what a successful run looks like:

      ![Screenshot showing terminal output for a successful Docker installation.](images/dockerSuccess.png)

### Build a Docker container based on image

4. Now that the Docker image is built, create a Docker container using that image by running:

   ```
     docker run -u 0 -it -p 8181:8181 --name {container_name} -v {path_to_oppia_parent_dir}:/home {image_name}:latest bash
   ```

   where you should replace `{container_name}` with whatever you want to call your Docker container (say `oppia_container`), `{path_to_oppia_parent_dir}` with the **absolute path** to your oppia folder's parent directory (which might be `C:\Users\name\Desktop\opensource`), and `{image_name}` with the name of your Docker image (see above).

5. At this point, a container is built with your current oppia directory. Now you should have a new terminal prompt `root@...`. This is a Linux-based terminal. Everything is now set up to run scripts like start.py and run_backend_tests.py. You can type `exit` to return to your Command Prompt.

## Running Oppia on a development server

### Ensure container is running

1. Run `docker ps`.
    - If this outputs a container, move on to step 3. Note: the `{container_name}` in the following steps can be found under the “NAMES” column of the output of `docker ps`.
    - If this does not output a container, move on to step 2.

2. Run `docker ps -a`
    - If this outputs names of containers, find the NAME of the most recent container and run: `docker start {container_name}`
    - If this does not output names of containers, run: `docker images` to get the name of a previously built image and follow step 4 from the prerequisite instructions. Then return to step 1 to ensure that the container is running.

### Start bash and run the start script

3. Start bash in the updated Docker container: `docker exec -it {container_name} bash`

4. Now you should have a new terminal prompt`root@...`. Run the start.py script: `python -m scripts.start`

The estimated runtime for this script is about 10-20 minutes. It will open a server at localhost:8181. After the terminal prints `INFO ... http://0.0.0.0:8181` or `+ 27 hidden modules`, open localhost:8181 in your local computer browser. If the Oppia server does not load, restart this step.

## Running frontend tests

**Note**: run_frontend_tests.py might not run correctly every time, and we’re still working on figuring out why. 

1. If you are in the Docker container bash, type `exit` to return to your Command Prompt. 

2. Ensure that node.js is installed on your Windows computer by running `node -v`. If not, install it from [here](https://nodejs.org/en/download/).

3. Run `pip install future`

4. Run these two commands to manually compile the frontend tests and run the tests:
     ```
       node .\node_modules\typescript\bin\tsc --project .
       node .\node_modules\karma\bin\karma start .\core\tests\karma.conf.ts
     ```
   If this outputs an error, please see [this section](https://github.com/oppia/oppia/wiki/Installing-Oppia-(Windows)#troubleshooting) for alternative commands.

You're done! Now return to the [code contribution instructions](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia), skipping the step about cloning the Oppia repository with `git`.

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

- If the frontend test command is not working
  - Then: try these 2 alternative options:
    - Option 1:
       Start bash in the Docker container (follow steps 1-3 from running Oppia on a development server).
       Run the run_frontend_tests.py script. The expected runtime is about 3-7 minutes. 
       ```
         python -m scripts.run_frontend_tests
       ```
    - Option 2:
       Start bash in the Docker container (follow steps 1-3 from running Oppia on a development server).
       Run these two commands to manually compile the frontend tests and run the tests:
       ```
         ./node_modules/typescript/bin/tsc --project .
         ./node_modules/karma/bin/karma start ./core/tests/karma.conf.ts
       ```

# Installation using the Ubuntu terminal on Windows 10

_These notes were kindly contributed by **@varun-tandon** on 18 Feb 2019. They were last tested successfully by **@BenHenning** on Sep 2019. They get Oppia working in a virtual environment on Windows, but with the caveat that the frontend (Karma) tests do not run because the Chrome browser does not open in the virtual environment. We are still looking for a fix for this._

First, start by [installing the Ubuntu terminal](https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0). Then, follow [the Ubuntu installation instructions](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), **but with the following changes**:

### After the prerequisites, but before running start.py:

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

### When running start.py:

Please note that the installation process can have some strange hiccups on the Windows Ubuntu subsystem. If you are installing to this subsystem and encounter errors, please restart your computer and try running the start script again. 

If you get an error that indicates that a server is already running, this is a good sign! Navigate to [https://localhost:8181](https://localhost:8181). If the Oppia homepage loads, you have successfully completed installation!

## Troubleshooting

- If you run into `distutilsOptionError`:
  - Then: Make sure you have set up the virtualenv. See [this comment](https://github.com/oppia/oppia/issues/7613#issuecomment-531429687).
