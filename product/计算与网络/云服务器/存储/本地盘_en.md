Local disk is a storage device located on the same physical server as the CVM instance and is featured by high read/write IO and low latency. Local disk comes from the local storage of the physical machine where the CVM resides. It is a storage area reserved on the physical machine where the CVM resides. It is advised to choose local disk for both system disk and data disk. In addition, in case of the purchase of a High IO model, only SSD local disk is recommended. However, a CVM for which local disk is selected DOES NOT support the upgrade of hardware (CPU, memory) and only supports upgrade of bandwidth.

## Lifecycle of local disk
Since the local disk can only be created following CVM instances,  it will be started and stopped with the life cycle of CVM.

## Types of local disks

The local disk is a local storage located on the physical machine where the CVM resides. By storage media, local disks are classified into local HDD and SSD local disk.

### Local HDD

The local HDD is a local storage located on the physical machine where the CVM instances reside. It is a part for storage separated from the physical machine where the CVM instances are located. You cannot upgrade hardware (CPU and memory) in CVM with local disk, except the bandwidth.


| Specifications | Performance | Price |
|---------|---------|---------|
| System disk: a fee-free capacity of 20 GB. You can choose to buy disks of a larger capacity. It supports a maximum of 50 GB (Linux)<br><br> A fee-free non-expandable capacity of 50 GB (Windows).<br><br> Data disk: the local HDD supports the capacity from 10 GB up to 1,000 GB (in 10 GB increments), and its maximum capacity to be selected varies with the specific hardware configuration.  | Reading and writing speed of more than 80 MB/S | Prepaid plan: 0.3 CNY/GB/month <br>Postpaid: 0.042 CNY/100 GB/hour |

### SSD local disk
The SSD local disk is a local storage located on the physical machine where the CVM resides, providing instances with block-level data access with low latency, high random IOPS, and high I/O throughput.

| Specifications | Performance | Price |
|---------|---------|---------|
| System disk:<br> a fee-free capacity of 20 GB (Linux)<br> A fee-free non-expandable capacity of 50 GB (Windows)<br><br> Data disk: the SSD local disk supports the capacity from 10 GB up to 250 GB (in 10 GB increments), and its maximum capacity to be selected varies with the specific hardware configuration.  | Throughput of up to 300 MB/s and 30,000 random IOPS| Prepaid plan: 0.8 yuan/GB/ <br>Postpaid: 0.33 CNY/100 GB/hour |

SSD local disk is suitable for the following scenarios:

- Low latency: the access latency in microseconds 
- Distributed application: NoSQL, MPP data warehouse, distributed file system and other I/O intensive applications. These applications have their own distributed data redundancy. 
- Logs for large online applications: large online applications can produce a large amount of log data and require high-performance storage, while the log data does not require highly reliable storage. 
- Single point of failure (SPOF) risks:  There are the potential SPOF risks. It is recommended to implement data redundancy at the application layer to ensure data availability.


## Purchasing local disks
Since the local disk can only be started together with the launch of CVM,  you can just specify the local disks when purchasing CVM instances. For more information, please refer to the [Purchase and Start an Instance](/doc/product/213/4855).

## Formatting, partitioning and creating a file system
As the Cloud Block Storage mounted to instances, the local disk is used by CVM instances as a hard disk. For formatting, partitioning and creating a file system, please refer to [Linux System Partitioning, Formatting, Mounting and File System Creation](https://cloud.tencent.com/doc/product/362/5448) and [Windows System Partitioning, Formatting and File System Creation](https://cloud.tencent.com/doc/product/362/5450) in product documents of Cloud Block Storage.
