_Note: if you're developing Oppia using Vagrant, please consider signing up to the [oppia-vagrant@](https://groups.google.com/forum/#!forum/oppia-vagrant) mailing list. Fellow Vagrant users may be able to help you out, and vice versa._

_Note: The instructions on this page were last tested by @dawsoneliasen on 7/29/2018 on Windows 10, and they worked successfully. That said, setting up Vagrant can be **complicated**, and we recommend direct installation of Oppia on [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29) or [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29) instead if you're able to do so (or possibly installing the [Ubuntu terminal](https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0) if you're on Windows 10)._

*For information on issues that may occasionally arise with the installation process, please see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting) page.*

## What is Vagrant?

While Oppia can be built on any OS that supports Python, Node.js, and its other fundamental parts, all the build and startup scripts are targeted for Linux systems. This means that for Windows, the best path is to install via our supported Vagrant build.

To aid in this process and ensure you always have a clean machine identical to other developers, we use a tool called [Vagrant](https://www.vagrantup.com/docs/why-vagrant/). In fact, even if you are already on Linux/BSD/OSX, you may want to use Vagrant as it will provide isolation between your host machine and things that Oppia needs to install and change, or allow you to build different development versions of Oppia on different branches. 

### Terms and definitions

 * The terms *VM*, *guest*, and *Vagrant machine* here can all be used interchangeably to mean the virtual machine that Vagrant creates during the build process. 
 * *Host* refers to the host machine that is hosting your VM guest.

### Prerequisites

In order to build Oppia via Vagrant, you will need to first install a hypervisor that can build your virtual machine. Our Vagrant build is optimized for VirtualBox, so we recommend using that. However, you may also use VMware Player if you have that available. These instructions will assume you are using VirtualBox. 

  1. Download and install [VirtualBox 5.0.14](https://www.virtualbox.org/wiki/Downloads). You do not need to create a virtual machine (VM); that will be handled later. 
  1. Download and install [Vagrant 1.8.1](https://www.vagrantup.com/downloads.html). After installation, Vagrant will prompt for a restart. Restart your machine. 
  1. Make sure that virtualization is enabled in your computer’s BIOS.

### Vagrant Up! Launching your first VM

After following the instructions for obtaining the Oppia source code for your OS ([Windows here](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29), and [Linux/OSX here](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29)), open your terminal (if on Windows, use git bash) and navigate to the directory you just cloned down in git. You should be in a directory called `oppia`. 

Once inside the `oppia` directory, run the command `vagrant up`. From here, Vagrant will look for a file called `Vagrantfile` and use its instructions like a recipe for creating a VM. It will use your installed hypervisor to create a VM, then configure it according to the Vagrantfile. If this is the first time building the Oppia machine, it will take a fairly long time, as Vagrant has to download a template operating system (a "box" in Vagrant-ese). Otherwise, a fresh build of a Vagrant VM takes about 25 minutes from start to finish. 

**Note**: If running `vagrant up` does not work, make sure that the virtual box version is correct (Ubuntu 64-bit) .If the VM is still running, run `vagrant halt`, and then, re-run `vagrant up`.

Once the machine finishes building, it will start Oppia and you can access the web page at `http://localhost:8181/`

The Oppia process is in the foreground, preventing Vagrant from returning control of the terminal back to the user. Therefore, ctrl+c will break it for you. Oppia will still be running in the background. 

You can stop the machine by using `vagrant halt`, and start the machine again by using `vagrant up`. On subsequent starts, you will have to SSH (Run `vagrant ssh`) into the machine, move to the `oppia` directory  and run `bash scripts/start.sh`. To exit SSH of vagrant, run `exit` command or press `CTRL+D`.  

### Accessing and editing source code

- You can edit Oppia's source locally on your machine and it will automatically sync to the Vagrant VM directory `/home/vagrant/oppia`. 
- However, when committing/pushing, we recommend running `git commit` and `git push` from the **guest** instead (see the troubleshooting notes below for the rationale). To access the guest, run `vagrant ssh` from the root of the Oppia respository on your host.

* For the reason why, see the [rationale](#troubleshooting) below.
 
### If the Oppia server does not start automatically...
If the Oppia server does not start automatically when you run 'vagrant up', this may mean that the VM has already been created (in which case it will not attempt to provision again). To restart the Oppia server, you will also need to do the following:

   1. Run `vagrant ssh` to SSH into the guest.
   2. In the guest, run:

   ```
     cd /home/vagrant/oppia
     bash ./scripts/start.sh
   ```

   3. The Oppia server should now be available. Open a new tab in your browser and navigate to `http://localhost:8181`. 

**Note:** If this does not work, cd into the oppia folder on the VM and check if the folder is empty. If so:
- Run `exit` to go back to your machine.
- Run `vagrant provision` to copy the files into the VM. If, the folders "ckeditor-sharedspace-4.9.2" and "ckeditor-bootstrapck-1.0" are still missing (it will throw an error), download those from the Oppia dependencies drive and copy them to the oppia/third_party/static folder.
- Next, run `vagrant ssh` again and then run `bash scripts/start.sh` as described above. This might throw errors if gitpython and java are not installed. If that's the case, run:

  ```
    sudo pip install gitpython
    sudo apt-get install openjdk-6-jre
  ```

  and then run `bash scripts/start.sh` again, then check `http://localhost:8181` in your browser.

### If trying to restart the server throws an error...

Try deleting the `.lock` file in the top-level Oppia directory.

### Tweaking the virtual machine settings

In order to adjust the hardware settings of your VM (such as giving it more memory), stop the machine by issuing a `vagrant halt` from your Oppia directory on the host, then open up your hypervisor manager (typically VirtualBox). Your VM be a machine with a name that starts with `oppia_default_`. Select and edit the desired settings on that machine, then return to your Oppia repo and issue a `vagrant up` to run the machine with the new settings.

