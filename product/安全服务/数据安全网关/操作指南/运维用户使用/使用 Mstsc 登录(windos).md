## 操作场景
Windows 类资源包含两种单点登录方式：图形登录（WEB 登录）、FTP 登录。根据不同的登录协议，选择相应的登录工具。

该指南指导运维用户在登录堡垒机系统后，通过调用本地 Mstsc 登录 Windows 资源。用户在资源上执行的操作能够被堡垒机记录并生成相关的审计数据。



## 前提条件
1. 已下载安装 [控件](https://cloud.tencent.com/document/product/1025/32034)。
2. 拥有访问 Windows 资源权限，若无权限，请联系管理员进行配置。


## 操作步骤

1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/dsgc/bh)。
2. 运维用户登录堡垒机系统。
3. 单击【授权列表】，进入资源列表页。
4. 找到您需要登录的 Windows 资源，在其右侧单击【登录】，进行登录配置。
![](https://main.qcloudimg.com/raw/1d3663b79d1db2d3484fff9e5dec48bb.png)
5. 在配置窗口中，配置如下。
 - **协议**：选择“RDP”，Windows 默认远程协议使用 RDP。
 - **账号**：输入 Windows 的系统账号。
 - **口令**：输入 Windows 账号的密码。
 - **工具**：选择 RDP 工具。
 - **选择分辨率**：远程登录 Windows，其窗口的分辨率。
 - **超时时间**：连接 Windows 资源的超时时间，默认为5秒。
![](https://main.qcloudimg.com/raw/2556d8076152d338daa56e5ecbbe6f85.png)
5. 确认配置信息无误后，单击【登录】，系统将根据配置，调用本地的 Mstsc 连接到目标资源。


