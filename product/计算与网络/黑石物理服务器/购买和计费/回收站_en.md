In Recycle Bin, you can manage *isolated* CPMs centrally to renew and recover them with ease.</br>
The figure below shows how the status of an instance in arrears changes:

![](http://mc.qcloudimg.com/static/img/d13b2dc5437a38777bc77902848ccbd5/image.jpg)


## In Arrears
"In Arrears" status indicates the remaining usage period of a purchased CPM is 0 and its actual usage period has gone beyond the purchased validity period. A CPM in arrears can still be used, but it will be isolated when this status has lasted for a specified period. When isolated, the CPM does not allow the access from public network. Please renew the CPM in arrears in a timely manner to ensure a normal operation of your business.

## Isolated
If an instance fails to be renewed within 7 days after it goes into the status of "In Arrears", it will be isolated on the 8th day. When isolated, the instance will be shut down forcibly and does not allow access from public and out-of-band networks. If you still fails to renew the instance in time after its isolation, it will be destroyed by Tencent Cloud on the 8th day after isolation (the 15th day after it becomes in arrears). All the data on the physical disks will be cleared and cannot be recovered. Please renew your CPM in time to avoid business interruption and data loss</br>
*A CPM will be isolated on the 8th day after it becomes in arrears. This grace period is subject to change. Please regularly visit Tencent Cloud's official website for the latest update. Please renew your CPM in a timely manner to avoid its unavailability due to isolation*
