If you're running into an issue that you have trouble solving, you might find it useful to keep a record of your debugging process so that you can easily organize your thoughts and get help from other members of the team. The format we use for this is called a "debugging doc".

To get started, make a copy of [this "debugging doc" template](https://docs.google.com/document/d/1qRbvKjJ0A7NPVK8g6XJNISMx_6BuepoCL7F2eIfrGqM/edit?usp=sharing) and fill it in. If you're new to debugging, filling out as much of this template as you can is a great way to practice and improve your debugging skills. In general, we strongly recommend writing and sharing a debugging doc if you can't figure out the solution to a problem after working on it for **30 minutes**.

Once you've filled out the "Background" and "Initial investigation" parts of the template, share the debugging doc in your team's group chat or the relevant issue thread, so that others can look at it in parallel. Then, continue working on the "Hypotheses Testing" section (search the Internet, narrow down the problem window, etc.) and fill out as much of it as you can.

When it's not clear what to do further, please ask for help immediately on your team chat or [GitHub Discussions](https://github.com/oppia/oppia/discussions). Note that, at this stage, reviewers will reasonably expect, at minimum, at least one hypothesis to be proposed and under investigation.


## Benefits

Primarily, debugging docs help keep your thoughts organized. When you have written down the steps you've already tried and the results of your investigations, you don't have to worry about forgetting your earlier work. Further, when you document your work, you force yourself to reflect on what you've already tried.

Debugging docs also make it easy for you to bring someone else up to speed on your bug. For example, one time a member of the Automated QA team was debugging an end-to-end test flake. The flake was blocking nearly all PRs from being merged, but the member had to go to sleep before they could figure it out. They sent the [debugging doc](https://docs.google.com/document/d/1LAsDc1EMISjpwnn-FcdH-7TNrU20xfkJEO3uSLj_nyM/edit#heading=h.jl2gn54iqprw) to another contributor who read through the document and quickly spotted a problem. They worked with another team member to have a PR up to fix the issue before the first member woke up the next morning! The debugging doc made it easy for team members to hand the bug off and get it fixed fast.

Finally, these documents can serve as records of debugging strategies and bug causes that we can reference later on. For example, we might search these debugging docs for an error message we are encountering to see if it has been fixed before.

## Examples

To see these debugging docs in action, check out these examples:

* [2021-02-08 E2E Flake: session deleted because of page crash](https://docs.google.com/document/d/1LAsDc1EMISjpwnn-FcdH-7TNrU20xfkJEO3uSLj_nyM/edit#heading=h.jl2gn54iqprw)
* [2020-12-23 E2E Flake: Skill Editor is Taking Too Long to Appear](https://docs.google.com/document/d/1cI8fqAIFqsmZj5v35y49ohhNvgmE0_vH_sT02Aws77Y/edit?usp=sharing)
