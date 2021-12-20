## ALTER TABLE
本章介绍ALTER相关用法。ALTER TABLE 更改表的结构。 例如，您可以添加或删除列、创建或销毁索引、更改现有列的类型或重命名列或表本身。 您还可以更改特征，例如用于表或表注释的存储引擎。
但是请注意：线上系统的DDL变更请通过赤兔管理控制台的online-ddl模块进行。
语法如下：
```
ALTER TABLE tbl_name
    [alter_option [, alter_option] ...]
    [partition_options]

alter_option: {
    table_options
  | ADD [COLUMN] col_name column_definition
        [FIRST | AFTER col_name]
  | ADD [COLUMN] (col_name column_definition,...)
  | ADD {INDEX | KEY} [index_name]
        [index_type] (key_part,...) [index_option] ...
  | ALGORITHM [=] {DEFAULT | INSTANT | INPLACE | COPY}
  | CHANGE [COLUMN] old_col_name new_col_name column_definition
        [FIRST | AFTER col_name]
  | [DEFAULT] CHARACTER SET [=] charset_name [COLLATE [=] collation_name]
  | {DISABLE | ENABLE} KEYS
  | DROP [COLUMN] col_name
  | DROP {INDEX | KEY} index_name
  | LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}
  | MODIFY [COLUMN] col_name column_definition
        [FIRST | AFTER col_name]
  | ORDER BY col_name [, col_name] ...
}

partition_options:
    partition_option [partition_option] ...

partition_option: {
    ADD PARTITION (partition_definition)
  | DROP PARTITION partition_names
  | TRUNCATE PARTITION {partition_names | ALL}
}

key_part: {col_name [(length)]} [ASC | DESC]

index_type:
    USING {BTREE}

index_option: {
index_type | COMMENT 'string'
}

table_options:
    table_option [[,] table_option] ...

table_option: {AUTO_INCREMENT [=] value
  | [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'string'
  | COMPRESSION [=] {'ZLIB' | 'LZ4' | 'NONE'}
  | ENGINE [=] engine_name
  | KEY_BLOCK_SIZE [=] value
  | ROW_FORMAT [=] {DEFAULT | DYNAMIC | FIXED | COMPRESSED | REDUNDANT | COMPACT}
  | STATS_AUTO_RECALC [=] {DEFAULT | 0 | 1}
  | STATS_PERSISTENT [=] {DEFAULT | 0 | 1}
  | STATS_SAMPLE_PAGES [=] value)
}
```

>!
- 要使用 ALTER TABLE ，你需要 ALTER ， CREATE 和 INSERT 权限。
- 不支持改变shardkey类型、删除shardkey的操作
- 一级分区，语法和单表一样，只能改变db上表结构，不能改变数据分布方式。
- 二级分区，支持添加和删除分区，语法和单表一样，range分区只能向后追加。

**示例：**

```
--创建一级hash分区表
DROP TABLE IF EXISTS sbtest1;
CREATE TABLE `sbtest1` 
(`k` bigint(20) NOT NULL,
`id` bigint(20) NOT NULL,
`c` char(120)  NOT NULL, 
`pad` char(60) NOT NULL, 
`balance` int(11) NOT NULL, 
`lastModifyTime` datetime,
PRIMARY KEY (`k`,`id`), 
KEY `k_1` (`k`)) 
ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=id;

--添加删除索引
alter table sbtest1 add index idx_blc (balance);
alter table sbtest1 drop index idx_blc;

--修改表字段类型
alter table sbtest1 modify column pad varchar(50);

--增加一个新列为第一列
alter table sbtest1 add column col1 INT NOT NULL first;

--增加一个到指定列之后
alter table sbtest1 add column col_after_pad INT NOT NULL after pad;

--修改表增加字段
alter table sbtest1 add column mark varchar(50);

--修改表字段名字
alter table sbtest1 change column k k_new1 bigint(20);

--修改表删除字段
alter table sbtest1 drop column mark;

--重组表
ALTER TABLE sbtest1 ENGINE = InnoDB;

--更改 InnoDB 表以使用压缩行存储格式：
ALTER TABLE sbtest1 ROW_FORMAT = COMPRESSED;

--添加（或更改）表注释：
ALTER TABLE sbtest1 COMMENT = 'New table comment';
```
**示例：**

```
创建二级分区表：
DROP TABLE if exists customers_1;
CREATE TABLE customers_1 (
   first_name VARCHAR(25) primary key,
   last_name VARCHAR(25),
   street_1 VARCHAR(30),
   street_2 VARCHAR(30),
   city_name VARCHAR(15),
   renewal DATE
) shardkey=first_name
PARTITION BY LIST (city_name) (
   PARTITION pRegion_1 VALUES IN('BJ', 'GZ', 'SZ'),
   PARTITION pRegion_2 VALUES IN('SH', 'CD'),
   PARTITION pRegion_3 VALUES IN('GY'),
   PARTITION pRegion_4 VALUES IN('HZ')
);

删除分区：
ALTER TABLE customers_1 drop partition pRegion_4;

增加分区：
ALTER TABLE customers_1 add partition (partition pRegion_4 VALUES IN('TJ'));

截断分区：
ALTER TABLE customers_1 truncate partition pRegion_4;
```
**示例：**

```
创建二级分区表：
DROP TABLE IF EXISTS employees_list_range;
CREATE TABLE `employees_list_range` (
  `id`int NOT NULL,
  `city` varchar(10),
  `fired` DATE NOT NULL DEFAULT '1970.01.01',
  PRIMARY KEY(id,fired)
)
PARTITION BY RANGE (month(fired)) (
  PARTITION p0 VALUES LESS THAN (202106),
  PARTITION p1 VALUES LESS THAN (202107)
)
TDSQL_DISTRIBUTED BY LIST(id) (
  s1 VALUES IN (1,3,5),
  s2 VALUES IN (2,4,6)
);

删除分区：
ALTER TABLE employees_list_range drop partition p1;

增加分区：
ALTER TABLE employees_list_range add partition(partition p2 values less than (202108));

截断分区：
ALTER TABLE employees_list_range truncate partition p0;
```
