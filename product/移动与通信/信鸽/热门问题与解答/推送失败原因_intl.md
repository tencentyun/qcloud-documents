### Device Registration Failed
It generally takes a minute or so for a new App to synchronize data. A device registration during the synchronization process may cause the 20 error. Just try again later. For other cases leading to 20 error, check whether the access id and access key are correctly configured. Common errors are misuse of secret key or there are spaces at the start and end of access key.

### Account is not bound with the device
To push messages based on account, the account must be bound with the token first, otherwise the push fails.
>**Note:**
>The length of Android Token is 40 characters;
>The length of iOS Token is 64 characters;

Account, also known as alias, refers to the user account of the App with account login feature. It is not limited to QQ or WeChat. All user accounts are supported. For example, QQ number is the account of mobile QQ, email is the account of Gmail, and mobile phone number is the account of China Mobile.
>**Note:**
>A single character is not allowed in account (alias). A token can only be bound with one account. If multiple accounts are bound, only the last one can be bound successfully.
>A maximum of 15 devices can be bound under one account (namely, alias). When the limit is exceeded, the latest bound device randomly replaces a previously bound one.
>For Android, account is bound during registration via the API registerPush(context, account). For iOS, it is set via setAccount.

If you are prompted "token not found, check registration" after choosing an account for pushing, it indicates that the account is not associated with the token, which may be caused by the following:
1. The account or alias is logged out, which may not be called by the App, for logout may be automatically triggered in some cases.
2. The device is registered with another account or alias, so the original account is automatically unbound. (A device can only correspond to one alias. If there is no device under the current alias, the message "not found" appears.)

After an account is bound, notifications can be pushed by specifying an alias (account). Generally, all devices on which the account has recently logged in can receive the notifications. When the user account logs out, call registerPush(context,"") to unbind the current account.


### Service is terminated
Whether a terminated service can auto-activate is determined by the system, security software and user operations.
XGPush SDK communicates with XGPush backend via a unique service. For Android, the service can auto-activate after termination if the auto-activation is not forbidden by the system/security software. For more information, please search "Android service onstartcommand START_STICKY" on Internet.
If the auto-activation is forbidden by the security software, or in some customized systems (such as MIUI), XGPush service can be restarted only after the user open the App again. When XGPush service can be started is determined by the system scheduling. XGPush actively tries to start the service in the cases of locking screen and touch screen, network switching, App installation, system restart and more.

### iOS Certificate
If you are prompted "failed to load certificate, check your APNS certificate" in the iOS push, it indicates that the APNS certificate for the corresponding environment is not submitted, which may be caused by a certificate generated inappropriately. Please create the certificate by following the official guideline.
- Check whether the push environment is selected correctly. For test preview, select the development environment.
- Check whether the push environment is selected correctly. Development certificates correspond to test environment, while production certificates correspond to the formal environment.

Validity period of the certificate
![](//mc.qcloudimg.com/static/img/53669cfcf59794d336608ed0b22556f4/image.png)
Connect to APNS to test whether the certificate is valid.
Development environment ![](//mc.qcloudimg.com/static/img/99e241715f9c901c655cd970c12af68b/image.png)
Production environment ![](//mc.qcloudimg.com/static/img/0b315804df15922666ad6458ff5b716e/image.png)

### Message Latency
As most Internet services, the push service on Android platform is affected by the quality of network service, operator policies, differences in user requirements and other factors, so latency may occur. In addition, if XGPush service on the terminal is terminated by the system or security software, the device may fail to receive messages or push latency may occur.
For iOS platform, XGPush is only responsible to successfully forward messages to APNS. However, whether APNS can deliver messages to users successfully, how many messages are delivered, and how many are lost depend on the quality of network service, operator policies and other factors.

>**Note:**
>APNS only saves one message for the offline terminal. The offline terminal can only receive the latest message pushed during the offline period after it goes online.

### Troubleshooting Method

1. Check whether the device is connected to Internet properly.
2. Check whether the settings of accessId and accessKey is consistent with those configured when registering at the frontend.
3. Check whether the current package name of App is consistent with that configured when registering at the frontend. If no, choose the option "Use multiple package names" at the frontend.
4. Check whether the device is registered successfully.
5. When the notification is pushed from the frontend, check whether the time period in the "Period control" option is consistent with the current time of the terminal device.
6. Check whether the receiver matches the service tag in the xml. It is highly recommended to directly copy the demo example and then modify it.
7. Check whether "Android.permission.GET_TASKS" permission is added.


### Push Suspension

1. A push with the same content for all devices cannot be recreated within one hour.
2. A maximum of 30 full pushes can be created per hour.

