## 命名空间

Namespace=QCE/CES

## 监控指标

### 基础指标

| 指标英文名                            | 指标中文名                                             | 单位  | 维度        | 统计粒度（period）       |
| ------------------------------------- | ------------------------------------------------------ | ----- | ----------- | ------------------------ |
| CpuUsageAvg                           | 集群内所有节点 CPU 使用率平均值                          | %     | uInstanceId | 60s、300s、3600s、86400s |
| CpuUsageMax                           | 集群内所有节点 CPU 使用率最大值                          | %     | uInstanceId | 60s、300s、3600s、86400s |
| DiskUsageAvg                          | 集群内所有节点磁盘使用率平均值                         | %     | uInstanceId | 60s、300s、3600s、86400s |
| DiskUsageMax                          | 集群内所有节点磁盘使用率最大值                         | %     | uInstanceId | 60s、300s、3600s、86400s |
| IndexSpeed                            | 集群平均每秒写入请求次数                               | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| JvmMemUsageAvg                        | 集群内所有节点 JVM 内存使用率平均值                      | %     | uInstanceId | 60s、300s、3600s、86400s |
| JvmMemUsageMax                        | 集群内所有节点 JVM 内存使用率最大值                      | %     | uInstanceId | 60s、300s、3600s、86400s |
| SearchCompletedSpeed                  | 集群平均每秒查询请求次数                               | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| SearchRejectedCompletedPercent        | 集群负载过高时查询请求拒绝率                           | %     | uInstanceId | 60s、300s、3600s、86400s |
| Status                                | 集群健康状态：<br>0：Green<br>1：Yellow<br>2：Red                    | -     | uInstanceId | 60s、300s、3600s、86400s |
| IndexLatencyAvg                       | 平均写入延迟                                           | ms    | uInstanceId | 60s、300s、3600s、86400s |
| IndexLatencyMax                       | 最大写入延迟                                           | ms    | uInstanceId | 60s、300s、3600s、86400s |
| SearchLatencyAvg                      | 平均查询延迟                                           | ms    | uInstanceId | 60s、300s、3600s、86400s |
| SearchLatencyMax                      | 最大查询延迟                                           | ms    | uInstanceId | 60s、300s、3600s、86400s |
| CpuLoad1minAvg                        | 集群1分钟平均负载                                      | 0     | uInstanceId | 60s、300s、3600s、86400s |
| CpuLoad1minMax                        | 集群1分钟最大负载                                      | 0     | uInstanceId | 60s、300s、3600s、86400s |
| IndexDocs                             | 集群总文档数                                           | 个    | uInstanceId | 60s、300s、3600s、86400s |
| BulkRejectedCompletedPercent          | bulk 拒绝率                                             | %     | uInstanceId | 60s、300s、3600s、86400s |
| AutoSnapshotStatus                    | 自动快照备份状态                                       | 0     | uInstanceId | 60s、300s、3600s、86400s |
| MemUsageAvg                           | 集群内所有节点平均物理内存使用率                       | %     | uInstanceId | 60s、300s、3600s、86400s |
| MemUsageMax                           | 集群内所有节点最大物理内存使用率                       | %     | uInstanceId | 60s、300s、3600s、86400s |
| JvmOldMemUsageAvg                     | 平均 JVM old 区内存使用率                                | %     | uInstanceId | 60s、300s、3600s、86400s |
| JvmOldMemUsageMax                     | 最大 JVM old 区内存使用率                                | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskReadIopsAvg                   | 集群内所有节点平均磁盘每秒读次数                       | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskReadIopsMax                   | 集群内所有节点最大磁盘每秒读次数                       | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskWriteIopsAvg                  | 集群内所有节点平均磁盘每秒写次数                       | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskWriteIopsMax                  | 集群内所有节点最大磁盘每秒写次数                       | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskUtilAvg                       | 集群内所有节点磁盘有 IO 操作的时间与总时间的百分比平均值 | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskUtilMax                       | 集群内所有节点磁盘有 IO 操作的时间与总时间的百分比最大值 | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeParentBreakerDifMax               | 节点单周期熔断次数_最大值                              | 个    | uInstanceId | 60s、300s、3600s、86400s |
| NodeParentBreakerDifAvg               | 节点单周期熔断次数_平均值                              | 个    | uInstanceId | 60s、300s、3600s、86400s |
| NodeJvmMemUsageMax                    | 节点 JVM 内存使用率_最大值                               | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeJvmMemUsageAvg                    | 节点 JVM 内存使用率_平均值                               | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeJvmOldMemUsageMax                 | JVM_Old 区内存使用率_最大值                             | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeJvmOldMemUsageAvg                 | JVM_Old 区内存使用率_平均值                             | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeOldGcDifMax                       | 节点单周期 OldGC 次数_最大值                             | 次    | uInstanceId | 60s、300s、3600s、86400s |
| NodeFielddataMemoryInBytesAvg         | 节点 FieldData 占用的堆内存大小_平均值                   | B     | uInstanceId | 60s、300s、3600s、86400s |
| NodeSearchSpeedMax                    | 节点查询速度_最大值                                    | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeSearchSpeedAvg                    | 节点查询速度_平均值                                    | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeIndexSpeedMax                     | 节点写入速度_最大值                                    | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeIndexSpeedAvg                     | 节点写入速度_平均值                                    | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeBulkSpeedMax                      | 节点单周期 bulk 速度_最大值                              | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeBulkSpeedAvg                      | 节点单周期 bulk 速度_平均值                              | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeSearchRejectedCompletedPercentMax | 节点单周期查询拒绝率_最大值                            | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeSearchRejectedCompletedPercentAvg | 节点单周期查询拒绝率_平均值                            | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeBulkRejectedCompletedPercentMax   | 节点单周期 bulk 拒绝率_最大值                            | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeBulkRejectedCompletedPercentAvg   | 节点单周期 bulk 拒绝率_平均值                            | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeSearchLatencyMax                  | 节点单周期查询平均延迟_最大值                          | ms    | uInstanceId | 60s、300s、3600s、86400s |
| NodeSearchLatencyAvg                  | 节点单周期查询平均延迟_平均值                          | ms    | uInstanceId | 60s、300s、3600s、86400s |
| NodeIndexLatencyMax                   | 节点单周期写入平均延迟_最大值                          | ms    | uInstanceId | 60s、300s、3600s、86400s |
| NodeIndexLatencyAvg                   | 节点单周期写入平均延迟_平均值                          | ms    | uInstanceId | 60s、300s、3600s、86400s |
| NodeCpuUsageMax                       | 节点 CPU 使用率_最大值                                   | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeCpuUsageAvg                       | 节点 CPU 使用率_平均值                                   | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeMemUsageMax                       | 节点内存使用率_最大值                                  | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeMemUsageAvg                       | 节点内存使用率_平均值                                  | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeCpuLoad1minMax                    | 节点 CPU 1分钟负载_最大值                                | -     | uInstanceId | 60s、300s、3600s、86400s |
| NodeCpuLoad1minAvg                    | 节点 CPU 1分钟负载_平均值                                | -     | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskUsageMax                      | 节点磁盘使用率_最大值                                  | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskUsageAvg                      | 节点磁盘使用率_平均值                                  | %     | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskReadTrafficAvg                | 节点磁盘读流量_平均值                                  | KB/s  | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskReadTrafficMax                | 节点磁盘读流量_最大值                                  | KB/s  | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskWriteTrafficMax               | 节点磁盘写流量_最大值                                  | KB/s  | uInstanceId | 60s、300s、3600s、86400s |
| NodeDiskWriteTrafficAvg               | 节点磁盘写流量_平均值                                  | KB/s  | uInstanceId | 60s、300s、3600s、86400s |
| BulkCompletedDif                      | 单周期 Bulk 完成次数                                     | 次    | uInstanceId | 60s、300s、3600s、86400s |
| IndexTotalDif                         | 单周期写入次数                                         | 次    | uInstanceId | 60s、300s、3600s、86400s |
| SearchCompletedDif                    | 单周期查询完成次数                                     | 次    | uInstanceId | 60s、300s、3600s、86400s |
| NodeBulkSpeedSum                      | 节点 bulk 速度_求和                                      | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeIndexSpeedSum                     | 节点写入速度_求和                                      | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| NodeSearchSpeedSum                    | 节点查询速度_求和                                      | 个/秒 | uInstanceId | 60s、300s、3600s、86400s |
| IsReadOnly                            | 集群是否只读                                           | -     | uInstanceId | 60s、300s、3600s、86400s |
| IsIndexBlock                          | 是否有索引只读                                         | -     | uInstanceId | 60s、300s、3600s、86400s |
| IsVisible                             | 集群是否正常响应                                       | -     | uInstanceId | 60s、300s、3600s、86400s |

