Different from postpaid instances, prepaid instance cannot be terminated by users. After a certain time following the its end of life cycle, it will be automatically terminated by the system. Prepaid CVM instances are shut down on the expiry date and automatically put into the Recycle Bin. It will be retained for 7 calendar days during which you can choose to renew. The instance will then be terminated if it is not renewed within 7 calendar days. At the same time, you can [renew (or set up auto renewal for)](/doc/product/213/6143) the instance with such plan before the expiry date, to prevent services interruption due to shutdown when it expires.

## Instance Recycle

Tencent Cloud Recycle Bin is a recovery mechanism and system for cloud services. Cloud services with an annual or monthly plan will be put into the **Recycle Bin** upon expiration and be kept for a certain time, during which users can find it in the Recycle Bin and renew it. In this way, users can avoid major risks such as loss of cloud service data cleared directly by the system.

If your CVM instance hasn't been renewed before the expiry date (including), the system will end its service (network outage and service shutdown with data saved only) from the expiry date. Within 7 workings days after it has been put into the Recycle Bin, you can still recover it by renewing it. If, during this period, the instance hasn't been renewed, the system will release the resources, and **data will be erased and cannot be recovered**.

- After putting into the Recycle Bin, CVM will be **forced to terminate** the mounting relationship with Cloud Load Balance, Elastic Public IP, elastic cloud disk, auxiliary ENI, and basic network interconnection. The mounting relationship **cannot be recovered** after renewal, you have to reset it.
- For sufficient account balance, the device with auto renewal setting will perform renewal automatically upon expiration.

For objects in the Recycle Bin, users can only **renew to recover** the recycled object before terminating.

## Recover instance

Within 7 days after the expiration of CVM, you can go to the Recycle Bin to recover the CVM by renewing it:

Open the [CVM Recycle Bin Console](https://console.cloud.tencent.com/cvm/recycle), locate the CVM that you want to recover in the list, and then select the resources that need to be restored, click on "Recovery". After you've paid for renewal, you can find the recovered resources in the [CVM Console](https://console.cloud.tencent.com/cvm).

## Batch Renew Instances

Open the [CVM Recycle Bin Console](https://console.cloud.tencent.com/cvm/recycle/cvm), locate the CVM that you want to recover in the list, and then select the resources to be recovered, click on "Batch Recovery". After you've paid for renewal, you can find the recovered resources in the [CVM Console](https://console.cloud.tencent.com/cvm).

## Terminate an Instance

Within 7 days after the expiration of CVM, you can go to the Recycle Bin to terminate the CVM completely:

Open the [CVM Recycle Bin Console](https://console.cloud.tencent.com/cvm/recycle/cvm), select the the CVM that you want to terminate, and click "Terminate" and confirm the operation. The selected item will be **terminated and cannot be recovered**.

## Batch Terminate Instances

Open the [CVM Recycle Bin Console](https://console.cloud.tencent.com/cvm/recycle/cvm), select the the CVMs you want to terminate, and click "Batch Terminate" and confirm the operation. The selected items will be **terminated and cannot be recovered**.

Note:

- **Once terminated, all data will be cleared and cannot be recovered. Please back-up your data before the operation.**
- **EIPs and elastic cloud disks of the terminated machines are still available. Idle IPs will be charged. Release them in the resource management page if you don't need them any more.**





