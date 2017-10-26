Welcome to CMQ (Cloud Message Queue).

Tencent Cloud's Cloud Message Queue (CMQ) is a distributed message queue service used for storing messages transferred between processes. It is designed to provide reliable message-based asynchronous communication service between different applications deployed in a distributed way or between different components of an application. Messages are stored in a highly reliable and available message queue, which allows multiple processes to perform read and write operations simultaneously without interfering with each other. With Tencent Cloud CMQ, messages can be transferred, without any data loss, between distributed components of applications executing different tasks. There is no need to keep every component available at all time.

The queue acts as a buffer between the data sender and the data receiver, eliminating the problems caused by the circumstances in which the data sender works faster than the data receiver or the data sender or receiver only connects to the network intermittently.

In the traditional process communication mode, the client requests a service from the server and waits for a response from the server. Such a mode has many shortcomings, for example, the likelihood of lost request in case of poor network conditions, or failed request due to timeout caused by overlong waiting of client in case of lengthy processing of server.

To deal with these problems, Tencent Cloud introduces the CMQ service for message distribution and management. With Tencent Cloud CMQ, components of an application can be separated to run independently, and message management between the components can be simplified. Any component of a distributed application can store messages in the queue, and Tencent Cloud CMQ ensures that each message is transmitted at least once and can be read and written many times. A single queue can be used by multiple distributed application components at the same time which are not required to collaborate with each other. All the components can programmatically retrieve and operate messages using CMQ APIs.

For all the supported operations, please see [API Overview](/doc/api/431/5852).

