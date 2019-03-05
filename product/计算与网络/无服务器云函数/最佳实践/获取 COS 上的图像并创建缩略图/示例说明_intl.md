In this tutorial, assuming that:
- A user is going to upload a photo to a specific COS Bucket
- You need to create a thumbnail for every image uploaded by the user
- Save the created thumbnails in another COS Bucket

```
Notes:
1. Two COS Buckets are required. If you use the same bucket as both source and target buckets, each thumbnail uploaded to the source bucket may trigger another object creation event that will again call the function, which may cause an infinite loop.
2. The function must be in the same region with COS Bucket.
```

## Implementation Overview

The implementation process of the function is as follows:

- Create the function and the event source mapping of COS Bucket
- A user uploads the object to the source bucket (object creation event) of COS.
- COS Bucket detects the object creation event.
- COS calls the function and passes the event data to the function in parameters, thus publishing the cos:ObjectCreated:* event to the function.
- The SCF platform receives the call request and runs the function.
- The function acquires the Bucket name and file name from the received event data, obtains the file from the source Bucket, and uses the graph database to create a thumbnail, and then saves it in the target Bucket.

Note: By the time you finish this tutorial, your account will contain the following resources:

- A SCF used to create thumbnails.
- Two COS Buckets: <example> and <exampleresized> (the COS Bucket name you specify. For example, if you use the Bucket named "example" as the source bucket, you will create "exampleresized" as the target Bucket)
- Notification configuration on the source Bucket: Bind SCF and COS Bucket to the notification configuration of the Bucket, and add a new option to identify the type of the event to be triggered by COS (file creation/deletion) and the name of the function to be called. For more information about COS notification features, please see API [PutBucketNotification](https://cloud.tencent.com/document/product/436/8588).

This tutorial is divided into two parts:

- Complete the steps required to create a function, and call the function manually using the sample COS event data. This is designed to verify whether the function works normally.
- Add notification configurations to the source Bucket to allow COS to call the function when it detects a file creation event.

