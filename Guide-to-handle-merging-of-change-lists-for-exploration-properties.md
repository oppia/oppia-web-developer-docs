## Overview
Currently, we allow multiple collaborators to work on the same exploration. If collaborators are making changes while someone updates the exploration in the backend, then the change list goes through the ExplorationChangeMergeVerifier class that checks whether the changes from the old version are mergeable on the latest version. So to check for mergeability, we have some conditions that can be improved, and if any new property is added, then the conditions to merge the changes in the new property need to be added in that class. 
While adding a new property or new cmd, these changes, as explained below in the implementation, need to be done.

## Implementation
These are some important variables for the reference used later in these instructions:
1. old_version: Refers to the version of an exploration on which the changes were made.
2. latest_version: Refers to the latest version of exploration in the backend on which the changes need to be applied in order to merge the changes.
3. composite_change_list: This list consists of all the changes made between the old_version and the latest_version in the backend.
4. current_change_list: This list consists of the changes between the old_version and the latest_version of an exploration.

Now let’s start with the changes we’ll need to make.
* Make a list of all the properties that depend on the new property. What this means is, if a user makes some changes in the newly added property, what are the other properties they may need to make changes to. The editor usually informs the user in the form of validation checks or the hiding of certain components to let them know that certain properties need to be updated if there are changes made to the new property. 
For example, if the user makes changes in the answer_groups of any interaction, they may need to make the changes in the solution as the solution is dependent on the answer rule. They may also need to change the translations and voiceovers corresponding to answer_groups feedback and solution explanation if they exist because these things may have changed. This means that translations, voiceovers, and solution properties are affected by answer_groups.
When the interaction is updated, the customization_args get updated as well, i.e., for every interaction, the customization_args are different. For interactions like image region, item selection, multiple-choice, drag and drop sort, all the maths interaction, code editor, and music interaction, the answer_groups are also affected by customization_args i.e. if the customization_args are changed, then the answer_groups may need to change. Thus answers_groups are affected by customization_args and thus indirectly affected by interaction id.

So the properties related to the answer_groups are interaction id, customization_args, solutions, voiceovers, and translations. 
This means that if changes are made to the answer_groups in a state then editors working on the previous version of the exploration can not make changes to these related properties, including answer_groups in the same state.



#### # If the change CMD corresponding to the newly added property is “edit-state-property.”

