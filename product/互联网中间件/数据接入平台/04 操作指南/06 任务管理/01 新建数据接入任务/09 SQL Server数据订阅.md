## 操作场景

数据接入平台 DIP 支持接入各种数据源产生的不同类型的数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道

DIP 支持订阅  SQL Server 变更数据，本文介绍在 DIP 控制台创建 SQL Server 数据接入任务的操作方法。

## 前提条件

- 已创建好数据目标 Topic。
- 已创建好数据源  SQL Server 连接。

  > ?仅支持 SQL Server 2016 及以上的版本。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据接入**，数据目标类型选择**SQL Server数据订阅**，单击**下一步**。
4. 填写数据源配置信息，单击下一步。
   ![](https://qcloudimg.tencent-cloud.cn/raw/64a5218d2ee90ce5ecff803daeeacfa1.png)
   - 数据源：选择提前创建好的 SQL Server 连接。
   - database：选择要监听的数据库。
   - table：选择要监听的数据表。
   - 复制存量数据：是否复制源 SQL Server 的存量数据。
5. 选择数据目标 Topic。
   - 自动创建 Topic：可以选择 **CKafka Topic** 或者 **DIP Topic**，若选择CKafka Topic，则需要指定目标CKafka 实例。支持批量连续命名或指定模式串命名，[参考文档](https://cloud.tencent.com/document/product/597/59246)。
   - 选择已有 Topic：支持选择 **DIP Topic** 或者 **CKafka Topic**。选择 CKafka Topic 时，若实例设置了ACL 策略，请确保选中的 Topic 有读写权限。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a69e5c59c27680d16f776400d59b3034.png)
   - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/1591/77020)。
   - CKafka Topic：选择在 CKafka 创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
5. 选择是否开启数据压缩，数据压缩可以减少网络 IO 传输量，减少磁盘存储空间，[数据压缩说明](https://cloud.tencent.com/document/product/597/40402)。
6. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以看到创建进度。
   ![](https://qcloudimg.tencent-cloud.cn/raw/98b12e00f6dc17332436b25199691ec2.png)
