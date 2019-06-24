连接到 MySQL 数据库的方式有两种：
- **内网访问**：使用在同一个可用区的 CVM 来访问自动分配给数据库的内网地址。这种方式使用内网高速网络，延迟低。（注意：此台 CVM 需要与数据库同一地域下的基础网络中，或者同一个 VPC 中，关于 VPC 的更多信息请查看<a href="https://cloud.tencent.com/document/product/215/20046" target="_blank"> VPC 概述</a>。）
- **外网访问**：借助外网账号，通过腾讯云控制台中的登录入口，登录到 phpMyAdmin 界面对数据库进行操作。

> !
- 外网访问需要开启数据库实例的外网地址，从而使您的数据库服务暴露在公网上，**此操作可能导致数据库被入侵或攻击**。建议您使用内网访问的方式来登录数据库。 
-  TencentDB 外网访问仅用于开发或辅助管理数据库，**强烈不建议**正式业务访问使用，因不可控因素会导致外网访问不可用（诸如但不限于 DDOS 攻击、突发大流量访问等）。

## 内网访问
1. 登录到与此数据库实例属于同一个可用区的网络可达的 CVM 主机。
关于登录 CVM 主机请查看 <a href="https://cloud.tencent.com/document/product/213/2764" target="_blank"> Windows CVM 入门</a> 或 <a href="https://cloud.tencent.com/document/product/213/2936" target="_blank">Linux CVM 入门 </a>。网络可达是指此 CVM 主机与 MySQL 数据库实例都处于基础网络之中，或者处于同一个 VPC 中。
2. 请根据 CVM 的操作系统选择推荐的连接方式。

