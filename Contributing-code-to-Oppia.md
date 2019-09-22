*These instructions are for developers and designers who'd like to contribute code or design help to improve the Oppia platform. If you'd prefer to help out with other things, please see our [general contribution guidelines](https://github.com/oppia/oppia/wiki).*

Thanks for your interest in improving the Oppia platform! This page explains how to get set up, how to find something to work on, and how to make a code change. If you run into any problems along the way, please file an issue on our [issue tracker](https://github.com/oppia/oppia/issues), or get help by posting to the [developers' mailing list](https://groups.google.com/forum/#!forum/oppia-dev). There are also lots of helpful resources in the sidebar, check that out too!

Also, if you'd like to get familiar with Oppia from a user's point of view, you can take a look at the [user documentation](http://oppia.github.io/).

## Setting things up

1. Please sign the CLA so that we can accept your contributions. If you're contributing as an individual, use the [individual CLA](https://goo.gl/forms/AttNH80OV0). If your company owns the copyright to your contributions, a company representative should sign the [corporate CLA](https://goo.gl/forms/xDq9gK3Zcv).
1. Fill in the [Oppia contributor survey](https://goo.gl/forms/otv30JV3Ihv0dT3C3) to let us know what your interests are. (You can always change your responses later.)  
1. Create a new, empty folder called `opensource/` in your computer's home folder. Navigate to it (`cd opensource`), then [fork and clone](https://help.github.com/articles/fork-a-repo/) ([why?](https://github.com/oppia/oppia/wiki/Why-fork-and-clone-Oppia%3F)) the Oppia repo so that it gets downloaded into `opensource/oppia`. Then, go to `opensource/oppia` (`cd oppia`) and do `git remote add upstream https://github.com/oppia/oppia.git` (use `git@github.com:oppia/oppia.git` if using SSH) to add a remote called upstream and link it to Oppia's main repository (this will be used to merge with the latest version on develop, mentioned later on and also to prevent running lint checks on merge commits when you later update your local branch with upstream/develop). Then follow the appropriate installation instructions -- [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29), [Windows](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29).
    - **Please do not use `sudo` at any point of the installation.** Oppia's setup does not require it. If you face any permissions issues, please make sure that the directory where you're trying to setup Oppia does not require additional permissions. If you run into any other problems during installation, please read [these notes](https://github.com/oppia/oppia/wiki/Issues-with-installation%3F).
   - If your upstream is not set correctly, the lint checks will run on merge commits as well. The way to fix this will be to update the upstream url by running the following command: `git remote set-url upstream https://github.com/oppia/oppia.git` (use `git@github.com:oppia/oppia.git` if using SSH)
1. Update your GitHub settings:
   * [Set up 2FA](https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/) on your GitHub account. **This is important to prevent people from impersonating you.**
       * You might need to create a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) so that you can log in from the command line.
   * Go to your [Notifications page](https://github.com/settings/notifications), and configure it according to your preferences.
   * (Optional) Consider setting up [automatic auth](https://help.github.com/articles/caching-your-github-password-in-git/) so you don't have to type in a username and password each time you commit a change.
   * (Optional) Go to the [Oppia repo](https://github.com/oppia/oppia), and click 'Watch' at the top right. Ensure that you're not 'ignoring' the repo, so that you'll be notified when someone replies to a conversation you're part of.
1. Familiarize yourself with the resources linked to from the sidebar of this page, especially the [overview of the codebase](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase), the [coding style guide](https://github.com/oppia/oppia/wiki/Coding-style-guide), and our [Frequently Asked Questions](https://github.com/oppia/oppia/wiki/Frequently-Asked-Questions). You don't have to read all the other stuff right now, but it's a good idea to be aware of what's available, so that you can refer to it later if needed.
1. Join the [oppia-dev@](https://groups.google.com/forum/#!forum/oppia-dev) mailing list, and say hi on the [gitter](https://gitter.im/oppia/oppia-chat) chat channel!
1. On your browser, consider [pinning](https://support.mozilla.org/en-US/kb/pinned-tabs-keep-favorite-websites-open) both this wiki page (for easy reference later) and the [Gitter tab](https://gitter.im/oppia/oppia-chat) (so that you can keep abreast of new activity). To pin a tab, just right-click the tab you want to pin, and select "Pin Tab".
1. If you use [Sublime Text](http://www.sublimetext.com/), consider installing the SublimeLinter, [SublimeLinter-jscs](https://github.com/SublimeLinter/SublimeLinter-jscs) and [SublimeLinter-pylint](https://github.com/SublimeLinter/SublimeLinter-pylint) plugins, following the instructions on their respective pages.
1. Take up your first starter project! You can find more details in the next section.

## Developing your skills

In general, it's easier to contribute to the Oppia codebase if you have some knowledge of git, as well as at least one of Python or AngularJS. You don't need to know all of this before you start, though! Many of our contributors have picked these skills up concurrently while tackling their first issues.

That said, we strongly recommend that you be open to learning new things. If you need to brush up on some of the technologies used in Oppia, here are some resources that may help:

- Git and Github are used to make changes to the repository. So, it's good to know how to use them to do basic stuff like branching, merging, pull/push etc. [Here](https://github.com/oppia/oppia/wiki/Learning-Resources) is a page we've compiled that contains some links to useful learning materials.
- AngularJS (v1) is used for Oppia's frontend. A nice youtube video tutorial can be found [here](https://www.youtube.com/watch?v=nO1ROKMjPqI&list=PLvZkOAgBYrsS_ugyamsNpCgLSmtIXZGiz) and you can check the official [tutorial](https://docs.angularjs.org/tutorial/index)/[guide](https://docs.angularjs.org/guide), also for an outline of AngularJS you can take a look into this [short overview](https://egghead.io/articles/new-to-angularjs-start-learning-here) with pointers to other resources. Most of our open issues are in the frontend and require at least some knowledge of HTML, AngularJS and CSS, so knowledge of frontend coding will serve you well if you'd like to contribute to Oppia over the longer term.
- If you are new to HTML, some tutorials include [Mozilla's guide](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) (which includes some practice assessments), as well as [this tutorial for beginners](http://htmldog.com/guides/html/beginner/).
- We also have some backend (python) and devops (bash) projects available, but not as many, so we'd strongly recommend learning AngularJS if you have the opportunity and inclination -- otherwise, the range of projects you can take up will be more limited. That said, let us know at welcome@oppia.org if you'd like suggestions for non-frontend projects, and we'll do our best to help.

## Finding something to do...

### ... as a new contributor

Welcome! Please make sure to follow the [setup instructions](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) above if you haven't already. After that, we'd **strongly recommend** tackling some part of one of the following starter issues:
- [#4057](https://github.com/oppia/oppia/issues/4057) (frontend; Karma tests)
- [#5002](https://github.com/oppia/oppia/issues/5002) (full stack; removing GLOBALS from html)
- [#6240](https://github.com/oppia/oppia/issues/6240) (writing end to end tests)

so that you can become familiar with the codebase and the development workflow. If you decide to do so, please go ahead and leave a comment saying which part of the issue you're taking, and submit a follow-up PR by following the [instructions below](Contributing-code-to-Oppia#instructions-for-making-a-code-change). You don't need to wait for approval to get started! 

**Important Note**: Please make sure to read and follow the [PR instructions](Contributing-code-to-Oppia#instructions-for-making-a-code-change) carefully, otherwise your PR review may be delayed.

### ... after completing two starter projects

After you've completed parts of at least two different starter projects and successfully submitted PRs for them into develop, we'll add you as a collaborator on the Oppia repository. Please visit [this link](https://github.com/oppia/oppia/invitations) to accept the invitation to collaborate. We'll also get in touch to suggest suitable longer-term projects based on your interests, but please feel free to email us at admin@oppia.org if you don't receive the email!

### ... as an existing contributor

There are lots of options!

- **Want easy projects?** Check out our [list of "good first issues"](https://github.com/oppia/oppia/labels/good%20first%20issue).
- **Want projects that matter?** Check out our [list of high-priority issues](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3Aimportant).
- **Want to practice debugging?** Check out our [list of issues needing debugging help](https://github.com/oppia/oppia/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20label%3A%22needs%20debugging%22%20).
- **Want to practice writing a design doc?** Check out the [list of issues requiring a design doc](https://github.com/oppia/oppia/labels/needs%20design%20doc). This is useful for learning how to write good "technical implementation" proposals.
- **Want to join a team working on a larger effort?** See our [list of projects](https://github.com/oppia/oppia/projects).
- **Want to lead a project?** Let us know by emailing admin@oppia.org. We may offer you the opportunity to do this once you've sent in several good PRs.
- **Want help figuring out what to do?** Just ask us on [Gitter](https://gitter.im/oppia/oppia-chat), or send an email to admin@oppia.org. We'll try to help!

If an issue hasn't got someone assigned to it, and there's no existing PR for the issue (you can check this by scanning the list of [existing PRs](https://github.com/oppia/oppia/pulls)), feel free to take it up by assigning yourself to it. You don't need to ask permission to do so. Also, if you need help or advice on an issue, you can contact the corresponding team lead, whose GitHub username you can find in the issue's grey label.

## Instructions for making a code change

**Working on your first Pull Request?** You can learn how from this free series: [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).

*If your change isn't trivial, please [talk to us](https://gitter.im/oppia/oppia-chat) before you start working on it -- this helps avoid duplication of effort, and allows us to offer advice and suggestions. For larger changes, it may be better to first create a short doc outlining a suggested implementation plan, and send it to the dev team for feedback.*

The following instructions describe how to make a one-off code change using a feature branch. (In case you're interested, we mainly use the [Gitflow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).) Please follow them carefully, otherwise your code review may be delayed.

1. **Choose a descriptive branch name.** It should be lowercase and hyphen-separated, such as `fuzzy-rules`. Also, it shouldn't start with `hotfix` or `release`.
2. **Before coding anything, create a new branch with this name, starting from 'develop'.** I.e., run:

    ```
      git fetch upstream
      git checkout develop
      git merge upstream/develop
      git checkout -b your-branch-name
    ```

3. **Make commit(s) to your feature branch.** Each commit should be self-contained and have a descriptive commit message that helps other developers understand why the changes were made. However, **do not write "Fix #ISSUE_NUMBER"** (e.g. Fix #99999) in your commit messages, as this will cause Github to close the original issue automatically. You can rename your commit messages using `git commit --amend`.

    * Before making the commit, do some sanity-checks:
       * Start up a local instance of Oppia and do some manual testing in order to check that you haven't broken anything!
       * Ensure that your code follows [the style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide) and that it is well-tested.
       * Ensure that the code has no lint errors and passes all automated tests by running the presubmit script:

            ```
              bash scripts/run_presubmit_checks.sh
            ```
      * Use a tool like `git diff` or `meld` to check that the changes you've made are exactly what you want them to be, and that you haven't left in anything spurious. Make sure to do this _before_ you push.

    * To actually make the commit and push it to your GitHub fork, run:

        ```
          git commit -a -m "{{YOUR COMMIT MESSAGE HERE}}"
          git push origin {{YOUR BRANCH NAME}}
        ```

      Make sure to do this from the command line (and not GitHub's Desktop client), since this also runs some important presubmit checks before your code gets uploaded to GitHub. **If any of these checks fail, the push will be interrupted**. If this happens, fix the issues that the tests tell you about and **repeat the instructions above** ('commit' and then 'push').

4. **When your feature is ready to merge, create a pull request.**
    * Go to your fork on GitHub, select your branch from the dropdown menu, and click "pull request". Ensure that the 'base' repository is the main oppia repo and that the 'base' branch is 'develop'. Add a descriptive title explaining the purpose of the PR (e.g. "Fix issue #bugnum: add a warning when the user leaves a page in the middle of an exploration.").
       * If the PR resolves an issue on the issue tracker, the title must start with **"Fix #bugnum: "**. This will be the case for most PRs.
       * However, if your PR fixes part of a bigger issue (e.g. the first-contributor-issues listed above), please use **"Fix part of #bugnum: "** instead. Otherwise, GitHub will close the entire issue automatically when your PR is merged.
    * Fill out the PR checklist, ensuring that your PR description includes the issue number (e.g. "This PR fixes issue #bugnum" or "This PR fixes part of issue #bugnum").
    * If users can now do any actions as a result of your PR that they couldn't do before (e.g. rating an exploration, adding a hint to a state, or replying to a feedback thread), **cc the QA team** (using @oppia/qa-team) so that they can ensure that there is sufficient automated test coverage and/or add it to the list of critical user journeys. (This is important to prevent the new functionality you added from breaking in the future!)
    * Click "Create pull request", then **immediately** check the "Files changed" tab on your PR on GitHub and read it carefully to make sure that the changes are correct (e.g., that you haven't left out important files that should be part of the PR. (If not, please fix this by making additional commits, or by closing this PR and submitting a new one, before requesting a review.) This is a good way to catch obvious errors that would otherwise lead to delays in the review process.
    * Request a review from the issue's "owner" (which can be found in a label on the issue) **and** also set them as the PR assignee.
    * Leave a top-level comment on your PR saying "@{{reviewer}} PTAL", where {{reviewer}} is the GitHub username of your reviewer. ("PTAL" means "Please take a look".)
    * After a while, check your PR to see whether the Travis checks have passed. If not, follow the instructions at "[If your build fails...](https://github.com/oppia/oppia/wiki/If-your-build-fails)".
    * Then, wait for your code to get reviewed! While you're doing so, it's totally fine to start work on a new PR if you like. Just make sure to **checkout the develop branch** and sync to HEAD before you check out a new branch, so that each of your feature branches is based off the main trunk.

5. #### **Address review comments until all reviewers give LGTM ('looks good to me').** 
    * When your reviewer has reviewed the code, you'll get an email. You'll need to respond in two ways:
       * Make a new commit addressing the comments you agree with, and push it to the same branch. (Continue to use descriptive commit messages. If your commit addresses lots of disparate review comments, it's fine to refer to the original commit message and add something like "(address review comments)".)
          * **Always make commits locally, and then push to GitHub.** Don't make changes using the online GitHub editor -- this bypasses lint/presubmit checks, and will cause the code on GitHub to diverge from the code on your machine.
          * **Never force-push changes to GitHub once reviews have started.** This will delay your review, because it overwrites history on GitHub and makes the incremental changes harder to review.
       * In addition, reply to each comment via the Files Changed tab, choosing the "Start a review" option for the first comment. Each reply should be either "Done" or a response explaining why the corresponding suggestion wasn't implemented. Once you have replied "Done" (or similar), you can also click "Resolve conversation" to close the comment thread. When you've responded to all comments, submit the review to add all your messages to the main thread. All comments must be responded to and resolved before LGTM can be given.
    * Resolve any merge conflicts that arise. To resolve conflicts between 'new-branch-name' (in your fork) and 'develop' (in the oppia repository), run:

      ```
        git checkout new-branch-name
        git fetch upstream
        git merge upstream/develop
        ...[fix the conflicts -- see https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line]...
        ...[make sure the tests pass before committing]...
        git commit -a
        git push origin new-branch-name
      ```
    * Once you've finished addressing everything, and would like the reviewer to take another look:
       * Run `bash scripts/start.sh` and play with the dev server in order to make sure that everything still works.
       * Check that the changes in the "Files Changed" tab are what you intend them to be.
       * **Write a top-level comment** explicitly asking the reviewer to take another look (e.g. "@XXX PTAL"), and set them as the assignee for the PR.
    * At the end, the reviewer will merge the pull request.

6. **Tidy up!** After the PR status has changed to "Merged", delete the feature branch from both your local clone and the GitHub repository:

     ```
       git branch -D new-branch-name
       git push origin --delete new-branch-name
     ```

7. **Celebrate.** Congratulations, you have contributed to Oppia!

### Notes

* Our central development branch is `develop`, which should be clean and ready for release at any time. All changes should be done in feature branches based off of `develop`.

* If you face any issues while setting things up, or your PR build fails unexpectedly (please go through the logs of the PR build and try debugging the problem on your own first!), feel free to ping **@oppia/dev-workflow-team** for help.

* To find the author of a particular change in a file, run this command:

  ```
  git blame file-name
  ```
  The output will show the latest commit SHA, author, date, and time of commit for each line.

  To confine the search of an author between particular lines in a file, you can use:

  ```
  git blame -L 40,60 file-name
  ```
  The output will then show lines 40 to 60 of the particular file.

  For more `git blame` options, you can visit the [git blame documentation](https://git-scm.com/docs/git-blame).

* If your PR includes changing the location of the file, if you simply move the file by cut and paste method, then the git will track it as a new file. So to prevent this, use:
  ```
  git mv old_file_path new_file_path
  ```
  By using this command git will detect the file as a renamed file.

## Communication channels

### Mailing lists

We have several mailing lists in the form of Google Groups that you can join:
  * [oppia-announce](https://groups.google.com/forum/#!forum/oppia-announce) is for announcements of new releases or blog posts.
  * [oppia-dev](https://groups.google.com/forum/#!forum/oppia-dev) is the main mailing list for communication between developers, and for technical questions.
  * [oppia-dev-workflow](https://groups.google.com/forum/#!forum/oppia-dev-workflow-team) is the mailing list for communication between Dev Workflow Team, and for workflow issues faced by the contributor.

We also have a developer chat room [here](https://gitter.im/oppia/oppia-chat). Feel free to drop in and say hi!
