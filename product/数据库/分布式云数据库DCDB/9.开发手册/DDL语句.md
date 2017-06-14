DCDB for Percona、MariaDB支持通用的DDL语句，如建库，建表，修改表结构等。


## 建表

DCDB for Percona、MariaDB可以创建三种类型的表，分表，小表以及单表。分表适用于表在单个数据库存不下的情况，此时对sql会有一定的限制，具体参考<SQL兼容性>；单表主要用于数据量能在单个数据库存储，同时sql比较复杂的情况

### 分表：参考<分表>

详见分表

### 广播表
广播表即小表广播功能，设置为广播表后，该表的所有操作都将广播到所有物理分片（set）中，每个分片都有改表的全量数据。

```
	mysql> create table test.global_table ( a int, b  int,primary key(b)) shardkey=noshardkey_allset
```
> 小表广播功能主要方便跨物理分片（set）的join操作和复杂运算,常用于某些更改频率相对低的表，但使用频繁的表，例如配置表等；
> 如果要更新广播表，只有当所有分片都完成更新后，才回给予事务应答，因此您无需担心每个分片中的数据不一致；

### 单表
单表，主要用于存储一些无需分片的表：该表的数据全量存在第一个物理分片（set）中，所有该类型的表都放在第一个物理分片（set）中，语法和使用防范和mysql完全一样，你可以把他理解为一个非分布式的表。
```
	mysql> create table test.noshard_table ( a int, b  int,primary key(b)) 
```

> 系统会自动均衡第一个物理分片（SET）的存储容量，避免多个单表将第一个物理分片写爆。



## 修改表

修改表和mysql的语法一样，目前不支持修改shardkey对应的列：

### 增加列
	mysql> alter table test.test1 add column d varchar(20);
	Query OK, 0 rows affected (0.10 sec)
	
### 增加索引
	mysql> alter table test.test1 add index index_c(c);
	Query OK, 0 rows affected (0.06 sec)

### 删除列
	mysql> alter table test.test1 drop column b;
	Query OK, 0 rows affected (0.10 sec)

### 删除索引
	mysql> alter table test.test1 drop index index_c;
	Query OK, 0 rows affected (0.06 sec)

### 修改字段
	mysql> alter table test.test1 modify column b varchar(20);
	Query OK, 0 rows affected (0.16 sec)

### 清除表数据
	mysql> truncate table test.test1;
	Query OK, 0 rows affected (0.16 sec)	

## 删除表

删除表和mysql的语法完全一样，DCDB for Percona、MariaDB会根据表的类型，自动去一个或者多个后端数据库删除表

	mysql> drop table test.ff;
	Query OK, 0 rows affected (0.07 sec)
	
