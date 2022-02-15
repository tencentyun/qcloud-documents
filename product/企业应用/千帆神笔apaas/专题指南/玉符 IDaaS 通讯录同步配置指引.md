## 操作场景

千帆玉符 IDaaS 是千帆应用连接器的重要组成部分，聚焦于企业各系统应用间统一用户、统一身份认证、单点登录等功能，用于实现一个账号登录所有应用。
本文适用于客户用户数据已经同步至玉符 IDaaS 的场景，您可以通过下文配置将玉符 IDaaS 作为神笔应用连接器用户数据源。

## 操作步骤

### 千帆玉符人员同步

1. 登录 [千帆神笔 aPaaS 运行态首页](https://apaas.weworkpro.tencent-cloud.com/1475709344300523568/main/)（即神笔应用中心），单击管理后台按钮，进入管理后台页面。
![1643096827858](https://qcloudimg.tencent-cloud.cn/raw/cca5bdc97ccc585a9f170500f28075a8.png)
2. 在管理后台的左侧导航栏中，单击**用户管理**，选择千帆玉符人员组织架构。
	- 首次进行人员组织初始化时，进入下图页面。对于用户管理的基本介绍可参考 [用户管理](https://cloud.tencent.com/document/product/1365/67915)。
![](https://qcloudimg.tencent-cloud.cn/raw/a91f3695f3ad1b2d7915d352e80cd2a8.png)
	- 切换人员组织架构时，会进入以下页面，单击**其他用户来源**，选择千帆玉符同步。
	![](https://qcloudimg.tencent-cloud.cn/raw/5a2235e90b6beb04b7a11182e4c1f373.png)
3. 进行千帆玉符人员同步信息填写。
![](https://qcloudimg.tencent-cloud.cn/raw/bdc45073f9f1ff74334297e7a41637c0.png)


### 获取玉符 Domain

1. 登录千帆玉符管理后台。
>?
>- 如需开通千帆玉符账号，请发送邮件至 v_vyingguo@tencent.com，我们会尽快安排工作人员为您开通。
>- 线下开通后，每位租户会有一个独立的登录链接，由工作人员提供 。
>
![](https://qcloudimg.tencent-cloud.cn/raw/aa20be08ac5f1c66baa11720084b9a7a.png)
2. 从地址栏获取 Domain 信息，并将其填入配置页面对应字段。
例如：`https://apaas-test-admin.cig.tencentcs.com/#/，-admin` 前面的 apaas-test 即为 Domain。
![img](https://main.qcloudimg.com/raw/3967e9a1a5eda7074e60e3789ab87141.png)


### 获取玉符 Service Account

请联系千帆玉符工作人员，并提供千帆玉符独立的登录链接和用户名，根据所在租户的 Service Account 信息，并将其填入配置页面对应字段。


### 创建玉符 OIDC 类型应用

1. 登录千帆玉符管理后台，在左侧导航栏单击**应用** > **应用管理**，进入应用管理页面。
2. 在应用管理页面，单击**添加应用**。
![](https://qcloudimg.tencent-cloud.cn/raw/09363a0dc61e2a7a38f8e102a962121a.png)
3. 在添加应用页面，单击**创建自定义应用**，进入创建应用页面。
![](https://qcloudimg.tencent-cloud.cn/raw/eb1bf8fc2a224501458e1a4bd6b15099.png)
4. 选择 OpenID Connect 类型。
![](https://qcloudimg.tencent-cloud.cn/raw/e99c727dcabcdba523adec7c0232f4de.png)
5. 选择适用的应用平台。
![](https://qcloudimg.tencent-cloud.cn/raw/44f3752cb0488ad8359dba6aca93efa8.png)
6. 填写应用基本信息，单击**确定**，完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/1100e9bbe8e969d15b85a46493d98310.png)


### 获取应用 Well-known 接口、 Clicent ID 和 Clicent  Secret  

1. 登录千帆玉符管理后台，在左侧导航栏单击**应用** > **应用管理**，进入应用管理页面。
2. 在应用管理页面，单击已经创建完成的 OIDC 类型应用，进入应用详情页。
![](https://qcloudimg.tencent-cloud.cn/raw/c1ed6ffc9dc81616d26900711ca5f518.png)
3. 在应用详情页，单击**常规配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/1eac30d82e304c8b07bd09c75cfdf803.png)
4. 在登录常规配置窗口，您可以查看 Well-kown 接口地址、Client ID 和 Client Secret 等信息。单击复制图标，并将其填入配置页面对应字段。
![](https://qcloudimg.tencent-cloud.cn/raw/8aa1d955628029b47ea3184bffade260.png)




### 获取回调 URL 和单点登录 URL 地址

1. 登录 [千帆神笔 aPaaS 运行态首页](https://apaas.weworkpro.tencent-cloud.com/1475709344300523568/main/)（即神笔应用中心），从地址栏获取 URL 信息。例如：在 `https://apaas.weworkpro.tencent-cloud.com/1424700660795945054/main/` 中，`https://apaas.weworkpro.tencent-cloud.com/1424700660795945054/` 即为回调 URL 和单点登录 URL 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/244379ab8c70099164df8f94ffca5ae0.png)
2. 并获取的地址填入配置页面对应字段。
![](https://qcloudimg.tencent-cloud.cn/raw/c5ce23b2e8d246595fe2be07186f37f8.png)


### 通讯录同步完成

1、相关千帆玉符信息已配置完成，单击下一步按钮。

![1643099200497](https://qcloudimg.tencent-cloud.cn/raw/eee9b17e8c4aa449f842e0cae2023d60.png)

2、请您耐心等待片刻即可完成通讯的同步。

![1643099909290](https://qcloudimg.tencent-cloud.cn/raw/caa8c60478550f5c71f1c6a651fcd185.png)

3、请设置千帆神笔 aPaaS 平台企业管理员。

![1643100128224](https://qcloudimg.tencent-cloud.cn/raw/036a8f8496f48b162c2b7db5bea4d1a4.png)

 4、千帆玉符人员组织信息同步成功，下次登录神笔平台时，请通过千帆玉符扫码登录。 

![1643102784965](https://qcloudimg.tencent-cloud.cn/raw/de385c5bc184997aec7ae15f4449cace.png)



