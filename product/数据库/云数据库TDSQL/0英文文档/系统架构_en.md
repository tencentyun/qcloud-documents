## 1. Overview of System Architecture
### 1.1 High Availability Architecture
The production system usually needs a high availability solution to ensure an uninterrupted operation of the system. Database is the core of system data storage and service, so the availability requirements for it is higher than that for computing service resources. Currently, a common high availability solution of databases is to make multiple databases work collaboratively. In this way, when one database fails, other databases can immediately replace it to continue the work, ensuring uninterrupted or shortly interrupted service. Another solution is to make multiple databases provide services simultaneously and allow users to access any database. In this way, when one database fails, users can immediately access another database.
To switch between multiple databases, the data recorded in them must be synced, so **data synchronization technology is the basis of the database high availability solution**. Currently, the data replication methods include the following:

- **Async replication**: When the application initiates an update (including add, delete and modify operations) request, the Master responds to the application immediately after completing the operation, and replicates the data asynchronously to the Slave. Therefore, under async replication, the unavailability of the Slave does not affect the operations on the Master database, while the unavailability of the Master may cause data inconsistencies.


- **Strongsync replication**: An application initiates a data update request. After completing the update operation, the Master replicates the data to the Slave. After receiving the data, the Slave returns success message to the Master. After receiving the message from the Slave the Master can return a response to the application. The Master replicates the data to a Slave synchronously, so the unavailability of the Slave can affect the operations on the Master, while the unavailability of the Master does not cause data inconsistencies.
> **Note: Under "strongsync" replication, if the self-built network of master database and slave database is interrupted or an error occurs to the slave database, the master database will be hung. At this point, if only one master database or one slave database is used, the high availability solution cannot be available. - Because under a single server, some data will lose completely if failure occurs, which does not meet the security requirements for financial level data.

- **Semisync replication**: Proposed by Google, semisync replication means the system uses strong sync replication in normal state, but if an exception occurs (the slave is unavailable or the network exception occurs between the two nodes) when the Master replicates data to the Slave, strong sync replication is degraded to async replication. When the system becomes normal, strong synchronous replication will be recovered. Under semisync replication, the unavailability of the Master may cause data inconsistencies in low probability.

### 1.2 Introductions to Common High Availability Architecture
- **Shared storage solution**: Use shared storage, such as SAN storage. The principle of SAN is that multiple database servers share the same storage area so that multiple databases can "read and write" the same data. When the master database fails, high-availability software from a third party mounts the file system on the slave database, and then starts the slave database to complete the switchover.


- **Log synchronization or stream replication synchronization**: The most common replication method of database. Take MySQL database an an example. When data are written to a MySQL database, MySQL Master Server transfers its Binary Log to the Slave via the replication thread. After receiving the log, the Slave writes the same data to the file system according to the Binary Log contents. Currently, MySQL provides:
  - Async replication: Ensure a rapid response structure, but cannot ensure that the binary log reaches the slave. Namely, async replication cannot guarantee data consistency.
  - Semisync replication: A synchronization plug provided by Google. It responds to customer's request relatively slow, and is downgraded to async replication during overtime and other situations. This means semisync replication can ensure data consistency basically rather than completely.


- **Trigger-based synchronization**: use triggers to record data changes and synchronize the changes to another database.


- **Middleware-based synchronization**: the system is connected to a middleware instead of the underlying databases. The middleware sends the database changes to multiple underlying databases for data synchronization. A few years ago, some software developers usually use such an architecture due to factors such as business needs, database performance and synchronization mechanism.



## 2. Introduction to CDB for MariaDB (TDSQL) Architecture
### 2.1 Multi-Thread Asynchronous Replication Technology (Strong Sync Replication) of CDB for MariaDB (TDSQL) 
In synchronization technology, developed are async replication and semisync replication and so on. The two technologies are designed for ordinary user groups, and can basically ensure data synchronization under the situation of lower user requirements, good network conditions and proper performance stress. However, async replication and semisync replication usually causes data inconsistencies, directly affecting system reliability, even leading to transaction data loss, and bringing direct or indirect economic losses.
With years of business accumulation, Tencent's internal team independently developed multi-thread asynchronous replication (MAR), and has advantages over Oracle's NDB engine, Percona XtraDB Cluster and MariaDB Galera Cluster in performance, efficiency and applicability. In short, MAR (strong synchronization) technology features the following

- Consistent sync replication, **ensuring strong consistency of data between nodes**.
- **Completely visible to the business level** so that the level needs no read and write separation or synchronization strengthening. 
- Asynchronize serial synchronization thread, and **introduce thread pool capacity**, greatly improving performance.
- Support **cluster** architecture.
- Support **automatic member control**, automatically removing faulty node from the cluster.
- Support **automatic node adding** without manual intervention.
- Each **node contains a complete data copy**, and can be switched at any time.
- **Shared storage device is not needed**.

