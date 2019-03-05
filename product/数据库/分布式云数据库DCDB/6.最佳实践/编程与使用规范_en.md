# Programming and Usage Specification of Distributed Version
> **DCDB refers to DCDB for Percona and MariaDB, unless otherwise specified in this document.**

## 1. Overview
### 1.1 Introduction to Distributed Solution
DCDB for Percona and MariaDB is a distributed database deployed on Tencent Cloud's public cloud. It is compatible with MySQL protocol and syntax and supports automatic horizontal split. With distributed database, a logic database table is acquired as a whole and then at backend, is evenly split into multiple shards and distributed to multiple physical nodes. Currently, DCDB for Percona and MariaDB deploys master/slave architecture by default and provides complete solutions for disaster recovery, backup, recovery, monitoring, migration, and so on. It is suitable for massive database scenarios at TB or PB level.
**DCDB for Percona and MariaDB supports horizontal split**, which is a distributed solution to split the data of a table to multiple databases (hosts) according to the logic of the data. This solution is also called horizontal data sharding.

### 1.2 Glossary
**DCDB for Percona and MariaDB**: It is a distributed version of DCDB and is named DCDB in short in the follow-up document where does not involve other engines.

**Vertical split**: Tables are classified according to business logic and distributed to different databases to share the pressure of single database.

**Horizontal split**: Instead of being classified, tables are split to different databases in certain rules. Each database is a shard containing only a part of data.

**Sharding rules**: Or data split rules. As relational database is a two-dimensional model, two split methods are available:
 - Manually split by a regular field, such as date ( for example, 2015 and 2016 can be considered as a shard respectively), user's ID card number...
 - Hash a specific field and distribute data to different databases according to the specified field, which is called **ShardKey**


**Instance**: Multiple logically unified shards compose a logic instance.

**Shard**: A physical-logic instance consists of database engines including "a master node (Master), some slave nodes (Slave_n), and some remote slave nodes (Watcher_m)".

**Node**: It is a physical device carrying shards. Node could be a physical machine, a virtual machine or a small cluster.

**Logic table**: Horizontal split is a physical split. While logically, the split database or database table is still a complete database table.

**proxy**: With Tproxy, DCDB achieves automatic databases and tables splitting, manages the underlying physical database instances and provides a unique service port that is compatible with mysql database.

**shard**: It is a physical database instance. A logical instance that is visible to users is composed of multiple physical instances.

## 2. Usage Specification
### 2.1 Database Connection
DCDB provides a unique IP and its ports can be accessed and used by users, for example:
```
mysql -h10.231.136.34 -P3306 -utest12 -ptestpassword
```
### 2.2 Overview of Incompatibility

