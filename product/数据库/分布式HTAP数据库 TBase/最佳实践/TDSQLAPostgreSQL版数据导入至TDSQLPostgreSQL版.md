您可以选择通过 pg_dump 工具将 TDSQL -A PostgreSQL版 实例数据导入到 TDSQL PostgreSQL版 实例中。

### 步骤1：准备 TDSQL PostgreSQL版 实例
[购买 TDSQL PostgreSQL版 实例](https://console.cloud.tencent.com/tdsqld/instance-tdpg/buy)，并在 [控制台](https://console.cloud.tencent.com/tdsqld/instance-tdpg) 获取连接地址。

>?请确保字符集与源实例一致。

### 步骤2：逻辑备份源实例数据
1. 登录云服务器 CVM，通过 PostgreSQL 客户端，连接源 TDSQL-A PostgreSQL版。
2. 执行如下命令，备份数据。
```
pg_dump -U username -h hostname -p port -x databasename -f filename
```
参数说明如下：
 - username：源数据库用户名。
 - hostname：源数据库 IP 地址。
 - port：源数据库端口号。
 - databasename：要导出的数据库名。
 - filename：要生成的备份文件名称。
 - -x：代表导出不带源对象的权限信息。建议在目标库根据实际情况再进行权限赋予，否则在导入时容易报错。
例如，数据库用户 pgtest 要备份本地 PostgreSQL 数据库，登录源 PostgreSQL 后，通过如下命令备份数据。
```
pg_dump -U pgtest -h 9.xxx.xxx.xxx -p 4321 pg001 -f pg001.sql
```

### 步骤3：恢复数据至目标实例
1. 登录有导出文件的云服务器 CVM。
2. 通过 PostgreSQL 客户端，执行如下命令将数据导入至目标 TDSQL PostgreSQL版。
```
psql -U username -h hostname -d databasename -p port -f filename
```
参数说明如下：
 - username：TDSQL PostgreSQL版 数据库用户名。
 - hostname：TDSQL PostgreSQL版 数据库 IP 地址。
 - port：TDSQL PostgreSQL版 数据库端口号。
 - databasename：TDSQL PostgreSQL版 数据库名。
 - filename：本地备份数据文件名。
例如，
```
psql -U pgtest -h 10.xxx.xxx.xxx -d pg001 -p 4321 -f pg001.sql
```
由于源端和目标数据库的权限设置可能不一致，在数据导入过程当中可能会出现一些与权限相关的 WARNING 或 ERROR，可以忽略。
