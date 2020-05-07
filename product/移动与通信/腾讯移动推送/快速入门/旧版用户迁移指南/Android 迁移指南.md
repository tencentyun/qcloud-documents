为保障迁移后的正常使用，请您升级至 Android V1.1.5.5 及以上版本，以下是针对从信鸽平台 4.x 版本迁移到腾讯移动推送平台 Android V1.1.5.5 及以上版本的变更说明。

## 注销信鸽平台推送服务
如果 App 的推送服务是从信鸽平台（https://xg.qq.com）迁移到腾讯移动推送平台，TPNS 版本需要增加以下配置：
- 在 AndroidManifest 上添加的 application 节点内添加以下配置，填写信鸽平台的 ACCESS ID
```xml
<meta-data
    android:name="XG_OLD_ACCESS_ID"
    android:value="信鸽平台应用的ACCESS ID" />
```
>! 如果未做以上配置，则在信鸽和腾讯移动推送两个平台上同时推送时，可能会出现重复消息。

- 在应用首次覆盖安装时，如您在logcat中看到如下日志打印，即说明 SDK 已成功获取信鸽版本的推送信息，将在推送注册时一并向服务器上报：
```
D/TPush: [PushServiceNetworkHandler] FreeVersionInfo ->  AccessId:2100168750, token:0e3baa5e895d47f94e21840a231a0e6b651b7f47, channel:huawei
```


## 自动集成方式
#### 依赖变更
在【app build.gradle】>【dependencies】下，请将以下信鸽 4.x 版本依赖做相应变更。

变更前：
```
implementation 'com.tencent.xinge:xinge:4.3.5-release'
implementation 'com.tencent.wup:wup:1.0.0.E-Release'
implementation 'com.tencent.mid:mid:4.0.7-Release'
```
变更后：
```
// TPNS 推送 [VERSION] 为当前SDK版本号，版本号可在SDK下载页查看
implementation 'com.tencent.tpns:tpns:[VERSION]-release'    
```
#### 组件变更
若监听消息自行继承过 XGBaseReceiver 接口类，请在 AndroidManifest 文件下，将该自定义组件注册内容做相应变更。

变更前：
```
<receiver android:name="完整包名.MessageReceiver"
    android:exported="true" >
    <intent-filter>
        <!-- 接收消息透传 -->
        <action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
        <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
        <action android:name="com.tencent.android.tpush.action.FEEDBACK" />
    </intent-filter>
</receiver>
```
变更后：
```
<receiver android:name="完整包名.MessageReceiver">
  <intent-filter>
      <!-- 接收消息透传 -->
      <action android:name="com.tencent.android.xg.vip.action.PUSH_MESSAGE" />
      <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
      <action android:name="com.tencent.android.xg.vip.action.FEEDBACK" />
  </intent-filter>
</receiver>
```

