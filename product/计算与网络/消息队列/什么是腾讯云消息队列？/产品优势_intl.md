Compared with various open source message queue products, CMQ has the following advantages:

## Advantages over Kafka

1. **Kafka is not suitable for core financial business:** CMQ features synchronous flush mechanism, ensuring reliable generation of data. If messages generated on the client are flushed to the disk by over half of brokers in "set", the acknowledgement will be returned to notify that messages are generated successfully. If the client does not receive the acknowledgement within a certain period, the messages will be resent to ensure that messages are sent successfully. However, Kafka features asynchronous flush, that is, asynchronous replication, which may lead to message lost. Therefore, Kafka cannot ensure reliable delivery of messages.

2.	**If a consumption failed, Kafka cannot try it again:** For example, a top-up failure may be caused by high pressures on the operator gateway called by a top-up application; but if the application recalls the gateway later, the consumption may succeed. This is also required when deducting money from bank accounts using Alipay. The retry needs to be reliable, which means a failure and retry message will not be lost if a consumer crashes. CMQ can retry the consumption several times.

3. **Compared with the message trace by CMQ, locating problem is cumbersome in Kafka:** Message trace refers to the complete link information such as when and where the producer sends the message to the consumer and the consumer consumes the message. It is used to quickly locate the problems in financial businesses.

## Advantages over RabbitMQ

1. **Higher QPS in CMQ:** In highly reliable scenarios, the throughput of CMQ is over four times larger than that of RabbitMQ in equivalent physical devices. The QPS of a single cluster is over 100,000.

2. **RabbitMQ does not support message rewind:** RabbitMQ does not support message rewind. But CMQ can rewind messages by time. For example, CMQ can re-consume messages sent after a certain time point of the previous day. A typical application scenario for message rewind is the order analysis of a consumer. For example, if all messages consumed today become invalid due to failures of program logic or dependent system, the messages sent after 00:00 of the previous day need to be re-consumed. At this time, time-oriented message playback is very helpful for business recovery

3. **Comparison of consistency algorithms:** Although CMQ and RabbitMQ both support hot backup using multiple servers for high availability, the Raft algorithm- based CMQ is easy to understand and maintain, while the Guaranteed Multicast-based RabbitMQ is hard to learn.

4. **Great difficulty with RabbitMQ O&M:** The programming language of RabbitMQ is Erlang, which is not common and costs more to study.

## Advantages over RocketMQ

1. **Data may be lost in RocketMQ in extreme cases:** RocketMQ can return acknowledgment to the client when flush is not made. In this way, messages will be lost if the server crashes.

2. ** Multiple masters and slaves are required in RocketMQ to ensure highly availability of services:** When there is no surviving node in ISR, RocketMQ cannot ensure the availability and reliability, leading to higher cost.

Therefore, compared with traditional open source MQ applications, Tencent Cloud CMQ has the following advantages:

| | Tencent Cloud CMQ | Open Source Message Broker | 
|---------|---------|---------|
| High Performance | Featuring both high performance and high reliability. The QPS of a single CMQ instance is up to 5,000 | Featuring either high data reliability or high performance |
| High Scalability | High scalability in number of queues and queue storage capacity<br><br>The underlying system can perform auto scaling according to the business scale and the upper layer service will not be affected<br><br>CMQ can efficiently send, receive, push and retain over hundreds of millions messages. There is no upper limit to the capacity<br><br>Services are available in multiple regions including Beijing, Shanghai and Guangzhou | Limited number of queues and retained messages<br><br>Each IDC must be redeployed with the purchased devices, which is very complex |
| High Reliability | Based on CRMQ (Cloud Reliable Message Queue), the distributed architecture independently developed by Tencent Cloud, CMQ has been widely applied in Tencent's services such as Red Packet in QQ and WeChat and lottery<br><br>When each message is returned to users and written, the message service ensures that 3 copies of the data has been generated and written into different physical machines. In addition, the backend data replication mechanism provides rapid data migration when any physical machine fails and guarantees that there are always three copies of user data available. The reliability is up to 99.999999%<br><br>The improved Raft consistency algorithm is used to ensure strong consistency of data<br><br>Guaranteed service availability: 99.95% | Data is stored on a single server or servers with simple master-slave structure. In this way, data SPOF problem may occur so that data cannot be rewound once lost<br><br>Open source Replicia algorithm is used. Adding or deleting a server node will cause the rebalancing of global data, leading to a sharp decline in availability<br><br>For example, Kafka cannot guarantee strong consistency of data by using asynchronous flush (asynchronous Replication) |
| Business Security | Multi-dimension security protection and anti-DDoS attack services<br><br>Each message service is provided with a separate namespace. The data of different clients are strictly isolated<br><br>Support HTTPS access<br><br>Support cross-region security messaging service<br><br> | Limited security protection<br><br> Cross-region and cross-IDC public network services are not always provided to protect from threats from public network |

