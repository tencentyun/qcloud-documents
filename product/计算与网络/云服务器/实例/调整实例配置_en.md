The hardware for Tencent Cloud instances can be adjusted easily and quickly, which is a key feature of cloud virtual machines that makes them more usable than physical machines. In the initial stage of application when the request volume is low, you can choose low hardware configuration. As the application quickly expands and the request volume surges, you can quickly adjust the hardware configuration to process the services faster and better cater to your changing demand.

##  Upgrade Configuration
### Upgrade on Console
>This operation is only available to CVM instances which are <font color="red">**shut down**</font> and <font color="red">**both the system and data disks of which are cloud disks**</font>.

1) Go to [Tencent Cloud Console](https://console.qcloud.com/), and click the "Cloud Virtual Machine" tab on the top to enter the CVM list.

2) Select the desired CVM instance, and click "More" - "Adjust Configuration" to its right.

3) In the "Adjust Configuration" box that pops up, select the target configuration, and complete payment or confirm to adjust the CVM configuration instantly.

![](//mccdn.qcloud.com/static/img/aff398296092bf67d5682849a049f39e/image.png)
![](//mccdn.qcloud.com/static/img/81b7faa667692506b4ee7f58e7480445/image.png)

### Upgrade via API
You can use the ResizeInstance and ResizeInstanceHour APIs to upgrade the instance configuration. For details, see [Adjust Prepaid Instance Configuration API](https://www.qcloud.com/doc/api/229/1306) and [Adjust Postpaid  Instance Configuration API](https://www.qcloud.com/doc/api/229/1306).

## Degrade Configuration
### Degrade configuration of prepaid instances
>The adjustment can only be made to CVM instances that are <font color="red">**shut down**</font> and <font color="red">**both the system and data disks of which are cloud disks**</font>.

1) Go to [Tencent Cloud Console](https://console.qcloud.com/), and click the "Cloud Virtual Machine" tab on the top to enter the CVM list.

2) Select the desired **prepaid** CVM instance，click "More" - "Adjust Configuration" to its right.

3) In the "Adjust Configuration" box that pops up, select the target configuration, and click "OK" to degrade the CVM configuration and extend the expiry time instantly.
![](//mccdn.qcloud.com/static/img/21681e206c9b96374135cdcf1d83bf22/image.png)

### Degrade configuration of postpaid instances
>The adjustment can only be made to CVM instances that are <font color="red">**shut down**</font> and <font color="red">**both the system and data disks of which are cloud disks**</font>.

1) Go to [Tencent Cloud Console](https://console.qcloud.com/), and click the "Cloud Virtual Machine" tab on the top to enter the CVM list.

2) Select the desired **postpaid** CVM instance, click "More" - "Adjust Configuration" to its right.

3) In the "Adjust Configuration" box that pops up, select the target configuration, and click "OK" to degrade the CVM configuration instantly.
![](//mccdn.qcloud.com/static/img/52fb811d1c55fa1f3c5905804ce75bef/image.png)