The details of performance comparison between Cloud Kafka and other message service products are as follows:

| Features |	CKafka	| Apache Kafka	| RabbitMQ	| RocketMQ	| CMQ |
|:--------|:--------|:--------|:--------|:--------|:--------|
| Advantages |	Very high throughput<br>Very flexible scalability<br>Very low OPS cost	| High throughout |	High reliability	| High reliability |	Very high reliability<br>Finance and other scenarios with strong consistency |
| Disadvantages | Occasionally message loss in extreme circumstances	| Occasionally message loss<br>Not flexible scalability<br>Multiple dependent components, large OPS<br>Limited security protection, poor isolation and compatibility |	Poor performance<br>Not flexible expansion	| Manual (not automatic) HA switching	| Average throughout for strong consistency |
| Development language	| C++	| Scala |	Erlang |	Java	| C++ |
| Scalability	 | Very flexible, easy to scale, only the vip address needs to be specified to send messages, and the broker changes are transparent for both sending and receiving messages |	Not flexible enough, the broker address needs to be specified to send messages, and the zookeeper coordination scheduling is required to receive messages |	Not flexible enough, the broker address needs to be specified to send messages |	More flexible, the sender and receiver are connected to the name server | Flexible, smooth, scale-out, and logically a single Queue can provide services across multiple clusters |
| Throughput |	Very large |	Large	| Average |	Average |	Average |
| General Performance |	Million-level QPS	| Million-level QPS |	100-thousand-level QPS |	100-thousand-level QPS |	100-thousand-level QPS |
| 2C 4GB Stress test |	Read/write 220,000 QPS |	Read/write 200,000 QPS |	Read/write 100,000 QPS |	Read/write 100,00 QPS |	Read/write 120,000 QPS |
| Synchronization Algorithm |	ISR (Replica) |	ISR (Replica) |	GM	| Double Synchronous writes |	Raft |
| Availability	| Very high availability, automatic switching between master and slave, Tencent Cloud Message Service guarantees an availability of 99.95% |	 High availability, automatic switching between master and slave, the messages may be lost after switching due to asynchronous flush and replication |	Automatic switching between master and slave, the mirror queue supports m/s, master for providing services and slave for backup only |	Automatic switching between master and slave is not supported. Slave only reads and does not write when master is not available |	Very high availability, broker provides highly available services as long as it contains 2 nodes |
| Consumption method |	Pull |	Pull |	Pull and push |	Pull |	Pull and push |
| Message reliability |	Higher<br> Improved reliability by three copies, good disaster recovery capability for clusters, rare occurrence of faults |	Low<br>Broker is only provided with the asynchronous flush mechanism while master and slave are only provided with asynchronous replication, which may result in loss of part messages	| High<br>When you send messages, the specified message are persistently written to the disk	| High<br>Broker is written to two disks synchronously. A message indicating success is returned only when both master and slave are written successfully	| Extremely high<br>Message loss is avoided by synchronous flush, with a data persistence of 99.999999% |
| Data verification	| CRC |	CRC	| None	| CRC	| checksum |
| Message rewind	| Yes	| Yes |	No |	No	| Yes |
| Security protection | Yes |	No | No | No | Yes |	
| Monitoring and alarming | Yes |	No | No | No | Yes |	
| Service support | Yes |	No | No | No | Yes |	

Note: "2C 4GB Stress Test" indicates the result of a stress test on a 2-core 4GB memory server.

