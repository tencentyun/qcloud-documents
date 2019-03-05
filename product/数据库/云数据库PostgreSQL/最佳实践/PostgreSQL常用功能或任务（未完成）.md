

### 创建角色

初始化数据库实例是，将为您创建一个postgresql管理员角色，该角色是一个预定义的系统角色，功能类似于 PostgreSQL 超级用户角色，具有对数据库实例的大多数权限，但有一些限制，例如不能修改系统库表，不能修改文件系统等。
>编者注：在PostgreSQL 里没有区分“用户”和“角色”的概念，`CREATE USER`为 `CREATE ROLE`的别名，这两个命令几乎是完全相同的，唯一的区别是`CREATE USER` 命令创建的用户默认带有LOGIN属性，而`CREATE ROLE` 命令创建的用户默认不带LOGIN属性(CREATE USER is equivalent to CREATE ROLE except that CREATE USER assumes LOGIN by default, while CREATE ROLE does not)。因此您也可以理解为PostgreSQL的角色类似于MySQL的登录用户。

创建角色方法如下：

```
请添加代码
```



### 管理 PostgreSQL 数据库访问

默认情况下，在创建 PostgreSQL 数据库对象后，这些对象会获得“public”访问特权。您可以撤消数据库的所有特权，然后在需要时显式添加回这些特权。

作为主用户，您可以使用以下命令格式从数据库中删除所有特权：

```
请添加代码
```

然后，您可以将特权添加回用户。例如，以下命令向名为 mytestuser 的用户授予对名为 test 的数据库的连接访问权限。 

```
请添加代码
```

 请注意，在本地实例中，您可以在 pg_hba.conf 文件中指定数据库特权，但在将 PostgreSQL 用于 Amazon RDS 时，更佳的做法是将特权限制在 Postgres 级别。更改 pg_hba.conf 文件更改需要重新启动服务器，因此您无法在 Amazon RDS 中编辑 pg_hba.conf，但会立即在 Postgres 级别发生特权变化。





### 使用 PostgreSQL 参数

postgresql.conf 文件中为本地 PostgreSQL 实例设置的 PostgreSQL 参数保留在数据库实例的数据库参数组中。如果使用默认参数组创建数据库实例，则参数设置在一个名为 default.postgres9.3 的参数组中。

 创建数据库实例时，将加载关联的数据库参数组中的参数。可通过更改该参数组中的值，修改参数值。如果有更改参数值的安全权限，则还可使用 ALTER DATABASE、ALTER ROLE 和 SET 命令这样做。注意，无法使用命令行 postgres 命令和 env PGOPTIONS 命令，因为将无权访问主机。 

偶尔可能难以跟踪 PostgreSQL 参数设置。使用以下命令列出当前的参数设置和默认值： 
select name, setting, boot_val, reset_val, unit
from pg_settings
order by name;  
 有关输出值的解释，请参阅 PostgreSQL 文档中的 pg_settings 主题。

 如果设置的内存设置对于 max_connections、shared_buffers 或 effective_cache_size 来说过大，则将使 PostgreSQL 实例无法启动。注意，您可能不熟悉某些参数使用的单位；例如，shared_buffers 设置服务器使用的 8 KB 共享内存缓冲区的数量。 

当实例尝试启动，但错误的参数设置使其无法启动时，将以下错误写入 postgres.log 文件。
2013-09-18 21:13:15 UTC::@:[8097]:FATAL:  could not map anonymous shared
memory: Cannot allocate memory
2013-09-18 21:13:15 UTC::@:[8097]:HINT:  This error usually means that 
PostgreSQL's request for a shared memory segment exceeded available memory or 
swap space. To reduce the request size (currently 3514134274048 bytes), reduce 
PostgreSQL's shared memory usage, perhaps by reducing shared_buffers or 
max_connections.  
 PostgreSQL 参数有两种类型，固定和动态。固定参数要求重启数据库实例，然后再应用这些参数。动态参数可立即应用。下表显示可为 PostgreSQL 数据库实例修改的参数以及参数类型：










参数名称
 

应用类型
 

说明
 




application_name
 
动态

设置要在统计数据和日志中报告的应用程序名称。




array_nulls
 
动态

允许在阵列中输入 NULL 元素。




authentication_timeout
 
动态

设置允许完成客户端身份验证的最长时间。




autovacuum
 
动态

启动 autovacuum 子进程。




autovacuum_analyze_scale_factor
 
动态

analyze 之前插入、更新或删除元组的次数，以对于 reltuple 的占比计。




autovacuum_analyze_threshold
 
动态

analyze 之前插入、更新或删除元组的最小次数。




autovacuum_naptime
 
动态

两次 autovacuum 运行之间的睡眠时间。




autovacuum_vacuum_cost_delay
 
动态

autovacuum 的真空开销延迟，以毫秒计。




autovacuum_vacuum_cost_limit
 
动态

autovacuum 在小睡之前可用的真空开销量。




autovacuum_vacuum_scale_factor
 
动态

vacuum 之前更新或删除元组的次数，以对于 reltuple 的占比计。




autovacuum_vacuum_threshold
 
动态

vacuum 之前更新或删除元组的最小次数。




backslash_quote
 
动态

设置字符串字面值中是否允许有反斜杠 (\)。




bgwriter_delay
 
动态

后台写入器在两轮之间的睡眠时间。




