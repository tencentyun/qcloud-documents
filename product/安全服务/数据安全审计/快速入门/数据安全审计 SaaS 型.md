本文将为您介绍如何快速使用数据安全审计 SaaS 型。

## 前提条件
已购买 [数据安全审计SaaS型](https://cloud.tencent.com/document/product/856/64697)。


## 步骤1：同步数据资产
1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/dsgc/dsaudit)，单击**立即进入**。
![](https://qcloudimg.tencent-cloud.cn/raw/8d656cb1a704ecdf9d3f54f261a8a10b.png)
2. 进入数据安全审计服务之后，单击侧边栏的**数据资产**，进入数据资产页面。
![](https://qcloudimg.tencent-cloud.cn/raw/7fe7c7a5c58ab1b91fd1cfc7d6599be4.png)
3. 通过单击**更新资产列表**拉取云数据库列表，也可使用自建数据库的添加数据资产功能，当需要审计腾讯云外的数据资产时，可在腾讯云外数据库添加。
4. 添加数据库后，可通过单击对应数据库后面的![](https://qcloudimg.tencent-cloud.cn/raw/d3638827e13e926286f7fee006ba8801.png)，开启审计权限，允许数据安全审计采集其日志进行安全分析。
![](https://qcloudimg.tencent-cloud.cn/raw/1c140874a233d33bce9cc6e8e23ee18e.png)
>!
>- 开启审计权限将消耗 License 授权资产数。
>- 部分操作需要用户授权，只需按提示操作即可。


## 步骤2： 部署 Agent
1. 完成资产添加，并开启审计权限后，进入 **[Agent 管理](https://console.cloud.tencent.com/dsaudit/agent)** > **Agent 部署** 页面。
2. 在 Agent 部署中，根据数据库和应用系统所在位置和操作系统，下载对应的 Agent，进行部署。
![](https://qcloudimg.tencent-cloud.cn/raw/6524df86f03e724323ef4fcd44c95e21.png)
3. Agent 部署完成后，单击 **Agent 列表**，切换至 Agent 列表页面，验证 Agent 状态是否正常。
![](https://qcloudimg.tencent-cloud.cn/raw/162d9eee630c7edf951accf1e930950a.png)

## 步骤3：配置审计规则
1. 在 **[审计规则](https://console.cloud.tencent.com/dsaudit/rule)** > **规则列表**页面，可查看系统中的审计规则，若内置规则无法满足您的特定需要，您可以单击**新建**创建自定义规则。
![](https://qcloudimg.tencent-cloud.cn/raw/e0cef05f6f25ef6b459ffc8b8852b686.png)
2. 单击**规则启用**，进入规则启用页面，选择数据资产，为其启用需要的审计规则。
![](https://qcloudimg.tencent-cloud.cn/raw/57607f148276a893738fb00ca4e46b3d.png)


## 步骤4：查看审计日志
1. 完成以上配置后，在 [审计日志](https://console.cloud.tencent.com/dsaudit/log) 页面，可查看数据库的操作日志。
![](https://qcloudimg.tencent-cloud.cn/raw/ef4f3fadafe426e2bdeb4aebb30a33d5.png)
2. 在 [审计风险](https://console.cloud.tencent.com/dsaudit/risk) 页面，可查看发现的数据安全风险，安全管理人员可根据风险提示，判断是否需要采取进一步措施。
![](https://qcloudimg.tencent-cloud.cn/raw/bb22bea5912ec790ce9d5033ff06dbda.png)


