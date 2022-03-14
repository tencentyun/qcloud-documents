## 前提条件
- 已通过多因子身份认证的 [使用申请](https://cloud.tencent.com/apply/p/h6yib8x1nce)。

## 操作步骤
### 步骤1：添加用户名密码登录的 WebApp 应用
1. 进入 [腾讯多因子身份认证平台](https://admin.tencentmfa.com/am/login/login.html)，输入站点管理员的账号密码后，单击**登录**。
![](https://main.qcloudimg.com/raw/6b35e3e91dbeba8717be71d126ef80b0.png)
2. 在左侧导航栏中，单击**双因素认证** > **应用**，进入应用页面。
3. 在本地应用组管理窗口中，单击**添加**，输入任意应用组名，单击**确定**。
>?本文档中使用“DemoWebApp”作为应用组名。
>
![](https://main.qcloudimg.com/raw/fa768124f443e85e3adc9d03dc369512.png)
![](https://main.qcloudimg.com/raw/1c3a366fc732281bcae5240a429261ba.png)
4. 在本地应用组管理窗口中，选择刚刚创建的用户组“DemoWebApp”，并在应用列表管理界面单击**添加**。
![](https://main.qcloudimg.com/raw/6637eaffc693f52027f908364f0f9706.png)
4. 在添加应用弹窗中，输入任意应用名称，设置相关参数，单击**确定**，创建“passwordAuthAPI”应用。 
>!
>- 本文档中使用“passwordAuthAPI”为应用名称。
>- 选择认证策略：DemoPassword。
>- 应用类型：API 调用。
>- 主机地址：输入测试网站的服务器地址。
>- 共享密钥：输入共享密钥，密钥自行设置，建议使用安全性较强的密钥。
>
![](https://main.qcloudimg.com/raw/f1e8bdbb48a8fa9eaa6511a46a0f3400.png)

### 步骤2：添加验证动态口令的 WebApp 应用
1. 在本地应用组管理窗口中，选择刚刚创建的用户组“DemoWebApp”，并在应用列表管理界面单击**添加**。
![](https://main.qcloudimg.com/raw/6637eaffc693f52027f908364f0f9706.png)
2. 在添加应用弹窗中，输入任意应用名称，设置相关参数，单击**确定**，创建“codeAuthAPI”应用。 
>!
>- 本文档中使用“passwordAuthAPI”为应用名称。
>- 选择认证策略：DemoCode。
>- 应用类型：API 调用。
>- 主机地址：输入测试网站的服务器地址。
>- 共享密钥：输入共享密钥，密钥自行设置，建议使用安全性较强的密钥。
>
![](https://main.qcloudimg.com/raw/3b2a32ce2e41cf04a77f6dbe2ce6e997.png)