bgwriter_lru_maxpages
 
动态

后台写入器每轮要刷新的最大 LRU 页数。




bgwriter_lru_multiplier
 
动态

每轮要释放的平均缓冲区用量的倍数。




bytea_output
 
动态

设置 bytea 的输出格式。




check_function_bodies
 
动态

在 CREATE FUNCTION 期间检查函数体。




checkpoint_completion_target
 
动态

在检查点期间刷新脏缓冲区所用的时间，以对于检查点间隔的占比计。




checkpoint_segments
 
动态

设置日志段中自动 WAL 检查点之间的最大距离。




checkpoint_timeout
 
动态

设置自动 WAL 检查点之间的最长时间。




checkpoint_warning
 
动态

如果填充检查点段的频率高于此，则启用警告。




client_encoding
 
动态

设置客户端的字符集编码。




client_min_messages
 
动态

设置发送到客户端的消息级别。




commit_delay
 
动态

设置事务提交与将 WAL 刷新到磁盘之间的延迟，以微秒计。




commit_siblings
 
动态

设置执行 commit_delay 之前同时打开的最少事务数。




constraint_exclusion
 
动态

使计划程序可使用约束优化查询。




cpu_index_tuple_cost
 
动态

设置计划程序对索引扫描期间处理每个索引条目的开销的估算。




cpu_operator_cost
 
动态

设置计划程序对处理每个运算符或函数调用的开销的估算。




cpu_tuple_cost
 
动态

设置计划程序对处理每个元组（行）的开销的估算。




cursor_tuple_fraction
 
动态

设置计划程序对光标将检索的行占比的估算。




datestyle
 
动态

设置日期和时间值的显示格式。




deadlock_timeout
 
动态

设置在检查死锁之前等待锁定的时间。




debug_pretty_print
 
动态

缩进分析树和计划树的显示内容。




debug_print_parse
 
动态

记录每个查询的分析树。




debug_print_plan
 
动态

记录每个查询的执行计划。




debug_print_rewritten
 
动态

记录每个查询重写的分析树。




default_statistics_target
 
动态

设置默认统计数据目标。




default_tablespace
 
动态

设置要从中创建表和索引的默认表空间。




default_transaction_deferrable
 
动态

设置新事务的默认可延迟状态。




default_transaction_isolation
 
动态

设置每个新事务的事务隔离级别。




default_transaction_read_only
 
动态

设置新事务的默认只读状态。




default_with_oids
 
动态

创建默认具有 OID 新表。




effective_cache_size
 
动态

设置计划程序对于磁盘缓存大小的假设。




effective_io_concurrency
 
动态

磁盘子系统可有效处理的并行请求数。




enable_bitmapscan
 
动态

使计划程序可使用位图扫描计划。




enable_hashagg
 
动态

使计划程序可使用哈希聚合计划。




enable_hashjoin
 
动态

使计划程序可使用哈希联接计划。




enable_indexscan
 
动态

使计划程序可使用索引扫描计划。




enable_material
 
动态

使计划程序可使用具体化。




enable_mergejoin
 
动态

使计划程序可使用合并联接计划。




enable_nestloop
 
动态

使计划程序可使用嵌套循环的联接计划。




enable_seqscan
 
动态

使计划程序可使用顺序扫描计划。




enable_sort
 
动态

使计划程序可使用显式排序步骤。




enable_tidscan
 
动态

使计划程序可使用 TID 扫描计划。




escape_string_warning
 
动态

警告在普通字符串字面值中有反斜杠 (\) 转义符。




extra_float_digits
 
动态

设置所显示的浮点值位数。




from_collapse_limit
 
动态

设置超出其即不折叠子查询的 FROM 列表大小。




fsync
 
动态

强制将更新同步到磁盘。




full_page_writes
 
动态

在检查点后首次修改时向 WAL 写入整页。




geqo
 
动态

启用基因查询优化。




geqo_effort
 
动态

GEQO：用于设置其他 GEQO 参数默认值的工作量。




geqo_generations
 
动态

GEQO：算法的迭代次数。




geqo_pool_size
 
动态

GEQO：群体中的个体数。




geqo_seed
 
动态

GEQO：随机路径选择的种子。




geqo_selection_bias
 
动态

GEQO：群体中的选择性压力。




geqo_threshold
 
动态

设置超出其即使用 GEQO 的 FROM 项阈值。




gin_fuzzy_search_limit
 
动态

通过允许由 GIN 进行的精确搜索得出的最大结果数。




intervalstyle
 
动态

设置间隔值的显示格式。




join_collapse_limit
 
动态

设置超出其即不平展 JOIN 结构的 FROM 列表大小。




lc_messages
 
动态

设置显示消息的语言。




lc_monetary
 
动态

设置用于使货币金额格式化的区域设置。




lc_numeric
 
动态

设置用于使数字格式化的区域设置。




lc_time
 
动态

设置用于使日期和时间值格式化的区域设置。




log_autovacuum_min_duration
 
动态

设置超出其即记录 autovacuum 操作的最短执行时间。




log_checkpoints
 
动态

记录每个检查点。




log_connections
 
动态

记录每个成功的连接。




log_disconnections
 
动态

记录会话结束，包括持续时间。




log_duration
 
动态

记录每个完成的 SQL 语句的持续时间。




