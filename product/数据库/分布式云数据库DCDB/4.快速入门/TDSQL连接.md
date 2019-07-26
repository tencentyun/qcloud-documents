以下为连接 TDSQL 的相关操作流程。
## 准备工作
### 新建用户权限
1. 在 [TDSQL 控制台](https://console.cloud.tencent.com/dcdb) 中，单击需要操作的实例最右方的【管理】，进入实例详情页面。
![](https://mc.qcloudimg.com/static/img/d2eafea1a7b03224961c0906180e6b22/image.png)
2. 在实例详情页面单击【账号管理】，进入帐号管理页面后单击【创建帐号】。
![](https://mc.qcloudimg.com/static/img/4e60badccaa63bf1632dbe1ed948793f/r2.png)
3. 依次输入帐号名、主机、密码、备注，检查无误后单击【确定】，进入设置权限页面。
主机名实际是网络出口地址。这里支持%这样的匹配方式，代表所有IP均可访问。
![](https://mc.qcloudimg.com/static/img/00f4abaa96562c16f0aa3a3af0e30c00/r3.png)
4. 在设置权限页面，根据需求分配权限后，单击【保存设置】即可完成权限分配。若需要稍后设置权限，单击【之后设置】即可。
通过左边的导航栏，我们提供了完全兼容 MySQL 管理方式的图形化界面，权限管理可以细化到列级。
![](https://mc.qcloudimg.com/static/img/9029ee57e3892fe92ac0c3a5ead80dbb/r4.png)
5. 完成创建后，单击【修改权限】可以修改用户权限，单击【克隆帐号】可以完全复制当前帐号权限来新建一个帐号。单击【更多】可以重置密码和删除帐号。
![](https://mc.qcloudimg.com/static/img/5f87261b43fc058adbd66b486a69e571/r5.png)

### 获取外网地址
1. 进入实例详情页面，在基本信息中找到外网地址，单击【打开】。
![](https://mc.qcloudimg.com/static/img/fc3d50322e3547722a8d3e29e479b2e5/r6.png)	
2. 稍等片刻后，即可获得外网地址以及端口号。
TDSQL 提供了唯一的 IP、端口供用户访问和使用。
![](https://mc.qcloudimg.com/static/img/234c21d6897515b6623055301771dd24/r7.png)

## 连接步骤
在创建用户权限和获取外网地址后，TDSQL 可通过第三方工具和程序驱动进行连接。在 Windows 端，以命令行连接、客户端连接和 JDBC 驱动连接三种方式为示例。在LINUX 端，以命令行连接为示例。

### Windows 命令行连接
1. 打开 Windows 命令行，在 mysql 的正确路径下输入以下命令。

		mysql -h外网地址 -P端口号 -u用户名  -p
		Enter password: **********（输入密码）

- 将相关代码正确输入后，显示如下信息，成功连接数据库，下一步即可进行数据库内相关操作。

		Welcome to the MySQL monitor.  Commands end with ; or \g.

### Windows 客户端连接
1. 下载一个标准的 SQL 客户端，例如 MySQL Workbench 、SQLyog 等。这里我们以 SQLyog 为示例。
2. 打开 SQLyog 选择【文件】>【新连接】，输入对应的主机地址、端口、用户名和密码，单击【连接】。
> 我的 SQL 主机地址：输入前面获得的外网地址。
> 用户名：输入前面创建用户的用户名。
> 密码：输入前面创建用户的密码。
> 端口：输入获取外网地址所分配的端口。

	![](//mc.qcloudimg.com/static/img/ee0a9b423103292797873f78637e960b/image.png)
3. 成功连接后的界面如图所示，在此页面即可进行数据库内相关操作。![](//mc.qcloudimg.com/static/img/93ecf636452505760086db5972d5fc6b/image.png)

### Windows JDBC驱动连接
> TDSQL 支持程序驱动连接，这里我们以 Java 使用 JDBC Driver for MySQL (Connector/J) 连接 TDSQL 为示例。

1. 首先在 MySQL 官网[下载](https://dev.mysql.com/downloads/connector/j/5.0.html)一个JDBC的jar包，将其导入 Java 引用的 Library 中。
2. 调用 JDBC 代码如下：
```
		public static final String url = "外网地址";
		public static final String name = "com.mysql.jdbc.Driver";//调用JDBC驱动
		public static final String user = "用户名";
		public static final String password = "密码";
		//JDBC
		Class.forName("com.mysql.jdbc.Driver"); 
				Connection conn=DriverManager.getConnection("url, user, password");
		//
		conn.close();
```
3. 连接成功后，下一步即可进行其他数据库内操作。
>!因为 TDSQL 在分表和插入数据时需要标记 shardkey，所以无法用 JDBC 调用这些操作。

### Linux 命令行连接
以腾讯云服务器中 CentOS 7.2 64 位系统的 CVM 为例，关于腾讯云服务器的购买详情，可以参考[云服务器选购](https://buy.cloud.tencent.com/cvm)。
1. 登录 Linux 后，输入命令 `yum install mysql` ,利用 CentOS 自带的包管理软件 Yum 在腾讯云的镜像源中下载安装 MySQL 客户端。
![](//mc.qcloudimg.com/static/img/7f6a1f7a953cc38809fa069182481a22/image.png)
2. 命令行显示 complete 后，MySQL 客户端安装完成。我们输入命令 `mysql -h外网地址 -P端口 -u用户名 -p密码` 连接 TDSQL。下一步即可进行分表操作。下图中以`show databases;`为例。![](//mc.qcloudimg.com/static/img/b3fba8f8ace315e5eba05fdd252bd4c0/image.png)
