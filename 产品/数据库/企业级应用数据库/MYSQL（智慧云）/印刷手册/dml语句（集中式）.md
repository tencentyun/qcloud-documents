## CREATE
### CREATE DATABASE语法
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
- CHARACTER SET 选项指定默认的数据库字符集。 COLLATE 选项指定默认的数据库排序规则。要查看可用的字符集和排序规则，请使用 SHOW CHARACTER SET 和 SHOW COLLATION 语句。

**示例：**
`create database d2 default charset 'utf8mb4';`

### 关于CREATE TABLE
语法：
```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    [(create_definition)]
    [table_options]
[partition_options]

CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name { LIKE old_tbl_name | (LIKE old_tbl_name) }

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
  | check_constraint_definition
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
      [check_constraint_definition]
}

key_part: {col_name [(length)] | (expr)} [ASC | DESC]

index_type:
USING {BTREE}

index_option: {
 index_type | COMMENT 'string'
}

[table_options]
table_option: {AUTO_INCREMENT [=] value
  | [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'string'
  | COMPRESSION [=] {'ZLIB' | 'LZ4' | 'NONE'}
  | KEY_BLOCK_SIZE [=] value
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
        [COMMENT [=] 'string']
        [(subpartition_definition [, subpartition_definition] ...)]

subpartition_definition:
    SUBPARTITION logical_name
        [[STORAGE] ENGINE [=] engine_name]
        [COMMENT [=] 'string']

```

CREATE TABLE 创建一个具有给定名称的表。 您必须具有该表的 CREATE 权限。
默认情况下，表是在默认数据库中创建的，使用 InnoDB 存储引擎。 如果表存在、没有默认数据库或数据库不存在，则会发生错误。
CREATE TABLE 语句有以下几个方面：
**表名**
- tbl_name
 	表名可以指定为 db_name.tbl_name 以在特定数据库中创建表。 假设数据库存在，无论是否存在默认数据库，这都有效。 如果使用带引号的标识符，请分别引用数据库和表名称。 例如，写`mydb`.`mytbl`，而不是`mydb.mytbl`。
- IF NOT EXISTS
 	如果表存在，则防止发生错误。 但是，没有验证现有表具有与 CREATE TABLE 语句指示的结构相同的结构。

**临时表**
创建表时可以使用 TEMPORARY 关键字。 TEMPORARY 表仅在当前会话中可见，并在会话关闭时自动删除。

**列数据类型和属性**
- data_type
data_type 表示列定义中的数据类型。 某些属性不适用于所有数据类型。 AUTO_INCREMENT 仅适用于整数和浮点类型。
- NOT NULL | NULL
如果既未指定 NULL 也未指定 NOT NULL，则将该列视为已指定 NULL。
- DEFAULT
指定列的默认值。 
如果启用了 NO_ZERO_DATE 或 NO_ZERO_IN_DATE SQL 模式并且日期值默认值根据该模式不正确，则 CREATE TABLE 在未启用严格 SQL 模式的情况下生成警告，如果启用了严格模式，则生成错误。 例如，启用 NO_ZERO_IN_DATE 后， c1 DATE DEFAULT '2010-00-00' 会产生警告。
- COMMENT
可以使用 COMMENT 选项指定列的注释，最长为 1024 个字符。 注释由 SHOW     CREATE TABLE 和 SHOW FULL COLUMNS 语句显示。

**表选项**
表选项用于优化表的行为。 在大多数情况下，您不必指定其中任何一个。 除非另有说明，否则这些选项适用于所有存储引擎。 不适用于给定存储引擎的选项可以作为表定义的一部分被接受和记住。 如果您稍后使用 ALTER TABLE 将表转换为使用不同的存储引擎，则此类选项将适用。
- ENGINE
请使用innodb存储引擎。
- [DEFAULT] CHARACTER SET
指定表的默认字符集。 CHARSET 是CHARACTER SET的同义词 。 如果字符集名称是 DEFAULT ，则使用数据库字符集。
- [DEFAULT] COLLATE
指定表的默认排序规则。
- COMMENT
该表的注释，最多2048个字符。 
- COMPRESSION
用于 InnoDB 表的页面级压缩的压缩算法。 支持的值包括 Zlib、LZ4 和 None。 COMPRESSION 属性是在透明    页面压缩功能中引入的。 页面压缩仅支持驻留在 file-per-table 表空间中的 InnoDB 表，并且仅在支持稀疏文件 的Linux系统使用。
- KEY_BLOCK_SIZE
对于 InnoDB 表，KEY_BLOCK_SIZE 指定用于压缩 InnoDB 表的页面大小（以千字节为单位）。KEY_BLOCK_SIZE 值被视为提示； 如有必要，InnoDB 可以使用不同的大小。 KEY_BLOCK_SIZE 只能小 于或等于 innodb_page_size 值。 值 0 表示默认压缩页面大小，它是 innodb_page_size 值的一半。 根据 innodb_page_size，可能的 KEY_BLOCK_SIZE 值包括 0、1、2、4、8 和 16。
建议在为 InnoDB 表指定 KEY_BLOCK_SIZE 时启用 innodb_strict_mode。 启用 innodb_strict_mode 时，指定无效的 KEY_BLOCK_SIZE 值会返回错误。 如果禁用 innodb_strict_mode，无效的 KEY_BLOCK_SIZE 值会导致警告，并且忽略 KEY_BLOCK_SIZE 选项。
InnoDB 仅在表级别支持 KEY_BLOCK_SIZE。
KEY_BLOCK_SIZE 不支持 32KB 和 64KB innodb_page_size 值。
InnoDB 表压缩不支持这些页面大小。
InnoDB 在创建临时表时不支持 KEY_BLOCK_SIZE 选项。
- ROW_FORMAT
定义存储行的物理格式。
创建禁用严格模式的表时，如果不支持指定的行格式，则使用存储引擎的默认行格式。 表的实际行格式在 Row_format 列中报告，以响应 SHOW TABLE STATUS。 create_options 列显示在 CREATE TABLE 语句中指定的行格式，SHOW CREATE TABLE 也是如此。
行格式选择因用于表的存储引擎而异。
 	对于 InnoDB 表：
	- 默认行格式由 innodb_default_row_format 定义，其默认设置为 DYNAMIC。 当未定义 ROW_FORMAT 选项或使用 ROW_FORMAT=DEFAULT 时，将使用默认行格式。如果未定义 ROW_FORMAT 选项，或者使用 ROW_FORMAT=DEFAULT，则重建表的操作也会静 默地将表的行格式更改为 innodb_default_row_format 定义的默认值。 
	- 为了更有效地 InnoDB 存储数据类型，请使用 DYNAMIC 。
	- 要为 InnoDB 表启用压缩，请指定 ROW_FORMAT=COMPRESSED。 创建临时表时不支持ROW_FORMAT=COMPRESSED 选项。
	- 当您指定非默认 ROW_FORMAT 子句时，请考虑启用 innodb_strict_mode 配置选项。
	- 不支持 ROW_FORMAT=FIXED。 如果在禁用 innodb_strict_mode 时指定了 ROW_FORMAT=FIXED，InnoDB 会发出警告并假定 ROW_FORMAT=DYNAMIC。 如果在启用 innodb_strict_mode 时指定 ROW_FORMAT=FIXED，这是默认设置，InnoDB 将返回错误。
- STATS_AUTO_RECALC
指定是否自动重新计算 InnoDB 表的持久统计信息。 值 DEFAULT 导致表的持久统计设置由 innodb_stats_auto_recalc 配置选项确定。 当表中 10% 的数据发生更改时，值 1 会导致重新计算统计信息。 值 0 阻止自动重新计算此表； 使用此设置，在对表进行实质性更改后，发出 ANALYZE TABLE 语句以重新计算统计信息。 
- STATS_PERSISTENT
指定是否为 InnoDB 表启用持久统计。 值 DEFAULT 导致表的持久统计设置由 innodb_stats_persistent 配置选项确定。 值 1 启用表的持久统计信息，而值 0 关闭此功能。 通过 CREATE TABLE 或 ALTER TABLE 语句启用持久统计后，在将代表性数据加载到表中后，发出 ANALYZE TABLE 语句来计算统计信息。
- STATS_SAMPLE_PAGES
估计索引列的基数和其他统计信息时要采样的索引页数，例如由 ANALYZE TABLE 计算的那些。