log_error_verbosity
 
动态

设置记录消息的详细程度。




log_executor_stats
 
动态

向服务器日志写入执行者性能统计数据。




log_filename
 
动态

设置日志文件的文件名模式。




log_hostname
 
动态

在连接日志中记录主机名。




log_lock_waits
 
动态

记录长锁定等待次数。




log_min_duration_statement
 
动态

设置超出其即记录语句的最短执行时间。




log_min_error_statement
 
动态

导致记录所有产生此水平或此水平之上错误的语句。




log_min_messages
 
动态

设置记录的消息级别。




log_parser_stats
 
动态

向服务器日志写入分析器性能统计数据。




log_planner_stats
 
动态

向服务器日志写入计划程序性能统计数据。




log_rotation_age
 
动态

将在 N 分钟后进行日志文件自动轮换。




log_rotation_size
 
动态

将在 N KB 后进行日志文件自动轮换。




log_statement
 
动态

设置所记录的语句类型。




log_statement_stats
 
动态

向服务器日志写入累计性能统计数据。




log_temp_files
 
动态

记录对大于此 KB 数的临时文件的使用情况。




maintenance_work_mem
 
动态

设置要用于维护操作的最大内存。




max_stack_depth
 
动态

设置最大堆栈长度，以 KB 计。




max_standby_archive_delay
 
动态

设置在有热备用服务器处理已存档的 WAL 数据时取消查询之前的最大延迟。




max_standby_streaming_delay
 
动态

设置在有热备用服务器处理流式 WAL 数据时取消查询之前的最大延迟。




quote_all_identifiers
 
动态

