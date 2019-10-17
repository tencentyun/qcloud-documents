开始一个事务块。

## 概要

```sql
START TRANSACTION [SERIALIZABLE | READ COMMITTED | READ UNCOMMITTED]
                  [READ WRITE | READ ONLY]
```

## 描述
START TRANSACTION 开始一个新的事务块。如果指定了隔离级别、读写模式，新的事务将会具有这些特性，就像执行了 **SET TRANSACTION** 一样，这和 BEGIN 命令一样。

## 参数

SERIALIZABLE
READ COMMITTED
READ UNCOMMITTED
SQL 标准定义四个事务隔离级别：READ COMMITTED、READ UNCOMMITTED、 SERIALIZABLE 和 REPEATABLE READ。
默认行为：一个语句只能看到在它开始前已经提交的行（READ COMMITTED）。在数据库中 READ UNCOMMITTED 和 READ COMMITTED 一样。REPEATABLE READ 目前还不支持；如果需要该隔离级别则使用 SERIALIZABLE。在 SERIALIZABLE 隔离模式下，当前事务内的所有语句只能看到在事务中第一条语句执行前已经提交的行，是一种严格的事务隔离。该事务级别模拟串行事务执行，事务一个接一个的执行，而不是并行地。使用该隔离级别的应用一定要准备由于串行失败而导致重新执行事务。

READ WRITE
READ ONLY
决定事务是 read/write 还是 read-only。默认为 read/write。当一个事务是 read-only，下面的 SQL 命令是不被允许的：
INSERT、 UPDATE、 DELETE 以及 COPY FROM（这种情况是如果将要写的表不是临时表） ； 所有的 CREATE、 ALTER 和 DROP 命令； GRANT、REVOKE、TRUNCATE；以及 EXPALIN ANALYZE 和 EXECUTE 要执行的命令。

## 示例

开始一个事务块：

```sql
START TRANSACTION;
```

## 兼容性
在标准中，没有必要发出 START TRANSACTION 来开始一个事务块，任何 SQL 命令会隐式地开始一个块。数据库的行为可以被视作在每个命令之后隐式地发出一个没有跟随在 START TRANSACTION（或者 BEGIN）之后的 COMMIT 并且因此通常被称作"自动提交"。为了方便，其他关系型数据库系统也可能会提供自动提交特性。

SQL 标准要求在连续的 transaction_modes 之间有逗号，但是出于历史的原因，数据库中允许逗号省略。

另见 SET TRANSACTION 的兼容性部分。

## 另见
BEGIN、SET TRANSACTION
