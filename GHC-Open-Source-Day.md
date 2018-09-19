# Getting Ready for Open Source Day

## How To Get Started
This document serves as a way to get you introduced to Oppia and also guides you to make your first change in Oppia’s codebase.
* Oppia’s codebase sits in Github at https://github.com/oppia. Some knowledge of Github would be useful to make changes to the repository. Take a look at the [Github guides](https://guides.github.com/activities/hello-world/) for a brief introduction to Github along with some common methods. 
* AngularJS (v1) is used for Oppia's frontend. A nice youtube video tutorial can be found [here](https://www.youtube.com/watch?v=nO1ROKMjPqI&list=PLvZkOAgBYrsS_ugyamsNpCgLSmtIXZGiz), also for an outline of AngularJS you can take a look into this [short overview](https://egghead.io/articles/new-to-angularjs-start-learning-here) with pointers to other resources. 
* If you are new to HTML, some useful tutorials are [Mozilla's guide](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) (which includes some practice assessments), as well as [this tutorial for beginners](http://htmldog.com/guides/html/beginner/).
* New features often require backend work. The Oppia backend is written in Python 2.7.

## Setting Up Before Open Source Day

### CLA

Please [sign the CLA](https://goo.gl/forms/AttNH80OV0) so that we can accept your contributions.

### GitHub

To make code changes, you will require a Github account with 2 factor authentication set up.

* [Install Github](https://help.github.com/articles/set-up-git/).
* [Set up 2FA](https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/) on your GitHub account. This is important to prevent people from impersonating you.
  * You might need to create a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) so you can log in from the command line.
* Go to your settings page (click the Settings option under the profile menu in the top right), then go to 'Notifications' and ensure that everything's as you want it.
* (Optional) Consider setting up [automatic auth](https://help.github.com/articles/caching-your-github-password-in-git/) so you don't have to type in a username and password each time you commit a change.
* (Optional) Go to the [Oppia repo](https://github.com/oppia/oppia), and click 'Watch' at the top right. Ensure that you're not 'ignoring' the repo, so that you'll be notified when someone replies to a conversation you're part of.

### Installing Oppia
* Create a new, empty folder called `opensource/` in your computer's home folder. Navigate to it (`cd opensource`), then [fork and clone](https://help.github.com/articles/fork-a-repo/) the Oppia repo so that it gets downloaded into `opensource/oppia`.
* Then follow the appropriate installation instructions -- [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29), [Windows](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29), [Vagrant](https://github.com/oppia/oppia/wiki/Installing-Oppia%28Vagrant%29). (If you run into any problems during installation, please read [these notes](https://github.com/oppia/oppia/wiki/Issues-with-installation%3F).)

## Some useful links
_Oppia_ [Wiki Page](https://github.com/oppia/oppia/wiki) | [Documentation](https://oppia.github.io/#/) | [Full "Getting Started" page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up)

_Github_ [Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) | [Guide](https://guides.github.com/activities/hello-world/)

_AngularJS_ [Tutorial](https://docs.angularjs.org/tutorial/index) | [Guide](https://docs.angularjs.org/guide)

_Python 2.7_ [Introduction](https://docs.python.org/2/library/intro.html) | [Tutorial](https://docs.python.org/2/tutorial/index.html) | [Documentation](https://docs.python.org/2/index.html)

_Bash_ [Introduction](http://cs.lmu.edu/~ray/notes/bash/)



## Making A Code Change
Our central development branch is **develop**, which should be clean and ready for release at any time. In general, all changes should be done as feature branches based off of _develop_. For a more detailed explanation on how to make a code change, please take a look at [this wiki page](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#instructions-for-making-a-code-change). 
In order to make a change in the repository, you can follow the steps below:

1. Sync with the _develop_ branch and create a new branch, starting from _develop_ (e.g. _your-branch-name_). The branch name should be descriptive, lowercase, and hyphen-separated. It shouldn’t start with the words _hotfix_ or _release_.
```bash
git fetch upstream
git checkout develop  
git merge upstream/develop 
git checkout -b your-branch-name
```

2. Make commit(s) to your feature branch. Each commit should be self-contained and have a descriptive commit message that helps other developers understand why the changes were made.
   * Before your code gets uploaded to GitHub, a script is automatically executed that checks the styling of all changed files and runs some front-end tests. **Run the 'push' command in command line** as the script needs access to other tools like pip.
   * If any of the tests fail, the push will be interrupted. If this happens, fix the issues that the tests tell you about and repeat the instructions above ('commit' and then 'push').

3. When your feature is ready to merge, create a pull request on Github. When you create a pull request, you will be assigned a reviewer who will take a look at your code.

4. **Address review comments until all reviewers give LGTM ('looks good to me').**
   * Resolve any merge conflicts that arise.
   * Run `bash scripts/start.sh` and play with the dev server in order to make sure that everything still works, and also to install any new dependencies that have been added since you last synced the repo.
   * WARNING: Do not make changes using the online GitHub editor -- this bypasses lint/presubmit checks, and will cause the code on GitHub to diverge from the code on your machine. Always make commits locally, and then push to GitHub.

5. Tidy up! After the PR status has changed to "Merged", delete the feature branch from both your local clone and the GitHub repository

6. Celebrate. Congratulations, you have contributed to Oppia!

## What to do when you are stuck
We have set up a Gitter chat room where everyone can post their questions and help each other out. The organizers and mentors will be walking around as well to help with any questions. If this doesn’t work, consider posting in the [Oppia gitter chat](https://gitter.im/oppia/oppia-chat) as well!
