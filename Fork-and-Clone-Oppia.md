For a detailed explanation for fork and clone, you can go to [github help page](https://help.github.com/articles/fork-a-repo/#platform-linux)

Make sure you are in `opensource/` folder. Now follow the steps below :
- Click on the `fork` button. It is placed on the right corner opposite to repository name `oppia/oppia`.
![fac1](https://user-images.githubusercontent.com/9693472/43354371-cfd77cec-9268-11e8-8b70-a89e7a00f3c9.png)

- You can now see Oppia under your repositories. It will be marked as forked from `oppia/oppia`
![fac2](https://user-images.githubusercontent.com/9693472/43354380-5cd4854a-9269-11e8-9fe5-266d330761ed.png)

- Let's clone this repository to your local computer using
  ```git clone https://github.com/USERNAME/oppia.git```

- We will configure remote repositories to keep your local repository, forked repository and main oppia repository in sync. You can check your current remote repositories by typing `git remote -v`.

- Type the following to add oppia as upstream
  ```git remote add upstream https://github.com/oppia/oppia```.

- And we are done! You can access main oppia repository using `git fetch upstream` and access your forked version using `git fetch origin`.

