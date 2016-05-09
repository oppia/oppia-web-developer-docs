
### How do I install Oppia ?

Oppia can be installed on your machine running [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29) or [Windows](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29). Or if you want to ensure that you always have a clean machine identical to other developers, you may want to install Oppia through [Vagrant](https://github.com/oppia/oppia/wiki/Installing-Oppia%28Vagrant%29). Vagrant will also provide isolation between your host machine and things that Oppia needs to install and change, or allow you to build different development versions of Oppia on different branches.

If you just want to create and share explorations, you may be able to use the hosted server at https://www.oppia.org (in which case you don't need to install anything).

### How do I start contributing to Oppia ?

Please refer to [CONTRIBUTING.md](https://github.com/oppia/oppia/). 
(Basically, start by forking the Oppia project on [Github](https://github.com/oppia/oppia), then creating your changes against our `develop` branch, and finally send us a pull request)

Also, don't be discouraged if you're new to "open source", or if you're still a student -- many of our contributors are, too. The main thing is that you care about helping more people around the world to learn things better. We'd also be happy to provide mentorship and support if this is your first time contributing to an open source project. 

### How do I run tests ?

For information on running tests, please refer to the [Running Tests](https://github.com/oppia/oppia/wiki/Running-Tests) wiki page. Note that there are 3 types of tests: server-side (Python), client-side (Karma) and end-to-end (Protractor). These tests help to ensure that the code is in a working state. Before checking in any commits to the Oppia repository, please ensure that every single test passes. 

### I need more help, where do I go ?

If you run into any problems, please read our [Developer Wiki](https://github.com/oppia/oppia/wiki), or file an issue on our [issue tracker](github.com/oppia/oppia/issues/), or post to our [developer mailing list](https://groups.google.com/forum/?fromgroups#!forum/oppia-dev).
Or you could probably ask your questions on our official [Gitter](http://gitter.im/oppia/oppia-chat) channel, preferably during the following office hours (in UTC):

__Tuesday__ -- 08:30 - 09:00, 21:30 - 22:00, 00:30 - 01:00

__Wednesday__ -- 16:30 - 17:00, 21:30 - 22:00, 00:30 - 01:00

__Sunday__ -- 16:30 - 17:00, 21:30 - 22:00, 00:30 - 01:00 

### Setup issues

- When setting up, I get a `[gulp-gae] stopping script` message, the server doesn't start, and localhost:8181 is unreachable.
  - Try checking that the folders in `../oppia_tools` actually have files in them, and, if not, re-run the installation. (See the discussion on [issue #1796](https://github.com/oppia/oppia/issues/1796#issuecomment-217783598) for more details.)