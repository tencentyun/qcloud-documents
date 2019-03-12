### DynamoDB集群介绍
DynamoDB是一个支持文档和键值存储模型的基于表维度的且具有高可扩展性NoSQL数据库服务。腾讯云数据库团队在已有的NoSQL模块框架上，全新推出了一项高度兼容DynamoDB协议，且性能快速稳定，支持实例级别的备份和回档，自动容灾机制的数据库服务。如果您是DynamoDB开发爱好者，您无需改动太多的代码既可以通过DynamoDB协议来访问数据库。


### 创建DynamoDB集群
进入MongoDB[购买页](https://buy.cloud.tencent.com/mongodb?clusterType=1)，单击"分片集群"，在协议类型上选择"DynamoDB协议"。
由于底层也是通过将数据分布在多台物理机上来达到存储容量平滑扩展的目的。所以您还需要按需选择分片的片数，片内节点数，以及节点规格。每个分片都是多节点的副本集，片内多节点自动容灾，保证服务高可用。
![](https://main.qcloudimg.com/raw/4bfbc275b5fa4a5937690bb33ae5d89d.png)

### 管理控制台
在控制台中可以查看DynamoDB集群实例的详细信息，如节点的构成，节点的规格和已使用容量，同时也可以在控制台上进行实例的续费管理以及扩容等操作。
[![](https://mc.qcloudimg.com/static/img/c101b8878cb77a9e486ed5e34467a995/D.png)](https://mc.qcloudimg.com/static/img/c101b8878cb77a9e486ed5e34467a995/D.png)

### 扩容操作
目前DynamoDB集群的扩容方式只支持将所有节点进行统一扩容，暂不支持通过添加节点的方式进行扩容。在实例列表页单击的“扩容”按钮，选择需要扩到的容量规格，单击“升级”。
[![](https://mc.qcloudimg.com/static/img/eac99761afe97e60a18438f5ef196e14/kuo.png)](https://mc.qcloudimg.com/static/img/eac99761afe97e60a18438f5ef196e14/kuo.png)


### 备份和回档
目前只支持实例级别的备份和回档，在实例详情页单击“备份”按钮，输入备注信息后，单击"提交"进行实例备份。
[![](https://mc.qcloudimg.com/static/img/608e4ec72a25d7a265d07d2720c5d1ef/beifeng.png)](https://mc.qcloudimg.com/static/img/608e4ec72a25d7a265d07d2720c5d1ef/beifeng.png)
在回档操作过程中，需要输入需要回档到的日期，目前支持5日内的任意时间回档，但前提是只能选择两次备份之间的时间点进行回档，如果没有满足的备份请执行一次手动备份。
[![](https://mc.qcloudimg.com/static/img/b2ef79e419a89976c96743aa7e4f6085/huidang.png)](https://mc.qcloudimg.com/static/img/b2ef79e419a89976c96743aa7e4f6085/huidang.png)

### 实例监控
实例提供三个维度的监控指标，分别是实例维度，片维度以及节点维度来进行整个集群的数据监控。提供操作请求，容量使用，负载等多项指标的监控数据。
[![](https://mc.qcloudimg.com/static/img/98766957d1748618dad40f133c0b35d2/jiank2.png)](https://mc.qcloudimg.com/static/img/98766957d1748618dad40f133c0b35d2/jiank2.png)
