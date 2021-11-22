## 命名空间

Namespace=QCE/CES

## 监控指标



| 指标英文名                      | 指标中文名                  | 计算方式                                                     | 指标含义                                                     | 单位    | 维度        | 统计粒度（period）       |
| ------------------------------- | --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------- | ----------- | ------------------------ |
| Status                          | 集群健康状态                | ES 集群在统计粒度内的最新值                                  | 集群健康状态:0:Green,1:Yellow,2:Red                          | -       | uInstanceId | 60s、300s、3600s、86400s |
| DiskUsageAvg                    | 平均磁盘使用率              | ES 集群在统计粒度内各节点磁盘使用率的平均值                  | ES 集群各节点磁盘使用率的平均值                              | %       | uInstanceId | 60s、300s、3600s、86400s |
| DiskUsageMax                    | 最大磁盘使用率              | ES 集群在统计粒度内各节点磁盘使用率的最大值                  | ES 集群各节点磁盘使用率的最大值                              | %       | uInstanceId | 60s、300s、3600s、86400s |
| JvmMemUsageAvg                  | 平均 JVM 内存使用率         | ES 集群在统计粒度内各节点 JVM 内存使用率的平均值             | ES 集群各节点 JVM 内存使用率的平均值                         | %       | uInstanceId | 60s、300s、3600s、86400s |
| JvmMemUsageMax                  | 最大 JVM 内存使用率         | ES 集群在统计粒度内各节点 JVM 内存使用率的最大值             | ES 集群各节点 JVM 内存使用率的最大值                         | %       | uInstanceId | 60s、300s、3600s、86400s |
| JvmOldMemUsageAvg               | 平均 JVM old 区内存使用率   | ES 集群在统计粒度内各节点 JVM old 区内存使用率的平均值       | ES 集群各节点 JVM old 区的平均内存使用率                     | %       | uInstanceId | 60s、300s、3600s、86400s |
| JvmOldMemUsageMax               | 最大 JVM old 区内存使用率   | ES 集群在统计粒度内各节点 JVM old 区内存使用率的最大值       | ES 集群各节点 JVM old 区的最大内存使用率                     | %       | uInstanceId | 60s、300s、3600s、86400s |
| CpuUsageAvg                     | 平均 CPU 使用率             | ES 集群在统计粒度内各节点 CPU 使用率的平均值                 | ES集群各节点 CPU使用率的平均值                               | %       | uInstanceId | 60s、300s、3600s、86400s |
| CpuUsageMax                     | 最大 CPU 使用率             | ES 集群在统计粒度内各节点 CPU 使用率的最大值                 | ES集群各节点 CPU使用率的最大值                               | %       | uInstanceId | 60s、300s、3600s、86400s |
| CpuLoad1minAvg                  | 集群1分钟 CPU 平均负载      | ES 集群在统计粒度内各节点1分钟 CPU 负载的平均值              | ES集群各节点 CPU 1分钟CPU负载的平均值                        | -       | uInstanceId | 60s、300s、3600s、86400s |
| CpuLoad1minMax                  | 集群1分钟 CPU 最大负载      | ES 集群在统计粒度内各节点1分钟 CPU 负载的最大值              | ES集群各节点 CPU 1分钟负载的最大值                           | -       | uInstanceId | 60s、300s、3600s、86400s |
| IndexLatencyAvg                 | 平均写入延迟                | ES 集群在统计粒度内写入延迟的平均值                          | ES 集群写入延迟的平均值                                      | ms      | uInstanceId | 60s、300s、3600s、86400s |
| IndexLatencyMax                 | 最大写入延迟                | ES 集群在统计粒度内写入延迟的最大值                          | ES 集群写入延迟的最大值                                      | ms      | uInstanceId | 60s、300s、3600s、86400s |
| SearchLatencyAvg                | 平均查询延迟                | ES 集群在统计粒度内查询延迟的平均值                          | ES 集群查询延迟的平均值                                      | ms      | uInstanceId | 60s、300s、3600s、86400s |
| SearchLatencyMax                | 最大查询延迟                | ES 集群在统计粒度内查询延迟的最大值                          | ES 集群查询延迟的最大值                                      | ms      | uInstanceId | 60s、300s、3600s、86400s |
| IndexSpeed                      | 写入速度                    | ES 集群单周期内写入速度的平均值                              | 每单位统计周期内，ES 集群各个节点接收到的每秒写入请求次数之和 | count/s | uInstanceId | 60s、300s、3600s、86400s |
| SearchCompletedSpeed            | 查询速度                    | ES 集群单周期内查询速度的平均值                              | ES 集群每秒完成查询操作次数                                  | count/s | uInstanceId | 60s、300s、3600s、86400s |
| BulkRejected CompletedPercent   | bulk拒绝率                  | ES 集群在统计粒度内 bulk 操作被拒绝次数占 bulk 总次数的百分比 | bulk 操作被拒绝次数占总次数的百分比                          | %       | uInstanceId | 60s、300s、3600s、86400s |
| SearchRejected CompletedPercent | 查询拒绝率                  | ES 集群在统计粒度内查询操作被拒绝次数占查询总次数的百分比    | 查询操作被拒绝次数占总次数的百分比                           | %       | uInstanceId | 60s、300s、3600s、86400s |
| IndexDocs                       | 文档总数                    | ES 集群在统计粒度内文档总数的平均值                          | ES 集群中的文档总数                                          | count   | uInstanceId | 60s、300s、3600s、86400s |
| AutoSnapshotStatus              | ES 集群自动备份任务执行状态 | ES 集群在统计粒度内最后一次执行自动备份任务的状态            | ES 集群自动备份任务的执行状态                                | -       | uInstanceId | 300s、3600s、86400s      |


