At Oppia, we use [Travis CI](https://travis-ci.com/) for running a comprehensive suite of tests for each PR. The Travis jobs are queued and then run for each PR. This process can take some time and if suppose the Travis build fails for your PR due to the changes you've made, you'll need to fix it and then wait again for the build to pass. The build might even fail again if not fixed properly in the first attempt.
Therefore, we recommend that developers set up their own Travis instance with a configuration similar to the one used at Oppia so that they can be very sure that the Travis build will pass for their PR on the first attempt. This will save both the developer's as well as the reviewer's time.
Setting up a Travis instance for your Oppia's fork hardly takes a couple of minutes. Please follow these steps:
1. [Fork](https://help.github.com/articles/fork-a-repo/) the oppia repository to your GitHub account.
2. Go to https://travis-ci.com and sign in/sign up using your GitHub account.
3. Authorize Travis CI for Open Source.
4. In the "Repositories" section, you will be able to see "oppia" listed. Activate the repository by clicking on the slider so that it turns blue:
![activate-oppia](https://user-images.githubusercontent.com/24826041/47151100-6f8b7b80-d2f6-11e8-8121-ea302909ce81.jpg)
5. Click on "Settings" and turn off "Build pushed pull requests". In general, configure them according to the image shown below:
![settings](https://user-images.githubusercontent.com/24826041/47151430-5e8f3a00-d2f7-11e8-9b26-4cafc8e0ae39.png)
6. Now its time to configure "Environment Variables". Add an environment variable with the following details:
Name: `CHROME_SOURCE_URL`
Value: `https://github.com/webnicer/chrome-downloads/raw/master/x64.deb/google-chrome-stable_77.0.3865.75-1_amd64.deb`
Display value in the build log: Yes (Click on the slider so that it turns blue).
After this, click on the "Add" button.
Post this process, this section would look something like this:
![env-vars](https://user-images.githubusercontent.com/24826041/47151941-ddd13d80-d2f8-11e8-9758-702b1c190164.png)

You've successfully set up your own Travis instance now! Any new branch you push to your fork will be built on Travis. If the newly pushed branch does not build automatically, create a PR using that branch to your own fork. This should trigger the Travis build.
