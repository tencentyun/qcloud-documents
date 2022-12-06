## 业务背景

云数据库 MongoDB 分片集群提供了多个 Mongos 节点，负责接收所有客户端应用程序的连接查询请求，并将请求路由到集群内部对应的分片上，同时会把接收到的响应拼装起来返回到客户端。用户通过一个 VIP 或多个 VIP 等方式接入负载均衡，将流量自动分发至不同的 Mongos 执行，以加强网络数据处理能力、增加吞吐量、提高网络的可用性和灵活性。

## 负载均衡原理

用户程序连接到一个负载均衡服务（VIP），通过一个 VIP 来屏蔽后端的多个 RSIP（ Real Server IP ）。云数据库 MongoDB 负载均衡服务通过源 IP、源端口、目标 IP、目标端口、通信协议5元组 Hash 策略，将不同请求源 IP 路由于不同的 Mongos 节点。如果后台出现 RSIP 变更，会有自动化的流程变更 VIP 和 RSIP 的映射关系，对用户无感知，接入简单。
<img src="https://qcloudimg.tencent-cloud.cn/raw/e0c2ef0cbb30645548307a25481563c1.png"  style="zoom:70%;">

#### 批量扫描 getMore 问题
当 MongoDB 无法将 find 结果一次性返回时，会优先返回第一批数据 + cursorID，客户端通过这个 cursorID 不断 getMore 迭代剩余的数据。所以一次批量扫描请求可能会对应1次 find 请求和多次 getMore 请求，并通过 cursorID 关联。 

- 每个 Mongos 节点在内存中维护了一个全局的 [ClusterCursorManager](https://github.com/mongodb/mongo/blob/r4.2.11/src/mongo/s/query/cluster_cursor_manager.h#L72)，通过 [HashMap](https://github.com/mongodb/mongo/blob/r4.2.11/src/mongo/s/query/cluster_cursor_manager.h#L721) 维护了 cursorID 和 ClusterClientCusor 的映射关系。其中，cursorID 是一个 int64 的随机数，ClusterClientCursor 则维护了请求的执行计划、当前状态等信息。 

- 如果查询结果不能一次性返回（如超过了16MB限制），则会生成一个非0的 cursorID，并将这个 ID 和 ClusterClientCusor 本身 [注册到 ClusterCursorManager](https://github.com/mongodb/mongo/blob/r4.2.11/src/mongo/s/query/cluster_cursor_manager.cpp#L263-L328) 中。
如果客户端需要后续的结果，可以携带前面返回的 cursorID 进行 getMore 请求，Mongos 会 [找到之前缓存的 ClusterClientCusor](https://github.com/mongodb/mongo/blob/r4.2.11/src/mongo/s/query/cluster_cursor_manager.cpp#L330-L383)，继续执行查询计划并返回结果。ID 和 cursor 的信息独立存在于各个 Mongos 节点中。

因此必须要保证 find 及其相关联的 getMore 请求发往同一个 Mongos 节点。而如果 getMore 请求发给了其他的 Mongos 节点，会因为找不到 Cursor 返回 CursorNotFound 错误，如下图所示。
<img src="https://qcloudimg.tencent-cloud.cn/raw/e499837ef4f0a56adb20f8a42e3ecfcb.jpg"  style="zoom:50%;">

#### 事务操作问题
MongoDB 在 4.2 版本支持了分布式事务，用户可以连接 Mongos 节点发起事务操作。在 startTransaction 和 commitTransaction/abortTransaction 之间可以执行多次 [读写操作](https://www.mongodb.com/docs/manual/core/transactions-operations/)，Mongos 在内存中记录了事务中每次请求携带的 logicalSessionId 和 txnId 等元数据来维护上下文关系。因此，[MongoDB 的设计](https://github.com/mongodb/mongo/blob/master/src/mongo/db/s/README.md#transactions) 决定了需要保证事务中的每个操作都发到同一个 Mongos 上执行。

#### 云数据库 MongoDB 负载均衡策略

基于批量扫描 getMore 问题及其事务操作问题的考虑，云数据库 MongoDB 负载均衡 Hash 策略根据访问端（一般是 CVM）IP 信息来均衡分流：一个源 IP 的请求都会落在同一个 Mongos 上，保证 getMore() 和事务操作在同一个上下文进行。

一般生产环境中访问端 IP 较多，这种策略效果较好。但是当访问端 IP 较少的情况下，特别是在压测场景下，容易引起 Mongos 负载不均衡的问题。

## Mongos 负载不均解决方案

如果您不想使用默认的云数据库 MongoDB 的负载均衡策略，可开通 Mongos 访问地址。在实例当前的 VIP 下面，系统将给不同的 Mongos 节点绑定不同的 VPORT，用户可灵活控制 Mongos 的请求分配。并且，Mongos 故障后系统将重新绑定新的 Mongos 进程，VIP 和 VPORT 地址不会变化，不影响原有的负载均衡访问地址。具体操作，请参见 [开通 Mongos 访问地址](https://cloud.tencent.com/document/product/240/75180)。

- 开通之后，在控制台**实例详情**页面的**网络配置**区域的**访问地址**中，可查看 Mongos 访问地址，展示不同连接类型的连接串。每一个连接串中配置了实例所有 Mongos 节点，通过参数 authSource、 readPreference 与  readPreferenceTags 控制访问节点类型，如下图所示。  
	![](https://qcloudimg.tencent-cloud.cn/raw/682e5fbd19922b76201f96e9e535ad93.png)

- 您可根据均衡分流的需求，直接复制连接串，在客户端连接数据库 SDK 程序中配置连接串，访问对应的 Mongos 节点。具体连接方式，请参见 [连接 MongoDB 实例](https://cloud.tencent.com/document/product/240/7092)。然而，连接串较长，请仔细操作。

- 需要注意的是，如果您在连接串中配置所有了 Mongos 节点，当您调整了实例中的 Mongos 节点数后，则需要在应用侧同步更新连接串。

