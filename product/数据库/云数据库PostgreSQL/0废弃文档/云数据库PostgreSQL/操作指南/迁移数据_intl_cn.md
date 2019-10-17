# 使用腾讯云DTS服务
PostgreSQL 数据库可使用腾讯云【数据传输服务DTS】的【数据迁移】功能做数据导入

详细操作参考 [数据迁移服务](https://intl.cloud.tencent.com/document/product/571)

# 使用psql命令
如果你的数据已经在PostgreSQL上，你可以psql命令将数据轻松的迁移到CDB for PostgreSQL中。
迁移数据的工作主要分为两大部分：
> （1）使用pg_dump命令进行逻辑备份，创建转储数据；
> （2）将上一步的备份数据恢复到CDB for PostgreSQL上。
准备操作：你应该已经完成PostgreSQL实例的准备，如未完成，请参见申请实例和连接实例的操作指引。

## 第一步
使用PostgreSQL客户端连接本地数据库，执行如下命令，备份数据。

```
pg_dump -U username -h hostname -p port -d databasename -f filename
```

参数说明如下


| 参数 | 意义 |
|---------|---------|---------|
| username | 本地数据库用户名|
| hostname | 本地数据库主机名，如果是在本地数据库主机登录，可以使用 localhost |
| port | 本地数据库端口号 |
| databasename | 要备份的本地数据库名 |
| filename | 要生成的备份文件名称，如mydump.sql |


## 第二步
准备操作：请先将备份好的数据上传到同一内网的云服务器主机上，然后通过内网进行数据恢复，以保证网络的稳定和数据的安全。
在您登录云服务器后，在PostgreSQL客户端中，执行如下命令，恢复数据。

```
psql -U username -h hostname -d desintationdb -p port -f dumpfilename
```
参数说明如下


| 参数 | 意义 |
|---------|---------|---------|
| username | CDB for PostgreSQL 的数据库用户名|
| hostname |CDB for PostgreSQL 的数据库地址 |
| desintationdb | CDB for PostgreSQL 的数据库名 |
| port | CDB for PostgreSQL 的数据库端口号 |
|dumpfilename | 备份数据文件名，如mydump.sql |

