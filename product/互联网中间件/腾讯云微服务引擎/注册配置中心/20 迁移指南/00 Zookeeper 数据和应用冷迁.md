
## 适用场景

将业务应用从自建 Zookeeper 冷迁到 TSE Zookeeper，在迁移过程中，新部署的服务暂不可用，存量服务不受影响。

## 迁移步骤

### 步骤1：持久化数据迁移（若有）

#### 1. 创建包含事务日志和快照日志的压缩包
首先，对自建 Zookeeper 集群的所有节点执行以下命令： `echo srvr | nc [Zookeeper 节点 IP] [Zookeeper 节点端口，默认为2181] | grep Mode` 来获取自建 Zookeeper 集群 Leader 节点的 IP。   

然后，根据 Leader 节点的 `zoo.cfg` 配置获取其事务日志和快照日志所对应的存储路径。在 `zoo.cfg` 配置文件中，`dataDir` 表示快照日志对应的本地存储路径；`dataLogDir` 表示事务日志对应的本地存储路径。  

最后，根据 `dataDir` 和 `dataLogDir` 的文件路径，拷贝对应的事务日志和快照日志到同一个压缩包中，其中，快照日志文件名以 snapshot 开头，存储在 `dataDir/version-2` 路径下；事务日志文件名以 log 开头，存储在`dataLogDir/version-2`路径下。   

#### 2. 通过事务日志和快照日志完成数据迁移 

事务日志和快照日志的组合包含了 Zookeeper 节点数据的全部信息。通过日志文件，可以快速的将自建 Zookeeper 的数据迁移到 TSE Zookeeper 中。   

**本功能尚未对外开放，如有需要可 [提工单咨询](https://console.cloud.tencent.com/workorder/category)** 。

### 步骤2：新部署的业务应用使用 TSE Zookeeper

将新部署的业务应用使用 TSE Zookeeper，详情查看 [以 Spring cloud 应用为例](https://cloud.tencent.com/document/product/1364/59334)。

### 步骤3：新部署的业务应用上线

验证新部署的业务应用运行是否正常，若能够正常运行，则将请求切换到新部署的业务应用，并下线存量的业务应用。
