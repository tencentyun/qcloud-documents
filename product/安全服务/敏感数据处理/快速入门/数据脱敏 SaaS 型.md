本文将为您介绍如何进入数据脱敏 SaaS 型控制台。

## 前提条件
已购买 [数据脱敏 SaaS 型](https://cloud.tencent.com/document/product/882/20024#.E6.95.B0.E6.8D.AE.E8.84.B1.E6.95.8F-saas-.E5.9E.8B)。

## 操作步骤
### 授权服务
1. 登录 [数据脱敏控制台](https://console.cloud.tencent.com/dmask)，单击**立即进入**。
![](https://main.qcloudimg.com/raw/60a319796a70211e29bfcba394e2f7e7.png)
2. 进入数据脱敏服务后，单击任一页面，即会提出授权提示，单击**去授权**，进入角色管理页面。
>?数据脱敏需要帮助企业拉取数据资产、读取资产信息、处理资产数据，需要得到您的授权许可。
>
![](https://main.qcloudimg.com/raw/2caf51b7963a072abfc82d7dedc1cae3.png)
3. 在角色管理页面，请阅读角色及策略说明，单击**同意授权**后完成授权，可正常使用数据脱敏服务。
![](https://main.qcloudimg.com/raw/b73c1157403b4848bcdcbf130a422cf5.png)

### 添加数据源
1. 登录 [数据脱敏控制台](https://console.cloud.tencent.com/dmask)，单击**立即进入**。
![](https://main.qcloudimg.com/raw/60a319796a70211e29bfcba394e2f7e7.png)
2. 进入数据脱敏服务后，在左侧导航栏中，单击**数据源**，管理数据资产的授权信息。
![](https://main.qcloudimg.com/raw/1dff53b6a0726da1ca7ab21c2437498a.png)
3. 若已开通 [数据安全中心](https://cloud.tencent.com/document/product/1087/35082)，则可自动从数据安全中心拉取数据资产及授权信息（含 TencentDB 和 CVM 自建数据库）。
4. 若未开通数据安全中心，您可自行添加资产。在 TencentDB 页面，单击**更新资产列表**列表更新后，单点操作栏中的**授权配置**进行授权配置。
![](https://main.qcloudimg.com/raw/37cddc4b7c6cafb67bfd865162101cd4.png)
5. 单击 **CVM 自建数据库**，切换 CVM 自建数据库页面，可手工添加数据库。
6. 在 CVM 自建数据库页面，单击**添加数据资产**，在弹出添加数据资产弹窗。
![](https://main.qcloudimg.com/raw/6c6cf95cc8273384ca876f61752b4d36.png)
7. 在添加数据资产弹窗，选择 CVM，输入对应的信息，即可完成添加及授权。
8. 在 CVM 自建数据库页面，单击操作栏中的**授权配置**，可进行配置修改。
![](https://main.qcloudimg.com/raw/bb94f63311d80fd628e8f8d09761290c.png)

### 创建脱敏任务
1. 登录 [数据脱敏控制台](https://console.cloud.tencent.com/dmask)，单击**立即进入**。
![](https://main.qcloudimg.com/raw/60a319796a70211e29bfcba394e2f7e7.png)
2. 进入数据脱敏服务后，在左侧导航栏中，单击**脱敏任务** > **任务管理**，进入任务管理页面。
3. 在任务管理页面，单击**新建脱敏任务**，进入新建脱敏任务页面。
![](https://main.qcloudimg.com/raw/9cd7ead63428b33ec99bafd7315f458d.png)
4. 在新建脱敏任务页面，根据任务创建向导提示，分步骤操作，即可完成脱敏任务的创建。
![](https://main.qcloudimg.com/raw/6e980e83077bd37393eebd83e6c85b35.png)
5. 脱敏任务执行完成后，可单击进入**任务运行状况**页面查看任务执行详情，并到脱敏目标库中查看脱敏结果。
