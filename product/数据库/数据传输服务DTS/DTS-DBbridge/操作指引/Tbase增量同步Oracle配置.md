
Oracle 增量同步到 TBase 的过程中，支持从 Tbase 到 Oracle 的反向数据同步。本文为您介绍从 Tbase 到 Oracle 反向数据同步的配置操作。

## 前提条件
需确保同步的表在 Oracle 和 TBase 端数据一致。

## 使用限制
TBase 到 Oracle 的增量同步仅支持 INSERT、UPDATE 和 DELETE操作。
对于无主键的表，默认情况下只支持 INSERT 类型的数据变更，对于 UPDATE 和 DELETE 类型的变更，需要在 TBase 端手动修改表的 REPLICA IDENTITY 为 FULL。
对于无主键表的数据同步，DBbridge 无法保证上下游数据的一致性。

## 同步说明
TBase 写入 kafka 中的数据变更事件分为四种类型：
- c：对应 INSERT 操作。
- u：对应 UPDATE 操作。
- d：对应 DELETE 操作。
- r：对应数据同步功能初次启动时，TBase 写入到 kafka 中的全量数据。

用户在初次启动 TBase 数据同步功能时，可以通过 snapshot.mode 参数来设置是否需要执行全量数据导出。
DBbridge 通过消费 kafka 中的消息，并将其翻译成对应的 SQL，从而写入到目的端数据库。DBbridge 在消费 kafka 中的数据时，会忽略类型为 r 的消息。需要注意的是，TBase 写入到 kafka 中的数据是一行记录对应一个消息，所以 TBase 到 Oracle 的增量同步短时间内可能会出现数据不一致问题，这里实现的目标是数据的最终一致性。

## 配置用户
在 TBase 端用户需要有访问同步用户下所有对象的权限。
```
#创建用户
create user dbbridge password  ‘dbbridge';
create schema dbbridge;
alter schema dbbridge owner to dbbridge
#授权限
grant all privileges on all tables  in schema dbbridge to dbbridge;
#如果表无主键，需要设置 replica identity full 属性
alter table test replica identity full;
```
  
## 配置 TBase 数据同步
1. 登录 TBase 管理台，例 http://192.168.1.1:8080。
2. 在左侧运维管理的数据同步中，单击【添加同步】添加数据同步，添加完成后，开启数据同步。
>!数据库用户必须有 TBase 管理员权限，否则启动会失败。
>
![](https://main.qcloudimg.com/raw/fd2c18085286a0a70b5ace2beef4ce82.png)
3. 配置 connect，编辑配置文件。
```
#/data/dbbridge/kafka/config/connectdistributed.properties
bootstrap.servers=172.21.16.2:9092
group.id=connect-cluster
key.converter=org.apache.kafka.connect.json.JsonConverter value.converter=org.apache.kafka.connect.json.JsonConverter
key.converter.schemas.enable=true
value.converter.schemas.enable=true
offset.storage.topic=connect-offsets
offset.storage.replication.factor=1
config.storage.topic=connect-configs
config.storage.replication.factor=1
status.storage.topic=connect-status
status.storage.replication.factor=1
offset.flush.interval.ms=10000
producer.max.message.bytes=20971520
producer.max.request.size=5242880
producer.batch.size=65536
producer.linger.ms=500
producer.buffer.memory=33554400
producer.request.timeout.ms=60000
consumer.max.partition.fetch.bytes=20971520
```
4. 修改 kafka 配置文件。
```
#/data/dbbridge/kafka/config/server.properties 追加如下参数
message.max.bytes=2147483647
```
5. 启动 connect 服务。
```
connect-distributed.sh -daemon /data/dbbridge/kafka/config/connect-distributed.properties
```
6. 创建 TBase 数据源，填写 TBase 集群名称和 kafka broker 地址。
![](https://main.qcloudimg.com/raw/1d375eca8e7e3c8ed8ca70dd7b7389e7.png)
7. 创建同步通道。
![](https://main.qcloudimg.com/raw/e855e2999ae2e85e63a5e2e963b04d71.png)

## Tbase 反向数据同步至 Oracle 
配置完成后，可参考 [DTS-DBbridge 使用流程](https://cloud.tencent.com/document/product/571/45866#.E4.BD.BF.E7.94.A8.E6.B5.81.E7.A8.8B) 进行后续数据同步操作。
