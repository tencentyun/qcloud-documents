锁定一个表。

## 概要

```sql
LOCK [TABLE] name [, ...] [IN lockmode MODE] [NOWAIT]
```

lockmode 可以是下列之一：

```sql
    ACCESS SHARE | ROW SHARE | ROW EXCLUSIVE | SHARE UPDATE EXCLUSIVE 
  | SHARE | SHARE ROW EXCLUSIVE | EXCLUSIVE | ACCESS EXCLUSIVE
```

## 描述
LOCK TABLE 获取一个表级锁，必须要等待锁被释放。如果指定了 NOWAIT，LOCK TABLE 不会等待锁被释放，如果无法获取到，该命令会立刻终止并产生一个错误。一旦获取到，该锁会被当前事务一直持有，直到事务结束。

在为引用表的命令自动获取锁时，数据库总是尽可能使用最不严格的锁模式。提供 LOCK TABLE 是用于获取更严格的锁，例如，假设一个应用运行一个 Read Committed 隔离级别的事务，并且需要确保一个表中的数据在事务中保持稳定，要实现这个目的，必须在查询之前在表上获得 SHARE 锁模式。这将组织并发的数据更改并且确保该表的后续读操作看到已提交数据的一个稳定视图，因为 SHARE 锁模式与写入者锁要求的 ROW EXCLUSIVE 锁有冲突，并且用户的 LOCK TABLE name IN SHARE MODE 语句将等待，直到任何持有 ROW EXCLUSIVE 模式锁的事务提交或者回滚。因此，一旦得到锁，就不会有未提交的写入没有解决。

要在运行 Serializable 隔离级别的事务中得到类似的效果，用户必须在执行任何 SELECT 或者数据修改语句之前执行 LOCK TABLE 语句，一个事务的数据视图将在它的第一个 SELECT 或者数据修改语句开始时被冻结，在该事务中稍后的一个 LOCK TABLE 仍将阻止并发写，但是它不会确保该事务读到的东西对应于最新的已提交值。

如果一个此类事务正要修改表中的数据，那么它应该使用 SHARE ROW EXCLUSIVE 锁模式来取代 SHARE 模式。这会保证一次只有一个此类事务运行。如果不用这种模式，死锁就可能出现，两个事务可能都要求SHARE 模式，并且都不能获得 ROW EXCLUSIVE 模式来真正地执行它们的更新注意一个事务所拥有的锁不会冲突，因此一个事务可以在它持有 SHARE 模式时获得 ROW EXCLUSIVE 模式，但是如果有其他人持有 SHARE 模式时则不能。
为了避免死锁，确保所有的事务在同样的对象上以相同的顺序获得锁，并且如果在一个对象上涉及多种锁模式，事务应该总是首先获得最严格的那种模式。

## 参数
name
要锁定的一个现有表的名称（可以是方案限定的）。
如果给出了多个表，这些表会按照 LOCK TABLE 中的顺序一个一个被锁定。

lockmode
锁模式指定这个锁和哪些锁冲突。I如果没有指定锁模式，那儿将使用最严格的模式 ACCESS EXCLUSIVE。 所模式包括下面的情况：
- ACCESS SHARE：只与 ACCESS EXCLUSIVE 锁模式冲突。SELECT 和 ANALYZE 命令在被引用的表上获得一个这种模式的锁。通常，任何只读取表而不修改它的查询都将获得这种锁模式。

- ROW SHARE：与 EXCLUSIVE 和 ACCESS EXCLUSIVE 锁模式冲突。SELECT FOR SHARE 命令在目标表上获得一个这种模式的锁（加上在被引用但没有选择 FOR SHARE 的任何其他表上的 ACCESS SHARE 锁）。

- ROW EXCLUSIVE：与 SHARE、 SHARE ROW EXCLUSIVE、 EXCLUSIVE 和 ACCESS EXCLUSIVE 锁模式冲突。
命令 INSERT 和 COPY 在目标表上取得这种锁模式（加上在任何其他被引用表上的 ACCESS SHARE 锁）。

- SHARE  UPDATE EXCLUSIVE：与 SHARE UPDATEEXCLUSIVE、SHARE、SHARE ROW EXCLUSIVE、 EXCLUSIVE 和 ACCESS EXCLUSIVE 锁模式冲突。这种模式保护一个表不受并发模式改变和 VACUUM 运行的影响。由 VACUUM （不带 FULL) 取得。

