### Sharding cluster introduction
TencentDB for MongoDB provides sharding clusters to distributively store data in multiple physical machines according to sharding keys. The clusters have smooth scalability and are very suitable for scenarios where TBs or PBs of data is stored. In addition, sharding cluster supports instance-level backup and data rollback, to ensure high data reliability. Multi-node automatic disaster recovery mechanism is used in each shard to ensure high service availability. You can leverage the sharding feature of Tencent Cloud MongoDB to build a massive distributed storage system easily and efficiently.


### Creating sharding cluster
Enter MongoDB [Purchase Page](https://buy.cloud.tencent.com/mongodb?clusterType=1), click **Sharding Cluster**, and select the number of shards, the number of nodes in each shard, and node specification, according to your needs. Each shard is a replica set containing multiple nodes. Multi-node automatic disaster recovery mechanism is used in each shard to ensure high service availability.
[![](https://mc.qcloudimg.com/static/img/6fb80892b40e93cbcc19cb43d2d70b80/goumaiye.png)](https://mc.qcloudimg.com/static/img/6fb80892b40e93cbcc19cb43d2d70b80/goumaiye.png)

### Sharding cluster console
In the console, you can view detailed information of the sharding cluster instance, such as the composition of the shard, the specifications of the shard node and occupied capacity, as well as perform operations including instance renewal management and scaling up.
[![](https://mc.qcloudimg.com/static/img/6cabd8fbb7652a85648fe454b243d365/k2.png)](https://mc.qcloudimg.com/static/img/6cabd8fbb7652a85648fe454b243d365/k2.png)

### Sharding cluster expansion
You can only expand MongoDB sharding cluster by expanding all nodes. Expanding by adding nodes is not supported. Click the **Expand** button on the instance list page, select the target capacity you wish to expand to and click **Upgrade**.
[![](https://mc.qcloudimg.com/static/img/e723c37c10c076c03e2836dbdeec7b80/%7BADB18884-AB90-4475-B309-83F334A26A1E%7D.png)](https://mc.qcloudimg.com/static/img/e723c37c10c076c03e2836dbdeec7b80/%7BADB18884-AB90-4475-B309-83F334A26A1E%7D.png)


### Backup and Rollback
Backup and rollback operations in sharding cluster instances are the same with that in replica set instances. You can only back up and roll back data at the instance level. Click the **Back Up** button in the instance details page and enter remarks, and then click **Submit** to commence instance backup.
[![](https://mc.qcloudimg.com/static/img/608e4ec72a25d7a265d07d2720c5d1ef/beifeng.png)](https://mc.qcloudimg.com/static/img/608e4ec72a25d7a265d07d2720c5d1ef/beifeng.png)
During rollback operation, you need to enter the date to which the data is to be rolled back to. Currently, you can enter any time point within the past 5 days, but you can only select a time between two backups (successful backup and oplog is not fully occupied). If there is no backup to satisfy this condition, please perform a manual backup.
[![](https://mc.qcloudimg.com/static/img/b2ef79e419a89976c96743aa7e4f6085/huidang.png)](https://mc.qcloudimg.com/static/img/b2ef79e419a89976c96743aa7e4f6085/huidang.png)

### Cluster instance monitoring
Monitoring metrics of three dimensions are provided to monitor data in the entire Cloud Database MongoDB sharding cluster: the instance dimension, the shard dimension and the node dimension. Monitoring data of multiple metrics will be provided, such as operation requests, capacity usage, load, etc.
[![](https://mc.qcloudimg.com/static/img/98766957d1748618dad40f133c0b35d2/jiank2.png)](https://mc.qcloudimg.com/static/img/98766957d1748618dad40f133c0b35d2/jiank2.png)

