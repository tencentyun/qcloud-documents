如您需要阅读或下载全量开发文档，请参见 [TDSQL 开发指南](https://cloud.tencent.com/document/product/557/7714)。


## 创建分表
**分表：**即自动水平拆分的表，水平拆分是基于分表键（shardkey）采用类似于一致性 hash 方式，根据 hash 后的值分配到不同的节点组中的一种技术方案，该能力几乎是所有分布式数据库的核心特性。TDSQL 的设计目标是期望开发者完全无需关注后端分表策略，像使用普通数据库一样使用 TDSQL，因此我们在设计上隐藏了分表的细节方案。

普通的分表创建时必须在最后面指定 shardkey 的值，该值为表中的一个字段名字，会用于后续 sql 的路由选择：
```
	mysql> create table test1 ( a int, b int, c char(20),primary key (a,b),unique key u_1(a,c) ) shardkey=a;
	Query OK, 0 rows affected (0.07 sec)
```

由于在 TDSQL 下，shardkey 对应后端数据库的分区字段，因此必须是主键以及所有唯一索引的一部分，否则无法建表；
```
	mysql> create table test1 ( a int, b int, c char(20),primary key (a,b),unique key u_1(a,c),unique key u_2(b,c) ) shardkey=a;;
```

此时有一个唯一索引 u_2 不包含 shardkey，没法创建表，会报如下错误：
```
	ERROR 1105 (HY000): A UNIQUE INDEX must include all columns in the table's partitioning function
```
因为主键索引或者 unique key 索引意味着需要全局唯一，而要实现全局唯一索引则必须包含 shardkey 字段。

**综述，shardkey 的要求如下：**
1. shardkey 必须是主键以及所有唯一索引的一部分。
2. shardkey 字段的类型必须是 int,bigint,smallint/char/varchar。
3. shardkey 字段的值不能有中文。
4. 不要 update shardkey 字段的值（如必须，请先 delete 该行，再 insert 新值）。
5. shardkey=a 放在 create 语句的最后。
6. 访问数据尽量都能带上 shardkey 字段（非强制要求，但如果不带 shardkey 将会导致该条 SQL 发送到所有节点，影响效率）。

>?某些分表方案可以支持“非主键或唯一索引”成为 shardkey，但此类方案会导致数据不一致，因此 TDSQL 默认禁止“非主键或唯一索引”成为 shardkey。

## 创建广播表
**广播表：**又名小表广播功能，创建了广播表后，每个节点都有该表的全量数据，该表的所有操作都将广播到所有物理分片（set）中。广播表主要用于提升跨 set 的 join 操作的性能，常用于配置表等。
```
	mysql> create table global_table ( a int, b int key) shardkey=noshardkey_allset;
	Query OK, 0 rows affected (0.06 sec)
```
>?广播表采用分布式事务机制，确保数据写入操作的原子性，因此广播表的数据天然情况下是完全一致的。

## 创建普通表（单表）
**普通表（又名单表）：**语法和 MySQL 完全一样，此时该表的数据全量存在第一个 set 中，所有该类型的表都放在第一个 set 中。
```
	mysql> create table noshard_table ( a int, b int key);
	Query OK, 0 rows affected (0.02 sec)
```

## 其他 DDL 操作
TDSQL 不支持修改表名，其他 alte、drop 等 DDL 操作，与 MySQL 语法基本一致。
