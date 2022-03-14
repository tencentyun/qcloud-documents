## 操作场景
该指南指导运维用户在登录堡垒机系统后，使用图形方式登录 Linux 资源进行操作。用户在资源进行的运维操作，能够被堡垒机记录并生成相关的审计数据。

## 前提条件
1. 已下载安装 [控件](https://cloud.tencent.com/document/product/1025/32034)。
2. 拥有访问 Linux 资源权限，若无权限，请联系管理员进行配置。


## 操作步骤

1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/dsgc/bh)。
2. 运维用户登录堡垒机。
3. 单击【授权列表】，进入资源列表页。
4. 找到您需要登录的 Linux 资源，在其右侧单击【登录】，在弹出的窗口中，进行登录配置。
![](https://main.qcloudimg.com/raw/949b357bb91840f7e18b745cfae30fe5.png)
5. 在配置登录窗口，配置如下：
	- 协议：Linux 资源建议选择 SSH2 协议。
	- 账号：输入 Linux 资源的账号。
	- 口令：输入 Linux 资源账号的密码。
	- 工具：选择 PuTTY 工具。
	- 超时时间：连接 Linux 资源的超时时间，默认为5秒。
![](https://main.qcloudimg.com/raw/c5a7cb91e6eb2d399318b4996d03c3d1.png)
5. 确认配置信息无误后，单击【登录】，登录到目标资源后，即可对资源进行运维操作。
![](https://main.qcloudimg.com/raw/7a86fc23bcbab13e6960024c5fcd17b7.png)

