
## 操作场景
当企业需要管理 Dropbox 资源时，管理员可以在 IDaaS 控制台的“应用管理”模块添加 Dropbox 应用。本文档将介绍 Dropbox 的配置方法及相关注意事项。配置成功后，您的企业用户即可以登录 Dropbox。

## 前提条件
- 您的腾讯云账号已开通 IDaaS 服务。详情请参见 [开通服务](https://cloud.tencent.com/document/product/1106/36332)。
- 您已开通腾讯企业邮服务，能够以管理员身份登录腾讯企业邮。

## 操作步骤
### 创建 Dropbox 应用
1. 管理员登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)。
2. 在左侧导航栏中，单击【应用管理】，进入应用管理页面。
3. 单击【新建应用】，选择【库应用程序】>【Dropbox】，并填写应用名称和应用详情。单击【提交】，完成 Dropbox 应用创建。
4. 记录登录 URL 和注销 URL，并单击【下载证书】。
![](https://main.qcloudimg.com/raw/d8e64e19b3f6fefb92d4ddb7e9ee65f9.png)

### 配置 Dropbox Business 单点登录
1.	新开窗口，登录 Dropbox 管理员控制台。
2.	选择左侧导航【设置】，选择【验证】>【单一登录】 。
3.	配置以下信息，单击【保存】。
![](https://main.qcloudimg.com/raw/b1b1aeed290c648c438063d91d068cd8.png)
身份提供商登入网址：上一步中记录的登录 URL。
身份提供商注销网址：上一步中记录的注销 URL。
X.509 证书：上一步中下载的证书文件。
4. 收集 Dropbox Business 单点登录配置信息。
单点登录的登录网址：
![](https://main.qcloudimg.com/raw/61942f818553db43e63cf995965f06d9.png)
5.	开启 Dropbox Business 单一登录 。
![](https://main.qcloudimg.com/raw/b899a56d8964d3c5df304f0ce8d3f3c2.png)

### 配置腾讯云 SSO 单点登录
1.	转回 IDaaS 控制台。
2.	进入 Dropbox 应用配置内容页。
3.	配置以下单一登录信息。
应用程序启动URL： 填入上一步收集的单点登录的登录网址。
![](https://main.qcloudimg.com/raw/f8e72b8a1b6cc938e11ead6460aae19b.png)
 
## 测试并分配权限
1.	为应用关联一个用于测试的用户。关联用户步骤可参见 [管理应用权限](https://cloud.tencent.com/document/product/1106/36361)。
2.	测试用户登录 IDaaS 企业门户，访问 Dropbox 应用。
3.	若访问成功即可关联其他用户，设置应用访问权限
![](https://main.qcloudimg.com/raw/4c82b93faaef32a83e3978f887ba55a6.png)

