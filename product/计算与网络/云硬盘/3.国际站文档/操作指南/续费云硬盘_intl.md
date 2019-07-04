Timely renewal of cloud disk can effectively avoid data loss due to expiry. It is recommended that users set an expiry reminder for important data.

## Renewing Elastic Cloud Disk

### Renewing Elastic Cloud Disk via Console

Before the expiration of elastic cloud disk, you can renew it to prevent the hard disk being unmounted and unable to read and write after the expiration:

1) Open [Cloud Disk Console](https://console.cloud.tencent.com/cvm/cbs).

2) For elastic cloud disk to be renewed, click on **Renew** on the operation column at the right side.

3) In the pop-up box of renewal, select the time for renewal, and click **OK**.

4) Make the payment to complete the renewal for the elastic cloud disk.

## Renewing Elastic Cloud Disk via API
Users can use the RenewCbsStorages API to renew the elastic cloud disk. For more information, please see [API to Renew Elastic Cloud Disk](https://cloud.tencent.com/doc/api/364/2521).

## Renewing Non-elastic Cloud Disk

### Renewing Non-elastic Cloud Disk via Console
The lifecycle of non-elastic cloud disk is subject to the lifecycle of CVM instance. If you need to renew it, go directly to the [Renew CVM instance](/doc/product/213/6143).

### Renewing Non-elastic Cloud Disk via API
The lifecycle of non-elastic cloud disk is subject to the lifecycle of CVM instance. Users can use RenewInstance API to renew the elastic cloud disk. For more information, please see [API to Renew Instance (prepaid)](https://intl.cloud.tencent.com/doc/api/229/1348).
