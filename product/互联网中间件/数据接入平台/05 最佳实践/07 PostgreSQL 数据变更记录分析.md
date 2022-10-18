## 操作场景

PostgreSQL 通过 WAL（Write-Ahead Logging）预写日志机制保证事务持久性和数据完整性，开发者可以将订阅 WAL 应用在**增量索引**、**缓存一致性**、**基于数据的任务分发**、**记录数据变更**等场景。

![](https://qcloudimg.tencent-cloud.cn/raw/79096196d7e2d8e98eef95f152ef7609.png)

本文以 PostgreSQL 接入 CKafka，并从 CKafka 流出到 CLS 为例，讲解如何使用数据接入平台实现 PostgreSQL 数据变更记录分析。


## 运行原理

数据接入平台通过订阅 PostgreSQL WAL，将行级数据变更记录转化为 JSON 格式的消息生产到 CKafka 中。


## 前提条件

- 需要开通**云数据库 PostgrepSQL**，然后修改以下配置。
<dx-codeblock>
:::  properties
wal_level=logical
#
# 9.4、9.5、9.6 版本需要根据业务需求设置下面参数
# 10 及以上版本则可以使用默认值
#
max_replication_slots=10
max_wal_senders=10
:::
</dx-codeblock>
- 需开启 CKafka 服务。
- 需开启 CLS 服务。

## 操作步骤

### 步骤1：创建数据接入连接

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏点击**连接列表**，选择好地域后，点击**新建连接**。
3. 连接类型选择 **PostgreSQL**，然后点击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/87341939d674ff20b201cf3ccf3956a2.png)
1. 选择有 **REPLICATION** 和 **LOGIN** 权限的用户，填写 PostgreSQL 连接配置，然后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/f2799a9c1f638078536b5caccc24d4fe.png)

### 步骤2：创建数据接入任务

1. 在在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，点击**新建任务**。
2. 任务类型选择**数据接入**，接入方式选择**PostgreSQL 数据订阅**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/3f9971f3dbbb98969d057168b3cd6142.png)
3. 数据源选择刚刚新建的 **PostgreSQL 连接。**`database` 留空表示监听所有数据库的变更。`table` 留空表示监听某个数据库的所有表的变更。`复制存量数据`可以根据业务需求选择是否打开，然后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/4a1500b8aadbb35d92313b2185677ffe.png)
4. 根据业务需求配置数据目标，然后点击**提交**。
5. 当 PostgreSQL 数据发送变化时，可以在目标 Topic 中查看到新增的消息。
    ![](https://qcloudimg.tencent-cloud.cn/raw/c73d9875d7762718d76cabee72152da6.png)
   - 数据目标为 CKafka 实例的 Topic，可以在左侧导航栏点击**消息查询**进行查看；
   - 数据目标为单独 Topic 时，可以在左侧导航栏点击**Topic 列表**，然后点击 Topic 进入详情页，再点击**查看消息**。

### 步骤3：创建数据流出任务

1. 在左侧导航栏点击**任务管理** > **任务列表**，选择好地域后，点击**新建任务**。
2. 任务类型选择**数据流出**，数据目标选择**日志服务（CLS）**，点击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/815e78914effabe23e96e08ffce0dd7f.png)
3. 填写任务详情，选取与数据接入任务相同的 CKafka 实例和 Topic，保证在消息生产后能直接进行消费。
![](https://qcloudimg.tencent-cloud.cn/raw/679da20b4298c4810c24926c6df97338.png)
4. 单击**提交**，等待任务显示健康，即表示创建成功。
<dx-alert infotype="explain" title="">
当任务在健康的状态时， Topic 有新增的消息写入，会直接被消费到指定的 CLS 日志主题中。
</dx-alert>

### 步骤4：查看流出数据

1. 登录 [日志服务](https://console.cloud.tencent.com/cls/overview) 控制台。
2. 在左侧导航栏选择**检索分析**，选择流出时填写的日志集与日志主题的“ID”，即可看到 PostgreSQL 的变更记录。
![](https://qcloudimg.tencent-cloud.cn/raw/7d8fbefc7cbc617c198cf96caec86547.png)
3. 通过关键字检索等操作，能直观得到所需要的记录。
