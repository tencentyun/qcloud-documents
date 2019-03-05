

## Expiry Reminder for Pay-by-usage Cloud Block Storage
 
![](//mc.qcloudimg.com/static/img/3a50706a27bfc92a2a52d524e04beca9/image.png)
 
### Balance Forewarning
We will estimate the remaining available period of your account based on your usage of pay-by-usage resources under your account and your balance over the past 24 hours. We will send you a balance forewarning message if the period is less than 5 days. The forewarning message will be sent by email and SMS to Tencent Cloud account creator and all the collaborators.

### Arrears Forewarning
For pay-by-usage resources, fees are deducted on the hour. When your account balance is a negative value (Point 1 in the figure above), we will notify Tencent Cloud account creator and all the collaborators via email and SMS.

### Arrears Processing

2 hours later after your account is in arrears (Point 2 in the figure above), your CBS will stop services and billing.

Within 24 hours after automatic shutdown, if your account balance is not greater than 0, you cannot perform read/write operations; if your balance is greater than 0, billing continues and you can perform read/write operations.

After automatic shutdown, if your negative balance lasts for 24 hours (Point 3 in the figure above), pay-by-usage CBS will be reclaimed, and all data will be cleared and CANNOT be recovered.

When reclaiming the CBS, we will notify the Tencent Cloud account creator and all the collaborators via email and SMS.

> Note: 
- When you do not use pay-by-usage resources any longer, **please terminate them promptly**, to avoid further fee deduction.
- After the resource is terminated or reclaimed, the data will be cleared and cannot be recovered.
- Your actual resource consumption may change, so there may be some error in the balance forewarning.
