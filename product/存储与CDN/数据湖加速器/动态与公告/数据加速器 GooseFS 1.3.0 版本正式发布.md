为了满足云上数据湖存储对安全、高性能的要求，腾讯云存储团队正式发布数据加速器 GooseFS 1.3.0 版本。该版本总结并收敛了 GooseFS 在过往大规模生产环境实践中遇到的性能、稳定性和安全问题，全面提升产品稳定性。

## 重要更新点一：支持 Kerberos 认证

Kerberos 用于非安全网络中，对个人通信以安全的手段进行身份认证。软件设计上采用客户端/服务器结构，并且能够进行相互认证，即客户端和服务器端均可对对方进行身份认证。可以用于防窃听、防重放攻击、保护数据完整性等场合，是一种应用对称密钥体制进行密钥管理的系统。目前 Kerberos 已经在大数据、AI 场景下被广泛应用于集群和文件系统之间的身份认证。

GooseFS 在本次更新中支持了 Kerberos 认证，支持将集群节点和用户访问接入 Kerberos 认证服务中，提供更安全的访问。GooseFS 支持 Kerberos 认证的基本框架如下：

![Kerberos认证服务架构](https://qcloudimg.tencent-cloud.cn/raw/f3fa3d97e385d113faf053cb989edef7.png)

GooseFS 集成 Kerberos 认证的主要优势点如下：
1. 可以保障 GooseFS 集群中的数据访问安全。
2. 与 HDFS 接入 Kerberos 的认证架构和流程基本一致，在 HDFS 上启用了 Kerberos 认证流程的应用可以很容易地迁移到 GooseFS。
3. 支持 Hadoop 的 Delegation Token 认证机制，因此可以很好地兼容 Hadoop 生态的应用作业。

如果需要了解 GooseFS 接入 Kerberos 的详细配置说明，可参见 [GooseFS 接入 Kerberos 认证](https://cloud.tencent.com/document/product/1424/76450)。


## 重要更新点二：支持通过原生 POSIX 语义访问对象存储服务

对象存储服务通过 [元数据加速能力](https://cloud.tencent.com/document/product/436/56971) 提供了原生的 POSIX 语义接口，支持用户通过文件系统语义访问对象存储服务，提供原生的元数据操作能力。系统设计指标可以达到 Gb 级单链接带宽、10万级 QPS 以及 ms 级延迟。启用元数据加速功能后，可以提升集群对元数据的操作性能，例如 List、Rename 等操作，可以广泛应用于大数据、高性能计算、机器学习、AI 等场景。

GooseFS 在本次更新中集成了最新版本的 COSN interface（COSN 8.14版本），支持了原生 POSIX 语义访问对象存储服务。整体的读写流程框架如下：

![](https://qcloudimg.tencent-cloud.cn/raw/99e322492b183c88c06b553dbb1fbc9b.png)

通过本次更新版本 GooseFS 以原生 POSIX 语义访问对象存储服务的主要步骤如下：
1. 确保您的存储桶已经开启元数据加速服务能力，元数据加速能力只能在创建存储桶时开启。
2. 安装最新版本的 GooseFS 客户端和服务端安装包。
3. 安装完成后，在 `core-site.properties`文件中修改访问协议的配置，就可以通过原生的 POSIX 协议访问指定存储桶。

如果您需要了解更详细的操作步骤，可参见 [数据加速器 GooseFS 最佳实践文档](https://cloud.tencent.com/document/product/1424/70963)。

## 重要更新点三：缓存淘汰能力优化

缓存淘汰能力是 GooseFS 为计算业务提供实时热数据的关键特性。在本次更新中，GooseFS 服务针对缓存淘汰能力提供了两项重点优化。
1. 提供了元数据清理工具
元数据一般存储在 GooseFS Master 节点。在生产环境中，随着时间推移，线上元数据的数据量必然越来越大，但 Master 节点的存储容量始终有限，增长的元数据最终会导致 OOM。因此 GooseFS 在本次更新中提供了一个元数据清理工具，可以基于 `inode`的`expiretime`检索出过期的文件元数据并执行清理动作。
元数据的操作流程如下：
 1. 从 Master 节点提供的`Journal`目录中提取`Journal`信息，并将其回放成`InodeStore`。
 2. 检索`FileInode`进行过期检查，对过期`Inode`进行删除操作。
 3. 检索`DirectoryInode`进行过期检查，对过期`Inode`进行删除操作。
2. Master 节点提供了 LRU 淘汰策略
默认淘汰策略下， GooseFS Master 节点中的元数据增大时，`concurrentHashMap`遍历一个`segment`的时间变长，淘汰的数据会越来越热，进而陷入缓存频繁置入置出的陷阱。在这种陷阱下，会出现缓存命中率下滑和缓存淘汰率增加的情况，进而影响 GC 性能，导致 GC 无法回收的情况。

因此，本次更新提供了基于 LRU 的淘汰策略。在该淘汰策略下，元数据缓存逃出频繁置换陷阱，能够提升缓存命中率，减少缓存淘汰速率，同时 GC 操作恢复正常，进一步减缓了元数据占用的内存增速。

## 其他更新点

除了上述更新之外，我们在本次版本中优化了 GooseFS 的产品性能，进一步提升 GooseFS 在大数据、AI 场景下的性能表现。主要更新点如下：

1. GooseFS Master 节点优化了锁瓶颈问题，显著提升 Master QPS，带来35%左右的性能优化效果。
2. GooseFS Worker 节点支持并发 Format，提升操作性能。
3. GooseFS Fuse 客户端支持覆盖写操作。
4. GooseFS Fuse 客户端优化了`ls`命令的内存占用问题。
5. GooseFS HDFS 客户端优化 ListNamespace 的性能。

同时，GooseFS 1.3.0 版本还修复了若干问题，其中存在潜在稳定性风险的重要修复点如下：

1. 修复了 RocksDB 泄漏和 Core 的问题，避免内存泄露。
2. 修复了 Zookeeper Curator 误打日志的问题。
3. 修复了 UFS 读带宽不准的问题。
4. 修复了 DistributedLoad 的时候由于日志打印过多导致的 LostWorker问题。

如果您想了解数据加速器 GooseFS 的更多信息，或者上手使用 GooseFS ，请参见 [数据加速器 GooseFS 产品文档](https://cloud.tencent.com/document/product/1424)。
