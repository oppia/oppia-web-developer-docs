__If you are looking for more elaborate instructions on how to get started with Oppia, go to [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up).__
If you get stuck somewhere and need help please refer to getting help page[https://github.com/oppia/oppia/wiki/Get-help]

Note that throughout our wiki, we use the following notations:

* `$` represents a command prompt that is not root. For example, if we want you to type the command `python` into your terminal, you'll see `$ python`. This distinguishes commands (which are prefixed with `$`) from output from those commands (whose lines are not prefixed with `$`).
* `#` represents a root command prompt. For example, `# apt-get install python` means to run `apt-get install python` as root (e.g. using `sudo`).
* `...` indicates where we've omitted content for the sake of brevity.

We also assume that readers (and all Oppia developers) are familiar with the
following:

* Standard Unix path notation, including `~` as an abbreviation for the home directory.
* Creating and editing text files, including hidden files. Be careful with using graphical editors like Notepad in Windows. These can add carriage returns (`\r`) that confuse our Linux-based development tools. Instead, we recommend using editors designed for programming or command-line text editors.
* Basic Unix commands like `ls`, `cat`, `echo`, `cd`, etc.
* Using `git`.

If you need to learn or brush up on these, please do so before trying to start the installation so you don't get confused by our instructions.

## Standard installation using Python setup
To install Oppia, follow these instructions:

* [[Linux|Installing-Oppia-(Linux;-Python-3)]]
* [[Mac OS|Installing-Oppia-(Mac-OS;-Python-3)]]
* [[Windows|Installing-Oppia-(Windows;-Python-3)]]

## Experimental installation using Docker - under development
To install Oppia using Docker, follow these instructions:
* [[Oppia Docker Setup|Installing-Oppia-using-Docker]]

If you run into any problems during installation, please read [[these notes|Issues-with-installation]] and the [[Troubleshooting page|Troubleshooting]].

Take a look at our [[guide for getting started with some common code editors|Tips-for-common-IDEs]].

**Warning:** You should always edit Oppia code on your local machine. Do not use web-based editors like github.dev or the editor on github.com. These web-based editors won't run the automated checks that run on your local machine. Pushing without these checks just means that the tests will fail on your PR.
