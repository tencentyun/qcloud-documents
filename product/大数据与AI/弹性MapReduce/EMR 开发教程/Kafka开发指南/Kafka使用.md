## 生成数据
### java 代码方式
 ![](https://main.qcloudimg.com/raw/c6f641369c53d28e8a50e246dde66e97.png)
### 命令方式
```
bin/kafka-console-producer.sh --broker-list node86:9092 --topic t_cdr
```

## 消费数据
### java 代码方式
![](https://main.qcloudimg.com/raw/ec55f3d19722444b32c9f6dc2d0ac85b.png)
 
### 命令方式
```
bin/kafka-console-consumer.sh --zookeeper node01:2181 --topic t_cdr --from-beginning
```

### 新增 topic（命令方式）
```
bin/kafka-topics.sh --zookeeper node01:2181 --create --topic t_cdr --partitions 30  --replication-factor 2
```
详细使用可参考 [kafka 官方文档](https://kafka.apache.org/11/documentation.html)。