- SHARE：与 ROW EXCLUSIVE、SHARE UPDATE EXCLUSIVE、SHARE ROW EXCLUSIVE、EXCLUSIVE 和 ACCESS EXCLUSIVE锁模式冲突。这种模式保护一个表不受并发数据改变的影响。由 CREATE INDEX 取得。

- SHARE ROW EXCLUSIVE：与 ROW EXCLUSIVE、SHARE UPDATE EXCLUSIVE、SHARE、SHARE ROW EXCLUSIVE、EXCLUSIVE 和 ACCESS EXCLUSIVE 锁模式冲突。该锁模式不能由数据库中的命令直接取得。

- EXCLUSIVE ：与 ROW SHARE、ROW EXCLUSIVE、SHARE UPDATE EXCLUSIVE、SHARE、SHARE ROW EXCLUSIVE、EXCLUSIVE 和 ACCESS EXCLUSIVE 锁模式冲突。这种模式只允许并发的 ACCESS SHARE 锁，即只有来自于表的读操作可以与一个持有该锁模式的事务并行处理。在数据库中，该锁模式由 UPDATE、SELECT FOR UPDATE 和 DELETE 命令取得（这里比 PostgreSQL 更加的严格）。

- ACCESS  EXCLUSIVE：与所有模式的锁冲突 （ACCESS SHARE、ROW SHARE、ROW EXCLUSIVE、SHARE UPDATE EXCLUSIVE、SHARE、SHAREROW EXCLUSIVE、EXCLUSIVE 和 ACCESS EXCLUSIVE）。
这种模式保证持有者是访问该表的唯一事务。由 ALTER TABLE、DROP TABLE、REINDEX、CLUSTER 和 VACUUM FULL 命令取得。这也是未显式指定模式的 LOCK TABLE 命令的默认锁模式。在处理过程中，该锁模式也可以由使用 VACUUM （不带 FULL）命令追加优化表上取得。

NOWAIT
指定 LOCK TABLE 不等待任何冲突锁被释放，如果所指定的锁不能立即获得，那么事务就会中止。

## 注解
LOCK TABLE ... IN ACCESS SHARE MODE 要求目标表上的 SELECT 特权。所有其他形式的 LOCK 要求 UPDATE、DELETE 特权。

LOCK TABLE 只在一个事务块内部有用（BEGIN/COMMIT 对），因为一旦事务结束，锁就会被删除。出现在事务块之外的任何 LOCK TABLE 命令会形成一个自包含的事务，这样锁将在被获得时马上被删除。

LOCK TABLE 只处理表级锁，因此涉及到 ROW 的模式名称在这里都是不正当的。这些模式名称应该通常被解读为用户在被锁定表中获取行级锁的意向。还有，ROW EXCLUSIVE 模式是一个可共享的表锁。就 LOCK TABLE 而言，所有的锁模式都具有相同的语义，只有模式的冲突规则有所不同。关于如何获取一个真正的行级锁的信息， 请见 SELECT 参考文档中的 FOR UPDATE/FOR SHARE。

## 示例
获取一个 SHARE 锁在 films 表上当在表 films_user_comments 上执行插入时：

```sql
BEGIN WORK;
LOCK TABLE films IN SHARE MODE;
SELECT id FROM films 
    WHERE name = 'Star Wars: Episode I - The Phantom Menace';
-- 如果记录没有被返回就ROLLBACK
INSERT INTO films_user_comments VALUES 
    (_id_, 'GREAT! I was waiting for it for so long!');
COMMIT WORK;
```

在将要执行一次删除操作前在表上取一个 SHARE ROW EXCLUSIVE 锁：

```sql
BEGIN WORK;
LOCK TABLE films IN SHARE ROW EXCLUSIVE MODE;
DELETE FROM films_user_comments WHERE id IN
    (SELECT id FROM films WHERE rating < 5);
DELETE FROM films WHERE rating < 5;
COMMIT WORK;
```

## 兼容性
在 SQL 标准中没有 LOCK TABLE，SQL 标准中使用 SET TRANSACTION 指定事务上的并发层次。数据库也支持这样做。

除 ACCESS SHARE、ACCESS EXCLUSIVE 和 SHARE UPDATE EXCLUSIVE 锁模式之外，数据库的锁模式和 LOCK TABLE 语法与 Oracle 中的兼容。

## 另见
BEGIN、SET TRANSACTION、SELECT
