文档主要介绍 FE 的相关监控项。

## 监控指标列表
|指标名称|前台标题|指标Tag名称|单位|指标含义|英文指标含义|统计方法|
|-------|-------|-------|-------|-------|-------|-------|
|DORIS.FE.MASTER|主节点|IsMaster||是否为fe master节点|Is or not master node of fe|数据来源Doris的metrics接口,node_info{type=is_master}|
|DORIS.FE.CONNECTION.TOTAL|connection 数量|Num|count|FE节点JVM connection 数量|The total number of doris fe connection|数据来源Doris的metrics接口,doris_fe_connection_total|
|DORIS.FE.JVM.THREAD.COUNT|JVM THREAD|Total|count|FE节点JVM中线程总数，包含daemon线程和非daemon线程|Doris fe jvm thread total count|数据来源Doris的metrics接口,jvm_thread{type=count}|
|||Peak|count|FE节点JVM线程峰值|Doris fe jvm thread peak count|数据来源Doris的metrics接口,jvm_thread{type=peak_count}|
|||New|count|FE节点JVM中处于NEW状态的线程数量|Doris fe jvm thread new count|数据来源Doris的metrics接口,jvm_thread{type=new_count}|
|||Runnable|count|FE节点JVM中处于runnable状态的线程数量|Doris fe jvm thread runnable count|数据来源Doris的metrics接口,jvm_thread{type=runnable_count}|
|||Blocked|count|FE节点JVM中处于BLOCKED状态的线程数量|Doris fe jvm thread blocked count|数据来源Doris的metrics接口,jvm_thread{type=blocked_count}|
|||Waiting|count|FE节点JVM中处于TIMED_WAITING状态的线程数量|Doris fe jvm thread waiting count|数据来源Doris的metrics接口,jvm_thread{type=waiting_count}|
|||TimedWaiting|count|FE节点JVM中处于TERMINATED状态的线程数量|Doris fe jvm thread timed waiting count|数据来源Doris的metrics接口,jvm_thread{type=timed_waiting_count}|
|||Terminated|count|FE节点JVM中处于TERMINATED状态的线程数量|Doris fe jvm thread terminated count|数据来源Doris的metrics接口,jvm_thread{type=terminated_count}|
|DORIS.FE.GC.COUNT|GC COUNT|YoungGC|count|FE节点JVM Young GC 次数|Doris fe jvm young gc count|数据来源Doris的metrics接口,jvm_young_gc{type=count}|
|||OldGC|count|FE节点JVM Old GC 次数|Doris fe jvm old gc count|数据来源Doris的metrics接口,jvm_old_gc{type=count}|
|DORIS.FE.GC.TIME|GC TIME|YoungGC|s|FE节点JVM Young GC 时间|Doris fe jvm young gc time|数据来源Doris的metrics接口,jvm_young_gc{type=time}|
|||OldGC|s|FE节点JVM Old GC 时间|Doris fe jvm old gc time|数据来源Doris的metrics接口,jvm_old_gc{type=time}|
|DORIS.FE.QUERY.LATENCY|QUERY LATENCY|Quantile75|ms|FE查询延时的75分位数|Doris fe query latency time that quantile is 0.75|数据来源Doris的metrics接口,doris_fe_query_latency_ms{quantile=0.75}|
|||Quantile95|ms|FE查询延时的95分位数|Doris fe query latency time that quantile is 0.95|数据来源Doris的metrics接口,doris_fe_query_latency_ms{quantile=0.95}|
|||Quantile99|ms|FE查询延时的99分位数|Doris fe query latency time that quantile is 0.99|数据来源Doris的metrics接口,doris_fe_query_latency_ms{quantile=0.99}|
|||Quantile99.9|ms|FE查询延时的99.9分位数|Doris fe query latency time that quantile is 0.999|数据来源Doris的metrics接口,doris_fe_query_latency_ms{quantile=0.999}|
|DORIS.FE.TABLET.COMPACTION|TABLET COMPACTION SCOR|max|score|FE tablet进行compaction时compaction score最大值|Doris fe tablet compaction max scor|数据来源Doris的metrics接口,doris_fe_max_tablet_compaction_scor|
|DORIS.FE.TABLET.NUM|SCHEDULED TABLET 数量|ScheduledTablet|count|FE 中 scheduled tablet数量|Doris fe scheduled tablet num|数据来源Doris的metrics接口,doris_fe_scheduled_tablet_num|
|DORIS.FE.EFFICIENCY|请求&响应|QPS|count|每秒查询率|Doris fe qps|数据来源Doris的metrics接口,doris_fe_qps|
|||RPS|count|每秒能处理的请求数目|Doris fe rps|数据来源Doris的metrics接口,doris_fe_rps|||
|DORIS.FE.QUERY.ERRRATE|QUERY ERR RATE|ErrRate|%|查询错误率|Doris fe err rate of query|数据来源Doris的metrics接口,doris_fe_query_err_rate|
|DORIS.FE.CACHE|缓存查询|SqlModelHitQuery|count|模式为sql的Query命中Cache的数量|Doris fe total hits query by sql model|数据来源Doris的metrics接口,doris_fe_cache_hit_sql|
|||PartitionModelHitQuery|count|通过Partition命中的Query数量|Doris fe total hits query by partition model|数据来源Doris的metrics接口,doris_fe_cache_hit_partition|||
|||SqlModelQuery|count|识别缓存模式为sql的Query数量|The total count of query of sql mode|数据来源Doris的metrics接口,doris_fe_cache_mode_sql|||
|||PartitionModelQuery|count|识别缓存模式为Partition的Query数量|The total count of query of partition mode|数据来源Doris的metrics接口,doris_fe_query_mode_partition|||
|||CachePartitionHit|count|查询中通过cache命中的分区数量|The counter of hit partition of cache partition model|数据来源Doris的metrics接口,doris_fe_partition_hit|||
|||CachePartitionScan|count|查询中扫描的所有分区数量|The counter of scan partition of cache partition model|数据来源Doris的metrics接口,doris_fe_partition_all|||
|DORIS.FE.ROUTINE.LOAD|ROUTINE LOAD|TotalRows|count|FE routine load的行数|The rows of routine load|数据来源Doris的metrics接口,doris_fe_routine_load_rows|
|||ErrorRows|count|FE routine load 错误的行数|The total error rows of routine load|数据来源Doris的metrics接口,doris_fe_routine_load_error_rows|||
|DORIS.FE.TXN.COUNT|TRANSACTION STATUS|Reject|count|FE 被拒绝的transaction数量|The counter of rejected transactions|数据来源Doris的metrics接口,doris_fe_txn_reject|
|||Begin|count|FE 开始的transaction数量|The counter of beginning transactions|数据来源Doris的metrics接口,doris_fe_txn_begin|||
|||Success|count|FE 成功的transaction数量|The counter of success transactions|数据来源Doris的metrics接口,doris_fe_txn_success|||
|||Failed|count|FE 失败的transaction数量|The counter of failed transactions|数据来源Doris的metrics接口,doris_fe_txn_failed|||
|DORIS.FE.IMAGE|IMAGE|Write|count|FE image write 的数量|the counter of image generated|数据来源Doris的metrics接口,doris_fe_image_write|
|||Push|count|FE image push 的数量|Doris fe the counter of image succeeded in pushing to other frontends|数据来源Doris的metrics接口,doris_fe_image_push|||
|DORIS.FE.ALTER.JOB|ALTER JOB|RollupRunning|count|运行中的alter job,类型为ROLLUP的数量|Doris fe alter job of ROLLUP, state is running|数据来源Doris的metrics接口,doris_fe_job{job=alter|type=ROLLUP|state=running}|
|||SchemaChangeRunning|count|运行中的alter job,类型为SCHEMA_CHANGE的数量|Doris fe alter job of SCHEMA_CHANGE, state is "running"|数据来源Doris的metrics接口,doris_fe_job{job=alter|type=SCHEMA_CHANGE|state=running}|
|DORIS.FE.UNKNOWN.LOAD.JOB|UNKNOWN LOAD JOB|UNKNOWN|count|类型为UNKNOWN，状态为UNKNOWN 的load job 数量|Doris fe load job of UNKNOWN, state is "UNKNOWN"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=UNKNOWN|state=UNKNOWN}|
|||PENDING|count|类型为UNKNOWN，状态为PENDING 的load job 数量|Doris fe load job of UNKNOWN, state is "PENDING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=UNKNOWN|state=PENDING}|
|||ETL|count|类型为UNKNOWN，状态为ETL 的load job 数量|Doris fe load job of UNKNOWN, state is "ETL"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=UNKNOWN|state=ETL}|
|||LOADING|count|类型为UNKNOWN，状态为LOADING 的load job 数量|Doris fe load job of UNKNOWN, state is "LOADING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=UNKNOWN|state=LOADING}|
|||COMMITTED|count|类型为UNKNOWN，状态为COMMITTED 的load job 数量|Doris fe load job of UNKNOWN, state is "COMMITTED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=UNKNOWN|state=COMMITTED}|
|||FINISHED|count|类型为UNKNOWN，状态为FINISHED 的load job 数量|Doris fe load job of UNKNOWN, state is "FINISHED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=UNKNOWN|state=FINISHED}|
|||CANCELLED|count|类型为UNKNOWN，状态为CANCELLED 的load job 数量|Doris fe load job of UNKNOWN, state is "CANCELLED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=UNKNOWN|state=CANCELLED}|
|DORIS.FE.SPARK.LOAD.JOB|SPARK LOAD JOB|UNKNOWN|count|类型为SPARK，状态为UNKNOWN 的load job 数量|Doris fe load job of SPARK, state is "UNKNOWN"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=SPARK|state=UNKNOWN}|
|||PENDING|count|类型为SPARK，状态为PENDING 的load job 数量|Doris fe load job of SPARK, state is "PENDING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=SPARK|state=PENDING}|
|||ETL|count|类型为SPARK，状态为ETL 的load job 数量|Doris fe load job of SPARK, state is "ETL"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=SPARK|state=ETL}|
|||LOADING|count|类型为SPARK，状态为LOADING 的load job 数量|Doris fe load job of SPARK, state is "LOADING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=SPARK|state=LOADING}|
|||COMMITTED|count|类型为SPARK，状态为COMMITTED 的load job 数量|Doris fe load job of SPARK, state is "COMMITTED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=SPARK|state=COMMITTED}|
|||FINISHED|count|类型为SPARK，状态为FINISHED 的load job 数量|Doris fe load job of SPARK, state is "FINISHED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=SPARK|state=FINISHED}|
|||CANCELLED|count|类型为SPARK，状态为CANCELLED 的load job 数量|Doris fe load job of SPARK, state is "CANCELLED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=SPARK|state=CANCELLED}|
|DORIS.FE.DELETE.LOAD.JOB|DELETE LOAD JOB|UNKNOWN|count|类型为DELETE，状态为UNKNOWN 的load job 数量|Doris fe load job of DELETE, state is "UNKNOWN"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=DELETE|state=UNKNOWN}|
|||PENDING|count|类型为DELETE，状态为PENDING 的load job 数量|Doris fe load job of DELETE, state is "PENDING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=DELETE|state=PENDING}|
|||ETL|count|类型为DELETE，状态为ETL 的load job 数量|Doris fe load job of DELETE, state is "ETL"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=DELETE|state=ETL}|
|||LOADING|count|类型为DELETE，状态为LOADING 的load job 数量|Doris fe load job of DELETE, state is "LOADING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=DELETE|state=LOADING}|
|||COMMITTED|count|类型为DELETE，状态为COMMITTED 的load job 数量|Doris fe load job of DELETE, state is "COMMITTED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=DELETE|state=COMMITTED}|
|||FINISHED|count|类型为DELETE，状态为FINISHED 的load job 数量|Doris fe load job of DELETE, state is "FINISHED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=DELETE|state=FINISHED}|
|||CANCELLED|count|类型为DELETE，状态为CANCELLED 的load job 数量|Doris fe load job of DELETE, state is "CANCELLED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=DELETE|state=CANCELLED}|
|DORIS.FE.INSERT.LOAD.JOB|INSERT LOAD JOB|UNKNOWN|count|类型为INSERT，状态为UNKNOWN 的load job 数量|Doris fe load job of INSERT, state is "UNKNOWN"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=INSERT|state=UNKNOWN}|
|||PENDING|count|类型为INSERT，状态为PENDING 的load job 数量|Doris fe load job of INSERT, state is "PENDING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=INSERT|state=PENDING}|
|||ETL|count|类型为INSERT，状态为ETL 的load job 数量|Doris fe load job of INSERT, state is "ETL"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=INSERT|state=ETL}|
|||LOADING|count|类型为INSERT，状态为LOADING 的load job 数量|Doris fe load job of INSERT, state is "LOADING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=INSERT|state=LOADING}|
|||COMMITTED|count|类型为INSERT，状态为COMMITTED 的load job 数量|Doris fe load job of INSERT, state is "COMMITTED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=INSERT|state=COMMITTED}|
|||FINISHED|count|类型为INSERT，状态为FINISHED 的load job 数量|Doris fe load job of INSERT, state is "FINISHED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=INSERT|state=FINISHED}|
|||CANCELLED|count|类型为INSERT，状态为CANCELLED 的load job 数量|Doris fe load job of INSERT, state is "CANCELLED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=INSERT|state=CANCELLED}|
|DORIS.FE.BROKER.LOAD.JOB|BROKER LOAD JOB|UNKNOWN|count|类型为BROKER，状态为UNKNOWN 的load job 数量|Doris fe load job of BROKER, state is "UNKNOWN"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=BROKER|state=UNKNOWN}|
|||PENDING|count|类型为BROKER，状态为PENDING 的load job 数量|Doris fe load job of BROKER, state is "PENDING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=BROKER|state=PENDING}|
|||ETL|count|类型为BROKER，状态为ETL 的load job 数量|Doris fe load job of BROKER, state is "ETL"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=BROKER|state=ETL}|
|||LOADING|count|类型为BROKER，状态为LOADING 的load job 数量|Doris fe load job of BROKER, state is "LOADING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=BROKER|state=LOADING}|
|||COMMITTED|count|类型为BROKER，状态为COMMITTED 的load job 数量|Doris fe load job of BROKER, state is "COMMITTED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=BROKER|state=COMMITTED}|
|||FINISHED|count|类型为BROKER，状态为FINISHED 的load job 数量|Doris fe load job of BROKER, state is "FINISHED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=BROKER|state=FINISHED}|
|||CANCELLED|count|类型为BROKER，状态为CANCELLED 的load job 数量|Doris fe load job of BROKER, state is "CANCELLED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=BROKER|state=CANCELLED}|
|DORIS.FE.MINI.LOAD.JOB|MINI LOAD JOB|UNKNOWN|count|类型为MINI，状态为UNKNOWN 的load job 数量|Doris fe load job of MINI, state is "UNKNOWN"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=MINI|state=UNKNOWN}|
|||PENDING|count|类型为MINI，状态为PENDING 的load job 数量|Doris fe load job of MINI, state is "PENDING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=MINI|state=PENDING}|
|||ETL|count|类型为MINI，状态为ETL 的load job 数量|Doris fe load job of MINI, state is "ETL"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=MINI|state=ETL}|
|||LOADING|count|类型为MINI，状态为LOADING 的load job 数量|Doris fe load job of MINI, state is "LOADING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=MINI|state=LOADING}|
|||COMMITTED|count|类型为MINI，状态为COMMITTED 的load job 数量|Doris fe load job of MINI, state is "COMMITTED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=MINI|state=COMMITTED}|
|||FINISHED|count|类型为MINI，状态为FINISHED 的load job 数量|Doris fe load job of MINI, state is "FINISHED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=MINI|state=FINISHED}|
|||CANCELLED|count|类型为MINI，状态为CANCELLED 的load job 数量|Doris fe load job of MINI, state is "CANCELLED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=MINI|state=CANCELLED}|
|DORIS.FE.HADOOP.LOAD.JOB|HADOOP LOAD JOB|UNKNOWN|count|类型为HADOOP，状态为UNKNOWN 的load job 数量|Doris fe load job of HADOOP, state is "UNKNOWN"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=HADOOP|state=UNKNOWN}|
|||PENDING|count|类型为HADOOP，状态为PENDING 的load job 数量|Doris fe load job of HADOOP, state is "PENDING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=HADOOP|state=PENDING}|
|||ETL|count|类型为HADOOP，状态为ETL 的load job 数量|Doris fe load job of HADOOP, state is "ETL"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=HADOOP|state=ETL}|
|||LOADING|count|类型为HADOOP，状态为LOADING 的load job 数量|Doris fe load job of HADOOP, state is "LOADING"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=HADOOP|state=LOADING}|
|||COMMITTED|count|类型为HADOOP，状态为COMMITTED 的load job 数量|Doris fe load job of HADOOP, state is "COMMITTED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=HADOOP|state=COMMITTED}|
|||FINISHED|count|类型为HADOOP，状态为FINISHED 的load job 数量|Doris fe load job of HADOOP, state is "FINISHED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=HADOOP|state=FINISHED}|
|||CANCELLED|count|类型为HADOOP，状态为CANCELLED 的load job 数量|Doris fe load job of HADOOP, state is "CANCELLED"|数据来源Doris的metrics接口,doris_fe_job{job=load|type=HADOOP|state=CANCELLED}|

