# Guide for release testing

In Oppia, we do monthly releases. In a particular release, all commits since the previous release will go into production. We do a round of manual testing to verify that all core functionality remains intact. 

## How do we do testing in Oppia?

Typically, we have 3 safeguards. While a contributor makes a PR, we expect that the contributor has thoroughly tested the changes made in the PR for functional correctness. The reviewer is expected to validate this (either through screenshots or by manually testing). This testing is important and mostly it doesn’t affect the release process.
The vast majority of bugs caught during release testing can be traced back to how one particular change affected another change elsewhere in the codebase. To mitigate this, we have automated tests (backend, frontend, and e2e tests). The automated tests are necessary and good, but they are currently not complete. The ultimate goal is to have the complete codebase covered by automated tests and the release testing should be a very minimal effort. As we can’t completely rely on just the automated tests, we do a round of manual testing of what we call “Critical user journeys”. These are core pathways that cannot under any circumstance be broken. 
We have compiled a list of critical user journeys and we have listed out steps for each of them. The steps give you something to do, and something you would expect to happen. As an example here is a user journey that tests feedback given by students while playing an exploration.

<table>
<tr><th>After taking this action...</th><th>Check the following:</th></tr>
<tr><td>Add feedback for the exploration (both as anonymous and not)</td><td>No console errors are seen</td></tr>
<tr><td>Log in as the first user, go to the editor page of exploration.</td><td>The feedback icon on the navbar should show that 2 open feedback is there.</td></tr>
<tr><td>Go to improvements tab</td><td>Make sure the feedback are visible as new cards. The anonymous one should explicitly say it’s anonymous, and the other should show the username.</td></tr>
</table>

These serve as the general skeleton for the test to be performed. A good “testing mentality” is what we look for in testers.

## A good “testing mentality”
This is the most important note from the last section, and hence it should deserve its own section. Basically, to develop a good testing mentality, you should have the mindset that you should break a given functionality. Try to find loopholes, craft intelligent inputs, devise corner cases which might break the functionality. For example, in the view where you can suggest changes to the exploration state, you can try to create a suggestion with no changes, remove a string and add it back so that it is the same, try with and without a suggestion message, etc. In each of these cases, you would expect certain behaviour and if the functionality differs, then it is a problem!
A large portion of the bugs we fix are visual bugs, like missing padding, alignment is off, animations not working, etc. These are important to make sure that the page looks visually pleasing to the user. We had a bug once where the exploration player’s transition from one state to another was buggy ([#4902](https://github.com/oppia/oppia/issues/4902)). This wasn’t noticed during testing and was later caught and fixed outside of the testing team. Developing the skill to find such anomalies is key to becoming a good tester.
Another group of issues occur on specific browsers or environments. There are issues that occur only on mobile, and others which happen only on safari and so on. So as part of the procedure, while testing we expect testers to test across multiple browsers. Learner facing features need to look and feel good on mobile and tablet environments as well. The learner facing views include the library, learner dashboard and the players. For examples of browser-specific issues, automatic text to speech translations wouldn’t work on safari. After one particular chrome update, it wouldn’t work on chrome mobile alone (worked perfectly fine on desktop). Debugging these are tricky and very interesting. Sometimes, the best possible solution would be hacky in a way.

## Tips to keep in mind while testing
A list of general tips to keep in mind while testing is mentioned below!
- If anything doesn’t look right, it is probably a bug. Try to clearly describe what doesn’t look as expected to a third person and confirm with them that it is indeed something that isn’t expected.
- File issues on GitHub for any problems you see. This way you will be able to communicate to a larger section of people that you feel something is wrong, and also will be able to get their feedback on the issue. Even if you are unsure whether the issue you have encountered is even a valid bug or not, please open up an issue on Github. It’s better to find bugs as early as possible.
- We generally recommend testing across various browsers and various screen sizes. We also strongly recommend testing on a mobile/tablet if you have access to one. This will help us catch and reduce bugs across a variety of operating systems, and browser configurations. (Note: we don’t support IE, but we do support Edge). Also note, currently pages facing learners on Oppia are expected to work on mobiles/tabs. Creator views are designed for desktop only.
- Always keep the console open. Any error logged on the console is an issue. It would be better if you know the sequence of actions that led to the console error as this will speed up the debugging process.
Take screenshots/screen-recording of a bug when you see it. Providing a screenshot makes it easier for others to judge if what you see is indeed a bug.
- We give a general skeleton of what should be tested. This should be the bare minimum testing that we expect you to do. We also encourage you to digress from this “happy” path and see what outcomes you reach. Thinking-out-of-the-box can help catch many non-trivial bugs.
- Always remember that the testing should be from a users’ perspective, not a developers’ perspective. As a developer who knows the codebase quite well, certain UIs might be well understood by you. But a new user who lands on that page might need some hand-holding. File such problems also as issues!
- Another thing that we would recommend is to try learner facing views on low-speed internet (can be simulated using chrome dev tools). A large fraction of our students come from places with slower internet connections!
- If possible, try to guess or find out what’s causing the issue and try to debug a little of how that issue can be fixed and provide the information you have found while opening up the issue so that the person working on the issue has something to start with. And it’d be great if you can take up that issue yourself if you have found a working solution while debugging.
