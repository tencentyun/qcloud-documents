本文档使用 Windows Server 2012 R2 示例，介绍搭建 MySQL 5.5 的具体步骤。

通常情况下 Windows 系统经常使用 SQL Server 数据库，但由于 SQL Server 属于收费产品需要您自行授权，也可购买 [腾讯云 SQL Server 数据库 CDB 实例](http://www.qcloud.com/product/sqlserver.html) 。

## 步骤一：下载 MySQL 安装包
在云服务器中打开浏览器，输入下载地址：https://dev.mysql.com/downloads/mysql/5.5.html#downloads
![](//mc.qcloudimg.com/static/img/86343df911820dde5f95ace650bd5f4b/image.png)

## 步骤二：安装程序
 1. 运行安装程序，单击【下一步(Next)】，勾选同意协议。
	![](//mc.qcloudimg.com/static/img/1d16c11baba35894e4fcf7acd93601e4/image.png)
 
 2. 选择典型安装方式(Typical)。
	![](//mc.qcloudimg.com/static/img/1a84c1064bbfeea0696f2ccbe0b2e94e/image.png)

 3. 勾选引导配置 MySQL 的选项（Luanch the MySQL Instance Configuration Wizard）
	![](//mc.qcloudimg.com/static/img/1a6b6ad499c0c00d294d6f24d5ee1645/image.png)

## 步骤三：配置 MySQL


 1. 配置 MySQL 的类型。此处以详细配置(Detailed Configuration)为例。
  - 详细配置(Detailed Configuration)，适合想要更加细粒度控制服务器配置的高级用户。
  - 标准配置(Standard Configuration)，适合想要快速启动 MySQL而不必考虑服务器配置的新用户。
 
 > **注意：**
 > 标准配置(Standard Configuration)可能与操作系统不兼容。推荐选择详细配置。

	![](//mc.qcloudimg.com/static/img/434424a84d76f9492c511f567ae2d03f/image.png)
 
 2.  配置 MySQL 服务器类型。此处以开发机器(Developer Machine)为例。
  - 开发机器(Developer Machine)，代表典型个人用桌面工作站。同时运行多个桌面应用程序时，将 MySQL 服务器配置成占用最少资源的状态。
  - 服务器(Server Machine)，代表服务器，MySQL 服务器可以同其它应用程序一起运行，例如 FTP 、 email 和 web 服务器。 MySQL 服务器配置成占用适当比例资源的状态。
  - 专用 MySQL 服务器(Dedicated MySQL Server Machine)，代表只运行 MySQL 服务的服务器。MySQL 服务器配置成可占用所有资源的状态。

	![](//mc.qcloudimg.com/static/img/2eac8b38999f31d3cd70d7c421388730/image.png)

 3. 配置 MySQL 数据库。此处以多功能数据库(Multifunctional Database)为例。
  - 多功能数据库(Multifunctional Database)，同时使用 InnoDB 和 MyISAM 储存引擎，并在两个引擎之间平均分配资源。建议经常使用两个储存引擎的用户选择该选项。
  - 仅事务处理数据库(Transactional Database Only)，同时使用 InnoDB 和 MyISAM 储存引擎，大多数服务器资源指派给 InnoDB 储存引擎。建议经常使用 InnoDB ，偶尔使用 MyISAM 的用户选择该选项。
  - 仅非事务处理数据库(Non-Transactional Database Only)，完全禁用 InnoDB 储存引擎，所有服务器资源指派给 MyISAM 储存引擎。建议不使用 InnoDB 的用户选择该选项。
  
 ![](//mc.qcloudimg.com/static/img/50599f06e56eb01dd4c91d615005c618/image.png)

 4. 配置 MySQL的 InnoDB 表空间。此处选择的默认配置。
	![](//mc.qcloudimg.com/static/img/c8ef95275e181b08cdada4b6ebe99f8c/image.png)

 5. 配置 MySQL 并发连接。此处以决策支持(Decision Support)为例。
  - 决策支持(Decision Support)，适合不需要大量的并行连接情况。
  - 联机事务处理(Online Transaction Processing)，适合需要大量的并行连接情况。
  - 人工设置(Manual Setting)，适合手动设置服务器并行连接的最大数目。
 
	 ![](//mc.qcloudimg.com/static/img/4c0e84f14e4b6a040fa4768b0fb07c37/image.png)

 6. 配置 MySQL 的网络选项。可以启用或禁用 TCP/IP 网络，并配置用来连接 MySQL 服务器的端口号。
 > **注意：**
 > 默认情况启用TCP/IP网络。
 > 默认使用3306端口。
 
	 ![](//mc.qcloudimg.com/static/img/b864e47b1e4b0e87cd5015007f9bd8dc/image.png)

 7. 配置 MySQL 字符集。此处以标准字符集(Standard Character Set)为例。
  - 标准字符集(Standard Character Set)，默认 Latin1 做为服务器字符集。
  - 支持多种语言(Best Support For Multilingualism)，默认 UTF8 做为服务器字符集。
  - 人工设置/校对规则( Manual Selected Default Character Set/Collation)，从下拉列表中选择期望的字符集。
 
	![](//mc.qcloudimg.com/static/img/f7a8e52f06552c1d6a8da1fd8b8a2c31/image.png)

 8. 配置 MySQL 服务选项。建议两种都选择上以便使用命令行管理 MySQL 。
	![](//mc.qcloudimg.com/static/img/361ce058ffc35e6cc56332d8ce2c589c/image.png)

 9. 设置 root 密码。
	![](//mc.qcloudimg.com/static/img/a7a68d4be1baec04fda1724ede597f05/image.png)

 10. 完成配置。单击 【Excute】 完成安装。
	![](//mc.qcloudimg.com/static/img/fd815f05c40d11c61d801a321131e3ec/image.png)

## 步骤四：登录 MySQL 测试

1. 在云服务器中，单击【开始】，单击【搜索(图标)】，输入```cmd```，打开管理员命令框：
![](//mc.qcloudimg.com/static/img/a06bef4aa01469b23dc5c810b007fdbc/image.png)

2. 输入命令```mysql -u root -p```，回车。
 
3. 通过设置的 root 密码登录 MySQL ，显示下图表示安装配置成功。
![](//mc.qcloudimg.com/static/img/1eb8350471ca12c198ad9b851c9c7a38/image.png)