### 磁盘指标

| 指标英文名       | 指标中文名   | 单位     | 维度                         | 统计粒度（period）       |
| ---------------- | ------------ | -------- | ---------------------------- | ------------------------ |
| DiskUsage        | 磁盘使用率   | %        | uInstanceId、device、env、ip | 60s、300s、3600s、86400s |
| DiskAwait        | 操作等待时间 | ms       | uInstanceId、device、env、ip | 60s、300s、3600s、86400s |
| DiskIoutil       | 磁盘 IO Util  | %        | uInstanceId、device、env、ip | 60s、300s、3600s、86400s |
| DiskIps          | 每秒写入次数 | 次     | uInstanceId、device、env、ip | 60s、300s、3600s、86400s |
| DiskOps          | 每秒读取次数 | 次   | uInstanceId、device、env、ip | 60s、300s、3600s、86400s |
| DiskReadTraffic  | 硬盘读流量   | KB/s | uInstanceId、device、env、ip | 60s、300s、3600s、86400s |
| DiskSvctm        | 操作服务时间 | ms       | uInstanceId、device、env、ip | 60s、300s、3600s、86400s |
| DiskWriteTraffic | 硬盘写流量   | KB/s | uInstanceId、device、env、ip | 60s、300s、3600s、86400s |

### 节点指标

