本文主要介绍 BE 的相关监控项。

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
