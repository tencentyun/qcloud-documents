文档主要介绍 FE 的相关监控项。
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
