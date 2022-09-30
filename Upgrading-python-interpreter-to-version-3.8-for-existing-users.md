# Upgrading python interpreter version from 3.7.10 to 3.8.12

Currently, in Oppia we are utilizing python interpreter version 3.7.10. We are now in a phase of switching to a more updated interpreter version 3.8.12. For effective and effortless switching to the newer version, this guide will provide a brief and detailed instruction on how to achieve just that. Please follow the below mentioned instructions carefully.

## Prerequisite
Please make sure your local as well as remote fork is up-to-date with the develop. 

### Step 1: Installing python 3.8.12 through pyenv
```
❯ pyenv install 3.8.12
Installing Python-3.8.12...
patching file Misc/NEWS.d/next/Build/2021-10-11-16-27-38.bpo-45405.iSfdW5.rst
patching file configure
patching file configure.ac
Installed Python-3.8.12 to /home/user/.pyenv/versions/3.8.12
```

### Step 1.5: Setting up Python 3.8 for Direnv Users
*Note : Follow this step if you are using direnv for automatic switching of interpreter versions on entering oppia directory. Also skip all the below steps if you are following this step*

1. Edit the `.envrc` file in your oppia folder to this
```
use python 3.8.12
```

2. Run this command in the same directory to complete the setup
```
$ direnv allow
```

### Step 2. Setting up virtualenv
In this step, we will be setting up a new virtual enviornment for our new python interpreter to specifically work with Oppia.
```
❯ pyenv virtualenv 3.8.12 Oppia
Looking in links: /tmp/tmp8m4yvlfl
Requirement already satisfied: setuptools in /home/user/.pyenv/versions/3.8.12/envs/Oppia/lib/python3.8/site-packages (56.0.0)
Requirement already satisfied: pip in /home/user/.pyenv/versions/3.8.12/envs/Oppia/lib/python3.8/site-packages (21.1.1)
```

### Step 3. Setting up Python 3.8 for Oppia directory 
In this step, we will be using pyenv to automatically activate the virtualenv as soon as we enter the Oppia directory.
```
❯ cd /home/$USER/$oppia-directory 
pyenv local Oppia
```


