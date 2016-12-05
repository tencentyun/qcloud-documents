存储层 HDFS 高可用 HA，HA 即为 High Availability,用于解决 NameNode单点故障问题

该特性通过热备的方式为主 NameNode 提供一个备用者,一旦主NameNode 出现故障,可以迅速切换至备 NameNode, 从而实现不间断对外提供服务，在该方案中HA的namenode节点通常由两个 NameNode 组成,一个处于 active 状态, 另一个处于 standby 状态。Active NameNode 对外提供服务,比如处理来自客户端的 RPC请求,而 Standby NameNode 则不对外提供服务,仅同步 active namenode 的状态,以便能够在它失败时快速进行切换。


主备 NameNode 之间通过一 组 JournalNode 同步元数据信息,一条数据只要成功 写入多数 JournalNode 即认为写 入成功。 通常配置 奇数个(2N+1) 个JournalNode,这样,只要 N+1 个写入成功就认为数据写入成功, 此时最多容忍 N-1 个JournalNode 挂掉,比如 3 个 JournalNode 时,最多允许 1 个 JournalNode 挂掉,5个 JournalNode 时,最多允许 2 个 JournalNode 挂掉。

![](https://mc.qcloudimg.com/static/img/2d6e738edcabe791089188918c254ab9/HDFS_HA.png)