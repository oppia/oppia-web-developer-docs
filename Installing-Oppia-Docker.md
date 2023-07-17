# **Dockerized Oppia Installation Guide**

This guide provides step-by-step instructions for installing Oppia using Docker. Docker simplifies the installation process and ensures a consistent environment across different systems, making it easier to set up and run Oppia.

## Table of Contents

* Docker - Brief Overview
* Installation Steps
  * Clone Oppia
  * Install Docker Desktop
  * Start development server using `make` commands
* Using Flags with Make Command
* Additional Make Commands

## Docker - Brief Overview

Docker is an open-source platform that automates the deployment, scaling, and management of applications using containerization. Containers provide lightweight and isolated environments that encapsulate application dependencies and configurations, making installations more reliable and error-resistant.

Using Docker to install Oppia eliminates the need for extra configurations or setting up development environments for the local server. It provides a consistent and reproducible environment for running Oppia across different systems.

## Installation Steps

To install Oppia under Docker, follow these steps:

### Clone Oppia

1. Create a new, empty folder that will hold your Oppia work. Here, we call the folder `opensource`.

2. Navigate to the folder (`cd opensource/`). Next, we'll [fork and clone](https://help.github.com/articles/fork-a-repo/) the Oppia repository.

3. Navigate to https://github.com/oppia/oppia and click on the `fork` button. It is placed on the right corner opposite the repository name `oppia/oppia`.

   ![Screenshot with the fork button](images/install/fork.png)

   You should now see Oppia under your repositories. It will be marked as forked from `oppia/oppia`.

   ![Screenshot of repository list with Oppia](images/install/repositoryList.png)

4. Clone the repository to your local computer (replacing the values in `{{}}`):

   ```console
   $ git clone https://github.com/{{GITHUB USERNAME}}/oppia.git
   Cloning into 'oppia'...
   remote: Enumerating objects: 203313, done.
   remote: Total 203313 (delta 0), reused 0 (delta 0), pack-reused 203313
   Receiving objects: 100% (203313/203313), 179.26 MiB | 3.12 MiB/s, done.
   Resolving deltas: 100% (155851/155851), done.
   Updating files: 100% (4199/4199), done.
   ```

   > Note that you will see slightly different output because the numbers change as Oppia grows.

5. Now your `origin` remote is pointing to your fork (`{{GITHUB USERNAME}}/oppia`). To stay up to date with the main `oppia/oppia` repository, add it as a remote called `upstream`. You'll first need to move into the `oppia` directory that was created by the clone operation.

   ```console
   $ cd oppia
   $ git remote add upstream https://github.com/oppia/oppia.git
   $ git remote -v
   origin     https://github.com/{{GITHUB USERNAME}}/oppia.git (fetch)
   origin     https://github.com/{{GITHUB USERNAME}}/oppia.git (push)
   upstream   https://github.com/oppia/oppia.git (fetch)
   upstream   https://github.com/oppia/oppia.git (push)
   ```

   The `git remote -v` command at the end shows all your current remotes.

   Now you can pull in changes from `oppia/oppia` by running `git pull upstream {{branch}}` and push your changes to your fork by running `git push origin {{branch}}`.

   We have established a clean setup now. We can make any changes we like and push it to this forked repository, and then make a pull request for getting the changes merged into the original repository. Here's a nice picture explaining the process ([image source](https://github.com/Rafase282/My-FreeCodeCamp-Code/wiki/Lesson-Save-your-Code-Revisions-Forever-with-Git)).

   ![Diagram of the fork-and-clone workflow](images/install/forkCloneWorkflow.png)

   For making any changes to original repository, we first sync our cloned repository with original repository. We merge develop with `upstream/develop` to do this. Now we make a new branch, do the changes on the branch, push the branch to forked repository, and make a PR from Github interface. We use a different branch to make changes so that we can work on multiple issues while still having a clean version in develop branch.

### Install Docker Desktop
Download and install the latest version of Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop/). Docker Desktop provides a user-friendly interface and one must follow simple steps to download and install it from the given link.

> NOTE: The above 2 steps need to be followed only once. The next time you want to run Oppia, you can directly start from the next section, i.e. by executing simple `make` commands from the root directory of the cloned Oppia repository.

### Start development server using `make` commands

1. **Navigate to Oppia Root Directory**: Open a terminal or command prompt and navigate to the root directory of the cloned Oppia repository.

2. **Build Oppia for the First Time**: Run the following command to build Oppia for the first time. This step downloads all the necessary third-party libraries, python dependencies, and the other services required for the Oppia development server, which may take approximately 15-20 minutes (may vary according to the network connection speed).

   ```
   make setup-devserver
   ```

3. **Start the Local Development Server**: To start the local development server, execute the following command:

   ```
   make run-devserver
   ```

   This command launches the Oppia development server, and you can continue to perform your tasks as usual.


## Using Flags with Make Command

You can use flags with the `make run-devserver` command to modify the behavior of Oppia development server as per the flag which is required to enhance your development workflow. The following table lists the available flags and their descriptions:
- `save_datastore`: This flag saves donot clear the datastore on shutting down the development server.
- `disable_host_checking`: It disables host checking so that the dev server can be accessed by any device on the same network using the host device's IP address. DO NOT use this flag if you're running on an untrusted network.
- `prod_env`: It runs the development server in production mode. This flag is useful for testing the production build of Oppia locally.
- `maintenance_mode`: This flag puts the Oppia development server into the maintenance mode.
- `source_maps`: It builds webpack with source maps.
- `no_auto_restart`: This flag disables the auto-restart feature of the development server when files are changed.

You can run the `make run-devserver` command with any of the above flags as follows:

```
make run-devserver save_datastore=true
```

Similarly, you can use multiple flags with the `make run-devserver` command as follows:

```
make run-devserver prod_env=true maintenance_mode=true
```

## Additional Make Commands

The Oppia development environment provides additional `make` commands that you can use for various purposes. The following lists the available `make` commands and their descriptions --
- `make terminal`: This command opens a terminal in the Docker container environment.
- `make stop-devserver`: It stops and kills the Docker containers running the Oppia development server.
- `make clean`: This command cleans the Oppia development environment (under Docker) by removing all the docker containers, images, and volumes.

## Contributing

If you encounter any issues during the installation process or have suggestions for improvement, please feel free to open a discussion on [Oppia's GitHub Discussion](https://github.com/oppia/oppia/discussions)

------

That's it! You have successfully installed Oppia using Docker, and ready-to-go for your contributions at Oppia.
