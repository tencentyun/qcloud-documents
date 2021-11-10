## 前提条件
- 已通过多因子身份认证的 [使用申请](https://cloud.tencent.com/apply/p/h6yib8x1nce)。

## 操作步骤
1. 通过浏览器访问 [登录测试页面](https://admin.demo.tencentmfa.com/index )，输入如下信息：
>?
>- 站点名 (UIN)：输入申请 [开通多因子身份认证服务](https://cloud.tencent.com/document/product/1326/55080) 时使用的腾讯云账户 UIN。 
>- 密码认证应用名：输入用户名密码策略的应用名称。
>- 密码认证密钥：输入用户名密码策略的应用密钥。
>- 动态口令认证应用名：输入动态口令策略的应用名称。
>- 动态口令认证密钥：用户名密码策略的应用密钥。
>
![](https://main.qcloudimg.com/raw/14c244b86dba4a803bfe045f1694517b.png)
2. 单击**登录测试**，进入用户登录页面。 
>!在实际应用场景中，“MFA 配置”界面的全部信息需要在 WebApp 中提前配置好，安全存储于 WebApp 服务器上。供 WebApp 调用 MFA SaaS API 认证接口时使用，终端用户登录时无需此配置页面。 

3. 进入用户登录页面后，输入用户名和密码，单击**登录**，进入多因素认证页面。
>?用户名密码请参见 [创建的测试用户信息](https://cloud.tencent.com/document/product/1326/55081)。
>
![](https://main.qcloudimg.com/raw/cc32fa043ff80e78a3bcb8c68ef68fab.jpg)
5. 在多因素认证页面，输入6位动态口令，单击**验证**。如果口令正确，您将会看到登录成功提示。 
>?动态令牌需要从用户手机中安装的腾讯身份验证器中读取。在之前的步骤中，已经通过扫 描二维码的形式将手机移动令牌与用户账户绑定。 
>
![](https://main.qcloudimg.com/raw/38402d33c1721b1072af2bbbf51e0132.jpg)
