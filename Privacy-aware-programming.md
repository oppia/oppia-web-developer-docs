_This wiki page is not a legal document and does not give binding legal advice in any way. This wiki page does not create any representation or warranty by Oppia with respect to its data practices. If you have any questions or suggestions for this wiki page, please contact [vojtech.jelinek@hey.com](mailto:vojtech.jelinek@hey.com). For any official privacy-related inquiries, please contact [admin@oppia.org](mailto:admin@oppia.org)._

This wiki page contains a basic explanation of privacy-aware programming, a section about privacy practices to follow in the design stage and a third section about privacy practices to follow in the implementation stage. A lot of the content of this page is based on [Privacy Design Strategies](https://www.cs.ru.nl/J.H.Hoepman/publications/pds-booklet.pdf) by Jaap-Henk Hoepman.


# Basics

Privacy-aware programming is an approach to coding that always makes sure that any user data is properly protected via various techniques and methods. Proper privacy measures are required by law (most notably GDPR in European Union). Since, at Oppia, we work with user data (especially, in some cases, the data of underage users), we want to protect such data properly so that it cannot be misused in any way.


### User data

User data refers to any data produced by the user that we collect, such as their username, email, IP address, or profile picture. Some of this data can be **sensitive** — this is usually defined as data about the users racial or ethnic origin, political opinions, religious beliefs, or data related to physical or mental health. Currently, we do not collect any sensitive data at Oppia, if you have even a slight suspicion that the data you plan to collect is sensitive ask the data owners for a confirmation. The data owners are Sean Lip ([sean@seanlip.org](mailto:sean@seanlip.org)) and Ben Henning ([ben@oppia.org](mailto:ben@oppia.org)).


# Design stage

This part focuses both on writing and reviewing design docs that contain changes to or additions of new user data.

In the design stage of a feature or refactor, all newly-introduced handling of user data or changes to existing handling of user data should be mentioned and considered. There is a specific section to discuss privacy aspects in the [Oppia design doc template](https://docs.google.com/document/d/1eMivKj5uWkOkj4AB684JVJslAe49gSskZ-VsyUjgPN4/edit).

For each piece of newly introduced user data or change in handling of existing user data, the privacy section should mention which exact data is collected and then explain how all the **data-oriented privacy strategies** are met for that piece of user data.


## Data oriented strategies in design stage


### Minimize

The best way to minimize the amount of collected data is to not collect user data at all. If you need to collect some data, make sure that:



*   You only collect the minimal subset of data from each user that is required for the feature that we want to implement
*   You only collect data for the users for whom the data is actually needed.
*   The data is destroyed when it is no longer needed.

Do not store any **sensitive** data (see above for the explanation of **sensitive** data).

An example of a good practice in Oppia codebase: 



*   We have a process that periodically deletes models that were marked as deleted and also some models that contain user queries. 
*   Users can register with only a small number of information and the other data are provided on a completely voluntary basis.


### Separate

Separate the handling of user data into unique services. Some user data might make sense to add to existing models, but if we collect a bigger subset of data that was not collected before, it might make sense to separate those into its own models. In general, if the code can be easily separated into its own models or parts of the codebase, then the data should also be separated. This doesn’t mean that all the parts of the code need to be separated, for example the rules for the Wipeout and Takeout are placed in our model modules, but the code that performs the operation is then separated. (Also, if the data is **sensitive**, it needs to be stored in a separate model that can be easily deleted in its entirety — but see the point above on not storing any sensitive data in the first place).

An example of a good practice in Oppia codebase: 



*   Most of the code that handles Wipeout and Takeout migration is separated into its own services. 
*   All admin features are separated into its own page.
*   We separate permissions for the contributor dashboard in a separate model and only create this model for users that actually have some permissions.


### Abstract

Make sure that, where possible, the less granular versions of user data are collected (e.g. collecting only a birth year instead of the whole birthdate). Also, instead of collecting data specific for one user, aggregate the data for a whole group of people. One possible approach is to collect specific data only for a particular retention period, then aggregate and rely on aggregations indefinitely. Where possible, use a more approximate value instead of the exact value for user data.

An example of a good practice in Oppia codebase: 


*   When we collect the ratings that students give to explorations we both collect the individual rating of the student (so that when the student looks at the exploration again they can see what rating they gave) but also we immediately recalculate the overall average rating of the exploration. When the user deletes themselves we can remove its given rating right away, yet still benefit from the aggregate.  


### Hide

Restrict access to user data only to people with enough rights. In some cases we might want to show that some data exists to all the users, but only show the actual data to the admins. Remove links between user data where there is no need for the links. 

An example of a good practice in Oppia codebase: 


*   We have an admin page where all the admin features reside, the authorisation for this page is only given to the people that also have access to Oppia in the Google Cloud Console.
*   We only show the edits to an exploration only to creators & other editors of the exploration.


### Example

#### Task

Imagine we wanted to have a time-limited promotion where every student that completed a particular math topic would receive some kind of physical item via mail. The sending of the physical item is handled by a separate company (in this example we assume that the company handles privacy with utmost concern too).

#### Possible solution

For every student that logs in during the time when we have the promotion, we would collect their physical mail address. That address would be saved in the UserSettingsModel. The address is then available for all admins so that they can pass the mail addresses to the company that handles the delivery.

#### Privacy strategies application

##### Minimize privacy strategy applied

Instead of collecting the mail address for everyone we only collect the mail address for users that successfully complete the math topic. Also, after the promotion ends and all items are sent we remove the mail addresses from Oppia.

##### Separate privacy strategy applied

Instead of collecting the data in the UserSettingsModel, a new model is created and used for saving the mail address.

##### Abstract privacy strategy applied

Provide the students a way to retrieve the physical item in some other way, without providing their mail address. For example, they can receive the item through their schools and thus instead of collecting their exact mail address we only need to know their school.

##### Hide privacy strategy applied

Instead of collecting the mail address directly, Oppia generates code for the students that successfully complete the math topic. That code can then be used for redeeming the physical item on the website of the company that handles the deliveries or the students can provide the code to their school and the school will validate it and give the students the physical item.

#### Final solution

The final solution is to generate a code for all students that complete the math topic. This code then can be used by the students to apply for their physical item. We do not record which code was generated for which user, we only record codes that are valid. The records of codes are removed after the promotion ends.


# Implementation stage

This part focuses both on writing and reviewing code that contains changes to or additions of new user data.

In the design stage, we mainly make sure that the overall design is privacy-aware. In the implementation stage, we therefore shouldn’t have to make big decisions about privacy-related changes. If such decisions arise,  then the design doc should be reopened and these issues should be resolved there. However, in the implementation stage, it is important to make sure that we catch all the possible bugs related to privacy or data leaks. Here are some key points to bear in mind when doing this.


### Data tracing

When writing code that affects or works with user data, always try to trace through all the possible paths where the user data can end up, and make sure that the data only ends up in places where it is supposed to be saved or displayed.

In the backend, the data needs to be saved in models and in fields which clearly indicate that they can contain user data. Old logs or outputs of jobs are deleted periodically so it is fine to leave user data there. **User data in Oppia's backend must not be stored anywhere else, including in log statements.** Determining where user data should be stored is a decision that should be handled in the design doc, and care should be taken during implementation to ensure that it is not accidentally stored in the wrong place.

We need to make sure that the data is only displayed to and modifiable by the appropriate user, and that any other operation for editing user data is located on the admin page. The checks should always be performed on the backend because hiding stuff in the frontend still makes it available for malicious users who have experience with accessing frontend stuff like caches or requests.

### Wipeout and Takeout

All user data needs to be handled with Wipeout (deletion of user data) and Takeout (export of user data). More on this can be found in [Creating and modifying storage models](https://github.com/oppia/oppia/wiki/Creating-and-modifying-storage-models) and [Wipeout Implementation](https://github.com/oppia/oppia/wiki/Wipeout-Implementation). 

**Important**: Note that if data is stored in external systems (such as Cloud Storage or Firebase), care must be taken to include those storage locations in the Takeout and Wipeout processes. Please consult Vojta ([vojtech.jelinek@hey.com](mailto:vojtech.jelinek@hey.com)) if you need advice on this.
