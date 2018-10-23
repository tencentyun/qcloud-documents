## Activating ISMS
### Sign up for a Tencent Cloud account
You need to sign up for a Tencent Cloud account if you don't have one. For more information on registration, please see [Sign up for Tencent Cloud](https://intl.cloud.tencent.com/document/product/378/9603).
If you already have a Tencent Cloud account, go to the next step.

### Log in to the Tencent Cloud SMS Console
Log in to the Tencent Cloud **[SMS Console](https://console.cloud.tencent.com/sms)**. You need to apply for the activation of SMS upon the first login.
![](https://main.qcloudimg.com/raw/4208ecfb62d65be1dc42a17f5976f1f6.png)
### Apply for activation of ISMS
If your account has not gone through identity verification, go to [Account Center](https://console.cloud.tencent.com/developer) for identity verification. For more information, please see [here](https://intl.cloud.tencent.com/document/product/378/3629).
If you have completed identity verification, click **Start connection**.

> You must complete enterprise verification before applying for activation of ISMS. Verified individual users can submit a ticket to modify the verification information.


## Preparations
>1. A complete SMS message consists of **SMS signature** and **SMS body**. You can set different message body templates based on business needs, and then combine the signature and body to form a final display. **SMS signature + SMS body = final display**.
>2. Our review will be completed within half a work day after the SMS signature and template are submitted. If necessary, you can set a mobile number and email address to receive the notification of SMS message content audit for this project.

![](https://main.qcloudimg.com/raw/7a2f506fb2b2a6773ec9c9223208b9ce.png)
The final SMS message sent to users is as follows:
![](https://main.qcloudimg.com/raw/58425f39c5da3f339d325ee7534e4062.png)

### Add project
Add a project to get SDK AppID and App Key. For more information, please see [Add Project](https://intl.cloud.tencent.com/document/product/382/18053#add-project).

### Create signature
A complete SMS message consists of SMS signature and SMS body. Rules for SMS signatures can be found in [Signature Audit Criteria](https://intl.cloud.tencent.com/document/product/382/13444#signature-audit-criteria). For more information on how to create a signature, please see [Create Signature](https://intl.cloud.tencent.com/document/product/382/18053#create-signature).

### Create body template
Rules for message body templates can be found in [Audit Criteria for Common SMS Messages](https://intl.cloud.tencent.com/document/product/382/13444#audit-criteria-for-common-sms-messages). For more information on how to create a message body template, please see [Create Message Body Template](https://intl.cloud.tencent.com/document/product/382/18053#create-body-template).


## Sending ISMS Messages
After the message body template and SMS signature are approved, you can send SMS messages through the console, cloud SMS API or SDK.
- For more information on how to send SMS messages through the console, please see [Send Text Messages](https://intl.cloud.tencent.com/document/product/382/18053).
- For more information on how to send SMS messages using API, please see [API Documentation](https://intl.cloud.tencent.com/document/product/382/13297).



### View SMS message delivery result
After an SMS message is successfully sent, you can view the delivery result and statistics in [Statistical Analysis of ISMS Messages](https://intl.cloud.tencent.com/document/product/382/18054).

