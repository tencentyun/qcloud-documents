

## 操作场景

Datahub 提供数据流出能力，您可以将 CKafka 数据分发至数据仓库 Clickhouse 以对数据进行存储、查询和分析。

## 前提条件

- 若使用腾讯云数据仓库 Clickhouse 产品，使用时需开通相关产品功能。同时也支持数据流出至自建 Clickhouse。

- 在 Clickhouse 建好表，建表的时候需要指定好 Column 和 Type。

## 操作步骤

### 创建任务

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。

2. 在左侧导航栏单击**数据流出**，选择好地域后，单击**新建任务**。

3. 目标类型选择**数据仓库 Clickhouse**，单击**下一步**。

   ![](https://qcloudimg.tencent-cloud.cn/raw/f0aba2d2251312aa9743a2915565bc83.png)

   - 任务名称：只能包含字母、数字、下划线、"-"、"."。

   - CKafka 实例：选择数据源 CKafka。

   - 源 Topic：选择源 Topic。

   - 源数据：支持拉取源数据。

   - 起始位置：转储时历史消息的处理方式，topic offset 设置。

   - 数据仓库类型：

     - 云上 Clickhouse：选择数据仓库实例。

     - 自建 Clickhouse：需选择 CLB 实例。

   - 指定端口：Clickhouse 的连接端口（需要是 TCP 连接的端口）

   - 用户名：目标 Clickhouse 的用户名。

   - 密码：目标 Clickhouse 的用密码。

   - cluster： Clickhouse 的集群名称。

   - database：Clickhouse 设置的数据库名称。

   - table：在该数据库内构建的表名称，必须是源数据已存在的表。

4. 单击**提交**，完成任务创建。



### 查看监控

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。

2. 在左侧导航栏单击**数据流出**，单击目标任务的**ID**，进入任务基本信息页面。

3. 在任务详情页顶部，单击**监控**，选择要查看资源，设置好时间范围，可以查看对应的监控数据。

   - 单击![img](https://main.qcloudimg.com/raw/9ba57bbd3b8ef3efc4f687d63d27a46d.png)，可查看监控指标同环比。
   - 单击![img](https://main.qcloudimg.com/raw/34bdbdbdabb7b5720bf17d78c636a4ad.png)，可刷新获取最新的监控数据。
   - 单击![img](https://main.qcloudimg.com/raw/8f2bf7f4df9ddd959f0ecb69fdda8e4c.png)，可将图表复制到 Dashboard，关于 Dashboard 请参考 [什么是 Dashboard](https://cloud.tencent.com/document/product/248/47161)。
   - 选中![img](https://main.qcloudimg.com/raw/af20129df7be46f33ab7d3598f6e9213.png)，可在图表上显示图例信息。

   选择分区后，可以查看指定 Partition 的监控数据。

   ![](https://qcloudimg.tencent-cloud.cn/raw/7dbbfca73fd617ea96e276c7ab55370a.png)

   不选择时默认全部，展示现有的 Topic 级别的监控数据。

   ![](https://qcloudimg.tencent-cloud.cn/raw/7ad8dd52abe75bda0e827c71c6d1da16.png)



## 产品限制和费用计算

- 转储速度与 CKafka 实例峰值带宽上限有关，如出现消费速度过慢，请检查 CKafka 实例的峰值带宽或增加 CKafka partition 数。
- 转储速度与 CKafka 单个文件大小相关，如超过该500M，会自动分包上传。
