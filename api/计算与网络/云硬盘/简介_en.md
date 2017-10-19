Welcome to Tencent Cloud Block Storage!

Cloud Block Storage (CBS) is a highly available, highly reliable, low-cost, customizable network block storage device. For more information, please refer to [CBS Product Overview](https://cloud.tencent.com/doc/product/362/2345).

Users can perform relevant operations (such as creating elastic cloud storage, creating snapshot or roll backing snapshot etc.) on cloud disk or snapshots with the APIs described in this document by referring to [API Overview](https://cloud.tencent.com/doc/api/231/1723).

Before using these APIs, please make sure that you have a thorough understanding of [CBS Product Overview](https://cloud.tencent.com/doc/product/362/2345), [Tips on Usage](https://cloud.tencent.com/doc/product/362/2922) and [Billing Methods](https://cloud.tencent.com/doc/product/362/2413).

## 1. Glossary

To allow you to get familiar with CBS and snapshot services more quickly, we provide the definitions of some commonly used terms in the following table:

| Term | Full Name | Description |
| --- |  --- | --- |
| CBS | [Cloud Block Storage](https://cloud.tencent.com/document/product/439/6329
) | This refers to distributed block storage independently developed by Tencent Cloud and called Could Storage for short. For more information, please refer to [CBS Product Overview](https://cloud.tencent.com/doc/product/362/%E4%BA%A7%E5%93%81%E6%A6%82%E8%BF%B0).It includes cloud disk purchased with CVM and elastic cloud storage purchased separately. |
| Elastic Cloud Storage | [Elastic Cloud Storage](https://cloud.tencent.com/document/product/439/6329#1.2.-.E5.BC.B9.E6.80.A7.E4.BA.91.E7.A1.AC.E7.9B.98
) | This refers to the cloud storage which is purchased separately, instead of being purchased with CVM. It has an independent life cycle (billing cycle), and can be flexibly mounted to or unmounted from different CVMs (being mounted to several CVMs at the same time is not supported). It is also called Elastic Block Storage.  |
| snapshot |   [Cloud Disk Snapshot](https://cloud.tencent.com/doc/product/213/502) | Used to save a copy of cloud disk at a certain point in time. You can use the snapshot to restore the cloud disk to the point when the snapshot was created |

<!--
| root disk |   System Disk | The disk purchased with CVM and used to store the OS of CVM, such as drive C in Windows and vdb in Linux |
| data disk |   Data Disk | The disk used to store user data rather than OS, including HDD cloud storage and elastic cloud storage |
| root disk snapshot |  System Disk Snapshot | A snapshot made for system cloud disk. It can be used to restore the data on cloud disk by rolling back to original cloud disk, but *can not* be used to create a new elastic cloud storage |
| data disk snapshot |  Data Disk Snapshot | A snapshot made for data cloud disk. It can be used to restore the data on cloud disk by rolling back to original cloud disk, and to create a new elastic cloud storage that contains all the data of the snapshot |
-->


## 2. API QuickStart

To use an elastic cloud storage through APIs, you need to complete the following three steps (For more information, please refer to [Examples of Usage of APIs for Elastic Cloud Storage](https://cloud.tencent.com/doc/api/364/5684)):

1. Create an elastic cloud storage: You can use the API [CreateCbsStorages (Create Elastic Cloud Storage)](/doc/api/364/2524) to create an elastic cloud storage.
2. Mount the elastic cloud storage to the specified CVM: When an elastic cloud storage has been created, use the API [AttachCbsStorages (Mount Elastic Cloud Storage)](/doc/api/364/2520) to mount it to the specified CVM.** Note: The term "mount" here refers to assigning the elastic cloud storage to the specified CVM, being equivalent to a hot-plug of a hard disk to the server **.
3. Log in to the CVM to initialize the elastic cloud storage: When using the new elastic cloud storage for the first time, you need to perform a series of operations on it, such as partitioning and formatting. For instructions on how to perform the operations, please refer to [Data Disk Partitioning and Formatting on Windows System](https://cloud.tencent.com/doc/product/213/2158) and [Data Disk Partitioning, Formatting, Mounting and File System Creation on Linux System ](https://cloud.tencent.com/doc/product/362/6735). Note: For Linux system, partitioning is not necessary. You can skip the partitioning process and directly proceed to the formatting.


To use the cloud disk snapshot, you need to complete the following two steps (For more information, please refer to [Examples of Usage of APIs for Cloud Disk Snapshot](https://cloud.tencent.com/doc/api/364/4674)):

1. Create a cloud disk snapshot: You can use the API [CreateSnapshot (create snapshot)](/doc/api/364/2529) to create a snapshot for the specified cloud disk.
2. Rollback the cloud disk snapshot: If necessary, you can use the API [ApplySnapshot (rollback snapshot)](/doc/api/364/2533) to roll back the snapshot to the specified cloud disk.


## 3. Usage Restriction

For restrictions on the usage of CBS and snapshot, please refer to [CBS Usage Restrictions](https://cloud.tencent.com/doc/product/362/5145). For restrictions on specific parameters, please refer to the descriptions of output parameters in the related API's documentation.


