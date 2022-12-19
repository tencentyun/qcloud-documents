
## Pulsar 跨可用区部署

Pulsar 支持跨可用区部署，即在有 3 个或 3 个以上可用区的地域购买 Pulsar 集群时，可以最多选择 3 个可用区购买跨可用区实例。该实例分区副本会强制分布在各个可用区节点上，这种部署方式能够让您的实例在单个可用区不可用情况下仍能正常提供服务。

![](https://qcloudimg.tencent-cloud.cn/raw/c641db94fbacd0a1a8a2a12b927f6c71.jpg)

### 跨可用区部署原理

Pulsar 跨可用区容灾是通过机架感知原理实现，即将不同组件的服务节点部署到不同可用区的不同机架中，但本质还是一套 Pulsar 集群。

机架感知是 Ensemble Placement Policy 的一种，是 Bookkeeper Client 用来选择 Ensembles 的算法，选择的依据主要是依赖网络拓扑属性。

#### 如何选择 Bookie

在初始化部署 Bookie 集群时，Bookie 会向当前的 Zookeeper 注册一个临时的 zk-node，Bookkeeper Client 通过 Zookeeper （watcher）来发现 Bookie 列表。当 bookie 变更时（宕机），Ensemble Placement Policy 会通过 onClusterChanged(Set, Set) 接口被通知，然后重新构造新的网络拓扑，后续的操作，例如 newEnsemble 就会基于新的网络拓扑来生成。


#### NetworkTopology

网络拓扑用一个树状的分层结构来表示一个集群中的 Bookie 节点信息。一个 Bookie 集群可以由很多的 data center（region）组成。在一个 data center 内部包含了分布在不同 rack 上的机器，在树状结构中，叶子节点表示 bookie 信息。

- **示例1：**Region A 有三个 bookie， bk1 , bk2 and bk3 , 它们的网络位置是， /region-a/rack-1/bk1 , /region-a/rack-1/bk2 , /region-a/rack-2/bk3 , 网络拓扑结构就是如下所示：
```
         root
          |
      region-a
        /  \
  rack-1  rack-2
    /  \      \
 bk1  bk2     bk3

```
- **示例2：**Region A 和 Region B 有四个 bookie， bk1 , bk2 , bk3 and bk4 ，它们的网络位置是， region-a/rack-1/bk1 , /region-a/rack-1/bk2 , /region-b/rack-2/bk3 和 /region-b/rack-2/bk4 ，网络拓扑结构如下：
```

              root
            /      \
      region-a      region-b
        |              |  
     rack-1          rack-2
      /  \           /    \
   bk1  bk2         bk3   bk4

```

网络位置是通过 DNSToSwitchMapping 来解析的， DNSToSwitchMapping 会将域名或者 IP 解析到网络位置。网络位置一定是 /region/rack 格式， / 表示 root，region 表示 data center，rack 表示机架信息。

>?在 Pulsar 中实现的 DNSToSwitchMapping 是 BookieRackAffinityMapping，通过 ZK 保存 rack 信息，目前只实现了 rackaware 的能力。

## 使用说明

Pulsar 虚拟集群不支持跨可用区部署，目前仅支持独占集群，如需使用该功能，请 [联系我们](https://cloud.tencent.com/apply/p/cb20pyzvsrv)。

>?目前该功能公测中，暂不单独计费。
