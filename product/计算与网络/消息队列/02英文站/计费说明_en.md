The original Log of Queue/Topic is stored in COS. By default, Logging is not enabled when you create a Queue/Topic. To enable Logging, you need to create and specify a bucket for it. The Logging fee will be collected by Tencent Cloud COS. For more information, refer to [COS Billing Item Overview](https://cloud.tencent.com/doc/product/430/5871).

One message operation log is generated per minute. After being named according to a set of rules, the log will be written into a specific Bucket 

and saved as a json object for you to download and process directly.

> Note:
> 
1) There may be a delay of 15-30 minutes when CMW pushes the log to the user's Bucket

>2) As it is difficult for customers to parse original logs, CMQ provides the log trace (generated from the original log) for customers to target the problem immediately.

