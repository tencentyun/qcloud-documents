连接到MariaDB数据库的方式有两种：
- 内网访问：使用腾讯云中一台与MariaDB数据库实例网络相通的CVM来访问MariaDB数据库实例的内网地址。（注意：此台CVM需要与数据库处于某个VPC下的同一个子网中，关于VPC的更多信息请查看<a href="https://cloud.tencent.com/document/product/215/20046" target="_blank">VPC概述</a>。）
- 外网访问：在外网的Windows或者Linux主机中，安装数据库客户端来访问腾讯云中的MariaDB数据库实例的外网地址。

<font color="red">**安全提示：**</font>外网访问需要开启数据库实例的外网地址，从而使您的数据库服务暴露在公网上，此操作可能导致数据库被入侵或攻击。建议您使用内网访问的方式来登录数据库。

无论从内网还是外网访问，都需要先创建帐号。
## 创建帐号
1. 在[腾讯云控制台](https://console.cloud.tencent.com/)中，进入菜单【云产品】-【关系型数据库】-【TDSQL(MariaDB)】-【实例列表】，单击运行中的MariaDB数据库实例的ID名，进入详情页。
![](//mc.qcloudimg.com/static/img/08e24afbf51b941df4b8c4a893857b31/image.png)
2. 在**帐号管理**页单击【创建帐号】，并设置帐号的相关权限。此处以帐号test123为例，开通全部权限。
创建帐号，设置密码，并单击【确定】。
![](//mc.qcloudimg.com/static/img/b5673f5c88f57d4a389fc4e673416659/image.png)
设置帐号test123拥有的权限，单击【保存配置】。
![](//mc.qcloudimg.com/static/img/38297ac6bb2bde4a085cddd53ba8dcd7/image.png)
查看帐号权限的配置是否正确，然后单击**关闭**完成配置。
![](//mc.qcloudimg.com/static/img/385bfb7ab899da5266a56242601a4c62/image.png)
如需了解更多关于帐号创建的信息，请参考[帐号创建](https://cloud.tencent.com/document/product/237/7054)。

## 访问数据库
连接到MariaDB数据库的方式有两种：
 - 内网访问：使用腾讯云中一台与MariaDB数据库实例网络相通的CVM来访问MariaDB数据库实例的内网地址。（注意：此台CVM需要与数据库处于某个VPC下的同一个子网中，关于VPC的更多信息请查看<a href="https://cloud.tencent.com/document/product/215/20046" target="_blank">VPC概述</a>。）
 - 外网访问：在外网的Windows或者Linux主机中，安装数据库客户端来访问腾讯云中的MariaDB数据库实例的外网地址。

### 内网访问

1. 登录到与此数据库实例属于同一个可用区的网络可达的CVM主机，关于登录CVM主机请查看<a href="https://cloud.tencent.com/document/product/213/2764" target="_blank">WIndows CVM入门</a>或<a href="https://cloud.tencent.com/document/product/213/2936" target="_blank">Linux CVM入门</a>。网络可达是指此CVM主机与MariaDB数据库实例都处于基础网络之中，或者处于同一个VPC中。
2. 请根据CVM的操作系统选择推荐的连接方式。
**-从Windows系统登录**
1). 下载并安装MariadDB的客户端。此步骤中我们推荐您下载sqlyog，官网地址如下：https://www.webyog.com/ 。
2). 打开sqlyog，输入输入MariaDB数据库实例的内网IP和端口号，数据库帐号以及密码。
 - 我的SQL主机地址：此例中输入10.30.0.7。
 - 用户名：用前文中创建的用户名test123。
 - 密码：用户test123对应的密码。
 - 端口：此例中输入3306。
![](//mc.qcloudimg.com/static/img/d4b72b365c7e31ac824851602ca5a29a/image.png)
3). 登录成功的界面如图所示，在此页面上您可以看到MariaDB数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](//mc.qcloudimg.com/static/img/7646040af53a923f47c4973a4aac7680/image.png)
**-从Linux系统登录**
1). 以CentOS 7.2 64位系统的CVM为例，利用CentOS自带的包管理软件Yum去腾讯云的镜像源下载安装MySQL客户端。
相关命令为：
`yum install mysql`
图示如下：![](//mc.qcloudimg.com/static/img/eee76fa95379b8a25fc076b66b4ca28c/image.png)
2). 使用MySQL命令行工具登录到MariaDB数据库。
相关命令为：
`mysql -h hostname -u username -p`
请将hostname替换为目标MariaDB数据库实例的内网IP地址，将username替换为之前创建的用户test123，并在提示**Enter password：**后输入账户test123对应的密码。
本例中hostname为10.30.0.7。
![](//mc.qcloudimg.com/static/img/f8dccff34309cfd332f600f1ceb35ff1/image.png)
3). 在MySQL>提示符下可以发送SQL语句到要执行的MariaDB服务器，具体命令行请参考此网站：<https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html>
下图中以`show databases；`为例。
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

### 外网访问
<font color="red">**安全提示：**</font>外网访问需要开启数据库实例的外网地址，从而使您的数据库服务暴露在公网上，此操作可能导致数据库入侵或攻击。
1. 获取数据库的外网地址。
1). 单击运行中的MariaDB数据库实例的ID名，进入详情页。
![](//mc.qcloudimg.com/static/img/08e24afbf51b941df4b8c4a893857b31/image.png)
2). 在**实例详情**页单击外网地址后的【打开】，开启此数据库实例的外网地址。
![](//mc.qcloudimg.com/static/img/e4793d117939c3f56c5f3d63b0491fe9/image.png)
3). 查看此数据库实例的外网地址。
下图中，此数据库的外网域名为：	tdsql-6gy3mopk.gz.cdb.myqcloud.com，端口号为：114
![](//mc.qcloudimg.com/static/img/e364724c2944099a9cd9c8c8c79fd96f/image.png)

2. 登录到数据库
**-从Windows系统登录**
1). 下载一个MariaDB客户端并安装。此步骤中我们推荐您下载sqlyog，官网地址如下：https://www.webyog.com/ 。
2). 打开sqlyog，输入输入MariaDB数据库实例的外网域名和端口号，数据库帐号以及密码。
 - 我的SQL主机地址：此例中输入tdsql-6gy3mopk.gz.cdb.myqcloud.com。
 - 用户名：用前文中创建的用户名test123。
 - 密码：用户test123对应的密码。
 - 端口：此例中输入114。
![](//mc.qcloudimg.com/static/img/1924e51d3519bab0ab9705217466fec2/image.png)
3). 登录成功的界面如图所示，在此页面上您可以看到MariaDB数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。![](//mc.qcloudimg.com/static/img/d050b1917e7ccfea62a9ec7c8992c313/image.png)
 
**-从Linux系统登录**
1). 以CentOS 7.2 64位系统的CVM为例，去官网下载安装MySQL客户端。具体命令为：
`
yum intall mysql
`
2). 使用MySQL命令行工具登录到MariaDB数据库。相关命令为：
`
mysql -h hostname -P port -u username -p
`
请将hostname替换为目标MariaDB数据库实例的外网IP地址，将username替换为之前创建的用户test123，并在提示**Enter password：**后输入账户test123对应的密码。
本例中hostname为tdsql-6gy3mopk.gz.cdb.myqcloud.com，port为114。
![](//mc.qcloudimg.com/static/img/230ca6d65526050e062c3f59186d4e6c/image.png)
3). 在MySQL>提示符下可以发送SQL语句到要执行的MariaDB服务器，具体命令行请参考此网站：
<https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html>
下图中以 `show databases；`为例。
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)


