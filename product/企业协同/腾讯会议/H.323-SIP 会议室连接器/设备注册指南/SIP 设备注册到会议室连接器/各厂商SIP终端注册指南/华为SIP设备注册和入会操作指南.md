## 概述
华为 SIP 终端可以注册到腾讯会议的会议室连接器，注册成功后，可以直接呼叫会议号码加入到腾讯会议，或通过腾讯会议 App 邀请 SIP 注册设备加入会议。
本指南以华为 TE50 为例说明如何进行 SIP 设备注册操作设置。

## 注册操作步骤
### 创建账号
按链接创建和管理 SIP 注册账号的步骤先创建 SIP 设备注册使用的账号。

### 设备注册
使用终端管理员身份，登录终端的网页管理界面，按下述步骤完成设备注册。
1. 访问**系统配置** > **服务器设置** > **SIP**，在配置详情页选择启用注册服务器。
![](https://qcloudimg.tencent-cloud.cn/raw/c1bf2840b115d6291a4b1545aa91524a.png)
2. 设置服务器地址，腾讯会议的会议室连接器 SIP 注册服务地址：sip.qqmra.com。
![](https://qcloudimg.tencent-cloud.cn/raw/e34a7b5b732a26d293eb54c080da8a11.png)
3. 输入注册信息
 - URI：创建 SIP 注册账号的设置的登录地址，例如：1001_abcd@sip.qqmra.com。
 - 认证用户名：创建 SIP 注册账号时设置的用户名。
 - 认证密码：创建 SIP 注册账号时设置的密码。
 - 服务器类型：选择标准。
 - 传输类型：选择 TCP。

 ![](https://qcloudimg.tencent-cloud.cn/raw/7dc1ab126ad0746653e644f6eaf0aed3.png)
4. 验证注册状态
查看系统状态，在线路状态页面，SIP 的状态显示为**成功注册 SIP 服务器**，则表示注册成功。
![](https://qcloudimg.tencent-cloud.cn/raw/7ad758ee436f132db06e8819f8ce830a.png)

## 注册设备加入会议
### 方法一：SIP 注册设备拨打腾讯会议号码加入会议
1. 在设备主页选择**呼叫/拨打**，进入拨号界面。
2. 在拨号界面输入会议号或会议号 ** 会议密码，例如 607117181 或 607117181**567967，然后加入会议。

### 方法二：腾讯会议 App 邀请 SIP 注册设备加入会议
在腾讯会议 App 中，单击**邀请**，选择 **H.323/SIP 会议室邀请**，切换到 **SIP**选项，输入 SIP 设备注册登录地址（例如1001_abcd）或 URI（例如1001_abcd@sip.qqmra.com）邀请 SIP 注册设备加入会议。
>?只支持邀请本企业的注册设备加入会议。

![](https://qcloudimg.tencent-cloud.cn/raw/a0a0a75108b8bee45fa14a6113d8f3b9.png)
