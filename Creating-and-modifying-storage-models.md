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
    * Takeout policy (define both methods below)
        * `get_model_association_to_user`: This method should return one of the following:
            * `base_models.MODEL_ASSOCIATION_TO_USER.ONE_INSTANCE_PER_USER`. In this case, there is a single instance of the model per user. An example of this would be the UserSettingsModel. The UserSettingsModel has a one-to-one relationship with the user.'
            * `base_models.MODEL_ASSOCIATION_TO_USER.ONE_INSTANCE_SHARED_ACROSS_USERS`. In this case, an instance of a model is shared across users. For example, explorations may have multiple contributors, so the ExplorationRightsModel is shared by multiple users, but there is only one instance of this model per exploration.
            * `base_models.MODEL_ASSOCIATION_TO_USER.MULTIPLE_INSTANCES_PER_USER`. In this case, there could be multiple models associated with a single user. For example, a user could have multiple feedback threads, thus they could have multiple GeneralFeedbackThreadModels associated with their account.
            * `base_models.MODEL_ASSOCIATION_TO_USER.NOT_CORRESPONDING_TO_USER`. In this case, the model has no association with any user. In other words, the model does not contain user data.
        * `get_export_policy`. This method should return a dictionary which indicates whether each field in the model is exported or not exported. Each field in the dictionary must be one of the values in the enum base_models.EXPORT_POLICY. Specifically, this field will contain a key-value pair mapping like so:
            * `field_name: base_models.EXPORT_POLICY.EXPORTED`. (In this case, the indicated field is exported as one of the values in the takeout dictionary).
            * `field_name: base_models.EXPORTED_AS_KEY_FOR_TAKEOUT_DICT`. In this case, the indicated field is exported as one of the keys for a subdictionary within the takeout dictionary. For example, consider the case where we have a model with a MULTIPLE_INSTANCE_PER_USER association to a user. In this case, in order to distinguish between multiple models in the Takeout dictionary, we need a unique ID per model. Thus, we may export the model ID as a key for the subdictionaries within the takeout dictionary. For an example of this, reference any model with a MULTIPLE_INSTANCE_PER_USER association.
            * `field_name: base_models.EXPORT_POLICY.NOT_APPLICABLE`. In this case, the indicated field is not exported as part of the Takeout dictionary.

5. (Only if deletion policy **is not** NOT_APPLICABLE) Add a `has_reference_to_user_id(cls, user_id)` method to the model. This method should return `True` when any of the model fields contains the given `user_id`.
6. If the deletion policy is:
    - DELETE or DELETE_AT_END: Add an `apply_deletion_policy(cls, user_id)` method to the model. This method should delete all the models of this class that in any field reference the user through the user ID.
    - LOCALLY_PSEUDONYMIZE or PSEUDONYMIZE_IF_PUBLIC_DELETE_IF_PRIVATE: You will need to know the context of this model and do the pseudonymization in a wipeout service. See [Adding pseudonymizable models](https://github.com/oppia/oppia/wiki/Creating-and-modifying-storage-models#adding-pseudonymizable-models) below for more information.
7. (Only if the takeout policy is CONTAINS_USER_DATA) Add an `export_data(user_id)` method to the model. This method should return the data fields that are associated with or refer to the given user.
8. (Only if the keys in the Takeout dictionary are different from the names of the fields being exported). Add a `get_field_names_for_takeout` method. This method defines the mapping of field names to Takeout keys. 
  - By default, the Takeout key will have the exact same name as the field -- for example, a field named `asdf` is by default exported as `asdf`. 
  - However, there are cases where we want to rename a field for the sake of clarity in the Takeout dictionary. For example, instead of exporting dates (such as `last_updated`) as simply their names, we append `_msec` to the end of their name, to make it clear to a user that the data they are viewing is represented as time since the Epoch. Furthermore, we also use this for when we want to hide user IDs -- e.g. if we want to export information about a user’s parent, rather than exporting the parent_id, we will instead export the username of the parent. Thus, we define a mapping from parent_id to parent_username, since instead of exporting the information as an ID, we export it as a username.

9. [Add a validator for the model](https://github.com/oppia/oppia/wiki/Writing-Validators-for-storage-models).
10. **If this model relates to other models** (e.g., if this model exists for every exploration, the "other models" would be `ExplorationModel` and other exploration-related models) **then make sure that, when the other models are deleted, this model is also deleted**. (For example, in the case of `ExplorationModel`, the `delete_explorations` method should also be modified to include the newly added model). Also, add tests that verify that the model is deleted when the other models are deleted (e.g., in the case of `ExplorationModel`, a test should be added for `delete_exploration()` which explicitly tests that the newly-added model is also deleted).

### Adding pseudonymizable models

1. Check whether the new model is already connected to some existing model or set of models. (For example, when you add a model that is supposed to track statistics for a feedback thread, it would be connected to `GeneralFeedbackThreadModel`.)
    - If it is connected to an existing model, find where the existing model is handled in [wipeout_service.py](https://github.com/oppia/oppia/blob/develop/core/domain/wipeout_service.py) and include the new model in that place to be part of the pseudonymization. (Continuing with the example above, the new feedback model would need to be included in the `_pseudonymize_feedback_models()` function.)
    - If it is not connected to an existing model, create a new function in the wipeout service that will handle the pseudonymization. (You can take a look at the existing pseudonymization functions like `_pseudonymize_feedback_models()` or `_pseudonymize_activity_models_without_associated_rights_models()` for inspiration.)
2. If the model has a deletion policy of PSEUDONYMIZE_IF_PUBLIC_DELETE_IF_PRIVATE, make sure that, for private models, the whole model is actually deleted and not just pseudonymized. This should be done in deletion functions that are usually placed in the model services files. (E.g., for explorations, there is a `delete_exploration()` function in [exp_services.py](https://github.com/oppia/oppia/blob/develop/core/domain/exp_services.py)).
3. Make sure to add tests for the newly-added model in [wipeout_service_test.py](https://github.com/oppia/oppia/blob/develop/core/domain/wipeout_service_test.py). The tests are structured as follows: for each storage module, there are two test classes, one for deletion and the other for verification. Add new test methods for your newly-created model to both classes. 

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