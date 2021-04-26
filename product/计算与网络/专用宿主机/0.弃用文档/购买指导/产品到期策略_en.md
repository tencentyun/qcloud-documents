## 1. Expiration of CDH

![cdhdq](http://mc.qcloudimg.com/static/img/6db78edb3d692f865cf9b6e634c9dfba/image.png)

> **Expiration Forewarning**

CDH is only available in prepaid mode. Seven days before the expiration of prepaid CDHs, we will send you an expiration alert message every two days. The alert message will be sent by email and SMS to Tencent Cloud account creator and all the collaborators.

> **Isolation Alert**

On the day when prepaid CDHs expire and every two days after that, we will send you an expiration isolation alert message to Tencent Cloud account creator and all the collaborators via email and SMS.

> **Recovery Mechanism**

- Seven days before the expiration of CDH resources, we will send you a renewal reminder.
- For sufficient account balance, the CDHs with auto renewal setting will perform renewal automatically upon expiration.
- If a CDH is not renewed before the expiry date (including), we will end its service (**network outage and shutdown of all dedicated CVMs** on CDHs and CDH devices, and service shutdown of all cloud disks of the CVM with data saved only) from the expiry date.
- You can renew and recover the CDHs in the recycle bin within 7 days after the expiration, during which, you can resume the network and cloud disk of the CDH and its CVMs after renewal.
- If a CDH is not renewed with 7 days (including) after the expiration, we will release the resources from 0:00 on the 8th day after expiration. **All dedicated CVMs on the CDH will be terminated**, and **all data on local disk and cloud disk of the CVM will be cleared and cannot be restored**.

## 2. Pay-per-use network in arrears

![netdq](http://mc.qcloudimg.com/static/img/3c1469541cb231b8b6ce32eb65fa8cca/image.png)

> **Balance Forewarning**

Network traffic consumption may fluctuate significantly and is hard to predict. Therefore, balance alert is not supported.

> **Arrears Forewarning**

Pay-per-use network are charged per hour based on the actual outbound traffic. When your account balance is a negative value, we will notify Tencent Cloud account creator and all the collaborators via email and SMS.

> **Arrears Processing**

- When your balance is less than 0, you can still use pay-per-use network for a further of ** 2 **hours with the usage being further billed.

  We will notify the Tencent Cloud account creator and all the collaborators via email and SMS that the balance is less than 0 and the network service will be suspended after 2 hours.

- If the balance remains below 0 after **2** hours, the dedicated CVMs on the CDHs will **disconnect the network and stop billing**. The CDHs remain available.

  When network service is about to be disconnected, we will immediately notify the Tencent Cloud account creator and all the collaborators via email and SMS that the balance is insufficient and the network will be disconnected soon.

- If the balance is topped up to an amount greater than 0 within **2 hours**, the traffic service will resume its availability. In this case, check the network configuration and restore the binding between affected CVMs and load balancers. The network service will remain unavailable until your account balance is topped up to an amount greater than 0.

- After top-up, we will notify the Tencent Cloud account creator and all the collaborators via email and SMS whether the top-up is completed, and the current balance is sufficient to resume the network service (If the balance >0, the network service will be resumed; otherwise it will not.)

## 3. Pay-per-use cloud disk in arrears

![cbsdq](http://mc.qcloudimg.com/static/img/f9d2f2e6808c7d1e458e70e8d1678c5d/image.png)

> **Balance Forewarning**

We will estimate the remaining available period of your account based on your usage of pay-by-usage resources under your account and your balance over the past 24 hours. We will send you a balance alert message if the period is less than 5 days. The alert message will be sent by email and SMS to Tencent Cloud account creator and all the collaborators.

Your actual resource consumption may change, so there may be some error in the balance forewarning.

> **Arrears Forewarning**

For pay-per-use resources, fees are deducted on the hour. When your account balance is a negative value, we will notify Tencent Cloud account creator and all the collaborators via email and SMS.

> **Arrears Processing**

- 2 hours later after your account is in arrears, your CBS will stop services and billing.
- After automatic shutdown, if your account balance is not greater than 0, you cannot perform read/write operations; if your balance is greater than 0, billing continues and you can perform read/write operations.

## 4. Validity of dedicated CVMs

The validity of dedicated CVMs is the same as those of the CDHs where the CVM resides.

* If a CDH is not renewed before the expiry date (including), we will end its service (**network outage and shutdown of all dedicated CVMs** on CDHs and CDH devices, and service shutdown of all cloud disks of the CVM with data saved only) from the expiry date.
* If a CDH is not renewed with 7 days (including) after the expiration, we will release the resources from 0:00 on the 8th day after expiration. **All dedicated CVMs will be terminated**, and **all data on local disk and cloud disk of the CVM will be cleared and cannot be restored**.
