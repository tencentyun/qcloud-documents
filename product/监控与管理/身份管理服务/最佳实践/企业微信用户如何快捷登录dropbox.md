
随着移动办公、云文档的发展，越来越多的企业、政府将文档放到云端来编辑、存储，云同步文档平台既能保存与复原所有历史文档、实现多人同时编辑文档，又避免了意外导致的重要文档丢失。然而云同步文档平台和移动办公软件往往不在一个厂商体系内，登录方式各不同。例如，云同步文档平台使用 Dropbox，移动办公使用企业微信。Dropbox 使用邮箱登录，企业微信则是用户名密码登录。那么，如何能将企业的移动办公与业务系统更好地融合呢？腾讯云身份管理服务（IDaaS）告诉您答案！

腾讯云 IDaaS 简单配置，一键登录！以企业微信用户登录 Dropbox 为例，展示如何通过腾讯云IDaaS实现便捷访问。
## 开通 IDaaS 服务
1. 企业管理员可 [点此注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。
2. 未进行实名认证的用户，需先完成实名认证。详细认证流程请参见 [实名认证指引](https://cloud.tencent.com/document/product/378/3629) 。
![](https://main.qcloudimg.com/raw/dd0d2d9154f568a579d1a514e8729674.png)
2. 管理员登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)， 选择【开通使用】。
3. 填写门户 URL 以及企业名称后，单击【确定】，即开通 IDaaS 服务成功。
![](https://main.qcloudimg.com/raw/95e53175598bba0a4c913b52d2053771.png)

## 开启企业微信数据源并同步至 IDaaS 目录
1. 管理员登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)，单击【添加数据源】。
![](https://main.qcloudimg.com/raw/a4d86437c1aee10b67bc84cecaa47686.png)
2. 选择企业微信数据源，单击【创建】。
![](https://main.qcloudimg.com/raw/060208519cd276b1824fefd0c0bad447.png)
3. 填写数据源基本信息并设置数据源规则，需要在企业微信管理后台添加应用“数字腾讯业务系统”。具体配置请参见 [企业微信认证源配置](https://cloud.tencent.com/document/product/1106/41094)。
![](https://main.qcloudimg.com/raw/f50966390bf62e5ad6c13dce986f0aca.png) 
4. 企业微信数据源创建成功，单击【同步】。
![](https://main.qcloudimg.com/raw/44b83a8bcacc85c84aab968abc8517ca.png)
	可以看到企业微信的目录已同步至 IDaaS 目录中。
 ![](https://main.qcloudimg.com/raw/5ff142a53c2e9fbf61e66dd55c960b5c.png)
 ![](https://main.qcloudimg.com/raw/56b3bb4c396568b293651b7e08031443.png)
 
## 新建 Dropbox 应用并配置 
1. 应用管理页面，选择【新建应用】。
![](https://main.qcloudimg.com/raw/8bc38ce4df735eec4cd8ace4047dff9b.png)
2. 库应用程序中选择 Dropbox，输入应用名称，单击【提交】，即创建 Dropbox 应用成功。  
![](https://main.qcloudimg.com/raw/78dab7f6c8ef8dd45848b73c6ebcee7e.png)
3. 在 IDaaS 控制台和 Dropbox 管理后台进行相关配置，并关联企业微信用户。具体配置方法请参见 [配置 Dropbox](https://cloud.tencent.com/document/product/1106/47020)。
![](https://main.qcloudimg.com/raw/34763f0dcc7cb1949177d351fd2e33bf.png)
![](https://main.qcloudimg.com/raw/a8c922f63238a6b2e61ba0cc29cfd645.png) 
![](https://main.qcloudimg.com/raw/ec9a32b0cfe282c37f0301b777cc451a.png)

## 使用 Dropbox
配置成功！现在就可以使用您的企业微信账号登录到业务系统，使用 Dropbox 应用啦！
![](https://main.qcloudimg.com/raw/3d79e85cc3e0c41607d13da33258e737.png)
![](https://main.qcloudimg.com/raw/5972d1ee4992f2a571b7361fac852a62.png)
![](https://main.qcloudimg.com/raw/e67d70a3c04f50d40e29ff3deaf82dd1.png)

>! 腾讯云 IDaaS 还支持腾讯云账号、AD 数据源，支持多种预置应用（如腾讯企业邮、AWS、Salesforce 等）与自定义应用配置，您可结合自身业务需要进行选择。

