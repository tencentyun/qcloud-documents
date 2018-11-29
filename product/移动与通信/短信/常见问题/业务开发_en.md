## 1 Frequency Limit of Sending SMS Messages
To ensure business and channel security and minimize financial loss caused by malicious call of SMS API by others, the default frequency limit for sending SMS messages is set as follows:
1. For SMS messages with the same content, a maximum of one such message can be sent to the same phone number within 30 seconds.
2. A maximum of ten SMS messages can be sent to the same phone number in one calendar day.
In the SMS Console, you can set or modify the frequency limit in the "Project Configuration" -> "Basic Configuration" -> "Frequency of Sending SMS Messages".
![](//mc.qcloudimg.com/static/img/7ee8dd6892d2fbb59ffe8959279fa440/image.png)

## 2 Add Alarm Contact
You can add alarm contact in "Project Configuration -> Notification and Alarm -> Add Alarm Contact" page in the SMS console. When added, the alarm contact can receive notifications about approvals for SMS signature and body template as well as alarm for frequency limit in a timely manner:
(Note: You are strongly recommended to use this feature so that you can receive an alarm when the frequency limit is reached, thus minimizing the financial loss caused by malicious call of SMS API by others.)
![](//mc.qcloudimg.com/static/img/eb48d970c482cd638c528e9f95e3ab24/image.png)

## 3 Frequency Limit of Sending Voice Messages
To ensure business and channel security and minimize financial loss caused by malicious call of SMS API by others, the default frequency limit for sending voice messages is set as follows:
1. A maximum of one voice message can be sent to the same phone number within 30 seconds. 
2. A maximum of two voice messages can be sent to the same phone number within ten minutes. 
3. A maximum of three voice messages can be sent to the same phone number in one day. 
As the frequency of sending voice messages is controlled by operators, you cannot modify it by yourself. If you want to add the test number into the whitelist, [contact SMS Helper](/document/product/382/3773).

## 4 SMS Bombing and Prevention
SMS bombing is a method of sending massive verification code messages to lots of phone numbers in a short time (for example, within a day) by using malicious programs or tools to exploit web client or server vulnerabilities, which seriously harasses the phone users.
The following shows an example of SMS bombing: Normally, the customer sends dozens of SMS messages per day. During SMS bombing, the customer sends tens of thousands of SMS messages per day.
![](//mc.qcloudimg.com/static/img/dbebfa33e35ae5542c1f00e006956eff/image.png)
SMS bombing harasses innocent users, causing complaints from them, and makes SMS channels unavailable. Besides, the business side will also suffer heavy financial losses. Therefore, SMS bombing must be prevented in advance.
Because SMS bombing is generally launched on servers, it is recommended to apply the following methods to defend against it:
1. Use image verification codes. Tencent Cloud provides [Tianyu](https://cloud.tencent.com/product/yy) anti-cheating feature.
2. Limit the number of requests from the same IP address.
3. Limit the number of SMS messages sent by the same phone number. This can be achieved by setting [frequency limit of sending SMS messages](#1-.E7.9F.AD.E4.BF.A1.E9.A2.91.E7.8E.87.E9.99.90.E5.88.B6) and [adding alarm contacts](#2-.E6.B7.BB.E5.8A.A0.E5.91.8A.E8.AD.A6.E8.81.94.E7.B3.BB.E4.BA.BA) in the console.
4. Check the delivery status of SMS messages regularly (for example, daily). Specific data is shown in the SMS console. In case of any exception, deal with it immediately. In case of emergency, disable SMS in the SMS console.

## 5 Send an SMS message with One of the Signatures
If you have multiple [SMS signatures](./9557#2-.E7.9F.AD.E4.BF.A1.E7.AD.BE.E5.90.8D.E8.A7.84.E8.8C.83), put the desired SMS signature in the front of the SMS message and then send the message by calling the SMS API.
For example, if you have two signatures of "[Tencent Technology]" and "[Tencent Cloud]" and you want to send a SMS message with "[Tencent Cloud]", configure the SMS message to "[Tencent Cloud] Your verification code is xxxx". "xxxx" represents the verification code.

## 6 Differences between SMS in China and International SMS
As required by operators, you need to add a signature when sending an SMS message in China. However, if you send an international SMS message to a mobile overseas, the signature is optional.
If you want to send an SMS message to a mobile in China with a body template applied in the international SMS page, you must apply for an SMS signature and add it in the SMS message.

## 7 Query the Delivery History of a Mobile
If you receive feedbacks of SMS messages not received, or you want to view the SMS message delivery status of a user's mobile phone, you can query the delivery history in the "Statistics" -> "China/International Voice/Text messages" -> "SMS History" on the page of Tencent Cloud SMS Console, as shown below:
![](//mc.qcloudimg.com/static/img/f14d976f443ace2e4ef73d62ed144a2b/image.png)
