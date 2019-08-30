### How do I ask for help?

We would like to help you out but please ensure that you propose solutions instead of saying "solve this for me" or "debug this for me".
For example, make sure that your comment on any issue/pull request includes a very clear question at the end that is easy to answer, otherwise people don't know what you're looking for. This often involves showing your work (e.g. what happened when you searched for the error message? what analysis have you done to figure out the root of the issue?). Examples of good questions include: "here is my proposed solution, and here's the analysis I've done to support it, do you agree?" or "here are two ways I could proceed, and the rationale I chose for each; which one would you suggest I go with?". If you can't formulate your question in this way, that might be a sign that you have not yet done enough debugging/analysis on your own.  

### I have not yet received any response/review on an issue/pull request. What should I do?

If you are running into a lack of response and this is blocking work, please feel free to ping again after a couple of days, and if you still get no response please escalate to the development workflow team (led by @apb7). We'd be happy to look into the situation.

### How do I install Oppia ?

Oppia can be installed on your machine running [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29) or [Windows](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29).

If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

### How do I start contributing to Oppia ?

Please refer to [Contributing code to Oppia](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia) for details. Basically, start off by forking the Oppia project on [GitHub](https://github.com/oppia/oppia), then creating your changes against our `develop` branch, and finally send us a pull request.

Also, don't be discouraged if you're new to "open source", or if you're still a student -- many of our contributors are, too. The main thing is that you care about helping more people around the world to learn things better. We'd also be happy to provide mentorship and support if this is your first time contributing to an open source project. 

### Where do I find some good issues to begin with ?

Here are some [issues](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#finding-something-to-do) you can begin with.

### I am facing difficulty in finding the code related to the issue, what do I do ?

The basic pattern is to inspect an element and search for an unique class/keyword (`oppia-signin-google`) and the try git grep `oppia-signin-google` you'll find a file related to this. It will also show the line where the unique word is used in that file.

### How to run only the linting test on a file ?

There is a `pre_commit_linter.py` for linting the files. Let's say you want to run the linting tests on the file. In the oppia directory, run the following command.
 
python scripts/pre_commit_linter.py --path=path/to/the/file

### How to test email functionality?
 You can test email functionality by deploying your own oppia in appengine, this works perfectly, you'll just have to enable the flags from `feconf.py`. Other workaround would be a hacky way to test this using logs: 
- Simple and hacky way: 
   - Enable the email functionality, i.e, make `feconf.CAN_SEND_EMAILS` equals true and other email related flags true. 
   - Change the `send_mail` function of `core/platform/email/gae_email_service.py` to `print` instead of 
    `mail.EmailMessage`.
   - Do the mannual testing which will kisck the email functionality.
   - Check the logs in terminal.

### I am not very familiar with Git, what should I do ?

Here are some materials which will help you get familiarised with Git:
- [Learning Resources](https://github.com/oppia/oppia/wiki/Learning-Resources): For some basic and advanced Git features.
- [Git Cheat Sheet](https://github.com/oppia/oppia/wiki/Git-cheat-sheet): For some commonly used Git commands.

### How do I run tests ?

For information on running tests, please refer to the [Running Tests](https://github.com/oppia/oppia/wiki/Running-Tests) wiki page. Note that there are 3 types of tests: server-side (Python), client-side (Karma) and end-to-end (Protractor). These tests help to ensure that the code is in a working state. Before checking in any commits to the Oppia repository, please ensure that every single test passes. 

### Setup issues

- When setting up, I get a `[gulp-gae] stopping script` message, the server doesn't start, and localhost:8181 is unreachable.
  - Try checking that the folders in `../oppia_tools` actually have files in them; if not, re-run the installation. (See the discussion on [issue #1796](https://github.com/oppia/oppia/issues/1796#issuecomment-217783598) for more details.)

### I’ve made a PR, it’s been reviewed, and I’ve got some changes to make. Do I do this in a new PR or add it to the existing one ?

Add the new changes to the same PR. For instructions on how to do this, see [here](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#address-review-comments-until-all-reviewers-give-lgtm-looks-good-to-me).

### I have merge conflicts on my PR, what should I do ?

In this case, you should resolve these merge conflicts on your local machine and then push the updated version to your branch corresponding to your PR. This is done as follows:
- First merge your branch with develop locally after fetching from the upstream repository (the master one at oppia/oppia) by doing:
 ``` 
   git fetch upstream
   git checkout <your_branch_name_corresponding_to_PR>
   git merge upstream/develop 
 ```
 (if you get `fatal: 'upstream' does not appear to be a git repository` or a similar error, do `git remote add upstream 
 https://github.com/oppia/oppia.git` to add the upstream remote to your local fork of the repository and then do the above 
 3 steps)

- Now, in the terminal, the files which have merge conflicts will be listed, so in your local editor, go to those files and look for merge conflict markers that look like this:
 ```
 <<<<<<< HEAD:<file_name>
 <code_1>
 =======
 <code_2>
 >>>>>>> <commit_id>:<file_name>
 ``` 
 Here <code_1> is the change you did locally, while <code_2> is the corresponding code that is there on develop that is causing the conflict, so here you can choose whether to keep your change, keep the existing one or maybe combine the two.

- After resolving the conflict, the markers (lines starting with `>>>>`, `<<<<` & `===`) should be removed.
- Do this for all the files with merge conflicts and push the code to your branch corresponding to your PR and the merge conflicts error on your PR would be gone!
 
### I need more help, where do I go ?

If you run into any problems, please read our [Developer Wiki](https://github.com/oppia/oppia/wiki), or file an issue on our [issue tracker](github.com/oppia/oppia/issues/), or post to our [developer mailing list](https://groups.google.com/forum/?fromgroups#!forum/oppia-dev).
Or you could probably ask your questions on our official [Gitter](http://gitter.im/oppia/oppia-chat) channel.
