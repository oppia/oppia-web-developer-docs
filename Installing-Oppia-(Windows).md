**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

These instructions outline how to install Oppia on a Windows machine.

1. Setting up Vagrant:
   - Download and install [VirtualBox 5.0.12](https://www.virtualbox.org/wiki/Downloads). (You do not need to create a VM, just installing VirtualBox is sufficient.)
   - Download and install [Vagrant 1.8.1](https://www.vagrantup.com/downloads.html). After installation, Vagrant will prompt for a restart. Restart your machine.
   - Create a new folder somewhere on your machine, download the [Vagrantfile](https://raw.githubusercontent.com/oppia/oppia/develop/Vagrantfile), and add it to the folder. Then, open a command prompt, navigate to the folder you just created, and run `vagrant up`. This will create a new virtual machine.
   - Run `vagrant ssh` to ssh into the virtual machine.
   - Run `sudo apt-get install git` to install git on the virtual machine.
   - Navigate to the vagrant folder: `cd /vagrant`.
1. Setting up Oppia:
   - [Fork and clone](https://help.github.com/articles/fork-a-repo/) the oppia repository. (You might have to add your ssh keys to github.)
   - Run `cd oppia`.
   - Run `bash scripts/install_prerequisites.sh`. This installs the build tools and project dependencies.
   - Run `bash scripts/start.sh`. This will install Google App Engine, and start a Python server from which you can run Oppia locally.
   - If installation has succeeded, you should now be able to access Oppia at `http://localhost:8181/`.

### Troubleshooting
- Some users have reported that the scripts in the second part need to be run using `sudo`. E.g.:
  - `sudo bash scripts/install_prerequisites.sh`
  - `sudo bash scripts/start.sh`

### If the above doesn't work...

If you run into any issues with the installation process, please let us know by [filing an issue](https://github.com/oppia/oppia/issues/new?title=Describe%20your%20feature%20request%20or%20bug%20report%20succinctly&body=If%20you%27d%20like%20to%20propose%20a%20feature,%20describe%20what%20you%27d%20like%20to%20see.%20Mock%20ups%20would%20be%20great!%0A%0AIf%20you%27re%20reporting%20a%20bug,%20please%20be%20sure%20to%20include%20the%20expected%20behaviour,%20the%20observed%20behaviour,%20and%20steps%20to%20reproduce%20the%20problem.%20Console%20copy-pastes%20and%20any%20background%20on%20the%20environment%20would%20also%20be%20helpful.%0A%0AThanks!). Thanks!