本节主要介绍了使用DDL语句创建表和常用DDL语句说明。
## 创建普通表
```
MySQL [test]> CREATE TABLE t_stu (stu_id int primary key,first_name VARCHAR(10),last_name VARCHAR(10),full_name VARCHAR(255)) ENGINE=InnoDB default charset=utf8mb4;
Query OK, 0 rows affected (0.03 sec)
```
## 创建分区表
### 支持的分区表类型
TDSQL支持RANGE、LIST、COLUMNS、HASH、KEY类型的分区。
- 	RANGE 分区：这种类型的分区基于落在给定范围内的列值将行分配给分区。此类型还包含一种扩展类型为RANGE COLUMNS的分区类型。
 	Range分区支持类型：
–	DATE，DATETIME，TIMESTAMP
–	TINYINT, SMALLINT, MEDIUMINT, INT , BIGINT
- 	LIST 分区：类似于按RANGE分区，区别在于LIST分区是基于列值匹配一个离散值集合中的某个值来进行选择。此类型包含一种扩展类型为LIST COLUMNS的分区类型。
 	List分区支持类型：
–	DATE，DATETIME，TIMESTAMP
–	TINYINT, SMALLINT, MEDIUMINT, INT , BIGINT
- COLUMN分区：RANGE 和 LIST 分区的扩展类型，分为RANGE COLUMNS和LIST COLUMNS两类。COLUMNS 分区允许在分区键中使用多个列，所有指定列都被考虑在内，以便在分区中放置行，以及确定在分区裁剪中检查分区的匹配行。RANGE COLUMNS 分区和 LIST COLUMNS 分区都支持使用非整数列来定义值范围或列表成员。
 	COLUMN分区支持类型：
–	DATE，DATETIME
–	TINYINT, SMALLINT, MEDIUMINT, INT , BIGINT
–	CHAR, VARCHAR
- 	HASH分区： 主要用于确保数据在分区之间均匀分布。TDSQL支持两种HASH分区，常规HASH(HASH)和线性HASH(LINEAR HASH)。
 	HASH分区支持的数据类型为：
–	DATE，DATETIME
–	TINYINT, SMALLINT, MEDIUMINT, INT, and BIGINT
-	KEY 分区：类似于按哈希分区，区别是哈希分区采用用户定义的表达式，而Key分区的哈希函数由TDSQL服务器提供。
【建议】以上分区类型如果支持的分区键包括char或者varchar类型，建议长度不超255

### RANE分区
#### Range分区表
```
MySQL [test]> CREATE TABLE employees (
    ->     id INT NOT NULL,
    ->     fname VARCHAR(30),
    ->     lname VARCHAR(30),
    ->     hired DATE NOT NULL DEFAULT '1970-01-01',
    ->     separated DATE NOT NULL DEFAULT '9999-12-31',
    ->     job_code INT NOT NULL,
    ->     store_id INT NOT NULL primary key
    -> )
    -> PARTITION BY RANGE (store_id) (
    ->     PARTITION p0 VALUES LESS THAN (6),
    ->     PARTITION p1 VALUES LESS THAN (11),
    ->     PARTITION p2 VALUES LESS THAN (16),
    ->     PARTITION p3 VALUES LESS THAN (21)
    -> );
Query OK, 0 rows affected (0.08 sec)
```
#### RANGE分区适用场景
- 当需要删除旧的数据时。有了分区，只需要执行alter table employees drop partition p0;就能删除以上employees表中store_id<6的所有数据，这样比delete from employees where store_id<6;要有效得多。
- 想要使用一个包含有日期或时间值，或包含有从一些其他级数开始增长的值的列
- 经常运行直接依赖于用于分割表的列的查询。例如，当执行一个如“SELECT COUNT(*) FROM employees WHERE store_id=5 GROUP BY store_id；”这样的查询时，TDSQL可以很迅速地确定只有分区p0需要扫描，这是因为余下的分区不可能包含有符合该WHERE子句的任何记录

