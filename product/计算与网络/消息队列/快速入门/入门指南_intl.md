Cloud Message Queue (CMQ) is a distributed message queuing service that provides a reliable message-based asynchronous communication between distributed applications or components of an application. Each message is stored in highly available and highly reliable queues. Multiple processes can read/write from/to a queue at the same time without interfering with each other.

CMQ provides four SDKs. The following is illustrated in the case of Python.

## 1. Introduction to Python SDK

For ease of use, CMQ classifies users' actions, queue operations, and topic operations into the following categories:

- Account: To encapsulate account secretId and secretKey. Users can create/delete queues, topics and subscriptions, and view these objects;
- queue: To send/receive messages and view queue setting attributes;
- topic: To publish messages and view topic setting attributes and subscribers;
- cmq_client: Users can set some attributes for connection from client to server, such as whether to enable log writing, connection timeout and persistent connection.

Please note that all the categories are non-thread-safe. If you want to use it for multi-threading, you'd better instantiate your object for each thread.


**[Click to download SDK>>](https://cloud.tencent.com/document/product/406/6107)**


## 2. Queue Model

The queue here is different from the Queue defined in the data structure. The queue in data structure must follow FIFO rule, but the distributed queue here is not strictly controlled by FIFO. (Later, we will develop dedicated FIFO products.) The latter is a container featuring high performance, high capacity and high reliability, where you can post generated messages or acquire messages for consumption. The queue is initialized with default setting attributes.

Now, let's see these attributes and their descriptions:

| Attribute | Description |
|---------|---------|
| maxMsgHeapNum | Maximum number of messages in the queue. The number of messages that can be stored in the queue, which indicates the storage and retention capabilities of the queue. |
| pollingWaitSeconds | Waiting time for messages to be received when using long-polling. Value range is 0 to 30 seconds. This time is set to specify the default waiting time for the message to be received when consuming messages. <br>For example, when the value is set to 10, it will wait 10 seconds and return if there is no message to be consumed; otherwise, it will return the acquired message immediately. <br>Note: You can also set the custom waiting time when the message is received to replace the default attribute value of the queue. | 
| visibilityTimeout | Message visibility timeout. <br>When the message is acquired by a consumer, there will be an invisibility period of time, during which other consumers cannot receive this message. Value range is 1-43200 seconds (within 12 hours). Default is 30. | 
| maxMsgSize | Maximum message length. Value range is 1024-65536 Byte (1-64 K). Default is 65536. | 
| MsgRetentionSeconds | The message retention period, that is, the message storage time in the queue. Value range is 60-1296000 seconds (1 minute-15 days). Default is 345600 (4 days). | 
| createTime | Queue creation time. A Unix timestamp will be returned (accurate to second). | 
| lastModifyTime | The time when the queue attributes were modified for the last time. A Unix timestamp will be returned (accurate to second). | 
| activeMsgNum | Total number of messages in the queue whose status is Active (i.e. not Consumed). This is an approximate value. | 
| inactiveMsgNum | Total number of messages in the queue whose status is Inactive (i.e. being consumed). This is an approximate value. | 
| rewindSeconds | The maximum rewind time for messages in the queue. Value range is 0-43200 seconds. 0 means message rewind is disabled. | 
| rewindmsgNum | Number of messages that has been deleted by calling the DelMsg API but are still within the rewind time. | 
| minMsgTime | Minimum time for messages to be in the "not consumed" status (in seconds). | 
| delayMsgNum | Number of delayed messages. | 

[**View Queue Model Quick Start >>**](/document/product/406/8436)

## 3. Topic Model

The topic model is similar to the Publish/Subscribe model in the design pattern. Topic is equivalent to the one who publishes the message and the subscriber of the topic is equivalent to the observer. Topic will send the published messages to the subscribers:
    

| Attribute | Description |
|---------|---------|
| msgCount| Current number of messages in the topic (number of retained messages). |
| maxMsgSize | Maximum message length. Value range is 1024-65536 Byte (1-64 K). Default is 65536. |
| msgRetentionSeconds | The maximum available time of the message in the topic (in seconds). Whether or not the message has been retrieved after being pushed to the users, it will be deleted after the period of time specified in this parameter. This parameter value is always one day (86,400 seconds) and cannot be modified. |
| Topic creation time | A Unix timestamp will be returned (accurate to second). |
| lastModifyTime | The time when the topic attributes were last modified. A Unix timestamp will be returned (accurate to second). |
| filterType | Specify the filtering rules when a user creates a subscription: <br> If filterType =1, filterTag is used for tag filtering;<br>If filterType =2, bindingKey is used for filtering. |

[**View Topic Model Quick Start >>**](/document/product/406/8437)
