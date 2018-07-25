## Prepaid CVMs
### Expiration alert
You will receive an expiration alert message 7 days before the expiration of prepaid cloud resources. The alert message will be sent to Tencent Cloud account creator, global resource collaborators and financial collaborators via email and SMS.

### Arrears alert
You will receive an arrears alert on and after the day your prepaid CVM expires. The alert message will be sent to Tencent Cloud account creator and all the collaborators via email and SMS.

### Reclaiming mechanism
- You will receive a renewal notice 7 days before the expiration of cloud resources. 
- If your account balance is sufficient, the device configured with auto renewal is automatically renewed on the expiry date.
- If your CVM hasn't been renewed before the expiry date (including), the system will end its service (network outage and service shutdown with data saved only) from the expiry date. The CVM is removed into the recycle bin.
After being put into the recycle bin, the CVM will be **forced to terminate** the mounting relationship with EIPs, elastic cloud disks, secondary ENIs, and Classiclink. The mounting relationship **cannot be recovered** after renewal, and you have to reset it.
- You can renew and recover the instance in the recycle bin within 7 days after the expiration. Note: **The renewal period of the renewed and recovered instance starts on the expiry date of the previous period.**
- If your CVM instance has not been renewed within 7 days (including the 7th day) upon its expiration, its resources will be released at 00:00 on the 8th day. **All the data of the expired instance is cleared and cannot be recovered**.

## Postpaid CVMs
### Arrears alert
For postpaid resources, fees are deducted on the hour. When your account balance is negative, we will notify Tencent Cloud account creator, global resource collaborators and financial collaborators via email and SMS.

### Arrears processing
The CVM can still be used and billed **within 2 hours** after your account balance becomes negative.
After 2 hours, the CVM will be automatically shut down and the billing will be stopped.
**After automatic shutdown:**
- Within 24 hours, when the balance is topped up to an amount greater than 0, you can start up the CVM and the billing will continue.
- Within 24 hours, if your account balance is not topped up to an amount greater than 0, you cannot start up the CVM.
- If your balance has been negative for 24 hours, the postpaid CVM will be reclaimed, and all data will be cleared and cannot be recovered.
When reclaiming the CVM, we will notify the Tencent Cloud account creator and all the collaborators via email and SMS.

> **Notes:** 
>- When you do not use a postpaid resource any longer, **please terminate it as soon as possible** to avoid further fee deduction.
>- After the CVM is terminated or reclaimed, the data will be cleared and cannot be recovered.
>- Since your actual resource consumption may change from time to time, some deviation in the balance alert may exist.

## Network Billed by Traffic
### Balance alert
Network traffic consumption may fluctuate significantly and is hard to predict. Therefore, balance alert is not supported.

### Arrears alert
The network billed by traffic can still be used and billed **within 2 hours** after your balance becomes negative. After 2 hours, the network service billed by traffic will be shut down.

After the balance is topped up to an amount greater than 0, the service is resumed. Please check the network settings and resume the binding of the affected CVM and load balancers.