* Add the condition to handle the changes made in the new property as an else if block in the [is_change_list_mergeable()](https://github.com/oppia/oppia/blob/a2223926fb5ca6f1e8daaa9cb8909fdbfa5507e4/core/domain/exp_domain.py#L2687) function inside the code block related to the [“edit_state_property” cmd](https://github.com/oppia/oppia/blob/a2223926fb5ca6f1e8daaa9cb8909fdbfa5507e4/core/domain/exp_domain.py#L2746). Inside that else-if block, add the conditions to check whether the composite change list contains changes to properties related to the newly added property and if they can be handled or not.
For example, this block handles answer_groups changes.

&emsp; <img src="https://user-images.githubusercontent.com/56637531/125595877-fc334535-c164-485a-914e-6839c3c8dac4.png" width="600" height="250"/>

&emsp; **Snippet 1**

The changed_properties dict records the changed properties in a particular state. Here, all the properties related to answer_groups are handled and checked for changes. First, we’re checking whether the latest version has the same interaction as that of the old_version of an exploration. If it is then only the change in answer_group can be merged, and thus we are moving on to the next properties. Changes in the solution, cust_args, and voiceovers will directly conflict with the answer_groups changes and so, we are grouping these properties in one list called PROPERTIES_CONFLICTING_ANSWER_GROUPS_CHANGES. It looks like this: 

```
PROPERTIES_CONFLICTING_ANSWER_GROUPS_CHANGES = [
    STATE_PROPERTY_INTERACTION_SOLUTION,
    STATE_PROPERTY_RECORDED_VOICEOVERS,
    STATE_PROPERTY_INTERACTION_CUST_ARGS]
```
**Snippet 2**

So as we can see on line number 2811-2812 inside snippet 1, we check if any changes are made in PROPERTIES_CONFLICTING_ANSWER_GROUPS_CHANGES in the backend, if yes, then we simply reject the changes as they can not be handled but if not, then we’ll proceed further to the next steps to confirm if the change is mergeable. We are also checking that if there are any changes in the answer_groups itself in the composite_change_list, if yes then that means that the answer_group property is changed by some other user and then we can not merge any changes in that related to the answer_group. 
If any of the conditions mentioned above returns False, we check if there is any change made in the same state as of answer group change, if not, then that answer_group change will be easily mergeable as there are no property changes in the same state; thus, there will not be any conflicting change.
In a similar way, we’ll need to write the conditions to handle the merging conditions of the new property. If there are more than 2 related properties handled in the same way, we can create a list just like in Snippet 2 and write the common condition to avoid repetitive if-else blocks. 

* So after handling the new property changes above, we should handle the changes to the properties related to the newly added property from the current change list. 
To do this, add the conditions in the existing blocks of all the properties related to the new property inside the [is_change_list_mergeable()](https://github.com/oppia/oppia/blob/a2223926fb5ca6f1e8daaa9cb8909fdbfa5507e4/core/domain/exp_domain.py#L2687) function to check if there are any new property changes in the composite_change_list. If so, also check if they affect the related property.
For example: 
Ex. 1: PROPERTIES_CONFLICTING_SOLUTION_CHANGES includes the answer group property as it is affected by the answer_groups, and if there are any changes in the answer groups, the solution changes can not be merged.
```
    PROPERTIES_CONFLICTING_SOLUTION_CHANGES = [
        STATE_PROPERTY_INTERACTION_ANSWER_GROUPS,
        STATE_PROPERTY_RECORDED_VOICEOVERS,
        STATE_PROPERTY_INTERACTION_CUST_ARGS]
```

Ex. 2: Inside the condition of the content property changes we check if the content has really changed or not, i.e. if the final content is similar to the old content then the net change is zero and thus we can merge the new content changes by another user. We also check if the voiceover and/or translations of the content have changed or not, if yes then the content changes will be conflicting and will not be able to get merged. 

<img src="https://user-images.githubusercontent.com/56637531/125607112-2917feef-3bc9-4861-94ee-b198ad0a7373.png" width="600" height="250"/>

So similarly, add the condition to check if there are any changes made in the newly added property in the composite_change_list, and if yes, will they affect the related property or not. 


#### # If the newly added property is non-state property, i.e. change command associated with the new property is not edit_state_property and is a new command, like for renaming the states we use ‘rename_state’ and for adding new state it’s ‘add_new_state’.
In such cases:

* First, add a condition to keep the record of the changes made in the new property from the composite_change_list. Go to the exp_domain.py file and add an else if block for the new cmd there inside the [_parse_exp_change(self, change)](https://github.com/oppia/oppia/blob/a2223926fb5ca6f1e8daaa9cb8909fdbfa5507e4/core/domain/exp_domain.py#L2634) function. Inside that new cmd block add the conditions to record the changes made in the new property.
For example: 
Example 1: Inside the [“edit_state_property” block](https://github.com/oppia/oppia/blob/a2223926fb5ca6f1e8daaa9cb8909fdbfa5507e4/core/domain/exp_domain.py#L2666) we keep the record of the changed properties of a state inside the dict where the key is the state name and the value is the list of the changed properties inside that state. We call this dict the  changed_properties dict and use it later when we need to check if a particular property has changed in the backend.
Example 2: In order to keep the record of the new states added in the latest_version from the composite_change_list, we store the names of newly added states inside the added_state_names list like this: 

<img src="https://user-images.githubusercontent.com/56637531/125607712-788e21b3-fed2-4cbc-b02e-e801da0db658.png" width="600" height="50"/>

So, keep the record of the changes in the newly added property from the composite change list inside its new cmd block as explained above.


* Now add a condition to handle the merging of the new property changes inside the [is_change_list_mergeable()](https://github.com/oppia/oppia/blob/a2223926fb5ca6f1e8daaa9cb8909fdbfa5507e4/core/domain/exp_domain.py#L2687) function under the [for loop](https://github.com/oppia/oppia/blob/a2223926fb5ca6f1e8daaa9cb8909fdbfa5507e4/core/domain/exp_domain.py#L2732) and create a new else block for the new cmd just like other commands blocks. Now inside that cmd block, add the conditions to check whether the properties related to the new property have changed in the composite_change_list or not.
For example: 
To handle the translation changes, we have an “add_written_translation” cmd block. So the translation is only related to the property for which the translation is added or changed. Inside that [“add_written_translation” cmd block](https://github.com/oppia/oppia/blob/a2223926fb5ca6f1e8daaa9cb8909fdbfa5507e4/core/domain/exp_domain.py#L2875), we just check if the property for which the translation is added/changed has been updated if so, we can not merge the translation change, and if not we can easily merge that translation change.  So the condition looks like this:

    <img src="https://user-images.githubusercontent.com/56637531/125611780-0c31e835-de6f-49a6-ac18-a10c88b157d0.png" width="600" height="200"/>

So in a similar way as explained, add the conditions for the new property change mergeability according to how the newly added property is related to the other properties.


* So after handling the new property changes above, we should handle the changes of the properties related to the new property from the current change list. 
To do this, add the conditions in the existing blocks of all the properties related to the new property inside the [is_change_list_mergeable()](https://github.com/oppia/oppia/blob/a2223926fb5ca6f1e8daaa9cb8909fdbfa5507e4/core/domain/exp_domain.py#L2687) function to check if there are any new property changes in the composite_change_list, and if yes, will they affect the related property.
For example: 
Hints are related to the translations, so if there are any changes in the hint’s translation in the composite_change_list, we can not merge the hints changes from the current change list, therefore we have just checked if the hints exist in the changed_translations dict. The conditions look like this:

<img src="https://user-images.githubusercontent.com/56637531/125612054-86f27171-1a4c-4ad0-8887-c0c80faa963c.png" width="600" height="200"/>


***
