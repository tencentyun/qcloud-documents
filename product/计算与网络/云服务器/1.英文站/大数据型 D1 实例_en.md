
## What is big-data D1 instance?

Big-data D1 instance is a CVM instance designed exclusively for Hadoop distributed computing, massive log processing, distributed file systems, large data warehouses and other business scenarios. It is mainly used to solve the problems of cloud computing and storage of massive business data in the age of big data.



## Which industry customers and business scenarios is big-data D1 instance applicable to?

It is applicable to customers in the Internet, game, finance and other industries who require big data computing and storage analysis, as well as business scenarios where massive data storage and offline computing is performed. It can fully satisfy the requirement of distributed computing businesses represented by Hadoop for the storage performance, capacity and private network bandwidth of instances.
In addition, combining the highly available architecture design of distributed computing businesses represented by Hadoop, big-data D1 instance adopts a local storage design, so as to achieve a total cost of ownership close to that of an offline IDC self-built Hadoop cluster based on massive storage space and high storage performance.

## Features of big-data D1 instance


* A single instance has throughput performance up to 2.3 GB/sec. A throughput-intensive HDD local disk is the best choice for throughput-intensive storage. The big-data D1 instance is designed exclusively for Hadoop distributed computing, massive log processing, large data warehouses and other business scenarios, providing stable high sequential read/write throughput performance.
* Local storage has a unit price as low as 1/10. The big-data D1 instance has optimum cost performance in big data scenarios, and can achieve a total cost of ownership close to that of an IDC self-built Hadoop cluster based on massive storage space and high storage performance.
* Read/write time delay is as low as 2-5 ms. The big-data D1 instance is a high-performance enterprise-level model, defined for matured enterprise developers.
* The big-data D1 instance supports two billing methods: Prepaid and Prepaid, with a price as low as 4.17 CNY/hr.

## Specifications of big-data D1 instance

| Model | vCPU (core) | Memory (GB) | Local Data Disk | Private Network Bandwidth | Note |
|-------|----|------|------|------|------|
| D1.2XLARGE32 | 8 | 32 | 2 × 3720 GB | 1.5 Gbps | - |
| D1.4XLARGE64 | 16 | 64 | 4 × 3720 GB | 3 Gbps | - |
| D1.6XLARGE96 | 24 | 96 | 6 × 3720 GB | 4.5 Gbps | - |
| D1.8XLARGE128 | 32 | 128 | 8 × 3720 GB | 6 Gbps | - |
| D1.14XLARGE224 | 56 | 224 | 12× 3720 GB | 10 Gbps | Exclusive for host |



## Notes for big-data D1 local data storage


Big-data D1 instance uses local disk as its data disk, so there is a **risk of data loss** (for example, when host crashes). If your application does not have an architecture of data reliability, you are strongly recommended to use an instance which can use a CBS disk as its data disk.

Operations on an instance with a local disk and the data retention relationship are shown in the table below.


| Operation | Status of Local Disk Data | Description |
|------|-----|-----|
| Operating system restart/Console restart/Forced restart | Retained | Local disk storage is retained. Data is retained. |
| Operating system shutdown/Console shutdown/Forced shutdown | Retained | Local disk storage is retained. Data is retained. |
| Terminate (instance) on the console | Erased | Local disk storage is erased. No data is retained. |

> **Note**:
DO NO store business data that needs to be kept for a long time on the local disk. Back up data in time and use a highly available architecture. For long-term retention, it is recommended to store the data on a CBS disk.

## How to purchase big-data D1 local disks?

Local disks cannot be purchased separately. You can only purchase local disks when creating a D1 instance. The number and capacity of a local disk depend on the specifications of the instance you selected.

## Does the local storage of big-data D1 instance support snapshots?
No.

## Does big-data D1 instance support configuration upgrading/downgrading and failover?

It does not support configuration adjustment.

The big-data D1 instance is a massive data storage instance whose data disk is based on local HDD disk. It does not support failover of data disk (such as host crash, and local disk damage). To prevent data loss, you are recommended to use a redundancy policy, for example a file system that supports redundancy and fault tolerance (such as HDFS, Mapr-FS). In addition, you're also advised to back up data to a more persistent storage system periodically, such as Tencent COS. For more information, please see [Cloud Object Storage](https://cloud.tencent.com/document/product/436).

After the local disk is damaged, you need to shut down the CVM instance before we can change the local disk. If the CVM instance has crashed, we will inform you and make repairs.


## In which regions can I purchase big-data D1 instances?

The following availability zones are supported:

* Shanghai Zone 2
* Beijing Zone 2
* Guangzhou Zone 3

More regions and availability zones will be available soon.

## Why can't I find the data disk after purchasing the big-data D1 instance?

The local disk corresponding to the big-data D1 instance can not be mounted automatically. You can mount it as required.

## What is the difference between the big-data D1 instance and the high IO I2 instance?

High IO I2 instance is a CVM instance designed exclusively for business scenarios with low latency and high random IO. It has ultra high IOPS performance, and is generally used for high-performance databases (relational database, NoSQL). Big-data D1 instance is a CVM instance designed exclusively for business scenarios of high sequential read/write, low-cost massive data storage. It has ultra high storage cost performance and properly configured private network bandwidth.

## How is the disk throughput performance of big-data D1 instance?

The sequential read/write throughput performance of the local disk of big-data D1 instance is shown as follows (D1.14XLARGE224 is taken as an example):
 
* For a single disk, sequential read/write speed: 190+ MB/sec (block size is 128 KB, depth is 32).
* For 12 disks, concurrent sequential read/write speed: 2.3+ GB/sec (block size is 128 KB, depth is 32).

## What is the difference between the local disk of big-data D1 instance and CBS?

[Cloud Block Storage](https://cloud.tencent.com/document/product/362) provides a highly efficient and reliable storage device for CVM instances. It is a customizable block storage device with high availability, high reliability and low cost, and can be used as an independent scalable disk for CVM. It provides data storage at the data block level and employs a 3-copy distributed mechanism to ensure data reliability for CVM instances, thus meeting the requirements of various application scenarios. The local disk of big-data D1 instance is designed exclusively for business scenarios where high sequential read/write performance is required for local massive data sets, such as Hadoop distributed computing, large-scale concurrent computing, data warehouses.


