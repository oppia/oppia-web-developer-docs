## Creating a new storage model

1. Decide if the model should be versioned or not. 
    * The versioned model preserves the history of all the fields in its snapshots and should be able to revert the current state into the any historical version. Versioned storage models need to inherit from `VersionedModel` (more info is defined in the [VersionedModel docstring](https://github.com/oppia/oppia/blob/develop/core/storage/base_model/gae_models.py#L526))
    * The normal model preserves just the current version. Normal storage models need to inherit from `BaseModel`.
2. Add properties to the model, all info regarding properties is explained in [Entity property reference](https://cloud.google.com/appengine/docs/standard/python/ndb/https://cloud.google.com/appengine/docs/standard/python/ndb/entity-property-reference).
3. Decide the model deletion and takeout policy.
    * Deletion policy is a policy used when the user requests the deletion of their user account. The deletion policy should be decided together with the data admins. Some models can be affected by this, there are multiple deletion policies:
        * KEEP — the model should be kept for auditing or logging purposes
        * DELETE — the model only belongs to one user and should be deleted
        * ANONYMIZE — the model should be completely anonymized
        * LOCALLY_PSEUDONYMIZE — the model should anonymized accounting for the local context (for example messages from one user in the same thread should have the same id) 
        * KEEP_IF_PUBLIC — the model should be kept if it is accessible from the public (like published explorations)
        * NOT_APPLICABLE — the model is not related to user data at all
    * Takeout policy
        * CONTAINS_USER_DATA — the model contains user data
        * NOT_APPLICABLE — the model doesn't contain any user data
4. Add `has_reference_to_user_id(user_id)` to the model, this method should return true when any of the models fields contains the specified `user_id`.
5. [Add validator for the model](https://github.com/oppia/oppia/wiki/Writing-Validators-for-storage-models).

## Deprecating old field
For now, the deprecated fields are moved to the bottom of the list of fields and marked with a comment saying `# DEPRECATED in <version>. Do not use.`. If the field was previously set as required it should be set as optional.