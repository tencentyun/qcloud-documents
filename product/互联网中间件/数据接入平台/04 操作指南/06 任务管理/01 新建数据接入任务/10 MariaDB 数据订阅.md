## 操作场景

数据接入平台 DIP 支持接入各种数据源产生的不同类型的数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道

DIP 支持订阅  MariaDB 变更数据，本文介绍在 DIP 控制台创建 MariaDB 数据接入任务的操作方法。

## 前提条件

- 已创建好数据目标 Topic。
- 已创建好数据源  MariaDB 连接。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据接入**，数据目标类型选择 **MariaDB 数据订阅**，单击**下一步**。
4. 填写数据源配置信息，单击下一步。
   ![](https://qcloudimg.tencent-cloud.cn/raw/2dd33e41f3b4b1f7e35cd0047d49ffa9.png)
   - 数据源：选择提前创建好的 MariaDB 连接。连接源设置的用户需要拥有 SELECT，RELOAD，SHOW DATABASES，REPLICATION SLAVE，REPLICATION CLIENT 的权限。
   - database：选择要监听的数据库。
   - table：选择要监听的数据表。
   - 复制存量数据：是否复制源 MariaDB 的存量数据。
5. 选择数据目标 Topic，支持选择 **DIP Topic** 或者 **CKafka Topic**。
   - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/1591/77020)。
   - CKafka Topic：选择在 CKafka 创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
6. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以看到创建进度。
   ![](https://qcloudimg.tencent-cloud.cn/raw/6e7de3ade04778916596742245176cd7.png)



