RabbitMQ is the most popular open source message broker deployed at enterprise systems to meet high-consistency, high-stability and high-reliability requirements.
　　　
Based on the highly reliable RabbitMQ/AMQ, and by leveraging the Raft protocol, Tencent Cloud develops the CMQ with improved reliability, throughput and performance.

This document focuses on the reliability principle of RabbitMQ, the improvements of Tencent Cloud CMQ, and their respective performances.

## 1. Reliable Message Delivery with RabbitMQ 
### 1.1. Acknowledgements

Abnormal networks, failed servers, or program bugs may cause data loss. This problem can be resolved by acknowledging messages. If a message is acknowledged, it is verified and processed properly.
![](//mccdn.qcloud.com/static/img/163df9296d3add5dede94173a54e01df/image.png)

RabbitMQ uses message production acknowledgement and consumer acknowledgement to provide reliable delivery.

- Message production acknowledgement: The producer sends a message to MQ for acknowledgement; if not acknowledged, the producer will resend the message to MQ. This process can be done asynchronously. The producer continues sending messages, and MQ processes the messages in batch and makes acknowledgement. The producer identifies the successfully processed messages by the IDs returned upon acknowledgement.

- Consumer acknowledgement: MQ delivers a message to the consumer for acknowledgement; if not acknowledged, MQ will re-deliver the message to the consumer. This process can also be done asynchronously. MQ continues delivering messages, and the customer processes the messages in batch and makes acknowledgement.

It can be seen that RabbitMQ/AMQP guarantees "at-least-once delivery". Messages are delivered or consumed repeatedly under abnormal circumstances.

### 1.2. Message Storage

In order to improve the reliability of the message, the received messages are persistently written to the disk when RabbitMQ cannot be rebooted. When a message is received, RabbitMQ writes the message to a file. When the messages written to the file reach a certain number or the messages have been written to the file for a certain period of time, RabbitMQ will store the file in the disk.

The production message acknowledgement is made by MQ replying the stored message ID to the producer after the message is stored in the disk.

## 2. Tencent Cloud CMQ Vs. RabbitMQ

Despite the similar infrastructure principle and implementation method, CMQ excels over RabbitMQ in many aspects:
### 2.1 Strengthened Functions
In addition to production and consumption acknowledgements, CMQ also provides consumption rewind.

The user can specify Tencent Cloud CMQ to save the production message for a certain number of days, rewind the consumption to a certain point in time, and start to re-consume from that point. Time-oriented message playback is very helpful for business recovery when you encounter business logic exception.

### 2.2 Optimized Performance

| Performance Indicator| Description |
|---------|---------|
| Network IO | CMQ supports mass production/consumption of messages, while RabbitMQ does not support mass production. CMQ has fewer requests and lower average latency when dealing with large numbers of small messages. |
| File IO | CMQ makes full use of the file system cache by writing the production/consumption message to a single file sequentially and storing in the disk periodically. RabbitMQ has relatively poor performance because it has to perform three IO actions: The persistence message mechanism changes the statuses of the first input memory queues, writes the log cache, and finally writes the message files and index files (index files are written in sequence and message files are written randomly). |
| CPU performance | RabbitMQ needs to consume lots of CPU resources to cache logs and change status due to the complex algorithms. Therefore, it has relatively poor CPU performance. |

### 2.3. Enhanced Availability
Although CMQ and RabbitMQ both support hot backup using multiple servers for high availability, the Raft algorithm- based CMQ is easy to understand and maintain, while the Guaranteed Multicast-based RabbitMQ is hard to learn.

In the Raft protocol, as long as most of the nodes return success messages to Leader when copying Log, Leader can apply the request and return success message to the client:
![](//mccdn.qcloud.com/static/img/bcf3dbba73a38775779763dacf2d79d8/image.png)
　　　
Guaranteed Multicast (GM) organizes all the nodes in the cluster into a ring. Log copy spreads from Leader to the successive nodes. When Leader receives the request again, it will send the acknowledgment message in the ring until the leader receives the acknowledgment message again, thus completing the synchronization of Log in all the nodes of the ring.

![](//mccdn.qcloud.com/static/img/117c56f150966c375070977947543286/image.png)

The GM algorithm requires Log to be synchronized in all the nodes within the cluster before returning success message to the client, while the Raft algorithm requires Log to be synchronized in most of the nodes within the cluster. Raft algorithm reduces half of the waiting time than GM algorithm in synchronizing path.

### 2.4. Performance Test of CMQ and RabbitMQ

Test scenarios are as follows: Three servers with the same configuration form a cluster. Tencent Cloud CMQ and RabbitMQ are configured as mirrored queues, with the data synchronized in these three servers. Tencent Cloud CMQ and RabbitMQ both activate message production and consumption acknowledgement mechanisms. The production message size in the test is 1KB.

| Test Environment | Environment Description |
|---------|---------|
| CPU | 24-core	Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz |
| Memory | 64G |
| Disk | 12\*2T SATA	12-SATA Raid0 |
| NIC | 10G	 |
| Linux version | 2.6.32.43	 |
| RabbitMQ version | 3.6.2 |
| Erlang version | 18.3 |

Testing data:

| QPS | Production | Consumption | Production & Consumption |
|---------|---------|---------|---------|
| CMQ | Production: 68,000 counts per second (cps) | Consumption: 90,000 cps | Production: 36,000 cps <br> Consumption: 36,000 cps |
| RabbitMQ | Production: 12,500 cps | Consumption: 26,000 cps | Production: 8,500 cps <br> Consumption: 8,500 cps|

In highly reliable scenarios, the throughput of CMQ is over four times larger than that of RabbitMQ.
