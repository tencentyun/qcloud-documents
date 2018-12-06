This document describes the reclaiming mechanism of an instance and the operation method for recovering an instance. For more information on expiration, please see [Expiry Reminder](/doc/product/213/2181). 

## Reclaiming Instance
Tencent Cloud Recycle Bin is a cloud service reclaiming mechanism. The prepaid instance will be shut down on the expiry date or on the day when it is actively terminated before expiry, and then is automatically put into the recycle bin. The instance configured with auto renewal is automatically renewed if account balance is sufficient. No reclaiming mechanism is provided for postpaid instances.

 - **Retention time:** The instance is retained for 7 calendar days in the recycle bin.
 - **Expiry processing:** If the instance is not renewed within 7 days, the system will release resources and start to automatically [Terminate Instance](/doc/product/213/4930).
 - **Mounting relationship:** After being put into the recycle bin, the instance will be **forced to terminate** the mounting relationship with CLB, elastic public IP, elastic cloud disk, secondary ENI, and Classiclink. The mounting relationship **cannot be recovered** after renewal, you have to reset it.
 - **Operation limits:** You can only [**renew**](/doc/product/213/4931) or [**terminate**](/doc/product/213/4930) the instances in the recycle bin.

## Recovering Instance
 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
 2. On the left navigation bar, click **Recycle Bin** -> **CVM Recycle Bin** to enter the CVM reclaiming list.
 3. Recover single instance: Find the instance to be recovered in the list, click **Recover** button, and complete the renewal payment.
 4. Recover instances in batch: Select all instances to be recovered, click **Recover in Batch** on the top, and complete the renewal payment.


