At Oppia we don’t care how silly your question is! Just ensure your question isn’t incomplete, and provide us enough info to help us resolve it faster. We've divided the questions into 2 categories - Setup related and General questions. You can start following the sections below to understand how you can ask each of them.

## Setup related questions

**Helpful advice**: You can choose any OS you’re comfortable with. However, most contributors use Linux or MacOS ([Source](https://github.com/oppia/oppia/wiki/Issues-with-installation%3F#overview)).

### Before you ask a question

1. You can setup/install Oppia by visiting [this](https://github.com/oppia/oppia/wiki/Installing-Oppia) page. Make sure you follow **all** the mentioned instructions from the beginning in a step by step manner.
2. Make sure each step succeeds (verify it with the expected behavior if mentioned in wiki).
3. In case of any unexpected behavior/errors at any step, make sure you check out our wiki on [how to troubleshoot when you are facing installation errors](https://github.com/oppia/oppia/wiki/Issues-with-installation%3F#when-you-encounter-an-installation-error).

If you are still not able to fix your error, start following the section below to raise your question on [Gitter](https://gitter.im/oppia/oppia-chat#).

### How to ask a setup question?
**Note**: If you are stuck at Step X, we will assume all previous steps till X-1 were successful for you. In case there were any previously failed steps, kindly mention those too with their error logs.

Please follow the template given below (mark x inside checkboxes to tick them):

``````
**Checklist**
- [ ]  I have followed through “Before you ask a question” section

**System Information**
- OS: (Be specific Ex: Ubuntu 20.04)
- [ ] Virtual machine

**Error log**

//paste error log here

or

paste a screenshot

**Approaches already used to resolve the issue**

(eg: Link to a stackoverflow answer or any solution that you have tried)
- enter any additional description
``````

## General questions

### Before you ask a question
1. We expect that you have already **set up Oppia on your machine**, and it is successfully running. (If not, kindly do that first!)
2. Prepare a debugging doc following [the guidelines provided on the wiki page](https://github.com/oppia/oppia/wiki/Debugging-Docs).
2. If there are **failing e2e tests** on your PR, and you haven’t done any changes in that direction, kindly understand that sometimes they just fail due to flakiness. You should request for a re-run of those only when it’s preventing your PR from getting merged.

### How to ask a general question?
Follow the template below for asking questions (fill in the values inside <> brackets and mark x inside checkboxes to tick them):
``````
@{{PR reviewer or Mentor username}} PTAL!

**Checklist**
- [ ] I have filled the [CLA](https://goo.gl/forms/AttNH80OV0) and the [Oppia Contributor Survey](https://goo.gl/forms/otv30JV3Ihv0dT3C3)
- [ ] Setup Oppia locally (verified by running `python -m scripts.start`)
- [ ] I have followed through "Before you ask a question" section

**System Information**
- OS: (Be specific Ex: Ubuntu 20.04)
- [ ] Virtual machine

**About the issue**
- #{{Issue_No}}
- #{{PR_No}}
- {{Describe the issue}} (eg. Failing e2e tests: "The test has been failing repeatedly since {{x}} previous runs, and I haven’t done any changes related to it. Requesting for a re-run.")

**Approaches already used to resolve the issue**

(eg: Link to a stackoverflow answer or any solution that you have tried)
- #{{Link to the debugging doc}}
- enter any additional description
``````

### Important points
- If you are unable to push changes due to some reason, you can create a [patch file](https://docs.gitlab.com/omnibus/development/creating-patches.html) and share it with your Point of Contact.
- If you are facing issues in completing the assigned task, you can create a PR on the forked version of the Oppia repository, get it resolved by contacting your mentor, and then create a new PR on the original Oppia repository.
- If you have not made a PR yet, because you are not sure:
  - what the issue is about, or 
  - which files have to be modified, or
  - if your approach towards the solution is correct
  Then ask for help by commenting with your doubt/suggested approach on the issue page itself.  If you don’t get any response within **24 hours**, you can drop a message on [gitter](https://gitter.im/oppia/oppia-chat#) chat too.
- If you want to have a discussion on your approach, but aren’t ready to make a PR yet, you can create a [public gist](https://gist.github.com/) and include the link to it in your question. It’s always better to see the code you are talking about!
- **Avoid** asking for help from people via emails or direct messaging. We encourage everyone to ask for help on a common channel so that whoever sees your query first can help you or guide you how to take your query forward.
  - Comment on issue page or the PR if it’s very specific,
  - Use [gitter chat](https://gitter.im/oppia/oppia-chat#) if it is a non-issue specific doubt.