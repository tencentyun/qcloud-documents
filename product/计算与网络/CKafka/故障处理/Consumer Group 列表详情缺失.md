
## 现象概述

CKafka 的消费组列表有消费组名称，点开详情，却没有消费详情。例如：下图的消费组 CR 没有展示详情。
![](https://main.qcloudimg.com/raw/c1cdbfb124ec0dfd2829a6c011c4c9b3.png)

## 可能原因

Kafka 的数据消费有两种模式，消费组模式和自定义分区消费模式。

- 当使用消费组模式消费，客户端会通过消费协调者进行协调消费，在消费数据完成后，会往服务端提交 offset 的存储请求。则此时服务端会存储消费的 Topic、分区进度、客户端等信息。
- 当使用自定义分区消费的模式，则客户端不会自动往服务端提交 offset 存储请求，则此时如果客户端没有主动发起提交 offset 请求，则服务端是看不到消费的相关信息的。
- 当 Topic 设置了 ACL 以后，某些实例可能会出现无法看到消费者组的详情，如果出现无法看详情，请先检查是否有 ACL，如果有，则需要您 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行处理。


## 解决方法

1. 查看实例的消费组列表。
   ```
   ]$ bin/kafka-consumer-groups.sh --bootstrap-server 9.146.153.249:9092 --list
   CR
   ```
   可以看到当前的所有消费组名称。  

2. 查看实例特定的消费组详情。
   ```
   ]$ bin/kafka-consumer-groups.sh --bootstrap-server 9.146.153.249:9092 --describe --group CR
   Note: This will not show information about old Zookeeper-based consumers.
   ```
   会发现该消费组并没有详情。这表示消费者客户端没有使用 consumerGroup 机制去消费数据。即客户端没有往服务端提交消费详情，服务端没有存储消费数据，则不会正常显示。

3. 定位是否是服务端的问题.
   通过原生自带的消费组命令，指定消费组名称 test1 进行消费，如下所示: 
   ```
   ]$ bin/kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --from-beginning --topic test --group test1
   ```
   则在控制台能正常显示的消费组，通过 `--describe` 命令是可以看到详情的，如下所示：
   ![](https://main.qcloudimg.com/raw/d54eb823fe66da94364849e670f83fba.png)
