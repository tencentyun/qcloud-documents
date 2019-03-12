When you need to mount the ***elastic cloud disk*** to another instance, you can disconnect it from the current instance and then connect it to another instance. The unmounting of elastic cloud disk WILL NOT erase the data on it.

## Unmount an elastic cloud disk in console

It currently supports the unmounting of common elastic cloud disk which is used as data disk, but not as system disk.

When you unmount the data disk, please make sure that you understand the followings:

- In Windows operating system, in order to ensure data integrity, it is recommended that you suspend all read and write operations on all file systems of the disk, otherwise the data in the middle of read/write process will be lost. You need to set the disk offline first before the unmounting of elastic cloud disk, or you may not be able to mount the elastic cloud disk again without rebooting the CVM.
![](//mccdn.qcloud.com/static/img/92a187945b9f4318981ea70b6532e1d6/image.png)

- In Linux operating system, you need to log in to the instance and perform ` unmount ` command to the elastic cloud disk required to be unmounted, then enter the console to unmount the disk after the command is successfully performed. If the elastic cloud disk is forced to be unmounted without "unmount" operation, the following problems may occur while the system is being shut down or booted up: 
![](//mccdn.qcloud.com/static/img/9939fccce6e6d9ead64b5703455d4403/image.png)
![](//mccdn.qcloud.com/static/img/9939fccce6e6d9ead64b5703455d4403/image.png)

1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

2) Enter "Cloud Virtual Machine" - "Cloud Block Storage" tab.

3) In the Cloud Block Storage list page, click "More" - "Unmount" button next to the Clocd Block Storage with the status of "Mounted" or "Support Mounting/Unmounting" to unmount the single Cloud Block Storage;
Or in the Cloud Block Storage list page, check the Cloud Block Storage with the status of "Mounted" or "Support Mounting/Unmounting", and click "Mount" button on the top to batch unmount.

4) Confirm warnings in the pop-up dialog box, and click "Confirm" button.

## Unmounting an elastic cloud disk with API
Users can use the DetachCbsStorages API to unmount the elastic cloud disk. For more information, refer to [API to Unmount Elastic Cloud Disk](https://cloud.tencent.com/doc/api/364/2521).
