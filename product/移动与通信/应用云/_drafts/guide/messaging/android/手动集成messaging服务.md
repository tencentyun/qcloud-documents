如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：

### 1. 下载服务资源压缩包

1. 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-core-1.0.0.zip)，并解压。
2. 下载 [移动开发平台（MobileLine） Messaging 资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-messaging-1.0.0.zip)，并解压。

### 2. 集成 jar 包 和 so 包

* 将资源文件中的所有 jar 包拷贝到您工程的 `libs` 目录。
* 如果您是采用 Eclipse 开发，将资源文件中的 `jni` 目录下的内容 拷贝到您工程您工程的 `libs` 目录。
* 如果您是采用 Android Studio 开发，将资源文件中的 `jni` 目录下的内容 拷贝到 app 模块的 `main` 文件夹下的 `jniLibs` 目录下 。如果不存在该目录，请新建一个。

### 3. 修改您工程的 AndroidManifest.xml 文件

请按照下面的示例代码修改您工程下的 AndroidManifest.xml 文件：

```
<!-- Messaging 所需权限   -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.VIBRATE" />
<uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_SETTINGS" />

<application
  <!-- 消息receiver广播接收 -->
  <receiver android:name="com.tencent.android.tpush.XGPushReceiver"
   	android:process=":xg_service_v3" >
  	<intent-filter android:priority="0x7fffffff" >
  	
      	<action android:name="com.tencent.android.tpush.action.SDK" />
      	<action android:name="com.tencent.android.tpush.action.INTERNAL_PUSH_MESSAGE" />
      	
      	<action android:name="android.intent.action.USER_PRESENT" />
     	<action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
     	<action android:name="android.bluetooth.adapter.action.STATE_CHANGED" />
      	<action android:name="android.intent.action.ACTION_POWER_CONNECTED" />
      	<action android:name="android.intent.action.ACTION_POWER_DISCONNECTED" />
  	</intent-filter>
  </receiver>

  <!-- Messaging receiver，用于接收消息透传和操作结果的回调 -->
  <receiver android:name="com.tencent.tac.messaging.TACMessagingXGReceiver"
      android:exported="true" >
      <intent-filter>
          <!-- 接收消息透传 -->
          <action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
          <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
          <action android:name="com.tencent.android.tpush.action.FEEDBACK" />
      </intent-filter>
  </receiver>

   <!-- 接受通知的activity -->
   <activity
            android:name="com.tencent.android.tpush.XGPushActivity"
            android:exported="false"
            android:theme="@android:style/Theme.Translucent" >
            <intent-filter>	
                <action android:name="android.intent.action" />
            </intent-filter>
   </activity>

   <service
       android:name="com.tencent.android.tpush.service.XGPushServiceV3"
       android:exported="true"
       android:persistent="true"
       android:process=":xg_service_v3" />


  <service
      android:name="com.tencent.android.tpush.rpc.XGRemoteService"
      android:exported="true">
      <intent-filter>
          <action android:name="[您的应用包名].PUSH_ACTION" />
      </intent-filter>
   </service>


  <provider
       android:name="com.tencent.android.tpush.XGPushProvider"
       android:authorities="[您的应用包名].AUTH_XGPUSH"
       android:exported="true"/>

  <provider
       android:name="com.tencent.android.tpush.SettingsContentProvider"
       android:authorities="[您的应用包名].TPUSH_PROVIDER"
       android:exported="false" />

  <provider
       android:name="com.tencent.mid.api.MidProvider"
       android:authorities="[您的应用包名].TENCENT.MID.V3"
       android:exported="true" >
  </provider>
  
</application>
```
