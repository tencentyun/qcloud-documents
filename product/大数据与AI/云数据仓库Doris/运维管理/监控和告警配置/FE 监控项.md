文档主要介绍 FE 的相关监控项。
## 监控指标列表
<table>
<thead>
<tr>
<th>指标名称</th>
<th>前台标题</th>
<th>指标Tag名称</th>
<th>单位</th>
<th>指标含义</th>
<th>英文指标含义</th>
<th>统计方法</th>
</tr>
</thead>
<tbody><tr>
<td>DORIS.FE.MASTER</td>
<td>主节点</td>
<td>IsMaster</td>
<td>-</td>
<td>是否为 fe master 节点</td>
<td>Is or not master node of fe</td>
<td>数据来源 Doris 的 metrics 接口，node_info{type=is_master}</td>
</tr>
<tr>
<td>DORIS.FE.CONNECTION.TOTAL</td>
<td>connection 数量</td>
<td>Num</td>
<td>count</td>
<td>FE 节点 JVM connection 数量</td>
<td>The total number of doris fe connection</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_connection_total</td>
</tr>
<tr>
<td rowspan=8>DORIS.FE.JVM.THREAD.COUNT</td>
<td rowspan=8>JVM THREAD</td>
<td>Total</td>
<td>count</td>
<td>FE 节点 JVM 中线程总数，包含 daemon 线程和非 daemon 线程</td>
<td>Doris fe jvm thread total count</td>
<td>数据来源 Doris 的 metrics 接口，jvm_thread{type=count}</td>
</tr>
<tr>
<td>Peak</td>
<td>count</td>
<td>FE 节点 JVM 线程峰值</td>
<td>Doris fe jvm thread peak count</td>
<td>数据来源 Doris 的 metrics 接口，jvm_thread{type=peak_count}</td>
</tr>
<tr>
<td>New</td>
<td>count</td>
<td>FE 节点 JVM 中处于 NEW 状态的线程数量</td>
<td>Doris fe jvm thread new count</td>
<td>数据来源 Doris 的 metrics 接口，jvm_thread{type=new_count}</td>
</tr>
<tr>
<td>Runnable</td>
<td>count</td>
<td>FE 节点 JVM 中处于 runnable 状态的线程数量</td>
<td>Doris fe jvm thread runnable count</td>
<td>数据来源 Doris 的 metrics 接口，jvm_thread{type=runnable_count}</td>
</tr>
<tr>
<td>Blocked</td>
<td>count</td>
<td>FE 节点 JVM 中处于 BLOCKED 状态的线程数量</td>
<td>Doris fe jvm thread blocked count</td>
<td>数据来源 Doris 的 metrics 接口，jvm_thread{type=blocked_count}</td>
</tr>
<tr>
<td>Waiting</td>
<td>count</td>
<td>FE 节点 JVM 中处于 TIMED_WAITING 状态的线程数量</td>
<td>Doris fe jvm thread waiting count</td>
<td>数据来源 Doris 的 metrics 接口，jvm_thread{type=waiting_count}</td>
</tr>
<tr>
<td>TimedWaiting</td>
<td>count</td>
<td>FE 节点 JVM 中处于 TERMINATED 状态的线程数量</td>
<td>Doris fe jvm thread timed waiting count</td>
<td>数据来源 Doris 的 metrics 接口，jvm_thread{type=timed_waiting_count}</td>
</tr>
<tr>
<td>Terminated</td>
<td>count</td>
<td>FE 节点 JVM 中处于 TERMINATED 状态的线程数量</td>
<td>Doris fe jvm thread terminated count</td>
<td>数据来源 Doris 的 metrics 接口，jvm_thread{type=terminated_count}</td>
</tr>
<tr>
<td rowspan=2>DORIS.FE.GC.COUNT</td>
<td rowspan=2>GC COUNT</td>
<td>YoungGC</td>
<td>count</td>
<td>FE 节点 JVM Young GC 次数</td>
<td>Doris fe jvm young gc count</td>
<td>数据来源 Doris 的 metrics 接口，jvm_young_gc{type=count}</td>
</tr>
<tr>
<td>OldGC</td>
<td>count</td>
<td>FE 节点 JVM Old GC 次数</td>
<td>Doris fe jvm old gc count</td>
<td>数据来源 Doris 的 metrics 接口，jvm_old_gc{type=count}</td>
</tr>
<tr>
<td rowspan=2>DORIS.FE.GC.TIME</td>
<td rowspan=2>GC TIME</td>
<td>YoungGC</td>
<td>s</td>
<td>FE 节点 JVM Young GC 时间</td>
<td>Doris fe jvm young gc time</td>
<td>数据来源 Doris 的 metrics 接口，jvm_young_gc{type=time}</td>
</tr>
<tr>
<td>OldGC</td>
<td>s</td>
<td>FE 节点 JVM Old GC 时间</td>
<td>Doris fe jvm old gc time</td>
<td>数据来源 Doris 的 metrics 接口，jvm_old_gc{type=time}</td>
</tr>
<tr>
<td  rowspan=4>DORIS.FE.QUERY.LATENCY</td>
<td rowspan=4>QUERY LATENCY</td>
<td>Quantile75</td>
<td>ms</td>
<td>FE 查询延时的75分位数</td>
<td>Doris fe query latency time that quantile is 0.75</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_query_latency_ms{quantile=0.75}</td>
</tr>
<tr>
<td>Quantile95</td>
<td>ms</td>
<td>FE 查询延时的95分位数</td>
<td>Doris fe query latency time that quantile is 0.95</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_query_latency_ms{quantile=0.95}</td>
</tr>
<tr>
<td>Quantile99</td>
<td>ms</td>
<td>FE 查询延时的99分位数</td>
<td>Doris fe query latency time that quantile is 0.99</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_query_latency_ms{quantile=0.99}</td>
</tr>
<tr>
<td>Quantile99.9</td>
<td>ms</td>
<td>FE 查询延时的99.9分位数</td>
<td>Doris fe query latency time that quantile is 0.999</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_query_latency_ms{quantile=0.999}</td>
</tr>
<tr>
<td >DORIS.FE.TABLET.COMPACTION</td>
<td>TABLET COMPACTION SCOR</td>
<td>max</td>
<td>score</td>
<td>FE tablet 进行 compaction 时 compaction score 最大值</td>
<td>Doris fe tablet compaction max scor</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_max_tablet_compaction_scor</td>
</tr>
<tr>
<td>DORIS.FE.TABLET.NUM</td>
<td>SCHEDULED TABLET 数量</td>
<td>ScheduledTablet</td>
<td>count</td>
<td>FE 中 scheduled tablet 数量</td>
<td>Doris fe scheduled tablet num</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_scheduled_tablet_num</td>
</tr>
<tr>
<td rowspan=2>DORIS.FE.EFFICIENCY</td>
<td rowspan=2>请求&amp;响应</td>
<td>QPS</td>
<td>count</td>
<td>每秒查询率</td>
<td>Doris fe qps</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_qps</td>
</tr>
<tr>
<td>RPS</td>
<td>count</td>
<td>每秒能处理的请求数目</td>
<td>Doris fe rps</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_rps</td>
</tr>
<tr>
<td >DORIS.FE.QUERY.ERRRATE</td>
<td>QUERY ERR RATE</td>
<td>ErrRate</td>
<td>%</td>
<td>查询错误率</td>
<td>Doris fe err rate of query</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_query_err_rate</td>
</tr>
<tr>
<td rowspan=6>DORIS.FE.CACHE</td>
<td rowspan=6>缓存查询</td>
<td>SqlModelHitQuery</td>
<td>count</td>
<td>模式为 sql 的 Query 命中 Cache 的数量</td>
<td>Doris fe total hits query by sql model</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_cache_hit_sql</td>
</tr>
<tr>
<td>PartitionModelHitQuery</td>
<td>count</td>
<td>通过 Partition 命中的 Query 数量</td>
<td>Doris fe total hits query by partition model</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_cache_hit_partition</td>
</tr>
<tr>
<td>SqlModelQuery</td>
<td>count</td>
<td>识别缓存模式为 sql 的 Query 数量</td>
<td>The total count of query of sql mode</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_cache_mode_sql</td>
</tr>
<tr>
<td>PartitionModelQuery</td>
<td>count</td>
<td>识别缓存模式为 Partition 的 Query 数量</td>
<td>The total count of query of partition mode</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_query_mode_partition</td>
</tr>
<tr>
<td>CachePartitionHit</td>
<td>count</td>
<td>查询中通过 cache 命中的分区数量</td>
<td>The counter of hit partition of cache partition model</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_partition_hit</td>
</tr>
<tr>
<td>CachePartitionScan</td>
<td>count</td>
<td>查询中扫描的所有分区数量</td>
<td>The counter of scan partition of cache partition model</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_partition_all</td>
</tr>
<tr>
<td rowspan=2>DORIS.FE.ROUTINE.LOAD</td>
<td rowspan=2>ROUTINE LOAD</td>
<td>TotalRows</td>
<td>count</td>
<td>FE routine load 的行数</td>
<td>The rows of routine load</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_routine_load_rows</td>
</tr>
<tr>
<td>ErrorRows</td>
<td>count</td>
<td>FE routine load 错误的行数</td>
<td>The total error rows of routine load</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_routine_load_error_rows</td>
</tr>
<tr>
<td rowspan=4>DORIS.FE.TXN.COUNT</td>
<td rowspan=4>TRANSACTION STATUS</td>
<td>Reject</td>
<td>count</td>
<td>FE 被拒绝的 transaction 数量</td>
<td>The counter of rejected transactions</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_txn_reject</td>
</tr>
<tr>
<td>Begin</td>
<td>count</td>
<td>FE 开始的 transaction 数量</td>
<td>The counter of beginning transactions</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_txn_begin</td>
</tr>
<tr>
<td>Success</td>
<td>count</td>
<td>FE 成功的 transaction 数量</td>
<td>The counter of success transactions</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_txn_success</td>
</tr>
<tr>
<td>Failed</td>
<td>count</td>
<td>FE 失败的 transaction 数量</td>
<td>The counter of failed transactions</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_txn_failed</td>
</tr>
<tr>
<td rowspan=2>DORIS.FE.IMAGE</td>
<td rowspan=2>IMAGE</td>
<td>Write</td>
<td>count</td>
<td>FE image write 的数量</td>
<td>the counter of image generated</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_image_write</td>
</tr>
<tr>
<td>Push</td>
<td>count</td>
<td>FE image push 的数量</td>
<td>Doris fe the counter of image succeeded in pushing to other frontends</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_image_push</td>
</tr>
<tr>
<td rowspan=2>DORIS.FE.ALTER.JOB</td>
<td rowspan=2>ALTER JOB</td>
<td>RollupRunning</td>
<td>count</td>
<td>运行中的 alter job，类型为 ROLLUP 的数量</td>
<td>Doris fe alter job of ROLLUP, state is running</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=alter}</td>
</tr>
<tr>
<td>SchemaChangeRunning</td>
<td>count</td>
<td>运行中的 alter job，类型为 SCHEMA_CHANGE 的数量</td>
<td>Doris fe alter job of SCHEMA_CHANGE, state is "running"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=alter}</td>
</tr>
<tr>
<td rowspan=7>DORIS.FE.UNKNOWN.LOAD.JOB</td>
<td rowspan=7>UNKNOWN LOAD JOB</td>
<td>UNKNOWN</td>
<td>count</td>
<td>类型为 UNKNOWN，状态为 UNKNOWN 的 load job 数量</td>
<td>Doris fe load job of UNKNOWN， state is "UNKNOWN"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>PENDING</td>
<td>count</td>
<td>类型为 UNKNOWN，状态为 PENDING 的 load job 数量</td>
<td>Doris fe load job of UNKNOWN, state is "PENDING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>ETL</td>
<td>count</td>
<td>类型为 UNKNOWN，状态为 ETL 的 load job 数量</td>
<td>Doris fe load job of UNKNOWN, state is "ETL"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>LOADING</td>
<td>count</td>
<td>类型为 UNKNOWN，状态为 LOADING 的 load job 数量</td>
<td>Doris fe load job of UNKNOWN, state is "LOADING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>COMMITTED</td>
<td>count</td>
<td>类型为 UNKNOWN，状态为 COMMITTED 的 load job 数量</td>
<td>Doris fe load job of UNKNOWN, state is "COMMITTED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>FINISHED</td>
<td>count</td>
<td>类型为 UNKNOWN，状态为 FINISHED 的 load job 数量</td>
<td>Doris fe load job of UNKNOWN, state is "FINISHED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>CANCELLED</td>
<td>count</td>
<td>类型为 UNKNOWN，状态为 CANCELLED 的 load job 数量</td>
<td>Doris fe load job of UNKNOWN, state is "CANCELLED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td rowspan=7>DORIS.FE.SPARK.LOAD.JOB</td>
<td rowspan=7>SPARK LOAD JOB</td>
<td>UNKNOWN</td>
<td>count</td>
<td>类型为 SPARK，状态为 UNKNOWN 的 load job 数量</td>
<td>Doris fe load job of SPARK, state is "UNKNOWN"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>PENDING</td>
<td>count</td>
<td>类型为 SPARK，状态为 PENDING 的 load job 数量</td>
<td>Doris fe load job of SPARK, state is "PENDING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>ETL</td>
<td>count</td>
<td>类型为 SPARK，状态为 ETL 的 load job 数量</td>
<td>Doris fe load job of SPARK, state is "ETL"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>LOADING</td>
<td>count</td>
<td>类型为 SPARK，状态为 LOADING 的 load job 数量</td>
<td>Doris fe load job of SPARK, state is "LOADING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>COMMITTED</td>
<td>count</td>
<td>类型为 SPARK，状态为 COMMITTED 的 load job 数量</td>
<td>Doris fe load job of SPARK, state is "COMMITTED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>FINISHED</td>
<td>count</td>
<td>类型为 SPARK，状态为 FINISHED 的 load job 数量</td>
<td>Doris fe load job of SPARK, state is "FINISHED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>CANCELLED</td>
<td>count</td>
<td>类型为 SPARK，状态为 CANCELLED 的 load job 数量</td>
<td>Doris fe load job of SPARK, state is "CANCELLED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td rowspan=7>DORIS.FE.DELETE.LOAD.JOB</td>
<td rowspan=7>DELETE LOAD JOB</td>
<td>UNKNOWN</td>
<td>count</td>
<td>类型为 DELETE，状态为 UNKNOWN 的 load job 数量</td>
<td>Doris fe load job of DELETE, state is "UNKNOWN"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>PENDING</td>
<td>count</td>
<td>类型为 DELETE，状态为 PENDING 的 load job 数量</td>
<td>Doris fe load job of DELETE, state is "PENDING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>ETL</td>
<td>count</td>
<td>类型为 DELETE，状态为 ETL 的 load job 数量</td>
<td>Doris fe load job of DELETE, state is "ETL"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>LOADING</td>
<td>count</td>
<td>类型为 DELETE，状态为 LOADING 的 load job 数量</td>
<td>Doris fe load job of DELETE, state is "LOADING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>COMMITTED</td>
<td>count</td>
<td>类型为 DELETE，状态为 COMMITTED 的 load job 数量</td>
<td>Doris fe load job of DELETE, state is "COMMITTED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>FINISHED</td>
<td>count</td>
<td>类型为 DELETE，状态为 FINISHED 的 load job 数量</td>
<td>Doris fe load job of DELETE, state is "FINISHED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>CANCELLED</td>
<td>count</td>
<td>类型为 DELETE，状态为 CANCELLED 的 load job 数量</td>
<td>Doris fe load job of DELETE, state is "CANCELLED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td rowspan=7>DORIS.FE.INSERT.LOAD.JOB</td>
<td rowspan=7>INSERT LOAD JOB</td>
<td>UNKNOWN</td>
<td>count</td>
<td>类型为 INSERT，状态为 UNKNOWN 的 load job 数量</td>
<td>Doris fe load job of INSERT, state is "UNKNOWN"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>PENDING</td>
<td>count</td>
<td>类型为 INSERT，状态为 PENDING 的 load job 数量</td>
<td>Doris fe load job of INSERT, state is "PENDING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>ETL</td>
<td>count</td>
<td>类型为 INSERT，状态为 ETL 的 load job 数量</td>
<td>Doris fe load job of INSERT, state is "ETL"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>LOADING</td>
<td>count</td>
<td>类型为 INSERT，状态为 LOADING 的 load job 数量</td>
<td>Doris fe load job of INSERT, state is "LOADING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>COMMITTED</td>
<td>count</td>
<td>类型为 INSERT，状态为 COMMITTED 的 load job 数量</td>
<td>Doris fe load job of INSERT, state is "COMMITTED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>FINISHED</td>
<td>count</td>
<td>类型为 INSERT，状态为 FINISHED 的 load job 数量</td>
<td>Doris fe load job of INSERT, state is "FINISHED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>CANCELLED</td>
<td>count</td>
<td>类型为 INSERT，状态为 CANCELLED 的 load job 数量</td>
<td>Doris fe load job of INSERT, state is "CANCELLED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td rowspan=7>DORIS.FE.BROKER.LOAD.JOB</td>
<td rowspan=7>BROKER LOAD JOB</td>
<td>UNKNOWN</td>
<td>count</td>
<td>类型为 BROKER，状态为 UNKNOWN 的 load job 数量</td>
<td>Doris fe load job of BROKER, state is "UNKNOWN"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>PENDING</td>
<td>count</td>
<td>类型为 BROKER，状态为 PENDING 的 load job 数量</td>
<td>Doris fe load job of BROKER, state is "PENDING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>ETL</td>
<td>count</td>
<td>类型为 BROKER，状态为 ETL 的 load job 数量</td>
<td>Doris fe load job of BROKER, state is "ETL"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>LOADING</td>
<td>count</td>
<td>类型为 BROKER，状态为 LOADING 的 load job 数量</td>
<td>Doris fe load job of BROKER, state is "LOADING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>COMMITTED</td>
<td>count</td>
<td>类型为 BROKER，状态为 COMMITTED 的 load job 数量</td>
<td>Doris fe load job of BROKER, state is "COMMITTED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>FINISHED</td>
<td>count</td>
<td>类型为 BROKER，状态为 FINISHED 的 load job 数量</td>
<td>Doris fe load job of BROKER, state is "FINISHED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>CANCELLED</td>
<td>count</td>
<td>类型为 BROKER，状态为 CANCELLED 的 load job 数量</td>
<td>Doris fe load job of BROKER, state is "CANCELLED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td rowspan=7>DORIS.FE.MINI.LOAD.JOB</td>
<td rowspan=7MINI LOAD JOB</td>
<td>UNKNOWN</td>
<td>count</td>
<td>类型为 MINI，状态为 UNKNOWN 的 load job 数量</td>
<td>Doris fe load job of MINI, state is "UNKNOWN"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>PENDING</td>
<td>count</td>
<td>类型为 MINI，状态为 PENDING 的 load job 数量</td>
<td>Doris fe load job of MINI, state is "PENDING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>ETL</td>
<td>count</td>
<td>类型为 MINI，状态为 ETL 的 load job 数量</td>
<td>Doris fe load job of MINI, state is "ETL"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>LOADING</td>
<td>count</td>
<td>类型为 MINI，状态为 LOADING 的 load job 数量</td>
<td>Doris fe load job of MINI, state is "LOADING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>COMMITTED</td>
<td>count</td>
<td>类型为 MINI，状态为 COMMITTED 的 load job 数量</td>
<td>Doris fe load job of MINI, state is "COMMITTED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>FINISHED</td>
<td>count</td>
<td>类型为 MINI，状态为 FINISHED 的 load job 数量</td>
<td>Doris fe load job of MINI, state is "FINISHED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>CANCELLED</td>
<td>count</td>
<td>类型为 MINI，状态为 CANCELLED 的 load job 数量</td>
<td>Doris fe load job of MINI, state is "CANCELLED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td rowspan=7>DORIS.FE.HADOOP.LOAD.JOB</td>
<td rowspan=7>HADOOP LOAD JOB</td>
<td>UNKNOWN</td>
<td>count</td>
<td>类型为 HADOOP，状态为 UNKNOWN 的 load job 数量</td>
<td>Doris fe load job of HADOOP, state is "UNKNOWN"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>PENDING</td>
<td>count</td>
<td>类型为 HADOOP，状态为 PENDING 的 load job 数量</td>
<td>Doris fe load job of HADOOP, state is "PENDING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>ETL</td>
<td>count</td>
<td>类型为 HADOOP，状态为 ETL 的 load job 数量</td>
<td>Doris fe load job of HADOOP, state is "ETL"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>LOADING</td>
<td>count</td>
<td>类型为 HADOOP，状态为 LOADING 的 load job 数量</td>
<td>Doris fe load job of HADOOP, state is "LOADING"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>COMMITTED</td>
<td>count</td>
<td>类型为 HADOOP，状态为 COMMITTED 的 load job 数量</td>
<td>Doris fe load job of HADOOP, state is "COMMITTED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>FINISHED</td>
<td>count</td>
<td>类型为 HADOOP，状态为 FINISHED 的 load job 数量</td>
<td>Doris fe load job of HADOOP, state is "FINISHED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
<tr>
<td>CANCELLED</td>
<td>count</td>
<td>类型为 HADOOP，状态为 CANCELLED 的 load job 数量</td>
<td>Doris fe load job of HADOOP, state is "CANCELLED"</td>
<td>数据来源 Doris 的 metrics 接口，doris_fe_job{job=load}</td>
</tr>
</tbody></table>

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
