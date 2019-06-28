定义一个新的序列生成器。

## 概要

```sql
CREATE [TEMPORARY | TEMP] SEQUENCE name
       [INCREMENT [BY] value] 
       [MINVALUE minvalue | NO MINVALUE] 
       [MAXVALUE maxvalue | NO MAXVALUE] 
       [START [ WITH ] start] 
       [CACHE cache] 
       [[NO] CYCLE] 
       [OWNED BY { table.column | NONE }]
```

## 描述

CREATE SEQUENCE 创建一个序列数字生成器。 这包含了创建和初始化一个新的特殊的单行表。该生成器将被执行该命令的用户所拥有。

如果给定了模式名称，则序列在指定的模式上建立。否则在当前的模式中建立。临时序列存在于特殊的模式中，所以创建临时序列时一般不会给定模式名。序列名称不能和同模式中的其他序列、表、索引或视图同名。

创建序列之后，用户可以使用 nextval 函数来操作序列。例如，插入一行到表中要获取序列的下一个值：

```sql
INSERT INTO distributors VALUES (nextval('myserial'), 'acme');
```

用户也可以使用函数 setval 来操作序列，但是只能对不操作分布式数据的查询。例如以下的查询是允许的，因为它对主机上的序列生成器进程重置了序列计数器的值：
```sql
SELECT setval('myserial', 201);
```
但是以下数据库中的查询将会拒绝，因为它操作了分布式的数据：
```sql
INSERT INTO product VALUES (setval('myserial', 201), 'gizmo');
```

在常规数据库中（非分布式的），操作序列的函数去本地序列表获取他们需要的值。但是在数据库中，要注意每个段都是它自己特有的数据库进程。因此段需要单个真值点来获取序列值，以至于所有的段都能正确的递增，并且使得序列能以正确的顺序向前移动。序列服务器进程在主机上运行，是分布式数据库中序列的真值点（point-of-truth），段主机在运行时从主机获取序列值。

因为该分布式序列的设计，在对数据库操作序列的函数上有一些限制：
- lastval 和 currval 函数不支持。
- setval 只能用来设置主机上序列生成器的值，不能用来在子查询中更新分布式表数据的记录。
- nextval 有时候根据查询，有时会从主数据库中获取一块值供段数据库使用。所以，如果所有块在段级别不需要，则在序列中跳过该值。注意，常规的 PostgresSQL 数据库也是这样做，所以这不是数据库独有的。

尽管用户不能直接更新一个序列，但是用户可以使用以下查询：
```sql
SELECT * FROM sequence_name;
```
来检查参数和当前序列的状态。尤其是序列的 last_value 字段显示了任何会话所分配的最后值。

## 参数

TEMPORARY | TEMP
如果指定了该字段，则该序列对象仅为该会话所创建，并且会在会话退出时，自动删除。当临时序列存在时，同样名字的存在的永久序列是不可见的（在该会话中）。出给他们引用了该方案限定的名字。

name
所创建的序列的名字（可选方案限定）。

increment
指明了在当前序列值上加上一个什么样的增量来得到一个新的值。一个正值会产生一个递增序列，一个负值会产生一个递减序列，默认值是1。

minvalue
NO MINVALUE
决定该序列所能生成的最小的值，如果没有提供该子句或者指定了 NO MINVALUE，则使用默认值。该升序，降序默认值分别为1和<typora>-2^63-1。

maxvalue
NO MAXVALUE
决定该序列产生的最大值，如果没有提供该子句或者指定了 NO MAXVALUE，则将使用默认值。该升序，降序的默认值分别为<typora>2^63-1和-1。

start
允许序列能在任何地方开始，该升序的默认开始值为 minvalue，降序的默认开始值为 maxvalue。

cache
指明了有多少预先分配并存在内存中供快速访问的序列值。最小值（也是默认值）是1（不用 cache）。

CYCLE
NO CYCLE
序列允许轮回当达到了 maxvalue（对升序来说）或 minvalue（对降序来说）。如果达到了限制，下个生成的值将是 minvalue（对升序来说）或者 maxvalue（对降序来说）。如果指定了 NO CYCLE，任何在序列达到了极限时对 nextval 的调用都将会返回错误。如果没有指定，则默认是 NO CYCLE。

OWNED BY table.column
OWNED BY NONE
会导致序列和一个特定表列相联系，因此如果删除该表列（或者删除整个表），该序列也将会自动删除，该指定的表必须和序列有相同的拥有者，并且在同一模式中。默认值为 OWNED BY NONE 指明没有这样的联系。

## 注意
序列是基于 bigint 的算术，所以该范围不能超过8字节整数的范围（-9223372036854775808到9223372036854775807）。

尽管保证多个会话来分配不同的序列值，但当考虑所有会话时必须保证该值按序列所出。例如会话A保留值1..10，并且返回 nextval=1，然后会话 B 可能在会话 A 生成 nextval=2 之前保留值11..20，并且返回 nextval=11。因此，用户应该只假设 nextval 都是不同的，而不是纯粹按顺序生成。此外，last_value 会反应任何会话保留的最新值。无论其是否已被 nextval 返回。

## 示例

创建名为 myseq 的序列：

```sql
CREATE SEQUENCE myseq START 101;
```

使用 next value 向表中插入一行数据：

```sql
INSERT INTO distributors VALUES (nextval('myseq'), 'acme'); 
```

重置主机上序列计数器的值：

```sql
SELECT setval('myseq', 201);
```

数据库中非法使用 setval（在分布式数据上设置序列的值）：

```sql
INSERT INTO product VALUES (setval('myseq', 201), 'gizmo'); 
```

## 兼容性

CREATE SEQUENCE 遵循 SQL 标准，但是以下除外：
- 不支持该在 SQL 标准中指定的 AS data_type 表达式。
- 使用 nextval() 函数替代 SQL 标准中指定的 NEXT VALUE FOR 表达式获得下一个值。
- 该 OWNED BY 子句是数据库扩展。

## 另见
ALTER SEQUENCE、DROP SEQUENCE
