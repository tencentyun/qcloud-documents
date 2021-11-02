## 操作场景
Ghost 是使用 Node.js 语言编写的开源博客平台，您可使用 Ghost 快速搭建博客，简化在线出版过程。本文档介绍如何在腾讯云云服务器（CVM）上手动搭建 Ghost 个人网站。

进行 Ghost 网站搭建，您需要熟悉 Liunx 操作系统及命令，例如 [Ubuntu 环境下通过 Apt-get 安装软件](https://cloud.tencent.com/document/product/213/2123) 等常用命令。

## 示例软件版本
本文搭建 Ghost 博客使用的操作系统及软件版本及说明如下：
- 操作系统：本文以 Ubuntu 20.04 为例。
- Nginx：Web 服务器，本文以 Nginx 1.18.0 为例。
- MySQL：数据库，本文以 MySQL 8.0.25 为例。
- Node.js：运行环境，本文以 Node.js 14.17.0 版本为例。
- Ghost：开源博客本台，本文以 Ghost 4.6.4 版本为例。


## 前提条件
- 已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
- Ghost 博客配置的过程中需要使用已完成备案，并且已解析到所使用云服务器的域名。
腾讯云提供 [域名注册](https://dnspod.cloud.tencent.com/)、[网站备案](https://cloud.tencent.com/product/ba) 及 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns) 服务，您可通过服务并参考 [建站基本流程](https://cloud.tencent.com/document/product/242/8584) 获得可使用域名。



## 操作步骤

### 步骤1：登录 Linux 实例
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)

### 步骤2：创建新用户
1. 当您登录 Ubuntu 操作系统的云服务器后，请参考 [Ubuntu 系统使用 root 用户登录](https://cloud.tencent.com/document/product/213/17278#ubuntu-.E7.B3.BB.E7.BB.9F.E5.A6.82.E4.BD.95.E4.BD.BF.E7.94.A8-root-.E7.94.A8.E6.88.B7.E7.99.BB.E5.BD.95.E5.AE.9E.E4.BE.8B.EF.BC.9F) 切换为 root 用户。
2. 执行以下命令，创建新用户。本文以 `user` 为例。
>!请勿使用 `ghost` 作为用户名，会导致与 Ghost-CLI 发生冲突。 
>
```
adduser user
```
 1. 请按照提示输入并确认用户密码，密码默认不显示，输入完成后按 **Enter** 进入下一步。
 2. 根据您的实际情况填写用户相关信息，可默认不填写，按 **Enter** 进行下一步。
 3. 输入 **Y** 确认信息，并按 **Enter** 完成设置。如下图所示：
 ![](https://main.qcloudimg.com/raw/66ca399607b89f2653668eb4b0cb71f5.png)
3. 执行以下命令，增加用户权限。
```
usermod -aG sudo user
```
4. 执行以下命令，切换 `user` 登录。
```
su - user
```

### 步骤3：更新安装包
依次执行以下命令，更新安装包。
>?请按照界面上的提示输入 `user` 的密码，并按 **Enter** 开始更新。
>
```
sudo apt-get update
```
```
sudo apt-get upgrade -y
```

### 步骤4：环境搭建
#### 安装配置 Nginx
执行以下命令，安装 Nginx。
```
sudo apt-get install -y nginx 
```

#### 安装配置 MySQL
1. 执行以下命令，安装 MySQL。
```
sudo apt-get install -y mysql-server 
```
2. 执行以下命令，连接 MySQL。
```
sudo mysql
```
3. <span id="database"></span>执行以下命令，创建 Ghost 使用的数据库。本文以 `ghost_data` 为例。
```
CREATE DATABASE ghost_data;
```
4. <span id="sercet"></span>执行以下命令，设置 root 帐户密码。
```
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '输入root帐户密码';
```
5. 执行以下命令，退出 MySQL。
```
\q
```

#### 安装配置 Node.js
1. 执行以下命令，添加 Node.js 支持的安装版本。
>? Ghost 不同版本对于 Node.js 有不同的版本需求，请参考 [Supported Node versions](https://ghost.org/docs/faq/node-versions/) 及以下命令，执行对应命令。
>
```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash
```
2. 执行以下命令，安装 Node.js。
```
sudo apt-get install -y nodejs
```

#### 安装 Ghost-CLI
执行以下命令，安装 Ghost 命令行工具，以便快速配置 Ghost。
```
sudo npm install ghost-cli@latest -g
```

### 步骤5：安装配置 Ghost
1. 依次执行以下命令，设置并进入 Ghost 安装目录。
```
sudo mkdir -p /var/www/ghost
```
```
sudo chown user:user /var/www/ghost
```
```
sudo chmod 775 /var/www/ghost
```
```
cd /var/www/ghost
```
2. 执行以下命令，运行安装程序。
```
ghost install
```
3. 安装过程中需要进行相关配置，请参考界面及以下提示完成配置。如下图所示：
![](https://main.qcloudimg.com/raw/4fa1bccb961fa6c05c01892e5fbfd367.png)
主要配置如下：
 1. **Enter your blog URL**：输入已解析的域名，请输入 `http://(您的域名)`。
 2. **Enter your MySQL  hostname**：输入数据库连接地址，请输入 `localhost` 后按 **Enter**。
 3. **Enter your MySQL username**：输入数据库用户名，请输入 `root` 后按 **Enter**。
 4. **Enter your MySQL password**：输入数据库密码，请输入在 [设置 root 帐户密码](#sercet) 中已设置的密码后按 **Enter**。
 5. **Enter your database name**：输入 Ghost 使用的数据库，请输入在 [创建数据库](#database) 中已创建的 `ghost_data` 后按 **Enter** 。
 6. **Do you wish to set up SSL?**：如需开启 HTTPS 访问，请输入 **Y** 后按 **Enter**。
 其余配置请结合实际情况及页面提示完成。完成设置后，界面下方会输出 Ghost 的管理员访问地址。
4. 使用本地浏览器访问 Ghost 的管理员访问地址，开始个人博客配置。如下图所示：
>?若您已开启 HTTPS 访问，则可使用 `https://` 进行访问或博客配置等操作。
>
单击【Create your account】开始创建管理员账户。
![](https://main.qcloudimg.com/raw/e2eeacd71eec4c27660eeb4797f83f2a.png)
5. 输入相关信息，并单击【Last step】。如下图所示：
![](https://main.qcloudimg.com/raw/a7a81f16b811bdceeb429116ee23081c.png)
6. 可邀请他人一起参与博客创建，也可跳过此步骤。
7. 进入管理界面后，即可开始管理博客。如下图所示：
![](https://main.qcloudimg.com/raw/fd9071dba9748ce8125f8597be0d248a.png)
配置完成后，使用本地浏览器访问已配置的 `www.xxxxxxxx.xx` 域名即可看到个人博客主页。如下图所示：
![](https://main.qcloudimg.com/raw/055decab4524eb9f2f5602fbd0502c7c.png)

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。

 
 
 
 
 
