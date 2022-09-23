### 出现 Yarn nodemanager 节点不健康问题怎么处理？
#### 问题现象
Core 节点磁盘利用率超过90%，nodemanager 会置为不健康状态（Unhealthy Nodes）。

#### 解决方案
1. 建议添加云监控，设置 EMR 子机磁盘利用率在80% - 85%时告警，避免节点磁盘利用率超过90%时，nodemanager 节点状态不健康。云监控配置 EMR 磁盘利用率地址：
`https://console.cloud.tencent.com/monitor/policyTemplate`
![](https://main.qcloudimg.com/raw/75fd5e90d94ec11e178bd336f19e814c.png)
2. 若磁盘不足可进行扩容 Core 节点后做 balancer，分担 HDFS 存储空间在当前 Core 节点上的压力。
3. 定期清理磁盘空间。
 - Core 节点本身的存储空间。
 - 整个 HDFS 的存储空间。
