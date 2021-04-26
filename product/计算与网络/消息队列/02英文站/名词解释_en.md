
This section describes the basic attributes, and the identifiers of queues and messages of Tencent Cloud CMQ queues.

## 1. Message Related Terms
| Term | English | Description | 
|---------|---------|---------|
| Message | Message | Content that needs to be passed between different processes, including data and attributes |
| Message ID | Message ID | Each message will receive a system assigned message ID, which is useful for identifying messages |
| Message handle | ReceiptHandle | Users will get a message handle that can operate the message, when reading the message from the messaging service queue. <br><br>Users can use the message handle to delete the message or modify some attributes of the message. The message handle is associated with the operation of receiving the message, instead of the message itself. The message handle instead of the message ID must be provided when deleting or modifying the message. This means that you must always receive the message before modifying/deleting it. <br><br>The message handle provided by Tencent Cloud CMQ has a time limit, which will become invalid after the time set by users (default is 30 seconds, or you can customize the time). <br><br>The message handle with a time limit provided by Tencent Cloud CMQ can effectively avoid data misoperation, and also help users greatly reduce the risk brought by handle leaks |
| Producer | Producer | The role that sending messages to CMQ's messaging service |
| Consumer | Consumer | The role that getting messages from CMQ's messaging service |

## 2. Queue Related Terms
| Term | English | Description | 
|---------|---------|---------|
| Queue | Queue | The destination that stored the message. The consumer will obtain messages from here. The message will be uniquely identified using MessageId or ReceiptHandle in a queue |
| Topic | Topic | The destination and storage address of the publishing message, automatically sent to all consumers with requirements |
| Request | Request | Content sent to the queue when consumers obtain messages from the queue |
| Message-receiving model | Message-receiving model | The way that consumers obtain messages. Currently, it only supports the PULL model that consumers obtain messages actively. The PQH model that CMQ push messages actively will be supported later |
| Active messages | Activemessages | Total number of messages in the queue whose status is Active (approximate value) |
| Inactive messages | InactiveMessages | Total number of messages in the queue whose status is Inactive (approximate value) |
| Long Polling | Long Polling | With long polling, a message consumption request will only return a response when a valid message is obtained or a long polling timeout is occurred, avoiding repeated and invalid pollings |
| Polling waiting time | PollingWaitSeconds | Maximum waiting time for polling timeout (in seconds). The valid value​ranges from 0 to 30 seconds. |
| Maximum message size | MaxMsgSize | The maximum size (in byte ) of the message body allowed to be sent to this queue. Valid value range is 1024-65536, i.e. 1K-64K |
| Message lifecycle| msgRetentionSeconds | The number of seconds for which the message can be retained in the queue. The message will be deleted after this time has elapsed since the message has been sent to this queue, regardless of whether the message has been pulled or not. Valid values: An integer representing seconds, from 60 (1 minute) to 1,296,000 (15 days). |
| Total number of messages consumed | DequeueCount| Total number of messages consumed in the queue |
| First consume time | FirstDequeueTime| Time when a message in the queue is consumed for the first time |
| Message body | Message Body| Received message body. The default sending and receiving encoding of Tencent Cloud message is base64, which is consistent with the official SDK of Message Service. |
| Message digest | MsgBodyMD5 | Check whether the information is being tampered with when using it |
| Visibility timeout | VisibilityTimeout | This message may be received and processed by other people if the message is not processed within this time after the message is received. Valid values: an integer from 0 to 43,200 seconds (12 hours). The time will be counted after the message is received |
| Next visible time of message| NextVisibleTime | Time when a received message can be consumed again when the VisibilityTimeout is set |

## 3. Topic Related Terms
| Term | English | Description | 
|---------|---------|---------|
| Subscriber | Subscriber | The subscriber to a service in CMQ-topic mode |
| Produce	| Produce	| The process where producer writes messages into topic |
| Deliver	| Subscription	| The process where topic delivers messages to the subscriber |
| Message-receiving model (PUSH) |	Message-receiving model (PUSH) | TOPIC model of CMQ; PUSH mode (active pushing) is supported already |
| Retry strategy	| NotifyStrategy	| NotifyStrategy attribute of subscription, that is, the retry strategy used when an error occurs during the pushing of message to the receiver. This strategy is enabled by default. There are two options, out of which only one is allowed: a. backoff retry: retry three times, with the interval being a random value between 10s and 20s; after retry three times, the message will be discarded for the subscriber, and no retry will be made any more; b. Decay exponential retry: retry 176 times with the total retry time being 1 day and the internals being 2^0, 2^1, ..., 512, 512, ..., 512 seconds in turn. Decay exponential retry strategy is checked by default. One option must be selected from the two.
| Message lifecycle| msgRetentionSeconds |The number of seconds for which the message can be retained in the TOPIC. The message will be deleted after this time has elapsed since it is sent to the queue, regardless of whether the message has been pulled or not. Default value is 86400s (one day) and cannot be modified |
| Maximum message size | MaxMsgSize | The maximum size (in byte) of the message body allowed to be sent to this queue. Valid value range is 1024-65536, i.e. 1K-64K |
| Message heap | MessageRetentionPeriod | Enabled by default. When the message of a producer has not been triggered and delivered to the subscriber or the subscriber fails to receive the message, the message will be placed into TOPIC temporarily for multiple retries. This is not configurable and the maximum heap period is 1 day |
| Retry verification| Status code | After TOPIC is delivered to the subscriber, an https return code of 200 indicates success |
| Add subscriber tag |	FilterTag | When a subscriber is added, a FilterTag can be added; after the addition of FilterTag, the subscriber can only receive messages with this filtertag. Each tag is a string with no more than 16 characters, and a maximum of 5 tags can be added for a single subscriber. As long as one of the tags can match the filter tag of topic, the subscriber can receive the message delivered under this Topic; if the message comes without any tag, the subscriber cannot receive this type of message |
| Add message filter tag | Messagetag	| Message tag, or message type, used to differentiate message categories under Topic of a CMQ. MQ allows consumers to filer messages by tags so as to ensure that consumers will only consume the message types that are of interest to them. This feature is disabled by default. In this case, all the messages will be sent to all the subscribers. If a subscriber has set the tag, the subscriber will not receive the messages that do not match the tag. Message filter tag describes the tag for the message filtration in this subscription (only the messages with matching tags will be pushed). Each tag is a string with no more than 16 characters, and a maximum of 5 tags can be added for a single message.
| Enable log trace |	LoggingEnabled | Whether to enable log management function. True: enable; False: disable. When it is enabled, the original log of CMQ will be written into COS (Cloud Object Storage). And user can perform LOG aggregation query through the CMQ console to eliminate the need of building an analysis system independently |