**表分区**
partition_options 可用于控制使用 CREATE TABLE 创建的表的分区。 
可以修改、合并、添加到表中以及从表中删除分区。 
- PARTITION BY
如果使用，则 partition_options 子句以 PARTITION BY 开头。 该子句包含用于确定分区的函数； 该函数返回一个从 1 到 num 的整数值，其中 num 是分区数。 （一个表可以包含的用户定义分区的最大数量是 1024；子分区的数量包括在这个最大值中。）
- RANGE(*expr*)
在这种情况下， expr 使用一组 VALUES LESS THAN 运算符显示一系列值。 使用范围分区时，您必须使用 VALUES LESS THAN 定义至少一个分区。 您不能将 VALUES IN 与范围分区一起使用。
>!
对于按 RANGE 分区的表，VALUES LESS THAN 必须与整数文字值或计算结果为单个整数值的表达式一起使用。 在 TDSQL中，您可以在使用 PARTITION BY RANGE COLUMNS 定义的表中克服此限制。

假设您有一个表，您希望根据以下方案在包含年份值的列上进行分区。

|Partition Number: | Years Range: |
|---------|---------|
|0|1990 and earlier|
|1|1991 to 1994|
|2|1995 to 1998|
|3|1999 to 2002|
|4|2003 to 2005|
|5|2006 and later|

实现这种分区方案的表可以通过此处显示的 CREATE TABLE 语句实现，示例如下：

```
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (
    year_col  INT primary key,
    some_data INT
)
PARTITION BY RANGE (year_col) (
    PARTITION p0 VALUES LESS THAN (1991),
    PARTITION p1 VALUES LESS THAN (1995),
    PARTITION p2 VALUES LESS THAN (1999),
    PARTITION p3 VALUES LESS THAN (2002),
    PARTITION p4 VALUES LESS THAN (2006),
    PARTITION p5 VALUES LESS THAN MAXVALUE
);

```


VALUES LESS THAN 子句以类似于 switch ... case 块的 case 部分的方式顺序工作（在许多编程语言中都可以找到，例如 C、Java 和 PHP）。 也就是说，子句必须以这样一种方式排列，即每个连续 VALUES LESS THAN 中指定的上限大于前一个的上限，引用 MAXVALUE 的一个在列表中排在最后。
- RANGE COLUMNS(*column_list*)
RANGE 上的此变体有助于对使用多列范围条件的查询进行分区修剪（即具有 WHERE a = 1 AND b < 10 或 WHERE a = 1 AND b = 10 AND c < 10 等条件）。 它使您能够通过使用 COLUMNS 子句中的列列表和每个 PARTITION ... VALUES LESS THAN (value_list) 分区定义子句中的一组列值来指定多列中的值范围。 （在最简单的情况下，该集合由单个列组成。） column_list 和 value_list 中可以引用的最大列数为 16。
COLUMNS 子句中使用的 column_list 可能只包含列名； 列表中的每一列必须是以下 TDSQL 数据类型之一：整数类型； 字符串类型； 和时间或日期列类型。 不允许使用 BLOB、TEXT、SET、ENUM、BIT 或空间数据类型的列； 也不允许使用浮点数类型的列。 您也不能在 COLUMNS 子句中使用函数或算术表达式。
分区定义中使用的 VALUES LESS THAN 子句必须为出现在 COLUMNS() 子句中的每一列指定一个文字值； 也就是说，用于每个 VALUES LESS THAN 子句的值列表必须包含与 COLUMNS 子句中列出的列数相同的值。 尝试在 VALUES LESS THAN 子句中使用比 COLUMNS 子句中更多或更少的值会导致语句失败并显示错误 Inconsistency in usage of column lists for partitioning.... 您不能对出现在中的任何值使用 NULL 值小于。 对于第一列以外的给定列，可以多次使用 MAXVALUE，如下例所示：
```
DROP TABLE IF EXISTS rc;
CREATE TABLE rc (
    a INT NOT NULL,
    b INT NOT NULL,
primary key (a,b)
)
PARTITION BY RANGE COLUMNS(a,b) (
    PARTITION p0 VALUES LESS THAN (10,5),
    PARTITION p1 VALUES LESS THAN (20,10),
    PARTITION p2 VALUES LESS THAN (50,MAXVALUE),
    PARTITION p3 VALUES LESS THAN (65,MAXVALUE),
    PARTITION p4 VALUES LESS THAN (MAXVALUE,MAXVALUE)
);

```
>!VALUES LESS THAN 值列表中使用的每个值必须与相应列的类型完全匹配； 不进行转换。 例如，不能将字符串 '1' 用于匹配使用整数类型的列的值（必须使用数字 1 代替），也不能将数字 1 用于匹配使用整数类型的列的值。 字符串类型（在这种情况下，您必须使用带引号的字符串：'1'）
- LIST(*expr*)
这在基于具有一组受限可能值（例如州或国家/地区代码）的表列分配分区时非常有用。 在这种情况下，可以将属于某个州或国家的所有行分配给单个分区，或者可以为某个州或国家的集合保留一个分区。 它类似于 RANGE，不同之处在于只能使用 VALUES IN 来指定每个分区的允许值。
VALUES IN 与要匹配的值列表一起使用。 例如，您可以创建一个分区方案，如下所示：
```
DROP TABLE IF EXISTS client_firms;
CREATE TABLE client_firms (
    id   INT primary key,
    name VARCHAR(35)
)
PARTITION BY LIST (id) (
    PARTITION r0 VALUES IN (1, 5, 9, 13, 17, 21),
    PARTITION r1 VALUES IN (2, 6, 10, 14, 18, 22),
    PARTITION r2 VALUES IN (3, 7, 11, 15, 19, 23),
    PARTITION r3 VALUES IN (4, 8, 12, 16, 20, 24)
);

```
>!使用列表分区时，您必须至少使用 VALUES IN 定义一个分区。 您不能将 VALUES LESS THAN 与 PARTITION BY LIST 一起使用。
- LIST COLUMNS(*column_list*)
LIST 上的这个变体有助于使用多列上的比较条件（即具有 WHERE a = 5 AND b = 5 或 WHERE a = 1 AND b = 10 AND c = 5 等条件）的查询的分区修剪。它使您能够通过使用 COLUMNS 子句中的列列表和每个 PARTITION ... VALUES IN (value_list) 分区定义子句中的一组列值来指定多列中的值。
LIST COLUMNS(column_list) 中使用的列列表和 VALUES IN(value_list) 中使用的值列表的数据类型规则与 RANGE COLUMNS(column_list) 中使用的列列表和值列表中使用的规则相同VALUES LESS THAN(value_list)，除了在 VALUES IN 子句中不允许使用 MAXVALUE，您可以使用 NULL。
用于 VALUES IN 和 PARTITION BY LIST COLUMNS 的值列表与用于 PARTITION BY LIST 的值列表之间有一个重要区别。当与 PARTITION BY LIST COLUMNS 一起使用时，VALUES IN 子句中的每个元素都必须是一组列值；每个集合中的值数必须与 COLUMNS 子句中使用的列数相同，并且这些值的数据类型必须与列的数据类型匹配（并以相同的顺序出现）。在最简单的情况下，该集合由单个列组成。 column_list 和组成 value_list 的元素中可使用的最大列数为 16。
以下 CREATE TABLE 语句定义的表提供了一个使用 LIST COLUMNS 分区的表示例：
```
DROP TABLE IF EXISTS lc;
CREATE TABLE lc (
    a INT not NULL,
    b INT not NULL,
primary key(a,b)
)
PARTITION BY LIST COLUMNS(a,b) (
    PARTITION p0 VALUES IN( (0,0) ),
    PARTITION p1 VALUES IN( (0,1), (0,2), (0,3), (1,1), (1,2) ),
    PARTITION p2 VALUES IN( (1,0), (2,0), (2,1), (3,0), (3,1) ),
    PARTITION p3 VALUES IN( (1,3), (2,2), (2,3), (3,2), (3,3) )
);
```
>!无论您在创建按 RANGE 或 LIST 分区的表时是否使用 PARTITIONS 子句，您仍然必须在表定义中至少包含一个 PARTITION VALUES 子句。