#### RANGE COLUMNS分区表：
范围列分区与范围分区类似，但是使您能够基于多个列值使用范围来定义分区。 另外，可以使用非整数类型的列来定义范围。
```
MySQL [test]> CREATE TABLE rcx (
    ->          a INT not null,
    ->          b INT not null,
    ->          c CHAR(3) not null,
    ->          d INT not null,
    ->          primary key(a,d,c)
    ->      )
    ->      PARTITION BY RANGE COLUMNS(a,d,c) (
    ->          PARTITION p0 VALUES LESS THAN (5,10,'ggg'),
    ->          PARTITION p1 VALUES LESS THAN (10,20,'mmm'),
    ->          PARTITION p2 VALUES LESS THAN (15,30,'sss'),
    ->          PARTITION p3 VALUES LESS THAN (MAXVALUE,MAXVALUE,MAXVALUE)
    -> );
Query OK, 0 rows affected (0.11 sec)
```
###  LIST分区
List分区表创建语法如下：
```
MySQL [test]> CREATE TABLE employees_list (
    ->     id INT NOT NULL,
    ->     fname VARCHAR(30),
    ->     lname VARCHAR(30),
    ->     hired DATE NOT NULL DEFAULT '1970-01-01',
    ->     separated DATE NOT NULL DEFAULT '9999-12-31',
    ->     job_code INT,
    ->     store_id INT primary key
    -> )
    -> PARTITION BY LIST(store_id) (
    ->     PARTITION pNorth VALUES IN (3,5,6,9,17),
    ->     PARTITION pEast VALUES IN (1,2,10,11,19,20),
    ->     PARTITION pWest VALUES IN (4,12,13,14,18),
    ->     PARTITION pCentral VALUES IN (7,8,15,16)
    -> );
Query OK, 0 rows affected (0.10 sec)
LIST COLUMNS分区表创建语法如下：
CREATE TABLE customers_2 (
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    street_1 VARCHAR(30),
    street_2 VARCHAR(30),
    city VARCHAR(15),
    renewal DATE primary key
)
PARTITION BY LIST COLUMNS(renewal) (
    PARTITION pWeek_1 VALUES IN('2010-02-01', '2010-02-02', '2010-02-03',
        '2010-02-04', '2010-02-05', '2010-02-06', '2010-02-07'),
    PARTITION pWeek_2 VALUES IN('2010-02-08', '2010-02-09', '2010-02-10',
        '2010-02-11', '2010-02-12', '2010-02-13', '2010-02-14'),
    PARTITION pWeek_3 VALUES IN('2010-02-15', '2010-02-16', '2010-02-17',
        '2010-02-18', '2010-02-19', '2010-02-20', '2010-02-21'),
    PARTITION pWeek_4 VALUES IN('2010-02-22', '2010-02-23', '2010-02-24',
        '2010-02-25', '2010-02-26', '2010-02-27', '2010-02-28')
);
```
###  HASH分区
#### 普通Hash分区表
```
MySQL [test]> CREATE TABLE employees_p_hash (
    ->     id INT NOT NULL,
    ->     fname VARCHAR(30),
    ->     lname VARCHAR(30),
    ->     hired DATE NOT NULL DEFAULT '1970-01-01',
    ->     separated DATE NOT NULL DEFAULT '9999-12-31',
    ->     job_code INT,
    ->     store_id INT primary key
    -> )
    -> PARTITION BY HASH(store_id)
    -> PARTITIONS 4;
Query OK, 0 rows affected (0.10 sec)
```
#### 线性Hash分区表
```
MySQL [test]> CREATE TABLE employees_l_hash(
    ->     id INT NOT NULL,
    ->     fname VARCHAR(30),
    ->     lname VARCHAR(30),
    ->     hired DATE NOT NULL DEFAULT '1970-01-01',
    ->     separated DATE NOT NULL DEFAULT '9999-12-31',
    ->     job_code INT,
    ->     store_id INT
    -> )
    -> PARTITION BY LINEAR HASH( YEAR(hired) )
    -> PARTITIONS 4;
Query OK, 0 rows affected (0.09 sec)
```
线性哈希分区的优点是分区的添加，删除，合并和拆分要快得多，这在处理包含极大量（兆兆字节）数据的表时非常有用。 缺点是与使用常规散列分区获得的分布相比，数据不太可能在分区之间均匀分布。
###  KEY分区
#### Key分区表
```
MySQL [test]> CREATE TABLE k1 (
    ->     id INT NOT NULL PRIMARY KEY,
    ->     name VARCHAR(20)
    -> )
    -> PARTITION BY KEY()
    -> PARTITIONS 2;
Query OK, 0 rows affected (0.05 sec)

MySQL [test]> CREATE TABLE k2 (
    ->     id INT NOT NULL,
    ->     name VARCHAR(20),
    ->     UNIQUE KEY (id)
    -> )
    -> PARTITION BY KEY()
    -> PARTITIONS 2;
Query OK, 0 rows affected (0.05 sec)
```
如果表有主键，则KEY分区首先选取主键列作为分区键，如果表没有主键，但是存在唯一索引，则选取唯一索引作为分区键。

