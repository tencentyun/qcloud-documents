Xiaomi Push channel, a system-level push channel, is **officially provided by Xiaomi**. Messages pushed from Xiaomi mobile phones can reach terminal devices through Xiaomi's system channel, and users can receive pushed content without opening the application. XGPush 3.2.0 or above must be integrated before this feature can be used.

>**[Notes]**
>The feature is under internal trial. Confirm whether the corresponding column is on console, More columns will be available soon.

## Obtaining Xiaomi Push Key
Create a Xiaomi developer account as instructed on the [Xiaomi Open Platform](https://dev.mi.com/console/appservice/push.html), then register the application, and obtain Xiaomi Push key. Send the Xiaomi Push key and your access ID of XGPush via email to dtsupport@tencent.com, or add QQ: 2631775454. The access ID of XGPush and Xiaomi Push key need to be bound manually at the backend of XGPush.

**Verify Xiaomi developer:**
![](//mc.qcloudimg.com/static/img/0dad64af035fb3cce34c5e6ea64cbedf/image.jpg)
**Obtain Xiaomi Push key:**
![](//mc.qcloudimg.com/static/img/228ad72acdf1c1be765077df231080ab/image.jpg)

## Configuring Xiaomi Push
### It is recommended to use jcenter dependency for the connection during the development of Android Studio
1. Introduce the jar package of Xiaomi Push.
```
//Add the jar package of Xiaomi Push after XGPush has been integrated
compile 'com.tencent.xinge:mipush:3.2.2-release'
```
2. Create a class inheritance Xiaomi **PushMessageReceiver**, and configure it in **Androidmanif.xml**. This node must be configured as required by Xiaomi.
```
<receiver
android:exported="true"
android:name="complete path+class name, for example: com.qq.xgdemo.receiver.MiMessageReceiver">
<intent-filter>
<action android:name="com.xiaomi.mipush.RECEIVE_MESSAGE" />
</intent-filter>
<intent-filter>
<action android:name="com.xiaomi.mipush.MESSAGE_ARRIVED" />
</intent-filter>
<intent-filter>
<action android:name="com.xiaomi.mipush.ERROR" />
</intent-filter>
</receiver>
```

### Connection during Eclipse development
1. Introduce the jar package of Xiaomi Push, which can be downloaded from Xiaomi Push official website.
2. Add the configuration of Xiaomi Push after XGPush has been integrated:
```
</application>
<service
android:name="com.xiaomi.push.service.XMPushService"
android:enabled="true"
android:process=":pushservice" />
<service
android:name="com.xiaomi.push.service.XMJobService"
android:enabled="true"
android:exported="false"
android:permission="android.permission.BIND_JOB_SERVICE"
android:process=":pushservice" />
<!-- Note: This service to be added must be version 3.0.1 or above -->
<service
android:name="com.xiaomi.mipush.sdk.PushMessageHandler"
android:enabled="true"
android:exported="true" />
<service
android:name="com.xiaomi.mipush.sdk.MessageHandleService"
android:enabled="true" />
<!-- Note: This service to be added must be version 2.2.5 or above -->
<receiver
android:name="com.xiaomi.push.service.receivers.NetworkStatusReceiver"
android:exported="true" >
<intent-filter>
<action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
<category android:name="android.intent.category.DEFAULT" />
</intent-filter>
</receiver>
<receiver
android:name="com.xiaomi.push.service.receivers.PingReceiver"
android:exported="false"
android:process=":pushservice" >
<intent-filter>
<action android:name="com.xiaomi.push.PING_TIMER" />
</intent-filter>
</receiver>
</application>
<!-- Note: The permission "begin" required for Xiaomi Push -->
<permission
android:name="application package name.permission.MIPUSH_RECEIVE"
android:protectionLevel="signature" />
<!-- The com.example.mipushtest here should be changed to the application package name -->
<uses-permission android:name="application package name.permission.MIPUSH_RECEIVE" />
<!-- The com.example.mipushtest here should be changed to the application package name -->
<!-- Note: The permission "end" required for Xiaomi Push -->
```
3. Create a class inheritance Xiaomi PushMessageReceiver, and configure it in Androidmanif.xml. This node must be configured as required by Xiaomi.
```
<receiver
android:exported="true"
android:name="complete path+class name, for example: com.qq.xgdemo.receiver.MiMessageReceiver">
<intent-filter>
<action android:name="com.xiaomi.mipush.RECEIVE_MESSAGE" />
</intent-filter>
<intent-filter>
<action android:name="com.xiaomi.mipush.MESSAGE_ARRIVED" />
</intent-filter>
<intent-filter>
<action android:name="com.xiaomi.mipush.ERROR" />
</intent-filter>
</receiver>
```

#### Launching Xiaomi Push
Set Xiaomi App ID and App KEY.
```
XGPushConfig.setMiPushAppId(getApplicationContext(), "APPID");
XGPushConfig.setMiPushAppKey(getApplicationContext(), "APPKEY");
//Enable third-party push
XGPushConfig.enableOtherPush(getApplicationContext(), true);
//Log for successful registration is as follows:
12-02 16:17:32.299 12584-12584/com.qq.xgdemo I/XINGE: [XGPushManager] Action -> Register to xinge server
12-02 16:17:32.996 12584-12584/com.qq.xgdemo I/XINGE: [XGPushManager] Register call back to com.qq.xgdemo
12-02 16:17:32.997 12584-12626/com.qq.xgdemo I/XINGE: [XGPushManager] XG register push success with token : 1d31bb3ea6185baebdf05dfc2e586dfe5dc41fb5
12-02 16:17:33.001 12584-12626/com.qq.xgdemo I/XINGE: [XGOtherPush] other push token is : YZQfRxmxdfNlbSKpNWCa3tM4Esnq6op4qeOsQO2qT88= other push type: xiaomi
```

## Obfuscated Code
```
-keepclasseswithmembernames class com.xiaomi.**{*;}
-keep public class * extends com.xiaomi.mipush.sdk.PushMessageReceiver
```

## How to Test Vendor Channel (General)
1. Integrate XGPush V 3.2.1 SDK in your App, and integrate required vendor SDK by following the "Guide on Integration of Vendor Channel".
2. Confirm that the relevant information has been entered in **Application Configuration** -> **Vendor & Oversees Channels** on the XGPush console. Generally, the configuration **takes effect in an hour, and after this you can proceed to the next step**.
3. Install the integrated App (test version) on the test machine, and run the App.
4. Keep the App running in the foreground, and perform single push/full push on the device.
5. If the App receives messages, switch the App to the background, and terminate all App progresses.
6. Perform single push/full push again. If the pushed content is received, then the vendor channel is integrated successfully.

