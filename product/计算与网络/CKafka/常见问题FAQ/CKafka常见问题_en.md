
### Which version of open-source Kafka is compatible with Cloud Kafka?
CKafka service is compatible with the open-source Kafka.api of version 0.9 and later, achieving free migration to the cloud for users.

### What is TOPIC?
Topic is the category to which each message published in the Cloud Kafka cluster belongs. That is to say, Cloud Kafka is topic-oriented. Users need to create a topic before read and write.

### What is PARTITION?
Partition is a physical concept. Each topic can be divided into one or more partitions. Partition is used to scale out topic throughput. Published messages are written to different partitions and read by several consumers at the same time. As the assignment unit of Cloud Kafka is partition, the parallel throughput of topic is directly proportional to the number of partitions.

### What is the difference between Cloud Kafka and CMQ?
CMQ provides financial-level message transmission with high reliability and high data persistence while ensuring strong data consistency.
Cloud Kafka is suitable for scenarios requiring higher throughput and relatively lower reliability, such as log aggregation. In addition, Cloud Kafka is compatible with the regular users of Kafka, with zero migration cost and complete exclusive instance.

### Can the Kafka client be directly connected to Cloud Kafka?
Cloud Kafka is compatible with the open-source Kafka of version 0.9 and later. You can connect to the message center through the Kafka client, and deploy codes to Tencent Cloud services to produce or consume messages.

### How does Cloud Kafka ensure security?
Cloud Kafka ensures security with the following security features:

Tenant Isolation: The network accesses of instances are naturally isolated between accounts.
Permission Control: Cloud Kafka provides an authentication mechanism for the source ip whitelist in the extra application layer.
Security Protection: Services including multi-dimensional security protection and anti-DDoS attacks are provided.

### Will CKafka lose messages?
1. The open-source Apache Kafka does not guarantee no loss of messages. As CKafka is optimized in availability, Tencent Cloud promises that the availability of CKafka exceeds 99.95%.
2. CKafka customers can enable ACK during production to avoid message loss as much as possible and improve reliability.
3. Cluster change and upgrade are transparent to customers. Clusters can be changed instantly.
4. CKafka is mainly used in big data processing scenarios that require high throughput and high performance but average data reliability. A small amount of messages may be lost in extreme circumstances. For scenarios that require no message loss but average performance, it is recommended to use CMQ.

### What are the restrictions on CKafka products?
Restrictions on product forms:
1. A maximum of 50 partitions and 20 groups can be created for each instance.
2. A maximum of 8 partitions and 3 copies can be created for each topic.
3. The idleness time of a consumer group is 1 month.