- You should specify the shardkey (a sharding field) when create a table. A sample code is as follows:
```
create table test(a int, b int, …) shardkey=b
```
- Cross-node "join" and "transaction"
- A batch operation like batch insert will fail when data is split into two different shards. It only supports the batch operation when the value of shardkey is always same.
- View, storage procedure, trigger
-	Self-built partition
- It does not support the version below MySQL 3.4.0, SSL, and compression protocol.
- Compatibility: [Compatibility Description](https://cloud.tencent.com/doc/product/237/%E5%85%BC%E5%AE%B9%E6%80%A7%E8%AF%B4%E6%98%8E).

#### 2.2.1 Creating a Table

When creating a table, you must specify the value of shardkey at the end, which is a field name in the table used for SQL routing selection:
```
mysql> create table test1 ( a int , b int, c char(20) );
ERROR 1005 (07000): Proxy Warning - sql is not legal,tokenizer_gram went wrong

mysql> create table test1 ( a int , b int, c char(20) ) shardkey=a;
Query OK, 0 rows affected (1.56 sec)

```
**The field of "shardkey" has the following restrictions:**
1. If there is a primary key or a unique index, "shardkey" must be a part of the primary key and all unique indexes;
2. If it contains multiple unique indexes (including primary key), these indexes must have an intersection field that is the "shardkey";
3. The type of "shardkey" must be int, bigint, smallint/char/varchar;
4. The value of "shardkey" should not contain Chinese characters. Otherwise, different character sets could be routed to different partitions because the gateway cannot convert character set;
5. Do not update the value of "shardkey";
6. Put "shardkey=a" at the end of sql.

#### 2.2.2 Ordinary sql
**select:** It is recommended to contain the "shardkey" field. If the field is not contained, you need to scan the whole table, and then the gateway aggregates the result set. But this will cause a great impact on performance:
```
mysql> select * from test1 where a=2;
+------+------+---------+
| a     | b     | c        |
+------+------+---------+
| 2     | 3     | record2 |
| 2     | 4     | record3 |
+------+------+---------+
2 rows in set (0.00 sec)

```

**insert/replace:** Field **"must"** contain "shardkey", or the sql will not be executed. Because the proxy cannot confirm which shard should be inserted into:
```
mysql> insert into test1 (b,c) values(4,"record3");
ERROR 1105 (07000): Proxy Warning - sql have no shardkey

mysql> insert into test1 (a,c) values(4,"record3");
Query OK, 1 row affected (0.01 sec)
```


**delete/update:** When we execute this kind of sql, for safety, the sql **"must"** contain "where" conditions, or it will not be executed:
```
mysql> delete from test1;
ERROR 1005 (07000): Proxy Warning - sql is not legal,tokenizer_gram went wrong

mysql> delete from test1 where a=1;
Query OK, 1 row affected (0.01 sec)

```

#### 2.2.3 join
**join:** Currently, DCDB only supports the join operation in a single shard. This means all sqls in a transaction must be based on the same shard, so the shardkey must be specified.

```
mysql> create table test1 ( a int , b int, c char(20) ) shardkey=a;
Query OK, 0 rows affected (1.56 sec)

mysql> create table test2 ( a int , d int, e char(20) ) shardkey=a;
Query OK, 0 rows affected (1.46 sec)

mysql> insert into test1 (a,b,c) values(1,2,"record1"),(2,3,"record2");
Query OK, 2 rows affected (0.02 sec)

mysql> insert into test2 (a,d,e) values(1,3,"test2_record1"),(2,3,"test2_record2");
Query OK, 2 rows affected (0.02 sec)

mysql> select * from test1 join test2 on test1.a=test2.a;
ERROR 1105 (07000): Proxy Warning - join shardkey error
mysql> select * from test1 join test2 on test1.a=test2.a where test1.a=1;
+------+------+---------+------+------+---------------+
| a     | b     | c        | a     | d     | e                |
+------+------+---------+------+------+---------------+
| 1     | 2     | record1 | 1    | 3      | test2_record1 |
+------+------+---------+------+------+---------------+
1 row in set (0.00 sec)
```


> Note: The statement `mysql> select * from test1 join test2 on test1.a=test2.a;` will be supported in subsequent versions, but with the following preconditions:
> 1. Must be inner join
> 2.The "where" condition of inner join must be that the "shardkey" of two tables are equal

#### 2.2.4 Transactions

DCDB supports transactions in a single shard, which means all sqls in a transaction must be based on the same shard
```
mysql> select * from test1;
+------+------+---------+
| a     | b     | c        |
+------+------+---------+
| 2     | 3     | record2 |
| 1     | 2     | record1 |
+------+------+---------+
2 rows in set (0.00 sec)

mysql> begin;
Query OK, 0 rows affected (0.00 sec)

mysql> insert into test1 (a,b,c) values(2,4,"record3");
Query OK, 1 row affected (0.00 sec)

mysql> insert into test1 (a,b,c) values(1,4,"record3");
ERROR 1105 (07000): Proxy ERROR - In transaction,this sql use a diffent backend

mysql> select * from test1;
ERROR 1105 (07000): Proxy ERROR - In transaction,this sql use more than one backend

mysql> rollback;
Query OK, 0 rows affected (0.01 sec)

```
> Note: Subsequent versions will support part of simple DML statements

#### 2.2.5 Auto-increment Field

DCDB supports auto-increment field in a certain sense to ensure that a field is globally unique, but monotonic increment is not ensured. Specific usage is as shown below:
**Create:**
```
create table auto_inc ( a int,b int,c int auto_increment,d int) shardkey=d;
```

**Insert:**
```
mysql> insert into shard.auto_inc ( a,b,d,c) values(1,2,3,0),(1,2,3,0);
Query OK, 2 rows affected (0.01 sec)
Records: 2 Duplicates: 0 Warnings: 0
mysql> select * from shard.auto_inc;
+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
| a | b | c | d |
+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
| 1 | 2 | 1 | 3 |
| 1 | 2 | 2 | 3 |
+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
2 rows in set (0.01 sec)

```

Note that when the proxy is scheduling the processes of switching, restarting and others, there could be void in auto-increment field, for example:
```
mysql> insert into shard.auto_inc ( a,b,d,c) values(11,12,13,0),(21,22,23,0);
Query OK, 2 rows affected (0.03 sec)
mysql> select * from shard.auto_inc;
+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
| a | b | c | d |
+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
| 21 | 22 | 2002 | 23 |
| 1 | 2 | 1 | 3 |
| 1 | 2 | 2 | 3 |
| 11 | 12 | 2001 | 13 |
+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
4 rows in set (0.01 sec)

```
Modify the current value
```
alter table auto auto_increment=100
```

> The current version does not support the auto-increment field as shardkey, but subsequent versions will support.

#### 2.2.6 SQL Command Restrictions

Currently, DCDB supports the sql commands as follows:

1. delele, update, insert, replace, select
2. alter, create, drop, truncate
3. show, describe (desc, explain), help
4. start, begin, commit, rollback, savepoint
5. set

> Note: For general sql used to query the information of database status, proxy will sent a default shard. In this case, if you query the statistics information, the result is the information of a single shard.

#### 2.2.7 Restrictions on User Permission

You cannot use sql command to configure user permission through the proxy, please go to **Tencent Cloud Console** -> **Cloud Database** -> **DCDB** -> **Management** to operate.

#### 2.2.8 Other Unsupported MySQL features
1. Cross-node join and transaction (Note that join and transaction can be supported when they are not cross-code and use same shardkey in data operation)
2. View, storage procedure, trigger
3. Self-built partition
4. Batch data import: It does not support the sql like "load data local infile", which needs to be converted to "insert" statement, such as "insert into values (xxx,xxx), (xxx,xxx)";
5. Sub-query, "having" clause

#### 2.2.9 Restrictions on Aggregate Functions
1. If you aggregate after "distinct", "where" condition must contain "shardkey":
For example: `select count(distinct a), sum(distinct a), avg(distinct a) from table where sk=\*\*`

2. If `distinct, order by, group by` are followed by a function, the function must appear in the "select" field and must be defined by an alias which is used after corresponding "distinct", "order by" and "group by":
For example: `select concat(...) as substr from table where ... order by substr`

3. The "group by" field must be contained in the "select" field:
For example: `select count(a),b from test group by b`, where "select" field must contain the "b" field
