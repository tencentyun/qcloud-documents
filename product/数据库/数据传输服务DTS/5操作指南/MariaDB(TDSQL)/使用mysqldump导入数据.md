使用 mysqldump 工具的优点是简单易用、容易上手，缺点是停机时间较长，因此它适用于数据量不大，或者允许停机的时间较长的情况。

### 使用 mysqldump 的数据导出工具，将本地数据库数据导出为数据文件。

> 说明： 导出期间请勿进行数据更新。本步骤仅仅导出数据，不包括存储过程、触发器及函数。

```
mysqldump -h localIp -u userName -p --opt --default-character-set=utf8 --hex-blob dbName --skip-triggers > /tmp/dbName.sql

```
参数说明：

localIp：本地数据库服务器 IP 地址
userName：本地数据库的迁移账号
dbName：需要迁移的数据库名
/tmp/dbName.sql：备份生成的文件名

### 使用 mysqldump 导出存储过程、触发器和函数。

> 说明： 若数据库中没有使用存储过程、触发器和函数，可跳过此步骤。在导出存储过程、触发器和函数时，需要将 definer 去掉，以兼容云数据库。

```
mysqldump -h localIp -u userName -p --opt --default-character-set=utf8 --hex-blob dbName -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/triggerProcedure.sql

```
参数说明：
localIp：本地数据库服务器 IP 地址
userName：本地数据库的迁移账号
dbName：需要迁移的数据库名
/tmp/triggerProcedure.sql：备份生成的文件名


### 将数据文件和存储过程文件上传到 云服务器 CVM 上。
> 请确保 CVM 和云数据库 TencentDB 能正常连通，且 CVM 存储空间足够。

### 登录 CVM，将数据文件和存储过程文件导入到目标云数据库中。

> 请确保您拥有相应权限的数据库帐号，否则可能需要前往控制台生成帐号

```
mysql -h xxx.xxx.xxx.xxx:xxxx –u userName -p dbName < /tmp/dbName.sql
mysql -h xxx.xxx.xxx.xxx:xxxx -u userName -p dbName < /tmp/triggerProcedure.sql

```
参数说明：
xxx.xxx.xxx.xxx:xxxx  实例连接地址，本例以内网地址为例<br>
userName：RDS 数据库的迁移账号
dbName：需要导入的数据库名
/tmp/dbName.sql：要导入的数据文件名
/tmp/triggerProcedure.sql：要导入的存储过程文件名