Before using these APIs, please make sure that you have a thorough understanding of [CMQ Product Overview](https://cloud.tencent.com/doc/product/406).

**Note: Currently, collaborator account is not allowed to perform CMQ operations.**

## Queue Model

### Glossary
The key terms involved in the document are as follows:

| Term | Full Name | Chinese | Description |
|---------|---------|---------|---------|
| CMQ | Cloud Message Queue | Cloud Message Queue | Tencent Cloud CMQ includes queue models, topic model, and high-performance messaging services, etc. |
| Queue | Queue | Queue | Queue is a data model built on a "first-in-first-out" basis. Producers can concurrently add data to the tail of a queue, and consumers can concurrently pull data from the head of the queue. |
| Active | Active | Consumable (visible) | When being active, a message can be scrambled for by all the consumers, among whom only one consumer will succeeds in consuming the message. In this case, the message changes to a status of "inactive", and is invisible to other consumers. |
| Inactive | Inactive | Inconsumable (invisible) | A message with a status of "inactive" is being consumed by a consumer and other consumers cannot consume it. |
| (Batch)ReceiveMessage | (Batch) Receive Message | Consume Message | ReceiveMessage operation only changes the status of a message from "inactive" to "active" so that it cannot be consumed by other consumers. After being consumed, the message can only be deleted from the queue after (Batch)DeleteMessage operation is called explicitly. If the operation is not called, when the time specified by visibilityTimeout is up, the message will change back to the status of "active" and thus can be consumed by other consumers, leading to unexpected duplicate messages. |
| maxMsgHeapNum | Maximum Message Heap Number | Maximum number of heaped messages| In order to prevent loss of messages caused by the failure to consume the messages in time, CMA provides the message heaping function with an upper limit on the number of heaped messages. When the upper limit is reached, producers cannot add messages to the queue. After the messages are consumed and deleted, producers can add messages to the queue. |
| pollingWaitSeconds | Polling Wait Seconds | Long-Polling Waiting Time for Message Receipt | When a consumer wants to pull messages from a queue for consumption, there may not be data available in the queue. Perhaps the consumer does not want to go backn immediately (similar to the non-blocking mode) and wants to wait a while to see if some messages will come (similar to the blocking mode); pollingWaitSeconds is similar to the timeout in the blocking mode; once this time is up, the consumer must go back regardless of whether there is a message. If you want to consume a message in a non-blocking manner, set this value to 0. |
| msgRetentionSeconds | Message Retention Seconds | Message Retention Period | Messages heaped in the queue are kept within a certain time period and will be deleted from the queue if not consumed within the time limit. Once being deleted, , they cannot be consumed any longer. |
| receiptHandle | Receipt Handle | Message Receipt Handle | This handle is returned when a message is consumed. Only the handle which is currently consuming the message can be used to delete the message. If consumption is so lengthy that the visibilityTimeout is exceeded, and the message is consumed by another consumer, the handle through which the former consumer obtains the message will become invalid and cannot be used to delete the message. |
| qps throttling | QPS Throttling | qps limt | This term originally means the limit on the number of requests per second, but in practice it refers to the limit on the number of messages per second. For single-operation APIs (SendMessage, ReceiveMessage, DeleteMessage), it still refers to the number of requests per second. But for batch-opeartion APIs (BatchSendMessage, BatchReceiveMessage, BatchDeleteMessage), it is the sum of all the batch values within 1s. This limit is designed to provide users with a more consistent and fairer product. If you need to raise the limit on the number of messages, please send a request to us by submitting a [ticket](https://console.cloud.tencent.com/workorder/category). |




### Definitions of input and response parameters
- limit and offset

	> These parameters are used to control paging. For the results in a list format, if the number of entries exceeds the "limit" value, the number of returned values will be limited to the "limit" value. You can use the parameters "limit" and "offset" to control paging. "limit" indicates the maximum number of entries returned at a time, and "offset" is the offset value.
	For example, if offset = 0 & limit = 20, the 0th to the 20th entries will be returned; if offset=20&limit=20, the 20th to the 40th entries will be returned; if offset=40&limit=20, the 40th to the 60th entries will be returned, and so on.
	
- id.n

	> Format for inputting multiple parameters at a time. Multiple parameters in such a format can be input at the same time. For example:
	
	> id.0="10.12.243.21"&id.1="10.12.243.21"&id.2="10.12.243.21"&id.3="10.12.243.21"...
	
	> And so on (starting with the subscript 0).


## API Quick Start

You can use CMQ services through [CMQ SDK](https://cloud.tencent.com/product/cmq#sdk)(recommended; it is available in multiple languages) or by directly calling cloud APIs (this method is very inconvenient and is suitable for the users using a language other than SDK language):

1. Select a region and private/public network. The request domains for the CMQ APIs, unlike those of APIs of other cloud products, vary with the regions, and need to be selected based on the region. Each request domain name has a composition such as `cmq-queue-region.api.qcloud.com/v2/index.php`, where the "region" field needs to be replaced with the specific region: gz (Guangzhou), sh (Shanghai), bj (Beijing). If you are using a Tencent Cloud CVM, private network domain is preferred, otherwise a public network domain.

2. [Create a queue](/doc/api/431/5832). SDK (or cloud API) calls CreateQueue API.

3. [Send a message](/doc/api/431/5837). SDK (or cloud API) calls SendMessage (or BatchSendMessage) API.

4. [Consume a message](/doc/api/431/5839). SDK (or cloud API) calls ReceiveMessage (or BatchReceiveMessage) API.

5. [Delete a message](/doc/api/431/5840). SDK (or cloud API) calls DeleteMessage (or BatchDeleteMessage) API.

6. [Delete a queue](/doc/api/431/5836). SDK (or cloud API) calls DeleteQueue API.

## Topic Model

### Glossary
The key terms involved in the document are as follows:

| Terms | English | Description |
|---------|---------|---------|
| Subscriber | Subscriber | The subscriber to a service in CMQ-topic mode |
| Produce	| Produce	| The process where producer writes messages into topic |
| Deliver	| Subscription	| The process where messages under a topic is delivered to the subscriber |
| Message-receiving model (PUSH) |	Message-receiving model (PUSH) | TOPIC model of CMQ; PUSH mode (active pushing) is supported already |
| Retry strategy	| NotifyStrategy	| NotifyStrategy attribute of subscription, that is, the retry strategy used when an error occurs during the pushing of message to the receiver. This strategy is enabled by default. There are two options, out of which only one is allowed: a. backoff retry: retry three times, with the interval being a random value between 10s and 20s; after retry three times, the message will be discarded for the subscriber, and no retry will be made any more; b. Decay exponential retry: retry 176 times with the total retry time being 1 day and the internals being 2^0, 2^1, ..., 512, 512, ..., 512 seconds in turn. Decay exponential retry strategy is checked by default. One option must be selected from the two.
| Message lifecycle| msgRetentionSeconds |The number of seconds for which the message can be retained in the TOPIC. The message will be deleted after this time has elapsed since it is sent to the queue, regardless of whether the message has been pulled or not. Default value is 86400s (one day) and cannot be modified |
| Maximum message size | MaxMsgSize | The maximum size (in byte ) of the message body allowed to be sent to this queue. Valid value range is 1024-65536, i.e. 1K-64K |
| Message heap | MessageRetentionPeriod | Enabled by default. When the message of a producer has not been triggered and delivered to the subscriber or the subscriber fails to receive the message, the message will be placed into TOPIC temporarily for multiple retries. This is not configurable and the maximum heap period is 1 day |
| Retry verification| Status code | After messages under a TOPIC is delivered to the subscriber, an https return code of 200 indicates success |
| Add subscriber tag |	FilterTag | When a subscriber is added, a FilterTag can be added; after the addition of FilterTag, the subscriber can only receive messages with this filtertag. Each tag is a string with no more than 16 characters, and a maximum of 5 tags can be added for a single subscriber. As long as one of the tags can match the filter tag of topic, the subscriber can receive the message delivered under this Topic; if the message comes without any tag, the subscriber cannot receive this type of message |
| Add message filter tag | Messagetag	| Message tag, or message type, used to differentiate message categories under Topic of a CMQ. MQ allows consumers to filer messages by tags so as to ensure that consumers will only consume the message types that are of interest to them. This feature is disabled by default. In this case, all the messages will be sent to all the subscribers. If a subscriber has set the tag, the subscriber will not receive the messages that do not match the tag. Message filter tag describes the tag for the message filtration in this subscription (only the messages with matching tags will be pushed). Each tag is a string with no more than 16 characters, and a maximum of 5 tags can be added for a single message.
| Enable log trace |	LoggingEnabled | Whether to enable log management function. True: enable; False: disable. When it is enabled, the original log of CMQ will be written into COS (Cloud Object Storage). And user can perform LOG aggregation query through the CMQ console to eliminate the need of building an analysis system independently |

### Definitions of input and response parameters
- limit and offset

	> These parameters are used to control paging. For the results in a list format, if the number of entries exceeds the "limit" value, the number of returned values will be limited to the "limit" value. You can use the parameters "limit" and "offset" to control paging. "limit" indicates the maximum number of entries returned at a time, and "offset" is the offset value.
	For example, if offset = 0 & limit = 20, the 0th to the 20th entries will be returned; if offset=20&limit=20, the 20th to the 40th entries will be returned; if offset=40&limit=20, the 40th to the 60th entries will be returned, and so on.
	
- id.n

	> Format for inputting multiple parameters at a time. Multiple parameters in such a format can be input at the same time. For example:
	
	> id.0="10.12.243.21"&id.1="10.12.243.21"&id.2="10.12.243.21"&id.3="10.12.243.21"...
	
	> And so on (starting with the subscript 0).


## API Quick Start

You can use CMQ services through CMQ SDK (recommended; it is available in multiple languages) or by directly calling cloud APIs (this method is very inconvenient and is suitable for the users using a language other than SDK language):

1. Select a region and private/public network. The request domains for the CMQ APIs, unlike those of APIs of other cloud products, vary with the regions, and need to be selected based on the regions. Each request domain name has a composition such as `cmq-queue-region.api.qcloud.com/v2/index.php`, where the "region" field needs to be replaced with the specific region: gz (Guangzhou), sh (Shanghai), bj (Beijing). If you are using a Tencent Cloud CVM, private network domain is preferred, otherwise a public network domain.

2. [Create a topic](/doc/api/406/7405). SDK (or cloud API) calls CreateTopic API.

3. [Modify topic attributes](/doc/api/406/7406). SDK (or cloud API) calls SetTopicAttributes API.

4. [Obtain topic list](/doc/api/406/7407). SDK (or cloud API) calls ListTopic API.

5. [Obtain topic attributes](/doc/api/406/7408). SDK (or cloud API) calls GetTopicAttributes API.

6. [Delete a topic](/doc/api/406/7409). SDK (or cloud API) calls DeleteTopic API.

7. [Publish a message](/doc/api/406/7411). SDK (or cloud API) calls PublishMessage API.

8. [Publish messages in batch](/doc/api/406/7412). SDK (or cloud API) calls BatchPublishMessage API.

9. [Deliver a Messages](/doc/api/406/7420).

10. [Create a subscription](/doc/api/406/7414). SDK (or cloud API) calls Subscribe API.

11. [Obtain subscription list](/doc/api/406/7415). SDK (or cloud API) calls ListSubscriptionByTopic API.

12. [Modify subscription attributes](/doc/api/406/7416). SDK (or cloud API) calls SetSubscriptionAttributes API.

13. [Obtain subscription attributes](/doc/api/406/7418). SDK (or cloud API) calls GetSubscriptionAttributes API.

14. [Delete a subscription](/doc/api/406/7417). SDK (or cloud API) calls Unsubscribe API.







