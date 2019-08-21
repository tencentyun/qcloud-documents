

## 操作场景
Android SDK 是腾讯移动推送服务为客户端实现消息推送而提供给开发者的接口，本文将提供 AndroidStudio Gradle 自动集成和 Android Studio 手动集成两种方式。

## 操作步骤
### 集成方法
#### AndroidStudio Gradle 自动集成

>!在配置 SDK 前，确保已创建 Android 平台的应用。

1. 进入 [应用列表页面](https://console.cloud.tencent.com/tpns/applist)， 获取应用的包名、AccessID、AccessKey。
2. 在 app build.gradle 文件下，配置 以下内容：

```
android {
    ......
    defaultConfig {

        //控制台上注册的包名.注意application ID 和当前的应用包名以及控制台上注册应用的包名必须一致。
        applicationId "您的包名"
        ......

        ndk {
            //根据需要 自行选择添加的对应cpu类型的.so库。
            abiFilters 'armeabi', 'armeabi-v7a', 'arm64-v8a'
            // 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
        }

        manifestPlaceholders = [

            XG_ACCESS_ID:"注册应用的accessid",
            XG_ACCESS_KEY : "注册应用的accesskey",
        ]
        ......
    }
    ......
}

dependencies {
    ......
    //添加以下依赖
    implementation 'com.tencent.jg:jg:1.1'
    implementation 'com.tencent.tpns:tpns:1.1.0.0-release' //  TPNS 推送

}
```


>!
- 如在添加以上 abiFilter 配置后， Android Studio 出现以下提示：
NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin。  则在 Project 根目录的 gradle.properties 文件中添加  android.useDeprecatedNdk=true。
- 如需监听消息请参考 XGPushBaseReceiver 接口或是 demo 的 MessageReceiver 类。自行继承 XGPushBaseReceiver 并且在配置文件中配置如下内容：
    ```xml
    <receiver android:name="com.tencent.android.xg.cloud.demo.MessageReceiver">
            <intent-filter>
                <!-- 接收消息透传 -->
                <action android:name="com.tencent.android.xg.vip.action.PUSH_MESSAGE" />
                <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
                <action android:name="com.tencent.android.xg.vip.action.FEEDBACK" />
            </intent-filter>
        </receiver>
    ```




####  Android Studio 手动集成

**工程配置**
将 SDK 导入到工程的步骤为：

1. 创建或打开 Android 工程（关于如何创建 Android 工程，请参照开发环境的章节）。
2. 将腾讯移动推送 SDK 目录下的 libs 目录所有 .jar 文件拷贝到工程的 libs（或 lib）目录下。
3. .so 文件是腾讯移动推送必须的组件，支持armeabi、armeabi-v7a、arm64-v8a、mips、mips64、x86、x86_64平台，请根据自己当前 .so 支持的平台添加
4. 打开 Androidmanifest.xml，添加以下配置（建议参考下载包的 Demo 修改），其中 YOUR_ACCESS_ID和YOUR_ACCESS_KEY 替换为 App 对应的 AccessId 和 AccessKey，请确保按照要求配置，否则可能导致服务不能正常使用。

**权限配置**
腾讯移动推送 SDK 正常运行所需要的权限。示例代码如下：
```xml
    <!-- 【必须】 腾讯移动推送SDK VIP版本所需权限 -->
    <permission
        android:name="应用包名.permission.XGPUSH_RECEIVE"
        android:protectionLevel="signature" />
    <uses-permission android:name="应用包名.permission.XGPUSH_RECEIVE" />

    <!-- 【必须】 腾讯移动推送 SDK 所需权限 -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <!-- 【常用】 腾讯移动推送SDK所需权限 -->
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
```

#### 组件和应用信息配置

```xml
<application>
    <!-- 应用的其它配置 -->

    <!-- 【必须】 腾讯移动推送默认通知 -->
    <activity
        android:name="com.tencent.android.tpush.XGPushActivity">
        <intent-filter>
            <action android:name="android.intent.action" />
        </intent-filter>
    </activity>

    <!-- 【必须】 腾讯移动推送receiver广播接收 -->
    <receiver
        android:name="com.tencent.android.tpush.XGPushReceiver"
        android:process=":xg_vip_service">
        <intent-filter android:priority="0x7fffffff">
            <!-- 【必须】 腾讯移动推送SDK的内部广播 -->
            <action android:name="com.tencent.android.xg.vip.action.SDK" />
            <action android:name="com.tencent.android.xg.vip.action.INTERNAL_PUSH_MESSAGE" />

            <!-- 【可选】 系统广播：网络切换 -->
            <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
            <!-- 【可选】 系统广播：开屏 -->
            <action android:name="android.intent.action.USER_PRESENT" />
            <!-- 【可选】 一些常用的系统广播，增强腾讯移动推送service的复活机会，请根据需要选择。当然，您也可以添加App自定义的一些广播让启动service -->
            <action android:name="android.bluetooth.adapter.action.STATE_CHANGED" />
            <action android:name="android.intent.action.ACTION_POWER_CONNECTED" />
            <action android:name="android.intent.action.ACTION_POWER_DISCONNECTED" />
        </intent-filter>
    </receiver>

    <!-- 【必须】 腾讯移动推送service -->
    <service
        android:name="com.tencent.android.tpush.service.XGVipPushService"
        android:persistent="true"
        android:process=":xg_vip_service"></service>

    <!-- 云控相关 -->
    <receiver android:name="com.tencent.android.tpush.cloudctr.network.CloudControlDownloadReceiver">
        <intent-filter>
            <action android:name="com.tencent.android.xg.vip.action.cloudcontrol.action.DOWNLOAD_FILE_FINISH" />
        </intent-filter>
    </receiver>
    <service android:name="com.tencent.android.tpush.cloudctr.network.CloudControlDownloadService" />

    <!-- 【必须】 通知service，其中android:name部分要改为当前包名 -->
    <service android:name="com.tencent.android.tpush.rpc.XGRemoteService">
        <intent-filter>
            <!-- 【必须】 请修改为当前APP名包.XGVIP_PUSH_ACTION -->
            <action android:name="应用包名.XGVIP_PUSH_ACTION" />
        </intent-filter>
    </service>

    <!-- 【必须】 【注意】authorities修改为 包名.XGVIP_PUSH_AUTH -->
    <provider
        android:name="com.tencent.android.tpush.XGPushProvider"
        android:authorities="应用包名.XGVIP_PUSH_AUTH" />

    <!-- 【必须】 【注意】authorities修改为 包名.TPUSH_PROVIDER -->
    <provider
        android:name="com.tencent.android.tpush.SettingsContentProvider"
        android:authorities="应用包名.TPUSH_PROVIDER" />

    <!-- 【可选】用于增强保活能力 -->
    <provider
        android:name="com.tencent.android.tpush.XGVipPushKAProvider"
        android:authorities="应用包名.AUTH_XGPUSH_KEEPALIVE"
        android:exported="true" />

    <!-- 【可选】APP实现的Receiver，用于接收消息透传和操作结果的回调，请根据需要添加 -->
    <!-- YOUR_PACKAGE_PATH.CustomPushReceiver需要改为自己的Receiver： -->
    <receiver android:name="应用包名.MessageReceiver">
        <intent-filter>
            <!-- 接收消息透传 -->
            <action android:name="com.tencent.android.xg.vip.action.PUSH_MESSAGE" />
            <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
            <action android:name="com.tencent.android.xg.vip.action.FEEDBACK" />
        </intent-filter>
    </receiver>

    <!-- MQTT START-->
    <service android:exported="false"
             android:process=":xg_vip_service"
             android:name="com.tencent.bigdata.mqttchannel.services.MqttService" />

    <!--【注意】authorities修改为 包名.XG_SETTINGS_PROVIDER, 如demo的包名为：com.tencent.android.xg.cloud.demo -->
    <provider
        android:exported="false"
        android:name="com.tencent.bigdata.baseapi.base.SettingsContentProvider"
        android:authorities="应用包名.XG_SETTINGS_PROVIDER" />

    <!-- MQTT END-->

    <!-- 【必须】 请修改为APP的AccessId，“21”开头的10位数字，中间没空格 -->
    <meta-data
        android:name="XG_V2_ACCESS_ID"
        android:value="APP的AccessId" />
    <!-- 【必须】 请修改为APP的AccessKey，“A”开头的12位字符串，中间没空格 -->
    <meta-data
        android:name="XG_V2_ACCESS_KEY"
        android:value="APP的AccessKey" />

</application>

<!-- 【必须】 腾讯移动推送SDK5.0版本所需权限 -->
<permission
    android:name="应用包名.permission.XGPUSH_RECEIVE"
    android:protectionLevel="signature" />
<uses-permission android:name="应用包名.permission.XGPUSH_RECEIVE" />

<!-- 【必须】 腾讯移动推送SDK所需权限 -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />

<!-- 【常用】 腾讯移动推送SDK所需权限 -->
<uses-permission android:name="android.permission.VIBRATE" />
<uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
<hr>

### 调试及设备注册

**开启 Debug 日志数据**
>!上线时请设置为false

```java
XGPushConfig.enableDebug(this,true);
```


**Token 注册**

```java
XGPushManager.registerPush(this, new XGIOperateCallback() {
    @Override
    public void onSuccess(Object data, int flag) {
        //token在设备卸载重装的时候有可能会变
        Log.d("TPush", "注册成功，设备token为：" + data);
    }

    @Override
    public void onFail(Object data, int errCode, String msg) {
        Log.d("TPush", "注册失败，错误码：" + errCode + ",错误信息：" + msg);
    }
});
```
过滤 "TPush" 注册成功的日志如下：

```xml
XG register push success with token : 6ed8af8d7b18049d9fed116a9db9c71ab44d5565
```
<hr>

### 代码混淆

如果您的项目中使用 proguard 等工具，已做代码混淆，请保留以下选项，否则将导致腾讯移动推送服务不可用。

```xml
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver
-keep class com.tencent.android.tpush.** {*;}
-keep class com.tencent.bigdata.baseapi.** {*;}
-keep class com.tencent.bigdata.mqttchannel.** {*;}
-keep class com.tencent.tpns.dataacquisition.** {*;}

```

<hr>

### 接口变更
与4.x对比，部分 API 接口做了变更。

- 删除带账号注册的 API，设置账号只能通过 bindAccount 或 appendAccount 来设置。
	```java
	// 以下api被删除
	XGPushManager.registerPush(Context context, String account)
	XGPushManager.registerPush(Context context, String account, final XGIOperateCallback callback)
	XGPushManager.registerPush(Context context, String account,String url, String payload, String otherToken, final XGIOperateCallback callback)
	```

- registerPush 不再支持设置账号，需要注册账号的话，要单独调用 bindAccount 或 appendAccount，推荐在 registerPush 成功的回调里调用。
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


#### 获取 Token（非必选）
建议您完成 SDK 集成后，在 App 的【关于】、【意见反馈】等比较不常用的 UI 中，通过手势或者其他方式显示 Token，该操作便于我们后续进行问题排查。
示例代码如下：
```java
//获取 Token
XGPushConfig.getToken(getApplicationContext());
```
![](https://main.qcloudimg.com/raw/854020af14428df9972629e7dbbee55f.png)
