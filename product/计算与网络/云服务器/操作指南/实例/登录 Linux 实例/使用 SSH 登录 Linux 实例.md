## 操作场景
本文介绍如何在 Linux、Mac OS 或者 Windows 系统的本地电脑中通过 SSH 登录 Linux 实例。

## 适用本地操作系统
Linux、Mac OS 或 Windows（Windows 10 和 Windows Server 2019 版本）

## 鉴权方式
**密码**或**密钥**

## 前提条件
- 已获取登录实例的管理员帐号及密码（或密钥）。
 - Linux 实例管理员帐号通常默认为 `root`，Ubuntu 系统默认为 `ubuntu`。您需结合实际情况修改。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您 [使用密钥登录](#LoginWithKey) 实例，需完成密钥的创建，并已将密钥绑定至该云服务器中。 具体操作请参看 [SSH 密钥](https://cloud.tencent.com/document/product/213/16691)。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
- 您的云服务器实例已购买公网 IP，且该实例已开通云服务器实例的22号端口（对于通过快速配置购买的云服务器实例已默认开通）。

## 操作步骤
<dx-tabs>
::: 使用密码登录[](id:passwordLogin)
1. 执行以下命令，连接 Linux 云服务器。
<dx-alert infotype="explain" title="">
- 如果您的本地电脑为 Mac OS 系统，需先打开系统自带的终端（Terminal），再执行以下命令。
- 如果您的本地电脑为 Linux 系统，可直接执行以下命令。
- 如果您的本地电脑为 Windows 10 或 Windows Server 2019 系统，需先打开命令提示符（CMD），再执行以下命令。
</dx-alert>
```
ssh <username>@<hostname or IP address>
```
 - `username` 即为前提条件中获得的默认帐号。
 - `hostname or IP address` 为您的 Linux 实例公网 IP 或自定义域名。
2. 输入已获取的密码，按 **Enter**，即可完成登录。

:::
::: 使用密钥登录[](id:LoginWithKey)
1. 执行以下命令，赋予私钥文件仅本人可读权限。
 - 如果您的本地电脑为 Mac OS 系统，需先打开系统自带的终端（Terminal），再执行以下命令。
 - 如果您的本地电脑为 Linux 系统，可直接执行以下命令。
```
chmod 400 <下载的与云服务器关联的私钥的绝对路径>
```
 - 如果您的本地电脑为 Windows 10 系统，需先打开命令提示符（CMD），再依次执行以下命令。
```
icacls <下载的与云服务器关联的私钥的绝对路径> /grant <Windows 系统用户帐户>:F
``` ```
icacls <下载的与云服务器关联的私钥的绝对路径> /inheritancelevel:r
```
2. 执行以下命令，进行远程登录。
```
ssh -i <下载的与云服务器关联的私钥的绝对路径> <username>@<hostname or IP address>
```
 - `username` 即为前提条件中获得的默认帐号。
 - `hostname or IP address` 为您的 Linux 实例公网 IP 或自定义域名。

 例如，执行 `ssh -i "Mac/Downloads/shawn_qcloud_stable.pem" ubuntu@192.168.11.123` 命令，远程登录 Linux 云服务器。
:::
</dx-tabs>

## 后续操作

当您成功登录云服务器后，您可以在腾讯云服务器上搭建个人站点，论坛或者使用其他操作。相关操作可参考：
- [搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/34064)
- [搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/34065)


