
### Metrics

| 指标名称                   | 单位 | 指标含义                               |
| -------------------------- | ---- | -------------------------------------- |
| tcp                        | 个   | TCP 服务器的连接数                      |
| http                       | 个   | HTTP 服务器的连接数                     |
| watches                    | 个   | ZK 事件订阅数                           |
| ephemeralNode              | 个   | ZooKeeper 中保存的临时节点数            |
| backgroundPoolTask         | 个   | BackgroundProcessingPool 中的活跃任务数 |
| backgroundSchedulePoolTask | 个   | BackgroundSchedulePool 中的活跃任务数   |
| contextLockWait            | 个   | 在 Context 中等待锁的线程数              |
| delayedInserts             | 个   | 被抑制的 Insert 查询数                   |
| dictCacheRequests          | 个   | cache 类型字典的数据源中的请求数        |
| distributedSend            | 个   | pending 的异步插入到分布式表的文件数    |
| global                     | 个   | 全局线程池中的线程数                   |
| globalActive               | 个   | 全局线程池中活跃的线程数               |
| local                      | 个   | 本地线程池中的线程数                   |
| localActive                | 个   | 本地线程池中活跃的线程数               |
| leaderElection             | 个   | 参与 leader 选举的副本数量               |
| leaderReplica              | 个   | 属于 leader 的 Replicated table 的数量     |
| readonlyReplica            | 个   | 处于只读状态的 Replicated table 的数量   |
| memoryTracking             | GB   | 当前执行的查询中所分配的内存总量       |
| backgroundProcessingPool   | GB   | 后台处理池中分配的内存总量             |
| backgroundSchedulePool     | GB   | 后台调度池中所分配的内存总量           |
| memoryTrackingForMerges    | GB   | 后台 merges 所分配的内存总量             |
| merge                      | 个   | 正在后台执行的 merge 数量                |
| read                       | 个   | 打开的可读文件的数量                   |
| write                      | 个   | 打开的可写文件的数量                   |
| partMutation               | 个   | 表变更的次数                           |
| queryThread                | 个   | 查询处理的线程数量                     |
| queryPreempted             | 个   | 停止或等待的查询数量                   |
| read                       | 个   | 读系统调用的数量                       |
| write                      | 个   | 写系统调用的数量                       |
| fetch                      | 个   | 从副本收集的数据块数量                 |
| send                       | 个   | 发送到副本的数量块数量                 |
| check                      | 个   | 检查一致性的数据块数量                 |
| revision                   | 个   | server 的修改                           |
| version                    | 1    | 版本号                                 |
| waitingRead                | 个   | 等待读表的读写锁的线程数量             |
| waitingWrite               | 个   | 等待写表的读写锁的线程数量             |
| activeRead                 | 个   | 在一个表的读写锁中持有读锁的线程数     |
| activeWrite                | 个   | 在一个表的读写锁中持有写锁的线程数     |
| storageBufferRows          | 个   | Buffer tables 中的行数                  |
| storageBufferBytes         | MB   | Buffer tables 中的字节数                |

### Events

| 指标名称      | 单位 | 指标含义                                              |
| ------------- | ---- | ----------------------------------------------------- |
| total         | 个   | 可能执行的查询总数                                    |
| select        | 个   | 可能执行的 Select 查询数                                |
| insert        | 个   | 可能执行的 Insert 查询数                                |
| insertedRows  | 个   | 被插入到所有表中的行数                                |
| insertedBytes | 个   | 被插入到所有表中的字节数                              |
| read          | 微秒 | 等待读系统调用的总时间                                |
| write         | 微秒 | 等待写系统调用的总时间                                |
| fileOpen      | 个   | 已打开的文件数                                        |
| read          | 个   | 来自文件描述器的读个数                                |
| write         | 个   | 来自文件描述器的写个数                                |
| read          | MB   | 来自文件描述器的读字节数                              |
| write         | MB   | 写入文件描述器的字节数                                |
| realtime      | 微秒 | 处理线程花费的总时间                                  |
| user          | 微秒 | 在用户空间下处理线程在执行 CPU 指令花费的总时间         |
| system        | 微秒 | 在操作系统内核空间下处理线程在执行 CPU 指令花费的总时间 |
| regexpCreated | 个   | 编译的正则表达式数                                    |

### Asynchronous_metrics

| 指标名称                 | 单位 | 指标含义                            |
| ------------------------ | ---- | ----------------------------------- |
| markCacheBytes           | MB   | StorageMergeTree 的 marks 的缓存大小   |
| markCacheFiles           | 个   | StorageMergeTree 的 marks 的缓存文件数 |
| maxPartCountForPartition | 个   | partitions 中最大的活跃数据块的数量  |
| databaseCount            | 个   | 数据库数量                          |
| tableCount               | 个   | 数据表数量                          |
| absolute                 | 微秒 | 最大的 replica 队列时延               |
| relative                 | 微秒 | 来自其他块的绝对时延的差异的最大值  |
| insert                   | 个   | 需要完成的数据块 insert 数            |
| merge                    | 个   | 待完成的 merge 数                     |
| replicasMaxQueueSize     | 个   | 待完成的操作队列的大小              |
