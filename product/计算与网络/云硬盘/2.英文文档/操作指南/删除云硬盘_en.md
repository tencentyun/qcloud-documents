The life cycle of Cloud Block Storage varies with its type: With its life cycle being independent of CVM instances, elastic cloud disk can be terminated independently. The life cycle of the non-elastic cloud disk is subject to the CVM, which can only be deleted when the CVM is terminated.

## Deleting Elastic Cloud Disk
The life cycle of elastic cloud disk is independent of the CVM instance. After a certain time following its end of life cycle, the elastic cloud disk with an annual or monthly plan will be automatically terminated by the system. The elastic cloud disk will automatically disassociate with the instance on the expiry date and automatically put into the Recycle Bin. It will be retained for 7 calendar days during which you can choose to renew. The Cloud Block Storage will then be terminated if it is not renewed within 7 calendar days, and the data will be completely lost. At the same time, you can also renew it before the expiry date, to prevent the loss of data due to the storage being terminated upon expiration.

### Recycle of Elastic Cloud Disk

Tencent Cloud Recycle Bin is a recovery mechanism and system for cloud services. The elastic cloud disk will be put into the Recycle Bin upon expiration and be kept for a certain time, during which users can find it in the Recycle Bin and renew it. In this way, users can avoid major risks such as loss of cloud service data cleared directly by the system.

If your elastic cloud disk hasn't been renewed before the expiry date (including), the system will unmount it from its mounted CVM instance, and will put it into Recycle Bin with data saved from the expiry date. Within 7 workings days after it has been put into the Recycle Bin, you can still recover this Cloud Block Storage by renewing it. If, during this period, the elastic cloud disk hasn't been renewed, the system will release the resources, and **data will be erased and cannot be recovered**.

For Elastic Cloud Disk in the Recycle Bin, users can only apply **renew to recover** to the recycled objects before terminating.

### Recovering Elastic Cloud Disk

Within 7 days after the expiration of elastic cloud disk, you can go to the Recycle Bin to recover this Cloud Block Storage by renewing it:

Open the [Recycle Bin Console](https://console.cloud.tencent.com/cvm/recycle), locate the elastic cloud disk that you want to recover in the list, and then click on "Recovery". After you've paid for renewal, you can find the recovered resources in the [Cloud Block Storage Console](https://console.cloud.tencent.com/cvm/cbs).

Or you can renew multiple expired elastic Cloud Disks:

Open the [Recycle Bin Console](https://console.cloud.tencent.com/cvm/recycle), locate the elastic cloud disk that you want to recover in the list, and then select the resources to be recovered, click on "Batch Recovery". After you've paid for renewal, you can find the recovered resources in the [Cloud Block Storage Console](https://console.cloud.tencent.com/cvm/cbs).

## Deleting Non-elastic cloud disk
The life cycle of non-elastic cloud disk is subject to the created CVM instance, so the non-elastic cloud disk will be terminated when its mounted instance is terminated. For more information about instance termination, refer to [Expiration of Instance with an Annual or Monthly Plan](/doc/product/213/4931) and [Terminate Instance with Bill-by-Traffic Plan](/doc/product/213/4930).


