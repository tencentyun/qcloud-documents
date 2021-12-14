## CREATE DATABASE
本节介绍CREATE DATABASE语法。
```
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
    [create_option] ...

create_option: [DEFAULT] {
    CHARACTER SET [=] charset_name
  | COLLATE [=] collation_name
}
```
>!
- CREATE DATABASE 创建具有给定名称的数据库。 要使用此语句，您需要对数据库具有 CREATE 权限。 CREATE SCHEMA 是 CREATE DATABASE 的同义词。
- 如果数据库存在并且您没有指定 IF NOT EXISTS，则会发生错误。
- 在具有活动 LOCK TABLES 语句的会话中不允许 CREATE DATABASE。
- CHARACTER SET 选项指定默认的数据库字符集。 COLLATE 选项指定默认的数据库排序规则。要查看可用的字符集和排序规则，请使用 SHOW CHARACTER SET 和 SHOW COLLATION 语句 

### 示例：
`create database d2 default charset 'utf8mb4'; `

## CREATE TABLE
TDSQL分布式实例支持创建分表、单表和广播表。分表即自动水平拆分的表（Shard表），水平拆分是基于分表键采用类似于一致性 Hash、Range、List等方式，根据计算后的值分配到不同的节点组中的一种技术方案。可以将满足对应条件的行将存储在相同的物理节点组中。这种场景称为组拆分（Groupshard）,可以迅速提高应用层联合查询等语句的处理效率。TDSQL支持LIST、RANGE、HASH三种类型的一级分区，同时支持RANGE、LIST两种格式的二级分区。
**创建一级hash分区表语法**
```
CREATE TABLE [IF NOT EXISTS] tbl_name
    [(create_definition)]
    [local_table_options]
shardkey=column_name

create_definition: {
    col_name column_definition
  | {INDEX | KEY} [index_name] [index_type] (key_part,...)
      [index_option] ...
  | [INDEX | KEY] [index_name] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] PRIMARY KEY
      [index_type] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY]
      [index_name] [index_type] (key_part,...)
      [index_option] ...
}

column_definition: {
    data_type [NOT NULL | NULL] [DEFAULT]
      [AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [COLLATE collation_name]
      [COLUMN_FORMAT {FIXED | DYNAMIC | DEFAULT}]
      [ENGINE_ATTRIBUTE [=] 'string']
  | data_type
      [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
}

key_part: {col_name [(length)]} [ASC | DESC]

index_type:
USING {BTREE}

index_option: {
 index_type | COMMENT 'string'
}
[local_table_options]
Local_table_option: {AUTO_INCREMENT [=] value
  | [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'string'
  | ENGINE [=] engine_name
  | ROW_FORMAT [=] {DEFAULT | DYNAMIC | FIXED | COMPRESSED | REDUNDANT | COMPACT}
  | STATS_AUTO_RECALC [=] {DEFAULT | 0 | 1}
  | STATS_PERSISTENT [=] {DEFAULT | 0 | 1}
  | STATS_SAMPLE_PAGES [=] value)
}
```
**创建一级range| list分区表语法**
```
CREATE TABLE [IF NOT EXISTS] tbl_name
    [(create_definition)]
    [local_table_options]
TDSQL_DISTRIBUTED BY range|list (column_name) [partition_options]

create_definition: {
    col_name column_definition
  | {INDEX | KEY} [index_name] [index_type] (key_part,...)
      [index_option] ...
  | [INDEX | KEY] [index_name] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] PRIMARY KEY
      [index_type] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY]
      [index_name] [index_type] (key_part,...)
      [index_option] ...
}

column_definition: {
    data_type [NOT NULL | NULL] [DEFAULT]
      [AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [COLLATE collation_name]
      [COLUMN_FORMAT {FIXED | DYNAMIC | DEFAULT}]
      [ENGINE_ATTRIBUTE [=] 'string']
  | data_type
      [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
}

key_part: {col_name [(length)]} [ASC | DESC]

index_type:
USING {BTREE}

index_option: {
 index_type | COMMENT 'string'
}
[local_table_options]
Local_table_option: {AUTO_INCREMENT [=] value
  | [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'string'
  | ENGINE [=] engine_name
  | ROW_FORMAT [=] {DEFAULT | DYNAMIC | FIXED | COMPRESSED | REDUNDANT | COMPACT}
  | STATS_AUTO_RECALC [=] {DEFAULT | 0 | 1}
  | STATS_PERSISTENT [=] {DEFAULT | 0 | 1}
  | STATS_SAMPLE_PAGES [=] value)
}
partition_options:
    PARTITION BY
        | RANGE{(expr)}
        | LIST{(expr)}
    [(partition_definition [, partition_definition] ...)]

partition_definition:
    PARTITION partition_name
        [VALUES
            {LESS THAN {(expr | value_list) | MAXVALUE}
            |
            IN (value_list)}]
        [[STORAGE] ENGINE [=] engine_name]
        [COMMENT [=] 'string']
```
### 创建分区表
#### 一级分区表
在TDSQL中，分表也叫一级分区表。有hash、range、list三种规则。一级hash分区使用shardkey关键字指定拆分键。range和list分区使用tdsql_distributed by语法指定拆分键。
##### 一级HASH分区
- 一级hash分区支持类型
–	DATE，DATETIME
–	TINYINT, SMALLINT, MEDIUMINT, INT, BIGINT
–	CHAR，VARCHAR

