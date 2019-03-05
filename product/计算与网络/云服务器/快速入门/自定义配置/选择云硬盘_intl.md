To meet the needs of different customers in different application scenarios, Tencent Cloud provides the following recommendations for selecting a cloud disk:

### Local SSD Application Scenario
- Low latency: Access latency within microseconds.

- Logs for large online applications: Large online applications produce a large amount of log data, which require high-performance storage with less demand on storage reliability.

- Acts as temporary read cache: Local SSD has excellent random read performance (4 KB/8 KB/16 KB random read) and is suitable for read-only slaves for relational databases such as MySQL and Oracle. Since the cost for using memories is still higher than using SSDs, a local SSD can also be used as the secondary cache of cache services such as Redis and Memcache.

- Single point of failure (SPOF) risk: If SPOF risk exists, it is recommended to implement data redundancy at the application layer to ensure data availability. It is recommended to use SSD cloud storage for core business.

### HDD Cloud Storage Application Scenario
- HDD cloud storage has low storage cost, and the same level of data persistency as SSD cloud storage. It can be used as cold data backup and archive, with a maximum capacity of 16 TB for a single disk.
- It is suitable for scenarios that involve sequential reading and writing of large files, such as journal log, stream media service and data storage. It can satisfy the demands for offline analysis of massive data calculated in TBs under Hadoop framework.
- It is not suitable for OLTP core business.

### Premium Cloud Storage Application Scenario

- It is applicable to 90% of the I/O scenarios with the highest possible quality under the lowest possible prices
- It is suitable for medium to small sized databases, web servers and so on, and provides consistent I/O performance
- It meets the I/O demands for testing core businesses and developing integrated testing environments.


### SSD Cloud Storage Application Scenario
- High performance and high data reliability: SSD cloud storage utilizes best-in-class NVMe solid state storage as the disk media. It is suitable for I/O-intensive businesses and can provide long-term and ultra-excellent single disk performance.
- Medium and large databases: Supports medium and large relational database applications containing tables with millions of rows, such as MySQL, Oracle, SQL Server, and MongoDB. 
- Core business systems: I/O-intensive applications and other core business systems with high data reliability requirements. 
- Big data analysis: Supports distributed processing of TB/PB-level data for applications such as data analysis, data mining, and business intelligence.


For more application scenarios, please see [Cloud Storage Application Scenarios](https://cloud.tencent.com/document/product/362/3065).




