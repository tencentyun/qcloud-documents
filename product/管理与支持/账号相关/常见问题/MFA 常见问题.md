### 什么是 MFA 设备？
MFA (Multi-FactorAuthentication)即多因子认证，是一种简单有效的安全认证方法，它能够实现在用户名和密码之外再增加一层保护。MFA 设备（又叫动态口令卡或 token 卡）是提供这种安全认证方法的设备。目前腾讯云提供两种MFA设备： 硬件 MFA 设备 和 虚拟 MFA 设备 。

### 如何绑定虚拟 MFA 设备？
1. 登录腾讯云控制台，进入安全设置，在 MFA 设备那一栏上，单击【绑定】。
![图片描述](http://tss.sng.com/ticket/upload/downloadFile?filename=59964c7d8a0cc.png)

2. 在弹出来的页面中，单击【发送验证码】，收到验证码后，将6位数字验证码输入框内。
![图片描述](http://tss.sng.com/ticket/upload/downloadFile?filename=59964c8b5deff.png)

3. 在弹出来的页面中，依次按照图片中的步骤进行操作。
![图片描述](http://tss.sng.com/ticket/upload/downloadFile?filename=59964c9801d11.png)

4. 将手机中的应用程序出现的连续的安全码输入到框内，安全码每 30 秒更新一次。
![图片描述](http://tss.sng.com/ticket/upload/downloadFile?filename=59964ca455f73.png)

5. 选择您想启用的范围，您可以选择登录保护，也可以选择操作保护，只需要在你想选择的范围前面勾选出来即可，可多选。选择完之后，单击【提交】。
![图片描述](http://tss.sng.com/ticket/upload/downloadFile?filename=59964cafa58f1.png)

### 如何绑定 MFA 设备？
目前腾讯云提供的硬件 MFA设备为“腾讯云安全令牌”，也叫动态口令卡或 token 卡，首批 token 卡采用内测的形式发放给客户，照片如图所示（不同版本可能在外观上有差异）
![图片描述](http://tss.sng.com/ticket/upload/downloadFile?filename=59964dcfbf3bb.png)
主要有以下几个步骤：
1. 进入用户中心>账户信息>安全设置，单击【绑定】按钮。
![图片描述](http://tss.sng.com/ticket/upload/downloadFile?filename=59964dd7d36c4.png)

2. 弹出身份验证框，输入手机中收到的6位数验证码，单击【确定】按钮。
![图片描述](http://tss.sng.com/ticket/upload/downloadFile?filename=59964de0493df.png)

3. 在绑定 MFA 设备页中选择“硬件MFA设备”，根据提示输入 token 卡背面的序列码（SN 码），和 token 卡正面的 6 位数动态安全码。

 启用范围可勾选也可以不勾选：
- 不勾选则默认您的账户不开启安全保护；
- 勾选登陆保护则登陆后需要验证 token 卡上的安全码；

勾选操作保护则在账户中进行删除云主机，修改安全资料，查看云 API 密钥等敏感操作前需要验证 token 卡上的安全码;
![图片描述](http://tss.sng.com/ticket/upload/downloadFile?filename=59964df234659.png)
信息输入无误后，点击【确认】则绑定完成，绑定成功，并开启登录保护和操作保护的状态如下图所示。
![图片描述](http://tss.sng.com/ticket/upload/downloadFile?filename=59964dfaee048.png)

### 什么是登录保护？
目前腾讯云提供两种登录保护，普通用户采用 QQ 安全中心口令验证方式，内测版用户采用 MFA 口令验证方式（Multi-FactorAuthentication多因子认证）；

开启登录保护后，在登录腾讯云官方网站时需要验证身份。这样即使他人盗取您的密码，也无法登录您的帐号，能够最大限度地保证您的帐号安全。
- 普通用户采用 QQ 安全中心口令验证，输入 QQ 安全中心工具栏顶部的 6 位动态安全码即可完成身份验证。
- 内测用户采用 MFA 口令验证，输入对应帐号的 MFA 设备上的 6 位动态安全码即可完成身份验证。

开启登陆保护后，即使密码泄漏，也能最大限度的保证您的帐号安全。

