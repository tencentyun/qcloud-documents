
## What is Big Data D1 instance?

Big Data D1 instances are CVM instances designed exclusively for Hadoop distributed computing, massive log processing, distributed file systems, large data warehouses and other business scenarios. This instance type is mainly used to deal with cloud computing and storage of massive business data in the age of big data.



## Which industry customers and business scenarios are Big Data D1 instances applicable to?

Big Data D1 instances are applicable to customers in the Internet, game, finance and other industries who require big data computing and storage analysis, as well as business scenarios where massive data storage and offline computing is performed. They can fully satisfy the requirements of distributed computing businesses represented by Hadoop for the storage performance, capacity and private network bandwidth of instances.
In addition, combining the highly available architecture design of distributed computing businesses represented by Hadoop, Big Data D1 instances adopt a local storage design to achieve a total cost of ownership close to that of offline IDC self-built Hadoop clusters based on massive storage space and high storage performance.

## Features of Big Data D1 instances


* The throughput of a single instance can reach up to 2.3 GB/sec. A throughput-intensive HDD local disk is optimal for throughput-intensive storage. Big Data D1 instances are designed exclusively for Hadoop distributed computing, massive log processing, large data warehouses and other business scenarios, providing stable and high sequential read/write throughput performance.
* Local storage has a unit price as low as 1/10. Big Data D1 instances have the best cost performance in big data scenarios, and can achieve a total cost of ownership close to that of IDC self-built Hadoop clusters based on massive storage space and high storage performance.
* Read/write time delay is minimized to 2-5 ms. Big Data D1 instances, as high-performance enterprise-level models, are defined for matured enterprise developers.
* Both prepaid and postpaid billing methods are available for Big Data D1 instances, with a price as low as 4.17 CNY/hour.

## Specifications of Big Data D1 instances

| Model | vCPU (core) | Memory (GB) | Local Data Disk | Private Network Bandwidth | Note |
|-------|----|------|------|------|------|
| D1.2XLARGE32  | 8  | 32  | 2 × 3,720 GB  |1.5 Gbps |-|
|D1.4XLARGE64  | 16  | 64 | 4× 3,720 GB| 3 Gbps |-|
| D1.6XLARGE96  | 24  | 96  | 6× 3,720 GB  | 4.5 Gbps | -|
| D1.8XLARGE128  | 32  | 128  | 8× 3,720 GB | 6 Gbps | -|
| D1.14XLARGE224  | 56  | 224  | 12× 3720 GB  | 10 Gbps | Exclusive for hosts |



## Notes on local data storage for Big Data D1 instances


Big Data D1 instances use local disks as data disks, which may lead to **a risk of data loss** (in case of host crash). If your application does not have a data reliability architecture, you are strongly recommended to choose instances with cloud disks used as data disks.

Operations on an instance coming with local disks and the data retention relationship are shown below.


| Operation | Status of Local Disk Data | Description |
|------|-----|-----|
| Restart operating system/Restart instance using console/Forced restart | Retained | Local disk storage is retained. Data is retained. |
| Shut down operating system/Shut down instance via the console/Forced shutdown | Retained | Local disk storage is retained. Data is retained. |
| Terminate (instance) on the console | Erased | Local disk storage is erased. No data is retained. |

> **Note**:
Do not store business data that needs to be kept for a long time on a local disk. Back up data in time and use a highly available architecture. For long-term retention, it is recommended to store the data on a cloud disk.

## How can I purchase Big Data D1 local disks?

Local disks cannot be purchased separately. You can only purchase local disks when creating a D1 instance. The number and capacity of local disks depend on the specifications of the instance you selected.

## Does the local storage of Big Data D1 instances support snapshots?
No.

## Do Big Data D1 instances support configuration upgrading/downgrading and failover?

Configuration adjustment is not supported.

Big Data D1 instances are massive data storage-based instances using local HDD as data disk. This instance type does not support failover of data disk (in case of host crash or local disk damage). To prevent data loss, you are recommended to use a redundancy policy, for example, a file system that supports redundancy and fault tolerance (such as HDFS, Mapr-FS). In addition, you're also advised to back up data to a more persistent storage system periodically, such as Tencent COS. For more information, please see [Cloud Object Storage](https://cloud.tencent.com/document/product/436).

After a local disk is damaged, you need to shut down the CVM instance before we can change the local disk. If the CVM instance has crashed, we will inform you and make repairs.


## In which regions can I purchase Big Data D1 instances?

The following availability zones are supported:

* Shanghai Zone 2
* Beijing Zone 2
* Guangzhou Zone 3

More regions and availability zones will be available soon.

## Why can't I find the data disks after purchasing a Big Data D1 instance?

The local disks of a Big Data D1 instance are not mounted automatically. You can mount them as needed.

## What is the difference between Big Data D1 instances and High IO I2 instances?

High IO I2 instances are CVM instances designed exclusively for business scenarios with low latency and high random IO, featuring ultra high IOPS performance. They are generally used for high-performance databases (relational database, NoSQL). Big Data D1 instances are CVM instances designed exclusively for business scenarios of high sequential read/write, low-cost massive data storage, featuring ultra high storage cost performance and properly configured private network bandwidth.

## How is the disk throughput performance of Big Data D1 instances?

Take D1.14XLARGE224 as an example, the sequential read/write throughput performance of the local disks of Big Data D1 instances is described as below:
 
* For a single disk, the sequential read/write speed is 190+ MB/sec (128 KB of block size and depth of 32).
* For 12 disks, the concurrent sequential read/write speed is 2.3+ GB/sec (128 KB of block size and depth of 32).

## What is the difference between the local disk of Big Data D1 instances and CBS?

[Cloud Block Storage (CBS)](https://cloud.tencent.com/document/product/362) provides a highly efficient and reliable storage device for CVM instances. As a customizable block storage device featured by high availability, high reliability and low cost, it can be used as a scalable standalone disk for CVMs. It provides data storage at data block level and employs a 3-copy distributed mechanism to ensure the data reliability for CVM, thus meeting the requirements of various application scenarios. The local disk of Big Data D1 instances is designed exclusively for business scenarios where high sequential read/write performance is required for local massive data sets, such as Hadoop distributed computing, large-scale concurrent computing, data warehouses.


