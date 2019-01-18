### Registering and Downloading SDK
Go to XGPush Console [xg.qq.com](http://xg.qq.com/) and log in to the Application Registration page using QQ number. Enter the "Application Name" and "Application Package Name" (must be consistent with the application), select **Operating System** and **Category**, and then click **New Application**. After the application is successfully created, click **Application Configuration** to see its AccessId, AccessKey, and other information.
After registration is completed, download the latest version of the Android SDK to your local computer and decompress it.

### Configuring Project
Import the SDK into the project following the steps below:
1. Create or open an Android project. For more information on how to create an Android project, please see the Development Environment section.
2. Copy all the files in the libs directory under the XGPush SDK directory to the project's libs (or lib) directory.
3. Select the XGPush jar package in the libs (or lib) directory, select Build Path from the shown menu, and select Add to Build Path to add the SDK to the project's reference directory.
4. .so file is a necessary component of XGPush. It supports armeabi, armeabi-v7a, misp and x86. You need to add based on the platform supported by your .so file.
 a. If you do not use other .so files in your project, it is recommended to copy the four platform directories into your own project;
 b. If you already have .so files, you only need to copy the files in the corresponding directory of XGPush;
 c. If the game is connected via MSDK, only .so in the armeabi directory is required in most cases;
 d. If the current project already has armeabi, only .so under the armeabi of XGPush needs to be added. Do the same in other situations. You only need to add the platform that exists on the current platform.
 e. If an error (error: 10004.SOERROR) occurs when you import the .so file to Androidstudio, add a folder named jniLibs in the .main file directory, and then copy all the architecture files (all the files under Other-Platform-SO in the SDK) into the jniLibs folder, as shown below:
![](https://main.qcloudimg.com/raw/279d8aad18d43a109ccc18dba41c5885.png)
5. Open Androidmanifest.xml and add the following configurations. (It is recommended to modify the configurations according to the Demo in the download package.) Replace YOUR_ACCESS_ID and YOUR_ACCESS_KEY with the application's accessId and accessKey. Make sure the configurations are completed as required. Otherwise, the service may not work properly.
 
```
<application
  <!-- [Required] XGPush receiver for receiving broadcast -->
  <receiver android:name="com.tencent.android.tpush.XGPushReceiver"
   android:process=":xg_service_v3" >
  <intent-filter android:priority="0x7fffffff" >
        <!-- [Required] Internal broadcasting of XGPush SDK -->
        <action android:name="com.tencent.android.tpush.action.SDK" />
        <action android:name="com.tencent.android.tpush.action.INTERNAL_PUSH_MESSAGE" />
        <!-- [Required] System broadcasting: launch screen and network switchover -->
       <action android:name="android.intent.action.USER_PRESENT" />
       <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
       <!-- [Optional] Common System broadcastings for increasing the possibility of XGPush service reactivation. You can also add application-defined broadcastings to activate the service -->
       <action android:name="android.bluetooth.adapter.action.STATE_CHANGED" />
       <action android:name="android.intent.action.ACTION_POWER_CONNECTED" />
       <action android:name="android.intent.action.ACTION_POWER_DISCONNECTED" />
       </intent-filter>
  </receiver>

<!-- [Optional] Receiver implemented by the application for receiving callbacks of transparent message transmission and operation results. Add it as needed -->
 <!-- YOUR_PACKAGE_PATH.CustomPushReceiver needs to be changed to your own Receiver: -->
  <receiver android:name="com.qq.xgdemo.receiver.MessageReceiver"
      android:exported="true" >
      <intent-filter>
          <!-- Receive transparently transferred messages -->
          <action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
          <!-- Listen on the results of registration, unregistration, tag configuration/deletion, and clicks of notification -->
          <action android:name="com.tencent.android.tpush.action.FEEDBACK" />
      </intent-filter>
  </receiver>

   <!-- [Note] If the launch mode of the opened activity is SingleTop, SingleTask, or SingleInstance, process it according to clause 8 of the exception self-check list in the notification -->
   <activity
        android:name="com.tencent.android.tpush.XGPushActivity"
        android:exported="false" >
        <intent-filter>
           <!-- If AndroidStudio is used, set android:name="android.intent.action"-->
            <action android:name="" />
        </intent-filter>
   </activity>

   <!-- [Required] XGPush service -->
   <service
       android:name="com.tencent.android.tpush.service.XGPushServiceV3"
       android:exported="true"
       android:persistent="true"
       android:process=":xg_service_v3" />


  <!-- [Required] Increase the service survival rate -->
  <service
      android:name="com.tencent.android.tpush.rpc.XGRemoteService"
      android:exported="true">
      <intent-filter>
 <!-- [Required] Change to the current application name. PUSH_ACTION, for example, demo package name: com.qq.xgdemo -->
              <action android:name="Current application package name.PUSH_ACTION" />
      </intent-filter>
   </service>


<!-- [Required] [Note] Modify authorities to package name .AUTH_XGPUSH. For example, package name in demo is: com.qq.xgdemo-->
  <provider
       android:name="com.tencent.android.tpush.XGPushProvider"
       android:authorities="Current application package name.AUTH_XGPUSH"
       android:exported="true"/>

  <!-- [Required] [Note] Modify authorities to package name .TPUSH_PROVIDER. For example, package name in demo is: com.qq.xgdemo-->
  <provider
       android:name="com.tencent.android.tpush.SettingsContentProvider"
       android:authorities="Current application package name.TPUSH_PROVIDER"
       android:exported="false" />

  <!-- [Required] [Note] Modify authorities to package name .TENCENT.MID.V3. For example, package name in demo is: com.qq.xgdemo-->
  <provider
       android:name="com.tencent.mid.api.MidProvider"
       android:authorities="Current application package name.TENCENT.MID.V3"
       android:exported="true" >
  </provider>

<!-- [Required] Change YOUR_ACCESS_ID to the application's AccessId, which is a 10-digit number starting with "21" and has no spaces in between -->
   <meta-data
       android:name="XG_V2_ACCESS_ID"
       android:value="YOUR_ACCESS_ID" />
   <!-- [Required] Change YOUR_ACCESS_KEY to the application's AccessKey, which is a 12-digit string starting with "A" and has no spaces in between -->
   <meta-data
       android:name="XG_V2_ACCESS_KEY"
       android:value="YOUR_ACCESS_KEY" />
</application>
<!-- [Required] Permissions required for XGPush SDK   -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.VIBRATE" />
<!-- [Common] Permissions required for XGPush SDK -->
<uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_SETTINGS" />
<!-- [Optional] Permissions required for XGPush SDK -->
<uses-permission android:name="android.permission.RESTART_PACKAGES" />
<uses-permission android:name="android.permission.BROADCAST_STICKY" />
<uses-permission android:name="android.permission.KILL_BACKGROUND_PROCESSES" />
<uses-permission android:name="android.permission.GET_TASKS" />
<uses-permission android:name="android.permission.READ_LOGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.BATTERY_STATS" />
```