## 查看监控项

FE 的监控项可以通过以下方式访问：`http://fe_host:fe_http_port/metrics`；默认显示为 [Prometheus](https://prometheus.io/) 格式。

通过以下接口可以获取 Json 格式的监控项：`http://fe_host:fe_http_port/metrics?type=json`。

## 监控项列表
### `doris_fe_snmp{name="tcp_in_errs"}`
该监控项为 `/proc/net/snmp` 中的 `Tcp: InErrs` 字段值。表示当前接收到的错误的 TCP 包的数量。
结合采样周期可以计算发生率。通常用于排查网络问题。

### `doris_fe_snmp{name="tcp_retrans_segs"}`
该监控项为 `/proc/net/snmp` 中的 `Tcp: RetransSegs` 字段值。表示当前重传的 TCP 包的数量。
结合采样周期可以计算发生率。通常用于排查网络问题。

### `doris_fe_snmp{name="tcp_in_segs"}`
该监控项为 `/proc/net/snmp` 中的 `Tcp: InSegs` 字段值。表示当前接收到的所有 TCP 包的数量。
通过 `(NEW_tcp_in_errs - OLD_tcp_in_errs) / (NEW_tcp_in_segs - OLD_tcp_in_segs)` 可以计算接收到的 TCP 错误包率。通常用于排查网络问题。

### `doris_fe_snmp{name="tcp_out_segs"}`
该监控项为 `/proc/net/snmp` 中的 `Tcp: OutSegs` 字段值。表示当前发送的所有带 [RST](https://baike.baidu.com/item/rst/3222752) 标记的 TCP 包的数量。
通过 `(NEW_tcp_tcp_retrans_segs - OLD_tcp_retrans_segs) / (NEW_tcp_out_segs - OLD_tcp_out_segs)` 可以计算 TCP 重传率。通常用于排查网络问题。

### `doris_fe_meminfo{name="memory_total"}`
该监控项为 `/proc/meminfo` 中的 `MemTotal` 字段值。表示所有可用的内存大小，总的物理内存减去预留空间和内核大小。通常用于排查内存问题。

### `doris_fe_meminfo{name="memory_free"}`
该监控项为 `/proc/meminfo` 中的 `MemFree` 字段值。表示系统尚未使用的内存。通常用于排查内存问题。

### `doris_fe_meminfo{name="memory_available"}`
该监控项为 `/proc/meminfo` 中的 `MemAvailable` 字段值。真正的系统可用内存，系统中有些内存虽然已被使用但是可以回收的，所以这部分可回收的内存加上MemFree才是系统可用的内存。通常用于排查内存问题。

### `doris_fe_meminfo{name="buffers"}`
该监控项为 `/proc/meminfo` 中的 `Buffers` 字段值。表示用来给块设备做缓存的内存(文件系统的metadata、pages)。通常用于排查内存问题。

### `doris_fe_meminfo{name="cached"}`
该监控项为 `/proc/meminfo` 中的 `Cached` 字段值。表示分配给文件缓冲区的内存。通常用于排查内存问题。

### `jvm_thread{type="count"}`
该监控项表示 FE 节点当前 JVM 总的线程数量，包含 daemon 线程和非 daemon 线程。通常用于排查 FE 节点的 JVM 线程运行问题。

### `jvm_thread{type="peak_count"}`
该监控项表示 FE 节点从 JVM 启动以来的最大峰值线程数量。
通常用于排查 FE 节点的 JVM 线程运行问题。

### `jvm_thread{type="new_count"}`
该监控项表示 FE 节点 JVM 中处于 NEW 状态的线程数量。
通常用于排查 FE 节点的 JVM 线程运行问题。

### `jvm_thread{type="runnable_count"}`
该监控项表示 FE 节点 JVM 中处于 RUNNABLE 状态的线程数量。
通常用于排查 FE 节点的 JVM 线程运行问题。

### `jvm_thread{type="blocked_count"}`
该监控项表示 FE 节点 JVM 中处于 BLOCKED 状态的线程数量。
通常用于排查 FE 节点的 JVM 线程运行问题。

### `jvm_thread{type="waiting_count"}`
该监控项表示 FE 节点 JVM 中处于 WAITING 状态的线程数量。
通常用于排查 FE 节点的 JVM 线程运行问题。

### `jvm_thread{type="timed_waiting_count"}`
该监控项表示 FE 节点 JVM 中处于 TIMED_WAITING 状态的线程数量。
通常用于排查 FE 节点的 JVM 线程运行问题。

### `jvm_thread{type="terminated_count"}`
该监控项表示 FE 节点 JVM 中处于 TERMINATED 状态的线程数量。
通常用于排查 FE 节点的 JVM 线程运行问题。
