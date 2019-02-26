连接到MySQL数据库的方式有两种：
- 内网访问：使用在同一个可用区的CVM来访问自动分配给数据库的内网地址。这种方式使用内网高速网络，延迟低。（注意：此台CVM需要与数据库同时处于基础网络中，或者属于同一个VPC，关于VPC的更多信息请查看<a href="https://cloud.tencent.com/document/product/215/535" target="_blank">VPC概述</a>。）
- 外网访问：借助外网账号，通过腾讯云控制台中的登录入口，登录到phpMyAdmin界面对数据库进行操作。

<font color="red">**安全提示：**</font>外网访问需要开启数据库实例的外网地址，从而使您的数据库服务暴露在公网上，此操作可能导致数据库被入侵或攻击。建议您使用内网访问的方式来登录数据库。
# 内网访问
1. 登录到与此数据库实例属于同一个可用区的网络可达的CVM主机。
关于登录CVM主机请查看<a href="https://cloud.tencent.com/document/product/213/2783" target="_blank">WIndows CVM入门</a>或<a href="https://cloud.tencent.com/document/product/213/2973" target="_blank">Linux CVM入门</a>。网络可达是指此CVM主机与MySQL数据库实例都处于基础网络之中，或者处于同一个VPC中。
1. 请根据CVM的操作系统选择推荐的连接方式。
**-从Windows系统登录**
1). 下载一个标准的SQL客户端。此步骤中我们推荐您下载MySQL Workbench，这是Windows系统下较常见的SQL客户端。在CVM中打开https://dev.mysql.com/downloads/workbench/ ，根据您的系统来下载适配版本的安装程序。
![](//mc.qcloudimg.com/static/img/4d7e6c56f02aad86f232e5cdd8c0bb17/image.png)
2). 界面上将提示【Login】, 【Sign Up】和【No, thanks, just start my download.】， 请选择【No, thanks, just start my download.】来快速下载。
	![](//mc.qcloudimg.com/static/img/7169ce063b1b41c58c48089bc2a61441/image.png)
3). 在此台CVM上安装MySQL Workbench。前置条件：此电脑上需要安装Microsoft .NET Framework 4.5和Visual C++ Redistributable for Visual Studio 2015。 您可以点击MySQL Workbench安装向导中的【Download Prerequisites】来安装这两个软件，然后安装MySQL Workbench。
	![](//mc.qcloudimg.com/static/img/bcf08cec72e8ea9c490cb30ae79f0da4/image.png)
	4). 打开MySQL Workbench，选择【Database】-【Connect to Database】，输入MySQL数据库实例的内网地址和用户名，密码，点击【OK】进行登录。
 - Hostname：输入内网地址。在控制台中的MySQL数据库实例详情页可以查看到目标数据库实例的内网地址，此处以10.66.238.24为例。
 - Port：3306，保持为默认端口即可。
 - Username：默认为root。
 - Password：输入您在初始化数据库实例时设置的密码。
	![](//mc.qcloudimg.com/static/img/feb4b95b1038532330e876a605016b87/image.png)
5). 登录成功的界面如图所示，在此页面上您可以看到MySQL数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
	![](//mc.qcloudimg.com/static/img/abd8efce579343d25f534143c19c132e/image.png)
	
**-从Linux系统登录**
1). 以CentOS 7.2 64位系统的CVM为例，利用CentOS自带的包管理软件Yum去腾讯云的镜像源下载安装MySQL客户端。
	相关命令为：
	```yum install mysql```
	图示如下：
	![](//mc.qcloudimg.com/static/img/eee76fa95379b8a25fc076b66b4ca28c/image.png)
2). 使用MySQL命令行工具登录到MySQL。相关命令为：
```mysql -h hostname -u username -p```
请将hostname替换为目标MySQL数据库实例的内网IP地址，将username替换为默认的用户名root，并在提示Enter password：后输出root账户对应的密码。
	本例中hostname为10.66.238.24。
![](//mc.qcloudimg.com/static/img/d1da9f59f0fff77ad2a8ff18e0b11e7c/image.png)
3). 在MySQL>提示符下可以发送SQL语句到要执行的MySQL服务器，具体命令行请参考此网站：https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html
下图中以show databases；为例:
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

# 外网访问
<font color="red">**安全提示：**</font>外网访问需要开启数据库实例的外网地址，从而使您的数据库服务暴露在公网上，此操作可能导致数据库被入侵或攻击。
请根据外网中主机的操作系统选择对应的登录方式。
**- 从Windows系统登录**
1. 在[腾讯云控制台](https://console.cloud.tencent.com/)中，依次单击【云产品】-【关系型数据库】-【MySQL】-【实例列表】，选择状态为运行中的目标实例，点击【登录】。
![](//mc.qcloudimg.com/static/img/248ca91c3b13e3f249c752f43019ed1a/image.png)
1. 在数据管理控制台的登录界面，帐号输入root，密码为之前在初始化选项中配置的root账户的密码，点击【登录】来登录。
![](//mc.qcloudimg.com/static/img/b5538d93dc27d99af6fed9f0e5c9b798/image.png)
1. 在数据管理页面可以查看实例的状态和基本信息。点击【返回PMA】访问数据库。
![](//mc.qcloudimg.com/static/img/ceab808b44adf5feba818e70a079b83e/image.png)
1. 您现在已经通过phpMyAdmin成功连接到MySQL数据库，在此页面上您可以看到MySQL数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](//mc.qcloudimg.com/static/img/c8f60117f5aec772663d3c7890c96b1e/image.png)

**-从Linux系统登录**
1. 在腾讯云控制台中，选择【云产品】-【关系型数据库】-【MySQL-实例列表】，点击目标实例的ID进入实例详情页。
![](//mc.qcloudimg.com/static/img/018350e48f1d535d105c3c6340d36b2d/image.png)
1. 在实例详情页点击外网地址后的【开启】，设置外网访问帐号cdb_outerroot对应的密码，点击【确定】。
![](//mc.qcloudimg.com/static/img/730e65a8b10f429a80ea15456b9a7193/image.png)
![](//mc.qcloudimg.com/static/img/48a8489d3c0341ef87627fdc108f93e7/image.png)
1. 实例详情页会显示开通后的外网地址，随后的步骤里会用到此地址。
![](//mc.qcloudimg.com/static/img/3d1176c8958f8ffc0e1f2594fc7f3141/image.png)
1. 以CentOS 7.2 64位系统为例，利用CentOS自带的包管理软件Yum去下载安装MySQL客户端。
	相关命令为：
	```yum install mysql```
1. 使用MySQL命令行工具登录到MySQL。
相关命令为：
```mysql -h hostname -P port -u username -p```
请将hostname替换为目标MySQL数据库实例的外网IP地址，将port替换为外网端口号将username替换为默认的外网访问用户名cdb_outerroot，并在提示**Enter password：**后输出cdb_outerroot账户对应的密码。
本例中hostname为59281c4e4b511.gz.cdb.myqcloud.com，外网端口号为15311。
![](//mc.qcloudimg.com/static/img/48df6390ccf7669d04403cd84b8b6fad/image.png)
1. 在MySQL>提示符下可以发送SQL语句到要执行的MySQL服务器，具体命令行请参考此网站：https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html
下图中以show databases；为例。
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)
