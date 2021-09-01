## 测试工具
Kafka Producer 和 Consumer 的性能测试均可使用 Kafka 客户端自带的开源脚本，主要输出每秒发送消息量（MB/second）和每秒发送消息数（records/second）两项指标。
- Kafka Producer 测试脚本：`$KAFKA_HOME/bin/kafka-producer-perf-test.sh`
- Kafka Consumer 测试脚本：`$KAFKA_HOME/bin/kafka-consumer-perf-test.sh`


## 测试命令
>?以下命令中的 `ckafka vip:vport` 应替换为您实际实例分配的 IP 和端口。

生产测试命令示例：
```
bin/kafka-producer-perf-test.sh   
--topic test 
--num-records 123 
--record-size 1000  
--producer-props bootstrap.servers= ckafka vip : port 
--throughput 20000   
```

消费测试命令示例：
```
bin/kafka-consumer-perf-test.sh   
--topic test 
--new-consumer  
--fetch-size 10000 
--messages 1000  
--broker-list bootstrap.servers=ckafka vip : port
```

## 测试建议
- 为了提高吞吐量，建议创建分区时数量 ≥ 3 （因后端 CKafka 集群节点数量最少是3，如只创建1个分区则分区会分布在一个 Broker 上面，影响性能）。     
- 由于 CKafka 是分区级别消息有序的，因此过多的分区也会影响生产性能，根据实际压测，建议分区数不超过6。
- 为了保证压力测试的效果，需要多客户端模拟一定的并发，建议采用多台机器作为压测客户端（生产端），每台启动多个压测程序，提高并发。此外建议每1s启动一个生产者，避免同时启动所有生产者导致测试机器高负载。  

