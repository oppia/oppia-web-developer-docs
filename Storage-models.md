## Table of contents

* [Introduction](#introduction)
* [How the storage layer works](#how-the-storage-layer-works)
  * [Storage model concepts](#storage-model-concepts)
  * [Model classes with ndb](#model-classes-with-ndb)
  * [Oppia's datastore interface](#oppias-datastore-interface)
    * [The GAE datastore interface implementation](#the-gae-datastore-interface-implementation)
  * [Model classes at Oppia](#model-classes-at-oppia)
    * [Naming conventions and structure](#naming-conventions-and-structure)
    * [Model versioning](#model-versioning)
    * [Deletion policy for wipeout](#deletion-policy-for-wipeout)
    * [Takeout policy](#takeout-policy)
    * [Export data](#export-data)
    * [Map property names to takeout keys](#map-property-names-to-takeout-keys)
    * [Has reference to user ID](#has-reference-to-user-id)
    * [Apply deletion policy](#apply-deletion-policy)
    * [Pseudonymizable models](#pseudonymizable-models)
* [Common procedures](#common-procedures)
  * [Create a new model class](#create-a-new-model-class)
  * [Add a pseudonymizable model](#add-a-pseudonymizable-model)
  * [Modify a model field](#modify-a-model-field)
    * [Add an index to a field](#add-an-index-to-a-field)
    * [Remove an old field from a model](#remove-an-old-field-from-a-model)
* [Contact](#contact)

## Introduction

You might be used to programs holding data in variables, but for an application like Oppia, we need some way to store that data such that it survives the application shutting down. We don't want to lose all our data just because we release a new version of Oppia! To store data persistently, you might think about storing it in a file like this:

```text
 User        Application               File system
 ----        -----------               -----------
  |  GET /prefs   |                         |
  | ------------> |                         |
  |               |   f = open('f.json')    |
  |               |   data = json.load(f)   |
  |               | ----------------------> |
  |               |                         |
  |               |          data           |
  |               | <---------------------- |
  | data['prefs'] |                         |
  | <------------ |                         |
```

This works, but it turns out we can do better by using a dedicated database server. At Oppia, we use Google Cloud's [Datastore](https://cloud.google.com/datastore) like this:

```text
 User        Application                Datastore
 ----        -----------                ---------
  |  GET /prefs   |                         |
  | ------------> |                         |
  |               |  Retrieve preferences   |
  |               | ----------------------> |
  |               |                         |
  |               |          prefs          |
  |               | <---------------------- |
  |      prefs    |                         |
  | <------------ |                         |
```

To interact with the datastore, we use Google's [ndb library](https://googleapis.dev/python/python-ndb/latest/index.html). We refer to the code that uses ndb and defines what kind of data we store in the datastore as the "storage layer." In this guide, we'll discuss how the storage layer works and how to make some common storage layer changes.

## How the storage layer works

### Storage model concepts

We organize our data using _models_, which you can think of like Python classes. A model describes an object that can have properties of various types. Instances of these models can then be created with particular values for those properties. However, unlike Python classes, a model has only data (no functions), and a model's properties are strictly typed.

For example, we might define a user model with the following properties:

* `id`: An integer
* `username`: A string
* `user_is_admin`: A boolean

Then we could create many instances of this model:

```text
User[id=1, username=learner1, user_is_admin=False]
User[id=14, username=admin1, user_is_admin=True]
```

### Model classes with ndb

In practice, we define models using special Python classes called _model classes_. If we used ndb directly ([we don't](#oppias-datastore-interface)), we could define our user model from above as the following model class:

```python
class User(Model):
    id = IntegerProperty()
    username = StringProperty()
    user_is_admin = BooleanProperty()
```

Then we can create a user model instance (called an _entity_) like this:

```python
user = User(id=1, username='learner1', user_is_admin=False)
```

The `Model` superclass provides methods for writing entities to the datastore and retrieving them:

```python
user1 = User(id=1, username='learner1', user_is_admin=False)
user2 = User(id=14, username='admin1', user_is_admin=True)

user1.put()
user2.put()

User.query().filter(User.id == 1).get()  # Returns user1
```

For more information on how ndb model classes work, including all the available property types, see the [ndb documentation](https://googleapis.dev/python/python-ndb/latest/model.html). Also note that "properties" are also sometimes called "fields."

### Oppia's datastore interface

Most Oppia code doesn't use ndb directly. Instead, we provide our own _datastore interface_ that matches the ndb interface pretty closely. This interface is called a _seam_ because, just like a seam in clothing joins two pieces of cloth, the interface joins two pieces of code: Oppia and ndb. It's true that the seam just calls ndb under the hood, but it's important that you use the seam, and not ndb, in your code so that if one day we wanted to switch to a different storage provider, we would only have to change the seam.

The seam code lives in [`core/platform/`](https://github.com/oppia/oppia/tree/develop/core/platform).

Now this discussion of a "seam" is pretty abstract, so let's see how this works in practice. At the start of every file that defines a model, you'll see code like this:

```python
(base_models,) = models.Registry.import_models([models.NAMES.base_model])

datastore_services = models.Registry.import_datastore_services()
transaction_services = models.Registry.import_transaction_services()
```

All datastore interactions should occur through the `base_models`, `datastore_services`, and `transaction_services` modules. We never import `ndb` into files outside the seam.

The `Registry` we are retrieving these modules from is defined in [`core/platform/models.py`](https://github.com/oppia/oppia/blob/develop/core/platform/models.py). This registry lets us load the implementation of our seam interface that applies for our platform. Right now we only have one implementation, which is defined as `_Gae` in `core/platform/models.py`.

`Registry` defines the datastore interface. It provides a number of functions, but here are the most important ones:

* `import_models(model_names)`: Returns a tuple of the model modules named in `model_names`. The modules are returned in the same order in which they appeared in `model_names`. Each module's name is specified in the `core.platform.models.NAMES` constant.

* `import_datastore_services()`: Returns a module (by convention named `datastore_services`) that includes most of the functions you'll need to interact with the datastore. For example, instead of defining a property with `ndb.IntegerProperty()`, you'll use `datastore_services.IntegerProperty()`.

  Note that `datastore_services` will not include everything from ndb. For example, only some properties are included. This is intentional! The properties in `datastore_services` are the only ones we support, so if you can't achieve what you want through `datastore_services`, you should not fall back to ndb. Instead, you should devise an alternate approach that only requires the functionality available through `datastore_services`, or you should extend `datastore_services`.

* `import_transaction_services()` returns a module that contains the decorator `run_in_transaction_wrapper`. You can use it to perform a datastore operation as a _transaction_, which means that it is guaranteed to either complete fully or not happen at all. In other words, if a transaction fails, the datastore will look like the transaction was never started.

  Transactions are useful for keeping the datastore in a self-consistent state. For example, suppose you have both user models and user profile models, but you never want to have a profile without a corresponding user or a user with no associated profile. To prevent this, you can use transactions like this:

  ```python
  @transaction_services.run_in_transaction_wrapper
  def delete_user(user_key, profile_key):
      user_key.delete()
      profile_key.delete()
  ```

  Now if `profile_key.delete()` fails, the transaction will ensure that the user doesn't get deleted either.

Note that in some places the datastore interface is not well-defined. For example, `Registry` doesn't specify which ndb properties should be available. In practice, we assume that the interface is what our Google Appengine (GAE) implementation provides.

#### The GAE datastore interface implementation

The GAE implementation provides modules that the `Registry` functions return.

* `import_models(model_names)`: Loading each module is handled by dedicated code in `_Gae.import_models()`. This means that if you add a new model module, you need to update `import_models()` to support it.

  By convention, models are defined in files whose paths have the form `core/storage/<model module name>/gae_models.py`. For example, above we saw `base_models` being loaded using `import_models`. This module is defined at `core/storage/base_model/gae_models.py`, so `base_models` in the example above refers to `core.storage.base_model.gae_models`.

* `import_datastore_services()`: The returned module determines which ndb properties we support.

* `import_transaction_services()`: Returns a module that provides a transaction decorator.

### Model classes at Oppia

#### Naming conventions and structure

Naming conventions:

* The modules that define storage models (model modules) have file paths of the form `core/storage/<model module name>/gae_models.py`. These modules then define model classes.

* Model class names end in `Model`, for example `UserSettingsModel`.

#### Model versioning

For some models (e.g. explorations), we want to keep a record of old versions. These models inherit from `core.storage.base_model.gae_models.VersionedModel`. To use a versioned model, you must also define two models for representing snapshots: a snapshot metadata model (subclass of `BaseSnapshotMetadataModel`) and a snapshot content model (subclass of `BaseSnapshotContentModel`). Then in your model, set the `SNAPSHOT_METADATA_CLASS` and `SNAPSHOT_CONTENT_CLASS` instance variables equal to your snapshot metadata and content model classes, respectively.

That's pretty much it! The functions in `VersionedModel` will handle the snapshots for you. All you need to remember is that instead of calling `put()`, you should call `commit()` when saving versioned entities to the datastore. See the source code for [`VersionedModel`](https://github.com/oppia/oppia/blob/develop/core/storage/base_model/gae_models.py) for more information about what you can do with it.

Unversioned models don't track old versions and inherit from `core.storage.base_model.gae_models.BaseModel` instead.

#### Deletion policy for wipeout

[[Wipeout|Wipeout-implementation]] is our program for ensuring that when a user deletes their account, we properly delete their data or make it pseudonymous. Whenever you create a new model, you should have already gotten a [[design doc|Writing-design-docs]] approved by Oppia's data owners. If you have questions about how this approval process works or how we handle privacy at Oppia, see our [[guide to privacy-aware programming|Privacy-aware-programming]].

**IMPORTANT: You MUST get your model's deletion policy approved through a design doc before opening a PR.**

The deletion policies are defined in the `DELETION_POLICY` enum in [`core/storage/base_model/gae_models.py`](https://github.com/oppia/oppia/blob/develop/core/storage/base_model/gae_models.py). This enum has the following values:

* `KEEP`: The model should be kept for auditing or logging purposes. For example: `DeletedUserModel` or `SentEmailModel`.
* `DELETE`: The model only belongs to one user and should be deleted. For example: `CompletedActivitiesModel` or `LearnerPlaylistModel`.
* `DELETE_AT_END`: The model only belongs to one user and should be deleted, but since the data in that model is relevant for the wipeout process, the model should only be deleted at the end after all other models are deleted. For example: `UserSettingsModel` or `UserAuthDetailsModel`.
* `LOCALLY_PSEUDONYMIZE`: The model should be pseudonymized accounting for the local context. For example, `GeneralFeedbackThreadModel` is pseudonymized together with `GeneralFeedbackMessageModel` and `GeneralSuggestionModel`.
* `PSEUDONYMIZE_IF_PUBLIC_DELETE_IF_PRIVATE`: The model should be pseudonymized if it is accessible by the general public (like published explorations) and deleted if it is not public. For example: `ExplorationRightsModel` or `ExpSummaryModel`.
* `NOT_APPLICABLE`: The model is not related to user data at all. For example: `ClassifierTrainingJobModel` or `CommunityContributionStatsModel`.

Your model class must provide a static `get_deletion_policy()` method that returns one of these deletion policies. For example:

```python
@staticmethod
def get_deletion_policy() -> base_models.DELETION_POLICY:
    return base_models.DELETION_POLICY.DELETE
```

#### Takeout policy

Takeout is our program that lets users download their data. Takeout needs to know two things to let users export their data:

* How is each model associated to users? For example, there is one `UserSettingsModel` per user, but a single `ExplorationRightsModel` may be shared across many users.

  This question is answered by the `get_model_association_to_user()` static method, which returns one of the values of the enum `MODEL_ASSOCIATION_TO_USER` in [`core/storage/base_model/gae_models.py`](https://github.com/oppia/oppia/blob/develop/core/storage/base_model/gae_models.py). These values are:

  * `ONE_INSTANCE_PER_USER`: There is a single instance of the model per user and a single user for each model instance. An example of this would be the `UserSettingsModel` because each user has exactly one settings model, and each settings model is for exactly one user.
  * `ONE_INSTANCE_SHARED_ACROSS_USERS`: An instance of a model may be shared across users. For example, explorations may have multiple contributors, so the `ExplorationRightsModel` is shared by multiple users.
  * `MULTIPLE_INSTANCES_PER_USER`: There could be multiple models associated with a single user. For example, a user could have multiple feedback threads, so they could have multiple `GeneralFeedbackThreadModels` associated with their account.
  * `NOT_CORRESPONDING_TO_USER`: The model has no association with any user. In other words, the model does not contain user data.

  For example, our User model would have a one-to-one relationship with users, so its model association would look like this:

  ```python
  @staticmethod
  def get_model_association_to_user() -> base_models.MODEL_ASSOCIATION_TO_USER:
      return base_models.MODEL_ASSOCIATION_TO_USER.ONE_INSTANCE_PER_USER
  ```

* Which of the model's properties should be exported? For example, there is some data, like internal user IDs, that we don't want to export.

  This question is answered by the `get_export_policy()` static method, which returns a dictionary mapping each property name to one of the values of the enum `EXPORT_POLICY` in [`core/storage/base_model/gae_models.py`](https://github.com/oppia/oppia/blob/develop/core/storage/base_model/gae_models.py). These values are:

  * `EXPORTED`: The property is exported as one of the values in the takeout dictionary.
  * `EXPORTED_AS_KEY_FOR_TAKEOUT_DICT`: The property is exported as the key for a sub-dictionary within the takeout dictionary. For example, consider the case where we have a model with a `MULTIPLE_INSTANCE_PER_USER` association to a user. In this case, in order to distinguish between multiple models in the takeout dictionary, we need a unique ID per model. Thus, we may export the model ID as a key for the sub-dictionaries within the takeout dictionary. To do this, we would assign the model ID an export policy of `EXPORTED_AS_KEY_FOR_TAKEOUT_DICT`.
  * `NOT_APPLICABLE`: The indicated field is not exported as part of the takeout dictionary. This should only be done when we have a reason to not export the property, such as with internal user IDs.

    For example, if we want to export all the properties of our example User model except the ID, we would have:

    ```python
    @staticmethod
    def get_export_policy() -> Dict[str, base_models.EXPORT_POLICY]:
        return {
            'id': base_models.EXPORT_POLICY.NOT_APPLICABLE,
            'username': base_models.EXPORT_POLICY.EXPORTED,
            'user_is_admin': base_models.EXPORT_POLICY.EXPORTED,
        }
    ```

#### Export data

If a model has a [takeout policy](#takeout-policy) that results in exporting data from the model, the model class needs to provide an `export_data(user_id)` static method that returns the takeout dictionary for the model. This dictionary should follow the structure specified by the takeout policy.

For instance, our example User model had a takeout policy indicating that the `username` and `user_is_admin` properties should be exported. Therefore, its `get_data()` function might look like this:

```python
@staticmethod
def export_data(user_id) -> Dict[str, Union[str, bool]]:
    user = User.query().filter(User.id == user_id).get()
    assert user
    return {
        'username': user.username,
        'user_is_admin': user.user_is_admin,
    }
```

#### Map property names to takeout keys

By default, the key in the takeout dictionary will have the exact same name as the property. For example, a field named `asdf` is by default exported as `asdf`. However, there are cases where we want to rename a field for the sake of clarity in the takeout dictionary. For example, instead of exporting date properties (such as `last_updated`) unchanged, we append `_msec` to the ends of their names to make it clear to a user that the data they are viewing is represented as time since the Epoch.

To support this, models can optionally provide a static `get_field_names_for_takeout()` method that returns a dictionary mapping from property names to the corresponding names in the takeout dictionary.

For example, suppose we have a model with the property `date_created`, but when we create the takeout dictionary in `export_data()`, we use the key `date_created_msec`. Then we would provide the following function:

```python
@staticmethod
def get_field_names_for_takeout() -> Dict[str, str]:
    return {
        'date_created': 'date_created_msec',
    }
```

Further, we also use this for when we want to hide user IDs, often by replacing the user ID with the username. For example, suppose we wanted to replace the value of the `parent_id` property with the value of the `parent_username` property. Then we would include `'parent_id': 'parent_username'` in the mapping.


#### Has reference to user ID

For models that store references to user IDs, we sometimes want to check whether a particular model has a reference to a particular user ID. One important example is wipeout, where we want to find all the models associated with a user's account so we can follow their deletion policies.

To support this functionality, every model that does not have a deletion policy of `NOT_APPLICABLE` should provide a `has_reference_to_user_id(cls, user_id)` class method that returns `True` if any of the properties of any instances of the model contain `user_id`. Otherwise, it should return `False`. Here's an example for our User model:

```python
@classmethod
def has_reference_to_user_id(cls, user_id):
    return cls.query().filter(User.id == user_id).count() > 0
```

Note that in this example we only have to check the `id` property because the `username` and `user_is_admin` properties aren't going to store user IDs.

#### Apply deletion policy

If a model's [deletion policy](#deletion-policy-for-wipeout) specifies that it should be deleted (`DELETE` or `DELETE_AT_END`), the model class must provide an `apply_deletion_policy(cls, user_id)` class method that deletes all the entities of this model that in any field reference `user_id`. (The [`has_reference_to_user_id()` method](#has-reference-to-user-id) may be helpful for this!)

For our User model, we could do something like this:

```python
def apply_deletion_policy(cls, user_id):
    for user in User.query().filter(User.id == user_id):
        user.delete()
```

Note that after you write `apply_deletion_policy()`, you have to make sure it is called by the [wipeout service](https://github.com/oppia/oppia/blob/develop/core/domain/wipeout_service.py).

#### Pseudonymizable models

Pseudonymization is not handled by the model classes. Instead, it's handled in [`wipeout_service.py`](https://github.com/oppia/oppia/blob/develop/core/domain/wipeout_service.py). See that file and our [[wipeout wiki page|Wipeout-implementation]] for details.

## Common procedures

### Create a new model class

1. Decide if you want a [versioned or an unversioned model](#model-versioning). Based on your decision, create the model following the [naming conventions ans structure](#naming-conventions-and-structure) and with the correct superclass (`VersionedModel` or `BaseModel`).

   Note that if you add a new module for your model class, you'll need to add support for it in our [GAE datastore interface implementation](#the-gae-datastore-interface-implementation).

2. Add properties to the model. Refer to the [GAE datastore interface implementation section above](#gae-datastore-interface-implementation) for details on what properties are available.
3. Specify your model's [deletion policy](#deletion-policy-for-wipeout) and [takeout policy](#takeout-policy).
4. Provide a [`has_reference_to_user_id()` method](#has-reference-to-user-id) if required.
5. If the deletion policy is:

   * `DELETE` or `DELETE_AT_END`: Provide a function to [apply the model's deletion policy](#apply-deletion-policy).
   * `LOCALLY_PSEUDONYMIZE` or `PSEUDONYMIZE_IF_PUBLIC_DELETE_IF_PRIVATE`: You will need to know the context of this model and do the pseudonymization in a wipeout service. See [Adding pseudonymizable models](#adding-pseudonymizable-models) below for more information.

6. If the takeout policies will result in any data export, add a method to [export user data](#export-data).
7. Optionally [provide a mapping from property names to takeout dictionary keys](#map-property-names-to-takeout-keys).
8. [[Add a validator for the model|Writing-Validators-for-storage-models]].
9. **Important:** If this model relates to other models, then make sure that when the other models are deleted, this model is also deleted.

   For example, if this model exists for every exploration, then when `ExplorationModel` gets deleted, we want this model to be deleted also. In this example, the `ExplorationModel.delete_explorations` method should be modified to delete your new model.

   Add tests that verify that this deletion works correctly!

10. Write [[backend tests|Backend-tests]] for your new model.

### Add a pseudonymizable model

1. Check whether the new model is already connected to some existing model or set of models. For example, when you add a model that is supposed to track statistics for a feedback thread, it would be connected to `GeneralFeedbackThreadModel`.

   * If your new model is connected to an existing model, find where the existing model is handled in [wipeout_service.py](https://github.com/oppia/oppia/blob/develop/core/domain/wipeout_service.py). Wherever the existing model is handled, you should update the code to also handle your new model.

     Continuing with the example above, the new feedback model would need to be included in the `_pseudonymize_feedback_models()` function.

   * If your new model is not connected to an existing model, create a new function in the wipeout service that will handle the pseudonymization. You can take a look at the existing pseudonymization functions like `_pseudonymize_feedback_models()` or `_pseudonymize_activity_models_without_associated_rights_models()` for inspiration.

2. If the model has a deletion policy of `PSEUDONYMIZE_IF_PUBLIC_DELETE_IF_PRIVATE`, make sure that, for private models, the whole model is actually deleted and not just pseudonymized. This should be done in deletion functions that are usually placed in the model services files. For example, explorations are deleted by a `delete_exploration()` function in [exp_services.py](https://github.com/oppia/oppia/blob/develop/core/domain/exp_services.py)).

3. Make sure to add tests for the newly-added model in [wipeout_service_test.py](https://github.com/oppia/oppia/blob/develop/core/domain/wipeout_service_test.py). The tests are structured as follows: for each storage module, there are two test classes, one for deletion and the other for verification. Add new test methods for your newly-created model to both classes.

### Modify a model field

#### Add an index to a field

If you need to index a field (i.e., add `indexed=True` to the field constructor), you'll need to also build the index manually in the production datastore. This can be done by a simple MapReduce job that iterates over all the models and, without any modification, puts them again in the datastore.

Once you have gotten a PR with your job merged, you'll need to [[submit the job to be tested on the backup server|Running-jobs-in-production]].

#### Remove an old field from a model

Prepare for removal in the next release:

1. Move the field to the bottom of the list of fields, and mark it with a comment saying:

   ```python
   # TODO(#XXXX): DEPRECATED in <version>. Do not use.
   ```

2. If the field was previously set as required, set it to be optional instead.

3. Create an issue for proper removal of the field in next release.

Actually remove the field:

1. Remove the field from the storage model code.

2. Add a migration job to remove the field from existing models.

3. If the model inherits from `VersionedModel`, add a `_reconstitute()` method for the model that will ensure that, when we revert to an older version of the model, we properly remove the field so that the model can be loaded. To see an example, take a look at the `_reconstitute()` methods in `CollectionRightsModel` and `ExplorationRightsModel` [here](https://github.com/oppia/oppia/blob/7623cd028d15a6326cac186f673f368dcae30929/core/storage/exploration/gae_models.py#L403-L440)

4. Create a PR and [[submit the job to be tested on the backup server|Running-jobs-in-production]].

## Contact

If you have any questions about Oppia's storage models, please reach out to @vojtechjelinek (vojtech.jelinek@hey.com).
