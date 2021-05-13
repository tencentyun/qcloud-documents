## 命名空间

Namespace=QCE/TBASE

## 监控指标

| 指标英文名             | 指标中文名         | 单位  | 维度               | 统计周期                 |
| ---------------------- | ------------------ | ----- | ------------------ | ------------------------ |
| CpuUsedPct             | CPU利用率          | %     | InstanceId         | 60s、300s、3600s、86400s |
| CpuUsedPctNode         | CPU利用率          | %     | InstanceId、NodeId | 60s、300s、3600s、86400s |
| CapacityUsage          | 已使用容量         | GB    | InstanceId         | 60s、300s、3600s、86400s |
| WriteRequests          | 写请求数           | 次    | InstanceId         | 60s、300s、3600s、86400s |
| WriteRequestsNode      | 写请求数           | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| XlogDiff               | 主备xlog同步差异   | B     | InstanceId         | 60s、300s、3600s、86400s |
| XlogDiffNode           | 主备xlog同步差异   | B     | InstanceId、NodeId | 60s、300s、3600s、86400s |
| TotalRequests          | 总请求数           | 次    | InstanceId         | 60s、300s、3600s、86400s |
| TotalRequestsNode      | 总请求数           | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| Connections            | 连接数             | 次    | InstanceId         | 60s、300s、3600s、86400s |
| XidSyncDelay           | XLOG同步延迟       | ms    | InstanceId         | 60s、300s、3600s、86400s |
| XidSyncDelayNode       | XLOG同步延迟       | ms    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| SqlRuntimeMax          | 最大TOP10执行耗时  | ms    | InstanceId         | 60s、300s、3600s、86400s |
| SqlRuntimeMaxNode      | 最大TOP10执行耗时  | ms    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| MasterSwitch           | 主备切换次数       | 次    | InstanceId         | 60s、300s、3600s、86400s |
| MasterSwitchNode       | 主备切换次数       | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| SqlRuntimeAvg          | 平均SQL执行耗时    | ms    | InstanceId         | 60s、300s、3600s、86400s |
| SqlRuntimeAvgNode      | 平均SQL执行耗时    | ms    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| SqlRuntimeMin          | 最小TOP10执行耗时  | ms    | InstanceId         | 60s、300s、3600s、86400s |
| SqlRuntimeMinNode      | 最小TOP10执行耗时  | ms    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| ErrorRequests          | 错误请求数         | 次    | InstanceId         | 60s、300s、3600s、86400s |
| ErrorRequestsNode      | 错误请求数         | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| ReadRequests           | 读请求数           | 次    | InstanceId         | 60s、300s、3600s、86400s |
| ReadRequestsNode       | 读请求数           | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| TwoPhaseCommitTrxs     | 残留两阶段事务数目 | 个    | InstanceId         | 60s、300s、3600s、86400s |
| TwoPhaseCommitTrxsNode | 残留两阶段事务数目 | 个    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| OtherRequests          | 其他请求数         | 次    | InstanceId         | 60s、300s、3600s、86400s |
| OtherRequestsNode      | 其他请求数         | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| CacheHitPct            | 缓存命中率         | %     | InstanceId         | 60s、300s、3600s、86400s |
| CapacityUsedPct        | 容量使用率         | %     | InstanceId         | 60s、300s、3600s、86400s |
| CapacityUsageNode      | 已使用容量         | GB    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| ConnectionsNode        | 连接数             | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| CacheHitPctNode        | 缓存命中率         | %     | InstanceId、NodeId | 60s、300s、3600s、86400s |
| CapacityUsedPctNode    | 容量使用率         | %     | InstanceId、NodeId | 60s、300s、3600s、86400s |
| XidRemain              | 剩余XID数量        | 个    | InstanceId         | 60s、300s、3600s、86400s |
| XidRemainNode          | 剩余XID数量        | 个    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| MemUsedPctNode         | 内存利用率         | %     | InstanceId、NodeId | 60s、300s、3600s、86400s |
| IopsNode               | IO吞吐量           | 次/秒 | InstanceId、NodeId | 60s、300s、3600s、86400s |
| UserRequests           | 业务请求数         | 次    | InstanceId         | 60s、300s、3600s、86400s |
| UpdateRequestsNode     | 更新请求数         | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| MemUsedPct             | 内存利用率         | %     | InstanceId         | 60s、300s、3600s、86400s |
| Iops                   | IO吞吐量           | 次/秒 | InstanceId         | 60s、300s、3600s、86400s |
| UserRequestsNode       | 业务请求数         | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| UpdateRequests         | 更新请求数         | 次    | InstanceId         | 60s、300s、3600s、86400s |
| DeleteRequests         | 删除请求数         | 次    | InstanceId         | 60s、300s、3600s、86400s |
| DeleteRequestsNode     | 删除请求数         | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |
| InsertRequests         | 插入请求数         | 次    | InstanceId         | 60s、300s、3600s、86400s |
| InsertRequestsNode     | 插入请求数         | 次    | InstanceId、NodeId | 60s、300s、3600s、86400s |

## 各维度对应参数总览

| 参数名称                       | 维度名称   | 维度解释                   | 格式                                 |
| ------------------------------ | ---------- | -------------------------- | ------------------------------------ |
| Instances.N.Dimensions.0.Name  | InstanceId | 云数据库实例 ID 的维度名称 | 输入 String 类型维度名称：InstanceId |
| Instances.N.Dimensions.0.Value | InstanceId | 云数据库实例的具体 ID      | 输入具体实例 ID，例如：ins-mm8bs222  |
| Instances.N.Dimensions.1.Name  | NodeId     | 云数据库节点 ID 的维度名称       | 输入 String 类型维度名称：NodeId     |
| Instances.N.Dimensions.1.Value | NodeId     | 云数据库节点的具体 ID      | 输入具体实例 ID，例如：877adc0ada3e  |

## 入参说明

**查询实例级别监控指标数据，入参取值如下：**
&Namespace=QCE/TBASE
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=云数据库实例的具体 ID

**查询节点级别监控指标数据，入参取值如下：**
&Namespace=QCE/TBASE
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=云数据库实例的具体 ID
&Instances.N.Dimensions.0.Name=NodeId
&Instances.N.Dimensions.0.Value=云数据库节点的具体 ID
