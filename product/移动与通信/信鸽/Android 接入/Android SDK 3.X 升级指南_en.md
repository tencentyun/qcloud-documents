1.[Required] Extract the latest jar package in the SDK documentation to replace the current version of XGPush SDK.
2.[Required] Extract libtpnsSecurity.so and libxguardian.so to replace the old version depending on the required platform.
3.[Required] Set XGPushActivity. It is recommended to set the Android:exported of user-defined MessageReceiver to "false".
 
```
<activity android:name="com.tencent.android.tpush.XGPushActivity" android:exported="false" > </activity> 

<!-- This is the user-defined receiver. If it is configured already, set "exported" to "false", or ignore it --> 
<receiver android:name="User-defined MessageReceiver, which is inherited from XGPushBaseReceiver" android:exported="true"> 
      <intent-filter> 
            <!-- Receive transparently transfered messages --> 
            <action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" /> 
            <!-- Listen on the results of registration, unregistration, tag configuration/deletion, and clicks of notification --> 
            <action android:name="com.tencent.android.tpush.action.FEEDBACK" />
      </intent-filter> 
</receiver>
```
4.[Required] Check whether `com.tencent.android.tpush.service.XGPushServiceV3` and `com.tencent.android.tpush.rpc.XGRemoteService` have been configured. If not, the feature is unavailable.

```
<!-- [Required] XGPush service -->
       <service
           android:name="com.tencent.android.tpush.service.XGPushServiceV3"
           android:exported="true"
           android:persistent="true"
           android:process=":xg_service_v3" />

<!-- [Required] Notification service, which helps improve the arrival rate -->
       <service
           android:name="com.tencent.android.tpush.rpc.XGRemoteService"
           android:exported="true" >
           <intent-filter>
               <!-- [Required] Modify to the current App package name .PUSH_ACTION-->
               <action android:name="com.qq.xgdemo.PUSH_ACTION" />
           </intent-filter>
       </service>
```
5.[Required] Check whether ` com.tencent.android.tpush.XGPushProvider`, `com.tencent.android.tpush.SettingsContentProvider`, and `com.tencent.mid.api.MidProvider` have been configured. If not, the feature is unavailable.

```
<!-- [Required] [Note] Modify authorities to package name .AUTH_XGPUSH. For example, package name in demo is: com.qq.xgdemo-->
       <provider
           android:name="com.tencent.android.tpush.XGPushProvider"
           android:authorities="com.qq.xgdemo.AUTH_XGPUSH"
           android:exported="true"
           />       
<!-- [Required] [Note] Modify authorities to package name .TPUSH_PROVIDER. For example, package name in demo is: com.qq.xgdemo-->
       <provider
           android:name="com.tencent.android.tpush.SettingsContentProvider"
           android:authorities="com.qq.xgdemo.TPUSH_PROVIDER"
           android:exported="false" />
<!-- [Required] [Note] Modify authorities to package name .TENCENT.MID.V3. For example, package name in demo is: com.qq.xgdemo-->
       <provider
           android:name="com.tencent.mid.api.MidProvider"
           android:authorities="com.qq.xgdemo.TENCENT.MID.V3"
           android:exported="true" >
       </provider>
```
1.[Optional] Permission management
```
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

   <!-- [Optional] Permissions required for XGPush SDK -->
   <uses-permission android:name="android.permission.WRITE_SETTINGS" />
   <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
   <uses-permission android:name="android.permission.RESTART_PACKAGES" />
   <uses-permission android:name="android.permission.BROADCAST_STICKY" />
   <uses-permission android:name="android.permission.KILL_BACKGROUND_PROCESSES" />
   <uses-permission android:name="android.permission.GET_TASKS" />
   <uses-permission android:name="android.permission.READ_LOGS" />
   <uses-permission android:name="android.permission.BLUETOOTH" />
   <uses-permission android:name="android.permission.BATTERY_STATS" />
```
