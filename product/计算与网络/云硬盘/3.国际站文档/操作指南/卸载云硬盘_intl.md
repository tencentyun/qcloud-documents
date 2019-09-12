When you need to mount an ***elastic cloud disk*** to another instance, you can disconnect it from the current instance and then connect it to another instance.<font color="red"> Unmounting an elastic cloud disk does not clear the data on it.</font>

## Unmounting an Elastic Cloud Disk in Console

Elastic cloud disks used as data disks can be unmounted, but those used as system disks cannot.

<font color="red">
Please note the following points before unmounting a data disk:
</font>

- In the Windows operating system, to ensure data integrity, you're recommended to suspend reading and writing operations on all file systems on the disk. Otherwise, data that has not been read or written will be lost. <font color="red"> You need to set the elastic cloud disk offline before unmounting it. Otherwise, you may not be able to mount the disk again without restarting the CVM. </font>
![](//mccdn.qcloud.com/static/img/92a187945b9f4318981ea70b6532e1d6/image.png)

- In the Linux operating system, you need to log in to the instance and perform ` unmount ` operation on the elastic cloud disk to be unmounted. After the command is successfully executed, go to the console to unmount the disk. If the elastic cloud disk is forced to be unmounted without "unmount" operation, the following problems may occur during shutdown and startup of CVM: 
![](//mccdn.qcloud.com/static/img/9939fccce6e6d9ead64b5703455d4403/image.png)
![](//mccdn.qcloud.com/static/img/9939fccce6e6d9ead64b5703455d4403/image.png)

(1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/).

(2) Go to **CVM** -> **CBS** tab.

(3) In the cloud disk list page, click the **More** -> **Unmount** button next to the cloud disk with a status of <font color="red">Mounted, and Supports Mounting/Unmounting</font> to unmount the single disk.
You can also select the cloud disks with a status of <font color="red">Mounted, and Supports Mounting/Unmounting</font> in the cloud disk list page, and then click the **Unmount** button on the top to unmount disks in batch.

(4) Confirm the operation in the pop-up box by clicking the **Confirm** button.

## Unmounting an Elastic Cloud Disk Using APIs
You can unmount an elastic cloud disk by using the API DetachCbsStorages. For more information, please see [API for Unmounting Elastic Cloud Disk](https://cloud.tencent.com/doc/api/364/2521).
