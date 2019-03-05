腾讯云云监控为云服务器实例（CVM）提供以下监控指标：

## 1 不需要安装监控agent，就能获取数据的监控指标

| 指标名称           | 含义    | 单位   | 统计粒度（period） |
| -------------- | ----- | ---- | ------------ |
| lan_outtraffic | 内网出带宽 | Mbps | 60s、300s     |
| lan_intraffic  | 内网入带宽 | Mbps | 60s、300s     |
| lan_outpkg     | 内网出包量 | 个/秒  | 60s、300s     |
| lan_inpkg      | 内网入包量 | 个/秒  | 60s、300s     |
| wan_outtraffic | 外网出带宽 | Mbps | 60s、300s     |
| wan_intraffic  | 外网入带宽 | Mbps | 60s、300s     |
| acc_outtraffic | 外网出流量 | MB   | 60s、300s     |
| wan_outpkg     | 外网出包量 | 个/秒  | 60s、300s     |
| wan_inpkg      | 外网入包量 | 个/秒  | 60s、300s     |

## 2 安装监控agent才能获取数据的监控指标

| 指标名称               | 指标中文名称  | 计算方式                                     | 指标含义                        | 单位   | 统计粒度（period） |
| ------------------ | ------- | ---------------------------------------- | --------------------------- | ---- | ------------ |
| cpu_usage          | CPU使用率  | CPU的user+nice+system+irq+softirq+idle+iowait时间占总的时间的百分比 | 机器运行期间实时占用的CPU百分比           | %    | 10s、60s、300s |
| cpu_loadavg        | CPU平均负载 | 分析/proc/loadavg中的数据，以10s为间隔采集过去1分钟内系统平均负载<br>(windows机器没有此指标) | 一段时间内正在使用和等待使用CPU的平均任务数     | -    | 10s、60s、300s |
| mem_used           | 内存使用量   | windows：调用GlobalMemoryStatusEx<br>Linux：调用psutil.virtual_memory()<br>计算：总内存 - 可用内存（包括buffers与cached）得到内存使用量数值，不包含buffers和cached | 用户实际使用的内存量，不包括缓冲区与系统缓存占用的内存 | MB   | 10s、60s、300s |
| disk_read_traffic  | 磁盘读流量   | windows：通过ioctrl调用发送IOCTL_DISK_PERFORMANCE获取磁盘读取字节大小<br>Linux：通过psutil.disk_io_counters获取磁盘读取字节大小<br>计算：两次调用的差值/调用时间的差值 获得磁盘读流量 | 磁盘分区每秒读取的字节数                | KB/s | 10s、60s、300s |
| disk_write_traffic | 磁盘写流量   | windows：通过ioctrl调用发送IOCTL_DISK_PERFORMANCE获取磁盘写入字节大小<br>Linux：通过psutil.disk_io_counters获取磁盘写入字节大小<br>计算：两次调用的差值/调用时间的差值 获得磁盘写流量 | 磁盘分区每秒写入的字节数                | KB/s | 10s、60s、300s |
| disk_io_await      | 磁盘IO等待  | windows：通过ioctrl调用发送IOCTL_DISK_PERFORMANCE获取磁盘读写次数<br>Linux：通过psutil.disk_io_counters获取磁盘读写次数<br>计算：读写时间和/读写次数和 获得IOWait值 | 磁盘分区每个I/O操作的平均耗时            | ms   | 10s、60s、300s |

注：安装agent才能获取的指标上报、展示、告警时间为客户云服务器的本地时间。若客户云服务器本地时间非东八区时间，将导致该云服务器的监控数据的时间为非东八区的子机本地时间。

> 有关更多如何使用云服务器的监控指标内容，可以查看云监控 API 中的[云服务器监控接口](https://cloud.tencent.com/document/product/248/10992)。