#### CREATE TEMPORARY TABLE语法
创建表时可以使用 TEMPORARY 关键字。 TEMPORARY 表仅在当前会话中可见，并在会话关闭时自动删除。这意味着两个不同的会话可以使用相同的临时表名称，而不会相互冲突或与现有的同名非临时表发生冲突。 （现有表是隐藏的，直到临时表被删除。）
InnoDB 不支持压缩临时表。当启用 innodb_strict_mode 时（默认值），如果指定了 ROW_FORMAT=COMPRESSED 或 KEY_BLOCK_SIZE，CREATE TEMPORARY TABLE 将返回错误。如果禁用 innodb_strict_mode，则会发出警告并使用非压缩行格式创建临时表。 innodb_file_per-table 选项不影响 InnoDB 临时表的创建。
CREATE TABLE 导致隐式提交，除非与 TEMPORARY 关键字一起使用。
TEMPORARY 表与数据库（模式）的关系非常松散。删除数据库不会自动删除在该数据库中创建的任何 TEMPORARY 表。
要创建临时表，您必须具有 CREATE TEMPORARY TABLES 权限。会话创建临时表后，服务器不会对该表执行进一步的权限检查。创建会话可以对表执行任何操作，例如 DROP TABLE、INSERT、UPDATE 或 SELECT。
这种行为的一个含义是会话可以操作其临时表，即使当前用户没有创建它们的权限。假设当前用户没有 CREATE TEMPORARY TABLES 权限，但能够执行定义者上下文存储过程，该存储过程以拥有 CREATE TEMPORARY TABLES 的用户的权限执行并创建临时表。当过程执行时，会话使用定义用户的权限。过程返回后，有效权限恢复为当前用户的有效权限，该用户仍然可以看到临时表并对其进行任何操作。
您不能使用 CREATE TEMPORARY TABLE ... LIKE 根据驻留在表空间、InnoDB 系统表空间 (innodb_system) 或通用表空间中的表的定义创建空表。此类表的表空间定义包含一个 TABLESPACE 属性，该属性定义了该表所在的表空间，上述表空间不支持临时表。要根据此类表的定义创建临时表，请改用以下语法：
`CREATE TEMPORARY TABLE new_tbl(id int primary key);`
CREATE TABLE ... LIKE语法
使用 CREATE TABLE ... LIKE 根据另一个表的定义创建一个空表，包括原始表中定义的任何列属性和索引，示例：

```
drop table if exists t1;
drop table if exists test2;
create table t1 (id int primary key);
create table test2 like t1;

```
副本是使用与原始表相同版本的表存储格式创建的。 原始表需要 SELECT 权限。
LIKE 仅适用于基表，不适用于视图。
>?当 LOCK TABLES 语句有效时，您不能执行 CREATE TABLE 或 CREATE TABLE ... LIKE。
CREATE TABLE ... LIKE 进行与 CREATE TABLE 相同的检查。 这意味着如果当前的 SQL 模式与创建原始表时生效的模式不同，则表定义可能被认为对新模式无效并导致语句失败。
- 对于 CREATE TABLE ... LIKE，目标表保留原始表中生成的列信息。
- 对于 CREATE TABLE ... LIKE，目标表保留原始表中的表达式默认值。
- 对于 CREATE TABLE ... LIKE，目标表保留原始表中的 CHECK 约束，除了生成所有约束名称。
- 如果原始表是 TEMPORARY 表，则 CREATE TABLE ... LIKE 不会保留 TEMPORARY。要创建临时目标表，请使用 CREATE TEMPORARY TABLE ... LIKE。

### 创建普通表
**示例：**
```
DROP TABLE IF EXISTS t_stu;
CREATE TABLE t_stu (stu_id int primary key,first_name VARCHAR(10),last_name VARCHAR(10),full_name VARCHAR(255)) ENGINE=InnoDB default charset=utf8mb4;

```
### 创建分区表
#### 支持的分区表类型
TDSQL支持RANGE、LIST、COLUMNS类型的分区。
- RANGE 分区：这种类型的分区基于落在给定范围内的列值将行分配给分区。此类型还包含一种扩展类型为RANGE COLUMNS的分区类型。
Range分区支持类型：
	- DATE，DATETIME，TIMESTAMP
	- TINYINT, SMALLINT, MEDIUMINT, INT , BIGINT
- LIST 分区：类似于按RANGE分区，区别在于LIST分区是基于列值匹配一个离散值集合中的某个值来进行选择。此类型包含一种扩展类型为LIST COLUMNS的分区类型。
 List分区支持类型：
	- DATE，DATETIME，TIMESTAMP
	- TINYINT, SMALLINT, MEDIUMINT, INT , BIGINT
- COLUMN分区：RANGE 和 LIST 分区的扩展类型，分为RANGE COLUMNS和LIST COLUMNS两类。COLUMNS 分区允许在分区键中使用多个列，所有指定列都被考虑在内，以便在分区中放置行，以及确定在分区裁剪中检查分区的匹配行。RANGE COLUMNS 分区和 LIST COLUMNS 分区都支持使用非整数列来定义值范围或列表成员。
 COLUMN分区支持类型：
	- DATE，DATETIME
	- TINYINT, SMALLINT, MEDIUMINT, INT , BIGINT
	- CHAR, VARCHAR

#### RANGE分区
Range分区表示例：

```
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id INT NOT NULL,
    fname VARCHAR(30),
    lname VARCHAR(30),
    hired DATE NOT NULL DEFAULT '1970-01-01',
    separated DATE NOT NULL DEFAULT '9999-12-31',
    job_code INT NOT NULL,
    store_id INT NOT NULL PRIMARY KEY
) PARTITION BY RANGE (store_id) (
PARTITION p0 VALUES LESS THAN (6), 
PARTITION p1 VALUES LESS THAN (11), 
PARTITION p2 VALUES LESS THAN (16), 
PARTITION p3 VALUES LESS THAN (21));
```

RANGE分区适用场景：
- 当需要删除旧的数据时。有了分区，只需要执行alter table employees drop partition p0;就能删除以上employees表中store_id<6的所有数据，这样比delete from employees where store_id<6;要有效得多。
- 想要使用一个包含有日期或时间值，或包含有从一些其他级数开始增长的值的列
- 经常运行直接依赖于用于分割表的列的查询。例如，当执行一个如“SELECT COUNT(*) FROM employees WHERE store_id=5 GROUP BY store_id；”这样的查询时，TDSQL可以很迅速地确定只有分区p0需要扫描，这是因为余下的分区不可能包含有符合该WHERE子句的任何记录


RANGE COLUMNS分区表示例：
范围列分区与范围分区类似，但是使您能够基于多个列值使用范围来定义分区。 另外，可以使用非整数类型的列来定义范围。

```
DROP TABLE IF EXISTS rcx;
CREATE TABLE rcx (
    a INT NOT NULL,
    b INT NOT NULL,
    c CHAR(3) NOT NULL,
    d INT NOT NULL,
    PRIMARY KEY (a, d, c)
) PARTITION BY RANGE COLUMNS (A, D, C) (
PARTITION p0 VALUES LESS THAN (5, 10, 'ggg'), 
PARTITION p1 VALUES LESS THAN (10, 20, 'mmm'), 
PARTITION p2 VALUES LESS THAN (15, 30, 'sss'), 
PARTITION p3 VALUES LESS THAN (MAXVALUE, MAXVALUE, MAXVALUE)
);

```

#### LIST分区
List分区表示例：
```
DROP TABLE IF EXISTS employees_list;
CREATE TABLE employees_list (
    id INT NOT NULL,
    fname VARCHAR(30),
    lname VARCHAR(30),
    hired DATE NOT NULL DEFAULT '1970-01-01',
    separated DATE NOT NULL DEFAULT '9999-12-31',
    job_code INT,
    store_id INT PRIMARY KEY
) PARTITION BY LIST (store_id) (
PARTITION pNorth VALUES IN (3 , 5 , 6 , 9 , 17) , 
PARTITION pEast VALUES IN (1 , 2 , 10 , 11 , 19 , 20) , 
PARTITION pWest VALUES IN (4 , 12 , 13 , 14 , 18) ,
 PARTITION pCentral VALUES IN (7 , 8 , 15 , 16));
```
LIST COLUMNS分区表示例：
```
DROP TABLE IF EXISTS customers_2;
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

### CREATE INDEX语法
通常，您在使用 CREATE TABLE 创建表本身时在表上创建所有索引。该准则对于 InnoDB 表尤其重要，其中主键决定了数据文件中行的物理布局。 CREATE INDEX 使您能够向现有表添加索引。
语法：
```
CREATE [UNIQUE ] INDEX index_name
    [index_type]
    ON tbl_name (key_part,...)
    [index_option]
    [algorithm_option | lock_option] ...

