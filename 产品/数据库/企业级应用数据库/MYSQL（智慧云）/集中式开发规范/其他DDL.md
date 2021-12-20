ALTER，DROP 等其他 DDL 语句操作，都与 MySQL 语法一致。
但是要注意的是，TDSQL不支持将字段长度缩至实际长度以下：

```
MySQL [test]> create table t_ddl_char(name char(8) not null primary key,address varchar(10));
Query OK, 0 rows affected (1.72 sec)

MySQL [test]> insert into t_ddl_char values('abcdefg','Shenzhen');
Query OK, 1 row affected (0.07 sec)

MySQL [test]> insert into t_ddl_char values('gfedcba','Shanghai');
Query OK, 1 row affected (0.02 sec)

MySQL [test]> select name,address from t_ddl_char;
+---------+----------+
| name    | address  |
+---------+----------+
| gfedcba | Shanghai |
| abcdefg | Shenzhen |
+---------+----------+
2 rows in set (0.11 sec)

MySQL [test]> alter table t_ddl_char modify name char(12);
Query OK, 2 rows affected (0.06 sec)
Records: 2  Duplicates: 0  Warnings: 0

MySQL [test]> alter table t_ddl_char modify name char(4);
ERROR 1265 (01000): Data truncated for column 'name' at row 1
支持修改列的类型，例如从char(10)修改至varchar(100)：
MySQL [test]> show create table t_ddl_char\G;
*************************** 1. row ***************************
       Table: t_ddl_char
Create Table: CREATE TABLE `t_ddl_char` (
  `name` char(12) NOT NULL,
  `address` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

MySQL [test]> select name,address from t_ddl_char;
+---------+----------+
| name    | address  |
+---------+----------+
| abcdefg | Shenzhen |
| gfedcba | Shanghai |
+---------+----------+
2 rows in set (0.00 sec)

MySQL [test]> alter table t_ddl_char modify name varchar(100);
Query OK, 2 rows affected (0.06 sec)
Records: 2  Duplicates: 0  Warnings: 0
```
【建议】线上系统的DDL变更请通过赤兔管理平台的online-ddl模块进行。
