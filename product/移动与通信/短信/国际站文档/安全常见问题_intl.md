### What is the default frequency limit for sending SMS messages?
To ensure business and channel security and minimize financial loss caused by unauthorized usage, the default frequency limit for sending SMS messages is set as follows:
1. For SMS messages with the same content, a maximum of one such message can be sent to the same phone number within 30 seconds.
2. A maximum of 10 SMS messages can be sent to the same phone number in one calendar day.
Users who have completed the enterprise identity verification go to **Project Configuration** -> **Basic Configuration** -> **Delivery Frequency Limit** in the SMS console to set or modify the frequency limit:

### How to prevent SMS bombing?
SMS bombing is a method of sending massive SMS verification messages to numerous phone numbers within a short period of time (such as a day) by using malicious programs or tools to exploit web client or server vulnerabilities, which seriously harasses the phone users.
![](https://main.qcloudimg.com/raw/71e239febf41a4ec37f691fd6cfe9e69.png)
If harassed by SMS bombing, users will complain a lot and SMS channels will be unavailable. Besides, the business side will also suffer heavy economic losses. Therefore, SMS bombing must be prevented in advance.
Because SMS bombing is generally implemented on servers, it is recommended to apply the following methods to defend against it:
1. Limit the number of requests from the same IP address.
2. Limit the number of SMS messages sent from the same phone number by setting the [delivery frequency limit](https://intl.cloud.tencent.com/document/product/382/13483#configuring-frequency-limit) on the console.
3. Check the sending of SMS messages regularly (for example, daily), and view the specific data in the SMS console. Resolve any exception immediately. Suspend the SMS service in the SMS console if an emergency arises.

### What are the differences between China SMS messaging and international SMS messaging?
As required by operators, you need to add a signature when sending SMS messages in China. However, if you send international SMS messages to international phone numbers, the signature is optional.
If you want to send SMS messages to Chinese phone numbers with a text template applied for on the international SMS page, you must apply for an SMS signature and add it in the SMS messages to be sent to Chinese phone numbers.

### How can I query the delivery records of a phone number?
If your customers cannot receive SMS messages, or if you want to check the delivery status of SMS messages sent to users, you can query the delivery records in **China SMS Messages** or **International SMS Messages** -> **Statistical Analysis** -> **SMS Message Records** on the Tencent Cloud SMS Console, as shown below:
![](https://main.qcloudimg.com/raw/ef647abc4454b2b5460b632e68fa50ac.png)

### What is sdkappid and appkey? How can I create and view projects?

The sdkappid is the unique ID of an SMS project, which is used to identify the project. The appkey is the corresponding password and must be kept confidential.
For more information on how to create a project, please see the access guide.


### How to set a whitelist with no frequency limit on sending SMS messages for a test phone number or alarm phone number?

To impose no frequency limit on test numbers, [contact SMS helper](/document/product/382/3773) to add the numbers to the whitelist.

### How can I check whether a specified phone number has received SMS messages?

1. Check the delivery records in **China SMS Messages** or **International SMS Messages** -> **Statistical Analysis** -> **SMS Message Records** on the Tencent Cloud SMS Console.
2. Export an excel file containing the records of sending SMS messages over a period of time from **China SMS Messages** or **International SMS Messages** -> **Statistical Analysis** -> **SMS Message Records** on the Tencent Cloud SMS Console.



