## 连接方式
连接云原生数据库 TDSQL-C 的方式如下：
- **内网地址连接**：通过内网地址连接云原生数据库 TDSQL-C，使用云服务器 CVM 直接连接云数据库的内网地址，这种连接方式使用内网高速网络，延迟低。
 - 云服务器和数据库须是同一账号，且同一个[ VPC](https://cloud.tencent.com/document/product/215/20046) 内（保障同一个地域）。
 - 内网地址系统默认提供，可在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 的集群列表或集群详情页查看。
>?对于不同的 VPC 下（包括同账号/不同账号，同地域/不同地域）的云服务器和数据库，内网连接方式请参见 [云联网](https://cloud.tencent.com/document/product/877)。
>
- **外网地址连接**：通过外网地址连接云原生数据库 TDSQL-C。外网地址需 [手动开启](#waiwang)，可在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 的实例详情页查看，不需要时也可关闭。
 - 开启外网地址，会使您的数据库服务暴露在公网上，可能导致数据库被入侵或攻击。建议您使用内网连接数据库。 
 - 云数据库外网访问适用于开发或辅助管理数据库，不建议正式业务访问使用，因为可能存在不可控因素会导致外网访问不可用（例如 DDOS 攻击、突发大流量访问等）。
- **通过 DMC 连接**：通过数据管理平台（Database Management Console，DMC）访问云原生数据库 TDSQL-C。


## 内外网连接 TDSQL-C for MySQL
### 从 Windows 云服务器连接
1. 登录到 Windows 云服务器，请参见 [快速配置 Windows 云服务器](https://cloud.tencent.com/document/product/213/2764)。
2. 下载一个标准的 SQL 客户端。
>?推荐您下载 MySQL Workbench，并根据您的系统来下载适配版本的安装程序，下载地址请参见 https://dev.mysql.com/downloads/workbench/。
>
![](https://main.qcloudimg.com/raw/851ab46468c554097a0cf742017157b7.png)
3. 界面将提示**Login**、**Sign Up** 和 **No, thanks, just start my download.**， 选择 **No thanks, just start my download.** 来快速下载。
![](https://main.qcloudimg.com/raw/47b195fb37ff584f21038ee54342d362.png)
4. 在此台云服务器上安装 MySQL Workbench。
>?
>- 此电脑上需要安装 Microsoft .NET Framework 4.5 和 Visual C++ Redistributable for Visual Studio 2015。
>- 您可以单击 MySQL Workbench 安装向导中的 **Download Prerequisites**，跳转至对应页面下载并安装这两个软件，然后安装 MySQL Workbench。
>
![](https://main.qcloudimg.com/raw/1af292f989f03f3e02e1200b77cb70c1.png)
5. 打开 MySQL Workbench，选择 **Database** > **Connect to Database**，输入 MySQL 数据库实例的内网（或外网）地址和用户名、密码，单击 **OK** 进行登录。
 - Hostname：输入内网（或外网）地址。在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 的集群详情页可查看到目标数据库的内网（或外网）地址。若为外网地址，请确认是否已开启，请参见 [开启外网地址](#waiwang)。
 - Port：内网（或外网）对应端口。
 - Username：默认为 root。
 - Password：Username 对应的密码。如忘记密码可在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 进行修改。
![](https://main.qcloudimg.com/raw/9c9e5dcc8a2bb9fa15fa4d98a18308f1.png)
6. 登录成功的页面如图 所示，在此页面上您可以看到数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](https://main.qcloudimg.com/raw/33f081e99c384258bbc5ed3683ed4d7d.png)

### 从 Linux 云服务器连接
1. 登录到 Linux 云服务器，请参见 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 以 CentOS 7.2 64 位系统的云服务器为例，执行如下命令安装 MySQL 客户端：
```
yum install mysql
```
提示`Complete!`说明 MySQL 客户端安装完成。
![](https://main.qcloudimg.com/raw/16c77e28c40ae9be9a182b1c61843ecd.png)
3. 根据不同连接方式，选择相应的操作：
 - **内网连接时：**
    1. 执行如下命令，登录到 TDSQL-C 集群。
```
mysql -h hostname -u username -p
```
      - hostname：替换为目标 TDSQL-C 集群的内网地址，在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 的集群详情页可查看内网地址。
		- username：替换为默认的用户名 root。
    2. 在提示`Enter password：`后输入 TDSQL-C 集群的 root 帐号对应的密码，如忘记密码可在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 进行修改。
    本例中提示`MySQL [(none)]>`说明成功登录到 TDSQL-C。![](https://main.qcloudimg.com/raw/83b8a95cf4b99919b5899510691289b4.png)
   - **外网连接时：**
    1. 执行如下命令，登录到 TDSQL-C 集群。
```
mysql -h hostname -P port -u username -p
```
      - hostname：替换为目标 TDSQL-C 集群的外网地址，在  [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 的集群详情页可查看外网地址和端口号。若外网地址未开启，请参见 [开启外网地址](#waiwang) 开启。
      - port：替换为外网端口号。
      - username：替换为外网连接用户名，用于外网连接，建议您在控制台单独创建帐号便于连接控制管理。
    2. 在提示`Enter password：`后输入外网连接用户名对应的密码，如忘记密码可在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 进行修改。
    本例中 hostname 为 59281c4exxx.myqcloud.com，外网端口号为15311。
![](https://main.qcloudimg.com/raw/16839344da3a588be93d814de224277a.png)
4. 在`MySQL \[(none)]>`提示符下可以发送 SQL 语句到要执行的 TDSQL-C 服务器，具体命令行请参见 [mysql Client Commands](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
下图中以`show databases;`为例：
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

## 内外网连接 TDSQL-C for PostgreSQL
### 从 Windows 云服务器连接
1. 登录到 Windows 云服务器，请参见 [快速配置 Windows 云服务器](https://cloud.tencent.com/document/product/213/2764)。
2. 下载一个标准的 SQL 客户端。
>?推荐您下载 pgadmin 4，并根据您的系统来下载适配版本的安装程序，下载地址请参见 https://www.pgadmin.org/download/pgadmin-4-windows/
>
3. 单击想要下载的 pgadmin 4 版本号与下载链接进行快速下载。
4. 打开 PgAdmin 4，右键选择 **Server** > **Create** > **Server**，在弹出的连接配置对话框中，配置相应的连接信息。
 - Hostname/address：输入内网（或外网）地址。在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 的集群详情页可查看到目标数据库的内网（或外网）地址。若为外网地址，请确认是否已开启，请参见 [开启外网地址](#waiwang)。
 - Port：内网（或外网）对应端口。
 - Maintenance database：访问的默认数据库，可直接配置为 postgres。
 - Username：配置创建数据库实例时设置的用户名。
 - Password：Username 对应的密码。如忘记密码可在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 进行修改。
6. 登录成功的页面如图 所示，在此页面上您可以看到数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](https://main.qcloudimg.com/raw/056dff12c85d3560eb37ed8bfb4edbe7.png)

### 从 Linux 云服务器连接
1. 登录到 Linux 云服务器，请参见 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 以 CentOS 7.2 64 位系统的云服务器为例，进入到社区的 [下载网址](https://www.postgresql.org/download/linux/redhat/)，选择想要安装的数据库版本以及操作系统版本。执行如下命令安装 PostgreSQL 客户端，如下图所示。
![](https://main.qcloudimg.com/raw/74737da91235b20ca63ee61661d4ceeb.png)
```
yum install postgresql13
```
提示 `Complete!` 说明 PostgreSQL 客户端安装完成。
3. 执行如下命令，登录到 TDSQL-C 集群。
```
psql -h hostname -U username -p 5432 -d postgres
```
  - hostname：替换为目标 TDSQL-C PostgreSQL版集群的内网地址，在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 的集群详情页可查看内网地址。如使用外网，则为外网域名。
  - username：替换为默认的用户名 root。
  - port： 默认为5432
4. 在提示 `Enter password：` 后输入 TDSQL-C for PostgreSQL 集群的帐号对应的密码，如忘记密码可在 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb) 进行修改。
本例中提示 `postgres #>` 说明成功登录到 TDSQL-C for PostgreSQL。


## 通过 DMC 平台连接
1. 登录 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb)，在集群列表，单击**操作**列的**登录**。
2. 在数据管理控制台的登录界面，帐号输入 root，密码为之前在创建集群时配置的 root 帐户的密码，单击**登录**。
>?DMC 平台可便捷地访问实例、操作库表级、管理实例会话、实时监控、InnoDB 锁等待、SQL 窗口等。
>
![](https://main.qcloudimg.com/raw/d07b1477bd524f23fbaa9450c352c49f.png)

## [附录1：开启外网连接地址](id:waiwang)
>?使用外网连接时，需要先开启数据库的外网地址。
>
1. 登录 [TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb)，在集群列表，单击集群 ID，进入集群详情页面。
2. 在集群详情页的连接外网地址处，单击**开启**。
![](https://main.qcloudimg.com/raw/09b186229ae121fe32c53317727ef8b8.png)
3. 在弹出的对话框，单击**确定**。
>?
>- 开启成功后，即可在连接信息中查看外网地址。
>- 通过开关可以关闭外网访问权限，重新开启外网，域名对应的外网 IP 不变。
