## 1. Background Architecture
The architecture is as follows:
![](//mccdn.qcloud.com/static/img/514a1ae9a57038309bb75ac09fb606b7/image.png)
CDB for SQLServer is composed of a master SQLServer database and a mirror one, which are deployed cross frames, with each of them corresponding to a set of monitoring agents that monitor the database through heartbeat in real time. The independently deployed decision-making and scheduling cluster and configuration cluster, as the management and scheduling center of clusters, are responsible for managing the database node group, access gateway clusters and HDFS's normal operation. Hadoop Distributed File System (HDFS) offers disaster recovery service by providing cold backup data. Access gateway cluster provides a unique IP externally which remains unchanged upon switching of data node.

## 2. Database Mirroring
By default, CDB for SQLServer uses Database Mirroring scheme (high-availability replication scheme) to allow automatic failover in seconds
![](//mccdn.qcloud.com/static/img/b271b907acf9f9e40a65d289c51d1ad1/image.png)
and offer high reliability with no data loss.

## 3. Auto-recovery of Node upon Failure
CDB for SQLServer supports automatic rebuilding of database nodes. If a node fails, it will automatically recover/rebuild the faulty node within 1 hour. The node switching is visible to the service and the database access IP remains unchanged.
![](//mccdn.qcloud.com/static/img/a30d1011f9dc8646fd3a8eeae8c4cfb0/image.png)



