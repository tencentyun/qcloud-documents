
本文为您介绍创建云数据库 SQL Server 实例，然后在 Windows 云服务器中通过 SQL Server Management Studio（SSMS）连接到该数据库实例并运行简单的查询，以及删除该数据库实例的具体操作。
如果您想要在本地使用 SQL Server Management Studio（SSMS） 连接到 SQL Server 云数据库，请参见 [创建并连接 SQL Server 云数据库（本地端）](/doc/product/238/11627)。

>!创建云数据库 SQL Server 实例之前，您必须拥有一个腾讯云账号。可参见 [账号相关](https://cloud.tencent.com/document/product/378/17985) 注册腾讯云账号。

## 创建云数据库 SQL Server 实例
1. 登录 [云数据库控制台](https://console.cloud.tencent.com/cdb)。选择【SQLServer】>【实例列表】页。
![](https://main.qcloudimg.com/raw/c8a5843dc5f1ddecb1e7767f848ca895.png)
2. 单击【+新建】，在购买页中，选择数据库相关配置。确认无误后，单击【立即购买】。
 - 【计费模式】：目前只支持包年包月。
 - 【地域】和【可用区】：地域说明请参见 [地域与可用区](/doc/product/236/8458)。本文以广州和广州三区为例。
 - 【网络类型】：支持基础网络和私有网络。基础网络和私有网络的区别请参见 [网络环境](/doc/product/213/5227)。本文以基础网络为例。
 - 【数据库版本】：支持 SQL Server 2008 R2、SQL Server 2012、SQL Server 2016 SP1 两个版本。不同可用区可能有所不同，具体以实际情况为准。本文以 SQL Server 2012 为例。
 - 选择实例规格和所需的硬盘。
 - 选择购买数量和购买时长。
![](https://main.qcloudimg.com/raw/85a55961d655af3870919df938dddaf0.png)
3. 返回 SQL Server 实例列表，查看刚才创建的云数据库实例，待运行状态显示【运行中】，表示实例创建成功。
4. 在实例的【操作】列，单击【管理】，进入实例详情页。
5. 在实例详情页，选择【帐号管理】>【创建帐号】，在弹出的创建帐号页填写相关信息，确认无误后，单击【确定】。
**此步骤填写的帐号名和密码将在连接 SQL Server 云数据库时使用，请妥善保管。**本教程以 test 为例。
![](//mc.qcloudimg.com/static/img/1cac253d8eb9029bbaf10aa385b4c0bd/image.png)
6. 在实例详情页，选择【数据库管理】>【创建数据库】，在弹出的创建数据库页填写相关信息，确认无误后，单击【确定】。
本步骤将数据库的 **读写权限** 或者 **只读权限** 授权给第 上一步中创建的帐号。
![](//mc.qcloudimg.com/static/img/8db9f2aaa65978c0e0005739c7861aad/image.png)

## 连接云数据库 SQL Server 实例（Windows 云服务器）
1. 登录腾讯云 Windows 云服务器。如果您还没有腾讯云 Windows 云服务器，请参见 [快速入门 Windows 云服务器](/doc/product/213/2764)。本文以 Windows Server 2012 R2 标准版 64 位中文版为例。
2. 在腾讯云 Windows 云服务器中下载并安装 [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)。更多有关 SQL Server Management Studio 的文档请参见微软官方文档 [使用 SQL Server Management Studio](https://docs.microsoft.com/zh-cn/sql/database-engine/use-sql-server-management-studio?view=sql-server-2014)。
3. 在云数据库 SQL Server 实例详情页，单击【实例详情】，查看云数据库 SQL Server 实例的内网 IP 及端口号。**该内网 IP 及端口号会在连接云数据库时使用。**
![](https://main.qcloudimg.com/raw/05866d097de8b621b3a27b230ed6de8c.png)
4. 在 Windows 云服务器上启动 SQL Server Management Studio。在【Connect to server】界面，填写相关信息连接云数据库。单击【Connect】，稍等几分钟后，SQL Server Management Studio 将连接到您的数据库实例。
![](//mc.qcloudimg.com/static/img/1cac47c4fc515d30d2cb5a0ef0141e22/image.png)
 - Server type：选择 Database Engine。
 - Server name：键入或黏贴数据库实例的内网 IP 和端口号，注意要用 **逗号** 隔开。例如在上一步中查看得到的内网 IP 和端口号为：`10.10.10.10：1433`，那么在此填入：`10.10.10.10，1433`。注意使用 **英文标点符号**。
 -  Authentication：选择 SQL Server Authentication。
 -  Login 和 Password：在创建实例的创建帐号时，填写的帐号名和密码。本教程以“test”为例。
5. 连接到数据库后，可以查看到 SQL Server 的标准内置系统数据库（master、model、msdb 和 tempdb）。
![](//mc.qcloudimg.com/static/img/a39d9db6f6a4050d1fa4285a53b55157/image.png)
6. 现在您可以开始创建您自己的数据库并对数据库运行查询。选择【File】>【New】>【Query with Current Connection】，键入以下 SQL 查询：
```
select @@VERSION
```
运行查询，SQL Server Management Studio 会返回 SQL Server 版的腾讯云云数据库实例。
![](//mc.qcloudimg.com/static/img/fbf64c03c7addda9c80fdd3dac7bbebb/image.png)

## 删除云数据库 SQL Server 实例
1. 在云数据库 SQL Server 实例详情页，选择【帐号管理】>【删除帐号】。删除帐号需要一定的时间，请耐心等待。
![](//mc.qcloudimg.com/static/img/7ce670ca67766ed32d088b4f733c56b6/image.png)
2. 在实例详情页，选择【数据库管理】>【删除】。删除数据库需要一定的时间，请耐心等待。
![](//mc.qcloudimg.com/static/img/fa68b790fe7a12e1c17bfde648ac6e98/image.png)
3. 云数据库 SQL Server 云数据库实例暂时不支持手动删除，到期后没有续费将会自动停止。

