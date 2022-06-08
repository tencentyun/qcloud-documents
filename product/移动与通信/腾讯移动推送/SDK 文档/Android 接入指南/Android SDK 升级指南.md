## TPNS Android SDK 1.3.2.0
TPNS 1.3.2.0 升级了各厂商推送依赖版本，版本详情如下：
- 华为 : 6.3.0.302
- 小米 : 4.9.1
- 魅族 : 4.1.0
- OPPO : 3.0.0
- vivo :  3.0.0.4

厂商推送依赖的升级伴随部分配置改动，请参见以下内容进行变更。

### 通过 AndroidStudio 自动集成
如您的工程通过远程拉取依赖集成，请注意以下内容变更。
#### OPPO 推送
请注意新增以下依赖语句，否则可能导致 OPPO 推送注册失败：
```groovy
implementation 'com.google.code.gson:gson:2.6.2'
implementation 'commons-codec:commons-codec:1.15'
```

### 通过 Eclipse 集成
如您的工程通过手动引入 jar 文件集成，请注意以下内容变更。
#### 小米推送
请在 AndroidManifest 文件 application 标签下新增以下节点，否则可能导致在 Android 12 起的小米设备上通知点击失效：
```xml
<activity
    android:name="com.xiaomi.mipush.sdk.NotificationClickedActivity"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
    android:launchMode="singleInstance"
    android:exported="true"
    android:enabled="true">
</activity>
```

####  魅族推送
1. 请在主工程添加以下类资源文件，否则可能导致在 Android 6.0 及以下的魅族设备上接收通知失效。代码如下：
```java
package com.meizu.cloud.pushinternal;
public class R {
    public static final class drawable {
		    // 资源文件 stat_sys_third_app_notify.png 请从 TPNS SDK 压缩包魅族厂商依赖目录的 flyme-notification-res 文件夹获取，并复制到应用自己的资源目录下
        public static final int stat_sys_third_app_notify = com.tencent.android.tpns.demo.R.drawable.stat_sys_third_app_notify;
    }
}
```

2. 请在 AndroidManifest 文件新增以下权限：
```xml
<uses-permission android:name="com.meizu.flyme.permission.PUSH" />
```
并在 application 标签内移除 receiver 节点 `com.meizu.cloud.pushsdk.SystemReceiver`，新增以下 receiver 节点：
```xml
<receiver
    android:name="com.meizu.cloud.pushsdk.MzPushSystemReceiver"
    android:exported="false"
    android:permission="com.meizu.flyme.permission.PUSH">
    <intent-filter>
        <action android:name="com.meizu.flyme.push.intent.PUSH_SYSTEM" />
    </intent-filter>
</receiver>
```

####  OPPO 推送
1. 请在主工程将之前为 OPPO 推送添加的类资源文件 `com.heytap.mcssdk.R` 变更包名为 `com.pushsdk.R`（如未添加过则直接新增），否则可能导致 OPPO 推送注册失败，示例如下：
```java
package com.pushsdk;
class R {
    public static final class string {
        public final static int system_default_channel = com.tencent.android.tpns.demo.R.string.app_name; // 可更改为自定义字符串资源ID
    }
}
```

2. 请将 TPNS SDK 压缩包 OPPO 厂商依赖目录的 jar 文件 commons-codec-1.15.jar、gson-2.6.2-sources.jar 新增复制到工程 app 模块 libs 目录下并引入工程，否则可能导致 OPPO 推送注册失败：
```groovy
implementation files('libs/gson-2.6.2-sources.jar')
implementation files('libs/commons-codec-1.15.jar')
```

####  vivo 推送
1. 请在 AndroidManifest 文件 application 标签内修改 service 节点 `com.vivo.push.sdk.service.CommandClientService` 为如下内容：
```xml
<service
    android:name="com.vivo.push.sdk.service.CommandClientService"
    android:permission="com.push.permission.UPSTAGESERVICE"
    android:exported="true" />
```
2. 并添加以下节点：
```xml
<meta-data
    android:name="sdk_version_vivo"
    android:value="483" />

<meta-data
    android:name="local_iv"
    android:value="MzMsMzQsMzUsMzYsMzcsMzgsMzksNDAsNDEsMzIsMzgsMzcsMzYsMzUsMzQsMzMsI0AzNCwzMiwzMywzNywzMywzNCwzMiwzMywzMywzMywzNCw0MSwzNSwzNSwzMiwzMiwjQDMzLDM0LDM1LDM2LDM3LDM4LDM5LDQwLDQxLDMyLDM4LDM3LDMzLDM1LDM0LDMzLCNAMzQsMzIsMzMsMzcsMzMsMzQsMzIsMzMsMzMsMzMsMzQsNDEsMzUsMzIsMzIsMzI" />
```



