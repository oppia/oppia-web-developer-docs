**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

**Note:** Installing Oppia on Windows can be **complicated**. We strongly recommend installing on [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29) or [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29) instead if you're able to do so.

**Note:** These instructions are tested to work on Windows 10. If you have some other version of windows, we strongly recommend using Linux or Mac OS, if possible. Alternatively, if you have sufficient RAM (>=6 gb), you could try installing Linux in virtualbox and then installing Oppia on the virtual Linux machine.

*For information on issues that may occasionally arise with the installation process, please see the [Troubleshooting](https://github.com/oppia/oppia/wiki/Troubleshooting) page.*

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


# Installation using Virtualbox/Vagrant

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
  1. follow instructions at [fork and clone](https://github.com/oppia/oppia/wiki/Fork-and-Clone-Oppia) in order to clone the Oppia repository to your local machine.
  1. Run `cd oppia` to navigate to the oppia folder.

### Installing Oppia using Vagrant

Oppia is targeted as a Linux application, and for contributors and developers on Windows, we have provided a Vagrant build process. Please refer to [those instructions](https://github.com/oppia/oppia/wiki/Installing-Oppia(Vagrant)) for development on Windows. 
