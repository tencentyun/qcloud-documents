## 操作场景
本文介绍如何在 Linux 及 Mac OS 系统的本地机器上使用 FTP 服务，将文件从本地上传到腾讯云轻量应用服务器中。

## 前提条件
已在轻量应用服务器中搭建 FTP 服务。具体操作请参考 [Linux 轻量应用服务器搭建 FTP 服务](https://cloud.tencent.com/document/product/1207/47638)。

## 操作步骤
### 获取公网 IP
登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在“服务器”页面中获取需上传文件轻量应用服务器的公网 IP。

### Linux 系统使用 FTP 服务
1. 执行以下命令，安装 ftp。
>? 若 Linux 系统的本地机器已安装了 ftp，请跳过此步骤，执行下一步。
>
```
yum -y install ftp
```
2. 执行以下命令，在本地机器上连接轻量应用服务器，并根据界面提示，输入 FTP 服务的用户名和密码。
```
ftp 轻量应用服务器的 IP 地址
```
进入如下界面，即表示连接成功。
![](https://main.qcloudimg.com/raw/9d93f45167addf70e023a21543af59f8.png)

#### 上传及下载文件
<dx-tabs>
::: 上传文件
执行以下命令，将本地文件上传至轻量应用服务器中。
```
put local-file [remote-file]
```例如，将本地文件 `/home/1.txt` 上传到轻量应用服务器。
```
put /home/1.txt 1.txt
```
:::
::: 下载文件
执行以下命令，将轻量应用服务器中的文件下载至本地。
```
get [remote-file] [local-file]
```例如，将轻量应用服务器中的 `A.txt` 文件下载到本地的 `/home` 目录下。
```
get A.txt /home/A.txt
```
:::
</dx-tabs>

### Mac OS 系统使用 FTP 服务
1. 单击左下角的 <img src="https://main.qcloudimg.com/raw/992cc18057d7ab31bcc0c01cb571d395.png" style="margin:-5px 0px; width:4%">，在右上角菜单栏中选择【前往】>【连接服务器...】。
2. 在“连接服务器”窗口中输入 `ftp://轻量应用服务器的 IP 地址`，并单击【连接】。如下图所示：
![](https://main.qcloudimg.com/raw/0cb8e99214441e8ea93db3cf25867cd5.png)
3. 在弹出的窗口中选择“注册用户”，输入 ftp 服务的用户名和密码后单击【连接】。
进入如下界面，即表示连接成功。
![](https://main.qcloudimg.com/raw/9551fbefacded0216cf55b6fe69e2762.png)

#### 上传及下载文件
您可直接将文件复制至 FTP 访达窗口，即可完成文件上传操作。
如需将轻量应用服务器中的文件下载至本地计算机，也可以参照上传文件的操作，将所需文件从轻量应用服务器中复制到本地硬盘中，即可完成文件下载操作。
