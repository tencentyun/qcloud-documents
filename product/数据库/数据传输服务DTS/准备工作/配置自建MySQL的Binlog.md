## 操作场景
当数据迁移、数据同步、数据订阅任务的源库为自建 MySQL/TDSQL MySQL/TDSQL-C MySQL 时，需要用户在自建数据库上设置 Binlog，以满足校验项阶段对源库的要求。

## 操作影响
本操作需要重启数据库，会对业务造成一定影响，建议在业务低峰阶段操作。 

## 操作步骤
1. 登录源数据库。
2. 参考如下内容修改配置文件 `my.cnf`。 
> ?
> - `my.cnf` 配置文件的默认路径为 `/etc/my.cnf`，现场以实际情况为准。 
> - 建议源端 Binlog 日志至少保留3天及以上，否则可能会因任务暂停/中断时间大于 Binlog 日志保留时间，造成任务无法续传，进而导致任务失败。
>    - 在 `my.cnf` 配置文件中修改会永久生效，如果用户仅想临时生效，请执行 `set global expire_logs_days=3` 命令修改。
>    - MySQL 8.0版本及以上也可以使 `binlog_expire_logs_seconds` 来修改 Binlog 保留时间，该参数精确到秒级。
>
```
log_bin = MYSQL_BIN
binlog_format = ROW
server_id = 2 //建议设为大于1的整数，此处仅为示例。
binlog_row_image = FULL
expire_logs_days=3  //修改 binlog 的保留时间，建议大于等于3天
```
3. 重启 MySQL 进程。 
```
[\$Mysql_Dir]/bin/mysqladmin -u root -p shutdown
[\$Mysql_Dir]/bin/safe_mysqld &
```
> ?[$Mysql_Dir] 指源数据库的安装路径，请替换为实际的源数据库安装目录。 

