## 操作场景

MongoDB 内有 Change Stream 作为其追踪变更的解决方案，但为了更好地对变更记录进行搜索，往往需要将变更记录同步到 Elasticsearch、日志服务(CLS) 等。

![](https://qcloudimg.tencent-cloud.cn/raw/4689f690f7d5753e0fcdbe7142fca6ea.jpg)

本文以 MongoDB 接入 CKafka 并从 CKafka 流出到 CLS 为例，讲解如何使用 DIP 数据转储服务实现 Mongo Stream 数据变更记录分析。

## 运行原理

MongoDB 的数据流入配置项可参见官方 [MongoDB Kafka source connector](https://docs.mongodb.com/kafka-connector/current/source-connector/)，通过设置不同的配置项，能够对接入的变更记录做相应的数据处理后再写入到 CKafka 实例的 Topic。

## 前提条件

- 需开启云数据库 MongoDB 服务或使用负载均衡 CLB 监听自建 MongoDB。
![](https://qcloudimg.tencent-cloud.cn/raw/1386958ceb6ad238cde997d2c53eb722.png)
并且设置的安全组需要开放 TCP:27017 端口。
![](https://qcloudimg.tencent-cloud.cn/raw/3a7a7593ecdedf07de2e087d0687d258.png)
- 需开启 CKafka 服务。
- 需开启 CLS 服务。

## 操作步骤

### 步骤1：创建数据接入连接

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏点击**连接列表**，选择好地域后，点击**新建连接**。
3. 连接类型选择 **MongoDB**，然后点击**下一步**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4b8841a7138191fbe58a597966db2821.png)
4. 填写 MongoDB 连接配置，然后单击**下一步**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4ff6606cac6117c885019319eab85d97.png)
5. 等待连接校验成功后，可以在连接列表看到创建好的连接。





### 步骤2：创建数据接入任务

1. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
2. 任务类型选择**数据接入**，接入方式选择 **MongoDB数据订阅**，单击**下一步**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/5306577955f25ada475ae97b056119c4.png)
3. **数据源**选择刚刚新建的 **MySQL 连接**。`database` 留空表示监听所有数据库的变更。`table` 留空表示监听某个数据库的所有表的变更。`复制存量数据`可以根据业务需求选择是否打开，然后单击**下一步**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/bb1711c9d78553b7e885f7bd58d5afea.png)
4. 根据业务需求配置数据目标然后点击**提交**。等待任务显示健康，即表示创建成功。
   ![](https://qcloudimg.tencent-cloud.cn/raw/c3de44cecf13ba331b78914ebb100f53.png)
5. 当 MongoDB 数据发生变更时，可以在目标 Topic 中查看到新增的消息。![](https://qcloudimg.tencent-cloud.cn/raw/c73d9875d7762718d76cabee72152da6.png)
   - 数据目标为 CKafka 实例的 Topic，可以在侧边栏点击**消息查询**进行查看；
   - 数据目标为单独 Topic 时，可以在侧边栏点击 **Topic 列表**，然后点击 Topic 进入详情页，再点击**查看消息**。



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

1. 登录 [日志服务](https://console.cloud.tencent.com/cls/overview?region=ap-guangzhou) 控制台。
2. 在左侧导航栏选择**检索分析**，选择流出时填写的日志集与日志主题的“ID”，即可看到 MongoDB 的变更记录。
![](https://qcloudimg.tencent-cloud.cn/raw/bb814dba5eac4aa46e9ad3f8732a7951.png)
3. 通过关键字检索等操作，能直观得到所需要的记录。
![](https://qcloudimg.tencent-cloud.cn/raw/f4d1f65187e45a9c40d92f590d192029.png)
