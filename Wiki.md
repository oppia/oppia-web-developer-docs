## Table of contents

* [Wiki architecture](#wiki-architecture)
* [Contributing to the wiki](#contributing-to-the-wiki)
  * [Opening a pull request](#opening-a-pull-request)
  * [Run pylint on python files in the Oppia-docs-repo](#run-pylint-on-python-files-in-the-oppia-docs-repo)
  * [When you make changes through the web interface](#when-you-make-changes-through-the-web-interface)
* [Implementation details](#implementation-details)
  * [GitHub App for synchronizer bot](#github-app-for-synchronizer-bot)
  * [Workflow to revert changes through the web interface](#workflow-to-revert-changes-through-the-web-interface)
  * [Security analysis](#security-analysis)
  * [Failed to push changes to wiki upon PR merge](#failed-to-push-changes-to-wiki-upon-pr-merge)

## Wiki architecture

Our wiki consists of the following components:

* The `oppia/oppia.wiki` git repository automatically created by GitHub to hold the wiki viewable at https://github.com/oppia/oppia/wiki. This is our deployment repository where we put wiki source files to be viewed by the community.
* The `oppia/oppia-web-developer-docs` repository is our source repository where we store and edit the wiki source files. We consider this to be the single source of truth for our wiki.
* A [synchronizer bot](https://github.com/apps/oppia-wiki-synchronizer) that keeps the source and deployment repositories in sync. While you might think of bots as running on their own servers somewhere, our bot's code lives in GitHub Actions workflows in both the source and deployment repositories:

  * A [`revert-web-wiki-updates.yml`](https://github.com/oppia/oppia/blob/develop/.github/workflows/revert-web-wiki-updates.yml) workflow in `oppia/oppia` reverts any changes made to the wiki through the web interface by creating a revert commit in the deployment repository and pushing that commit to the source repository.
  * A [`deploy.yml`](https://github.com/oppia/oppia-web-developer-docs/blob/develop/.github/workflows/deploy.yml) workflow in the source repository deploys any new commits in the source repository to the deployment repository.

## Contributing to the wiki

If you notice something about the wiki that could be improved, please let us know! There are a couple of ways you can do so:

* If the improvement you have in mind is big, you want feedback before you start working on it, or you don't have time to make the change yourself, [open an issue](https://github.com/oppia/oppia-web-developer-docs/issues/new/choose) in the source repository.
* If you can make the change yourself, see the instructions below for opening a pull request (PR).

### Opening a pull request

For your first contribution, you'll need to set up your repository (you only have to do this once):

1. [Create a fork](https://github.com/oppia/oppia-web-developer-docs/fork) of the source repository into your user account (which we'll refer to as `user` from now on).

2. Clone the fork to your computer (you can also use SSH if you prefer):

   ```console
   git clone https://github.com/user/oppia-web-developer-docs.git
   ```

3. Add the upstream repository as a remote:

   ```console
   git remote add upstream https://github.com/oppia/oppia-web-developer-docs.git
   ```

Then for every new contribution (including your first), you should follow these steps:

1. Checkout the `develop` branch and pull in the latest changes from upstream:

   ```console
   git checkout develop
   git pull upstream develop
   ```

2. Create a new branch for your changes:

   ```console
   git checkout -b {{branch name}}
   ```

3. Make your changes, being sure to follow our [[style guide|Wiki-style-guide]]. You can use whatever text editor you prefer for this.

4. Commit your changes. You can make multiple commits as you write if you prefer.

   ```console
   git add {{paths to the files you changed}}
   git commit
   ```

5. Push your changes to your fork (called `origin` by default):

   ```console
   git push -u origin {{branch name}}
   ```

6. [Open a pull request.](https://github.com/oppia/oppia-web-developer-docs/compare) Remember to click the "compare across forks" link since your changes are on a different fork than the source repository. The base for your PR should be the `develop` branch on the `oppia/oppia-web-developer-docs` repository.

7. Wait for the welfare team to review your PR.

8. Once the welfare team leaves comments, respond to them and make changes as needed. Like on oppia/oppia, please do not resolve review threads--let the reviewer do that. Repeat as needed until reviewers approve. Note that we don't have code owners in the source repository. Instead, the welfare team will ask other developers to review PRs as needed. For example, we'll usually ask team leads to review substantive changes to wiki pages on their team's work.

9. Once reviewers have approved, the welfare team will merge your PR, and your changes will be automatically deployed to the Oppia wiki. Congratulations!

### Run pylint on python files in the [Oppia-docs-repo](https://github.com/oppia/oppia-web-developer-docs).
steps:

  1.  Install Pylint

      If pip refers to python3, then run:
      > pip install pylint
      
      else run:
      > pip3 install pylint

  2. Run pylint on all python files in the repository:

      > pylint **/*.py

### When you make changes through the web interface

If you change the wiki through the web interface at https://github.com/oppia/oppia/wiki, the synchronizer bot will automatically revert your change with a commit like [this example](https://github.com/oppia/oppia-web-developer-docs/commit/7b9efd2542e4858b8ef9ccf0d02f9ecc59796860). Please open a PR to the source repository instead.

## Implementation details

### GitHub App for synchronizer bot

The code for the synchronizer bot is split across GitHub Actions workflows in the oppia/oppia-web-developer-docs and oppia/oppia repositories. These workflows are part of the same synchronizer bot (which is a GitHub App) because they both authenticate to GitHub using the bot's private key.

We use a GitHub App because it lets us restrict the bot's access to only the relevant repositories. It also means that the bot's actions will appear as being by the bot instead of by a user, which is more accurate.

Here are instructions for creating and using the GitHub App:

* Create a GitHub App with the following settings ([docs](https://docs.github.com/en/developers/apps/building-github-apps/creating-a-github-app)):

  * `Name` and `Description` that describe the app's purpose.
  * For `Homepage URL` you can just put the link to your documentation source repository. This URL is required by GitHub, but we don't use it for anything.
  * Leave `Callback URL`, `Setup URL`, `Webhook URL`, and `Webhook secret` blank.
  * We don't use user authorization tokens, so you can leave `Expire user authorization tokens` checked and leave `Request user authorization (OAuth) during installation` and `Enable Device Flow` unchecked.
  * We don't use webhooks, so leave the `Active` checkbox under `Webhook` unchecked.
  * Give `Read & write` access to the `Contents` permission.
  * Don't subscribe to any events.
  * Allow installation `Only on this account` since we don't expect this app to be used outside of the organization.

* Download the app's private key.

  * **WARNING**: Treat this private key like a password! Anyone in possession of it can access and change the contents of the repositories the app has been installed on.

* Install the app on the repository with the wiki source and on the repository whose wiki will contain the deployed documentation.
* To both repositories, add the following secrets:

  * `OPPIA_WIKI_SYNCHRONIZER_APP_ID`: The ID for your GitHub App
  * `OPPIA_WIKI_SYNCHRONIZER_APP_PRIVATE_KEY`: A private key for your GitHub App in PEM format.

* Delete the private key from your machine. If you need to add the key to a new repository secret in the future, you can just generate a new key.

### Workflow to revert changes through the web interface

Here are a few points about the [`revert-web-wiki-updates.yml`](https://github.com/oppia/oppia/blob/develop/.github/workflows/revert-web-wiki-updates.yml) workflow:

* The workflow uses the `oppia/get-github-app-token` action to retrieve an authentication token using the synchronizer bot's private key. We specify the version of the action using a git hash as an extra security precaution since the `oppia/get-github-app-token` repository won't be as closely watched as `oppia/oppi`. This means that even if `oppia/get-github-app-token` is compromised, any malicious code added there won't be pulled into `oppia/oppia`.
* We configure the git name as `oppia-wiki-synchronizer[bot]` and email as `102317631+oppia-wiki-synchronizer[bot]@users.noreply.github.com`. This choice of name and email causes GitHub to show the app as the commit author, though this feature is not documented by GitHub.
* When we push to the deployment repository, we run `git push source master:develop`. The `master:develop` says to push the local `master` branch to the remote `develop` branch. We have different branch names because at Oppia we generally use `develop` as our main development branch, but GitHub requires that the wiki deployment repository main branch be called `master` (this detail is also not documented).

### Security analysis

This approach introduces the following security concerns:

* The permissions for the documentation source repository must be maintained as they no longer automatically follow the deployment repository permissions.
* Access to the GitHub App must be secured. In particular, the app should be created at the organization level, and the minimum number of people should be granted [app manager permissions](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#github-app-managers). Organization owners automatically have access.
* The GitHub App's credentials must also be secured. In particular, there should be no copies of the private key outside of GitHub actions secrets.

Here are some alternative approaches:

* Creating a new user account that we can give access to the necessary repositories and who the scripts will act as.

  * This means we have to keep track of securing another account and that account's credentials. The GitHub App approach is better because we can use existing GitHub accounts to manage the app, and it's not possible to log in as the app.
  * The app's actions are clearly marked as being by a bot, which is better than a user account which will look like a human user.

* Using a personal access token (PAT).

  * The PAT generated by a user gives broad access across all the repositories where the user has privileges. This introduces a risk that a compromise of Oppia could grant an attacker access to other, unaffiliated repositories. A GitHub App has more fine-grained permissions that can be restricted to particular repositories.

* Using the `GITHUB_TOKEN` generated automatically for actions workflows.

  * This token does not grant access to the wiki, so even if we force-deployed from the source repository instead of creating a revert commit, the workflow in the deployment repository that detects an edit through the web interface would not have permission to force-deploy the source documentation to the deployment wiki.

### Failed to push changes to wiki upon PR merge.

If the deployment of changes to the wiki following the merging of a pull request was unsuccessful, you have the option to manually push the changes to the wiki by following these steps:

1. Navigate to the Oppia wiki repository's Actions tab.
2. Select the "Deploy to wiki" workflow.
3. Refer to these [instructions](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow?tool=webui#running-a-workflow) to manually execute the workflow.
