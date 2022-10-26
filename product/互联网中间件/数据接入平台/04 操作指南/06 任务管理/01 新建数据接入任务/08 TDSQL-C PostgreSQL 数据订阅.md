## 操作场景

数据接入平台 DIP 支持接入各种数据源产生的不同类型的数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道

DIP 支持订阅 TDSQL-C PostgreSQL 版变更数据，免去对基于 CDC 的订阅组件如（Canal、Debezium等）的运维成本。本文介绍在 DIP 控制台创建 TDSQL-C PostgreSQL 版数据接入任务的操作方法。

## 前提条件

- 已创建好数据目标 Topic。
- 已创建好数据源 TDSQL-C PostgreSQL 连接。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。

2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。

3. 填写任务名称，任务类型选择**数据接入**，数据源类型选择 **TDSQL_C PostgreSQL 数据订阅**，单击**下一步**。

4. 填写数据源配置信息。

   | 参数     | 说明                                                         |
   | :------- | :----------------------------------------------------------- |
   | 数据源   | 选择提前创建好的 PostgreSQL 源数据连接                       |
   | database | 选择要监听的数据库。                                         |
   | Table    | 支持两种种选择方式：<br><li>批量选择：支持手动勾选要订阅的数据库和表，支持订阅多个数据库、多个表。</li><br/><li>正则匹配：支持使用正则匹配筛选订阅符合条件的表。</li> |

   ![](https://qcloudimg.tencent-cloud.cn/raw/3623ac5667b8c750e2f0943f683450ba.png)

5. （可选）设置高级参数。

   | 参数           | 说明                                                         |
   | :------------- | :----------------------------------------------------------- |
   | 复制存量数据   | 开启后将复制源 PostgreSQL 数据库中的存量数据，开关一经打开，无论后续是否关闭，都无法新增需要监听的库。 |
   | 是否包含Schema | 消息输出时，key和value内容是否包含schema。                   |
   | pluginName     | 选择自建的 PostgreSQL 连接时，需要使用 pgoutput。            |
   | 分区策略       | 订阅数据写入，默认情况下根据主键 hash 到不同的分区。可以手动指定表的 hash 字段。 |

   ![](https://qcloudimg.tencent-cloud.cn/raw/0265e7a8c635d4098888a6dcb2d2b7dc.png)

6. 选择数据目标 Topic，支持选择 **DIP Topic** 或者 **CKafka Topic**。

   分发到多个 Topic：支持将不同数据库表中的数据分发到不同的 Topic 中去。

   - 开启后：只能选择同一个 CKafka 实例下的 Topic。
   - 未开启：支持选择 **DIP Topic** 或者 **CKafka Topic**。
     ![](https://qcloudimg.tencent-cloud.cn/raw/0daa51f156dc33a3602f90b23208dec3.png)

7. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以看到创建进度。

   
