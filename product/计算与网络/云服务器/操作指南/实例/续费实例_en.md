Unlike postpaid instances, pripaid instance cannot be terminated by users. It will be recycled by the system after a certain time following the expiration. You can renew the instance with an annual or monthly plan through manual or auto renewal at any time to avoid data loss or interruption of service due to instances being terminated by the system upon expiration.

## Instance Renewal

### Renew instance via the console
You can renew the instance with an annual or monthly plan before the expiry date to prevent services interruption due to shutdown when it expires:

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) For CVM instances with an annual or monthly plan to be renewed, click on "Renew" on the action bar to the right side.

3) In the pop-up box of host renewal, select the time for renewal and select whether or not to adjust the bandwidth, and then click "OK".

4) After making the payment, you can renew CVM instances.
![](//mccdn.qcloud.com/img568c94be10169.png)

### Renew instance via API
Users can use Renew Instance API to renew instances. For details, see [Renew Prepaid Instances API](https://cloud.tencent.com/doc/api/229/1348).

## Set up auto renewal

## Set up auto renewal via the console
At the same time, you can also set auto renewal for CVM instance with an annual or monthly plan to avoid the same manual operation of renewal every time when it is about to expire:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com), move the mouse pointer to the top right corner of your account name, and select "Renew" in the menu.

2) To renew prepaid CVM instances, click on "Set to Auto Renew" on the action bar to the right side.

3) Click "OK" in the pop-up box of auto renewal.

For instances with auto renewal setting, it will automatically deduct the charge for next billing period at the expiry date. If your account balance is sufficient, the instance will be automatically advanced to the next cycle.

## Set up auto renewal via API
Users can use Set Auto Renew API to automatically renew instances. For details, see [Set Auto Renewal for Instances via API](https://cloud.tencent.com/doc/api/229/1746).

## Renewal for same expiry date
Tencent Cloud provides the function of instance renewal for same expiry date. By specifying same expiry time for Cloud Services created by users at different time, users can be relieved from repetitive renewal operation for services with different expiry date and will be able to end all services at a specified date so as to save costs. For more information about renewal for same expiry date, see [Set Same Expiry Date](https://cloud.tencent.com/doc/product/285/1894#.E4.BA.94.E3.80.81.E8.AE.BE.E7.BD.AE.E7.BB.9F.E4.B8.80.E5.88.B0.E6.9C.9F.E6.97.A5).