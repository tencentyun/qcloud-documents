MySQL5.7

20190830版本
新特性：

   支持binlog 文件损坏跳过继续解析的功能,可避免主实例及binlog均损坏的前提下，可最大程度在备库中恢复数据并提供使用。
   支持非GTID模式到GTID模式的数据同步
   支持用户可通过show full processlist查询：用户线程内存使用信息
   支持快速加列的功能：表快速加列，不拷贝数据，不占用磁盘空间和磁盘IO，业务高峰期可以实时变更。
   支持自增值持久化


Bugfix：

   修复Grant中列名出现保留字会造成复制中断问题
   官方bug：修复分区表上进行反向扫描导致SQl执行效率变慢的问题
   官方bug：修复主键表虚拟索引数据不一致导致查询结果异常的问题
   官方bug：修复innodb主键范围查询导致数据缺失的问题
   官方bug：修复对带有空间索引的表执行DDL导致系统crash的问题
   官方bug：修复 Binlog 过大时,心跳信息中文件长度溢出导致主备中断的问题
   官方bug：修复删除event导致其他event不按时执行的问题
   官方bug：修复汇总查询结果错误的问题

20190615版本
新特性：

   支持透明数据加密功能

20190430版本
  
   
Bugfix：

   修复在子查询中使用长文本功能时的空指针引用问题
   修复 Hash Scan 所引起的主备中断问题
   修复因主库binlog切换导致slave节点I/O线程中断的问题
   修复使用NAME_CONST导致crash问题
   修复字符集引起的 illegal mix of collation 的问题


20190203版本
新特性：

   异步删除大表：异步、缓慢地清理文件，进而避免因删除大表导致业务性能出现抖动情况
   支持CATS锁调度方式
   GTID开启时，支持事务中创建和删除临时表和CTS语法
   支持隐式主键
   支持普通用户kill其他普通用户会话的功能


Bugfix：

   修复binlog缓存文件空间不足时造成复制中断的问题
   修复fsync返回EIO，反复尝试陷入死循环的问题
   修复gtid空洞造成复制中断且不能恢复的问题
   

20180918版本
新特性：

   自动kill空闲任务，减少资源冲突
   memory引擎自动转换为innodb引擎:如果全局变量cdb_convert_memory_to_innodb为ON，则创建/修改表时会将表引擎从MEMORY转换为InnoDB。
   支持隐藏索引功能
   支持Jemalloc内存管理，替换jlibc内存管理模块，降低内存占用，提高内存分配效率
   
性能优化：
   binlog切换优化，减少rotate持有锁时间，进而提升系统性能
   提升Crash Recovery 时的恢复速度
   
   
Bugfix：

   修复由于主备切换而引起的 event 失效的问题
   修复REPLAY LOG RECORD所引起的 Crash问题
   修复 Loose index scans 所导致的查询结果错误问题


20180530版本
新特性：

   支持SQL审计功能
   支持表级别的并行复制
   
性能优化：
   slave实例的锁优化，提高slave机同步性能   
   select ... limit的下推优化
   
Bugfix：

   修复由于 relay_log_pos & master_log_pos 位点不一致导致的切换失败的问题
   修复Crash on UPDATE ON DUPLICATE KEY产生的Crash问题
   修复由于JSON列导入时引起的 "Invalid escape character in string." 错误
   
20171130版本
新特性：

   支持information_schema.metadata_locks视图，查询当前实例中的MDL授予和等待状态;
   支持语法ALTER TABLE NO_WAIT | TIMEOUT，给DDL操作赋予等待超时;
   支持线程池功能
Bugfix：

   根据 bytes_data 计算 innodb_buffer_pool_pages_data，避免该参数溢出
   修复在异步模式下速度限制插件不可用的问题

   
MySQL5.6
20190930版本
新特性：
   
   用户可通过show full processlist查询：用户线程内存使用信息
   
   

Bugfix：

   修复备库 replication filter 所引起的 gtid 空洞的问题
   修复 Binlog 过大时,心跳信息中文件长度溢出导致主备中断的问题
   修复字符集引起的 illegal mix of collation 的问题
   修复 Hash Scan 所引起的主备中断问题
   修复一个NAME_CONST用法导致crash问题
   修复因主库binlog切换导致slave节点I/O线程中断的问题
   修复 innodb_log_checusum 所导致的备份不兼容问题

20190530版本
Bugfix：

   修复RC模式下读到脏数据问题
   修复删除临时表会导致备机回放失败的问题
   修复高并发下死锁的问题
   



20190203版本
新特性：
   
   异步删除大表：异步、缓慢地清理文件，进而避免因删除大表导致业务性能出现抖动情况
   支持普通用户kill其他普通用户会话的功能
   GTID开启时，支持事务中创建和删除临时表和CTS语法
   
性能优化：   
   分区表的复制回放优化，进而提升分区表的回放速度
   
Bugfix：

   修复临时空间不足所导致的主备不一致问题
   修复热点记录更新挂起的问题
   修复并行复制下Seconds_Behind_Master值异常的问题

20180915版本
新特性：
   memory引擎自动转换为innodb引擎:如果全局变量cdb_convert_memory_to_innodb为ON，则创建/修改表时会将表引擎从MEMORY转换为InnoDB。
   自动kill空闲任务，减少资源冲突
   
Bugfix：

   修复 REPLAY LOG RECORD 所导致的 crash 问题
   修复decimal精度问题所导致的主备时间数据不一致问题


20180130版本
新特性：
   
   支持线程池功能
   slave节点支持动态修改复制过滤条件

性能优化：
   drop table带来的性能抖动
   
Bugfix：

   修复认证密码串导致数据库crash的问题
   
20180122版本
新特性：

   支持SQL审计功能
Bugfix：

    修复整数溢出的问题
    修复使用全文索引查询出错的问题
    修复复制时slave机crash问题
	
20170830版本

Bugfix：

   修复异步模式下 binlog 限速失效的问题
   修复 buffer_pool 状态异常的问题
   修复SEQUENCE与隐含主键冲突的问题 
   
20170228版本

Bugfix：

  修复drop table 中的字符编码的BUG
  修复 replicate-wild-do-table 无法正确过滤db或者table中含有小数点等特殊字符的问题
  修复备库产生的rotate事件后，导致sql线程提前退出的问题
  
20161130版本
性能优化：
   lock_log 锁拆分，减少 lock log 占用的的时间，提高并发性能
   主库 ACK 线程独立出来，提升响应时间;
   用户线程在等待 ACK 的过程中不允许 kill 功能，以防止幻象读
   修复在 sync_binlog != 1 时导致不必要的 lock_sync 锁
