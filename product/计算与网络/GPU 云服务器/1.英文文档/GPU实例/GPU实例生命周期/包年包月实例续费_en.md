You can renew or enable auto renewal for a prepaid instance at any time before the end of its lifecycle to prevent data loss and service interruption due to termination of instance upon its expiration.

## Renewing Instance

### Renew instance via console
You can renew a prepaid instance before its expiration to avoid service interruption caused by a shutdown.

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Select **GPU G2** from　instance type, then choose the prepaid GCC instance you want to renew. Click **Renew** in the operation column on the right.

3) In the pop-up window, select the renewal period and adjust the bandwidth if necessary, and then click **OK**.

4) The GCC instance is renewed when your payment is received.


### Renew instance via API
You can use RenewInstance API to renew instances. For more information, please see [API for Renewing Instance](https://cloud.tencent.com/doc/api/229/1348).

## Setting Auto Renewal

### Set auto renewal via console
You can also set auto renewal for prepaid GCC instances to eliminate the need to renew the instances whenever they are about to expire:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com), mouse-over to your account name at the top right corner, and then select **Renew**.

2) For the prepaid GCC instances you want to renew, click **Set Auto Renewal** on the operation column on the right.

3) Click **OK** in the pop-up of auto renewal.

For instances set to auto renewal, the charge for the next billing period is automatically deducted from the balance on the expiry date. If you have a sufficient account balance, the instance goes into the next billing period automatically.

> "Batch Renewal" is not available to prepaid GCC instances now.

## Set auto renewal via API
You can use SetAutoRenew API to automatically renew instances. For more information, please see [SetAutoRenew API](https://cloud.tencent.com/doc/api/229/1746).

## Renewing to Unified Expiry Date
Tencent Cloud allows you to renew instances to the unified expiry date. By specifying the unified expiry date for cloud products created at different times, you can be freed from repetitive renewal operations for services with different expiry dates and stop all services at the specified expiry date to save costs. For more information about the unified expiry date, please see [here](https://cloud.tencent.com/doc/product/285/1894#.E4.BA.94.E3.80.81.E8.AE.BE.E7.BD.AE.E7.BB.9F.E4.B8.80.E5.88.B0.E6.9C.9F.E6.97.A5).


