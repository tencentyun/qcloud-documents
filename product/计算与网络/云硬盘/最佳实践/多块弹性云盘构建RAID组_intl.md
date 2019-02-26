RAID (Redundant Array of Independent Disks) combines multiple disks to form a disk array in order to improve data read and write performance and reliability. Meanwhile, the operating system will treat the disk array as a hard disk to use. RAID has a variety of grades at present. The following will introduce RAID0, RAID1, RAID01 and RAID10. Depending on the version of RAID, the disk array domains in enhancing data integration, enhancing fault tolerance, and increasing throughput or capacity compared with a large hard disk with considerable capacity.

The following is a comparison of different RAID versions:
<table>
<tbody>
<tr><th>RAID version</th><th>RAID0</th><th>RAID1</th><th>RAID01</th><th>RAID10</th>
<tr><td>Features</td><td> Data is stored on different disks in segments. The size of virtual disk is the sum capacity of the disks in the array </td><td>The data is stored through image memory into disks. The size of virtual disk depends on the capacity of the disk with the smallest one in the array</td><td> First deal with data through RAID0, then RAID1</td><td> First deal with data through RAID1, then RAID0</td>
<tr><td>Advantages</td><td> Read and write can be synchronized, thus the theoretical read and write rate can reach N times faster than a single disk (N is the number of disks in RAID0). But in fact, it is limited by file size, file system size and other factors</td><td> Damage to a single disk will not lead data irreversible, read fast</td><td colspan="2"> Take into both RAID0 and RAID1 advantages</td>
<tr><td>Disadvantages </td><td>No data redundancy. If a single disk is damaged, it is likely to cause all data lost in the most serious cases</td><td> Disk utilization rate is minimal and write speed is limited by that of a single disk</td><td colspan="2"> Costs are relatively high and it is essential to use at least 4 disks</td>
<tr><td>Recommended Using Scenario </td><td>Require a higher level of I/O performance, and has backed up data through other means or there is no need for data backup</td><td> Require a high level of read performance, and it is essential to back up the written data</td><td colspan="2"> RAID10 is recommended because RAID01 will cause disks in the same group unavailable if a single disk is corrupted</td>
</tbody>
</table>

The following describes how to use four Tencent Cloud elastic cloud disks to build RAID0 array. Linux kernel provides RAID device which is managed by md module in the bottom level. We can use mdadm tool to call md module.

![](//mccdn.qcloud.com/static/img/9f42e96976ee6f3655090a4208f461c5/image.png)
> Note: Please renew fees for elastic cloud disk about to expire in order to prevent the elastic cloud disk from being enforced isolation by the system, resulting in impacts on the RAID array.

## Installing mdadm (take CentOS as an example)
![](//mccdn.qcloud.com/static/img/59896b0ee3f20cd0f20f2f3633e56a1f/image.png)

## Creating RAID0 with mdadm
![](//mccdn.qcloud.com/static/img/8d180220850c396dcf91266b43f2220d/image.png)

> Note: When creating RAID1, RAID01, and RAID10, it is best to create RAID with partitions of the same size to avoid wasting disk space.

## Using mkfs to Create File System
![](//mccdn.qcloud.com/static/img/e92608f31d914556a585e3190a009a64/image.png)

## Mounting File System
![](//mccdn.qcloud.com/static/img/a4c36941609c64a3753648622392de65/image.png)

## Modifying mdadm Configuration File
Determine UUID of the file system:
![](//mccdn.qcloud.com/static/img/e42b1f74126420929cd3b3668cca3f21/image.png)

Execute commands below to modify mdadm configuration files:

```
vi /etc/mdadm.conf
```

It is recommended to write the following configuration for elastic cloud disk:

```
DEVICE /dev/disk/by-id/virtio-elastic cloud disk 1ID-part1 
DEVICE /dev/disk/by-id/virtio-elastic cloud disk 2ID-part1 
DEVICE /dev/disk/by-id/virtio-elastic cloud disk 3ID-part1 
DEVICE /dev/disk/by-id/virtio-elastic cloud disk 4ID-part1 
ARRAY logical device path metadata = UUID =
```
In this case: ARRAY /dev/md0 metadata=1.2 UUID=3c2adec2:14cf1fa7:999c29c5:7d739349


