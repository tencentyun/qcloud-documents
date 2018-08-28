You can write an SCF to process the object creation and deletion events in a COS Bucket. COS publishes events to the SCF and call the function using the event data as parameters. You can add the bucket notification configuration in the COS Bucket, which identifies the type of an event that can trigger a function, the name of a function to be called, and other information. For more information, please see the API [PutBucketNotification](https://cloud.tencent.com/document/product/436/8588).

COS trigger has the following features:

- **Push model**: COS monitors the specified Bucket action (event type) and calls a relevant function to push event data to the SCF. Use the Bucket notification in the push model to store the event source mapping of COS.
- **Asynchronous call**: COS always calls the function asynchronously, and does not return the result to the caller. For more information about call types, please see [Call Types](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B).

## Attributes of COS Trigger

- (Required) COS Bucket: Configured COS Bucket. Only the COS bucket in the same region is supported.
- (Required) Event type: "File Upload" and "File Deletion" are supported to determine when the trigger triggers the function. For example, if "File Upload" is selected, the function is triggered when a file is uploaded to the COS Bucket.

## Use Limits of COS Trigger

To prevent errors in COS event generation and delivery, COS sets a limit to bind only one function that can be triggered to each event (such as file upload/file deletion) in a bucket. Therefore, when you create a COS trigger, do not bind multiple function triggers to the same event of the same COS Bucket.

COS trigger supports triggering SCF with COS Bucket events in the same region, that is, when you configure a COS trigger for an SCF created in Guangzhou region, you can only choose a COS Bucket in the Guangzhou region (South China). To trigger an SCF with COS Bucket events in the specified region, you can create a function in this region.

## Event Message Structure of COS Trigger

When an object creation or object deletion event is generated in the specified COS Bucket, COS sends the following event data in JSON format to the bound SCF.

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

The data structure is described as follows:

| Name | Content |
| ---------- | --- |
| Records | List structure. Multiple messages may be merged into the list |
| event       | Records event information, including event version, event source, event name, time, queue information |
| cos | Records the COS information of the event |
| cosBucket | Records the bucket of the specific event, including bucket name, region, user APPID |
| cosObject | Records the object of the specific event, including object path, size, custom metadata, access URL |
| subscriptionName | Records the subscription name of SCF under the topic |

