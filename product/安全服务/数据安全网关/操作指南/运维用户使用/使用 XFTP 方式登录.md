## 操作场景
该指南指导运维用户在登录堡垒机系统后，使用 XFTP 方式登录 Windows 资源进行操作，通过 XFTP 工具能够上传下载文件。用户上传下载文件能够被堡垒机记录并生成相关的审计数据。

## 前提条件
1. 已下载安装 [控件](https://cloud.tencent.com/document/product/1025/32034)。
2. 已下载安装 WinSCP 工具。
3. 拥有访问 Windows 资源权限，若无权限，请联系管理员进行配置。
4. Windows 资源机使用 XFTP 工具前，需要在 Windows 资源机上部署 FTP 服务。 


## 操作步骤

1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/dsgc/bh)。
2. 运维用户登录堡垒机系统。
3. 单击【授权列表】，进入资源列表页。
4. 找到您需要登录的 Windows 资源，在其右侧单击【登录】，进行登录配置。
![](https://main.qcloudimg.com/raw/1d3663b79d1db2d3484fff9e5dec48bb.png)
5. 在配置窗口中，配置如下。
	- 协议：选择“FTP”。
	- 账号：输入 Windows 的系统账号。
	- 口令：输入 Windows 账号的密码。
>?账号和口令为 [添加资源](https://cloud.tencent.com/document/product/1025/32220) 时设置的账号和口令。
	- 工具：选择 XFTP 工具。
	- 超时时间：连接 Windows 资源的超时时间，默认为5秒。
![](https://main.qcloudimg.com/raw/bf7bdfec613dc093b79c9dbc93a95fdf.png)
5. 确认配置信息无误后，单击【登录】，系统将根据配置，调用本地的 WinSCP 工具连接到目标资源，目标资源连接成功后即可上传、下载文件。

