
在本文档中，您可以创建 SQL Server 云数据库实例。然后在 Windows 云服务器中通过 SQL Server Management Studio（SSMS）连接到该数据库实例并运行简单的查询。最后，您将删除该数据库实例。
如果您想要在本地使用 SQL Server Management Studio（SSMS） 连接到 SQL Server 云数据库，请参考入门教程 [创建并连接 SQL Server 云数据库（本地端）]()。

> **注意：**
> 在创建 SQL Server 云数据库实例之前，您必须拥有一个腾讯云账户。如果您没有腾讯云账户，请在 [注册页面](https://cloud.tencent.com/register) 填写相关信息注册腾讯云账户。

## 一、创建 SQL Server 云数据库实例
在此步骤中，您会使用腾讯云 [控制台](https://console.cloud.tencent.com/) 创建数据库实例。
1. 登录腾讯云云数据库 [控制台](https://console.cloud.tencent.com/cdb)。
![](//mc.qcloudimg.com/static/img/7f454c8f988ec22c4045b33c47571024/image.png)
2. 在右侧导航栏选择需要创建的云数据库类型，这里选择【SQL Server】。单击【新建】，进入云数据库 SQL Server 购买界面。
![](//mc.qcloudimg.com/static/img/798911fbe873e0a59de7d749b365c0ca/image.png)
3. 在云数据库 SQL Server 购买界面中，选择配置属性。确认无误后，单击【立即购买】。
![](//mc.qcloudimg.com/static/img/1630495ca9ca9001b4cdef32e1b85364/image.png)
 - 计费模式。目前只支持包年包月。
 - 地域和可用区。地域说明请参见 [地域与可用区](/doc/product/236/8458)。
 - 网络环境。支持基础网络和私有网络。基础网络和私有网络的区别请参见 [网络环境](/doc/product/213/5227)。
 - 数据库版本。提供 SQL Server 2008 R2 和 SQL Server 2012 两个版本。不同可用区可能有所不同，具体以实际情况为准。
 - 实例规格和所需的硬盘。
 - 购买数量和购买时长。
4. 再次进入腾讯云云数据库 [控制台](https://console.cloud.tencent.com/cdb)，选择【SOL Server】，查看刚才创建的云数据库实例。当运行状态显示 **运行中**，表示云数据库 SQL Server 创建成功。
![](//mc.qcloudimg.com/static/img/eedd98d6992bdb6e06d25d8380365e89/image.png)
5. 在 SQL Server 云数据库管理界面，单击【管理】，进入 SQL Server 云数据库实例详情页。
![](//mc.qcloudimg.com/static/img/aeb4d8c1b053c4ea9dbb6f5a9a48fc4d/image.png)
6. 在 SQL Server 云数据库实例详情页，单击【账号管理】>【创建账号】，弹出创建账号页面。填写相关信息创建账号，确认无误后，单击【确定】。此步骤填写的 **账号名** 和 **密码** 将在连接 SQL Server 云数据库时使用，请妥善保管。
![](//mc.qcloudimg.com/static/img/1cac253d8eb9029bbaf10aa385b4c0bd/image.png)
7. 在 SQL Server 云数据库实例详情页，单击【数据库管理】>【创建数据库】，弹出创建数据库页面。填写相关信息创建数据库，确认无误后，单击【确定】。这里需要将数据库的 **读写权限** 或者 **只读权限** 授权给第 6 步中创建的账号。
![](//mc.qcloudimg.com/static/img/8db9f2aaa65978c0e0005739c7861aad/image.png)

## 二、连接 SQL Server 云数据库实例（Windows 云服务器）
1. 登陆腾讯云 Windows 云服务器。如果您还没有腾讯云 Windows 云服务器，请参考 [快速入门 Windows 云服务器](/doc/product/213/2764)。这里以 Windows Server 2012 R2 标准版 64 位中文版为例。
2. 在腾讯云 Windows 云服务器中下载并安装 [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)。更多有关 SQL Server Management Studio 的文档请参考微软官方文档 [使用 SQL Server Management Studio][1]。
3. 在 SQL Server 云数据库实例详情页，单击【实例详情】，查看 SQL Server 云数据库实例的内网 IP 及端口号。该内网 IP 及端口号会在连接云数据库时使用。
![](//mc.qcloudimg.com/static/img/6dcf51fc839f1ea7c47c26609b711ede/image.png)
4. 在 Windows 云服务器上启动 SQL Server Management Studio。在 **Connect to server** 界面，填写相关信息连接云数据库。单击【Connect】，稍等几分钟后，SSMS 将连接到您的数据库实例。
![](//mc.qcloudimg.com/static/img/1cac47c4fc515d30d2cb5a0ef0141e22/image.png)
 - Server type。选择 Database Engine。
 - Server name。键入或黏贴数据库实例的内网 IP 和端口号，注意要用 **逗号** 隔开。例如在第 3 步中查看得到的内网 IP 和端口号为：`10.10.10.10：1433`，那么在此填入：`10.10.10.10，1433`。注意使用 **英文标点符号**。
 -  Authentication。选择 SQL Server Authentication。
 -  Login 和 Password。第一章第 6 步中创建账号时填写的账号名和密码。
5. 连接到数据库后，可以查看到 SQL Server 的标准内置系统数据库（master、model、msdb 和 tempdb）。
![](//mc.qcloudimg.com/static/img/a39d9db6f6a4050d1fa4285a53b55157/image.png)
6. 现在您可以开始创建您自己的数据库并对数据库运行查询。单击【File】>【New】>【Query with Current Connection】，键入以下 SQL 查询：
```
select @@VERSION
```
运行查询。SSMS 会返回 SQL Server 版的腾讯云云数据库实例。
![](//mc.qcloudimg.com/static/img/fbf64c03c7addda9c80fdd3dac7bbebb/image.png)

## 三、删除 SQL Server 云数据库实例
1. 在 SQL Server 云数据库实例详情页，单击【账号管理】>【删除账号】。删除账号需要一定的时间，请耐心等待。
![](//mc.qcloudimg.com/static/img/7ce670ca67766ed32d088b4f733c56b6/image.png)
2. 在 SQL Server 云数据库实例详情页，单击【数据库管理】>【删除】。删除数据库需要一定的时间，请耐心等待。
![](//mc.qcloudimg.com/static/img/fa68b790fe7a12e1c17bfde648ac6e98/image.png)
3. SQL Server 云数据库实例不需要手动删除，到期后没有续费将会自动停止。

[1]:https://msdn.microsoft.com/zh-cn/library/ms174173(v=sql.105).aspx