| 指标英文名                         | 指标中文名                      | 单位  | 维度                                | 统计粒度（period）       |
| ---------------------------------- | ------------------------------- | ----- | ----------------------------------- | ------------------------ |
| NodeStatus                         | 节点健康状态                    | -     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeJvmMemUsage                    | 节点 JVM 内存使用率             | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeJvmOldMemUsage                 | JVM_Old 区内存使用率            | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeOldGcDif                       | 节点单周期 OldGC 次数           | 次    | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeOldGcTimeDif                   | 节点单周期 OldGC 时间           | ms    | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeFielddataMemoryInBytes         | 节点 FieldData 占用的堆内存大小 | B     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeSegmentCount                   | 节点 segment 数量               | -     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeSearchSpeed                    | 节点查询速度                    | 次/秒 | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeIndexSpeed                     | 节点写入速度                    | 次/秒 | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeBulkSpeed                      | 节点单周期 bulk 速度            | 次/秒 | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeSearchRejectedCompletedPercent | 节点单周期查询拒绝率            | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeBulkRejectedCompletedPercent   | 节点单周期 bulk 拒绝率          | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeSearchLatency                  | 节点单周期查询平均延迟          | ms    | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeIndexLatency                   | 节点单周期写入平均延迟          | ms    | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeCpuUsage                       | 节点 CPU 使用率                 | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeMemUsage                       | 节点内存使用率                  | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeCpuLoad1min                    | 节点 CPU 1分钟负载              | -     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |
| NodeDiskPathMaxUsage               | 节点磁盘最大使用率              | %     | uInstanceId、hotwarm、nodeId、setid | 60s、300s、3600s、86400s |

### 冷热集群

