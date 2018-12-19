## Product Overview

Cloud Kafka is a high-throughput and highly scalable message queue service provided by Tencent based on the self-developed CMQ engine. Compatible with Apache kafka 0.9, Cloud Kafka has superior advantages in performance, scalability, business security, and OPS, allowing you to enjoy powerful features at low cost while eliminating the tedious operation OPS work.

### Application Scenarios
1. Webpage tracking
Cloud Kafka processes website activities (PV, search, and other user activities) in real time, and then posts them to topics by type. These info flows can be used for real-time monitoring or offline statistical analysis.
Since a large amount of activity information is generated in each user's page view, the website activity tracking requires high throughput. Cloud Kafka can perfectly meet the requirements of high throughput and offline processing.

2. Log aggregation
Cloud Kafka provides the features of low-latency processing, easy support for multiple data sources and distributed data processing (consumption). Compared to the centralized log aggregation system, Cloud Kafka can implement stronger persistence guarantees as well as lower end-to-end latency while providing the same performance.
The above features make Cloud Kafka an ideal "log collection center". Multiple servers/applications can send the operation logs "asynchronously" to a Cloud Kafka cluster "in batch" without being stored locally or in a DB. Cloud Kafka can submit/compress messages in batch, and the producers can hardly perceive the performance overhead. At this time, the consumers can use systematic storage and analysis systems such as Hadoop to collect and analyze pulled logs.

3. Big Data Scenario
For some business scenarios related to big data, a large amount of concurrent data needs to be processed and aggregated. Therefore, high cluster processing performance and high scalability are required. In the implementation, Cloud Kafka is also suitable for handling massive real-time messages and aggregating distributed application data in terms of its data distribution mechanism, allocation of disk storage spaces, processing of message formats, server selection, and data compression, facilitating system OPS.

In a specific big data scenario, Cloud Kafka processes offline data and streaming data very well, and aggregates and analyzes data easily.

### Advantages
1. Decoupling
  The relationship between producers and consumers is effectively decoupled. Under the premise that the same API constraint is ensured, the processing between producers and consumers is allowed to be independently expanded or modified.
  
2. Scalability
  Because the message processing is decoupled, it only needs to be horizontally scaled to effectively increase the enqueue efficiency and processing efficiency of the message, which is very flexible.
  
3. Peak Load Shifting
  Message queue can withstand the sudden access pressure, without completely crashing due to the sudden overloaded requests, which effectively boosts the system robustness.
  
4. Resiliency
  When part of the system components fail, the overall system is not affected, which increases the system's fault tolerance. The process failure of a certain message is processed timely, and the messages in the queue can still be processed after the system is restored.

5. Sequential Read/Write
  Cloud Kafka can guarantee the orderliness of messages within a Partition, which is consistent with most message queues. Besides, Cloud Kafka ensures that data is processed in order, greatly improving the disk efficiency.

6. Asynchronous Communication
  In the scenario where the business does not need to process messages immediately, Cloud Kafka provides the asynchronous message processing mechanism. When the traffic is large, messages are put into the queue only, and they will be processed after the traffic is reduced, which relieves the system pressure.
  
## Glossary

| No.     |     Name |   Explanation |
| :-------- | :--------| :------ |
| 1 | Broker | The server in the Cloud Kafka cluster |
| 2 | Topic | The message type, Cloud Kafka is message-oriented |
| 3 | Partition | A concept in physical partition, where one Topic can contain one or more partitions, and Cloud Kafka uses partition as an allocation unit |
| 4 | Replica | The copy of partition, used for guaranteeing the high availability of partition |
| 5 | Offset | The unique serial number of a message in partition |
| 6 | Producer | The producer, responsible for publishing messages |
| 7 | Consumer | The consumer, consuming messages from the cluster |
| 8 | Consumer group | The group of consumers, each consumer must belong to one consumer group. Each message can be consumed by multiple consumer groups, but can only be consumed by one consumer in this group |
| 9 | Zookeeper | Used to store meta data of cluster, conduct leader election, fault tolerance, etc. |



