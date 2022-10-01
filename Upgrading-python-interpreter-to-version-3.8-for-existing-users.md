# Upgrading python interpreter version from 3.7.10 to 3.8.12

Currently, in Oppia we are utilizing python interpreter version 3.7.10. We are now in a phase of switching to a more updated interpreter version 3.8.12. For effective and effortless switching to the newer version, this guide will provide a brief and detailed instruction on how to achieve just that. Please follow the below mentioned instructions carefully.

## Prerequisite
Please make sure your local as well as remote fork is up-to-date with the develop. 

## Step 1. Installing python 3.8.12 through pyenv
Our first step is to install the new interpreter version `3.8.12` through pyenv by issuing the following command through a terminal
```
pyenv install 3.8.12
```
After you execute the above command you can expect some output as depicted below :
```
❯ pyenv install 3.8.12
Installing Python-3.8.12...
patching file Misc/NEWS.d/next/Build/2021-10-11-16-27-38.bpo-45405.iSfdW5.rst
patching file configure
patching file configure.ac
Installed Python-3.8.12 to /home/user/.pyenv/versions/3.8.12
```

## Step 2 (a). Setting up virtualenv for Direnv Users
*`Note` : Follow this step if you are using direnv for automatic switching of interpreter versions on entering oppia directory.*

`Important` Inorder to know whether you are using direnv or not please carry out the following instructions.

* Go to the directory where you have installed Oppia and check if you have `.envrc` file in that directory. If the `.envrc` file is present, that means you are using direnv for virtualenv activation.

* In the case you are using `direnv` __please follow the below steps to setup virtualenv activation with direnv. Else if you are not a direnv user you can follow instructions from [Step 2 (b)](#step-2-(b).-setting-up-virtualenv-for-pyenv-users).__

#### Steps :

1. Edit the `.envrc` file in your oppia folder to this
```
use python 3.8.12
```

2. Run this command in the same directory to complete the setup
```
$ direnv reload
```

## Step 2 (b). Setting up virtualenv for pyenv users
*`Note` : Only follow this if you are not using direnv for automatic virtualenv activation*

`Important` Inorder to know whether you are using pyenv or not for virtualenv activation please carry out the following instructions.

* Go to the directory where you have installed Oppia and check if you have `.python-version` file in that directory. If the `.python-version` file is present, that means you are using pyenv for virtualenv activation.

* You can also issue the `pyenv versions` command in your Oppia directory to get the currently active virtualenv. For ex.
  ```
  ❯ pyenv versions
    system
    3.7.10
    3.7.10/envs/init
    3.7.10/envs/oppia
    3.7.13
    3.7.13/envs/oppia_3.7.13
    3.8.12
    3.8.12/envs/oppia_3.8.12
    init
    oppia
    oppia_3.7.13
  * oppia_3.8.12 (set by /home/user/Opensource/oppia-main/oppia/.python-version)
  ```

  The `*` depicts the currently activated virtual enviornment.

* In the case you are using `pyenv` for virtualenv activation __please follow the below steps to setup virtualenv activation with pyenv. Else if you are not a pyenv user you can follow instructions from [Step 2 (a)](#step-2-(a).-setting-up-virtualenv-for-direnv-users).__

#### Steps :

1. In this step, we will be setting up a new virtual enviornment for our new python interpreter to specifically work with Oppia.

    Use the command given below to setup a virtualenv with python `3.8.12`. Be sure to replace the `{unique-virtualenv-name}` with a suitable virtualenv name:

    ```
    pyenv virtualenv 3.8.12 {unique-virtualenv-name}
    ```
    The above command will produce output as depicted below :

    ```
    ❯ pyenv virtualenv 3.8.12 Oppia
    Looking in links: /tmp/tmp8m4yvlfl
    Requirement already satisfied: setuptools in /home/user/.pyenv/versions/3.8.12/envs/Oppia/lib/python3.8/site-packages (56.0.0)
    Requirement already satisfied: pip in /home/user/.pyenv/versions/3.8.12/envs/Oppia/lib/python3.8/site-packages (21.1.1)
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

## Step 3. Verify you have a working installation
To verify that you have right working installation, follow the steps mentioned below :

#### Steps :

1. Verify you are using `python 3.8.12` on entering Oppia directory by running `python --version` in your Oppia directory.

2. Spin up a development server to test the new setup through `python -m scripts.start`
