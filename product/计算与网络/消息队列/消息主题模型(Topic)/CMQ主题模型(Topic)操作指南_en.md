## 1. Creating/Viewing Topic

Main Operations:

(1) Enter Topic name. Topic name cannot be changed once it has been created. Name can only contain letters, numbers, dashes (-) and underscores (_). The length of the name must be between 3-64 Bytes, the name will be truncated if it goes beyond this limit
(2) Configure region attribute of the Topic
(3) Configure the maximum length of messages (the MaximumMessageSize attribute). This determines the max length of message bodies that can be sent to this Topic. (Unit: Byte) Value range: 1024 (1 KB)-65536 (64 KB). Default is 65536.
(4) Enter notes
(5) Message life cycle: The longest time that messages will be kept in this queue. The message will be deleted after this time has elapsed since the message has been sent to this queue, regardless of whether the message has been pulled or not. (Unit: second) Default is 86400s, this value cannot be changed.
(6) Message retention: Enabled by default. When the message of a producer has not been triggered and delivered to the subscriber, or the subscriber failed to receive the message, the message will be retained into Topic temporarily
(7) Current number of retained messages: You can view the approximate number of retained messages in the details section of the topic
(8) The Qps performance of a single topic: The peak production and delivery QPS performance of a single Topic is 5000

## 2. Modifying Topic Attributes
(1) The name and resource ID of a Topic cannot be changed
(2) The region attribute of a Topic that is displayed cannot be changed
(3) The maximum length of messages can be changed. This determines the max length of message bodies that can be sent to this Topic. (Unit: Byte) Value range: 1024 (1 KB)-65536 (64 KB). Default is 65536.
(4) Creation time and last modification time cannot be changed

## 3. Adding Subscribers
(1) Enter Topic name
(2) Topic resource ID
(3) Subscription name. This cannot be changed once it has been entered
(4) Subscription terminal protocol. Options are: Queue message service, URL address
(5) Subscription address. Enter URL or Queue name here. Currently, a Topic is only allowed to send messages to Queues under the same account
(6) Retry strategy: The NotifyStrategy attribute of subscription. This is the retry strategy in case of errors when pushing messages to the receiving end. This strategy is enabled by default. You can select one of the two options: a. backoff retry: Message push is retried for three times, the interval between two reties is a random value between 10s and 20s. After three times, this message will be discarded for this subscriber, with no further retries; b. exponential decay retry: Message push is retried 176 times, the total time for the retries is one day, intervals between retires are 2^0, 2^1, ..., 512, 512, ..., 512 seconds. The exponential decay retry strategy is checked by default. The user must check one of the two options 
(7) Retry verification: (When using HTTPS) a return code of 200 indicates success
(8) Add subscriber tag: When adding a subscriber, you can add FilterTag to make the subscriber receive only the messages with this filtertag. Each tag is a string with no more than 16 characters. There can be at most 10 tags for a single subscriber. The subscriber will receive the message delivered by this topic as long as one of the tags matches with the filter tag of the topic. Subscriber cannot receive messages without any tags.
(9) Subscriber limit for a single Topic: Up to 100 subscribers can be associated under a single Topic
(10) Total number of messages associated with the subscriber: This is an approximate value. It indicates the number of messages that are waiting to be delivered (or waiting for retry) to the subscriber, under a certain Topic

## 4. Modifying/Deleting Subscribers

You can modify retry strategy, subscriber tag, message delivery format, message delivery strategy, etc.

## 5. Viewing All Subscribers of a Certain Topic
(1) Subscription name
(2) Receiver address
(3) Retry strategy
(4) Message pushing format
(5) Subscription terminal protocol
(6) Subscription address
(7) Creation time
(8) Subscription tag

## 6.(Producers) Publishing Messages to Topic
(1) Topic name
(2) Topic resource ID
(3) Published title. Customers may enter the title according to their own needs
(4) Published content: Main body of the message, customers may enter the content according to their own needs. CMQ will not encode or modify this content
(5) Add message filter tag: Tag, namely message tag, message type, is used to differentiate message categories under the Topic of a certain CMQ. CMQ allows consumers to filter messages based on the tags and thus only consume the messages that they're interested in. This feature is disabled by default. In this case, all messages will be sent to all the subscribers. If a subscriber configured a tag, the subscriber will not receive any messages because the tag doesn't match with the tag of the Topic. The message filter tag describes the tag used for message filtering for this subscription (only the messages with consistent tags will be pushed). Each tag is a string with no more than 16 characters. There can be at most 10 tags for a single message

## 7. (Topic) Delivering Messages to Subscriber (Notification)
(1) The Topic will do its best to deliver messages published by producers (notification) to subscribers
(2) If the delivery isn't successful after multiple retries, the message will be retained in Topic and wait for the next delivery. If still not successful, the message will be discarded after the maximum message life cycle (1 day) has elapsed

## 8. Topic API Access Address

This is the access address that a user will be using when the user perform operations to Topics or subscriptions (such as add, delete, modify, view or publish). The private key is required when using this address.