>!
- Shardkey 字段必须是主键以及所有唯一索引的一部分
- Shardkey字段的值不能为中文，因为Proxy不会转换字符集，所以不同字符集可能会路由到不同的分区
- Shardkey=a 需放在SQL语句的最后

**示例**
```
DROP TABLE IF EXISTS employees_hash;
CREATE TABLE `employees_hash` (
  `id`int NOT NULL,
  `city` varchar(10),
  `fired` DATE NOT NULL DEFAULT '1970.01.01',
  PRIMARY KEY(id)
) shardkey=id;
```

##### 一级RANGE分区
- 一级range分区支持类型
–	DATE，DATETIME，TIMESTAMP
–	TINYINT, SMALLINT, MEDIUMINT, INT, and BIGINT
–	CHAR，VARCHAR
```
create table t1(a int key, b int) tdsql_distributed by range(a) (s1 values less than(100), s2 values less than(200));

```
【禁止】避免使用TIMESTAMP类型作为分区键，因为timestamp受到时区的影响，同时只能使用到2038年
【建议】如果分区键是char或者varchar类型，建议长度不超255

### 一级LIST分区
- 一级list分区支持类型
–	DATE，DATETIME，TIMESTAMP
–	TINYINT, SMALLINT, MEDIUMINT, INT, and BIGINT
–	CHAR，VARCHAR
```
create table t2(a int key, b int)  tdsql_distributed by list(a) (s1 values in(1,2), s2 values in (3,4));
```

>!
- dsql_distributed by ...语法放置于create table ...的末尾
- 创建一级range分区表语句中指定的s1和s2是每个set的别名，基于实现原理，s1、s2不能自定义，只能按照顺序依次命名为s1、s2…
- set的别名可通过/*proxy*/show status;获取到

**示例**
```
--创建分布在2个set上的分区表：
DROP TABLE IF EXISTS employees_range;
CREATE TABLE `employees_range` (
  `id`int NOT NULL,
  `city` varchar(10),
  `fired` DATE NOT NULL DEFAULT '1970.01.01',
  PRIMARY KEY(id)
)
TDSQL_DISTRIBUTED BY RANGE(id) (
  s1 VALUES LESS THAN (6),
  s2 VALUES LESS THAN (11)
);
--查看set_1624363222_1和set_1624363251_3的别名分别为s1和s2：
```
##### 一级LIST分区
- 一级list分区支持类型
–DATE，DATETIME，TIMESTAMP
–TINYINT, SMALLINT, MEDIUMINT, INT, and BIGINT
–CHAR，VARCHAR

>!
- 分区键为字符串时，不要使用中文
- tdsql_distributed by ...语法放置于create table ...的末尾
- 创建一级list分区表语句中指定的s1和s2是每个set的别名，基于实现原理，s1、s2不能自定义，只能按照顺序依次命名为s1、s2…
- set的别名可通过/*proxy*/show status;获取到

