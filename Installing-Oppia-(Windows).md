**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

These instructions outline how to install Oppia on a Windows machine.

1. Setting up Vagrant:
   - Download and install [VirtualBox 5.0.12](https://www.virtualbox.org/wiki/Downloads). (You do not need to create a VM, just installing VirtualBox is sufficient.)
   - Download and install [Vagrant 1.8.1](https://www.vagrantup.com/downloads.html). After installation, Vagrant will prompt for a restart. Restart your machine.
   - Create a new folder somewhere on your machine, download the [Vagrantfile](https://raw.githubusercontent.com/oppia/oppia/develop/Vagrantfile), and add it to the folder. Then, open a command prompt, navigate to the folder you just created, and run `vagrant up`. This will create a new virtual machine.
   - Run `vagrant ssh` to ssh into the virtual machine.
   - Navigate to the vagrant folder: `cd /vagrant`.
1. Setting up Oppia:
   - [Fork and clone](https://help.github.com/articles/fork-a-repo/) the oppia repository. (You might have to add your ssh keys to github.)
   - Run `cd oppia`.
   - Run `bash scripts/install_prerequisites.sh`. This installs the build tools and project dependencies.
   - Run `bash scripts/start.sh`. This will install Google App Engine, and start a Python server from which you can run Oppia locally.
   - If installation has succeeded, you should now be able to access Oppia at `http://localhost:8181/`.

** Troubleshooting **
- Some users have reported that the scripts in the second part need to be run using `sudo`.