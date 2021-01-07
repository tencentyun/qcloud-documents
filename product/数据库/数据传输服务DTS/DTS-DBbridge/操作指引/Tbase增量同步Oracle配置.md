# 7.2 Tbase到Oracle反向同步配置
## 7.2.1 前置条件
   在Oracle到Tbase的增量同步过程中，支持从TBASE到Oracle的反向数据同步。需要在先确保ORACLE和TBASE两端数据一致。
## 7.2.2 使用限制
   TBase到Oracle的增量同步仅支持INSERT，UPDATE和DELETE操作。对于无主键的表，默认情况下只支持INSERT类型的数据变更，对于UPDATE和DELETE类型的变更，需要在TBase端手动修改表的REPLICA IDENTITY为FULL。对于无主键表的数据同步，DBbridge无法保证上下游数据的一致性。
## 7.2.3 同步说明
   TBase写入kafka中的数据变更事件分为四种类型：
    c：对应INSERT操作
    u：对应UPDATE操作
    d：对应DELETE操作
    r：对应数据同步功能初次启动时TBase写入到kafka中的全量数据

   用户在初次启动TBase的数据同步功能时，可以通过snapshot.mode参数来设置是否需要执行全量数据导出。DBbridge通过消费kafka中的消息，并将其翻译成对应的SQL，从而写入到目的端数据库。DBbridge在消费kafka中的数据时，会忽略类型为r的消息。需要注意的是，TBase写入到kafka中的数据是一行记录对应一个消息，所以TBase到Oracle的增量同步短时间内可能会出现数据不一致问题，这里实现的目标是数据的最终一致性。
## 7.2.4 用户配置
     在Tbase端用户需要有访问同步用户下所有对象的权限。
     #创建用户
       create user dbbridge password  ‘dbbridge';
       create schema dbbridge;
       alter schema dbbridge owner to dbbridge
     #授权限
       grant all privileges on all tables  in schema dbbridge to dbbridge;
     #如果表无主键需要设置replica identity full属性(重要)
       alter table test replica identity full;

## 7.2.5 配置tbase数据同步
    1)	登陆TBASE管理台
          例：http://192.168.1.1:8080
    2)	点击左侧【运维管理】中的<数据同步>，添加数据同步
         ![](https://main.qcloudimg.com/raw/fd2c18085286a0a70b5ace2beef4ce82.png)
         添加完成后，开启数据同步。
         说明：数据库用户必须有tbase管理员权限,否则启动会失败。
    3)	配置connect,编辑配置文件
        #/data/dbbridge/kafka/config/connectdistributed.properties
          bootstrap.servers=172.21.16.2:9092
          group.id=connect-cluster
          key.converter=org.apache.kafka.connect.json.JsonConverter
          value.converter=org.apache.kafka.connect.json.JsonConverter
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

    4)	修改kafka配置文件
         #/data/dbbridge/kafka/config/server.properties 追加如下参数
          message.max.bytes=2147483647

    5)	启动connect服务
         connect-distributed.sh -daemon /data/dbbridge/kafka/config/connect-distributed.properties   
    6)	创建TBASE数据源
        ![](https://main.qcloudimg.com/raw/1d375eca8e7e3c8ed8ca70dd7b7389e7.png)
         填写正确的TBASE集群名称和kafka broker的地址。
    7)	创建同步通道
        ![](https://main.qcloudimg.com/raw/e855e2999ae2e85e63a5e2e963b04d71.png)