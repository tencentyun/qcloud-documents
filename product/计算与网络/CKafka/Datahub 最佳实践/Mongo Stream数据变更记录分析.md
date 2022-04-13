## 操作场景

MongoDB 内有 Change Stream 作为其追踪变更的解决方案，但为了更好地对变更记录进行搜索，往往需要将变更记录同步到 Elasticsearch、日志服务(CLS) 等。

![](https://qcloudimg.tencent-cloud.cn/raw/4689f690f7d5753e0fcdbe7142fca6ea.jpg)

本文以 MongoDB 接入 CKafka 并从 CKafka 流出到 CLS 为例，讲解如何使用 DataHub 数据转储服务实现 Mongo Stream 数据变更记录分析。

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

### 步骤1：创建数据接入任务

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏单击**数据流入**，选择好地域后，单击**新建任务**。
3. 在弹窗中数据源类型选择 **异步拉取** > **MongoDB**。
![](https://qcloudimg.tencent-cloud.cn/raw/2733ca5e5b966bac82f1858962cc960c.png)
4. 单击**下一步**，填写任务详情。
![](https://qcloudimg.tencent-cloud.cn/raw/a5647a8d101714a982858ff81c827f10.png)
5. 单击**提交**，等待任务显示健康，即表示创建成功。
![](https://qcloudimg.tencent-cloud.cn/raw/c3de44cecf13ba331b78914ebb100f53.png)
6. 当 MongoDB 数据发生变更时，可以看到选中的 CKafka 实例的 Topic 有新增的消息。
![](https://qcloudimg.tencent-cloud.cn/raw/94494e70d68682da95a83a3c3f56d124.png)

### 步骤2：创建数据流出任务

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏单击**数据流出**，选择好地域后，单击**新建任务**。
3. 目标类型选择**日志服务（CLS）**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/49edecde6642832c3d7c2d57322ed672.png)
4. 填写任务详情，选取与数据接入任务相同的 CKafka 实例和 Topic，保证在消息生产后能直接进行消费。
![](https://qcloudimg.tencent-cloud.cn/raw/3d0e8a13995fcd325cf8e32a9b8dbbda.png)
5. 单击**提交**，等待任务显示健康，即表示创建成功。
![](https://qcloudimg.tencent-cloud.cn/raw/8f4ff805167b1b84d7dacc8c8dc4a333.png)
<dx-alert infotype="explain" title="">
当任务在健康的状态时， Topic 有新增的消息写入，会直接被消费到指定的 CLS 日志主题中。
</dx-alert>



### 步骤3：查看流出数据

1. 登录 [日志服务](https://console.cloud.tencent.com/cls/overview?region=ap-guangzhou) 控制台。
2. 在左侧导航栏选择**检索分析**，选择流出时填写的日志集与日志主题的“ID”，即可看到 MongoDB 的变更记录。
![](https://qcloudimg.tencent-cloud.cn/raw/bb814dba5eac4aa46e9ad3f8732a7951.png)
3. 通过关键字检索等操作，能直观得到所需要的记录。
![](https://qcloudimg.tencent-cloud.cn/raw/f4d1f65187e45a9c40d92f590d192029.png)