| 指标英文名                                       | 指标中文名                                                   | 单位  | 维度                 | 统计粒度（period）       |
| ------------------------------------------------ | ------------------------------------------------------------ | ----- | -------------------- | ------------------------ |
| NodeParentBreaker<br/>DifHotwarmMax              | 节点熔断次数_冷热_最大值                                     | 次    | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeParentBreaker<br/>DifHotwarmAvg              | 节点熔断次数_冷热_平均值                                     | 次    | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeJvmMemUsageHotwarmAvg                        | 节点JVM 内存使用率_平均值_冷热                               | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeJvmMemUsageHotwarmMax                        | 节点JVM 内存使用率_最大值_冷热                               | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeJvmOldMem<br/>UsageHotwarmMax                | JVM_Old 区内存使用率_最大值_冷热                             | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeJvmOldMemUsage<br/>HotwarmAvg                | JVM_Old 区内存使用率_平均值_冷热                             | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeOldGcDifHotwarmMax                           | 节点单周期 OldGC 次数_最大值_冷热                            | 次    | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeOldGcDifHotwarmAvg                           | 节点单周期 OldGC 次数_平均值_冷热                            | 次    | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeOldGcTimeDifHotwarmMax                       | 节点单周期 OldGC 时间_最大值_冷热                            | ms    | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeOldGcTimeDifHotwarmAvg                       | 节点单周期 OldGC 时间_平均值_冷热                            | ms    | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeFielddataMemoryIn<br>BytesHotwarmMax         | 节点 FieldData 占用的堆内存大小_最大值_冷热                  | B     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeFielddataMemoryIn<br/>BytesHotwarmAvg        | 节点 FieldData 占用的堆内存大小_平均值_冷热                  | B     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeSearchSpeedHotwarmMax                        | 节点查询速度_最大值_冷热                                     | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeSearchSpeedHotwarmAvg                        | 节点查询速度_平均值_冷热                                     | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeSearchSpeedHotwarmSum                        | 节点查询速度_加和值_冷热                                     | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeIndexSpeedHotwarmMax                         | 节点写入速度_最大值_冷热                                     | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeIndexSpeedHotwarmAvg                         | 节点写入速度_平均值_冷热                                     | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeIndexSpeedHotwarmSum                         | 节点写入速度_加和值_冷热                                     | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeBulkSpeedHotwarmMax                          | 节点单周期 bulk 速度_最大值_冷热                             | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeBulkSpeedHotwarmAvg                          | 节点单周期 bulk 速度_平均值_冷热                             | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeBulkSpeedHotwarmSum                          | 节点单周期 bulk 速度_加和值_冷热                             | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeBulkRejectedCompleted<br>PercentHotwarmMax   | 节点单周期 bulk 拒绝率_最大值_冷热                           | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeBulkRejectedCompleted<br>PercentHotwarmAvg   | 节点单周期 bulk 拒绝率_平均值_冷热                           | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeSearchRejectedCompleted<br>PercentHotwarmMax | 节点单周期查询拒绝率_最大值_冷热                             | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeSearchRejectedCompleted<br>PercentHotwarmAvg | 节点单周期查询拒绝率_平均值_冷热                             | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeSearchLatencyHotwarmMax                      | 节点单周期查询平均延迟_最大值_冷热                           | ms    | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeSearchLatencyHotwarmAvg                      | 节点单周期查询平均延迟_平均值_冷热                           | ms    | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeIndexLatencyHotwarmMax                       | 节点单周期写入平均延迟_最大值_冷热                           | ms    | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeIndexLatencyHotwarmAvg                       | 节点单周期写入平均延迟_平均值_冷热                           | ms    | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeCpuUsageHotwarmMax                           | 节点 CPU 使用率_最大值_冷热                                  | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeCpuUsageHotwarmAvg                           | 节点 CPU 使用率_平均值_冷热                                  | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeMemUsageHotwarmMax                           | 节点内存使用率_最大值_冷热                                   | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeMemUsageHotwarmAvg                           | 节点内存使用率_平均值_冷热                                   | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeCpuLoad1minHotwarmMax                        | 节点 CPU 1分钟负载_最大值_冷热                               | -     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeCpuLoad1minHotwarmAvg                        | 节点 CPU 1分钟负载_平均值_冷热                               | -     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskUsageHotwarmMax                          | 节点磁盘使用率_最大值_冷热                                   | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskUsageHotwarmAvg                          | 节点磁盘使用率_平均值_冷热                                   | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskReadIopsHotwarmAvg                       | 集群内所有节点平均磁盘每秒读次数_冷热                        | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskReadIopsHotwarmMax                       | 集群内所有节点最大磁盘每秒读次数_冷热                        | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskWriteIopsHotwarmMax                      | 集群内所有节点最大磁盘每秒写次数_冷热                        | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskWriteIopsHotwarmAvg                      | 集群内所有节点平均磁盘每秒写次数_冷热                        | 次/秒 | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskUtilHotwarmAvg                           | 集群内所有节点磁盘有 IO 操作的时间与总时间的百分比平均值_冷热 | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskUtilHotwarmMax                           | 集群内所有节点磁盘有 IO 操作的时间与总时间的百分比最大值_冷热 | %     | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskReadTrafficHotwarmAvg                    | 节点磁盘读流量_平均值_冷热                                   | KB/s  | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskReadTrafficHotwarmMax                    | 节点磁盘读流量_最大值_冷热                                   | KB/s  | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskWriteTrafficHotwarmMax                   | 节点磁盘写流量_最大值_冷热                                   | KB/s  | uInstanceId、hotwarm | 60s、300s、3600s、86400s |
| NodeDiskWriteTrafficHotwarmAvg                   | 节点磁盘写流量_平均值_冷热                                   | KB/s  | uInstanceId、hotwarm | 60s、300s、3600s、86400s |

