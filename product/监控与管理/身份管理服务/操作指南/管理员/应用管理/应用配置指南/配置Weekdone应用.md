## 操作场景
当企业需要管理 Weekdone 资源时，管理员可以在 IDaaS 控制台的“应用管理”模块添加 Weekdone 应用。本文将介绍 Weekdone 的配置方法及相关注意事项。配置成功后，您的企业用户即可登录 Weekdone 进行操作。 

## 前提条件
- 您的腾讯云账号已开通 IDaaS 服务。详情请参见 [开通服务](https://cloud.tencent.com/document/product/1106/36332)。
- 您已有 Weekdone 管理员，并有权限管理 Weekdone。

## 操作步骤
### 创建 Weekdone 应用
1. 管理员登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)。
2. 在左侧导航栏中，单击【应用管理】，进入应用管理页面。
3. 单击【新建应用】，选择【自定义 SAML2.0 应用程序】，并填写应用名称和应用详情。单击【提交】。完成 Weekdone 应用的创建。
![](https://main.qcloudimg.com/raw/607f3fb35868524ec2a963518ba77ce5.png)
4. 记录登录 URL 和注销 URL，并单击【下载证书】。
![](https://main.qcloudimg.com/raw/e01b41647de4c750d71ba9e6c8557cd5.png)

### 配置 Weekdone 单点登录设置
1. 新开页前往 [Weekdone 官网](https://weekdone.com/)，登录您的管理员账号。
2. 顶部导航右上角个人头像下拉菜单里，单击设置一栏。
3. 单击【Single-sign-on (SAML2)】。
4. 填写在腾讯云 IDaaS 创建的 Weekdone 应用信息：
![](https://main.qcloudimg.com/raw/d96835701707f975e42ba24a3cfca598.png)
	- SAML 名称：您可以随意设置您的 SAML 名称，例如 IDaaS。
	- SAML 登录网址：您在【创建Weekdone应用】第4步里准备的登录 URL，如下图所示。
	- SAML 登出网址：您在【创建Weekdone应用】第4步里准备的注销 URL，如下图所示。
	- X509认证：	输入您在【创建 Weekdone 应用】下载的证书，打开证书内容并复制在 X509 认证文本框内。
![](https://main.qcloudimg.com/raw/49d4cf5bcf910572778953c47b14fefb.png)

### 配置 Weekdone 应用信息
1. 返回 Weekdone 配置页面，配置应用程序 SAML 配置。
	- 应用程序 ACS URL：您在【配置Weekdone单点登录设置】第4步里填写的SAML名称，本案例即为：`https://weekdone.com/a/tencent-idaas`
	- 应用程序 SAML 受众：您在【配置Weekdone单点登录设置】第4步里填写的SAML名称，本案例即为：`https://weekdone.com/a/tencent-idaas`
![](https://main.qcloudimg.com/raw/46eec05ae0b2133612103df79b31f05a.png)


2. 配置应用程序属性值
由于 Weekdone 使用邮箱作为用户标识，您需要修改属性 NameID 的值为 ${user:Email}。如下图所示：
![](https://main.qcloudimg.com/raw/41e566c9176e4ef0424b0b960d748c46.png)

### 测试并分配权限
1. 为应用关联一个用于测试的用户，且该用户的邮箱需和 Weekdone 应用里用户邮箱匹配。关联用户步骤可参见 [管理应用权限](https://cloud.tencent.com/document/product/1106/36361)。
2. 测试用户登录 IDaaS 企业门户，尝试访问 Weekdone 应用。
3. 若访问成功即可关联其他用户，设置应用访问权限。
>!IDaaS 门户的用户邮箱必须和 Weekdone 应用的用户邮箱匹配。
