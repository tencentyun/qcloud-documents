### 分片集群介绍
腾讯云数据库MongoDB目前已经支持分片功能，分片集群将数据按照片键分布存储在多台物理机上，平滑的扩展能力，非常适用于TB或PB级的数据存储场景。同时分片集群支持实例级别的备份和回档来保证数据高可靠。每个分片内采用多节点自动容灾的机制，保证服务高可用。您可以使用腾讯云MongoDB分片功能便捷高效的搭建海量分布式存储系统。


### 创建分片集群
进入MongoDB[购买页](https://buy.cloud.tencent.com/mongodb?clusterType=1)，单击"分片集群"，按需选择分片的片数，片内节点数，以及节点规格。每个分片都是多节点的副本集，片内多节点自动容灾，保证服务高可用。
[![](https://mc.qcloudimg.com/static/img/6fb80892b40e93cbcc19cb43d2d70b80/goumaiye.png)](https://mc.qcloudimg.com/static/img/6fb80892b40e93cbcc19cb43d2d70b80/goumaiye.png)

### 分片集群控制台
在控制台中可以查看分片集群实例的详细信息，如分片的构成，片节点的规格和已使用容量，同时也可以在控制台上进行实例的续费管理以及扩容等操作。
[![](https://mc.qcloudimg.com/static/img/6cabd8fbb7652a85648fe454b243d365/k2.png)](https://mc.qcloudimg.com/static/img/6cabd8fbb7652a85648fe454b243d365/k2.png)

### 分片集群扩容
目前云数据库MongoDB分片集群的扩容方式只支持将所有节点进行统一扩容，暂不支持通过添加节点的方式进行扩容。在实例列表页单击的“扩容”按钮，选择需要扩到的容量规格，单击“升级”。
[![](https://mc.qcloudimg.com/static/img/e723c37c10c076c03e2836dbdeec7b80/%7BADB18884-AB90-4475-B309-83F334A26A1E%7D.png)](https://mc.qcloudimg.com/static/img/e723c37c10c076c03e2836dbdeec7b80/%7BADB18884-AB90-4475-B309-83F334A26A1E%7D.png)


### 备份和回档
分片集群实例的备份回档和副本集实例的备份回档操作相同，目前只支持实例级别的备份和回档，在实例详情页单击“备份”按钮，输入备注信息后，单击"提交"进行实例备份。
[![](https://mc.qcloudimg.com/static/img/608e4ec72a25d7a265d07d2720c5d1ef/beifeng.png)](https://mc.qcloudimg.com/static/img/608e4ec72a25d7a265d07d2720c5d1ef/beifeng.png)
在回档操作过程中，需要输入需要回档到的日期，目前支持5日内的任意时间回档，但前提是只能选择两次备份（成功且非oplog写满状态）之间的时间点进行回档，如果没有满足的备份请执行一次手动备份。
[![](https://mc.qcloudimg.com/static/img/b2ef79e419a89976c96743aa7e4f6085/huidang.png)](https://mc.qcloudimg.com/static/img/b2ef79e419a89976c96743aa7e4f6085/huidang.png)

### 集群实例监控
云数据库MongoDB分片集群实例提供三个维度的监控指标，分别是实例维度，片维度以及节点维度来进行整个集群的数据监控。提供操作请求，容量使用，负载等多项指标的监控数据。
[![](https://mc.qcloudimg.com/static/img/98766957d1748618dad40f133c0b35d2/jiank2.png)](https://mc.qcloudimg.com/static/img/98766957d1748618dad40f133c0b35d2/jiank2.png)
