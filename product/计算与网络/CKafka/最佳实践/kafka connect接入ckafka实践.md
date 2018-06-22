Kafka Connect目前支持两种执行模式：standalone和distributed。


## 1. 通过以下命令以standalone模式启动connect：
```
bin/connect-standalone.sh config/connect-standalone.properties connector1.properties [connector2.properties ...]
```
接入ckafka与接入开源kafka没有区别，仅需要修改bootstrap.servers为申请实例时分配的ip。

## 2. 通过以下命令以distributed模式启动connect：
```
bin/connect-distributed.sh config/connect-distributed.properties
```
该模式下，kafka connect会将offsets、configs和task status信息存储在kafka topic中，存储的topic在connect-distributed中的以下字段配置：
```
config.storage.topic
offset.storage.topic
status.storage.topic
```
这三个topic需要手动创建，才能保证创建的属性符合connect的要求。
> 
config.storage.topic需要保证只有一个partition，多副本且为compact模式。
offset.storage.topic需要有多个partition，多副本且为compact模式
status.storage.topic需要有多个partition，多副本且为compact模式

配置bootstrap.servers为申请实例是分配的ip；
配置group.id，这个用于标识connect集群，需要与消费者分组区分开来。

