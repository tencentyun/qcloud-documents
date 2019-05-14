| Restriction Type | Restriction Description | 
| --- |  --- |
| Restrictions on relevant cloud block storage APIs | If an API's name contains "Elastic Cloud Block Storage", it means this API can only operate on elastic cloud block storage (for example, mounting elastic cloud disk). If the name doesn't contain "Elastic Cloud Block Storage", it can operate on all cloud storage (for example, modifying cloud disk attribute) |
| Regions that support the use of elastic cloud block storage capabilities |  All [Availability Zones](https://intl.cloud.tencent.com/doc/api/229/1286) are available (Except Guangzhou Zone 1, which is out of stock) |
| Available regions for purchasing SSD cloud block storage and high-performance cloud block storage | Currently, SSD cloud block storage and high-performance cloud block storage are only available for Guangzhou Zone 3, Beijing Zone 1, Shanghai Zone 1 and Singapore zone 1. High-performance cloud block storage is in closed test. Open test application will become available soon |
| Cloud block storage performance restriction | About the IO performance described in product documentations. For example, the random IOPS of a 1 TB SSD cloud block storage can reach 24000 IOPS as described in document. This means read and write can reach 24000 IOPS at the same time. The IO performances of 4 KB/8 KB can both reach this number, while the IO of 16 KB cannot reach 24000 IOPS because its throughput has already reached the limit of 260 MB/s |
| Maximum number of elastic cloud disks under a single account | 500 at most |
| Maximum number of elastic cloud disks that can be mounted to a single CVM | 10 at most |
| Maximum number of elastic cloud disks allowed in a single API request (including operations such as purchasing, mounting, unmounting) | 10 at most |
| Maximum capacity for a single HDD cloud disk (data disk) |10 GB-16,000 GB. Currently, the maximum capacity of 16,000 GB is supported for Guangzhou Zone 3, Beijing Zone 1, Singapore Zone 1 |
| Number of snapshots in a single region | Up to (number of cloud disks in the current region\*7) |
| Restriction on mounting elastic cloud block storage to CVM |    The CVM and the elastic cloud block storage must be in the same project/availability zone |
| Elastic cloud block storage billing method restriction | Elastic Cloud Block Storage service only supports monthly or annual billing. Bill-by-traffic is currently not supported |
| Snapshot rollback restriction | Snapshot data can only be rolled back to the cloud disk from which the snapshot was created |
| Type restriction when creating elastic cloud disks using snapshots | You can only use data disk snapshots to create new elastic cloud disks |
| Size restriction when creating elastic cloud disks using snapshots | The size of the new elastic cloud disk that you created must be bigger or equal to the size of the cloud disk from which the snapshot was created |
| Retrieving overdue elastic cloud disks | Elastic cloud disks are billed monthly or annually. If the associated CVM or elastic cloud disk is overdue, the association relation will be canceled and the product will be moved into Recycle Bin. Currently, auto-renewal policy is enabled by default when mounting elastic cloud disks, in order to prevent business interruption when you forget to renew the product |
