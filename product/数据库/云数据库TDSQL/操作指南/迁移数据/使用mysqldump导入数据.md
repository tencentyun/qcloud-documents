使用 mysqldump 工具导入数据简单易上手，但停机时间较长，适用于数据量不大，或允许停机时间较长的场景。

1. 使用 mysqldump 数据导出工具，将本地数据库数据导出为数据文件。
>?导出期间请勿进行数据更新。本步骤仅导出数据，不包括存储过程、触发器和函数。
>
```
mysqldump -h localIp -u userName -p --opt --default-character-set=utf8 --hex-blob dbName --skip-triggers > /tmp/dbName.sql
```
参数说明：
 - localIp：本地数据库服务器 IP 地址。
 - userName：本地数据库的迁移帐号。
 - dbName：需要迁移的数据库名。
 - /tmp/dbName.sql：备份生成的文件名。
2. 使用 mysqldump 导出存储过程、触发器和函数。
>?若数据库中没有使用存储过程、触发器和函数，可跳过此步骤。导出存储过程、触发器和函数时，需要将 definer 去掉，以兼容云数据库。
>
```
mysqldump -h localIp -u userName -p --opt --default-character-set=utf8 --hex-blob dbName -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/triggerProcedure.sql
```
参数说明：
 - localIp：本地数据库服务器 IP 地址。
 - userName：本地数据库的迁移帐号。
 - dbName：需要迁移的数据库名。
 - /tmp/triggerProcedure.sql：备份生成的文件名。
3. 将数据文件和存储过程文件上传至云服务器 CVM。请确保 CVM 和云数据库能正常连通，且 CVM 存储空间足够。
4. 登录 CVM，将数据文件和存储过程文件导入至目标云数据库。请确保您拥有相应权限的数据库帐号，否则需至控制台生成帐号。
```
mysql -h xxx.xxx.xxx.xxx:xxxx –u userName -p dbName < /tmp/dbName.sql
mysql -h xxx.xxx.xxx.xxx:xxxx -u userName -p dbName < /tmp/triggerProcedure.sql
```
参数说明：
 - xxx.xxx.xxx.xxx:xxxx：实例连接地址，本文以内网地址为例。
 - userName：云数据库的迁移帐号。
 - dbName：需要导入的数据库名。
 - /tmp/dbName.sql：需要导入的数据文件名。
 - /tmp/triggerProcedure.sql：需要导入的存储过程文件名。
