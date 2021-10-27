## 功能说明
ClickHouse 集群由 N ≥ 1 个节点构成，在集群中用户可以通过配置定义出N≥1个虚拟集群（Cluster），当虚拟集群（Cluster）节点数量或存储量发生变化时，可以使用数据迁移功能，均衡数据分布，提升集群资源利用率，支持下线模式和均衡模式两种模式。

## 应用场景
- 均衡模式是将迁出节点中的数据按平均原则分摊到迁入节点中，只迁移分区表，不迁移非分区表；适用于集群扩容或节点负载均衡场景。
- 下线模式是将迁出节点中的数据全部迁移到迁入节点中，分区表和非分区表全部迁移；适用于销毁节点或数据备份场景。

## 操作说明
登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中选择 CLICKHOUSE 集群，单击集群 **ID/名称**，进入集群详情页。
![](https://qcloudimg.tencent-cloud.cn/raw/0d31fc6d1d8113575c44c7eeb026e866.png)
在集群详情页中，单击**集群服务**，在 CLICKHOUSE 卡片中选择**操作 > 数据迁移**。
![](https://qcloudimg.tencent-cloud.cn/raw/20da9b76179a27a1cc7397b96d1495d5.png)
数据迁移步骤分为四步：
1. 选择 Cluster，并选择迁移类型，默认为“均衡模式”，每次迁移时只能选择一个 Cluster。
![](https://main.qcloudimg.com/raw/f2982450f56d4f176eac3a0f3bd53a85.png)
2. 单击**下一步：选择迁移节点**，设置数据迁移带宽上限值，系统默认推荐值200MB/S，可自定义调整。系统会默认勾选 Cluster 中所有节点列表，并自动标记迁出和迁入节点，可自行轻微调整设置，同一节点只能作为迁出节点或迁入节点，且同一个 Cluster 中必须包含迁出节点和迁入节点。
![](https://main.qcloudimg.com/raw/f77415bbb9cddf179ff1374c6ee3a75e.png)
3. 单击**下一步：选择迁移数据表**，系统拉取所有迁出节点中的表，默认数据总量由高到低排列，单页只展示10张表，默认勾选10张表，可能根据阈值以及包含不包含条件进行搜索查询。
 ![](https://main.qcloudimg.com/raw/1a2366ce9f1a4039ef24965f0773ea21.png)
4. 单击**下一步：信息确认**，确认最终迁移信息。
 ![](https://main.qcloudimg.com/raw/04d0834ff9eaf5a66ba53f91c5dec792.png)
>!
>- 均衡模式：只迁移分区表。
>- 下线模式：迁移分区表和非分区表。
