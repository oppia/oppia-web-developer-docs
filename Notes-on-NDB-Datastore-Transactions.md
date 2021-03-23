
## What is a transaction?

A transaction is an operation or set of operations that is atomic -- either all of the operations in the transaction occur, or none of them occur. An application can perform multiple operations and calculations in a single transaction.

  

## How to identify and use transactions?

In the Oppia codebase, you can find transactions used in several places. Some examples are updating exploration statistics and user ratings, sending emails, and in MapReduce jobs.

  

When a function needs to be run as a transaction, use the annotation `@transaction_services.run_in_transaction_wrapper` above the function.

  
![transactions](https://user-images.githubusercontent.com/11008603/112216277-544f9380-8c47-11eb-9a26-7349e6036e75.png)
  

  
Search for this annotation in the codebase for more examples.

  

The maximum number of models that can be operated on is limited to 25, so for example you can put_multi at max 25 models in one NDB datastore transaction (see [source](https://cloud.google.com/datastore/docs/concepts/cloud-datastore-transactions)). If you need to operate on more than 25 models, look into [core/domain/wipeout_service.py](https://github.com/oppia/oppia/blob/7d43d0b1ef231d5b335ef413484cfce3ff660d26/core/domain/wipeout_service.py#L645-L683). In general, always write code to be rerunnable so that if one run fails, the subsequent run can take over and complete the task.
