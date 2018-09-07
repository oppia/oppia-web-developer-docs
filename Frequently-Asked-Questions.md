
### How do I install Oppia ?

Oppia can be installed on your machine running [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29) or [Windows](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29). Or if you want to ensure that you always have a clean machine identical to other developers, you may want to install Oppia through [Vagrant](https://github.com/oppia/oppia/wiki/Installing-Oppia%28Vagrant%29). Vagrant will also provide isolation between your host machine and things that Oppia needs to install and change, or allow you to build different development versions of Oppia on different branches.

If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

### How do I start contributing to Oppia ?

Please refer to [Contributing code to Oppia](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia) for details. Basically, start off by forking the Oppia project on [GitHub](https://github.com/oppia/oppia), then creating your changes against our `develop` branch, and finally send us a pull request.

Also, don't be discouraged if you're new to "open source", or if you're still a student -- many of our contributors are, too. The main thing is that you care about helping more people around the world to learn things better. We'd also be happy to provide mentorship and support if this is your first time contributing to an open source project. 

### Can't find a way to begin contributing ?

Here are some [issues](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#finding-something-to-do) you can begin with.

### Facing difficulty in finding the code related to the issue ?

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

### Need help with the Git?

- Check [Learning Resources](https://github.com/oppia/oppia/wiki/Learning-Resources) for some basic and advanced Git features.
- Check the [Git Cheat Sheet](https://github.com/oppia/oppia/wiki/Git-cheat-sheet) for some commonly used commands.

### How do I run tests ?

For information on running tests, please refer to the [Running Tests](https://github.com/oppia/oppia/wiki/Running-Tests) wiki page. Note that there are 3 types of tests: server-side (Python), client-side (Karma) and end-to-end (Protractor). These tests help to ensure that the code is in a working state. Before checking in any commits to the Oppia repository, please ensure that every single test passes. 

### Setup issues

- When setting up, I get a `[gulp-gae] stopping script` message, the server doesn't start, and localhost:8181 is unreachable.
  - Try checking that the folders in `../oppia_tools` actually have files in them; if not, re-run the installation. (See the discussion on [issue #1796](https://github.com/oppia/oppia/issues/1796#issuecomment-217783598) for more details.)

### I’ve made a PR, it’s been reviewed, and I’ve got some changes to make. Do I do this in a new PR or add it to the existing one?

Add the new changes to the same PR. For instructions on how to do this, see [here](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#address-review-comments-until-all-reviewers-give-lgtm-looks-good-to-me).

### I need more help, where do I go ?

If you run into any problems, please read our [Developer Wiki](https://github.com/oppia/oppia/wiki), or file an issue on our [issue tracker](github.com/oppia/oppia/issues/), or post to our [developer mailing list](https://groups.google.com/forum/?fromgroups#!forum/oppia-dev).
Or you could probably ask your questions on our official [Gitter](http://gitter.im/oppia/oppia-chat) channel, preferably during the following office hours (in UTC):

__Tuesday__ -- 08:30 - 09:00, 21:30 - 22:00, 00:30 - 01:00

__Wednesday__ -- 16:30 - 17:00, 21:30 - 22:00, 00:30 - 01:00

__Sunday__ -- 16:30 - 17:00, 21:30 - 22:00, 00:30 - 01:00 
