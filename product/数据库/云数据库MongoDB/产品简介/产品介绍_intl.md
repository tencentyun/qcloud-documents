## 1. About TencentDB for MongoDB 
TencentDB for MongoDB is a high-performance distributed data storage service created by Tencent Cloud based on MongoDB, the world's most promising open source NoSQL database.
It is 100% compatible with MongoDB protocol, and is highly compatible with DynamoDB protocol. It is suitable for non-relational database-oriented scenarios such as games, logistics, social networking, Internet of Things, and videos.
## 2. Key Features 
TencentDB for MongoDB has the following key features:
(1) High flexibility and scalability. The database provides replica set and sharding instances. For replica set instances, nodes can be expanded vertically. For sharding instances, nodes can be expanded vertically and shards can be expanded horizontally to meet the expansion requirements of services.
(2) Ultra-high performance. With super-large memory, new PCI-E SSD storage media and new generation storage engine, as well as the optimized Mongo kernel, it realizes a QPS of up to over 39,000 and can meet the requirements of massive and highly concurrent business scenarios.
(3) High system availability. With a distributed architecture (at least 1 Primary and 1 Secondary), the system can automatically detect failures and switch services to ensure the high availability of the cluster. Meanwhile, the system performs a physical backup every 7 days and an incremental backup each day. You can roll back data to any time within 7 days using the file backups.
(4) High data security. The isolation and high security of networks can be ensured via VPCs and security groups. Also, it provides the encrypted storage feature to ensure the high security of data at the storage layer, so the business is free of the data theft risk.
(5) Data can be migrated. Support migration of instances with public network IPs, self-built migration of CVMs, direct connect migration and database migration. The business can freely move the database.
(6) Read-only and remote disaster recovery. Provide read-only instances to meet the requirements of read/write separation in some business scenarios. Provide remote disaster recovery instances to quickly switch the service to the disaster recovery instance in case of a master instance failure to keep the service uninterrupted.

## 3. Product Architecture 
A Replica set instance has a similar architecture with a sharding instance, except that there is only one shard in a replica set instance. The following describes the components in the system architecture.<br>
- Access module: ProxySet
ProxySet can provide consistent access for the replica set or the sharding cluster service. It is also partially responsible for reporting monitoring data and blocking sensitive operations.
- Management Control System: Master
It is the control center for the entire MongoDB cluster. It mainly manages the status and availability of each replica set or sharding cluster instance in the cluster, as well as providing functions such as migration, upgrade, backup, monitor, system deployment and so on.
- Monitor System: monitorsystem
It is mainly used to process monitoring data reported by each instance to analysis instance availability and reliability and push real-time alerts and e-mails to inform the status of instance under the username to the corresponding user.
- Backup System: backupcenter
It is used to store cold backup data of database MongoDB cluster.
- Log Center: logcenter
It is used to store the detailed access log for each replica set or sharding cluster instance and provide detailed log for detailed traceable issues.
- Task Scheduling System
It is responsible for the scheduling of task processes such as the creation, upgrade, and termination of instances in the entire system.

### 3.1 Replica set architecture 
![](https://main.qcloudimg.com/raw/80aa3335bfe4dfe9a683508a99307662.png)

In the replica set architecture, the system automatically builds a "one master, two slaves" architecture. If the business expands, you can expand the computing or storage resources of each node.
### 3.2 Multipart architecture 
![](https://main.qcloudimg.com/raw/16e480d0c43ca93d7f98d7fb9e02183e.png)

In the sharding architecture, the system consists of multiple shards. If the business expands, the shards can be expanded indefinitely to support business scenarios of massive data.

