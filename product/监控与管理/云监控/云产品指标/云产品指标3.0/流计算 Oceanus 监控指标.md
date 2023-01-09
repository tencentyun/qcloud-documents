## 命名空间

Namespace=QCE/TSTREAM

## 监控指标

| 指标英文名                                   | 指标中文名                                    | 指标含义                                                     | 单位    | 维度    |
| -------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------ | ------- | ------- |
| JobRestartingtime                            | 作业重启耗时                                  | 作业最近一次重启耗时                                         | ms      | tjob_id |
| JobmanagerLastcheckpointrestoretimestamp     | 作业最近一次恢复的时间戳                      | 作业最近一次从快照恢复的 Unix 时间戳（以毫秒为单位，如果未恢复过则是 -1） | ms      | tjob_id |
| TaskmanagerJvmThreadsCount                   | TaskManager 活动线程数                        | 作业中所有 TaskManager 中活动的线程数之和，含 Daemon 和非 Daemon 线程。 | 个      | tjob_id |
| TaskmanagerMemoryNonheapCommitted            | TaskManager 已提交的非堆内存容量              | 作业中所有 TaskManager 已提交（committed）的非堆内存（JVM 元空间、代码缓存等）用量总和 | Bytes   | tjob_id |
| TaskmanagerMemoryHeapCommitted               | TaskManager 已提交的堆内存容量                | 作业中所有 TaskManager 已提交（committed）的堆内存容量总和   | Bytes   | tjob_id |
| TaskmanagerNetworkTotalmemorysegments        | TaskManager 已分配的 MemorySegment 总数       | 作业中所有 TaskManager 已分配的 MemorySegment 个数总和       | Bytes   | tjob_id |
| TaskmanagerJvmYoungGcTime                    | TaskManager 年轻代 GC 时间                    | 作业中所有 TaskManager 年轻代 GC 时间之和                    | ms      | tjob_id |
| TaskmanagerJvmYoungGcCount                   | TaskManager 年轻代 GC 次数                    | 作业中所有 TaskManager 年轻代 GC 次数之和                    | 次      | tjob_id |
| TaskmanagerJvmOldGcTime                      | TaskManager 老年代 GC 时间                    | 作业中所有 TaskManager 老年代 GC 时间之和                    | ms      | tjob_id |
| TaskmanagerJvmOldGcCount                     | TaskManager 年轻代 GC 次数                    | 作业中所有 TaskManager 老年代 GC 次数之和                    | 次      | tjob_id |
| TaskmanagerStatusJvmMemoryNonheapMax         | TaskManager 非堆内存最大容量                  | 作业中所有 TaskManager 非堆内存（JVM 元空间、代码缓存等）最大容量总和 | Bytes   | tjob_id |
| TaskmanagerMemoryDirectCount                 | TaskManager 堆外直接内存缓存数                | 作业中所有 TaskManager 堆外直接内存（Direct Buffer Pool）中的缓存（Buffer）个数之和 | 个      | tjob_id |
| TaskmanagerMemoryDirectTotalcapacity         | TaskManager 堆外直接内存总容量                | 作业中所有 TaskManager 堆外直接内存（Direct Buffer Pool）的最大容量之和 | Bytes   | tjob_id |
| TaskmanagerMemoryMappedCount                 | TaskManager 堆外映射内存缓存数                | 作业中所有 TaskManager 堆外映射内存（Mapped Buffer Pool）中的缓存（Buffer）个数之和 | 个      | tjob_id |
| TaskmanagerMemoryMappedTotalcapacity         | TaskManager 堆外映射内存总容量                | 作业中所有 TaskManager 堆外映射内存（Mapped Buffer Pool）的最大容量之和 | Bytes   | tjob_id |
| TaskmanagerStatusJvmMemoryHeapUsedPercentage | TaskManager 堆内存使用率                      | 作业中所有 TaskManager 的平均堆内存使用率                    | %       | tjob_id |
| TaskmanagerNetworkAvailablememorysegments    | TaskManager 可用的 MemorySegment 个数         | 作业中所有 TaskManager 的可用 MemorySegment 个数之和         | Bytes   | tjob_id |
| JobMemoryHeapMax                             | TaskManager 堆内存最大容量                    | 作业中所有 TaskManager 的堆内存最大（max）容量总和           | Bytes   | tjob_id |
| TaskmanagerCpuTime                           | TaskManager CPU 使用时长                      | 作业中所有 TaskManager CPU 使用时长总和（毫秒）              | ms      | tjob_id |
| JobBytesInPerSecond                          | 作业每秒输入的数据量                          | 作业所有数据源（Source）每秒输入的数据总量（仅对 Kafka Source 有效） | Bytes/s | tjob_id |
| JobBytesOutPerSecond                         | 作业每秒输出的数据量                          | 作业所有数据目的（Sink）每秒输出的数据总量（仅对 Kafka Sink 有效） | Bytes/s | tjob_id |
| JobmanagerNumrunningjobs                     | 运行中的作业数                                | 正在运行中作业数。如果作业正常运行，则值为 1. 如果作业崩溃则值为 0 | 个      | tjob_id |
| TaskmanagerStatusJvmMemoryProcessMemoryused  | 所有 TaskManager JVM 的物理内存用量的最大值   | 所有 TaskManager JVM 的物理内存用量的最大值                  | Bytes   | tjob_id |
| JobNumrecordsinbutfailed                     | 严重异常数据个数                              | 算子中发生严重异常（例如抛出各种 Exception）的数据个数，如果大于 1 则会影响 Exactly-Once 语义（试验参数，仅供参考） | 个      | tjob_id |
| Syndelay                                     | 数据源同步百分比                              | 数据源同步百分比                                             | %       | tjob_id |
| Binlogpos                                    | 数据源日志位点信息                            | 数据源日志位点信息                                           | -       | tjob_id |
| TaskmanagerJobTaskOperatorKafkaSwitch        | 是否包含 Kafka connector                      | 是否包含 Kafka connector                                     | -       | tjob_id |
| JobmanagerTaskslotsavailable                 | 可用任务槽数量                                | 如果作业正常运行，则可用的任务槽（Task Slot）数为 0. 如果不为 0 则说明作业可能出现短时间的非运行状态 | 个      | tjob_id |
| JobUptime                                    | 作业无中断持续执行的时间                      | 对于运行中的作业，表示当次作业持续处于运行中的时长           | ms      | tjob_id |
| JobmanagerDowntime                           | 注册的 TaskManager 数                         | 对于失败或恢复等非运行状态的作业，表示本次中断运行的时长。对于正在运行中的作业，值为 0. | ms      | tjob_id |
| JobLastcheckpointduration                    | 最近一次的 Checkpoint 耗时                    | 当前作业最近一次的 Checkpoint 耗时                           | ms      | tjob_id |
| JobLastcheckpointsize                        | 最近一次的 Checkpoint 大小                    | 当前作业最近一次的 Checkpoint 大小                           | Bytes   | tjob_id |
| JobmanagerNumregisteredtaskmanagers          | JobManager 已注册的 TaskManager 数            | 当前作业已注册的 TaskManager 数，通常等于所有算子并行度的最大值。如果 TaskManager 个数减少，说明存在 TaskManager 失联，作业可能崩溃并尝试恢复。 | 个      | tjob_id |
| JobmanagerMemoryNonheapCommitted             | JobManager 已提交的非堆内存容量               | 当前作业已提交（committed）的 JobManager 非堆内存（JVM 元空间、代码缓存等）容量 | Bytes   | tjob_id |
| JobmanagerNumberofinprogresscheckpoints      | 正在进行的 Checkpoint 个数                    | 当前作业进行中（未完成）的 Checkpoint 个数                   | 个      | tjob_id |
| JobmanagerThreadsCount                       | JobManager 中活动的线程数                     | 当前作业 JobManager 中活动的线程数，含 Daemon 和非 Daemon 线程。 | 个      | tjob_id |
| JobmanagerMemoryHeapCommitted                | JobManager 已提交的堆内存容量                 | 当前作业 JobManager 已提交（committed）的堆内存容量          | Bytes   | tjob_id |
| JobmanagerJvmYoungGcTime                     | JobManager 年轻代 GC 时间                     | 当前作业 JobManager 年轻代 GC 时间                           | ms      | tjob_id |
| JobmanagerJvmYoungGcCount                    | JobManager 年轻代 GC 次数                     | 当前作业 JobManager 年轻代 GC 次数                           | 次      | tjob_id |
| JobmanagerJvmOldGcTime                       | JobManager 老年代 GC 时间                     | 当前作业 JobManager 老年代 GC 时间                           | ms      | tjob_id |
| JobmanagerJvmOldGcCount                      | JobManager 老年代 GC 次数                     | 当前作业 JobManager 老年代 GC 次数                           | 次      | tjob_id |
| JobmanagerStatusJvmMemoryNonheapUsed         | JobManager 非堆内存用量                       | 当前作业 JobManager 非堆内存（JVM 元空间、代码缓存等）用量   | Bytes   | tjob_id |
| JobmanagerStatusJvmMemoryNonheapMax          | JobManager 非堆内存最大容量                   | 当前作业 JobManager 非堆内存（JVM 元空间、代码缓存等）的最大容量 | Bytes   | tjob_id |
| JobmanagerMemoryHeapMax                      | JobManager 堆内存最大容量                     | 当前作业 JobManager 堆内存最大容量                           | Bytes   | tjob_id |
| JobmanagerStatusJvmMemoryHeapUsedPercentage  | JobManager 堆内存使用率                       | 当前作业 JobManager 堆内存使用率                             | %       | tjob_id |
| JobmanagerStatusJvmMemoryHeapUsed            | JobManager 堆内存的用量                       | 当前作业 JobManager 堆内存的用量                             | Bytes   | tjob_id |
| JobmanagerCpuLoad                            | JobManager CPU 使用率                         | 当前作业 JobManager 的 CPU 使用率                            | %       | tjob_id |
| JobmanagerCpuTime                            | JobManager CPU 使用时长                       | 当前作业 JobManager CPU 使用时长（毫秒）                     | ms      | tjob_id |
| JobNumberoffailedcheckpoints                 | Checkpoint 失败次数                           | 当前作业 Checkpoint 失败（例如超时、遇到异常等）的次数       | 次      | tjob_id |
| JobNumberofcompletedcheckpoints              | Checkpoint 成功次数                           | 当前作业 Checkpoint 成功完成的次数                           | 次      | tjob_id |
| JobmanagerJobNumrestarts                     | 当前实例崩溃重启次数                          | 当前实例 JobManager 记录的任务崩溃重启次数（不含 JobManager 退出后作业重新拉起的场景） | 次      | tjob_id |
| RecordsLagMaxMin                             | Kafka - Records_Lag 最小值                    | TaskManger 上报的 Kafka 最大 lag 指标最小值                  | -       | tjob_id |
| RecordsLagMaxSum                             | Kafka - Records_Lag 最大值                    | TaskManger 上报的 Kafka 最大 lag 指标的求和值                | -       | tjob_id |
| RecordsLagMaxAvg                             | Kafka - Records_Lag 均值                      | TaskManger 上报的 Kafka 最大 lag 指标的均值                  | -       | tjob_id |
| RecordsLagMax                                | Kafka - Records_Lag 最大指标                  | TaskManger 上报的 Kafka 最大 lag 指标                        | -       | tjob_id |
| Sourceidletime                               | Source 处理的空闲时间                         | Source 处理的空闲时间                                        | ms      | tjob_id |
| Currentfetcheventtimelag                     | Source Fetch消息的延迟时间                    | Source Fetch消息的延迟时间(EmitTime-messageTimestamp)        | ms      | tjob_id |
| Dbflushdelay                                 | Sink 刷新延迟                                 | Sink 刷新延迟                                                | ms      | tjob_id |
| JobmanagerTaskslotstotal                     | 任务槽总数                                    | Oceanus 中一个 TaskManager 只有一个任务槽，因此任务槽总数等于注册的 TaskManager 数 | 个      | tjob_id |
| JobmanagerStatusJvmMemoryProcessMemoryused   | JobManager 所在的 JVM 的物理内存用量          | JobManager 所在的 JVM 的物理内存用量                         | Bytes   | tjob_id |
| JobmanagerMemoryDirectCount                  | JobManager 堆外直接内存中的缓存数             | JobManager 堆外直接内存（Direct Buffer Pool）中的缓存（Buffer）个数 | 个      | tjob_id |
| JobmanagerMemoryDirectTotalcapacity          | JobManager 堆外直接内存总容量                 | JobManager 堆外直接内存（Direct Buffer Pool）的最大用量      | Bytes   | tjob_id |
| JobmanagerMemoryDirectMemoryused             | JobManager 堆外直接内存使用量                 | JobManager 堆外直接内存（Direct Buffer Pool）的用量          | Bytes   | tjob_id |
| JobmanagerMemoryMappedCount                  | JobManager 堆外存缓存个数                     | JobManager 堆外映射内存（Mapped Buffer Pool）中的缓存（Buffer）个数之和 | 个      | tjob_id |
| JobmanagerMemoryMappedTotalcapacity          | JobManager 堆外映射内存的总容量               | JobManager 堆外映射内存（Mapped Buffer Pool）的最大用量      | Bytes   | tjob_id |
| JobmanagerMemoryMappedMemoryused             | JobManager 堆外映射内存的使用量               | JobManager 堆外映射内存（Mapped Buffer Pool）的用量          | Bytes   | tjob_id |
| JobTotalnumberofcheckpoints                  | Checkpoint 总次数                             | Checkpoint 总次数（进行中、已完成和失败的总和）              | 次      | tjob_id |
| Currentemiteventtimelag                      | CDC Source 处理发送下游的时间与消息本身时间差 | CDC Source 处理发送下游的时间与消息本身时间差                | ms      | tjob_id |
| TaskmanagerJobTaskOperatorSchemachange       | CDC Schema 变更次数                           | CDC Schema 变更次数                                          | 次      | tjob_id |

## 各维度对应参数总览

| 参数名称                       | 维度名称 | 维度解释           | 格式                                                         |
| :----------------------------- | :------- | :----------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | tjob_id  | 作业 ID 的维度名称 | 输入 String 类型维度名称：tjob_id                            |
| Instances.N.Dimensions.0.Value | tjob_id  | 具体作业 ID        | 输入具体作业 ID ，可从 [DescribeJobs](https://cloud.tencent.com/document/product/849/52008) 中获取 JobId 字段 |

## 入参说明

**查询云服务器监控数据，入参取值如下：**
&Namespace=QCE/TSTREAM
&Instances.N.Dimensions.0.Name=tjob_id
&Instances.N.Dimensions.0.Value=具体作业 ID