key_part: {col_name [(length)] | (expr)} [ASC | DESC]

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
- CREATE INDEX 不能用于创建 PRIMARY KEY.
	- 对于主键，请改用 ALTER TABLE。
	- 对于INNODB存储引擎，允许的索引类型为BTREE。

CREATE INDEX 映射到 ALTER TABLE 语句以创建索引。CREATE INDEX 不能用于创建 PRIMARY KEY；请改用 ALTER TABLE。
以下部分描述了 CREATE INDEX 语句的不同方面：
- 列前缀索引
- 功能键索引
- 唯一索引
- 多值索引
- 索引选项

**列前缀索引**
对于字符串列，可以创建仅使用列值的前导部分的索引，使用 col_name(length) 语法指定索引前缀长度：
- 可以为 CHAR、VARCHAR、BINARY 和 VARBINARY 键部分指定前缀。
- 前缀限制以字节为单位。 但是，CREATE TABLE、ALTER TABLE 和 CREATE INDEX 语句中索引规范的前缀长度被解释为非二进制字符串类型（CHAR、VARCHAR、TEXT）的字符数和二进制字符串类型（BINARY、VARBINARY、BLOB）的字节数 . 在为使用多字节字符集的非二进制字符串列指定前缀长度时，请考虑这一点。前缀支持和前缀长度（如果支持）取决于存储引擎。 例如，对于使用 REDUNDANT 或 COMPACT 行格式的 InnoDB 表，前缀最长可达 767 字节。 对于使用 DYNAMIC 或 COMPRESSED 行格式的 InnoDB 表，前缀长度限制为 3072 字节。 
如果指定的索引前缀超过最大列数据类型大小，则 CREATE INDEX 按如下方式处理索引：
- 对于非唯一索引，要么发生错误（如果启用了严格 SQL 模式），要么将索引长度减少到最大列数据类型大小并产生警告（如果未启用严格 SQL 模式）。
- 对于唯一索引，无论 SQL 模式如何，都会发生错误，因为减少索引长度可能会允许插入不满足指定唯一性要求的非唯一条目。
此处显示的语句使用 name 列的前 10 个字符创建索引（假设 name 具有非二进制字符串类型）：
`CREATE INDEX part_of_name ON customer (name(10));`
如果列中的名称通常在前 10 个字符中不同，则使用此索引执行的查找不应比使用从整个名称列创建的索引慢多少。 此外，为索引使用列前缀可以使索引文件更小，这可以节省大量磁盘空间，还可以加快 INSERT 操作。

**功能键索引**
“正常”索引索引列值或列值的前缀。 例如，在下表中，给定 t1 行的索引条目包括完整的 col1 值和由前 10 个字符组成的 col2 值的前缀：
```
DROP TABLE IF EXISTS t2;
CREATE TABLE t2 (col1 VARCHAR(10) primary key,col2 VARCHAR(20),INDEX(col1,col2(10)));

```
TDSQL支持索引表达式值而不是列或列前缀值的功能键部分。 使用功能关键部件可以对未直接存储在表中的值进行索引。 例子：
```
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (col1 INT primary key, col2 INT, INDEX func_index ((ABS(col1))));
CREATE INDEX idx1 ON t1 ((col1 + col2));
CREATE INDEX idx2 ON t1 ((col1 + col2), (col1 - col2), col1);
ALTER TABLE t1 ADD INDEX ((col1 * 40) DESC);

```
具有多个关键部分的索引可以混合非功能性和功能性关键部分。
功能关键部件支持 ASC 和 DESC。
功能关键部件必须遵守以下规则。 如果关键部分定义包含不允许的构造，则会发生错误。
- 在索引定义中，将表达式括在括号内以将它们与列或列前缀区分开来。 例如，这是允许的； 表达式括在括号中：
 	INDEX（（col1 + col2），（col3-col4））
 	这会产生错误； 表达式未括在括号内：
 	INDEX（col1 + col2，col3 - col4）
- 功能键部分不能仅由列名组成。 例如，这是不允许的：
 	INDEX（（col1），（col2））
 	相反，将关键部分写为非功能性关键部分，不带括号：
 	INDEX（col1，col2）
- 功能键部分表达式不能引用列前缀。

**唯一索引**
UNIQUE 索引创建了一个约束，使得索引中的所有值都必须是不同的。 如果您尝试添加具有与现有行匹配的键值的新行，则会发生错误。 如果为 UNIQUE 索引中的列指定前缀值，则列值在前缀长度内必须是唯一的。 UNIQUE 索引允许可以包含 NULL 的列有多个 NULL 值。
如果表的 PRIMARY KEY 或 UNIQUE NOT NULL 索引由具有整数类型的单个列组成，则可以使用 _rowid 来引用 SELECT 语句中的索引列，如下所示：
- 如果 PRIMARY KEY 由单个整数列组成，则 _rowid 指的是 PRIMARY KEY 列。 如果有一个 PRIMARY KEY 但它不包含单个整数列，则不能使用 _rowid。
- 否则，如果第一个 UNIQUE NOT NULL 索引包含单个整数列，则 _rowid 将引用该列。 如果第一个 UNIQUE NOT NULL 索引不包含单个整数列，则不能使用 _rowid。

**多值索引**
InnoDB 支持多值索引。 多值索引是在存储值数组的列上定义的二级索引。 “正常”索引对每个数据记录有一个索引记录 (1:1)。 多值索引可以为单个数据记录 (N:1) 包含多个索引记录。 多值索引用于索引 JSON 数组。 例如，在以下 JSON 文档中的邮政编码数组上定义的多值索引为每个邮政编码创建一个索引记录，每个索引记录引用相同的数据记录。
`{"user":"Bob", "user_id":31, "zipcode":[94477,94536]}`

**创建多值索引**
您可以在 CREATE TABLE、ALTER TABLE 或 CREATE INDEX 语句中创建多值索引。 这SQL 数据类型数组。 然后使用 SQL 数据类型数组中的值透明地生成一个虚拟列； 最后，在虚拟列上创建功能索引（也称为虚拟索引）。 它是在形成多值索引的 SQL 数据类型数组的虚拟值列上定义的功能索引。
以下列表中的示例显示了在名为 customers 的表中的 JSON 列 custinfo 上的数组 $.zipcode 上创建多值索引 zip 的三种不同方式。 在每种情况下，JSON 数组都被转换为 UNSIGNED 整数值的 SQL 数据类型数组。
CREATE TABLE only:
```
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    	id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    	modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    	custinfo JSON,
    	INDEX zips((CAST(custinfo->'$.zipcode' AS UNSIGNED ARRAY)) )
    	);

```
CREATE TABLE plus CREATE INDEX:
```
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    	id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    	modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    	custinfo JSON
    	);

CREATE INDEX zips ON customers ((CAST(custinfo->'$.zipcode' AS UNSIGNED ARRAY)));

```
>!
复合索引中只能使用一个多值键部分。 多值键部分可以相对于键的其他部分以任何顺序使用。 换句话说，刚刚显示的 ALTER TABLE 语句可以使用 comp(id, (CAST(custinfo->'$.zipcode' AS UNSIGNED ARRAY), modified)) （或任何其他排序）并且仍然有效。

使用多值索引
当在 WHERE 子句中指定以下函数时，优化器使用多值索引来获取记录：
- MEMBER OF()
- JSON_CONTAINS()
- JSON_OVERLAPS()
我们可以通过使用以下 CREATE TABLE 和 INSERT 语句创建和填充客户表来证明这一点：

```
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
         id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
         modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
         custinfo JSON
         );

INSERT INTO customers VALUES
         (NULL, NOW(), '{"user":"Jack","user_id":37,"zipcode":[94582,94536]}'),
         (NULL, NOW(), '{"user":"Jill","user_id":22,"zipcode":[94568,94507,94582]}'),
         (NULL, NOW(), '{"user":"Bob","user_id":31,"zipcode":[94477,94507]}'),
         (NULL, NOW(), '{"user":"Mary","user_id":72,"zipcode":[94536]}'),
         (NULL, NOW(), '{"user":"Ted","user_id":56,"zipcode":[94507,94582]}');

```
首先，我们在客户表上执行三个查询，每个查询使用 MEMBER OF()、JSON_CONTAINS() 和 JSON_OVERLAPS()，每个查询的结果如下所示：

