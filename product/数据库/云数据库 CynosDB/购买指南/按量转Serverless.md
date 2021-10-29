
TDSQL-C for MySQL 计费方式支持按量计费转 Serverless。TDSQL-C 通过后台转换集群类型来实现按量计费转 Serverless，转换后 [账单和明细](https://console.cloud.tencent.com/expense/bill/summary) 会发生变化，计费模式仍然为后付费。

>!
>- 按量计费转换 Serverless 过程中，数据库可提供访问，转换的时间点会发生闪断，建议您的应用程序配置自动重连功能。
>- 按量计费转换 Serverless 后，Serverless 实例无法转换回按量计费实例。

## 操作步骤
1. 登录 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb)，在实例列表选择所需实例，在**操作**列选择**更多** > **按量转Serverless**。
![](https://main.qcloudimg.com/raw/cf6bd2eb1307d1930b9afd6bf95db828.png)
2. 在弹出的对话框，选择所要转换 [Serverless](https://cloud.tencent.com/document/product/1003/50853) 数据库的最小最大 CCU 和自动暂停时间，勾选同意规则，单击**确定**。
![](https://main.qcloudimg.com/raw/9e96526fb0aad69e6aabd32e203f5c01.png)
