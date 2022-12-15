# Upgrading Python interpreter from any version to version 3.8.165

For effective and effortless switching to the newer version, this guide will provide a brief and detailed instruction on how to achieve just that. Please follow the instructions below carefully.

## Prerequisite

This page is aimed at developers who want to upgrade their Python interpreter in their existing Oppia directory, instead of creating a separate copy of Oppia with the new interpreter.

Before starting, please make sure that your local repo, as well as your remote fork on GitHub, are both up-to-date with the `develop` branch.

## Step 1. Installing python 3.8.16 through pyenv
Our first step is to install the new interpreter version `3.8.16` through pyenv by issuing the following command through a terminal:
```
pyenv install 3.8.16
```

The command might fail with output similar to this one:

```
python-build: definition not found: 3.8.16

See all available versions with `pyenv install --list'.

If the version you need is missing, try upgrading pyenv:

  cd /xxx/.pyenv/plugins/python-build/../.. && git pull && cd -
```

If that is the case then copy the command from the last line of the output and 
execute it to update the available Python versions.

If the command is successful then the output will look like this:
```
❯ pyenv install 3.8.16
Installing Python-3.8.16...
patching file Misc/NEWS.d/next/Build/2021-10-11-16-27-38.bpo-45405.iSfdW5.rst
patching file configure
patching file configure.ac
Installed Python-3.8.16 to /home/user/.pyenv/versions/3.8.16
```

## Step 2. Determining your virtualenv manager

Oppia developers and contributors use either `pyenv` or `direnv` for creating a python virtualenv and automatic switching of python version.

This step will guide you through determining which one you are using currently, so that you can update your virtualenv accordingly.
* Go to the directory where you have installed Oppia and check if you have ***.envrc*** file in that directory. If the ***.envrc*** file is present, that means you are using direnv for virtualenv activation. direnv users should follow the instructions in [Step 3 (a)](#step-3-(a).-setting-up-virtualenv-for-direnv-users).

* In case you don't have a ***.envrc***. file, check if you have ***.python-version*** file in that directory. If the ***.python-version*** file is present, that means you are using pyenv for virtualenv activation. pyenv users should follow the instructions in [Step 3 (b)](#step-3-(b).-setting-up-virtualenv-for-pyenv-users).

## Step 3 (a). Setting up virtualenv for Direnv Users
> **Note**
> Follow this step if you are using direnv as your virtualenv manager.

1. Edit the ***.envrc*** file in your oppia folder to this :
```
use python 3.8.16
```

2. Run this command in the same directory to complete the setup:
```
$ direnv reload
```

## Step 3 (b). Setting up virtualenv for pyenv users
> **Note**
> Follow this step if you are using pyenv as your virtualenv manager.

#### Do the following:

1. In this step, we will set up a new virtual enviornment for our new python interpreter to specifically work with Oppia.

    Use the command given below to set up a virtualenv with python `3.8.16`. Be sure to replace the `{unique-virtualenv-name}` with a suitable virtualenv name:

    ```
    pyenv virtualenv 3.8.16 {unique-virtualenv-name}
    ```
    The above command will produce output as depicted below:

    ```
    ❯ pyenv virtualenv 3.8.16 Oppia
    Looking in links: /tmp/tmp8m4yvlfl
    Requirement already satisfied: setuptools in /home/user/.pyenv/versions/3.8.16/envs/Oppia/lib/python3.8/site-packages (56.0.0)
    Requirement already satisfied: pip in /home/user/.pyenv/versions/3.8.16/envs/Oppia/lib/python3.8/site-packages (21.1.1)
    ```

2. Now, we will be using pyenv to automatically activate the virtualenv as soon as we enter the Oppia directory.
    
    Change the directory to your local Oppia directory.
    ```
    cd /home/$USER/$oppia-directory 
    ```

    Setup the virtualenv to activate on entering the Oppia directory.
    ```
    pyenv local {unique-virtualenv-name}
    ```

## Step 4. Verify you have a working installation
To verify that you have a working installation, do the following:

1. Verify you are using `python 3.8.16` on entering Oppia directory by running `python --version` in your Oppia directory. You should see the following output:
```
python --version
Python 3.8.16
```

2. Spin up a development server to test the new setup through `python -m scripts.start`. You should get a working developement server accessible on `localhost:8181`.
