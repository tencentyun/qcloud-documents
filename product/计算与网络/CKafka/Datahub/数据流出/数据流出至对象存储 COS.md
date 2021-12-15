## 操作场景

Datahub 提供数据流出能力，您可以将 CKafka 数据分发至 COS 以便于对数据进行分析与下载等操作。
处理流程及架构如下：
![img](https://main.qcloudimg.com/raw/8fdf8c6f74a3d4597688fddd4a3bffd4.svg)



## 前提条件

该功能目前依赖云函数（SCF）、对象存储（COS）等产品，使用时需开通相关产品功能。

## 操作步骤

### 创建任务

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。

2. 在左侧导航栏单击**数据流出**，选择好地域后，单击**新建任务**。

3. 目标类型选择**对象存储（COS）**，单击**下一步**。

   ![](https://qcloudimg.tencent-cloud.cn/raw/6bd9d6662d90d66ca6dc26de82561938.png)

   - 任务名称：只能包含字母、数字、下划线、"-"、"."。
   - CKafka 实例：选择数据源 CKafka。
   - 源 Topic：选择源 Topic。
   - 目标存储桶：对不同的 Topic，选取相应的 COS 中 Bucket，则请求消息会自动在 Bucket 下创建 instance-id/topic-id/date/timestamp为名称的文件路径进行存储。相关路径如无法满足业务需要，请创建完成后在云函数 CkafkaToCosConsumer 下自行修改。
   - 聚合方式：请至少填写一种聚合方式，文件将根据指定方式聚合进入 COS 存储桶。如果指定了两种聚合方式，则会同时生效。例：指定每1h或1GB聚合一次，若在1h之前达到1GB，则文件会聚合，同时在1h时也会聚合一次。
   - 起始位置：转储时历史消息的处理方式，topic offset 设置。
   - 角色授权：使用云函数 SCF 产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
   - 云函数授权：知晓并同意开通创建云函数，该函数创建后需用户前往云函数设置更多高级配置及查看监控信息。

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
- 当前仅支持和 CKafka 实例同个地域的 COS 进行消息存储，为保证延时，不支持跨地域存储。
- 使用COS消息转储，文件内容是 CKafka 消息里的 value 用 utf-8 String 序列化拼接而成，暂不支持二进制的数据格式。
- 开启转 COS 的操作账号必须对目标 COS Bucket 具备写权限。
- 使用 COS 消息转储必须至少拥有一个 VPC 网络环境，如在创建时选择基础网络请参考 [路由接入方式](https://cloud.tencent.com/document/product/597/36348) 绑定 VPC 网络。
- 该功能基于云函数 SCF 服务提供。SCF为用户提供了一定 [免费额度](https://cloud.tencent.com/document/product/583/12282) ，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。
- 转储方案价格与 CKafka Partition 数有关，当前 Partition 个数与函数并发个数保持一致。若需修改函数并发个数请检查 schedule 函数逻辑。