```
mysql> SELECT * FROM customers
    	     WHERE 94507 MEMBER OF(custinfo->'$.zipcode');
+----+---------------------+-------------------------------------------------------------------+
| id | modified            | custinfo                                                          |
+----+---------------------+-------------------------------------------------------------------+
|  2 | 2019-06-29 22:23:12 | {"user": "Jill", "user_id": 22, "zipcode": [94568, 94507, 94582]} |
|  3 | 2019-06-29 22:23:12 | {"user": "Bob", "user_id": 31, "zipcode": [94477, 94507]}         |
|  5 | 2019-06-29 22:23:12 | {"user": "Ted", "user_id": 56, "zipcode": [94507, 94582]}         |
+----+---------------------+-------------------------------------------------------------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM customers
         WHERE JSON_CONTAINS(custinfo->'$.zipcode', CAST('[94507,94582]' AS JSON));
+----+---------------------+-------------------------------------------------------------------+
| id | modified            | custinfo                                                          |
+----+---------------------+-------------------------------------------------------------------+
|  2 | 2019-06-29 22:23:12 | {"user": "Jill", "user_id": 22, "zipcode": [94568, 94507, 94582]} |
|  5 | 2019-06-29 22:23:12 | {"user": "Ted", "user_id": 56, "zipcode": [94507, 94582]}         |
+----+---------------------+-------------------------------------------------------------------+
2 rows in set (0.00 sec)

mysql> SELECT * FROM customers
         WHERE JSON_OVERLAPS(custinfo->'$.zipcode', CAST('[94507,94582]' AS JSON));
+----+---------------------+-------------------------------------------------------------------+
| id | modified            | custinfo                                                          |
+----+---------------------+-------------------------------------------------------------------+
|  1 | 2019-06-29 22:23:12 | {"user": "Jack", "user_id": 37, "zipcode": [94582, 94536]}        |
|  2 | 2019-06-29 22:23:12 | {"user": "Jill", "user_id": 22, "zipcode": [94568, 94507, 94582]} |
|  3 | 2019-06-29 22:23:12 | {"user": "Bob", "user_id": 31, "zipcode": [94477, 94507]}         |
|  5 | 2019-06-29 22:23:12 | {"user": "Ted", "user_id": 56, "zipcode": [94507, 94582]}         |
+----+---------------------+-------------------------------------------------------------------+
4 rows in set (0.00 sec)

```
接下来，我们对前三个查询中的每一个运行 EXPLAIN：

```
mysql> EXPLAIN SELECT * FROM customers
    	     WHERE 94507 MEMBER OF(custinfo->'$.zipcode');
+----+-------------+-----------+------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table     | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+-----------+------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | customers | NULL       | ALL  | NULL          | NULL | NULL    | NULL |    5 |   100.00 | Using where |
+----+-------------+-----------+------------+------+---------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)

mysql> EXPLAIN SELECT * FROM customers
         WHERE JSON_CONTAINS(custinfo->'$.zipcode', CAST('[94507,94582]' AS JSON));
+----+-------------+-----------+------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table     | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+-----------+------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | customers | NULL       | ALL  | NULL          | NULL | NULL    | NULL |    5 |   100.00 | Using where |
+----+-------------+-----------+------------+------+---------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)

mysql> EXPLAIN SELECT * FROM customers
         WHERE JSON_OVERLAPS(custinfo->'$.zipcode', CAST('[94507,94582]' AS JSON));
+----+-------------+-----------+------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table     | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+-----------+------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | customers | NULL       | ALL  | NULL          | NULL | NULL    | NULL |    5 |   100.00 | Using where |
+----+-------------+-----------+------------+------+---------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.01 sec)

```
刚刚显示的三个查询都不能使用任何键。 为了解决这个问题，我们可以在 JSON 列 (custinfo) 中的邮政编码数组上添加一个多值索引，如下所示：

```
ALTER TABLE customers
    	     ADD INDEX zips((CAST(custinfo->'$.zipcode' AS UNSIGNED ARRAY)));

```
当我们再次运行之前的 EXPLAIN 语句时，我们现在可以观察到查询可以（并且确实）使用刚刚创建的索引 zip：

```
mysql> EXPLAIN SELECT * FROM customers
    	     WHERE 94507 MEMBER OF(custinfo->'$.zipcode');
+----+-------------+-----------+------------+------+---------------+------+---------+-------+------+----------+-------------+
| id | select_type | table     | partitions | type | possible_keys | key  | key_len | ref   | rows | filtered | Extra       |
+----+-------------+-----------+------------+------+---------------+------+---------+-------+------+----------+-------------+
|  1 | SIMPLE      | customers | NULL       | ref  | zips          | zips | 9       | const |    1 |   100.00 | Using where |
+----+-------------+-----------+------------+------+---------------+------+---------+-------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)

mysql> EXPLAIN SELECT * FROM customers
         WHERE JSON_CONTAINS(custinfo->'$.zipcode', CAST('[94507,94582]' AS JSON));
+----+-------------+-----------+------------+-------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table     | partitions | type  | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+-----------+------------+-------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | customers | NULL       | range | zips          | zips | 9       | NULL |    6 |   100.00 | Using where |
+----+-------------+-----------+------------+-------+---------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)

mysql> EXPLAIN SELECT * FROM customers
         WHERE JSON_OVERLAPS(custinfo->'$.zipcode', CAST('[94507,94582]' AS JSON));
+----+-------------+-----------+------------+-------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table     | partitions | type  | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+-----------+------------+-------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | customers | NULL       | range | zips          | zips | 9       | NULL |    6 |   100.00 | Using where |
+----+-------------+-----------+------------+-------+---------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.01 sec)

```
多值索引可以定义为唯一键。 如果定义为唯一键，则尝试插入多值索引中已存在的值会返回重复键错误。 如果已存在重复值，则尝试添加唯一的多值索引会失败，如下所示：

```
MySQL [test]> ALTER TABLE customers DROP INDEX zips;
Query OK, 0 rows affected (0.03 sec)
Records: 0  Duplicates: 0  Warnings: 0

MySQL [test]> ALTER TABLE customers
              ADD UNIQUE INDEX zips((CAST(custinfo->'$.zipcode' AS UNSIGNED ARRAY)));
ERROR 1062 (23000): Duplicate entry '[94507, ' for key 'zips'

MySQL [test]> ALTER TABLE customers
              ADD INDEX zips((CAST(custinfo->'$.zipcode' AS UNSIGNED ARRAY)));
Query OK, 0 rows affected (0.03 sec)
Records: 0  Duplicates: 0  Warnings: 0

```

**索引选项**
index_option 值可以是以下任何值：
- KEY_BLOCK_SIZE [=] *value*
InnoDB 表的索引级别不支持 KEY_BLOCK_SIZE
- index_type
某些存储引擎允许您在创建索引时指定索引类型。
Innodb存储引擎支持的index_type为BTREE 。例如：
```
DROP TABLE IF EXISTS lookup;
CREATE TABLE lookup (id INT primary key) ENGINE = INNODB;
CREATE INDEX id_index ON lookup (id) USING BTREE;
```


## ALTER
### ALTER TABLE
语法：
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
  | REORGANIZE PARTITION partition_names INTO (partition_definitions)
  | EXCHANGE PARTITION partition_name WITH TABLE tbl_name [{WITH | WITHOUT} VALIDATION]
  | ANALYZE PARTITION {partition_names | ALL}
  | CHECK PARTITION {partition_names | ALL}
  | REBUILD PARTITION {partition_names | ALL}
  | REPAIR PARTITION {partition_names | ALL}
  | REMOVE PARTITIONING
}
 
key_part: {col_name [(length)] | | (expr)} [ASC | DESC]
 
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
  | STATS_SAMPLE_PAGES [=]
