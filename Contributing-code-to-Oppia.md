*These instructions are for developers and designers who'd like to contribute code or design help to improve the Oppia platform. If you'd prefer to help out with other things, please see our [general contribution guidelines](https://github.com/oppia/oppia/wiki).*

Thanks for your interest in improving the Oppia platform! This page explains how to get set up, how to find something to work on, and how to make a code change. If you run into any problems along the way, please file an issue on our [issue tracker](https://github.com/oppia/oppia/issues), or get help by posting to the [developers' mailing list](https://groups.google.com/forum/#!forum/oppia-dev). There are also lots of helpful resources in the [developer wiki](https://github.com/oppia/oppia/wiki) -- check out the sidebar!

## Setting things up

1. Please sign the CLA so that we can accept your contributions. If you're contributing as an individual, use the [individual CLA](https://goo.gl/forms/AttNH80OV0). If your company owns the copyright to your contributions, a company representative should sign the [corporate CLA](https://goo.gl/forms/xDq9gK3Zcv).
1. Fill in the [Oppia contributor survey](https://goo.gl/forms/otv30JV3Ihv0dT3C3) to let us know what your interests are. (You can always change your responses later.)  
1. Create a new, empty folder called `opensource/` in your computer's home folder. Navigate to it (`cd opensource`), then [fork and clone](https://help.github.com/articles/fork-a-repo/) the Oppia repo so that it gets downloaded into `opensource/oppia`. Then follow the appropriate installation instructions -- [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), [Mac OS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29), [Windows](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29). (If you run into any problems during installation, please read [these notes](https://github.com/oppia/oppia/wiki/Issues-with-installation%3F).)
1. Update your GitHub settings:
   * Go to your settings page (click the Settings option under the profile menu in the top right), then go to 'Notification center' and ensure that everything's as you want it.
   * Go to the [Oppia repo](https://github.com/oppia/oppia), and click 'Watch' at the top right. Ensure that you're not 'ignoring' the repo, so that you'll be notified when someone replies to a conversation you're part of.
   * (Optional) Consider setting up [automatic auth](https://help.github.com/articles/caching-your-github-password-in-git/) so you don't have to type in a username and password each time you commit a change.
1. Familiarize yourself with the resources linked to from the sidebar of this page, especially the [overview of the codebase](https://github.com/oppia/oppia/wiki/Overview-of-the-Oppia-codebase), the [coding style guide](https://github.com/oppia/oppia/wiki/Coding-style-guide), and our [Frequently Asked Questions](https://github.com/oppia/oppia/wiki/Frequently-Asked-Questions). You don't have to read all the other stuff right now, but it's a good idea to be aware of what's available, so that you can refer to it later if needed.
1. Join the [oppia-dev@](https://groups.google.com/forum/#!forum/oppia-dev) mailing list, and say hi on the [gitter](https://gitter.im/oppia/oppia-chat) chat channel!
1. On your browser, consider [pinning](https://support.mozilla.org/en-US/kb/pinned-tabs-keep-favorite-websites-open) both this wiki page (for easy reference later) and the [Gitter tab](https://gitter.im/oppia/oppia-chat) (so that you can keep abreast of new activity). To pin a tab, just right-click the tab you want to pin, and select "Pin Tab".
1. Take up your first starter project! You can find more details in the next section.

## Developing your skills

- Consider learning AngularJS (v1), if you're new to it. A nice tutorial can be found [here](https://www.codeschool.com/courses/shaping-up-with-angularjs). Most of our open issues are in the frontend, and require at least some knowledge of HTML, AngularJS and CSS, so knowledge of frontend coding will serve you well if you'd like to contribute to Oppia over the longer term.
- We also have some backend (python) and devops (bash) projects available, but not as many, so we'd strongly recommend learning AngularJS if you have the opportunity and inclination -- otherwise, the range of projects you can take up will be more limited. That said, let us know at welcome@oppia.org if you'd like suggestions for non-frontend projects, and we'll do our best to help.

## Finding something to do...

### ... as a new contributor

Welcome! Please make sure to follow the [setup instructions](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up) above if you haven't already. After that, we'd **strongly recommend** tackling some part of one of the following starter issues:

- [#3826](https://github.com/oppia/oppia/issues/3826) (frontend)
- [#3950](https://github.com/oppia/oppia/issues/3950) (frontend)
- [#3954](https://github.com/oppia/oppia/issues/3954) (e2e tests reorganization; frontend)
- [#4374](https://github.com/oppia/oppia/issues/4374) (docstrings; backend)
- [#4057](https://github.com/oppia/oppia/issues/4057) (frontend; Karma tests)

so that you can become familiar with the codebase and the development workflow. If you decide to do so, please go ahead and leave a comment saying which part of the issue you're taking, and submit a follow-up PR by following the [instructions below](Contributing-code-to-Oppia#instructions-for-making-a-code-change). You don't need to wait for approval to get started!

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

Our central development branch is `develop`, which should be clean and ready for release at any time. In general, all changes should be done as feature branches based off of `develop`. (In case you're interested, we mainly use the [Gitflow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow), which also incorporates `master`, `hotfix-` and `release-` branches -- but you don't need to worry about these.)

Here's how to make a one-off code change. (If you're working on a larger feature, see the instructions at the end.)

1. **Choose a descriptive branch name.** It should be lowercase and hyphen-separated, such as `fuzzy-rules`. Also, it shouldn't start with `hotfix` or `release`.
2. **Create a new branch with this name, starting from 'develop'.** I.e., run:

    ```
      git fetch upstream
      git checkout develop
      git merge upstream/develop
      git checkout -b your-branch-name
    ```

3. **Make commit(s) to your feature branch.** Each commit should be self-contained and have a descriptive commit message that helps other developers understand why the changes were made.
    * You can refer to relevant issues in the commit message by writing, e.g., "Fixes #105".
    * Please read [these style rules](https://github.com/oppia/oppia/wiki/Coding-style-guide) and ensure that your code follows them. If you use [Sublime Text](http://www.sublimetext.com/), consider installing the SublimeLinter, [SublimeLinter-jscs](https://github.com/SublimeLinter/SublimeLinter-jscs) and [SublimeLinter-pylint](https://github.com/SublimeLinter/SublimeLinter-pylint) plugins, following the instructions on their respective pages.
    * Please ensure that the code you write is well-tested.
    * Before making the commit, start up a local instance of Oppia and do some manual testing in order to check that you haven't broken anything! After that, ensure that the added code has no lint errors and passes all automated tests by running the presubmit script:

        ```
          bash scripts/run_presubmit_checks.sh
        ```

    * Check that the changes you've made are exactly what you want them to be, and that you haven't left in anything spurious. You can do this by using a tool like `git diff` or `meld`. Make sure to do this _before_ you push.

    * To actually make the commit and push it to your GitHub fork, run:

        ```
          git commit -a -m "{{YOUR COMMIT MESSAGE HERE}}"
          git push origin {{YOUR BRANCH NAME}}
        ```
    
      Before your code gets uploaded to GitHub, a script is automatically executed that checks the styling of all changed JavaScript and Python files and runs the front-end tests. Run the push command in command line, and not GitHub's Desktop client, as the script needs access to other tools like pip.
    
      **If any of the tests fail, the push will be interrupted**. If this happens, fix the issues that the tests tell you about and **repeat the instructions above** ('commit' and then 'push').

4. **When your feature is ready to merge, create a pull request.**
    * Go to your fork on GitHub, select your branch from the dropdown menu, and click "pull request". Ensure that the 'base' repository is the main oppia repo and that the 'base' branch is 'develop'.
    * Add a descriptive title explaining the purpose of the PR (e.g. "Fix #bugnum: add a warning when the user leaves a page in the middle of an exploration."). The "Fix #bugnum: " prefix **must** be included if this PR resolves an issue on the issue tracker.
    * Ensure that the PR description includes the issue number (e.g. "This PR fixes #bugnum").
    * Click "Create pull request".
    * **Important:** Manually check the "Files changed" tab on your PR on GitHub to make sure that the list of files you want to submit, and the changes you want to make to each, are correct -- e.g., that you haven't left additional console logging statements in them, or left out important files that should be part of the PR. (If not, please fix this by making additional commits, or by closing this PR and submitting a new one, before requesting a review.)
    * Request a review from the issue's "owner" (which can be found in a label on the issue) **and** set the assignee of the PR to be the same person.
    * After a while, check your PR to see whether the Travis checks have passed. If not, follow the instructions at "[If your build fails...](https://github.com/oppia/oppia/wiki/If-your-build-fails)".
    * N.B.: If your PR is incomplete, please add a list of checkboxes representing the to-do list to the github conversation thread (like [this example](https://github.com/oppia/oppia/issues/1205)). That lets the reviewer know that you're already aware of those issues, so that they don't spend time telling you things you already know!
    * N.B.: While you're waiting for a review, it's fine to start work on a new PR. Just make sure to **checkout the develop branch** and sync to HEAD before you check out a new branch, so that each of your feature branches is based off the main trunk.

5. **Address review comments until all reviewers give LGTM ('looks good to me').**
    * When your reviewer has reviewed the code, you'll get an email. You'll need to respond in two ways:
       * Make a new commit addressing the comments you agree with, and push it to the same branch. Ideally, the commit message would explain what the commit does (e.g. "Fix lint error"), but if there are lots of disparate review comments, it's fine to refer to the original commit message and add something like "(address review comments)".
       * In addition, go to the Files Changed tab, and reply to each comment, choosing the "Start a review" option for the first comment. Each reply should be either "Done" or a response explaining why the corresponding suggestion wasn't implemented. When you've responded to all comments, you can add all your messages to the main thread by submitting the review. All comments must be resolved before LGTM can be given.
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
    * Run `bash scripts/start.sh` and play with the dev server in order to make sure that everything still works, and also to install any new dependencies that have been added since you last synced the repo.
    * Once you've finished addressing everything, and would like the reviewer to take another look, **please write a top-level comment explicitly asking them to do so**, and set them as the Assignee for the PR.
    * At the end, the reviewer will merge the pull request.
    * **WARNING:** Do not make changes using the online GitHub editor -- this bypasses lint/presubmit checks, and will cause the code on GitHub to diverge from the code on your machine. Always make commits locally, and then push to GitHub.
6. **Tidy up!** After the PR status has changed to "Merged", delete the feature branch from both your local clone and the GitHub repository:

  ```
    git branch -D new-branch-name
    git push origin --delete new-branch-name
  ```

7. **Celebrate.** Congratulations, you have contributed to Oppia!

### Notes

We do not use author tags in files, since they tend to be inaccurate or become stale when the author is no longer a regular contributor. However, you can still find the author of a particular change in a file by running the command:

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

## Communication channels

### Mailing lists

We have several mailing lists in the form of Google Groups that you can join:
  * [oppia-announce](https://groups.google.com/forum/#!forum/oppia-announce) is for announcements of new releases or blog posts.
  * [oppia-dev](https://groups.google.com/forum/#!forum/oppia-dev) is the main mailing list for communication between developers, and for technical questions.

We also have a developer chat room [here](https://gitter.im/oppia/oppia-chat). Feel free to drop in and say hi!
