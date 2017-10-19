The CVM instance described below also refers to dedicated CVM.

Local disk is a storage device located on the same physical server as the CVM instance and features high read/write IO and low latency. It is a local storage reserved on the physical machine where the CVM resides in. You're recommended to choose local disk for both system disk and data disk. In addition, in case of the purchase of a High IO model, only local SSD disk is supported. For a CVM with local disk, you cannot upgrade hardware (CPU and memory), and can only upgrade bandwidth.

## Life Cycle of Local Disk
Local disk is created with the creation of CVM instance, so its life cycle is same as that of CVM.

## Local Disk Types

Local disk is a local storages on the physical machine where the CVM resides in, and can be classified into local HDD and SSD disks.

### Local HDD Disk

Local HDD disk is a local storage reserved on the physical machine where the CVM instance resides in. For a CVM with local HDD disk, you cannot upgrade hardware (CPU and memory), and can only upgrade bandwidth.


| Specification | Performance | Price |
| ---------------------------------------- | ---------- | ------------------------------------- |
| System disk: 20 GB is given for free. You can choose to buy a larger capacity. A maximum of 50 GB is supported (Linux).<br><br>50 GB is given for free and is unchangeable (Windows).<br><br>Data disk: The capacity ranging from 10 GB to 1000 GB (in 10 GB increments) is supported. The maximum capacity supported varies with the hardware configuration.  | IOPS is more than 80 MB/sec | Prepaid: 0.3 CNY/GB/month <br>Pay per use: 0.042 CNY/100 GB/hour |

### Local SSD Disk
Local SSD disk is a local storage on the physical machine where the CVM resides in. It provides instances with block-level data access capability with a low latency, high random IOPS, and high I/O throughput.

| Specification | Performance | Price |
| ---------------------------------------- | ---------------------------- | ------------------------------------ |
| System disk:<br> 20 GB is given for free (Linux)<br> 50GB is given for free and is unchangeable (Windows)<br><br> Data disk: A capacity ranging from 10 GB to 250 GB (in 10 GB increments) is supported. The maximum capacity supported varies with hardware configuration.  | A maximum of throughput 300 MB/sec and 30,000 random IOPS | Prepaid: 0.8 CNY/GB/month<br>Pay-per-use: 0.33 CNY/100 GB/hour |

Local SSD is suitable for the following scenarios:

- Low latency: Access latency within microseconds 
- Distributed application: NoSQL, MPP data warehouse, distributed file system and other I/O intensive applications. These applications themselves have distributed data redundancy. 
- Logs for large online applications: Large online applications can produce a large amount of log data, which requires high-performance storage but is less demanding in storage reliability. 
- Single point of failure (SPOF) risk: If SPOF risk exists, it is recommended to implement data redundancy at the application layer to ensure data availability.


## Purchase of Local Disk
Local disk can only be enabled with the enabling of CVM, which means you can specify a local disk only when purchasing a CVM instance. For more information about purchasing a CVM, please see [Purchase and Enable an Instance](/doc/product/213/4855).

## Formatting, Partitioning and File System Creation
Like a cloud disk mounted to an instance, the local disk is used by CVM instance as a hard disk. For more information on formatting, partitioning and file system creation, please see [Partitioning, Formatting, Mounting and File System Creation on Linux](https://cloud.tencent.com/doc/product/362/5448) and [Partitioning, Formatting and File System Creation on Windows](https://cloud.tencent.com/doc/product/362/5450) in Cloud Block Storage product documentation.

