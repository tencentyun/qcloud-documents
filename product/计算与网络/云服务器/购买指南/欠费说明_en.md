## 1. Expiration reminder for prepaid CVMs 

### 1.1. Expiration warning
Seven days before the expiration of annual/monthly-package resources, we will push an expiration warning message every two days to Tencent Cloud account creators and all collaborators by Email and SMS. 

### 1.2. Arrears warning
On the day when prepaid resources expire and every two days after that, we will push an expiration warning message to Tencent Cloud account creators and all collaborators by Email and SMS. 

### 1.3. Reclamation mechanism
- Seven days before the expiration of CVMs, the system will send you a renewal reminder notice. 
- If your balance is sufficient, for the devices that you have set automatic renewal, automatic renewal will be completed on the expiration date.
- If your CVM is not renewed before expiration (including the expiration date), the system will, at the expiration time, stop the services (disconnecting and shutting down the device and only keeping data).
- Within 7 days after expiration, you can still recover data from the recycle bin after renewing your device.
- If your CVM is not renewed within 7 days (including the 7th day), the system will begin releasing resources at 0:00 on the 8th day after expiration. **The data will be cleared and cannot be recovered.**
- After a CVM is put into the Recycle Bin, its mounting of load balance, elastic public network IP, elastic COS, auxiliary network card, basic network interoperability will be **removed forcedly**. After its recovery through renewal, its mounting **will not be restored** and you need to configure them again.

## 2.	Expiration reminder for postpaid CVMs
 
 ![](//mccdn.qcloud.com/img567f91951599d.png)
 
### 2.1. Balance warning
The system will estimate the period you balance can last every day based on your consumption of the pay-per-use resources under your account and your balance. If the period is less than 5 days, we will push a balance warning message to you. The warning message will be sent by Email and SMS to the Tencent Cloud account creator and all collaborators.

### 2.2. Arrears warning
For pay-per-use resources, fees are deducted every hour on the hour. When your balance becomes negative (point 1 in the figure above), we will notify Tencent Cloud account creators and all collaborators by Email and SMS.

### 2.3. Arrears processing
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


## 3.	Expiration reminder for pay-by-traffic network
 
 
### 3.1. Balance warning
Traffic consumption is highly fluctuated and is very difficult to forecast; therefore, we do not provide balance warning.

### 3.2. Arrears warning
For pay-by-traffic network, fees are deducted every hour on the hour. When your balance becomes negative, we will notify Tencent Cloud account creators and all collaborators by Email and SMS.

### 3.3. Arrears processing
Within **2** hours from the point when your balance becomes negative, your pay-by-traffic network remains usable and continues to deduct fees. 2 hours later, your pay-by-traffic network will be out of service.


When your balance becomes positive, the traffic service will be recovered. Check the network settings and restore mounting of load balance on the CVM.

