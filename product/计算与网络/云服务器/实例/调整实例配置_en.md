Specifications of CVM instances can be adjusted easily and quickly. In the initial stage of application when the request volume is low, you can choose low hardware configuration. As the application quickly expands and the request volume surges, you can quickly adjust the hardware configuration to process the services faster and better cater to your changing demand.

##  Upgrading Configuration
### Upgrading on Console
>This operation is only available to CVM instances which are **shut down** and **both the system and data disks of which are cloud disks**.


2) Select the desired CVM instance, and click **More - Adjust Configuration** to its right.

3) In the **Adjust Configuration** box that pops up, select the target configuration, and complete payment or confirm to adjust the CVM configuration instantly.

![](//mc.qcloudimg.com/static/img/10c777b1cea234cec1ca4eb250b3b179/image.png)

### Upgrading via API
You can use the ResizeInstance and ResizeInstanceHour APIs to upgrade the instance configuration. For details, see [Adjust Prepaid Instance Configuration API](https://cloud.tencent.com/doc/api/229/1306) and [Adjust Postpaid  Instance Configuration API](https://cloud.tencent.com/doc/api/229/1306).

## Degrading Configuration
### Degrading Postpaid Instances
>The adjustment can only be made to CVM instances that are **shut down** and **both the system and data disks of which are cloud disks**.

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm), and select **CVM** from the left. 

2) Select the desired postpaid CVM instance, click **More - Adjust Configuration** to its right.

3) In the **Adjust Configuration** box popped up, select the target configuration, and click **OK** to degrade the CVM configuration instantly.
![](//mc.qcloudimg.com/static/img/d36be6bddbd184978ea6000de0531303/image.png)
