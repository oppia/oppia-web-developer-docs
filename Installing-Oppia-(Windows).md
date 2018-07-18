**Note:** If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

**Note:** We strongly recommend using Linux or Mac OS, if possible. It is much easier to install a local copy of Oppia on those operating systems than it is to install Oppia on Windows.

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

### Troubleshooting:

It's possible that windows firewall might be preventing localhost:8181 to launch. In such a case, you should re-config the firewall by adding new inbound rule so that ports 8181 and 8000 are allowed. (Instruction about how to add inbound rules can be found [here](https://msdn.microsoft.com/en-us/library/hh168549(v=nav.90).aspx))

  * If you get an error that ends with:

    ```
      File "/usr/lib/python2.7/ssl.py", line 405, in do_handshake
    self._sslobj.do_handshake()
      IOError: [Errno socket error] [Errno 1] _ssl.c:510: error:14077410:SSL routines:SSL23_GET_SERVER_HELLO:sslv3 alert handshake failure
    ```

    try upgrading your python, follow these steps:
    - `sudo apt-get update`
    - `sudo apt-get install --only-upgrade python2.7`

    **Note:** This issue will only raise if your python version is < 2.7.9.