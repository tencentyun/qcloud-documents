![](//mc.qcloudimg.com/static/img/231de26d0bfb7c7fca1dfc93f8be51ec/image.png)

HTAP database TiDB cluster is divided into three components:

**TiDB Node**

TiDB is in charge of receiving SQL requests, processing SQL-related logic, and locating the TiKV address for storing and computing data through the PD, exchanging data with TiKV, and finally returning the result. 

The TiDB server is stateless. It doesn't store data and it is for computing only. It is horizontally scalable with no upper limit and provides the unified interface to the outside through the load balancing components such as Linux Virtual Server (LVS), HAProxy, or F5.


**PD Node**

Placement Driver (referred to as PD) is the managing component of the entire cluster and is in charge of the following three operations:


1. Storing the metadata of the cluster such as in which TiKV node a key is stored.
2. Scheduling and load balancing of TiKV cluster, such as data migration, Raft group leader migration, etc.
3. Allocating the transaction ID that is globally unique and monotonic increasing.



**TiKV Node**

TiKV is responsible for storing data. From an external view, TiKV is a distributed transactional Key-Value storage engine.

Region is the basic unit to store data. Each Region stores the data for a particular Key Range which is a left-closed and right-open interval from StartKey to EndKey. There are multiple Regions in each TiKV node. TiKV uses the Raft protocol for replication to ensure the data consistency and disaster recovery. The replicas of the same Region on different nodes compose a Raft Group. The load balancing of the data among different TiKV nodes are scheduled by PD. Region is also the basic unit for scheduling the load balance.


