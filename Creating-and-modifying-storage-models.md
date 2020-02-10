## Creating a new storage model

1. Decide if the model should be versioned or not. 
    * The versioned model preserves the history of all the fields in its snapshots and should be able to revert the current state into the any historical version. Versioned storage models need to inherit from `VersionedModel` (more info is defined in the [VersionedModel docstring](https://github.com/oppia/oppia/blob/develop/core/storage/base_model/gae_models.py#L526))
    * The normal model preserves just the current version. Normal storage models need to inherit from `BaseModel`.
2. Add properties to the model, all info regarding properties is explained in [Entity property reference](https://cloud.google.com/appengine/docs/standard/python/ndb/https://cloud.google.com/appengine/docs/standard/python/ndb/entity-property-reference).
3. Decide the model deletion and takeout policy.
    * Deletion policy
    * Takeout policy
4. [Add validator for the model](https://github.com/oppia/oppia/wiki/Writing-Validators-for-storage-models).

## Deprecating model field