With Tencent's MAR (strong synchronization) technology, the master can returns a transaction response to the application only after the slave synchronizes data, as shown below:
![](//mccdn.qcloud.com/static/img/aee81e2ae246bd8e08d83f37132d7684/image.png)

MAR technology excels other mainstream synchronization solutions in performance. When using the same test scheme for cross-availability zones (IDCs), we found that, in performance, MAR technology is about 5 times better than MySQL semisyncis, and 1.5 times than MariaDB Galera Cluster (sysbench standard case was used for the test).
![](//mccdn.qcloud.com/static/img/60b6e6b80ccccad6692f9d68d93d7a51/image.png)

### 2.2 Cluster Architecture of CDB for MariaDB (TDSQL)
CDB for MariaDB (TDSQL) uses a cluster architecture. An independent CDB for MariaDB (TDSQL) system consists of over 10 systems or components, with the architecture diagram as follows:
![](//mccdn.qcloud.com/img56834007cd44f.png)


The core modules of CDB for MariaDB (TDSQL) are: decision-making and scheduling cluster (Tschedule), database node group (SET) and access gateway cluster (TProxy). The interaction between them are completed through configuration cluster (TzooKeeper).
![](//mccdn.qcloud.com/img5683403e58125.png)


- **Database node group (SET)**: Consists of database engine compatible with MySQL, and monitoring and information collection module (Tagent). It uses the architecture of "one master node (Master), several slave nodes (Slave_n) and several remote slave nodes (Watcher_m )". Generally:
 - Database node group is deployed in the cross-rack and cross-data center server
 - Database node group monitors the cluster through the heartbeat monitoring and information collection module (Tagent) to ensure the robustness of the cluster.
 - Under distributed architecture, based on horizontal sharding, several shardings (database node group) provide a "logically unified, physically decentralized" distributed database instance.

- **Decision-making and scheduling cluster (Tschedule)**: The management and scheduling center of the cluster. It maintains the normal operation of the SET, and records and distributes global configuration of the database.
 - Operation scheduling cluster (MariaDB (TDSQL) Scheduler) helps DBAs or database users automatically schedule and run various operations, such as database backup, collection monitoring data, generate various reports or perform business processes. CDB for MariaDB (TDSQL) combines Schedule, Zookeeper, OSS (operations support system) to activate the specified resource plan through the time window, and fulfill various complex needs of the database in resource management and operation scheduling. Oralce also uses DBMS_SCHEDULER to support similar capabilities.
 - Program coordition and configuration cluster (TzooKeeper): It is provided by CDB for MariaDB (TDSQL) to configure maintenance, election decision-making and routing synchronization, and can support the creation, deletion and replacement of database node group (shardings). In addition, the cluster issues and schedules all DDL (data definition language) operations in a unified manner. The number of deployed TzooKeepers should equal 3 or larger.
 - Operations support system (OSS): A comprehensive business operations and management platform developed based on CDB for MariaDB (TDSQL). It integrates features of database management, organically combining network management, system management and monitoring services.
 - Decision-making and scheduling clusters are deployed independently in Tencent Cloud's three data centers in China (cross-data center deployment, remote disaster recovery).

- **Access gateway cluster (TProxy)**: Connect and manage SQL resolution and assign routing (TProxy is not Tencent Cloud gateway (TGW) ) at the network layer.
 - The number of access gateway cluster is the same as that of the deployed database engines, share the load and achieve disaster recovery.
 - Pull database node (sharding) status from the configuration cluster (TzooKeeper) and provide sharding routing to make read and write visible.
 - Record and monitor SQL execution information, analyze SQL execution efficiency, record and monitor user access information to authenticate security and block risky operations.
 - Tencent gateway system (TGW) is deployed at TProxy frontend to provide users with a unique virtual IP service.

This cluster architecture greatly simplifies the communication mechanism between the nodes and the needs for hardware. It means that even with a simple x86 server, you can build a stable and reliable database similar to the minicomputer, shared storage and so on.

### 2.2 High Availability of CDB for MariaDB (TDSQL)
#### 2.2.1 Physical High Availability
CDB for MariaDB (TDSQL) usually uses the architecture of dual nodes (one master and one slave)or triple nodes (one master and two slaves), depending on the instance configuration you purchase. Each node is installed on a physical machine with independent and cross-rack deployment to ensure that database services cannot be affected due to failure of a single device or rack network, or power outage.

#### 2.2.3 Network High Availability
The physical machine of each node of CDB for MariaDB (TDSQL) uses the configuration of dual network cards connected to dual-switches so that physical network is secure and reliable. In practice, TProxy frontend interfaces TGW. If a node in the set falis, TProxy switches DB routing in at least 200 ms. If the TProxy fails, TGW loads to other normal TProxy in 1 s. The switchover does not change the VIP (Virtual IP) to shield the impact of physical server changes.

#### 2.2.4 Backup and Recovery Services
**Backup service**: The backup module backs up (physically) CDB for MariaDB (TDSQL) and Binlogs. The backup files are uploaded to a distributed file cluster with higher-security level (HDFS). Generally, the backup is executed on the slave node to avoid the impact on services provided by the master node.

**Rcovery service**: Also known as rollback recovery. The recovery module recover the backup files in the HDFS to a temporary instance for your check or adjustment without affecting the master instance.

**Backup download**: You can dump and download files to a specified location, such as cheaper Tencent Cloud COS.

#### 2.2.4 2-region-3-DC

The deployment architecture of CDB for MariaDB (TDSQL) is 2-region-3-DC, under which the straight-line distance between nodes in the same city is over 10 KM, and between nodes in different cities is over 100km. It is achieved through high availability (HA) scheduling solution independently developed by Tencent. The diagram is as follows:
![](//mccdn.qcloud.com/img56834737b4b73.png)

