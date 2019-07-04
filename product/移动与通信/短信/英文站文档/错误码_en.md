## Error Codes for SMS Delivery
| Error Code  | Reason | Solution  |
|--------|------|--------|
| 1001 | sig verification failed | Check the sig format of the API. |
| 1002 | Text/voice SMS contains sensitive words | A response packet including these sensitive words is returned. Delete these words and send again. |
| 1003 | The sig field is missing or left empty in request packet | Comply with the specifications in API description. |
| 1004 | Failed to resolve request packet. This is generally because the specifications in API description is not complied with | Refer to [1004 Error Description](https://cloud.tencent.com/document/product/382/9558#5-1004.E9.94.99.E8.AF.AF.E8.AF.A6.E8.A7.A3). |
| 1006 | No permission to request. For example, no extended code permission, etc. | Check error message. For other questions, provide the mobile number from which you failed to send SMS message when you [contact SMS Helper](https://cloud.tencent.com/document/product/382/3773). |
| 1007 | Other error | Check error message. For other questions, provide the mobile number from which you failed to send SMS message when you [contact SMS Helper](https://cloud.tencent.com/document/product/382/3773). |
| 1008 | Request to send text/voice SMS timed out | Rare occurrence. Try again. |
| 1009 | Request IP is not on the whitelist. | Verification of request's source IP has been configured, but the current request IP is not found in the configuration list. If necessary, [contact SMS Helper](https://cloud.tencent.com/document/product/382/3773). |
| 1011 | REST API does not exist. | Check REST API description. |
| 1012 | Signature format is incorrect or signature is not approved. | Signature is a combination of 2-12 characters comprised of English letters and numbers only. If the signature format is correct, check whether it is approved. |
| 1013 | Text/voice SMS hits the delivery frequency limit policy. | You can adjust the delivery frequency limit policy for text SMS messages on the console. For voice SMS messages, [contact SMS Helper](https://cloud.tencent.com/document/product/382/3773). |
| 1014 | Template is not approved or request content does not match the approved template content. | Refer to [1014 Error Description](https://cloud.tencent.com/document/product/382/9558#6-1014.E9.94.99.E8.AF.AF.E8.AF.A6.E8.A7.A3). |
| 1015 | Mobile number on the blacklist. This is generally because you unsubscribed from the SMS service or hit the ISP's blacklist. | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) to solve the problem. |
| 1016 | Incorrect mobile number format | Check whether the format of the mobile number you used to send text/voice SMS is correct. |
| 1017 | The content of the requested SMS is too long | [The length of SMS content](https://cloud.tencent.com/document/product/382/3772#2-.E7.9F.AD.E4.BF.A1.E9.95.BF.E5.BA.A6) exceeds the limit. Adjust the length of SMS content. |
| 1018 | The format of voice verification code is incorrect. | Comply with the specifications in the API description. |
| 1019 | sdkappid does not exist. |  |
| 1020 | sdkappid is disabled. | This sdkappid is unavailable. If necessary, [contact SMS Helper](https://cloud.tencent.com/document/product/382/3773). |
| 1021 | The time when the request was initiated is exceptional. This is generally because the difference between the time on your server and that on the Tencent Cloud server exceeds 10 minutes. | Check whether the server time and the time field in the API are normal. |
| 1022 | The number of business SMS messages sent every day exceeds the upper limit. | You can adjust the SMS frequency limit policy on the console. |
| 1023 | The number of SMS messages sent from a single mobile number within 30 seconds exceeds the upper limit. | You can adjust the SMS delivery frequency limit policy on the console. |
| 1024 | The number of SMS messages sent from a single mobile number within 1 hour exceeds the upper limit. | You can adjust the SMS delivery frequency limit policy on the console. |
| 1025 | The number of SMS messages sent from a single mobile number every day exceeds the upper limit. | You can adjust the SMS delivery frequency limit policy on the console. |
| 1026 | The number of the same SMS messages sent from a single mobile number exceeds the upper limit. | You can adjust the SMS delivery frequency limit policy on the console. |
| 1029 | The time when marketing SMS messages are sent is limited. | To avoid harassing users, the marketing SMS messages are only allowed to be sent from 8:00 to 22:00. |
| 1030 | This request is not supported. |  |
| 1031 | Account balance in the service package is insufficient. | Please [purchase package](https://buy.cloud.tencent.com/sms). |
| 1032 | Individual user does not have the permission to send marketing SMS messages. |  
| 1033 | 	Service is suspended due to arrears. | You can log in to Tencent Cloud to top up your account. |   
| 1036 | The number of variable characters in a single template exceeds 15. | To adjust the limit, please [contact SMS Helper](https://cloud.tencent.com/document/product/382/3773). |
## Error Codes for Status
| Error Code | Category | Reason | Solution |
|--------|-------|------|--------|
| DELIVRD | Three ISPs | SMS message is received successfully. | None |
| UNDELIVRD | Three ISPs | Invalid number, out-of-service or powered-off | None |
| MX:0003 | Three ISPs | The number of SMS messages sent from a single mobile number on the day exceeds the limit. | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) to remove the limit. |
| REJECTD | Three ISPs | SMS message is rejected for some reason. | Verify whether the mobile device is normal. |
| MX:0012 | Three ISPs | The target number is on the customer unsubscription blacklist. | The user is added to the blacklist after replying to the unsubscription SMS massage. [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) to remove the number from the blacklist. |
| BWLIST _006 | Three ISPs | Gateway blacklist | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) for a discussion. |
| TE:0003 | Three ISPs | The number of downlink SMS messages sent from a single mobile number on the day exceeds the limit. | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) to remove the limit. |
| TE:0014 | Three ISPs | Manual verification failed | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) for a discussion. |
| TE:0002 | Three ISPs | Failed to submit SMS messages to gateway | None |
| TD:0001 | Three ISPs | Gateway blacklist | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) for a discussion. |
| TD:0004 | Three ISPs | Suspected of fishing. Make a check. ||
| TD:19 | Three ISPs | Number on the blacklist | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) for a discussion. |
| TD:18 | Three ISPs | Number from unknown ISP | None |
| UNDELIV | China Mobile | Invalid number, out-of-service or powered-off | Verify whether the mobile device is normal. |
| MI:0013 | China Mobile | Out-of-service or powered-off | None |
| MN:0001 | China Mobile | Invalid number, out-of-service or powered-off | Verify whether the mobile device is normal. |
| MK:0012 | China Mobile | Invalid number | Verify whether the mobile device is normal. |
| MK:0005 | China Mobile | Whether the No. 21 value-added service attribute of the account opening data of the target user is supported. | If the number status is normal, the user can contact local ISP's customer service to confirm whether the SMS service is enabled. |
| MK:0000 | China Mobile | Invalid number | Verify whether the mobile device is normal. |
| MN:0054 | China Mobile | Invalid number, out-of-service or powered-off | Verify whether the mobile device is normal. |
| MK:0001 | China Mobile | MK0001 means that this number is not found by HLR. The status returned from SMC is unrecognized number, indicating that the SMS message is sent to a wrong number. | Verify whether the mobile device is normal. |
| EXPIRED | China Mobile | SMS message expired | Failed to receive SMS message due to no response from the mobile device after a long period of time. |
| MI:0024 | China Mobile | Out-of-service or powered-off | None |
| MI:0011 | China Mobile | Invalid number, out-of-service or powered-off | None |
| MC:0151 | China Mobile | Invalid number, out-of-service or powered-off | None |
| IC:0001 | China Mobile | Out-of-service or powered-off | None |
| MI:0029 | China Mobile | Out-of-service or powered-off | None |
| MI:0005 | China Mobile | Invalid number, out-of-service or powered-off | None |
| MK:0004 | China Mobile | Out-of-service or powered-off | None |
| MI:0000 | China Mobile | Invalid number, out-of-service or powered-off | None |
| MI:0022 | China Mobile | China Mobile gateway internal error | Verify whether the mobile device is normal. |
| IA:0054 | China Mobile | Failed to receive response message due to timeout | Verify whether the mobile device is normal. Restart the phone and try again. |
| MC:0055 | China Mobile | Failed to send SMS message because user's phone is out of the service area or the memory is full. | Verify whether the mobile device is normal. |
| MN:0059 | China Mobile | User's phone was out of the service area. | Verify whether the mobile device is normal. SMS delivery failed because the user is busy. |
| MI:0004 | China Mobile | Invalid number, out-of-service or powered-off | None |
| MI:0020 | China Mobile | Invalid number, out-of-service or powered-off | None |
| MK:0029 | China Mobile | Temporarily unavailable | Verify whether the mobile device is normal. |
| MI:0084 | China Mobile | Invalid number, out-of-service or powered-off | None |
| MK:0024 | China Mobile | Failed to send SMS message because the target phone is powered off. | Verify whether the mobile device is normal. |
| MK00001 | China Mobile | Invalid number | Verify whether the mobile device is normal. |
| MI:0017 | China Mobile | Invalid number, out-of-service or powered-off | None |
| MK:0015 | China Mobile | When an SMS message is sent, the target phone has a software problem in the process of receiving message. For example, after the phone is restarted, the software for processing the SMS message is not initialized to process the message normally. | Verify whether the mobile device is normal. |
| MN:0029 | China Mobile | Invalid number, out-of-service or powered-off | Verify whether the mobile device is normal. |
| IC:0151 | China Mobile | Invalid number, out-of-service or powered-off | Verify whether the mobile device is normal. |
| MN:0075 | China Mobile | ISP internal error | None |
| MK:0010 | China Mobile | Temporarily unavailable | Verify whether the mobile device is normal. |
| IC:0015 | China Mobile | ISP internal error | None |
| BEYONDN | China Mobile | ISP internal error | None |
| MI:0055 | China Mobile | Invalid number, out-of-service or powered-off | None |
| MI:0010 | China Mobile | The number has expired | None |
| MC00151 | China Mobile | ISP internal error | None |
| IC:0055 | China Mobile | ISP internal error | None |
| MB:1078 | China Mobile | ISP internal error | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) to provide the phone number and submit a ticket to verify with ISP. |
| MN00001 | China Mobile | ISP internal error | None |
| ID:0013 | China Mobile | ISP internal error | None |
| MC:0001 | China Mobile | Unknown error | None |
| MK:0017 | China Mobile | The memory is full. | The space for storing SMS messages is full. Free up space by clearing the SMS messages stored in the phone. |
| MI:0081 | China Mobile | ISP internal error | None |
| DA:0054 | China Mobile | Failed to receive response message due to timeout | Verify whether the mobile device is normal. |
| MB:1042 | China Mobile | The number of SMS messages cached in the SMC memory and to be sent to the target user exceeds the maximum number of SMS messages received by this user. | Check the number of the SMS messages sent to the target number in the SMC memory. If the number has reached the maximum number of SMS messages received by the target user, submit the SMS message again later. |
| ERR_NUM | China Mobile | Target number is incorrect or restricted. | Verify whether the mobile device is normal. |
| MI:0054 | China Mobile | Invalid number, out-of-service or powered-off | None |
| MK:0011 | China Mobile | Out-of-service or powered-off | None |
| MN:0052 | China Mobile | ISP internal error | None |
| MK:0008 | China Mobile | Failed to receive SMS message due to poor signal in the location of the user. | Verify whether the mobile device is normal. |
| IA:0073 | China Mobile | ISP internal error | None |
| IA:0051 | China Mobile | ISP internal error | None |
| MK:0075 | China Mobile | Invalid number, out-of-service or powered-off | Verify whether the mobile device is normal. |
| MN:0022 | China Mobile | Invalid number, out-of-service or powered-off | Verify whether the mobile device is normal. |
| MN:0022 | China Mobile | Invalid number, out-of-service or powered-off | Verify whether the mobile device is normal. |
| MN:0020 | China Mobile | China Mobile gateway internal error | Verify whether the mobile device is normal. |
| MN:0029 | China Mobile | ISP internal error | None |
| MI:0008 | China Mobile | China Mobile gateway internal error | None |
| MI:0012 | China Mobile | Invalid device | Verify whether the mobile device is normal. |
| MN:0012 | China Mobile | Invalid number, out-of-service or powered-off | Verify whether the mobile device is normal. |
| MI:0059 | China Mobile | Invalid number, out-of-service or powered-off | None |
| MN:0050 | China Mobile | Invalid number, out-of-service or powered-off | Verify whether the mobile device is normal. |
| MN:0017 | China Mobile | SMS message rejected | Verify whether the mobile device is normal. |
| MI:0045 | China Mobile | China Mobile gateway internal error | None |
| MN:0055 | China Mobile | ISP internal error | None |
| NOROUTE | China Mobile | No route found | None |
| MI:0036 | China Mobile | China Mobile gateway internal error | None |
| MB:1077 | China Mobile | User on the blacklist. This is because China Mobile keeps a record of the user's malicious complaints. | The user needs to communicate with China Mobile by calling 10086 to remove the number from the blacklist. |
| MK:0020 | China Mobile | ISP internal error | None |
| MK:0022 | China Mobile | ISP internal error | None |
| MN:0053 | China Mobile | ISP internal error | None |
| DB:0505 | China Mobile | ISP internal error | None |
| ID:0070 | China Mobile | ISP internal error | None |
| MX:0002 | China Mobile | Failed to submit SMS message to the higher channel | None |
| DB:0141 | China Mobile | User on the blacklist. This is because the user has filed complaints to China Mobile or MIIT for many times. | Cannot be removed from the blacklist. |
| MA:0051 | China Mobile | ISP internal error | None |
| IB:0008 | China Mobile | ISP internal error | None |
| MI00000 | China Mobile | SMS message has expired in SMC | None |
| DB:0164 | China Mobile | ISP blacklist | None |
| MK:0013 | China Mobile | Invalid number | None |
| DB:0144 | China Mobile | User on the global blacklist | None |
| BWLIST | China Mobile | Gateway blacklist | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) to remove the number from the blacklist. |
| HD:19 | China Mobile | Gateway blacklist | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) to remove the number from the blacklist. |
| MI0020 | China Mobile | Failed to send SMS message to mobile device (ErrorinMS) | None |
| MI:0041 | China Mobile | ISP internal error | None |
| MC:0055_006 | China Mobile | Failed to send SMS message because user's phone is out of the service area or the memory is full | Verify whether the mobile device is normal. |
| MI:0064 | China Mobile | ISP internal error | None |
| ERR_NUM_006 | China Mobile | Target number is incorrect or restricted. | Verify whether the mobile device is normal. |
| MI:0057 | China Mobile | ISP internal error | None |
| MI:0056 | China Mobile | Response timeout | Verify whether the mobile device is normal. |
| MI:0098 | China Mobile | ISP internal error | None |
| MK:0036 | China Mobile | Unknown error from MSC | None |
| MN:0019 | China Mobile | ISP internal error | None |
| MI:0030 | China Mobile | ISP internal error | None |
| MI:0023 | China Mobile | ISP internal error | None |
| MI:0002 | China Mobile | ISP internal error | None |
| MK:0019 | China Mobile | SMS message termination business is not supported for MS. | Verify whether the mobile device is normal. |
| IB:0064 | China Mobile | Powered off | Verify whether the mobile device is normal. |
| MB:1026 | China Mobile | SMC-related parameters (such as MO speed, MT speed, number of SMS messages, number of SMS message entities) have reached the upper limit of license. | Submit the SMS message again later. |
| MK:0055 | China Mobile | ISP internal error | None |
| MK:0066 | China Mobile | ISP internal error | None |
| MI00022 | China Mobile | The memory of mobile device is full. | Verify whether the mobile device is normal. |
| IB:0009 | China Mobile | ISP internal error | None |
| MK:0006 | China Mobile | ISP internal error | None |
| MK:0053 | China Mobile | ISP internal error | None |
| MK:0023 | China Mobile | ISP internal error | None |
| MK:0045 | China Mobile | ISP internal error | None |
| MC:0055_000 | China Mobile | Failed to send SMS message because user's phone is out of the service area or the memory is full | Verify whether the mobile device is normal. |
| MA:0054 | China Mobile | ISP internal error | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| MK:0041 | China Mobile | ISP internal error | None |
| MK:0063 | China Mobile | ISP internal error | None |
| ID:0012 | China Mobile | Incorrect billing address | Verify whether the mobile device is normal. |
| MK:0084 | China Mobile | HLR response: receipt of unexpected response | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| MB:0088 | China Mobile | ISP internal error | None |
| MI00036 | China Mobile | ISP internal error | None |
| DB00144 | China Mobile | Target number is blocked by the global blacklist. | None |
| MA:0073 | China Mobile || Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| MI:0099 | China Mobile | vmsc response: receipt of unexpected response | Verify whether the mobile device is normal. |
| MI:0089 | China Mobile | ISP internal error | None |
| MI:0063 | China Mobile | ISP internal error | None |
| MI:0090 | China Mobile | vmsc response: remote address is unreachable | Verify whether the mobile device is normal. |
| MN0013 | China Mobile | The Mobile device is out of service. | Verify whether the mobile device is normal. |
| DB:0107 | China Mobile | ISP internal error | None |
| IB:0255 | China Mobile | ISP internal error | None |
| MA:0022 | China Mobile | ISP internal error | None |
| IB:0013 | China Mobile | ISP internal error | None |
| MA:0001 | China Mobile | ISP internal error | None |
| MK:0065 | China Mobile | No response from GIW due to timeout | None |
| MN:0009 | China Mobile | ISP internal error | None |
| UNKNOWN | China Mobile | Unknown SMS status | None |
| DB:0010 | China Mobile | ISP internal error | None |
| MK:0021 | China Mobile | ISP internal error | None |
| MI:0038 | China Mobile | ISP internal error | None |
| MI:0052 | China Mobile | Roaming restriction | None |
| MK:0003 | China Mobile | Invalid user. User authentication failed when this SMS message is sent. The possible reason is that MSC considers the authentication password of the mobile phone to be invalid. The error code is 3 in maintenance and test console and 9 in ETSI GSM 0902 protocol. | None |
| MK:0009 | China Mobile | User is out of the service area MWDSET. | None |
| MK:0051 | China Mobile | ISP internal error | None |
| MK:0068 | China Mobile | ISP internal error | None |
| DB:0106 | China Mobile | Service code error | None |
| MB:1031 | China Mobile | SMC response: the upper limit of SMS delivery has been reached, which is probably because the phone memory is full. | Verify whether the mobile device is normal. |
| MI:0048 | China Mobile | ISP internal error | None |
| MK:0056 | China Mobile | ISP internal error | None |
| MK:0057 | China Mobile | ISP internal error | None |
| MK:0088 | China Mobile | vmsc response: possible version mismatch | None |
| TUIDING | China Mobile | ISP blacklist | None |
| HIGRISK | China Mobile | ISP blacklist | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) to remove the number from the blacklist. |
| CA:0054 | China Mobile | China Mobile internal error | None |
| MN:0041 | China Mobile | The phone is powered off, temporarily unavailable, or in other exceptional statuses. | None |
| MK:0090 | China Mobile | The phone is powered off, temporarily unavailable, or in other exceptional statuses. | None |
| XL:169 | China Mobile | The number is invalid or does not exist. | None |
| MN:xxxx | China Mobile | Error codes starting with M refer to Mobile, which are mostly caused by the problems occurred in mobile device. Possible reasons include: powered off, out of service, poor signal, out of the service area, invalid number, etc. | None |
| MI:xxxx | China Mobile | Error codes starting with M refer to Mobile, which are mostly caused by the problems occurred in mobile device. Possible reasons include: powered off, out of service, poor signal, out of the service area, invalid number, etc. | None |
| TA:169 | China Mobile | Invalid number | None |
| TC:0001 | China Mobile | Number on the blacklist | Contact [SMS Helper](https://cloud.tencent.com/document/product/382/3773) for communication. |
| TC:0007 | China Mobile | SMS message contains sensitive words | Contact [SMS Helper](https://cloud.tencent.com/document/product/382/3773) for communication. |
| 12 | China Unicom | Incorrect billing address (invalid number, out-of-service phone, powered-off phone, call restriction or user transferred to China Unicom Secretary) | Verify whether the mobile device is normal. |
| 1 | China Unicom | The number is invalid or does not exist. | Verify whether the mobile device is normal. |
| 10 | China Unicom | Incorrect Src_ID (invalid number, out-of-service phone, powered-off phone, call restriction or user transferred to China Unicom Secretary) | Verify whether the mobile device is normal. |
| 24 | China Unicom | Invalid billing number (no longer in use) | Verify whether the mobile device is normal. |
| 5 | China Unicom | The number is out of service. | Verify whether the mobile device is normal. |
| 29 | China Unicom | Incorrect user information | Verify whether the mobile device is normal. |
| 13 | China Unicom | Business code is not assigned. The corresponding declaration item cannot be found according to the access number and service code in the MT bill. | Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated. |
| 93 | China Unicom | Monthly rent authentication failed (out of service or cancellation of account) | Verify whether the mobile device is normal. |
| 11 | China Unicom | ISP internal error | None |
| 4 | China Unicom | Powered off | Verify whether the mobile device is normal. |
| 54 | China Unicom | Powered off | Verify whether the mobile device is normal. |
| 59 | China Unicom | ISP internal error | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| 15 | China Unicom | The mobile number is out of the service area. | Verify whether the mobile device is normal. |
| 23 | China Unicom | ISP internal error | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| 27 | China Unicom | SMS service is not supported. | Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated. |
| W-BLACK | China Unicom | Number on the global blacklist | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) to remove the number from the blacklist. |
| 17 | China Unicom | ISP internal error | None |
| 51 | China Unicom | Powered off | Verify whether the mobile device is normal. |
| -37 | China Unicom | Powered off | Verify whether the mobile device is normal. |
| 20 | China Unicom | Out of service | Verify whether the mobile device is normal. |
| 55 | China Unicom | The mobile number is out of the service area. | Verify whether the mobile device is normal. |
| 67 | China Unicom | Invalid number | Verify whether the mobile device is normal. |
| 95 | China Unicom | Authentication failed due to cancellation or inexistence of account. | Verify whether the mobile device is normal. |
| 22 | China Unicom | ISP internal error | None |
| 90 | China Unicom | ISP internal error | None |
| -74 | China Unicom | ISP internal error | None |
| 2 | China Unicom | ISP internal error | None |
| 104 | China Unicom | ISP internal error | None |
| 92 | China Unicom | |Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| 86 | China Unicom | Out of the service area | None |
| 50 | China Unicom | Out of service | None |
| 8 | China Unicom | Message length error | None |
| 57 | China Unicom | ISP internal error | None |
| 79 | China Unicom | The memory is full. | Verify whether the mobile device is normal. |
| 53 | China Unicom | Powered off | Verify whether the mobile device is normal. |
| 3 | China Unicom | ISP internal error | None |
| 255 | China Unicom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| 100 | China Unicom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| 61 | China Unicom | Invalid number | Verify whether the mobile device is normal. |
| 117 | China Unicom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| 45 | China Unicom | Out of service | Verify whether the mobile device is normal. |
| 164 | China Unicom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| 46 | China Unicom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| 14 | China Unicom | ISP internal error | None |
| 9 | China Unicom | Invalid sequential number, including repetition, wrong format, etc. | Verify whether the mobile device is normal. |
| 69 | China Unicom | User on the blacklist | None |
| 89 | China Unicom | The mobile number is out of the service area. | Verify whether the mobile device is normal. |
| 64 | China Unicom | The mobile number is out of the service area. | Verify whether the mobile device is normal. |
| 88 | China Unicom | The mobile number is out of the service area. | Verify whether the mobile device is normal. |
| 98 | China Unicom | Out of service | Verify whether the mobile device is normal. |
| 18 | China Unicom | User does not subscribe to the service | Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated. |
| 36 | China Unicom | Out of service | Verify whether the mobile device is normal. |
| 44 | China Unicom | The SMS function is unavailable on the mobile phone. | Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated. |
| 99 | China Unicom | Out of service | Verify whether the mobile device is normal. |
| 43 | China Unicom | The memory is full. | Verify whether the mobile device is normal. |
| -43 | China Unicom | The memory is full. | Verify whether the mobile device is normal. |
| 118 | China Unicom | The SMS function is unavailable on the mobile phone. | Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated. |
| 52 | China Unicom | The mobile device is incapable of receiving SMS messages. | Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated. |
| 31 | China Unicom | Invalid device. | Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated. |
| 75 | China Unicom | Number restriction | Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated. |
| 103 | China Unicom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| 56 | China Unicom | In arrears and out of service | Verify whether the mobile device is normal. |
| 106 | China Unicom | Invalid fee. Authentication failed. | None |
| -1 | China Unicom | ISP internal error | None |
| 19 | China Unicom | User does not subscribe to the service. | None |
| 148 | China Unicom | ISP internal error | None |
| 48 | China Unicom | ISP internal error | None |
| 63 | China Unicom | ISP internal error | None |
| 73 | China Unicom | ISP internal error | None |
| 70 | China Unicom | The mobile number is out of the service area. | Verify whether the mobile device is normal. |
| 32 | China Unicom | ISP internal error | None |
| 40 | China Unicom | ISP internal error | None |
| 110 | China Unicom | ISP internal error | None |
| 116 | China Unicom | ISP internal error | None |
| 21 | China Unicom | ISP internal error | None |
| 219 | China Unicom | User's mobile device cannot receive SMS messages because it is powered off, out of service, temporarily unavailable, or in other exceptional statuses. | None |
| 182 | China Unicom | User's mobile device is temporarily out of service. | None |
| 124 | China Unicom | User's mobile device is powered off, restricted from calling, temporarily out of service, or in other exceptional statuses. | None |
| 101 | China Unicom | Mobile number is invalid. | None |
| 105 | China Unicom | The phone is powered off, restricted from calling, temporarily out of service, or in other exceptional statuses. | None |
| 213 | China Unicom | The phone is powered off, restricted from calling, temporarily out of service, or in other exceptional statuses. | None |
| 72 | China Unicom | The number segment 145 is invalid or does not exist. | None |
| LT:0002 | China Unicom | Connection failed due to poor signal. In case of batch delivery failure (it may be caused by sensitive words), verify with ISP. | None |
| UNDELIV_601 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| EXPIRED_602 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_640 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| REJECTD_006 | China Telecom | SMS message is rejected for some reason. | Verify whether the message is business SMS message. If so, contact China Telecom customer service to check whether the SMS service is activated. |
| UNDELIV_705 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| EXPIRED_760 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| EXPIRED_601 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_869 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_999 | China Telecom | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| UNDELIV_602 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_614 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| EXPIRED_660 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_713 | China Telecom | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| UNDELIV_615 | China Telecom | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| EXPIRED_702 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| EXPIRED_640 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| REJECTD_706 | China Telecom | SMS message is rejected for some reason. | Verify whether the message is business SMS message. If so, contact China Telecom customer service to confirm whether the SMS service is activated. |
| EXPIRED_615 | China Telecom |SMS message is rejected for some reason. | Verify whether the mobile device is normal. |
| UNDELIV_765 | China Telecom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| UNDELIV_870 | China Telecom | ISP internal error | None |
| UNDELIV_899 | China Telecom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| EXPIRED_001 | China Telecom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| UNDELIV_612 | China Telecom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| UNDELIV_714 | China Telecom | | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |
| UNDELIV_702 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_815 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_771 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_711 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_627 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_814 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_660 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| EXPIRED_612 | China Telecom | ISP internal error | None |
| UNDELIV_613 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_619 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_680 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_636 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_726 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_718 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_880 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_634 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| EXPIRED_010 | China Telecom | SMS message expired | No response from the mobile device due to timeout |
| EXPIRED_619 | China Telecom | SMS message expired | No response from the mobile device due to timeout |
| EXPIRED_999 | China Telecom | SMS message expired | No response from the mobile device due to timeout |
| UNDELIV_001 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| UNDELIV_620 | China Telecom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | Verify whether the mobile device is normal. |
| EXPIRED_614 | China Telecom | ISP internal error | None |
| EXPIRED_618 | China Telecom | ISP internal error | None |
| EXPIRED_613 | China Telecom | ISP internal error | None |
| EXPIRED_617 | China Telecom | ISP internal error | None |
| UNDELIV_701 | China Telecom | Invalid number, out-of-service phone or powered-off phone | None |
| UNDELIV_802 | China Telecom | Invalid number, out-of-service phone or powered-off phone | None |
| UNDELIV_801 | China Telecom | Invalid number, out-of-service phone or powered-off phone | None |
| UNDELIV | China Telecom/China Unicom | User's mobile device cannot receive SMS messages because it is out of service, suspended or in other exceptional statuses. | None |
| MOBILE BLACK | China Telecom/China Unicom | Number on the global blacklist | [Contact SMS Helper](https://cloud.tencent.com/document/product/382/3773) to remove the number from the blacklist. |
| Other | China Telecom/China Unicom | Reason not announced by ISP | Provide the phone number to [SMS Helper](https://cloud.tencent.com/document/product/382/3773) and submit a ticket to verify with ISP. |

