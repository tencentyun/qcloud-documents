## Activating SMS
### Signing up for a Tencent Cloud Account
You need to sign up for a Tencent Cloud account if you don't have one. For more information on registration procedure, please see [Sign up for Tencent Cloud](https://cloud.tencent.com/document/product/378/9603).
If you already have a Tencent Cloud account, go to next step.

### Logging in to Tencent Cloud SMS Console
Log in to the Tencent Cloud SMS [Console](https://console.cloud.tencent.com/sms). You need to apply for the activation of SMS upon first login.
![](//mc.qcloudimg.com/static/img/b389b56907d722fe1203ac39d539db42/image.png)
### Applying for Activation of SMS
If your account has not gone through identity verification, please go to [Account Center](https://console.cloud.tencent.com/developer) for identity verification. For more information, please see [Identity Verification Guide](https://cloud.tencent.com/document/product/378/3629).
If your identity verification is approved, click Access
 
![](//mc.qcloudimg.com/static/img/717125fa63eebc837a76896349eda666/image.png)
>For individual verification, some features of Tencent Cloud SMS may be restricted. For more information, please see [Individual Verification vs. Enterprise Verification](https://cloud.tencent.com/document/product/382/13444#.E4.B8.AA.E4.BA.BA.E8.AE.A4.E8.AF.81.E5.92.8C.E4.BC.81.E4.B8.9A.E8.AE.A4.E8.AF.81.E6.9D.83.E7.9B.8A.E5.8C.BA.E5.88.AB). Users who have gone through individual verification can also apply for enterprise verification to enable all the features.


## Preparations
>1. A complete SMS message is composed of a **signature** and a **main content**. You can configure different main content templates based on your business needs, and get a final message content by combining the signature and different content templates. **SMS signature + SMS main content = Final SMS message**.
>2. After the SMS signature and template are submitted, the approval process will be completed within half a work day. If necessary, you can set a commonly used phone number and email address to receive notification of review progress.

![](https://mc.qcloudimg.com/static/img/1223b6b179dbbbda7dcda06070eb4360/image.png)
Finally, you will receive an SMS message in the following format:
![](https://mc.qcloudimg.com/static/img/fe223e52477df4de3fec20eeb14ddc8f/image.png)

### Adding Application
Add an application to obtain SDK AppID and App Key. For more information, please see [Add Application](https://cloud.tencent.com/document/product/382/13483#.E6.B7.BB.E5.8A.A0.E5.BA.94.E7.94.A8).

### Creating Signature
A complete SMS message is composed of a signature and main content. For more information on SMS signature rules, please see [Signature Verification Standard](https://cloud.tencent.com/document/product/382/13444#.E7.AD.BE.E5.90.8D.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86). For more information on how to create a signature, please see [Create Signature](https://cloud.tencent.com/document/product/382/13481#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D).


### Creating Main Content Template
For more information on SMS main content template rules, please see [Verification Standard for Common SMS](https://cloud.tencent.com/document/product/382/13444#.E6.99.AE.E9.80.9A.E7.9F.AD.E4.BF.A1.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86). For more information on how to create a main content template, please see [Create Main Content Template](https://cloud.tencent.com/document/product/382/13481#.E5.88.9B.E5.BB.BA.E6.AD.A3.E6.96.87.E6.A8.A1.E7.89.88).

### Purchasing SMS Package
China text messages are billed on a prepaid basis. You can go to [Package Management](https://console.cloud.tencent.com/sms/packageList) to purchase SMS packages. For more information, please see [How to Purchase SMS Package](https://cloud.tencent.com/document/product/382/13479). To avoid service interruption, you may receive a notification if the number of remaining messages in the package you purchased is lower than a certain threshold.
>Packages are only available for China text messages. Voice messages and international SMS products used by enterprise users are [postpaid on a monthly basis](https://cloud.tencent.com/document/product/382/9556#.E7.9F.AD.E4.BF.A1.E3.80.81.E8.AF.AD.E9.9F.B3.E4.BB.B7.E6.A0.BC).

## Sending SMS Messages
After the main template and SMS signature are approved, you can send SMS messages through the console, cloud SMS API or SDK.
- For more information on how to send SMS messages through the console, please see [Send Text Message](https://cloud.tencent.com/document/product/382/13481).
- For more information on how to send SMS messages through APIs, please see [API Documentation](https://cloud.tencent.com/document/product/382/13297).
- For more information on how to send SMS messages through SDK, please see [SDK Documentation](https://cloud.tencent.com/document/product/382/5804).


### Viewing SMS Delivery Results
After an SMS is successfully sent, you can view SMS delivery result and statistics in [Statistical Analysis](https://cloud.tencent.com/document/product/382/3775#.E7.9F.AD.E4.BF.A1.E8.AE.B0.E5.BD.95) of SMS delivery.



