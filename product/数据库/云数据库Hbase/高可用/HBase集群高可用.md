HBase 在完全分布式环境下
1.Master 进程负责管理 RegionServers 集群的负载均衡以及资源分配
2.ZooKeeper 负责集群元数据的维护并且监控集群的状态以防止单点故障
3.RegionServer 会负责具体数据块的读写，HBase 所有的数据存储在 HDSF 系统上

启动后会去分布式协调器的根路径（依赖于 hbase 的配置文件默认为/hbase）下创建 master 节点如果创建成功则当前节点为 active 节点，其余节点为 standby 状态，当 active 状态的节点死掉的时候会因为和 zookeeper 链接超时导致注册的节点失效而其他节点会继续抢注该节点而成为新的 active 节点。

对于 regionserver 节点宕机后 zookeeper 节点会感知到立刻通知 master 进行 RS宕机处理把宕机节点的 region 重新指派给新的 regionserver 进行托管，数据安全性是由 HDFS 来保证真的，同时用户也可以根据自己的需要来设定数据的安全程度，建议 HDFS 数据备份数为 3

![](https://mc.qcloudimg.com/static/img/979187777e8588f01c48d6792c439484/hbase_ha.png)
