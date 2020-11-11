_If you miss any info or do not understand some instruction in this wiki page please contact @vojtechjelinek (vojtin.j@gmail.com)._ 

The purpose of this wiki is to provide guides on how to add, remove, or modify model classes.

## Creating a new model class

1. Decide if the model should be versioned or not. 
    * The versioned model preserves the history of all the fields in its snapshots and should be able to revert the current state into the any historical version. Versioned storage models need to inherit from `VersionedModel` (more info is defined in the [VersionedModel docstring](https://github.com/oppia/oppia/blob/develop/core/storage/base_model/gae_models.py#L526))
    * The normal model preserves just the current version. Normal storage models need to inherit from `BaseModel`.
2. Add properties to the model, all info regarding properties is explained in [Entity property reference](https://cloud.google.com/appengine/docs/standard/python/ndb/entity-property-reference).
3. Decide the model deletion and takeout policy.
    * Deletion policy is a policy used when the user requests the deletion of their user account. The deletion policy should be decided together with the data admins. Some models can be affected by this, there are multiple deletion policies:
        * KEEP — the model should be kept for auditing or logging purposes (for example `DeletedUserModel` or `SentEmailModel`)
        * DELETE — the model only belongs to one user and should be deleted (for example `CompletedActivitiesModel` or `LearnerPlaylistModel`)
        * DELETE_AT_END — the model only belongs to one user and should be deleted, but the data in that model are relevant for the wipeout process so the model needs to be deleted at the end after all other models are deleted (for example `UserSettingsModel` or `UserAuthDetailsModel`)
        * LOCALLY_PSEUDONYMIZE — the model should be anonymized accounting for the local context (for `GeneralFeedbackThreadModel` is pseudonymized together with `GeneralFeedbackMessageModel` and `GeneralSuggestionModel`) 
        * PSEUDONYMIZE_IF_PUBLIC_DELETE_IF_PRIVATE — the model should be pseudonymized if it is accessible from the public (like published explorations) and deleted if it is not public (for example `ExplorationRightsModel` or `ExpSummaryModel`)
        * NOT_APPLICABLE — the model is not related to user data at all (for example `ClassifierTrainingJobModel` or `CommunityContributionStatsModel`)
    * Takeout policy
        * CONTAINS_USER_DATA — the model contains user data
        * NOT_APPLICABLE — the model doesn't contain any user data
4. Decide the lowest level role in the [role hierarchy](https://github.com/oppia/oppia/wiki/Instructions-for-editing-roles-or-actions#7-view-role-hierarchy) for which the model can be populated. 
    - By default, the static method `get_lowest_supported_role` (defined in the storage base model) assumes `EXPLORATION_EDITOR` to be the lowest role (meaning that the model can be created for all roles above this role in the hierarchy, including itself).
    - To set a different role, simply override the method in the model class and specify the desired value. 
    - For example - `UserSettingsModel` overrides the `get_lowest_supported_role` and sets the lowest supported role to `LEARNER`. 
5. (Only if deletion policy **is not** NOT_APPLICABLE) Add `has_reference_to_user_id(cls, user_id)` to the model, this method should return true when any of the models fields contains the specified `user_id`.
6. If the deletion policy is:
    - DELETE or DELETE_AT_END: Add `apply_deletion_policy(cls, user_id)` to the model, this method should delete all the models of this class that in any field reference the user with `user_id`.
    - LOCALLY_PSEUDONYMIZE or PSEUDONYMIZE_IF_PUBLIC_DELETE_IF_PRIVATE: You will need to know the context of this model and do the pseudonymization in a wipeout service.
10. (Only if takeout policy is CONTAINS_USER_DATA) Add `export_data(user_id)` to the model, this method should return the data from the models that belong or reference the specified `user_id`.
11. [Add validator for the model](https://github.com/oppia/oppia/wiki/Writing-Validators-for-storage-models).
12. **If this model relates to some parent models (for example this is a model that will exist for every exploration so the parent model would be `ExplorationModel`) make sure that when the parent model is deleted this model is also deleted.**

## Modifying a model field

### Adding index to field

When the field is newly indexed (`indexed=True` is added to the field constructor) we need to update the index by reiterating over all the models that we have in our datastore, this can be done by a simple map-reduce job that iterates over all the models and without any modification puts them again in the datastore. Example job can be seen at https://github.com/oppia/oppia/blob/624e4b1a9f09996df5ffcd4cbed96ebd6ba96e32/core/domain/takeout_domain_jobs_one_off.py#L38-L79.

## Removing an old field from a model

Firstly, the removed field is moved to the bottom of the list of fields and marked with a comment saying `# TODO(#XXXX): DEPRECATED in <version>. Do not use.`. If the field was previously set as required it should be set as optional. An issue should be created for proper removal of the field in next release.


### Steps to remove a field from models that inherit from `BaseModel`

1. Remove the field form the storage model code itself.
2. Add a migration job to remove the field from already existing models. The one-off job for removing the `username` from commit log models looks like this: https://github.com/oppia/oppia/blob/170bdeae5912ced0abc71257f5b0e5ca98fd1418/core/domain/activity_jobs_one_off.py#L142-L182
3. Create a PR and submit the job to be tested on the backup server.

### Steps to remove a field from models that inherit from `VersionedModel`

1. Remove the field form the storage model code itself.
2. Add a migration job to remove the field from already existing models. The one-off job for removing the `username` from commit log models looks like this: https://github.com/oppia/oppia/blob/170bdeae5912ced0abc71257f5b0e5ca98fd1418/core/domain/activity_jobs_one_off.py#L142-L182
4. Add `_reconstitute` method for the model that will ensure that when we revert to an older version of the model we properly remove the field so that the model can be loaded. `_reconstitute` is already implemented for the `CollectionRightsModel` and `ExplorationRightsModel` (https://github.com/oppia/oppia/blob/7623cd028d15a6326cac186f673f368dcae30929/core/storage/exploration/gae_models.py#L403-L440).
4. Create a PR and submit the job to be tested on the backup server.