## TPNS Android SDK 1.3.1.1
###  AndroidManifest 新增节点
如您通过手动引入 jar 文件，即参考 SDK 集成文档 [Android Studio 手动集成](https://cloud.tencent.com/document/product/548/36652#android-studio-.E6.89.8B.E5.8A.A8.E9.9B.86.E6.88.90) 部分接入 TPNS SDK 的，请注意在应用的 AndroidManifest 文件 application 标签内添加以下节点，或直接参考上述链接重新引入 AndroidManifest 配置。否则可能引起应用在线时收到的推送无法响应通知点击事件。

>! 此项变更仅需要通过手动引入 jar 文件的应用开发者注意。如您通过拉取远程依赖接入 TPNS SDK，可忽略此项配置。

```xml
    <activity
        android:name="com.tencent.android.tpush.InnerTpnsActivity"
        android:exported="false"
        android:launchMode="singleInstance"
        android:theme="@android:style/Theme.Translucent.NoTitleBar">
        <intent-filter>
            <action android:name="${applicationId}.OPEN_TPNS_ACTIVITY_V2" />

            <category android:name="android.intent.category.DEFAULT" />
        </intent-filter>
        <intent-filter>
            <data
                android:host="${applicationId}"
                android:scheme="stpns" />

            <action android:name="android.intent.action.VIEW" />

            <category android:name="android.intent.category.BROWSABLE" />
            <category android:name="android.intent.category.DEFAULT" />
        </intent-filter>
        <intent-filter>
            <action android:name="android.intent.action" />
        </intent-filter>
    </activity>
```

## TPNS Android SDK 1.2.7.0

###  新增应用内消息补推能力
新增是否允许应用内消息展示接口，请注意高版本 Android 使用 WebView 的兼容性详见 [Android 接口文档](https://cloud.tencent.com/document/product/548/36659#.E5.BA.94.E7.94.A8.E5.86.85.E6.B6.88.E6.81.AF.E5.B1.95.E7.A4.BA)。

## TPNS Android SDK 1.2.5.0

###  1. 配置工程依赖环境（可选）

如果您在使用 SDK 依赖时遇到依赖拉取不到的情况，可以考虑在项目工程根目录 build.gradle 文件 allprojects.repositories 位置添加谷歌官方推荐镜像源 MavenCentral 和腾讯云镜像源。代码示例如下：
```
allprojects {
    repositories {
        google()
        // 谷歌推荐 MavenCentral 镜像源
        mavenCentral()
        jcenter()
        // 腾讯云镜像源
        maven { url 'https://mirrors.tencent.com/nexus/repository/maven-public/' }
    }
}
```

### 2. 新增配置（必需）
新增的标签查询接口，需要注意在继承 `XGPushBaseReceiver` 的实现类中增加实现方法 `onQueryTagsResult`。代码示例如下：
``` 
public class MessageReceiver extends XGPushBaseReceiver {

    // 其他回调接口
		// ...
		// 标签查询回调接口
    public void onQueryTagsResult(Context context, int errorCode, String data, String operateName) {
        Log.i(LogTag, "action - onQueryTagsResult, errorCode:" + errorCode + ", operateName:" + operateName + ", data: " + data);
    }
}
```


## TPNS Android SDK 1.2.1.3
### 华为推送 SDK 接入变更
此版本起正式支持华为推送 V5 版本 SDK，请参见 [华为通道 V5 接入](https://cloud.tencent.com/document/product/548/45909) 更新华为推送集成配置。

## TPNS Android SDK 1.2.0.2
### 通过 Eclipse 集成
如您的工程通过手动引入 jar 文件集成，请注意以下内容变更。
#### TPNS 主包
1. 替换 SDK 压缩包目录 libs 下的各 tpns-.jar 文件；
2. 替换 SDK 压缩包目录 Other-Platform-SO 下的各平台 so 文件；
3. 请在 AndroidManifest 文件 application 标签内移除以下节点：
```xml
    <activity
        android:name="com.tencent.android.tpush.XGPushActivity">
        <intent-filter>
            <action android:name="android.intent.action" />
        </intent-filter>
    </activity>

    <service android:exported="false"
            android:process=":xg_vip_service"
            android:name="com.tencent.bigdata.mqttchannel.services.MqttService" />

    <provider
            android:exported="false"
            android:name="com.tencent.bigdata.baseapi.base.SettingsContentProvider"
            android:authorities="应用包名.XG_SETTINGS_PROVIDER" />
```
并新增以下节点：
```xml
    <activity android:name="com.tencent.android.tpush.TpnsActivity"
        android:theme="@android:style/Theme.Translucent.NoTitleBar">
        <intent-filter>
            <action android:name="${applicationId}.OPEN_TPNS_ACTIVITY" />
            <category android:name="android.intent.category.DEFAULT" />
        </intent-filter>
        <intent-filter>
            <data
                android:scheme="tpns"
                android:host="应用包名"/>
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.BROWSABLE" />
            <category android:name="android.intent.category.DEFAULT" />
        </intent-filter>
    </activity>

    <service android:exported="false"
            android:process=":xg_vip_service"
            android:name="com.tencent.tpns.mqttchannel.services.MqttService" />

    <provider
            android:exported="false"
            android:name="com.tencent.tpns.baseapi.base.SettingsContentProvider"
            android:authorities="应用包名.XG_SETTINGS_PROVIDER" />
```
4. 在 proguard 混淆配置添加如下内容：
```
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver
-keep class com.tencent.android.tpush.** {*;}
-keep class com.tencent.tpns.baseapi.** {*;} 
-keep class com.tencent.tpns.mqttchannel.** {*;}
-keep class com.tencent.tpns.dataacquisition.** {*;}
```

#### OPPO 推送
1. 在主工程添加类资源文件 `com.heytap.mcssdk.R`，代码如下：
```java
package com.heytap.mcssdk;
class R {
    public static final class string {
        public static final int system_default_channel = 
    com.tencent.android.tpns.demo.R.string.oppo_system_default_channel;//可更改为自定义字符串资源ID
    }
}
```
2.  请在 AndroidManifest 文件 application 标签内移除以下节点：
```xml
<service
   android:name="com.heytap.mcssdk.PushService"
   android:permission="com.coloros.mcs.permission.SEND_MCS_MESSAGE">
   <intent-filter>
       <action android:name="com.coloros.mcs.action.RECEIVE_MCS_MESSAGE"/>
   </intent-filter>
</service>
<service
   android:name="com.heytap.mcssdk.AppPushService"
   android:permission="com.heytap.mcs.permission.SEND_MCS_MESSAGE">
   <intent-filter>
       <action android:name="com.heytap.mcs.action.RECEIVE_MCS_MESSAGE"/>
   </intent-filter>
</service>
```
并新增以下节点：
```xml
<service
   android:name="com.heytap.msp.push.service.CompatibleDataMessageCallbackService"
   android:permission="com.coloros.mcs.permission.SEND_MCS_MESSAGE">
   <intent-filter>
       <action android:name="com.coloros.mcs.action.RECEIVE_MCS_MESSAGE"/>
   </intent-filter>
</service>
<service
   android:name="com.heytap.msp.push.service.DataMessageCallbackService"
   android:permission="com.heytap.mcs.permission.SEND_PUSH_MESSAGE">
   <intent-filter>
       <action android:name="com.heytap.mcs.action.RECEIVE_MCS_MESSAGE"/>
       <action android:name="com.heytap.msp.push.RECEIVE_MCS_MESSAGE"/>
   </intent-filter>
</service>
```
4. 在 proguard 混淆配置添加如下内容：
```
-keep public class * extends android.app.Service
-keep class com.heytap.mcssdk.** {*;}
-keep class com.heytap.msp.push.** { *;}
```
