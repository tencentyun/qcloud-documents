## 操作场景
WIMP 环境是指在 Windows 系统下，由 IIS 服务 + MySQL + PHP 组成的服务器架构。本文档介绍如何在腾讯云云服务器（CVM）上手动搭建 WIMP 环境。

## 示例软件版本
本文搭建的 WIMP 环境软件组成版本及说明如下：
- Windows：Windows 操作系统，本文以 Windows Server R2 2012 中文版为例。
- IIS 服务：Microsoft Internet 信息服务（Web 服务器），本文以 IIS 6.2 为例。
- MySQL：数据库，本文以 MySQL 5.5 为例。
- PHP：脚本语言，本文以 PHP 7.0.3 为例。

## 操作步骤
### 步骤1：登录 Windows 云服务器
[使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)，您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)
- [使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704)

### 步骤2：安装 IIS 服务
请参考 [安装 IIS 服务](https://cloud.tencent.com/document/product/213/2755#windows-server-2012-r2-.E6.93.8D.E4.BD.9C.E7.B3.BB.E7.BB.9F) 完成安装。

### 步骤3：安装 MySQL 和 PHP
1. 下载并安装 [Microsoft Web 平台安装程序](https://www.microsoft.com/web/downloads/platform.aspx)。
2. 选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px"> > <img src="https://main.qcloudimg.com/raw/3ad1de7c2eaef565dbd9c42dfdcedc12.png" style="margin:-3px 0px">，并在应用中打开 Web 平台安装程序。
安装平台初始化时间较长，请耐心等待。
3. 选择 Web 安装平台程序左上角的【产品】，并在右上角搜索框中输入 `MySQL`，按 “**Enter**” 进行搜索。
4. 根据实际需求选择不同版本的数据库，并单击【添加】。如下图所示：
![](https://main.qcloudimg.com/raw/4a6523e2c8f64b3fab8e4cb4ced241d2.png)
5. 搜索 `PHP`，选择版本后添加到安装队列。如下图所示：
![](https://main.qcloudimg.com/raw/62689fee50a0a5447dc31b5d932f308c.png)
6. 单击【安装】。
7. <span id="passwd"></span>在弹出的窗口中设置 MySQL  数据库帐号密码，并单击【继续】。
数据库帐号为 `root`，数据库密码请自行设置并记录，本文以 `123456` 为例。
8. 在窗口中接受许可条款，即可开始安装。
9. （可选）完成安装后，可通过 [数据库安全配置](#safe) 提高 MySQL 数据库安全性。

### 验证环境配置
1. （可选）请参考相关操作中的 [展示文件扩展名](#show) 完成设置。
2. 在 `C:\inetpub\wwwroot` 目录下新建 `phpinfo.php` 文件，写入以下内容并保存：
```
<?php phpinfo(); ?>
```
3. 在本地浏览器中访问以下地址，验证环境配置。
```
http://云服务器实例的公网 IP
```
显示结果如下，则说明环境配置成功。
![](https://main.qcloudimg.com/raw/db227fe8869a545215baa2a2493ec975.png)

## 相关操作
###  <span id="show"></span>展示文件扩展名
1. 选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px"> >【这台电脑】，并单击页面上方的【查看】。
2. 在弹出的工具栏中勾选【文件扩展名】。如下图所示：
![](https://main.qcloudimg.com/raw/c3183be3bd8f82442f7c80b280eea8a6.png)

### 数据库安全配置<span id="safe"></span>
>?当您完成 MySQL 数据库安装后，可通过执行以下步骤，提高 MySQL 数据库的安全性。
>
1. 前往 [Perl Programming Language](https://www.perl.org/) 下载并安装 Perl。
2. 在 `C:\Program Files\MySQL\MySQL Server 5.5\bin` 目录中打开 `mysql_secure_installation.pl` 文件。
>?
>- 首次运行 `.pl` 文件，需通过【打开方式】> 选择 `C:\Perl64\bin\perl.exe` 程序方式运行。
>- `C:\Perl64` 为本文中 Perl 的安装路径。
>
3. 在弹出窗口中根据以下步骤禁用 MySQL  默认功能，提高安全性。
 1. 输入[ 安装 MySQL](#passwd) 时设置的数据库密码，输入密码默认不显示，输入完成后按 “**Enter**”。
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
