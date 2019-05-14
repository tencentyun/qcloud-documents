## Expiry Reminder
### Arrears reminder for CFS postpaid resources

![](https://main.qcloudimg.com/raw/2b456d2454d45297292f63d2551c3951.png)

### Balance alert
We will estimate the remaining available period of your account based on your usage of postpaid resources under your account and your balance over the past 24 hours. We will send you a balance alert message if the period is less than 5 days. The alert message will be sent by email and SMS to Tencent Cloud account creator and all the collaborators.


### Arrears alert
For postpaid resources, fees are deducted on the hour. When your account balance is a negative value, we will notify Tencent Cloud account creator and all the collaborators via email and SMS.


### Arrears processing
The CFS file system can be used normally within 24 hours after your account falls into arrears (the orange segment in the above figure), but there will be a prompt of suspense of the service on the console.

Within 24-168 hours(7 days) after the arrears (the red segment in the above figure), if your account balance is not topped up to an amount greater than 0, the CFS service will be suspended and the billing will be stopped. The file system cannot be read or written, and the console only supports top-up operations. When the balance is topped up to an amount greater than 0, the billing will continue and the file system can be read and written.

If your negative balance lasts for 7 days (the black segment in the above figure), the postpaid CFS file system will be reclaimed, and all data will be cleared and cannot be recovered.

Tencent Cloud account creator and all the collaborators will be notified of the reclaim via email and SMS.

Note:
	•	When you do not use a postpaid resource any longer, please terminate it as soon as possible to avoid further fee deduction.
	•	After the resource is terminated or reclaimed, the data will be cleared and cannot be recovered.
	•	Since your actual resource consumption may change from time to time, some deviation in the balance alert may exist.



