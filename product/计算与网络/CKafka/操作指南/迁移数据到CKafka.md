根据以下流程，您可以依据实际业务场景选择合适的迁移方式。从而实现业务数据的迁移上云。本指南主要针对云服务器数据切换到 CKafka，通过内网访问可以实现；如果需要公网数据流的访问，首先需要开通 CKafka 公网 IP 的访问。

## 保证消息有序性，迁移数据到 CKafka

保证消息有序性的前提是严格控制单个消费者来消费数据，因此对于切换的时间节点要求较高。其迁移步骤如下所示：

![Alt text](https://main.qcloudimg.com/raw/4736662afc81f7dba0cf23fb81cf5e2e.png)

详细步骤说明：

1. 创建 CKafka 实例，并创建对应 topic：
![Alt text](https://main.qcloudimg.com/raw/389bb5536612d17dbc9aad626b53c10b.png)

2. 切换生产流，生产者将数据生产到 CKafka 实例。
 修改 broker-list 中的 IP 为 CKafka 实例的 vip，topicName 为 CKafka 实例中的 topic 名称：
```
 ./kafka-console-producer.sh --broker-list xxx.xxx.xxx.xxx:9092 --topic topicName
```

3. 原有消费者无需做配置，持续消费自建 Kafka 集群的数据，在消费完成时，通过以下配置切换为新消费者消费 CKafka 集群的数据。（单个消费者消费数据，保证消息的有序性）

 新增消费者，需要配置 --bootstrap-server 中的 IP 为 CKafka 实例的 vip：
```
./kafka-console-consumer.sh --bootstrap-server xxx.xxx.xxx.xxx:9092 --from-beginning --new-consumer --topic topicName --consumer.config ../config/consumer.properties
```

4. 新消费者持续消费 CKafka 集群中的数据，迁移完毕（如果消费者为云主机，此处也可以继续使用原有消费者进行消费）。

>**注意：**
>上文给出的是测试命令，正式业务的运行只需要修改相应应用程序配置的 broker 地址，然后重启相应的应用即可。

## 不保证数据有序，迁移数据到 CKafka

对于数据有序性要求不高的情况下，可以采用多个消费者并行消费的方式进行切换。其迁移步骤如下所示：

![Alt text](https://main.qcloudimg.com/raw/22bc7a3e4d745078a03e0f45813cfc7b.png)

详细步骤说明：

1. 创建 CKafka 实例，并创建对应 topic：
![Alt text](https://main.qcloudimg.com/raw/cdcfa5de5c52df2b27d597dd46496b4e.png)

2. 切换生产流，生产者将数据生产到 CKafka 实例。

 修改 broker-list 中的 IP 为 CKafka 实例的 vip，topicName 为 CKafka 实例中的 topic 名称
```
 ./kafka-console-producer.sh --broker-list xxx.xxx.xxx.xxx:9092 --topic topicName
```

3. 原有消费者无需特殊配置，继续消费自建 Kafka 集群的数据，同时也可以增加新的消费者消费 CKafka 集群的数据。当原有自建集群的数据消费完成后，即迁移完毕。（适用于不要求消息有序性的场景）

 配置 --bootstrap-server 中的 IP 为 CKafka 实例的 vip：
```
./kafka-console-consumer.sh --bootstrap-server xxx.xxx.xxx.xxx:9092 --from-beginning --new-consumer --topic topicName --consumer.config ../config/consumer.properties
```

>!上文给出的是测试命令，正式业务的运行只需要修改相应应用程序配置的 broker 地址，然后重启相应的应用即可。
