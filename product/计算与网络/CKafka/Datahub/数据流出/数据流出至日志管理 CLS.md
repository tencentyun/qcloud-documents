## 操作场景

Datahub 提供数据流出能力，您可以将 CKafka 数据分发至日志管理 CLS 便于解决业务问题定位，指标监控，安全审计等日问题。

## 前提条件

该功能目前依赖 SCF、CLS 服务。使用时需提前开通云函数 SCF、CLS 等相关服务及功能。

## 操作步骤

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。

2. 在左侧导航栏单击**数据流出**，选择好地域后，单击**新建任务**。

3. 目标类型选择**日志管理（CLS）**，单击**下一步**。

   ![](https://qcloudimg.tencent-cloud.cn/raw/f0e5074fc884a13286457c2cfe6a1406.png)

   - 任务名称：只能包含字母、数字、下划线、"-"、"."。
   - CKafka 实例：选择数据源 CKafka。
   - 源 Topic：选择源 Topic。
   - 日志集：日志服务的项目管理单元，用于区分不同项目的日志。一个日志集对应一个项目或应用。
   - 日志主题：一个 [日志集](https://cloud.tencent.com/document/product/614/35676) 可以包含多个日志主题，一个日志主题对应一类应用或服务，建议将不同机器上的同类日志收集到同一个日志主题。
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
- 该功能基于云函数 SCF 服务提供。SCF为用户提供了一定 [免费额度](https://cloud.tencent.com/document/product/583/12282) ，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。
