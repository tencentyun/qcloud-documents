
使用 ODBC 连接 TDSQL-A PostgreSQL版 进行数据库操作需要提前部署 ODBC 的驱动包，驱动包可前往 [官网](https://odbc.postgresql.org/) 获取，或者向软件提供商获取。

## Linux 下进行 ODBC 开发
Linux 环境下，开发应用程序要用到 unixODBC 提供的头文件（sql.h、sqlext.h 等）和库 libodbc.so。这些头文件和库可从 ODBC 的安装包中获得。

Linux 部署 ODBC：
可使用 yum 命令直接进行 ODBC 和 unixODBC 的部署。
```
yum install -y unixODBC
yum install -y postgresql-odbc
```
部署完成后执行 isql 表明 ODBC 部署完成。
![](https://main.qcloudimg.com/raw/c0298cbf0e7988583dc6ccaccf16b6ac.png)

Linux ODBC 配置：
1. 创建 /etc/odbc.ini 文件，修改其中的 Servername、UserName、Password、Port 等参数。
```
vi /etc/odbc.ini 
[tdapg]
Description = Test to tdapg
Driver = PostgreSQL
Database = postgres
Servername = localhost
UserName = dbadmin
Password = tdapg@tdapg
Port = 11345
ReadOnly = 0
ConnSettings = set client_encoding to UTF8
```
完成后保存退出。
2. 执行 `isql -v tdapg(数据源名称)` 命令。
如果显示如下信息，表明配置正确，连接成功。
```
+---------------------------------------+
| Connected!              |
|                   |
| sql-statement              |
| help [tablename]            |
| quit                  |
|                   |
+---------------------------------------+
SQL>
```
若显示 ERROR 信息，则表明配置错误，请检查上述配置是否正确。

## Windows 下进行 ODBC 开发
Windows 环境下，开发应用程序用到的相关头文件和库文件都由系统自带。
Windows 配置数据源：
1. 解压 psqlodbc_13_00_0000-x64 .zip 获取 psqlodbc_x64.msi 驱动直接进行部署。
2. 打开驱动管理器，使用快捷键 Win+R 直接运行 odbcad32。
![](https://main.qcloudimg.com/raw/225c100597f30cef8af2cbc7ed81c8ac.png)
3. 配置数据源，在打开的驱动管理器上，选择【用户 DSN】>【添加】 > 【PostgreSQL Unicode】，然后进行配置。
![](https://main.qcloudimg.com/raw/03fee0de11884517bca025f654727b5a.png)
4. 单击【Test】进行连接测试，测试成功后单击【Save】保存连接信息，完成数据源的配置，即可进行后续开发。
![](https://main.qcloudimg.com/raw/22d3aa82b7591b0bbe70acd26495b595.png)
