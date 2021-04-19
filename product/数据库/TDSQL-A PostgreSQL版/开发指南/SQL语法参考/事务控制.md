事务（transaction）是访问并可能操作各种数据项的一个数据库操作序列，这些操作要么全部执行，要么全部不执行，是一个不可分割的工作单位。事务由事务开始与事务结束之间执行的全部数据库操作组成。
事务的存在包含了两个目的：
- 为数据库操作序列提供了一个从失败中恢复到正常状态的方法，同时提供数据库即使在异常状态下仍能保持一致性的方法。
- 当多个应用程序在并发访问数据库时，可以在这些应用程序之间提供一个隔离方法，以防止彼此的操作互相干扰。

## 事务特性
事务具有 ACID 特性，具体如下：
- 原子性(Atomicity)：事务中的全部操作在数据库中是不可分割的，要么全部完成，要么全部不执行。
- 一致性(Consistency)：几个并行执行的事务，其执行结果必须与按某一顺序串行执行的结果相一致。
- 隔离性(Isolation)：事务的执行不受其他事务的干扰，事务执行的中间结果对其他事务必须是透明的。
- 持久性(Durability)：对于任意已提交事务，系统必须保证该事务对数据库的改变不被丢失，即使数据库出现故障。

事务的 ACID 特性是由关系数据库系统（DBMS）来实现的，DBMS 采用日志来保证事务的原子性、一致性和持久性。日志记录了事务对数据库所作的更新，如果某个事务在执行过程中发生错误，就可以根据日志撤销事务对数据库已做的更新，使得数据库回滚到执行事务前的初始状态。

对于事务的隔离性，DBMS 是采用锁机制来实现的。当多个事务同时更新数据库中相同的数据时，只允许持有锁的事务能更新该数据，其他事务必须等待，直到前一个事务释放了锁，其他事务才有机会更新该数据。

## 事务隔离
SQL 标准定义了四种隔离级别。最严格的是可序列化，在标准中用了一整段来定义它，其中说到一组可序列化事务的任意并发执行被保证效果和以某种顺序一个一个执行这些事务一样。其他三种级别使用并发事务之间交互产生的现象来定义，每一个级别中都要求必须不出现一种现象。注意由于可序列化的定义，在该级别上这些现象都不可能发生。

在各个级别上被禁止出现的现象是：
**脏读**
一个事务读取了另一个并行未提交事务写入的数据。

**不可重复读**
一个事务重新读取之前读取过的数据，发现该数据已经被另一个事务（在初始读之后提交）修改。

**幻读**
一个事务重新执行一个返回符合一个搜索条件的行集合的查询，发现满足条件的行集合因为另一个最近提交的事务而发生了改变。

**序列化异常**
成功提交一组事务的结果与这些事务所有可能的串行执行结果都不一致。

| **隔离级别** | **脏读** | **不可重复读** | **幻读** | **序列化异常** |
| ------------ | -------- | -------------- | -------- | -------------- |
| 读未提交     | 允许     | 可能           | 可能     | 可能           |
| 读已提交     | 不可能   | 可能           | 可能     | 可能           |
| 可重复读     | 不可能   | 不可能         | 允许     | 可能           |
| 可序列化     | 不可能   | 不可能         | 不可能   | 不可能         |

声明事务时，隔离级别可以声明为四种标准事务隔离级别中的任意一种，目前 TDSQL-A PostgreSQL版 读未提交和读已提交模式相同，实现了读已提交和可重复读。

## 事务控制
### 启动事务
启动事务可以使用 START TRANSACTION 或者 BEGIN 语法，可以在启动事务的同时，声明该事务的隔离级别、读写模式。
示例：
```
postgres=# START TRANSACTION;
START TRANSACTION
```
或者：
```
postgres=# BEGIN;
BEGIN
```
或者：
```
postgres=# START TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION
```
或者：
```
postgres=# BEGIN WORK ISOLATION LEVEL READ COMMITTED; 
BEGIN
```

### 提交事务
进程#1访问：
```
postgres=# BEGIN;
BEGIN
postgres=# DELETE FROM tdapg WHERE id=5;
DELETE 1
postgres=#
postgres=# SELECT * FROM tdapg ORDER BY id;
 id |  nickname  
----+---------------
 1 | hello tdapg
 2 | tdapg好
 3 | tdapg好
 4 | tdapg default
```

TDSQL-A PostgreSQL版 也是完全支持 ACID 特性，没提交前开启另一个连接查询，会看到是5条记录，这是 TDSQL-A PostgreSQL版 隔离性和多版本视图的实现，如下所示：
进程#2访问：
```
postgres=# SELECT * FROM tdapg ORDER BY id;
 id |  nickname  
----+---------------
 1 | hello tdapg
 2 | tdapg好
 3 | tdapg好
 4 | tdapg default
 5 | tdapg swap
(5 rows)
```

进程#1提交数据：
```
postgres=# COMMIT;
COMMIT
```

进程#2再查询数据，这时能看到已经提交的数据了，这个级别叫“读已提交”：
```
postgres=# SELECT * FROM tdapg ORDER BY id;
 id |  nickname  
----+---------------
 1 | hello tdapg
 2 | tdapg好
 3 | tdapg好
 4 | tdapg default
(4 rows)
```

### 回滚事务
```
postgres=# BEGIN;
BEGIN
postgres=# DELETE FROM tdapg WHERE id IN (3,4);
DELETE 2
postgres=# SELECT * FROM tdapg;
 id | nickname  
----+-------------
 1 | hello tdapg
 2 | tdapg好
(2 rows)

postgres=# ROLLBACK;
ROLLBACK
```

ROLLBACK 后数据又恢复回事务开始前的状态：
```
postgres=# SELECT * FROM tdapg;
 id |  nickname  
----+---------------
 1 | hello tdapg
 2 | tdapg好
 3 | tdapg好
 4 | tdapg default
(4 rows)
```
