This document introduces how to renew **prepaid instances**.
 - **Prepaid instance**: You can renew or set auto renewal for prepaid instances.
 - **Postpaid instance**: Postpaid instances can be automatically activated with sufficient balance in your account. For more information, please see [Online Top-up](/doc/product/555/7425) and [Offline Bank transfer Top-up](/doc/product/555/9901). You can also follow [Balance Alert Instruction](/doc/product/555/9942) to set alert to prevent your instance from being terminated.

## Instance Renewal
Prepaid instances can be renewed using various methods. The following example shows the renewal procedure on [CVM Console](https://console.cloud.tencent.com/cvm/). You can also view the document [Renewal Management via Console](https://console.cloud.tencent.com/account/renewal) to set auto renewal or renew to a certain time, etc.

### Instance Renewal via Console
 **Renew reclaimed instances:**
 
1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
2. On the left navigation bar, click **Recycle Bin** -> **CVM Recycle Bin** to enter the CVM reclaiming list.
3. Renew single instance: Find the instance to be renewed in the list, click **Recover** button on the right and finish the renewal payment.
4. Renew instances in batch: Select all instances to be renewed, click **Recover in Batch** on the top and finish the renewal payment.

**Renew running instances:**
 
1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
2. Renew single instance: Find the instance to be renewed in the list, click **Renew** button on the right and finish the renewal payment.
3. Renew instances in batch: Select all instances to be renewed, click **Recover** button on the top and finish the renewal payment.

### Instance Renewal via API
You can use the API RenewInstances to renew instances. For more information, please see [Instance Renewal](/doc/api/213/9392).

## Set Auto Renewal
You can also view the document [Renewal Management via Console](https://console.cloud.tencent.com/account/renewal) to set auto renewal or renew to a certain time, etc.

### Auto Renewal via Console
You can set auto renewal for prepaid instances to eliminate the need to renew the instances whenever they are about to expire:
 1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com), move the mouse cursor to **Fees** at the top right corner, and then select **Renew** in the menu.
 2. Click **Set Auto Renewal** on the right of the prepaid instance to be renewed.
 3. Click **OK** button in the popup dialog box.
 
For instances set to auto renewal, the charge for the next billing period is automatically deducted from the balance on the expiry date. If you have a sufficient account balance, the instance goes into the next billing period automatically.

### Auto Renewal via API
You can use the API SetAutoRenew to set auto renewal for instances. For more information, please see [Set Auto Renewal for Instances](/doc/api/229/1746).

