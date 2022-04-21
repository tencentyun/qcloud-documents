## 操作场景 

[数据传输服务（Data Transmission Service，DTS）](https://cloud.tencent.com/document/product/571/8707)支持 MySQL、MariaDB、PostgreSQL、Redis、MongoDB 等多种关系型数据库及 NoSQL 数据库数据订阅，数据库中关键业务的数据变化信息，并提供给下游进行业务订阅、获取和消费，方便用户搭建云数据库和异构系统之间的数据同步，如缓存更新，ETL（数据仓库技术）实时同步，业务异步解耦等。

在事件总线（EventBridge）中，您可以通过配置 DTS 连接器，基于 DTS 数据订阅实时拉取源实例的 Binlog 增量日志，完成日志的消费与处理，并实现下游不同目标的分发。本文为您介绍如何创建 DTS 连接器及 DTS 连接器生成的事件结构。

## 功能介绍
更多详情，请参考[ DTS 数据订阅产品文档](https://cloud.tencent.com/document/product/571/59388)。

### 支持数据库

| **源数据库类型**           | **源数据库版本**                  | **支持订阅的数据类型** |
| ------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| MySQL | MySQL 5.5.x、5.6.x、5.7.x、8.0.x | <li>数据更新<li>结构更新<li>全实例 |
| MariaDB           | MariaDB 10.0.10、MariaDB 10.1.9 | <li>数据更新<li>结构更新<li>全实例 |
| MariaDB（Percona） | MariaDB（Percona）5.6.x、5.7.x | <li>数据更新<li>结构更新<li>全实例 |
| TDSQL MySQL | TDSQL MySQL 5.6.x、5.7.x、8.0.18 | <li>数据更新<li>结构更新<li>全实例 |
| TDSQL-C MySQL | TDSQL-C MySQL 5.7.x、8.0.x | <li>数据更新<li>结构更新<li>全实例 |
| TDSQL PostgreSQL 版 | PostgreSQL 版 | 数据更新 |

### 支持订阅操作
DTS 支持订阅对象选择的粒度为库、表，具体支持如下三种订阅类型：

- 数据更新：指订阅 DML 操作。
- 结构更新：指订阅 DDL 操作。
- 全实例：指订阅所有库表的 DML 以及 DDL 操作。

###  限制说明
- EB 侧限制事件大小，如果上游日志大小超过 **1 MB**，将无法成功投递至 EB 完成消费，请注意控制您的日志大小。
- 当前方案下，EB 对于多 Partition 会并发消费，无法保证顺序性。
- 为保证您的数据可以正常消费，创建成功后，请谨慎更新消费组账号密码信息，如果更新后，请重新绑定连接器，否则可能无法正常完成消费。
- DTS 支持批量投递，对于批量变更的操作，将会在同一条事件中以数组格式完成投递。

## 前提条件 

1. 已 [开通 DTS 数据订阅服务](https://cloud.tencent.com/document/product/571/59951) 并创建实例。
2. **子账号**需要通过主账号获取 EventBridge 和 DTS 的相关操作权限。

## 操作步骤 
1. 登录 [事件总线控制台](https://console.cloud.tencent.com/eb/)，选择左侧导航栏中的**事件集**。
2. 在“事件集”列表，选择期望配置 DTS 连接器的事件集。
3. 在“事件集详情”页事件连接器配置项中单击**添加**，连接器类型选择**数据订阅(DTS)**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a27ab1f886cea5b67cca6052505daafd.png)
4. 根据页面提示选择需要消费的数据订阅实例，并填入消费组名称、账号、密码等信息。如果还没有完成消费对象绑定，请在 DTS 控制台完成相关配置，操作详情见 [创建 MySQL 或 MariaDB 数据订阅](https://cloud.tencent.com/document/product/571/52412)。
5. 单击**确定**完成创建，在事件集页面查看您绑定的连接器信息。
![](https://qcloudimg.tencent-cloud.cn/raw/20a49057dbb47ee9983200195658b011.png)
6. 在事件集详情页中，单击**管理事件规则**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/74ea5782d981011c0cb7fd21201b0921.png)
7. 单击**新建事件规则**，根据页面提示填写相关信息，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d0d27d70588a8012e84c1f8bf32fccd7.png)
   其中**云服务类型**选择**数据订阅（DTS）**，并根据实际需求，配置 [数据转换](https://cloud.tencent.com/document/product/1359/71392) 和绑定触发目标。
8. 单击**确定**即可完成创建。

## 事件格式
DTS 连接器接收处理后的事件格式如下： 

### DDL 操作示例
```JSON
 {
   "id":"38cecd93-a9c2-11ec-b952-******d8da53:16",
   "type":"dts:MYSQL:INSERT",
   "specversion":"1.0",
   "source":"dts.cloud.tencent",
   "subject":"cdb-xxxx",
   "time":1648109734,
   "region":"ap-guangzhou",
   "datacontenttype":"application/json;charset=utf-8",
   "tags":null,
   "data":{
      "topic":"topic-subs-xxxx-cdb-xxxx",
      "partition":3,
      "offset":16005,
      "partition_seq":16006,
      "event":{
         "dmlEvent":{
            "columns":[
               {
                  "name":"string",
                  "originalType":"text"
               },
               {
                  "name":"int",
                  "originalType":"tinyint(4)"
               },
               {
                  "name":"time",
                  "originalType":"time"
               },
               {
                  "name":"double",
                  "originalType":"double"
               },
               {
                  "name":"id",
                  "originalType":"int(11)",
                  "isKey":true
               },
               {
                  "name":"float",
                  "originalType":"float"
               },
               {
                  "name":"longtext",
                  "originalType":"longtext"
               }
            ],
            "rows":[
               {
                  "newColumns":[
                     {
                        "dataType":13,
                        "charset":"utf8",
                        "bv":"dG1w"
                     },
                     {
                        
                     },
                     {
                        
                     },
                     {
                        "dataType":10,
                        "sv":"1"
                     },
                     {
                        "dataType":3,
                        "sv":"3"
                     },
                     {
                        
                     },
                     {
                        
                     }
                  ]
               }
            ]
         }
      },
      "header":{
         "sourceType":1,
         "messageType":2,
         "timestamp":1648109734,
         "serverId":109741,
         "fileName":"mysql-bin.000005",
         "position":2234587,
         "gtid":"38cecd93-a9c2-11ec-b952-******d8da53:16",
         "schemaName":"dts",
         "tableName":"dts_mysql",
         "seqId":16017,
         "isLast":true
      },
      "eb_consumer_time":"2022-03-24 16:15:34.287359965 +0800 CST m=+1120.357657669",
      "eb_connector":""
   }
}
```

### DML 操作示例
```JSON
{
   "id":"38cecd93-a9c2-11ec-b952-******8da53:19",
   "type":"dts:MYSQL:DDL",
   "specversion":"1.0",
   "source":"dts.cloud.tencent",
   "subject":"cdb-xxxx",
   "time":1648110060,
   "region":"ap-guangzhou",
   "datacontenttype":"application/json;charset=utf-8",
   "tags":null,
   "data":{
      "topic":"topic-subs-aniwxeewm4-cdb-xxxx",
      "partition":0,
      "offset":16065,
      "partition_seq":16066,
      "event":{
         "ddlEvent":{
            "schemaName":"dts",
            "sql":"ALTER TABLE `dts_mysql` ADD COLUMN `t` tinyint (0) NULL , ADD UNIQUE `t` USING btree (`t`)"
         }
      },
      "header":{
         "sourceType":1,
         "messageType":3,
         "timestamp":1648110060,
         "serverId":109741,
         "fileName":"mysql-bin.000005",
         "position":2235430,
         "gtid":"38cecd93-a9c2-11ec-b952-******d8da53:19",
         "seqId":16087,
         "isLast":true
      },
      "eb_consumer_time":"2022-03-24 16:21:01.19682088 +0800 CST m=+1447.267118604",
      "eb_connector":""
   }
}
```

### 参数说明

| **参数**            | **描述**                                                         |
| ---------------- | ------------------------------------------------------------ |
| id            | 事件 ID，EB 自动生成，每条事件在 EB 内的唯一标识。      |
| type | 事件类型，三段式形式，对 dts 连接器，格式为`dts:${数据库类型}:${操作类型}` 。                |
| specversion   | Cloudevents 版本，默认 1.0，EB 自动生成。    |
| source            | 事件来源，对 dts 连接器，统一为`dts.cloud.tencent`。           |
| subject          | 事件产生具体实例，对 dts 连接器，为数据订阅绑定的数据库实例 ID。        |
|time|事件投递到 EB 的时间。|
|region|事件产生地域。|
|tags|资源标签。|
|data|数据库实际 binlog 日志内容。|
|data.topic|数据订阅实例信息。|
|data.partition|消费 partition。|
|data.offset|消费位点。|
|data.event|分为 dmlEvent 和 ddlEvent，dmlEvent 介绍数据表的 schema 格式和更改内容，ddlEvent 介绍具体 sql 操作。|
|data.header|操作日志头部信息，包含数据库名称、表名称、变更时间戳等具体信息。|
