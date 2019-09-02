### Authorizing a sub-account with all the permissions of the messaging services

A sub-account Developer under the enterprise account CompanyExample requires all the permissions of the message queue under this enterprise account. The read and write operations can be performed to the message queue regardless of whether it is based on a topic model or a queue model.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policies QCloudCmqQueueFullAccess and QCloudCmqTopicFullAccess to the sub-account Developer. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy through policy syntax.
```
 {
    "version": "2.0",
    "statement":
     {
         "effect": "allow",
         "action": ["name/cmqtopic:*","name/camqueue:*"]
         "resource": "*"
     }
}
```
Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

### Authorizing a sub-account with all the permissions of the message queue it created

A sub-account Developer under the enterprise account CompanyExample wants to assess the message queue it created.

Solution A:

The enterprise account CompanyExample directly authorizes the preset policies QCloudCmqQueueCreaterFullAccess and QCloudCmqTopicCreaterFullAccess to the sub-account Developer. For more information on how to authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

Solution B:

Step 1: Create the following policy through policy syntax.

```
{
    "version": "2.0",
    "statement":
    [
       {
           "effect": "allow",
           "action": "name/cmqtopic:*",
           "resource": "qcs::cmqtopic:::topicName/uin/${uin}/*"
       },
       {
           "effect": "allow",
           "action": "name/cmqqueue:*",
           "resource": "qcs::cmqqueue:::queueName/uin/${uin}/*"
       }
    ]
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

### Authorizing a sub-account with the read permission of the message queue with a specific topic model

The enterprise account CompanyExample (ownerUin is 1234) has a message queue based on the topic model, and a sub-account Developer who wants to access the message queue.

Step 1: Create the following policy through policy syntax.
```
{
    "version": "2.0",
    "statement":   
     {
        "action": "name/cmqqueue:SendMessage",
        "resource":"qcs::cmqqueue:::queueName/uin/1234/test-caten",
        "effect": "allow"
     } 
}
```

Step 2: Authorize the policy to the sub-account. For more information on authorization, please see [Authorization Management](https://cloud.tencent.com/document/product/378/8961).

