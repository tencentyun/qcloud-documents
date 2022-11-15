## 功能介绍
HDFS 联邦管理是基于 HDFS  Federation 特性提供的 HDFS 联邦集群部署管理能力，包含 NameService 管理以及挂载表管理。在 Hadoop 集群类型 HA 模式下支持联邦管理，支持 ViewFS Federation 和 Router-based Federation 两种联邦类型选择，联邦类型选择后不可更改。Router 节点会用于新扩展的 NameNode 部署，用作 NameNode 部署后的 Router 节点不支持销毁和节点维度所有角色启停。

>!
1. 当前 HDFS 联邦管理为白名单开放，如需要可[联系工单](https://console.cloud.tencent.com/workorder/category)开通。
2. EMR 所有产品版本均支持 ViewFs Federation 联邦类型；因 HDFS-2.9.0及以上支持 Router-based Federation 联邦类型，所以 EMR 仅 EMR-V3.x.x 及以上产品版本支持 Router-based Federation 联邦类型, EMR-V2.x.x 系列不支持。
3. 在角色管理页中，将联邦节点 NameNode 角色进程暂停时，会影响集群的扩容操作，需恢复 NameNode 角色进程后再执行扩容。
4. 添加联邦后，各组 NameNode 上的 fs.defaultFS 的配置会不同。当选择集群维度对 HDFS的 core-site.xml 文件进行配置下发操作时，会造成各组 NameNode 上的 fs.defaultFS 的值被覆盖，所以配置下发时，不要选择集群维度；其它配置文件不影响。

## 操作步骤

1.  登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的**集群 ID/名称**进入**集群详情页**。
2. 在集群详情页中单击**集群服务**，然后选择 **HDFS 组件右上角操作>联邦管理**，即可进入联邦管理页面。
![](https://qcloudimg.tencent-cloud.cn/raw/ef49976e0481e8adfd0627fb9fc3c21d.png)

3. 单击添加 NameService 即可进行 HDFS 联邦新建，需要输入 NameService 名称，选择联邦类型、NameNode 节点、DFSRouter 节点（Router-based Federation 选择）等。
![](https://qcloudimg.tencent-cloud.cn/raw/fcd0556538b8a2a7b261934d43da93ba.png)
4.选择**添加联邦节点**
联邦节点采用集群中的 Router 节点，需先在资源管理页中扩容增加 Router 节点后，再将其设置为联邦节点；NameNode 进程需要选择2个节点，每个节点将会部署 NameNode 进程和 ZKFC 进程。
第一次新建联邦类型 Router-based Federation 时，部署 DFSRouter 进程需要选择至少2个节点；当再次新建联邦时 DFSRouter 节点可复用，节点数量可大于等于0。
![](https://qcloudimg.tencent-cloud.cn/raw/9eb8f157f648ceb82f7a0c9ec7cdee94.png)

>!
1. HDFS-3.3.0以下的版本，在**非首次**新增 NameService 成功后且联邦类型为 Router-based Federation 时，需在角色管理页重启历史的 DFSRouter 进程（为保证业务正常建议在业务低峰期执行）；HDFS-3.3.0版本及以上支持了热加载配置，无需此操作。
2. 开启了 Kerberos 的集群，添加联邦 NameService 后，提交到 yarn 的任务如要用到新 NameService 上的文件，需要先重启 yarn 的 ResourceManager（为保证业务正常建议在业务低峰期执行）。
3. 设置 NameService 名称后，不可修改也可以删除且 NameService 名称不能为"nsfed"、“haclusterX”、”ClusterX“等系统关键词。

5. 添加挂载表
当新增 NameService 成功后，才能添加挂载表。为了避免配置复杂度过高，对当前集群目录进行映射，建议仅全局一级目录进行NameService 映射，例如挂载“/tmp”，“/user”，“/srv”等；可批量添加挂载路径。
	- 路径：在 ViewFs 统一命名空间的路径名称，在 Router-based Federation 统一命名空间的路径名称，也称挂载点。
	- 目标NameService：挂载点映射到真实路径对应的 NameService。
	- 目标路径：在对应 NameService 上的真实路径，与全局路径的名字无需保持一致。
![](https://qcloudimg.tencent-cloud.cn/raw/9b0643a9432c73a9cf3d577bc78437e5.png)

>!
1. 路径指向：
1）登录 NameNode 节点，执行 hdfs dfs -ls /指向的是这个 NameNode 所管理的 namespace 下的路径，对于 ViewFs 联邦需要用 hdfs dfs -ls ViewFs://ClusterX/ 才会指向全局路径，对于 Router-based 联邦需要用 hdfs dfs -ls hdfs://nsfed/ 才会指向全局路径。
2）登录其它节点，例如充当客户端的Router节点，hdfs dfs -ls / 指向的是全局路径。
2.	各业务组件数据放在一级目录之下，不支持直接放在根目录下访问，根目录不支持挂载。
3.	默认的 NameService 上是有/emr 目录，需要挂载。


