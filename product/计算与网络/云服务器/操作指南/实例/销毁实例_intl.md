This document describes how to terminate an instance. For more information on expiration, please see [Expiry Reminder](/doc/product/213/2181).

## Overview
 - **Manual termination:** Prepaid instances can be terminated by users before they expire. Instances are retained in the recycle bin for 7 days once terminated, and can also be terminated completely in the recycle bin. Postpaid instances can be terminated manually.
 - **Timed termination:** Timed termination is supported for postpaid instances. Select a time later than the current time to terminate a resource, with an accuracy down to second. You can set a new termination time to overwrite the previous one.
 - **Automatic termination:** Prepaid instances that have not been restored after being retained in the recycle bin for 7 calendar days are automatically terminated. Postpaid instances are automatically terminated when your account balance has remained below 0 for 24 hours. You can continue to use them if you finish [Renewal](/doc/product/213/6143) within a specified period of time.
 - **Instance data:** Local disks and non-elastic cloud disks mounted to instances are also terminated, and the data on these disks will be lost. Back up the data in advance. Elastic cloud disks are not affected.
 - **Billing:** When an instance is being terminated or has been terminated, no expenses related to this instance are incurred.
 - **EIP:** EIPs (including IPs on the secondary ENI) of a terminated instance are retained, and idle IPs may incur expenses. If you do not need these IPs, release them in time.

## Terminating Prepaid Instance
### Terminating Unexpired Instance on the Console

A prepaid instance can be terminated if you no longer need it. When an instance is being terminated or has been terminated, no expenses related to this instance are incurred. The instance is then moved to the CVM recycle bin and kept for 7 days, and services running on this instance are completely suspended.

When a prepaid instance is returned, the local disks and non-elastic cloud disks mounted to this instance are also returned, and the data stored on these disks will be lost. However, the elastic cloud disks mounted to this instance are retained, and the data will not be affected.

1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
2. Terminate a single instance: Find the instance to be terminated in the list, and click **Terminate** in the Operation column.
3. Terminate instances in batches: Select all the instances to be terminated, and click **Terminate** on the top.
4. In the pop-up box, confirm the information related to the CVM to be terminated, and click **OK**. Then, you are directed to **Check Refund Information** page.
5. Carefully check the refund information related to the instance. After **Confirm Refund** is submitted, refund is initiated and the instance is terminated.
  For more information on how to return a prepaid instance, please see [Refund Rules for Terminated Prepaid Instances](https://cloud.tencent.com/document/product/213/9711).

### Completely Terminating Prepaid Instances in Recycle Bin
You can terminate prepaid instances retained in the [Recycle Bin](/doc/product/213/4931) through the console.

  1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
  2. On the left navigation bar, click **Recycle Bin** -> **CVM Recycle Bin** to enter the CVM reclaiming list.
  3. Terminate a single instance: Find the instance to be terminated in the list, and click **Terminate** in the Operation column.
  4. Terminate instances in batches: Select all the instances to be terminated, and click **Terminate** on the top.
  5. Enter the verification code in the pop-up box, and click **OK** to complete the termination process.

## Terminating Postpaid Instances
A terminated postpaid instance is still visible in the console within a short period of time. It will be automatically removed from the instance list later, and its services will be completely suspended.
### Terminating Instances on the Console
  1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
  2. Terminate a single instance: Find the instance to be terminated in the list, and click **More** -> **CVM Status** -> **Terminate** on the right side.
  3. Terminate instances in batches: Select all the instances to be terminated. On the top of the list, click the **More** drop-down box, and then click **Terminate**. Reasons are given for instances that cannot be terminated.

### Setting Timed Termination
#### Setting at the Time of Purchase
1. Log in to the CVM purchase page.
2. Select Postpaid, region, model, image, storage, bandwidth and other data. Check "**Timed Termination**" on the "**Information Setting**" page, and set the date and time for timed termination, with an accuracy down to second.
  ![](https://mc.qcloudimg.com/static/img/378237a35e69bed7a4c61c8e9e6f3b99/image.jpg)
3. Click Enable, and all the instances with timed termination enabled will be terminated at the specified time.

### Setting via Console
  1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
  2. **Set timed termination for a single instance**: Find the instance to be terminated, and click **More** -> **CVM Status** -> **Terminate** on the right. Select Timed Termination in the pop-up box, and set the date and time for timed termination, with an accuracy down to second.
    ![](https://mc.qcloudimg.com/static/img/fa57dc1c68069846eed85b9c34952999/image.jpg)
  3. **Terminate instances in batches**: Select all the instances to be terminated. On the top of the list, click the **More** drop-down box, and then click **Terminate**. Set the date and time for timed termination, with an accuracy down to second. Reasons are given for instances that cannot be terminated.
    ![](https://mc.qcloudimg.com/static/img/0e3b3e907e71d51639d948bd579821f6/image.jpg)
  4. Confirm the information of instances for timed termination, and click "**OK**" to complete the setting.


### Canceling Timed Termination
  1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
  2. **Cancel timed termination for a single instance**: Find the instance for which timed termination needs to be canceled, then click the icon beside the "**Timed Termination**" in the "**CVM Billing Method**" column, and click "**Cancel**" in the pop-up tips.
    ![](https://mc.qcloudimg.com/static/img/f9e81105d8572e517ad9b128cf083f37/image.jpg)
  3. Confirm the information of the selected instance in the pop-up box, and click **OK**. Cancellation of timed termination takes effect immediately.
    ![](https://mc.qcloudimg.com/static/img/883b117e9e00f4b29da82738bf4ea241/image.jpg)



### Terminating Instances using API
For more information, please see the [API TerminateInstances](/doc/product/213/9395).

