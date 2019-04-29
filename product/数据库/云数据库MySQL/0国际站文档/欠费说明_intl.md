

## 1. Expiry Reminder for Pay-by-usage Cloud Database
 

![](//mc.qcloudimg.com/static/img/3a50706a27bfc92a2a52d524e04beca9/image.png) 
### 1.1. Balance Forewarning
We will estimate the remaining available period of your account based on your usage of pay-by-usage resources under your account and your balance over the past 24 hours. We will send you a balance forewarning message if the period is less than 5 days. The forewarning message will be sent by email and SMS to Tencent Cloud account creator and all the collaborators.

### 1.2. Arrears Forewarning
For pay-by-usage resources, fees are deducted on the hour. When your account balance is a negative value (Point 1 in the figure above), we will notify Tencent Cloud account creator and all the collaborators via email and SMS.

### 1.3. Arrears Processing
Within **2** hours from the point when your balance becomes negative, your CVM remains usable and continues to deduct fees.

2 hours later (Point 2 in the figure above), your cloud database instance will automatically shut down and stop deducting fees.

Within 24 hours after automatic shutdown, if your account balance is not greater than 0, your cloud database instance cannot be started; if your balance is greater than 0, billing continues and your cloud database instance can be started.

After automatic shutdown, if your negative balance lasts for 24 hours (Point 3 in the figure above), pay-by-usage host will be reclaimed, and all data will be cleared and cannot be recovered.

When reclaiming the host, we will notify the Tencent Cloud account creator and all the collaborators via email and SMS.

> Note: 
- When you do not use pay-by-usage resources any longer, **please terminate them promptly**, to avoid further fee deduction.
- After the host is terminated or reclaimed, the data will be cleared and cannot be recovered.
- Your actual resource consumption may change, so there may be some error in the balance forewarning.


