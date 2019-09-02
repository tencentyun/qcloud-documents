## Expiry Reminder for Prepaid Cloud Disks

### Expiration Reminder
Seven days before the expiration of prepaid resources, we will send you an expiration reminding message every two days to Tencent Cloud account creator and all the collaborators via email and SMS.

### Arrears Reminder
On the day when prepaid resources expire and every two days after that, we will send you an arrears isolation reminding message to Tencent Cloud account creator and all the collaborators via email and SMS.

### Reclaiming Mechanism
- Seven days before the expiration of CBS resources, we will send you a renewal reminder. 
- You can continue using the cloud services for a further period of **seven days** after the expiration. We will send you an expiry reminder for such cloud services, and you must renew them as soon as possible.
- From the eighth day after the expiration, this CBS cannot be used (for reading/writing), and will be put into the **Recycle Bin**. You can still view devices and renew it on the Recycle Bin Console page.
- CBS resources in the recycle bin will be retained for **seven days**. If the CBS in the recycle bin is not renewed within 7 days, the resources will be reclaimed by the system. The data will be cleared and cannot be recovered. 
- In other words, there are **7-day availability duration** and **7-day unavailability duration** for the expired CBS. Within the 14 days, you can opt to renew the device. If your balance is sufficient and auto renewal is set for the device, the system will perform renewal automatically on the expiration date.

## Expiry Reminder for Postpaid Cloud Disks
 
 ![](https://main.qcloudimg.com/raw/3a50706a27bfc92a2a52d524e04beca9.png)
 
### Balance Reminder
We will estimate the remaining available period of your account based on your usage of postpaid resources under your account and your balance over the past 24 hours. We will send you a balance reminding message if the remaining period is less than 5 days. The reminding message will be sent to Tencent Cloud account creator and all the collaborators via email and SMS.

### Arrears Reminder
For postpaid resources, fees are deducted on the hour. When your account balance is a negative value (Point 1 in the figure above), we will notify Tencent Cloud account creator and all the collaborators via email and SMS.

### Arrears Processing

After 2 hours passes since your account goes into arrears (Point 2 in the figure above), your CBS service and the billing will be stopped.

Within 24 hours after automatic shutdown, if your account balance is not greater than 0, you cannot perform read/write operations; if your balance is greater than 0, the billing continues and you can perform read/write operations.

After automatic shutdown, if your negative balance lasts for 24 hours (Point 3 in the figure above), the postpaid CBS will be reclaimed, and all data will be cleared and <font color="red">cannot be recovered</font>.

When reclaiming the CBS, we will notify the Tencent Cloud account creator and all the collaborators via email and SMS.

> Note: 
- When you do not use postpaid resources any longer, **terminate them as soon as possible**, to avoid further fee deduction.
- After the resource is terminated or reclaimed, the data will be cleared and cannot be recovered.
- Since your actual resource consumption changes from time to time, some deviation in balance reminder may exist.
