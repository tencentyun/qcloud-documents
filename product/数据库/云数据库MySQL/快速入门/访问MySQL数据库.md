## 访问方式
访问云数据库 MySQL 的方式有三种：
- **内网访问**：使用云服务器 CVM 访问自动分配给云数据库的内网地址，这种访问方式使用内网高速网络，延迟低。CVM 和云数据库要在同一地域、同一账号且同一网络类型（都是基础网络或都在同一个 [私有网路 VPC](https://cloud.tencent.com/document/product/215/20046)）。
- **外网访问**：通过外网地址访问云数据库 MySQL 。
>!
>- 外网访问需要开启数据库实例的外网地址，此操作会使您的数据库服务暴露在公网上，可能导致数据库被入侵或攻击。建议您使用内网访问的方式来登录数据库。 
>- 云数据库外网访问适用于开发或辅助管理数据库，不建议正式业务访问使用，因为可能存在不可控因素会导致外网访问不可用（例如 DDOS 攻击、突发大流量访问等）。
- **对等连接**：对于不同地域、不同账号或不同网络类型的 CVM 与数据库的内网连接方式，请参见 [对等连接](https://cloud.tencent.com/document/product/553/18827)，收费标准请参见 [对等连接计费概述](https://cloud.tencent.com/document/product/553/18833)。


## 访问 MySQL 实例
### （可选）开启外网访问地址
>?使用外网访问时，需要先开启数据库实例的外网地址。
>
1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb/ )。
2. 在实例列表中，选择需要修改的实例，单击实例名或操作列的【管理】，进入实例详情页面。
3. 在实例详情页下的基本信息里找到【外网地址】，单击【开启】。
![](https://main.qcloudimg.com/raw/c1ef4d6d01fe9cd3f7e9caabae440fc6.png)
4. 单击【确定】后，外网开通进入处理状态。
![](https://main.qcloudimg.com/raw/b2a407e7609fa0c31b0e7ee06c94a3de.png)
5. 开启成功后，即可在基本信息中查看到外网地址。
6. 通过开关可以关闭外网访问权限，重新开启外网，域名对应的外网 IP 不变。

### 从 Windows 系统登录
1. 登录到与数据库实例属于同一个地域且网络可达的 Windows 系统 CVM。
登录 CVM 主机请参见 <a href="https://cloud.tencent.com/document/product/213/2764" target="_blank"> Windows CVM 入门</a> 或 <a href="https://cloud.tencent.com/document/product/213/2936" target="_blank">Linux CVM 入门 </a>。网络可达是指此 CVM 主机与 MySQL 数据库实例都处于基础网络之中，或者处于同一个 VPC 中。
1. 下载一个标准的 SQL 客户端。推荐您下载 MySQL Workbench，这是 Windows 系统下较常见的 SQL 客户端。在 CVM 中打开 https://dev.mysql.com/downloads/workbench/ ，根据您的系统来下载适配版本的安装程序。
![](https://main.qcloudimg.com/raw/f82d66f0470813c6b972a7d0125043e1.png)
2. 界面上将提示【Login】、【Sign Up】和【No, thanks, just start my download.】， 请选择【No thanks, just start my download.】来快速下载。
![](//mc.qcloudimg.com/static/img/7169ce063b1b41c58c48089bc2a61441/image.png)
3. 在此台 CVM 上安装 MySQL Workbench。**前置条件：**此电脑上需要安装 Microsoft .NET Framework 4.5 和 Visual C++ Redistributable for Visual Studio 2015。您可以单击 MySQL Workbench 安装向导中的【Download Prerequisites】来安装这两个软件，然后安装 MySQL Workbench。
![](//mc.qcloudimg.com/static/img/bcf08cec72e8ea9c490cb30ae79f0da4/image.png)
4. 打开 MySQL Workbench，选择【Database】>【Connect to Database】，输入 MySQL 数据库实例的内网（或外网）地址和用户名、密码，单击【OK】进行登录。
 - Hostname：输入内网（或外网）地址。在 MySQL 控制台中的实例详情页可以查看到目标数据库实例的内网（或外网）地址。
 - Port：内网（或外网）对应端口。
 - Username：默认为 root，外网访问时建议您单独创建帐号便于访问控制管理。
 - Password：Username 对应的密码。
![](https://main.qcloudimg.com/raw/9c9e5dcc8a2bb9fa15fa4d98a18308f1.png)
5. 登录成功的页面如图所示，在此页面上您可以看到 MySQL 数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](https://main.qcloudimg.com/raw/8f02e50fcc9c5c8dff33bcd2a83e3522.png)

### 从 Linux 系统登录 
1. 登录到与数据库实例属于同一个地域且网络可达的 Linux 系统 CVM。
登录 CVM 主机请参见 <a href="https://cloud.tencent.com/document/product/213/2764" target="_blank"> Windows CVM 入门</a> 或 <a href="https://cloud.tencent.com/document/product/213/2936" target="_blank">Linux CVM 入门 </a>。网络可达是指此 CVM 主机与 MySQL 数据库实例都处于基础网络之中，或者处于同一个 VPC 中。
1. 以 CentOS 7.2 64 位系统的 CVM 为例，利用 CentOS 自带的包管理软件 Yum 去腾讯云的镜像源下载安装 MySQL 客户端。
执行以下命令安装 MySQL 客户端：
```
yum install mysql
```
提示 Complete! 说明 MySQL 客户端安装完成。
![](https://main.qcloudimg.com/raw/907e047fed90f6cf68752fb386382927.png)
2. 根据访问方式选择执行以下操作：
 - 内网访问时，执行以下命令登录到 MySQL 数据库实例。
```
mysql -h hostname -u username -p
```
>?
>- 请将 hostname 替换为目标 MySQL 数据库实例的内网（或外网）地址，将 username 替换为默认的用户名 root，并在提示 Enter password：后输出 root 帐号对应的密码。
>- 提示 MySQL [(none)]> 说明成功登录到 MySQL。
>
![](https://main.qcloudimg.com/raw/83b8a95cf4b99919b5899510691289b4.png)
 - 外网访问时，执行以下命令登录到 MySQL 数据库实例。
```
mysql -h hostname -P port -u username -p
```
>?
>- 请将 hostname 替换为目标 MySQL 数据库实例的外网 IP 地址；将 port 替换为外网端口号；将 username 替换为外网访问用户名，例如 cdb_outerroot；并在提示 Enter password：后输入 cdb_outerroot 帐号对应的密码。
>- 外网访问用户名用于外网访问，建议您单独创建便于访问控制管理。
>- 本例中 hostname 为 59281c4exxx.myqcloud.com，外网端口号为15311。
>
![](https://main.qcloudimg.com/raw/16839344da3a588be93d814de224277a.png)
3. 在 MySQL > 提示符下可以发送 SQL 语句到要执行的 MySQL 服务器，具体命令行请参见 [此网站](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
下图中以`show databases;`为例：
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)


