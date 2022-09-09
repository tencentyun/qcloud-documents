本文主要介绍 BE 的相关监控项。

## 监控指标列表

|指标名称|前台标题|指标Tag名称|单位|指标含义|英文指标含义|统计方法|
|-------|-------|-------|-------|-------|-------|-------|
|DORIS.BE.THRIFT.USED.CLIENTS|THRIFT USED|Broker|count|Broker使用thrift的数量|The count of thrift used of broker|数据来源Doris的metrics接口,doris_be_thrift_used_clients{name=broker}|
|||Backend|count|BE 使用thrift的数量|The count of thrift used of be|数据来源Doris的metrics接口,doris_be_thrift_used_clients{name=backend}|
|||Extdatasource|count|extdatasource 使用thrift的数量|The count of thrift used of extdatasource|数据来源Doris的metrics接口,doris_be_thrift_used_clients{name=extdatasource}|
|||Frontend|count|FE 使用thrift的数量|The count of thrift used of fe|数据来源Doris的metrics接口,doris_be_thrift_used_clients{name=frontend}|
|DORIS.BE.STREAMING.LOAD.COUNT|STREAMING LOAD|RequestsTotal|count|streaming load请求数量|The count of streaming load requests|数据来源Doris的metrics接口,doris_be_streaming_load_requests_total|
|||CurrentProcessing|count|streaming load 现有进程数|The count of streaming load current processing|数据来源Doris的metrics接口,doris_be_streaming_load_current_processing|
|||PipeCount|count|streaming load Pipe数量|The count of stream load pipe|数据来源Doris的metrics接口,doris_be_stream_load_pipe_count|
|DORIS.BE.STREAMING.LOADTIME|STREAMING LOADTIME|Duration|ms|streaming load 持续时间|The time of streaming load duration|数据来源Doris的metrics接口,doris_be_streaming_load_duration_ms|
|DORIS.BE.STREAMING.LOAD|STREAMING LOAD BYTES|LoadTotal|bytes|stream load导入的数据大小|The total bytes of streaming load|数据来源Doris的metrics接口,doris_be_streaming_load_bytes|
|DORIS.BE.USAGE|USAGE|LastestSuccessChannelCache|%|LastestSuccessChannelCache 使用率|Doris be usage of LastestSuccessChannelCache|数据来源Doris的metrics接口,doris_be_usage{name=LastestSuccessChannelCache}|
|||SegmentIndexCache|%|SegmentIndexCache 使用率|Doris be usage of SegmentIndexCache|数据来源Doris的metrics接口,doris_be_usage{name=SegmentIndexCache}|
|||FileHandlerCache|%|FileHandlerCache 使用率|Doris be usage of FileHandlerCache|数据来源Doris的metrics接口,doris_be_usage{name=FileHandlerCache}|
|||DataPageCache|%|DataPageCache 使用率|Doris be usage DataPageCache|数据来源Doris的metrics接口,doris_be_usage{name=DataPageCache}|
|||IndexPageCache|%|IndexPageCache 使用率|Doris be usage IndexPageCache|数据来源Doris的metrics接口,doris_be_usage{name=IndexPageCache}|
|DORIS.BE.CPU|CPU|GuestNice|%|低优先级运行虚拟机的时间占比|Time spent in user mode with low priority|数据来源/proc/stat,在一个采样周期内，guest_nice cpu时间/total cpu时间 * 100%；|
|||Guest|%|运行虚拟处理器所用的时间百分比|Percentage of time spent running virtual processors|数据来源/proc/stat,在一个采样周期内，guest cpu时间/total cpu时间 * 100%；|
|||Steal|%|虚拟 CPU 等待实际 CPU 时间占比|The stolen time, which is the time spent in other operating systems when running in a virtualized environment|数据来源/proc/stat,在一个采样周期内，steal cpu时间/total cpu时间 * 100%；|
|||SoftIrq|%|CPU 软中断占比|CPU Soft Interruption Percentage|数据来源/proc/stat,在一个采样周期内，softirq cpu时间/total cpu时间 * 100%；|
|||Irq|%|中断占比|Interruption percentage|数据来源/proc/stat,在一个采样周期内，irq cpu时间/total cpu时间 * 100%；|
|||Iowait|%|进程等待 IO CPU 空闲占比|The percentage of time that the CPUs were idle during which the system had an outstanding disk I/O request.|数据来源/proc/stat,在一个采样周期内，iowait cpu时间/total cpu时间 * 100%；|
|||Idle|%|CPU IDLE 时间占比|The percentage of CPU idle time|数据来源/proc/stat,在一个采样周期内，idle cpu时间/total cpu时间 * 100%；|
|||System|%|内核态 CPU 占用比|Kernel mode CPU Usage Percentage|数据来源/proc/stat,在一个采样周期内，system cpu时间/total cpu时间 * 100%；|
|||Nice|%|NICE 优先级使用 CPU 占比|Percentage of NICE priority CPU usage|数据来源/proc/stat,在一个采样周期内，nice cpu时间/total cpu时间 * 100%；|
|||User|%|用户态 CPU 占用比|Percentage of user mode CPU usage|数据来源/proc/stat,在一个采样周期内，user cpu时间/total cpu时间 * 100%；|
|DORIS.BE.CAPACITY|CAPACITY|LastestSuccessChannelCache|bytes|LastestSuccessChannelCache 占用空间|The capacity of LastestSuccessChannelCache|数据来源Doris的metrics接口,doris_be_capacity{name=LastestSuccessChannelCache}|
|||SegmentIndexCache|bytes|SegmentIndexCache 占用空间|The capacity of SegmentIndexCache|数据来源Doris的metrics接口,doris_be_capacity{name=SegmentIndexCache}|
|||FileHandlerCache|bytes|FileHandlerCache 占用空间|The capacity of FileHandlerCache|数据来源Doris的metrics接口,doris_be_capacity{name=FileHandlerCache}|
|||DataPageCache|bytes|DataPageCache 占用空间|The capacity of DataPageCache|数据来源Doris的metrics接口,doris_be_capacity{name=DataPageCache}|
|||IndexPageCache|bytes|IndexPageCache 占用空间|The capacity of IndexPageCache|数据来源Doris的metrics接口,doris_be_capacity{name=IndexPageCache}|
|DORIS.BE.FRAGMENT.COUNT|FRAGMENT COUNT|PlanFragmen|count|plan fragmen 数量|The count of plan fragment|数据来源Doris的metrics接口,doris_be_plan_fragment_count|
|||Endpoint|count|DataStream的数量|The count of fragment endpoint|数据来源Doris的metrics接口,doris_be_fragment_endpoint_count|
|||TimeoutCanceled|count|超时取消的fragment的数量|The count of canceled fragment for timeout|数据来源Doris的metrics接口,doris_be_timeout_canceled_fragment_count|
|||RequestsTotal|count|fragment的请求次数|The count of fragment requests|数据来源Doris的metrics接口,doris_be_fragment_requests_total|
|DORIS.BE.FRAGMENT.REQUEST.TIME|FRAGMENT 请求时间|Duration|μs(微秒)|fragment的请求时间|The time of fragment request duration|数据来源Doris的metrics接口,doris_be_fragment_request_duration_us|
|DORIS.BE.MEMORY|MEMORY|Total|bytes|BE memory pool大小|The total bytes memory pool|数据来源Doris的metrics接口,doris_be_memory_pool_bytes_total|
|||Allocated|bytes|BE memory allocated 大小|The total bytes of memory allocated|数据来源Doris的metrics接口,doris_be_memory_allocated_bytes|
|||CacheMemoryTotal|bytes|BE query cache memory 大小|The total bytes of query cache memory|数据来源Doris的metrics接口,doris_be_query_cache_memory_total_byte|
|DORIS.BE.COMPACTION.PERMITS|COMPACTION.PERMITS|Used|count|正在使用的compaction permits大小|The permit count of compaction used|数据来源Doris的metrics接口,doris_be_compaction_used_permits|
|||waitting|count|等待 compaction permits的数量|The permit count of compaction waitting|数据来源Doris的metrics接口,doris_be_compaction_waitting_permits|
|DORIS.BE.TABLET.COMPACTION.SCORE|COMPACTION.SCORE|CumulativeMax|score|tablet中最大的base compaction score|The max compaction score of tablet cumulative|数据来源Doris的metrics接口,doris_be_tablet_cumulative_max_compaction_score|
|||BaseMax|score|tablet base 最大compaction 分数|The max compaction score of tablet_base|数据来源Doris的metrics接口,doris_be_tablet_base_max_compaction_score|
|DORIS.BE.COMPACTION.TOTAL|COMPACTION TOTAL|Cumulative|bytes|Cumulative compaction的数据量|The total bytes of cumulative compaction|数据来源Doris的metrics接口,doris_be_compaction_bytes_total{type=cumulative}|
|||Base|bytes|Base compaction的数据量|The total bytes of base compaction|数据来源Doris的metrics接口,doris_be_compaction_bytes_total{type=base}|
|DORIS.BE.COMPACTION.DELTAS|COMPACTION DELTAS|Cumulative|count|Cumulative compaction deltas的数据量|The count of cumulative compaction deltas|数据来源Doris的metrics接口,doris_be_compaction_deltas_total{type=cumulative}|
|||Base|count|Base compaction deltas的数据量|The count of base compaction deltas|数据来源Doris的metrics接口,doris_be_compaction_deltas_total{type=base}|
|DORIS.BE.COMPACTION.MEM|doris_be_compaction_mem_current_consumption|CurrentConsumption|count|Compaction使用的MemPool总和(所有Compaction线程)|The number of compaction mem current consumption|数据来源Doris的metrics接口,doris_be_compaction_mem_current_consumption|
|DORIS.BE.PROCESS.FD.NUM|PROCESS.FD|Used|count|BE 进程使用文件句柄数量|The number of process fd used|数据来源Doris的metrics接口,doris_be_process_fd_num_used|
|||SoftLimit|count|BE 进程文件句柄soft限制数量|The number of process fd soft limited|数据来源Doris的metrics接口,doris_be_process_fd_num_limit_soft|
|||HardLimit|count|BE 进程文件句柄hard限制数量|The number of process fd hard limited|数据来源Doris的metrics接口,doris_be_process_fd_num_limit_hard|
|DORIS.BE.PROCESS.THREAD|PROCESS THREAD NUMBER|num|count|BE进程运行的线程个数|The number of process thread|数据来源Doris的metrics接口,doris_be_process_thread_num|
|DORIS.BE.ENGINE.REQUESTS.NUM|ENGINE.REQUESTS|FailedBaseCompaction|count|类型为base_compaction，engine请求失败数量|The total number of base compaction engine requests failed|数据来源Doris的metrics接口,doris_be_engine_requests_total{status=failed|type=base_compaction}|
|||FailedCumulativeCompaction|count|类型为cumulative_compaction，engine请求失败数量|The total number of cumulative compaction engine requests|数据来源Doris的metrics接口,doris_be_engine_requests_total{status=failed|type=cumulative_compaction}|
|||TotalBaseCompaction|count|类型为base_compaction，engine请求总数|The total number of base compaction engine requests failed|数据来源Doris的metrics接口,doris_be_engine_requests_total{status=total|type=base_compaction}|
|||TotalCumulativeCompaction|count|类型为cumulative_compaction，engine请求总数|The total number of cumulative compaction engine requests|数据来源Doris的metrics接口,doris_be_engine_requests_total{status=total|type=cumulative_compaction}|

