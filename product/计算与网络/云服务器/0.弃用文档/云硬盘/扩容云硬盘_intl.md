Cloud disk is an expandable storage device. When a cloud disk is created, you can expand its capacity at any time to increase its storage space without losing any data on it. To expand and use the expanded capacity, the users need to expand both the physical cloud disk and the file system on it to identify the newly available space.

> If the maximum capacity of cloud disk (4T) cannot meet your needs, you can create a logically super-large space by using RAID to cross multiple physical block storage. For more information, please refer to [Configuring RAID Group of a Cloud Disk](https://cloud.tencent.com/document/product/362/2932
).

## Expanding Elastic Cloud Disk
### Expanding an Elastic cloud disk via the Console

1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click "Cloud Block Storage" in the navigation pane.

3) Only the cloud disk which is in the status of "To be Mounted" and "Mounting/Unmounting Supported" can be expanded (i.e., the elastic cloud disk which is in the status of "Not mounted"). Click "More" - "Expand" buttons in the end to select the new required size (it must be larger than or equal to the current size), and complete the payment to finish expanding the cloud disk.

> For elastic cloud block storage which has been connected to the instance, please firstly perform [Unmounting the Elastic Cloud Disk](https://cloud.tencent.com/document/product/362/6740
)

### Expanding an Elastic cloud disk via API
Please refer to [ResizeCbsStorage API](https://cloud.tencent.com/doc/api/364/2527).

## Expanding non-elastic cloud disk
### Expanding non-elastic cloud disk via console
1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click "Cloud Virtual Machine" in the navigation pane.

3) Only the instance which is in the status of "Shutdown" and whose system disk and data disk are cloud disks can be expanded. Click "More" - "CVM Settings" - "Adjust Cloud Disk" buttons in the end, and select the new required size (it must be larger than or equal to the current size), and complete the payment to finish expanding the cloud disk.

> For a running instance with its system disk and data disk being cloud disks, you need to perform [Instance Shutdown](/doc/product/213/4929) before expansion.

### Expanding Elastic Cloud Disk via API
Please refer to [ResizeInstance API](https://cloud.tencent.com/doc/api/229/1306) and [ResizeInstanceHour API](https://cloud.tencent.com/doc/api/229/1344).
