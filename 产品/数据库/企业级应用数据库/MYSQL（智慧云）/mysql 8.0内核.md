## 新增功能
- xtrbackup从8.0.10升级到8.0.13
- 支持设置default_collation_for_utf8mb4。建库建表时采用utf8mb4作为字符集。如果不指定字符集，则MySQL用utf8mb4_0900_ai_ci作为默认字符集
- 支持表级别并行复制，设置复制模式变量：slave_parallel_type=TABLE
- 为mysqldump工具增加--ignore-database参数，可以忽略指定的库导出
- 增加show detail processlist语法，展示更多的会话信息。同时增加三个状态变量：total_innodb_memory_used，total_pfs_memory_used，total_server_memory_used。需要开启txsql_enable_resource_statistics特性才生效（默认开启）
- mysqlbinlog增加flashback参数，将binlog解释为闪回SQL方便回滚
- 列压缩： 建表时可以指定列compressed属性( 只适用于InnoDB存储引擎 )，拥有这个属性的列在插入时会对数据进行压缩存储，查询时会在底层进行解压。压缩/解压操作默认采用ZLIB算法 ，并对开发者透明
压缩列创建的语法为:
```
  CREATE TABLE t1(
     id INT PRIMARY KEY,
     b  BLOB COMPRESSED [ALGORITHM = [ZLIB|LZ4|ZSTD]] --ALGORITHM可省略，默认ZLIB
  );
```
或者
```
  CREATE TABLE t1(
     id INT PRIMARY KEY,
     b  BLOB COLUMN_FORMA COMPRESSED [ALGORITHM = [ZLIB|LZ4|ZSTD]] --ALGORITHM可省略，默认ZLIB
  );
```

>!1. 支持列压缩属性的数据类型包括BLOB，TEXT，VARCHAR，VARBINARY和JSON。其中BLOB包含 TINYBLOB , MEDIUMBLOB , LONGBLOG ；TEXT包含 TINYTEXT , MEDUUMTEXT , LONGTEXT 
2. 只有字段长度超过innodb_min_column_compress_length(默认256)才压缩


- tde 支持配置sm4算法，新增innodb_encryption_algorithm用于配置innodb层tablespace encrypt的算法。目前只支持aes和sm4两种
- binlog支持配置sm4算法，新增binlog_encryption_algorithm用于配置binlog加密的算法，目前只支持aes和sm4两种。
- 升级xtrabackup，支持备份和回档有sm4算法加密的库


>!国密加密算法为选配组件，需要额外付费才能使用。


- 支持oracle语法 for update wait n, 单独设置sql的等锁时间
- 添加一个session 变量allow_access_dd_tables，允许用户读取字典表
- 添加参数 sqlasync_wait_n_slaves 支持同步等待n个slave的ack后返回成功

## 功能优化
- 拆分xa transaction cache为128个分片，以减少锁竞争
- 如果没有开启ibuf，则优化代码逻辑，降低对ibuf bitmap的访问
- 优化备机针对xa commit/xa rollback写gtid的性能，提升备机apply速度（主要是正确设置trx_t::skip_persist_gtid标志）
- 优化访问undo head page的流程，通过缓存，提升获取head page的速度
- 通过设置带内存池的history，优化在设置binlog_transaction_dependency_tracking = WRITESET的情况下，tpcc性能提升30%。不过目前默认binlog_transaction_dependency_tracking = COMMIT_ORDER，所以一般看不到这个效果
- 优化fil_write_zeros分配/释放大量内存，优化innodb在分配新的数据页面的时候的性能
- 优化slave节点写relay log的性能，收到事务完成才write。通过txsql_slave_io_optimaze_write开启，模板里默认开启
- 优在对同一个B树索引并发构建AHI记录时，存在大量锁竞争，导致性能低下。本优化通过预先避免锁冲突的策略，解决了锁竞争问题，提升了系统性能。不过TDSQL默认是关闭ahi的，所以感受不到这点
- 针对大内存，优化innodb buffer pool的初始化逻辑，提升启动速度
- 优化PFS histogram tables，减少开启性能视图的内存占用开销
- 支持热点更新，解决秒杀场景性能急剧下降的问题，通过参数innodb_hot_update_detect动态开启与关闭
- 修改默认参数，table_open_cache_instances(64->32),table_open_cache(10240→20480)，降低在表数量多，并发多的情况下table cache加锁的瓶颈。
- 增加参数:innodb_quickly_stoped，开启后会提升大内存实例stop的速度，比如512G内存的实例，stop速度由300秒提升到130秒
- 添加编译选项-DMUTEXTYPE=futex，使得innodb降低锁消耗的内存，并且提升sysbench性能(update non index 提升5%)
- 构建动态链接jemalloc，解决在某些页大小和jemalloc不一致在操作系统上mysqld无法启动的问题
- 安装脚本强制设置句柄数为40w，修复为：“检测当前配置值低于40w才设置为40w”

## Bug修复
- 修复强同步超时后的错误提示“The transaction is in doubt. Please check whether the transaction has been committed.”
- 解决xtrabackup在扩容时无法正确定位到binlog同步点导致重建主备失败的问题（强制加FTWRL锁）
- 修复master xa 死锁导致slave hang
- 修复新的dcn master start sql_thread 失败的情况
- 修复关闭服务器 assertion TRX_SYS_ANY_ACTIVE_TRANSACTIONS() == 0 （失败）
- Reset master 后重置 ask position, 防止提交未同步的binlog
- 修复线程池执行完一条sql后没有清理current_thd导致大量短连接场景下统计信息（update_thread_stats)的问题
- 修复条件永假导致txsql_returnning return ok packet的问题
- 修复热点更新场景下update transaction age死锁
- 修复按照5.7配置keyring_file_data在数据库sys下时导致初始化sys库失败的问题

## 兼容性
- 在tdsql的template.cnf模板中新增reject_table_no_pk参数，默认禁止无主键表的创建
- 在配置模版里打开 skip_name_resolve
- 配置模版中开启writeset
- 配置预加载 keyring_file.so插件
- 将静态编译jemalloc修改为动态链接

