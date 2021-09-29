_These instructions are for developers who'd like to contribute code to improve the Oppia platform. If you'd prefer to help out with other things, please see our [[general contribution guidelines|Home]]._

Thanks for your interest in improving the Oppia platform! This page explains how you can get involved.

If you run into any problems along the way, we're here to help! Check out our [[wiki page on getting help|Get-help]] for the communication channels you can use. If you find any bugs, you can also file an issue on our [issue tracker](https://github.com/oppia/oppia/issues). There are also lots of helpful resources in the sidebar, check that out too! Also, if you'd like to get familiar with Oppia from a user's point of view, you can take a look at the [user documentation](http://oppia.github.io/).

**Important! Please read this page in its entirety before making any code changes.** It contains lots of really important information. You should also read through our [[guide to making pull requests|Make-a-pull-request]]

## Table of Contents

* [Setting things up](#setting-things-up)
* [Developing your skills](#developing-your-skills)
* [Finding something to do](#finding-something-to-do)
  * [Starter projects for new contributors](#starter-projects-for-new-contributors)
    * [Backend](#backend)
    * [Frontend](#frontend)
  * [Contributor Roles](#contributor-roles)
  * [Tasks for Existing Contributors](#tasks-for-existing-contributors)
* [Tips for Success](#tips-for-success)
* [Notes](#notes)

## Setting things up

1. Please sign the CLA so that we can accept your contributions. If you're contributing as an individual, use the [individual CLA](https://goo.gl/forms/AttNH80OV0). If your company owns the copyright to your contributions, a company representative should sign the [corporate CLA](https://goo.gl/forms/xDq9gK3Zcv).  **If you do not sign the CLA, any PRs you open will be closed.**

2. Fill in the [Oppia contributor survey](https://goo.gl/forms/otv30JV3Ihv0dT3C3) to let us know what your interests are. (You can always change your responses later.) Filling out the survey will also get you assigned to a mentor at Oppia who will reach out to you over email to help you get started.

3. Install Oppia following the [[installation instructions|Installing-Oppia]].  If you run into any issues, please check out the [[troubleshooting instructions|Troubleshooting]].

<!--
TODO(#4): Add link to IDE tutorial.
-->

4. Update your GitHub settings:

   * [Set up 2FA]( https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/) on your GitHub account. **This is important to prevent people from impersonating you.**

     When using 2FA, you might need to create a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) so that you can log in from the command line. Alternatively, you can [log in using SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).

   * Set your GitHub notification preferences [here](https://github.com/oppia/oppia/subscription). The important thing is to make sure you notice when someone replies to a conversation you're part of -- many people choose "Not watching" so that they do not get overwhelmed. Selecting "Watching" will notify you about everything that happens on the Oppia repository (which is a lot!), and notifications specifically addressed to you might end up getting lost in the noise.

   * (Optional) Consider setting up [automatic auth](https://help.github.com/articles/caching-your-github-password-in-git/) so you don't have to type in a username and password each time you push a change. Note that this isn't an issue if you use SSH.

5. On your browser, consider bookmarking both this wiki page (for easy reference later) and the [Gitter tab](https://gitter.im/oppia/oppia-chat) (so that you can keep abreast of new activity).

6. Familiarize yourself with the resources linked to from the sidebar of this page, especially the [[overview of the codebase|Overview-of-the-Oppia-codebase]] the [[coding style guide|Coding-style-guide]], and the [[Frequently Asked Questions|Frequently-Asked-Questions]]. You don't have to read all the other stuff right now, but it's a good idea to be aware of what's available, so that you can refer to it later if needed.

7. Say hi on the [gitter](https://gitter.im/oppia/oppia-chat) chat channel!

8. Join [our discord](https://discord.com/invite/dCJwEAgk3D) for fun activities!

9. Take up your first starter project! You can find more details below. (Make sure to read and follow the [[PR instructions|Make-a-pull-request]] closely so that your PR review proceeds smoothly.)


## Developing your skills

See our [[page of learning resources|Learning-Resources]] for suggestions on how you can improve your development skills. When you take up an issue that requires programming languages or tools you are unfamiliar with, check out that page for resources that other developers have found useful when learning.

## Finding something to do

### Starter projects for new contributors

Welcome! Please make sure to follow the instructions above if you haven't already. After that, we'd **strongly recommend** tackling some part of one of the following starter issues:

#### Backend

* [#11496](https://github.com/oppia/oppia/issues/11496) (Write lint checks for the end-to-end tests)

* [#13162](https://github.com/oppia/oppia/issues/13162) (Write schemas for handler class arguments)

#### Frontend

* [#10700](https://github.com/oppia/oppia/issues/10700) (Refactor all migrated object factories to model.ts files in angular)

* [#9749](https://github.com/oppia/oppia/issues/9749) (Migrate directives/controllers to Angular components)

* [#13764](https://github.com/oppia/oppia/issues/13764) (Maintaining Oppia's core data with frontend validation checks)

* [#10798](https://github.com/oppia/oppia/issues/10798) (Fixing end-to-end tests, which are written with protractor)

* [#8668](https://github.com/oppia/oppia/issues/8668) (frontend; documenting the services)

* [#8015](https://github.com/oppia/oppia/issues/8015) (Refactoring frontend - Services should return domain objects instead of dicts)

* [#8016](https://github.com/oppia/oppia/issues/8016) (Refactoring frontend - The backend api calls in the frontend should only happen through services)

* [#8038](https://github.com/oppia/oppia/issues/8038) (Refactoring frontend services - The backend api calls in the frontend should only happen through services)

* [#10474](https://github.com/oppia/oppia/issues/10474) (Make typescript checks strict)

* [#10616](https://github.com/oppia/oppia/issues/10616) (Introduce new @typescript-eslint rules n the codebase)

These issues are hand-picked to ensure that you don't run into unexpected roadblocks while working on them. For other issues, you may need to be more independent because often times, we don’t know how to solve them either.

If you decide to pick one of these, please go ahead and leave a comment saying which part of the issue you're taking, and submit a follow-up PR by following the instructions to [[make a PR|Make-a-pull-request]]. You don't need to wait for approval to get started!

If you need some help from someone with a more prominent UI/UX or design perspective, tag **@mschanteltc** and expect a response within 2-3 days, if not, ping in the Oppia Gitter channel.

**Important Note**: Please make sure to read and follow the [[PR instructions|Make-a-pull-request]] carefully, otherwise your PR review may be delayed or your PR may be closed.


### Contributor Roles

If you want to play a more integral role in sustaining Oppia, you can look forward to being able to take on more responsibilities as you continue to make quality contributions to the project. Here is a rough outline of the roles developers play at Oppia:

```text
        Everyone (read access)
            |
            |
            v
     New Contributors (read access)
            |
            | Get 2 PRs Merged
            v
      Collaborators (triage access)
            |
            | Make Sustained Quality Contributions
            v
         Members (write access)
            |
            |
            v
      Project Leads
           and
     Core Maintainers
```

As a new contributor, you won't have any permissions on the repository except to read the code, so you'll need to ask other developers (or Oppiabot) to assign reviewers to your PR or add labels to your issue.

After you've completed parts of at least two different non-trivial starter projects and successfully submitted PRs for them into develop, we'll mail you a collaborator invite link for the Oppia repository. This is a manual process and may take up to 48 hours. Please visit [this link](https://github.com/oppia/oppia/invitations) to accept the invitation to collaborate. We'll also get in touch to suggest suitable longer-term projects based on your interests, but please feel free to email us at admin@oppia.org if you don't receive the email!

Then you'll be a collaborator with triage access, which lets you assign reviewers and labels. No more asking for reviewers to be assigned! If you continue to make quality contributions, you may be added as a member of the Oppia organization, which grants you write access. Then you'll be able to restart tests, serve as a [code owner](https://docs.github.com/en/articles/about-code-owners), and review pull requests.

Finally, after you've been contributing to the project for a while, you may become a project lead and/or core maintainer. In those roles, you'll help plan and lead Oppia's development.

If you ever wonder why you don't have permission to perform some action on the Oppia repository, it might be because of your role. GitHub details each role's privileges in more detail in [their documentation](https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories/repository-permission-levels-for-an-organization).

### Tasks for Existing Contributors

There are lots of options!

* **Want easy projects?** Check out our [list of "good first issues"](https://github.com/oppia/oppia/labels/good%20first%20issue).

* **Want projects that matter?** Check out our [list of high-priority issues](https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3Aimportant).

* **Want to practice debugging?** Check out our [list of issues needing debugging help](https://github.com/oppia/oppia/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20label%3A%22needs%20debugging%22%20).

* **Want to practice writing a design doc?** Check out the [list of issues requiring a design doc](https://github.com/oppia/oppia/labels/needs%20design%20doc). This is useful for learning how to write good "technical implementation" proposals.

* **Want to join a team working on a larger effort?** See our [list of projects](https://github.com/oppia/oppia/projects).

* **Want to lead a project?** Let us know by emailing admin@oppia.org.  We may offer you the opportunity to do this once you've sent in several good PRs.

* **Want help figuring out what to do?** Just ask us on [Gitter](https://gitter.im/oppia/oppia-chat), or send an email to admin@oppia.org. We'll try to help!

If an issue hasn't got someone assigned to it, and there's no existing PR for the issue (you can check this by scanning the list of [existing PRs](https://github.com/oppia/oppia/pulls)), feel free to take it up by assigning yourself to it. You don't need to ask permission to do so. Also, if you need help or advice on an issue, you can contact the corresponding team lead, whose GitHub username you can find in the description of the project the issue is assigned to.  You can also find a list of all Oppia teams on the [Projects page](https://github.com/oppia/oppia/projects).

## Tips for Success

1. Make dependent (“stacked”) PRs to ensure smaller time between reviews and subsequent PRs. A large PR results in difficulty to review for the reviewer as well as difficulty in making changes according to a review for an author. So, it is better to create smaller PRs which deliver a single small goal. If you have code changes dependent on a PR, it is better to create a separate PR for those changes.

2. Try and follow test-driven development. This is the easiest way to make sure the code you wrote is working fine. The basic idea is to first write tests for the expected behaviour and then write code that will pass those tests. Refer to our guides for writing good tests:

   * [[Backend Tests|Backend-tests]]
   * [[Frontend Tests|Frontend-unit-tests-guide]]
   * [[End to end tests|End-to-End-Tests]]

3. If you're stuck on something, ask for help instead of letting it block all your work. It can be difficult to know when to ask for help, so one rule of thumb is to ask whenever you've been unable to make progress for an hour.

4. When asking questions, follow our guide to [[getting help|Get-help]] to make sure your question gets to the right people and has the information they need to help you.

5. Remember that you're working with volunteers, nearly all of whom spend most of their time at school or a job. Don't be surprised if it takes a few hours for someone to get back to you (they might be in a different time zone!).

6. Do a self-review to find your own mistakes. Reviews by other developers take time, so any mistakes you can catch by yourself will speed things up.

7. Take the time to understand what the code you are changing is doing.  Sometimes we see PRs for changes that don't do anything useful or that don't make sense given the context of the code. These won't get merged.

8. If you are making a contribution which involves changing some user interface or introducing a new feature, it is good to start with a design doc to avoid wasting efforts later. Follow our [[guide for writing design docs|Writing-design-docs]].

## Notes

* Our central development branch is `develop`, which should be clean and ready for release at any time. All changes should be done in feature branches based off of `develop`.

* Sometimes, GitHub comments in the main conversation thread don't have a reply box. This seems to be a quirk with GitHub: apparently the reply box doesn't show up on outdated threads if you're currently in the middle of a review (or a reply to someone else's review) that you haven't submitted. After you submit the review, the reply field should show up again.

* If you want to do a codebase change that is large and somewhat repetitive, do a small trial PR first for a limited subset of the change, and check with reviewers whether the approach makes sense. Only after getting that trial PR merged (or at least approved by all reviewers) should you do the full change.

  This helps because, if you just did the full PR at the outset instead, then if a reviewer requests changes to the approach, you'd need to go back and modify all the files. On the other hand, with a trial PR, addressing an initial round of changes is less work, and by the time you get to the full PR, you'd already know what you need to do!

* To find the author of a particular change in a file, run this command:

  ```console
  git blame file-name
  ```

  The output will show the latest commit SHA, author, date, and time of commit for each line.

  To confine the search of an author between particular lines in a file, you can use:

  ```console
  git blame -L 40,60 file-name
  ```

  The output will then show lines 40 to 60 of the particular file.

  For more `git blame` options, you can visit the [git blame documentation](https://git-scm.com/docs/git-blame). You can also view this information on GitHub. Just navigate to the file you are interested and click the "Blame" button:

  ![Screenshot showing the blame button on GitHub](images/githubBlame.png)

* **Important** PRs marked with the “critical” label need to be tested in the backup server before being merged. For this, one of the release coordinators (with access to deploy) should checkout a new branch from develop, merge the branch from the PR into the new branch, and initiate deployment to the backup server from this branch. The PR author should give specific testing instructions for the changes (like which job to run, what the expected output is, etc) and the coordinator should verify the same. Once successfully tested, the PR should be merged into develop. This is to prevent cases like exploration migrations which can result in data corruption (as it will auto-migrate) if the migration isn’t safe. The "critical" label needs to be applied on PRs that change data validation checks, and other possibly critical changes which could affect production data.
