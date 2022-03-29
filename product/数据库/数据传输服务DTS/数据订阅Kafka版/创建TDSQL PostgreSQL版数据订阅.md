本场景介绍使用 DTS 创建腾讯云 [TDSQL PostgreSQL 版](https://cloud.tencent.com/document/product/1129) 的数据订阅任务操作指导。

## 前提条件
- 已准备好待订阅的 [TDSQL PostgreSQL 版](https://cloud.tencent.com/document/product/1129/39893)，并且各数据库版本符合要求，请参见 [数据订阅支持的数据库](https://cloud.tencent.com/document/product/571/59965)。
- 已在源端实例中创建订阅帐号，需要帐号权限如下： LOGIN 和 REPLICATION 权限。
  LOGIN 和 REPLICATION 授权请 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。
- 订阅帐号必须拥有被订阅表的 select 权限，如果是整库订阅，那么订阅帐号要拥有该 schema 下所有表的 select 权限，具体授权语句如下：
```
grant SELECT on all tables in schema "schema_name" to '迁移帐号' ;
```
- 用户必须拥有 pg_catalog.pgxc_node 表的 select 权限，具体授权语句如下：
```
grant SELECT on pg_catalog.pgxc_node to '迁移帐号';
```
- DN 节点的 wal_level 必须是 logical。
- 被订阅的表如果是全复制表（建表语句中有 distribute by replication 关键字），必须拥有主键；被订阅的表如果不是全复制表，必须拥有主键或 REPLICA IDENTITY 为 FULL；修改表的  REPLICA IDENTITY  为 FULL 的语句： 
```
alter table '表名' REPLICA IDENTITY FULL;
```

## 约束限制
- 订阅的消息内容目前默认保存时间为最近1天，超过保存时间的数据会被清除，请用户及时消费，避免数据在消费完之前就被清除。
- 数据消费的地域需要与订阅实例的地域相同。
- 当前不支持 gtsvector, pg_dependencies, pg_node_tree, pg_ndistinct, xml 相关的数据类型。 
- 数据订阅源是 TDSQL PostgreSQL 版时，不支持直接执行授权语句授权，所以订阅帐号的权限需要在 [TDSQL 控制台](https://console.cloud.tencent.com/tdsqld) 单击实例 ID，获取实例登录信息后，通过客户端登录数据库进行帐号授权。

## 支持订阅的 SQL 操作

| 操作类型 | 支持的 SQL 操作        |
| -------- | ---------------------- |
| DML      | INSERT、UPDATE、DELETE |

## 操作步骤
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/dss)，在左侧导航选择**数据订阅**，单击**新建数据订阅**。
2. 在新建数据订阅页，选择相应配置，单击**立即购买**。
 - 计费模式：支持包年包月和按量计费。
 - 地域：地域需与待订阅的数据库实例订阅保持一致。
 - 数据库：请根据具体数据库类型进行选择。
 - 版本：选择 **kafka 版**，支持通过 Kafka 客户端直接消费。
 - 订阅实例名称：编辑当前数据订阅实例的名称。
3. 购买成功后，返回数据订阅列表，单击**操作**列的**配置订阅**对刚购买的订阅进行配置，配置完成后才可以进行使用。
4. 在配置数据库订阅页面，选择相应配置，单击**下一步**。
 - 实例：选择对应数据库实例，只读实例和灾备实例不支持数据订阅。
 - 数据库帐号：添加订阅实例的帐号和密码，帐号的 LOGIN 、REPLICATION 权限和全部对象、pg_catalog.pgxc_node 表的 SELECT 权限。
5. 在订阅类型和对象选择页面，选择订阅类型，单击**保存配置**。
 - 订阅类型为数据更新（订阅选择对象的数据更新，包括数据 INSERT、UPDATE、DELETE 操作）。
 - Kafka 分区策略：支持按表名分区。
![](https://qcloudimg.tencent-cloud.cn/raw/6db09899d50c54652bd178895e45dca8.png)
6. 在预校验页面，预校验任务预计会运行2分钟 - 3分钟，预校验通过后，单击**启动**完成数据订阅任务配置。
>?如果校验失败，请根据失败提示在待订阅实例中进行修正，并重新进行校验。
>
![](https://qcloudimg.tencent-cloud.cn/raw/e64f245e449d2dc12fa5f65648364320.png)
7. 单击启动后，订阅任务会进行初始化，预计会运行3分钟 - 4分钟，初始化成功后进入**运行中**状态。
8. [新增消费组](https://cloud.tencent.com/document/product/571/52377)，数据订阅 Kafka 版支持用户创建多个消费组，进行多点消费。数据订阅 Kafka 版消费依赖于 Kafka 的消费组，所以在消费数据前需要创建消费组。 
9. 订阅实例进入运行中状态之后，就可以开始消费数据。Kafka 的消费需要进行密码认证，具体示例请参考 [数据消费 Demo](https://cloud.tencent.com/document/product/571/52381)，我们提供了多种语言的 Demo 代码，也对消费的主要流程和关键的数据结构进行了说明。

