__If you are looking for more elaborate instructions on how to get started with Oppia, go to [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up).__

Note that throughout our wiki, we use the following notations:

* `$` represents a command prompt that is not root. For example, if we want you to type the command `python` into your terminal, you'll see `$ python`. This distinguishes commands (which are prefixed with `$`) from output from those commands (whose lines are not prefixed with `$`).
* `#` represents a root command prompt. For example, `# apt-get install python` means to run `apt-get install python` as root (e.g. using `sudo`).
* `...` indicates where we've omitted content for the sake of brevity.

To install Oppia, follow these instructions:

* [[Linux|Installing-Oppia-(Linux;-Python-3)]]
* [[Mac OS|Installing-Oppia-(Mac-OS;-Python-3)]]
* [[Windows|Installing-Oppia-(Windows;-Python-3)]]

If you run into any problems during installation, please read [[these notes|Issues-with-installation]] and the [[Troubleshooting page|Troubleshooting]].

Take a look at our [[guide for getting started with some common code editors|Tips-for-common-IDEs]].

**Warning:** You should always edit Oppia code on your local machine. Do not use web-based editors like github.dev or the editor on github.com. These web-based editors won't run the automated checks that run on your local machine. Pushing without these checks just means that the tests will fail on your PR.
