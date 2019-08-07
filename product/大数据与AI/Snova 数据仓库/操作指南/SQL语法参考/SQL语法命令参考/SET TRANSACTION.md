设置当前事务的特性。

## 概要

```sql
SET TRANSACTION [transaction_mode] [READ ONLY | READ WRITE]
 
SET SESSION CHARACTERISTICS AS TRANSACTION transaction_mode 
     [READ ONLY | READ WRITE]
```

其中 transaction_mode 为下列之一：

```sql
   ISOLATION LEVEL {SERIALIZABLE | READ COMMITTED | READ UNCOMMITTED}
```

## 描述
SET TRANSACTION 命令设置当前会话的特性。它对任何子序列事务没有影响。

可用的事务特性是事务隔离级别和事务访问模式（读/写或只读）。

一个事务的隔离级别决定当其他事务并行运行时该事务能看见什么数据。
- **READ COMMITTED**：一个语句只能看到在它开始前提交的行。这是默认值。
- **SERIALIZABLE**：当前事务的所有语句只能看到这个事务中执行的第一个查询或者数据修改语句之前提交的行。

SQL 标准定义了两种额外的级别，READ UNCOMMITTED 和 REPEATABLE READ。在数据库中 READ UNCOMMITTED 被当作为 READ COMMITTED。 REPEATABLE READ 还不支持；如果需要 REPEATABLE READ 行为，使用 SERIALIZABLE。

一个事务执行了第一个查询或者数据修改语句（SELECT、INSERT、 DELETE、UPDATE、FETCH 或 COPY）之后就无法更改事务隔离级别。

事务的访问模式决定该事务是否为读/写或者只读。 读/写是默认值。 当一个事务为只读时，如果 SQL 命令 INSERT、UPDATE、DELETE 和 COPY FROM 要写的表不是一个临时表，则它们不被允许。不允许 CREATE、ALTER 和 DROP 命令。不允许 GRANT、REVOKE、TRUNCATE。如果 EXPLAIN ANALYZE 和 EXECUTE 要执行的命令是上述命令之一， 则它们也不被允许。这是一种高层的只读概念，它不能阻止所有对磁盘的写入。

## 参数

SESSION CHARACTERISTICS
为一个会话的子事务序列设置默认的事务特征。

SERIALIZABLE
READ COMMITTED
READ UNCOMMITTED
SQL 标准定义的四个事务隔离级别：READ COMMITTED、READ UNCOMMITTED、 SERIALIZABLE 和 REPEATABLE READ。
将一个语句只能看到在它开始前已经提交的行作为（samp class="ph codeph">READ COMMITTED）默认行为。在数据库中， READ UNCOMMITTED 被看作为 READ COMMITTED。 REPEATABLE READ 是不支持的，使用SERIALIZABLE 作为替代。 SERIALIZABLE 是最严格的事务隔离级别。该级别模拟了串行化的事务执行，好像事务一个接着一个执行，串行而不是并行的。实际应用中使用该级别要准备由于线性执行的失败而尝试重启事务。

READ WRITE
READ ONLY
决定事务是读/写还是只读。读/写是默认模式。当一个事务是只读的，下面的SQL命令：INSERT、UPDATE、DELETE 和 COPY FROM 执行将被禁止，如果他们将要写的表不是临时表。也不允许 CREATE、ALTER 和 DROP命令执行。不允许执行 GRANT、REVOKE、TRUNCATE。同时 EXPLAIN ANALYZE 和 EXECUTE要执行的命令是上述命令之一也会不允许执行。

## 注解
如果执行 SET TRANSACTION 之前没有 START TRANSACTION 或者 BEGIN，它会发出一个警告并且不会有任何效果。

可以通过在 BEGIN 或者 START TRANSACTION 中指定想要的 transaction_modes 来省掉 SET TRANSACTION。

会话默认的事务模式也可以通过设置配置参数 default_transaction_isolation 和 default_transaction_read_only 来设置。

## 示例
为当前事务设置一个事务隔离级别：

```sql
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

## 兼容性
SQL 标准中定义了这些命令。 SERIALIZABLE 在标准中是默认的隔离级别。在数据库中默认的隔离级别是 READ COMMITTED。由于缺少断言锁， SERIALIZABLE 并不是真正的串行化。从本质上讲，一个断言锁系统通过严格限制写的内容来防止幻读，而数据库中使用的多版本并发控制模型通过严格显示读的内容来方式幻读。

在 SQL 标准中，可以用这些命令设置一个其他的事务特性：诊断区域的尺寸。这个概念与嵌入式 SQL 有关，并且因此没有在数据库服务器中实现。

SQL 标准要求连续的 transaction_modes 之间有逗号， 但是出于历史原因数据库允许省略逗号。

## 另见
BEGIN、LOCK
