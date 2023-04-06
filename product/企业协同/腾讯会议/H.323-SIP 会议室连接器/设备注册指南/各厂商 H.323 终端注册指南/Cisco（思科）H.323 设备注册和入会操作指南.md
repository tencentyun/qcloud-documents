## 概述
Cisco（思科）H.323 终端可以注册到腾讯会议的会议室连接器，注册成功后，可以直接呼叫会议号码加入到腾讯会议或通过腾讯会议 App 邀请 H.323 注册设备加入会议。
本指南以思科 Room Kit Mini 为例说明如何对思科的设备进行 H.323 设备注册操作。

## 设备注册操作步骤
### 创建账号
按链接创建和管理 H.323 注册账号的步骤先创建 H.323 设备注册使用的账号。

### 设备注册
使用终端管理员身份，登录终端的网页管理界面，按下述步骤完成设备注册。
1. 访问导航栏到 **Setup** > **Configuration** > **NetworkServices**，在配置详情页选择启用 H.323，把 H.323 Mode 设为 **On**。
![](https://qcloudimg.tencent-cloud.cn/raw/6e56aad95ea6c79ede8c65720ae9cd1a.png)
2. 输入注册信息：
 - CallSetup Mode：选择 **Gatekeeper**。
 - Encryption KeySize：默认设置。
 - Gatekeeper Address：腾讯会议会议室连接器的注册服务地址：gk.qqmra.com。
 - PortAllocation：默认设置。
3. 输入注册验证信息：
 - LoginName：创建账号时设置的用户名，例如1003。
 - Mode：设置为 **On**。
 - Password：创建账号时设置的密码。
4. 设置注册号码：
 - E.164：创建账号时分配的短号码，例如111003。
 - ID：创建账号时设置的显示名称（也可以不同，不做验证）。

![](https://qcloudimg.tencent-cloud.cn/raw/f9b6317a7beafac1e614d13cdb8ba484.png)
5. 验证注册状态
查看 System Information，如果Status 显示为“Registered”，则表示注册成功。
![](https://qcloudimg.tencent-cloud.cn/raw/e445f621723c461bfdd655ed921e055f.png)

## 注册设备加入会议
### 方法一：H.323 注册设备拨打腾讯会议号码加入会议
1. 在设备主页选择呼叫/拨打，进入拨号界面。
2. 在拨号界面输入会议号或会议号 ** 会议密码，例如 607117181 或 607117181**567967，然后加入会议。

### 方法二：腾讯会议 App 邀请 H.323 注册设备加入会议
在腾讯会议 App 中，单击**邀请**，选择 **H.323/SIP 会议室邀请**，选择 **H.323** 选项，输入 H.323 设备注册短号码（例如：111003）邀请 H.323 注册设备加入会议。
>?只支持邀请本企业的注册设备加入会议。

![](https://qcloudimg.tencent-cloud.cn/raw/5289db8dc95259ccad5808cc4c829ed0.png)