## 查看监控项

BE 的监控项可以通过以下方式访问：`http://be_host:be_webserver_port/metrics`；默认显示为 [Prometheus](https://prometheus.io/) 格式。
通过以下接口可以获取 Json 格式的监控项：`http://be_host:be_webserver_port/metrics?type=json`。

## 监控项列表
### `doris_be_snmp{name="tcp_in_errs"}`
该监控项为 `/proc/net/snmp` 中的 `Tcp: InErrs` 字段值。表示当前接收到的错误的 TCP 包的数量。
结合采样周期可以计算发生率。通常用于排查网络问题。

### `doris_be_snmp{name="tcp_retrans_segs"}`
该监控项为 `/proc/net/snmp` 中的 `Tcp: RetransSegs` 字段值。表示当前重传的 TCP 包的数量。
结合采样周期可以计算发生率。通常用于排查网络问题。

### `doris_be_snmp{name="tcp_in_segs"}`
该监控项为 `/proc/net/snmp` 中的 `Tcp: InSegs` 字段值。表示当前接收到的所有 TCP 包的数量。
通过 `(NEW_tcp_in_errs - OLD_tcp_in_errs) / (NEW_tcp_in_segs - OLD_tcp_in_segs)` 可以计算接收到的 TCP 错误包率。通常用于排查网络问题。

### `doris_be_snmp{name="tcp_out_segs"}`
该监控项为 `/proc/net/snmp` 中的 `Tcp: OutSegs` 字段值。表示当前发送的所有带 RST 标记的 TCP 包的数量。
通过 `(NEW_tcp_tcp_retrans_segs - OLD_tcp_retrans_segs) / (NEW_tcp_out_segs - OLD_tcp_out_segs)` 可以计算 TCP 重传率。通常用于排查网络问题。

### `doris_be_compaction_mem_current_consumption`
该监控项为 Compaction 使用的 MemPool 总和（所有 Compaction 线程）。通过该值，可以迅速判断 Compaction 是否占用过多内存，引起高内存占用，甚至 OOM 等问题。
通常用于排查内存使用问题。
