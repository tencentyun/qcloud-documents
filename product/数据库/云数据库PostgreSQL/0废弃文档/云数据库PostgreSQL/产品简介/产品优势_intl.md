## 1. More Powerful
> **Over the past few years, PostgreSQL has become the preferred open source relational database for businesses**

- Follows the BSD protocol, which means there are no restrictions on using PostgreSQL.
- Supports most of the programming languages such as C, C++, Java, PHP, Python and Perl, thus making the development of your business applications easier and faster.
- PostgreSQL is the closest open source database to Oracle in terms of architecture, syntax and data types.
- It is compatible with SQL standard "SQL 2003", and supports the main features of SQL 2011.
- In addition to the traditional SQL LIKE operator, it also supports the new SIMILAR TO operator of SQL 99 and POSIX-style regular expressions.
- Rich data types: geometry, network address, XML, JSON, RANGE, Array, etc.
- Supports complex types (custom data types).
- Supports complex multi-table join SQL query, and join algorithms are supported such as hash join, merge join, etc.
- Supports window functions or complex analytic functions as the latter ones include window functions.
- Supports function index, partial (row) index, custom index and full-text index.
- Thanks to its multi-process architecture, it is more stable, and a high-throughput database can be implemented on a single machine.
- Includes powerful, high-performance built-in plug-ins, such as PostGIS, which is a database extension for geo-spatial data and provides additional support for geography location objects, allowing you to run location queries with SQL.
- Has strong data consistency required for commercial use. With synchronous replication, PostgreSQL guarantees zero data loss, and even suitable for financial trading systems.

## 2. High Performance
> **High-performance database for use cases of OLAP and OLTP**

- Provides query optimizers comparable to commercial databases. It also supports common multi-table join query (such as nested loop, hash join, sort merge join, etc.). For example, the performance of joining two tables, each with 100,000 rows, is 100 times faster than that of MySQL. With the capability of obtaining query results faster from more tables, you can make your analysis more accurate.
- Built on PCI-E SSD storage, with QPS as high as 230,000. You can support more concurrent business requests with fewer databases.
- Supports a large number of performance profiles. You can view performance data such as the running SQL queries, current lock waits, table scan and index scan to help you quickly and accurately locate the performance problems.

## 3. Easy to Administer

- Tencent Cloud allows you to start and connect to a PostgreSQL instance in just few minutes without further configuration. It is configured with common parameters by default which can be modified in real time in the console. This helps you eliminate the hassle of complicated installation and configuration tasks and improve your OPS efficiency.

## 4. Easy Monitoring
Tencent Cloud provides key operation metrics for PostgreSQL, including CPU utilization, storage utilization, I/O activity, and other performance monitoring data. You can view them in the console free of charge to quickly locate and solve problems. You can customize alarm thresholds for these metrics, which keeps you updated on any exceptions by email or SMS, without you having to monitor them all the time.

## 5. Superior Performance
Tencent Cloud improves the performance of built-in operators by optimizing the PostgreSQL kernel, and provides QPS configuration at least three times higher than SATA through the disk configured with super high performance PCI-E SSD. TencentDB for PostgreSQL uses "One Master and One Slave" architecture for deployment by default. Synchronous replication is enabled by default, protecting your business from being interrupted and prevent problems such as data corruption and data loss.

## 6. More Reliable
After a node failure, the recovery of the node will be immediately retried by cluster scheduling. When there is a serious problem with your data, you can quickly recover the node to a normal point in time to deal with upgrade failures, disaster recovery, etc. By default, TencentDB comes with multiple security protections for each database.

## 7. Scalable
You can upgrade your instance to a desired specification with just one click in Tencent Cloud's console without extra operations. The upgraded instance inherits the IPs and all the configurations from the original instance, and there is only a 1-second disconnection during the upgrade process instead of long downtime, to meet your business needs at any time in a flexible way. When the existing PostgreSQL cannot support your business development, you can support massive customer again with only a few changes or even no changes to your business, without capacity limitation and performance bottleneck.

