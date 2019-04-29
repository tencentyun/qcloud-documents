## Android Platform

### Multi-line Display
Android multi-line display feature has been implemented in version 2.38 or above and is enabled by default. The main code is shown below. Search and confirm it in your project: `NotificationCompat.BigTextStyle bigText = new NotificationCompat.BigTextStyle();`
`bigText.bigText(this.tickerText); build.setStyle(bigText);`

### Multi-package-name Push
Some Apps have different package names for different channels. A single App may have hundreds of package names. In this case, you can push messages to all package names of the App using access id. In the multi-package-name push mode, all Apps on the device that are registered with push service using this access id will receive the messages. Multi-package-name push for a single App involves the following three steps:

1) Register the App at XGPush. The package name is not required and will not affect the push effect.
2) Integrate the latest SDK in the App.
3) Set the push parameter multi_pkg to 1 before pushing.

### What if the following error occurs?

```
android.app.IntentReceiverLeaked: Activity com.xxxx has leaked IntentReceiver com.tencent.android.tpush.f@422a4dc8 that was originally registered here. Are you missing a call to unregisterReceiver()?
```
Cause: activity finishes before the registration in XGPush returns. As a result, the receiver registered in XGPush is not cancelled.
Solution: Change the context passed by registerPush to context.getApplicationContext().

### How to delete the Toast prompt of "Registration Successful"?

Cause: The CustomPushReceiver in the demo carries a Toast prompt.
Solution: Delete the content related to Toast in CustomPushReceiver.

### Many .so files used for different platforms exist in the libs directory, such as armabi, x86.

Cause: XGPush developed the .so library for all Android platforms.
Solution: Unnecessary platform directories can be deleted. For example, for games that only use armabi, other directories can be deleted.

### What to do if an activity page often cannot be opened?

Reason: In some mobile phones, the notification bar is not permitted to be redirected to a page.
Solution: Add Android:exported="true" in AndroidManifest.xml for the activity to be opened.

### Does XGPush still work without SD card?

Yes, but the log will be written into different places.

### Can the registration method be created in the thread? Can it be created in APPLICATON onCreate?

The registration method can be called anywhere, but applicationContext must be passed.

## iOS Platform

### Why is the pem certificate required?

A: The pem certificate is used for establishing a connection with Apple. When you upload the pem certificate, XGPush will try to connect to the Apple server to verify its validity.

### If the following error occurs:
![](//mc.qcloudimg.com/static/img/af6242c39daa43c033722e7e74842a79/image.png)
Configure as follows in your project:
![](//mc.qcloudimg.com/static/img/63a02331e81edbaa5c9a4f179d828e98/image.png)

### If the following error occurs:
![](//mc.qcloudimg.com/static/img/ee63d1718366a4023563145e1616c0c9/image.png)
Configure as follows in your project:
The provisioning profile file needs to contain the device being debugged, and the provisioning profile file must be generated after APNS is enabled in the App.

### Why cannot XGPush provide statistics about arrivals for iOS?
Due to the restrictions of Apple system, XGPush cannot count the arrivals after the messages are pushed. However, if users click on the message, XGPush can count the click action and report it.
Due to the restrictions of APNS and iOS, some statistical errors may exist.

### What to do if I cannot upload the iOS certificate?
Check if the certificate format is correct.

### What to do if the certificate verification failed?
Please create the certificate by strictly following the iOS Certificate Setup Guide.

### When I click Push, it prompts: failed to load certificate, check your APNS certificate

1) The APNS certificate for the corresponding environment is not submitted.
2) The certificate is not created correctly. Please refer to the official guideline for creation.
3) Check whether the push environment is selected correctly. For test preview, select the development environment.

### What is the difference between a development certificate and a production certificate? 
A development certificate is used for the development of the push service. The deviceToken obtained by the device is the deviceToken of the development environment issued by Apple.
A production certificate is used for formal delivery. Apple issues a deviceToken for the production environment, and after the App Store approval is obtained, all devices with the App installed can receive the push.

### Why can't I compile my project on iPhone 5s after connection with XGPush?
Configure Xcode as follows, and delete the arm 64d in the corresponding Target's Valid Architectures.

### What does it mean if the followings occur when I register an iOS SDK in XGPush?

[xgpush seccess]rspCode is 0
[xgpush]Disconnected.

A: The first message indicates that the registration is successful. The second message indicates that the server will be disconnected if a message is returned by the server or timeout occurs.

### If an account is registered with multiple devices, what to do to allow all these devices to get push messages??

A: Call registerDevice again after you call setAccount. For more information, please see how to configure/delete an account.


