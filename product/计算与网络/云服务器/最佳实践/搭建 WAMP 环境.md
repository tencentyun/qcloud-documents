## 操作场景
WAMP 环境是指在 Windows 系统下，由 Apache Web 服务器 + MySQL + PHP 组成的服务器架构。本文档介绍如何在腾讯云云服务器（CVM）上，使用 Bitnami WAMP 手动搭建 WAMP 环境。

## 示例软件版本
本文搭建的 WAMP 环境软件组成版本及说明如下：
- Windows：Windows 操作系统，本文以 Windows Server R2 2012 中文版为例。
- Apache：Web 服务器，本文以 Apache 2.4.41 为例。
- MySQL：数据库，本文以 MySQL 8.0.18 为例。
- PHP：脚本语言，本文以 PHP 7.3.11 为例。

## 操作步骤
### 步骤1：登录 Windows 云服务器
[使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)，您也可以根据实际操作习惯，选择其他不同的登录方式：

- [使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)
- [使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704)

### 步骤2：下载并安装 WAMP 环境
1. 安装 [Bitnami WAMP](https://bitnami.com/stack/wamp) 环境。
2. （可选）完成安装后，可通过 [数据库安全配置](#safe) 提高 MySQL 数据库安全性。

### 验证环境配置
1. （可选）请参考相关操作中的 [展示文件扩展名](#show) 完成设置。
2.  前往 `C:\Bitnami\wampstack-7.3.11-0\apache2\htdocs` 目录下，新建 `phphinfo.php` 文件并输入以下内容。
```
<?php phpinfo(); ?>
```
3. 在本地浏览器中访问以下地址，查看环境是否安装成功。
```
http://云服务器实例的公网 IP/phpinfo.php
```
显示结果如下，则说明 WAMP 环境安装成功。
![](https://main.qcloudimg.com/raw/b90c1c1e09888266b9916debaa159364.png)

## 相关操作
###  <span id="show"></span>展示文件扩展名
1. 选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px"> >【这台电脑】，并单击页面上方的【查看】。
2. 在弹出的工具栏中勾选【文件扩展名】。如下图所示：
![](https://main.qcloudimg.com/raw/c3183be3bd8f82442f7c80b280eea8a6.png)

### 数据库安全配置<span id="safe"></span>
>?当您完成 MySQL 数据库安装后，可通过执行以下步骤，提高 MySQL 数据库的安全性。
>
1. 在 `C:\Bitnami\wampstack-7.3.11-0\mysql\bin` 目录中打开 `mysql_secure_installation.exe` 文件。
2. 在弹出窗口中根据以下步骤禁用 MySQL  默认功能，提高安全性。
 1. 输入安装时设置的数据库密码，输入密码默认不显示，输入完成后按 “**Enter**”。
 2. 输入 “**n**” 跳过密码更改。
 3. 输入 “**Y**” 删除匿名用户。
 4. 输入 “**Y**” 禁用远程 root 登录。
 5. 输入 “**Y**” 删除测试数据库。
 6. 输入 “**Y**” 重新加载权限表并保存您的更改。

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。
