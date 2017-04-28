You can terminate unnecessary [postpaid instances](https://www.qcloud.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9) any time. (Note: you can not terminate prepaid instances manually. They will be terminated automatically after expiration). A terminated instance will not incur charges.

When a postpaid instance is terminated, the local disks and non-elastic Cloud Block Storage mounted to the instance will be terminated as well, and the data stored on them will be discarded. But the elastic Cloud Block Storage mounted to the instance will be kept, and the data will not be affected. When a postpaid instance is terminated, it is still visible on Console for a short period.

## Terminate postpaid instances on Console

1) Open [CVM console](https://console.qcloud.com/cvm/).

2) Only postpaid CVMs can be terminated.

3) To release one postpaid CVM instance, click "Terminate" on the action bar to the right side.

4) To release multiple postpaid CVM instances at once, check the desired CVMs, and click "More" - "Terminate" on the top of the list. Reasons will be given for CVM instances that cannot be terminated.

## Terminate postpaid instances via API
Please refer to [Return Instance API](https://www.qcloud.com/doc/api/229/1347).