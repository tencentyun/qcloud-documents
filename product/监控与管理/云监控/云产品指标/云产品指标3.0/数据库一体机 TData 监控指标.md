## 命名空间

Namespace = QCE/TDATA

## 监控指标

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

| 指标英文名             | 指标含义                                                     | 指标单位 | 维度                   | 统计粒度  |
| ---------------------- | ------------------------------------------------------------ | -------- | ---------------------- | --------- |
| TablespaceCapacity     | 单个表空间总容量                                             | GB       | InstanceId、Tablespace | 60s、300s |
| DataFileNum            | 数据文件个数                                                 | 个       | InstanceId、Tablespace | 60s、300s |
| TablespaceUsedCapacity | 单个表空间已使用容量                                         | GB       | InstanceId、Tablespace | 60s、300s |
| TablespaceUsedPct      | 单个表空间使用率                                             | %        | InstanceId、Tablespace | 60s、300s |
| FraUsedPct             | 闪回区使用率                                                 | %        | InstanceId             | 60s、300s |
| BufferBusyWaits        | 缓存区忙等待                                                 | 个       | InstanceId             | 60s、300s |
| DbHitRatio             | 缓存命中率                                                   | %        | InstanceId             | 60s、300s |
| BlockingSessions       | 阻塞会话数                                                   | 个       | InstanceId             | 60s、300s |
| DeadLock               | 死锁次数                                                     | 次       | InstanceId             | 60s、300s |
| ExecuteCount           | 执行次数                                                     | 次       | InstanceId             | 60s、300s |
| HardParseRatio         | 硬解析比例                                                   | %        | InstanceId             | 60s、300s |
| HardParseCount         | 硬解析次数                                                   | 次       | InstanceId             | 60s、300s |
| TotalParseCount        | 总解析次数                                                   | 次       | InstanceId             | 60s、300s |
| QueryLock              | 查询锁次数                                                   | 次       | InstanceId             | 60s、300s |
| QueryRollbacks         | 查询回滚次数                                                 | 次       | InstanceId             | 60s、300s |
| SessionUsedPct         | 会话使用率                                                   | %        | InstanceId             | 60s、300s |
| UserCommits            | 用户提交次数                                                 | 次       | InstanceId             | 60s、300s |
| TableScanRowsGotten    | 表扫描获取行数                                               | 行       | InstanceId             | 60s、300s |
| LongTableScans         | 大表扫描次数                                                 | 次       | InstanceId             | 60s、300s |
| UserActiveSessions     | 用户活跃会话数                                               | 个       | InstanceId             | 60s、300s |
| UserSessions           | 用户会话数                                                   | 个       | InstanceId             | 60s、300s |
| TablespaceMaxUsedPct   | 表空间最大使用率                                             | %        | InstanceId             | 60s、300s |
| ArchiveDest2GapStatus  | 归档日志2间隔状态<br/>0-NO CONFIG<br/>1-NO GAP<br/>2-LOG SWITCH GAP<br/>3-RESOLVABLE GAP<br/>4-UNRESOLVABLE GAP | -        | InstanceId             | 60s、300s |
| ArchiveDest3GapStatus  | 归档日志3间隔状态<br>0-NO CONFIG<br/>1-NO GAP<br/>2-LOG SWITCH GAP<br/>3-RESOLVABLE GAP<br/>4-UNRESOLVABLE GAP | -        | InstanceId             | 60s、300s |
| DataGuardMRPStatus     | DataGuard MRP 进程状态。作为主实例时无数据，<br/>作为 DataGuard 备实例时：<br/>0-NO AVAILABLE<br/>1-APPLYING LOG<br/>2-WAIT FOR GAP<br/>3-WAIT FOR LOG<br/>4-ANNOUNCING<br/>5-RECEIVING/6-WRITING<br/>7-CLOSING<br/>8-OPENING<br/>9-ERROR<br/>10-IDEL<br/>11-ATTACHED<br/>12-CONNECTED | -        | InstanceId             | 60s、300s |
| TotalAssignedCapacity  | 总分配容量                                                   | GB       | InstanceId             | 60s、300s |
| RacInstanceCount       | RAC 节点个数                                                 | 个       | InstanceId             | 60s、300s |
| RmanBackupStatus       | RMAN 备状态<br/>0-FAILED<br/>1-COMPLETED<br/>2-COMPLETED WITH WARNING<br/>3-COMPLETED WITH ERROR | -        | InstanceId             | 60s、300s |
| PhysicalWrites         | 数据块写次数                                                 | 次       | InstanceId             | 60s、300s |
| PhysicalReads          | 数据块读次数                                                 | 次       | InstanceId             | 60s、300s |
| DatabaseRole           | 数据库运行角色                                               | 个       | InstanceId             | 60s、300s |

## 各维度对应参数总览

| 参数名称                       | 维度名称   | 维度解释           | 格式                                 |
| :----------------------------- | :--------- | :----------------- | :----------------------------------- |
| Instances.N.Dimensions.0.Name  | InstanceId | 实例的维度名称     | 输入 String 类型维度名称：InstanceId |
| Instances.N.Dimensions.0.Value | InstanceId | 具体实例 ID        | 输入具体实例 ID                      |
| Instances.N.Dimensions.0.Name  | Tablespace | 表空间名的维度名称 | 输入 String 类型维度名称：Tablespace |
| Instances.N.Dimensions.0.Value | Tablespace | 具体表空间名       | 输入具体表空间名                     |



## 入参说明

**查询表空间相关指标监控数据，入参取值如下：**

&Namespace =QCE/TDATA
&Instances.N.Dimensions.0.Name =InstanceId
&Instances.N.Dimensions.0.Value =具体实例 ID
&Instances.N.Dimensions.1.Name =Tablespace
&Instances.N.Dimensions.1.Value =具体表空间名

**查询其余指标监控数据，入参取值如下：**

&Namespace =QCE/TDATA
&Instances.N.Dimensions.0.Name =InstanceId
&Instances.N.Dimensions.0.Value =具体数据库实例 ID
