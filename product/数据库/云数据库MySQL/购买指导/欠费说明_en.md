## 1. Expiry Reminder for Annual/Monthly-plan Cloud Database

### 1.1. Expiration Forewarning
Seven days before the expiration of annual/monthly-plan resources, we will send you an expiration forewarning message every two days to Tencent Cloud account creator and all the collaborators via email and SMS.

### 1.2. Arrears Forewarning
On the day when annual/monthly-plan resources expire and every two days after that, we will send you an arrears isolation forewarning message to Tencent Cloud account creator and all the collaborators via email and SMS.

### 1.3. Recovery Mechanism
- Seven days before the expiration of Cloud Services resources, we will send you a renewal reminder notice. 
- You can continue using the cloud services for a further period of**seven days** after the expiration. We will send you the expiry reminder for such cloud services, and you need to renew them as soon as possible.
- From the eighth day after the expiration, this cloud database cannot be used, and will be put into the **Recycle Bin**. You can still view devices and renew it on Recycle Bin Console page.
- Such in the recycle bin will be retained for **seven days**. If the cloud database in the recycle bin is not renewed within 7 days, the resources will be reclaimed by the system. The data will be cleared and cannot be recovered. 
- In other words, there are **7-day available duration** and **7-day unavailable duration** for the expired cloud database. Within the 14 days, you can opt to renew the device. If your balance is sufficient, for the device with auto renewal setting, it will perform renewal automatically on the expiration date.

## 2. Expiry Reminder for Pay-by-usage Cloud Database
 
 ![](//mccdn.qcloud.com/img567f91951599d.png)
 
### 2.1. Balance Forewarning
We will estimate the remaining available period of your account based on your usage of pay-by-usage resources under your account and your balance over the past 24 hours. We will send you a balance forewarning message if the period is less than 5 days. The forewarning message will be sent by email and SMS to Tencent Cloud account creator and all the collaborators.

### 2.2. Arrears Forewarning
For pay-by-usage resources, fees are deducted on the hour. When your account balance is a negative value (Point 1 in the figure above), we will notify Tencent Cloud account creator and all the collaborators via email and SMS.

### 2.3. Arrears Processing
Within **2** hours from the point when your balance becomes negative, your CVM remains usable and continues to deduct fees.

2 hours later (Point 2 in the figure above), your cloud database instance will automatically shut down and stop deducting fees.

Within 24 hours after automatic shutdown, if your account balance is not greater than 0, your cloud database instance cannot be started; if your balance is greater than 0, billing continues and your cloud database instance can be started.

After automatic shutdown, if your negative balance lasts for 24 hours (Point 3 in the figure above), pay-by-usage host will be reclaimed, and all data will be cleared and cannot be recovered.

When reclaiming the host, we will notify the Tencent Cloud account creator and all the collaborators via email and SMS.

> Note: 
- When you do not use pay-by-usage resources any longer, **please terminate them promptly**, to avoid further fee deduction.
- After the host is terminated or reclaimed, the data will be cleared and cannot be recovered.
- Your actual resource consumption may change, so there may be some error in the balance forewarning.


