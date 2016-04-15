# What is Vagrant?

While Oppia can be built on any OS that supports Python, Node.js, and its other fundamental parts, all the build and startup scripts are targeted for Debian-based systems. This means that for any non-Debian systems, such as Windows, OSX, and Linux distros like CentOS and Arch, it will be easier to use a VM than running Oppia locally. 

To aid in this process and ensure you always have a clean machine identical to other developers, we use a tool called [Vagrant](https://www.vagrantup.com/docs/why-vagrant/). In fact, even if you are already on Debian or Ubuntu, you may want to use Vagrant as it will provide isolation between your host machine and things that Oppia needs to install and change, or allow you to build different development versions of Oppia on different branches. 

## Prerequisites

In order to build Oppia via Vagrant, you will need to first install a hypervisor that can build your virtual machine. Our Vagrant build is optimized for VirtualBox, so we recommend that. However, you may also use VMware Player if you have that available. 

Next, you will need to download and install Vagrant following the [instructions on Vagrant's website](https://www.vagrantup.com/docs/installation/). 

## Vagrant Up! Launching your first VM

After following the instructions for obtaining the Oppia source code for your OS ([Windows here](), and [Linux/OSX here]()), open your terminal (if on Windows, use git bash) and navigate to the directory you just cloned down in git. You should be in a directory called `oppia`. 

Once inside the `oppia` directory, run the command `vagrant up`. From here, Vagrant will look for a file called `Vagrantfile` and use its instructions like a recipe for creating a VM. It will use your installed hypervisor to create a VM, then configure it according to the Vagrantfile. If this is the first time building the Oppia machine, it will take a fairly long time, as Vagrant has to download a template operating system (a "box" in Vagrant-ese). Otherwise, a fresh build of a Vagrant VM takes about 25 minutes from start to finish. 

## Git, Tests, and Vagrant

Currently, when you run Oppia for the first time, it installs a git hook on your local machine that runs some tests before you commit and push. If the tests fail, your commit gets aborted. This is good. It prevents you from accidentally committing something bad. However, doing development in Vagrant complicates this, as you do your Git work from the host machine, and Oppia runs on the guest VM, therefore the Git hook never installs. Even if it did, it wouldn't work when running from the host, since the necessary testing tools aren't installed. 

Solution? At this time, we are working on a better answer. For now, we recommend checking your work by starting tests manually and noting the results. If you fail a test, you should fix it before committing, of course.

## Troubleshooting

### `\r: command not found

### Vagrant cannot SSH into guest machine

### Builds take a very long time

### Tests are aborting or not finishing, but not failing

### Oppia starts the first time but not a second time  

