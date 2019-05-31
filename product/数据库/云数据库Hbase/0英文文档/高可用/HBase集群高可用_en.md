HBase working in a fully distributed environment, 
1. The Master process is responsible for managing the load balancing of RegionServers cluster and resource allocation.
2. ZooKeeper is responsible for maintaining the cluster meta data and monitoring the cluster status to prevent single-point failure.
3. RegionServer is responsible for reading and writing the specific data blocks, and all the data of HBase is stored in the HDSF system.

After started, it will create the master node under the root path (which depends on the configuration file of HBase. The default is /HBase) of the distributed coordinator. If the node is successfully created, the current one is the active node, and the other nodes are in the standby state. When the node in active state is dead, it will cause the registered nodes invalidated due to the timeout with zookeeper link, while the other nodes will continue to preregister this node and become the new active node.

After the regionserver node crashes, the zookeeper node will perceive it and immediately notify master to implement the RS crash processing, and re-assign the region of crashed node to the new regionserver for hosting. Data security is guaranteed by HDFS, while the users can also set the security degree of data according to their own needs. It is recommended that the number of HDFS data backups is set to 3.

![](https://mc.qcloudimg.com/static/img/979187777e8588f01c48d6792c439484/hbase_ha.png)
