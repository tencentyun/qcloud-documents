Recently, the subscription tag filtering feature has been added to the Topic mode of CMQ. It is similar to the direct_routing mode of rabbitMQ. The topic_pattern mode will be provided at the next iteration. The usage strategy of filter tags is relatively complicated. It will be explained in details below:

**Scenario 1:**Topic: test1, the subscription publishing API was called at 12:01. This operation is defined "Publish test1", after which the topic delivered 200 messages to each of the three subscribers A, B and C. Assume that A failed to receive 100 of the messages, B failed to received 30 of the messages and C successfully received all of the messages

Scenario analysis:

- Message retention: For the three subscribers A, B and C, we assume there are 110 messages that failed to be delivered (100 failed messages for A, 30 for B, none for C, the failed messages include duplicates). As long as a certain message is associated with one of the subscribers, this message will not be unsubscribed
- Block strategy: Take A as an example. The Topic delivered 200 messages to A, when the 101th message failed, the remaining 99 messages will be blocked. The status is that 100 messages failed to be received
- Retry strategy (backoff retry): Topic-test1 will re-deliver the message to A after every N seconds. The first one of the 100 failed messages will be re-delivered first, this message will be discarded after another three failed retries, after which the topic will retry the next message, so forth
- Retry strategy (exponential decay retry): Take A as an example. The Topic will deliver the 100 messages in a concurrent manner (the order of delivery is not fixed). If the first message failed to be received by the subscriber, the topic will retry from the first message. And if retry fails, this message will continue to be blocked. Newly added messages to be delivered will continue to be blocked
- Message life cycle cannot be prolonged. Assume there are 110 messages retained in topic-test1. Their life cycle is 1 day. Starting from the time point when the producer pushed these messages to the Topic, the messages will be deleted after 1 day has elapsed, no matter how many retries were committed
- Re-push: The producer keeps producing new messages into the Topic. The customer called the subscription publish API again at 12:02. Together with the 110 failed messaged previously retained, we assume that there are now 210 messages in the Topic (110 retained failed messages + 100 newly added messages within the minute), then try to deliver again. In this case, the retry strategy for A and B is exponential decay retry, and the status is "connection lost". The 210 messages will continue to be blocked. C will only receive the newly added 100 messages.

***Key point: The ID of each message is the key, and value is the associated subscribers, which indicates whether the subscribers have successfully consumed the message***


---


**Scenario 2:**Topic: test2, the subscription publishing API was called at 12:01. This operation is defined "Publish test2", after which the topic delivered 200 messages to each of the three subscribers A, B and C. Assume that all three of them successfully received all the 200 messages

Scenario analysis:

- For topic-test2, there are only three subscribers A, B and C, all of whom successfully consumed the 200 messages. In this case, the topic will immediately delete these messages

---


**Scenario 3:**Assume we have four subscribers A, B, C and D. We add tags for these subscribers: The message tag for A is "apple", B is "xiaomi", C doesn't have any configured tags, and D is "imac"+"xiaomi". Now, a producer published 100 messages to the topic, and the tags for message filtering are: apple, imac, iphone, macbook. Then the topic delivers the messages to A/B/C/D.

Scenario analysis:

- For subscriber A, "apple" matches with the message filtering tag "apple", so he/she will receive the 100 messages
- Subscriber B will not receive any messages
- Subscriber C will not receive any messages either
- For subscriber D, one of the tags "imac" matches with the filtering tag, so he/she will receive the 100 messages

---


**Scenario 4:**Assume there are only four subscribers for Topic: A, B, C and D. None of them have any tags configured. Now, a producer published 100 messages to the topic, and the tags for message filtering are: apple, imac, iphone, macbook. Then the topic delivers the messages to A/B/C/D.

Scenario analysis:

- No tags are configured for the subscribers A, B, C and D, so message filtering is not required when delivering. All of them will receive the 100 messages


---


**Scenario 5:**Assume there is only one subscriber for Topic: A. The subscription tag "xiaomi" has been configured for A. Now, a producer published 100 messages to the topic, and the tags for message filtering are: apple, imac, iphone, macbook. Then the topic delivers the messages to A

Scenario analysis:

- For subscriber A, the subscription tag does not match, thus A will not receive the 100 messages. In this case, the messages will be immediately discarded, without being retained in CMQ
- When the producer publishes messages to topic, message filtering tags can only be configured for once before publishing. The tags will then bind to the message id and can no longer be modified

---


**Summary:**

1. If there is no message tags but the subscriber has tags, the subscriber does not have a matching tag and will not receive the message
2. If the message has tags but the subscriber does not, message matching is not required and the subscriber will receive the message
3. If both the message and subscriber has tags, then the subscriber can receive the message only if there is a pair of matching tags. N:M matching is supported. For example, a message has 10 tags, a subscriber has 4 tags, there is a pair of matching tags, then the subscriber will receive the message
4. Neither the message nor the subscribers have tags. All subscribers will receive the message upon delivery