**示例**
```
DROP TABLE IF EXISTS  employees_list;
CREATE TABLE `employees_list` (
  `id`int NOT NULL,
  `city` varchar(10),
  `fired` DATE NOT NULL DEFAULT '1970.01.01',
  PRIMARY KEY(id)
)
TDSQL_DISTRIBUTED BY LIST(id) (
  s1 VALUES IN (1,3,5),
  s2 VALUES IN (2,4,6)
);
```

#### 二级分区表
二级分区是将特定条件的数据进行分区处理，目前TDSQL支持Range和List两种格式的二级分区，具体建表语法和MySQL分区语法类似。
**创建二级range| list分区表语法**
```
CREATE TABLE [IF NOT EXISTS] tbl_name
    [(create_definition)]
    [local_table_options]
TDSQL_DISTRIBUTED BY range|list (column_name) [partition_options]

create_definition: {
    col_name column_definition
  | {INDEX | KEY} [index_name] [index_type] (key_part,...)
      [index_option] ...
  | [INDEX | KEY] [index_name] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] PRIMARY KEY
      [index_type] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY]
      [index_name] [index_type] (key_part,...)
      [index_option] ...
}

column_definition: {
    data_type [NOT NULL | NULL] [DEFAULT]
      [AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [COLLATE collation_name]
      [COLUMN_FORMAT {FIXED | DYNAMIC | DEFAULT}]
      [ENGINE_ATTRIBUTE [=] 'string']
  | data_type
      [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
}

key_part: {col_name [(length)]} [ASC | DESC]

index_type:
USING {BTREE}

index_option: {
 index_type | COMMENT 'string'
}
[local_table_options]
Local_table_option: {AUTO_INCREMENT [=] value
  | [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'string'
  | ENGINE [=] engine_name
  | ROW_FORMAT [=] {DEFAULT | DYNAMIC | FIXED | COMPRESSED | REDUNDANT | COMPACT}
  | STATS_AUTO_RECALC [=] {DEFAULT | 0 | 1}
  | STATS_PERSISTENT [=] {DEFAULT | 0 | 1}
  | STATS_SAMPLE_PAGES [=] value)
}
partition_options:
    PARTITION BY
        | RANGE{(expr)}
        | LIST{(expr)}
    [SUBPARTITION BY
        {HASH(expr)
        |(column_list) }
    ]
    [(partition_definition [, partition_definition] ...)]

partition_definition:
    PARTITION partition_name
        [VALUES
            {LESS THAN {(expr | value_list) | MAXVALUE}
            |
            IN (value_list)}]
        [[STORAGE] ENGINE [=] engine_name]
        [COMMENT [=] 'string' ]
        [(subpartition_definition [, subpartition_definition] ...)]

subpartition_definition:
    SUBPARTITION logical_name
        [[STORAGE] ENGINE [=] engine_name]
        [COMMENT [=] 'string']
```

##### 二级RANGE分区
- Range支持类型
–	DATE，DATETIME，TIMESTAMP
—支持year，month，day函数，函数为空和day函数一样
–	TINYINT, SMALLINT, MEDIUMINT, INT , BIGINT
 —支持year，month，day函数，此时传入的值转换为年月日，然后和分表信息进行对比

>!
- 使用tdsql_distributed by ...语法创建分区表时，语句中指定的s1和s2是每个set的别名，基于实现原理，s1、s2不能自定义，只能按照顺序依次命名为s1、s2…
- 分区使用小于符号“<”，如果要存储当年数据（例如，2017），需要创建小于往后一年（<2018）的分区，用户只需创建到当前的时间分区。TDSQL会自动增加后续分区，默认往后创建3个分区，以Year为例，TDSQL会自动往后创建3年（2018年、2019年、2020年）的分区，后续也会自动增减。

