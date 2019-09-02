## 1 SMS messages cannot be received
First, check the returned message after you call the API. If a message indicating success is returned, check whether the status in the status report is "Successful". You can query the status of the SMS message in the SMS console.
If a message indicating failure is returned, check the failure description in the response packet. The reason may be the request hits the frequency control policy, the format of the SMS message is wrong or the phone number is listed in the blacklist.
Under any of the following circumstances, users cannot receive SMS messages even if a message indicating success is returned:
1. The phone is powered off, or the number is in arrears or out of service. You can dial the number to check it out.
2. The number is listed in the blacklist because the subscriber has complained against the operator or unsubscribed from some services.
3. The phone has been on for a long time. Power it off and on again.
4. Weak signal. Restart the phone if necessary.
5. The inbox is full. Delete some SMS messages and try again.
6. If your mobile phone can hold two SIM cards, put the SIM card in another slot.
7. The SMS messages are blocked by the security software in the mobile phone. Check whether the messages are listed in the block list.
8. If the above seven methods do not work, put your SIM card into another phone and test.
9. If all of the above methods do not work, [contact SMS Helper](/document/product/382/3773).

## 2 It takes a long time to call the API
If it takes a long time to initiate a request when you access Tencent Cloud SMS API, use the following methods to locate and solve the problem:
1. dig yun.tim.qq.com, check whether a private or public DNS is used. If a private DNS is used, configure the host to the Tencent Cloud SMS IP address that is closest to the operator, and then check whether the problem is solved.
  1.1 If the problem is solved, it indicates that DNS resolution gets stuck or the DNS is resolving access by operator across regions. You need to use DNS proxy or configure the public DNS server.
  1.2 If the problem is not solved, skip to method 2.  
2. Review whether the persistent or short connection is used, and whether the policy of connection pool is used.
  2.1 If HTTP requests are sent one after another over a single persistent connection, when a request gets stuck, the subsequent requests are also blocked. You are recommended to use the persistent connection plus the connection pool mode.
  2.2 If the short connection is used, use netstat to check whether the maximum number of connections is reached. If the maximum number is reached, you are recommended to use the persistent connection plus the connection pool mode.
  2.3 Use netstat to check whether the Recv-Q and Send-Q of the connections are accumulated. If accumulation exists, use tcpdump capture packet to check whether the lost packets are retransmitted.

## 3 It takes a long time to receive an SMS message.
1. Check whether the SMS message is rapidly submitted to Tencent Cloud SMS platform. Locally record the time when the request is sent, and then query in the console the time when the SMS message is sent in the corresponding mobile phone.
  1.1 If the former is greatly different from the latter, see [It takes a long time to call the API](./9558#2-.E8.B0.83.E7.94.A8.E6.8E.A5.E5.8F.A3.E8.80.97.E6.97.B6.E6.AF.94.E8.BE.83.E9.95.BF) to solve the problem.
  1.2 If the former is slightly different from the latter, skip to method 2.  
2. Query in the console the difference between the time when the SMS message in sent in the phone and the time in the status report.
  2.1 If the difference is rather small, it indicates that the SMS message is successfully sent to the phone. Such difference might be caused by the signal or the status of the phone.
  2.2 If the difference is relatively large, the message may contain sensitive words that need to be manually verified, or the phone has poor signals or in poor status. 
3. If all of the above methods do not work, [contact SMS Helper](/document/product/382/3773).

## 4 Mobile blacklist
The mobiles of users who has complained about the unwanted messages or unsubscribed from some SMS services are added into the operator's blacklist. After that, the operator will not send SMS messages to the mobiles in this blacklist so that the users are not bothered.
If your customer confirms that he/she cannot receive SMS messages due to the blacklist, [contact SMS Helper](/document/product/382/3773) to remove his/her mobile from the blacklist.

## 5 Description of error 1004
When you send SMS messages using Tencent Cloud SMS API, if the response packet returns error 1004, use the following methods to locate and solve the problem:
1. Check whether the sent request is in the standard JSON format. Click [here](http://tool.oschina.net/codeformat/json) to verify.
2. Check whether the single quotation marks are misused as double quotation marks. Double quotation marks should be in the standard JSON format.
3. Check whether there is a typo in the parameter name.
4. Check whether the requested field type is the same as that described in the API and whether the JSON string and JSON integer are confused.
For example: `{"Name":"Xiao Ming", "Age":23}`,"Name " is a JSON string and "Age" is a JSON integer.
5. Check whether the API is called as described in the official website. For example, you call the API for bulk SMS but use the packet format for single SMS.

## 6 Description of error 1014
When you send SMS messages using Tencent Cloud SMS API, if the response packet returns error 1014, use the following methods to locate and solve the problem:
1. Check the format of the main body template. For example, "{}" should be used and the numeral enclosed in the brackets should be a consecutive integer starting from 1, for example: {1}, {2}…
2. Check whether the body template is approved.
3. Check whether the value (0 indicates common SMS messages and 1 indicates marketing SMS messages) of the parameter "type" in the request packet matches the type of the used body template.
4. Check whether the format of the main body in the SMS message matches that of the used template. Note whether the mismatch is caused by **invisible characters such as space**.
5. If the message contains Chinese characters, check whether the Chinese characters are encoded using UTF-8.

## 7 Description of error 60008
When you send SMS messages using Tencent Cloud SMS API, if the response packet returns error 60008, use the following methods to locate and solve the problem:
1. After your request, if error 60008 is returned in one second, check whether the request is in the standard HTTP format.
2. Check whether the DNS is configured properly and make sure that a public DNS server is used.
3. It is recommended to use the HTTP persistent connection plus the connection pool to improve the network quality.
4. If all of the above methods do not work, [contact SMS Helper](/document/product/382/3773).

## 8 Descriptions of other common error codes
For more information, please see [Error Codes](/document/product/382/3771#1-.E7.9F.AD.E4.BF.A1.E5.8F.91.E9.80.81.E9.94.99.E8.AF.AF.E7.A0.811).
