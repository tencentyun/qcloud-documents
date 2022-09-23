本文主要介绍 BE 的相关监控项。
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
<td rowspan=4>DORIS.BE.THRIFT.USED.CLIENTS</td>
<td rowspan=4>THRIFT USED</td>
<td>Broker</td>
<td>count</td>
<td>Broker 使用 thrift 的数量</td>
<td>The count of thrift used of broker</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_thrift_used_clients{name=broker}</td>
</tr>
<tr>
<td>Backend</td>
<td>count</td>
<td>BE 使用 thrift 的数量</td>
<td>The count of thrift used of be</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_thrift_used_clients{name=backend}</td>
</tr>
<tr>
<td>Extdatasource</td>
<td>count</td>
<td>extdatasource 使用 thrift 的数量</td>
<td>The count of thrift used of extdatasource</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_thrift_used_clients{name=extdatasource}</td>
</tr>
<tr>
<td>Frontend</td>
<td>count</td>
<td>FE 使用 thrift 的数量</td>
<td>The count of thrift used of fe</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_thrift_used_clients{name=frontend}</td>
</tr>
<tr>
<td rowspan=3>DORIS.BE.STREAMING.LOAD.COUNT</td>
<td rowspan=3>STREAMING LOAD</td>
<td>RequestsTotal</td>
<td>count</td>
<td>streaming load 请求数量</td>
<td>The count of streaming load requests</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_streaming_load_requests_total</td>
</tr>
<tr>
<td>CurrentProcessing</td>
<td>count</td>
<td>streaming load 现有进程数</td>
<td>The count of streaming load current processing</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_streaming_load_current_processing</td>
</tr>
<tr>
<td>PipeCount</td>
<td>count</td>
<td>streaming load Pipe 数量</td>
<td>The count of stream load pipe</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_stream_load_pipe_count</td>
</tr>
<tr>
<td >DORIS.BE.STREAMING.LOADTIME</td>
<td>STREAMING LOADTIME</td>
<td>Duration</td>
<td>ms</td>
<td>streaming load 持续时间</td>
<td>The time of streaming load duration</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_streaming_load_duration_ms</td>
</tr>
<tr>
<td>DORIS.BE.STREAMING.LOAD</td>
<td>STREAMING LOAD BYTES</td>
<td>LoadTotal</td>
<td>bytes</td>
<td>stream load 导入的数据大小</td>
<td>The total bytes of streaming load</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_streaming_load_bytes</td>
</tr>
<tr>
<td rowspan=4>DORIS.BE.FRAGMENT.COUNT</td>
<td rowspan=4>FRAGMENT COUNT</td>
<td>PlanFragmen</td>
<td>count</td>
<td>plan fragmen 数量</td>
<td>The count of plan fragment</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_plan_fragment_count</td>
</tr>
<tr>
<td>Endpoint</td>
<td>count</td>
<td>DataStream 的数量</td>
<td>The count of fragment endpoint</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_fragment_endpoint_count</td>
</tr>
<tr>
<td>TimeoutCanceled</td>
<td>count</td>
<td>超时取消的 fragment 的数量</td>
<td>The count of canceled fragment for timeout</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_timeout_canceled_fragment_count</td>
</tr>
<tr>
<td>RequestsTotal</td>
<td>count</td>
<td>fragment 的请求次数</td>
<td>The count of fragment requests</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_fragment_requests_total</td>
</tr>
<tr>
<td >DORIS.BE.FRAGMENT.REQUEST.TIME</td>
<td>FRAGMENT 请求时间</td>
<td>Duration</td>
<td>μs(微秒)</td>
<td>fragment 的请求时间</td>
<td>The time of fragment request duration</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_fragment_request_duration_us</td>
</tr>
<tr>
<td rowspan=3>DORIS.BE.MEMORY</td>
<td>MEMORY</td>
<td>Total</td>
<td>bytes</td>
<td>BE memory pool大小</td>
<td>The total bytes memory pool</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_memory_pool_bytes_total</td>
</tr>
<tr>
<td>Allocated</td>
<td>bytes</td>
<td>BE memory allocated 大小</td>
<td>The total bytes of memory allocated</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_memory_allocated_bytes</td>
</tr>
<tr>
<td>CacheMemoryTotal</td>
<td>bytes</td>
<td>BE query cache memory 大小</td>
<td>The total bytes of query cache memory</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_query_cache_memory_total_byte</td>
</tr>

