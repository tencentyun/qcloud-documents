Cloud disk is an expandable storage device on the cloud. When a cloud disk is created, you can expand its capacity at any time to increase its storage space without losing any data on it. To expand and use the expanded capacity, you need to expand both physical cloud disk and file system on it to identify newly available space.

> If the maximum capacity of a cloud disk (4 TB) cannot meet your needs, you can use RAID to create a logically large space across multiple physical disks. For more information, please see [Configure RAID Group of Cloud Disk](/document/product/362/2932).
> 
> If MBR format is used when you partition your disk, it is not supported when the capacity exceeds 2 TB. We recommend that you create a new data disk, partition the disk using GPT format, and copy data to the new disk.

## Expanding Cloud Data Disks
### Expanding Data Disk Via CBS Console

1) Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

2) Click **Cloud Block Storage** in the navigation pane.

3) Only the disks in the status of "Unmounted" and "Support Mounting/Unmounting" can be expanded. Click **More -> Expand** at the end to select a new desired size (it must be larger than or equal to the current size), and complete payment to finish the capacity expansion of physical disk.

> For elastic cloud disks which have been connected to the instance, you first need to [Unmount Cloud Disk](/doc/product/362/6740).

### Expanding Data Disk via API
For more information, please see [ResizeCbsStorage](https://cloud.tencent.com/doc/api/364/2527) API.

### Expanding Data Disk via CVM Console
1) Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

2) Click **Cloud Virtual Machine** in the navigation pane.

3) An instance can be expanded only when it is in the status of "Shutdown" and its system disks and data disks are cloud disks. Click "More" -> "CVM Settings" -> "Adjust Disk" at the end, and select a new desired size (it must be larger than or equal to the current size), and complete payment to the capacity expansion of physical disk.

> For a running instance with system disks and data disks being cloud disks, you need to perform [Instance Shutdown](/doc/product/213/4929) before expansion.

## Expanding Cloud System Disk
A system disk with type of CBS is allowed for expansion only by reinstalling the operating system of CVM. For more information, please see [Reinstall System](https://cloud.tencent.com/document/product/213/4933).
