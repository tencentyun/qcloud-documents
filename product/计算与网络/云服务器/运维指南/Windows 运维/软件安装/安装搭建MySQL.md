## 操作场景
本文档以 Windows Server 2012 R2 数据中心版 64位中文版操作系统云服务器为例，介绍搭建 MySQL 5.5 的具体步骤。
通常情况下 Windows 系统经常使用 SQL Server 数据库，但由于 SQL Server 属于收费产品需要您自行授权，您也可购买 [腾讯云云数据库 TencentDB for SQL Server 实例](http://cloud.tencent.com/product/sqlserver.html)。

## 操作步骤

### 下载 MySQL 安装包
1. 登录云服务器。
2. 在云服务器中打开浏览器，并访问 `https://dev.mysql.com/downloads/mysql/5.5.html#downloads`，下载 MySQL 安装包。如下图所示：
![](https://main.qcloudimg.com/raw/b96236244404b3e65d3e750dec8ea8c0.png)

### 安装 MySQL

1. 双击打开 MySQL 安装包，并在 “MySQL Server 5.5 Setup” 安装界面单击【Next】。
2. 勾选【I accept the terms in the License Agreement】，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/fd10bf4885214fc586940663f37b29bd.png)
3. 单击【Typical】。如下图所示：
Typical 表示典型安装方式。
![](https://main.qcloudimg.com/raw/85292c920bafd81c341e23214c01eac7.png)
4. 单击【Install】，安装 MySQL。如下图所示：
![](https://main.qcloudimg.com/raw/e4e73dd70f382ed5d3abcbda619f07ea.png)
5. 勾选【Luanch the MySQL Instance Configuration Wizard】，单击【Finish】。如下图所示：
关闭 MySQL 安装窗口，进入 MySQL 的配置向导界面。
![](https://main.qcloudimg.com/raw/46932c0a2868178be1cbdb1af02a1716.png)

### 配置 MySQL

1. 在 MySQL 的配置向导界面，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/018a37f73b3493f2f72a58393530eb60.png)
2. 选择【Detailed Configuration】，单击【Next】。如下图所示：
>? 本操作步骤以 Detailed Configuration 为例。
>
![](https://main.qcloudimg.com/raw/64374e0257e0b5c13838bd4fc2a3631e.png)
 - Detailed Configuration（详细配置），适合想要更加细粒度控制服务器配置的高级用户。
 - Standard Configuration（标准配置），适合想要快速启动 MySQL 而不必考虑服务器配置的新用户。但标准配置可能与操作系统不兼容，推荐您选择详细配置。
3. 选择【Developer Machine】，单击【Next】。如下图所示：
>? 本操作步骤以 Developer Machine 为例。
>
![](https://main.qcloudimg.com/raw/40ba999555a5f7de8299aeb09b4f7fdd.png)
 - Developer Machine（开发者机器），代表典型个人用桌面工作站。同时运行多个桌面应用程序时，将 MySQL 服务器配置成占用最少资源的状态。
 - Server Machine（服务器机器），代表服务器。MySQL 服务器可以同其它应用程序一起运行，例如 FTP 、 email 和 web 服务器。 MySQL 服务器配置成占用适当比例资源的状态。
 - Dedicated MySQL Server Machine（专用 MySQL 服务器），代表只运行 MySQL 服务的服务器。MySQL 服务器配置成可占用所有资源的状态。
4. 选择【Multifunctional Database】，单击【Next】。如下图所示：
>? 本操作步骤以 Multifunctional Database 为例。
>
![](https://main.qcloudimg.com/raw/20a581e1af44694cc0f3188438f10742.png)
 - Multifunctional Database（多功能数据库），同时使用 InnoDB 和 MyISAM 储存引擎，并在两个引擎之间平均分配资源。建议经常使用两个储存引擎的用户选择该选项。
 - Transactional Database Only（仅事务处理数据库），同时使用 InnoDB 和 MyISAM 储存引擎，大多数服务器资源指派给 InnoDB 储存引擎。建议经常使用 InnoDB ，偶尔使用 MyISAM 的用户选择该选项。
 - Non-Transactional Database Only（仅非事务处理数据库），完全禁用 InnoDB 储存引擎，所有服务器资源指派给 MyISAM 储存引擎。建议不使用 InnoDB 的用户选择该选项。
5. 保持默认配置，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/7cef832b46fdf9855d02e21762ce8978.png)
6. 选择【Decision Support (DSS)/OLAP】，单击【Next】。如下图所示：
>? 本操作步骤以 Decision Support (DSS)/OLAP 为例。
>
![](https://main.qcloudimg.com/raw/6e0158904bd05862c423d84b33adb260.png)
 - Decision Support (DSS)/OLAP（决策支持），适合不需要大量的并行连接情况。
 - Online Transaction Processing (OLTP)（联机事务处理），适合需要大量的并行连接情况。
 - Manual Setting（人工设置），适合手动设置服务器并行连接的最大数目。
7. 设置 TCP/IP 网络，配置连接 MySQL 服务器的端口号，单击【Next】。如下图所示：
>? 
> - 默认启用 TCP/IP 网络。
> - 默认使用 3306 端口。
> 
![](https://main.qcloudimg.com/raw/15dafbfbb27d6195effc8d94aa9a109f.png)
8. 选择【Standard Character Set】，单击【Next】。如下图所示：
>? 本操作步骤以 Standard Character Set 为例。
>
![](https://main.qcloudimg.com/raw/d995acdb742ead678d3909305e560e7f.png)
 - Standard Character Set（标准字符集），默认 Latin1 作为服务器字符集。
 - Best Support For Multilingualism（支持多种语言），默认 UTF8 作为服务器字符集。
 - Manual Selected Default Character Set/Collation（人工设置/校对规则），从下拉列表中选择期望的字符集。 
9. 勾选【Install As Windows Service】和【Include Bin Directory in Windows PATH】，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/4e3f9b7c330a0f59e3ed319ddc8b882d.png)
10. 设置 root 的密码，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/8c66302686ca7c47eb32583b4722e4f8.png)
11. 单击【Execute】，配置 MySQL。如下图所示：
![](https://main.qcloudimg.com/raw/328fa1f3eb39ed00f9492ffcf5b93c46.png)
12. 单击【Finish】，完成配置。

### 验证 MySQL 是否安装成功

1. 在操作系统界面，右键单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin: 0;"></img> > 【运行】，打开运行框。
2. 在运行框中输入 **cmd**，按 **Enter**，打开管理员命令框。
3. 在管理员命令框中，执行以下命令。
```
mysql -u root -p
```
4. 输入设置的 root 密码，按 **Enter**，登录 MySQL。
若显示如下界面信息，则表示安装配置成功。
![](https://main.qcloudimg.com/raw/c5269c7e1acfedd3038dc60c74a2850f.png)




