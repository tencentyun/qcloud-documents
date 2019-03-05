DCDB 支持通用的 DDL 语句，如建库，建表，修改表结构等。

## 创建表

DCDB 可以创建三种类型的表：分表，广播表以及单表。分表适用于表数据在单个数据库中存储不下的情况。广播表在所有物理分片中都是全量数据，适用于跨物理分片的 join 操作。单表适用于用于数据量能在单个数据库存储，同时 sql 比较复杂的情况。

### 分表
DCDB 支持分表，通过分表键（shardkey）把一个大表水平拆分到多个数据库，形成“独立”的数据库“分片”。多个分片共同组成一个逻辑完整的数据库实例。关于创建分表的详情请见[创建分表](https://cloud.tencent.com/document/product/557/8767)。

### 广播表
广播表即小表广播功能，设置为广播表后，该表的所有操作都将广播到所有物理分片（set）中，每个分片都有改表的全量数据。
```
mysql> create table test.global_table ( a int, b  int,primary key(b)) shardkey=noshardkey_allset
```
小表广播功能主要方便跨物理分片（set）的 join 操作和复杂运算,常用于某些更改频率相对低但使用频率高的表，例如配置表等。
如果要更新广播表，只有当所有分片都完成更新后，才会给予事务应答，因此您无需担心每个分片中的数据不一致。

### 单表
单表主要用于存储一些无需分片的表，该表的数据全量存在第一个物理分片（set）中，所有该类型的表都放在第一个物理分片（set）中，语法和使用防范和 MySQL 完全一样，可理解为一个非分布式的表。
```
mysql> create table test.noshard_table ( a int, b  int,primary key(b)) 
```

> **注意：**
> 系统会自动均衡第一个物理分片（set）的存储容量，避免多个单表将第一个物理分片写爆。

## 修改表
修改表和 MySQL 的语法一样，但目前暂不支持修改 shardkey 对应的列。

### 增加列
```
	mysql> alter table test.test1 add column d varchar(20);
	Query OK, 0 rows affected (0.10 sec)
```	
### 增加索引
```
mysql> alter table test.test1 add index index_c(c);
Query OK, 0 rows affected (0.06 sec)
```
### 删除列
```
	mysql> alter table test.test1 drop column b;
	Query OK, 0 rows affected (0.10 sec)
```
### 删除索引
```
	mysql> alter table test.test1 drop index index_c;
	Query OK, 0 rows affected (0.06 sec)
```
### 修改字段
```
	mysql> alter table test.test1 modify column b varchar(20);
	Query OK, 0 rows affected (0.16 sec)
```
### 清除表数据
```	
	mysql> truncate table test.test1;
	Query OK, 0 rows affected (0.16 sec)	
```
## 删除表
删除表和 MySQL 的语法完全一样，DCDB 会根据表的类型，自动在一个或多个后端数据库删除表。
```
	mysql> drop table test.ff;
	Query OK, 0 rows affected (0.07 sec)
```
