## Activating ISMS
### Sign up for a Tencent Cloud account
You need to sign up for a Tencent Cloud account if you don't have one. For more information on registration, please see [Sign up for Tencent Cloud](https://cloud.tencent.com/document/product/378/9603).
If you already have a Tencent Cloud account, go to the next step.

### Log in to the Tencent Cloud SMS Console
Log in to the Tencent Cloud **[SMS Console](https://console.cloud.tencent.com/sms)**. You need to apply for the activation of SMS upon the first login.
![](https://main.qcloudimg.com/raw/4208ecfb62d65be1dc42a17f5976f1f6.png)
### Apply for activation of ISMS
If your account has not gone through identity verification, go to [Account Center](https://console.cloud.tencent.com/developer) for identity verification. For more information, please see [here](https://cloud.tencent.com/document/product/378/3629).
If you have completed identity verification, click **Start connection**.

> You must complete enterprise verification before applying for activation of ISMS. Verified individual users can submit a ticket to modify the verification information.


## Preparations
>1. A complete SMS message consists of **SMS signature** and **SMS body**. You can set different message body templates based on business needs, and then combine the signature and body to form a final display. **SMS signature + SMS body = final display**.
>2. Our review will be completed within half a work day after the SMS signature and template are submitted. If necessary, you can set a mobile number and email address to receive the notification of SMS message content audit for this project.

![](https://main.qcloudimg.com/raw/7a2f506fb2b2a6773ec9c9223208b9ce.png)
The final SMS message sent to users is as follows:
![](https://main.qcloudimg.com/raw/58425f39c5da3f339d325ee7534e4062.png)

### Add project
Add a project to get SDK AppID and App Key. For more information, please see [Add Project](https://cloud.tencent.com/document/product/382/18053#.E6.B7.BB.E5.8A.A0.E5.BA.94.E7.94.A8).

### Create signature
A complete SMS message consists of SMS signature and SMS body. Rules for SMS signatures can be found in [Signature Audit Criteria](https://cloud.tencent.com/document/product/382/13444#.E7.AD.BE.E5.90.8D.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86). For more information on how to create a signature, please see [Create Signature](https://cloud.tencent.com/document/product/382/18053#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D).

### Create body template
Rules for message body templates can be found in [Audit Criteria for Common SMS Messages](https://cloud.tencent.com/document/product/382/13444#.E6.99.AE.E9.80.9A.E7.9F.AD.E4.BF.A1.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86). For more information on how to create a message body template, please see [Create Message Body Template](https://cloud.tencent.com/document/product/382/18053#.E5.88.9B.E5.BB.BA.E6.AD.A3.E6.96.87.E6.A8.A1.E7.89.88).


## Sending ISMS Messages
After the message body template and SMS signature are approved, you can send SMS messages through the console, cloud SMS API or SDK.
- For more information on how to send SMS messages through the console, please see [Send Text Messages](https://intl.cloud.tencent.com/document/product/382/18053).
- For more information on how to send SMS messages using API, please see [API Documentation](https://cloud.tencent.com/document/product/382/13297).
- For more information on how to send SMS messages using SDK, please see [SDK Documentation](https://cloud.tencent.com/document/product/382/5804).


### View SMS message delivery result
After an SMS message is successfully sent, you can view the delivery result and statistics in [Statistical Analysis of ISMS Messages](https://cloud.tencent.com/document/product/382/18054).

