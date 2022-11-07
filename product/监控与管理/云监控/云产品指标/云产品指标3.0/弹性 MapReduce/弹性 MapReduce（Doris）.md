## 命名空间

Namespace=QCE/TXMR_DORIS



## 监控指标

### Doris-BK

| 指标英文名                              | 指标中文名                         | 指标含义                                | 单位 | 维度                                       |
| --------------------------------------- | ---------------------------------- | --------------------------------------- | ---- | ------------------------------------------ |
| DorisBkOsCpuTimeProcesscputime          | CPU使用时间_ProcessCpuTime         | CPU 累计使用时间                        | ms   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilGcCountYgc                 | GC次数_YGC                         | Young GC 次数                           | 次   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilGcCountFgc                 | GC次数_FGC                         | Full GC 次数                            | 次   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilGcTimeFgct                 | GC时间_FGCT                        | Full GC 消耗时间                        | s    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilGcTimeGct                  | GC时间_GCT                         | 垃圾回收时间消耗                        | s    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilGcTimeYgct                 | GC时间_YGCT                        | Young GC 消耗时间                       | s    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilMemoryS0                   | 内存区域占比_S0                    | Survivor 0区内存使用占比                | %    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilMemoryE                    | 内存区域占比_E                     | Eden 区内存使用占比                     | %    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilMemoryCcs                  | 内存区域占比_CCS                   | Compressed class space 区内存使用占比   | %    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilMemoryS1                   | 内存区域占比_S1                    | Survivor 1区内存使用占比                | %    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilMemoryO                    | 内存区域占比_O                     | Old 区内存使用占比                      | %    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkGcUtilMemoryM                    | 内存区域占比_M                     | Metaspace 区内存使用占比                | %    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkJvmMemMemnonheapcommittedm       | JVM内存_MemNonHeapCommittedM       | JVM 当前已经提交的 NonHeapMemory 的数量 | MB   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkJvmMemMemnonheapusedm            | JVM内存_MemNonHeapUsedM            | JVM 当前已经使用的 NonHeapMemory 的数量 | MB   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkJvmMemMemheapcommittedm          | JVM内存_MemHeapCommittedM          | JVM 已经提交的 HeapMemory 的数量        | MB   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkJvmMemMemheapmaxm                | JVM内存_MemHeapMaxM                | JVM 配置的 HeapMemory 的数量            | MB   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkJvmMemMemheapinitm               | JVM内存_MemHeapInitM               | JVM 初始 HeapMem 的数量                 | MB   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkJvmMemMemnonheapinitm            | JVM内存_MemNonHeapInitM            | JVM 初始 HeapMem 的数量                 | MB   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkJvmMemMemheapusedm               | JVM内存_MemMemHeapUsedM            | JVM 当前已经使用的 HeapMemory 的数量    | MB   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkOsCpuLoadProcesscpuload          | CPU利用率_ProcessCpuLoad           | CPU 利用率                              | %    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkOsFdCountMaxfiledescriptorcount  | 文件句柄数_MaxFileDescriptorCount  | 最大文件描述符数                        | 个   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkOsFdCountOpenfiledescriptorcount | 文件句柄数_OpenFileDescriptorCount | 已打开文件描述符数                      | 个   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkRtUptimeUptime                   | 进程运行时间_Uptime                | 进程运行时长                            | s    | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkThreadCountDaemonthreadcount     | 工作线程数_DaemonThreadCount       | 后台线程数量                            | 个   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkThreadCountThreadcount           | 工作线程数_ThreadCount             | 线程数量                                | 个   | host4dorisdorisbroker、id4dorisdorisbroker |
| DorisBkThreadCountPeakthreadcount       | 工作线程数_PeakThreadCount         | 峰值线程数量                            | 个   | host4dorisdorisbroker、id4dorisdorisbroker |

###  Doris-BE

