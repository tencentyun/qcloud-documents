## Drop database
**语法如下：**
```
DROP {DATABASE | SCHEMA} [IF EXISTS] db_name
```

>!
- DROP DATABASE 删除数据库中的所有表并删除数据库。 对此语句要非常小心！ 要使用 DROP DATABASE ，您需要 DROP database 的 权限。 DROP SCHEMA 是DROP DATABASE的同义词。
- 删除数据库时， 不会自动删除专门为数据库授予的权限，必须手动删除它们。

**示例：**

```
DROP DATABASE test;
```

## Drop table
**语法如下：**
```
DROP TABLE [IF EXISTS]
    tbl_name [, tbl_name] ...
    [RESTRICT | CASCADE]
```

>!
- DROP TABLE 删除一个或多个表。 您必须拥有 DROP 每个表 的 权限。
- 对于每个表，它将删除表定义和所有表数据。 如果表已分区，则该语句将删除表定义，其所有分区，存储在这些分区中的所有数据以及与已删除表关联的所有分区定义。
- 删除表也会删除表的任何触发器。
- DROP TABLE 导致隐式提交。 
- 删除表时，不会自动删除专门为该表授予的权限 。 必须手动删除它们。
- 所有 innodb_force_recovery 设置都不支持 DROP TABLE
- RESTRICT 和 CASCADE 关键字什么也不做。 它们被允许使从其他数据库系统移植更容易。

**示例：**

```
DROP TABLE test;
drop table test RESTRICT;
drop table test5 CASCADE;
```

## Drop index
**语法如下：**

```
DROP INDEX index_name ON tbl_name
    [algorithm_option | lock_option] ...

algorithm_option:
    ALGORITHM [=] {DEFAULT | INPLACE | COPY}

lock_option:
    LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}
```

>!要删除主键，索引名称始终为 PRIMARY，必须将其指定为带引号的标识符，因为 PRIMARY 是保留字：DROP INDEX `PRIMARY` ON t;

**示例：**

```
MySQL [test]> show create table customer\G;
*************************** 1. row ***************************
       Table: customer
Create Table: CREATE TABLE `customer` (
  `cust_id` int(11) NOT NULL,
  `name` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `job_id` int(11) DEFAULT NULL,
  `job_name` varchar(300) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`cust_id`),
  UNIQUE KEY `uniq_idx_job_id` (`cust_id`,`job_id`),
  KEY `idx_cust` (`name`,`job_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=cust_id
1 row in set (0.00 sec)

MySQL [test]> drop index uniq_idx_job_id on customer;
Query OK, 0 rows affected (0.04 sec)

MySQL [test]> drop index idx_cust on customer;
Query OK, 0 rows affected (0.08 sec)
```
