## 操作场景
该指南指导运维用户在登录堡垒机系统后，使用 XFTP 方式登录 Linux 资源进行操作，通过 XFTP 工具能够上传下载文件。用户上传下载文件能够被堡垒机记录并生成相关的审计数据。

## 前提条件
1. 已下载安装 [控件](https://cloud.tencent.com/document/product/1025/32034)。
2. 已下载安装 WinSCP 工具。
2. 拥有访问 Linux 资源权限，若无权限，请联系管理员进行配置。


## 操作步骤

1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/dsgc/bh)。
2. 运维用户登录堡垒机系统。
3. 单击【授权列表】，进入资源列表页。
4. 找到您需要登录的 Linux 资源，在其右侧单击【登录】，进行登录配置。
![](https://main.qcloudimg.com/raw/a4f4537bf6615d10d824538b77f407c9.png)
5. 在配置登录窗口，配置如下：
 - 协议：选择 SFTP 协议。
 - 账号：输入 Linux 资源的账号。
 - 口令：输入 Linux 账号的口令。
 - 连接工具：选择 XFTP 工具。
 - 超时时间：连接 Linux 资源的超时时间，默认为5秒。
![](https://main.qcloudimg.com/raw/28628651934b7e638d7f0581e7c9981b.png)
6. 单击【登录】，系统将调用 WinSCP 通过 SFTP 协议登录到 Linux 资源。