| 指标英文名                                   | 指标中文名                                     | 指标含义                                              | 单位 | 维度                               |
| -------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------- | ---- | ---------------------------------- |
| DorisBeThriftUsedClientsBroker               | THRIFT使用数量_Broker                          | Broker 使用 thrift 的数量                             | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeThriftUsedClientsBackend              | THRIFT使用数量_Backend                         | BE 使用 thrift 的数量                                 | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeThriftUsedClientsExtdatasource        | THRIFT使用数量_Extdatasource                   | extdatasource 使用 thrift 的数量                      | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeThriftUsedClientsFrontend             | THRIFT使用数量_Frontend                        | FE 使用 thrift 的数量                                 | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeStreamingLoadCountRequeststotal       | STREAMING_LOAD统计_RequestsTotal               | streaming load 请求数量                               | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeStreamingLoadCountCurrentprocessing   | STREAMING_LOAD统计_CurrentProcessing           | streaming load 现有进程数                             | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeStreamingLoadCountPipecount           | STREAMING_LOAD统计_PipeCount                   | streaming load Pipe 数量                              | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeStreamingLoadtimeDuration             | STREAMING_LOAD时间_Duration                    | streaming load 持续时间                               | ms   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeStreamingLoadLoadtotal                | STREAMING_LOAD数据量_Loadtotal                 | stream load 导入的数据大小                            | B    | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeFragmentCountEndpoint                 | FRAGMENT统计_Endpoint                          | DataStream 的数量                                     | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeFragmentCountPlanfragment             | FRAGMENT统计_PlanFragment                      | plan fragment 数量                                    | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeFragmentCountRequeststotal            | FRAGMENT统计_RequestsTotal                     | fragment 的请求次数                                   | 次   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeFragmentRequestTimeDuration           | FRAGMENT请求时间_Duration                      | fragment 的请求时间                                   | us   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeMemoryTotal                           | BE内存_Total                                   | BE memory pool 大小                                   | B    | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeMemoryAllocated                       | BE内存_Allocated                               | BE memory allocated 大小                              | B    | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeTabletCompactionScoreCumulativemax    | TABLET_COMPACTIO最高分__CumulativeMax          | tablet 中最大的 base compaction score                 | -    | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeTabletCompactionScoreBasemax          | TABLET_COMPACTIO最高分_Basemax                 | tablet base 最大 compaction 分数                      | -    | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeCompactionTotalCumulative             | COMPACTION数据量_Cumulative                    | Cumulative compaction 的数据量                        | B    | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeCompactionTotalBase                   | COMPACTION数据量_Base                          | Base compaction 的数据量                              | B    | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeCompactionDeltasCumulative            | COMPACTION_DELTAS数据量_Cumulative             | Cumulative compaction deltas 的数据量                 | B    | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeCompactionDeltasBase                  | COMPACTION_DELTAS数据量_Base                   | Base compaction deltas 的数据量                       | B    | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeCompactionMemCurrentconsumption       | COMPACTION使用的MemPool数量_CurrentConsumption | Compaction 使用的 MemPool 总和 (所有 Compaction 线程) | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeProcessFdNumUsed                      | 进程文件句柄数_ProcessFdNumUsed                | BE 进程使用文件句柄数量                               | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeProcessFdNumSoftlimit                 | 进程文件句柄数_ProcessFdNumSoftlimit           | BE 进程文件句柄 soft 限制数量                         | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeProcessFdNumHardlimit                 | 进程文件句柄数_ProcessFdNumHardlimit           | BE 进程文件句柄 hard 限制数量                         | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeProcessThreadNum                      | 进程运行线程数_ProcessThreadNum                | BE 进程运行的线程个数                                 | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeEngineRequestsNumFailedbasecompaction | ENGINE_REQUESTS统计_FailedBaseCompaction       | 类型为base_compaction，engine 请求失败数量            | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeEngineRequestsNumTotalbasecompaction  | ENGINE_REQUESTS统计_TotalBaseCompaction        | 类型为base_compaction，engine 请求总数                | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeEngineRequestsNumFailedcultcompt      | ENGINE_REQUESTS统计_FailedCultCompt            | 类型为cumulative_compaction，engine 请求失败数量      | 个   | host4dorisdorisbe、id4dorisdorisbe |
| DorisBeEngineRequestsNumTotalcultcompt       | ENGINE_REQUESTS统计_TotalCultCompt             | 类型为cumulative_compaction，engine 请求总数          | 个   | host4dorisdorisbe、id4dorisdorisbe |



### Doris-FE

