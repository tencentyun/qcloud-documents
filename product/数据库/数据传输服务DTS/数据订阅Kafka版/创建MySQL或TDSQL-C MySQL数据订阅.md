本场景介绍使用 DTS 创建腾讯云数据库 MySQL 或 TDSQL-C MySQL 的数据订阅任务操作指导。

## 前提条件
- 已准备好待订阅的腾讯云数据库，并且数据库版本符合要求，请参见 [数据订阅支持的数据库](https://cloud.tencent.com/document/product/571/59965)。
- 已在源端实例中开启 binlog。
- 已在源端实例中创建订阅帐号，需要帐号权限如下：REPLICATION CLIENT、REPLICATION SLAVE、PROCESS 和全部对象的 SELECT 权限。
具体授权语句如下：
```
create user '迁移账号' IDENTIFIED BY '账号密码';
grant SELECT, REPLICATION CLIENT,REPLICATION SLAVE,PROCESS on *.* to '迁移账号'@'%';
flush privileges;
```

## 约束限制
- 订阅的消息内容目前默认保存时间为最近1天，超过保存时间的数据会被清除，请用户及时消费，避免数据在消费完之前就被清除。
- 数据消费的地域需要与订阅实例的地域相同。
- 当前不支持 geometry 相关的数据类型。 
- DTS 订阅 Kafka 的消息投递语义采用的是至少一次（at least once），所以在特殊情况下消费到的数据可能存在重复。如订阅任务发生重启，重启后拉取源端的 Binlog 会从中断的位点往前多拉取一些，导致重复投递消息。控制台修改订阅对象、恢复异常任务等操作都可能会导致消息重复。如果业务对重复数据敏感，需要用户在消费 Demo 中根据业务数据增加去重逻辑。


## 支持订阅的 SQL 操作
|  操作类型 | 支持的 SQL 操作 |
| ------ | --------------------------- |
| DML | INSERT、UPDATE、DELETE |
| DDL | CREATE DATABASE、DROP DATABASE、CREATE TABLE、ALTER TABLE、DROP TABLE、RENAME TABLE |

## 操作步骤
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/dss)，在左侧导航选择**数据订阅**，单击**新建数据订阅**。
2. 在新建数据订阅页，选择相应配置，单击**立即购买**。
 - 计费模式：支持包年包月和按量计费。
 - 地域：地域需与待订阅的数据库实例地域保持一致。
 - 数据库：请根据具体数据库类型进行选择。
 - 版本：选择 **kafka 版**，支持通过 Kafka 客户端直接消费。
 - 订阅实例名称：编辑当前数据订阅实例的名称。
3. 购买成功后，返回数据订阅列表，单击**操作**列的**配置订阅**对刚购买的订阅进行配置，配置完成后才可以进行使用。
![](https://main.qcloudimg.com/raw/d45bbff5e702281fdc57984720999e6c.png)
4. 在配置数据库订阅页面，选择相应配置，单击**下一步**。
 - 实例：选择对应数据库实例，只读实例和灾备实例不支持数据订阅。
 - 数据库帐号：添加订阅实例的帐号和密码，帐号具有订阅任务需要的权限，包括 REPLICATION CLIENT、REPLICATION SLAVE、PROCESS 和全部对象的 SELECT 权限。
 - kafka 分区数量：设置 kafka 分区数量，增加分区数量可提高数据写入和消费的速度。单分区可以保障消息的顺序，多分区无法保障消息顺序，如果您对消费到消息的顺序有严格要求，请选择 kafka 分区数量为1。
![](https://main.qcloudimg.com/raw/531477e532ac70c5bf2646922c93405c.png)
5. 在订阅类型和对象选择页面，选择订阅类型，单击**保存配置**。
 - 订阅类型，包括数据更新、结构更新和全实例。
    - 数据更新：订阅选择对象的数据更新，包括数据 INSERT、UPDATE、DELETE 操作。
    - 结构更新：订阅实例中全部对象的结构创建、修改和删除。
    - 全实例：包括该订阅实例的全部对象的数据更新和结构更新。
 - 订阅数据格式：支持 ProtoBuf、Avro 和 Json 三种格式。 ProtoBuf 和 Avro 采用二进制格式，消费效率更高，Json 采用轻量级的文本格式，更加简单易用。
 - Kafka 分区策略：选择按表名分区，按表名+主键分区。
 - 使用自定义分区策略：用户根据自己的需求自定义分区，详情内容请参考 [设置分区策略](https://cloud.tencent.com/document/product/571/78161)。
![](https://qcloudimg.tencent-cloud.cn/raw/b5364aa79598fb8e6046e2a60c686fda.png)
6. 在预校验页面，预校验任务预计会运行2分钟 - 3分钟，预校验通过后，单击**启动**完成数据订阅任务配置。
>?如果校验失败，请 [校验不通过处理方法](https://cloud.tencent.com/document/product/571/58685) 进行修正，并重新进行校验。
>
![](https://main.qcloudimg.com/raw/c47a857b65b6d3244b985e01492aff9f.png)
7. 单击启动后，订阅任务会进行初始化，预计会运行3分钟 - 4分钟，初始化成功后进入**运行中**状态。
8. [新增消费组](https://cloud.tencent.com/document/product/571/52377)，数据订阅 Kafka 版支持用户创建多个消费组，进行多点消费。数据订阅 Kafka 版消费依赖于 Kafka 的消费组，所以在消费数据前需要创建消费组。 
9. 订阅实例进入运行中状态之后，就可以开始消费数据。Kafka 的消费需要进行密码认证，具体示例请参考 [数据消费 Demo](https://cloud.tencent.com/document/product/571/52381)，我们提供了多种语言的 Demo 代码，也对消费的主要流程和关键的数据结构进行了说明。
