## 前提条件

- 已创建好数据目标 Topic。
- 已创建好数据源  MySQL 连接。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据接入**，数据目标类型选择 **MySQL数据接入**，单击**下一步**。
4. 填写数据源配置信息，单击下一步。
   ![](https://qcloudimg.tencent-cloud.cn/raw/14f25ae429bb726545ba19edd3553c81.png)
   - 数据源：选择提前创建好的 MySQL 连接。连接源设置的用户需要拥有 SELECT，RELOAD，SHOW DATABASES，REPLICATION SLAVE，REPLICATION CLIENT 的权限。
   - database：选择要监听的数据库。
   - 读取模式：支持**表模式**和**query 模式**。
     - 当读取模式为表模式时，需要选择 table。
     - 当读取模式为query模式是，需要输入 query 语句。
   - 增量依赖模式：任务定时查询数据库增量数据时，所依赖的列称作增量列。"时间”表示增量列为时间戳，“自增 ID”表示增量列为自增 ID。
   - 增量监听列：监听列只允许非空；数据接入无法监听到当前时间内被删除或者没有更新监听列的数据。
   - 复制存量数据：是否复制源数据库的存量数据。
5. 选择数据目标 Topic，支持选择 **DIP Topic** 或者 **CKafka Topic**。
   - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/1591/77020)。
   - CKafka Topic：选择在 CKafka 创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
6. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以看到创建进度。
   ![](https://qcloudimg.tencent-cloud.cn/raw/1bcbefe8c4d3bb3a48880ce0401f061f.png)
