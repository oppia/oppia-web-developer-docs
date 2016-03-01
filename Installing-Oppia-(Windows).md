**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

### Prerequisites

The Windows installation of Oppia relies on a number of third-party programs, which you will need to install beforehand:

  1. Download and install [VirtualBox 5.0.14](https://www.virtualbox.org/wiki/Downloads). You do not need to create a virtual machine (VM); that will be handled later. 
  1. Download and install [Vagrant 1.8.1](https://www.vagrantup.com/downloads.html). After installation, Vagrant will prompt for a restart. Restart your machine. 
  1. Download and install [git](https://git-scm.com/downloads). 
  1. Make sure git correctly [converts Windows line endings](https://help.github.com/articles/dealing-with-line-endings/).

### Installing Oppia on Windows

These steps outline how to install Oppia on a Windows machine:

  1. Open Git Bash and navigate to a directory somewhere on your machine (such as `Desktop/opensource`) where you'd like the Oppia code to live.
  1. In Git Bash, run `git clone https://github.com/oppia/oppia.git`. This will clone the repository into a new directory called 'oppia'.
  1. In Git Bash, run `cd ./oppia` to navigate into the new 'oppia' directory. 
  1. Once in the directory, run `vagrant up` in Git Bash. This will create a VM for you, install the necessary prerequisites, and start the Oppia server automatically at `http://localhost:8181`. Since the server runs automatically in the foreground, the server will grab the terminal until you `Ctrl+C` to stop the Oppia server, but the VM itself will still be running.

**Note**: In the rest of this page, we'll refer to the VM as the **guest** machine, and your local computer as the **host** machine.

### Accessing and editing source code
- You can edit Oppia's source locally on your machine and it will automatically sync to the Vagrant VM directory `/home/vagrant/oppia`. 
- However, when committing/pushing, we recommend running `git commit` and `git push` from the **guest** instead (see the troubleshooting notes below for the rationale). To access the guest, run `vagrant ssh` from the root of the Oppia respository on your host.

### If the Oppia server does not start automatically
If the Oppia server does not start automatically when you run 'vagrant up', this may mean that the VM has already been created (in which case it will not attempt to provision again). To restart the Oppia server, you will also need to do the following:

   1. Run `vagrant ssh` to SSH into the guest.
   2. In the guest, run:

   ```
     cd /home/vagrant/oppia
     bash ./scripts/start.sh
   ```

   3. The Oppia server should now start at `http://localhost:8181`.

**Note**: If this doesn't work, you may need to exit and rebuild the VM. To do this, run the following command on the host: `vagrant destroy -f; vagrant up`.

### Troubleshooting
- If you run `git commit` from the host machine, you will likely have your commit rejected because you have not installed the pre-commit hooks. The hooks only install after you have run Oppia for the first time on a machine. Since you are actually installing and running Oppia on a VM, those hooks do not exist on the host. There are several ways to overcome this:
  - (Recommended) Do `git commit` and `git push` from the guest. This is actually not as onerous as it may sound: All directories are mapped into the Vagrant VM, including `.git`, so configurations (such as your username and e-mail) will carry over as well.
  - Try to build Oppia natively on Windows (this is difficult, and is neither recommended nor supported).
  - Note that doing a `git push` using SSH will not work, since the guest machine cannot see your host's private key. If you want to use SSH, you can add the Vagrant VM's public key to your account, but *this is NOT RECOMMENDED*! Vagrant uses the same SSH key for all machines, so anyone could write to any of your repos. 
-  If Vagrant prints an error involving "\r not found", then, in Git Bash, run `find . -name "*" -type f -exec dos2unix {} \;`. After that, exit the Vagrant environment, run `vagrant box reload`, and try again.



### If the above doesn't work...

If you run into any issues with the installation process, please let us know by [filing an issue](https://github.com/oppia/oppia/issues/new?title=Describe%20your%20feature%20request%20or%20bug%20report%20succinctly&body=If%20you%27d%20like%20to%20propose%20a%20feature,%20describe%20what%20you%27d%20like%20to%20see.%20Mock%20ups%20would%20be%20great!%0A%0AIf%20you%27re%20reporting%20a%20bug,%20please%20be%20sure%20to%20include%20the%20expected%20behaviour,%20the%20observed%20behaviour,%20and%20steps%20to%20reproduce%20the%20problem.%20Console%20copy-pastes%20and%20any%20background%20on%20the%20environment%20would%20also%20be%20helpful.%0A%0AThanks!). Thanks!