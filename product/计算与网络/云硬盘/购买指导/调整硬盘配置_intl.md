Cloud disk is an expandable storage device on cloud. When a cloud disk is created, you can expand its capacity at any time to increase its storage space without losing any data on it. To expand and use the expanded capacity, you need to expand both the physical cloud disk and the file system on it to identify the newly available space.

> If the maximum capacity of a cloud disk (4 TB) cannot meet your needs, you can use RAID to create a logically large space across multiple physical disks. For more information, please see [Configure RAID Group of Cloud Disk](/document/product/362/2932).

## Prerequisites
- For prepaid and postpaid CVMs, you can only change the configuration when the system disk and data disk are <font color="red">cloud disks</font>.
- You can only expand the server system disks of cloud disks by reinstalling OS.
- For a cloud disk not mounted on a CVM, you can expand its capacity directly. If it has been mounted on a CVM, you need to shut down the CVM first before the expansion, or unmount the cloud disk before the expansion, and remount it on the original CVM after the expansion.
- After disk expansion, you need to manually modify the file system configuration to make use of the newly expanded capacity. For more information, please see [Expanding Linux File System](https://intl.cloud.tencent.com/document/product/362/6738) 
and [Expanding Windows File System](https://intl.cloud.tencent.com/document/product/362/6737
).
- To ensure the user data security, the disk capacity can only be expanded but cannot be reduced.

## Expanding Elastic Cloud Disk
### Expanding an Elastic Cloud Disk via the Console

1) Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

2) Click **Cloud Block Storage** in the navigation pane.

3) Only the cloud disk in the status of **Unmounted** and **Support Mounting/Unmounting** can be expanded (i.e., the elastic cloud disk in the status of **Unmounted**). Click **More** -> **Expand** at the end to select the desired size (it must be larger than or equal to the current size), and complete the payment to finish the capacity expansion of physical disks.

> For elastic cloud disks which have been connected to the instance, you need to [Unmount Cloud Disk](https://cloud.tencent.com/document/product/362/6740).

### Expanding Elastic Cloud Disk via API
For more information, please see [API ResizeCbsStorage](https://intl.cloud.tencent.com/doc/api/364/2527).

## Expanding Non-elastic Cloud Disk
### Expanding Non-elastic Cloud Disk via the Console
1) Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

2) Click **Cloud Virtual Machine** in the navigation pane.

3) Only the instance which is in the status of **Shutdown** and whose system disk and data disk are cloud disks can be expanded. Click **More** -> **CVM Settings** -> **Adjust Cloud Disk** buttons in the end, and select the new required size (it must be larger than or equal to the current size), and complete payment to finish the capacity expansion of physical disk.

> For a running instance with system disks and data disks being cloud disks, you need to perform [Instance Shutdown](/doc/product/213/4929) before expansion.

### Expanding Non-elastic Cloud Disk via API
Please see [API ResizeInstance](https://intl.cloud.tencent.com/doc/api/229/1306) and [API ResizeInstanceHour](https://intl.cloud.tencent.com/doc/api/229/1344).

