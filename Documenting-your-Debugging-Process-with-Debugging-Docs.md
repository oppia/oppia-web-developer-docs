Whenever you are debugging a problem, you may find it useful to keep a record of your debugging process. We often do this already in issues. Issues usually begin with a detailed description of the problem, which is followed by discussion, reports of attempted debugging steps, and what root cause was identified. However, issues' linear comment structure makes them more amenable to communication among team members than organizing your thoughts. Debugging docs, on the other hand, serve primarily to organize your thoughts.

## Benefits

Primarily, debugging docs help keep your thoughts organized. When you have written down the steps you've already tried and the results of your investigations, you don't have to worry about forgetting your earlier work. Further, when you document your work, you force yourself to reflect on what you've already tried. On the Automated QA team, we've found that this reflection often helps us see new debugging approaches.

Debugging docs also make it easy for you to bring someone else up to speed on your bug. For example, one time a member of the Automated QA team was debugging an end-to-end test flake. The flake was blocking nearly all PRs from being merged, but the member had to go to sleep before they could figure it out. They sent the [debugging doc](https://docs.google.com/document/d/1LAsDc1EMISjpwnn-FcdH-7TNrU20xfkJEO3uSLj_nyM/edit#heading=h.jl2gn54iqprw) to another contributor who read through the document and quickly spotted a problem. They worked with another team member to have a PR up to fix the issue before the first member woke up the next morning! The debugging doc made it easy for team members to hand the bug off and get it fixed fast.

Finally, these documents can serve as records of debugging strategies and bug causes that we can reference later on. For example, we might search these debugging docs for an error message we are encountering to see if it has been fixed before.

## How to Write a Debugging Doc

1. Debugging docs should begin with a **detailed description of what's going wrong**. This should include:

   * Context: What branch or PR is the bug happening on? If this is happening locally, what system are you running, and what code changes have you made?
   * How the Bug Manifests: This might include error logs that you pasted into the document, screenshots, or links to a test run on a PR. **If you provide a link, copy the relevant part of the page you are linking to.** This keeps the document self-contained so we can search them. It also makes the doc easier for people to read.

2. Next, **describe any investigation** you did. What did you try, and what happened when you tried it? You want to include enough detail so that someone could reproduce your investigation to see if they get the same results.

3. After some investigation, you might have some ideas for what might be going wrong. **Document your guesses and describe how you go about testing them**. Report the results of that testing and describe whether you think your guess was right. What's your reasoning?

4. **Continue** documenting the your investigations, guesses, and tests of those guesses.

5. Once you figure out what the problem was, write that down too! **Include an analysis of how the root cause you identify caused the errors you described at the top**.

Ready to get started with your own debugging doc? You can make a copy of [this template](https://docs.google.com/document/d/1qRbvKjJ0A7NPVK8g6XJNISMx_6BuepoCL7F2eIfrGqM/edit?usp=sharing) to get started. On the Automated QA team we store all our debugging documents in a [folder](https://drive.google.com/drive/folders/1wYdiP6PfhiF553FEIqNBhW2hQxWmWo_Y?usp=sharing) on Google Drive. Check with your team to see what works best for you.

To see these debugging docs in action, check out these examples:

* [2021-02-08 E2E Flake: session deleted because of page crash](https://docs.google.com/document/d/1LAsDc1EMISjpwnn-FcdH-7TNrU20xfkJEO3uSLj_nyM/edit#heading=h.jl2gn54iqprw)
* [2020-12-23 E2E Flake: Skill Editor is Taking Too Long to Appear](https://docs.google.com/document/d/1cI8fqAIFqsmZj5v35y49ohhNvgmE0_vH_sT02Aws77Y/edit?usp=sharing)