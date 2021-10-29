
## 操作场景
本文介绍借助具有外网 IP 的 Linux 云服务器进行端口映射，并通过 SQL Server Management Studio（SSMS）连接到实例运行简单查询的操作。
>?云服务器和云数据库须是同一账号，且同一个 VPC 内（保障同一个地域，不限可用区）。

## 操作步骤
考虑到数据的安全，云数据库 SQL Server 尚未开放实例外网 IP，如有需求可以利用 SSH2 的端口映射在外网连接实例，并对其进行配置和管理。
1. 登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver)，在实例详情页查看实例内网 IP 及端口号。该内网 IP 及端口号会在配置端口映射时使用。
![](https://main.qcloudimg.com/raw/5482cc658c605ea56a5502097b862e92.png)
2. 准备一台具有外网 IP的 Linux 云服务器，请参见 [快速入门 Linux 云服务器](/doc/product/213/2936)。
3. 在本地使用 SSH 工具（如 SecureCRT 或 PuTTY 等，本文以 SecureCRT 为例）登录 Linux 云服务器，请参见 [登录 Linux 实例](/doc/product/213/5436)。
4. 在 SecureCRT 菜单栏选择 **Options** > **Session Options**，进入会话属性设置。
![](https://main.qcloudimg.com/raw/acbb1ad0a808ac59a0053063b75aab8b.png)
5. 在会话属性设置页，选择 **Connection** > **Port Forwarding** > **Add**，进入配置端口映射页。
![](https://main.qcloudimg.com/raw/05f0cadcda75c6f931f34eb296a5ab6f.png)
6. 在配置端口映射页，配置相应参数。
![](https://main.qcloudimg.com/raw/0ac1295fb04aebff56050b3bc6b32f6e.png)
7. 在本地下载并安装 [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)。SQL Server Management Studio 相关介绍请参见 [使用 SQL Server Management Studio](https://docs.microsoft.com/zh-cn/sql/ssms/sql-server-management-studio-ssms?view=sql-server-ver15)。
8. 本地启动 SQL Server Management Studio。在 **Connect to server**  页面，填写相关信息连接云数据库。单击 **Connect**，稍等几分钟后，SQL Server Management Studio 将连接到您的数据库实例。
 - **Server type**：选择 Database Engine。
 - **Server name**：本机 IP 地址和端口号，需用英文逗号隔开，例如`10.0.0.1,4000`。端口号需与第6步中配置的端口保持一致。
 -  **Authentication**：选择 SQL Server Authentication。
 -  **Login 和 Password**：在实例**帐号管理**页创建帐号时，填写的帐号名和密码。
![](https://main.qcloudimg.com/raw/14d90aa2eda6c841680f0fdc74db8219.png)
9. 连接到数据库后，可以查看到 SQL Server 的标准内置系统数据库（master、model、msdb 和 tempdb）。
![](https://main.qcloudimg.com/raw/c65c02197b506bd5b326128f1a3983a0.png)
10. 现在您可以开始创建自己的数据库并对数据库运行查询。选择 **File** > **New** > **Query with Current Connection**，键入以下 SQL 查询：
```
select @@VERSION
```
运行查询，SQL Server Management Studio 会返回 SQL Server 版的腾讯云云数据库实例。
![](//mc.qcloudimg.com/static/img/fbf64c03c7addda9c80fdd3dac7bbebb/image.png)

