
## 1	Overview
### 1.1 Data Sharding
In the Internet architecture of high-performance concurrence, performance bottlenecks often appear in database servers, especially when the business scale (users) reach millions. At this point, reasonable data sharding at data level can effectively solve problems about database performance and scalability. Database sharding includes two methods: vertical sharding (by function) and horizontal sharding.

- **Vertical sharding** (by function) is closely related to the business and easy to implement. For example, on the e-commerce platforms including "Jingdong", data are split by function into member database, commodity database, transaction database, logistics database and so on. However, because the load and capacity of a single database server are limited, and is bound to become bottlenecks as the business develops, vertical sharding cannot completely solve the stress problems. A common solution is horizontal sharding.
![](//mccdn.qcloud.com/static/img/f893ec978e92c77fcf2001b28e55e93c/image.jpg)
- **Horizontal sharding** is to, based on a certain rule, distribute the data of a table to multiple physically independent database servers to form independent database "shardings". Multiple shardings constitute a logically complete database instance.
 ![](//mccdn.qcloud.com/static/img/04195cfdaff8aa285ca224a74da12a3a/image.jpg)
### 1.2 Sharding Rule
Relational database is based on a two-dimensional model. In data sharding, we usually need to find a sharding field (shardkey) to determine sharding dimension, and then define a rule to split the database. To find a proper rule, you need to comprehensively consider the business. Here are several common sharding rules:
1.	Based on chronological order. For example, year-based splitting, with 2015 a sharding and 2016 another sharding.
 - Advantages: Simple and clear, and easy to search.
 - Disadvantages: The server performance for hot data during current stage (2016) may be insufficient while for cold data storage is idle.
2. Perform the modulo operation based on the user ID, and distribute the specific range of the operated field to different databases.
 - Advantages: The performance is relatively balanced, and data of the same user are stored in one database.
 - Disadvantages: Data skew may occur. For example, in a commerce system, Jingdong has much more data than thousands of small business.
3. Perform the modulo operation based on primary key, and distribute the specific range of the operated field to different databases.
 - Advantages: The performance is relatively balanced. Data skew seldom occurs. Data with the same primary key are stored in one database.
 - Disadvantages: Data are randomly distributed. Some business logic may need to cross shardings to join, which cannot be directly supported.

In addition, the ways to manage the data source of shardings include:
1.	Client mode: The configuration in the business process module manages the data source of multiple shardings. Sharding read/write and data integration are performed within the business process.
2. Middleware proxy mode: Build a middleware proxy in the frontend of sharding databases. Multiple sharding databases at the backend are visible to the frontend applications.

## 2	DCDB for TDSQL
### 2.1 Automatic Horizontal Sharding (splitting databases and tables) 
DCDB for TDSQL is a distributed database that is deployed on Tencent Cloud's public cloud, is compatible with MySQL protocol and syntax, and supports automatic horizontal sharding. Distributed database means that a complete logical database table acquired by the business s is evenly distributed at the backend to multiple physical sharding nodes. Currently, DCDB for TDSQL uses a master/slave architecture by default, and provides complete solutions to disaster recovery, backup, recovery, monitoring, migration and so on. It is suitable for massive databases atTB or PB level.
DCDB for TDSQL dates from 2004 when Tencent's Internet value-added businesses began to surge, bringing great stress on the expansion of MySQL database capacity. Therefore, a mechanism of splitting database and table was introduced to solve the problem, meaning that, based on ShardKey, large tables were split into multiple sub-tables in advance, and then the sub-tables were distributed in different physical machine nodes. Today, the data stored in the backend of DCDB for TDSQL are huge. Take Midas as an example. The DCDB for TDSQL carries 10 billion accounts of Midas in various channels, with users close to 900 million and daily transaction amount over 1 billion CNY.

The reasons why DCDB for TDSQL can easily support massive business are as follows:
 - **Automatic splitting tables**: DCDB for TDSQL can split databases and tables automatically, and achieve on-demand capacity scaling in combination with the unified data scheduling mechanism. Because DCDB for TDSQL shields the details of database and table splitting inside through the gateway, ways to split data and route waiting requests are not important to developers. They only need to initiate shardkey, directly program based on the logic database tables, and focus on the achievement of business logic, greatly easing the program.


 - **Automatic disaster recovery switchover**: Any business with massive data storage, such as Internet of Things, big data or payment services, imposes high availability requirements on the backend storage database. A common solution is disaster recovery switchover, which requires business detection and coordination and manual intervention. It is complex and deep coupled with business process. Besides, data errors may occur during the switchover and need to be repaired manually after the business recovery, causing difficult OPS. Data nodes and gateways of DCDB for TDSQL achieve multi-node disaster recovery and automatically detect the operation status of an instance. When a master node is found to be unavailable, DCDB for TDSQL will automatically trigger the master/slave disaster recovery switchover to ensure high availability of the database during server failure, network failure, IDC failure and other disasters. This disaster recovery process is completely visible to the business and free from manual intervention, ensuring user experience and greatly simplifying OPS.


 - **Data High Consistency**: If you disallow data loss or error: Based on the original async replication and semisync replication of MySQL, multi-thread strongsync replication is created for DCDB for TDSQL to ensure that each transaction has at least two copies in the cluster before the user response is returned. Besides, through a series of switchover mechanisms, DCDB for TDSQL can prevent data loss or error when switchover occurs after node failure.


 - **Cluster management and automatic capacity expansion**: Peak requests of the business may surge by several or dozens of times for launched new features, marketing activities, and so on. Previously, DBAs need to know the trend of business in advance to manually expand capacity ahead of time. It is usually a complex process for most distributed databases and requires many manual operations that is prone to errors. DCDB for TDSQL achieves features at the cluster level, such as automatic deployment, auto scaling, automatic backup and recovery, timed data rollback and multi-dimensional monitoring. When capacity expansion is needed, DBAs only need to click button at the frontend to start the process, and the capacity can be expanded automatically. The cluster operation system of DCDB for TDSQL greatly improves the efficiency of DBAs while greatly reduces errors that may caused by manual operations.


### 2.2	Product Architecture
The basic architecture of a DCDB for TDSQL instance is as follows:
![](//mccdn.qcloud.com/static/img/d60581140d84202517f9c30dcad02b56/image.png)
**Data sharding**: Consist of database engine compatible with MySQL, and monitoring and information collection module (Tagent).
> Note: In the distributed database, each sharding is configured with two nodes (one master and one salve) by default. Each distributed database needs at least two shardings.

**Scheduling cluster**: the management and scheduling center of the cluster. It maintains the normal operation of the SET, records and distributes global configuration of the database.
**Access gateway cluster (TProxy)**: Connect and manage SQL resolution and assign routing at the network layer, meaning it can be considered as middleware of the open source distributed database.
> Note: In case that proxies become performance bottlenecks, the number of proxies of a distributed database usually equals that of shardings.

**Backup cluster**: The data backup cluster of Tencent Cloud's cloud database.
> Note: the distributed database backup is saved for 5 days by default and has two copies.


