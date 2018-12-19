<table cellspacing ="10" >
<tr><td width = 70 align = center><a href ="#1F">A-E</a> </td><td width = 70 align = center><a href ="#2F">F-N</td><td width = 70 align = center><a href ="#3F">O-Q</a></td><td width = 70 align = center><a href ="#4F">R-Z</a></td></tr>
</table>
## A-E
<a name = "1F"></href> 
**Vertical Split**
A database consists of many tables, and each table corresponds to a different business. Vertical split is to classify tables according to business functions and distribute them to different databases.
**Single Table**
Single table is used to store tables that do not need sharding. All data of this table is stored in the first physical shard, and all tables of this type are placed in the first physical shard, with exact the same syntax and usage methods as MySQL. You can consider it as a non-distributed table.
**DCDB**
Tencent Distributed Cloud Database.
**DDL**
Data Definition Language, with the main commands of CREATE, ALTER and DROP.
**DML**
Data Manipulation Language, with the commands of SELECT, UPDATE, INSERT and DELETE.
## F-N
<a name = "2F"></href> 
**Sharding**
A physical-logic instance consisting of database engines, which contains a master node, several slave nodes, and some remote slave nodes.
**Table Split**
Table split means that the original table with enormous amount of data needs to be split to multiple database nodes, so that each physical shard carries some of the data and all the physical shards provide the complete data.
**Broadcast Table**
Broadcast table works as the broadcast feature of a small table. If a table is set as broadcast table, all operations made to this table will be broadcast to all physical shards, and each shard possesses all data of the table.
**Node**
It is a physical device carrying shards. A node can be a physical machine, a virtual machine or a small cluster.
**MariaDB**
MariaDB is one of the most important services of MySQL. Compared to MySQL, MariaDB has a better performance in extensions, storage engine and new feature enhancements. Now, DCDB supports MariaDB 10.1 (compatible with MySQL 5.6).
**MySQL**
MySQL is one of the most popular relational database management systems, using the most commonly used standardized language for database accessing.
## O-Q
<a name = "3F"></href> 
**OLTP**
On-Line Transaction Processing, as the main application of traditional relational database, is mainly used to process basic and daily transactions, such as bank transactions.
**OLAP**
As the main application of data warehouse systems, On-Line Analytical Processing supports complex analysis operations, focuses on decision support, and provides intuitive query results.
**Percona**
Percona is fully compatible with MySQL protocol and has a significant improvement in feature and performance over MySQL. Now, DCDB supports Percona 5.7.
**Proxy**
With Tproxy, DCDB achieves automatic databases and tables splitting, manages the underlying physical database instances and provides a unique service port that is compatible with MySQL database.
**Strongsync**
Strongsync is a MySQL-based multi-thread asynchronous strongsync replication program.
**Unique Global Digital Sequence**
Unique Global Digital Sequence is "sequence" for short, using the unsigned long type of 8 bytes. Now, DCDB can guarantee the global uniqueness and orderly increment of this field, but not the continuity.
## R-Z
<a name = "4F"></href> 
**Shard**
It is a physical database instance. A logical instance that is visible to users is composed of multiple physical instances.
**Shard Key**
DCDB splits tables through shard key modulo program.
**Horizontal Split** 
According to certain rules, the data of a table is split across multiple physically independent database servers to form a "separate" database "shard". Multiple shards together form a logically complete database instance.
**TDSQL**
It's the project code for Tencent's self-developed distributed database.
