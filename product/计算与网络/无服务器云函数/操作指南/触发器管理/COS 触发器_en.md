Users can write SCF to handle the object creation and deletion events in COS Bucket. COS can publish the events to SCF and call the function by using the event data as parameters. Users can add bucket notification configuration in COS Bucket. This configuration can identify the event type that can trigger a function, the name of a function to be called, and other information. For more information, please see API [PutBucketNotification](https://cloud.tencent.com/document/product/436/8588).

COS trigger has the following features:

- Push model: COS monitors specified Bucket action (event type) and call relevant function to push event data to SCF. Use Bucket notification in push model to store the event source mapping of COS.
- Asynchronous call: COS always uses asynchronous call type to call the function, and the result is not returned to the caller. For more information about the call type, please see [Call Type](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B).

## COS Trigger Attribute

- COS Bucket (Required): Configured COS Bucket. Only COS bucket under the same region is supported.
- Event type (Required): Currently, two types "File Upload" and "File Deletion" are supported to determine when the trigger triggers the function. For example, if "File Upload" is selected, the function is triggered when a file is uploaded to COS Bucket.

## Service Limit of COS Trigger
To prevent error in COS event generation and delivery, COS sets a limit to bind only one function that can be triggered to each event (such as file upload/file deletion, etc.) of each Bucket. Therefore, when you create a COS trigger, do not bind multiple function triggers to the same event of the same COS Bucket.

## COS Trigger Event Message Structure
When object creation or object deletion event is generated in a specified COS Bucket, the following form of JSON event data is sent to the bound SCF.

```
{  
   "Records":[  
      {
        "event": {
          "eventVersion":"1.0",
          "eventSource":"qcs::cos",
          "eventName":"cos:ObjectCreated:*,
          "eventTime":"1970-01-01T00:00:00.000Z",
          "eventQueue":"qcs:0:cos:gz:1251111111:cos",
          "requestParameters":{
            "requestSourceIP": "111.111.111.111",
            "requestHeaders":{
              "Authorization": "Example"
            }
          }
         },
         "cos":{  
            "cosSchemaVersion":"1.0",
            "cosNotificationId":"Configured or returned ID",
            "cosBucket":{  
               "name":"bucketname",
               "appid":"1251111111",
               "region":"gz",
            },
            "cosObject":{  
               "key":"/test.jpg",
               "size":"1024",
               "meta":{
                 "Content-Type": "text/plain",
                 "x-cos-meta-test": "Custom meta",
                 "x-image-test": "Custom meta"
               },
               "url": "Origin server URL for accessing files"
            }
         }
      }
   ]
}  
```
