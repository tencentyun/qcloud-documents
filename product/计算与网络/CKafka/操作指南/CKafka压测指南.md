### 性能测试工具

$KAFKA_HOME/bin/kafka-producer-perf-test.sh  该开源脚本被设计用于测试Kafka Producer的 性能，主要输出每秒发送消息量（MB/second），每秒发送消息数（records/second）等两项指标。

$KAFKA_HOME/bin/kafka-consumer-perf-test.sh 该脚本用于测试 Kafka Consumer的性能， 测试指标与 Producer 性能测试脚本一样

### 测试命令

生产测试命令示例
```
bin/kafka-producer-perf-test.sh   --topic test --num-records 123 --record-size 1000  --producer-props bootstrap.servers= ckafka vip : port --throughput 20000   
```

消费测试命令示例
```
bin/kafka-consumer-perf-test.sh   --topic test --new-consumer  --fetch-size 10000 --messages 1000  --broker-list bootstrap.servers=ckafka vip : port
```

### 测试建议

1. 为了提高吞吐量，创建分区时数量建议>=3 （因后端ckafka集群节点数量最少是3，如只创建一个分区则分区会分布在一个broker上面，影响性能）     
2. 由于CKafka是分区级别消息有序的，因此过多的分区也会影响生产性能，根据实际压测，建议分区数不超过6
3. 为了保证压力测试的效果，需要多客户端模拟一定的并发，建议采用多台机器作为压测客户端（生产端），每台启动多个压测程序，提高并发 。此外建议每1s启动一个生产者防止同时启动所有生产者导致测试机器高负载。  