```
ALTER TABLE 更改表的结构。 例如，您可以添加或删除列、创建或销毁索引、更改现有列的类型或重命名列或表本身。 您还可以更改特征，例如用于表或表注释的存储引擎。
- 要使用 ALTER TABLE ，你需要 ALTER ， CREATE 和 INSERT 权限。 
- 在表名后面，指定要进行的更改。 如果没有给出， ALTER TABLE 什么都不做。
- COLUMN 一词是可选的，可以省略，但 RENAME COLUMN 除外（用于区分列重命名操作和 RENAME 表重命名操作）。
- 该字 COLUMN 是可选的，可以省略，除了 RENAME COLUMN （区分列重命名操作和 RENAME 表重命名操作）。
 
ALTER TABLE 语句 还有其他几个方面 ，本节中的以下主题对此进行了描述：
- 表选项
- 性能和空间要求
- 并发控制
- 添加和删除列
- 重命名，重新定义和重新排序列
- 主键和索引
- 更改字符集
- 分区选项

**表选项**
table_options 表示可在 CREATE TABLE 语句中使用的表选项，例如 ENGINE、AUTO_INCREMENT。
将表选项与 ALTER TABLE 一起使用提供了一种更改单个表特征的便捷方式。 例如：
如果 t1 当前不是 InnoDB 表，则此语句将其存储引擎更改为 InnoDB ：
```
ALTER TABLE t1 ENGINE = InnoDB;
```
- 指定 ENGINE 子句时， ALTER TABLE 重建表。 即使表已具有指定的存储引擎，也是如此。
- 在现有 InnoDB 表上运行 ALTER TABLE tbl_name ENGINE=INNODB 会执行“NULL”ALTER TABLE 操作，该操作可用于对 InnoDB 表进行碎片整理。在 InnoDB 表上运行 ALTER TABLE tbl_name FORCE 执行相同的功能.
- 尝试更改表的存储引擎的结果受所需存储引擎是否可用以及 NO_ENGINE_SUBSTITUTION SQL 模式设置的影响
- 要更改 InnoDB 表以使用压缩行存储格式：
```
ALTER TABLE t1 ROW_FORMAT = COMPRESSED;
```
- 要重置当前的自动增量值：
```
ALTER TABLE t1 AUTO_INCREMENT = 13;
```
>!您无法将计数器重置为小于或等于当前正在使用的值的值。 对于 InnoDB，如果该值小于或等于 AUTO_INCREMENT 列中当前的最大值，则将该值重置为当前最大 AUTO_INCREMENT 列值加1。

- 要更改默认表格字符集：
```
ALTER TABLE t1 CHARACTER SET = utf8mb4;
```
- 添加（或更改）表注释：
```
ALTER TABLE t1 COMMENT = 'New table comment';
```
要验证表选项是否按预期更改，请使用 SHOW CREATE TABLE 或查询 INFORMATION_SCHEMA.TABLES。

**性能和空间要求**
ALTER TABLE 使用以下算法之一处理操作：
- COPY ：对原表的一个副本进行操作，将表数据从原表逐行复制到新表中。 不允许并发 DML。
- INPLACE ：操作避免复制表数据，但可能会就地重建表。 在操作的准备和执行阶段可能会短暂地对表进行独占元数据锁定。 通常，支持并发 DML
- INSTANT ：操作只修改数据字典中的元数据。 在准备和执行过程中不对表采取独占元数据锁，表数据不受影响，操作瞬间完成。 允许并发 DML。

ALGORITHM 子句是可选的。 如果省略 ALGORITHM 子句，TDSQL 将 ALGORITHM=INSTANT 用于存储引擎和支持它的 ALTER TABLE 子句。 否则，使用 ALGORITHM=INPLACE。 如果不支持 ALGORITHM=INPLACE，则使用ALGORITHM=COPY。 

**并发控制**
对于支持它的 ALTER TABLE 操作，您可以使用 LOCK 子句来控制表被更改时并发读取和写入的级别。 为该子句指定非默认值使您能够在更改操作期间要求一定数量的并发访问或独占性，并在请求的锁定程度不可用时停止操作。
对于使用 ALGORITHM=INSTANT 的操作，只允许 LOCK = DEFAULT。 其他 LOCK 子句参数不适用。
LOCK 子句的参数是：
- LOCK = DEFAULT
给定 ALGORITHM 子句（如果有）和 ALTER TABLE 操作的最大并发级别：如果支持，则允许并发读取和写入。 如果没有，则允许并发读取（如果支持）。 如果不是，则强制执行独占访问。
- LOCK = NONE
如果支持，则允许并发读取和写入。 否则，会发生错误。
- LOCK = SHARED
如果支持，则允许并发读取但阻止写入。 即使存储引擎支持给定 ALGORITHM 子句（如果有）和 ALTER TABLE 操作的并发写入，写入也会被阻止。 如果不支持并发读取，则会发生错误。
- LOCK = EXCLUSIVE
强制独占访问。 即使存储引擎支持给定 ALGORITHM 子句（如果有）和 ALTER TABLE 操作的并发读/写，也会这样做。

**添加和删除列**
使用 ADD 向表添加新列，使用 DROP 删除现有列。 
要在表行内的特定位置添加列，请使用 FIRST 或 AFTER col_name。 默认是最后添加列。
如果一个表只包含一列，则不能删除该列。 如果您打算删除该表，请改用 DROP TABLE 语句。
如果从表中删除列，列也会从它们所属的任何索引中删除。 如果构成索引的所有列都被删除，则该索引也会被删除。 如果您使用 CHANGE 或 MODIFY 缩短列上存在索引的列，并且生成的列长度小于索引长度，TDSQL会自动缩短索引。
对于 ALTER TABLE ... ADD，如果列具有使用非确定性函数的表达式默认值，则该语句可能会产生警告或错误。 

**重命名，重新定义和重新排序列**
CHANGE、MODIFY、RENAME COLUMN 和 ALTER 子句允许更改现有列的名称和定义。 它们具有以下比较特征：
- CHANGE ：
	- 可以重命名列并更改其定义，或两者兼而有之。
	- 比 MODIFY 或 RENAME COLUMN 具有更多功能，但牺牲了某些操作的便利性。 CHANGE 如果不重命名列，则需要对其命名两次，如果仅重命名，则需要重新指定列定义。
	- 使用 FIRST 或 AFTER，可以对列重新排序。
- MODIFY ：
	- 可以更改列定义但不能更改其名称。
	- 比 CHANGE 更方便地重命名列而不更改其定义。
	- 使用 FIRST 或 AFTER，可以对列重新排序。
- RENAME COLUMN ：
	- 可以更改列名但不能更改其定义。
	- 比 CHANGE 更方便地重命名列而不更改其定义。
- ALTER ：仅用于更改列默认值。
要更改列以更改其名称和定义，请使用 CHANGE，指定旧名称和新名称以及新定义。 例如，要将 INT NOT NULL 列从 a 重命名为 b 并将其定义更改为使用 BIGINT 数据类型同时保留 NOT NULL 属性，请执行以下操作：
```
DROP TABLE IF EXISTS t1;
create table t1(a int primary key,c int,d int,e int);
ALTER TABLE t1 CHANGE a b BIGINT NOT NULL;
```
要更改列定义但不更改其名称，请使用 CHANGE 或 MODIFY。 对于 CHANGE，语法需要两个列名，因此您必须两次指定相同的名称以保持名称不变。 例如，要更改 b 列的定义，请执行以下操作：
```
DROP TABLE IF EXISTS t1;
create table t1(a int primary key,b int,d int,c int);
ALTER TABLE t1 CHANGE b b INT NOT NULL;
```
MODIFY 更方便地更改定义而不更改名称，因为它只需要列名一次：
```
ALTER TABLE t1 MODIFY b INT NOT NULL;
```
要更改列名称但不更改其定义，请使用 CHANGE 或 RENAME COLUMN。 对于 CHANGE，语法需要列定义，因此要保持定义不变，您必须重新指定列当前具有的定义。 例如，要将 INT NOT NULL 列从 b 重命名为 a，请执行以下操作：
```
DROP TABLE IF EXISTS t1;
create table t1(b int primary key,c int,d int,e int);
ALTER TABLE t1 CHANGE b a INT NOT NULL;
```
RENAME COLUMN 更改名称而不更改定义更方便，因为它只需要旧名称和新名称：
```
DROP TABLE IF EXISTS t1;
create table t1(b int primary key,c int,d int,e int);
ALTER TABLE t1 RENAME COLUMN b TO a;
```
对于使用 CHANGE 或 MODIFY 的列定义更改，定义必须包括数据类型和所有应应用于新列的属性，除了索引属性（如 PRIMARY KEY 或 UNIQUE）。 原始定义中存在但未为新定义指定的属性不会被继承。 假设列 col1 被定义为 INT UNSIGNED DEFAULT 1 COMMENT 'my column' 并且您按如下方式修改该列，打算仅将 INT 更改为 BIGINT：
```
DROP TABLE IF EXISTS t1;
create table t1(col1 int primary key,col2 int,col3 int,col4 int);
ALTER TABLE t1 MODIFY col1 BIGINT;
```
该语句将数据类型从 INT 更改为 BIGINT，但也会删除 UNSIGNED、DEFAULT 和 COMMENT 属性。 要保留它们，语句必须明确包含它们：
```
ALTER TABLE t1 MODIFY col1 BIGINT UNSIGNED DEFAULT 1 COMMENT'my column';
```
对于使用 CHANGE 或 MODIFY 的数据类型更改，TDSQL尝试尽可能将现有列值转换为新类型。
>!这种转换可能会导致数据的更改。 例如，如果缩短字符串列，值可能会被截断。 如果转换到新数据类型会导致数据丢失，为了防止操作成功，请在使用 ALTER TABLE 之前启用严格 SQL 模式。
如果您使用 CHANGE 或 MODIFY 缩短列上存在索引的列，并且生成的列长度小于索引长度，TDSQL 会自动缩短索引。
要对表中的列重新排序，请在 CHANGE 或 MODIFY 操作中使用 FIRST 和 AFTER。 

**主键和索引**
DROP PRIMARY KEY 删除主键。 如果没有主键，则会发生错误。
如果启用了 sql_require_primary_key 系统变量，则尝试删除主键会产生错误。
如果向表中添加 UNIQUE INDEX 或 PRIMARY KEY，TDSQL会将其存储在任何非唯一索引之前，以允许尽早检测重复键。
DROP INDEX 删除索引，要确定索引名称，请使用 SHOW INDEX FROM tbl_name。
RENAME INDEX old_index_name to new_index_name 重命名索引。表的内容保持不变。 old_index_name 必须是表中未由同一 ALTER TABLE 语句删除的现有索引的名称。 new_index_name 是新的索引名称，在应用更改后不能与结果表中的索引名称重复。 两个索引名称都不能是 PRIMARY。
在 ALTER TABLE 语句之后，可能需要运行 ANALYZE TABLE 来更新索引基数信息。
ALTER INDEX 操作允许使索引可见或不可见。 优化器不使用不可见索引。 索引可见性的修改适用于主键以外的索引（显式或隐式）。 此功能与存储引擎无关（支持任何引擎）。

**check约束**
ALTER TABLE 允许 CHECK 添加，删除或更改现有表的约束：
- 添加新约束：
```
ALTER TABLE tbl_name
    ADD CONSTRAINT [ symbol] CHECK（expr）[[NOT] ENFORCED];
