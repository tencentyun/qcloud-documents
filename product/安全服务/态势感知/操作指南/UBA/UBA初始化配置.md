用户行为分析（User Behavior Analysis，以下简称为 UBA）是腾讯云安全运营中心对您所有用户的行为分析，用户包括您的主账号、子账号、协作者。
## 前提条件
UBA 功能目前正在试用中，已 [开通安全运营中心高级版](https://buy.cloud.tencent.com/soc) 的用户可获得试用资格。

## 操作步骤
1. 登录 [安全运营中心控制台](https://console.cloud.tencent.com/ssav2/account)，在左侧导航栏，单击**用户行为分析**，进入 用户行为分析页面。
2. 如您未创建服务预设角色并授予安全运营中心相关权限，在 UBA 概览页，单击**前往访问管理**，进入角色管理页面，单击**同意授权**即可，如您已授权请跳过此步。
3. 创建云审计跟踪集
>!创建云审计跟踪集时，需在云审计所支持的区域进行创建。您可登录 [云审计控制台](https://console.cloud.tencent.com/cloudaudit/audit) ，单击**创建**，在“存储位置”中查看云审计所支持的区域。
>
	1. 在创建云审计跟踪集页面，单击**立即前往**，进入 [云审计控制台](https://console.cloud.tencent.com/cloudaudit/audit)。
![](https://main.qcloudimg.com/raw/b67c7263d0611d78d2d58d2c48258dc3.png)
	2. 在云审计控制台，左侧导航栏中，单击**跟踪集**，在跟踪集页面，单击**创建**，打开创建跟踪集页面。
		![](https://main.qcloudimg.com/raw/98ab88c79330a5c33c54608ec4ae4c49.png)
	3. 在创建跟踪集页面，填写跟踪集名称、管理事件（选择全部，包含只读和只写）及 cos 存储桶位置，填写完成后，单击**完成新建**即可。
	>!请选择云审计支持的区域创建跟踪集存储桶。存储桶 ID 必须和 soc 侧的存储桶 ID 配置一致，否则不可用。
	>
	![](https://main.qcloudimg.com/raw/9ba869f1ec824f953369a9e39b2cd7fd.png)
4. [查看跟踪集存储桶 ID](id:fuzhi)
	1. 在查看跟踪集存储桶 ID 页面，单击**立即前往**，进入 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket)。
		![](https://main.qcloudimg.com/raw/6cb155c15c49842a65b3b58522de747b.png)
	2. 在对象存储控制台的左侧导航中，单击**存储桶列表**。
	3. 在存储桶列表中，找到在创建跟踪集时填写的 cos 存储桶，并复制该存储桶名称。
		![](https://main.qcloudimg.com/raw/20886eb9186bc026a41fc7a378e6e81a.png)
5. 填写对象存储桶 ID。在填写对象存储桶 ID 页面，填写 [第四步](#fuzhi) 中复制的存储桶名称（即存储桶 ID），填写完成后，单击**完成**即可。
>!请确保您填写的存储桶为公有读写权限。
>
![](https://main.qcloudimg.com/raw/75b314613318e730c9e13a9432cbb9d6.png)
6. 修改存储桶 ID。初始化完成后，如您需要修改存储桶 ID，可登录 [安全运营中心控制台](https://console.cloud.tencent.com/ssav2/setting)，在左侧导航中单击**产品设置**，进入产品设置页面，选择**通用设置**>**UBA 初始化配置**，重新填写存储桶 ID。
![](https://main.qcloudimg.com/raw/9530ff52d8a44a015a4fb928aec11ec8.png)
>!新存储桶 ID 保存成功后，新存储桶对应的 UBA 数据更新可能会延迟6小时，数据更新速度受数据量的影响。


## 后续操作
UBA 初始化配置完成后，进入 [UBA 概览](https://cloud.tencent.com/document/product/664/41791) 及 [用户列表](https://cloud.tencent.com/document/product/664/41792) 进行操作。
