更改资源队列的限制。

## 概要

```sql
ALTER RESOURCE QUEUE name WITH ( queue_attribute=value [, ... ] ) 
```

其中queue_attribute是：

```sql
   ACTIVE_STATEMENTS=integer
   MEMORY_LIMIT='memory_units'
   MAX_COST=float
   COST_OVERCOMMIT={TRUE|FALSE}
   MIN_COST=float
   PRIORITY={MIN|LOW|MEDIUM|HIGH|MAX}
ALTER RESOURCE QUEUE name WITHOUT ( queue_attribute [, ... ] )
```

```sql
   ACTIVE_STATEMENTS
   MEMORY_LIMIT
   MAX_COST
   COST_OVERCOMMIT
   MIN_COST
```

>!资源队列必须有一个 ACTIVE_STATEMENTS 或一个 MAX_COST 值。不要从资源队列中删除这两个 queue_attributes。

## 描述
ALTER RESOURCE QUEUE 更改资源队列的限制。只有超级用户可以更改资源队列。
资源队列必须有一个 ACTIVE_STATEMENTS 或一个 MAX_COST 值（或者可以同时使用）。用户还可以设置或重置资源队列的优先级，以控制与队列相关联的查询使用的可用 CPU 资源的相对份额，或资源队列的内存限制，以控制通过队列提交的所有查询消耗的内存量在段主机上。

ALTER RESOURCE QUEUE WITHOUT 删除先前设置的资源的指定限制。资源队列必须有一个 ACTIVE_STATEMENTS 或一个 MAX_COST 值。不要从资源队列中删除这两个 queue_attributes。

## 参数
name
要更改其限制的资源队列的名称。

ACTIVE_STATEMENTS integer
任何时刻系统中允许在该资源队列中的用户提交的活动语句的数量。ACTIVE_STATEMENTS 的值应该是一个大于0的整数。要把 ACTIVE_STATEMENTS 重置为没有限制，输入一个-1.0值。

MEMORY_LIMIT 'memory_units'
设置从此资源队列中的用户提交的所有语句的总内存配额。内存单位可以用 KB、MB 或 GB 指定。资源队列的最小内存配额为10MB。没有最大值，查询执行时间的上边界受到段主机的物理内存的限制。默认值为无限制（-1）。

MAX_COST float
任何时刻系统中允许在该资源队列中的用户提交的语句的查询优化器总代价。MAX_COST 的值被指定为一个浮点数（例如100.00）或者还可以被指定为一个指数（例如1e+2）。要把 MAX_COST 重置为没有限制，输入一个-1.0值。

COST_OVERCOMMIT boolean
如果资源队列受到基于查询代价的限制，那么管理员可以允许代价过量使用（COST_OVERCOMMIT=TRUE，默认）。这意味着一个超过允许的代价阈值的查询将被允许运行，但只能在系统空闲时运行。如果指定 COST_OVERCOMMIT=FALSE，超过代价限制的查询将总是被拒绝并且绝不会被允许运行。

MIN_COST float
代价低于此限制的查询将不会排队而是立即运行。代价是以取得的磁盘页为单位来衡量的。1.0等于一次顺序磁盘页面读取。MIN_COST 的值被指定为浮点数（例如100.00）或者还能被指定为一个指数（例如1e+2）。要把 MIN_COST 重置为没有限制，输入一个-1.0值。

PRIORITY={MIN|LOW|MEDIUM|HIGH|MAX}
设置与资源队列关联的查询的优先级。具有较高优先级的队列中的查询或语句将在竞争中获得更多的可用 CPU 资源份额。低优先级队列中的查询可能会被延迟，同时执行更高优先级的查询。

## 注解
使用 CREATE ROLE 或 ALTER ROLE 将角色（用户）添加到资源队列中。

## 示例
更改资源队列的活动查询限制：

```sql
ALTER RESOURCE QUEUE myqueue WITH (ACTIVE_STATEMENTS=20);
```

更改资源队列的内存限制：

```sql
ALTER RESOURCE QUEUE myqueue WITH (MEMORY_LIMIT='2GB');
```

将资源队列的最大和最小查询代价限制重置为无限制：

```sql
ALTER RESOURCE QUEUE myqueue WITH (MAX_COST=-1.0, 
  MIN_COST= -1.0);
```

将资源队列的查询代价限制重置为<typora>3^10（or 30000000000.0） 不允许过量使用：

```sql
ALTER RESOURCE QUEUE myqueue WITH (MAX_COST=3e+10, 
  COST_OVERCOMMIT=FALSE);
```

将与资源队列关联的查询的优先级重置为最小级别：

```sql
ALTER RESOURCE QUEUE myqueue WITH (PRIORITY=MIN);
```

去除 MAX_COST 和 MEMORY_LIMIT 资源队列限制：

```sql
ALTER RESOURCE QUEUE myqueue WITHOUT (MAX_COST, MEMORY_LIMIT);
```

## 兼容性
ALTER RESOURCE QUEUE 语句是一个数据库扩展。此命令在标准 PostgreSQL 中不存在。

## 另见
CREATE RESOURCE QUEUE、DROP RESOURCE QUEUE、CREATE ROLE、ALTER ROLE
