To meet the needs of different customers in different application scenarios, Tencent Cloud provides the following recommendations for selecting a cloud disk:

### Local SSD Application Scenario
- Low latency: Access latency within microseconds.

- Logs for large online applications: Large online applications produce a large amount of log data, which require high-performance storage with less demand on storage reliability.

- Act as temporary read cache: Local SSD has excellent random read performance (4 KB/8 KB/16 KB random read) and is suitable to be used as read-only slave for relational databases such as mysql, oracle. Since the cost for using RAMs is still higher than using SSDs, a local SSD can also be used as the L2 cache of cache services such as redis, memcache.

- Single point of failure (SPOF) risk: If SPOF risk exists, it is recommended to implement data redundancy at the application layer to ensure data availability. SSD cloud storage should be used for core business.

### HDD Cloud Storage Application Scenario
- HDD cloud storage has a low storage cost, and the same level of data persistency as SSD cloud storage. It can be used as cold data backup and archive, with a maximum capacity of 16 TB for a single disk.
- It is suitable for the scenarios where sequential read/write of large files is needed, such as logs, streaming media, data storage, etc. It can satisfy the demands for offline analysis of massive data calculated in TB under hadoop framework.
- It is not suitable for OLTP core business.

### Premium Cloud Storage Application Scenario

- It is applicable to 90% of the I/O scenarios and is a best choice if you want a storage with both high quality and low cost.
- It is suitable for medium to small sized databases, web servers and so on, and provides consistent IO performance.
- It meets the IO demands for testing core businesses and developing joint testing environment.


### SSD Cloud Storage Application Scenario
- High performance, high data reliability: SSD cloud storage utilizes best-in-class NVMe solid state storage as disk media. It is suitable for I/O-intensive businesses and can provide long-term, ultra-excellent single disk performance.
- Medium and large database: Support medium and large relational database applications such as MySQL, Oracle, SQL Server, MongoDB with table containing millions of rows. 
- Core business system: I/O-intensive applications and other core business systems demanding high data reliability. 
- Big data analysis: It supports distributed processing of TB/PB-level data, and is suitable for data analysis, mining, business intelligence and other fields.


For more application scenarios, please see [Cloud Storage Application Scenarios](https://cloud.tencent.com/document/product/362/3065).