在生成 SQL 片段时向所有标识符添加引号 (")。




random_page_cost
 
动态

设置计划程序对非连续提取磁盘页面的开销的估算。




cdb.log_retention_period
 
动态

Amazon RDS 将删除 N 分钟之前的 PostgreSQL 日志。




search_path
 
动态

设置针对非架构限定名称的架构搜索顺序。




seq_page_cost
 
动态

设置计划程序对连续提取磁盘页面的开销的估算。




session_replication_role
 
动态

设置触发器和重写规则的会话行为。




sql_inheritance
 
动态

导致在各种命令中默认加入子表。




ssl_renegotiation_limit
 
动态

设置在重新协商加密密钥之前发送和接收的流量。




standard_conforming_strings
 
动态

导致 ... 字符串按字面处理反斜杠。




statement_timeout
 
动态

设置允许任何语句的最长持续时间。




synchronize_seqscans
 
动态

启用同步顺序扫描。




synchronous_commit
 
动态

设置当前事务同步级别。




tcp_keepalives_count
 
动态

重新传输 TCP 保持连接信号的最大次数.




tcp_keepalives_idle
 
动态

发出两次 TCP 保持连接信号之间的时间。




tcp_keepalives_interval
 
动态

两次 TCP 保持连接信号重新传输之间的时间。




temp_buffers
 
动态

设置每个会话使用的临时缓冲区的最大数量。




temp_tablespaces
 
动态

选择用于临时表和排序文件的表空间。




timezone
 
动态

设置用于显示和解译时间戳的时区。




track_activities
 
动态

收集有关执行命令的信息。




track_counts
 
动态

收集有关数据库活动的统计数据。




track_functions
 
动态

收集有关数据库活动的函数级别统计数据。




track_io_timing
 
动态

收集有关数据库活动的时序统计数据。




transaction_deferrable
 
动态

指示是否将某个只读可序列化事务推迟到执行它不会发生序列化失败时。




transaction_isolation
 
动态

设置当前事务隔离级别。




transaction_read_only
 
动态

设置当前事务只读状态。




transform_null_equals
 
动态

将 expr=NULL 视为 expr IS NULL。




update_process_title
 
动态

更新进程标题以显示活动的 SQL 命令。




vacuum_cost_delay
 
动态

真空开销延迟，以毫秒计。




vacuum_cost_limit
 
动态

小睡之前可用的真空开销量。




vacuum_cost_page_dirty
 
动态

由真空弄脏的页面的真空开销。




vacuum_cost_page_hit
 
动态

在缓冲区缓存中找到的页面的真空开销。




vacuum_cost_page_miss
 
动态

在缓冲区缓存中未找到的页面的真空开销。




vacuum_defer_cleanup_age
 
动态

真空和热清理应推迟的事务数（如有）。




vacuum_freeze_min_age
 
动态

真空应冻结表格行的最短期限。




vacuum_freeze_table_age
 
动态

真空应扫描整个表以冻结元组的期限。




wal_writer_delay
 
动态

两次 WAL 刷新之间的 WAL 写入器睡眠时间。




work_mem
 
动态

设置要用于查询工作区的最大内存。




xmlbinary
 
动态

设置如何将二进制值编码到 XML 中。




xmloption
 
动态

设置要将隐式分析和序列化操作中的 XML 数据视为文档还是内容片段。




autovacuum_freeze_max_age
 
静态

对表进行 autovacuum 以防事务 ID 重现的期限。




autovacuum_max_workers
 
静态

设置同时运行的 autovacuum 工作者的最大数量。




max_connections
 
静态

设置最大并行连接数。




max_files_per_process
 
静态

设置同时为每个服务器进程打开的最大文件数。




max_locks_per_transaction
 
静态

设置每个事务的最大锁定数。




max_pred_locks_per_transaction
 
静态

设置每个事务的最大谓词锁定数。




max_prepared_transactions
 
静态

设置同时准备的最大事务数。




shared_buffers
 
静态

设置服务器使用的共享内存缓冲区数。




ssl
 
静态

启用 SSL 连接。




track_activity_query_size
 
静态

设置为 pg_stat_activity.current_query 保留的大小，以字节计。




wal_buffers
 
静态

设置 WAL 的共享内存中的磁盘页面缓冲区数。


Amazon RDS 对所有参数均使用默认的 PostgreSQL 单位。下表显示每个参数的 PostgreSQL 单位值。









参数名称
 

单位
 




effective_cache_size
 
8 KB




segment_size
 
8 KB




shared_buffers
 
8 KB




temp_buffers
 
8 KB




wal_buffers
 
8 KB




wal_segment_size
 
8 KB




log_rotation_size
 
KB




log_temp_files
 
KB




maintenance_work_mem
 
KB




max_stack_depth
 
KB




ssl_renegotiation_limit
 
KB




temp_file_limit
 
KB




work_mem
 
KB




log_rotation_age
 
min




autovacuum_vacuum_cost_delay
 
ms




bgwriter_delay
 
ms




deadlock_timeout
 
ms




lock_timeout
 
ms




log_autovacuum_min_duration
 
ms




log_min_duration_statement
 
ms




max_standby_archive_delay
 
ms




max_standby_streaming_delay
 
ms




statement_timeout
 
ms




vacuum_cost_delay
 
ms




wal_receiver_timeout
 
ms




wal_sender_timeout
 
ms




wal_writer_delay
 
ms




archive_timeout
 
s




authentication_timeout
 
s




autovacuum_naptime
 
s




checkpoint_timeout
 
s




checkpoint_warning
 
s




post_auth_delay
 
s




pre_auth_delay
 
s




tcp_keepalives_idle
 
s




tcp_keepalives_interval
 
s




wal_receiver_status_interval
 
s






在 Amazon RDS 上使用 PostgreSQL Autovacuum

PostgreSQL 数据库的 autovacuum 功能是我们强烈向您推荐的一项功能，您可使用此功能保持 PostgreSQL 数据库实例正常运行。Autovacuum 自动执行 VACUUM 和 ANALYZE 命令；使用 autovacuum 是 PostgreSQL 所需的而不是 Amazon RDS 强制的，并且使用此功能对于获得良好性能是至关重要的。默认情况下，为所有新的 Amazon RDS PostgreSQL 数据库实例启用此功能，并将正确设置相关的配置参数。由于默认值是某个通用值，因此您可以通过针对特定工作负载来优化参数中受益。此部分可以帮助您执行所需的 autovacuum 优化。


Topics
?维护工作内存
?确定数据库中的表是否需要 Vacuum 操作
?确定哪些表当前有资格经销 Autovacuum 操作
?确定 Autovacuum 当前是否正在运行以及运行时长
? 执行手动 Vacuum 冻结
? 在 Autovacuum 正在运行时重新为表建立索引
? 其他影响 Autovacuum 的参数
?Autovacuum 日志记录





维护工作内存

影响 autovacuum 性能的最重要参数之一是 maintenance_work_mem 参数。此参数确定您为 autovacuum 分配多少内存以用于扫描数据表和保留将执行 vacuum 操作的所有行 ID。如果将 maintenance_work_mem 参数的值设得太小，则 vacuum 过程可能必须扫描表多次才能完成其工作，这可能会影响性能。

在执行计算以确定 maintenance_work_mem 参数值时，需记住以下两点：

?
此参数的默认单位为 KB

?
maintenance_work_mem 参数与 autovacuum_max_workers 参数结合使用。如果您有多个小型表，请分配更多的 autovacuum_max_workers 和更少的 maintenance_work_mem。如果您拥有大型表（假设表的大小大于 100GB），则请分配更多内存和更少工作线程。您需要分配有足够的内存才能对最大的表成功完成操作。每个 autovacuum_max_workers 均可使用您分配的内存，因此您应确保工作线程和内存的组合等于要分配的总内存。


 一般来说，对于大型主机，将 maintenance_work_mem 参数设置为一个介于 1 GB 和 2 GB 之间的值。对于特大型主机，将此参数设置为一个介于 1 GB 和 4 GB 之间的值。为此参数设置的值应取决于工作负载。Amazon RDS 已更新此默认值以使此参数为 GREATEST({DBInstanceClassMemory/63963136*1024},65536)。 





确定数据库中的表是否需要 Vacuum 操作

在 PostgreSQL 执行动态操作以避免数据丢失之前，PostgreSQL 数据库可具有 20 亿“正在进行的”未执行 unvacuum 操作的事务。如果未执行 unvacuum 操作的事务数达到 (2^31 - 10,000,000)，则日志将开始发出需要执行 vacuum 操作的警告。如果未 vacuum 的事务的数目 (2^31 - 1,000,000)，则 PostgreSQL 会将数据库设置为只读并需要脱机的、单用户的独立 vacuum。这需要停机几小时或几天（取决于规模）。在 Postgres 文档中找到了 TransactionID 重现的非常详细的说明。

以下查询可用于显示数据库中未执行 vacuum 操作的事务的数目。数据库的 pg_database 行的 datfrozenxid 列是数据库中出现的正常 XID 的下限；它是数据库中的每表 relfrozenxid 值的最小值。 
select datname, age(datfrozenxid) from pg_database order 
by age(datfrozenxid) desc limit 20;
例如，运行上述查询的结果可能是：
datname    | age
mydb       | 1771757888
template0  | 1721757888
template1  | 1721757888
cdbadmin   | 1694008527
postgres   | 1693881061
(5 rows)  
 当数据库的期限命中数为 20 亿时，TransactionID (XID) 重现将出现，并且数据库仅处于只读状态。此查询可用于生成指标，并且一天可运行几次。默认情况下，将设置 autovacuum 以确保事务期限不超过 200,000,000 (autovacuum_freeze_max_age)。

示例监控策略可能类似于：

?
Autovacuum_freeze_max_age 设置为 2 亿。

?
如果表命中 5 亿个未执行 vacuum 操作的事务，则将触发低严重性警报。这是一个不合理的值，但它指示 autovacuum 未保持同步。

?
如果表期限为 10 亿，这将被视为可操作的警报。通常，您出于性能原因，需要使期限更接近 autovacuum_freeze_max_age。建议执行使用以下步骤的调查。

?
如果表命中 15 亿个未执行 vacuum 操作的事务，则将触发高严重性警报。根据数据库使用 XID 的频率，此警报将指示系统运行 autovacuum 的时间不多了，并且应考虑即时解决方案。


如果表持续违反这些阈值，则您需要进一步修改 autovacuum 参数。默认情况下，VACUUM（已禁用基于成本的延迟）比默认的 autovacuum 更积极，但对整个系统来说更具侵入性。

我们提供了以下建议：

?
了解和启用监控机制，以便您了解最早的事务的期限。

?
对于更复杂的表，在维护时段内定期执行手动 vacuum 冻结操作，并依赖 autovacuum。有关执行手动 vacuum 冻结的信息，请参阅 执行手动 Vacuum 冻结






确定哪些表当前有资格经销 Autovacuum 操作

通常，它是需要执行 vacuum 操作的一个或两个表。其 relfrozenxid 值多于旧 autovacuum_freeze_max_age 事务数的表始终是 autovacuum 操作的目标。否则，如果元组数因上一个 VACUUM 超出“vacuum 阈值”而变得过时，则对表执行 vacuum 操作。

autovacuum 阈值的定义如下：
Vacuum threshold = vacuum base threshold + vacuum scale factor * number of tuples
在连接到数据库时，运行以下查询可查看 autovacuum 认为有资格执行 vacuum 操作的表的列表：
WITH vbt AS (SELECT setting AS autovacuum_vacuum_threshold FROM 
pg_settings WHERE name = 'autovacuum_vacuum_threshold')
    , vsf AS (SELECT setting AS autovacuum_vacuum_scale_factor FROM 
pg_settings WHERE name = 'autovacuum_vacuum_scale_factor')
    , fma AS (SELECT setting AS autovacuum_freeze_max_age FROM 
pg_settings WHERE name = 'autovacuum_freeze_max_age')
    , sto AS (select opt_oid, split_part(setting, '=', 1) as param, 
split_part(setting, '=', 2) as value from (select oid opt_oid, 
unnest(reloptions) setting from pg_class) opt)
SELECT
    '"'||ns.nspname||'"."'||c.relname||'"' as relation
    , pg_size_pretty(pg_table_size(c.oid)) as table_size
    , age(relfrozenxid) as xid_age
    , coalesce(cfma.value::float, autovacuum_freeze_max_age::float) 
autovacuum_freeze_max_age
    , (coalesce(cvbt.value::float, autovacuum_vacuum_threshold::float) 
+ coalesce(cvsf.value::float,autovacuum_vacuum_scale_factor::float) * 
pg_table_size(c.oid)) as autovacuum_vacuum_tuples
    , n_dead_tup as dead_tuples
FROM pg_class c join pg_namespace ns on ns.oid = c.relnamespace
join pg_stat_all_tables stat on stat.relid = c.oid
join vbt on (1=1) join vsf on (1=1) join fma on (1=1)
left join sto cvbt on cvbt.param = 'autovacuum_vacuum_threshold' and 
c.oid = cvbt.opt_oid
left join sto cvsf on cvsf.param = 'autovacuum_vacuum_scale_factor' and 
c.oid = cvsf.opt_oid
left join sto cfma on cfma.param = 'autovacuum_freeze_max_age' and 
c.oid = cfma.opt_oid
WHERE c.relkind = 'r' and nspname <> 'pg_catalog'
and (
    age(relfrozenxid) >= coalesce(cfma.value::float, 
autovacuum_freeze_max_age::float)
    or
    coalesce(cvbt.value::float, autovacuum_vacuum_threshold::float) + 
coalesce(cvsf.value::float,autovacuum_vacuum_scale_factor::float) * 
pg_table_size(c.oid) <= n_dead_tup
   -- or 1 = 1
)
ORDER BY age(relfrozenxid) DESC LIMIT 50;




确定 Autovacuum 当前是否正在运行以及运行时长

如果需要手动对表执行 vacuum 操作，您需要确定 autovacuum 当前是否正在运行。如果它当前正在运行，则您可能需要调整参数以使其更有效地运行，或者终止 autovacuum 以便手动运行 VACUUM。

使用以下查询可确定 autovacuum 是否正在运行以及它已运行的时长。这需要 RDS Postgres 9.3.12+、9.4.7+ 和 9.5.2+ 才能完全了解当前正在运行的 cdbadmin 过程。
SELECT datname, usename, pid, waiting, current_timestamp - xact_start 
AS xact_runtime, query
FROM pg_stat_activity WHERE upper(query) like '%VACUUM%' ORDER BY 
xact_start;
在运行查询后，您将看到类似以下内容的输出：
datname | usename  |  pid  | waiting |      xact_runtime       | 
query  --
 mydb    | cdbadmin | 16473 | f       | 33 days 16:32:11.600656 | 
 autovacuum: VACUUM ANALYZE public.mytable1 (to prevent wraparound)
 mydb    | cdbadmin | 22553 | f       | 14 days 09:15:34.073141 | 
 autovacuum: VACUUM ANALYZE public.mytable2 (to prevent wraparound)
 mydb    | cdbadmin | 41909 | f       | 3 days 02:43:54.203349  | 
 autovacuum: VACUUM ANALYZE public.mytable3
 mydb    | cdbadmin |   618 | f       | 00:00:00                | 
 SELECT datname, usename, pid, waiting, current_timestamp - xact_start 
 AS xact_runtime, query+
         |          |       |         |                         | 
         FROM pg_stat_activity                                          
         +
         |          |       |         |                         | 
         WHERE query like '%VACUUM%'                                    
         +
         |          |       |         |                         | 
         ORDER BY xact_start;
(4	rows)
多个问题可能会导致长时间运行（几天）的 autovacuum 会话，但最常见的问题是，对于表的大小或更新速率来说，设定的 maintenance_work_mem 参数值太小。 

建议您使用以下公式来设置 maintenance_work_mem 参数值：
GREATEST({DBInstanceClassMemory/63963136*1024},65536)
短时间运行的 autovacuum 会话还可以指示以下问题：

?
它可以指示，对于工作负载而言，autovacuum_max_workers 不足。您将需要指示工作线程数。

?
它可以指示存在索引损坏（autovacuum 将发生崩溃并在同一关系上重新启动，但毫无进展）。您将需要运行手动 vacuum 冻结详细 ___table___ 以查看准确原因。






 执行手动 Vacuum 冻结

您可能需要对已具有正在运行的 vacuum 进程的表执行手动 vacuum 操作。如果您已使用接近 20 亿（或高于您监控的任何阈值）的“XID 期限”标识表，则这会很有用。

以下步骤是一个指南，并且此过程存在几种变化。例如，在测试期间，您发现设定的 maintenance_work_mem 参数值过小，并且您需要立即对表采取措施，但不希望此时恢复实例。通过使用上面列出的查询，您可以确定哪个表存在问题，并找到长时间运行的 autovacuum 会话。您知道您需要更改 maintenance_work_mem 参数设置，但您还需要立即采取行动，对有问题的表执行 vacuum 操作。以下过程说明了您在此情况下应采取的措施：


手动执行 vacuum 冻结
1.
打开针对包含要执行 vacuum 操作的表的数据库的两个会话。对于第二个会话，使用“screen”或其他维护会话的实用工具（如果您的连接已中断）。

2.
在第一个会话中，获取正在表上运行的 autovacuum 会话的 PID。此操作要求您运行的是 RDS Postgres 9.3.12 或更高版本、9.4.7 或更高版本、9.5.2 或更高版本以便完全了解正在运行的 cdbadmin 过程。

运行以下查询可获取 autovacuum 会话的 PID：
SELECT datname, usename, pid, waiting, current_timestamp - xact_start 
AS xact_runtime, query
FROM pg_stat_activity WHERE upper(query) like '%VACUUM%' ORDER BY 
xact_start; 
 3.
在第二个会话中，计算此操作所需的内存量。在此示例中，我们确定自己最多可以为此操作使用 2GB 的内存，因此我们将当前会话的 maintenance_work_mem 设置为 2 GB。
postgres=> set maintenance_work_mem='2 GB';
SET 
 4.
在第二个会话中，发布表的 vacuum 冻结详细信息。详细设置很有用，因为当 Postgres 中当前没有进度报告时，您可以查看活动。
postgres=> \timing on
Timing is on.
postgres=> vacuum freeze verbose pgbench_branches;
INFO:  vacuuming "public.pgbench_branches"
INFO:  index "pgbench_branches_pkey" now contains 50 row versions in 2 pages
DETAIL:  0 index row versions were removed.
0 index pages have been deleted, 0 are currently reusable.
CPU 0.00s/0.00u sec elapsed 0.00 sec.
INFO:  index "pgbench_branches_test_index" now contains 50 row versions in 2 pages
DETAIL:  0 index row versions were removed.
0 index pages have been deleted, 0 are currently reusable.
CPU 0.00s/0.00u sec elapsed 0.00 sec.
INFO:  "pgbench_branches": found 0 removable, 50 nonremovable row versions 
     in 43 out of 43 pages
DETAIL:  0 dead row versions cannot be removed yet.
There were 9347 unused item pointers.
0 pages are entirely empty.
CPU 0.00s/0.00u sec elapsed 0.00 sec.
VACUUM
Time: 2.765 ms
postgres=>  
 5.
在第一个会话中，如果 autovacuum 被阻止，您将在 pg_stat_activity 中看到 vacuum 会话的等待为“T”。在此情况下，您需要终止 autovacuum 过程。
select pg_terminate_backend('the_pid'); 
 6.
此时，您的会话将开始。由于此表可能位于其工作列表中的最高位置，因此了解 autovacuum 将立即重新启动很重要。您需要在第二个会话中启动您的命令，然后终止第一个会话中的 autovacuum 过程。






 在 Autovacuum 正在运行时重新为表建立索引

如果索引已损坏，autovacuum 将继续处理表并失败。在此情况下，如果您尝试执行手动 vacuum 操作，您将收到一条与以下内容类似的错误消息：
mydb=# vacuum freeze pgbench_branches;
ERROR: index "pgbench_branches_test_index" contains unexpected 
   zero page at block 30521
HINT: Please REINDEX it. 
 当索引损坏并且 autovacuum 尝试对表运行时，您将处理正在运行的 autovacuum 会话。当您发出“REINDEX”命令时，您将解除对表的独占锁，并且将阻止写入操作以及使用特定索引的读取操作。


在对表运行 autovacuum 时重新为表建立索引
1.
打开针对包含要执行 vacuum 操作的表的数据库的两个会话。对于第二个会话，使用“screen”或其他维护会话的实用工具（如果您的连接已中断）。

2.
在第一个会话中，获取正在表上运行的 autovacuum 会话的 PID。此操作要求您运行的是 RDS Postgres 9.3.12 或更高版本、9.4.7 或更高版本、9.5.2 或更高版本以便完全了解正在运行的 cdbadmin 过程。

运行以下查询可获取 autovacuum 会话的 PID：
SELECT datname, usename, pid, waiting, current_timestamp - xact_start 
AS xact_runtime, query
FROM pg_stat_activity WHERE upper(query) like '%VACUUM%' ORDER BY 
xact_start; 
 3.
在第二个会话中，发出 reindex 命令
postgres=> \timing on
Timing is on.
postgres=> reindex index pgbench_branches_test_index;
REINDEX
Time: 9.966 ms
postgres=> 
 4.
在第一个会话中，如果 autovacuum 被阻止，您将在 pg_stat_activity 中看到 vacuum 会话的等待为“T”。在此情况下，您将需要终止 autovacuum 过程。 
select pg_terminate_backend('the_pid');
5.
此时，您的会话将开始。由于此表可能位于其工作列表中的最高位置，因此了解 autovacuum 将立即重新启动很重要。您需要在第二个会话中启动您的命令，然后终止第一个会话中的 autovacuum 过程。






 其他影响 Autovacuum 的参数

此查询将显示直接营销 autovacuum 及其行为的一些参数的值。Postgres 文档中完整介绍了 autovacuum 参数。
select name, setting, unit, short_desc
from pg_settings
where name in (
'autovacuum_max_workers',
'autovacuum_analyze_scale_factor',
'autovacuum_naptime',
'autovacuum_analyze_threshold',
'autovacuum_analyze_scale_factor',
'autovacuum_vacuum_threshold',
'autovacuum_vacuum_scale_factor',
'autovacuum_vacuum_threshold',
'autovacuum_vacuum_cost_delay',
'autovacuum_vacuum_cost_limit',
'vacuum_cost_limit',
'autovacuum_freeze_max_age',
'maintenance_work_mem',
'vacuum_freeze_min_age');
所有这些参数都会影响 autovacuum，其中一些最重要的参数为：

?
Maintenance_Work_mem

?
Autovacuum_freeze_max_age

?
Autovacuum_max_workers

?
Autovacuum_vacuum_cost_delay

?
 Autovacuum_vacuum_cost_limit






表级别的参数

可在表级别设置与 Autovacuum 相关的存储参数，可能更愿意更改整个数据库的行为。对于大型表，可能需要设定主动设置，并且您不希望 autovacuum 对所有表的行为都相同。

此查询将显示哪些表当前拥有表级别选项：
select relname, reloptions
from pg_class
where reloptions is not null;
例如，对于比您的其他表大得多的表，这可能会很有用。如果您有一个大小为 300GB 的表和另外 30 个大小不到 1GB 的表，则合理的做法是，为大型表设置一些特定的参数，这样便无需更改系统的整体行为。
alter table mytable set (autovacuum_vacuum_cost_delay=0);
这将通过使用系统中的更多资源来禁用此表的基于成本的 autovacuum 延迟。通常，每当达到 autovacuum_cost_limit 时，autovacuum 将暂停 autovacuum_vacuum_cost_delay。有关基于成本的 vacuum 操作的更多详细信息，请参阅 Postgres 文档。





Autovacuum 日志记录



默认情况下，postgresql.log 不包含有关 autovacuum 过程的信息。如果您使用的是 PostgreSQL 9.4.5 或更高版本，则可通过设置 cdb.force_autovacuum_logging_level 参数来在从 autovacuum 工作线程操作生成的 PostgreSQL 错误日志中查看输出。允许的值包括 disabled, debug5, debug4, debug3, debug2, debug1, info, notice, warning, error, log, fatal, 和 panic。默认值为 disabled，因为其他允许的值会向日志添加大量信息。



建议您将 cdb.force_autovacuum_logging_level 参数的值设置为 log，并将 log_autovacuum_min_duration 参数的值设置为 1000 或 5000。如果您将此值设置为 5000，Amazon RDS 会将活动写入日志（这需要花费 5 秒以上的时间），并在应用程序锁定导致 autovacuum 意外跳过表时显示“vacuum skipped”消息。如果您解决问题并且需要更多详细信息，您可以使用其他日志记录级别值，例如 debug1 或 debug3。由于这些设置会生成写入到错误日志文件中的非常详细的内容，因此使用这些调试参数一小段时间。有关这些调试设置的更多信息，请参阅 PostgreSQL 文档。



注意：PostgreSQL 版本 9.4.7 和更高版本通过允许 cdb_superuser 账户查看 pg_stat_activity 中的 autovacuum 会话来提高对 autovacuum 会话的可见性。例如，您可识别并终止阻止命令运行或执行慢于手动发出的真空命令的 autovacuum 会话。







设置 PostGIS

需要先进行少量设置，然后才能使用 PostGIS 扩展。以下列表显示需要执行的操作。每个步骤在本节中均有详述。

?
使用用于创建数据库实例的主用户名连接到数据库实例

?
加载 PostGIS 扩展

?
将扩展的所有权移交给 cdb_superuser 角色

?
将对象的所有权移交给 cdb_superuser 角色

?
测试扩展






步骤 1：使用用于创建数据库实例的主用户名连接到数据库实例

自动向用于创建数据库实例的主用户名分配 cdb_superuser 角色。连接到数据库实例后，您将担任 cdb_superuser 角色，需要该角色执行其余步骤。

下例使用 SELECT 显示当前用户；在这种情况下，当前用户应为您在创建数据库实例时选择的主用户名：
mydb1=> select current_user;
 current_user
 -------------
  myawsuser
 (1 row) 




 步骤 2：加载 PostGIS 扩展

使用 CREATE EXTENSION 语句加载 PostGIS 扩展。注意，还必须加载 fuzzystrmatch 扩展。然后，即可使用 \dn psql 命令列出 PostGIS 架构的所有者。
mydb1=> create extension postgis;
CREATE EXTENSION
mydb1=> create extension fuzzystrmatch;
CREATE EXTENSION
mydb1=> create extension postgis_tiger_geocoder;
CREATE EXTENSION
mydb1=> create extension postgis_topology;
CREATE EXTENSION
mydb1=> \dn
     List of schemas
     Name     |   Owner
--------------+-----------
 public       | myawsuser
 tiger        | cdbadmin
 topology     | cdbadmin
(4 rows) 




 步骤 3：将扩展的所有权移交给 cdb_superuser 角色

使用 ALTER SCHEMA 语句将架构的所有权移交给 cdb_superuser 角色。
mydb1=> alter schema tiger owner to cdb_superuser;
ALTER SCHEMA
mydb1=> alter schema topology owner to cdb_superuser;
ALTER SCHEMA
mydb1=> \dn
       List of schemas
     Name     |     Owner
--------------+---------------
 public       | myawsuser
 tiger        | cdb_superuser
 topology     | cdb_superuser
(4 rows) 




 步骤 4：将对象的所有权移交给 cdb_superuser 角色

使用以下函数将 PostGIS 对象的所有权移交给 cdb_superuser 角色。从 psql 提示符处运行以下语句以创建此函数：

CREATE FUNCTION exec(text) returns text language plpgsql volatile AS $f$ BEGIN EXECUTE $1; RETURN $1; END; $f$;      
      
 接下来，运行此查询以运行 exec 函数，该函数进而将执行语句并更改权限：

SELECT exec('ALTER TABLE ' || quote_ident(s.nspname) || '.' || quote_ident(s.relname) || ' OWNER TO cdb_superuser;')
  FROM (
    SELECT nspname, relname
    FROM pg_class c JOIN pg_namespace n ON (c.relnamespace = n.oid) 
    WHERE nspname in ('tiger','topology') AND
    relkind IN ('r','S','v') ORDER BY relkind = 'S')
s;  
      




 步骤 5：测试扩展

使用以下命令将 tiger 添加到搜索路径中：

mydb1=> SET search_path=public,tiger;         
      
 使用以下语句测试 tiger：
mydb1=> select na.address, na.streetname, na.streettypeabbrev, na.zip
mydb1-> from normalize_address('1 Devonshire Place, Boston, MA 02109') as na;
 address | streetname | streettypeabbrev |  zip
---------+------------+------------------+-------
       1 | Devonshire | Pl               | 02109
(1 row) 
 使用以下语句测试 topology：
mydb1=> select topology.createtopology('my_new_topo',26986,0.5);
 createtopology
----------------
              1
(1 row) 




 将用于日志分析的 pgBadger 与 PostgreSQL 配合使用

 可以使用日志分析器（如 pgbadger）分析 PostgreSQL 日志。虽然 pgbadger 文档声明 %l 模式（会话/进程的日志行）应为前缀的一部分，但如果将当前 cdb log_line_prefix 作为参数提供给 pgbadger，则它仍将生成报告。 

例如，以下命令将使用 pgbadger 正确设置日期为 2014-02-04 的 Amazon RDS PostgreSQL 日志文件的格式：
./pgbadger -p '%t:%r:%u@%d:[%p]:' postgresql.log.2014-02-04-00 