| 指标英文名                         | 指标中文名                           | 指标含义                                          | 单位  | 维度                               |
| ---------------------------------- | ------------------------------------ | ------------------------------------------------- | ----- | ---------------------------------- |
| DorisFeNodeInfoFenodenum           | 节点信息_FenodeNum                   | FE 总节点数                                       | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeNodeInfoBealivenum          | 节点信息_BealiveNum                  | BE 活动节点数                                     | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeNodeInfoBkdeadnum           | 节点信息_Bkdeadnum                   | Broker 死亡节点数                                 | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeConnectionTotalNum          | CONNECTION数量_Num                   | FE 节点 JVM connection 数量                       | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeJvmThreadCountTotal         | JVM线程数_Total                      | FE节点JVM中线程总数，包含daemon线程和非daemon线程 | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeJvmThreadCountPeak          | JVM线程数_Peak                       | FE节点JVM线程峰值                                 | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeGcCountYounggc              | GC次数_YoungGC                       | FE 节点 JVM Young GC 次数                         | 次    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeGcCountOldgc                | GC次数_OldGC                         | FE 节点JVM Old GC 次数                            | 次    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeGcTimeYounggc               | GC时间_YoungGC                       | FE 节点 JVM Young GC 时间                         | s     | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeGcTimeOldgc                 | GC时间_OldGC                         | FE 节点 JVM Old GC 时间                           | s     | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeQueryLatencyQuantile75      | FE查询延时_Quantile75                | FE 查询延时的75分位数                             | ms    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeQueryLatencyQuantile95      | FE查询延时_Quantile95                | FE 查询延时的95分位数                             | ms    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeQueryLatencyQuantile99      | FE查询延时_Quantile99                | FE 查询延时的99分位数                             | ms    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeQueryLatencyQuantile999     | FE查询延时_Quantile999               | FE 查询延时的99.9分位数                           | ms    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeTabletCompactionMax         | TABLET_COMPACTION最高分_MAX          | FE tablet 进行compaction时compaction score 最大值 | -     | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeTabletNumScheduledtablet    | SCHEDULED_TABLET数量_ScheduledTablet | FE 中 scheduled tablet 数量                       | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeEfficiencyQps               | 请求响应_QPS                         | 每秒查询率                                        | 个/秒 | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeEfficiencyRps               | 请求响应_RPS                         | 每秒能处理的请求数目                              | 个/秒 | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeQueryErrrateErrrate         | 查询失败率_ErrRate                   | 查询错误率                                        | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeCacheSqlmodelhitquery       | 缓存查询_SqlModelHitQuery            | 模式为 sql 的 Query 命中 Cache 的数量             | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeCachePartitionmodelhitquery | 缓存查询_PartitionModelHitQuery      | 通过 Partition 命中的 Query 数量                  | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeCacheSqlmodelquery          | 缓存查询_SqlModelQuery               | 识别缓存模式为 sql 的 Query 数量                  | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeCachePartitionmodelquery    | 缓存查询_PartitionModelQuery         | 识别缓存模式为 Partition 的 Query 数量            | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeCacheCachepartitionhit      | 缓存查询_CachePartitionHit           | 查询中通过 cache 命中的分区数量                   | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeCacheCachepartitionscan     | 缓存查询_CachePartitionScan          | 查询中扫描的所有分区数量                          | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeRoutineLoadTotalrows        | ROUTINE_LOAD行数_TotalRows           | FE routine load的行数                             | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeRoutineLoadErrorrows        | ROUTINE_LOAD行数_ErrorRows           | FE routine load 错误的行数                        | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeTxnCountReject              | TRANSACTION状态统计_Reject           | FE 被拒绝的 transaction 数量                      | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeTxnCountBegin               | TRANSACTION状态统计_Begin            | FE 开始的 transaction 数量                        | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeTxnCountSuccess             | TRANSACTION状态统计_Success          | FE 成功的 transaction 数量                        | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeTxnCountFailed              | TRANSACTION状态统计_Failed           | FE 失败的 transaction 数量                        | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeImageWrite                  | IMAGE统计_Write                      | FE image write 的数量                             | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeImagePush                   | IMAGE统计_Push                       | FE image push 的数量                              | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeAlterJobRolluprunning       | ALTER任务统计_RollupRunning          | 运行中的 alter job,类型为 ROLLUP 的数量           | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeAlterJobSchemachangerunning | ALTER任务统计_SchemaChangeRunning    | 运行中的 alter job,类型为 SCHEMA_CHANGE 的数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeUnknownLoadJobCancelled     | UNKNOWN_LOAD任务统计_Cancelled       | 类型为 UNKNOWN，状态为 CANCELLED 的 load job 数量 | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeUnknownLoadJobCommitted     | UNKNOWN_LOAD任务统计_Committed       | 类型为 UNKNOWN，状态为 COMMITTED 的 load job 数量 | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeUnknownLoadJobEtl           | UNKNOWN_LOAD任务统计_Etl             | 类型为 UNKNOWN，状态为 ETL 的 load job 数量       | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeUnknownLoadJobFinished      | UNKNOWN_LOAD任务统计_Finished        | 类型为 UNKNOWN，状态为 FINISHED 的 load job 数量  | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeUnknownLoadJobLoading       | UNKNOWN_LOAD任务统计_Loading         | 类型为 UNKNOWN，状态为 LOADING 的 load job 数量   | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeUnknownLoadJobPending       | UNKNOWN_LOAD任务统计_Pending         | 类型为 SPARK，状态为 PENDING 的load job 数量      | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeUnknownLoadJobUnknown       | UNKNOWN_LOAD任务统计_Unknown         | 类型为 SPARK，状态为 UNKNOWN 的load job 数量      | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeSparkLoadJobCancelled       | SPARK_LOAD任务统计_Cancelled         | 类型为 UNKNOWN，状态为 CANCELLED 的 load job 数量 | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeSparkLoadJobCommitted       | SPARK_LOAD任务统计_Committed         | 类型为 UNKNOWN，状态为 COMMITTED 的 load job 数量 | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeSparkLoadJobEtl             | SPARK_LOAD任务统计_Etl               | 类型为 SPARK，状态为 ETL 的load job 数量          | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeSparkLoadJobFinished        | SPARK_LOAD任务统计_Finished          | 类型为 SPARK，状态为 FINISHED 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeSparkLoadJobLoading         | SPARK_LOAD任务统计_Loading           | 类型为 SPARK，状态为 LOADING 的load job 数量      | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeSparkLoadJobPending         | SPARK_LOAD任务统计_Pending           | 类型为 DELETE，状态为 PENDING 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeSparkLoadJobUnknown         | SPARK_LOAD任务统计_Unknown           | 类型为 DELETE，状态为 UNKNOWN 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeDeleteLoadJobCancelled      | DELETE_LOAD任务统计_Cancelled        | 类型为 SPARK，状态为 CANCELLED 的 load job 数量   | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeDeleteLoadJobCommitted      | DELETE_LOAD任务统计_Committed        | 类型为 DELETE，状态为 COMMITTED 的 load job 数量  | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeDeleteLoadJobEtl            | DELETE_LOAD任务统计_Etl              | 类型为 DELETE，状态为 ETL 的 load job 数量        | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeDeleteLoadJobFinished       | DELETE_LOAD任务统计_Finished         | 类型为 DELETE，状态为 FINISHED 的 load job 数量   | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeDeleteLoadJobLoading        | DELETE_LOAD任务统计_Loading          | 类型为 DELETE，状态为LOADING 的 load job 数量     | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeDeleteLoadJobPending        | DELETE_LOAD任务统计_Pending          | 类型为 DELETE，状态为 PENDING 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeDeleteLoadJobUnknown        | DELETE_LOAD任务统计_Unknown          | 类型为 DELETE，状态为 UNKNOWN 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeInsertLoadJobCancelled      | INSERT_LOAD任务统计_Cancelled        | 类型为 DELETE，状态为 CANCELLED 的 load job 数量  | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeInsertLoadJobEtl            | INSERT_LOAD任务统计_Etl              | 类型为 INSERT，状态为 ETL 的 load job 数量        | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeInsertLoadJobFinished       | INSERT_LOAD任务统计_Finished         | 类型为 INSERT，状态为 FINISHED 的 load job 数量   | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeInsertLoadJobLoading        | INSERT_LOAD任务统计_Loading          | 类型为 INSERT，状态为 LOADING 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeInsertLoadJobPending        | INSERT_LOAD任务统计_Pending          | 类型为 INSERT，状态为 UNKNOWN 的load job 数量     | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeInsertLoadJobUnknown        | INSERT_LOAD任务统计_Unknown          | 类型为 INSERT，状态为 UNKNOWN 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeBrokerLoadJobCancelled      | BROKER_LOAD任务统计_Cancelled        | 类型为 BROKER，状态为 CANCELLED 的 load job 数量  | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeBrokerLoadJobCommitted      | BROKER_LOAD任务统计_Committed        | 类型为 BROKER，状态为 COMMITTED 的 load job 数量  | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeBrokerLoadJobEtl            | BROKER_LOAD任务统计_Etl              | 类型为 BROKER，状态为 ETL 的 load job 数量        | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeBrokerLoadJobFinished       | BROKER_LOAD任务统计_Finished         | 类型为 BROKER，状态为 FINISHED 的 load job 数量   | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeBrokerLoadJobLoading        | BROKER_LOAD任务统计_Loading          | 类型为 BROKER，状态为 LOADING 的load job 数量     | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeBrokerLoadJobPending        | BROKER_LOAD任务统计_Pending          | 类型为 BROKER，状态为 PENDING 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeBrokerLoadJobUnknown        | BROKER_LOAD任务统计_Unknown          | 类型为 BROKER，状态为 UNKNOWN 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeMiniLoadJobCancelled        | MINI_LOAD任务统计_Cancelled          | 类型为 MINI，状态为 CANCELLED 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeMiniLoadJobCommitted        | MINI_LOAD任务统计_Committed          | 类型为 HADOOP，状态为 COMMITTED 的 load job 数量  | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeMiniLoadJobEtl              | MINI_LOAD任务统计_Etl                | 类型为 MINI，状态为 ETL 的load job 数量           | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeMiniLoadJobFinished         | MINI_LOAD任务统计_Finished           | 类型为 MINI，状态为 FINISHED 的 load job 数量     | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeMiniLoadJobLoading          | MINI_LOAD任务统计_Loading            | 类型为 MINI，状态为 LOADING 的load job 数量       | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeMiniLoadJobPending          | MINI_LOAD任务统计_Pending            | 类型为 MINI，状态为 PENDING 的load job 数量       | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeMiniLoadJobUnknown          | MINI_LOAD任务统计_Unknown            | 类型为 MINI，状态为 UNKNOWN 的load job 数量       | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeHadoopLoadJobCancelled      | HADOOP_LOAD任务统计_Cancelled        | 类型为 HADOOP，状态为 CANCELLED 的 load job 数量  | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeHadoopLoadJobCommitted      | HADOOP_LOAD任务统计_Committed        | 类型为 HADOOP，状态为 COMMITTED 的 load job 数量  | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeHadoopLoadJobEtl            | HADOOP_LOAD任务统计_Etl              | 类型为 HADOOP，状态为 ETL 的 load job 数量        | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeHadoopLoadJobFinished       | HADOOP_LOAD任务统计_Finished         | 类型为 HADOOP，状态为 FINISHED 的 load job 数量   | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeHadoopLoadJobLoading        | HADOOP_LOAD任务统计_Loading          | 类型为 HADOOP，状态为 LOADING 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeHadoopLoadJobPending        | HADOOP_LOAD任务统计_Pending          | 类型为 HADOOP，状态为 PENDING 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeHadoopLoadJobUnknown        | HADOOP_LOAD任务统计_Unknown          | 类型为 HADOOP，状态为 UNKNOWN 的 load job 数量    | 个    | host4dorisdorisfe、id4dorisdorisfe |
| DorisFeInsertLoadJobCommitted      | INSERT_LOAD任务统计_Committed        | 类型为 Insert ，状态为 COMMITTED 的 load job 数量 | 个    | host4dorisdorisfe、id4dorisdorisfe |



