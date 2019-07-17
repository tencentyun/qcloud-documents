连接到 MySQL 数据库的方式有两种：
- **内网访问**：CVM访问自动分配给数据库的内网地址，这种访问方式使用内网高速网络，延迟低。
> !
> - 使用内网访问CVM和数据库要在同一地域、同一账号且同一网络类型（都是基础网络或者在同一个 [私有网路 VPC](https://cloud.tencent.com/document/product/215/20046) 下）
> - 不同地域、不同账号、不同网络类型
 
步骤：
1. 登录到与此数据库实例属于同一个地域的网络可达的 CVM 主机。
关于登录 CVM 主机请查看 <a href="https://cloud.tencent.com/document/product/213/2764" target="_blank"> Windows CVM 入门</a> 或 <a href="https://cloud.tencent.com/document/product/213/2936" target="_blank">Linux CVM 入门 </a>。网络可达是指此 CVM 主机与 MySQL 数据库实例都处于基础网络之中，或者处于同一个 VPC 中。
2. 请根据 CVM 的操作系统选择推荐的连接方式。


- **外网访问**：通过外网地址，访问MySQL数据库。

> !
- 外网访问需要开启数据库实例的外网地址，从而使您的数据库服务暴露在公网上，此操作可能导致数据库被入侵或攻击。建议您使用内网访问的方式来登录数据库。 
-  TencentDB 外网访问仅用于开发或辅助管理数据库，不建议正式业务访问使用，因不可控因素会导致外网访问不可用（诸如但不限于 DDOS 攻击、突发大流量访问等）。

 步骤：
具体使用方式，请参见 [从外网访问数据库](https://cloud.tencent.com/document/product/236/9038)。


### 从 Windows 系统登录
1. 下载一个标准的 SQL 客户端。此步骤中我们推荐您下载 MySQL Workbench，这是 Windows 系统下较常见的 SQL 客户端。在 CVM 中打开 https://dev.mysql.com/downloads/workbench/ ，根据您的系统来下载适配版本的安装程序。
![](//mc.qcloudimg.com/static/img/4d7e6c56f02aad86f232e5cdd8c0bb17/image.png)
2. 界面上将提示【Login】、【Sign Up】和【No, thanks, just start my download.】， 请选择【No thanks, just start my download.】来快速下载。
![](//mc.qcloudimg.com/static/img/7169ce063b1b41c58c48089bc2a61441/image.png)
3. 在此台 CVM 上安装 MySQL Workbench。**前置条件：**此电脑上需要安装 Microsoft .NET Framework 4.5 和 Visual C++ Redistributable for Visual Studio 2015。 您可以单击 MySQL Workbench 安装向导中的【Download Prerequisites】来安装这两个软件，然后安装 MySQL Workbench。
![](//mc.qcloudimg.com/static/img/bcf08cec72e8ea9c490cb30ae79f0da4/image.png)
4. 打开 MySQL Workbench，选择【Database】>【Connect to Database】，输入 MySQL 数据库实例的内网地址和用户名，密码，单击【OK】进行登录。
  - Hostname：输入内网（或外网）地址。在控制台中的 MySQL 数据库实例详情页可以查看到目标数据库实例的内网地址，此处以 10.66.238.24 为例。
 - Port：3306，保持为默认端口即可。
 - Username：默认为 root。
 - Password：输入您在初始化数据库实例时设置的密码。
![](https://main.qcloudimg.com/raw/c480e5db0d2fa40c059af8963a4ff404.png)
5. 登录成功的界面如图所示，在此页面上您可以看到 MySQL 数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](//mc.qcloudimg.com/static/img/abd8efce579343d25f534143c19c132e/image.png)	

### 从 Linux 系统登录 
1. 以 CentOS 7.2 64 位系统的 CVM 为例，利用 CentOS 自带的包管理软件 Yum 去腾讯云的镜像源下载安装 MySQL 客户端。
执行以下命令安装 MySQL 客户端：
```
yum install mysql
```
提示 Complete! 说明 MySQL 客户端安装完成。
![](https://main.qcloudimg.com/raw/907e047fed90f6cf68752fb386382927.png)
2. 执行以下命令登录到 MySQL 数据库实例。
```
mysql -h hostname -u username -p
```
>?
>- 请将 hostname 替换为目标 MySQL 数据库实例的内网(或外网) 地址，将 username 替换为默认的用户名 root，并在提示 Enter password：后输出 root 账户对应的密码。
>- 本例中 hostname 为10.66.238.24。
>- 提示 MySQL [(none)]> 说明成功登录到 MySQL。
>
![](https://main.qcloudimg.com/raw/cf1d6c76d8a30dea49745699a22c9f7a.png)
3. 在 MySQL > 提示符下可以发送 SQL 语句到要执行的 MySQL 服务器，具体命令行请参见 [此网站](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
下图中以`show databases;`为例：
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

