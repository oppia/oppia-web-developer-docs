# Oppia-ml Extension
 
[Oppia-ml](https://github.com/oppia/oppia-ml/) is developed and maintained by Oppia developers. It allows Oppia to train machine learning models so that Oppia can provide better answers to learners. Oppia-ml is developed in its own [repo](https://github.com/oppia/oppia-ml/), separate from Oppia.
 
## Communication with Oppia
Oppia-ml communicates with Oppia over the network for fetching job requests and storing result of job requests.
 
#### The following url handler is used for fetching job requests:
```
/ml/trainingjobhandler
```
* **Request data**: above handler requires following JSON data in the request:
    ```
    {
        ‘vm_id’: a unique ID assigned to VM.
        ‘signature’: digital signature for authenticity of VM.
    }
    ```
* **Response data**: above handler returns following JSON data in the response:
    ```
    {
        ‘job_id’: a unique ID using which Oppia can distinguish different jobs.
        ‘algorithm_id’: an ID using which Oppia-ml can identify the type of classifier to be trained.
        ‘training_data’: training data using which classifier will be trained.
    }
    ```
 
#### The following url handler is used for storing the result of job request:
```
/ml/trainedclassifierhandler
```
* **Request data**: Above handler requires following JSON data in the request:
    ```
    {
        ‘vm_id’: unique ID assigned to Oppia-ml instance.
        ‘message’: The dict that contains job_id and classifier_data, using which signature is generated.
        ‘signature’: digital signature for authenticity of VM.
    }
    ```
     
* **Response data**: It returns HTTP 200 in response if “classifier_data” has been saved successfully.


These URLs are defined in the [`oppia-ml/vmconf.py`](https://github.com/oppia/oppia-ml/blob/develop/vmconf.py) and [`oppia/feconf.py`](https://github.com/oppia/oppia/blob/develop/feconf.py) files. They must match the above ones, otherwise Oppia-ml will not be able to work with Oppia.


## How to try your own algorithms.
The new oppia-ml project allows developers to try out their own ML algorithms for classification. The steps that need to be followed for using a new algorithm:

- Extend BaseClassifier in the oppia-ml repo and implement all its base functions for your chosen classifier.
- It is very important to add your algorithm to the Interaction-Classifier mapping. Without this step, your algorithm won't be functional.
- Implement a front-end service that will be called by the PredictionAlgorithmRegistryService. This service should have a predict() method which returns the predicted labels given user responses and classifier model.