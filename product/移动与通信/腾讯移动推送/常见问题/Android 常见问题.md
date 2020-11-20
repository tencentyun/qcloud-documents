### 如何关闭 TPNS 的保活功能？

TPNS 默认开启联合保活能力，请在应用初始化的时候，例如 Application 或 LauncherActivity 的 onCreate 中调用如下接口，并传递 false 值:

```java
XGPushConfig.enablePullUpOtherApp(Context context, boolean pullUp);
```

若您使用 gradle 自动集成方式，请在自身应用的 AndroidManifest.xml 文件 <application> 标签下配置如下结点，其中 ```xxx``` 为任意自定义名称；如果使用手动集成方式，请修改如下节点属性：

```xml
<!-- 在自身应用的AndroidManifest.xml文件中添加如下结点，其中 xxx 为任意自定义名称: -->     
<!-- 关闭与 TPNS 应用的联合保活功能，请配置 -->
<provider
	 android:name="com.tencent.android.tpush.XGPushProvider"
	 tools:replace="android:authorities"
	 android:authorities="应用包名.xxx.XGVIP_PUSH_AUTH"
	 android:exported="false" />    
```

若控制台有以下日志打印，则表明联合保活功能已经关闭：`I/TPush: [ServiceUtil] disable pull up other app`。

### 设备注册失败的原因？

