## MySQL 5.7
### 20190830版本
#### 新特性：
- 支持 binlog 文件损坏时跳过继续解析的功能，在主实例及 binlog 均损坏的场景下，可最大程度在备库中恢复数据并提供使用。
- 支持非 GTID 模式到 GTID 模式的数据同步。
- 支持用户通过 show full processlist 查询“用户线程内存使用信息”。
- 支持表 [快速加列功能](https://cloud.tencent.com/document/product/236/43732)，不拷贝数据，不占用磁盘空间和磁盘 I/O，业务高峰期可以实时变更。
- 支持自增值持久化。

#### 修复：
- 修复 Grant 中列名出现保留字会造成复制中断问题。
- 修复分区表上进行反向扫描导致 SQL 执行效率变慢的问题。
- 修复主键表虚拟索引数据不一致导致查询结果异常的问题。
- 修复 InnoDB 主键范围查询导致数据缺失的问题。
- 修复对带有空间索引的表执行 DDL 导致系统 crash 的问题。
- 修复 binlog 过大时，心跳信息中文件长度溢出导致主备中断的问题。
- 修复删除 event 导致其他 event 不按时执行的问题。
- 修复汇总查询结果错误的问题。

### 20190615版本
#### 新特性：
- 支持透明数据加密功能。

### 20190430版本
#### 修复：
- 修复在子查询中使用长文本功能时的空指针引用问题。
- 修复 Hash Scan 所引起的主备中断问题。
- 修复因主库 binlog 切换导致 slave 节点 I/O 线程中断的问题。
- 修复使用 NAME_CONST 导致的 crash 问题。
- 修复字符集引起的 illegal mix of collation 问题。


### 20190203版本
#### 新特性：
- 支持异步删除大表：异步、缓慢地清理文件，进而避免因删除大表导致业务性能出现抖动情况，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持 CATS 锁调度方式。
- GTID 开启时，支持事务中创建和删除临时表和 CTS 语法，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持隐式主键，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持非 super 权限用户 kill 其他用户会话的功能，通过 cdb_kill_user_extra 参数进行设置，默认值为 root@%。
- 支持企业级加密函数，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。

#### 修复：
- 修复 binlog 缓存文件空间不足时造成复制中断的问题。
- 修复 fsync 返回 EIO，反复尝试陷入死循环的问题。
- 修复 GTID 空洞造成复制中断且不能恢复的问题。
   

### 20180918版本
#### 新特性：
- 支持自动 kill 空闲任务，减少资源冲突，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- Memory 引擎自动转换为 InnoDB 引擎：如果全局变量 cdb_convert_memory_to_innodb 为 ON，则创建/修改表时会将表引擎从 Memory 转换为 InnoDB。
- 支持隐藏索引功能。
- 支持 Jemalloc 内存管理，替换 jlibc 内存管理模块，降低内存占用，提高内存分配效率。
   
#### 性能优化：
- binlog 切换优化，减少 rotate 持有锁时间，进而提升系统性能。
- 提升 Crash Recovery 时的恢复速度。
    
#### 修复：
- 修复由于主备切换而引起 event 失效的问题。
- 修复 REPLAY LOG RECORD 所引起的 Crash 问题。
- 修复 Loose index scans 所导致查询结果错误的问题。


### 20180530版本
#### 新特性：
- 支持 SQL 审计功能。
- 支持表级别的并行复制，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
   
#### 性能优化：
- slave 实例的锁优化，提高 slave 实例同步性能。   
- select ... limit 的下推优化。
   
#### 修复：
- 修复由于 relay_log_pos & master_log_pos 位点不一致导致切换失败的问题。
- 修复 Crash on UPDATE ON DUPLICATE KEY 产生的 Crash 问题。
- 修复由于 JSON 列导入时引起的 “Invalid escape character in string.” 错误。
   
### 20171130版本
#### 新特性：
- 支持 information_schema.metadata_locks 视图，查询当前实例中的 MDL 授予和等待状态。
- 支持语法 ALTER TABLE NO_WAIT | TIMEOUT，给 DDL 操作赋予等待超时，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持线程池功能，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。

#### 修复：
- 根据 bytes_data 计算 innodb_buffer_pool_pages_data，避免该参数溢出。
- 修复在异步模式下速度限制插件不可用的问题。

   
## MySQL 5.6
### 20190930版本
#### 新特性：
- 用户可通过 show full processlist 查询“用户线程内存使用信息”，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。  

#### 修复：
- 修复备库 replication filter 所引起的 gtid 空洞的问题。
- 修复 Binlog 过大时,心跳信息中文件长度溢出导致主备中断的问题。
- 修复字符集引起 illegal mix of collation 的问题。
- 修复 Hash Scan 所引起主备中断的问题。
- 修复一个 NAME_CONST 用法导致 crash 的问题。
- 修复因主库 binlog 切换导致 slave 节点 I/O 线程中断的问题。
- 修复 innodb_log_checusum 所导致备份不兼容的问题。

### 20190530版本
#### 修复：
- 修复 RC 模式下读到脏数据的问题。
- 修复删除临时表会导致备机回放失败的问题。
- 修复高并发下死锁的问题。
   

### 20190203版本
#### 新特性：
- 异步删除大表：异步、缓慢地清理文件，进而避免因删除大表导致业务性能出现抖动情况，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- 支持非 super 权限用户 kill 其他用户会话的功能，通过 cdb_kill_user_extra 参数进行设置，默认值为 root@%。
- GTID 开启时，支持事务中创建和删除临时表和 CTS 语法，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
   
#### 性能优化：   
- 分区表的复制回放优化，进而提升分区表的回放速度。
   
#### 修复：
- 修复临时空间不足所导致主备不一致的问题。
- 修复热点记录更新挂起的问题。
- 修复并行复制下 Seconds_Behind_Master 值异常的问题。

### 20180915版本
#### 新特性：
- MEMORY  引擎自动转换为 InnoDB 引擎：如果全局变量 cdb_convert_memory_to_innodb 为 ON，则创建、修改表时会将表引擎从 MEMORY 转换为 InnoDB。
- 自动 kill 空闲任务，减少资源冲突，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
   
#### 修复：
- 修复 REPLAY LOG RECORD 所导致 crash 的问题。
- 修复 decimal 精度问题所导致主备时间数据不一致的问题。


### 20180130版本
#### 新特性：
- 支持线程池功能，该功能需 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。
- slave 节点支持动态修改复制过滤条件。

#### 性能优化：
- drop table 带来的性能抖动。
   
#### 修复：
- 修复认证密码串导致数据库 crash 的问题。
   
### 20180122版本
#### 新特性：
- 支持 SQL 审计功能。

#### 修复：
- 修复整数溢出的问题。
- 修复使用全文索引查询出错的问题。
- 修复复制时 slave 机 crash 问题。
	
### 20170830版本
#### 修复：
- 修复异步模式下 binlog 限速失效的问题。
- 修复 buffer_pool 状态异常的问题。
- 修复 SEQUENCE 与隐含主键冲突的问题。
   
### 20170228版本
#### 修复：
- 修复 drop table 中的字符编码 bug。
- 修复 replicate-wild-do-table 无法正确过滤 db 或者 table 中含有小数点等特殊字符的问题。
- 修复备库产生的 rotate 事件后，导致 SQL 线程提前退出的问题。
  
### 20161130版本
#### 性能优化：
- lock_log 锁拆分，减少 lock log 占用的时间，提高并发性能。
- 主库 ACK 线程独立出来，提升响应时间。
- 用户线程在等待 ACK 的过程中不允许 kill 功能，以防止幻象读。
- 修复在 sync_binlog != 1 时导致不必要的 lock_sync 锁。

