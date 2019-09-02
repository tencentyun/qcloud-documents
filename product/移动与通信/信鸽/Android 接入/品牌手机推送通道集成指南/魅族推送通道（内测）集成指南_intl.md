Meizu Push channel, a system-level push channel, is **officially provided by Meizu**. Messages pushed from Meizu mobile phones can reach terminal devices through Meizu's system channel, and users can receive pushed content without opening the application. XGPush 3.2.1-beta or above must be integrated before this feature can be used.

>**[Notes]**
>1. The feature is under internal trial. Confirm whether the corresponding column is on console, More columns will be available soon.
>2. For Meizu Push channel, the title of notification cannot exceed 32 characters and the content cannot exceed 100 characters.
>3. Transparent transmission of messages is not supported for Meizu Push channel

## Obtaining Meizu Push Key
1. Open [Meizu Push Official Website](https://open.flyme.cn/open-web/views/push.html).
2. Sign up for a developer account or log in with developer account. Identity verification is required for new accounts, and it takes about 2 days. For more information, please contact Meizu.
3. Create an application on Meizu Push platform (Note: "Application package name" must be consistent with the package name you entered in XGPush).
4. Obtain the information of the application, and copy these information to the XGPush console, including App ID, App Key, AppSecret.
![](//mc.qcloudimg.com/static/img/92ea5d33a94ca749b5046c6efe427458/image.png)
>Note: For more information, please see [Meizu development document](http://open.res.flyme.cn/fileserver/upload/file/201709/a271468fe23b47408fc2ec1e282f851f.pdf).

5. Enter the push key in **[XGPush Console](http://xg.qq.com/)** -> **Application Configuration** -> **Vendor & Oversees Channels** -> **Meizu Push Channel**.

## Integration Method
### How to Integrate Android Studio
1. Add the dependency required by Meizu channel to build.gradle under the App module (use the default repository jcenter of Androidstudio);
```
compile 'com.tencent.xinge:xgmz:3.3.1-3-alpha'
```
2. Configure Meizu message receiver.


### How to Integrate Eclipse
1. Import the jar package required by Meizu channel (pushsdk-3.3.170110.jar) to libs directory.
2. Implement the following configuration under Androidmanifest:

```
<application>
<service
    android:name="com.meizu.cloud.pushsdk.NotificationService"
     android:exported="true"/>
<receiver android:name="com.meizu.cloud.pushsdk.SystemReceiver" >
     <intent-filter>
      <action android:name="com.meizu.cloud.pushservice.action.PUSH_SERVICE_START"/>
      <category android:name="android.intent.category.DEFAULT" />
     </intent-filter>
 </receiver>
</application>
 <!-- Note: The permission "begin" required for Meizu Push -->
 <!-- Compatible with flyme5.0 or below. The pushSDK integrated in Meizu is required, otherwise no message will be received-->
  <uses-permission android:name="com.meizu.flyme.push.permission.RECEIVE"></uses-permission>
  <permission android:name="Application package name.push.permission.MESSAGE" 
                   android:protectionLevel="signature"/>
  <uses-permission android:name="Application package name.push.permission.MESSAGE"></uses-permission>
  <!--  Compatible with flyme3.0 configuration permission-->
  <uses-permission android:name="com.meizu.c2dm.permission.RECEIVE" />
  <permission android:name="Application package name.permission.C2D_MESSAGE"
              android:protectionLevel="signature">
  </permission>
  <uses-permission android:name="Application package name.permission.C2D_MESSAGE"/>
<!-- Note: The permission "end" required for Meizu Push -->
```

### Meizu Message Receiver
To customize the broadcasting for Meizu messages, you need to create a class inheritance (MzPushMessageReceiver). Then, configure the following node in Androidmanifest.xml:
```
<!-- Default custom broadcasting receiver, which is used to customize the broadcasting of Meizu push messages. The name of receiver is the custom broadcasting receiving class "start" -->
<receiver android:name="Application package name.MzReceiver">
    <intent-filter>
        <!-- Receive push message -->
        <action android:name="com.meizu.flyme.push.intent.MESSAGE" />
        <!-- Receive register message -->
         <action android:name="com.meizu.flyme.push.intent.REGISTER.FEEDBACK"/>
        <!-- Receive unregister message -->
         <action android:name="com.meizu.flyme.push.intent.UNREGISTER.FEEDBACK"/>
         <action android:name="com.meizu.c2dm.intent.REGISTRATION" />
         <action android:name="com.meizu.c2dm.intent.RECEIVE" />
         <category android:name="Application package name"></category>
     </intent-filter>
</receiver>
```

## Registration of Launch Code and Log output
Configure the following code before launching XGPush (XGPushManager.registerPush):
```
//Set Meizu APPID and APPKEY
XGPushConfig.enableOtherPush(context, true);
XGPushConfig.setMzPushAppId(this, APP_ID);
XGPushConfig.setMzPushAppKey(this, APP_KEY);
```
Log for successful registration is as follows:
```
//The application is registered successfully if both XGPush token and Meizu token have been obtained and bound successfully
INFO16:24:27.94313075XINGE[a] >> bind OtherPushToken success ack with [accId = 2100273138 , rsp = 0] token = 08d7ea8e4b93952cbfdd2cb68461342c314d281a otherPushType = meizu otherPushToken = ULY6c5968627059714a475c63517f675b7f655e62627e
```
## Obfuscated Code
```
-dontwarn com.meizu.cloud.pushsdk.**
-keep class com.meizu.cloud.pushsdk.**{*;}
```
## How to Test Vendor Channel (General)
1. Integrate XGPush V 3.2.1 SDK in your App, and integrate required vendor SDK by following the "Guide on Integration of Vendor Channel".
2. Confirm that the relevant information has been entered in **Application Configuration** -> **Vendor & Oversees Channels** on the XGPush console. Generally, the configuration takes effect in an hour, and after this you can proceed to the next step.
3. Install the integrated App (test version) on the test machine, and run the App.
4. Keep the App running in the foreground, and perform single push/full push on the device.
5. If the App receives messages, switch the App to the background, and terminate all App progresses.
6. Perform single push/full push again. If the pushed content is received, then the vendor channel is integrated successfully.

