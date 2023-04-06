## 概述
Cisco（思科）SIP 终端可以注册到腾讯会议的会议室连接器，注册成功后，可以直接呼叫会议号码加入到腾讯会议，或通过腾讯会议 App 邀请 SIP 注册设备加入会议。
本指南以思科 Room Kit Mini 为例说明如何进行 SIP 设备注册操作设置。

## 设备注册操作步骤
### 创建账号
按链接创建和管理 SIP 注册账号的步骤先创建 SIP 设备注册使用的账号。

### 设备注册
使用终端管理员身份，登录终端的网页管理界面，按下述步骤完成设备注册。
1. 访问导航栏到 **Setup** > **Configuration** > **NetworkServices**，在配置详情页选择启用 SIP，把 SIP Mode 设为 **On**。
![](https://qcloudimg.tencent-cloud.cn/raw/2a5002421006266d0f7ba7b2e6cc0135.png)
2. 访问导航栏到 **Setup** > **Configuration** > **SIP**，在配置详情页输入注册服务配置信息：
 - DefaultTransport：选择 **TCP**
 - PreferredIPSignaling：IPv4
 - Proxy 1 Address: 腾讯会议会议室连接器的注册服务地址：sip.qqmra.com
 - TlsVerify：Off
 - Type：Standard
3. 输入注册验证信息
 - URI：SIP 注册设备 URI，为注册到会议室连接器的账号信息，例如1001_abcd@sip.qqmra.com。
 - Password：创建账号时设置的验证密码。
 - UserName：创建账号是设置的登录用户名。

![](https://qcloudimg.tencent-cloud.cn/raw/1b8fae6f7f4cba781d243ae77183d3a2.png)
4. 验证注册状态
查看 System Information，如果 SIP 的状态 Status 显示为 **Registered**，则表示注册成功。
![](https://qcloudimg.tencent-cloud.cn/raw/311f8e2b1859a3ef207a82eed892ef7e.png)


## 注册设备加入会议
### 方法一：SIP 注册设备拨打腾讯会议号码加入会议
1. 在设备主页选择**呼叫/拨打**，进入拨号界面。
2. 在拨号界面输入会议号或会议号 ** 会议密码，例如 607117181 或 607117181**567967，然后加入会议。

### 方法二：腾讯会议 App 邀请 SIP 注册设备加入会议
在腾讯会议 App 中，单击**邀请**，选择 **H.323/SIP 会议室邀请**，切换到 **SIP** 选项， 输入 SIP 设备注册登录地址（例如1001_abcd）或 URI（如1001_abcd@sip.qqmra.com）邀请 SIP 注册设备加入会议。
>?只支持邀请本企业的注册设备加入会议。

![](https://qcloudimg.tencent-cloud.cn/raw/4397129a06d67abc08b876eff2fa4896.png)