## 各维度对应参数总览

| 参数名称                       | 维度名称              | 维度解释                     | 格式                                                         |
| :----------------------------- | :-------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | host4dorisdorisbroker | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：host4dorisdorisbroker              |
| Instances.N.Dimensions.0.Value | host4dorisdorisbroker | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | id4dorisdorisbroker   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4dorisdorisbroker                |
| Instances.N.Dimensions.0.Value | id4dorisdorisbroker   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4dorisdorisbe     | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4dorisdorisbe                  |
| Instances.N.Dimensions.0.Value | host4dorisdorisbe     | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4dorisdorisbe       | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4dorisdorisbe                    |
| Instances.N.Dimensions.0.Value | id4dorisdorisbe       | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4dorisdorisfe     | EMR 实例中节点 IP 的维度名称 | host4dorisdorisfe                                            |
| Instances.N.Dimensions.0.Value | host4dorisdorisfe     | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4dorisdorisfe       | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4dorisdorisfe                    |
| Instances.N.Dimensions.0.Value | id4dorisdorisfe       | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |



## 入参说明

**查询弹性 MapReduce（Doris-BK）监控数据，入参取值如下：**

Namespace=QCE/TXMR_DORIS
&Instances.N.Dimensions.0.Name=host4dorisdorisbroker
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4dorisdorisbroker
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID



**查询弹性 MapReduce（Doris-BE）监控数据，入参取值如下：**

Namespace=QCE/TXMR_DORIS
&Instances.N.Dimensions.0.Name=host4dorisdorisbe
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4dorisdorisbe
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID



**查询弹性 MapReduce（Doris-FE）监控数据，入参取值如下：**

Namespace=QCE/TXMR_DORIS
&Instances.N.Dimensions.0.Name=host4dorisdorisfe
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4dorisdorisfe
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID

