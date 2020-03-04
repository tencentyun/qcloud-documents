UBA（User Behavior Analysis）是腾讯云安全运营中心对您所有用户的行为分析，用户包括您的主账号、子账号、协作者。
## 前提条件
 UBA 功能目前正在试用中，[开通高级版](https://cloud.tencent.com/document/product/664/41641) 的用户可获得试用资格。
## 操作步骤
1. 登录 [安全运营中心控制台](https://console.cloud.tencent.com/ssav2/account)，在左侧导航栏，单击【UBA】，进入 UBA 页面。
2. 在UBA 页面，如您未进行授权，请单击【前往访问管理】，进入角色管理页面，单击【同意授权】，如您已授权请跳过此步。
3. 授权成功后，根据 UBA 初始化配置流程进行配置。
	1. **创建云审计跟踪集**
		1. 在 UBA 初始化配置第一步，单击【立即前往】，进入 [云审计控制台](https://console.cloud.tencent.com/cloudaudit/audit)。
![](https://main.qcloudimg.com/raw/b67c7263d0611d78d2d58d2c48258dc3.png)
		2. 在云审计控制台，左侧操作栏中，单击【跟踪集】，在跟踪集页面，单击【创建】，打开创建跟踪集页面。
		![](https://main.qcloudimg.com/raw/98ab88c79330a5c33c54608ec4ae4c49.png)
		3. 在创建跟踪集页面，填写跟踪集名称、管理事件（选择全部）及 cos 存储桶位置，填写完成后，单击【完成创建】即可。
		![](https://main.qcloudimg.com/raw/9ba869f1ec824f953369a9e39b2cd7fd.png)
	<span id="fuzhi"></span>
	2. **查看跟踪集存储桶 ID**
		1. 在 UBA 初始化配置第二步，单击【立即前往】，进入 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket)，在左侧导航中，单击【存储桶列表】。
		2. 在存储桶列表中，找到在创建跟踪集时填写的 cos 存储桶，并复制该存储桶名称。
		![](https://main.qcloudimg.com/raw/20886eb9186bc026a41fc7a378e6e81a.png)
	3. **填写对象存储桶 ID**
	在 UBA 初始化配置第三步，填写 [第二步](#fuzhi) 中复制的存储桶名称（即存储桶 ID），填写完成后，单击【完成】即可。
	![](https://main.qcloudimg.com/raw/75b314613318e730c9e13a9432cbb9d6.png)
