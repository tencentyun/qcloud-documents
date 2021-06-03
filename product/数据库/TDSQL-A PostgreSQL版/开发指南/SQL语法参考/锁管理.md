LOCK table 可获取表级锁，该语句只能在事务块中使用，没有 UNLOCK table 语句，事务结束时锁将自动释放。如果使用LOCK 命令对表进行加锁，缺省为最严格的模式 ACCESS EXCLUSIVE。
```
v3=# begin;
BEGIN
v3=# lock table t10;
LOCK TABLE
v3=# select relation::regclass,mode from pg_locks;
 relation |    mode
----------+---------------------
t10   | AccessExclusiveLock
```

## 表级锁
**ACCESS SHARE**
SELECT 命令在被引用的表上获得一个这种模式的锁。通常，任何只读取表而不修改它的查询都将获得这种锁模式。

**ROW SHARE**
SELECT FOR UPDATE 和 SELECT FOR SHARE 命令在目标表上取得一个这种模式的锁 （加上在被引用但没有选择 FOR UPDATE/FOR SHARE 的任何其他表上的 ACCESS SHARE 锁）。

**ROW EXCLUSIVE**
命令 UPDATE、DELETE 和 INSERT 在目标表上取得这种锁模式（加上在任何其他被引用表上的 ACCESS SHARE 锁）。通常，这种锁模式将被任何修改表中数据的命令取得。

**SHARE UPDATE EXCLUSIVE**
由 VACUUM（不带 FULL）、ANALYZE、CREATE INDEX CONCURRENTLY、CREATE STATISTICS 和 ALTER TABLE VALIDATE 以及其他 ALTER TABLE 的变体获得。

**SHARE**
由 CREATE INDEX（不带 CONCURRENTLY）取得。

**SHARE ROW EXCLUSIVE**
由 CREATE COLLATION、CREATE TRIGGER 和很多 ALTER TABLE 的很多形式所获得。

**EXCLUSIVE**
由 REFRESH MATERIALIZED VIEW CONCURRENTLY 获得。

**ACCESS EXCLUSIVE**
由 ALTER TABLE、DROP TABLE、TRUNCATE、REINDEX、CLUSTER、VACUUM FULL 和 REFRESH MATERIALIZED VIEW（不带 CONCURRENTLY）命令获取。ALTER TABLE 的很多形式也在这个层面上获得锁（见 [ALTER TABLE](http://postgres.cn/docs/10/sql-altertable.html)）。这也是未显式指定模式的 LOCK TABLE 命令的默认锁模式。

**冲突的锁模式**
锁之间会互相阻塞、冲突。
<table>
<thead><tr><th rowspan=2>请求的锁模式</th><th colspan=8>当前的锁模式</th></tr></thead>
<tbody><tr>
<td>-</td>
<td>ACCESS  SHARE</td>
<td>ROW SHARE</td>
<td>ROW  EXCLUSIVE</td>
<td>SHARE  UPDATE EXCLUSIVE</td>
<td>SHARE</td>
<td>SHARE ROW  EXCLUSIVE</td>
<td>EXCLUSIVE</td>
<td>ACCESS  EXCLUSIVE</td></tr>
<tr>
<td>ACCESS  SHARE</td>
<td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td></tr>
<tr>
<td>ROW SHARE</td>
<td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>X</td><td>X</td></tr>
<tr>
<td>ROW  EXCLUSIVE</td>
<td>-</td><td>-</td><td>-</td><td>-</td><td>X</td><td>X</td><td>X</td><td>X</td></tr>
<tr>
<td>SHARE  UPDATE EXCLUSIVE</td>
<td>-</td><td>-</td><td>-</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr>
<tr>
<td>SHARE</td>
<td>-</td><td>-</td><td>X</td><td>X</td><td>-</td><td>X</td><td>X</td><td>X</td></tr>
<tr>
<td>SHARE ROW  EXCLUSIVE</td>
<td>-</td><td>-</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr>
<tr>
<td>EXCLUSIVE</td>
<td>-</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr>
<tr>
<td>ACCESS  EXCLUSIVE</td>
<td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr>
</tbody></table>

除了表级锁以外，还有行级锁，行级锁不影响数据查询，它们只阻塞对同一行的写入者和加锁者。

## 死锁
TDSQL-A PostgreSQL版 中，并发执行的事务由于竞争同一个资源会导致死锁。要检查在一个数据库中所有被锁的对象，可以查看 pg_locks 系统视图。
显式锁定的使用可能会增加死锁的可能性，死锁是指两个（或多个）事务相互持有对方想要的锁。可以手动或者以其他方式结束其中一个事务来解决死锁的问题。

查询当前存在的锁：
```
select pid,relation::regclass,mode from pg_locks where relation<>'pg_locks'::regclass::oid;
pid | relation |   mode
-----------+------------+-----------------
27577 | t4   | AccessShareLock
```
可通过系统视图 pg_locks 的 pid 字段和系统视图 pg_stat_activity 关联查询出当前的持有锁的事务信息。