**示例**
```
一级hash二级range分区：
DROP TABLE IF EXISTS employees_hash_range;
CREATE TABLE `employees_hash_range` (
  `id`int NOT NULL,
  `city` varchar(10),
  `fired` DATE NOT NULL DEFAULT '1970.01.01',
  PRIMARY KEY(id)
) shardkey=id
PARTITION BY RANGE (month(fired)) (
  PARTITION p0 VALUES LESS THAN (202106),
  PARTITION p1 VALUES LESS THAN (202107)
);
一级list二级range分区:
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
一级range二级range分区:
DROP TABLE IF EXISTS employees_range_range;
CREATE TABLE `employees_range_range` (
  `id`int NOT NULL,
  `city` varchar(10),
  `fired` DATE NOT NULL DEFAULT '1970.01.01',
  PRIMARY KEY(id,fired)
)
PARTITION BY RANGE (month(fired)) (
  PARTITION p0 VALUES LESS THAN (202106),
  PARTITION p1 VALUES LESS THAN (202107)
)
TDSQL_DISTRIBUTED BY RANGE(id) (
  s1 VALUES LESS THAN (6),
  s2 VALUES LESS THAN (11)
);

一级range二级range分区和子分区
DROP TABLE if exists tb_sub_ev;
CREATE TABLE tb_sub_ev (
  id int NOT NULL,
  purchased date NOT NULL,
  PRIMARY KEY (id,purchased)
) ENGINE=InnoDB
PARTITION BY RANGE (YEAR(purchased))
    SUBPARTITION BY HASH (TO_DAYS(purchased))
(PARTITION p0 VALUES LESS THAN (1990)
       (SUBPARTITION s0 ENGINE = InnoDB,
       SUBPARTITION s1 ENGINE = InnoDB),
 PARTITION p1 VALUES LESS THAN (2000)
       (SUBPARTITION s2 ENGINE = InnoDB,
       SUBPARTITION s3 ENGINE = InnoDB))
TDSQL_DISTRIBUTED BY RANGE(id) (s1 values less than ('100'),s2 values less than ('1000'));
```

##### 二级LIST分区
-  List支持类型
–	DATE，DATETIME，TIMESTAMP —支持年月日函数
–	TINYINT, SMALLINT, MEDIUMINT, INT , BIGINT

>!使用tdsql_distributed by ...语法创建分区表时，语句中指定的s1和s2是每个set的别名，基于实现原理，s1、s2不能自定义，只能按照顺序依次命名为s1、s2…

**示例**

```
一级hash二级list分区：
DROP TABLE IF EXISTS employees_hash_list;
CREATE TABLE `employees_hash_list` (
  `id`int NOT NULL,
  `region`int NOT NULL,
  `city` varchar(10),
  `fired` DATE NOT NULL DEFAULT '1970.01.01',
  PRIMARY KEY(id)
) shardkey=id
PARTITION BY LIST (region) (
  PARTITION pRegion_1 VALUES IN (10, 30),
  PARTITION pRegion_2 VALUES IN (20, 40)
);
一级list二级list分区:
DROP TABLE IF EXISTS employees_list_list;
CREATE TABLE `employees_list_list` (
  `id`int NOT NULL,
  `region`int NOT NULL,
  `city` varchar(10),
  `fired` DATE NOT NULL DEFAULT '1970.01.01',
  PRIMARY KEY(id, region)
)
PARTITION BY LIST (region) (
  PARTITION pRegion_1 VALUES IN (10, 30),
  PARTITION pRegion_2 VALUES IN (20, 40)
)
TDSQL_DISTRIBUTED BY LIST(id) (
  s1 VALUES IN (1,3,5),
  s2 VALUES IN (2,4,6)
);

一级range二级list分区:
DROP TABLE IF EXISTS employees_range_list;
CREATE TABLE `employees_range_list` (
  `id`int NOT NULL,
  `region`int NOT NULL,
  `city` varchar(10),
  `fired` DATE NOT NULL DEFAULT '1970.01.01',
  PRIMARY KEY(id,region)
)
PARTITION BY LIST (region) (
  PARTITION pRegion_1 VALUES IN (10, 30),
  PARTITION pRegion_2 VALUES IN (20, 40)
)
TDSQL_DISTRIBUTED BY RANGE(id) (
  s1 VALUES LESS THAN (6),
  s2 VALUES LESS THAN (11)
);
```

