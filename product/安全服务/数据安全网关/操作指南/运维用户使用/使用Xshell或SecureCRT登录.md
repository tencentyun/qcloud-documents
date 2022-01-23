## 操作场景
本文为您详细介绍如何通过 SecureCRT 或 XShell 登录 Linux 资源。

## 前提条件
1. 已下载安装 [控件](https://cloud.tencent.com/document/product/1025/32034)。
2. 拥有访问 Linux 资源权限，若无权限，请联系管理员进行配置。
3. 已安装 SecureCRT 或 XShell。


## 配置路径

1. 控件安装之后，进入到控件安装路径下（默认安装路径为：C:\sso_client）。
2. 找到配置文件 db_path，将之前安装的 Xshell 安装路径复制到文件 xshell= 后，如下图所示。（ SecureCRT 无需添加路径）
![](https://main.qcloudimg.com/raw/ea1f5a7a3aad0abe3fd5010567135942.png)

## 操作步骤

#### 通过 Xshell 登录 

1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/dsgc/bh)。
2. 运维用户登录堡垒机。
3. 单击**授权列表**，进入资源列表页。
4. 找到您需要登录的 Linux 资源，在其右侧单击**登录**，在弹出的窗口中，进行登录配置。
![](https://main.qcloudimg.com/raw/239f131a3f980b3d7a3f9abed9d2d8fc.png)
5. 在配置登录窗口，配置如下：
	- 协议：Linux 资源建议选择 SSH2 协议。
	- 账号：输入 Linux 资源的账号。
	- 口令：输入 Linux 资源账号的密码。
	- 工具：选择 X-Shell 工具。
	- 超时时间：连接 Linux 资源的超时时间，默认为5秒。
![](https://main.qcloudimg.com/raw/28e9dac4a7ea63d0dedfb50e833a7368.png)
5. 确认配置信息无误后，单击**登录**，登录到目标资源后，即可对资源进行运维操作。


#### SecureCRT 如何登录？

1. 打开 SecureCRT。
2. 单击**选项** > **全局选项**。
3. 单击**终端** > **网页浏览器**，进入网页浏览器设置页面。
4. 将 SSH2，SSH1 和 Telnet 选项，设置为 “设置SecureCRT为你的默认xxx工具”。
![](https://main.qcloudimg.com/raw/e20d05f9b29b0d9b9fea61ebfdf6498b.png)
5. SecureCRT 设置完毕后，在运维界面登录 Linux 资源时，选择连接工具 SecureCRT 即可。


