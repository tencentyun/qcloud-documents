本文为您介绍 MySQL 内核版本更新动态，如需升级，请参见 [升级内核小版本](https://cloud.tencent.com/document/product/236/45522)。

## MySQL 8.0
### 20210830
#### 新特性：
- 支持预加载行数限制功能。
- 支持计划缓存点查优化功能。
- 支持扩展 ANALYZE 语法（UPDATE HISTOGRAM c USING DATA 'json'），支持直接写入直方图功能。

#### 性能优化：
- 使用直方图替代索引下探，降低评估误差以及 I/O 开销，该能力默认未打开。

#### Bug 修复：
- 修复 online-DDL 期间统计信息可能为零的情况。
- 修复从机 generated column 不更新的情况。
- 修复 binlog 压缩时实例 hang 住的问题。
- 修复新产生的 binlog 文件的 previous_gtids event 中的 gtid 缺失问题。
- 修复修改系统变量时可能死锁的问题。
- 修复 show processlist 中从机 sql 线程的 info 显示不正确的问题。
- 移植官方8.0.23中 hash join 相关的 bugfix。
- 移植官方 writeset 相关 bugfix。
- 移植官方8.0.24中查询优化器相关的 bugfix。
- 修复 FAST DDL 中优化 flush list 释放页面并发 bug。
- 优化海量个数表的实例升级数据字典时占用大量内存。
- 修复 instant add column 后在创建新主键场景下的 crash 问题。
- 修复全文索引查询中内存增长导致 OOM 问题。
- 修复 show processlist 返回结果集中 TIME 字段出现-1的问题。
- 修复直方图兼容性可能导致表无法打开的问题。
- 修复构建 Singleton 直方图的浮点累加误差。
- 修复 row 格式日志时表名为较长的中文字符导致复制中断问题。

### 20210330
#### 新特性：
- 支持主从 bp 同步功能：当发生 HA 并进行主备切换后，备库通常需要一段比较长的时间来 warmup，把热点数据加载到buffer pool。为加速备机的预热，TXSQL  支持了主从 bp 同步功能。
- 支持 Sort Merge Join 功能。
- 支持 FAST DDL 功能。
- 支持用户侧查询 character_set_client_handshake 参数显示当前值功能。

#### 性能优化：
- 优化扫描 flush list 刷脏：通过优化刷脏机制，解决了创建索引过程中的性能抖动问题，提升了系统稳定性。

#### 官方 bug 修复：
- 修复修改 offline_mode、cdb_working_mode 参数的死锁问题。
- 修复 trx_sys的max_trx_id 持久化并发问题。

### 20201230
#### 新特性：
- 合并官方 [8.0.19](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-19.html)、[8.0.20](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-20.html)、[8.0.21](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-21.html)、[8.0.22](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-22.html) 变更。
- 支持动态设置 thread_handling 线程模式或连接池模式。

#### 性能优化：
- 优化 BINLOG LOCK_done 锁冲突，提升写入性能。
- 使用 Lock Free Hash 优化 trx_sys mutex 冲突，提升性能。
- redo log 刷盘优化。
- buffer pool 初始化时间优化。
- 大表 drop table 清理 AHI 优化。
- 审计性能优化。

#### 官方 bug 修复：
- 修复清理 innodb 临时表时造成的性能抖动问题。
- 修复核数较多的实例 read only 性能下降的问题。
- 修复 hash scan 导致1032问题。
- 修复热点更新功能的并发安全问题。

### 20200630
#### 新特性：
- 支持异步删除大表：异步、缓慢地清理文件，进而避免因删除大表导致业务性能出现抖动情况，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持自动 kill 空闲任务，减少资源冲突，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持透明数据加密功能。

#### 官方 bug 修复：
- 修复由于 relay_log_pos & master_log_pos 位点不一致导致切换失败的问题。
- 修复异步落盘所引起的数据文件出错的问题。
- 修复 fsync 返回 EIO，反复尝试陷入死循环的问题。
- 修复全文索引中，词组查找（phrase search）在多字节字符集下存在的崩溃问题。

## MySQL 5.7
### 20210630
#### 新特性：
- 新增命令 SHOW SLAVE DETAIL [FOR CHANNEL channel]，用于展示当前 slave 已经回放的 binlog 时间戳。
- 支持 transaction_read_only/transaction_isolation 参数。

#### 性能优化：
- 优化 hash scan 的应用速度；在 slave 端，通过聚合 event 多个相同的 binlog event 来提升 hash scan 的应用速度。

#### Bug 修复：
- 修复更新语句触发的临时表的重复主键、找不到列、列长度过长问题。
- 修复 DDL 过程中统计信息可能为零的问题。
- 修复连接状态统计中 undo log size 统计不准确的问题。
- 修复查询 metadata_locks 表导致实例 crash 的问题。
- 修改 of 为非保留关键字。
- 修复动态修改版本号在新连接显示无效问题。
- 修复 page_cache cleanning 访问野指针的问题。
- 修复执行 alter table 语句可能引发“Incorrect key file for table”报错的问题。
- 修复分区表使用内存过大的问题。
- 修复 show processlist 返回结果集中 TIME 字段出现-1的问题。
- 修复 slave 节点 XA 事务复制锁等待问题。
- 修复分区表在 equal range 查询时错误加锁问题。

### 20210331
#### 新特性：
- 支持 delete/insert/replace 的 returning 语法，可以返回该 statment 所操作的数据行。 其中，delete 语句返回前镜像数据，insert/replace 返回后镜像数据。
- 支持列压缩功能：当前有针对行格式的压缩和针对数据页面的压缩，但是这两种压缩方式在处理一个表中的某些大字段和其他很多小字段，同时对小字段的读写很频繁，对大字段访问不频繁的情形中，它的读写访问都会造成很多不必要的计算资源浪费，列压缩可以压缩那些访问不频繁的大字段，同时能够减少整行字段的存储空间，提高读写访问的效率。
- 支持用户侧查询 character_set_client_handshake 参数显示当前值功能。
- 支持主动清理日志文件占用的 page cache：该功能采用滑动窗口的方式通过 posix_fadvise 主动清理日志文件占用的 page cache，降低操作系统内存压力，提升整机稳定性。

#### 性能优化：
- CREATE INDEX 并行化：CREATE INDEX 过程中需要执行外部归并排序，比较耗时。本次引入了并行外部归并排序算法，使 CREATE INDEX 耗时降低50%以上。
- 优化扫描 flush list 刷脏：通过优化刷脏机制，解决了创建索引过程中的性能抖动问题，提升了系统稳定性。

#### 官方 bug 修复：
- 修复内存泄漏问题。
- 移植8.0版本 json 的修复，提升使用 json 的稳定性。
- 修复 hash scan 导致1032问题。
- 修复热点更新功能的并发安全问题。
- 批量移植官方 gcol bug 修复。
- 修复 datetime 类型在某些场景下与字符串比较失败的问题。
- 修复主从 bp 同步功能文件句柄未释放 bug。
- 修复设置 offline_mode 的同时新建连接，可能触发死锁 bug。
- 修复范围查询并发场景下 m_end_range 设置不正确，导致的 crash 问题。
- 修复 groupby json 字段中 temporay table的update 耗时较长问题。

### 20201231
#### 新特性：
- 支持 SELECT FOR UPDATE/SHARE 使用 NOWAIT 和 SKIP LOCKED 选项。
- 支持动态设置 thread_handling 线程模式或连接池模式。
- 支持主从 buffer pool 同步功能。
- 用户连接状态监控功能，监控项包括：同步异步 IO、内存、日志量，CPU 时间、锁占用时长等。

#### 性能优化：
- 事务子系统优化，提升高并发性能。
- 大事务 crash recover 启动时间优化。
- redo log 刷盘优化。
- buffer pool 初始化时间优化。
- utf8/utf8mb4 字符串效率优化。
- 审计性能优化。
- 解除了设置 gtid_purged 必须为空的限制。
- 备份锁优化：引入3个新的 SQL 语句，LOCK TABLES FOR BACKUP, LOCK BINLOG FOR BACKUP 和 UNLOCK BINLOG。相对于 FLUSH TABLES WITH READ LOCK 的上锁备份方式导致整个数据库不可提供服务，这三个语句是为了用于能够轻量级地对数据进行上锁，从而支持备份过程中的数据访问。不论是物理备份还是逻辑备份都可以使用这些语句来实现备份一致性的保护。
- 大表 drop table 优化。

#### 官方 bug 修复：
- 修复对 performance_schema 查询时 hang 住的问题。
- 修复 digest_add_token 函数里面的 overflow 的问题。
- 修复 MySQL 官方 truncate table 时，ibuf 访问导致 crash 的问题。
- 修复 left join 语句下 const 提前计算导致的查询正确性问题。

### 20200930
#### 性能优化：
- 备份锁优化 
FLUSH TABLES WITH READ LOCK 的上锁备份方式导致整个数据库不可提供服务，该版本中提供了轻量级的数据备份加锁方式。
- 大表 drop table 优化 
快速清理自适应哈希的优化（innodb_fast_ahi_cleanup_for_drop_table 控制），可以大幅度缩短 drop 大表时，清理自适应哈希索引的耗时。

#### 官方 bug 修复：
- 修复 MySQL 官方 truncate table 时，ibuf 访问导致 crash 的问题。
- 修复有快速加列后的冷备无法拉起的问题。
- 修复频繁释放 innodb 内存表对象，导致性能下降的问题。
- 修复 left join 语句下 const 提前计算，导致的查询正确性问题。
- 修复 sql 限流和 query rewrite 插件因为 Rule 类名冲突，导致 core 的问题。
- 修复多个 session 下 insert on duplicate key update 语句的并发更新问题。
- 修复针对 auto_increment_increment 并发插入，导致 duplicate key error 失败的问题。
- 修复 innodb 内存对象淘汰触发宕机的问题。
- 修复热点更新功能的并发安全问题。
- 修复升级 jemalloc 版本至5.2.1，开启线程池触发 coredump 的问题。
- 修复 fwrite 无错误处理，导致审计日志不完整的问题。
- 修复 mysqld_safe以root 用户启动时，不打印日志的问题。
- 修复 alter table exchange partition 导致 ddl log 文件增长的问题。

### 20200701
#### 官方 bug 修复：
- 修复 INNOBASE_SHARE index mapping 错误问题。

### 20200630
#### 新特性：
- 支持 SELECT FOR UPDATE/SHARE 语句使用 NOWAIT 和 SKIP LOCKED 选项。
- 支持大事务优化功能，可缓解因大事务导致主从延迟、备份失败等问题。
- 审计性能优化：支持异步审计功能。

#### 官方 bug 修复：
- 修复 digest_add_token 函数里面的溢出问题。
- 修复 insert blob 导致实例 crash 的问题。
- 修复 hash scan 在 event 中出现对同一行更新而找不到记录，所造成主从中断的问题。
- 修复对 performance_schema 查询时 hang 住的问题。

### 20200331
#### 新特性：
- 新增官方 MySQL 5.7.22 版本的 JSON 系列函数。
- 支持基于电商秒杀场景的 [热点更新](https://cloud.tencent.com/document/product/1130/37882#.E7.83.AD.E7.82.B9.E6.9B.B4.E6.96.B0.E4.BF.9D.E6.8A.A4) 功能。
- 支持 [SQL 限流](https://cloud.tencent.com/document/product/1130/37882#sql-.E9.99.90.E6.B5.81)。
- 数据加密功能支持 KMS 自定义密钥加密。

#### 官方 bug 修复：
- 修复全文索引中，词组查找（phrase search）在多字节字符集下存在的崩溃问题。
- 修复高并发情况下，CATS 锁调度模块存在的崩溃问题。

### 20190830
#### 新特性：
- 支持 binlog 文件损坏时跳过继续解析的功能，在主实例及 binlog 均损坏的场景下，可最大程度在备库中恢复数据并提供使用。
- 支持非 GTID 模式到 GTID 模式的数据同步。
- 支持用户通过 show full processlist 查询“用户线程内存使用信息”。
- 支持表 [快速加列功能](https://cloud.tencent.com/document/product/236/43732)，不拷贝数据，不占用磁盘空间和磁盘 I/O，业务高峰期可以实时变更。
- 支持自增值持久化。

#### 官方 bug 修复：
- 修复 Grant 中列名出现保留字会造成复制中断问题。
- 修复分区表上进行反向扫描导致 SQL 执行效率变慢的问题。
- 修复主键表虚拟索引数据不一致导致查询结果异常的问题。
- 修复 InnoDB 主键范围查询导致数据缺失的问题。
- 修复对带有空间索引的表执行 DDL 导致系统 crash 的问题。
- 修复 binlog 过大时，心跳信息中文件长度溢出导致主备中断的问题。
- 修复删除 event 导致其他 event 不按时执行的问题。
- 修复汇总查询结果错误的问题。

### 20190615
#### 新特性：
- 支持透明数据加密功能。

### 20190430
#### 官方 bug 修复：
- 修复在子查询中使用长文本功能时的空指针引用问题。
- 修复 Hash Scan 所引起的主备中断问题。
- 修复因主库 binlog 切换导致 slave 节点 I/O 线程中断的问题。
- 修复使用 NAME_CONST 导致的 crash 问题。
- 修复字符集引起的 illegal mix of collation 问题。

### 20190203
#### 新特性：
- 支持异步删除大表：异步、缓慢地清理文件，进而避免因删除大表导致业务性能出现抖动情况，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持 CATS 锁调度方式。
- GTID 开启时，支持事务中创建和删除临时表和 CTS 语法，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持隐式主键，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持非 super 权限用户 kill 其他用户会话的功能，通过 cdb_kill_user_extra 参数进行设置，默认值为 root@%。
- 支持企业级加密函数，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。

#### 官方 bug 修复：
- 修复 binlog 缓存文件空间不足时造成复制中断的问题。
- 修复 fsync 返回 EIO，反复尝试陷入死循环的问题。
- 修复 GTID 空洞造成复制中断且不能恢复的问题。
   
### 20180918
#### 新特性：
- 支持自动 kill 空闲事务，减少资源冲突，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- Memory 引擎自动转换为 InnoDB 引擎：如果全局变量 cdb_convert_memory_to_innodb 为 ON，则创建/修改表时会将表引擎从 Memory 转换为 InnoDB。
- 支持隐藏索引功能。
- 支持 Jemalloc 内存管理，替换 jlibc 内存管理模块，降低内存占用，提高内存分配效率。
   
#### 性能优化：
- binlog 切换优化，减少 rotate 持有锁时间，进而提升系统性能。
- 提升 Crash Recovery 时的恢复速度。
    
#### 官方 bug 修复：
- 修复由于主备切换而引起 event 失效的问题。
- 修复 REPLAY LOG RECORD 所引起的 Crash 问题。
- 修复 Loose index scans 所导致查询结果错误的问题。

### 20180530
#### 新特性：
- 支持 SQL 审计功能。
- 支持表级别的并行复制，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
   
#### 性能优化：
- slave 实例的锁优化，提高 slave 实例同步性能。   
- select ... limit 的下推优化。
   
#### 官方 bug 修复：
- 修复由于 relay_log_pos & master_log_pos 位点不一致导致切换失败的问题。
- 修复 Crash on UPDATE ON DUPLICATE KEY 产生的 Crash 问题。
- 修复由于 JSON 列导入时引起的 “Invalid escape character in string.” 错误。
   
### 20171130
#### 新特性：
- 支持 information_schema.metadata_locks 视图，查询当前实例中的 MDL 授予和等待状态。
- 支持语法 ALTER TABLE NO_WAIT | TIMEOUT，给 DDL 操作赋予等待超时，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持线程池功能，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。

#### 官方 bug 修复：
- 根据 bytes_data 计算 innodb_buffer_pool_pages_data，避免该参数溢出。
- 修复在异步模式下速度限制插件不可用的问题。

## MySQL 5.6
### 20210630
#### 新特性：
- 支持大事务复制优化。

#### Bug 修复：
- 修复 index merge 打开的情况下拷贝的正确性问题。
- 修复在 row 模式下，打开 cdb_more_gtid_feature_supported 时，中断 create table select 的执行会复制中断。
- 修复 max(id) 大于 show create table 中 AUTO_INCREMENT 的 Bug。

### 20201231
#### 官方 bug 修复：
- 修复由于 hash scan，导致1032问题。 
- 修复 row 格式下 replace into，导致主从 auto increment 值不一致的问题。
- 修复 SQL 解析申请内存未释放，导致内存泄漏的问题。
- 修复 create table as select 建表时，跳过 sql mode 检查的问题。
- 修复 Insert 语句在插入默认值时，跳过 sql mode 检查的问题。
- 修复绑定参数执行 update 语句时，跳过 sql mode 检查的问题。

### 20200915
#### 新特性：
- 支持 [SQL 限流](https://cloud.tencent.com/document/product/1130/37882#sql-.E9.99.90.E6.B5.81) 功能。

#### 性能优化：   
- buffer pool 初始化加速优化 。

#### 官方 bug 修复：
- 修复主备 rename table 都 hang 住的问题。 
- 修复当设置 event_scheduler 为 disable，cdb_skip_event_scheduler 从 on 改为 off 时，出现 crash 问题。 
- 修复 tencentroot 最大链接数未计入 srv_max_n_threads，造成 sync_wait_array 相关断言失败的问题。 
- 修复由于其他云服务的 MySQL 5.6 和 腾讯 MySQL 5.6 的系统库中有些表的结构不同，导致主从开启并行复制时，出现 crash 问题。 
- 修复 INSERT ON DUPLICATE KEY UPDATE THE WRONG ROW 问题。 
- 修复 index_mapping 出现错误问题。 
- 修复 mtr 失败 bug 问题。 
- 修复 hash scan 在 event 中出现对同一行的更新时，找不到这条记录造成主从中断的问题。 

### 20190930
#### 新特性：
- 用户可通过 show full processlist 查询“用户线程内存使用信息”。  

#### 官方 bug 修复：
- 修复备库 replication filter 所引起的 gtid 空洞的问题。
- 修复 Binlog 过大时,心跳信息中文件长度溢出导致主备中断的问题。
- 修复字符集引起 illegal mix of collation 的问题。
- 修复 Hash Scan 所引起主备中断的问题。
- 修复一个 NAME_CONST 用法导致 crash 的问题。
- 修复因主库 binlog 切换导致 slave 节点 I/O 线程中断的问题。
- 修复 innodb_log_checusum 所导致备份不兼容的问题。

### 20190530
#### 官方 bug 修复：
- 修复 RC 模式下读到脏数据的问题。
- 修复删除临时表会导致备机回放失败的问题。
- 修复高并发下死锁的问题。
   
### 20190203
#### 新特性：
- 异步删除大表：异步、缓慢地清理文件，进而避免因删除大表导致业务性能出现抖动情况，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持非 super 权限用户 kill 其他用户会话的功能，通过 cdb_kill_user_extra 参数进行设置，默认值为 root@%。
- GTID 开启时，支持事务中创建和删除临时表和 CTS 语法，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
   
#### 性能优化：   
- 分区表的复制回放优化，进而提升分区表的回放速度。
   
#### 官方 bug 修复：
- 修复临时空间不足所导致主备不一致的问题。
- 修复热点记录更新挂起的问题。
- 修复并行复制下 Seconds_Behind_Master 值异常的问题。

### 20180915
#### 新特性：
- MEMORY  引擎自动转换为 InnoDB 引擎：如果全局变量 cdb_convert_memory_to_innodb 为 ON，则创建、修改表时会将表引擎从 MEMORY 转换为 InnoDB。
- 自动 kill 空闲事务，减少资源冲突，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
   
#### 官方 bug 修复：
- 修复 REPLAY LOG RECORD 所导致 crash 的问题。
- 修复 decimal 精度问题所导致主备时间数据不一致的问题。

### 20180130
#### 新特性：
- 支持线程池功能，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- slave 节点支持动态修改复制过滤条件。

#### 性能优化：
- drop table 带来的性能抖动。
   
#### 官方 bug 修复：
- 修复认证密码串导致数据库 crash 的问题。
   
### 20180122
#### 新特性：
- 支持 SQL 审计功能。

#### 官方 bug 修复：
- 修复整数溢出的问题。
- 修复使用全文索引查询出错的问题。
- 修复复制时 slave 机 crash 问题。
	
### 20170830
#### 官方 bug 修复：
- 修复异步模式下 binlog 限速失效的问题。
- 修复 buffer_pool 状态异常的问题。
- 修复 SEQUENCE 与隐含主键冲突的问题。
   
### 20170228
#### 官方 bug 修复：
- 修复 drop table 中的字符编码 bug。
- 修复 replicate-wild-do-table 无法正确过滤 db 或者 table 中含有小数点等特殊字符的问题。
- 修复备库产生的 rotate 事件后，导致 SQL 线程提前退出的问题。
  
### 20161130
#### 性能优化：
- lock_log 锁拆分，减少 lock log 占用的时间，提高并发性能。
- 主库 ACK 线程独立出来，提升响应时间。
- 用户线程在等待 ACK 的过程中不允许 kill 功能，以防止幻象读。
- 修复在 sync_binlog != 1 时导致不必要的 lock_sync 锁。

