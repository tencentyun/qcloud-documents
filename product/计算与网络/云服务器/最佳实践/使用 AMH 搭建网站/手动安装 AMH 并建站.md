## 操作场景
本文介绍如何在腾讯云云服务器（CVM）上手动安装 AMH 并搭建 PHP 网站。

进行手动安装 AMH，您需要熟悉 Linux 命令，例如  [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件的使用及版本兼容性比较了解。


<dx-alert infotype="notice" title="">
腾讯云建议您可以通过云市场的镜像环境部署 AMH，手动安装 AMH需要较长的时间。具体步骤可参考 [镜像部署 AMH 和建站](https://cloud.tencent.com/document/product/213/38357)。
</dx-alert>



## 示例软件版本
本文以在 CentOS 7.8 操作系统的 Linux 云服务器上安装 AMH 6.1 为例，您可前往 [AMH 官网](https://amh.sh/index.htm?amh) 了解更多 AMH 及支持操作系统的信息。


## 前提条件
- 已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
- 使用 AMH 搭建网站需要使用已完成备案，并且已解析到所使用云服务器的域名。
腾讯云提供 [域名注册](https://dnspod.cloud.tencent.com/)、[网站备案](https://cloud.tencent.com/product/ba) 及 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns) 服务，您可通过服务并参考 [建站基本流程](https://cloud.tencent.com/document/product/242/8584) 获得可使用域名。


## 操作步骤
### 步骤1：登录 Linux 实例
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)

### 步骤2：手动安装 AMH
1. 执行以下命令，下载并执行 AMH 安装脚本。
```
wget http://dl.amh.sh/amh.sh && bash amh.sh
```
2. 根据界面上的信息输入 `1` ，并按 **Enter** 表示使用中国源码镜像。如下图所示：
![](https://main.qcloudimg.com/raw/5dadf2033f744ff2bad0f956ab5e80a3.png)
3. 信息输入完成后，请等待 AMH 完成安装。
4. [](id:info)安装成功后，您可获取 AMH 地址，并请记录 AMH 及数据库管理员帐号及密码。如下图所示：
![](https://main.qcloudimg.com/raw/9fb2201f06059626f0896ed128da0ff7.png)



### 步骤3：登录 AMH
1. 使用浏览器访问以下地址
```
http://云服务器公网实例 IP:8888
```
进入 AMH 后台管理登录页面。如下图所示：
![](https://main.qcloudimg.com/raw/0b5891b2a121b005b159c5ed811e1d81.png)
2. 根据以下提示输入相关信息，并单击**登录**。
 - 管理员账号：`admin`。
 - 管理员密码：输入在 [安装 AMH](#info) 已获取的密码。
3. 如下图所示则为登录成功：
![](https://main.qcloudimg.com/raw/58990c7ec06e4b55c4693db87c0870fd.png)

### 步骤4：搭建 PHP 网站
搭建 PHP 网站步骤与镜像部署 AMH 并建站中的步骤相同，详情请参见 [搭建 PHP 网站](https://cloud.tencent.com/document/product/213/38357#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E6.90.AD.E5.BB.BA-php-.E7.BD.91.E7.AB.99)。


### 步骤5：安装 PHP 网站
安装 PHP 网站步骤与镜像部署 AMH 并建站中的步骤相同，详情请参见 [安装 PHP 网站](https://cloud.tencent.com/document/product/213/38357#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E5.AE.89.E8.A3.85-php-.E7.BD.91.E7.AB.99)。

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考[ IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。



