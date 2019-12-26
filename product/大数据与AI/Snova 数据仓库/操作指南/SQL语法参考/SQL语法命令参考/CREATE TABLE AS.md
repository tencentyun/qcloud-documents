从查询结果中定义一个新的表。

## 概要

```sql
CREATE [ [GLOBAL | LOCAL] {TEMPORARY | TEMP} ] TABLE table_name
   [(column_name [, ...] )]
   [ WITH ( storage_parameter=value [, ... ] ) ]
   [ON COMMIT {PRESERVE ROWS | DELETE ROWS | DROP}]
   [TABLESPACE tablespace]
   AS query
   [DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY]
```

该 storage_parameter 如下：

```sql
   APPENDONLY={TRUE|FALSE}
   BLOCKSIZE={8192-2097152}
   ORIENTATION={COLUMN|ROW}
   COMPRESSTYPE={ZLIB|QUICKLZ}
   COMPRESSLEVEL={1-9 | 1}
   FILLFACTOR={10-100}
   OIDS[=TRUE|FALSE]
```

## 描述

CREATE TABLE AS 创建一个表并且使用由 **SELECT** 命令计算所得的数据进行填充。该表列和 SELECT 命令出来的出来的列有相同的名字和数据类型，但是用户可以复写列名通过给出明确的新列名列表。

CREATE TABLE AS 创建一个新表，并且初始计算查询一次来填充新表。该新表不会同步追踪源表查询子序列的变化。

## 参数

GLOBAL | LOCAL
这些关键字用于 SQL 标准的兼容性，但是在数据库中不起作用。

TEMPORARY | TEMP
如果指定了，该新表被创建成为临时表。临时表在会话结束之时自动删除，或者可选地在当前事务结束时（请参阅 ON COMMIT）。当临时表存在时，在当前会话中，同名的永久表示不可见的。除非使用方案限定的名字来引用，临时表中创建的索引也自动是临时的。

table_name
所创建新表的名字（可选方案限定）。

column_name
新表的列名，如果没有提供列名，则使用查询输出的列名。如果表从 EXECUTE 命令中所创建，不能指定一个列名列表。

WITH ( storage_parameter=value )
该 WITH 子句可以用来为表和索引设置存储选项。注意，用户可以在特定的分区或子分区中设置不同的存储参数，通过在分区中指定 WITH 子句。有以下存储选项：
- APPENDONLY：设置到 TRUE 来创建一个表作为追加优化表。如果设定为 FALSE 或者没有声明，则该表将会创建为常规的堆存储表。
- BLOCKSIZE：对表中每个块设置字节大小。该 BLOCKSIZE 必须在8192和2097152字节之间，为8192的倍数，默认值时32768。
- ORIENTATION：对面向列存储设置列，或为面向行存储的设置行（默认值）。该选项仅在 APPENDONLY=TRUE 的时候有效。堆存储表只能是面向行的。
- COMPRESSTYPE：设置 ZLIB（默认值）或者 QUICKLZ1 来指定使用的压缩类型。QuickLZ 使用较少的 CPU 功率，并且比 zlib 具有更快的数据压缩和更低的压缩比。相反，zlib 在较低速率下提供更紧凑的压缩比。此选项仅在 APPENDONLY=TRUE 时有效。
- FILLFACTOR：更多关于此索引存储参数的信息请参阅 **CREATE INDEX**。
- OIDS：设置为 OIDS=FALSE（默认值），则行没有分配的对象标识符。强烈推荐用户在创建表的时候不要启用 OIDS 。在大型表中，如在典型的数据库中表，对表行使用 OIDs 能引起 32OID 计数器环绕。一旦计数器环绕，OIDs 就被认为是不再唯一的，这不仅使它们对用户应用程序无用，而且还可能在数据库系统目录表中引起问题。此外，从表中排出 OIDs 减少了磁盘上存储区表所需的空间，每行4字节，稍微地提升了性能。不允许在面向列的表上使用 OIDs。

ON COMMIT
事务块结束时的临时表的行为可以使用 ON COMMIT 来控制。该三个选项如下：
- PRESERVE ROWS：在临时表事务结束时不采取特别行动。这是默认行为。
- DELETE ROWS：临时表中的所有行将在每个事务块结束时删除。本质上，在每次提交时候执行了 TRUNCATE。
- DROP：在当前事务块结束时将删除临时表。

TABLESPACE tablespace
创建的新表所在的表空间的名字。如果没有指定，则使用数据库默认的表空间。

AS query
该 SELECT或 VALUES命令，或者运行准备好的 SELECT 或 VALUES 查询的 EXECUTE命令。

DISTRIBUTED BY (column, [ ... ] )
DISTRIBUTED RANDOMLY
用来声明数据库表的分布策略。DISTIBUTED BY 使用在分布键中声明一列或者多列进行哈希分布。对于大多数的均匀数据分布，该分布键应当是表的主键或是唯一列或列的集合。如果不可能，则用户可以选择 DISTRIBUTED RANDOMLY，这会将数据随机循环发送到 Segment 实例。
该数据库服务器配置参数 gp_create_table_random_default_distribution 控制默认的表分布策略，如果当用户创建表的时候没有指定 DISTRIBUTED BY 子句。如果没有指定分布策略，则遵循以下规则来创建表：
- 如果查询优化器创建表，并且该参数的值是 off，则该表的分布策略由命令所决定。
- 如果遗传查询优化器创建表，并且该参数的值为 on，则该表的分布策略是随机的。
- GPORCA 创建表，则表分布策略是随机的，该参数值没有影响。

在数据库管理员指南中，更多关于该参数的信息，参阅“服务器配置参数”。更多关于遗传查询优化器和 GPORCA 的信息，参阅“查询数据” 。

## 注意
该命令功能上和 SELECT INTO 相似，但是该命令更常用因为它相比使用 SELECT INTO 的语法不太可能产生混淆。此外， CREATE TABLE AS 提供了包含 SELECT INTO 功能在内超集。

CREATE TABLE AS 可以用于从外部表数据源中快速加载数据。参阅 CREATE EXTERNAL TABLE。

## 实例
创建一个新表 films_recent 仅由表 films 最近的条目组成：

```sql
CREATE TABLE films_recent AS SELECT * FROM films WHERE 
date_prod >= '2007-01-01';
```

创建一个临时表 films_recent，仅由 films 表的最近的条目组成，使用预编译（prepared）语句。新表拥有 OIDs 并在提交时删除：

```sql
PREPARE recentfilms(date) AS SELECT * FROM films WHERE 
date_prod > $1;
CREATE TEMP TABLE films_recent WITH (OIDS) ON COMMIT DROP AS 
EXECUTE recentfilms('2007-01-01');
```

## 兼容性

CREATE TABLE AS 服从 SQL 标准，但以下例外：
- 该标准要求将子查询用括号括起来；在数据库中，这些括号是可选的。
- 该标准定义了 WITH [NO] DATA 子句；这目前并没有由数据库实现。数据库提供的行为和标准的 WITH DATA 情况是一样的。WITH NO DATA 可以通过给查询追加 LIMIT 0 来模拟。
- 数据库处理临时表不同于标准，更多细节参阅 CREATE TABLE。
- 该 WITH 子句是数据库扩展； 存储参数和 OIDs 都不在标准中。
- 该数据库表空间的概念不是标准的一部分。 该 TABLESPACE 子句是一个扩展。

## 另见

CREATE EXTERNAL TABLE、CREATE EXTERNAL TABLE、EXECUTE、SELECT、SELECT INTO、VALUES
