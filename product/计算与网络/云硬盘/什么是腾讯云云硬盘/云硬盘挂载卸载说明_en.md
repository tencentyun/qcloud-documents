## Elastic Cloud Block Storage
### Introduction


To allow users to mount/unmount their cloud disks freely, Tencent Cloud has added a product attribute "Elastic Cloud Block Storage" to CBS. Elastic cloud disks can be mounted to/unmounted from CVMs in the same availability zone anytime. Once mounted, they will be considered as usable data disks by the CVM.


### Restriction

1. One CVM can mount up to 10 elastic cloud disks, that is, one CVM can mount elastic cloud block storage for a maximum capacity of 160TB.
2. A user can purchase up to 10 elastic cloud disks at a time. One account can purchase up to 500 elastic cloud disks.
3. Elastic cloud disks are billed monthly or annually. If the associated CVM or elastic cloud disk is overdue, the association relation will be canceled and the product will be moved into Recycle Bin. Currently, auto-renewal policy is enabled by default when mounting elastic cloud disks to CVMs, in order to prevent business interruption when you forget to renew your cloud disks


### Usage Scenarios

1. You have purchased a server (4-core, 8GB RAM) with 100GB local disk space. Now the disk space is insufficient, you can purchase elastic cloud disks to satisfy your extra storage demand

2. You don't wish to purchase additional disks when purchasing the server. You plan to purchase disks only when it is necessary.

3. Server A has 10GB of critical data stored in elastic cloud disk and you wish to share the data to server B.  You can simply unmount the disk and mount it to server B

4. The largest cloud disk (16TB) is not sufficient. You can purchase multiple 4TB cloud disks, then configure LVM logic partitions which will provide disk with a size of 10TB or 20TB

5. The IO performance of a single disk is insufficient. You can purchase multiple cloud disks, then configure RAIDs such as raid 0, raid 10, to improve IO performance
