## Table of Contents
- [Overview](#Overview)
- [When you encounter an installation error](#When-you-encounter-an-installation-error)

***

## Overview

The Oppia team has tried to make it easy to install Oppia on a number of different platforms. Please go to [[Installing Oppia|Installing-Oppia]] page if you want to find guides for different platforms.

We welcome help improving the latter, but if you have a choice, we strongly recommend **using Linux or Mac OS** if possible — it will make things much easier.

## When you encounter an installation error...

...it may look like this is an issue with core Oppia functionality. However, Oppia is a fairly standard web app, and errors during the installation process are usually due to third-party libraries, incomplete downloads, development environments that are behind Web proxies, different Python environments, etc. So, the Oppia team almost certainly doesn't have specialized knowledge that makes it easier for them to help solve the issue, although team members can often provide general guidance. In addition, remote debugging is hard, since other team members do not have access to your local environment.

This means that, to resolve your issue as quickly as possible, you should take a few steps first before contacting the team (e.g. via Gitter). These are likely the same steps that someone who's helping you will take anyway, but doing this yourself is advantageous because you have direct access to your local environment and can debug as needed.

- **Step 1.** There is a [[Troubleshooting|Troubleshooting]] page, where you can find solutions to common errors that you might encounter. See if your error is listed among those cases; if so, apply the solution given. Otherwise, carry on to Step 2.
- **Step 2.** Find the part of the error traceback that describes the error, and copy/paste it into a search engine. See if other people have encountered a similar error, and what they did to get around the problem. You may find that, e.g., the problem is due to your local web proxy, in which case it is an issue that only you can solve.
  - If their solution works for you, hooray! Please let us know if you think adding it to the "Troubleshooting" section will help other users; we'd be happy to do this.
  - If none of the solutions you found work, carry on to step 3.
- **Step 3.** Try and do a bit of local detective work. The setup scripts are all in the `scripts/` directory of the Oppia codebase, and it is a good idea to read them and try to understand what they do. A lot of the logic is in `scripts/setup.py` and `scripts/install_third_party.py`, so you might want to focus on those three files. Try and print things to the console, and see if you can narrow things down to exactly which line of the code is causing the failure (so that you can try running the line of code in isolation, and perhaps print out a more comprehensive error message). Note that the aim of this is to narrow down the problem as much as you can so that it's easy for someone else to help you, so feel free to stop once you have the above information and there are no clear next steps to take.

If you've done all of the above, and are still stuck, then please do ask for help. You can create a [GitHub Discussions](https://github.com/oppia/oppia/discussions/categories/setup-issues), or post to the oppia-dev@ mailing list!