```
- 删除名为symbol的现有 CHECK约束：
```
ALTER TABLE tbl_name DROP CHECK symbol;
```
- 更改是否强制执行名为symbol的现有 CHECK 约束：
```
ALTER TABLE tbl_name ALTER CHECK symbol [NOT] ENFORCED;
```
如果表更改导致违反强制执行的 CHECK 约束，则会发生错误并且不会修改表。 发生错误的操作示例：
- 尝试将 AUTO_INCREMENT 属性添加到在 CHECK 约束中使用的列。
- 尝试添加强制 CHECK 约束或强制现有行违反约束条件的非强制 CHECK 约束。
- 尝试修改、重命名或删除在 CHECK 约束中使用的列，除非该约束也在同一语句中删除。 例外：如果 CHECK 约束仅引用单个列，则删除该列会自动删除该约束。

**更改字符集**
要将表默认字符集和所有字符列（CHAR、VARCHAR）更改为新字符集，请使用如下语句：
```
ALTER TABLE tbl_name CONVERT TO CHARACTER SET charset_name;
```
该语句还会更改所有字符列的排序规则。 如果未指定 COLLATE 子句来指示要使用的排序规则，则该语句将使用字符集的默认排序规则。 
要仅更改表的默认 字符集，请使用以下语句：
```
ALTER TABLE tbl_name DEFAULT CHARACTER SET charset_name;
```
>!DEFAULT 一词是可选的。 默认字符集是在您没有为稍后添加到表中的列指定字符集时使用的字符集（例如，使用 ALTER TABLE ... ADD column）

**ALTER TABLE分区操作**
ALTER TABLE 的分区相关子句可与分区表一起使用，用于重新分区、添加、删除、丢弃、导入、合并和拆分分区，以及执行分区维护。
ALTER TABLE ADD PARTITION 的 partition_definition 子句支持与 CREATE TABLE 语句的同名子句相同的选项。假设您创建了分区表，如下所示：
```
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (
    	id INT,
    	year_col INT primary key
)
PARTITION BY RANGE (year_col) (
    PARTITION p0 VALUES LESS THAN (1991),
    PARTITION p1 VALUES LESS THAN (1995),
    PARTITION p2 VALUES LESS THAN (1999)
);
```
您可以 p3 向此表 添加新分区 ，以存储小于以下值的值 2002 ：
```
ALTER TABLE t1 ADD PARTITION (PARTITION p3 VALUES LESS THAN (2002));
```
DROP PARTITION 可用于删除一个或多个 RANGE 或 LIST 分区。 存储在 partition_names 列表中命名的已删除分区中的任何数据都将被丢弃。 例如，给定先前定义的表 t1，您可以删除名为 p0 和 p1 的分区，如下所示：
```
ALTER TABLE t1 DROP PARTITION p0,p1;
```
>?ADD PARTITION 和 DROP PARTITION 目前不支持 IF [NOT] EXISTS。

支持分区表的重命名。 您可以使用 ALTER TABLE ... REORGANIZE PARTITION; 间接重命名单个分区。 但是，此操作会复制分区的数据。
```
drop table orders_range;
CREATE TABLE orders_range (
   	 id INT AUTO_INCREMENT PRIMARY KEY,
   	 customer_surname VARCHAR(30),
   	 store_id INT,
  	  salesperson_id INT,
    	order_Date DATE,
   	 note VARCHAR(500)
) PARTITION BY RANGE (id) 
(PARTITION p0 VALUES LESS THAN (5), 
PARTITION p1 VALUES LESS THAN (10), 
PARTITION p3 VALUES LESS THAN (15));


alter table orders_range
reorganize partition p0 into
(partition n0 values less than(3),
partition n1 values less than(5));
```
要从选定分区中删除行，请使用 TRUNCATE PARTITION 选项。 此选项采用一个或多个逗号分隔的分区名称列表。 考虑由该语句创建的表 t1：
```
drop table t1;
CREATE TABLE t1 (
    id INT,
    year_col INT primary key
)
PARTITION BY RANGE (year_col) (
    PARTITION p0 VALUES LESS THAN (1991),
    PARTITION p1 VALUES LESS THAN (1995),
    PARTITION p2 VALUES LESS THAN (1999),
    PARTITION p3 VALUES LESS THAN (2003),
    PARTITION p4 VALUES LESS THAN (2007)
);
```
要从分区中删除所有行 p0 ，请使用以下语句：
```
ALTER TABLE t1 TRUNCATE PARTITION p0;
```
刚才显示的语句与以下 DELETE 语句 具有相同的效果 ：
```
DELETE FROM t1 WHERE year_col <1991;
```
截断多个分区时，分区不必是连续的：这可以极大地简化分区表上的删除操作，否则如果使用 DELETE 语句完成，这些操作将需要非常复杂的 WHERE 条件。 例如，此语句删除分区 p1 和 p3 中的所有行：
```
ALTER TABLE t1 TRUNCATE PARTITION p1,p3;
```
等效的 DELETE 语句如下所示：

```
DELETE FROM t1 WHERE
  (year_col >= 1991 AND year_col < 1995)
    OR
  (year_col >= 2003 AND year_col < 2007);
```
如果使用 ALL 关键字代替分区名称列表，则该语句作用于所有表分区。
TRUNCATE PARTITION 只是删除行； 它不会改变表本身或其任何分区的定义。
要验证行是否已删除，请使用如下查询检查 INFORMATION_SCHEMA.PARTITIONS 表：
```
SELECT PARTITION_NAME, TABLE_ROWS
    FROM INFORMATION_SCHEMA.PARTITIONS
    WHERE TABLE_NAME = 't1';
