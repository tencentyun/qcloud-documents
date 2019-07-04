## 1. Introduction
DCDB is a distributed database deployed on Tencent Cloud's public cloud that features a share nothing architecture that allows automatic horizontal split. With distributed database, a logic database table is acquired as a whole and then at backend, is evenly split into multiple shards and distributed to multiple physical nodes. Currently, DCDB is deployed with a master/slave architecture by default and provides a complete set of solutions covering disaster recovery, backup, restoration, monitoring, migration, and so on. It is suitable for TB-level or PB-level massive database scenarios. 

It now supports MariaDB and Percona engines (formerly known as TDSQL). More engines will be available soon.



## 2. Background
### 2.1 Differences between OLTP and OLAP
| Features | OLTP | OLAP |
|:--:|:--:|:--:|
| **Main Scenario** | Daily transaction processing | Statistics, statements, analysis |
| **Applications** | Designed for real-time transactions, such as e-commerce transactions and orders | Designed for statistical analysis, such as ERP, BI, etc. |
| **Consumption** | Disk IO | CPU |
| **Real-timeness** | High requirement for real-time read/write | Low requirement for real-time read/write |

> **DCDB is an OLTP-oriented distributed database.**

### 2.2 Vertical Split and Horizontal Split
**Vertical Split** is about split by features in a straightforward way and is closely linked with business areas. For example, the data of e-commerce platforms like "JD.com" is split based on features into membership database, commodity database, transaction database, logistics database, etc.

![](https://mccdn.qcloud.com/static/img/f893ec978e92c77fcf2001b28e55e93c/image.jpg)

Sometimes vertical split cannot completely solve the problem of high load because of the limited load capacity of a single database server. With the growth business, this will inevitably cause a bottleneck. A common solution to this problem is horizontal split. **Horizontal Split** is about spreading the data of a single table among multiple physically independent database servers based on a rule. "Sharding" is implemented on the "independent" databases, with multiple shards forming a database instance with complete logic.
![](https://mccdn.qcloud.com/static/img/04195cfdaff8aa285ca224a74da12a3a/image.jpg)

> **DCDB is a distributed database that supports horizontal partition.**

### 2.3 Shard Nothing architecture

Share nothing architecture allows expanding the data and access capacity by simply stacking machines. Despite the fact it meets the database capacity requirement of most users, it is based on minicomputer plus shared storage in essence with a ceiling on capacity and performance and is rather expensive. This is shown below:
![](https://mc.qcloudimg.com/static/img/60bbbcd57ec258375c109ced2bc4a8c1/shardnothing.png)

> **DCDB is based on a Share Nothing architecture and minimizes the users' awareness of details of distributed environment through automatic split technology.**

### 2.4 Data split method (sharding rules)
Relational database is a two-dimensional model where data split involves specifying a **shardkey** to determine the split dimension and defining split rules.

**Common options of shardkey**

- Based on order of dates. For example, for split by year, 2015 and 2016 represent two individual shards respectively.
	- Advantages: Simplicity and ease of search
	- Disadvantages: Server's storage may be insufficient for storing current year's (2016) hot data, but is idle for cold data.
	
- Perform a modulo operation on user IDs, and distribute the specific ranges of the results to different databases.
	- Advantages: Relatively balanced performance; data of a single user is stored in the same database.
	- Disadvantages: It may cause data skew (in case of a merchant system, a JD.com merchant may have much more data than thousands of small merchants).
	
- Perform a modulo operation on primary key, and distribute specific ranges of the results to different databases.
	- Advantages: Relatively balanced performance; low possibility of data skew; the data of a single primary key is stored in the same database;
	- Disadvantages: The need of joining some business logics across shards due to randomly dispersed data.

**Before using the solution of multi-table sharding, you can consider the following solutions:**

- Noshard: No sharding is performed;
- tableshard: Table sharding is performed based on user needs, regardless of relationship between tables, and the shardkey can be selected arbitrarily.
- Groupshard: Several tables associated with each other are grouped by the same shardkey to aggregate the similar data on a single physical node.

**Two modes are available now in data source management after sharding:**

- Client mode: The data sources of multiple shards are managed by the business application module, with read/write operations of shards and data integration implemented within the business application.
- Middleware proxy mode: Set up a middleware proxy at the frontend of sharded databases, with multiple sharded databases at backend being transparent to the front-end application.


> **Currently, DCDB is mainly based on automatic horizontal split, in which a modulo operation is performed on shardkey and the specific ranges of results are distributed to different databases through proxy gateway - TProxy.**

## 3.What problems can DCDB solve?

### 3.1 Bottleneck of a stand-alone database

The limitation of hardware and software of a stand-along database causes a bottleneck in its performance including storage capacity, access capacity and disaster recovery, making it unable to cater to the rapidly growing Internet businesses with a million-level user base.

Even if the server is upgraded to dozens of CPU cores with tens of TB capacity, a significant performance decline may be seen in DDL and DML. Moreover, with the rapid growth of business, there is a possibility that a high-end device you just bought several months ago needs a replacement due to its limited performance.

### 3.2 A lot of development work is needed for sharding at application layer

The high coupling between business logic and database logic in sharding at application layer brings a heavy development workload to the fast iteration of business. With DCDB's transparent automatic split solution, developers only need to modify the code upon the first access, without the need to care about the database logic in subsequent iterations. This can greatly reduce the development workload.


### 3.3 How to solve the problems of open-source solution or NoSQL

Open-source or NOSQL products indeed can solve database bottleneck, and these products are free or less expensive. However, before using these products, you need to consider the following questions:

(1) The bug fixes of a product depend on the progress of community. Can you wait if you encounter a big bug?
(2) Is there any person in your team who is familiar with the product and can continuously maintain it without affecting the project in case of a personnel change?
(3) Has the associated system been made ready?
(4) What business do you focus on? Does your KPI system involve inputting resources to ensure the open-source product's resource & life cycle management, distributed logic, high-availability deployment and switching, disaster recovery & backup, self-service OPS, troubleshooting, etc..

