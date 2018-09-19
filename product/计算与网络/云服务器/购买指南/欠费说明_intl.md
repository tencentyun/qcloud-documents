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