```
要更改分区表使用的部分而非全部分区，您可以使用 REORGANIZE PARTITION。 该语句可以以多种方式使用：
- 将一组分区合并为一个分区。 这是通过在 partition_names 列表中命名多个分区并为 partition_definition 提供单个定义来完成的。
- 将现有分区拆分为多个分区。 通过为 partition_names 命名单个分区并提供多个 partition_definitions 来完成此操作。
- 更改使用 VALUES LESS THAN 定义的分区子集的范围或使用 VALUES IN 定义的分区子集的值列表。

>!对于没有明确命名的分区，TDSQL会自动提供默认名称 p0、p1、p2 等。 对于子分区也是如此。

要将表分区或子分区与表交换，请使用 ALTER TABLE ... EXCHANGE PARTITION 语句——即将分区或子分区中的任何现有行移至非分区表，并将非分区表中的任何现有行移至 表分区或子分区。
另外有几个选项提供分区维护和修复功能，类似于通过 CHECK TABLE 和 REPAIR TABLE 等语句为非分区表实现的功能。 这些包括分析分区、检查分区、优化分区、重建分区和修复分区。 这些选项中的每一个都采用 partition_names 子句，该子句由一个或多个分区名称组成，以逗号分隔。 分区必须已经存在于目标表中。 您还可以使用 ALL 关键字代替 partition_names，在这种情况下，该语句作用于所有表分区。 
- InnoDB 目前不支持 per-partition 优化； ALTER TABLE ... OPTIMIZE PARTITION 导致整个表重建和分析，并发出适当的警告。要解决此问题，请改用 ALTER TABLE ... REBUILD PARTITION 和 ALTER TABLE ... ANALYZE PARTITION。
- 未分区的表不支持 ANALYZE PARTITION、CHECK PARTITION、OPTIMIZE PARTITION 和 REPAIR PARTITION 选项。
- REMOVE PARTITIONING 使您能够在不影响表或其数据的情况下删除表的分区。 此选项可以与其他 ALTER TABLE 选项结合使用，例如用于添加、删除或重命名列或索引的选项。

除了其他变更规范之外，ALTER TABLE 语句可以包含 PARTITION BY 或 REMOVE PARTITIONING 子句，但必须在任何其他规范之后最后指定 PARTITION BY 或 REMOVE PARTITIONING 子句。
ADD PARTITION、DROP PARTITION、REORGANIZE PARTITION、ANALYZE PARTITION、CHECK PARTITION 和 REPAIR PARTITION 选项不能与单个 ALTER TABLE 中的其他更改规范结合使用，因为刚刚列出的选项作用于单个分区。
在给定的 ALTER TABLE 语句中只能使用以下任一选项的单个实例：PARTITION BY、ADD PARTITION、DROP PARTITION、TRUNCATE PARTITION、EXCHANGE PARTITION、REORGANIZE PARTITION 或ANALYZE PARTITION、CHECK PARTITION、OPTIMIZE 分区，重建分区，删除分区。
例如，以下两个语句无效：
```
ALTER TABLE t1 ANALYZE PARTITION p1,ANALYZE PARTITION p2;
ALTER TABLE t1 ANALYZE PARTITION p1,CHECK PARTITION p2;
```
在第一种情况下，您可以使用带有单个 ANALYZE PARTITION 选项的单个语句同时分析表 t1 的分区 p1 和 p2，该选项列出了要分析的两个分区，如下所示：
```
ALTER TABLE t1 ANALYZE PARTITION p1,p2;
```
在第二种情况下，不能同时对同一个表的不同分区执行 ANALYZE 和 CHECK 操作。 相反，您必须发出两个单独的语句，如下所示：
```
ALTER TABLE t1 ANALYZE PARTITION p1;
ALTER TABLE t1 CHECK PARTITION p2;
```
子分区目前不支持 REBUILD 操作。 REBUILD 关键字明确禁止用于子分区，如果使用，会导致 ALTER TABLE 失败并出现错误。
当要检查或修复的分区包含任何重复的键错误时，CHECK PARTITION 和 REPAIR PARTITION 操作将失败。

**ALTER TABLE示例**
从 t1 如下所示创建 的表开始 ：
```
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (a INTEGER primary key, b CHAR(10));
```
要将表重命名 t1 为 t2 ：
```
ALTER TABLE t1 RENAME t2;
```
要将列 a 从 INTEGER 更改为 TINYINT NOT NULL（保留名称不变），并将列 b 从 CHAR(10) 更改为 CHAR(20) 并将其从 b 重命名为 c：
```
ALTER TABLE t2 MODIFY a TINYINT NOT NULL, CHANGE b c CHAR(20);
```
要在 d 列上添加索引并在 a 列上添加 UNIQUE 索引：
```
ALTER TABLE t2 ADD INDEX(c),ADD UNIQUE(a);
```
要删除列 c ：
```
ALTER TABLE t2 DROP COLUMN c;
```
添加名为 c 的新 AUTO_INCREMENT 整数列：
```
DROP TABLE IF EXISTS t2;
create table t2(a int primary key);
ALTER TABLE t2 ADD c INT UNSIGNED NOT NULL AUTO_INCREMENT,ADD KEY (c);
ALTER TABLE t2 RENAME t6;
```

## DROP
### Drop database
语法如下：
```
DROP {DATABASE | SCHEMA} [IF EXISTS] db_name
```
>!
- DROP DATABASE 删除数据库中的所有表并删除数据库。 对此语句要非常小心！ 要使用 DROP DATABASE ，您需要 DROP database 的 权限。 DROP SCHEMA 是DROP DATABASE的同义词。
- 删除数据库时， 不会自动删除专门为数据库授予的权限，必须手动删除它们。
示例：`DROP DATABASE test;`

### Drop index
语法如下：
```
DROP INDEX index_name ON tbl_name
    [algorithm_option | lock_option] ...

algorithm_option:
    ALGORITHM [=] {DEFAULT | INPLACE | COPY}

lock_option:
    LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}

```
>!
- 要删除主键，索引名称始终为 PRIMARY，必须将其指定为带引号的标识符，因为 PRIMARY 是保留字：DROP INDEX `PRIMARY` ON t;


示例：

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
1 row in set (0.00 sec)

MySQL [test]> drop index uniq_idx_job_id on customer;
Query OK, 0 rows affected (0.04 sec)

MySQL [test]> drop index idx_cust on customer;
Query OK, 0 rows affected (0.08 sec)
```

### Drop table
语法如下：
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

示例：
```
DROP TABLE test;
drop table test RESTRICT;
drop table test5 CASCADE;

```

## TRUNCATE
语法如下：
```
TRUNCATE [TABLE] tbl_name
```

示例：
`truncate table t1;`
TRUNCATE TABLE 完全清空一个表。 它需要 DROP 权限。 从逻辑上讲，TRUNCATE TABLE 类似于删除所有行的 DELETE 语句，或一系列 DROP TABLE 和 CREATE TABLE 语句。
为了实现高性能，TRUNCATE TABLE 绕过了删除数据的 DML 方法。 因此，它不会导致 ON DELETE 触发器触发，不能对具有父子外键关系的 InnoDB 表执行，也不能像 DML 操作一样回滚。 但是，如果服务器在操作期间停止，则对使用原子 DDL 支持的存储引擎的表的 TRUNCATE TABLE 操作要么完全提交，要么回滚。 
虽然 TRUNCATE TABLE 类似于 DELETE，但它被归类为 DDL 语句而不是 DML 语句。 它在以下方面与 DELETE 不同：
- 截断操作删除并重新创建表，这比逐行删除要快得多，特别是对于大表。
- 截断操作会导致隐式提交，因此无法回滚。 
- 如果会话持有活动表锁，则无法执行截断操作。
- 截断操作不会为已删除的行数返回有意义的值。通常的结果是“0 行受影响”，这应该被解释为“没有信息”。
- 只要表定义有效，即使数据或索引文件已损坏，也可以使用 TRUNCATE TABLE 将表重新创建为空表。
- 任何 AUTO_INCREMENT 值都重置为其起始值。即使对于通常不重用序列值的InnoDB 也是如此。
- 当与分区表一起使用时，TRUNCATE TABLE 保留分区；也就是说，删除并重新创建数据和索引文件，而分区定义不受影响。
- TRUNCATE TABLE 语句不会调用 ON DELETE 触发器。
- 支持截断损坏的 InnoDB 表。

出于二进制日志记录和复制的目的，TRUNCATE TABLE 被视为 DDL 而不是 DML，并且始终作为语句记录。
