At Oppia, we use CircleCI for running the lint, frontend and backend testes (as of now) for each PR. The CircleCI jobs are queued and then run for each PR. This process can take some time and if suppose the build fails for your PR due to the changes you've made, you'll need to fix it and then wait again for build to pass. The build might even fail again if not fixed properly in the first attempt.
Therefore, we recommend that developers setup their own CircleCI instance with a configuration similar to the one used at Oppia so that they can be very sure that the CircleCI build will pass for their PR on the first attempt. This will save both the developer's as well as the reviewer's time.
Setting up a CircleCI instance for your Oppia's fork hardly takes a couple of minutes. Please follow these steps:
1. [Fork](https://help.github.com/articles/fork-a-repo/) the oppia repository to your GitHub account.
2. Visit the [CircleCI](https://circleci.com/signup) signup page and click “Start with GitHub”. You will need to give CircleCI access to your GitHub account to run your builds. If you already have a CircleCI account then you can navigate to your [dashboard](https://circleci.com/dashboard).
3. Next, you will be given the option of following any projects you have access to that are already building on CircleCI (this would typically apply to developers connected to a company or organization’s GitHub account). On the next screen, you’ll be able to add the repo you just created as a new project on CircleCI.
4. To add your new repo, ensure that your GitHub account is selected in the dropdown in the upper-left, find the repository you just created below, and click the Setup project button next to it.

![Setup-Project](https://circleci.com/docs/assets/img/docs/CircleCI-add-new-project-list.png)

5. On the next screen, you’re given some options for configuring your project on CircleCI. You can leave everything as-is since you already have a configuration file in your fork of oppia. Click the Start building button a bit down the page on the right. 

![Start-Building](https://circleci.com/docs/assets/img/docs/CircleCI-2.0-start-building.png)



You've successfully setup CircleCI for your fork of oppia. Enjoy testing your PRs beforehand!


***
## Troubleshooting in case of stalled Codecov coverage checks

In case the Codecov coverage checks on your PR appear to be stalled (something like this except that **there is a yellow dot before `codecov/patch` and `codecov/project` and not a green tick**)


![pr-checks](https://user-images.githubusercontent.com/24826041/59090041-42451980-8929-11e9-8fde-1e84c3fac6ea.png)


and you have set up your own instance of CircleCI, then please go ahead and unfollow `your-github-name/oppia` project on CircleCI by visiting this link:  

`https://circleci.com/gh/organizations/your-github-username/settings#projects`  
(please remember to fill in your GitHub username in place of `your-github-username` here). 
 
Once you've done that, please re-trigger the build by making any commit or bringing your PR branch up-to-date with develop.

If you face any further problems, please feel free to ping @oppia/dev-workflow-team.