## Overview

The lifecycle of CDH instance refers to the period ranging from its being purchased till its termination.



## Purchase of instances

All users can purchase CDHs on Tencent Cloud's official website.

1. Log in to [Tencent Cloud CDH Purchase Page](https://buy.cloud.tencent.com/cdh).
2. Select region, availability zone, model, quantity and purchased usage period, and then confirm your order.
3. You can pay with your balance, Tenpay, Wechat Pay or QQ Wallet.
4. The CDH you purchased is assigned immediately after the order is paid. You can log in to the console to assign CVM instances.




## Expiration of CDH instances

CDH instances are only available in prepaid mode and cannot be terminated by users before expiration. It is reclaimed after a certain time following the expiration. You can renew CDH instances through manual or auto renewal at any time to avoid data loss or interruption of service due to instances being terminated by the system upon expiration.



Seven days before the expiration of prepaid CDHs, we will send you an expiration alert message every two days. The alert message will be sent by email and SMS to Tencent Cloud account creator and all the collaborators.



## Expiration of CDH instances

On the day when prepaid CDHs expire and every two days after that, we will send you an arrears isolation alert message to Tencent Cloud account creator and all the collaborators via email and SMS.



### Renewal of CDH instances

- Log in to [CDH Console](https://console.cloud.tencent.com/cvm/cdh).
- For prepaid CDH instances to be renewed, click on "Renew" in the operation column on the right side.
- In the pop-up box of CVM renewal, select the time for renewal, and click "OK".
- Make the payment to finish the renewal of CDH instances.





## Recovery mechanism of CDH instances

- Seven days before the expiration of CDH resources, we will send you a renewal reminder notice.
- For sufficient account balance, the CDHs with auto renewal setting will perform renewal automatically upon expiration.
- If a CDH is not renewed before the expiry date (including), we will end its service (**network outage and shutdown of all CVM instances** on CDH and CDH devices, and service shutdown of all cloud disks of the CVM with data saved only) from the expiry date.
- You can renew CDHs in the recycle bin within 7 days after the expiration to recover them. The network and cloud disk of the CDH and its CVMs are recovered as well.
- If a CDH is not renewed with 7 days (including) after the expiration, the CDH is reclaimed by 0:00 on the 8th day after expiration. **All CVM instances on the CDH are terminated**, and **all data on local disk and cloud disk of the CVM are cleared and cannot be restored**.


