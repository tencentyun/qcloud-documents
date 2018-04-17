Here is detailed description:

| Value | Description | Solution |
|-|-|-|
| 0 | Successful call |
| -1 | Parameter error | Check parameter configuration |
| -2 | The request timestamp is not within the validity period | Check the current time of the device |
| -3 | The sign failed to pass verification | Check Access ID and Secret Key (not Access Key) |
| 2 | Parameter error | Check parameter configuration |
| 14 | Invalid token. For example, the iOS terminal does not get the correct token | Length of Android Token is 40 characters, and that of iOS Token is 64 characters. |
| 15 | XGPush logic server is busy. | Try again later |
| 19 | The operation timing is wrong. For example, deviceToken is not obtained before tag operation | Reasons: 1. XGPush or Apple Push is not registered; 2. Provisioning profile is not made correctly |
| 20 | Authentication error. It may be caused by mismatch of Access ID and Access Key | Check Access ID and Access Key |
| 40 | Pushed token is not registered on XGPush | Check if token is registered |
| 48 | The account for push is not bound with token | For more information on how to check if the account is bound with token, please see the FAQ of binding account and device in the push guide. |
| 63 | Label system is busy | For more information on how to check if the label is set successfully, please see Label Setting in the push guide. |
| 71 | APNS server is busy | Apple server is busy. Try again later |
| 73 | The number of message characters exceeds the limit | iOS supports around 1,000 bytes. Apple's extra push settings such as a corner mark also consume bytes. |
| 76 | Requests are initiated too frequently. Try again later | The frequency limit for full broadcast is once every 3 seconds. |
| 78 | Loop task parameter error | - |
| 100 | APNS certificate error. Please re-submit the correct certificate | The certificate format is pem. Please pay attention to the difference between production certificate and development certificate.
| Others | Other errors | - |

