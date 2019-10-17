定义一个新的资源队列。

## 概要

```sql
CREATE RESOURCE QUEUE name WITH (queue_attribute=value [, ... ])
```

其中queue_attribute是：

```sql
    ACTIVE_STATEMENTS=integer
        [ MAX_COST=float [COST_OVERCOMMIT={TRUE|FALSE}] ]
        [ MIN_COST=float ]
        [ PRIORITY={MIN|LOW|MEDIUM|HIGH|MAX} ]
        [ MEMORY_LIMIT='memory_units' ]
 
 | MAX_COST=float [ COST_OVERCOMMIT={TRUE|FALSE} ]
        [ ACTIVE_STATEMENTS=integer ]
        [ MIN_COST=float ]
        [ PRIORITY={MIN|LOW|MEDIUM|HIGH|MAX} ]
        [ MEMORY_LIMIT='memory_units' ]
```

## 描述
对数据库负载管理，创建一个新的资源队列。资源队列必须要有 ACTIVE_STATEMENTS 或者 MAX_COST 值（也可以两个都有）。只有超级用户可以创建一个资源队列。

带有 ACTIVE_STATEMENTS 阈值的资源队列在查询数量上做了最大限制，该查询能够被分配到该队列上的角色所执行。它（阈值）控制了活跃查询的数量，活跃查询是在同一时间允许运行的查询。ACTIVE_STATEMENTS 的值应当是一个大于0的值。

带有 MAX_COST 阈值的资源队列在查询总代价上设置了一个最大限制，该查询能够被分配到该队列上的角色所执行。代价是按照数据库查询计划器（正如查询的 EXPLAIN 输出显示的）确定的查询的\*估计总成本*来进行衡量的。
因此，管理员必须熟悉系统典型执行的查询，以对队列设置一个合适的代价阈值。代价是以磁盘页的提取为单位进行衡量的。1.0等于一个顺序的磁盘页面的读取。MAX_COST 的值被指定为浮点数（例如100.0）或者也可以被指定为指数（例如1e + 2）。
如果基于成本阈值限制资源队列，则管理员可以允许 COST_OVERCOMMIT = TRUE（默认值）。这意味着超过成本阈值的查询将被允许查询，但只有当系统空闲的时候才行。如果指定 COST_OVERCOMMIT = FALSE，超过成本限制的查询将始终被拒绝，从不允许执行。对 MIN_COST 指定一个值，这将允许管理员定义小查询的成本，低于该成本的小查询将免除排队的烦恼。