### 从 Windows 系统登录
1. 下载一个标准的 SQL 客户端。此步骤中我们推荐您下载 MySQL Workbench，这是 Windows 系统下较常见的 SQL 客户端。在 CVM 中打开 https://dev.mysql.com/downloads/workbench/ ，根据您的系统来下载适配版本的安装程序。
![](//mc.qcloudimg.com/static/img/4d7e6c56f02aad86f232e5cdd8c0bb17/image.png)
2. 界面上将提示【Login】、【Sign Up】和【No, thanks, just start my download.】， 请选择【No thanks, just start my download.】来快速下载。
![](//mc.qcloudimg.com/static/img/7169ce063b1b41c58c48089bc2a61441/image.png)
3. 在此台 CVM 上安装 MySQL Workbench。**前置条件：**此电脑上需要安装 Microsoft .NET Framework 4.5 和 Visual C++ Redistributable for Visual Studio 2015。 您可以单击 MySQL Workbench 安装向导中的【Download Prerequisites】来安装这两个软件，然后安装 MySQL Workbench。
    ![](//mc.qcloudimg.com/static/img/bcf08cec72e8ea9c490cb30ae79f0da4/image.png)
4. 打开 MySQL Workbench，选择【Database】>【Connect to Database】，输入 MySQL 数据库实例的内网地址和用户名，密码，单击【OK】进行登录。
  - Hostname：输入内网地址。在控制台中的 MySQL 数据库实例详情页可以查看到目标数据库实例的内网地址，此处以 10.66.238.24 为例。
 - Port：3306，保持为默认端口即可。
 - Username：默认为 root。
 - Password：输入您在初始化数据库实例时设置的密码。
    ![](//mc.qcloudimg.com/static/img/feb4b95b1038532330e876a605016b87/image.png)
5. 登录成功的界面如图所示，在此页面上您可以看到 MySQL 数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
    ![](//mc.qcloudimg.com/static/img/abd8efce579343d25f534143c19c132e/image.png)	

### 从 Linux 系统登录 
1. 以 CentOS 7.2 64 位系统的 CVM 为例，利用 CentOS 自带的包管理软件 Yum 去腾讯云的镜像源下载安装 MySQL 客户端。
	相关命令为：
```
	yum install mysql
```
	图示如下：
	![](//mc.qcloudimg.com/static/img/eee76fa95379b8a25fc076b66b4ca28c/image.png)
2. 使用 MySQL 命令行工具登录到 MySQL。相关命令为：
```
mysql -h hostname -u username -p
```
>?
>- 请将 hostname 替换为目标 MySQL 数据库实例的内网 IP 地址，将 username 替换为默认的用户名 root，并在提示 Enter password：后输出 root 账户对应的密码。
>- 本例中 hostname 为10.66.238.24。
>
![](//mc.qcloudimg.com/static/img/d1da9f59f0fff77ad2a8ff18e0b11e7c/image.png)
3. 在 MySQL > 提示符下可以发送 SQL 语句到要执行的 MySQL 服务器，具体命令行请参考 [此网站](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
下图中以`show databases;`为例：
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

## 外网访问
**安全提示：**外网访问需要开启数据库实例的外网地址，从而使您的数据库服务暴露在公网上，此操作可能导致数据库被入侵或攻击。
请根据外网中主机的操作系统选择对应的登录方式。
### 从 Windows 系统登录
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb)。
2. 在左侧导航选择【实例列表】页签。
3. 选择状态为运行中的目标实例，单击【登录】。
![](https://main.qcloudimg.com/raw/807212252e237e04ab62560fdda54795.jpg)
4. 在数据管理控制台的登录界面，帐号输入 root，密码为之前在初始化选项中配置的 root 帐户的密码，单击【登录】。
![](//mc.qcloudimg.com/static/img/b5538d93dc27d99af6fed9f0e5c9b798/image.png)
5. 在数据管理页面可以查看实例的状态和基本信息，单击【前往PMA】访问数据库。
![](https://main.qcloudimg.com/raw/fa71f75c683647af62bb8f9e2820282e.png)
6. 您现在已经通过 phpMyAdmin 成功连接到 MySQL 数据库，在此页面上您可以看到 MySQL 数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](https://main.qcloudimg.com/raw/2a502f89d6a3e05bc16487802c4da042.png)

### 从 Linux 系统登录
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb)。
2. 在左侧导航选择【实例列表】页签。
3. 单击目标实例的 ID 进入实例详情页。
![](https://main.qcloudimg.com/raw/daba9621274e7ec1e06065a86c3cd4cd.png)
4. 在【实例详情】页签下的【基本信息】中，单击外网地址后的【开启】，单击【确定】。
![](https://main.qcloudimg.com/raw/fa7034bf01bdebbaa21d35b86cbc52b9.png)
5. 完成后会显示开通后的外网地址，随后的步骤里会用到此地址。
![](https://main.qcloudimg.com/raw/86557c48a6f7d492b33ac85196c6b5ea.png)
6. 以 CentOS 7.2 64 位系统为例，利用 CentOS 自带的包管理软件 Yum 去下载安装 MySQL 客户端。
	相关命令为：
```
	yum install mysql
```
7. 使用 MySQL 命令行工具登录到 MySQL。
相关命令为：
```
mysql -h hostname -P port -u username -p
```
>?
>- 请将 hostname 替换为目标 MySQL 数据库实例的外网 IP 地址；将 port 替换为外网端口号；将 username 替换为外网访问用户名，例如：cdb_outerroot；并在提示 **Enter password：**后输入 cdb_outerroot 帐户对应的密码。
>- 外网访问用户名用于外网访问，建议用户单独创建便于访问控制管理。
>- 本例中 hostname 为 59281c4e4b511.gz.cdb.myqcloud.com，外网端口号为 15311。
>
![](//mc.qcloudimg.com/static/img/48df6390ccf7669d04403cd84b8b6fad/image.png)
8. 在 MySQL > 提示符下可以发送 SQL 语句到要执行的 MySQL 服务器，具体命令行请参考 [此网站](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
下图中以`show databases;`为例：
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)
