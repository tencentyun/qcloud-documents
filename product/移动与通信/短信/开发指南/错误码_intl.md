## 1. Error Codes for SMS Delivery
<table style="word-break:break-all; word-wrap:break-all;">
<thead><tr><th style="width:15%;">Error Code</th><th style="width:45%;">Reason</th><th style="width:35%;">Solution</th></tr></thead>
  <tbody>
<tr><td>1001</td><td>sig verification failed.</td><td>Check the sig format of the API.</td></tr>
<tr><td>1002</td><td>Text/Voice SMS contains sensitive words.</td><td>A response packet including these sensitive words is returned. Delete these words and send again.</td></tr>
<tr><td>1003</td><td>sig field is missing or left empty in request packet.</td><td>Comply with the specifications in API description.</td></tr>
<tr><td>1004</td><td>Failed to resolve request packet. This is generally because the specifications in API description is not complied with.</td><td>Refer to <a href="https://intl.cloud.tencent.com/document/product/382/9558#what-can-i-do-if-a-1004-error-is-returned.3F">1004 error description.</a></td></tr>
<tr><td>1006</td><td>No permission to request. For example, no extended code permission, etc.</td><td>Check error message. For other questions, provide the mobile number from which you failed to send SMS message when you <a href="/doc/product/382/3773">contact SMS Helper.</a></td></tr>
<tr><td>1007</td><td>Other error</td><td>Check error message. For other questions, provide the mobile number from which you failed to send SMS message when you <a href="/doc/product/382/3773">contact SMS Helper.</a></td></tr>
<tr><td>1008</td><td>Request to send text/voice SMS timed out.</td><td>Rare occurrence. Try again.</td></tr>
<tr><td>1009</td><td>Request ip is not on the whitelist.</td><td>Verification of request's source ip has been configured, but the current request ip is not found in the configuration list. If necessary, <a href="/doc/product/382/3773">contact SMS Helper.</a></td></tr>
<tr><td>1011</td><td>REST API does not exist.</td><td>Check REST API description.</td></tr>
<tr><td>1012</td><td>Signature format is incorrect or signature is not approved.</td><td>Signature is a combination of 2-8 characters comprised of English letter and numbers only. If the signature format is correct, check whether it is approved.</td></tr>
<tr><td>1013</td><td>Text/Voice SMS hits the delivery frequency limit policy. </td><td>You can adjust the delivery frequency limit policy for text SMS messages on the console. For voice SMS messages, <a href="/doc/product/382/3773">contact SMS Helper.</a></td></tr>
<tr><td>1014</td><td>Template is not approved or request content does not match the approved template content.</td><td>Refer to <a href="https://intl.cloud.tencent.com/document/product/382/9558#what-can-i-do-if-a-1014-error-is-returned.3F">1014 error description.</a></td></tr>
<tr><td>1015</td><td>Number on the blacklist. This is generally because you unsubscribed from the SMS service or hit the operator's blacklist.</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>to solve the problem.</td></tr>
<tr><td>1016</td><td>Incorrect number format</td><td>Check whether the format of the mobile number from which you send text/voice SMS is correct.</td></tr>
<tr><td>1017</td><td>The content of the requested SMS is too long.</td><td>The length of SMS content exceeds the limit. Adjust the length of SMS content.</td></tr>
<tr><td>1018</td><td>The format of voice verification code is incorrect.</td><td>Comply with the specifications in the API description.</td></tr>
<tr><td>1019</td><td>sdkappid does not exist.</td><td></td></tr>
<tr><td>1020</td><td>sdkappid is disabled.</td><td>This sdkappid is unavailable. If necessary, <a href="/doc/product/382/3773">contact SMS Helper.</a></td></tr>
<tr><td>1021</td><td>The time when the request was initiated is exceptional. This is generally because the difference between the time on your server and that on the Tencent Cloud server exceeds 10 minutes.</td><td>Check whether the server time and the time field in the API are normal.</td></tr>
<tr><td>1022</td><td>The number of business SMS messages sent every day exceeds the upper limit.</td><td>You can adjust the SMS delivery frequency limit policy on the console.</td></tr>
<tr><td>1023</td><td>The number of SMS messages sent from a single mobile number within 30 seconds exceeds the upper limit.</td><td>You can adjust the SMS delivery frequency limit policy on the console.</td></tr>
<tr><td>1024</td><td>The number of SMS messages sent from a single mobile number within 1 hour exceeds the upper limit.</td><td>You can adjust the SMS delivery frequency limit policy on the console.</td></tr>
<tr><td>1025</td><td>The number of SMS messages sent from a single mobile number every day exceeds the upper limit.</td><td>You can adjust the SMS delivery frequency limit policy on the console.</td></tr>
<tr><td>1026</td><td>The number of the same SMS messages sent from a single mobile number exceeds the upper limit.</td><td>You can adjust the SMS delivery frequency limit policy on the console.</td></tr>
<tr><td>1029</td><td>Time constraint on delivering marketing SMS messages.</td><td>To avoid disturbing users, marketing SMS messages are only allowed to be sent between 8:00 and 22:00.</td></tr>
<tr><td>1030</td><td>This request is not supported.</td><td></td></tr>
<tr><td>1031</td><td>Insufficient balance in SMS package.</td><td>Purchase package.</td></tr>
<tr><td>1032</td><td>Individual user does not have the permission to send marketing SMS messages.</td><td></td></tr>
<tr><td>1033</td><td>Service is suspended due to arrears.</td><td>You can top up your account by logging in to Tencent Cloud to pay off the overdraft.</td></tr>
</table>