如果没有给 ACTIVE_STATEMENTS 或者 MAX_COST设定值，将被设置为默认值 -1（意味着没有限制）。在定义了资源队列之后，用户必须使用 [ALTER ROLE](https://gp-docs-cn.github.io/docs/ref_guide/sql_commands/ALTER_ROLE.html#topic1) 或者 [CREATE ROLE](https://gp-docs-cn.github.io/docs/ref_guide/sql_commands/CREATE_ROLE.html#topic1) 命令向队列分配角色。

用户可以选择性的分配 PRIORITY 给一个资源队列来控制与（和其他资源队列相关的）队列相关查询使用的可用 CPU 资源的相对份额。如果没有指定 PRIORITY的值，则和队列相关的查询默认优先级为 MEDIUM。

带有可选择的 MEMORY_LIMIT 阈值的资源队列对内存数量上设置了最大限制。该内存是 Segment 主机上被所有通过资源队列提交的查询所使用的。这决定了在 Segment 主机上，在一次查询执行中，一个查询的所有工作进程所能消耗的总内存的数量。推荐 MEMORY_LIMIT 和 ACTIVE_STATEMENTS 联合使用而不是和 MAX_COST。
基于语句的队列每个查询分配的默认内存量为：MEMORY_LIMIT / ACTIVE_STATEMENTS。
基于成本队列每个查询分配的默认内存量为：MEMORY_LIMIT * (query_cost / MAX_COST)。

默认内存分配可以使用 statement_mem 服务器配置参数在每个查询的基础上被覆盖。前提是不超过 MEMORY_LIMIT 或 max_statement_mem。例如要为特定查询分配更多的内存。

```sql
=> SET statement_mem='2GB';
=> SELECT * FROM my_big_table WHERE column='value' ORDER BY id;
=> RESET statement_mem;
```

该 MEMORY_LIMIT 值对于用户所有的资源队列都不应该超过 Segment 主机上的物理内存。如果工作负载在多个队列中交错，内存分配可以重新拟定。但是，如果 Segment 主机在 gp_vmem_protect_limit 指定的内存限制被超的话，执行中查询可以被取消。

## 参数

name
资源队列的名字。

ACTIVE_STATEMENTS integer
带有 ACTIVE_STATEMENTS 阈值的资源队列限制了分配到队列角色所能够执行的查询的数量。它（阈值）控制着活跃查询的数量，活跃查询是在同一时间允许运行的查询数量。ACTIVE_STATEMENTS 的值应该是一个大于0的整数值。

MEMORY_LIMIT 'memory_units'
对于所有从该资源队列中提交的语句设置总内存配额。内存单元可以指定为KB、MB 或者 GB。对于一个资源队列来说最小的内存配额是10MB，没有最大限值，但是查询执行的上边界由 Segment 主机的物理内存所限定。默认值时没有限制为（-1）。

MAX_COST float
带有 MAX_COST 阈值的资源队列对查询代价设置了一个最大限制。该查询能够被分配到该队列的用户所执行。代价由数据库查询优化器（正如查询 EXPLAIN 输出显示的）确定的查询的\*估计共代价*进行衡量的。 因此，管理员必须要熟悉在系统中执行的典型查询，以对队列设置一个合理的阈值。成本以磁盘页提取为单位进行衡量；1.0等于顺序读取一个磁盘页。MAX_COST 的值可以被指定为浮点数（例如100.0） ，或者可以被指定为（例如 1e+2）。

COST_OVERCOMMIT boolean
如果基于 MAX_COST 限制资源队列，则管理员可以允许 COST_OVERCOMMIT（默认）。这意味着超过允许的成本阈值的查询将被允许运行，但只有在系统空闲时才能运行。如果指定 COST_OVERCOMMIT = FALSE ，超过成本限制的查询将始终被拒绝，从不允许运行。

MIN_COST float
该是最小查询的最小查询成本限制。成本低于此限制的查询将不会排队等待立即运行。成本由数据库查询优化器（正如查询 EXPLAIN 输出所示）确定的查询的\*估计总成本* 所衡量。 因此，管理员必须熟悉通常在系统上执行的查询，以便为被认为是小型查询设置适当的成本。成本是以磁盘页提取为单位来衡量的；1.0等于一个顺序的磁盘页面读取。MIN_COST 的值可以被指定为浮点数（例如100.0），或也可以被指定为一个指数（例如 1e+2）。

PRIORITY={MIN|LOW|MEDIUM|HIGH|MAX}
设置和资源队列相关查询的优先级。队里中拥有高优先级的查询和语句会在竞争中拥有更大的可用 CPU 资源份额。队列中拥有低优先级的查询将会被推迟，同时，更高优先级的查询将会被执行。如果没有指定优先级，和队列相关的查询的优先级为 MEDIUM。

## 注意
使用 gp_toolkit.gp_resqueue_status 系统视图查看限制设置和当前资源队列的状态：

```sql
SELECT * from gp_toolkit.gp_resqueue_status WHERE 
  rsqname='queue_name';
```

还有一个叫 pg_stat_resqueues 的系统视图，这显示了资源队列随时间的统计指标。但是为了使用该视图，用户必须启用 stats_queue_level 服务器配置参数。更多使用资源队列的信息请参阅“数据库管理指南”的“管理工作负载和资源”。

CREATE RESOURCE QUEUE 不能再事务中运行。

此外，在 EXPLAIN ANALYZE 命令执行期间执行的 SQL 命令被从资源队列排除。

## 示例

创建一个活跃查询限制为20的资源队列：

```sql
CREATE RESOURCE QUEUE myqueue WITH (ACTIVE_STATEMENTS=20);
```

创建一个活跃查询限制为20的资源队列并且总内存限制为2000MB （在执行时，每个查询会被分配100MB端主机内存)：

```sql
CREATE RESOURCE QUEUE myqueue WITH (ACTIVE_STATEMENTS=20, 
  MEMORY_LIMIT='2000MB');
```

创建一个查询代价限制为3000.0的资源队列：

```sql
CREATE RESOURCE QUEUE myqueue WITH (MAX_COST=3000.0);
```

创建一个查询代价限制为310 的资源队列（或者 30000000000.0）并且不允许复写。允许500以下的小查询立即运行：

```sql
CREATE RESOURCE QUEUE myqueue WITH (MAX_COST=3e+10, 
  COST_OVERCOMMIT=FALSE, MIN_COST=500.0);
```

创建一个带有活跃查询限制和查询代价限制的资源队列：

```sql
CREATE RESOURCE QUEUE myqueue WITH (ACTIVE_STATEMENTS=30, 
  MAX_COST=5000.00);
```

创建一个带有活跃查询限制为5并且有最大优先级设置的资源队列：

```sql
CREATE RESOURCE QUEUE myqueue WITH (ACTIVE_STATEMENTS=5, 
  PRIORITY=MAX);
```

## 兼容性

CREATE RESOURCE QUEUE 是数据库扩展，在 SQL 标准中没有资源队列和工作负载管理的规定。

## 另见

ALTER ROLE、CREATE ROLE、ALTER RESOURCE QUEUE、DROP RESOURCE QUEUE
