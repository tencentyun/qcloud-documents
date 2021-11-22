云数据仓库 PostgreSQL 集群架构图如下图所示，采用 Shared-Nothing 的大规模并行处理架构，其中 Master 一主一备，分布在两台机器上。
![](https://main.qcloudimg.com/raw/04b9a1451cab04df95f43a7734c2bc6e.png)

- **Master 节点：**Master 节点不存储业务数据，只存储数据字典，负责生成、分发 SQL 执行计划到每个 Segment 节点，同时负责与客户端的交互及权限认证。
- **Segment 节点：**Segment 节点负责存储业务数据并执行由 Master 节点分发的 SQL 语句，同时为了保证每一个 Segment 服务在同一个性能水平上，每一个 Segment 节点机器有相同的资源配置，扩容时不作机型的改变。

为了保证集群高可用，每一个 Segment 节点上分别放置一个当前节点的 Primary Segment 和一个其他节点的 Mirror Segment 作为对应的备节点。当 Segment 节点不可用时，将采用镜像节点代替。当 Master 节点不可用时会自动切换至备 Master 节点（Standby Master），以保持集群可用状态，主节点恢复启动后会自动同步变更。

集群所有的业务数据存放于所有 Segment 节点的数据库上，每一张数据表都会被切片存放于各个 Segment 节点中，当进行分析时，所有 Segment 节点同时工作计算自己部分的数据，从而大大提升计算效率。

云数据仓库 PostgreSQL 支持数据备份及恢复功能，在开启数据备份后，每个 Segment 节点会创建包含重建数据命令的转储文件，在 Master 节点会创建几个包含系统目标、元数据文件、DDL 语句等信息的转储文件。在数据恢复时，所有的 Segment 都同时从本地备份文件恢复数据。

