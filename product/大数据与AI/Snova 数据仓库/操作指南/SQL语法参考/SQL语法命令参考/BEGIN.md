#### BEGIN

开始一个事务块。

##### 概要

```sql
BEGIN [WORK | TRANSACTION] [transaction_mode]
      [READ ONLY | READ WRITE]
```

其中transaction_mode是下列之一：

```sql
ISOLATION LEVEL | {SERIALIZABLE | READ COMMITTED | READ UNCOMMITTED}
```

##### 描述

BEGIN 开始一个事务块，也就是说所有 BEGIN 命令之后的所有语句将被在一个 事务中执行，直到给出一个显式的 COMMIT 或ROLLBACK。 默认情况下 (没有 BEGIN)，数据库在 "自动提交"模式中执行事务，也就是说每个语句都 在自己的事务中执行并且在语句结束时隐式地执行一次提交（如果执 行成功，否则会完成一次回滚）。

在一个事务块内的语句会执行得更快，因为事务的开始/提交也要求可观 的 CPU 和磁盘活动。在进行多个相关更改时，在一个事务内执行多个语 句也有助于保证一致性：在所有相关更新还没有完成之前，其他会话将不 能看到中间状态。

如果指定了隔离级别、读/写模式或者延迟模式，新事务也会有那些特性， 就像执行了 SET TRANSACTION 一样。

##### 参数

WORK

TRANSACTION

可选的关键词。它们没有效果。

SERIALIZABLE

READ COMMITTED

READ UNCOMMITTED

SQL标准定义了四个事务隔离级别： READ COMMITTED, READ UNCOMMITTED, SERIALIZABLE,和REPEATABLE READ。默认行为是一个语句只能看到在开始之前提交的行 (READ COMMITTED)。在数据库中 READ UNCOMMITTED被视为与 READ COMMITTED相同。不支持 REPEATABLE READ； 如果需要此行为请使用SERIALIZABLE 。 SERIALIZABLE 是最严格的事务隔离。该级别模拟串行事务执行，就好像事务已经连续执行，而不是同时执行。使用此级别的应用程序必须准备好重试因序列化失败而导致的事务。

READ WRITE

READ ONLY

确定事务是读/写还是只读。读/写是默认值。当事务为只读时，不允许以下SQL命令：INSERT, UPDATE, DELETE, 和COPY FROM 如果他们的表不是临时表的话； 所有的CREATE,ALTER, 和DROP 命令还有 GRANT, REVOKE, TRUNCATE;和EXPLAIN ANALYZE 以及 EXECUTE 如果他们将执行的命令列在列表的话。

##### 注解

START TRANSACTION] 具有BEGIN相同的功能。

使用 COMMIT 或  ROLLBACK 来终止一个事务块。

在已经在一个事务块中时发出BEGIN 将惹出一个警告 消息。事务状态不会被影响。要在一个事务块中嵌套事务，可以使用保 存点(见SAVEPOINT).

##### 示例

开始一个事务块：

```sql
BEGIN;
```

要使用可序列化隔离级别开始事务块：

```sql
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

##### 兼容性

BEGIN 是数据库语言扩展。它相当于SQL标准的命令START TRANSACTION 。

顺便一提， BEGIN关键词用于嵌入式SQL中的不同用途。建议在移植数据库应用程序时注意事务语义。

##### 另见

COMMIT, ROLLBACK ,START TRANSACTION ,SAVEPOINT