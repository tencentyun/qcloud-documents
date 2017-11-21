

## 1.	Expiration reminder for postpaid CVMs
 
![ ](//mc.qcloudimg.com/static/img/3a50706a27bfc92a2a52d524e04beca9/image.png)
 
### 1.1. Balance warning
The system will estimate the period you balance can last every day based on your consumption of the pay-per-use resources under your account and your balance. If the period is less than 5 days, we will push a balance warning message to you. The warning message will be sent by Email and SMS to the Tencent Cloud account creator and all collaborators.

### 1.2. Arrears warning
For pay-per-use resources, fees are deducted every hour on the hour. When your balance becomes negative (point 1 in the figure above), we will notify Tencent Cloud account creators and all collaborators by Email and SMS.

### 1.3. Arrears processing
Within **2** hours from the point when your balance becomes negative, your CVM remains usable and continues to deduct fees.

2 hours (point 2 in the above figure) later, your CVM will automatically shut down and stop deducting fees.

Within 24 hours after automatic shutdown, if your balance is not greater than 0, your CVM cannot start; if your balance is greater than 0, billing continues and your CVM can start.

After automatic shutdown, if your negative balance lasts for 24 hours (point 3 in the figure), the postpaid CVM will be reclaimed, and all data will be cleared and cannot be recovered.

When reclaiming the CVM, we will notify the Tencent Cloud account creator and all collaborators by Email and SMS.

> Note: 
> 
- When you do not use prepaid resources any longer, **please terminate them promptly** to stop it from charging.
- After a CVM is terminated/reclaimed, its data will be cleared and cannot be recovered.
- When a CVM is isolated (in arrears for more than two hours), its mounting relationship with the Cloud Load Balance will be removed forcedly.
- Your actual resource consumption may constantly change, so balance warning may have some error.


## 2.	Expiration reminder for pay-by-traffic network
 
 
### 2.1. Balance warning
Traffic consumption is highly fluctuated and is very difficult to forecast; therefore, we do not provide balance warning.

### 2.2. Arrears warning
For pay-by-traffic network, fees are deducted every hour on the hour. When your balance becomes negative, we will notify Tencent Cloud account creators and all collaborators by Email and SMS.

### 2.3. Arrears processing
Within **2** hours from the point when your balance becomes negative, your pay-by-traffic network remains usable and continues to deduct fees. 2 hours later, your pay-by-traffic network will be out of service.


When your balance becomes positive, the traffic service will be recovered. Check the network settings and restore mounting of load balance on the CVM.

