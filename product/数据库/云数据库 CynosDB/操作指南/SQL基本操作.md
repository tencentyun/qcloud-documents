本文为您列举了部分常用 SQL 命令。

如需了解更详细的 SQL 命令信息，包括命令参数和限制条件等，请参见 [MySQL 官方指南](https://dev.mysql.com/doc/refman/5.7/en/?spm=a2c4g.11186623.0.0.1987457aTFGg7y)。

## 查询版本
方法一：
```
MySQL [(none)]> SELECT CYNOS_VERSION();
+------------------------+
| CYNOS_VERSION() |
+------------------------+
| 5.7.mysql_cynos.1.3.10 |
+------------------------+
1 row in set (0.00 sec)
```
方法二：
```
MySQL [(none)]> SELECT @@CYNOS_VERSION;
+------------------------+
| @@CYNOS_VERSION |
+------------------------+
| 5.7.mysql_cynos.1.3.10 |
+------------------------+
1 row in set (0.00 sec)
```
方法三：
```
MySQL [(none)]> SHOW VARIABLES LIKE 'CYNOS_VERSION'; 
+---------------+------------------------+
| Variable_name | Value |
+---------------+------------------------+
| cynos_version | 5.7.mysql_cynos.1.3.10 |
+---------------+------------------------+
1 row in set (0.01 sec)
```

## 数据库相关

| 命令 | 示例 | 
|---------|---------|
| 创建数据库并指定字符集 | `create database db01 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;` |
| 删除数据库 | `drop database db01;` |

## 帐号相关

| 命令 | 示例 | 
|---------|---------|
| 创建帐号 | `CREATE USER 'username'@'host' IDENTIFIED BY 'password';` | 
| 删除帐号 | `DROP USER 'username'@'host';` | 
| 赋权 | `GRANT SELECT ON db01.* TO 'username'@'host';` | 
| 查询数据库中的帐号 | `SELECT user,host,password FROM mysql.user_view;`<br>或<br>`show grants for xxx` | 
| 权限回收 | 收回全部权限：`REVOKE ALL PRIVILEGES,GRANT OPTION FROM 'username'@'host';`<br>收回指定权限：`REVOKE UPDATE ON *.* FROM 'username'@'host';` | 



