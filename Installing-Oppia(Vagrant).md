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

### Vagrant Up! Launching your first VM

After following the instructions for obtaining the Oppia source code for your OS ([Windows here](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29), and [Linux/OSX here](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29)), open your terminal (if on Windows, use git bash) and navigate to the directory you just cloned down in git. You should be in a directory called `oppia`. 

Once inside the `oppia` directory, run the command `vagrant up`. From here, Vagrant will look for a file called `Vagrantfile` and use its instructions like a recipe for creating a VM. It will use your installed hypervisor to create a VM, then configure it according to the Vagrantfile. If this is the first time building the Oppia machine, it will take a fairly long time, as Vagrant has to download a template operating system (a "box" in Vagrant-ese). Otherwise, a fresh build of a Vagrant VM takes about 25 minutes from start to finish. 

Once the machine finishes building, it will start Oppia automatically and you can access the web page at `http://localhost:8181/`

The Oppia process is in the foreground, preventing Vagrant from returning control of the terminal back to the user. Therefore, ctrl+c will break it for you. Oppia will still be running in the background. 

You can stop the machine by using `vagrant halt`, and start the machine again by using `vagrant up`. On subsequent starts, you will have to SSH into the machine and run `bash scripts/start.sh` from `/home/vagrant/oppia`. 

### Accessing and editing source code

- You can edit Oppia's source locally on your machine and it will automatically sync to the Vagrant VM directory `/home/vagrant/oppia`. 
- However, when committing/pushing, we recommend running `git commit` and `git push` from the **guest** instead (see the troubleshooting notes below for the rationale). To access the guest, run `vagrant ssh` from the root of the Oppia respository on your host.

* For the reason why, see the [rationale](#troubleshooting) below.
 
### If the Oppia server does not start automatically
If the Oppia server does not start automatically when you run 'vagrant up', this may mean that the VM has already been created (in which case it will not attempt to provision again). To restart the Oppia server, you will also need to do the following:

   1. Run `vagrant ssh` to SSH into the guest.
   2. In the guest, run:

   ```
     cd /home/vagrant/oppia
     bash ./scripts/start.sh
   ```

   3. The Oppia server should now start at `http://localhost:8181`.

### Troubleshooting

- If you run `git commit` from the host machine, you will likely have your commit rejected because you have not installed the pre-commit hooks. The hooks only install after you have run Oppia for the first time on a machine. Since you are actually installing and running Oppia on a VM, those hooks do not exist on the host. There are several ways to overcome this:
  - (Recommended) Do `git commit` and `git push` from the guest. This is actually not as difficult or burdensome as it may sound: All directories are mapped into the Vagrant VM, including `.git`, so configurations such as your username and e-mail will carry over as well.
  - Try to build Oppia natively on Windows (this is difficult, and is neither recommended nor supported).
  - Note that doing a `git push` using SSH will not work, since the guest machine cannot see your host's private key. If you want to use SSH, you can add the Vagrant VM's public key to your account, but *this is NOT RECOMMENDED*! Vagrant uses the same SSH key for all machines, so anyone could write to any of your repos. 
-  If Vagrant prints an error involving `\r not found`, the recommended fix is to ensure you have the [appropriate line endings set up](#prerequisites) and then clone your repo down again after copying out or saving any work.

### If the above doesn't work...

If you run into any issues with the installation process, please let us know by [filing an issue](https://github.com/oppia/oppia/issues/new?title=Describe%20your%20feature%20request%20or%20bug%20report%20succinctly&body=If%20you%27d%20like%20to%20propose%20a%20feature,%20describe%20what%20you%27d%20like%20to%20see.%20Mock%20ups%20would%20be%20great!%0A%0AIf%20you%27re%20reporting%20a%20bug,%20please%20be%20sure%20to%20include%20the%20expected%20behaviour,%20the%20observed%20behaviour,%20and%20steps%20to%20reproduce%20the%20problem.%20Console%20copy-pastes%20and%20any%20background%20on%20the%20environment%20would%20also%20be%20helpful.%0A%0AThanks!). Thanks!