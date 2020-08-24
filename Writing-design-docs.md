## Instructions
When writing design docs at Oppia, please use this [design doc template](https://docs.google.com/document/d/1eMivKj5uWkOkj4AB684JVJslAe49gSskZ-VsyUjgPN4/edit). This will ensure that all the necessary information for the project is documented in a central location, and enable project reviews to be done effectively.

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

## Why we write design documents
Design documents provide team members with the opportunity to review the future implementation of a project before the code has been fully written. A good design document:

1. Outlines the technical goals of a feature or project that needs to be implemented
2. Describes the architectural changes in the codebase that the project will include
3. Describes how the project will be implemented (specific details of what you plan to build, but not the actual code)
4. Provides a break-down of tasks that will be completed
5. Provides time estimates for each task & how they will fit within defined milestones
6. Considers other aspects of the project, including privacy, security, accessibility, and others

## Tips when writing design documents

- Make sure that you understand the high-level goals of the project, then add increasingly more detail once that's established. Consider using the following strategy:
  1. Start with the overview & goals of the project
  2. Make sure that other team members are in agreement
  1. Fill in the product design section of the document (mocks are really helpful)
  1. Make sure that other team members are in agreement with the product design
  3. Then, go into detail on the technical & architectural approach
  4. Make sure other team members are in agreement with the architectural changes
  5. Go into specifics of how the project will be implemented
  6. Make sure other team members are in agreement with the specifics of the implementation
  7. Fill in the milestones, PRs, time estimates, and other sections
  8. Make sure other team members are in final agreement with the approach before beginning implementation
- Use dependency graphs, flow diagrams, and bullet lists when communicating the high-level architectural changes of the project.
- When considering additional options that go beyond the initial goals of the project, consider whether these are essential. If they aren't, add them to a "future work" section that could be worked on alongside or after the project (but not as part of the project itself). If it is essential, make sure you factor that into the implementation plan.
- When breaking down a project, determine all of the tasks that need to be completed for the project. A task is either performing a migration, adding/updating documentation, or creating a PR (each PR should correspond to a single task).
- When estimating how long a task will take for a project, assume it will take longer than you expect. Engineers often have a tendency of assuming implementation will go perfectly, but they sometimes don't and it's difficult to anticipate the things that could go wrong (e.g. bugs are found, a chosen library won't work, etc.). Suggest always multiplying your time estimates by 1.5x or 2x based on past experience (we call this a "fudge factor"). Consider also going back to old projects and comparing how much time you spent versus your estimates--this can help you figure out a good "fudge factor" to use when providing time estimates for future projects.
- If you're unsure how to approach the implementation, start by writing a basic hacked-together prototype to help solve specific questions of the implementation that you're unsure of. Look at other similar features for how they're laid out to compare. You should avoid implementing too much of the project in advance: the main purpose of a design document is to get feedback for a project before spending the large amount of time implementing it. For that reason, the document should take much less time than the project to create.
- If you're unsure about specific parts of the project: call these out as open questions so that other team members can weigh in and provide suggestions or resources that can help you resolve the open questions.
- If there's something you don't fully understand when writing any part of the design document, ask more questions. Sometimes we make mistakes in how we explain things, and that can lead to projects being taken in a direction we didn't anticipate. Other times, we see contributors make assumptions about one particular technical area (such as testing) and describe something other than what we expect. More questions can help bridge any missing knowledge, and can result in changes to our document templates or project goals.
- Use related artifacts when coming up with designs. We have lots of past design docs that can provide more detail on the types of things we value as a team, and how to describe those things. Things that follow established patterns are easier to understand since they minimize the amount of context needed to comprehend it. One way to evaluate how much a particular design document or proposal minimizes context is by considering how much easier/harder it is to understand when compared with other documents describing a project of similar complexity.

### Additional tips for large projects

The following tips correspond to projects that span 3+ months:
- Use milestones to organize tasks & specify expected completion times to communicate expectations with the team
- When creating milestones, consider the high-level "deliverables" of a project: what can you demonstrate to someone else after a set of tasks are completed that move Oppia toward the finished result of your project? For full-stack projects, an example set of milestones may look something like (note that the order of milestone is often interchangeable, but sometimes there are dependencies between tasks that force a specific order):
  i. Milestone 1: Implement the backend/logical/service portion of the feature
  ii. Milestone 2: Implement the frontend/user-facing portion of the feature
  iii. Milestone 3: Performing any necessary migrations in production
- When estimating a milestone, first estimate how much time each task takes and then fit as many tasks as you can within a milestone. Don't change your time estimates based on the milestone (just because something is expected to get done within a certain timeframe doesn't mean it can). If the milestones don't provide enough time to finish the project, that may indicate that the project needs to be rescoped.
- If the project has multiple developers, ensure tasks and milestones have clear owners assigned to them

## Generating Sequence Diagrams using Text

Sequence diagrams can be used to convey the structure of a system more clearly. It helps represent the main interactions between different layers such as controllers / domain / storage.

In order to create a sequence diagram, you can use this [tool](https://bramp.github.io/js-sequence-diagrams/). The tool takes a text source as input to generate an SVG file with the sequence diagram. You will use a text editor to type out the source text following the steps below. Once source text is complete, we will copy-paste it in one of the 'Demo' boxes in the webpage, select 'Simple' as the theme, and then download the generated SVG file.

### Tutorial to write source text
For the sake of this tutorial, assume that you have to generate a sequence diagram for `get_topic_page()` (defined below).


`controller.py`
```
def get_topic_page(self):
    topic = service.get_all_topics()
    return topic
```

`service.py`
```
def get_all_topics():
    topics = []
    for i in range(MAX_TOPICS):
        topics.append(fetcher.get_topic(i))
    return topics
```

`fetcher.py`
```
def get_topic(topic_id):
    return topic_models.get(topic_id)
```

The entry point of the sequence diagram will be `controller.get_topic_page()`. Starting from that method, whenever a new file is referred to, add it as a 'participant' in the top of the source text.
Remember to also add the file containing the entry method as a participant.
In the example, `get_topic_page()` refers to service to execute the method `service.get_all_topics()`. So 'service' needs to be added as a participant. The source file will look like this:

`text_source.txt`
```
participant controller
participant service
```

When a call is made to a method in a different file, use this syntax: ```current_file->new_file: method_being_called()```. In other words, this represents `new_file.method_being_called()` is executed in current_file.
In the example, ```service.get_all_topics()``` is called in get_topic_page(). The corresponding representation in the source text will be as follows:

`text_source.txt`
```
participant controller
participant service

controller -> service: get_all_topics()
```

This also represents that the control flow goes to `service.get_all_topics()`. In `service.get_all_topics()`, ```fetcher.get_topic()``` is called inside a loop.
In order to represent a loop, add 2 notes to the left of the calling method where the first indicates the beginning and the second inidates the end of the loop.
The statements between the two notes should represent the calls made inside the loop. The source text for this will look as follows:

```
Note left of service: LOOP BEGIN:\nLoop MAX_TOPICS times
// Logic inside the loop.
Note left of service: LOOP END
```

```fetcher.get_topic()``` does a fetch from the datastore. This can be represented in the source text like this:
```Note over fetcher: Get Topic from datastore```

When a method execution is completed, use this syntax to show control returning to the calling method and the data returned: ```current_file --> new_file: XYZ model```
In the example, ```get_topic()``` returns the Topic model to the calling method. This can be represented in the source text like this:
```
fetcher --> service: Topic model
```

After combining these statements, the source text should look like this:

`text_source.txt`
```
participant controller
participant service
participant fetcher

controller -> service: get_all_topics()
Note left of service: LOOP BEGIN:\nLoop MAX_TOPICS times
service -> fetcher: get_topic()
Note over fetcher: Get Topic from datastore
fetcher --> service: Topic model
Note left of service: LOOP END
service -> controller: Topic list
```
You can generate an SVG sequence diagram by copying this source text into one of the 'Demo' boxes at https://bramp.github.io/js-sequence-diagrams/.

Select 'Simple' as the theme and download the SVG file. The downloaded SVG file will contain the sequence diagram.

The generated sequence diagram will look like this:

<img src="https://user-images.githubusercontent.com/11008603/91026669-b34d1b80-e618-11ea-9df8-e234f3f6d0fe.png" width="600px"/>


See more examples [here](https://gist.github.com/kevintab95/3b2375f71f04476b507b22e7ad8d123f).

Reference for syntax:
https://bramp.github.io/js-sequence-diagrams/
