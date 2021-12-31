ALTER，DROP 等其他 DDL 语句操作，绝大部分都与 MySQL 语法完全一致，但如4.1.2节中所述，对于ALTER语句修改shardkey的语句会有以下限制：
不支持ALTER对shardkey改名：

```
MySQL [test]> create table t_ddl(id int primary key not null,name char(8),address char(10)) shardkey=id;
Query OK, 0 rows affected (2.17 sec)

MySQL [test]> insert into t_ddl(id,name,address) values(1,'abcdefg','Shenzhen');
Query OK, 1 row affected (0.05 sec)

MySQL [test]> insert into t_ddl(id,name,address) values(2,'gfedcba','Shanghai');
Query OK, 1 row affected (0.05 sec)

MySQL [test]> select id,name,address from t_ddl;
+----+---------+----------+
| id | name    | address  |
+----+---------+----------+
|  1 | abcdefg | Shenzhen |
|  2 | gfedcba | Shanghai |
+----+---------+----------+
2 rows in set (0.05 sec)

MySQL [test]> /*sets:allsets */ alter table t_ddl change id stu_num int;
ERROR 3855 (HY000): Column 'id' has a partitioning function dependency and cannot be dropped or renamed.

```
不支持将shardkey字段长度缩至实际长度以下：

```
MySQL [test]> create table t_ddl_char(name char(8) not null primary key,address varchar(10)) shardkey=name;
Query OK, 0 rows affected (1.72 sec)

MySQL [test]> insert into t_ddl_char(name,address) values('abcdefg','Shenzhen');
Query OK, 1 row affected (0.07 sec)

MySQL [test]> insert into t_ddl_char(name,address) values('gfedcba','Shanghai');
Query OK, 1 row affected (0.02 sec)

MySQL [test]> select name,address from t_ddl_char;
+---------+----------+
| name    | address  |
+---------+----------+
| gfedcba | Shanghai |
| abcdefg | Shenzhen |
+---------+----------+
2 rows in set (0.11 sec)

MySQL [test]> /*sets:allsets */  alter table t_ddl_char modify name char(12);
Query OK, 2 rows affected (5.02 sec)

MySQL [test]>/*sets:allsets */ alter table t_ddl_char modify name char(4);
ERROR 1265 (HY000): Data truncated for column 'name' at row 1

```
支持修改shardkey的类型，例如从char(10)修改至varchar(100)：

```
MySQL [test]> show create table t_ddl_char\G;
*************************** 1. row ***************************
       Table: t_ddl_char
Create Table: CREATE TABLE `t_ddl_char` (
  `name` varchar(100) COLLATE utf8_bin NOT NULL,
  `address` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=name
1 row in set (0.01 sec)

MySQL [test]> select name,address from t_ddl_char;
+---------+----------+
| name    | address  |
+---------+----------+
| abcdefg | Shenzhen |
| gfedcba | Shanghai |
+---------+----------+
2 rows in set (0.00 sec)

MySQL [test]> /*sets:allsets */  alter table t_ddl_char modify name varchar(100);
Query OK, 2 rows affected (5.22 sec)

```
【建议】线上系统的DDL变更请通过赤兔管理控制台的online-ddl模块进行