### Kibana节点

| 指标英文名      | 指标中文名       | 单位 | 维度            | 统计粒度（period）       |
| --------------- | ---------------- | ---- | --------------- | ------------------------ |
| KibanaDiskUsage | 磁盘使用率       | %    | uInstanceId、ip | 60s、300s、3600s、86400s |
| KibanaCpuLoad1  | CPU 1分钟平均负载 | -    | uInstanceId、ip | 60s、300s、3600s、86400s |
| KibanaCpuUsage  | CPU 使用率        | %    | uInstanceId、ip | 60s、300s、3600s、86400s |
| KibanaMemUsage  | 内存使用率       | %    | uInstanceId、ip | 60s、300s、3600s、86400s |
| KibanaStatus    | kibana 进程状态   | -    | uInstanceId、ip | 60s、300s、3600s、86400s |

## 各维度对应参数总览

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
| Instances.N.Dimensions.0.Name  |device      |磁盘 ID 所属维度名称| 输入 String 类型维度名称：device                        |
| Instances.N.Dimensions.0.Value | device    | 磁盘具体 ID      | 输入实例具体 ID，例如:disk-123456|
| Instances.N.Dimensions.0.Name  |env    |磁盘所属环境的维度名称  | 输入 String 类型维度名称： env                          |
| Instances.N.Dimensions.0.Value |env     | 具体环境名称      | 输入实例具体 ID，例如：cvm            |
| Instances.N.Dimensions.0.Name  | ip      | 所属 IP 的维度名称  | 输入 String 类型维度名称：ip                            |
| Instances.N.Dimensions.0.Value | ip      | 具体 ip       | 输入实例具体 ID，例如：111.111.111.111                  |

## 入参说明

1. 查询 Elasticsearch Service -基础指标监控数据，入参取值如下：
&Namespace=QCE/CES
&Instances.N.Dimensions.0.Name=uInstanceId
&Instances.N.Dimensions.0.Value=ES 具体实例 ID

2. 查询 Elasticsearch Service -磁盘指标控数据，入参取值如下：
&Namespace=QCE/CES
&Instances.N.Dimensions.0.Name=uInstanceId
&Instances.N.Dimensions.0.Value=ES 具体实例 ID
&Instances.N.Dimensions.1.Name=device
&Instances.N.Dimensions.1.Value= 磁盘具体 ID
&Instances.N.Dimensions.2.Name=env
&Instances.N.Dimensions.2.Value= 磁盘所属环境
&Instances.N.Dimensions.2.Name=ip
&Instances.N.Dimensions.2.Value= 磁盘所属 ip

3. 查询 Elasticsearch Service -节点指标监控数据，入参取值如下：
&Namespace=QCE/CES
&Instances.N.Dimensions.0.Name=uInstanceId
&Instances.N.Dimensions.0.Value=ES 具体实例 ID
&Instances.N.Dimensions.1.Name=hotwarm
&Instances.N.Dimensions.1.Value=ES 具体节点冷热属性 
&Instances.N.Dimensions.2.Name=nodeId
&Instances.N.Dimensions.2.Value=ES 具体节点 ID
&Instances.N.Dimensions.3.Name=setid
&Instances.N.Dimensions.3.Value=ES 具体节点所属可用区 ID

4. 查询 Elasticsearch Service -节点冷热属性指标控数据，入参取值如下：
&Namespace=QCE/CES
&Instances.N.Dimensions.0.Name=uInstanceId
&Instances.N.Dimensions.0.Value=ES 具体实例 ID
&Instances.N.Dimensions.1.Name=hotwarm
&Instances.N.Dimensions.1.Value=ES 具体节点冷热属性 

5. 查询 Elasticsearch Service -Kibana 节点指标控数据，入参取值如下：
&Namespace=QCE/CES
&Instances.N.Dimensions.0.Name=uInstanceId
&Instances.N.Dimensions.0.Value=ES 具体实例 ID
&Instances.N.Dimensions.1.Name=ip
&Instances.N.Dimensions.1.Value= 节点所属 ip