| 指标英文名                                        | 指标中文名                                                  | 单位  | 维度                                | 统计粒度                 |
| ------------------------------------------------- | ----------------------------------------------------------- | ----- | ----------------------------------- | ------------------------ |
| NodeDiskReadIopsAvg                               | 集群内所有节点平均磁盘每秒读次数                            | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskReadIopsMax                               | 集群内所有节点最大磁盘每秒读次数                            | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskWriteIopsAvg                              | 集群内所有节点平均磁盘每秒写次数                            | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskWriteIopsMax                              | 集群内所有节点最大磁盘每秒写次数                            | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskUtilAvg                                   | 集群内所有节点磁盘有IO操作的时间与总时间的百分比平均值      | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskUtilMax                                   | 集群内所有节点磁盘有IO操作的时间与总时间的百分比最大值      | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeParentBreakerDifMax                           | 节点单周期熔断次数_最大值                                   | 次    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeParentBreakerDifAvg                           | 节点单周期熔断次数_平均值                                   | 次    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeJvmMemUsageMax                                | 节点JVM内存使用率_最大值                                    | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeJvmMemUsageAvg                                | 节点JVM内存使用率_平均值                                    | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeJvmOldMemUsageMax                             | JVM_Old区内存使用率_最大值                                  | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeJvmOldMemUsageAvg                             | JVM_Old区内存使用率_平均值                                  | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeOldGcDifMax                                   | 节点单周期OldGC次数_最大值                                  | 次    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeOldGcDifAvg                                   | 节点单周期OldGC次数_平均值                                  | 次    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeOldGcTimeDifMax                               | 节点单周期OldGC时间_最大值                                  | ms    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeOldGcTimeDifAvg                               | 节点单周期OldGC时间_平均值                                  | ms    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeFielddata<br/>MemoryInBytesMax                | 节点FieldData占用的堆内存大小_最大值                        | B     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeFielddata<br/>MemoryInBytesAvg                | 节点FieldData占用的堆内存大小_平均值                        | B     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeSearchSpeedMax                                | 节点查询速度_最大值                                         | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeSearchSpeedAvg                                | 节点查询速度_平均值                                         | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeIndexSpeedMax                                 | 节点写入速度_最大值                                         | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeIndexSpeedAvg                                 | 节点写入速度_平均值                                         | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeBulkSpeedMax                                  | 节点单周期bulk速度_最大值                                   | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeBulkSpeedAvg                                  | 节点单周期bulk速度_平均值                                   | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeSearchRejected<br>CompletedPercentMax         | 节点单周期查询拒绝率_最大值                                 | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeSearchRejected<br>CompletedPercentAvg         | 节点单周期查询拒绝率_平均值                                 | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeBulkRejected<br>CompletedPercentMax           | 节点单周期bulk拒绝率_最大值                                 | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeBulkRejected<br>CompletedPercentAvg           | 节点单周期bulk拒绝率_平均值                                 | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeSearchLatencyMax                              | 节点单周期查询平均延迟_最大值                               | ms    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeSearchLatencyAvg                              | 节点单周期查询平均延迟_平均值                               | ms    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeIndexLatencyMax                               | 节点单周期写入平均延迟_最大值                               | ms    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeIndexLatencyAvg                               | 节点单周期写入平均延迟_平均值                               | ms    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeCpuUsageMax                                   | 节点CPU使用率_最大值                                        | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeCpuUsageAvg                                   | 节点CPU使用率_平均值                                        | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeMemUsageMax                                   | 节点内存使用率_最大值                                       | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeMemUsageAvg                                   | 节点内存使用率_平均值                                       | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeCpuLoad1minMax                                | 节点CPU1分钟负载_最大值                                     | -     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeCpuLoad1minAvg                                | 节点CPU1分钟负载_平均值                                     | -     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskUsageMax                                  | 节点磁盘使用率_最大值                                       | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskUsageAvg                                  | 节点磁盘使用率_平均值                                       | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeStatus                                        | 节点健康状态                                                | -     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeJvmMemUsage                                   | 节点JVM内存使用率                                           | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeJvmOldMemUsage                                | JVM_Old区内存使用率                                         | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeOldGcDif                                      | 节点单周期OldGC次数                                         | 次    | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeOldGcTimeDif                                  | 节点单周期OldGC时间                                         | ms    | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeFielddataMemoryInBytes                        | 节点FieldData占用的堆内存大小                               | B     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeSegment                                    | 节点segment数量                                             | -     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeSearchSpeed                                   | 节点查询速度                                                | 次/秒 | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeIndexSpeed                                    | 节点写入速度                                                | 次/秒 | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeBulkSpeed                                     | 节点单周期bulk速度                                          | 次/秒 | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeSearchRejected<br/>CompletedPercent           | 节点单周期查询拒绝率                                        | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeBulkRejected<br/>CompletedPercent             | 节点单周期bulk拒绝率                                        | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeSearchLatency                                 | 节点单周期查询平均延迟                                      | ms    | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeIndexLatency                                  | 节点单周期写入平均延迟                                      | ms    | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeCpuUsage                                      | 节点CPU使用率                                               | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeMemUsage                                      | 节点内存使用率                                              | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeCpuLoad1min                                   | 节点CPU1分钟负载                                            | -     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| DiskUsage                                         | 磁盘使用率                                                  | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| DiskAwait                                         | 操作等待时间                                                | ms    | uInstanceId                         | 60s、300s、3600s、86400s |
| DiskIoutil                                        | 磁盘IO Util                                                 | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| DiskIps                                           | 每秒写入次数                                                | None  | uInstanceId                         | 60s、300s、3600s、86400s |
| DiskOps                                           | 每秒读取次数                                                | None  | uInstanceId                         | 60s、300s、3600s、86400s |
| DiskReadTraffic                                   | 硬盘读流量                                                  | KB/S  | uInstanceId                         | 60s、300s、3600s、86400s |
| DiskSvctm                                         | 操作服务时间                                                | ms    | uInstanceId                         | 60s、300s、3600s、86400s |
| DiskWriteTraffic                                  | 硬盘写流量                                                  | KB/S  | uInstanceId                         | 60s、300s、3600s、86400s |
| KibanaDiskUsage                                   | 磁盘使用率                                                  | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| KibanaCpuLoad1                                    | CPU1分钟平均负载                                            | None  | uInstanceId                         | 60s、300s、3600s、86400s |
| KibanaCpuUsage                                    | CPU使用率                                                   | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| KibanaMemUsage                                    | 内存使用率                                                  | %     | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskReadTrafficAvg                            | 节点磁盘读流量_平均值                                       | KB/S  | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskReadTrafficMax                            | 节点磁盘读流量_最大值                                       | KB/S  | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskWriteTrafficMax                           | 节点磁盘写流量_最大值                                       | KB/S  | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskWriteTrafficAvg                           | 节点磁盘写流量_平均值                                       | KB/S  | uInstanceId                         | 60s、300s、3600s、86400s |
| BulkCompletedDif                                  | 单周期Bulk完成次数                                          | 次    | uInstanceId                         | 60s、300s、3600s、86400s |
| IndexTotalDif                                     | 单周期写入次数                                              | 次    | uInstanceId                         | 60s、300s、3600s、86400s |
| SearchCompletedDif                                | 单周期查询完成次数                                          | 次    | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeBulkSpeedSum                                  | 节点bulk速度_求和                                           | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeIndexSpeedSum                                 | 节点写入速度_求和                                           | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeSearchSpeedSum                                | 节点查询速度_求和                                           | 次/秒 | uInstanceId                         | 60s、300s、3600s、86400s |
| NodeDiskPathMaxUsage                              | 节点磁盘最大使用率                                          | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeParentBreaker<br>DifHotwarmMax                | 节点熔断次数_冷热_最大值                                    | 次    | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeParentBreaker<br>DifHotwarmAvg                | 节点熔断次数_冷热_平均值                                    | 次    | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeJvmMemUsage<br/>HotwarmAvg                    | 节点JVM内存使用率_平均值_冷热                               | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeJvmMemUsage<br/>HotwarmMax                    | 节点JVM内存使用率_最大值_冷热                               | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeJvmOldMemUsage<br>HotwarmMax                  | JVM_Old区内存使用率_最大值_冷热                             | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeJvmOldMemUsage<br/>HotwarmAvg                 | JVM_Old区内存使用率_平均值_冷热                             | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeOldGcDifHotwarmMax                            | 节点单周期OldGC次数_最大值_冷热                             | 次    | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeOldGcDifHotwarmAvg                            | 节点单周期OldGC次数_平均值_冷热                             | 次    | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeOldGcTimeDifHotwarmMax                        | 节点单周期OldGC时间_最大值_冷热                             | ms    | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeOldGcTimeDifHotwarmAvg                        | 节点单周期OldGC时间_平均值_冷热                             | ms    | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeFielddataMemoryIn<br/>BytesHotwarmMax         | 节点FieldData占用的堆内存大小_最大值_冷热                   | Bytes | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeFielddataMemoryIn<br/>BytesHotwarmAvg         | 节点FieldData占用的堆内存大小_平均值_冷热                   | Bytes | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeSearchSpeedHotwarmMax                         | 节点查询速度_最大值_冷热                                    | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeSearchSpeedHotwarmAvg                         | 节点查询速度_平均值_冷热                                    | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeSearchSpeedHotwarmSum                         | 节点查询速度_加和值_冷热                                    | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeIndexSpeedHotwarmMax                          | 节点写入速度_最大值_冷热                                    | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeIndexSpeedHotwarmAvg                          | 节点写入速度_平均值_冷热                                    | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeIndexSpeedHotwarmSum                          | 节点写入速度_加和值_冷热                                    | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeBulkSpeedHotwarmMax                           | 节点单周期bulk速度_最大值_冷热                              | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeBulkSpeedHotwarmAvg                           | 节点单周期bulk速度_平均值_冷热                              | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeBulkSpeedHotwarmSum                           | 节点单周期bulk速度_加和值_冷热                              | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeBulkRejectedCompleted<br/>PercentHotwarmMax   | 节点单周期bulk拒绝率_最大值_冷热                            | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeBulkRejectedCompleted<br>PercentHotwarmAvg    | 节点单周期bulk拒绝率_平均值_冷热                            | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeSearchRejected<br/>PercentHotwarmMaxCompleted | 节点单周期查询拒绝率_最大值_冷热                            | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeSearchRejected<br/>CompletedPercentHotwarmAvg | 节点单周期查询拒绝率_平均值_冷热                            | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeSearchLatencyHotwarmMax                       | 节点单周期查询平均延迟_最大值_冷热                          | ms    | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeSearchLatencyHotwarmAvg                       | 节点单周期查询平均延迟_平均值_冷热                          | ms    | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeIndexLatencyHotwarmMax                        | 节点单周期写入平均延迟_最大值_冷热                          | ms    | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeIndexLatencyHotwarmAvg                        | 节点单周期写入平均延迟_平均值_冷热                          | ms    | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeCpuUsageHotwarmMax                            | 节点CPU使用率_最大值_冷热                                   | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeCpuUsageHotwarmAvg                            | 节点CPU使用率_平均值_冷热                                   | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeMemUsageHotwarmMax                            | 节点内存使用率_最大值_冷热                                  | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeMemUsageHotwarmAvg                            | 节点内存使用率_平均值_冷热                                  | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeCpuLoad1minHotwarmMax                         | 节点CPU1分钟负载_最大值_冷热                                | -     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeCpuLoad1minHotwarmAvg                         | 节点CPU1分钟负载_平均值_冷热                                | -     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskUsageHotwarmMax                           | 节点磁盘使用率_最大值_冷热                                  | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskUsageHotwarmAvg                           | 节点磁盘使用率_平均值_冷热                                  | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskReadIopsHotwarmAvg                        | 集群内所有节点平均磁盘每秒读次数_冷热                       | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskReadIopsHotwarmMax                        | 集群内所有节点最大磁盘每秒读次数_冷热                       | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskWriteIopsHotwarmMax                       | 集群内所有节点最大磁盘每秒写次数_冷热                       | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskWriteIopsHotwarmAvg                       | 集群内所有节点平均磁盘每秒写次数_冷热                       | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskUtilHotwarmAvg                            | 集群内所有节点磁盘有IO操作的时间与总时间的百分比平均值_冷热 | %     | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskUtilHotwarmMax                            | 集群内所有节点磁盘有IO操作的时间与总时间的百分比最大值_冷热 | 次/秒 | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskReadTraffic<br/>HotwarmAvg                | 节点磁盘读流量_平均值_冷热                                  | KB/S  | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskRead<br/>TrafficHotwarmMax                | 节点磁盘读流量_最大值_冷热                                  | KB/S  | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskWrite<br/>TrafficHotwarmMax               | 节点磁盘写流量_最大值_冷热                                  | KB/S  | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| NodeDiskWrite<br/>TrafficHotwarmAvg               | 节点磁盘写流量_平均值_冷热                                  | KB/S  | uInstanceId、hotwarm                | 60s、300s、3600s、86400s |
| IsReadOnly                                        | 集群是否只读                                                | -     | uInstanceId                         | 60s、300s、3600s、86400s |
| IsIndexBlock                                      | 是否有索引只读                                              | -     | uInstanceId                         | 60s、300s、3600s、86400s |
| KibanaStatus                                      | kibana进程状态                                              | -     | uInstanceId                         | 60s、300s、3600s、86400s |