### 创建广播表
广播表又名小表广播功能，创建时需要指定noshardkey_allset关键字。创建广播表后，每个节点都有该表的全量数据，且该表的所有操作都将广播到所有物理分片（set）中。
广播表主要用于提升跨节点组（ Set） 的Join 操作的性能，常用于配置表等。
**示例**
```
DROP TABLE IF EXISTS global_table_a;
CREATE TABLE  global_table_a (a int, b int key) shardkey=noshardkey_allset;

```

### 创建单片表
普通表：又名单片表（Noshard表），创建时无须指定shardkey或者tdsql_distributed by关键字。单片表无需拆分且没有做任何特殊处理的表。其语法和MySQL完全一样，所有该类型表的全量数据默认存放在第一个物理节点组（Set）中。
**示例**
```
DROP TABLE IF EXISTS noshard_table;
CREATE TABLE noshard_table (a int, b int key);
```

### 创建临时表
临时表：创建表时可以使用 TEMPORARY 关键字。 TEMPORARY 表仅在当前会话中可见，并在会话关闭时自动删除。这意味着两个不同的会话可以使用相同的临时表名称，而不会相互冲突或与现有的同名非临时表发生冲突。 （现有表是隐藏的，直到临时表被删除。）
>!
- 需要使用注释透传才可创建临时表。关于注释透传功能请参考6.5节。
- 使用/*sets:allsets*/创建的临时表，查询时可以指定任意setid。而如果使用/*sets:setid*/，则查询临时表时只能指定对应的setid。

**示例**

```
--使用/*sets:allsets*/创建临时表：
MySQL [test]> /*sets:allsets*/ DROP TABLE IF EXISTS new_tmp_tbl;
Query OK, 0 rows affected (0.01 sec)

MySQL [test]> /*sets:allsets*/ CREATE TEMPORARY TABLE new_tmp_tbl(id int primary key);
Query OK, 0 rows affected (0.00 sec)

MySQL [test]> /*sets:set_1624363222_1*/ select * from new_tmp_tbl;
Empty set (0.01 sec)

MySQL [test]> /*sets:set_1624363251_3*/ select * from new_tmp_tbl;
Empty set (0.00 sec)

MySQL [test]> /*sets:set_1626536042_12*/ select * from new_tmp_tbl;
Empty set (0.00 sec)

MySQL [test]> /*sets:allsets*/ select * from new_tmp_tbl;
Empty set (0.00 sec)

--使用/*sets:setid*/创建临时表：
MySQL [test]> /*sets:set_1624363222_1*/ CREATE TEMPORARY TABLE new_tmp_tbl(id int primary key);
Query OK, 0 rows affected (0.01 sec)

MySQL [test]> /*sets:set_1624363222_1*/ select * from new_tmp_tbl;
Empty set (0.01 sec)

MySQL [test]> /*sets:set_1624363251_3*/ select * from new_tmp_tbl;
ERROR 1146 (42S02): Table 'test.new_tmp_tbl' doesn't exist

MySQL [test]> /*sets:set_1626536042_12*/ select * from new_tmp_tbl;
ERROR 1146 (42S02): Table 'test.new_tmp_tbl' doesn't exist

MySQL [test]> /*sets:allsets*/ select * from new_tmp_tbl;
ERROR 1146 (42S02): Table 'test.new_tmp_tbl' doesn't exist
```

## CREATE INDEX
通常，在使用 CREATE TABLE 创建表本身时在表上创建所有索引。该准则对于 InnoDB 表尤其重要，其中主键决定了数据文件中行的物理布局。 CREATE INDEX 使您能够向现有表添加索引。
**语法：**
```
CREATE [UNIQUE ] INDEX index_name
    [index_type]
    ON tbl_name (key_part,...)
    [index_option]
    [algorithm_option | lock_option] ...

key_part: {col_name [(length)]} [ASC | DESC]

index_option: {
  index_type | COMMENT 'string'
}

index_type:
    USING {BTREE}

algorithm_option:
    ALGORITHM [=] {DEFAULT | INPLACE | COPY}

lock_option:
    LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}
```
>!
- CREATE INDEX 不能用于创建 PRIMARY KEY；对于主键，请改用 ALTER TABLE。
- 对于INNODB存储引擎，允许的索引类型为BTREE。

