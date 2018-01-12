When creating a queue, you need to specify the following attributes:

1) QueueName: Name of the queue

2) CreateTime: Creation time of the Queue

3) LastModifyTime: The last time when Queue attributes are modified.

4) PollingWaitSeconds: The number of waiting seconds for the messages to be received when using long-polling. When you are waiting for a response using long polling, a message consumption request will only return a response when a valid message is obtained or a long polling timeout is occurred, which is similar to the long polling used for Ajax request. Valid values: an integer from 0 to 30 seconds. Default is 0 (second).

5) VisibilityTimeout: The visibility timeout for the queue. Valid values: an integer from 0 to 43,200 seconds (12 hours). Each Message has a default VisibilityTImeout which will be counted after a worker receives the message. If the Message cannot be handled by the Worker within timeout, it may be received and handled by another Worker. Default is 30 (seconds).

6) MaxMsgSize: The maximum message size for the queue. The limit of how many bytes a message can contain when it is allowed to be sent to the queue. Valid values: An integer from 1,024 bytes (1 KB) up to 65,536 bytes (64 KB). Default is 64 (KB).

7) MsgRetentionSeconds: The number of seconds for which the message can be retained in the queue. The message will be deleted after this time has elapsed since the message has been sent to this queue, regardless of whether the message has been pulled or not. Valid values: An integer representing seconds, from 60 (1 minute) to 1,296,000 (15 days).

8) Queue API request address: This is an access address for the subscriber to pull messages in the CMQ message queue. It should be used together with a key. You can also use the address to configure queue attributes and modify parameters.
