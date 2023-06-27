## 常规升级步骤

### 通过 AndroidStudio 自动集成
若您的工程通过远程拉取依赖集成，如版本不涉及下方具体版本说明的，请直接更换工程中添加的移动推送SDK 相关依赖版本号为最新版本即可。最新版本号可前往 [Android SDK 发布动态](https://cloud.tencent.com/document/product/548/44520) 查看获取。

例如，当前使用的版本号为 1.3.3.3，最新版本号为 1.4.0.1，则将使用的推送 SDK 依赖版本号从 1.3.3.3 修改为 1.4.0.1：
```
dependencies {
    //移动推送主包
    implementation "com.tencent.tpns:tpns:1.4.0.1-release"

    // 小米推送依赖包
    implementation "com.tencent.tpns:xiaomi:1.4.0.1-release"

    // 魅族推送依赖包
    implementation "com.tencent.tpns:meizu:1.4.0.1-release"
    
    // 华为推送依赖包
    implementation "com.tencent.tpns:huawei:1.4.0.1-release"
    // 华为推送 HMS Core Push 模块依赖包
    implementation 'com.huawei.hms:push:6.7.0.300'       

    // OPPO 推送依赖包
    implementation "com.tencent.tpns:oppo:1.4.0.1-release"
    // 自 SDK 1.3.2.0 起，需一并加入以下依赖语句，否则可能导致 OPPO 推送注册失败
    implementation 'com.google.code.gson:gson:2.6.2'
    implementation 'commons-codec:commons-codec:1.15'

    // vivo 推送依赖包
    implementation "com.tencent.tpns:vivo:1.4.0.1-release"

    // 荣耀推送依赖包
    implementation "com.tencent.tpns:honor:1.4.0.1-release"
}
```


### 通过 Eclipse 集成
若您的工程通过手动引入 jar 文件集成，如版本不涉及下方具体版本说明的，请参考以下步骤进行变更：
1. 前往 [SDK 下载页](https://console.cloud.tencent.com/tpns/sdkdownload) 获取最新版本 SDK 压缩包。
2. 使用 SDK 压缩包目录 libs 下的各 `tpns-*.jar` 文件替换工程内原本的各 `tpns-*.jar` 文件。

>! 
>- 如您当前使用的版本和最新版本跨度较大，请务必参考下方涉及版本的变更内容进行配置修改。
>- 如无特殊情况，建议您对来自移动推送 SDK 的各厂商推送 SDK 依赖包也同步进行升级替换。


### 通过其他合集工具包集成
若您的工程通过其他三方合集工具包集成（例如 MSDK、GCloud 等），请优先参考合集工具包提供的升级指南。

## 移动推送 Android SDK 1.4.0.1
移动推送 1.4.0.1 升级了小米和魅族厂商推送依赖版本，目前使用的各厂商推送 SDK 原始版本如下：
- 华为：6.7.0.300
- 荣耀：7.0.41.301
- 小米：5.6.2
- 魅族：4.2.3
- OPPO：3.1.0
- vivo：3.0.0.4

## 移动推送 Android SDK 1.3.9.0
移动推送 1.3.9.0 升级了荣耀厂商推送依赖版本，目前使用的各厂商推送 SDK 原始版本如下：
- 华为：6.7.0.300
- 荣耀：7.0.41.301
- 小米：5.1.0
- 魅族：4.1.0
- OPPO：3.1.0
- vivo：3.0.0.4

厂商推送依赖的升级伴随部分配置改动，请参见以下内容进行变更。

### 通过 Eclipse 集成
如您的工程通过手动引入 jar 文件集成，请注意以下内容变更。

#### 荣耀推送
在 AndroidManifest.xml 文件移除以下节点：
```
    <permission
        android:name="${applicationId}.hihonor.permission.PROCESS_PUSH_MSG"
        android:protectionLevel="signatureOrSystem" />
		
		<queries>
        <intent>
            <action android:name="com.hihonor.push.action.BIND_PUSH_SERVICE" />
        </intent>
    </queries>
		
		<application>
        <receiver
            android:name="com.hihonor.push.sdk.PushReceiver"
            android:exported="true"
            android:permission="${applicationId}.hihonor.permission.PROCESS_PUSH_MSG">
            <intent-filter>
                <action android:name="com.hihonor.push.action.REGISTRATION" />
                <action android:name="com.hihonor.push.action.RECEIVE" />
            </intent-filter>
        </receiver>
				
				<provider
            android:name="com.hihonor.push.sdk.init.AutoInitProvider"
            android:authorities="${applicationId}.hihonor.autoinitprovider"
            android:exported="false"
            android:initOrder="500" />
    </application>
```
修改 meta-data 节点 com.hihonor.push.sdk_version 的值：
```
		<meta-data
				android:name="com.hihonor.push.sdk_version"
				android:value="7.0.41.301" />
```
修改后的配置如下：
```
    <uses-permission android:name="com.hihonor.push.permission.READ_PUSH_NOTIFICATION_INFO" />

    <application>

        <!-- 自定义荣耀推送回调 service -->
        <service
            android:name="com.tencent.android.tpush.honor.HonorMessageService"
            android:exported="false">
            <intent-filter>
                <action android:name="com.hihonor.push.action.MESSAGING_EVENT" />
            </intent-filter>
        </service>

        <meta-data
            android:name="com.hihonor.push.sdk_version"
            android:value="7.0.41.301" />

        <!-- 荣耀推送 appId -->
        <meta-data
            android:name="com.hihonor.push.app_id"
            android:value="${HONOR_APPID}" />
    </application>
```

## 移动推送 Android SDK 1.3.8.0
移动推送 1.3.8.0 版本，目前使用的各厂商推送 SDK 原始版本如下：
- 华为：6.7.0.300
- 荣耀：6.0.3.102
- 小米：5.1.0
- 魅族：4.1.0
- OPPO：3.1.0
- vivo：3.0.0.4

## 移动推送 Android SDK 1.3.7.2
移动推送 1.3.7.2 升级了华为、小米 厂商推送依赖版本，目前使用的各厂商推送 SDK 原始版本如下：
- 华为：6.7.0.300
- 小米：5.1.0
- 魅族：4.1.0
- OPPO：3.1.0
- vivo：3.0.0.4


## 移动推送 Android SDK 1.3.6.1
移动推送 1.3.6.1 升级了华为、小米、OPPO 厂商推送依赖版本，目前使用的各厂商推送 SDK 原始版本如下：
- 华为：6.5.0.300
- 小米：5.0.8
- 魅族：4.1.0
- OPPO：3.1.0
- vivo：3.0.0.4

## 移动推送 Android SDK 1.3.2.0
移动推送 1.3.2.0 升级了各厂商推送依赖版本，版本详情如下：
- 华为：6.3.0.302
- 小米：4.9.1
- 魅族：4.1.0
- OPPO：3.0.0
- vivo：3.0.0.4

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
		    // 资源文件 stat_sys_third_app_notify.png 请从移动推送 SDK 压缩包魅族厂商依赖目录的 flyme-notification-res 文件夹获取，并复制到应用自己的资源目录下
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
2. 请将移动推送 SDK 压缩包 OPPO 厂商依赖目录的 jar 文件 commons-codec-1.15.jar、gson-2.6.2-sources.jar 新增复制到工程 App 模块 libs 目录下并引入工程，否则可能导致 OPPO 推送注册失败：
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



## 移动推送 Android SDK 1.3.1.1
### 通过 Eclipse 集成
如您的工程通过手动引入 jar 文件集成，请注意以下内容变更。

1. 请在应用的 AndroidManifest 文件 application 标签内添加以下节点，否则可能引起应用在线时收到的推送无法响应通知点击事件。
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
2. 请在应用的 AndroidManifest 文件 application 标签内修改以下节点内容，否则可能存在自启动合规风险。
```xml
    <!-- 手动集成时该receiver的intent-filter只保留下面3个action -->
    <receiver
         android:name="com.tencent.android.tpush.XGPushReceiver"
         android:exported="false"
         android:process=":xg_vip_service" >
         <intent-filter android:priority="0x7fffffff" tools:node="replace" >
            <!-- 【必须】 信鸽SDK的内部广播 -->
            <action android:name="com.tencent.android.xg.vip.action.SDK" />
            <action android:name="com.tencent.android.xg.vip.action.INTERNAL_PUSH_MESSAGE" />
            <action android:name="com.tencent.android.xg.vip.action.ACTION_SDK_KEEPALIVE" />
         </intent-filter>
    </receiver>
    
    <!-- 如果您有集成小米通道,手动集成小米通道时，将该receiver对应的intent-filter删除 -->
    <receiver
       android:name="com.xiaomi.push.service.receivers.NetworkStatusReceiver"
       android:exported="true" >
       <intent-filter tools:node="remove">
           <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
           <category android:name="android.intent.category.DEFAULT" />
       </intent-filter>
    </receiver>
```

## 移动推送 Android SDK 1.2.7.0

###  新增应用内消息补推能力
新增是否允许应用内消息展示接口，请注意高版本 Android 使用 WebView 的兼容性详见 [Android 接口文档](https://cloud.tencent.com/document/product/548/36659#.E5.BA.94.E7.94.A8.E5.86.85.E6.B6.88.E6.81.AF.E5.B1.95.E7.A4.BA)。

## 移动推送 Android SDK 1.2.5.0

###  配置工程依赖环境（可选）

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

### 新增配置（必需）
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


## 移动推送 Android SDK 1.2.1.3
### 华为推送 SDK 接入变更
此版本起正式支持华为推送 V5 版本 SDK，请参见 [华为通道 V5 接入](https://cloud.tencent.com/document/product/548/45909) 更新华为推送集成配置。

## 移动推送Android SDK 1.2.0.2
### 通过 Eclipse 集成
如您的工程通过手动引入 jar 文件集成，请注意以下内容变更。

#### 移动推送主包
1. 替换 SDK 压缩包目录 libs 下的各 tpns-.jar 文件。
2. 替换 SDK 压缩包目录 Other-Platform-SO 下的各平台 so 文件。
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
2. 请在 AndroidManifest 文件 application 标签内移除以下节点：
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
3. 在 proguard 混淆配置添加如下内容：
```
-keep public class * extends android.app.Service
-keep class com.heytap.mcssdk.** {*;}
-keep class com.heytap.msp.push.** { *;}
```
