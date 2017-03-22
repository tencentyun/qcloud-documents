If users do not need [postpaid instances](https://www.qcloud.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9) any more, they may terminate the instance (Note: instances under an annual or monthly plan do not support voluntary termination, and can be terminated automatically within a period of time after expiration). When an instance is under termination or terminated, no fees related to this instance would be generated.

When an instance charged by quantity is terminated, the local disks and non-elastic Cloud Block Storage mounted to the instance will be terminated as well, and the data stored on these storages will be lost. But the elastic Cloud Block Storage mounted to the instance will be kept, and the data will not be affected. After an instance charged by quantity is terminated, it is still visible in console in a short period. Later the instance will be automatically deleted and removed from the instance list, and service on the instance will be terminated utterly.

## Use console to terminate postpaid instances

1) Open [CVM console](https://console.qcloud.com/cvm/).

2) The termination of CVM only works for machines charged by quantity.

3) To release a postpaid CVM instance running solely, click "Terminate" on the action bar to the right side.

4) To release CVM instances charged by quantity running in batch, check all the hosts charged by quantity to be released, and click "More" - "Terminate" on the top of the list. Reasons will be given for CVM instances that cannot be terminated.

## Use API to terminate postpaid instances
Please refer to [Return Instance API](https://www.qcloud.com/doc/api/229/1347).