- 新创建的 App 会有一分钟左右的数据同步过程，在此期间，注册可能返回20错误码，稍后重试即可。
- **参数填写有误**：Access ID 和 Access Key 是否正确配置，常见错误是误用 Secret key ，或者 Access key 头尾有空格。
- **注册返回错误**：若控制台返回10004、10002、20等错误码，请参见 [Android SDK 错误码](https://cloud.tencent.com/document/product/548/36660)。
- **注册无回调**：确认当前网络情况是否良好，建议使用4G网络测试，Wi-Fi 由于使用人数过多可能造成网络带宽不足。
- **努比亚品牌的手机**：在2015年下半年和2016年出的机器均无法注册，具体机型包括 Nubia Z11 系列，NubiaZ11S 系列，NubiaZ9S 系列。

### 为何注册成功，无法收到推送？

请参见 [排查工具指南](https://cloud.tencent.com/document/product/548/48774) 使用排查工具进行自动化排查，一般有如下错误：

- 请查看当前应用包名，是否与注册移动推送 TPNS 应用时填写的应用包名不一致。如果不一致，推送时，建议开启多包名推送。
- 检查手机网络是否异常，切换4G网络，进行测试。
- 移动推送 TPNS 分为通**知栏消息**和**应用内消息**（透传消息），通知栏消息可以展示到通知栏，应用内消息不能展示到通知栏。
- 确认手机当前模式是正常模式，部分手机在低电量，勿扰模式，省电模式下，会对后台移动推送 TPNS 进程进行一系列网络和活动的限制。
- 查看设备是否开启通知栏权限，OPPO，vivo 等手机，需要手动开启通知栏权限。



### 什么是 TPNS 通道？

- TPNS 通道是移动推送 TPNS 的自建通道，依赖移动推送 TPNS Service 在线（与移动推送 TPNS 后台服务器保持长连接）才能下发消息，因此 TPNS 通道的实际发送一般比其他厂商通道的数据要低。
- 如果需要实现离线推送，建议集成厂商通道，请参见 [厂商通道接入指南](https://cloud.tencent.com/document/product/548/45909)。



### 为何关闭应用后，无法收到推送？

- 目前第三方推送都无法保证关闭应用后仍可收到推送消息，该问题为手机定制 ROM 对移动推送 TPNS  Service 的限制问题，移动推送的 TPNS 通道推送，需要建立在移动推送 TPNS 的 Service 能够与移动推送 TPNS 后台服务器保持长连接，Service 被终止后，需由系统、安全软件和用户操作决定是否能够再次启动。
- 移动推送 TPNS 的 Service 和移动推送 TPNS 的服务器断开连接后，此时给这个设备下发的消息，将变成离线消息，离线消息最多保存72小时，每个设备最多保存三条，如果有多条离线消息，只保留最新的三条消息。在关闭应用期间推送的消息，如开启应用无法收到，请检查是否调用了反注册接口：XGPushManager.unregisterPush\(this\)。
- 如果已经集成厂商通道，但是仍收不到离线推送，请先在 [排查工具](https://console.cloud.tencent.com/tpns/user-tools) 上查询该 Token 是否已经注册上厂商通道，如果未注册成功，请参见 [厂商通道注册失败排查指南](https://cloud.tencent.com/document/product/548/45659) 进行排查。
- QQ 和微信是系统级别的应用白名单，相关的 Service 不会因为关闭应用而退出，所以用户感知推出应用过后，仍可收到消息，但相关的 Service 仍能够在后台存活。

### 在非华为手机上安装了华为移动服务，且在 App 中集成了 TPNS SDK，会导致华为推送及其它组件功能失效，如何解决？

自 TPNS SDK 1.1.6.3 版本起，为避免**在非本品牌手机上、其他品牌的推送服务在后台自启、传输用户数据**，会在非本品牌手机上禁用其他品牌的推送服务组件。
华为在账号、游戏、推送等不同功能上有一些公共组件，TPNS 禁用推送组件可能会导致其它服务功能在非华为品牌手机上同样不能启动；若您需要关闭此禁用功能，可配置以下内容：
在 AndroidManifest.xml 文件 application 标签下添加节点配置，并重装应用（需卸载后重装）。

```xml
<meta-data
		android:name="tpns-disable-component-huawei-v2"
		android:value="false" />
<meta-data
		android:name="tpns-disable-component-huawei-v4"
		android:value="false" />
```

### 如何设置消息点击事件？

TPNS 推荐使用 Intent 方式进行跳转（注：SDK 点击消息默认支持点击事件，触发后打开主界面，如果在 onNotifactionClickedResult 设置跳转操作会与管理台/API中指定的自定义跳转冲突，导致自定义的跳转失效）。
**使用 Intent 方式跳转指引：**
在客户端 App 的 manifest 上，配置需要跳转的页面：

- 如要跳转 AboutActivity 指定页面，示例代码如下：

```
<activity
            android:name="com.qq.xg.AboutActivity"
            android:theme="@android:style/Theme.NoTitleBar.Fullscreen" >
            <intent-filter >
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT"/>
                <!-- 通过自定义 data 块内容指定您的完整 scheme，按照您的配置，将会组成形如"语义名://主机名/路径名"的 url 标识 -->
                <!-- 为防止和其他应用的跳转目标页面冲突，您可以使用带有 app 名称、app 包名等可以唯一标记应用的字段进行配置-->
                <data
                    android:scheme="语义名"
                    android:host="主机名"
                    android:path="/路径名" />
            </intent-filter>
</activity>
```

- 若使用移动推送 TPNS 管理台设置 Intent 进行跳转，填写方式如下：
  ![](https://main.qcloudimg.com/raw/a904c7c7917fb7d69bf741f7b6e52099.png)
- 若使用服务端 SDK ，设置 Intent 进行跳转，可设置 Intent 为（以 Java SDK 为例）：
```
action.setIntent("xgscheme://com.tpns.push/notify_detail");
```

- 若需要带上 param1 和 param2 等参数，您可以做如下设置：
```
action.setIntent("xgscheme://com.tpns.push/notify_detail?param1=aa&param2=bb");
```

**终端获取参数**：

1. 在您跳转指定的页面 onCreate 方法里，添加如下代码：

```
Uri uri = getIntent().getData();
    if (uri != null) {                
String url = uri.toString();
String p1= uri.getQueryParameter("param1");
String p2= uri.getQueryParameter("param2");
 }
```

2. 如果传参包含有特殊字符，如 # 、& 等，可以参考使用如下方式解析：

```
Uri uri = getIntent().getData();
    if (uri != null) {                
 String url = uri.toString();
 UrlQuerySanitizer sanitizer = new UrlQuerySanitizer();
 sanitizer.setUnregisteredParameterValueSanitizer(UrlQuerySanitizer.getAllButNulLegal());
   sanitizer.parseUrl(url);
   String value1 = sanitizer.getValue("key1");
   String value2 = sanitizer.getValue("key2");
   Log.i("TPNS" , "value1 = " + value1 + " value2 = " + value2);
}
```

### 厂商通道的回调支持哪些？

- 小米通道支持抵达回调，不支持点击回调，支持透传。
- 华为通道不支持抵达回调，支持点击回调（需要自定义参数），支持透传（但忽略自定义参数）。
- 魅族通道支持抵达回调，支持点击回调，不支持透传。
- vivo 通道不支持抵达回调，支持点击回调，不支持透传
- OPPO 通道不支持点击和抵达回调，不支持透传

> ?如果需要通过点击回调获取参数或者跳转自定义页面，可以通过使用 Intent 来实现。



### 应用接入了厂商通道，但在调试过程中遇到 other push Token 为空的问题，如何解决？


在应用运行日志中观察到如下类似日志： 

```
[OtherPushClient] handleUpdateToken other push token is :  other push type: huawei
```



表示您的应用注册该厂商通道失败，您可以通过获取厂商通道注册失败的返回码来进行问题定位和排查，详情请参见 [厂商通道注册失败排查指南](https://cloud.tencent.com/document/product/548/45659)。

### 同时集成了即时通信 IM 和 TPNS，存在大量的厂商类冲突，该如何解决？

目前 IM 已使用 TPNS 提供的厂商 jar 包，请按照下方表格替换相关依赖包，替换后即可解决。

| 推送通道       |        系统要求           |    条件说明                  |
| --------------- | ------| -------------------------------------------- |
| 小米推送| MIUI|使用小米推送，添加依赖：`implementation 'com.tencent.tpns:xiaomi:1.2.1.2-release'`|
| 华为推送|  EMUI|使用华为推送，添加依赖：<li>`implementation 'com.tencent.tpns:huawei:1.2.1.2-release'`  <li> `implementation 'com.huawei.hms:push:5.0.2.300'`|
| Google FCM 推送|  Android 4.1及以上|手机端需安装 Google Play Services 且在中国大陆地区以外使用。添加依赖：`implementation 'com.google.firebase:firebase-messaging:20.2.3'`|
| 魅族推送 | Flyme|  使用魅族推送，添加依赖：`implementation 'com.tencent.tpns:meizu:1.2.1.2-release'` |
| OPPO 推送|  ColorOS |并非所有 OPPO 机型和版本都支持使用 OPPO 推送，使用 OPPO 推送，添加依赖：`implementation 'com.tencent.tpns:oppo:1.2.1.2-release'`|
| vivo 推送|  FuntouchOS|并非所有 OPPO 机型和版本都支持使用 OPPO 推送，使用 vivo 推送，添加依赖：`implementation 'com.tencent.tpns:vivo:1.2.1.2-release'`|






### Flyme 6.0 及以下版本的魅族手机，为何消息抵达设备却不在通知栏展示？

1. Flyme 6.0 及以下版本的魅族手机，使用手动集成方式。
2. Flyme 6.0 及以下版本的魅族手机，使用自动集成方式，且使用的 TPNS Android SDK 为1.1.4.0 以下的版本。

以上两种情况，需要在 drawable 不同分辨率的文件夹下对应放置一张名称必须为 stat_sys_third_app_notify 的图片，详情请参考 [TPNS Android SDK](https://console.cloud.tencent.com/tpns/sdkdownload) 中的 flyme-notification-res 文件夹。




### 使用控制台快速集成时出现异常，如何解决？

1. 如果集成出现异常， 则将 `tpns-configs.json `文件中的 `"debug"` 字段置为` true`,  运行命令： 
```
./gradlew --rerun-tasks :app:processReleaseManifest 
```
并通过` "TpnsPlugin" `关键字进行分析。
2. 单击【sync projects】。
   ![](https://main.qcloudimg.com/raw/5fecbe6b63374e7e0e58c4b2cd215acb.png)
3. 在项目的 External Libraries 中查看是否有相关依赖。
   ![](https://main.qcloudimg.com/raw/485c7595f1b478a6fad725d38deb87b4.png)



### Android 拓展库 V4 到 AndroidX 如何转换？

在 AndroidX 项目工程的 gradle.properties 文件中添加如下属性

```
android.useAndroidX=trueandroid.enableJetifier=true
```

> ? 
> - android.useAndroidX=true，表示当前项目启用 AndroidX。
> - android.enableJetifier=true，表示将依赖包迁移到 AndroidX。 