<tr>
<td rowspan=2>DORIS.BE.TABLET.COMPACTION.SCORE</td>
<td rowspan=2>COMPACTION.SCORE</td>
<td>CumulativeMax</td>
<td>score</td>
<td>tablet 中最大的 base compaction score</td>
<td>The max compaction score of tablet cumulative</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_tablet_cumulative_max_compaction_score</td>
</tr>
<tr>
<td>BaseMax</td>
<td>score</td>
<td>tablet base 最大 compaction 分数</td>
<td>The max compaction score of tablet_base</td>
<td>数据来源 Doris 的 metrics接口，doris_be_tablet_base_max_compaction_score</td>
</tr>
<tr>
<td rowspan=2>DORIS.BE.COMPACTION.TOTAL</td>
<td rowspan=2>COMPACTION TOTAL</td>
<td>Cumulative</td>
<td>bytes</td>
<td>Cumulative compaction 的数据量</td>
<td>The total bytes of cumulative compaction</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_compaction_bytes_total{type=cumulative}</td>
</tr>
<tr>
<td>Base</td>
<td>bytes</td>
<td>Base compaction 的数据量</td>
<td>The total bytes of base compaction</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_compaction_bytes_total{type=base}</td>
</tr>
<tr>
<td rowspan=2>DORIS.BE.COMPACTION.DELTAS</td>
<td rowspan=2>COMPACTION DELTAS</td>
<td>Cumulative</td>
<td>count</td>
<td>Cumulative compaction deltas 的数据量</td>
<td>The count of cumulative compaction deltas</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_compaction_deltas_total{type=cumulative}</td>
</tr>
<tr>
<td>Base</td>
<td>count</td>
<td>Base compaction deltas 的数据量</td>
<td>The count of base compaction deltas</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_compaction_deltas_total{type=base}</td>
</tr>
<tr>
<td >DORIS.BE.COMPACTION.MEM</td>
<td>doris_be_compaction_mem_current_consumption</td>
<td>CurrentConsumption</td>
<td>count</td>
<td>Compaction使用的 MemPool 总和（所有 Compaction 线程）</td>
<td>The number of compaction mem current consumption</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_compaction_mem_current_consumption</td>
</tr>
<tr>
<td rowspan=3>DORIS.BE.PROCESS.FD.NUM</td>
<td rowspan=3>PROCESS.FD</td>
<td>Used</td>
<td>count</td>
<td>BE 进程使用文件句柄数量</td>
<td>The number of process fd used</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_process_fd_num_used</td>
</tr>
<tr>
<td>SoftLimit</td>
<td>count</td>
<td>BE 进程文件句柄 soft 限制数量</td>
<td>The number of process fd soft limited</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_process_fd_num_limit_soft</td>
</tr>
<tr>
<td>HardLimit</td>
<td>count</td>
<td>BE 进程文件句柄 hard 限制数量</td>
<td>The number of process fd hard limited</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_process_fd_num_limit_hard</td>
</tr>
<tr>
<td >DORIS.BE.PROCESS.THREAD</td>
<td>PROCESS THREAD NUMBER</td>
<td>num</td>
<td>count</td>
<td>BE 进程运行的线程个数</td>
<td>The number of process thread</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_process_thread_num</td>
</tr>
<tr>
<td rowspan=4>DORIS.BE.ENGINE.REQUESTS.NUM</td>
<td rowspan=4>ENGINE.REQUESTS</td>
<td>FailedBaseCompaction</td>
<td>count</td>
<td>类型为 base_compaction，engine 请求失败数量</td>
<td>The total number of base compaction engine requests failed</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_engine_requests_total{status=failed}</td>
</tr>
<tr>
<td>FailedCumulativeCompaction</td>
<td>count</td>
<td>类型为 cumulative_compaction，engine 请求失败数量</td>
<td>The total number of cumulative compaction engine requests</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_engine_requests_total{status=failed}</td>
</tr>
<tr>
<td>TotalBaseCompaction</td>
<td>count</td>
<td>类型为 base_compaction，engine 请求总数</td>
<td>The total number of base compaction engine requests failed</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_engine_requests_total{status=total}</td>
</tr>
<tr>
<td>TotalCumulativeCompaction</td>
<td>count</td>
<td>类型为 cumulative_compaction，engine 请求总数</td>
<td>The total number of cumulative compaction engine requests</td>
<td>数据来源 Doris 的 metrics 接口，doris_be_engine_requests_total{status=total}</td>
</tr>
</tbody></table>

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
