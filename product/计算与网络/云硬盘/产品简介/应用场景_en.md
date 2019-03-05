## Introduction on Applicable Scenarios for Different Types of Storage Devices
### SSD Local Disk Application Scenario
- Low latency: Access latency under microseconds

- Logs for large online applications: Large online applications can produce a large amount of log data which requires high-performance storage, while log data does not require the storage to be highly reliable

- Act as temporary read cache: Local SSD has excellent random read performance (4 KB/8 KB/16 KB random read) and is suitable to be used as read-only slave for relational databases such as mysql, oracle. Since the cost for using RAMs is still higher than using SSDs, a local SSD can also be used as the L2 cache of cache services such as redis, memcache.

- Single point of failure (SPOF) risks:  There are potential SPOF risks. It is recommended to implement data redundancy at the application layer to ensure data availability. It is recommended to use SSD cloud block storage for core business

### HDD Cloud Storage Application Scenario
- HDD cloud storage has low storage cost, and the same level of data persistency as SSD cloud block storage. It can be used as cold data backup and archive, with a maximum capacity of 16 TB for a single disk 
- It is suitable for scenarios that involve sequential reading and writing of large files, such as journal log, stream media service and data storage. It can satisfy the demands for offline analysis of massive data calculated in TBs under hadoop framework
- It is not suitable for OLTP core business 

### High Performance Cloud Block Storage Application Scenario

- Suitable for 90% of the I/O scenarios. Best choice if you want a storage with both high quality and lost cost
- Suitable for medium to small sized databases, web servers and so on. Can provide long-term and stable IO performance 
- It can satisfy the IO demands for testing core businesses and developing integrated testing environment 


### SSD Cloud Block Storage Application Scenario
- High performance, high data reliability:  SSD cloud block storage utilizes best-in-class NVMe solid state storage as disk media. It is suitable for I/O intensive businesses and can provide long-term, ultra-excellent single disk performance
- Medium and large database: able to support medium and large relational database applications such as MySQL, Oracle, SQL Server, MongoDB which have table with millions of rows 
- Core business system: I/O-intensive applications and other core business systems with high data reliability requirements 
- Big data analysis:  Provides distributed processing capabilities for data calculated in TB or PB, suitable for data analysis, digging, business intelligence and other fields

## Typical Application Scenarios for Cloud Block Storage
### Delocalization
- **Data storage with high performance and high reliability**: Supports virtual machine hot migration with much efficiency, to prevent business interruption caused by physical failures ahead of time; Provides three copies of redundant data and complete data backup, snapshot capabilities as well as able to recover data within seconds; Suitable for critical core business systems with high load.
- **Elastic scaling**: Cloud disks can be mounted or unmounted flexibly within the region, without the need to shut down/reboot the server; the capacity of cloud storage can be configured in an elastic manner, and upgraded as required; up to 10 cloud disks can be mounted on a single virtual machine, with a capacity of up to 40 TB
![](//mccdn.qcloud.com/static/img/b6611d7eb39538f8376c2ed32ac58a5e/image.png)

### Analyze Massive Data
For the typical Spark-HDFS offline data analysis framework, RDD read/write, shuffle write towards disks all are sequential IO operations (only shuffle read IO is random IO), 95% of the IO read/write operations are sequential IO operations. CBS has excellent multi-thread concurrent throughput performance and supports offline data processing of TBs/PBs of data under Hadoop-Mapreduce, HDFS, Spark.
With multi-disk concurrency, a single HDFS cluster can achieve a throughput performance of 1 GB/sec.
Large enterprises such as xiaohongshu.com, ztgame.com, ele.me, yohobuy.com, weipiao.com have already launched big data practices (for example, data analysis, digging, commercial intelligence and so on) on CBS.
![](//mccdn.qcloud.com/static/img/fcd7c911ceec7205a36562dcf5f5288a/image.png)
**Deployment environment**: 5 servers (12 Core 40 GB RAM), each mounted with a 1 TB SSD cloud disk and a 1 TB HDD cloud disk, to simulate offline data analysis
**Test performance**: For 1.5 TB data, 5 HDD cloud disks can provide a read speed of 500 MB/sec, the data is read into RAM in 50 minutes, while SSD cloud disks will finish this process in 25 minutes!

### Core Database
SSD cloud disks are suitable for scenarios where both high I/O performance and high data reliability are required. It is especially suitable for core business systems such as medium and large relational database applications (like PostgreSQL, MySQL, Oracle, SQL Server) and I/O intensive services which require high data reliability, as well as medium to large scale developing/testing environments that require high data reliability.
CBS-SSD Cloud Block Storage holds both data reliability and high performance with perfection. The service has been providing reliable supports for large enterprises such as Heroes Evolved, Wendao, yohobuy.com, weipiao.com, xiaohongshu.com, etc.

![](//mccdn.qcloud.com/static/img/9867c8f2376fdf5d0878ca44159d6b66/image.png)
**Deployment environment**: Mount 800 G SSD cloud disks onto 4 virtual machines (Core 8 GB RAM) and deploy Mysql version 5.5.42.
**Test performance**: We simulate OLTP performance test using sysbench, with a test set of 10 million records. In this test, TPS reached 1616, QPS reached 29,000, which means a single disk is enough to support concurrent transactions performed by more than 10 thousand people per second!

