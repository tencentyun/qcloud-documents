You can subscribe a Topic by specifying the following attributes:

1) Enter Topic name

2) Enter Topic resource ID

3) Enter subscription name. This cannot be changed once it has been entered

4) Enter subscription terminal protocol. Options are: Queue message service, URL address

5) Subscription address. Enter URL or Queue name here. Currently, a Topic is only allowed to send messages to Queues under the same account

6) Retry strategy: The NotifyStrategy attribute of subscription. This is the retry strategy in case of errors when pushing messages to the receiving end. This strategy is enabled by default.
You can select one of the two options: a. backoff retry: Message push is retried for three times, the interval between two reties is a random value between 10s and 20s. After three retries, this message will be discarded for this subscriber, with no further retries; b. exponential decay retry: Message push is retried 176 times, the total time for the retries is one day, intervals between retires are 2^0, 2^1, ..., 512, 512, ..., 512 seconds. The `exponential decay retry` strategy is checked by default. The user must check one of the two options 

7) Retry verification: (When using HTTPS) a return code of 200 indicates success

8) Add subscriber tag: When adding a subscriber, you can add FilterTag to make the subscriber receive only the messages with this filtertag. Each tag is a string with no more than 16 characters. There can be at most 10 tags for a single subscriber. The subscriber will receive the message delivered by this topic as long as one of the tags matches with the filter tag of the topic. Subscriber cannot receive messages without any tags.

9) Subscriber limit for a single Topic: Up to 100 subscribers can be associated under a single Topic

10) Total number of messages associated with the subscriber: This is an approximate value. It indicates the number of messages that are waiting to be delivered (or waiting for retry) to the subscriber, under a certain Topic
