## 操作场景
本文介绍在 Windows 云服务器中通过 SQL Server Management Studio（SSMS）连接到 SQL Server 实例，并运行简单查询的操作。
>?云服务器和云数据库须是同一账号，且同一个 VPC 内（保障同一个地域）。

## 操作步骤
1. 登录 [云数据库 SQL Server](https://console.cloud.tencent.com/sqlserver) 实例详情页，查看实例内网 IP 及端口号。该内网 IP 及端口号会在连接云数据库时使用。
2. 登录腾讯云 Windows 云服务器，请参见 [快速入门 Windows 云服务器](https://cloud.tencent.com/document/product/213/2764)。本文以 Windows Server 2012 R2 标准版64位中文版为例。
3. 在 Windows 云服务器中下载并安装 [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)。SQL Server Management Studio 相关介绍请参见 [使用 SQL Server Management Studio](https://docs.microsoft.com/zh-cn/sql/database-engine/use-sql-server-management-studio?view=sql-server-2014)。
![](https://main.qcloudimg.com/raw/4fc43ce3788401857536c6ddb442ced0.png)
4. Windows 云服务器上启动 SQL Server Management Studio。在【Connect to server】页面，填写相关信息连接云数据库。单击【Connect】，稍等几分钟后，SQL Server Management Studio 将连接到您的数据库实例。
 - **Server type**：选择 Database Engine。
 - **Server name**：数据库实例的内网 IP 和端口号，需用英文逗号隔开。例如，内网 IP 和端口号为`10.10.10.10:1433`，则在此填入`10.10.10.10,1433`。注意使用英文标点符号。
 -  **Authentication**：选择 SQL Server Authentication。
 -  **Login 和 Password**：在实例【帐号管理】页创建帐号时，填写的帐号名和密码。
![](//mc.qcloudimg.com/static/img/1cac47c4fc515d30d2cb5a0ef0141e22/image.png)
5. 连接到数据库后，可以查看到 SQL Server 的标准内置系统数据库（master、model、msdb 和 tempdb）。
![](https://main.qcloudimg.com/raw/a25241cf8000e10bcf748abe99773a77.png)
6. 您可以开始创建自己的数据库并对数据库运行查询。选择【File】>【New】>【Query with Current Connection】，键入以下 SQL 查询：
```
select @@VERSION
```
运行查询，SQL Server Management Studio 会返回 SQL Server 版的腾讯云云数据库实例。
![](//mc.qcloudimg.com/static/img/fbf64c03c7addda9c80fdd3dac7bbebb/image.png)


