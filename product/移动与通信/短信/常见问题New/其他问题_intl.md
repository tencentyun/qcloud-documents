### What can I do if I cannot receive SMS messages?
First, check the returned message after you call the API. If a message indicating success is returned, check whether the status in the status report is "Successful". You can query the status of the SMS message in the SMS console.
If a message indicating failure is returned, check the failure description in the response packet, for example, the request hits the frequency control policy, the format of the message text is incorrect, or the phone number is listed in the blacklist.
In any of the following circumstances, users cannot receive SMS messages even if a message indicating success is returned:
1. The phone is powered off, or the number is in arrears or out of service. You can call the number to confirm it.
2. The number is listed in the blacklist because the user have filed a complaint against the operator or unsubscribed from some services.
3. The phone has been on for a long time. Power it off and on again.
4. Weak signal. Restart the phone if necessary.
5. The inbox is full. Delete some SMS messages and try again.
6. If your mobile phone can hold two SIM cards, put the SIM card in another slot.
7. The SMS messages are blocked by the security software in the mobile phone. Ask the user to check whether the messages are listed in the block list.
8. Put your SIM card into another phone and see if it can receive the messages.
9. If none of the above methods works, [contact SMS Helper](/document/product/382/3773).

### What can I do if it takes a long time to call the API?
If it takes a long time to initiate a request when you call the Tencent Cloud SMS API, use the following methods to locate and solve the problem:
1. Dig yun.tim.qq.com to check whether a private or public DNS is used. If a private DNS is used, configure the host with the Tencent Cloud SMS IP address of the same operator in the nearest region, and then check whether the problem is solved.
  1.1 If the problem is solved, it indicates that DNS resolution gets stuck or the operator is accessed from a different region upon DNS resolution. You need to use a DNS proxy or configure a public DNS server.
  1.2 If the problem is not solved, go to method 2.  
2. Check whether the persistent or short connection is used, and whether the policy of connection pool is used.
  2.1 If HTTP requests are sent one after another over a single persistent connection, when a request gets stuck, the subsequent requests are also blocked. It is recommended to use "persistent connection + connection pool".
  2.2 If the short connection is used, use netstat to check whether the maximum number of connections is reached. If so, "long connection + connection pool" should be used.
  2.3 Use netstat to check whether the connected Recv-Q and Send-Q are accumulated. If so, use tcpdump to check whether the lost packets are retransmitted.
  2.4 If there is a connection through which no request has occurred for a long time (90 seconds), the requester needs to disable the connection to prevent it from being reclaimed by the intermediate network device. A new connection should be created in case of an inadequate number of connections in the connection pool upon the initiation of next request.

### Why does it take a long time to receive an SMS message?
1. Check whether the SMS message is rapidly submitted to Tencent Cloud SMS platform. Locally record the time when the request is sent, and then query in the console the time when the SMS message is sent to the mobile phone.
  1.1 If the former is greatly different from the latter, see [here](https://intl.cloud.tencent.com/document/product/382/9558#2-it-takes-a-long-time-to-call-the-api) to solve the problem.
  1.2 If the former is slightly different from the latter, go to method 2.  
2. Query in the console the difference between the time when the SMS message is sent to the phone and the time of status reporting.
  2.1 A small difference indicates that the SMS message is successfully sent to the phone. Such difference may be caused by the signal or the status of the phone.
  2.2 For a large difference, the text may contain sensitive words that need to be manually verified, or the phone has poor signals or in poor status. 
3. If none of the above methods works, [contact SMS Helper](/document/product/382/3773).

### What is a phone number blacklist?
The numbers of users who have complained about the unwanted messages or unsubscribed from some SMS services are added to the operator's blacklist. By doing so, the operator will not send SMS messages to the numbers in this blacklist to avoid disturbing users.
If your customers cannot receive SMS messages due to the blacklist, [contact SMS Helper](/document/product/382/3773) to remove their numbers from the blacklist.

### What can I do if a 1004 error is returned?
When you send SMS messages using Tencent Cloud SMS API, if the error code 1004 is returned in the response packet, locate and solve the problem by the following methods:
1. Check whether the sent request is in the standard JSON format. Click [here](http://tool.oschina.net/codeformat/json) to verify.
2. Check whether single quotation marks are used as double quotation marks (which are standard JSON characters).
3. Check whether there is a typo in the parameter name.
4. Check whether the requested field type is the same as that described in the API, and whether the JSON string and JSON integer are mixed up.
For example: `{"Name":"Xiao Ming", "Age":23}`,"Name" is a JSON string and "Age" is a JSON integer.
5. Check whether the API is called as described in the official website. For example, the API for bulk SMS messages is called but the packet format for single SMS messages is used.
6. If none of the above methods works, [contact SMS Helper](/document/product/382/3773).

### What can I do if a 1014 error is returned?
When you send SMS messages using Tencent Cloud SMS API, if the error code 1014 is returned in the response packet, locate and solve the problem by the following methods:
1. Check whether the format of the body template is correct. For example, "{}" should be used and the number enclosed in the brackets should be a consecutive integer starting from 1, for example: {1}, {2}...
2. Check whether the used body template is approved.
3. Check whether the value (0 indicates common SMS messages and 1 indicates marketing SMS messages) of the parameter type in the request packet matches the type of the used body template.
4. Check whether the format of the content in the SMS message matches that of the used body template. Check whether the mismatch is caused by **invisible characters such as space**.
5. If the content contains Chinese characters, check whether the Chinese characters are UTF-8 encoded.
6. China SMS text message template is only used to send messages to Chinese phone numbers, while international SMS text message template is only used to send messages to international phone numbers.
7. If none of the above methods works, [contact SMS Helper](/document/product/382/3773).

### What does 60008 error code mean?
When you send SMS messages using Tencent Cloud SMS API, if the error code 60008 is returned in the response packet, locate and solve the problem by the following methods:
1. After you have sent a request, if the error 60008 is returned in one second, check whether the request is in the standard HTTP format.
2. Check whether the DNS is configured properly and whether the public DNS server is used.
3. It is recommended to use the HTTP persistent connection plus the connection pool to improve the network quality.
4. If none of the above methods works, [contact SMS Helper](/document/product/382/3773).

### What can I do if a 1001 error (sig verification failed) is returned?

1. Check whether the random number generated by sig matches the random number in the URL.
2. Check whether the sdkappid/appkey (sdkappid starts with 14000) in the code is entered incorrectly.
3. Check whether the code used is consistent with the sample code, and whether the sig pseudo code generated by the parameter you specified is consistent.

### Descriptions of other common error codes
[Other error codes](/document/product/382/3771#1-.E7.9F.AD.E4.BF.A1.E5.8F.91.E9.80.81.E9.94.99.E8.AF.AF.E7.A0.811)




