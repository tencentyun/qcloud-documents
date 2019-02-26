Huawei Push channel, a system-level push channel, is **officially provided by Huawei**. Messages pushed from Huawei mobile phones can reach terminal devices through Huawei's system channel, and users can receive pushed content without opening the application. XGPush 3.2.1-beta or above must be integrated before this feature can be used.

>Note:
1. The feature is under internal trial. Confirm whether the corresponding column is on console, More columns will be available soon.
2. Huawei Push can receive pushed messages only under the **environment of signature publishing package**.
3. **Mobile Push Service** in Huawei mobile phones must be upgraded to **version 2.5.3 or above**, otherwise the registration of Huawei channel may fail and XGPush channel is used by default.

## Obtaining Huawei Push Key
1. Open [Huawei Open Platform](http://developer.huawei.com/cn/).
2. Sign up for a developer account or log in with developer account (identity verification is required for new accounts).
3. Create an application on Huawei Push platform (Note: "Application package name" must be consistent with the package name you entered in XGPush).
4. Obtain the information of the application, and copy these information to the XGPush console, including App ID, AppSecret.
![](//mc.qcloudimg.com/static/img/8a753e59f1472707827cbc7774ff7988/image.jpg)

## Configuring SHA 256 Certificate Fingerprint
**[Configuration Example]**
![](//mc.qcloudimg.com/static/img/1b031caf8bf6d9413277b4a5696b26c4/image.jpg)
For more information on how to obtain SHA256 certificate fingerprint, please see [Connect to Huawei Push](http://developer.huawei.com/consumer/cn/service/hms/catalog/huaweipush_agent.html?page=hmssdk_huaweipush_introduction_agent).

## Integration Guide
### How to Integrate Android Studio
First, complete the configuration required for XGPush in the build.gradle file under the App module, and add the following Huawei node:

1. Configure Huawei AppId.
```
	manifestPlaceholders = [ 
				HW_APPID: "Huawei APPId"
						]
```
2. Import dependencies of Huawei Push.

```
	compile ' com.tencent.xinge:xghw:2.5.2.300-release'
```

### How to Integrate Eclipse
1. Import jar package of Huawei Push, and put HMSSdkBase*.jar and HMSSdkPush*.jar in the libs folder.
2. Add the following configuration in the Androidmanifest.xml file:
```
	<meta-data
            android:name="com.huawei.hms.client.appid"
            android:value="Your APPID (from Huawei official website)" >
        </meta-data>

        <activity
            android:name="com.huawei.hms.activity.BridgeActivity"
            android:configChanges="orientation|locale|screenSize|layoutDirection|fontScale"
            android:excludeFromRecents="true"
            android:exported="false"
            android:hardwareAccelerated="true"
            android:theme="@android:style/Theme.Translucent" >
         <meta-data
                android:name="hwc-theme"
                android:value="androidhwext:style/Theme.Emui.Translucent" />
        </activity>

        <provider
            android:name="com.huawei.hms.update.provider.UpdateProvider"
            android:authorities="com.qq.otherpush.hms.update.provider"
            android:exported="false"
            android:grantUriPermissions="true" >
        </provider>      

        <receiver android:name="com.huawei.hms.support.api.push.PushEventReceiver" >
            <intent-filter>
                <!-- Receive messages in the notification bar sent from the push channel. The old version of PUSH is compatible -->
                <action android:name="com.huawei.intent.action.PUSH" />
            </intent-filter>
        </receiver>
         <!-- Note: The end required by Huawei Push -->
```
3. Configure Huawei message receiver.

#### Huawei Message Receiver
1. It is customizable, and inherits **com.huawei.hms.support.api.push.PushReceiver**, with a related node configured in **Androidmanifest.xml**.
Sample code:
```
    public class MyReceiver extends PushReceiver {
    @Override
    public void onEvent(Context context, Event arg1, Bundle arg2) {
        super.onEvent(context, arg1, arg2);
        showToast("onEvent" + arg1 + " Bundle " + arg2 ,  context);
    }
    @Override
    public boolean onPushMsg(Context context, byte[] arg1, Bundle arg2) {
        showToast("onPushMsg" + new String(arg1) + " Bundle " + arg2 ,  context);
        return super.onPushMsg(context, arg1, arg2);
    }
    @Override
    public void onPushMsg(Context context, byte[] arg1, String arg2) {
        showToast("onPushMsg" + new String(arg1) + " arg2 " + arg2 ,  context);
        super.onPushMsg(context, arg1, arg2);
    }
    @Override
    public void onPushState(Context context, boolean arg1) {
        showToast("onPushState" + arg1,  context);
        super.onPushState(context, arg1);
    }
    @Override
    public void onToken(Context context, String arg1, Bundle arg2) {
        super.onToken(context, arg1, arg2);
         showToast(" onToken" + arg1 + "bundke " + arg2,  context);
    }
    @Override
    public void onToken(Context context, String arg1) {
        super.onToken(context, arg1);
         showToast(" onToken" + arg1 ,  context);
    }
    public  void showToast(final String toast, final Context context)
    {
        new Thread(new Runnable() {
            @Override
            public void run() {
                Looper.prepare();
                Toast.makeText(context, toast, Toast.LENGTH_SHORT).show();
                Looper.loop();
            }
        }).start();
    }

    private void  writeToFile(String conrent) {
        String SDPATH = Environment.getExternalStorageDirectory() + "/huawei.txt";
        try {
            FileWriter fileWriter = new FileWriter(SDPATH, true);
            fileWriter.write(conrent+"\r\n");
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }				
    }
```    
2. Add a custom **Receiver** under **AndroidManifest.xml**, as shown below:
```
<!-- xxx.xx.xx is the name of broadcasting defined by CP, for example: com.huawei.hmssample. HuaweiPushRevicer -->
        <receiver android:name=".MyReceiver" >
            <intent-filter>
                <!-- Required, used to receive TOKEN -->
                <action android:name="com.huawei.android.push.intent.REGISTRATION" />
                <!-- Required, used to receive messages -->
                <action android:name="com.huawei.android.push.intent.RECEIVE" />
                <!-- Optional, used to trigger onEvent callback after you click on the notification bar or the button on notification bar -->
                <action android:name="com.huawei.android.push.intent.CLICK" />
                <!-- Optional, used to check whether PUSH channel is connected, otherwise it is not required -->
                <action android:name="com.huawei.intent.action.PUSH_STATE" />
            </intent-filter>
        </receiver>
```


### Launching Huawei Push and Log for Successful Registration
Enable third-party push API before calling XGPush (XGPushManager.registerPush):
```
//Enable third-party push
XGPushConfig.enableOtherPush(getApplicationContext(), true);
```
Log for successful registration is as follows:
```
01-15 16:40:41.116 17916-17934/? I/XINGE: [XGOtherPush] other push token is : 0865551032618726300001294600CN01 other push type: huawei
01-15 16:40:41.122 15730-15846/? I/XINGE: [a] binder other push token with accid = 2100274337  token = 17c32948df0346d5837d4748192e9d2f14c81e08 otherPushType = huawei otherPushToken = 0865551032618726300001294600CN01
```
If the log of `otherPushType = huawei otherPushToken = null,` appears, call `XGPushConfig.setHuaweiDebug(true);` before registering the code
Developer needs to confirm the application storage permission manually, and then check the returned error code for failed Huawei registration outputted from huawei.txt file under SD card directory. Finally, find a solution according to the corresponding error code in [Huawei development document](http://developer.huawei.com/consumer/cn/service/hms/catalog/huaweipush_agent.html?page=hmssdk_huaweipush_api_reference_errorcode).

### Obfuscated Code
```
-ignorewarning
-keepattributes *Annotation*
-keepattributes Exceptions
-keepattributes InnerClasses
-keepattributes Signature
-keepattributes SourceFile,LineNumberTable
-keep class com.hianalytics.android.**{*;}
-keep class com.huawei.updatesdk.**{*;}
-keep class com.huawei.hms.**{*;}
```

## How to Test Vendor Channel
1. Integrate XGPush V3.2.1 SDK in your App, and integrate required vendor SDK by following the "Guide on Integration of Vendor Channel".
2. Confirm that the relevant information has been entered in **Application Configuration** -> **Vendor & Oversees Channels** on the XGPush console. Generally, the configuration takes effect in an hour, and after this you can proceed to the next step.
3. Install the integrated App (test version) on the test machine, and run the App.
4. Keep the App running in the foreground, and perform single push/full push on the device.
5. If the App receives messages, switch the App to the background, and terminate all App progresses.
6. Perform single push/full push again. If the pushed content is received, then the vendor channel is integrated successfully.

