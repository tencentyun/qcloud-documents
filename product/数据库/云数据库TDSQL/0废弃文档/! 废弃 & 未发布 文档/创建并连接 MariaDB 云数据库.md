在本文档中，您可以创建 MariaDB 云数据库实例并连接到该数据库实例。最后，您将删除该数据库实例。

> **注意：**
> 在创建 MariaDB 云数据库实例之前，您必须拥有一个腾讯云帐户。如果您没有腾讯云帐户，请在 [注册页面](https://cloud.tencent.com/register) 填写相关信息注册腾讯云帐户。

## 一、创建 MariaDB 云数据库实例
在此步骤中，您会使用腾讯云控制台创建 MariaDB 云数据库实例。
1. 登录 [云数据库控制台](https://console.cloud.tencent.com/cdb)。
![](//mc.qcloudimg.com/static/img/7f454c8f988ec22c4045b33c47571024/image.png)
2. 在右侧导航栏选择需要创建的云数据库类型，单击【TDSQL（MariaDB）】>【实例列表】>【+新建】，进入 MariaDB 云数据库购买界面。
![](//mc.qcloudimg.com/static/img/ffda5d7af5a406bd600b7732dd194928/image.png)
3. 在 TDSQL（MariaDB）云数据库购买界面中，选择数据库相关配置。确认无误后，单击【立即购买】。
 - 计费模式。目前只支持包年包月。
 - 地域和可用区。本教程以“广州”以及“广州三区”为例。地域说明请参见 [地域与可用区](/doc/product/236/8458)。
 - 网络类型。支持基础网络和私有网络。本教程以“基础网络”为例。基础网络和私有网络的区别请参见 [网络类型](/doc/product/213/5227)。
 - 实例版本。提供标准版和金融定制版。本教程以“标准版”为例。详细介绍请参考 [实例版本](/doc/product/237/6918)。
 - 数据库版本。提供 MariaDB 10.0.10 和 MariaDB 10.1.9 两个版本。不同可用区可能有所不同，具体以实际情况为准。本教程以 MariaDB 10.1.9 为例。
 - 实例规格和所需的硬盘。
 - 购买数量和购买时长。

 ![](//mc.qcloudimg.com/static/img/90a3065265c7be9af4151c97c9ee4658/image.png)
4. 进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，选择【TDSQL（MariaDB）】，查看刚才创建的云数据库实例。状态显示是 **未初始化**。
![](//mc.qcloudimg.com/static/img/a5f1f71b222633d6290287c0ab5b62b9/image.png)
5. 单击【初始化】，弹出初始化配置窗口，进行云数据库初始化操作。
![](//mc.qcloudimg.com/static/img/3d916c037e6cd988dac8f69416c8c15d/image.png)
6. 配置初始化参数，确认无误后，单击【确定】。初始化需要一定的时间，请耐心等待。当状态显示 **运行中**，表示云数据库初始化成功。
 - 支持的字符集。选择 MySQL 数据库支持的字符集。本教程以“utf8”为例。
 - 表名大小写敏感。表名是否大小写敏感，默认为是。
 - 开启强同步。开启强同步可以保证在主机故障时备机数据的一致性。默认为不开启，即同步方式为异步同步。
 - innodb_page_size。该数值为 Innodb 索引数据页长度，MariaDB 默认值为 16K。修改该值将影响索引创建，该值越小，性能越好。

 ![](//mc.qcloudimg.com/static/img/0bf59af9ccab51409e076915e8da6548/image.png)
7. 在 MariaDB 云数据库管理界面，单击【管理】，进入  MariaDB 云数据库实例详情页。
![](//mc.qcloudimg.com/static/img/f78e56bf13c5238c3bb793c3fd0367fa/image.png)
8. 在 MariaDB 云数据库实例详情页，单击【帐号管理】>【创建帐号】，弹出创建帐号页面。填写相关信息创建帐号，确认无误后，单击【确定】。**此步骤填写的帐号名和密码将在连接 MariaDB 云数据库时使用，请妥善保管。**
 - 帐号名。由字母、数字、下划线组成，字母开头，字母或数字结尾，最长 16 个字符组成。本教程以“test123”为例。
 - 主机。也可以理解为 HOST，支持 IP、IP 段、% 三种形式；% 代表结尾符，例如我们要支持 10.10.10.1~10.10.10.254 的所有主机 IP，可以输入 10.10.10.%；不输入代表 %。
 - 是否只读帐号。选中表示该帐号只能使用读请求（select）。
 - 密码。密码为 8~16 位的任意字符。腾讯云建议您的密码至少包括英文、数字和符号等，并定期修改密码。

 ![](//mc.qcloudimg.com/static/img/b5673f5c88f57d4a389fc4e673416659/image.png)
设置帐号拥有的权限，单击【保存配置】。
![](//mc.qcloudimg.com/static/img/38297ac6bb2bde4a085cddd53ba8dcd7/image.png)
查看帐号权限的配置是否正确，然后单击【关闭】完成配置。
![](//mc.qcloudimg.com/static/img/385bfb7ab899da5266a56242601a4c62/image.png)
9. 在 MariaDB 云数据库实例详情页，开通外网地址。当您需要从外网访问云数据库时，本步骤必选。其他情况下，本步骤可选。
![](//mc.qcloudimg.com/static/img/ed14405f61e54fe5225ae6ccfd3936f9/image.png)
> **注意：**
> 长期开放数据库外网 IP 可能存在安全风险，建议您在不需使用时及时关闭。
10. 在 MariaDB 云数据库实例详情页，单击【实例详情】，查看内网地址和外网地址。**内网地址和外网地址会在后续连接服务器时使用。**
![](//mc.qcloudimg.com/static/img/e6f96fedd4b9a01749258feadc25fec2/image.png)

## 二、连接 MariaDB 云数据库实例
连接 MariaDB 云数据库的方式有两种：
- 内网访问：使用腾讯云中一台与 MariaDB 数据库实例网络相通的 CVM 实例来访问 MariaDB 数据库实例的内网地址。此台 CVM 需要与数据库处于某个 VPC 下的同一个子网中，关于 VPC 的更多信息请查看 [VPC概述](/doc/product/215/535)。
- 外网访问：在外网的 Windows 或者 Linux 主机中，安装数据库客户端来访问腾讯云中的 MariaDB 云数据库实例的外网地址。

**注意：**
> 外网访问需要开启数据库实例的外网地址，从而使您的数据库服务暴露在公网上，此操作可能导致数据库被入侵或攻击。建议您使用内网访问的方式来登录数据库。

### 内网访问

1. 登录到与此数据库实例属于同一个可用区的网络可达的 CVM 主机，关于登录 CVM 主机请查看 [快速入门 Windows 云服务器](/document/product/213/2764) 或 [快速入门 Linux 云服务器](/document/product/213/2936)。网络可达是指此 CVM 主机与 MariaDB 数据库实例都处于基础网络之中，或者处于同一个 VPC 中。
2. 请根据 CVM 的操作系统选择推荐的连接方式。
**从 Windows 系统登录**
a. 下载并安装 MariadDB 的客户端。此步骤中我们推荐您使用 SQLyog，查看 [SQLyog 官网](https://www.webyog.com/) 以获得更多信息。
b. 打开 SQLyog，输入 MariaDB 数据库实例的内网 IP 和端口号，数据库帐号以及密码。
  - 我的 SQL 主机地址：本教程中输入 10.30.0.7。
  - 用户名：本教程中创建的用户名 test123。
  - 密码：用户 test123 对应的密码。
  - 端口：本教程中输入 3306。
![](//mc.qcloudimg.com/static/img/d4b72b365c7e31ac824851602ca5a29a/image.png)
c. 登录成功的界面如图所示，在此页面上您可以看到 MariaDB 数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](//mc.qcloudimg.com/static/img/7646040af53a923f47c4973a4aac7680/image.png)
**从 Linux 系统登录**
a. 以 CentOS 7.2 64 位系统的 CVM 为例，利用 CentOS 自带的包管理软件 Yum 去腾讯云的镜像源下载安装 MySQL 客户端。
相关命令为：
```
yum install mysql
```
![](//mc.qcloudimg.com/static/img/eee76fa95379b8a25fc076b66b4ca28c/image.png)
b. 使用 MySQL 命令行工具登录到 MariaDB 数据库。
相关命令为：
```
mysql -h hostname -u username -p
```
请将`hostname`替换为目标 MariaDB 数据库实例的内网 IP 地址，将`username`替换为本教程创建的用户`test123`，并在提示 **Enter password：** 后输入帐户 test123 对应的密码。本例中`hostname`为`10.30.0.7`。
![](//mc.qcloudimg.com/static/img/f8dccff34309cfd332f600f1ceb35ff1/image.png)
c. 在 **MySQL>** 提示符下可以发送 SQL 语句到要执行的 MariaDB 服务器。关于 SQL 语句的更多信息请参考 [MySQL 官方文档](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
例如执行以下命令，查看数据库基本信息。
```
show databases;
```
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

### 外网访问

1. 获取数据库的外网地址。
a. 单击运行中的 MariaDB 数据库实例的 ID 名，进入详情页。
![](//mc.qcloudimg.com/static/img/08e24afbf51b941df4b8c4a893857b31/image.png)
b. 在 **实例详情** 页中单击外网地址后的【打开】，开启此数据库实例的外网地址。
![](//mc.qcloudimg.com/static/img/e4793d117939c3f56c5f3d63b0491fe9/image.png)
c. 查看此数据库实例的外网地址。此例中，数据库的外网域名为：tdsql-6gy3mopk.gz.cdb.myqcloud.com，端口号为：114。
![](//mc.qcloudimg.com/static/img/e364724c2944099a9cd9c8c8c79fd96f/image.png)

2. 登录到数据库
**从Windows系统登录**
a. 下载 MariaDB 客户端并安装。此步骤中我们推荐您使用 SQLyog，查看 [SQLyog 官网](https://www.webyog.com/) 以获得更多信息。
b. 打开 SQLyog，输入 MariaDB 数据库实例的外网域名和端口号，数据库帐号以及密码。
  - 我的 SQL 主机地址：本教程中输入 tdsql-6gy3mopk.gz.cdb.myqcloud.com。
  - 用户名：本教程中创建的用户名 test123。
  - 密码：用户 test123 对应的密码。
  - 端口：本教程中输入 114。
![](//mc.qcloudimg.com/static/img/1924e51d3519bab0ab9705217466fec2/image.png)
c. 登录成功的界面如图所示，在此页面上您可以看到 MariaDB 数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](//mc.qcloudimg.com/static/img/d050b1917e7ccfea62a9ec7c8992c313/image.png)

 **从Linux系统登录**
a. 以 CentOS 7.2 64 位系统的 CVM 为例，官网下载安装 MySQL 客户端。具体命令为：
```
yum intall mysql
```
b. 使用 MySQL 命令行工具登录到 MariaDB 数据库。相关命令为：
```
mysql -h hostname -P port -u username -p
```
请将`hostname`替换为目标 MariaDB 数据库实例的外网 IP 地址，将`username`替换为本教程创建的用户`test123`，并在提示 **Enter password：** 后输入帐户 test123 对应的密码。本例中`hostname`为`tdsql-6gy3mopk.gz.cdb.myqcloud.com`，`port` 为 114。
![](//mc.qcloudimg.com/static/img/230ca6d65526050e062c3f59186d4e6c/image.png)
c. 在 **MySQL>** 提示符下可以发送 SQL 语句到要执行的 MariaDB 服务器。关于 SQL 语句的更多信息请参考 [MySQL 官方文档](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
例如执行以下命令，查看数据库基本信息。
```
show databases;
```
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

## 三、删除 MariaDB 云数据库实例
1. 在 MariaDB 云数据库实例详情页，单击【帐号管理】>【删除帐号】。删除帐号需要一定的时间，请耐心等待。
![](//mc.qcloudimg.com/static/img/43cd5692d7a07ad2e5c6bf26cf134090/image.png)
2. MariaDB 云数据库实例暂时不支持手动删除，到期后没有续费将会自动停止。
