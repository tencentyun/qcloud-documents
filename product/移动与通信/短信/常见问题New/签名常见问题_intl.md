### What can I do if my application for a signature is rejected?

Identification materials are required to apply for an SMS signature. Enter a signature based on the signature audit criteria and upload correct identification materials.

### Why is my application rejected because of "Neutral Signature"?

Neutral signatures, such as "test, aabb, verification code, notification", that cannot be identified as a company or an individual are not supported. You are recommended to use a company name to apply for a signature. For more information, please see [Signature Audit Criteria](https://intl.cloud.tencent.com/document/product/382/13444).

### Is there a limit on the number of SMS signatures?
The number of SMS signatures is limited to 200. To apply for multiple signatures, you should provide the qualification certificate for each signature.

### Can I modify the SMS signature?
Approved signatures cannot be modified. However, you can create multiple signatures to choose from when you send SMS messages.

### Products cannot be launched during the test, so how can I apply for a signature?

If a product is not launched, use the company name to apply for a signature for product testing. When the product is launched, use the product name to apply for a signature.

### Why hasn't the SMS signature been approved?

This may be caused by many reasons, for example, the signature and the uploaded information are not compliant with the audit criteria, or relevant information is not uploaded. Apply for an appropriate signature as prompted based on the [Signature Audit Criteria](https://intl.cloud.tencent.com/document/product/382/13444).

### What should I enter in the remarks for signature?

Signature type is an app: Enter the download URL of the app store.
Signature type is a website: Enter the domain name of the website.
Signature type is an Official Account or a Mini Program: Enter the full name of the Official Account or Mini Program.

### How can I send SMS message(s) with one of the signatures?

Send a single message or bulk messages: Place the required SMS signature before the SMS message text, and call the SMS API to send the message(s).
For example, if you have two signatures, "[Tencent Technology]" and "[Tencent Cloud]", and you want to send an SMS message with "[Tencent Cloud]", the "msg" field can be: "[Tencent Cloud] Your verification code is xxxx". ("xxxx" is the verification code issued)
Send a single message or bulk messages with a specified template: Specify the SMS signature in the sign field.
For example, if you have two signatures, "[Tencent Technology]" and "[Tencent Cloud]", and you want to send an SMS message with "[Tencent Cloud]", the "sign" field can be: "Tencent Cloud".