**示例**

```
创建测试表：
DROP TABLE IF EXISTS customer;
CREATE TABLE customer(cust_id int key,name varchar(200),job_id int,job_name varchar(300)) shardkey=cust_id;

使用using语句指定index_type，若不指定，默认为BTREE：
CREATE INDEX j_idx ON customer (name) USING BTREE;

创建列前缀索引：
CREATE INDEX idx_part_name ON customer (name(10));

创建降序索引：
CREATE INDEX idx_name_desc ON customer (name desc);

创建升序索引：
CREATE INDEX idx_name_asc ON customer (name asc);

创建唯一索引：
CREATE UNIQUE INDEX uniq_idx_job_id on customer(cust_id,job_id);

创建组合索引：
CREATE INDEX idx_cust on customer(name,job_name);

使用COMMENT语句指定索引页合并阈值：
CREATE INDEX j_idx_com ON customer (name) COMMENT 'MERGE_THRESHOLD=40';
```
## CREATE  VIEW
**语法如下**：
```
CREATE
    [OR REPLACE]
    VIEW view_name [(column_list)]
    AS select_statement
```
>!CREATE VIEW 语句创建一个新视图，如果给出OR REPLACE 子句，则替换现有视图。 如果视图不存在，CREATE OR REPLACE VIEW 与 CREATE VIEW 相同。 如果视图确实存在，CREATE OR REPLACE VIEW 将替换它。

**示例：**
```
MySQL [test]> create view v1 as select * from employee;
Query OK, 0 rows affected (0.01 sec)
```
## CREATE PROCEDURE
**语法如下：**
```
CREATE
    [DEFINER = user]
    PROCEDURE sp_name ([proc_parameter[,...]])
    [characteristic ...] routine_body
proc_parameter:
[ IN | OUT | INOUT ] param_name type
type:
Any valid MySQL data type
characteristic: {
    COMMENT 'string'
  | LANGUAGE SQL
  | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
}
routine_body:
    Valid SQL routine statement
```
>!这些语句用于创建存储过程。 默认情况下，存储过程与默认数据库相关联。 要将存储过程与给定数据库显式关联，请在创建时将名称指定为db_name.sp_name。
**示例：**

```
create database world;
use world;
create table cities(countryCode varchar(20),countryname varchar(20),city_code varchar(20) primary key,city_name varchar(20)) shardkey=city_code;

insert into world.cities(countryCode,countryname,city_code,city_name) values('CHN','CHINA','SH','SHANGHAI');
insert into world.cities(countryCode,countryname,city_code,city_name) values('CHN','CHINA','BJ','BEIJING');
insert into world.cities(countryCode,countryname,city_code,city_name) values('CHN','CHINA','SZ','SHENZHEN');
insert into world.cities(countryCode,countryname,city_code,city_name) values('CHN','CHINA','GZ','GUANGZHOU');
insert into world.cities(countryCode,countryname,city_code,city_name) values('CHN','CHINA','CD','CHENGDU');

--创建procedure
/*sets:allsets*/CREATE PROCEDURE citycount (IN country CHAR(3), OUT cities INT)
            BEGIN
              SELECT COUNT(*) INTO cities  FROM world.cities
              WHERE CountryCode = country;
            END
//
--调用procedure
MySQL [world]>  /*sets:allsets*/ CALL citycount('CHN', @cities)//

--查看调用结果，5条记录存储在3个set上：
MySQL [world]> /*sets:allsets*/SELECT @cities//
+---------+-------------------+
| @cities | info              |
+---------+-------------------+
|       1 | set_1624363222_1  |
|       2 | set_1626536042_12 |
|       2 | set_1624363251_3  |
+---------+-------------------+
3 rows in set (0.01 sec)
```
