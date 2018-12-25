## SMS format
An SMS message is composed of a signature and a body. For example, in the SMS message "[Tencent Technology] Your verification code for QQ login is 1234, which is valid for five minutes", "[Tencent Technology]" is the signature and "Your verification code for QQ login is 1234, which is valid for five minutes" is the body.
You need to apply for a signature and a body template before sending an SMS message. For the aforesaid SMS message, the signature is "[Tencent Technology]" and the body template is "Your verification code for QQ login is {1}, which is valid for {2} minutes.", in which {1} and {2} are variables.

## SMS Signature
A signature is an identifier added before the message body for identification of the company or business. Before applying for a signature, enterprise users need to upload qualification certificates, and individual users need to upload their identity certificates. An SMS signature must be verified and approved before it can be used. For more information, please see the [Signature Review Criteria](https://intl.cloud.tencent.com/document/product/382/13444#signature-audit-criteria) section.
**Signature example:**
Enterprise to be verified: Shenzhen Tencent Computer Systems Co., Ltd.
>For example:
The signature that can be applied for: [Tencent Technology]
Alternatively, enterprises can also use the name of their product to apply for a signature: [WeChat], [Tencent Cloud]

Note: "[]" is not required when you apply for an SMS signature on the console. For example, when applying for the signature "[Tencent Technology]", you just need to enter and submit "Tencent Technology".

## SMS Template
SMS template is the specific content of the SMS message to be sent. Tencent Cloud SMS templates include common SMS templates (verification SMS, notification SMS) and marketing SMS templates. Individual users cannot use marketing SMS templates nor send marketing SMS messages. A templated SMS can be customized with parameters.
You need to apply for an SMS signature before applying for an SMS template which can be used only after it is approved. For more information, please see [SMS Template Review Criteria](https://intl.cloud.tencent.com/document/product/382/13444#audit-criteria-for-common-sms-messages).
**SMS template example:**
Tencent Technology needs to send an SMS verification code message in the following format: "[Tencent Technology] Your verification code for QQ login is 1234, which is valid for two minutes". In practice, the content "1234" and the validity period "two minutes" in the verification code message are variables.
You can apply for a signature and a template as below:
>SMS signature: Tencent Technology
SMS template: Your verification code for QQ login is {1}, which is valid for {2} minutes.

Note: Both {1} and {2} in the SMS template are variables and arranged in order. The values of the variables change according to the setting of parameters in the template.

## Common SMS Message
Common SMS messages include verification SMS and notification SMS messages:
- **Verification SMS message**: It is used to send verification codes for registration, login, payment confirmation, identity verification, etc.
>Example: Your login verification code is 1234, which is valid for 2 minutes. If you are not using our service, ignore the message.
- **Notification SMS message**: It is used to send system notifications, such as logistics information, payment receipt, status reminder.
>Example: The documents you submitted for the ICP license order 201700001234 are approved. You can submit supplementary materials now. If you have already submitted them to Tencent Cloud, we will complete the review as soon as possible.

## Marketing SMS Message
Marketing SMS messages refer to marketing and promotional SMS messages for member care, new launch, event notice. These messages are generally sent from operating companies to websites and registered members during sales or member events for marketing and promotional purposes.
**Marketing SMS message example:**
>Good news! You can apply for a celebrated store on the official website now to enhance your brand reputation and attract more customers. You can also enjoy plenty of materials for free. Apply now! Reply T if you don't want to receive these messages.

>Another new year promotion is coming! Haircare products are 30% off. The sale begins on Feb, 17, 9 am. For more information, visit xxx. Reply T if you don't want to receive these messages.



