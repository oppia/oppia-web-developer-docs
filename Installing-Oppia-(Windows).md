**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

These instructions outline how to install Oppia on a Windows machine.

### Setting up a development server

1. Download and install [VirtualBox 5.0.12](https://www.virtualbox.org/wiki/Downloads). (You do not need to create a VM, just installing VirtualBox is sufficient.)
2. Download and install [Vagrant 1.8.1](https://www.vagrantup.com/downloads.html). After installation, Vagrant will prompt for a restart. Restart your machine.
3. Create a new folder somewhere on your machine, download the [Vagrantfile](https://raw.githubusercontent.com/oppia/oppia/develop/Vagrantfile), and add it to the folder. Then, open a command prompt, navigate to the folder you just created, and run `vagrant up`. This will create a new virtual machine.
4. Run `vagrant ssh` to ssh into the virtual machine.
5. Navigate to the vagrant folder: `cd /vagrant`. 
6. Run `bash scripts/install_prerequisites.sh` to install the build tools and project dependencies.
7. [Fork and clone](https://help.github.com/articles/fork-a-repo/) the oppia repository. (You might have to add your ssh keys to github.)
8. Run `cd oppia` and `bash scripts/start.sh`. This will install Google App Engine, and start a Python server from which you can run Oppia locally
9. If installation has succeeded, you should now be able to access Oppia at `http://localhost:8181/`.