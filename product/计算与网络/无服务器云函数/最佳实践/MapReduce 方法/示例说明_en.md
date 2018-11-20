In this tutorial, assuming that:
- You will upload some text files (such as logs, etc.) to a specific COS Bucket from time to time.
- You need to calculate the number of words for this text files.

```
Note:
1. Two COS Buckets are required. If you use the same bucket as both source and target buckets, each thumbnail uploaded to source bucket may trigger another object creation event that will again call the function, which may cause an infinite loop.
2. The function must be in the same region with COS Bucket.
```

## Implementation Overview

The implementation process for the function is as follows:

- Create function and the event source mapping of COS Bucket
- The user uploads the object to the source bucket (object creation event) of COS.
- COS Bucket detects the object creation event.
- COS calls the function and pass the event data as parameters to the function, thus publishing cos:ObjectCreated:* event to the function.
- SCF platform receives the calling request and implement the function.
- The function acquires the Bucket name and file name from the event data it received, obtains the file from the source Bucket, calculates the number of words using the wordcount implemented in the code, and save it in the target Bucket.

Note: After you finish learning this tutorial, your account will contain the following resources:

- Two SCFs: Mapper and Reducer
- Three COS Buckets: srcmr, middlestagebucket and destmr
- Notification configuration on source Bucket: Bind SCF and COS Bucket to the notification configuration of the Bucket, and add new option to identify the type of event to be triggered by COS (file creation/deletion) and the name of the function to be called. For more information about COS notification feature, please see API [PutBucketNotification](https://cloud.tencent.com/document/product/436/8588).

This tutorial is divided into two parts:

- Complete the steps required to create a function, and call the function manually using the sample COS event data. This is designed to verify whether the function works normally.
- Add notification configuration to source Bucket, to allow COS to call the function when it detects the file creation event.
