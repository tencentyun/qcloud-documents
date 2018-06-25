## Features

### CFS Features

#### Integrated management

- CFS provides a standard POSIX and file system access syntax (such as strong data consistency and file locking). You can mount CFS to Tencent Cloud CVM instances using mount commands for standard operating systems and NFS v3.0/v4.0 protocol.
- The CFS console allows you to quickly create and configure file systems while minimizing the workload of deploying and maintaining the file system.

#### Automatic expansion

- CFS can automatically expand the storage capacity of the file system based on file size without interrupting requests and applications. It ensures exclusive storage resources while reducing management workload.


#### Secure and reliable

- CFS is highly available and reliable, and each CFS instance has several redundant copies in multiple availability zones.
- CFS can tightly control access to the file system via POSIX permission, and combine permission groups for access control when using a basic network or VPC.

#### Low cost

- CFS can dynamically adjust the capacity as needed, without early storage provision. You only need to pay by usage and no minimum spend or deployment/OPS cost is required.
- CFS allows CVMs to share the same storage space via the NFS protocol, eliminating the need of purchasing other storage services or considering cache.


### Application scenarios: CFS vs. CBS

Item | CFS | CBS
------- | ------- | -------
Throughput | Single client: 100 MB/s (max. 1.5 GB/s) | Max. 600 MB/s
Shareability | Yes | No
Number of redundant copies | 3 | 3
How to use | Use directly after mounting | Need to install a file system first


### Total cost of ownership (TCO): CFS vs. CVM-built NAS

Item | CFS | CVM-built NAS
------- | ------- | -------
Usable storage | 1 TB | 1 TB
Purchased storage | 1 TB | 2 TB (As the disk utilization is 85%, two 1,205 GB premium cloud disks are purchased as master and slave)
Usable storage | 1 TB | 1 TB
Yearly storage resource cost | 7,127 (Postpaid: 0.58 CNY/GB/month) | 4,300 (Prepaid: 0.35 CNY/GB/month)
Yearly computing resource cost | 0 CNY (Users do not need to create a file server for use of CFS) | 23,744 CNY (Two CVMs with the specification of series 1-standard-8 core-32 GB memory are needed as master and slave)
Yearly TCO | 7,004 | 28,044
Monthly cost per GB | 0.58 | 2.28





