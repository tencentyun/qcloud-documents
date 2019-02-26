### Forewarning of Expiration
Seven days before your Ckafka instance expires, an expiration forewarning message is sent to you every other day. All forewarning messages are sent to Tencent Cloud account creator and all the collaborators via email and SMS.

### Forewarning of Arrears
From the day when your Ckafka instance expires, a forewarning message of isolation due to arrears is sent to you every other day. All forewarning messages are sent to Tencent Cloud account creator and all the collaborators via email and SMS.

### Reclaiming Mechanism
- Seven days before your Ckafka instance expires, a renewal reminder is sent to you by the system. 
- If your account balance is sufficient, the device configured with auto renewal is automatically renewed on the expiry date.
- If your CKafka instance hasn't been renewed on or before the expiry date, the service is suspended from the expiry date (your device is disconnected from network and shut down, CKafka messaging service is suspend, and only data is retained). Then, the CKafka instance is placed into the recycle bin.
After being reclaimed into the recycle bin, the CKafka instance is **forcibly unmounted* from the upstream and downstream components. When the instance is resumed upon renewal, the mounting relationship **cannot be restored**, which should be reconfigured.
- You can renew and resume the device in the recycle bin within 7 days after its expiration. Note: **The renewal period of the renewed and resumed instance starts on the expiry date of the previous period.**
- If your CKafka instance has not been renewed within 7 days (including the 7th day) upon its expiration, resources are released at 0:00 on the 8th day. **All the data of the expired instance is cleared and cannot be restored**.

