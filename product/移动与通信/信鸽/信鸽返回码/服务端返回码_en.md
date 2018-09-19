List of server error codes:

| Value | Description | Solution |
|-|-|-|
| 0 | Successful call |
| -1 | Parameter error | Check parameter configuration |
| -2 | The request timestamp is not within the validity period | Check the current time of the device |
| -3	| recv failed | Try again later |
| -5 |	Action processing timeout |	Try again later |
| 2 | Invalid parameter | Check parameter configuration |
| 5 | Failed to communicate with CMEM | Try again later |
| 7 | General error. The number of accounts exceeds the limit. | Delete other unused accounts (call the account unbinding). |
| 14 | Invalid token. | Length of Android Token is 40 characters, and that of iOS Token is 64 characters. |
| 15 | XGPush logic server is busy. | Try again later |
| 16 | System is busy. | Try again later |
| 19 | The operation timing is wrong. For example, deviceToken is not obtained before tag operation | Reasons: 1. XGPush or Apple Push is not registered; 2. Provisioning profile is not made correctly |
| 20 | Authentication error. It may be caused by mismatch of Access ID and Access Key | Check Access ID and Access Key (check spaces) |
| 21 | Authentication failed | Check Access ID and Access Key |
| 40 | Pushed token is not registered on XGPush | Check if token is registered |
| 48 | The account for push is not bound with token | For more information on how to check if the account is bound with token, please see the FAQ of binding account and device in the push guide. |
| 53 | The device is not registered | Re-register the device after unregistering it. |
| 73 | The number of message characters exceeds the limit | iOS supports around 1,000 bytes. Apple's extra push settings such as a corner mark also consume bytes. |
| 75 | Message body does not conform to json format | Check message body, i.e. content of the message field. |
| 76 | Requests are initiated too frequently. Try again later | The frequency limit for full broadcast is once every 3 seconds. |
| 78 | Loop task parameter error | Check loop time |
| 90 | The device is offline | Re-open the App |
| 91 | Too many tags for the device | Clear unused tags |
| 92 | Too many apptags | Clear unused tags |
| 100 | APNS certificate error. Please re-submit the correct certificate | The certificate format is pem. Please pay attention to the difference between production certificate and development certificate.
| -101 | Parameter error | Check parameters |
| -102 | Request's timestamp field is expired | Use timestamp of the current system to ensure time synchronization. |
| -103 | Invalid sign | Check the signature generation process and METHOD must be the same as the one used for the request when you generate a sign. |
| -105 | Requests are initiated too frequently. | Try again later |
| -106 | Certificate error | Certificate error |
| -111 | Common parameter access_id\timestamp\sign is missing | Check common parameter access_id\timestamp\sign |
| -112 | Invalid parameter value | Check the parameter value |
| Others | Internal XGPush errors | If an unknown error occurs and can be repeated, please contact us. |


