## 操作场景
本文介绍如何在 Linux、Mac OS 或者 Windows 系统的本地计算机中通过 SSH 登录 Linux 轻量应用服务器实例。

## 适用本地操作系统
Linux、Mac OS 或 Windows（Windows 10 和 Windows Server 2019 版本）

## 鉴权方式
**密码**或**密钥**

## 前提条件[](id:Prerequisites)
- 您已获取登录实例的用户名（自定义用户名或默认用户名 root）及密码（或密钥）。
<dx-alert infotype="notice" title="">
首次通过本地 SSH 客户端登录 Linux 实例之前，您需要重置默认用户名（root）的密码，或者绑定密钥。具体操作请参考 [重置密码](https://cloud.tencent.com/document/product/1207/44575) 或 [管理密钥](https://cloud.tencent.com/document/product/1207/44573) 文档。
</dx-alert>
- 请确认本地计算机与实例之间的网络连通正常，以及实例的防火墙已放行22端口（创建实例时默认已开通22端口）。


## 操作步骤

<dx-tabs>
::: 使用密码登录
1. 执行以下命令，连接 Linux 实例。
<dx-alert infotype="explain" title="">
- 如果您的本地计算机使用非桌面版的 Linux 系统，可直接在系统界面执行以下命令。
- 如果您的本地计算机使用桌面版 Linux 系统或 MacOS 系统，请先打开系统自带的终端（如 MacOS 的 Terminal），再执行以下命令。
- 如果您的本地电脑为 Windows 10 或 Windows Server 2019 系统，需先打开命令提示符（CMD），再执行以下命令。
</dx-alert>
```
ssh <username>@<IP address or domain name>
```
 - `username` 即为 [前提条件](#Prerequisites) 中已获取的用户名，如`root`、`ubuntu` 等。
 - `IP address or domain name` 为您的 Linux 实例公网 IP 地址或自定义域名。
2. 输入已获取的密码，按 **Enter**，即可完成登录。


:::
::: 使用密钥登录
1. 执行以下命令，赋予私钥文件仅本人可读权限。
 - 如果您的本地电脑为 Mac OS 系统，需先打开系统自带的终端（Terminal），再执行以下命令。
 - 如果您的本地电脑为 Linux 系统，可直接执行以下命令。
```
chmod 400 <已下载的与实例关联的私钥的绝对路径>
```
 - 如果您的本地电脑为 Windows 10 或 Windows Server 2019 系统，需先打开命令提示符（CMD），再依次执行以下命令。
```
icacls <已下载的与实例关联的私钥文件的路径> /grant <Windows 系统用户帐户>:F
```
```
icacls <已下载的与实例关联的私钥文件的路径> /inheritancelevel:r
```
2. 执行以下命令，进行远程登录。
```
ssh -i <已下载的与实例关联的私钥文件的路径> <username>@<IP address or domain name>
```
 - `username` 即为 [前提条件](#Prerequisites) 中已获取的用户名，如 `root`、`ubuntu` 等。
 - `IP address or domain name` 为您的 Linux 实例公网 IP 地址或自定义域名。
 
  例如，在 MacOS 系统终端执行 `ssh -i /Users/macuser/Downloads/test_private_key root@35.222.45.145` 命令，远程登录 Linux 实例。

:::
</dx-tabs>


