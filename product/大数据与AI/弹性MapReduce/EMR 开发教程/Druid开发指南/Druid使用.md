EMR 支持将 E-MapReduce Druid 集群作为单独的集群类型，主要基于以下几方面的考虑：
- 使用场景：E-MapReduce Druid 可以脱离 Hadoop 使用来适配不同的业务应用场景。
- 资源抢占：E-MapReduce Druid 对内存要求比较高，尤其是 Broker节点和 Historical 节点。E-MapReduce Druid 本身资源使用不受 Hadoop YARN 统一调度，运行时容易发生资源抢夺。
- 集群规模：Hadoop 作为基础设施，其规模一般较大，而 E-MapReduce Druid 集群可能相对较小，部署在同一集群上，由于规模不一致可能造成资源浪费，单独部署则更加灵活。

## 购买建议

在创建 EMR 集群时选择 Druid 集群类型即可。Druid 集群自带了Hadoop HDFS 和 YARN 服务，并已经和 Druid 集群完成集成。但是建议仅用于测试，**对于线上生产环境，强烈推荐您采用专门的 Hadoop 集群**。

如果需要关闭 Druid 集群自带的 Hadoop 相关服务，可以到 EMR 控制台 [组件管理](https://console.cloud.tencent.com/emr/static/component/) 中选择暂停对应的服务。

## Hadoop 和 Druid 集群连通配置

本节介绍如何配置 Hadoop 集群和 Druid 集群的连通性。如果您使用 Druid 集群自带的 Hadoop 集群（生产环境不推荐这么做），则无须做额外设置即可正常连通使用，可以跳过此节。

如果您需要将索引数据存放在另外一个单独的 Hadoop 集群的 HDFS 上（生产环境推荐这种方式），则首先需要设置两个集群的连通性。具体步骤如下：
1. 确保 Druid 集群和 Hadoop 集群能够正常通信。
两个集群在同一个 VPC 下，或两个集群在不同 VPC，但两个 VPC 之间能够正常通信（如通过云联网或者对等连接）。
2. 在 E-MapReduce Druid 集群的每个节点的`/usr/local/service/druid/conf/druid/_common`路径下，放置一份     Hadoop 集群中`/usr/local/service/hadoop/etc/hadoop`路径下的 core-site.xml、hdfs-site.xml、yarn-site.xml、mapred-site.xml 文件。
>!Druid 集群由于自带 Hadoop 集群，因此 Druid 路径下已经提前创建了上述文件的相关软链接，需要先删除，再拷贝另一个 Hadoop 集群的配置过来。同时需要确保文件权限正确，能被 hadoop 用户正常访问。
3. 在 Druid 配置管理中修改 common.runtime.properties 配置文件：
 - druid.storage.type：默认为 hdfs，无需修改
 - druid.storage.storageDirectory：
```
如果另一个 Hadoop 集群为非 HA：hdfs://{namenode_ip}:4007
如果另一个 Hadoop 集群为 HA：hdfs://HDFSXXXXX
请配置全路径，详细地址可以在目标 Hadoop 集群的 core-site.xml 文件的 fs.defaultFS 配置项里面找到。
```
保存配置并重启 Druid 集群相关服务。

## 使用 COS

E-MapReduce Druid 支持以 COS 作为 deep storage，本节介绍如何使用 COS 作为 Druid 集群的 deep storage。

首先您需要确保 Druid 集群和目标 Hadoop 均开启了 COS 服务，可以在购买 Druid 集群和 Hadoop 集群的时候开启，也可以购买后在 EMR 控制台进行后配置 COS。

在 Druid 配置管理中修改 common.runtime.properties 配置文件：
- druid.storage.type：仍然为 hdfs
- druid.storage.storageDirectory：`cosn://{bucket_name}/druid/segments`

可以到 COS 上预先创建并设置 segments 目录和权限。

保存配置并重启 Druid 集群相关服务。

## 调整 Druid 参数

E-MapReduce Druid 在创建集群后会自动生成一套配置，不过建议您根据业务需求调整最优内存配置。要调整配置，您可以在 EMR 控制台 [组件管理](https://console.cloud.tencent.com/emr/static/component) 页面上进行操作。

调整配置时，请确保调整正确：
```
MaxDirectMemorySize >= druid.processing.buffer.sizeByte *(druid.processing.numMergeBuffers + druid.processing.numThreads + 1) 
```
调整建议：
```
druid.processing.numMergeBuffers = max(2, druid.processing.numThreads / 4)
 
druid.processing.numThreads =  Number of cores - 1 (or 1)
 
druid.server.http.numThreads = max(10, (Number of cores * 17) / 16 + 2) + 30
```
更多配置请参考 [Druid 组件配置](https://druid.apache.org/docs/0.17.0/configuration/index.html#common-configurations) 文档。

## 扩展 Router 作为查询节点

当前 Druid 集群默认部署 Broker 进程在 EMR Master 节点上，由于 Master 节点部署较多进程，进程之间影响可能出现内存不够的情况，影响查询效率；同时许多业务也希望查询节点和中心节点分离部署。在这些情况下您可以在控制台扩容一到多个 Router 节点并选择安装 Broker 进程，可以方便的扩展 Druid 集群的查询节点。

## 访问 Web

统一通过 console 访问 Druid 集群，端口开在主节点的18888端口，可以自行配置公网 IP，在安全组中开通18888的端口并设置带宽后，即可通过`[http://{masterIp}:18888]()`访问。
