## 操作场景

本文档指导您如何在 Windows 系统的本地机器上使用 FTP 服务，将文件从本地上传到云服务器中。

## 前提条件

已在云服务器中搭建 FTP 服务。
- 如果您的云服务器为 Linux 操作系统，具体操作请参考 [Linux 云服务器搭建 FTP 服务](https://cloud.tencent.com/document/product/213/10912)。
- 如果您的云服务器为 Windows 操作系统，具体操作请参考 [Windows 云服务器搭建 FTP 服务](https://cloud.tencent.com/document/product/213/10414)。


## 操作步骤

### 连接云服务器
1. 在本地下载并安装开源软件 FileZilla。
>? 使用 3.5.3 版本的 FileZilla 进行 FTP 上传将会出现上传失败等问题，建议您从官方网站获取与使用 FileZilla 的 3.5.1 或 3.5.2 版本。
>
2. 打开 FileZilla。
3. 在 FileZilla 窗口中，填写主机、用户名、密码和端口等信息，单击**快速连接**。如下图所示：
![](https://mc.qcloudimg.com/static/img/dc603f912adf94a33749155c69ddddd2/24.png)
**配置信息说明：**
 - 主机：云服务器的公网 IP。在 [云服务器控制台](https://console.cloud.tencent.com/cvm) 的实例管理页面可查看对应云服务器的公网 IP。
 - 用户名：[搭建 FTP 服务](https://cloud.tencent.com/document/product/213/10912) 时设置的 FTP 用户的帐号。图中以 “ftpuser1” 为例。
 - 密码：[搭建 FTP 服务](https://cloud.tencent.com/document/product/213/10912) 时设置的 FTP 用户帐号对应的密码。
 - 端口：FTP 监听端口，默认为**21**。
连接成功后即可查看云服务器远程站点文件。

### 上传文件
在左下方的“本地站点”窗口中，右键单击待上传的本地文件，选择【上传】，即可将文件上传到 Linux 云服务器。如下图所示：
>! 
>- 云服务器 FTP 通道不支持上传 tar 压缩包后自动解压，以及删除 tar 包功能。
>- 远程站点路径为上传文件至 Linux 云服务器的默认路径。
>
![](https://main.qcloudimg.com/raw/45cd8f030ca74145b11e6c64203cedf2.png)

### 下载文件
在右下方“远程站点”窗口中，右键单击待下载的云服务器文件，选择【下载】，即可将文件下载到本地。如下图所示：
![](https://main.qcloudimg.com/raw/17fb8472353c4bea5e3c44a3a5b95220.png)


