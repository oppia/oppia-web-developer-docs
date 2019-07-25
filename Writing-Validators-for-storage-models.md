All the storage models defined in `core/storage`should have a corresponding validator defined in `core/domain/prod_validation_jobs_one_off.py`. 

The file contains a set of base validators and each new validator can inherit from those validators to use the common functionality. The base validators are as follows:

### BaseModelValidator

A base validator which defines the following functions:

* `_get_model_id_regex`: Returns a regular expression which is used to validate the model id. The function returns a default regex for models which do not have a specific id format but you should override this method if your model has a different id format.

* `_validate_model_id`: Validates the model id using the regex obtained from `_get_model_id_regex`.

* `_get_model_domain_object_instance`: Returns a domain object corresponding to the storage model. The domain object should have a `validate` function defined for the validation of object properties. This function returns a default value of `None` but it should be overridden if the model being validated has a domain object validation defined.

* `_validate_model_domain_object_instances`: Validates the model properties using the validate method of domain object corresponding to the model.

* `_get_external_id_relationships`: Returns a mapping of external ids related to a model instance mapped to the corresponding external models. The returned dict is of the format: `{FIELD_NAME: (MODEL_CLASS, [MODEL_IDS_TO_FETCH])}`

* `_validate_external_id_relationships`: Validates that the external model instances corresponding to the model instance are not deleted and exist in the datastore.

* `_fetch_external_instance_details`: Fetches the external model instances corresponding to a model instance using the dict returned from `_get_external_id_relationships`. Ensure that this method is called before other `_validate` methods so that external models are fetched already if required. The external model details are stored in the dict `external_instance_details`. The format is `{FIELD_NAME: (MODEL_CLASS_NAME, MODEL_ID, MODEL_INSTANCE)}`

* `_validate_model_time_fields`: Validates the `last_updated` and `created_on` fields of a model instance.

* `_get_custom_validation_functions`: Returns a list of custom validation functions specific to a model. It returns an empty list by default and can be overridden in subclasses.

* `validate`: Clears the errors dict for the validator class, fetches the external instance details and then runs all the validation functions for the model instance.

This Validator can be used for all the general models which do not need the common functions defined in other base validators.

### BaseSummaryModelValidator

A validator for summary models. It inherits from Base Validator and adds the following common functions:

* `_get_external_model_properties`: Returns the properties of external model corresponding to the summary model which should match the corresponding properties in the summary model. The return value is a tuple of the format: `(EXTERNAL_MODEL_NAME, EXTERNAL_MODEL_INSTANCE_DETAILS, {PROPERTY_NAME_IN_SUMMARY_MODEL: PROPERTY_NAME_IN_EXTERNAL_MODEL})`. The external model name should be in lowercase split by space.

  For example:
    * CollectionModel - collection
    * CollectionRightsModel - collection rights

  The external model instance details can be fetched from `external_instance_details` dict for the summary model.

* `_validate_external_model_properties`: Validates that properties of the summary model match the corresponding properties in the external model.

### BaseSnapshotContentModelValidator

A base validator for Snapshot Content Models. It inherits from Base Validator and adds the following common functions:

* `_validate_base_model_version_from_item_id`: Validates that the version of model corresponding to the snapshot content model matches the version used in model id.

`EXTERNAL_MODEL_NAME` should be defined by the subclasses. The external model name should be in lowercase split by space.

For example:
   * CollectionModel - collection
   * CollectionRightsModel - collection rights

### BaseSnapshotMetadataModelValidator

A base validator for Snapshot Metadata Models. It inherits from Base Snapshot Content Validator and adds the following common functions:

* `_validate_commit_type`: Validates the commit type defined in the model instance.

* `_get_change_domain_class`: Returns the change domain class corresponding to the model instance. This method should be overridden by subclasses. The change domain class defines the schema for the commit commands used in the model instance. For a detailed view, feel free to check the base class for change domain defined in `core/domain/change_domain.py`

* `_validate_commit_cmds_schema`: Validates the commit commands used in the model instance by using the validation of the change domain class corresponding to the model instance.

### BaseCommitLogEntryModelValidator

A base validator for commit log entry models. It inherits from Base Snapshot Metadata Validator and adds the following common functions:

* `_validate_post_commit_status`: Validates that post_commit_status is either public or private.

* `_validate_post_commit_is_private`: Validates that post_commit_is_private is true iff post_commit_status is private.

### BaseUserModelValidator

A base validator for user models. It inherits from Base Validator and adds the following common functions:

* `_get_exp_ids`: Returns a list of exploration ids corresponding to a user model. This returns an empty list but it should be overridden for User models which keep track of exploration ids associated to a user, for example: CompletedActivitiesModelValidator.

* `_get_col_ids`: Returns a list of collection ids corresponding to a user model. This returns an empty list but it should be overridden for User models which keep track of collection ids associated to a user, for example: CompletedActivitiesModelValidator.

* `_validate_explorations_are_public`: Validates that explorations associated with a user model are public.

* `_validate_collections_are_public`: Validates that collections associated with a user model are public.

* `_get_common_properties_of_external_model_which_should_not_match`: Returns a list of common properties to dismatch. For example: the exploration ids present in a CompletedActivitiesModel should not be present in an IncompleteActivitiesModel. So, this function will return the following list for CompletedActivitiesModel:

  ```
  ['IncompleteActivitiesModel',
  'exploration_ids',
  list of exploration_ids in completed activities, 
  'exploration_ids',
  list of exploration_ids in incomplete activities]
  ```

* `_validate_common_properties_do_not_match`: Validates that properties common with an external model are different in model instance and external model.

When you create a new validator, choose the base validator which covers the common code and no extra code is needed for the functions already defined. If you are adding a set of common validators which require some common functions not defined in any of the base validators, add a new base validators with all these common functions.

For writing a validator, prepare a complete list of validation rules which the storage model should follow and ensure that your validator is testing each of those rules.

Once you are done with writing the validator, add a new one off job for audit of the model which inherits from `ProdValidationAuditOneOffJob` and also update the `MODEL_TO_VALIDATOR_MAPPING`.

You can also have extra audit jobs apart from the ones that use the validator. For example, `UserNormalizedNameAuditOneOffJob` does not use a validator but instead iterates over a list of normalized usernames of all user models and ensures that no two names are the same.

Ensure that all audit jobs defined in `core/domain/prod_validation_jobs_one_off.py` have a corresponding test defined in `core/domain/prod_validation_jobs_one_off_test.py`.