Cloud disk is an expandable storage device on cloud. When a cloud disk is created, you can expand its capacity at any time to increase its storage space without losing any data on it. To expand and use the expanded capacity, the users need to expand both the physical cloud disk and the file system on it to identify the newly available space.

> If the maximum capacity of CBS (4T) cannot meet your needs, you can use RAID to create a logically large space by crossing multiple physical hard disks. For more information, please refer to [Configuring RAID Group of a Cloud Disk](https://cloud.tencent.com/document/product/362/2932
).

## Preconditions
- For CVMs with annual/monthly plan or pay-by-usage plan, you can only change its configuration when its system disk and data disk are cloud disks.
- For a 8 G system disk whose stock operating system is Linux, you can expand the capacity by reinstalling the system. The system disk supports a capacity of 20 G-50 G. Tencent Cloud will provide you with fee-free capacity of 20GB.
- For **a system disk** and a data disk typed as **non-elastic cloud disk**, you can expand the capacity only when the CVMs on which they are mounted are shut down.
- For an elastic cloud disk not mounted on a CVM, you can expand its capacity directly. If it has been mounted on a CVM, you need to shut down the CVM first before the expansion, or unmount the elastic cloud disk before the expansion, and remount it on the original CVM after the expansion.
- After disk expansion, you need to manually modify the file system configuration to make use of the newly expanded capacity. For more information, please refer to [Expanding Linux File System](https://cloud.tencent.com/document/product/362/6738
) and [Expanding Windows File System](https://cloud.tencent.com/document/product/362/6737
).
- To ensure the user security, the disk capacity can only be expanded but cannot be reduced.

## Expanding Elastic Cloud Disk
### Expanding elastic cloud disk via the console

1) Open [CVM Console](https://console.cloud.tencent.com/cvm).

2) Click "Cloud Block Storage" in the navigation pane.

3) Only the cloud disk which is in the status of "Not Mounted" and "Support Mount/Unmount" can be expanded (i.e. the elastic cloud disk which is in the status of "not mounted"). Click "More" - "Expand" buttons in the end to select the new required size (it must be larger than or equal to the current size), and complete the payment to finish expanding the cloud disk.

> For elastic cloud block storage which has been connected to the instance, firstly perform [Unmounting the Elastic Cloud Block Storage](https://cloud.tencent.com/document/product/362/6740
)

### Expanding Elastic Cloud Disk via API
Please refer to [ResizeCbsStorage API](https://cloud.tencent.com/doc/api/364/2527).

## Expanding Non-elastic Cloud Disk
### Expanding non-elastic cloud disk via console
1) Open [CVM Console](https://console.cloud.tencent.com/cvm).

2) Click "Cloud Virtual Machine" in the navigation pane.

3) Only the instance which is in the status of "Shutdown" and whose system disk and data disk are cloud disks can be expanded. Click "More" - "CVM Settings" - "Adjust Cloud Disk" buttons in the end, and select the new required size (it must be larger than or equal to the current size), and complete the payment to finish expanding the cloud disk.

> > For a running instance with its system disk and data disk being cloud disks, you need to perform [Instance Shutdown](/doc/product/213/4929) before expansion.

### Expanding Non-elastic Cloud Disk via API
Please refer to [ResizeInstance API](https://cloud.tencent.com/doc/api/229/1306) and [ResizeInstanceHour API](https://cloud.tencent.com/doc/api/229/1344).
