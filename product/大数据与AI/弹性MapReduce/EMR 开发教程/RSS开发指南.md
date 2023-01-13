## RSS 简介
Apache Uniffle 是用于计算引擎的统一远程 Shuffle 服务（RSS，Remote Shuffle Service），它具有在远程服务器上聚合和存储 Shuffle 数据的能力，从而极大地提高了大型作业的性能和可靠性。
## 背景介绍
现有 Shuffle 方案存在的问题：
- 现有 Shuffle 无法使计算做到 serverless，在机器资源被抢占时会导致 Shuffle 数据的重新计算。
- Shuffle Partition 会导致大量的 Shuffle 连接和网络小包，大规模场景下极容易发生超时问题。
- Shuffle 过程存在写放大和随机 IO 问题，当 Shuffle 数据过大时，会严重影响集群性能和稳定性。
- Spark Shuffle 服务和 NodeManager 在同一进程，IO 负载较高时极易导致 NodeManager 重启，影响 Yarn 调度。

## RSS 基本特点
1. 将 Shuffle 数据存储在远程服务器，支持计算存储分离，计算存储混布等集群部署模式。
2. 支持 Shuffle 数据聚合和数据缓存机制，最大化利用内存资源，降低对于磁盘的随机访问。
3. 支持 Shuffle 数据的多种存储方式，如本地文件，HDFS 文件及混合模式等。
4. 支持 Shuffle 数据的正确性校验，过滤无效数据的同时，保证任务计算过程中的数据正确性。
5. 采用主从架构和主备多活模式，提升了集群资源利用率和服务的稳定性。

## RSS 基本架构
![](https://qcloudimg.tencent-cloud.cn/raw/d96ed876585eb8f375108ccce1f07e58.png)
其中，各个组件的功能如下：
- Coordinator，基于心跳机制管理 Shuffle Server，存储 Shuffle Server 的资源使用等元数据信息，还承担任务分配职责，根据 Shuffle Server 的负载，分配合适的 Shuffle Server 给 Spark 应用处理不同的 Partition 数据。
- Shuffle Server，主要负责接收 Shuffle 数据，聚合后再写入存储中，基于不同的存储方式，还能用来读取 Shuffle 数据（如 LocalFile 存储模式）。
- Shuffle Client，主要负责和 Coordinator 和 Shuffle Server 通讯，发送 Shuffle 数据的读写请求，保持应用和 Coordinator 的心跳等。

## RSS 使用
RSS 集群提供远程 Shuffle 服务，无法单独使用，需要 Spark 容器集群关联后使用。
关联方法为：单击 **Spark 集群 > 集群信息 > 关联 RSS 集群**，然后选取处于运行中的 RSS 集群即可。详情请参见 [关联 RSS 集群](https://cloud.tencent.com/document/product/589/82650)。

## RSS 配置
您可在**集群服务 > 配置管理**页面查看 RSS 不同角色的配置文件和常见配置项内容。
Coordinator 角色的配置文件有 coordinator.conf 和 log4j.properties，Shuffle Server 角色有 server.conf 和 log4j.properties 文件。
coordinator.conf 常见配置项，不建议修改：

| 参数 | 默认值 | 描述 |
|---------|---------|---------|
| rss.coordinator.app.expired	| 60000	| Application 过期时间（ms）| 
| rss.coordinator.dynamicClientConf.enabled	| false	| 是否开启动态客户端配置，由 spark 客户端获取| 
| rss.coordinator.exclude.nodes.file.path	| file:///usr/local/service/rss/conf/exclude_nodes	| 排除节点的配置文件路径| 
| rss.coordinator.server.heartbeat.timeout	| 30000| 	如果无法从 shuffle 服务器获取心跳，则超时| 
| rss.coordinator.shuffle.nodes.max	| 1000| 	分配时最大 Shuffle Server 数| 
| rss.jetty.http.port	| 19998	| Coordinator 的 HTTP 端口| 
| rss.rpc.server.port	| 19999	| Coordinator 的 RPC 端口| 
| rss.storage.type	| MEMORY_LOCALFILE	| RSS 存储类型，有 MEMORY_ONLY、MEMORY_LOCALFILE 和 MEMORY_LOCALFILE_HDFS。由于无可用的 Hadoop 集群，当前默认 MEMORY_LOCALFILE| 

server.conf 常见配置项，不建议修改：

| 参数 | 默认值 | 描述 |
|---------|---------|---------|
| rss.coordinator.quorum	| rss-coordinator-rss-<集群Id>-0:19999,rss-coordinator-rss-<集群Id>-1:19999	| Coordinator 地址信息| 
| rss.jetty.http.port	| 19998	| Shuffle Server 的 HTTP 端口| 
| rss.rpc.server.port| 	19999	| Shuffle Server 的 RPC 端口| 
| rss.server.buffer.capacity	| 内存 Limit 值 * 0.75 * 0.6	| Shuffle Server 缓冲区管理器的最大内存| 
| rss.server.disk.capacity	| 单个数据盘容量*0.9| 	Shuffle Server 可以使用的磁盘容量| 
| rss.server.flush.thread.alive	| 数据盘数量| 	将数据刷新到文件的线程数| 
| rss.server.flush.threadPool.size	| 数据盘数量*2	| 将数据刷新到文件的线程池大小| 
| rss.server.heartbeat.interval	| 10000	| 到 Coordinator 的心跳间隔| 
| rss.server.heartbeat.timeout	| 60000	| 心跳超时时间| 
| rss.server.read.buffer.capacity	| 内存 Limit 值 * 0.75 * 0.2	| 读取数据的最大缓冲区大小| 
| rss.storage.basePath	| /data1/rssdata,/data2/rssdata... 路径个数默认等于数据盘数量| 	Shuffle 数据写入数据盘的路径| 
| rss.storage.type	| MEMORY_LOCALFILE	| RSS存储类型，需与 Coordinator 保持一致| 

更多信息可参考 [incubator-uniffle](https://github.com/apache/incubator-uniffle)。
