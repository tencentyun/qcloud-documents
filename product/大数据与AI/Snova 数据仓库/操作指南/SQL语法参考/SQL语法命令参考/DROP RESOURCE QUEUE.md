移除一个资源队列。

## 概要
```sql
DROP RESOURCE QUEUE queue_name
```

## 描述
该命令从数据库中移除一个负载管理资源队列。为了删除一个资源队列，要删除的队列不能有任何角色分配给它，也不能有任何的语句在队列中等待。只有超级用户能够删除资源队列。

## 参数
queue_name：将要被删除的资源队列的名称。

## 注解
通过命令 ALTER ROLE 从一个资源队列中移除一个用户。为了看到关于所有的资源队列的当前活动的查询，执行下面将 pg_locks 表、pg_roles 和 pg_resqueue 表相连接的查询：
```sql
SELECT rolname, rsqname, locktype, objid, transaction, pid, 
mode, granted FROM pg_roles, pg_resqueue, pg_locks WHERE 
pg_roles.rolresqueue=pg_locks.objid AND 
pg_locks.objid=pg_resqueue.oid;
```
为了看到分配到一个资源队列的角色，可以在 pg_roles 和 pg_resqueue 两个系统目录表执行下面查询：
```sql
SELECT rolname, rsqname FROM pg_roles, pg_resqueue WHERE 
pg_roles.rolresqueue=pg_resqueue.oid;
```

## 示例
从一个资源队列中移除一个角色（同时移动该角色到默认的资源队列 pg_default）：
```sql
ALTER ROLE bob RESOURCE QUEUE NONE;
```
移除一个名为 adhoc 的资源队列：
```sql
DROP RESOURCE QUEUE adhoc;
```

## 兼容性
DROP RESOURCE QUEUE 语句是一个数据库的扩展。

## 另见
ALTER RESOURCE QUEUE、CREATE RESOURCE QUEUE、ALTER ROLE
