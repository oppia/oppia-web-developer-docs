**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

### Prerequisites

The Windows installation of Oppia relies on a number of third-party programs, which you will need to install beforehand:

  1. Download and install [VirtualBox 5.0.14](https://www.virtualbox.org/wiki/Downloads). You do not need to create a virtual machine (VM); that will be handled later. 
  1. Download and install [Vagrant 1.8.1](https://www.vagrantup.com/downloads.html). After installation, Vagrant will prompt for a restart. Restart your machine. 
  1. Download and install [git](https://git-scm.com/downloads). 
  1. Make sure git correctly [converts Windows line endings](https://help.github.com/articles/dealing-with-line-endings/).

### Downloading Oppia to your local machine
  1. Navigate to your root directory.
  1. Make a new folder in your root directory called `opensource`.
  1. Navigate to this folder: `cd opensource`.
  1. Run `git clone https://github.com/oppia/oppia.git` in order to clone the Oppia repository to your local machine.
  1. Run `cd oppia` to navigate to the oppia folder.

### Installing Oppia on Windows

Oppia is targeted as a Linux application, and for contributors and developers on Windows, we have provided a Vagrant build process. Please refer to [those instructions](https://github.com/oppia/oppia/wiki/Installing-Oppia(Vagrant)) for development on Windows. 