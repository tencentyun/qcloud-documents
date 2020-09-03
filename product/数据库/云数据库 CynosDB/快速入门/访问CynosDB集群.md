
## 访问方式
访问云数据库 CynosDB（兼容 MySQL 版）的方式如下：
- **内网访问**：使用云服务器（CVM）访问自动分配给云数据库的内网地址，这种访问方式使用内网高速网络，延迟低。CVM 和云数据库要在同一地域、同一账号且同一网络类型（在同一个 [私有网络 VPC](https://cloud.tencent.com/document/product/215/20046)）。
>?对于不同地域、不同账号或不同网络类型的 CVM 和数据库，内网连接方式请参见 [对等连接](https://cloud.tencent.com/document/product/553/18827)，收费标准请参见 [对等连接计费概述](https://cloud.tencent.com/document/product/553/18833)。
- **外网访问**：通过外网地址访问云数据库 CynosDB。
>!
>- 外网访问需要开启数据库的外网地址，此操作会使您的数据库服务暴露在公网上，可能导致数据库被入侵或攻击。建议您使用内网访问的方式来登录数据库。 
>- 云数据库外网访问适用于开发或辅助管理数据库，不建议正式业务访问使用，因为可能存在不可控因素会导致外网访问不可用（例如 DDOS 攻击、突发大流量访问等）。
- **DMC 访问**：通过数据管理平台（Database Management Console，DMC）访问 CynosDB。


## 内外网访问 CynosDB（兼容 MySQL 版）
### （可选）开启外网访问地址
>?使用外网访问时，需要先开启数据库的外网地址。
>
1. 登录 [CynosDB 控制台](https://console.cloud.tencent.com/cynosdb)，在集群列表，单击集群名或操作列的【管理】，进入集群详情页面。
2. 在集群详情页下的连接信息里找到【外网地址】，单击【开启】。
![](https://main.qcloudimg.com/raw/b52321c8fdc11dc8435d0cd4305dff83.png)
3. 在弹出的对话框单击【确定】后，外网开通进入处理状态。
![](https://main.qcloudimg.com/raw/b6276671d4052aceaa65867d33839cef.png)
4. 开启成功后，即可在连接信息中查看外网地址。通过开关可以关闭外网访问权限，重新开启外网，域名对应的外网 IP 不变。

### 从 Windows 系统访问
1. 登录到 Windows 系统的 CVM，请参见 <a href="https://cloud.tencent.com/document/product/213/2764" target="_blank"> Windows CVM 入门</a>。
2. 下载一个标准的 SQL 客户端。推荐您下载 MySQL Workbench，这是 Windows 系统下较常见的 SQL 客户端。在 CVM 中打开 https://dev.mysql.com/downloads/workbench/ ，根据您的系统来下载适配版本的安装程序。
![](https://main.qcloudimg.com/raw/f82d66f0470813c6b972a7d0125043e1.png)
3. 界面将提示【Login】、【Sign Up】和【No, thanks, just start my download.】， 选择【No thanks, just start my download.】来快速下载。
![](//mc.qcloudimg.com/static/img/7169ce063b1b41c58c48089bc2a61441/image.png)
4. 在此台 CVM 上安装 MySQL Workbench。**前置条件：**此电脑上需要安装 Microsoft .NET Framework 4.5 和 Visual C++ Redistributable for Visual Studio 2015。您可以单击 MySQL Workbench 安装向导中的【Download Prerequisites】来安装这两个软件，然后安装 MySQL Workbench。
![](//mc.qcloudimg.com/static/img/bcf08cec72e8ea9c490cb30ae79f0da4/image.png)
5. 打开 MySQL Workbench，选择【Database】>【Connect to Database】，输入 CynosDB 集群的内网（或外网）地址和用户名、密码，单击【OK】进行登录。
 - Hostname：输入内网（或外网）地址。在 CynosDB 控制台中的集群详情页可查看到目标数据库的内网（或外网）地址。
 - Port：内网（或外网）对应端口。
 - Username：默认为 root。
 - Password：Username 对应的密码。
![](https://main.qcloudimg.com/raw/9c9e5dcc8a2bb9fa15fa4d98a18308f1.png)
6. 登录成功的页面如图所示，在此页面上您可以看到 CynosDB 集群的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](https://main.qcloudimg.com/raw/8f02e50fcc9c5c8dff33bcd2a83e3522.png)

### 从 Linux 系统访问 
1. 登录到 Linux 系统的 CVM，请参见 <a href="https://cloud.tencent.com/document/product/213/2936" target="_blank">Linux CVM 入门</a>。
1. 以 CentOS 7.2 64 位系统的 CVM 为例，利用 CentOS 自带的包管理软件 Yum 去腾讯云的镜像源下载安装 MySQL 客户端。
执行以下命令安装 MySQL 客户端：
```
yum install mysql
```
提示 Complete! 说明 MySQL 客户端安装完成。
![](https://main.qcloudimg.com/raw/907e047fed90f6cf68752fb386382927.png)
2. 根据访问方式选择执行以下操作：
 - 内网访问时，执行以下命令登录到 CynosDB 集群。
```
mysql -h hostname -u username -p
```
>?
>- 请将 hostname 替换为目标 CynosDB 集群的内网（或外网）地址，将 username 替换为默认的用户名 root，并在提示 Enter password：后输出 root 帐号对应的密码。
>- 本例中提示 MySQL [(none)]> 说明成功登录到 CynosDB 集群。
>
![](https://main.qcloudimg.com/raw/83b8a95cf4b99919b5899510691289b4.png)
 - 外网访问时，执行以下命令登录到 CynosDB 集群。
```
mysql -h hostname -P port -u username -p
```
>?
>- 请将 hostname 替换为目标 CynosDB 集群的外网 IP 地址；将 port 替换为外网端口号；将 username 替换为外网访问用户名，例如 cdb_outerroot；并在提示 Enter password：后输入 cdb_outerroot 帐号对应的密码。
>- 本例中 hostname 为 59281c4exxx.myqcloud.com，外网端口号为15311。
>
![](https://main.qcloudimg.com/raw/16839344da3a588be93d814de224277a.png)
3. 在 MySQL \[(none)]> 提示符下可以发送 SQL 语句到要执行的 CynosDB 服务器，具体命令行请参见 [此网站](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
下图中以`show databases;`为例：
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

## DMC 平台访问 CynosDB
1. 在集群列表，单击操作列的【登录】。
2. 在数据管理控制台的登录界面，帐号输入 root，密码为之前在创建集群时配置的 root 帐户的密码，单击【登录】。
![](https://main.qcloudimg.com/raw/5a98c6617b1a4aa17c10d1c369dfc465.png)
3. 在数据管理页面可以查看实例的状态和基本信息，单击【前往PMA】访问数据库。
![](https://main.qcloudimg.com/raw/34f10d3cf14636b35b607a7156f39fd7.png)
4. 通过 phpMyAdmin 成功连接到 CynosDB 集群，在此页面您可以看到数据库的各种模式和对象，以及进行创建表、数据插入和查询等操作。
![](https://main.qcloudimg.com/raw/1e2d0e2ee262e76235f53e58ed87b74b.png)
