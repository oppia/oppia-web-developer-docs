_If you miss any info or do not understand some instruction in this wiki page please contact @vojtechjelinek (vojtin.j@gmail.com). See also this wiki page for reference: [Creating and modifying storage models](https://github.com/oppia/oppia/wiki/Creating-and-modifying-storage-models)._


# Wipeout design

This part explains the design of the Wipeout process. It provides context for someone who would want to modify the Wipeout process or add new models to it.


## Backend

In the backend, the Wipeout process consists of three main parts: pre-deletion, deletion, and verification. This doc explains all the parts.


### Pre-deletion

In the pre-deletion phase, we do the following:



1. Make sure that the user is not able to sign in anymore.
2. Make sure the user is unsubscribed from all emails.
3. With the help of `_remove_user_from_activities_with_associated_rights_models(),` we:
    1. Try to delete the collections and explorations that are private and solely owned by the user that is being deleted.
    2. Remove the user from collections, explorations, and topics that the user co-owns with someone else, or has a lower tier non-owner role in them. 

If the user is a parent account of some profile users, we also do all the previously mentioned actions to the profile users.


### Deletion

The deletion runs periodically (via a CRON job).

First, we check whether the user has already been deleted. If yes, we skip that user.

Then we run the user deletion. It consists of multiple parts. Every module in core/storage is handled separately depending on what the rules are for the models in that module:



*   For modules that only contain models that need to be deleted, we use the `_delete_models` function. This method will run `apply_deletion_policy()` for all models in the module that have deletion policy `DELETE`.
*   For modules containing activities without associated rights models (like a question, story, or skill),  \
we use `_pseudonymize_activity_models_without_associated_rights_models()`, which pseudonymizes all the snapshot and commit models that contain the history of changes to the activity. 
*   For modules containing activities with associated rights models (like collection, topic, or exploration), we use `_pseudonymize_activity_models_with_associated_rights_models()`, which pseudonymizes all the snapshot and commit models that contain the history of changes to the activity, as well as the snapshot and commit models that includethe history of the rights models.

To make sure that we delete the collections and explorations that are private and solely owned by the user, as well as remove the user from collections, explorations, and topics that the user co-owns with someone else (or is not an owner but has a lower tier role within), we repeat the function `_remove_user_from_activities_with_associated_rights_models()`.

If there are summary models that contain `contributor_ids` and `contributors_summary` (as of this writing, the collection and exploration summary models fall into this category), we use the `_remove_user_id_from_contributors_in_summary_models()` function to remove the user from the contributors’ fields.

Finally, config models are pseudonymized via `_pseudonymize_config_models()`, feedback models (together with GeneralSuggestionModel) via `_pseudonymize_feedback_models()` and remaining suggestion models with `_pseudonymize_suggestion_models()`.


### Verification

The verification of the deletion runs periodically (via a CRON job). 

In the verification job, we first check whether the deletion was already run for the user (by checking the current status of the pending deletion model)if the deletion was not yet run we do not run the verification

When verification is running, for all models that have policies other than `KEEP`, `DELETE_AT_END`, and `NOT_APPLICABLE`, we run `has_reference_to_user_id()` for the user being deleted. At this point, two things may occur:



*   If the user is confirmed to be properly deleted/pseudonymized, then we:
    *   Delete the remaining models with deletion policy `DELETE_AT_END`.
    *   Create a `DeletedUserModel` with the ID of the user that was just deleted.
    *   Send emails to the deleted user and to the Oppia admin.
*   If the user was not properly deleted/pseudonymized, then we set the status of the pending deletion model to “not deleted”, and the deletion is then repeated again later via the CRON job.


## Frontend

In the frontend, there are two new pages: the “Delete Account” page and the “Pending Account Deletion” page.


### Delete Account page

Users can get onto the delete account page through the Preferences page. This page contains information about which types of data will be deleted, pseudonymized, or kept. There is also an email address where the user can send inquiries about the data that we have about them. 

Most importantly, the page includes a button that allows the user to initiate the deletion of their account. When the button is clicked, a confirmation modal will pop up where the user needs to type their username to confirm the deletion. Once they do so and click a second button to proceed, the pre-deletion phase is started, and the user is redirected to the Pending Account Deletion page.


### Pending Account Deletion page

The Pending Account Deletion page is shown to the user after they request deletion of their account, or if they try to log in while the deletion request is pending. The page explains that the account deletion will be completed in the next few hours, and after that, they will be able to create a new account.