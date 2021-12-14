
## 操作场景
使用新版 DTS 进行 MySQL 数据迁移时，新版本 DTS 数据迁移更专注数据内容本身，迁移对象为基础表和视图，对用户权限信息不做迁移，所以本文为您提供用户权限迁移的操作指导。 

本场景通过 pt-show-grants 来实现用户权限从源库导出，然后在目标库导入。

## 准备工作
- 安装 [pt-show-grants](https://www.percona.com/doc/percona-toolkit/LATEST/pt-show-grants.html) 并了解相关基本操作。本文档后续以3.2.0版本作为示例。
- 在源库中授权迁移使用帐号，如下以 `dts` 用户为例。
```
CREATE USER 'dts'@'%' IDENTIFIED BY '迁移密码'; 
GRANT SELECT ON `mysql`.* TO 'dts'@'%';
```
- 在目标库中授权迁移使用帐号，如下以 `dts` 用户为例。 
```
CREATE USER 'dts'@'%' IDENTIFIED BY '迁移密码';
GRANT SELECT,CREATE USER,LOCK TABLES,SHOW VIEW,TRIGGER,ALTER,ALTER ROUTINE,CREATE,CREATE ROUTINE,CREATE TABLESPACE,CREATE TEMPORARY TABLES,CREATE VIEW,DELETE,DROP,EVENT,EXECUTE, INDEX,INSERT,PROCESS,REFERENCES,RELOAD,UPDATE,SHOW DATABASES on *.* to 'dts'@'%';
FLUSH PRIVILEGES;
```
- 迁移过程中，建议目标库不要有除迁移以外的其他会话写入，如果需要访问目标库，建议用户创建一个只读权限的帐号访问目标库，这样可以规避双写的风险（双写可能引起数据冲突，导致任务失败）。如下以 `read_only` 用户为例。
```
CREATE USER 'read_only'@'%' IDENTIFIED BY '迁移密码';
GRANT SELECT, SHOW DATABASES, SHOW VIEW on *.* to 'read_only'@'%';
FLUSH PRIVILEGES;
```

## 注意事项
- 目标库为腾讯云 MySQL 数据库时，仅支持如下普通权限的导入，不支持高权限的导入。该限制主要是为了避免高权限用户可能的误操作给业务带来风险。
SELECT, CREATE USER, LOCK TABLES, SHOW VIEW, TRIGGER, ALTER, ALTER ROUTINE, CREATE,CREATE ROUTINE, CREATE TABLESPACE, CREATE TEMPORARY TABLES, CREATE VIEW,DELETE,DROP,EVENT,EXECUTE, INDEX, INSERT, PROCESS, REFERENCES, RELOAD, UPDATE, SHOW DATABASES, REPLICATION CLIENT, REPLICATION SLAVE 权限的账号。
- pt-show-grants 以源库版本 MySQL 5.7.6 作为界限会生成不同的 SQL 语句，低版本生成的语句无法导入高版本的目标库。

## 操作步骤
1. 在源数据库上执行如下命令，导出用户帐号信息。
部分账号的权限较高，MySQL 不支持导入的，可以指定 `--ignore` 过滤掉这类帐号。
```
pt-show-grants --user=root --host=<src host or ip> --port=<src port> --user=<user> --password=<password> --ignore 'mysql.sys'@'localhost','mysql.session'@'localhost','mysql.infoschema'@'localhost','root','root'@'localhost' > account.sql
```
2. 在目标库导入用户帐号信息。
```
mysql -u<user> -p<password> -h<dst ip or host> -P<dst port> -e "source account.sql"
```
MySQL 5.7.6 及以上版本导出的 SQL 示例如下：
```
-- Grants dumped by pt-show-grants
-- Dumped from server xxxx via TCP/IP, MySQL 8.0.22-txsql at 2021-09-01 11:28:21
-- Grants for 'dts'@'%'
CREATE USER IF NOT EXISTS 'dts'@'%';
ALTER USER 'dts'@'%' IDENTIFIED WITH 'mysql_native_password' AS '*F2XFE7135318FD1F12CDF7B027506096F223DDD46' REQUIRE NONE PASSWORD EXPIRE DEFAULT ACCOUNT UNLOCK PASSWORD HISTORY DEFAULT PASSWORD REUSE INTERVAL DEFAULT PASSWORD REQUIRE CURRENT DEFAULT;
GRANT LOCK TABLES, PROCESS, RELOAD, REPLICATION CLIENT, REPLICATION SLAVE, SELECT, SHOW DATABASES, SHOW VIEW ON *.* TO `dts`@`%`;
GRANT SELECT ON `mysql`.* TO `dts`@`%`;
```
MySQL 5.7.6 以下版本导出的 SQL 示例如下：
```
-- Grants dumped by pt-show-grants
-- Dumped from server xxxx via TCP/IP, MySQL 5.6.16-log at 2021-09-01 11:33:53
-- Grants for 'dts'@'%'
GRANT LOCK TABLES, PROCESS, RELOAD, REPLICATION CLIENT, REPLICATION SLAVE, SELECT, SHOW VIEW ON *.* TO 'dts'@'%' IDENTIFIED BY PASSWORD '*47D7DB84D97A8D7EFD5B3CFA20A7A2433A9E86A4';
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO 'dts'@'%';
GRANT SELECT ON `mysql`.* TO 'dts'@'%';
```

