## 操作场景

本文介绍如何在 Linux/Mac OS 系统的本地电脑中通过 SSH 登录 Linux 实例。

## 适用本地操作系统

Linux 或 Mac OS

## 鉴权方式

**密码**或**密钥**

## 前提条件
- 已获取登录实例的管理员帐号及密码（或密钥）。
   对于不同类型的 Linux 实例，默认帐号不同。如下表所示：
<table>
<tr><th>实例操作系统</th><th>默认帐号</th><th>密码/密钥</th></tr>
<tr><td><ul><li>SUSE</li><li>CentOS</li><li>Debian</li></ul></td><td>root</td><td rowspan="2"><ul><li>如果您在购买实例时选择自动生成密码，则可登录腾讯云控制台，单击右上角的 <img src="https://main.qcloudimg.com/raw/60e7d0de182a973d69fb82b69d01f52a.png" style="margin: 0;"></img> ，进入站内消息页面，获取云服务器登录管理员帐号及初始密码。</li><li>如果您在购买实例时选择自定义密码，则登录密码为您在购买云服务器实例时指定的密码。</li><li>如果您在购买实例时选择密钥登录，请牢记密钥存放在本地的绝对路径。</li><li>如果您忘记登录云服务器的密码或密钥，请参考 <a href="https://cloud.tencent.com/document/product/213/16566">重置实例密码</a> 或者 <a href="https://cloud.tencent.com/document/product/213/16691#.E5.88.9B.E5.BB.BA-ssh-.E5.AF.86.E9.92.A5">创建 SSH 密钥</a> 进行重置。</li></ul></td></tr>
<tr><td>Ubuntu</td><td>ubuntu</td></tr>
</table>
- 已打开云服务器实例的22号端口。
您可以通过 [检查网络连通性](https://cloud.tencent.com/document/product/213/10232#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E6.A3.80.E6.9F.A5.E7.BD.91.E7.BB.9C.E8.BF.9E.E9.80.9A.E6.80.A7) 检查22号端口是否放通。如果端口不通，您可以在 [配置安全组](https://cloud.tencent.com/document/product/213/15377) 时设置端口的入站/出站规则。
- 云服务器实例已购买公网 IP 并获取到公网 IP。
实例的公网 IP 可登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 进行查看。
- 如果您 [使用密钥登录](#LoginWithKey) 云服务器，需完成密钥的创建，并已将密钥绑定至该云服务器中。  
您可登录 [腾讯云云服务器控制台](https://console.cloud.tencent.com/cvm/)，单击左侧导航栏【SSH 密钥】，查看和管理已创建的密钥信息。更多详情请参阅 [SSH 密钥操作](/doc/product/213/6092)。
	
## 操作步骤

### 使用密码登录

1. 执行以下命令，连接 Linux 云服务器。
>? 如果您的本地电脑为 Mac OS 系统，需先打开系统自带的终端（Terminal），再执行以下命令。
> 如果您的本地电脑为 Linux 系统，可直接执行以下命令。
>
```
ssh <username>@<hostname or IP address>
```
 - `username` 即为前提条件中获得的默认帐号。
 - `hostname or IP address` 为您的 Linux 实例公网 IP 或自定义域名。
2. 输入已获取的密码，按 **Enter**，即可完成登录。

### 使用密钥登录

1. 执行以下命令，赋予私钥文件仅本人可读权限。
>? 如果您的本地电脑为 Mac OS 系统，需先打开系统自带的终端（Terminal），再执行以下命令。
> 如果您的本地电脑为 Linux 系统，可直接执行以下命令。
>
```
chmod 400 <下载的与云服务器关联的私钥的绝对路径>
```
2. 执行以下命令，进行远程登录。
```
ssh -i <下载的与云服务器关联的私钥的绝对路径> <username>@<hostname or IP address>
```
 - `username` 即为前提条件中获得的默认帐号。
 - `hostname or IP address` 为您的 Linux 实例公网 IP 或自定义域名。

 例如，执行 `ssh -i "Mac/Downloads/shawn_qcloud_stable" ubuntu@192.168.11.123` 命令，远程登录 Linux 云服务器。

## 后续操作

当您成功登录云服务器后，您可以在腾讯云服务器上搭建个人站点，论坛或者使用其他操作，相关操作可参考：
- [搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/34064)
- [搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/34065)


