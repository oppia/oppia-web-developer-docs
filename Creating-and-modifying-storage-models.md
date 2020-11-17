_If you miss any info or do not understand some instruction in this wiki page please contact @vojtechjelinek (vojtin.j@gmail.com)._ 

The purpose of this wiki is to provide step-by-step guides on how to add, remove, or modify model classes.

## Creating a new model class

1. Decide if the model should be versioned or not. 
    * Versioned storage models preserve the history of all fields in their snapshots, and support reverts to any historical version. All versioned models should inherit from the `VersionedModel` class (see the [VersionedModel docstring](https://github.com/oppia/oppia/blob/develop/core/storage/base_model/gae_models.py#L526) for more info).
    * Normal (non-versioned) models preserve just the current version. Normal storage models should inherit from `BaseModel`.
2. Add properties to the model. For more information about properties, please see the [GAE "Entity property reference" docs](https://cloud.google.com/appengine/docs/standard/python/ndb/entity-property-reference).
3. Decide the model deletion and takeout policy.
    * The deletion policy is used when the user requests the deletion of their user account. The deletion policy should be decided together with the data admins (**@BenHenning** and **@seanlip**). There are multiple deletion policies:
        * KEEP — the model should be kept for auditing or logging purposes (e.g. `DeletedUserModel` or `SentEmailModel`).
        * DELETE — the model only belongs to one user, and should be deleted (e.g. `CompletedActivitiesModel` or `LearnerPlaylistModel`).
        * DELETE_AT_END — the model only belongs to one user, and should be deleted. But, since the data in that model is relevant for the wipeout process, the model should only be deleted at the end after all other models are deleted. (E.g. `UserSettingsModel` or `UserAuthDetailsModel`.)
        * LOCALLY_PSEUDONYMIZE — the model should be anonymized accounting for the local context (e.g. `GeneralFeedbackThreadModel` is pseudonymized together with `GeneralFeedbackMessageModel` and `GeneralSuggestionModel`).
        * PSEUDONYMIZE_IF_PUBLIC_DELETE_IF_PRIVATE — the model should be pseudonymized if it is accessible by the general public (like published explorations) and deleted if it is not public (e.g. `ExplorationRightsModel` or `ExpSummaryModel`).
        * NOT_APPLICABLE — the model is not related to user data at all (e.g. `ClassifierTrainingJobModel` or `CommunityContributionStatsModel`).
    * Takeout policy
        * CONTAINS_USER_DATA — the model contains user data
        * NOT_APPLICABLE — the model doesn't contain any user data
4. Decide the lowest-level role in the [role hierarchy](https://github.com/oppia/oppia/wiki/Instructions-for-editing-roles-or-actions#7-view-role-hierarchy) by whom the model can be created. 
    - By default, the static method `get_lowest_supported_role` (defined in the storage base model) assumes `EXPLORATION_EDITOR` to be the lowest role (meaning that the model can be created by all roles above this role in the hierarchy, including itself).
    - To set a different role, simply override the method in the model class and specify the desired value. 
    - For example, `UserSettingsModel` overrides the `get_lowest_supported_role` and sets the lowest supported role to `LEARNER`.
5. (Only if deletion policy **is not** NOT_APPLICABLE) Add a `has_reference_to_user_id(cls, user_id)` method to the model. This method should return `True` when any of the model fields contains the given `user_id`.
6. If the deletion policy is:
    - DELETE or DELETE_AT_END: Add an `apply_deletion_policy(cls, user_id)` method to the model. This method should delete all the models of this class that in any field reference the user through the user ID.
    - LOCALLY_PSEUDONYMIZE or PSEUDONYMIZE_IF_PUBLIC_DELETE_IF_PRIVATE: You will need to know the context of this model and do the pseudonymization in a wipeout service. See [Adding pseudonymizable models](https://github.com/oppia/oppia/wiki/Creating-and-modifying-storage-models#adding-pseudonymizable-models) below for more information.
7. (Only if the takeout policy is CONTAINS_USER_DATA) Add an `export_data(user_id)` method to the model. This method should return the data fields that are associated with or refer to the given user.
8. [Add a validator for the model](https://github.com/oppia/oppia/wiki/Writing-Validators-for-storage-models).
9. **If this model relates to other models** (e.g., if this model exists for every exploration, the "other models" would be `ExplorationModel` and other exploration-related models) **then make sure that, when the other models are deleted, this model is also deleted (in case of `ExplorationModel` the `delete_explorations` method should also be modified to include the newly added model). Also, add tests that will verify that the model is deleted when the other models are deleted (in case of `ExplorationModel` the test souhld be added for the `delete_exploration` explicitely testing that the newly added model is also deleted).**

### Adding pseudonymizable models

1. Check whether the new model is already connected to some existing model or set of models. (For example, when you add a model that is supposed to track statistics for a feedback thread, it would be connected to `GeneralFeedbackThreadModel`.)
    - If it is connected to an existing model, find where the existing model is handled in the [wipeout_service.py](https://github.com/oppia/oppia/blob/develop/core/domain/wipeout_service.py) and include the new model in that place to be part of the pseudonymization. (Continuing with the example above, the new feedback model would need to be included in the `_pseudonymize_feedback_models()` function.)
    - If it is not connected to an existing model, create a new function in the wipeout service that will handle the pseudonymization. (You can take a look at the existing pseudonymization functions like `_pseudonymize_feedback_models()` or `_pseudonymize_activity_models_without_associated_rights_models()` for inspiration.)
2. If the model has a deletion policy of PSEUDONYMIZE_IF_PUBLIC_DELETE_IF_PRIVATE, make sure that, for private models, the whole model is actually deleted and not just pseudonymized. This should be done in deletion functions that are usually placed in the model services files. (E.g., for explorations, there is a `delete_exploration()` function in [exp_services.py](https://github.com/oppia/oppia/blob/develop/core/domain/exp_services.py)).
3. Do not forget to add tests for the newly added model into the [wipeout_service_test.py](https://github.com/oppia/oppia/blob/develop/core/domain/wipeout_service_test.py). The tests are structured in a way that for each storage module there are two tests classes, one for deletion and other for verification part, add new test methods for your newly created model to both classes. 

## Modifying a model field

### Adding an index to a field

If you need to index a field (i.e., add `indexed=True` to the field constructor), you'll need to also build the index manually in the production datastore. This can be done by a simple MapReduce job that iterates over all the models and, without any modification, puts them again in the datastore. An example job can be seen at https://github.com/oppia/oppia/blob/624e4b1a9f09996df5ffcd4cbed96ebd6ba96e32/core/domain/takeout_domain_jobs_one_off.py#L38-L79.

## Removing an old field from a model

Firstly, remove the field to the bottom of the list of fields, and mark it with a comment saying `# TODO(#XXXX): DEPRECATED in <version>. Do not use.`. If the field was previously set as required, it should be set to optional instead. Also, create an issue for proper removal of the field in next release.

To actually remove the field, perform the following steps:

### Steps to remove a field from models that inherit from `BaseModel`

1. Remove the field from the storage model code itself.
2. Add a migration job to remove the field from already-existing models. For example, the one-off job for removing the `username` from commit log models looks like this: https://github.com/oppia/oppia/blob/170bdeae5912ced0abc71257f5b0e5ca98fd1418/core/domain/activity_jobs_one_off.py#L142-L182
3. **If the model inherits from `VersionedModel`**: add a `_reconstitute()` method for the model that will ensure that, when we revert to an older version of the model, we properly remove the field so that the model can be loaded. (To see an example, take a look at the `_reconstitute()` methods in `CollectionRightsModel` and `ExplorationRightsModel` (https://github.com/oppia/oppia/blob/7623cd028d15a6326cac186f673f368dcae30929/core/storage/exploration/gae_models.py#L403-L440).)
4. Create a PR and [submit the job to be tested on the backup server](https://github.com/oppia/oppia/wiki/Running-jobs-in-production).