>?每个指标对应的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

##  各维度对应参数总览

| 参数名称                       | 维度名称    | 维度解释                         | 格式                                                         |
| ------------------------------ | ----------- | -------------------------------- | ------------------------------------------------------------ |
| Instances.N.Dimensions.0.Name  | uInstanceId | ES 实例 ID 的维度名称            | 输入 String 类型维度名称：uInstanceId                        |
| Instances.N.Dimensions.0.Value | uInstanceId | ES 具体实例 ID                   | 输入实例具体 ID，例如：es-example                            |
| Instances.N.Dimensions.0.Name  | hotwarm     | ES 节点冷热属性的维度名称        | 输入 String 类型维度名称：hotwarm                            |
| Instances.N.Dimensions.0.Value | hotwarm     | ES 具体节点冷热属性              | 输入实例具体节点冷热属性，根据节点数据盘确定，数据盘为高性能云盘填warm，为SSD云盘填hot |
| Instances.N.Dimensions.0.Name  | nodeId      | ES 节点 ID 的维度名称            | 输入 String 类型维度名称：nodeId                             |
| Instances.N.Dimensions.0.Value | nodeId      | ES 具体节点 ID                   | 输入实例具体 ID，例如：1111111111111111111                   |
| Instances.N.Dimensions.0.Name  | setid       | ES 节点所属可用区 ID 的维度名称 | 输入 String 类型维度名称：setid                              |
| Instances.N.Dimensions.0.Value | setid       | ES 具体节点所属可用区 ID        | 输入实例具体 ID，例如广州六区为：100006                      |

## 入参说明

1、查询 Elasticsearch Service -实例维度监控数据，入参取值如下：
&Namespace=QCE/CES
&Instances.N.Dimensions.0.Name=uInstanceId
&Instances.N.Dimensions.0.Value=ES 具体实例 ID

2、查询 Elasticsearch Service -节点维度监控数据，入参取值如下：
&Namespace=QCE/CES
&Instances.N.Dimensions.0.Name=uInstanceId
&Instances.N.Dimensions.0.Value=ES 具体实例 ID
&Instances.N.Dimensions.1.Name=hotwarm
&Instances.N.Dimensions.1.Value=ES 具体节点冷热属性 
&Instances.N.Dimensions.2.Name=nodeId
&Instances.N.Dimensions.2.Value=ES 具体节点 ID

3、查询 Elasticsearch Service -节点冷热属性监控数据，入参取值如下：
&Namespace=QCE/CES
&Instances.N.Dimensions.0.Name=uInstanceId
&Instances.N.Dimensions.0.Value=ES 具体实例 ID
&Instances.N.Dimensions.1.Name=hotwarm
&Instances.N.Dimensions.1.Value=ES 具体节点冷热属性 


