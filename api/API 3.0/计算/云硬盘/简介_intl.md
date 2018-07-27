Thank you for using Tencent Cloud Block Storage!

Cloud Block Storage is a highly available, highly reliable, low-cost and customizable network block device. For more information, please see [CBS Product Overview](https://cloud.tencent.com/doc/product/362/2345).

Users can use the APIs described in this document to perform operations on cloud disks and snapshots, such as creating an elastic cloud disk, creating a snapshot, or rolling back a snapshot. For more information on supported operations, please see [API Overview](/document/product/362/15634).

Before using these APIs, make sure you have a thorough understanding of the [CBS product](https://cloud.tencent.com/doc/product/362/2345) as well as its [usage](https://cloud.tencent.com/doc/product/362/2922) and [billing methods](https://cloud.tencent.com/doc/product/362/2413).

## Glossary

To help you get familiar with CBS and snapshot services more quickly, we provide the definitions of some commonly used terms in the following table:

| Term | Full Name | Description |
| --- |  --- | --- |
| CBS | [Cloud Block Storage](https://cloud.tencent.com/document/product/439/6329) | This refers to distributed block storage independently developed by Tencent Cloud and called Could Storage for short. For more information, please see [CBS Product Overview](https://cloud.tencent.com/doc/product/362/%E4%BA%A7%E5%93%81%E6%A6%82%E8%BF%B0). It includes cloud disk purchased with CVM and elastic cloud storage purchased separately. |
| Elastic cloud block storage | [Elastic Cloud Block Storage](https://cloud.tencent.com/document/product/439/6329#1.2.-.E5.BC.B9.E6.80.A7.E4.BA.91.E7.A1.AC.E7.9B.98) | A cloud disk, also known as elastic cloud disk, that is not purchased along with a CVM (purchased separately), with an independent lifecycle (billing cycle). It can be mounted and unmounted among different CVMs (cannot be mounted simultaneously on multiple CVMs). |
| Snapshot | [Cloud Disk Snapshot](https://cloud.tencent.com/doc/product/213/502) | Used to save a copy of a cloud disk at a certain point. You can use the snapshot to restore the cloud disk to the point when the snapshot was created. |

<!--
| root disk |   System Disk | The disk purchased with CVM and used to store the OS of CVM, such as drive C in Windows and vdb in Linux |
| data disk |   Data Disk | The disk used to store user data rather than OS, including HDD cloud disk and elastic cloud disk |
| root disk snapshot |  System Disk Snapshot | A snapshot made for system cloud disk. It can be used to restore data by rolling back to original cloud disk, but **cannot** be used to create a new elastic cloud disk. |
| data disk snapshot |  Data Disk Snapshot | A snapshot made for data cloud disk. It can be used to restore the data on cloud disk by rolling back to original cloud disk, and to create a new elastic cloud disk that contains all the data of the snapshot. |
-->

#### Definitions of input and response parameters

* Limit and Offset
> These parameters are used to control paging. "Limit" indicates the maximum number of entries returned at a time, and "Offset" is the offset value. For the results in a list format, if the number of entries exceeds the "Limit" value, the number of returned values will be limited to the "Limit" value.
>
>For example, if Offset=0&Limit=20, the 0st to 20th entries are returned; if Offset=20&Limit=20, the 20th to 40th entries are returned; if Offset=40&Limit=20, the 40th to 60th entries are returned, and so on.
    
* Ids.N
> Format for inputting multiple parameters at a time. Multiple parameters in such a format can be input at the same time. For example:
>   
> Ids.0=10.12.243.21&Ids.1=10.11.243.21&Ids.2=10.12.243.21&Ids.3=10.13.243.21...
>   
> And so on (with subscripts starting with 0).

## Getting Started with API

To use an elastic cloud disk via APIs, you need to complete the following three steps:

1. Create an elastic cloud disk: You can use the API [CreateDisks (create elastic cloud disk)](/document/product/362/16312) to create an elastic cloud disk.
2. Mount the elastic cloud disk to the specified CVM: When an elastic cloud disk has been created, use the API [AttachDisks (mount elastic cloud disk)](/document/product/362/16313) to mount it to the specified CVM. **Note: The term "mount" here refers to assigning the elastic cloud disk to the specified CVM, being equivalent to a hot-plug of a hard disk to the server**.
3. Log in to the CVM to initialize the elastic cloud disk: When using the new elastic cloud disk for the first time, you need to perform a series of operations on it, such as partitioning and formatting. For more information on how to perform the operations, please see [Data Disk Partitioning and Formatting on Windows System](https://cloud.tencent.com/doc/product/213/2158) and [Data Disk Partitioning, Formatting, Mounting and File System Creation on Linux System](https://cloud.tencent.com/doc/product/362/6735). Note: For Linux system, partitioning is not necessary. You can skip the partitioning process and directly proceed to the formatting.


To use cloud disk snapshots via APIs, you need to complete the following two steps:

1. Create a cloud disk snapshot: You can use the API [CreateSnapshot (create snapshot)](/document/product/362/15648) to create a snapshot for the specified cloud disk.
2. Roll back the cloud disk snapshot: If necessary, you can use the API [ApplySnapshot (roll back snapshot)](/document/product/362/15643) to roll back the snapshot to the specified cloud disk.


## Use Limits

For restrictions on the usage of CBS and snapshot, please see [CBS Use Limits](https://cloud.tencent.com/doc/product/362/5145). For restrictions on specific parameters, please see the descriptions of output parameters in the related API's documentation.


