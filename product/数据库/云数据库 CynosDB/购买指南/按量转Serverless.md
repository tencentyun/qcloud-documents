
云原生数据库 TDSQL-C 计费方式支持按量计费转 Serverless。TDSQL-C 通过后台转换集群类型来实现进行按量计费转 Serverless，转换后 [账单和明细](https://console.cloud.tencent.com/expense/bill/summary) 会发生变化，计费模式仍然为后付费。

>!
>- 按量计费转换 Serverless 过程中，不会对您的业务访问造成任何影响，请放心使用。
>- 按量计费转换 Serverless 后，Serverless 实例无法转换回按量计费实例。

## 操作步骤
1. 登录 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb)，在实例列表选择所需实例，在“操作”列选择【更多】>【按量转Serverless】。
![](https://main.qcloudimg.com/raw/cf6bd2eb1307d1930b9afd6bf95db828.png)
2. 在弹出的对话框，选择所要转换 Serverless 数据库的最小最大 CCU 和自动暂停时间，勾选同意规则，单击【确定】。
![](https://main.qcloudimg.com/raw/9e96526fb0aad69e6aabd32e203f5c01.png)
