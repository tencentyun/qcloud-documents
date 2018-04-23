## SMS format
An SMS message is composed of a signature and message body. For example, in the SMS message "[Tencent Technology] Your verification code for QQ login is 1234, which is valid for five minutes", "[Tencent Technology]" is the signature and "Your verification code for QQ login is 1234, which is valid for five minutes" is the message body.
You need to apply for a signature and a message body template before sending an SMS message. For the aforesaid SMS message, the signature is "[Tencent Technology]" and the message body template is "Your verification code for QQ login is {1}, which is valid for {2} minutes.", and {1} and {2} are variables.

## SMS Signature
A signature is an identifier added before the message body for identification of the company or business. Before applying for a signature, enterprise users need to upload qualification certificates, and individual users need to upload their identity certificates. The SMS signature must be verified and approved before it can be used. For more information, please see the [Signature Verification Standard](https://cloud.tencent.com/document/product/382/13444#.E7.AD.BE.E5.90.8D.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86) section.
**Signature Example:**
Enterprise to be verified: Shenzhen Tencent Computer Systems Co., Ltd.
>For example:
The signature that can be applied for: [Tencent Technology]
Alternatively, enterprises can also use the name of their product to apply for a signature: [WeChat], [Tencent Cloud]

Note: "[]" is not required when you apply for an SMS signature on the console. For example, when applying for the signature "[Tencent Technology]", you can just submit "Tencent Technology".

## SMS Template
SMS template is the specific content of the SMS message to be sent. Tencent Cloud SMS template supports common SMS template (verification SMS, notification SMS) and marketing SMS template. Individual users cannot use marketing SMS template nor send marketing SMS. A templated SMS can be customized using different parameters.
You need to apply for an SMS signature before applying for an SMS template which can be used only after it is approved. For more information on template verification standard, please see [SMS Verification Standard](https://cloud.tencent.com/document/product/382/13444#.E6.99.AE.E9.80.9A.E7.9F.AD.E4.BF.A1.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86).
**SMS Template Example:**
Tencent Technology needs to send an SMS verification code message in the following format: "[Tencent Technology] Your verification code for QQ login is 1234, which is valid for two minutes". In practice, the content "1234" and the validity period "two minutes" of verification codes are variables.
You can apply for a signature and a template as below:
>SMS signature: Tencent Technology
SMS template: Your verification code for QQ login is {1}, which is valid for {2} minutes.

Note: Both {1} and {2} in the SMS template are variables and arranged in order. The values of the variables change according to the setting of parameters in the template.

## Common SMS
Common SMS is divided into verification SMS and notification SMS:
- **Verification SMS**: It is used to send verification codes for registration/login, payment confirmation, identity verification, etc.
>Verification SMS example: Your login verification code is 1234, which is valid for 2 minutes. If you are not using our service, ignore the message.
- **Notification SMS**: It is used to send system notifications, such as logistics information, payment receipt, status alert.
>Notification SMS example: The documents you submitted for the ICP license order 201700001234 are approved. You can submit supplementary material now. If you have submitted it to Tencent Cloud, we will complete the review as soon as possible.

## Marketing SMS
It is used to send marketing and promotion SMS such as member care, new launch, event notice. These messages are generally sent from operating companies to websites and registered members during sales or member events for marketing and promotion purposes.
**Marketing SMS Example:**
>Good news! You can apply for a celebrated store on the official website now to enhance your brand reputation and attract more customers. You can also enjoy plenty of materials for free. Apply now! Reply T if you don't want to receive such message.

>Another new year promotion is coming! Haircare products are 30% off. The sale begins on Feb, 17, 9 am. For more information, visit xxx. Reply T if you don't want to receive such message.



