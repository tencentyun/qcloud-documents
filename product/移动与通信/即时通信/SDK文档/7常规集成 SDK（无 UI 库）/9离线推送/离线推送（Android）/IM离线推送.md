## 概述

即时通信 IM 的终端用户需要随时都能够得知最新的消息，而由于移动端设备的性能与电量有限，当 App 处于后台时，为了避免维持长连接而导致的过多资源消耗，即时通信 IM 推荐您使用各厂商提供的系统级推送通道来进行消息通知，系统级的推送通道相比第三方推送拥有更稳定的系统级长连接，可以做到随时接受推送消息，且资源消耗大幅降低。

>!
>- 在没有主动退出登录的情况下，应用退后台、手机锁屏、或者应用进程被用户主动杀掉三种场景下，如果想继续接收到 IM 消息提醒，可以接入即时通信 IM 离线推送。
>- 如果应用主动调用  logout 退出登录，或者多端登录被踢下线，即使接入了 IM 离线推送，也收不到离线推送消息。

## 跑通离线推送功能

TUIKitDemo 已经按照如下步骤接入了离线推送功能，文档中已有源码指引链接可供参考。

### 步骤1：注册应用到厂商推送平台

离线推送功能依赖厂商原始通道，您需要将自己的应用注册到各个厂商的推送平台，得到 AppID 和 AppKey 等参数。目前国内支持的手机厂商有：[小米]( https://dev.mi.com/console/doc/detail?pId=68)、[华为](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/service-introduction-0000001050040060)、[OPPO](https://open.oppomobile.com/wiki/doc#id=10195)、[VIVO](https://dev.vivo.com.cn/documentCenter/doc/281)、[魅族](http://open-wiki.flyme.cn/doc-wiki/index#id?129)，海外支持 [Google FCM](https://console.firebase.google.com/u/0/?hl=zh-cn)。

### 步骤2：IM 控制台配置

登录腾讯云 [即时通信 IM 控制台](https://console.qcloud.com/avc) ，添加各个厂商推送证书，并将您在步骤一中获取的各厂商的 AppId、AppKey、AppSecret 等参数配置给 IM 控制台的推送证书，其中 “单击后续动作” 参见步骤3。

<dx-tabs>
::: 小米
<table> 
   <tr> 
     <th nowrap="nowrap">厂商推送平台</th> 
     <th>IM 控制台配置</th> 
   </tr> 
   <tr> 
     <td><img src="https://qcloudimg.tencent-cloud.cn/raw/fbfcba10c2de51e24ff7391c15a5abcd.png" style="zoom:100%;" /></td> 
     <td><img src="https://qcloudimg.tencent-cloud.cn/raw/09d87e9cca3c98433fbd0ee08a5b413e.png" style="zoom:300%;" /> 
</td> 
   </tr> 
</table>
:::
::: 华为
<table> 
   <tr> 
     <th nowrap="nowrap">厂商推送平台</th> 
     <th>IM 控制台配置</th> 
   </tr> 
   <tr> 
     <td><img src="https://qcloudimg.tencent-cloud.cn/raw/f8c7c0c9c259919c1f93e79707ddde1d.png" style="zoom:100%;" /></td> 
     <td>注：Client ID 对应 AppID，Client Secret 对应 AppSecret <img src="https://qcloudimg.tencent-cloud.cn/raw/4a79b2f269d0c0b521fddf80d88aca71.png" style="zoom:300%;" />
</td> 
   </tr> 
</table>
:::
::: OPPO
<table> 
   <tr> 
     <th nowrap="nowrap">厂商推送平台</th> 
     <th>IM 控制台配置</th> 
   </tr> 
   <tr> 
     <td><img src="https://qcloudimg.tencent-cloud.cn/raw/051de434b51f77711e5a6aa7682abb72.png" style="zoom:100%;" /> </td> 
     <td> <img src="https://qcloudimg.tencent-cloud.cn/raw/1194d8b2fce31937c463f6b5430554e9.png" style="zoom:300%;" />
</td> 
   </tr> 
</table>
:::
::: vivo
<table> 
   <tr> 
     <th nowrap="nowrap">厂商推送平台</th> 
     <th>IM 控制台配置</th> 
   </tr> 
   <tr> 
     <td><img src="https://qcloudimg.tencent-cloud.cn/raw/a764b271e3ac1de64b3c9342fa9e96b1.png" style="zoom:100%;" /></td> 
     <td><img src="https://qcloudimg.tencent-cloud.cn/raw/5bfc5e6f5b3361323be326ca35962f7b.png" style="zoom:300%;" />
</td> 
   </tr> 
</table>
:::
::: 魅族
<table> 
   <tr> 
     <th nowrap="nowrap">厂商推送平台</th> 
     <th>IM 控制台配置</th> 
   </tr> 
   <tr> 
     <td><img src="https://qcloudimg.tencent-cloud.cn/raw/70ad94d8e843f92247c67a3ae4004c15.png" style="zoom:100%;" /></td> 
     <td><img src="https://qcloudimg.tencent-cloud.cn/raw/c4ded9269e0ac59ff58214be1bea89d6.png" style="zoom:300%;" /> 
</td> 
   </tr> 
</table>
:::
::: Google FCM
<table> 
   <tr> 
     <th nowrap="nowrap">厂商推送平台</th> 
     <th>IM 控制台配置</th> 
   </tr> 
   <tr> 
     <td><img src="https://qcloudimg.tencent-cloud.cn/raw/b344dee87f9d946e21480cd57556730d.png" style="zoom:100%;" /></td> 
     <td><img src="https://qcloudimg.tencent-cloud.cn/raw/2fb172afb1993af17c4021a31f256ce9.png" style="zoom:300%;" />
</td> 
   </tr> 
</table>
:::
</dx-tabs>

>!
>- 对于小米厂商，如果在厂商开发者官网配置了 ChannelID，需要在 [即时通信 IM 控制台](https://console.qcloud.com/avc) 配置同样的 ChannelID,否则可能推送不成功。

### 步骤3：配置离线推送跳转界面

收到离线推送后，通知栏会显示推送信息如图所示，单击通知栏会打开应用并进入配置的跳转界面。请您参见下面的步骤，配置单击通知消息后跳转的 Activity。

<img src="https://qcloudimg.tencent-cloud.cn/raw/7e6b56b3bb60bc9ccf7d5d0179eb51ea.png" style="zoom:40%;" />

- **控制台配置**
各个厂商的跳转界面配置方式有所不同，具体如下：
<table> 
   <tr> 
     <th nowrap="nowrap">厂商</th> 
     <th nowrap="nowrap">单击后后续动作</th> 
     <th>应用内指定界面</th> 
   </tr> 
   <tr> 
     <td>小米</td> 
     <td>打开应用内指定页面</td> 
     <td>intent://`您配置的 hostname`/`您配置的 path`#Intent;scheme=`您配置的协议，也就是你定义的 scheme`;launchFlags=0x4000000;component=`您应用跳转界面的完整类名`;end<br>(TUIKitDemo 配置的是：intent://com.tencent.qcloud/detail#Intent;scheme=pushscheme;launchFlags=0x4000000;component=com.tencent.qcloud.tim.tuikit/com.tencent.qcloud.tim.demo.main.MainActivity;end)
</td> 
   </tr> 
   <tr> 
     <td>华为</td> 
     <td>打开应用内指定页面</td>  <td>intent://`您配置的 hostname`/`您配置的 path`#Intent;scheme=`您配置的协议，也就是你定义的 scheme`;launchFlags=0x4000000;component=`您应用跳转界面的完整类名`;end<br>(TUIKitDemo 配置的是：intent://com.tencent.qcloud/detail#Intent;scheme=pushscheme;launchFlags=0x4000000;component=com.tencent.qcloud.tim.tuikit/com.tencent.qcloud.tim.demo.main.MainActivity;end)
</td> 
   </tr> 
   <tr> 
     <td>魅族</td> 
     <td>打开应用内指定页面</td> 
     <td>您应用跳转界面的完整类名<br>(TUIKitDemo 配置的是：com.tencent.qcloud.tim.demo.main.MainActivity)
</td> 
   </tr> 
   <tr> 
     <td nowrap="nowrap">OPPO</td> 
     <td>打开应用内指定页面</td> 
     <td>您应用跳转界面的完整类名<br>(TUIKitDemo 配置的是：activity：com.tencent.qcloud.tim.demo.main.MainActivity)
</td> 
   </tr>  
   <tr> 
     <td nowrap="nowrap">vivo</td> 
     <td nowrap="nowrap">打开应用内指定页面</td>   <td>intent://`您配置的 hostname`/`您配置的 path`#Intent;scheme=`您配置的协议，也就是你定义的 scheme`;launchFlags=0x4000000;component=`您应用跳转界面的完整类名`;end<br>(TUIKitDemo 配置的是：intent://com.tencent.qcloud/detail#Intent;scheme=pushscheme;launchFlags=0x4000000;component=com.tencent.qcloud.tim.tuikit/com.tencent.qcloud.tim.demo.main.MainActivity;end)
</td> 
   </tr>
	 </tr>  
   <tr> 
     <td nowrap="nowrap">Google FCM</td> 
     <td nowrap="nowrap">不需要配置</td>   <td> 默认会跳转至应用的 Launcher 界面
</td> 
   </tr>
</table>

-  **清单文件配置**
在 [清单文件 AndroidManifest.xml](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/AndroidManifest.xml) 中完成跳转界面的相关配置，需要注意的是，该配置必须与您在 IM 控制台推送证书的单击后续动作配置保持一致。
```
<!-- TUIKitDemo 配置的跳转界面是 MainActivity，所以这里填 com.tencent.qcloud.tim.demo.main.MainActivity。集成到您的应用后，需要替换您的应用界面完整类名 -->
    <activity
        android:name="您应用跳转界面的完整类名"
        android:launchMode="singleTask"
        android:screenOrientation="portrait"
        android:windowSoftInputMode="adjustResize|stateHidden">

        <!-- 离线推送打开应用内页面 -->
        <intent-filter>
            <action android:name="android.intent.a和Google FCmo配置的是：pushscheme://com.tencent.qcloud/detail -->
                <data
                    android:host="您配置的 hostname"
                    android:path="您配置的 path"
                    android:scheme="您配置的协议，也就是你定义的 scheme" />
        </intent-filter>

    </activity>
```

### 步骤4：配置厂商推送规则
-  **应用离线参数配置**
步骤二推送证书添加成功之后，IM 控制台会为您分配一个证书 ID，请您填充到  [PrivateConstants](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/utils/PrivateConstants.java)  的配置参数里，该证书配置给 IM 控制台的 ID 会在注册推送服务和上报 token 时使用, 以小米为例：
**推送证书 ID 如下：**
![](https://qcloudimg.tencent-cloud.cn/raw/772536e8a3f474572f5b85bfb2597fe1.png)
**填充的参数如下：**
```
   public class PrivateConstants {
   /****** 小米离线推送参数start ******/
   // 在腾讯云控制台上传第三方推送证书后分配的证书 ID
   public static final long XM_PUSH_BUZID = 您应用分配的证书 ID;
   // 小米开放平台分配的应用APPID及APPKEY
   public static final String XM_PUSH_APPID = "您应用分配的 APPID";
   public static final String XM_PUSH_APPKEY = "您应用分配的 APPKEY";
   /****** 小米离线推送参数end ******/
   }
```

-  **清单文件配置厂商推送权限相关**
清单文件中需要添加各个厂商的推送规则，可以参见 TUIKitDemo [清单文件](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/AndroidManifest.xml)相关配置，具体如下：
<dx-tabs>
::: 小米
<table> 
   <tr> 
```
<!-- 注意：TUIKitDemo 的 applicationId 是 com.tencent.qcloud.tim.tuikit，这里的 “xxxx” 需要替换您的应用的 applicationId。 -->

<!-- ********小米推送权限设置******** -->
<permission
    android:name="xxxx.permission.MIPUSH_RECEIVE"
    android:protectionLevel="signature" />
uses-permission android:name="xxxx.permission.MIPUSH_RECEIVE" />

<!-- ********小米推送service和receiver设置start******** -->
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
<!-- 注：此service必须在3.0.1版本以后（包括3.0.1版本）加入 -->
<service
    android:name="com.xiaomi.mipush.sdk.PushMessageHandler"
    android:enabled="true"
    android:exported="true" />
<service
    android:name="com.xiaomi.mipush.sdk.MessageHandleService"
    android:enabled="true" />
<!-- 注：此service必须在2.2.5版本以后（包括2.2.5版本）加入 -->
<receiver
    android:name="com.xiaomi.push.service.receivers.NetworkStatusReceiver"
    android:exported="true">
    <intent-filter>
        <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</receiver>
<receiver
    android:name="com.xiaomi.push.service.receivers.PingReceiver"
    android:exported="false"
    android:process=":pushservice">
    <intent-filter>
        <action android:name="com.xiaomi.push.PING_TIMER" />
    </intent-filter>
</receiver>
<!-- 自实现小米推送的接收广播 -->
<receiver
    android:name="xxxx.XiaomiMsgReceiver"
    android:exported="true">
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
<!-- ********小米推送service和receiver设置end******** -->
```
   </tr> 
</table>
:::
::: 华为
<table> 
   <tr> 
```
<!-- 注意：TUIKitDemo 的 applicationId 是 com.tencent.qcloud.tim.tuikit，这里的 “xxxx” 需要替换您的应用的 applicationId。 -->

<!-- ********华为推送权限设置******** -->
<permission
    android:name="xxxx.permission.PROCESS_PUSH_MSG"
    android:protectionLevel="signatureOrSystem" />
<uses-permission android:name="com.huawei.android.launcher.permission.CHANGE_BADGE" />
<uses-permission android:name="xxxx.permission.PROCESS_PUSH_MSG" />
	
<!-- ********华为推送设置start******** -->
<service
    android:name="xxxx.HUAWEIHmsMessageService"
    android:exported="false">
    <intent-filter>
         <action android:name="com.huawei.push.action.MESSAGING_EVENT"/>
    </intent-filter>
</service>
<!-- ********华为推送设置end******** -->	
```
</tr> 
</table>
:::
::: OPPO
<table> 
   <tr> 
```
<!-- ********OPPO 推送权限设置******** -->
<uses-permission android:name="com.coloros.mcs.permission.RECIEVE_MCS_MESSAGE" />
<uses-permission android:name="com.heytap.mcs.permission.RECIEVE_MCS_MESSAGE" />

<!-- ********OPPO 推送 start******** -->
<service
    android:name="com.heytap.msp.push.service.CompatibleDataMessageCallbackService"
    android:permission="com.coloros.mcs.permission.SEND_MCS_MESSAGE">
    <intent-filter>
        <action android:name="com.coloros.mcs.action.RECEIVE_MCS_MESSAGE" />
    </intent-filter>
</service>
<!-- 兼容Q以下版本 -->
<service
    android:name="com.heytap.msp.push.service.DataMessageCallbackService"
    android:permission="com.heytap.mcs.permission.SEND_PUSH_MESSAGE">
    <intent-filter>
        <action android:name="com.heytap.mcs.action.RECEIVE_MCS_MESSAGE" />
        <action android:name="com.heytap.msp.push.RECEIVE_MCS_MESSAGE" />
    </intent-filter>
</service>
<!-- 兼容Q版本 -->
<!-- ********OPPO 推送 end******** -->
```
   </tr> 
</table>
:::
::: vivo
<table> 
   <tr> 
```
<!-- ********vivo推送设置start******** -->
<service
    android:name="com.vivo.push.sdk.service.CommandClientService"
    android:exported="true" />
<activity
    android:name="com.vivo.push.sdk.LinkProxyClientActivity"
    android:exported="false"
    android:screenOrientation="portrait"
    android:theme="@android:style/Theme.Translucent.NoTitleBar" />
<!-- push应用定义消息receiver声明 -->
<receiver android:name="xxxx.VIVOPushMessageReceiverImpl">
    <intent-filter>
        <!-- 接收push消息 -->
        <action android:name="com.vivo.pushclient.action.RECEIVE" />
    </intent-filter>
</receiver>
<!-- ********vivo推送设置end******** -->
```
   </tr> 
</table>
:::
::: 魅族
<table> 
   <tr> 
```
<!-- 注意：TUIKitDemo 的 applicationId 是 com.tencent.qcloud.tim.tuikit，这里的 “xxxx” 需要替换您的应用的 applicationId。 -->

 <!-- 兼容flyme3.0配置权限 -->
 <permission
     android:name="xxxx.permission.C2D_MESSAGE"
     android:protectionLevel="signature" />

 <uses-permission android:name="com.meizu.c2dm.permission.RECEIVE" />
 <uses-permission android:name="xxxx.permission.C2D_MESSAGE" />
	
<!-- ********魅族推送设置start******** -->
<receiver android:name="xxxx.MEIZUPushReceiver">
     <intent-filter>
         <!-- 接收push消息 -->
         <action android:name="com.meizu.flyme.push.intent.MESSAGE" />
         <!-- 接收register消息 -->
         <action android:name="com.meizu.flyme.push.intent.REGISTER.FEEDBACK" />
         <!-- 接收unregister消息 -->
         <action android:name="com.meizu.flyme.push.intent.UNREGISTER.FEEDBACK" />
         <!-- 兼容低版本Flyme3推送服务配置 -->
         <action android:name="com.meizu.c2dm.intent.REGISTRATION" />
         <action android:name="com.meizu.c2dm.intent.RECEIVE" />

         <category android:name="com.tencent.qcloud.tim.demo.thirdpush" />
     </intent-filter>
 </receiver>
 <!-- ********魅族推送设置end******** -->
```
   </tr> 
</table>
:::
::: Google FCM
<table> 
   <tr> 
```
<!-- 注意：TUIKitDemo 的 applicationId 是 com.tencent.qcloud.tim.tuikit，这里的 “xxxx” 需要替换您的应用的 applicationId。 -->

<!-- ********海外google云消息传递start******** -->
<service
    android:name="xxxx.GoogleFCMMsgService"
    android:exported="false">
    <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
    </intent-filter>
</service>
<!-- ********海外google云消息传递end******** -->
```
   </tr> 
</table>
:::
</dx-tabs>

-  **vivo 适配**
根据 vivo 厂商接入指引，需要将 APPID 和 APPKEY 添加到清单文件中，否则会出现编译问题：
<dx-tabs>
::: 方法1
<table> 
<tr> 
```
android {
    ...
    defaultConfig {
		    ...
        manifestPlaceholders = [
                "VIVO_APPKEY" : "您应用分配的证书 APPKEY",
                "VIVO_APPID" : "您应用分配的证书 APPID"
        ]
    }
}
```
</tr> 
</table>
:::
::: 方法2
<table> 
<tr> 
```
<receiver android:name="com.tencent.qcloud.tim.demo.thirdpush.VIVOPushMessageReceiverImpl">
        <intent-filter>
            <!-- 接收push消息 -->
            <action android:name="com.vivo.pushclient.action.RECEIVE" />
        </intent-filter>
</receiver>

<meta-data tools:replace="android:value"
    android:name="com.vivo.push.api_key"
    android:value="您应用分配的证书 APPKEY" />
<meta-data tools:replace="android:value"
    android:name="com.vivo.push.app_id"
    android:value="您应用分配的证书 APPID" />
```
</tr> 
</table>
:::
</dx-tabs>

-  **华为和 Google FCM 适配**
华为和 Google FCM 需要按照厂商方法，集成对应的 plugin 和 json 配置文件。
 1. 在项目级 build.gradle 文件中 buildscript -> dependencies 下添加以下配置：
```
classpath 'com.google.gms:google-services:4.2.0'
classpath 'com.huawei.agconnect:agcp:1.4.1.300'
```
在项目级 build.gradle 文件中 allprojects -> repositories 下添加以下配置：
```
mavenCentral()
// 配置HMS Core SDK的Maven仓地址。
maven {url 'https://developer.huawei.com/repo/'}
```
添加后效果如下：
```
repositories {
    ...
     // 配置HMS Core SDK的Maven仓地址。
     maven {url 'https://developer.huawei.com/repo/'}
}
    
dependencies {
    ...
    classpath 'com.google.gms:google-services:4.2.0'
    classpath 'com.huawei.agconnect:agcp:1.4.1.300'
}
```

 2. 在应用级 build.gradle 文件中添加下方配置。
```
apply plugin: 'com.google.gms.google-services'
apply plugin: 'com.huawei.agconnect'
```
 3. 单击项目右上角 **Sync Now** 同步项目。

### 步骤5：集成厂商推送 SDK

- **集成 SDK**
在 [gradle](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/build.gradle) 文件中添加厂商推送 SDK。
 ```
 dependencies {
    ......
    // 主包
    implementation 'com.tencent.tpns:tpns:1.3.1.1-release'
    // Google FCM
    implementation "com.tencent.tpns:fcm:1.3.1.1-release"
    // google 云消息传递
    implementation ('com.google.firebase:firebase-messaging:19.0.1')
    // 小米
    implementation "com.tencent.tpns:xiaomi:1.3.1.1-release"
    // 魅族
    implementation "com.tencent.tpns:meizu:1.3.1.1-release"
    // OPPO
    implementation "com.tencent.tpns:oppo:1.3.1.1-release"
    // vivo
    implementation "com.tencent.tpns:vivo:1.3.1.1-release"
    // 华为
    implementation 'com.tencent.tpns:huawei:1.3.1.1-release'
    implementation 'com.huawei.hms:push:5.0.2.300'
}
```

-  **添加推送类**
引入厂商推送类，各个厂商推送方式有区别，可以参见拷贝 [TUIKitDemo 代码路径](https://github.com/tencentyun/TIMSDK/tree/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/thirdpush) 下如下文件：
![](https://main.qcloudimg.com/raw/e786a5bf942694baba680c92704ad7d3.png)

-  **推送服务注册**
应合规要求，在用户同意隐私协议登录成功后，分别初始化注册各个厂商推送服务，并在注册结果回调处保存注册成功后的 token，并调用 [setOfflinePushConfig](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) 接口上报推送 token 至后台。部分厂商在注册后，调用一些接口也会返回 token，可以再次同步更新下，具体参见以下代码。
```
public void init() {
    ...
        
    if (BrandUtil.isBrandXiaoMi()) {
        // 小米离线推送
        MiPushClient.registerPush(this, PrivateConstants.XM_PUSH_APPID, PrivateConstants.XM_PUSH_APPKEY);
    } else if (BrandUtil.isBrandHuawei()) {
        // 华为离线推送，设置是否接收Push通知栏消息调用示例
        HmsMessaging.getInstance(this).turnOnPush().addOnCompleteListener(new com.huawei.hmf.tasks.OnCompleteListener<Void>() {
            @Override
            public void onComplete(com.huawei.hmf.tasks.Task<Void> task) {
                if (task.isSuccessful()) {
                    DemoLog.i(TAG, "huawei turnOnPush Complete");
                } else {
                    DemoLog.e(TAG, "huawei turnOnPush failed: ret=" + task.getException().getMessage());
                }
            }
        });
						
        new Thread() {
            @Override
            public void run() {
                try {
                    // read from agconnect-services.json
                    String appId = AGConnectServicesConfig.fromContext(MainActivity.this).getString("client/app_id");
                    String token = HmsInstanceId.getInstance(MainActivity.this).getToken(appId, "HCM");
                    DemoLog.i(TAG, "huawei get token:" + token);
                    if(!TextUtils.isEmpty(token)) {
                        // 该 token 需要保存并调用 setOfflinePushConfig 接口上报 IMSDK
                        String token = (String) o;
                    }
                } catch (ApiException e) {
                    DemoLog.e(TAG, "huawei get token failed, " + e);
                }
            }
        }.start();
    } else if (MzSystemUtils.isBrandMeizu(this)) {
        // 魅族离线推送
        PushManager.register(this, PrivateConstants.MZ_PUSH_APPID, PrivateConstants.MZ_PUSH_APPKEY);
    } else if (BrandUtil.isBrandVivo()) {
        // vivo离线推送
        PushClient.getInstance(getApplicationContext()).initialize();
						
        DemoLog.i(TAG, "vivo support push: " + PushClient.getInstance(getApplicationContext()).isSupport());
        PushClient.getInstance(getApplicationContext()).turnOnPush(new IPushActionListener() {
            @Override
            public void onStateChanged(int state) {
                if (state == 0) {
                    String regId = PushClient.getInstance(getApplicationContext()).getRegId();
                    DemoLog.i(TAG, "vivopush open vivo push success regId = " + regId);
                       
					// // 该 token 需要保存并调用 setOfflinePushConfig 接口上报 IMSDK
					String token = (String) o;
                } else {
                    // 根据vivo推送文档说明，state = 101 表示该vivo机型或者版本不支持vivo推送，链接：https://dev.vivo.com.cn/documentCenter/doc/156
                    DemoLog.i(TAG, "vivopush open vivo push fail state = " + state);
                }
            }
        });
    } else if (HeytapPushManager.isSupportPush()) {
        // oppo离线推送
        OPPOPushImpl oppo = new OPPOPushImpl();
        oppo.createNotificationChannel(this);
        // oppo接入文档要求，应用必须要调用init(...)接口，才能执行后续操作。
        HeytapPushManager.init(this, false);
        HeytapPushManager.register(this, PrivateConstants.OPPO_PUSH_APPKEY, PrivateConstants.OPPO_PUSH_APPSECRET, oppo);
    } else if (BrandUtil.isGoogleServiceSupport()) {
        FirebaseInstanceId.getInstance().getInstanceId()
                .addOnCompleteListener(new com.google.android.gms.tasks.OnCompleteListener<InstanceIdResult>() {
                    @Override
                    public void onComplete(Task<InstanceIdResult> task) {
                        if (!task.isSuccessful()) {
                            DemoLog.w(TAG, "getInstanceId failed exception = " + task.getException());
                            return;
                        }

                        // Get new Instance ID token
                        String token = task.getResult().getToken();
                        DemoLog.i(TAG, "google fcm getToken = " + token);
                        
                        // 该 token 需要保存并调用 setOfflinePushConfig 接口上报 IMSDK
                        String token = (String) o;
                    }
                });
    }
}
```
以华为为例，在注册结果回调处保存注册成功后的 token，并调用 [setOfflinePushConfig](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) 接口上报给后台。
```
public class HUAWEIHmsMessageService extends HmsMessageService {

    ...

    @Override
    public void onNewToken(String token) {
        DemoLog.i(TAG, "onNewToken token=" + token);
        
        // 该 token 需要保存并调用 setOfflinePushConfig 接口上报 IMSDK
        String pushToken = token;
    }

    ...
}
```

- **推送证书和 token 上报后台**
调用 [setOfflinePushConfig](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a494d6cafe50ba25503979a4e0f14c28e) 接口上报推送 token。构造 V2TIMOfflinePushConfig 类，需设置 businessID 为对应厂商的证书 ID，isTPNSToken 为 false，上报注册厂商推送服务获取的 token。注意：如果使用 [TPNS](https://cloud.tencent.com/document/product/548/36645) 接入离线推送，请设置 isTPNSToken 为 true，上报注册 TPNS 推送服务获取的 token，推送会由 TPNS 提供服务。
```
V2TIMOfflinePushConfig v2TIMOfflinePushConfig = null;
// 需要设置 businessID 为对应厂商的证书 ID，isTPNSToken 为 false，上报注册厂商推送服务获取的 token。  
v2TIMOfflinePushConfig = new V2TIMOfflinePushConfig(0, token, true);
V2TIMManager.getOfflinePushManager().setOfflinePushConfig(v2TIMOfflinePushConfig, new V2TIMCallback() {
        @Override
        public void onError(int code, String desc) {
            DemoLog.d(TAG, "setOfflinePushToken err code = " + code);
        }

        @Override
        public void onSuccess() {
            DemoLog.d(TAG, "setOfflinePushToken success");
        }
});
```

### 步骤6：前后台状态同步 [](id:step6)

 如果您的应用退到后台，收到新消息时需要在手机通知栏进行展示，请您调用 IMSDK 的 [doBackground()](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a2b191294ac4d68a2d69e482eae1b638f) 接口，将应用的状态同步给 IM 后台；当应用回到前台时，请您调用 IMSDK 的 [doForeground()](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushManager.html#a4c2ff4eea609da1d0950648905fbf6aa) 接口，将应用的状态同步给 IM 后台。监听 App 前后台切换的方案推荐您参见 [DemoApplication](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/DemoApplication.java) 的 StatisticActivityLifecycleCallback 类相关逻辑。

```
// 应用切到后台时
V2TIMManager.getOfflinePushManager().doBackground(totalCount, new V2TIMCallback() {
    @Override
    public void onError(int code, String desc) {
        DemoLog.e(TAG, "doBackground err = " + code + ", desc = " + desc);
    }

    @Override
    public void onSuccess() {
        DemoLog.i(TAG, "doBackground success");
    }
});
// 应用切回前台时
V2TIMManager.getOfflinePushManager().doForeground(new V2TIMCallback() {
    @Override
    public void onError(int code, String desc) {
        DemoLog.e(TAG, "doForeground err = " + code + ", desc = " + desc);
    }

    @Override
    public void onSuccess() {
        DemoLog.i(TAG, "doForeground success");
    }
});
```


### 步骤7：发消息时设置离线推送参数

调用 [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) 发送消息时，您可以通过 V2TIMOfflinePushInfo 设置离线推送参数，可以参见 [ChatProvider](https://github.com/tencentyun/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/model/ChatProvider.java) 的 sendMessage() 方法：

```
OfflineMessageContainerBean containerBean = new OfflineMessageContainerBean();
OfflineMessageBean entity = new OfflineMessageBean();
entity.content = message.getExtra().toString();
entity.sender = message.getFromUser();
entity.nickname = chatInfo.getChatName();
entity.faceUrl = TUIChatConfigs.getConfigs().getGeneralConfig().getUserFaceUrl();
containerBean.entity = entity;
				
V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();
v2TIMOfflinePushInfo.setExt(new Gson().toJson(containerBean).getBytes());
// OPPO必须设置ChannelID才可以收到推送消息，这个channelID需要和控制台一致
v2TIMOfflinePushInfo.setAndroidOPPOChannelID("tuikit");

final V2TIMMessage v2TIMMessage = message.getTimMessage();
String msgID = V2TIMManager.getMessageManager().sendMessage(v2TIMMessage, isGroup ? null : userID, isGroup ? groupID : null,
    V2TIMMessage.V2TIM_PRIORITY_DEFAULT, false, v2TIMOfflinePushInfo, new V2TIMSendCallback<V2TIMMessage>() {
        @Override
        public void onProgress(int progress) {

        }

        @Override
        public void onError(int code, String desc) {
            TUIChatUtils.callbackOnError(callBack, TAG, code, desc);
        }

        @Override
        public void onSuccess(V2TIMMessage v2TIMMessage) {
            TUIChatLog.v(TAG, "sendMessage onSuccess:" + v2TIMMessage.getMsgID());
            message.setMsgTime(v2TIMMessage.getTimestamp());
            TUIChatUtils.callbackOnSuccess(callBack, message);
        }
    });
```

### 步骤8：解析离线推送消息

当手机收到离线推送消息时，会在系统通知栏里展示收到的推送消息。单击通知栏的消息时，会自动跳转到您在步骤四配置的界面，您可以在该界面通过调用 getIntent().getExtras() 获取您在 [步骤6](#step6) 中配置的离线推送参数。示例代码可以参见 TUIKitDemo 的 [handleOfflinePush()](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/main/MainActivity.java) 方法。

```
private void handleOfflinePush() {
    // 根据登录状态，判断是否需要重新登录 IM
    // 1. 如果登录状态为 V2TIMManager.V2TIM_STATUS_LOGOUT，跳转到登录界面，重新登录 IM
    if (V2TIMManager.getInstance().getLoginStatus() == V2TIMManager.V2TIM_STATUS_LOGOUT) {
        Intent intent = new Intent(MainActivity.this, SplashActivity.class);
        if (getIntent() != null) {
            intent.putExtras(getIntent());
        }
        startActivity(intent);
        finish();
        return;
    }
 
    // 2. 否则，说明 App 只是处于退后台的状态，直接解析离线推送参数
    final OfflineMessageBean bean = OfflineMessageDispatcher.parseOfflineMessage(getIntent());
        if (bean != null) {
            setIntent(null);
            NotificationManager manager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
            if (manager != null) {
                manager.cancelAll();
            }

            if (bean.action == OfflineMessageBean.REDIRECT_ACTION_CHAT) {
                if (TextUtils.isEmpty(bean.sender)) {
                    return;
                }
                TUIUtils.startChat(bean.sender, bean.nickname, bean.chatType);
            }
        }
}
		
```

>!
>- FCM 单击通知栏的消息会默认跳转至应用的默认 Launcher 界面，该界面可以通过调用 getIntent().getExtras() 获取您在 [步骤6](#step6) 中配置的离线推送参数，此处进行解析和自定义跳转。
 
以上完成后，当您的应用退到后台或者进程被杀掉时，消息会进行离线推送通知栏展示，可单击通知栏跳转到设定的应用界面，完成实现离线推送功能。



## 常见问题

### 离线推送怎么自定义推送的声音？

从 SDK 6.1.2155 版本开始，支持设置自定义铃音，支持机型有华为、小米、FCM 和 APNS。方法参见：V2TIMOfflinePushInfo 接口 [setAndroidSound()](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a3ff923225d5a79802a02c47a07e07fc5) 和 [setIOSSound()](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#acffd09150398b06c3d7eb42baee5aee1)。

### 收不到离线推送怎么排查？
#### 1、OPPO 手机
OPPO 手机收不到推送一般有以下几种情况：
- 按照 OPPO 推送官网要求，在 Android 8.0 及以上系统版本的 OPPO 手机上必须配置 ChannelID，否则推送消息无法展示。配置方法可以参见 [OPPO 推送配置](https://cloud.tencent.com/document/product/269/44516#oppo-.E6.8E.A8.E9.80.81)。
- 在消息中 [透传的离线推送的自定义内容](https://cloud.tencent.com/document/product/269/44516#.E9.80.8F.E4.BC.A0.E8.87.AA.E5.AE.9A.E4.B9.89.E5.86.85.E5.AE.B93) 不是 JSON 格式，会导致 OPPO 手机收不到推送。
- OPPO 安装应用通知栏显示默认关闭，需要确认下开关状态。

#### 2、发送消息为自定义消息
自定义消息的离线推送和普通消息不太一样，自定义消息的内容我们无法解析，不能确定推送的内容，所以默认不推送，如果您有推送需求，需要您在 [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a318c40c8547cb9e8a0de7b0e871fdbfe) 的时候设置 [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html) 的 [desc](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a78c8e202aa4e0859468ce40bde6fd602) 字段，推送的时候会默认展示 desc 信息。

#### 3、设备通知栏设置影响
离线推送的直观表现就是通知栏提示，所以同其他通知一样受设备通知相关设置的影响，以华为为例：

- “手机设置-通知-锁屏通知-隐藏或者不显示通知”，会影响锁屏状态下离线推送通知显示。
- “手机设置-通知-更多通知设置-状态栏显示通知图标”，会影响状态栏下离线推送通知的图标显示。
- “手机设置-通知-应用的通知管理-允许通知”，打开关闭会直接影响离线推送通知显示。
- “手机设置-通知-应用的通知管理-通知铃声” 和 “手机设置-通知-应用的通知管理-静默通知”，会影响离线推送通知铃音的效果。

#### 4、按照流程接入完成，还是收不到离线推送
- 首先在 IM 控制台通过 [离线测试工具](https://console.cloud.tencent.com/im-detail/tool-push-check) 自测下是否可以正常推送。
推送异常情况，设备状态异常，需要检查下 IM 控制台配置各项参数是否正确，再者需要检查下代码初始化注册逻辑，包括厂商推送服务注册和 IM 设置离线推送配置相关逻辑是否正确设置。
推送异常情况，设备状态正常，需要看下是否需要正确填写 channel ID 或者后台服务是否正常。
- 离线推送依赖厂商能力，一些简单的字符可能会被厂商过滤不能透传推送。
- 如果离线推送消息出现推送不及时或者偶尔收不到情况，需要看下厂商的推送限制。

### 跳转界面不成功怎么排查？

单击离线推送消息的通知栏，跳转到指定界面，原理是后台根据您在控制台配置的各个厂商的跳转方式和界面参数，根据厂商接口规则，传递给厂商服务器，单击时候进行对应界面启动跳转。对应界面启动还依赖清单文件的配置，必须和控制台配置的相对应，才能正确启动和跳转。

1、首先需要重点排查下控制台和清单文件相关配置是否对应且正确，可参见 TUIKitDemo 的配置，注意部分厂商提供接口方式存在差异。
2、如果跳转到了配置的界面，需要再看下配置界面内离线消息的解析和界面重定向是否正常。


### 厂商推送限制

1、国内厂商都有消息分类机制，不同类型也会有不同的推送策略。如果想要推送及时可靠，需要按照厂商规则设置自己应用的推送类型为高优先级的系统消息类型或者重要消息类型。反之，离线推送消息会受厂商推送消息分类影响，与预期会有差异。
2、另外，一些厂商对于应用每天的推送数量也是有限制的，可以在厂商控制台查看应用每日限制的推送数量。
如果离线推送消息出现推送不及时或者偶尔收不到情况，需要考虑下这里：
- 华为：将推送消息分为服务与通讯类和资讯营销类，推送效果和策略不同。另外，消息分类还和自分类权益有关：
  - 无自分类权益，推送消息厂商还会进行二次智能分类 。
  - 有申请自分类权益，消息分类会按照自定义的分类进行推送。
具体请参见 [厂商描述](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835)。
- vivo：将推送消息分为系统消息类和运营消息类，推送效果和策略不同。系统消息类型还会进行厂商的智能分类二次修正，若智能分类识别出不是系统消息，会自动修正为运营消息，如果误判可邮件申请反馈。另外，消息推送也受日推总数量限制，日推送量由应用在厂商订阅数统计决定。
具体请参见 [厂商描述1](https://dev.vivo.com.cn/documentCenter/doc/359) 或 [厂商描述2](https://dev.vivo.com.cn/documentCenter/doc/156)。
- OPPO：将推送消息分为私信消息类和公信消息类，推送效果和策略不同。其中私信消息是针对用户有一定关注度，且希望能及时接收的信息，私信通道权益需要邮件申请。公信通道推送数量有限制。
具体请参见 [厂商描述1](https://open.oppomobile.com/wiki/doc#id=11227) 或 [厂商描述2](https://open.oppomobile.com/wiki/doc#id=11210)。
- 小米：将推送消息分为重要消息类和普通消息类，推送效果和策略不同。其中重要消息类型仅允许即时通讯消息、个人关注动态提醒、个人事项提醒、个人订单状态变化、个人财务提醒、个人状态变化、个人资源变化、个人设备提醒这8类消息推送，可以在厂商控制台申请开通。普通消息类型推送数量有限制。
具体请参见 [厂商描述1](https://dev.mi.com/console/doc/detail?pId=2422) 或 [厂商描述2](https://dev.mi.com/console/doc/detail?pId=2086)。
- 魅族：推送消息数量有限制。
具体请参见 [厂商描述](http://open.res.flyme.cn/fileserver/upload/file/202201/85079f02ac0841da859c1da0ef351970.pdf)。
- FCM：推送上行消息频率有限制。
具体请参见 [厂商描述](https://firebase.google.com/docs/cloud-messaging/concept-options?hl=zh-cn#upstream_throttling)。
