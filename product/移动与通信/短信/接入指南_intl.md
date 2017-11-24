## 1 Overview
Tencent Cloud SMS service access procedure:
![](//mc.qcloudimg.com/static/img/54c5e0236d0a4185dc45b8052ff4a598/image.png)

## 2 Sign up for Tencent Cloud
### 2.1 Sign Up for a Tencent Cloud Account
(1)	Go to sign-up page [Tencent Cloud official website - sign-up page link](http://manage.qcloud.com/developerCenter/registUser.php).
(2)	Verify your identity with your QQ account.
(3)	Log in to QQ for verification. 
(4)	Complete the profile for your account.
(5)	Click the Email link to activate the account.
For more information, please see [Sign-up Instructions](http://bbs.qcloud.com/thread-2378-1-1.html).
### 2.2 Qualification Verification
(1)	Complete the profile:
[Instructions on completing profile](http://bbs.qcloud.com/forum.php?mod=viewthread&tid=2358&extra=page%3D1)
(2)	Qualification verification:
[FAQs about qualification verification](http://bbs.qcloud.com/forum.php?mod=viewthread&tid=2364&extra=page%3D1)

## 3 Apply for SMS Service
### 3.1 Completing business information
(1)	[About SMS service](http://cloud.tencent.com/product/sms.html)
![](//mc.qcloudimg.com/static/img/f3d9037d726fd9d022943835feb502f4/image.png)
(2)	Click "Experience". Corporate customers who do not go through the qualification verification or individual customers need to complete the profile in account management as instructed. For more information, please see [2.2 Qualification Verification](https://cloud.tencent.com/doc/product/382/%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97#2.2-.E8.B5.84.E8.B4.A8.E5.AE.A1.E6.A0.B8)
![](//mc.qcloudimg.com/static/img/0bf4ca3b61db958d5313a48b0c014399/image.png)
### 3.2 Log Into Console
After completing your profile, log in to [Console](http://console.cloud.tencent.com/sms) via console entry or link.

## 4. Create Application
(1)	Create an application. Go to SMS console and click "New" in the upper left corner of the application list.
![](//mc.qcloudimg.com/static/img/c996d30ff1ee445283abb063f146cb80/image.png)
Enter the application information in the "New Application" window that appears.
![](//mc.qcloudimg.com/static/img/521d83b2d63cd21d7d164e5d5c4b49cf/image.png)
(2)	After creating the application, click "Details", as shown below:
![](//mc.qcloudimg.com/static/img/7ade6588fcf75cb826373f5e98b78456/image.png)
In the "Application Information" window, you can find the SdkAppID and AppKey of the application.
![](//mc.qcloudimg.com/static/img/08ef51c6f1768f1854ab89742873646d/image.png)
Note: The Appkey for the SdkAppID should be kept confidential.

## 5 SMS Message Content Configuration
### 5.1	Configure SMS Signature
SMS signature is an ID included with the SMS message content for identifying company or business. It can be the company name or product name, and has a length of 2-8 words, for example, [Tencent Cloud Platform].
![](//mc.qcloudimg.com/static/img/96ab73f1b781c4f28db173548fd699cf/image.png)
You can create it in "Content Configuration - SMS Signature" under the Application Details, and put it into use upon the approval. Its approval status can be found in the upper right corner of the signature card.
![](//mc.qcloudimg.com/static/img/41e720ab75ae73623211a439546d7aaf/image.png)
Note: Generally, the approval process for SMS signature is completed within half a work day. For international SMS signature, please apply for it in the page for international text messages.
### 5.2	Configure SMS Content
SMS content is the full content of an SMS message sent. Only approved content templates can be sent.
You can create SMS content template in "Content Configuration - SMS Message Body" under the Application Details, and put it into use upon the approval.
![](//mc.qcloudimg.com/static/img/7d3e6b24db524f76a77b6120fe7d7447/image.png)
Click the "Create Message Body" button to enter the body template creation page.
![](//mc.qcloudimg.com/static/img/a3c934e20e3bc453f9df57b7eafba991/image.png)
Note: Generally, the approval process for SMS content template is completed within 2 hours. For international SMS message template, please apply for it in the page for international text messages.
### 5.3 Configure Frequency Limit
To ensure business and channel security and minimize financial loss caused by malicious call of SMS API by others, the default frequency limit for sending SMS messages is set as follows:
1. For SMS messages with the same content, a maximum of one such message can be sent to the same phone number within 30 seconds;
2. A maximum of ten SMS messages can be sent to the same phone number in one calendar day;
Individual customers have no permission to modify the frequency limit. Corporate customers can go to "Application Configuration" -> "Basic Configuration" -> "Frequency of Sending SMS Messages" in the SMS console to set or modify the frequency limit:
![](//mc.qcloudimg.com/static/img/7ee8dd6892d2fbb59ffe8959279fa440/image.png)
### 5.4 Add Alarm Contact
You can add alarm contact in "Application Configuration -> Notification and Alarm -> Add Alarm Contact" page in the SMS console. When added, the alarm contact can receive notifications about approvals for SMS signature and content template as well as alarm for frequency limit in a timely manner:
(Note: You are strongly recommended to use this feature so that you can receive an alarm when the frequency limit is reached, thus minimizing the financial loss caused by malicious call of SMS API by others.)
![](//mc.qcloudimg.com/static/img/eb48d970c482cd638c528e9f95e3ab24/image.png)
### 5.5 Configure Callback
To make it easier for customers to keep good track of the information about the SMS messages sent, Tencent Cloud SMS service provides powerful callback capability. For example, if a callback URL for SMS receipt status is configured, after receiving the callback message from operator, Tencent Cloud will push the callback message to the specified callback URL immediately. Currently, Tencent Cloud SMS service supports callbacks for SMS status, SMS reply and voice messages.
You can select the callback as needed and configure the callback URL in the Callback Configuration page under Application Details.
![](//mc.qcloudimg.com/static/img/1539d61a5f836da537dce10f458c6ea8/image.png)

## 6 Purchase Packages
Text messages within China are billed on a prepaid basis. You can go to [Package Management Page](https://console.cloud.tencent.com/sms/packageList) to [purchase SMS packages](https://buy.cloud.tencent.com/sms). The packages are only available for text messages within China. The fees for voice messages used by corporate customers and international SMS products are postpaid monthly. 
![](//mc.qcloudimg.com/static/img/ec6d3c61ad1b464b67b32aaab582f1dc/image.png)
