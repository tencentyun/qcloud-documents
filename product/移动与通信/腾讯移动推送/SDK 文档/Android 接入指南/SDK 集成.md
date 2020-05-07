

## 操作场景
Android SDK 是腾讯移动推送服务为客户端实现消息推送而提供给开发者的接口，本文将提供 AndroidStudio Gradle 自动集成和 Android Studio 手动集成两种方式。
>!如果您是从信鸽平台（https://xg.qq.com）迁移至腾讯移动推送平台，请务必使用 [Android 迁移指南](https://cloud.tencent.com/document/product/548/41609) 调整集成配置。


## 操作步骤
### 集成方法
#### AndroidStudio Gradle 自动集成

>!在配置 SDK 前，确保已创建 Android 平台的应用。

1. 登录 [腾讯移动推送控制台](https://console.cloud.tencent.com/tpns)，选择左侧菜单【配置管理】，获取应用的包名、AccessID、AccessKey。
2. 在 [SDK 下载](https://console.cloud.tencent.com/tpns/sdkdownload) 页面，获取当前最新版本号。
3. 在 app build.gradle 文件下，配置以下内容：

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
    implementation 'com.tencent.tpns:tpns:[VERSION]-release' //  TPNS 推送 [VERSION] 为当前SDK版本号,版本号可在SDK下载页查看

}
```
4. 境外集群接入方法请参考下文 [境外集群接入方法](https://cloud.tencent.com/document/product/548/36652#JWjieru)。

>!
- 如在添加以上 abiFilter 配置后， Android Studio 出现以下提示：
NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin。则在 Project 根目录的 gradle.properties 文件中添加  android.useDeprecatedNdk=true。
- 如需监听消息请参考 XGPushBaseReceiver 接口或是 demo 的 MessageReceiver 类。自行继承 XGPushBaseReceiver 并且在配置文件中配置如下内容（请勿在 receiver  里处理耗时操作）：
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
- 如需兼容 Android P，需要添加使用 Apache HTTP client 库，在 AndroidManifest 的 application 节点内添加以下配置即可。
```
<uses-library android:name="org.apache.http.legacy" android:required="false"/>
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
    <uses-permission android:name="android.permission.GET_TASKS" /> 
```


| 权限                                       | 是否必需 | 说明                           |
| ---------------------------------------- | ---- | ---------------------------- |
| android.permission.INTERNET              | **必需**   | 允许程序访问网络连接，可能产生 GPRS 流量        |
| android.permission.ACCESS_WIFI_STATE     | **必需**   | 允许程序获取当前 Wi-Fi 接入的状态以及 WLAN 热点的信息 |
| android.permission.ACCESS_NETWORK_STATE  | **必需**   | 允许程序获取网络信息状态                 |
| android.permission.WAKE_LOCK             | 可选  | 允许程序在手机屏幕关闭后，后台进程仍然运行         |
| android.permission.VIBRATE               | 可选   | 允许应用震动                       |
| android.permission.READ_PHONE_STATE      | 可选   | 允许应用访问手机状态                   |
| android.permission.RECEIVE_USER_PRESENT  | 可选   | 允许应用可以接收点亮屏幕或解锁广播            |
| android.permission.WRITE_EXTERNAL_STORAGE | 可选   | 允许程序写入外部存储                   |
| android.permission.RESTART_PACKAGES      | 可选   | 允许程序结束任务                     |
| android.permission.GET_TASKS             | 可选   | 允许程序获取任务信息                   |



#### 组件和应用信息配置

```xml
<application>
    <!-- 应用的其它配置 -->
    <uses-library android:name="org.apache.http.legacy" android:required="false"/> 
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
            <action android:name="com.tencent.android.xg.vip.action.ACTION_SDK_KEEPALIVE" />
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

    <!-- 【必须】 通知service，其中android:name部分要改为当前包名 -->
        <service android:name="com.tencent.android.tpush.rpc.XGRemoteService"
            android:exported="false">
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

    <!-- 【必须】 请修改为 APP 的 AccessId，“15”开头的10位数字，中间没空格 -->
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

<span id="JWjieru"></span>
#### 境外集群接入方法
如需将推送集群切换为新加坡或者中国香港，请按照上述步骤正常集成后，在 Androidanifest 文件 application 标签内添加以下元数据：
```
<application>
        // 其他安卓组件
        <meta-data
            android:name="XG_GUID_SERVER"
            android:value="境外域名/guid/api/GetGuidAndMqttServer" />           
        <meta-data
            android:name="XG_STAT_SERVER"
            android:value="境外域名/log/statistics/push" />        
        <meta-data
            android:name="XG_LOG_SERVER"
            android:value="境外域名/v3/mobile/log/upload" /> 
</application>
```
**境外域名如下：**
中国香港：`https://api.tpns.hk.tencent.com`
新加坡：`https://api.tpns.sgp.tencent.com`

#### 音视频富媒体使用方法（可选）
1. 在 App 的 layout 目录下，新建一个 xml 文件，命名为 xg_notification。
2. 复制以下代码到文件中：
```
<?xml version="1.0" encoding="UTF-8"?>
-<RelativeLayout android:layout_height="wrap_content" android:layout_width="match_parent" android:id="@+id/xg_root_view" xmlns:android="http://schemas.android.com/apk/res/android">
<!--通知的背景，id名字不能改变，其他可变-->
<ImageView android:layout_height="match_parent" android:layout_width="match_parent" android:id="@+id/xg_notification_bg" android:scaleType="centerCrop"/>
<!--通知的大图标，id名字不能改变，其他可变.必须-->
<ImageView android:layout_height="48dp" android:layout_width="48dp" android:id="@+id/xg_notification_icon" android:scaleType="centerInside" android:layout_marginLeft="5dp" android:layout_centerVertical="true" android:layout_alignParentLeft="true"/>
<!--通知的时间，id名字不能改变，其他可变.若不显示时间可以去掉此布局-->
<TextView android:layout_height="wrap_content" android:layout_width="wrap_content" android:id="@+id/xg_notification_date" android:textSize="12dp" android:layout_marginRight="5dp" android:layout_marginTop="5dp" android:layout_alignParentRight="true" android:layout_alignParentTop="true"/>
<!--通知的标题，id名字不能改变，其他可变。必须-->
<TextView android:layout_height="wrap_content" android:layout_width="match_parent" android:id="@+id/xg_notification_style_title" android:layout_marginLeft="10dp" android:layout_marginTop="20dp" android:singleLine="true" android:layout_toRightOf="@id/xg_notification_icon" android:layout_toLeftOf="@id/xg_notification_date"/>
<!--通知的内容，id名字不能改变，其他可变。必须-->
<TextView android:layout_height="wrap_content" android:layout_width="match_parent" android:id="@+id/xg_notification_style_content" android:layout_marginTop="1dp" android:singleLine="true" android:layout_toLeftOf="@id/xg_notification_date" android:layout_alignLeft="@+id/xg_notification_style_title" android:layout_below="@+id/xg_notification_style_title"/>
<!--带音频的富媒体通知的音频播放按钮，id名字不能改变，其他可变。若没用到音频富媒体可以去掉此布局-->
<ImageView android:layout_height="25dp" android:layout_width="25dp" android:id="@+id/xg_notification_audio_play" android:layout_alignLeft="@+id/xg_notification_style_title" android:visibility="gone" android:background="@android:drawable/ic_media_play" android:layout_alignParentBottom="true"/>
<!--带音频的富媒体通知的音频停止播放按钮，id名字不能改变，其他可变.若没用到音频富媒体可以去掉此布局-->
<ImageView android:layout_height="25dp" android:layout_width="25dp" android:id="@+id/xg_notification_audio_stop" android:layout_marginLeft="30dp" android:layout_toRightOf="@+id/xg_notification_audio_play" android:visibility="gone" android:background="@android:drawable/ic_media_pause" android:layout_alignParentBottom="true"/></RelativeLayout>
```


#### 关闭联合保活

如果需要关闭TPNS的保活功能，若您使用 gradle 自动集成方式，请在自身应用的 AndroidManifest.xml 文件 <application> 标签下配置如下结点，其中 ```xxx``` 为任意自定义名称；如果使用手动集成方式，请修改如下节点属性：

```xml
   <!-- 在自身应用的AndroidManifest.xml文件中添加如下结点，其中 xxx 为任意自定义名称: -->
   <!-- 关闭与 TPNS 应用的联合保活功能，请配置 -->
   <provider
       android:name="com.tencent.android.tpush.XGPushProvider"
       tools:replace="android:authorities"
       android:authorities="应用包名.xxx.XGVIP_PUSH_AUTH"
       android:exported="false" />    
```

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


### 集成建议
<span id="HQToken"></span>
#### 获取 Token（非必选）
建议您完成 SDK 集成后，在 App 的【关于】、【意见反馈】等比较不常用的 UI 中，通过手势或者其他方式显示 Token，该操作便于我们后续进行问题排查。
示例代码如下：
```java
//获取 Token
XGPushConfig.getToken(getApplicationContext());
```
![](https://main.qcloudimg.com/raw/854020af14428df9972629e7dbbee55f.png)
