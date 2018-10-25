## Product Architecture
The architecture diagram of Tencent Cloud MongoDB system is as follows:
![Architecture Diagram](https://mccdn.qcloud.com/static/img/65628226168a3cf8d89643e8aadaeda9/jiagou.png)


#### Tencent Cloud MongoDB system includes the following major modules:

## Access module: Tencent Gateway & firewall
It is used for the overall access of MongoDB, which primarily blocks IP/PORT changes, making them transparent to users and business logic, while isolates and controls unauthorized access
## Instance Module
In order to ensure high performance and high availability, Tencent Cloud MongoDB has no single-point deployed instance; instead, each instance is a replica set or a sharding cluster
## Access Module: Proxy Set
It is similar to mongos in the open source MongoDB component; the user can directly connect to the Proxy Set rather than connecting inside the replica set or the sharding cluster. The Proxy Set can provide consistent access for the replica set or the sharding cluster service, it is also partially responsible for reporting monitoring data and blocking sensitive operations.
## 	Management Control System: Master
It is the control center for the entire Tencent Cloud MongoDB cluster. It mainly manages the status and availability of each replica set or sharding cluster instance in the cluster, as well as providing functions such as migration, upgrade, backup, monitor, system deployment and so on
## Monitor System
It is mainly used to process monitoring data reported by each instance to analysis instance availability and reliability and push real-time alerts and e-mails to inform the status of Tencent Cloud MongoDB instance under the username to the corresponding user
## Backup System: Backup Center
It provides 7-day cold backup data and data rollback at any point of time within 5 days (see Rollback Feature Technical Principles for details about restrictions and conditions). Used to store Tencent Cloud MongoDB cluster cold backup data, the cold backup data for each instance is stored into 3 copies
## Log Center
It is used to store the detailed access log for each replica set or sharding cluster instance, which provides detailed log for detailed traceable issues.
## Flow Control System
It is used to provide sales and service activation features.
## Task Allocation System
It is used to allocate tasks when multiple users initiate sales or service activation operations.
## Console System
It is used to provide an entry for users to access instance control and instance monitoring feature, which displays information such as database status and specification.

