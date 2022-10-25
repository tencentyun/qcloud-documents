

## 操作场景

数据接入平台 DIP 支持接入各种数据源产生的不同类型的数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道

DIP 支持订阅 TDSQL-C MySQL 版变更数据，免去对基于 CDC 的订阅组件如（Canal、Debezium 等）的运维成本。本文介绍在 DIP 控制台创建 TDSQL-C MySQL 版数据接入任务的操作方法。

## 前提条件

- 已创建好数据目标 Topic。
- 已创建好数据源 TDSQL-C MySQL 连接。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据接入**，数据源类型选择 **TDSQL_C 数据订阅**，单击**下一步**。
4. 填写数据源配置信息，单击下一步。
   ![](https://qcloudimg.tencent-cloud.cn/raw/b66e4787406a8d3e48887c393ffd05e8.png)
   - 源数据类型：支选择 **MySQL**。
   - 数据源：选择提前创建好的数据库连接。
   - database：选择要监听的数据库。
   - 监听全部表：开后后表示监听数据库中的全部表的变更。
   - table：选择要监听的表。
   - 复制存量数据：是否复制源 TDSQL-C MySQL 版的存量数据。
5. 选择数据目标 Topic，支持选择 **DIP Topic** 或者 **CKafka Topic**。
   - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/1591/77020)。
   - CKafka Topic：选择在 CKafka 创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
6. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以看到创建进度。

   
