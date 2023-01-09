## 命名空间

Namespace=QCE/TXMR_CLICKHOUSE



## 监控指标

| 指标英文名                                             | 指标中文名                                            | 单位 | 维度                                       |
| ------------------------------------------------------ | ----------------------------------------------------- | ---- | ------------------------------------------ |
| ClickhouseBackgroundPoolTaskBackgroundpooltask         | BackgroundProcessingPool中的活跃任务数                | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseBackgroundPoolTaskBackgroundschedulepooltask | BackgroundSchedulePool中的活跃任务数                  | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseBufferFileDescriptorBytesRead                | 来自文件描述器的读字节数                              | MB   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseBufferFileDescriptorBytesWrite               | 写入文件描述器的字节数                                | MB   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseBufferFileDescriptorCountRead                | 来自文件描述器的读个数                                | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseBufferFileDescriptorCountWrite               | 来自文件描述器的写个数                                | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseConnectionCountHttp                          | HTTP服务器的连接数                                    | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseConnectionCountTcp                           | TCP服务器的连接数                                     | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseDatabaseCountDatabasecount                   | 数据库数量                                            | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseDelayedInsertCountDelayedinserts             | 被抑制的Insert查询数                                  | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseDictCacheRequestCountDictcacherequests       | cache类型字典的数据源中的请求数                       | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseDiskElapsedMicrosecondsRead                  | 等待读系统调用的总时间                                | us   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseDiskElapsedMicrosecondsWrite                 | 等待写系统调用的总时间                                | us   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseDistributedFilesToinsertCountDistributedsend | pending的异步插入到分布式表的文件数                   | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseExcuteQueryCountInsert                       | 可能执行的Insert查询数                                | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseExcuteQueryCountSelect                       | 可能执行的Select查询数                                | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseExcuteQueryCountTotal                        | 可能执行的查询总数                                    | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseFileOpenCountFileopen                        | 已打开的文件数                                        | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseInsertBytesInsertedbytes                     | 被插入到所有表中的字节数                              | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseInsertRowsInsertedrows                       | 被插入到所有表中的行数                                | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseLeaderElectionCountLeaderelection            | 参与leader选举的副本数量                              | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseMarkCacheBytesMarkcachebytes                 | StorageMergeTree的marks的缓存大小                     | MB   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseMarkCacheFilesMarkcachefiles                 | StorageMergeTree的marks的缓存文件数                   | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseMaxPartPartitionMaxpartcountforpartition     | partitions中最大的活跃数据块的数量                    | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseMemoryAllocatedBackgroundprocessingpool      | 后台处理池中分配的内存总量                            | GB   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseMemoryAllocatedBackgroundschedulepool        | 后台调度池中所分配的内存总量                          | GB   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseMemoryAllocatedMemorytracking                | 当前执行的查询中所分配的内存总量                      | GB   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseMemoryAllocatedMemorytrackingformerges       | 后台merges所分配的内存总量                            | GB   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseMergeCountMerge                              | 正在后台执行的merge数量                               | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseOpenFileCountRead                            | 打开的可读文件的数量                                  | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseOpenFileCountWrite                           | 打开的可写文件的数量                                  | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhousePartMutationCountPartmutation                | 表变更的次数                                          | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseProcessThreadTimeRealtime                    | 处理线程花费的总时间                                  | us   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseProcessThreadTimeSystem                      | 在操作系统内核空间下处理线程在执行CPU指令花费的总时间 | us   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseProcessThreadTimeUser                        | 在用户空间下处理线程在执行CPU指令花费的总时间         | us   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseQueryPreemptedCountQuerypreempted            | 停止或等待的查询数量                                  | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseQueryThreadCountQuerythread                  | 查询处理的线程数量                                    | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseRegexpCreatedCountRegexpcreated              | 编译的正则表达式数                                    | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseReplicasInQueueInsert                        | 需要完成的数据块insert数                              | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseReplicasInQueueMerge                         | 待完成的merge数                                       | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseReplicasMaxDelayAbsolute                     | 最大的replica队列时延                                 | us   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseReplicasMaxDelayRelative                     | 来自其他块的绝对时延的差异的最大值                    | us   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseReplicaCountLeaderreplica                    | 属于leader的Replicated table的数量                    | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseReplicaCountReadonlyreplica                  | 处于只读状态的Replicated table的数量                  | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseReplicaDataPartCountCheck                    | 检查一致性的数据块数量                                | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseReplicaDataPartCountFetch                    | 从副本收集的数据块数量                                | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseReplicaDataPartCountSend                     | 发送到副本的数量块数量                                | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseRevisionRevision                             | server的修改                                          | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseRwlockThreadCountActiveread                  | 在一个表的读写锁中持有读锁的线程数                    | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseRwlockThreadCountActivewrite                 | 在一个表的读写锁中持有写锁的线程数                    | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseRwlockThreadCountWaitingread                 | 等待读表的读写锁的线程数量                            | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseRwlockThreadCountWaitingwrite                | 等待写表的读写锁的线程数量                            | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseStorageBufferBytesStoragebufferbytes         | Buffer tables中的字节数                               | MB   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseStorageBufferRowsStoragebufferrows           | Buffer tables中的行数                                 | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseSyscallCountRead                             | 读系统调用的数量                                      | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseSyscallCountWrite                            | 写系统调用的数量                                      | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseTableCountTablecount                         | 数据表数量                                            | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseThreadContextLockWaitCountContextlockwait    | 在Context中等待锁的线程数                             | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseThreadCountGlobal                            | 全局线程池中的线程数                                  | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseThreadCountGlobalactive                      | 全局线程池中活跃的线程数                              | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseThreadCountLocal                             | 本地线程池中的线程数                                  | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseThreadCountLocalactive                       | 本地线程池中活跃的线程数                              | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseVersionVersion                               | 版本号                                                | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseZkEphemeralNodeCountEphemeralnode            | ZooKeeper中保存的临时节点数                           | 个   | host4clickhouseserver、id4clickhouseserver |
| ClickhouseZkWatchesCountWatches                        | ZK事件订阅数                                          | 个   | host4clickhouseserver、id4clickhouseserver |



## 各维度对应参数总览

| 参数名称                       | 维度名称              | 维度解释                     | 格式                                                         |
| :----------------------------- | :-------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | host4clickhouseserver | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4clickhouseserver              |
| Instances.N.Dimensions.0.Value | host4clickhouseserver | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4clickhouseserver   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4clickhouseserver                |
| Instances.N.Dimensions.0.Value | id4clickhouseserver   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |



## 入参说明

**查询弹性 MapReduce（Clickhouse）监控数据，入参取值如下：**

Namespace=QCE/TXMR_CLICKHOUSE
&Instances.N.Dimensions.0.Name=host4clickhouseserver
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4clickhouseserver
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID






