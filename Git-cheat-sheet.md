This page is meant as a handy reference for some basic Git commands.

1. Add a remote to link your local copy of the repository (cloned from your fork) to the main Oppia repository. Required for all the 'upstream' based commands below.
  ```
     $ git remote add upstream https://github.com/oppia/oppia.git
  ```
2. After making a local clone of Oppia, you can change code in your local `oppia/` directory. Git will track these changes. At any time, you can check what git thinks has been changed using:
  
  ```
     $ git status
  ```

  You can also view diffs of your changes by typing:

  ```
     $ git diff
  ```

3. To sync your local code with the latest updates from the GitHub repo, run:

  ```
    $ git fetch upstream
    $ git merge upstream/develop
  ```

4. To download a branch someone else created:

  ```
     $ git checkout -b {{branch-name}}
     $ git pull https://github.com/{{their-repo-name}}/oppia.git {{branch-name}}
  ```

5. To create a patch:

  ```
     $ git checkout {{branch-to-patch-from}}
     $ git format-patch -1   # goes back one commit
  ```
  
  This should create a file with the extension .patch. The name should include part of the commit message from the change it is patching. You may need to move this file outside `oppia/` so that it won't disappear when you switch branches.

6. To apply a patch:

  ```
     $ git checkout {{branch-to-patch-to}}
     $ git apply {{patch-file-name}}
  ```

7. To squash the last three commits into a single one:

  ```
    git reset --soft HEAD~3 &&
    git commit -m "{{YOUR_COMMIT_MESSAGE_HERE}}"
  ```

  Be careful to only squash "local" commits -- never squash anything that has been uploaded to the codesite before (no matter what branch). In particular, don't squash commits that already have code review comments on them. Also, don't squash any commit that merged two branches.

  If you want to squash commits that you previously pushed to GitHub, make a new local branch that includes the small commits, squash the commits locally, and push the new branch instead.
