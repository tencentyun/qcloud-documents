## 操作场景
本文介绍在腾讯云云服务器（CVM）上手动安装 AMH 并搭建 PHP 网站。

## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。


## 注意事项
- 本文以安装 AMH 4.2 版本为例，您可前往 [AMH 官网](https://amh.sh/index.htm?amh) 了解其他版本的最新信息。
- AMH 4.2 版本支持下列操作系统的云服务器，本文以 CentOS 6.9 为例。
 - CentOS 6 x64
 - CentOS 6 i386
 - CentOS 5 x64
 - CentOS 5 i386
 - Ubuntu 12 x64
 - Ubuntu 12 i386
 - Debian 6 x64（squeeze）
 - Debian 6 i386（squeeze）
- 本文针对全新购买云服务器，如果您已购买云服务器，请参考 [重装系统](https://cloud.tencent.com/document/product/213/4933) 选择对应操作系统。




## 操作步骤
### 创建并登录云服务器
1. 在实例的管理页面，单击【新建】。
具体操作请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 云服务器创建成功后，返回 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，查看并获取云服务器的以下信息。如下图所示：
![](https://main.qcloudimg.com/raw/0c53e53b69326286c5c5b359203b2971.png)
 - 云服务器用户名和密码。
 - 云服务器公网 IP。
3. 登录 Linux 云服务器，具体操作请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
登录云服务器后，默认已获取 root 权限，以下步骤需在 root 权限下操作。

### 手动安装 AMH
1. 执行以下命令，下载并执行 AMH 安装脚本。
```
wget http://amh.sh/file/AMH/4.2/amh.sh && chmod 775 amh.sh && ./amh.sh 2>&1 | tee amh.log
```
2. <span id="info"></span>根据界面上的信息分别输入以下信息。如下图所示：
![](https://main.qcloudimg.com/raw/3e619767eb7ac7884f5952d31251af43.png)
 1.  输入`1`并按 “**Enter**”，表示安装 AMH。
 2.  输入该云服务器的公网 IP，并按 “**Enter**”。
 3.  输入 MySQL 的登录密码，并按 “**Enter**”，本文以`123456`为例。
 4.  输入 AMH 的登录密码，并按 “**Enter**”，本文以`123456`为例。
3. 信息输入完成后，请等待 AMH 完成安装。


### 登录 AMH
1. 使用浏览器访问以下地址
```
http://云服务器公网实例 IP:8888
```
进入 AMH 后台管理登录页面。如下图所示：
![](https://main.qcloudimg.com/raw/6d2d36d2c192b7c8822fa2c8f64f95c8.png)
2. 输入在 [安装 AMH](#info) 已配置的用户名及密码，并单击【登录】。
3. 如下图所示则为登录成功：
![](https://main.qcloudimg.com/raw/9f8cd5e2914b0c2fde472c189a617f49.png)

### 搭建 PHP 网站
此步骤同使用镜像安装 AMH 中的 [搭建 PHP 网站](https://cloud.tencent.com/document/product/213/38357?!preview&!editLang=zh#.E6.90.AD.E5.BB.BA-php-.E7.BD.91.E7.AB.99)。


### 安装 PHP 网站
此步骤同使用镜像安装 AMH 中的 [安装 PHP 网站](https://cloud.tencent.com/document/product/213/38357?!preview&!editLang=zh#.E5.AE.89.E8.A3.85-php-.E7.BD.91.E7.AB.99)。
