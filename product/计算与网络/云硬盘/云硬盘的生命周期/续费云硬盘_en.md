Timely renewal of Cloud Block Storage can effectively avoid data loss due to expiry. It is recommended that users may set an expiry reminder for important data.

## Renewing Elastic Cloud Disk

### Renewing an elastic cloud disk in console

Before the expiration of elastic cloud disk, you can renew it to prevent the hard disk being unmounted and unable to read and write after the expiration:

1) Open [Cloud Block Storage Console](https://console.qcloud.com/cvm/cbs).

2) For elastic cloud disk to be renewed, click on "Renew" on the operation column to the right side.

3) In the pop-up box of renewal, select the time for renewal, and click "OK".

4) After making the payment, you can renew the elastic cloud disk.

## Renewing an elastic cloud disk with API
Users can use the DetachCbsStorages API to renew the elastic cloud disk. For more information, refer to [API to Renew Elastic Cloud Disk](https://www.qcloud.com/doc/api/364/2521).

## Renewing Non-elastic cloud disk

### Renewing an non-elastic cloud disk in console
The life cycle of non-elastic cloud disk is subject to the life cycle of CVM instance. If you need to renew it, go directly to the [Renew CVM instance](/doc/product/213/6143).

### Renewing a non-elastic cloud disk with API
The life cycle of non-elastic cloud disk is subject to the life cycle of CVM instance. Users can use RenewInstance API to renew the elastic cloud disk. For more information, refer to [API to Renew Instance (annual or monthly plan)](https://www.qcloud.com/doc/api/229/1348).
