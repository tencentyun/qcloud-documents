Cloud disk is an expandable storage device on cloud. When a cloud disk is created, you can expand its capacity at any time to increase its storage space without losing any data on it. To expand and use the expanded capacity, the users need to expand both the physical cloud disk and the file system on it to identify the newly available space.

> If the maximum capacity of cloud disk (4T) cannot meet your needs, you can create a logically super-large space by using RAID to cross multiple physical block storage. For more information, please see [Configure RAID Group of Cloud Disk](/document/product/362/2932).
> 
> If the disk partition is in MBR format, the MBR partition format is no longer supported when the expanded capacity exceeds 2TB. You are advised to create a data disk and copy the data to the new disk after using the GPT partition.

## Data Disk with Capacity Type as CBS
### Expanding Data Disk Via CBS Console

1) Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

2) Click **Cloud Block Storage** in the navigation pane.

3) Only the disks in the status of **Unmounted** and **Support Mounting/Unmounting** can be expanded. Click **More** -> **Expand** at the end to select a new desired size (it must be larger than or equal to the current size), and complete payment to finish the capacity expansion of physical disk.

> For elastic cloud disks which have been connected to the instance, you first need to [Unmount Cloud Disk](/doc/product/362/6740).

### Expanding CBS Data Disk via API
For more information, please see [API ResizeCbsStorage](https://intl.cloud.tencent.com/doc/api/364/2527).

### Expanding CBS Data Disk via CVM Console
1) Log in to the [CVM Console](https://console.cloud.tencent.com/cvm).

2) Click **Cloud Virtual Machine** in the navigation pane.

3) Only the instance which is in the status of **Shutdown** and whose system disk and data disk are cloud disks can be expanded. Click **More** -> **CVM Settings** -> **Adjust Cloud Disk** buttons in the end, and select the new required size (it must be larger than or equal to the current size), and complete payment to finish the capacity expansion of physical disk.

> For a running instance with its system disk and data disk being cloud disks, you need to perform [Instance Shutdown](/doc/product/213/4929) before expansion.

## Expanding System Disk of the Type of Cloud Disk
A system disk of the type of cloud disk is allowed for capacity expansion, but this can only be achieved by reinstalling CVM OS. For more information, please see [Reinstall System](https://intl.cloud.tencent.com/document/product/213/4933).
