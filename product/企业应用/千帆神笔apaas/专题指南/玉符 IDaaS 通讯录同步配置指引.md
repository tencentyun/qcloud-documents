## 操作场景

千帆玉符 IDaaS 是千帆应用连接器的重要组成部分，聚焦于企业各系统应用间统一用户、统一身份认证、单点登录等功能，用于实现一个账号登录所有应用。 本文适用于客户用户数据已经同步至玉符 IDaaS 的场景，您可以通过下文配置将玉符 IDaaS 作为神笔应用连接器用户数据源。

## 操作步骤

### 千帆玉符人员同步

1. 登录 [千帆神笔 aPaaS 运行态首页](https://apaas.weworkpro.tencent-cloud.com/1475709344300523568/main/)，单击管理后台按钮，进入管理后台页面。 ![1643096827858](https://qcloudimg.tencent-cloud.cn/raw/186536a07992ac48f596be1957b1919d.png)
2. 在管理后台的左侧导航栏中，单击**用户管理**，选择千帆玉符人员组织架构。
   - 首次进行人员组织初始化时，进入下图页面。对于用户管理的基本介绍可参考 [用户管理](https://cloud.tencent.com/document/product/1365/67915)。 ![img](https://qcloudimg.tencent-cloud.cn/raw/cf552d98c0ea5536f8ce11974a534c44.png)
   - 切换人员组织架构时，会进入以下页面，单击**其他用户来源**，选择千帆玉符同步。 ![img](https://qcloudimg.tencent-cloud.cn/raw/2c444d4c58a72aee5335454afba0369d.png)
3. 进行千帆玉符人员同步信息填写。 ![img](https://qcloudimg.tencent-cloud.cn/raw/35b9c3b6189dd16eec91217e76919e43.png)

### 获取玉符 Domain

1. 登录千帆玉符管理后台。
>?
> 如需开通千帆玉符账号，请发送邮件至 [v_vyingguo@tencent.com](mailto:v_vyingguo@tencent.com)，我们会尽快安排工作人员为您开通；线下开通后，每位租户会有一个独立的登录链接，由工作人员提供。

![img](https://qcloudimg.tencent-cloud.cn/raw/1e55c1e39e38113ad8723087950f2fee.png)

2. 从地址栏获取 Domain 信息，并将其填入配置页面对应字段。 例如：`https://apaas-test-admin.cig.tencentcs.com/#/，-admin` 前面的 apaas-test 即为 Domain。
 ![img](https://qcloudimg.tencent-cloud.cn/raw/31d5bf7723e1957c0a89e16fcd79e283.png)

### 获取玉符 Service Account

请联系千帆玉符工作人员，并提供千帆玉符独立的登录链接和用户名，根据所在租户的 Service Account 信息，并将其填入配置页面对应字段。

### 创建玉符 OIDC 类型应用

1. 登录千帆玉符管理后台，在左侧导航栏单击**应用** > **应用管理**，进入应用管理页面。
2. 在应用管理页面，单击**添加应用**。 ![img](https://qcloudimg.tencent-cloud.cn/raw/c2459888f91352cbd2ee26a5c8fdd934.png)
3. 在添加应用页面，单击**创建自定义应用**，进入创建应用页面。 ![img](https://qcloudimg.tencent-cloud.cn/raw/64f83325d7f477491585103ea3d86bc1.png)
4. 选择 OpenID Connect 类型。
 
 ![img](https://qcloudimg.tencent-cloud.cn/raw/b0017b1d0b774e78ce445bad56ef525b.png)

5. 选择适用的应用平台。  
![img](https://qcloudimg.tencent-cloud.cn/raw/5a90963879a885fbd01f34c02a2a8b03.png)

6. 填写应用基本信息，单击**确定**，完成创建。![img](https://qcloudimg.tencent-cloud.cn/raw/d8e8d06644fad3ce01f49f25652e9f29.png)
### 获取应用 Well-known 接口、 Clicent ID 和 Clicent Secret

1. 登录千帆玉符管理后台，在左侧导航栏单击**应用** > **应用管理**，进入应用管理页面。
2. 在应用管理页面，单击已经创建完成的 OIDC 类型应用，进入应用详情页。 ![img](https://qcloudimg.tencent-cloud.cn/raw/e3078b0eb81dfb8ccc3e7d94da9b66bd.png)
3. 在应用详情页，单击**常规配置**。 ![img](https://qcloudimg.tencent-cloud.cn/raw/f90dc4bce11b480a3b67050e2ab9fe9b.png)
4. 在登录常规配置窗口，您可以查看 Well-kown 接口地址、Client ID 和 Client Secret 等信息。单击复制图标，并将其填入配置页面对应字段。 

![img](https://qcloudimg.tencent-cloud.cn/raw/78edd7216599356a31863268e2f8656b.png)

### 获取回调 URL 和单点登录 URL 地址

1. 登录 [千帆神笔 aPaaS 运行态首页](https://apaas.weworkpro.tencent-cloud.com/1475709344300523568/main/)，从地址栏获取 URL 信息。例如：在 `https://apaas.weworkpro.tencent-cloud.com/1424700660795945054/main/` 中，`https://apaas.weworkpro.tencent-cloud.com/1424700660795945054/` 即为回调 URL 和单点登录 URL 地址。
2. 并获取的地址填入配置页面对应字段。
 
 ![img](https://qcloudimg.tencent-cloud.cn/raw/d359b0d97e72009854bc0e5e9899d63a.png)

### 通讯录同步完成

1. 相关千帆玉符信息已配置完成，单击**下一步**按钮。
![1643099200497](https://qcloudimg.tencent-cloud.cn/raw/b97855c50cf69c8f0fe2067c2be94e59.png)
2. 请您耐心等待片刻即可完成通讯的同步。
![1643099909290](https://qcloudimg.tencent-cloud.cn/raw/f1054e6731187813743895f6a0ae426f.png)
3. 请设置千帆神笔 aPaaS 平台企业管理员。
![1643100128224](https://qcloudimg.tencent-cloud.cn/raw/adf9e5de703324f739e25195c8a84979.png)
4. 千帆玉符人员组织信息同步成功，下次登录神笔平台时，请通过千帆玉符扫码登录。
