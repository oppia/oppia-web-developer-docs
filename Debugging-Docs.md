At Oppia, we use debugging docs to compile all the investigation that has been done on an issue that we're facing, so that others can understand the background of the issue and what has been tried before.

If you plan to ask for help from the community, creating a debugging doc is **necessary**. This provides a record of your debugging process so that you can organize your thoughts, and also helps avoid long back-and-forths to determine what the issue actually is.

To get started, make a copy of [this "debugging doc" template](https://docs.google.com/document/d/1qRbvKjJ0A7NPVK8g6XJNISMx_6BuepoCL7F2eIfrGqM/edit) and fill it in, then post it to the ['Debugging Docs' category on GitHub Discussions](https://github.com/oppia/oppia/discussions/categories/q-a-debugging-docs). If you're new to debugging, filling out as much of this template as you can is a great way to practice and improve your debugging skills.

In general, we strongly recommend writing and sharing a debugging doc if you can't figure out the solution to a problem after working on it for **30 minutes**. Note that, at this stage, reviewers will reasonably expect, at minimum, at least one hypothesis to be proposed and under investigation.


## Benefits

Primarily, debugging docs help keep your thoughts organized. When you have written down the steps you've already tried and the results of your investigations, you don't have to worry about forgetting your earlier work. Further, when you document your work, you force yourself to reflect on what you've already tried.

Debugging docs also make it easy for you to bring someone else up to speed on your bug. For example, once, a member of the dev workflow team was debugging an end-to-end test flake which was blocking nearly all PRs from being merged, but they had to go to sleep before they could figure it out. They sent the debugging doc to another contributor who read through the document, quickly spotted a problem, and worked with another team member to create a PR up to fix the issue before the first member woke up the next morning! The debugging doc made it easy for team members to hand the bug off and get it fixed fast.

Finally, these documents can serve as records of debugging strategies and bug causes that we can reference later on. For example, we might search these debugging docs for an error message we are encountering to see if it has been fixed before.
