The best solution to duplicate messages is to change the duplicate messages to a different ones directly.(repeated message consumption has no impact on the service). If it is not allowed to change duplicate messages, you should remove them on the consumer side.

## Ⅰ. Causes for Duplicate Messages

![](//mc.qcloudimg.com/static/img/821719ad41adc3c8e8de2473e6f3fbf5/image.png)


Messages may be lost due to network exception, server crash, etc. To avoid losing message and ensure reliable delivery, CMQ applies the message production and consumption acknowledgement mechanisms.

**Message production acknowledgement:** the producer sends a message to CMQ for acknowledgement; CMQ persists the message to disk, and then returns the acknowledgement to the producer. Otherwise, the producer needs to resend the message to CMQ in cases such as the producer request timeout, CMQ return failure.

**Consumer Acknowledgement:** CMQ delivers the message to the consumer and set it to invisible; during the invisibility period, the consumer uses the handle to delete the message. If the message is not deleted within the invisibility period, it will become visible again.

Since the message acknowledgement mechanism guarantees "at-least-once delivery", the producer/consumer may produce/consume repeatedly in cases such as network jitter, producer/consumer exceptions.


## Ⅱ. How to Remove Duplicates
You should identify duplicate messages before you remove the duplicates. A common method is to insert a Remove Duplicates key in the message body during production for consumers to identify the duplicates via the Remove Duplicates key. The Remove Duplicates key is a unique value composed of <Producer IP + Thread ID + Timestamp + Incremental Value within the Time>.

If there is only one consumer, you can store the consumed Remove Duplicates key in cache (such as KV), and check if the Remove Duplicates key is consumed for each consumption. The Remove Duplicates key cache expires based on the maximum validity period of message. You can use the minimum unconsumed message time (min_msg_time) of the queue provided by CMQ, as well as the maximum retry time for producing message provided by service, to identify when the cache expires.
If there are multiple consumers, a distributed Remove Duplicates key cache should be used.

•	Calculate the expiration time of the key based on the maximum validity period of message:
current_time - max_retention_time - max_retry_time - max_network_time

•	Calculate the expiration time of the key based on the minimum unconsumed message time of CMQ:
min_msg_time - max_retry_time - max_network_time


**Notes:**
![](//mc.qcloudimg.com/static/img/dbff4055c9fa8a10160ff59a830c016c/image.jpg)


CMQ provides a maximum message validity period of 15 days to meet the demands of different services.
All messages before the minimum unconsumed message time of CMQ Queue (the furthest point of time in the figure above) are deleted, and the messages after that may not.


## Ⅲ. Examples
**To avoid duplicate submission:**

Scenario: A is a producer, B is a consumer, and CMQ is a broker. A transferred 10 CNY to B and sent the message to CMQ. CMQ successfully received the message, but failed to response to client A due to a flash of interruption or client A crash. A thought the request failed and re-produced the message, resulting in duplicate submission.

Solution: A adds information like timestamp when producing messages, to generate a unique Remove Duplicates key. If, due to network failures, current delivery failed, producer A will re-send the message, and consumer B will use the previous Remove Duplicates key to remove the duplicates.
(The case also illustrates that the message ID of CMQ cannot be used for removing duplicates, because the two messages have different IDs but the same body.)

Note that before sending messages, producer A should persist the Remove Duplicates key to disk, to avoid loss due to power failure.

**To avoid messages with the same body from being filtered out:**

Scenario: A transferred 10 CNY to B and sent 5 requests with the same body. If consumer B removes the duplicates based on body, B will deal with 1 request instead of 5 requests.

Solution: A adds information like timestamp when producing messages. In such case, even if A repeatedly sends the same message, different Remove Duplicates keys will be generated, which allows removing duplicate messages with the same body.


