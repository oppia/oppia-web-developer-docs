When writing backend functions, it is good to keep in mind the effect that the written function has on an end user who is using a feature that calls that particular function, particularly the speed. 

If a lot of database requests are required in the backend, it can lead to slowdown for the end user. Hence, it is best to keep the total number of database requests to a minimum on any new function that is written in the backend, as much as possible.

Try to use the `get_multi` function if the keys of all the models to be fetched are known beforehand or `get_all` to fetch every database entry for a class, though even this one, use only if it's absolutely needed. To filter models based on other conditions, some other GAE functions can be used such as `query()` with filters.

You can refer to [this](https://github.com/oppia/oppia/blob/e7bd68feca31cd2309ba71c229094f3028ef296b/core/storage/question/gae_models.py#L202) function in the codebase for an example on how to use filters to directly fetch the required models from the datastore.

The official documentation for the `query` function can be found [here](https://cloud.google.com/datastore/docs/concepts/queries#datastore-datastore-basic-query-python). 


