本文档将指导您如何使用云访问安全代理（CASB）控制台。
## 前提条件
- 需已 [购买开通 CASB 实例](https://cloud.tencent.com/document/product/1303/53298)。
- 需已开通密钥管理系统（KMS）服务并完成 KMS 对云访问安全代理服务的角色授权，详情请参见 [使用 KMS 加密并授权](https://cloud.tencent.com/document/product/1303/48491)。

## 操作步骤
### 步骤一：查看已购买实例
登录 [云访问安全代理控制台](https://console.cloud.tencent.com/casb)，即可在 CASB 实例页面左上角，通过切换地域查看已购买实例。
> ?同一个地域仅支持购买一个实例。
> ![](https://main.qcloudimg.com/raw/70581925a1e8283af17ade35fe004837.png)
> 
### 步骤二：账户初始化设置（可选）
1. 登录 [云访问安全代理控制台](https://console.cloud.tencent.com/casb)，在 CASB 实例页面右下角，单击【初始化】，进行初始化操作。
	>?
	>- 仅首次使用 CASB 实例需要进行以下操作。
	>- 初始化操作需要3分钟 - 10分钟，初始化完成后，实例处于正常服务状态。
	
	![](https://main.qcloudimg.com/raw/aaba316df48c3e2515893dc178dd371d.png)
2. 初始化完成后初次使用，在 [实例列表](https://console.cloud.tencent.com/casb) 右侧操作栏，选择单击【登录】，进入“设置管理平台密码”页面，修改初始密码。
	![](https://main.qcloudimg.com/raw/76bbe18a73e2dd526a75d9f6404176f1.png)

	>?后续可在实例列表右侧操作栏，选择【更多】>【重置管理平台密码】，修改管理员密码。
	>
	>![](https://main.qcloudimg.com/raw/b86ad79d0cc4e7293c448e75770e95b4.png)、

### 步骤三：设置基本信息
1. 实例初始化后，在 [实例列表](https://console.cloud.tencent.com/casb) 左侧操作栏，单击 ID/名称处的“实例名”，进入“基本信息”页面。
![](https://main.qcloudimg.com/raw/f650193f1b85df3aed750a8c61e6862b.png)
4. 在“基本信息”页面中，可查看实例的基本信息并可进行相关操作。
	![](https://main.qcloudimg.com/raw/b3e92c474ffb69d8959de567430e2d11.png)
	字段说明：
	- **实例 ID**：购买实例后，系统自动生成的唯一 ID。
	- **实例名称**：系统默认的名称为 casb-default，您可以通过修改名称，给实例进行命名。
	- **地域**：实例所在地域。
	- **服务版本**：CASB 目前提供三个版本分别是：标准版、企业版、旗舰版。
	- **数据库实例数**：由版本提供实例数与扩展实例数组成。
	- **自动续费**：用户可设置自动续费或关闭自动续费，关闭自动续费的实例到期后，将会被系统自动回收。
	- **状态**：实例发货后，实例处于未初始化状态，单击账户设置【初始化】发起初始化操作，操作需要3分钟 - 10分钟，初始化完成后，实例处于正常服务状态。
	- **私有网络及所属子网**：可更换需要部署 CASB 加密服务的私有网络和子网，选择用于部署 CASB 服务的 VPC 环境，用户必须同一个 VPC 环境下，才能登录到 [CASB 管理平台](https://cloud.tencent.com/document/product/1303/48548)。

### 步骤四：设置安全组
1. 基本信息设置完成后，在 [实例列表](https://console.cloud.tencent.com/casb) 左侧操作栏，单击 ID/名称处的“实例名”，进入“基本信息”页面。
2. 在基本信息页面右上角操作栏中，单击【安全组】进入安全组页面。
![](https://main.qcloudimg.com/raw/0115a337644a15dd919dec2b54fabc4c.png)
3. 在安全组页面中，单击【编辑】，进入“绑定安全组”页面。
![](https://main.qcloudimg.com/raw/9f7d77b56fbb5c28e6602448befaac17.png)
4. 在绑定安全组页面中，选择所需的安全组，单击【确定】即完成安全组配置。
> !在进行操作前，需已完成安全组配置，详情请参见 [创建安全组](https://cloud.tencent.com/document/product/215/20398)。
> 
![](https://main.qcloudimg.com/raw/f5de699737a94153c0b6e57a43796205.png)
5. 完成安全组配置后，单击“入站规则”或“出站规则”，即可预览“入站规则”及“出站规则”。
![](https://main.qcloudimg.com/raw/71cb60af0b0f838e9ad148f6129719d9.jpg)

### 步骤五：设置Proxy 资源
1. 在 [实例列表](https://console.cloud.tencent.com/casb) 左侧操作栏，选择单击 ID/名称处的“实例名”，进入“基本信息”页面。
2. 在基本信息页面右上角操作栏中，单击【Proxy 资源】进入 Proxy 资源页面，在该页面可查看 Proxy 资源的相关信息。
>?在进行 Proxy 资源绑定操作之前，需要先创建关系元数据，创建完成之后才能进行 Proxy 的绑定。
>对于关系元数据的创建，详情请查阅 [**添加云元数据**](https://cloud.tencent.com/document/product/1303/55925) 或 [**添加自建元数据**](https://cloud.tencent.com/document/product/1303/55926) 。
