
## 适用场景

将业务应用从自建 Zookeeper 冷迁到 TSE Zookeeper，在迁移过程中，新部署的业务应用不提供服务。

## 迁移步骤

### 持久化数据迁移（若有）

#### 步骤1：创建包含事务日志和快照日志的压缩包
首先，对自建Zookeeper集群的所有节点执行以下命令： `echo srvr | nc [Zookeeper节点IP] [Zookeeper节点端口，默认为2181] | grep Mode` 来获取自建Zookeeper集群Leader节点的ip。   

然后，根据Leader节点的 `zoo.cfg` 配置获取其事务日志和快照日志所对应的存储路径。在 `zoo.cfg` 配置文件中，`dataDir` 表示快照日志对应的本地存储路径；`dataLogDir` 表示事务日志对应的本地存储路径。  

最后，根据 `dataDir` 和 `dataLogDir`的文件路径，拷贝对应的事务日志和快照日志到同一个压缩包中，其中，快照日志文件名以snapshot开头，存储在 `dataDir/version-2` 路径下；事务日志文件名以log开头，存储在`dataLogDir/version-2`路径下。   

#### 步骤2：通过事务日志和快照日志完成数据迁移 

事务日志和快照日志的组合包含了Zookeeper节点数据的全部信息。通过日志文件，可以快速的将自建Zookeeper的数据迁移到TSE Zookeeper中。   

**本功能尚未对外开放，如有需要可 [提工单咨询](https://console.cloud.tencent.com/workorder/category)** 。

### 新部署的业务应用接入

将新部署的业务应用接入到 TSE Zookeeper，暂时不对外提供服务。

### 新部署的业务应用上线

验证新部署的业务应用运行是否正常，若能够正常运行，则将请求切换到新部署的业务应用，并下线存量的业务应用。
