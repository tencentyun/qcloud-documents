The lifecycle of a cloud disk depends on its type. The lifecycle of an elastic cloud disk is independent of CVM instance and thus can be terminated independently of CVM instance. The lifecycle of a non-elastic cloud disk is same as that of CVM instance and can only be deleted when the CVM is terminated.

## Deleting an Elastic Cloud Disk
The lifecycle of an elastic cloud disk is independent of CVM instance. The lifecycle of a prepaid elastic cloud disk ends when it is terminated by system automatically after a period of time following its expiration. The elastic cloud disk is automatically disassociated from the instance on the expiration date and then is retained in the Recycle Bin for 7 natural days, during which you can renew it. If the cloud disk is not renewed within the 7 days, it will be terminated and the data on it will be lost permanently. You can also renew it before it expires to prevent data loss due to its termination after expiration.

### Recovery of elastic cloud disks

Tencent Cloud Recycle Bin is a recovery mechanism and system for cloud services. After an elastic cloud disk expires, it is retained in the Recycle Bin for a period of time. Users can find and renew in the Recycle Bin some cloud services that have expired. This can avoid the data loss caused by the cloud service being directly cleared by the system.

If your elastic cloud disk is not renewed before it expires (including the expiration date), it is unmounted from the CVM at the expiration time, and is put into in the Recycle Bin, with the data on it retained. Within 7 workings days after it is put into the Recycle Bin, you can recover the cloud disk by renewing it. If the elastic cloud disk is not renewed during this period, it will be released and the **data will be cleared and cannot be recovered**.

You can only recover an elastic cloud disk in the Recycle Bin **by renewing it** before its termination.

### Recovering an elastic cloud disk

Within 7 days after the expiration of an elastic cloud disk, you can go to the Recycle Bin to recover this disk by renewing it:

Go to the [Recycle Bin Console](https://console.cloud.tencent.com/cvm/recycle), locate the elastic cloud disk you want to recover in the list, and then click **Recover**. After you have made payment for renewal, you can find the recovered resource in the [CBS Console](https://console.cloud.tencent.com/cvm/cbs).

You can also renew multiple expired elastic cloud disks:

Go to the [Recycle Bin Console](https://console.cloud.tencent.com/cvm/recycle), locate and select the elastic cloud disks you want to recover in the list, and then click **Recover in Batch**. After you have made payment for renewal, you can find the recovered resources in the [CBS Console](https://console.cloud.tencent.com/cvm/cbs).

## Deleting a Non-Elastic Cloud Disk
The lifecycle of a non-elastic cloud disk is same as that of the CVM instance you create. Therefore, it is terminated with the termination of the instance to which it is mounted. For more information about instance termination, please see [Expiration of Prepaid Instances](/doc/product/213/4931) and [Termination of Postpaid Instances](/doc/product/213/4930).


