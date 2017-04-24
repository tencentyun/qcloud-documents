When creating a Topic, users need to specify the following attributes:

1) Enter Topic name. Topic name cannot be changed once it has been created. Name can only contain letters, numbers, dashes (-) and underscores (_). The length of the name must be between 3-64 Bytes, the name will be truncated if it goes beyond this limit

2) Configure region attribute of the Topic

3) Configure the maximum length of messages (the MaximumMessageSize attribute). This determines the max length of message bodies that can be sent to this Topic. (Unit: Byte) Value range: 1024 (1 KB)-65536 (64 KB). Default is 65536.

4) Enter notes

5) Message life cycle: The longest time that messages will be kept in this queue. The message will be deleted after this time has elapsed since the message has been sent to this queue, regardless of whether the message has been pulled or not. (Unit: second) Default is 86400s, this value cannot be changed.

6) Message retention: Enabled by default. When the message of a producer has not been triggered and delivered to the subscriber, or the subscriber failed to receive the message, the message will be retained into Topic temporarily

7) Current number of retained messages: You can view the approximate number of retained messages in the details section of the topic

8) The Qps performance of a single topic: The peak production and delivery QPS performance of a single Topic is 5000