>?因 XGBaseReceiver 接口类中有方法名变更和接口新增，请注意修改、新增实现对应接口。详情请参见 [接口变更说明](#jkbg)。

## 手动集成方式
####  依赖包变更
请前往 [腾讯移动推送控制台](https://console.cloud.tencent.com/tpns/sdkdownload)，下载 Android SDK 压缩包、解压并按照以下步骤替换依赖包文件：
- 删除信鸽 4.x 版本所使用的全部 .jar 文件，使用 libs 目录下的所有 .jar 文件替换。
- 删除信鸽 4.x 版本所使用的全部 .so 文件，在 Other-Platform-SO 目录下，按照当前 .so 支持的平台添加 .so 文件。

#### AndroidManifest 文件变更
1. 在 Android 配置文件 AndroidManifest.xml 中，删除所有信鸽 4.x 版本使用组件和权限，删除内容具体如下：
```
<application>
    <!-- 【必须】 信鸽receiver广播接收 -->
    <receiver android:name="com.tencent.android.tpush.XGPushReceiver"
        android:process=":xg_service_v4" >
        <intent-filter android:priority="0x7fffffff" >
            <!-- 【必须】 信鸽SDK的内部广播 -->
            <action android:name="com.tencent.android.tpush.action.SDK" />
            <action android:name="com.tencent.android.tpush.action.INTERNAL_PUSH_MESSAGE" />
            <!-- 【必须】 系统广播：开屏和网络切换 -->
            <action android:name="android.intent.action.USER_PRESENT" />
            <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
            <!-- 【可选】 一些常用的系统广播，增强信鸽service的复活机会，请根据需要选择。当然，您也可以添加APP自定义的一些广播让启动service -->
            <action android:name="android.bluetooth.adapter.action.STATE_CHANGED" />
            <action android:name="android.intent.action.ACTION_POWER_CONNECTED" />
            <action android:name="android.intent.action.ACTION_POWER_DISCONNECTED" />
        </intent-filter>
    </receiver>
    <!-- 【可选】APP实现的Receiver，用于接收消息透传和操作结果的回调，请根据需要添加 -->
    <!-- YOUR_PACKAGE_PATH.CustomPushReceiver需要改为自己的Receiver： -->
    <receiver android:name="com.qq.xgdemo.receiver.MessageReceiver"
        android:exported="true" >
        <intent-filter>
            <!-- 接收消息透传 -->
            <action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
            <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
            <action android:name="com.tencent.android.tpush.action.FEEDBACK" />
        </intent-filter>
    </receiver>
    <!-- 【注意】 如果被打开的activity是启动模式为SingleTop，SingleTask或SingleInstance，请根据通知的异常自查列表第8点处理-->
    <activity
        android:name="com.tencent.android.tpush.XGPushActivity"
        android:exported="false" >
            <intent-filter>
            <!-- 若使用AndroidStudio，请设置android:name="android.intent.action"-->
            <action android:name="" />
            </intent-filter>
    </activity>

    <!-- 【必须】 信鸽service -->
    <service
        android:name="com.tencent.android.tpush.service.XGPushServiceV4"
        android:exported="true"
        android:persistent="true"
        android:process=":xg_service_v4" />
    <!-- 云控相关 -->
    <receiver android:name="com.tencent.android.tpush.cloudctr.network.CloudControlDownloadReceiver">
        <intent-filter>
        <action android:name="com.tencent.android.xg.vip.action.cloudcontrol.action.DOWNLOAD_FILE_FINISH" />
        </intent-filter>
        </receiver>
    <service android:name="com.tencent.android.tpush.cloudctr.network.CloudControlDownloadService" />
    <!-- 【必须】 提高service的存活率 -->
    <service
        android:name="com.tencent.android.tpush.rpc.XGRemoteService"
        android:exported="true">
            <intent-filter>
            <!-- 【必须】 请修改为当前APP包名 .PUSH_ACTION, 如demo的包名为：com.qq.xgdemo -->
            <action android:name="当前应用的包名.PUSH_ACTION" />
        </intent-filter>
    </service>

    <!-- 【必须】 【注意】authorities修改为 包名.AUTH_XGPUSH, 如demo的包名为：com.qq.xgdemo-->
    <provider
        android:name="com.tencent.android.tpush.XGPushProvider"
        android:authorities="当前应用的包名.AUTH_XGPUSH"
        android:exported="true"/>
    <!-- 【必须】 【注意】authorities修改为 包名.TPUSH_PROVIDER, 如demo的包名为：com.qq.xgdemo-->
    <provider
        android:name="com.tencent.android.tpush.SettingsContentProvider"
        android:authorities="当前应用的包名.TPUSH_PROVIDER"
        android:exported="false" />
    <!-- 【必须】 【注意】authorities修改为 包名.TENCENT.MID.V4, 如demo的包名为：com.qq.xgdemo-->
    <provider
        android:name="com.tencent.mid.api.MidProvider"
        android:authorities="当前应用的包名.TENCENT.MID.V4"
        android:exported="true" >
    </provider>
    <!-- 【必须】 请将YOUR_ACCESS_ID修改为APP的AccessId，“21”开头的10位数字，中间没空格 -->
    <meta-data
        android:name="XG_V2_ACCESS_ID"
        android:value="YOUR_ACCESS_ID" />
    <!-- 【必须】 请将YOUR_ACCESS_KEY修改为APP的AccessKey，“A”开头的12位字符串，中间没空格 -->
    <meta-data
        android:name="XG_V2_ACCESS_KEY"
        android:value="YOUR_ACCESS_KEY" />
</application>
<!-- 【必须】 信鸽SDK所需权限 -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.VIBRATE" />
<!-- 【常用】 信鸽SDK所需权限 -->
<uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_SETTINGS" />
<!-- 【可选】 信鸽SDK所需权限 -->
<uses-permission android:name="android.permission.RESTART_PACKAGES" />
<uses-permission android:name="android.permission.BROADCAST_STICKY" />
<uses-permission android:name="android.permission.KILL_BACKGROUND_PROCESSES" />
<uses-permission android:name="android.permission.GET_TASKS" />
<uses-permission android:name="android.permission.READ_LOGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.BATTERY_STATS" />
```
2. 请参见新版本 [SDK 集成](https://cloud.tencent.com/document/product/548/36652) 重新添加组件和权限。

<span id="jkbg"></span>
## 接口变更
与 4.x 对比，部分 API 接口做了以下变更。

- 删除带账号注册的 API，设置账号只能通过 bindAccount 或 appendAccount 来设置。
	```java
	// 删除以下API
	XGPushManager.registerPush(Context context, String account)
	XGPushManager.registerPush(Context context, String account, final XGIOperateCallback callback)
	XGPushManager.registerPush(Context context, String account,String url, String payload, String otherToken, final XGIOperateCallback callback)
	```
- 账号绑定和注册推送功能分开，bindAccount 和 appendAccount 不再带有注册功能，推荐在 registerPush 成功的回调里，调用 bindAccount 或 appendAccount。
- 继承 XGPushBaseReceiver 时需要多实现以下两个函数。
	```java
	/**
	 * 设置帐号结果处理函数
	 */
	public abstract void onSetAccountResult(Context context, int errorCode,
					String operateName);
	/**
	 * 删除帐号结果处理函数
	 */
	public abstract void onDeleteAccountResult(Context context, int errorCode,
					String operateName);
	```
- 继承 XGPushBaseReceiver 的实现类，在 AndroidManifest 文件配置时，前缀命名规则为 com.tencent.android.xg.vip.action.，区别于 4.x 版本的 com.tencent.android.tpush.action.。
TPNS 版本正确配置：
```
<receiver android:name="com.tencent.android.xg.cloud.demo.MessageReceiver">
          <intent-filter>
              <!-- 接收消息透传 -->
              <action android:name="com.tencent.android.xg.vip.action.PUSH_MESSAGE" />
              <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
              <action android:name="com.tencent.android.xg.vip.action.FEEDBACK" />
          </intent-filter>
      </receiver>
```

## 厂商通道集成变更
厂商通道变更只需做以下变更：
- 删除 gradle 依赖（自动集成）
```
// 删除以下对应的厂商依赖
implementation 'com.tencent.xinge:mipush:4.3.2-xiaomi-release'
implementation 'com.tencent.xinge:xgmz:4.3.2-meizu-release'
implementation 'com.tencent.xinge:xghw:4.3.2-huawei-release'
// fcm
implementation 'com.tencent.xinge:fcm:4.3.2-release'
implementation 'com.google.firebase:firebase-messaging:17.3.1'
```
替换为以下对应的厂商依赖，[VERSION] 为当前 SDK 版本号，版本号可在 SDK 下载页查看。
```
implementation 'com.tencent.tpns:xiaomi:[VERSION]-release'
implementation 'com.tencent.tpns:meizu:[VERSION]-release'
implementation 'com.tencent.tpns:huawei:[VERSION]-release'
//fcm
implementation 'com.tencent.tpns:fcm:[VERSION]-release'
implementation  'com.google.firebase:firebase-messaging:17.6.0'
```
- 手动集成的方式需要替换 .jar 文件
前往 [腾讯移动推送控制台](https://console.cloud.tencent.com/tpns/sdkdownload)，下载 Android SDK 压缩包、并解压目录 Other-Push-jar 下，找到对应厂商通道所需 .jar 文件，替换信鸽 4.x 版本使用的厂商通道 .jar 文件。


## 代码混淆保留变更
如果您的项目中使用 proguard 等工具做了代码混淆，请将以下混淆保留选项：

变更前：
```
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver
-keep class com.tencent.android.tpush.** {*;}
-keep class com.tencent.mid.** {*;}
-keep class com.qq.taf.jce.** {*;}
-keep class com.tencent.bigdata.** {*;}
```
变更后：
```
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver
-keep class com.tencent.android.tpush.** {*;}
-keep class com.tencent.bigdata.baseapi.** {*;}
-keep class com.tencent.bigdata.mqttchannel.** {*;}
-keep class com.tencent.tpns.dataacquisition.** {*;}
```
