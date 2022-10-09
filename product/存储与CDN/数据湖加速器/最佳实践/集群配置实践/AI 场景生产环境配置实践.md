## 简介

数据加速器 GooseFS 提供了多种部署方式，支持 [自建部署](https://cloud.tencent.com/document/product/1424/68299)，在 [TKE 上部署](https://cloud.tencent.com/document/product/1424/68301) 以及在 [EMR 上部署](https://cloud.tencent.com/document/product/1424/68300) 等。在大数据场景中，通常使用**集群模式**部署，并且采用**高可用架构**以满足业务连续性的要求。

**高可用架构**指多个 Master 节点的主备多活架构。多个 Master 节点中只有一个会作为主（Leader）节点对外提供服务，其他的备（Standby）节点通过同步共享日志（Journal）来保持与主节点相同的文件系统状态。当主节点故障宕机后，会从当前的备节点中自动选择一个接替主节点继续对外提供服务，这样就消除了系统的单点故障，实现了整体高可用架构。目前 GooseFS 支持基于 Raft 日志和 Zookeeper 两种方式来实现主备节点状态的强一致性，在容器场景下，我们推荐基于 Raft 日志模式部署您的高可用架构。本文重点介绍基于 Raft 的高可用部署配置，并区分了顺序读和随机读两种不同场景。

## 基于 Raft 的高可用架构部署配置（顺序读场景）
在顺序读的场景下，您可以参考如下推荐配置，并将该配置项复制粘贴到 goosefs-site.properties 文件中，完成您的高可用架构配置：
```
goosefs.master.embedded.journal.addresses=<master1>:9202,<master2>:9202,<master3>:9202

goosefs.master.metastore=ROCKS
# 主要是在不确定rocksdb是否修复的情况下使用
goosefs.master.metastore.block=HEAP

# 根据内存大小而定
goosefs.master.metastore.inode.cache.max.size=10000000

# rocksdb数据存放的地方
goosefs.master.metastore.dir=/meta-1/metastore

# 根目录的挂载路径，需要放在安全目录中，防止被误删除
goosefs.master.mount.table.root.ufs=/meta-1/underFSStorage

# raft 日志存放的地方
goosefs.master.journal.folder=/meta-1/journal

# 触发切主的超时时间，不易过小（jvm gc会导致切主震荡），也不易过大（影响恢复可用性的时间）
goosefs.master.embedded.journal.election.timeout=20s

# 在大数据量情况下，强烈建议关闭
goosefs.master.startup.block.integrity.check.enabled=false

# 触发checkpoint的时机，不易过小（做checkpoint会很频繁，在做checkpoint期间不会参与选主），也不易过大（影响服务重启耗时），可根据checkpoint加载时间评估。
goosefs.master.journal.checkpoint.period.entries=20000000

# acl鉴权开关，根据场景定
goosefs.security.authorization.permission.enabled=false

# 建议打开，不然会采用hostname，而hostname可能相同。
goosefs.network.ip.address.used=true

# Worker properties
goosefs.worker.tieredstore.levels=1
goosefs.worker.tieredstore.level0.alias=HDD
goosefs.worker.tieredstore.level0.dirs.quota=7TB,7TB
goosefs.worker.tieredstore.level0.dirs.path=/data-1,/data-2

# worker 重启的超时时间，在大数量情况下，尽量调大。
goosefs.worker.registry.get.timeout.ms=3600s

# 读取数据响应的超时时间，默认1h
goosefs.user.streaming.data.timeout=60s

# 写策略，默认是LocalFirstPolicy，有可能导致数据不均衡
goosefs.user.block.write.location.policy.class=com.qcloud.cos.goosefs.client.block.policy.RoundRobinPolicy

# 影响distributedLoad的速度,在不考虑影响在线读的情况下，建议设置为 cpu数目 * 2，
gosefs.job.worker.threadpool.size=50
```


## 基于 Raft 的高可用架构部署配置（随机读场景）

在随机读的场景下，您可以参考如下推荐配置，并将该配置项复制粘贴到 goosefs-site.properties 文件中，完成您的高可用架构配置：

```
goosefs.master.embedded.journal.addresses=<master1>:9202,<master2>:9202,<master3>:9202

goosefs.master.metastore=ROCKS
# 主要是在不确定rocksdb是否修复的情况下使用
goosefs.master.metastore.block=HEAP

# 根据内存大小而定
goosefs.master.metastore.inode.cache.max.size=10000000

# rocksdb数据存放的地方
goosefs.master.metastore.dir=/meta-1/metastore

# 根目录的挂载路径，需要放在安全目录中，防止被误删除
goosefs.master.mount.table.root.ufs=/meta-1/underFSStorage

# raft 日志存放的地方
goosefs.master.journal.folder=/meta-1/journal

# 触发切主的超时时间，不易过小（jvm gc会导致切主震荡），也不易过大（影响恢复可用性的时间）
goosefs.master.embedded.journal.election.timeout=20s

# 在大数据量情况下，强烈建议关闭
goosefs.master.startup.block.integrity.check.enabled=false

# 触发checkpoint的时机，不易过小（做checkpoint会很频繁，在做checkpoint期间不会参与选主），也不易过大（影响服务重启耗时），可根据checkpoint加载时间评估。
goosefs.master.journal.checkpoint.period.entries=20000000

# acl鉴权开关，根据场景定
goosefs.security.authorization.permission.enabled=false

# 建议打开，不然会采用hostname，而hostname可能相同。
goosefs.network.ip.address.used=true

# Worker properties
goosefs.worker.tieredstore.levels=1
goosefs.worker.tieredstore.level0.alias=HDD
goosefs.worker.tieredstore.level0.dirs.quota=7TB,7TB
goosefs.worker.tieredstore.level0.dirs.path=/data-1,/data-2

# worker 重启的超时时间，在大数量情况下，尽量调大。
goosefs.worker.registry.get.timeout.ms=3600s

# 读取数据响应的超时时间，默认1h
goosefs.user.streaming.data.timeout=60s

# 写策略，默认是LocalFirstPolicy，有可能导致数据不均衡
goosefs.user.block.write.location.policy.class=com.qcloud.cos.goosefs.client.block.policy.RoundRobinPolicy

# 对于随机读情况，建议调小(默认为1MB)，防止读膨胀
goosefs.user.streaming.reader.chunk.size.bytes=256KB
goosefs.user.local.reader.chunk.size.bytes=256KB

# 等待worker读流关闭的时间，在大量小文件读或者随机读情况，建议调小（默认5s），避免长尾导致的性能降低
goosefs.user.streaming.reader.close.timeout=100ms
```
