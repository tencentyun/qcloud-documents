## 1. Introduction
Tencent Cloud CDB for MariaDB (TDSQL) is a highly secure enterprise-level cloud database under the OLTP scenario and has been serving Tencent's billing business for more than 10 years. [CDB for MariaDB (TDSQL) is compatible with MySQL syntaxes](https://cloud.tencent.com/document/product/237/6988). With advanced features such as thread pool, auditing, cross-region disaster recovery, TDSQL is expandable, simple and cost-efficient.

## Development History

CDB for MariaDB (TDSQL) has been developed for over 10 years, from a project to a service launched in Tencent Cloud:

- **In 2002**, Tencent database team began to modify MySQL based on ISP business;

- **In 2004**, Tencent's Internet value-added businesses began to surge, bringing great stress on the expansion of MySQL database capacity. Therefore, a mechanism of splitting database and table was introduced to solve the problem, meaning that, based on ShardKey, large tables were split into multiple sub-tables in advance, and then the sub-tables were distributed in different physical machine nodes; 

- **In 2008**, Tencent's various businesses such as games, QQ zone and TenPay surged again, bringing higher failure rate (such as hardware failure, operating system failure, and application or service failure). However, under the traditional async replication, some data between the master and slave were inconsistent, causing problems after master/slave switchover and bringing user complaints and economic losses to Tencent. With the principle of putting data consistency first, Tencent database team developed strongsync (MAR) technology after using multiple programs such as asynchronizing synchronization thread, island detection, blacklist and multi-level switchover. In addition, after years of development, the system could automatically achieve capacity expansion, fault detection, switchover and recovery.

-  **In 2010**, Internet payment business was popular and was required to feature ultra-high availability and concurrence, and extremely quick response. Based on that, Tencent started HOLD project to independently develop a distributed data storage layer featuring ultra-high concurrence, ultra-short latency and high consistency. Finally, HOLD project succeeded, and achieved main technologies of CDB for MariaDB (TDSQL), including cross-data center strongsync, remote disaster recovery, switchover consistency, automatic data sharding, auto scaling and automatic cluster management, which are introduced in other documents.

-   **In 2012**, Tencent's internal team officially named this uneasily developed product TDSQL. Considering cloud would be widely used in the future, Tencent started a project aiming to be compatible with MySQL engine, and selected MariaDB as a kernel. In the following two years, CDB for MariaDB (TDSQL) helped Tencent to launch multiple businesses such as Midas and WeBank. Besides, based on the data relationship model in bank scenario, Tencent designed a data aggregation with close relationship, and expanded the cross-node distributed architecture to the stand-alone architecture, effectively covering multi-level users.

-   **In 2015**, CDB for MariaDB (TDSQL) officially went online in Tencent Cloud.
![](//mccdn.qcloud.com/static/img/dc286f4282a5d487955ed89cef93ba69/image.png)

## 3. Kernel Instruction
CDB for MariaDB (TDSQL) kernel is based on **MariaDB 10.X**. For the specific version, please see specific instance instructions.

## 4. Distributed Architecture
Please see the Distributed Cloud Database (DCDB) for details.