## 2 Error Codes for Status Report
<table style="word-break:break-all; word-wrap:break-all;">
<thead><tr><th style="width:15%;">Error Code</th><th style="width:10%;">Category</th><th style="width:35%;">Reason</th><th style="width:35%;">Solution</th></tr></thead>
  <tbody>
    <tr><td>DELIVRD</td><td>Three major operators</td><td>SMS message is received successfully.</td><td>None</td></tr>
    <tr><td>UNDELIVRD</td><td>Three major operators</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MX:0003</td><td>Three major operators</td><td>The number of MT SMS messages sent from a single mobile number on the day exceeds the limit.</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>to remove the limit.</td></tr>
    <tr><td>REJECTD</td><td>Three major operators</td><td>SMS message is rejected for some reason.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MX:0012</td><td>Three major operators</td><td>The target number is on the customer unsubscription blacklist.</td><td>The user is added to the blacklist after replying to the unsubscription SMS massage.<a href="/doc/product/382/3773">Contact SMS Helper </a>to remove the number from the blacklist.</td></tr>
    <tr><td>MX:0011</td><td>Three major operators</td><td>The target number is on the blacklist of one-year prohibition.</td><td>The blacklist of one-year prohibition lists the phone numbers of users who file malicious complaints and of those who make complaints for multiple times.</td></tr>
    <tr><td>BWLIST _006</td><td>Three major operators</td><td>Gateway blacklist</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>to solve the problem through communication.</td></tr>
    <tr><td>TE:0003</td><td>Three major operators</td><td>The number of MT SMS messages sent from a single mobile number on the day exceeds the limit.</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>to remove the limit.</td></tr>
    <tr><td>TE:0014</td><td>Three major operators</td><td>Manual verification failed</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>for communication.</td></tr>
    <tr><td>TE:0002</td><td>Three major operators</td><td>Failed to submit SMS messages to gateway</td><td>None</td></tr>
    <tr><td>TD:0001</td><td>Three major operators</td><td>Gateway blacklist</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>for communication.</td></tr>
    <tr><td>TD: 0004 </td><td>Three major operators</td><td>Suspected of fishing. Make a check.</td><td></td></tr>
    <tr><td>TD:19</td><td>Three major operators</td><td>Number on the blacklist</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>to solve the problem through communication.</td></tr>
    <tr><td>TD:18</td><td>Three major operators</td><td>Number from unknown operator</td><td>None</td></tr>
    <tr><td>UNDELIV</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI:0013</td><td>China Mobile</td><td>Out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MN:0001</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MK:0012</td><td>China Mobile</td><td>Invalid number</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MK:0005</td><td>China Mobile</td><td>Whether the No. 21 value-added service attribute of the account opening data of the target user is supported.</td><td>If the number status is normal, the user can contact local operator's customer service to confirm whether the SMS service is enabled.</td></tr>
    <tr><td>MK:0005</td><td>China Mobile</td><td>You are prohibited from calling. Your SMS service is disabled. The error code is 5 in maintenance and test console and 13 in ETSI GSM 0902 protocol.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MK:0000</td><td>China Mobile</td><td>Invalid number</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN:0054</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MK:0001</td><td>China Mobile</td><td>MK0001 means that this number is not found by HLR. The status returned from SMC is unrecognized number, indicating that the SMS message is sent to a wrong number.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>EXPIRED</td><td>China Mobile</td><td>SMS message expired</td><td>Failed to receive SMS message due to no response from the mobile device after a long period of time.</td></tr>
    <tr><td>MI:0024</td><td>China Mobile</td><td>Out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MI:0011</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MC:0151</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>IC:0001</td><td>China Mobile</td><td>Out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MI:0029</td><td>China Mobile</td><td>Out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MI:0005</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MK:0004</td><td>China Mobile</td><td>Out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MI:0000</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MI:0022</td><td>China Mobile</td><td>China Mobile gateway internal error</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>IA:0054</td><td>China Mobile</td><td>Failed to receive response message due to timeout</td><td>Verify whether the mobile device is normal. Restart the phone and try again.</td></tr>
    <tr><td>MC:0055</td><td>China Mobile</td><td>Failed to send SMS message because user's phone is out of the service area or the memory is full</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN:0059</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN:0036</td><td>China Mobile</td><td>User's phone was out of the service area.</td><td>Verify whether the mobile device is normal. SMS delivery failed because the user is busy.</td></tr>
    <tr><td>MI:0004</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MI:0020</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MK:0029</td><td>China Mobile</td><td>Temporarily unavailable</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI:0084</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MK:0024</td><td>China Mobile</td><td>Failed to send SMS message because the target phone is powered off.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MK00001</td><td>China Mobile</td><td>Invalid number</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI:0017</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MK:0015</td><td>transaction</td><td>When an SMS message is sent, the target phone has a software problem in the process of receiving message. For example, after the phone is restarted, the software for processing the SMS message is not initialized to process the message normally.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN:0029</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>IC:0151</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN:0075</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0010</td><td>China Mobile</td><td>Temporarily unavailable</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>IC:0015</td><td>China Mobile</td><tdOperater's internal error</td><td>None</td></tr>
    <tr><td>BEYONDN</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0055</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MI:0010</td><td>China Mobile</td><td>The number has expired</td><td>None</td></tr>
    <tr><td>MC00151</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>IC:0055</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MB:1078</td><td>China Mobile</td><td>Operater's internal error</td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>MN00001</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>ID:0013</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MC:0001</td><td>China Mobile</td><td>Unknown error</td><td>None</td></tr>
    <tr><td>MK: 0017 </td><td>China Mobile</td><td>The memory is full.</td><td>The space for storing SMS messages is full. Free up space by clearing the SMS messages stored in the phone.</td></tr>
    <tr><td>MI:0081</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>DA:0054</td><td>China Mobile</td><td>Failed to receive response message due to timeout</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MB:1042</td><td>China Mobile</td><td>The number of SMS messages cached in the SMC memory and to be sent to the target user exceeds the maximum number of SMS messages received by this user.</td><td>Check the number of the SMS messages sent to the target number in the SMC memory. If the number has reached the maximum number of SMS messages received by the target user, submit again later.</td></tr>
    <tr><td>ERR_NUM</td><td>China Mobile</td><td>Target number is incorrect or restricted.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI:0054</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MI:0011</td><td>China Mobile</td><td>Out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MN:0052</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0008</td><td>China Mobile</td><td>Failed to receive SMS message due to poor signal in the location of the user.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>IA:0073</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>IA:0051</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0075</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN:0022</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN:0020</td><td>China Mobile</td><td>China Mobile gateway internal error</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI00029</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0008</td><td>China Mobile</td><td>China Mobile gateway internal error</td><td>None</td></tr>
    <tr><td>MK:0012</td><td>China Mobile</td><td>Invalid device</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN:0012</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI:0059</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>MN:0050</td><td>China Mobile</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN:0017</td><td>China Mobile</td><td>SMS message rejected</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI:0045</td><td>China Mobile</td><td>China Mobile gateway internal error</td><td>None</td></tr>
    <tr><td>MN:0055</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>NOROUTE</td><td>China Mobile</td><td>No route found</td><td>None</td></tr>
    <tr><td>MI:0036</td><td>China Mobile</td><td>China Mobile gateway internal error</td><td>None</td></tr>
    <tr><td>MB:1077</td><td>China Mobile</td><td>User on the blacklist. This is because China Mobile keeps a record of the user's malicious complaints.</td><td>The user need to communicate with China Mobile by calling 10086 to remove the number from the blacklist.</td></tr>
    <tr><td>MI:0020</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0022</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MN:0053</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>DB:0505</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>ID:0070</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MX:0002</td><td>China Mobile</td><td>Failed to submit SMS message to the higher channel</td><td>None</td></tr>
    <tr><td>DB:0141</td><td>China Mobile</td><td>User on the blacklist. This is because the user has filed complaints against China Mobile or MIIT for many times.</td><td>Cannot be removed from the blacklist.</td></tr>
    <tr><td>MA:0051</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>IB:0008</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI00000</td><td>China Mobile</td><td>SMS message has expired in SMC</td><td>None</td></tr>
    <tr><td>DB:0164</td><td>China Mobile</td><td>Operater's blacklist</td><td>None</td></tr>
    <tr><td>MI:0013</td><td>China Mobile</td><td>Invalid number</td><td>None</td></tr>
    <tr><td>DB:0144</td><td>China Mobile</td><td>User on the global blacklist</td><td>None</td></tr>
    <tr><td>BWLIST</td><td>China Mobile</td><td>Gateway blacklist</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>to remove the number from the blacklist.</td></tr>
    <tr><td>HD:19</td><td>China Mobile</td><td>Gateway blacklist</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>to remove the number from the blacklist.</td></tr>
    <tr><td>MI00020</td><td>China Mobile</td><td>Failed to send SMS message to mobile device (ErrorinMS)</td><td>None</td></tr>
    <tr><td>MI:0041</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MC:0055_006</td><td>China Mobile</td><td>Failed to send SMS message because user's phone is out of the service area or the memory is full</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI:0064</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>ERR_NUM_006</td><td>China Mobile</td><td>Target number is incorrect or restricted.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI:0057</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0056</td><td>China Mobile</td><td>Response timeout</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN:0098</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0036</td><td>China Mobile</td><td>Unknown error from MSC. </td><td>None</td></tr>
    <tr><td>MN:0019</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0030</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0023</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0002</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0019</td><td>China Mobile</td><td>SMS message termination business is not supported for MS.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>IB:0064</td><td>China Mobile</td><td>Powered off</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MB:1026</td><td>China Mobile</td><td>SMC-related parameters (such as MO speed, MT speed, number of SMS messages, number of SMS message entities) have reached the upper limit of License.</td><td>Submit the SMS message again later.</td></tr>
    <tr><td>MK:0055</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0066</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI00022</td><td>China Mobile</td><td>The memory of mobile device is full.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>IB:0009</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0006</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0053</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0023</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0045</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MC:0055_000</td><td>China Mobile</td><td>Failed to send SMS message because user's phone is out of the service area or the memory is full</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MA:0054</td><td>China Mobile</td><td>Operater's internal error</td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>MK:0041</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0063</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>ID:0012</td><td>China Mobile</td><td>Incorrect billing address</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MK:0084</td><td>China Mobile</td><td>HLR response: receipt of unexpected response</td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>MB:0088</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI00036</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>DB00144</td><td>China Mobile</td><td>Target number is blocked by the global blacklist.</td><td>None</td></tr>
    <tr><td>MA:0073</td><td>China Mobile</td><td></td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>MI:0099</td><td>China Mobile</td><td>vmsc response: receipt of unexpected response</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI:0089</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0063</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0090</td><td>China Mobile</td><td>vmsc response: remote address is unreachable</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MN00013</td><td>China Mobile</td><td>The Mobile device is out of service.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>DB:0107</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>IB:0255</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MA:0022</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>IB:0013</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MA:0001</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0065</td><td>China Mobile</td><td>No response from GIW due to timeout</td><td>None</td></tr>
    <tr><td>MN:0009</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>UNKNOWN </td><td>China Mobile</td><td>Unknown SMS status</td><td>None</td></tr>
    <tr><td>DB:0010</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0021</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0038</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MI:0052</td><td>China Mobile</td><td>Roaming restriction</td><td>None</td></tr>
    <tr><td>MK:0003</td><td>China Mobile</td><td>Invalid user. User authentication failed when this SMS message is sent. The possible reason is that MSC considers the authentication password of the mobile phone to be invalid. The error code is 3 in maintenance and test console and 9 in ETSI GSM 0902 protocol.</td><td>None</td></tr>
    <tr><td>MK:0009</td><td>China Mobile</td><td>User is out of the service area MWDSET.</td><td>None</td></tr>
    <tr><td>MK:0051</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0068</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>DB:0106</td><td>China Mobile</td><td>Service code error</td><td>None</td></tr>
    <tr><td>MB:1031</td><td>China Mobile</td><td>SMC response: the maximum number of deliveries exceeds the limit probably because the phone memory is full.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MI:0048</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK00011</td><td>China Mobile</td><td>The SMS service is unavailable on the mobile device.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>MK:0048</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0056</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0057</td><td>China Mobile</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>MK:0088</td><td>China Mobile</td><td>vmsc response: possible version mismatch</td><td>None</td></tr>
    <tr><td>TUIDING</td><td>China Mobile</td><td>Operater's blacklist</td><td>None</td></tr>
    <tr><td>HIGRISK</td><td>China Mobile</td><td>Gateway blacklist</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>to remove the number from the blacklist.</td></tr>
    <tr><td>CA:0054</td><td>China Mobile</td><td>China Mobile internal error</td><td>None</td></tr>
    <tr><td>MN:0041</td><td>China Mobile</td><td>The phone is powered off, temporarily unavailable, or exceptional due to other reasons.</td><td>None</td></tr>
    <tr><td>MK:0090</td><td>China Mobile</td><td>The phone is powered off, temporarily unavailable, or exceptional due to other reasons.</td><td>None</td></tr>
    <tr><td>XL:169</td><td>China Mobile</td><td>The number is invalid or does not exist.</td><td>None</td></tr>
    <tr><td>MN:xxxx</td><td>China Mobile</td><td>Error codes starting with M refer to Mobile, which are mostly caused by the problems occurred in mobile device. Possible reasons include: powered off, out of service, poor signal, out of the service area, invalid number, etc.</td><td>None</td></tr>
    <tr><td>MK:xxxx</td><td>China Mobile</td><td>Error codes starting with M refer to Mobile, which are mostly caused by the problems occurred in mobile device. Possible reasons include: powered off, out of service, poor signal, out of the service area, invalid number, etc.</td><td>None</td></tr>
    <tr><td>MI:xxxx</td><td>China Mobile</td><td>Error codes starting with M refer to Mobile, which are mostly caused by the problems occurred in mobile device. Possible reasons include: powered off, out of service, poor signal, out of the service area, invalid number, etc.</td><td>None</td></tr>
    <tr><td>TA:169</td><td>China Mobile</td><td>Invalid number</td><td>None</td></tr>
    <tr><td>TC:0001</td><td>China Mobile</td><td>Number on the blacklist</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>to solve the problem through communication.</td></tr>
    <tr><td>TC:0007</td><td>China Mobile</td><td>SMS message contains sensitive words.</td><td><a href="/doc/product/382/3773">Contact SMS Helper </a>to solve the problem through communication.</td></tr>
    <tr><td>12</td><td>China Unicom</td><td>Incorrect billing address (invalid number, out-of-service phone, powered-off phone, call restriction or user transferred to China Unicom Secretary)</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>1</td><td>China Unicom</td><td>The number is invalid or does not exist.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>10</td><td>China Unicom</td><td>Incorrect Src_ID (invalid number, out-of-service phone, powered-off phone, call restriction or user transferred to China Unicom Secretary)</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>24</td><td>China Unicom</td><td>Invalid billing number (no longer in use)</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>5</td><td>China Unicom</td><td>The number is out of service.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>29</td><td>China Unicom</td><td>Mobile user information error</td><td>Verify whether the mobile number is normal.</td></tr>
    <tr><td>13</td><td>China Unicom</td><td>Business code is not assigned. The corresponding declaration item cannot be found according to the access number and service code in the MT bill.</td><td>Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated.</td></tr>
    <tr><td>93</td><td>China Unicom</td><td>Monthly rent authentication failed (out of service or cancellation of account) </td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>11</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>4</td><td>China Unicom</td><td>Powered off</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>54</td><td>China Unicom</td><td>Powered off</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>59</td><td>China Unicom</td><td>Operater's internal error</td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>15</td><td>China Unicom</td><td>Out of the service area</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>23</td><td>China Unicom</td><td>Operater's internal error</td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>27</td><td>China Unicom</td><td>SMS service is not supported.</td><td>Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated.</td></tr>
    <tr><td>W-BLACK</td><td>China Unicom</td><td>Number on the global blacklist</td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper </a>to remove the number from the blacklist.</td></tr>
    <tr><td>17</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>51</td><td>China Unicom</td><td>Powered off</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>-37</td><td>China Unicom</td><td>Powered off</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>20</td><td>China Unicom</td><td>Out of service</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>55</td><td>China Unicom</td><td>Out of the service area</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>67</td><td>China Unicom</td><td>Invalid number</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>95</td><td>China Unicom</td><td>Authentication failed due to cancellation or inexistence of account.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>22</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>90</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>-74</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>2</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>104</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>92</td><td>China Unicom</td><td></td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>86</td><td>China Unicom</td><td>Out of the service area</td><td>None</td></tr>
    <tr><td>50</td><td>China Unicom</td><td>Out of service</td><td>None</td></tr>
    <tr><td>8</td><td>Unicom</td><td>Message length error</td><td>None</td></tr>
    <tr><td>57</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>79</td><td>China Unicom</td><td>The memory is full.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>53</td><td>China Unicom</td><td>Powered off</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>3</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>255</td><td>China Unicom</td><td></td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>100</td><td>China Unicom</td><td></td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>61</td><td>China Unicom</td><td>Invalid number</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>117</td><td>China Unicom</td><td></td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>45</td><td>China Unicom</td><td>Out of service</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>164</td><td>China Unicom</td><td></td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>46</td><td>China Unicom</td><td></td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>14</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>9</td><td>China Unicom</td><td>Invalid sequential number, including repetition, wrong format, etc.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>69</td><td>China Unicom</td><td>User on the blacklist</td><td>None</td></tr>
    <tr><td>89</td><td>China Unicom</td><td>Out of the service area</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>64</td><td>China Unicom</td><td>Out of the service area</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>88</td><td>China Unicom</td><td>Out of the service area</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>98</td><td>China Unicom</td><td>Out of service</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>18</td><td>China Unicom</td><td>User does not subscribe to the service</td><td>Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated.</td></tr>
    <tr><td>36</td><td>China Unicom</td><td>Out of service</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>44</td><td>China Unicom</td><td>The SMS function is unavailable on the mobile phone.</td><td>Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated.</td></tr>
    <tr><td>99</td><td>China Unicom</td><td>Out of service</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>43</td><td>China Unicom</td><td>The memory is full.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>-43</td><td>China Unicom</td><td>The memory is full.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>118</td><td>China Unicom</td><td>The SMS function is unavailable on the mobile phone.</td><td>Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated.</td></tr>
    <tr><td>52</td><td>China Unicom</td><td>The mobile device is incapable of receiving SMS messages.</td><td>Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated.</td></tr>
    <tr><td>31</td><td>China Unicom</td><td>Invalid device.</td><td>Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated.</td></tr>
    <tr><td>75</td><td>China Unicom</td><td>Number restriction</td><td>Verify whether the mobile device is normal. If it is normal, contact China Unicom customer service to confirm whether the SMS service is activated.</td></tr>
    <tr><td>103</td><td>China Unicom</td><td></td><td>Provide the specific mobile number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>56</td><td>China Unicom</td><td>In arrears and out of service</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>106</td><td>China Unicom</td><td>Invalid fee. Authentication failed.</td><td>None</td></tr>
    <tr><td>-1</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>19</td><td>China Unicom</td><td>User does not subscribe to the service.</td><td>None</td></tr>
    <tr><td>148</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>48</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>63</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>73</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>70</td><td>China Unicom</td><td>The mobile number is out of the service area.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>32</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>40</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>110</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>116</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>21</td><td>China Unicom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>219</td><td>China Unicom</td><td>SMS messages cannot be received because the user's mobile device is powered off, out of service, temporarily unavailable, or exceptional due to other reasons.</td><td>None</td></tr>
    <tr><td>182</td><td>China Unicom</td><td>User's mobile device is temporarily out of service.</td><td>None</td></tr>
    <tr><td>124</td><td>China Unicom</td><td>User's mobile device is powered off, restricted from calling, temporarily out of service, or exceptional due to other reasons.</td><td>None</td></tr>
    <tr><td>101</td><td>China Unicom</td><td>Mobile number is invalid.</td><td>None</td></tr>
    <tr><td>105</td><td>China Unicom</td><td>The phone is powered off, restricted from calling, temporarily out of service, or exceptional due to other reasons.</td><td>None</td></tr>
    <tr><td>213</td><td>China Unicom</td><td>The phone is powered off, restricted from calling, temporarily out of service, or exceptional due to other reasons.</td><td>None</td></tr>
    <tr><td>72</td><td>China Unicom</td><td>145 number segment is not invalid or does not exist</td><td>None</td></tr>
    <tr><td>LT:0002</td><td>China Unicom</td><td>Connection failed due to poor signal. In case of batch delivery failure that may be caused by sensitive words, you need to verify with operator.</td><td>None</td></tr>
    <tr><td>UNDELIV_601</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>EXPIRED_602</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_640</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>REJECTD_006</td><td>China Telecom</td><td>SMS message is rejected for some reason.</td><td>Verify whether the message is business SMS message. If so, contact China Telecom customer service to confirm whether the SMS service is activated.</td></tr>
    <tr><td>UNDELIV_705</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>EXPIRED_760</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>EXPIRED_601</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_869</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_999</td><td>China Telecom</td><td></td><td>Provide the specific mobile number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>UNDELIV_602</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_614</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>EXPIRED_660</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_713</td><td>China Telecom</td><td></td><td>Provide the specific mobile number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>UNDELIV_615</td><td>China Telecom</td><td></td><td>Provide the specific mobile number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>EXPIRED_702</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>EXPIRED_640</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>REJECTD_706</td><td>China Telecom</td><td>SMS message is rejected for some reason.</td><td>Verify whether the message is business SMS message. If so, contact China Telecom customer service to confirm whether the SMS service is activated.</td></tr>
    <tr><td>EXPIRED_615</td><td>China Telecom</td><td>SMS message is rejected for some reason.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_765</td><td>China Telecom</td><td></td><td>Provide the specific mobile number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>UNDELIV_870</td><td>China Telecom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>UNDELIV_899</td><td>China Telecom</td><td></td><td>Provide the specific mobile number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>EXPIRED_001</td><td>China Telecom</td><td></td><td>Provide the specific mobile number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>UNDELIV_612</td><td>China Telecom</td><td></td><td>Provide the specific mobile number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>UNDELIV_714</td><td>China Telecom</td><td></td><td>Provide the specific mobile number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
    <tr><td>UNDELIV_702</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_815</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_771</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_711</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_627</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_814</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_660</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>EXPIRED_612</td><td>China Telecom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>UNDELIV_613</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_619</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_680</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_636</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_726</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_718</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_880</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_634</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>EXPIRED_010</td><td>China Telecom</td><td>SMS message expired</td><td>No response from the mobile device due to timeout</td></tr>
    <tr><td>EXPIRED_619</td><td>China Telecom</td><td>SMS message expired</td><td>No response from the mobile device due to timeout</td></tr>
    <tr><td>EXPIRED_999</td><td>China Telecom</td><td>SMS message expired</td><td>No response from the mobile device due to timeout</td></tr>
    <tr><td>UNDELIV_001</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>UNDELIV_620</td><td>China Telecom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>Verify whether the mobile device is normal.</td></tr>
    <tr><td>EXPIRED_614</td><td>China Telecom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>EXPIRED_618</td><td>China Telecom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>EXPIRED_613</td><td>China Telecom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>EXPIRED_617</td><td>China Telecom</td><td>Operater's internal error</td><td>None</td></tr>
    <tr><td>UNDELIV_701</td><td>China Telecom</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>UNDELIV_701</td><td>China Telecom</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>UNDELIV_802</td><td>China Telecom</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>UNDELIV_801</td><td>China Telecom</td><td>Invalid number, out-of-service phone or powered-off phone</td><td>None</td></tr>
    <tr><td>UNDELIV</td><td>China Telecom/China Unicom</td><td>SMS messages cannot be received because user's phone is out of service, suspended or exceptional due to other reasons.</td><td>None</td></tr>
    <tr><td>MOBILE BLACK</td><td>China Telecom/China Unicom</td><td>Number on the global blacklist</td><td><a href="/doc/product/382/3773">Contact SMS Helper</a> to remove the number from the blacklist.</td></tr>
    <tr><td>Other</td><td>China Telecom/China Unicom</td><td>Reason not announced by operator</td><td>Provide the phone number to <a href="/doc/product/382/3773">SMS Helper</a> and submit a ticket to verify with operator.</td></tr>
  </tbody>
</table>
