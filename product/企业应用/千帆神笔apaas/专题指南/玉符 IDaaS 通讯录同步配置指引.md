## 操作场景

千帆玉符 IDaaS 是千帆应用连接器的重要组成部分，聚焦于企业各系统应用间统一用户、统一身份认证、单点登录等功能，实现一个账号登录所有应用。本文适用于客户用户数据已经同步至玉符 IDaaS 的场景，通过下文配置将玉符 IDaaS 作为神笔应用连接器用户数据源。

## 操作步骤

### 千帆玉符人员同步

1、登录千帆神笔 aPaaS 运行态首页（即神笔应用中心），单击管理后台按钮，进入管理后台。

![1643096827858](https://qcloudimg.tencent-cloud.cn/raw/cca5bdc97ccc585a9f170500f28075a8.png)

2、单击用户管理按钮，选择千帆玉符人员组织架构。

- 首次进行人员组织初始化时，进入下图页面。对于用户管理的基本介绍可参考 [用户管理](https://cloud.tencent.com/document/product/1365/57571)。

![1643097007120](https://qcloudimg.tencent-cloud.cn/raw/b92d379d1d7cca2e90f943fe86e89697.png)

- 切换人员组织架构时，会进入以下页面，单击其他用户来源，选择千帆玉符同步。

![1643097126881](https://qcloudimg.tencent-cloud.cn/raw/7bfc940f024e24a890d5671e2f489130.png)

3、进行千帆玉符人员同步信息填写。

![1643097231311](https://qcloudimg.tencent-cloud.cn/raw/40e2e92515141e310f61b2aa1dd75b66.png)

### 获取玉符 Domain

1、登录千帆玉符管理后台。

说明： 如需开通千帆玉符账号，请发送邮件至v_vyingguo@tencent.com，我们会尽快安排工作人员为您开通；线下开通后，每位租户会有一个独立的登录链接，由工作人员提供 。

![1643097346765](https://qcloudimg.tencent-cloud.cn/raw/a4d0dcdf091f07d51fbd08b7518dfbcd.png)

2、从地址栏获取 Domain 信息，并将其填入配置页面对应字段。例如：`https://apaas-test-admin.cig.tencentcs.com/#/，-admin` 前面的 apaas-test 即为 Domain。
![img](https://main.qcloudimg.com/raw/3967e9a1a5eda7074e60e3789ab87141.png)

### 获取玉符 Service Account

请联系千帆玉符工作人员，并提供千帆玉符独立的登录链接和用户名，根据所在租户的 Service Account 信息，并将其填入配置页面对应字段。

### 创建玉符 OIDC 类型应用

1、登录千帆玉符管理后台，选择进入应用管理页面，并单击添加应用按钮。

![1643098159239](https://qcloudimg.tencent-cloud.cn/raw/2c8dc2ea5d632ee9fe8b8c7fbc2170ef.png)2、单击创建自定义应用按钮，进入创建应用页面。

![1643098275219](https://qcloudimg.tencent-cloud.cn/raw/d989df3a3cd17679ecd58f90b813e683.png)

3、选择 OpenID Connect 类型。

![1643098333290](https://qcloudimg.tencent-cloud.cn/raw/563c9c2db28ce7809e1fde5f66df7cbe.png)

4、选择适用的应用平台。

![1643098380931](https://qcloudimg.tencent-cloud.cn/raw/a5caff245561f352c813629a79472f0b.png)

5、填写应用基本信息，单击确定按钮，完成创建。

![1643098419794](https://qcloudimg.tencent-cloud.cn/raw/ea84805a3bba4049afa51f1fc918a9ee.png)

### 获取应用 Well-known 接口、 Clicent ID 和 Clicent  Secret  

1、登录千帆玉符管理后台，选择已经创建完成的 OIDC 类型应用，并单击进入。

![1643098594936](https://qcloudimg.tencent-cloud.cn/raw/9ffbba633d7ac3ff398584c7f2cae903.png)

2、单击常规配置按钮。

![1643098649674](https://qcloudimg.tencent-cloud.cn/raw/417a15e3446cf9ef86bd1bbc3d44241b.png)

3、获取应用 Well-known 接口地址，并将其填入配置页面对应字段。

![1643098719896](https://qcloudimg.tencent-cloud.cn/raw/fdfe219a4a774dcf89e6c060f9447d75.png)

4、获取应用 Client ID，并将其填入配置页面对应字段。

![1643098893856](https://qcloudimg.tencent-cloud.cn/raw/e34476dcc6b080e19b6ed91eca27ea4e.png)

5、获取应用 Client Secret，并将其填入配置页面对应字段。

![1643098933464](https://qcloudimg.tencent-cloud.cn/raw/852bfd462cc0dcffe53bf9de4e2e4c17.png)

### 获取回调 URL 和单点登录 URL 地址

1、登录千帆神笔 aPaaS 运行态首页（即神笔应用中心），从地址栏获取 URL 信息。例如：`https://apaas.weworkpro.tencent-cloud.com/1424700660795945054/main/` 其中`https://apaas.weworkpro.tencent-cloud.com/1424700660795945054/` 其中即为回调 URL 和单点登录 URL 地址。
![img](https://qcloudimg.tencent-cloud.cn/raw/77cf441032eecbf3b673a5a09d527d2d.png)

2、获取对应地址后，并将其填入配置页面对应字段。

![img](https://qcloudimg.tencent-cloud.cn/raw/f7639c8d18f32096e2d96682b1ad6523.png)

### 通讯录同步完成

1、相关千帆玉符信息已配置完成，单击下一步按钮。

![1643099200497](https://qcloudimg.tencent-cloud.cn/raw/eee9b17e8c4aa449f842e0cae2023d60.png)

2、请您耐心等待片刻即可完成通讯的同步。

![1643099909290](https://qcloudimg.tencent-cloud.cn/raw/caa8c60478550f5c71f1c6a651fcd185.png)3、请设置千帆神笔 aPaaS 平台企业管理员。

![1643100128224](https://qcloudimg.tencent-cloud.cn/raw/036a8f8496f48b162c2b7db5bea4d1a4.png)

 4、千帆玉符人员组织信息同步成功，下次登录神笔平台时，请通过千帆玉符扫码登录。 

![1643102784965](https://qcloudimg.tencent-cloud.cn/raw/de385c5bc184997aec7ae15f4449cace.png)



