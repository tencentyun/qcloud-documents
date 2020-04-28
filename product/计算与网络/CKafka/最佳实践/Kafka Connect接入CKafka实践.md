Kafka Connect 目前支持两种执行模式：standalone 和 distributed。


##  以 standalone 模式启动 connect
通过以下命令以 standalone 模式启动 connect：
```
bin/connect-standalone.sh config/connect-standalone.properties connector1.properties [connector2.properties ...]
```
接入 ckafka 与接入开源 kafka 没有区别，仅需要修改 bootstrap.servers 为申请实例时分配的 IP。

## 以 distributed 模式启动 connect
通过以下命令以 distributed 模式启动 connect：
```
bin/connect-distributed.sh config/connect-distributed.properties
```
该模式下，kafka connect 会将 offsets、configs 和 task status 信息存储在 kafka topic 中，存储的 topic 在 connect-distributed 中的以下字段配置：
```
config.storage.topic
offset.storage.topic
status.storage.topic
```
这三个 topic 需要手动创建，才能保证创建的属性符合 connect 的要求。

- config.storage.topic 需要保证只有一个 partition，多副本且为 compact 模式。
- offset.storage.topic 需要有多个 partition，多副本且为 compact 模式。
- status.storage.topic 需要有多个 partition，多副本且为 compact 模式。

配置 bootstrap.servers 为申请实例是分配的 IP；

配置 group.id，用于标识 connect 集群，需要与消费者分组区分开来。

