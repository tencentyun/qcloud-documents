## 操作场景

MySQL Binlog 是记录 MySQL 所有数据变动的二进制日志文件，用于 MySQL 主从复制和数据恢复。此外开发者还可以将订阅 MySQL Binlog 应用在**增量索引**、**缓存一致性**、**基于数据的任务分发**、**记录数据变更**等场景。

![](https://qcloudimg.tencent-cloud.cn/raw/1e340a27ae0cc3b73fd10b1d3c3ac2da.png)


本文以 MySQL Binlog 接入 CKafka，并从 CKafka 流出到 CLS 为例，讲解如何使用数据接入平台实现 MySQL 数据变更记录分析。

## 运行原理

数据接入平台通过 Binlog 同步组件订阅 MySQL Binlog，然后将数据变更记录转化为 JSON 格式的消息生产到 CKafka 中。

## 前提条件

- 需要开通**云数据库 MySQL**开启 Binlog，并且根据业务需求修改**参数设置**。
<dx-codeblock>
:::  properties
binlog_format=ROW
# binlog_row_image 生产环境建议设置为 FULL，记录变更前后所有字段的值。可以快速恢复误操作的数据。
binlog_row_image=FULL
# binlog_rows_query_log_events 设为 ON 时，会记录变更时的 SQL 语句
binlog_rows_query_log_events=ON
:::
</dx-codeblock>
- 需开启 CKafka 服务。
- 需开启 CLS 服务。

## 操作步骤

### 步骤1：创建数据接入连接

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**连接列表**，选择好地域后，单击**新建连接**。
3. 连接类型选择 **MySQL**，然后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/b4efcb6cdac8367fe6766caec590c5c5.png)
4. 选择有 Binlog 权限的用户，填写 MySQL 连接配置后，单击**下一步**等待连接校验完成。
![](https://qcloudimg.tencent-cloud.cn/raw/814537add06333bd0e62a1783a16bb13.png)

### 步骤2：创建数据接入任务

1. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
2. 任务类型选择**数据接入**，接入方式选择 **MySQL 数据订阅**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/9b03cb8f6c9547334c30fe467b47b5e3.png)
3. **数据源**选择刚刚新建的 **MySQL 连接**。`database` 留空表示监听所有数据库的变更。`table` 留空表示监听某个数据库的所有表的变更。`复制存量数据`可以根据业务需求选择是否打开，然后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/cfd26f8b5c9b595f4e83b89c8a5f3ba3.png)
4. 根据业务需求配置数据目标然后点击**提交**。
> ! 为保证 Binlog 事件的全局顺序性，请设置 Topic 分区数请设置为 1 。
5. 当 MySQL 数据发送变化时，可以在目标 Topic 中查看到新增的消息。
    ![](https://qcloudimg.tencent-cloud.cn/raw/c73d9875d7762718d76cabee72152da6.png)
   - 数据目标为 CKafka 实例的 Topic，可以在侧边栏点击**消息查询**进行查看；
   - 数据目标为单独 Topic 时，可以在侧边栏点击 **Topic 列表**，然后点击 Topic 进入详情页，再点击**查看消息**。

### 步骤3：创建数据流出任务

1. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
2. 任务类型选择**数据流出**，接入方式选择**日志服务（CLS）**，单击**下一步**。
  ![](https://qcloudimg.tencent-cloud.cn/raw/8ce240e8aa67307d9175dc491bf7e19e.png)
3. 填写任务详情，选取与数据接入任务相同的 CKafka 实例和 Topic，保证在消息生产后能直接进行消费。
  ![](https://qcloudimg.tencent-cloud.cn/raw/679da20b4298c4810c24926c6df97338.png)
4. 配置好数据处理规则和数据目标后，单击**提交**，等待任务显示健康，即表示创建成功。
  <dx-alert infotype="explain" title="">
  当任务在健康的状态时， Topic 有新增的消息写入，会直接被消费到指定的 CLS 日志主题中。
  </dx-alert>

### 步骤4：查看流出数据

1. 登录 [日志服务](https://console.cloud.tencent.com/cls/overview) 控制台。
2. 在左侧导航栏选择**检索分析**，选择流出时填写的日志集与日志主题的“ID”，即可看到 MySQL 的变更记录。
  ![](https://qcloudimg.tencent-cloud.cn/raw/7d8fbefc7cbc617c198cf96caec86547.png)
3. 通过关键字检索等操作，能直观得到所需要的记录。
