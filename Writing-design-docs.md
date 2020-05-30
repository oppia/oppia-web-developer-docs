### Instructions
When writing design docs at Oppia, please consider using this [design doc template](https://docs.google.com/document/d/1eMivKj5uWkOkj4AB684JVJslAe49gSskZ-VsyUjgPN4/edit). This will ensure that all the necessary information for the project is documented in a central location, and enable project reviews to be done effectively.

More specifically, here’s how to get started:

1. Make a copy of [this document](https://docs.google.com/document/d/1eMivKj5uWkOkj4AB684JVJslAe49gSskZ-VsyUjgPN4/edit).
2. Delete the top "instructions" box.
3. Fill in all the sections with details pertaining to your feature/project (you can remove the existing text, which is just meant to help you get started). For sections that are not required for the particular project you’re working on, write a short explanation of why they’re not required, rather than deleting them altogether.
4. Make sure to proofread your design doc before asking reviewers to look at it.

## How to respond to doc reviews

When you're responding to a reviewer's comments in a doc, we recommend that you treat it like [responding to a code review](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#instructions-for-making-a-code-change). 

More specifically:
- Feel free to accept (or reject!) suggestions. If you reject a suggestion, that's fine, but say why.
- In general, treat comments similarly to how you would treat comments in a standard code review. In other words:
  - Before asking for a follow-up review, make sure to reply to each comment (maybe with "Done") and update the doc as needed, but **don't resolve the comment thread**. Let the reviewer handle that, so that they can keep track of which comments still need to be addressed. Sometimes, more follow-up might be needed when the reviewer looks at the updated version of the doc.
  - If you have any questions about the reviewer's comments, feel free to ask them for clarification.

## Tips when writing design documents

- Make sure that you understand the high-level goals of the project, then add increasingly more detail once that's established. Consider using the following strategy:
  1. Start with the overview & goals of the project
  2. Make sure that other team members are in agreement
  3. Then, go into detail on the technical & architectural approach
  4. Make sure other team members are in agreement with the architectural changes
  5. Go into specifics of how the project will be implemented
  6. Make sure other team members are in agreement with the specifics of the implementation
  7. Fill in the milestones, tasks, time estimates, and other sections
  8. Get final approval on the document before beginning implementation
- Always make sure you understand the purpose of why the design document is useful before beginning, and write the document to fulfill those goals. A design document should:
  1. Outline the technical goals of a feature or project that needs to be implemented
  2. Describe the architectural changes in the codebase that the project will include
  3. Describe how the project will be implemented (specific details of what you plan to build, but not the actual code)
  4. Provide a break-down of tasks that will be completed
  5. Provide time estimates for each task & how they will fit within defined milestones
  6. Consider other aspects of the project, including privacy, security, accessibility, and others
- Use dependency graphs, flow diagrams, and bullet lists when communicating the high-level architectural changes of the project.
- When considering additional options that go beyond the initial goals of the project, consider whether these are essential. If they aren't, add them to a "future work" section that could be worked on alongside or after the project (but not as part of the project itself). If it is essential, make sure you factor that into the implementation plan.
- When breaking down a project, think of roughly each pull request needs to be created in order to fulfill your implementation plan. Your document should include tasks for all pull requests that you know need to be implemented to complete the project.
- When estimating how long a task will take for a project, assume it will take longer than you expect. Engineers often have a tendency of assuming implementation will go perfectly, but they sometimes don't and it's difficult anticipate the things that could go wrong (e.g. bugs are found, a chosen library won't work, etc.). Suggest always multiplying your time estimates by 1.5x or 2x based on past experience (we call this a "fudge factor"). Consider also going back to old projects and comparing how much time you spent versus your estimates--this can help you figure out a good "fudge factor" to use when providing time estimates for future projects.
- When creating milestones, consider the high-level "deliverables" of a project: what can you demonstrate to someone else after a set of tasks are completed that move Oppia toward the finished result of your project? For full-stack projects, a typical set of milestones usually looks something like (note that the order of milestone is often interchangeable, but sometimes there are dependencies between tasks that force a specific order):
  i. Milestone 1: Implement the backend/logical/service portion of the feature
  ii. Milestone 2: Implement the frontend/user-facing portion of the feature
  iii. Milestone 3: Hook the two together, performing any necessary migrations in production
- When estimating a milestone, first estimate how much time each task takes and then fit as many tasks as you can within a milestone. Don't change your time estimates based on the milestone (just because something is expected to get done within a certain timeframe doesn't mean it can). If the milestones don't provide enough time to finish the project, that may indicate that the project needs to be rescoped.
- If there's something you don't fully understand when writing any part of the design document, ask more questions. Sometimes we make mistakes in how we explain things, and that can lead to projects going being taken in a direction we didn't anticipate. Other times, we see contributors make assumptions about one particular technical area (such as testing) and describe something other than what we expect. More questions can help bridge any missing knowledge, and can result in changes to our document templates or project goals.
- Use related artifacts when coming up with designs. Software should never be designed in a vacuum, especially when you're building something as part of a large team like Oppia. We have lots of past design docs that can provide more detail on the types of things we value as a team, and how to describe those things. This is true for both code and design documents: things that follow established patterns are easier to understand since they minimize the amount of context needed to comprehend it. One way to evaluate how much a particular design document or proposal minimizes context is by considering how much easier/harder it is to understand when compared with other documents describing a project of similar complexity. What makes one document easier to understand than another? This is a meta-skill that's really valuable for both document writing and for code: considering how understandable something is while writing it. This skill takes repetition to develop, and will get easier as you read and write more technical documents.