## 创建子分区
子分区是分区表中每个分区的再次分割。使用 RANGE或LIST分区，可以与HASH或KEY分区相结合 ，以产生复合分区（子分区）例如，参考下面的CREATE TABLE 语句：
```
MySQL [test]> CREATE TABLE ts (id INT, purchased DATE)
    ->     PARTITION BY RANGE( YEAR(purchased) )
    ->     SUBPARTITION BY HASH( TO_DAYS(purchased) )
    ->     SUBPARTITIONS 2 (
    ->         PARTITION p0 VALUES LESS THAN (1990),
    ->         PARTITION p1 VALUES LESS THAN (2000),
    ->         PARTITION p2 VALUES LESS THAN MAXVALUE
    ->     );
Query OK, 0 rows affected (0.15 sec)
```
### 删除和新增分区
TDSQL集中式实例删除和新增分区的语法格式和单机MySQL一致，语句如下：
```
MySQL [test]> SELECT PARTITION_NAME,PARTITION_METHOD,PARTITION_EXPRESSION,PARTITION_DESCRIPTION,TABLE_ROWS,SUBPARTITION_NAME,SUBPARTITION_METHOD FROM information_schema.PARTITIONS WHERE TABLE_SCHEMA=SCHEMA() AND TABLE_NAME='ts';
+----------------+------------------+----------------------+-----------------------+------------+-------------------+---------------------+
| PARTITION_NAME | PARTITION_METHOD | PARTITION_EXPRESSION | PARTITION_DESCRIPTION | TABLE_ROWS | SUBPARTITION_NAME | SUBPARTITION_METHOD |
+----------------+------------------+----------------------+-----------------------+------------+-------------------+---------------------+
| p0             | RANGE            | year(`purchased`)    | 1990                  |          0 | p0sp0             | HASH                |
| p0             | RANGE            | year(`purchased`)    | 1990                  |          0 | p0sp1             | HASH                |
| p1             | RANGE            | year(`purchased`)    | 2000                  |          0 | p1sp0             | HASH                |
| p1             | RANGE            | year(`purchased`)    | 2000                  |          0 | p1sp1             | HASH                |
| p2             | RANGE            | year(`purchased`)    | MAXVALUE              |          0 | p2sp0             | HASH                |
| p2             | RANGE            | year(`purchased`)    | MAXVALUE              |          0 | p2sp1             | HASH                |
+----------------+------------------+----------------------+-----------------------+------------+-------------------+---------------------+
6 rows in set (0.00 sec)

MySQL [test]> alter table ts drop partition p2;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

MySQL [test]>  SELECT PARTITION_NAME,PARTITION_METHOD,PARTITION_EXPRESSION,PARTITION_DESCRIPTION,TABLE_ROWS,SUBPARTITION_NAME,SUBPARTITION_METHOD FROM information_schema.PARTITIONS WHERE TABLE_SCHEMA=SCHEMA() AND TABLE_NAME='ts';
+----------------+------------------+----------------------+-----------------------+------------+-------------------+---------------------+
| PARTITION_NAME | PARTITION_METHOD | PARTITION_EXPRESSION | PARTITION_DESCRIPTION | TABLE_ROWS | SUBPARTITION_NAME | SUBPARTITION_METHOD |
+----------------+------------------+----------------------+-----------------------+------------+-------------------+---------------------+
| p0             | RANGE            | year(`purchased`)    | 1990                  |          0 | p0sp0             | HASH                |
| p0             | RANGE            | year(`purchased`)    | 1990                  |          0 | p0sp1             | HASH                |
| p1             | RANGE            | year(`purchased`)    | 2000                  |          0 | p1sp0             | HASH                |
| p1             | RANGE            | year(`purchased`)    | 2000                  |          0 | p1sp1             | HASH                |
+----------------+------------------+----------------------+-----------------------+------------+-------------------+---------------------+
4 rows in set (0.00 sec)

MySQL [test]> alter table ts add partition (partition p2 VALUES LESS THAN (2002));
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

MySQL [test]>  SELECT PARTITION_NAME,PARTITION_METHOD,PARTITION_EXPRESSION,PARTITION_DESCRIPTION,TABLE_ROWS,SUBPARTITION_NAME,SUBPARTITION_METHOD FROM information_schema.PARTITIONS WHERE TABLE_SCHEMA=SCHEMA() AND TABLE_NAME='ts';
+----------------+------------------+----------------------+-----------------------+------------+-------------------+---------------------+
| PARTITION_NAME | PARTITION_METHOD | PARTITION_EXPRESSION | PARTITION_DESCRIPTION | TABLE_ROWS | SUBPARTITION_NAME | SUBPARTITION_METHOD |
+----------------+------------------+----------------------+-----------------------+------------+-------------------+---------------------+
| p0             | RANGE            | year(`purchased`)    | 1990                  |          0 | p0sp0             | HASH                |
| p0             | RANGE            | year(`purchased`)    | 1990                  |          0 | p0sp1             | HASH                |
| p1             | RANGE            | year(`purchased`)    | 2000                  |          0 | p1sp0             | HASH                |
| p1             | RANGE            | year(`purchased`)    | 2000                  |          0 | p1sp1             | HASH                |
| p2             | RANGE            | year(`purchased`)    | 2002                  |          0 | p2sp0             | HASH                |
| p2             | RANGE            | year(`purchased`)    | 2002                  |          0 | p2sp1             | HASH                |
+----------------+------------------+----------------------+-----------------------+------------+-------------------+---------------------+
6 rows in set (0.00 sec)
```
## 分区表达式支持的函数
在分区表达式中只允许使用以下列表中显示的函数：
- ABS()
-	CEILING() (see CEILING() and FLOOR())
- DATEDIFF()
- DAY()
- DAYOFMONTH()
- DAYOFWEEK()
- DAYOFYEAR()
- EXTRACT() 
- FLOOR()
- HOUR()
-	MICROSECOND()
- MINUTE()
- MOD()
- MONTH()
- QUARTER()
- SECOND()
- TIME_TO_SEC()
- TO_DAYS()
- TO_SECONDS()
- UNIX_TIMESTAMP() (with TIMESTAMP columns)
- WEEKDAY()
- YEAR()
- YEARWEEK()
