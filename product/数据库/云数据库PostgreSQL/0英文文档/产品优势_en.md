## 1. More Powerful Features
> **In recent years, PostgreSQL has become the first choice of commercial open-source relational database**

- PostgreSQL, which conforms to BSD protocol, can be used without any restrictions.
- It supports such languages as C, C++, Java, PHP, Python and Perl, making the development of your business easier and faster.
- PostgreSQL is the most similar open-source database to Oracle in terms of architecture, syntax, data types, etc.
- It is compatible with SQL standards: SQL2003, and supports the major features of SQL2011.
- In addition to the operator LIKE of traditional SQL, it also supports a new operator SIMILAR TO of SQL99 and POSIX-style regular expression:
- Various types of data: geometric, IP, XML, JSON, RANGE, array, etc.
- Complex type (custom data type) is supported.
- Complex multi-table JOIN query SQL is supported: JOIN algorithm supports has, join, merge join, etc.
- Window functions are supported, and can be changed to complex analytic functions in which they are contained.
- Function index, partial (line) index, custom index, and full-text index are supported.
- Multi-process architecture ensures high stability. Databases with massive access volume are supported for a single CVM.
- It has powerful and high-performance plug-ins. For example, PostGIS is a database extensive plug-in for geo-spatial data. It provides additional support for geography location object, allowing you to run location queries with SQL.
- It supports strong consistency of data at the commercial level. With synchronous replication, PostgreSQL guarantees zero data loss. Financial trading system can also use PostgreSQL.

## 2. Higher Performance
> **High-performance database suitable for OLAP and OLTP**

- PostgreSQL provides query optimizers comparable to commercial databases. It also supports common joining operations between multiple tables. (such as nested loop, hash join, sort merge join, etc.). For example, the performance of joining two tables, each with 100,000 rows, is 100 times faster than that of MySQL. With the capability of obtaining query results faster from more tables, you can make your analysis more accurate.
- Tencent Cloud hosts PostgreSQL databases on PCI-E SSD storage, with QPS as high as 230,000. Therefore, you can support more concurrent business requests with fewer databases.
- PostgreSQL supports a large number of performance profiles. You can view performance data such as the running SQL queries, current lock waits, table scan and index scan to help you quickly and accurately locate the performance problems.

## 3. Convenient Management

- Tencent Cloud allows you to enable a PostgreSQL instance and connect it to your applications within minutes without further configuration. PostgreSQL is configured with generic parameters by default. You can modify these parameters in the console's parameter settings in real-time. Therefore, you can improve the ops efficiency by skipping the hassle of complicated installation and configuration procedures.

## 4. Easy Monitoring
Key operation metrics of PostgreSQL are provided, including the performance monitoring data such as CPU utilization, storage utilization and disk I/O. You can view them in the console free of charge to quickly locate and solve problems. Customization of metric alarm thresholds frees you from monitoring the metrics 24/7. Instead, you can learn about the exceptions by email and SMS in real-time.

## 5. Superior Performance
Tencent Cloud improves the performance of built-in operators by optimizing the PostgreSQL kernel. With high-performance PCI-E SSD, Tencent Cloud provides QPS at least three times higher than SATA disks. By default, Tencent Cloud CDB for PostgreSQL uses "One Master, One Slave" architecture for deployment, and the synchronous replication is enabled, to protect your business from being interrupted and prevent problems such as data corruption and data loss.

## 6. More Protection
When a failure occurs in a node, the cluster scheduling system will immediately perform an automatic retry to recover the node. Data with severe problems can be recovered to a certain point of time where it is normal, to respond to situations such as upgrade failure and disaster recovery. By default, CBD provides multiple security protections for each database free of charge.

## 7. Extensibility
An instance can be upgraded to a desired specification with just one click in Tencent Cloud's console without extra operations. The upgraded instance will inherit the IPs and all the configurations of the original instance, and it is only disconnected for a second during the upgrade process instead of long downtime, to meet your business needs at any time in a flexible way. For future business development, PostgreSQL can support unlimited capacity that requires only relatively minor or even no modifications on your business, so that you can serve massive users without limitations.
