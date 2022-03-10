### 如何设置自定义铃声？

使用自定义铃声可以通过创建通知渠道实现：
1. 创建通知渠道，通过 TPNS 封装 API 或安卓原生 API 创建指定自定义铃声文件的通知渠道，可参考 [创建通知渠道](https://cloud.tencent.com/document/product/548/36659#.E5.88.9B.E5.BB.BA.E9.80.9A.E7.9F.A5.E6.B8.A0.E9.81.93)。
2. 在 TPNS 推送 REST API 指定相同的通知渠道`n_ch_id `进行推送,厂商通道需指定厂商渠道 ID，如华为通道需指定`hw_ch_id`,小米通道需指定`xm_ch_id`。

>? 目前仅华为、小米、FCM 和 TPNS 通道支持自定义铃声，厂商通道渠道 ID 申请步骤可参考 [厂商通道消息分类功能使用说明](https://cloud.tencent.com/document/product/548/44531)。
>

### 如何关闭 TPNS 的保活功能？

如需关闭联合保活功能，请在应用初始化的时候，例如 Application 或 LauncherActivity 的 onCreate 中调用如下接口，并传递 false 值：
>!仅 1.1.6.0 之后版本支持关闭联合保活功能，1.1.6.0之前版本TPNS 默认开启联合保活能力，且不可关闭。

```java
XGPushConfig.enablePullUpOtherApp(Context context, boolean pullUp);
```

若您使用 gradle 自动集成方式，请在自身应用的 AndroidManifest.xml 文件 &lt;application&gt; 标签下配置如下结点，其中 `xxx` 为任意自定义名称；如果使用手动集成方式，请修改如下节点属性：
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

### 首次安装启动时如何配置不自动启动推送服务？

针对“用户同意隐私服务协议” 场景，开发者可以在 AndroidManifest.xml 文件添加以下节点，应用首次安装启动时即不会自启推送服务，直到调用了推送服务注册接口`XGPushManager.registerPush()` 才会开启：

```
<meta-data
android:name="XG_SERVICE_PULL_UP_OFF"
android:value="true" />
```
### TPNS SDK 支持鸿蒙系统的推送吗？

鸿蒙系统完全兼容 Android SDK，推送功能可正常使用。


### 厂商推送服务需要上架应用市场才可以开通吗？

| 厂商 | 是否需要上架应用市场 |
|---------|---------|
| 小米 | 否，个人开发者账号即可 [开通小米平台推送服务](https://dev.mi.com/console/doc/detail?pId=68) | 
| 魅族 | 否，个人开发者账号即可 [开通魅族平台推送服务](http://open.res.flyme.cn/fileserver/upload/file/201709/a271468fe23b47408fc2ec1e282f851f.pdf)| 
| FCM | 否，个人开发者账号即可开通 FCM 推送服务 |
| 华为 | 否，个人开发者账号即可 [开通华为平台推送服务](https://developer.huawei.com/consumer/cn/doc/distribution/app/agc-enable_service#enable-service) | 
| OPPO | 是，且需要企业开发者账号可 [开通 OPPO 平台推送服务](https://open.oppomobile.com/wiki/doc/#id=10195)| 
| vivo | 是 ，且需要企业开发者账号可 [开通 vivo 平台推送服务](https://dev.vivo.com.cn/documentCenter/doc/2)|


### 集成 vivo 厂商通道后 “APP 包含未使用的权限字符串”，如何处理？

开发者在集成 vivo 厂商通道推送服务后，部分安全检测工具可能会提示 “APP 包含未使用的权限字符串”，详情如下： 
问题来源：vivo 厂商通道推送 SDK 版本名 2.3.4。
涉及类文件：com.vivo.push.util.z 涉及敏感权限字符串：android.permission.GET_ACCOUNTS。
>! 经检查发现最新的 vivo 厂商通道推送 SDK 版本名 3.0.0.3 中同样包含此问题。

问题代码来源为 vivo 厂商通道推送 SDK，TPNS 项目组无法变更其内容；此问题已向 vivo 推送服务相关人员反馈，表示相关静态字段为 SDK 遗留代码，并无实际使用，会尽快排期修复。 当前可参考的快速解决办法如下：
- 方式一（推荐）： 在《APP隐私声明》里增加 [移动推送 TPNS 的隐私说明](https://cloud.tencent.com/document/product/548/36652#.E9.9A.90.E7.A7.81.E5.8D.8F.E8.AE.AE.E5.A3.B0.E6.98.8E.E5.BB.BA.E8.AE.AE)。 
- 方式二（不推荐）： 剔除掉 vivo 相关 jar 包，但是也会丧失掉 vivo 厂商通道的能力。
 
### 什么是 TPNS 通道？

- TPNS 通道是移动推送 TPNS 的自建通道，依赖移动推送 TPNS Service 在线（与移动推送 TPNS 后台服务器保持长连接）才能下发消息，因此 TPNS 通道的实际发送一般比其他厂商通道的数据要低。
- 如果需要实现离线推送，建议集成厂商通道，请参见 [厂商通道接入指南](https://cloud.tencent.com/document/product/548/45909)。



### 为何关闭应用后，无法收到推送？

- 目前第三方推送都无法保证关闭应用后仍可收到推送消息，该问题为手机定制 ROM 对移动推送 TPNS  Service 的限制问题，移动推送的 TPNS 通道推送，需要建立在移动推送 TPNS 的 Service 能够与移动推送 TPNS 后台服务器保持长连接，Service 被终止后，需由系统、安全软件和用户操作决定是否能够再次启动。
- 移动推送 TPNS 的 Service 和移动推送 TPNS 的服务器断开连接后，此时给这个设备下发的消息，将变成离线消息，离线消息最多保存72小时，每个设备最多保存三条，如果有多条离线消息，只保留最新的三条消息。在关闭应用期间推送的消息，如开启应用无法收到，请检查是否调用了反注册接口：XGPushManager.unregisterPush\(this\)。
- 如果已经集成厂商通道，但是仍收不到离线推送，请先在 [排查工具](https://console.cloud.tencent.com/tpns/user-tools) 上查询该 Token 是否已经注册上厂商通道，如果未注册成功，请参见 [厂商通道注册失败排查指南](https://cloud.tencent.com/document/product/548/45659) 进行排查。
- QQ 和微信是系统级别的应用白名单，相关的 Service 不会因为关闭应用而退出，所以用户感知推出应用过后，仍可收到消息，但相关的 Service 仍能够在后台存活。

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

### 努比亚机型无法收到推送？
不支持2015年后发布的努比亚机型，因为努比亚新的系统版本增加了超级省电的功能（会迅速将后台进程停止），移动推送 TPNS  Service 无法启动，所以努比亚机型无法注册成功。



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

当订阅者点击您的通知时，可以根据您的配置跳转至指定的应用内页面、H5、Deeplink 等，来满足您在不同场景下的需求。详情请参见 [通知点击跳转](https://cloud.tencent.com/document/product/548/48572)。

### 终端内厂商通道支持哪些通知事件回调？

| 回调 | 抵达回调 | 点击回调 |
|---------|---------|---------|
| 小米 | 不支持 | 支持 |
| 魅族 | 不支持 | 支持 |
| FCM | 不支持 | 支持 |
| 华为 | 不支持 | 支持 |
| OPPO | 不支持 | 支持 |
| vivo | 不支持 | 支持 |

>! 厂商通道的点击回调需 SDK 版本1.2.0.1及以上版本支持；旧版本仅支持华为、小米、魅族、vivo。
>


### 为什么关闭应用时，onNotifactionClickedResult、onNotificationShowedResult 获取的 title 和 content 为空？

由于厂商通道推送的 title 和 content 是拼接在 intent 中下发的，因此，在使用 onNotifactionClickedResult、onNotificationShowedResult 方法时，无法获取 title 和 content。如需获取参数，请使用 intent 的方式，详情请参考 [通知点击跳转](https://cloud.tencent.com/document/product/548/48572)。


### 应用接入了厂商通道，但在调试过程中遇到 other push Token 为空的问题，如何解决？


在应用运行日志中观察到如下类似日志： 
```
[OtherPushClient] handleUpdateToken other push token is :  other push type: huawei
```

表示您的应用注册该厂商通道失败，您可以通过获取厂商通道注册失败的返回码来进行问题定位和排查，详情请参见 [厂商通道注册失败排查指南](https://cloud.tencent.com/document/product/548/45659)。

### 同时集成了即时通信 IM 和 TPNS，存在大量的厂商类冲突，该如何解决？

目前 IM 已使用 TPNS 提供的厂商 jar 包，请按照下方表格替换相关依赖包，替换后即可解决。

 | 推送通道 | 系统要求 | 条件说明 |
 | --------------- | ------| -------------------------------------------- | 
 | 小米推送| MIUI|使用小米推送，添加依赖：`implementation 'com.tencent.tpns:xiaomi:1.2.1.3-release'`|
 | 华为推送| EMUI|使用华为推送，添加依赖：<li>`implementation 'com.tencent.tpns:huawei:1.2.1.3-release'`</li><li>`implementation 'com.huawei.hms:push:5.0.2.300'`</li>| 
| Google FCM 推送| Android 4.1及以上|手机端需安装 Google Play Services 且在中国大陆地区以外使用。添加依赖：`implementation 'com.google.firebase:firebase-messaging:20.2.3'`| 
| 魅族推送 | Flyme| 使用魅族推送，添加依赖：`implementation 'com.tencent.tpns:meizu:1.2.1.3-release'` | 
| OPPO 推送| ColorOS |并非所有 OPPO 机型和版本都支持使用 OPPO 推送，使用 OPPO 推送，添加依赖：`implementation 'com.tencent.tpns:oppo:1.2.1.3-release'`| 
| vivo 推送| FuntouchOS|并非所有 vivo 机型和版本都支持使用 vivo 推送，使用 vivo 推送，添加依赖：`implementation 'com.tencent.tpns:vivo:1.2.1.3-release'`|

### 如何适配 small icon 小图标？

- 谷歌原生 Android 5.0 以上的 ROM 都会对 target sdk 大于等于21的 App 的小图标进行处理，增加一层颜色，导致图标变灰。
- 若需要显示颜色效果，可以将 target sdk 设成低于21；如果并不想将 target sdk 设成低于21，可以将一张背景透明的 png 格式小图片名称改成 notification_icon.png（资源名称不能被混淆），并放在 drawable 目录下，该方式显示的小图标即可为灰色（但是图标有形状）。
- TPNS Android SDK 1.2.2.0 起，默认情况下 notification_icon.png 小图标资源将仅在谷歌 Pixel 手机上直接生效；其他品牌手机若需实现此类自定义通知小图标效果，还需指定推送 API 字段 message.android.small_icon 为资源文件名称（不带文件后缀）；同时自定义通知小图标支持染色为单一纯色，需指定推送 API 字段 message.android.icon_color 为 RGB 颜色的十进制值。

推送 API 字段设置示例如下，其中 icon_color: 123456，即为 RGB 颜色 #01e240：
```
{
    "message": {
        "android": {
            "small_icon": "notification_icon",
            "icon_color": 123456
        }
    }
}
```

适配后的具体效果如下，[建议参考 Demo logo 图标进行作图](https://git.code.tencent.com/tpns/TPNS-Demo-Android/blob/master/app/src/main/res/drawable/notification_icon.png)。

<img src="https://main.qcloudimg.com/raw/d9f92fb413aa98a01af64b2c17680bef.jpg" width="60%"></img>


>?
- small icon 必须是带 Alpha 透明通道的 PNG 图片。
- 背景必须是透明。
- 周围不宜留过多 padding。
- 建议统一使用46 x 46px，过小图片会模糊，过大系统会自动缩小。


### Flyme 6.0 及以下版本的魅族手机，为何消息抵达设备却不在通知栏展示？

1. Flyme 6.0 及以下版本的魅族手机，使用手动集成方式。
2. Flyme 6.0 及以下版本的魅族手机，使用自动集成方式，且使用的 TPNS Android SDK 为1.1.4.0 以下的版本。

以上两种情况，需要在 drawable 不同分辨率的文件夹下对应放置一张名称必须为 stat_sys_third_app_notify 的图片，详情请参考 [TPNS Android SDK](https://console.cloud.tencent.com/tpns/sdkdownload) 中魅族厂商依赖目录的 flyme-notification-res 文件夹。


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

在 AndroidX 项目工程的 gradle.properties 文件中添加如下属性：
```
android.useAndroidX=trueandroid.enableJetifier=true
```

> ? 
> - android.useAndroidX=true，表示当前项目启用 AndroidX。
> - android.enableJetifier=true，表示将依赖包迁移到 AndroidX。 
> 

### 厂商通道推送服务 SDK “存在通过 HTTP 明文传输信息的行为”，如何处理？

开发者在集成各厂商通道推送服务后，部分安全检测工具可能会提示 “App 存在通过 HTTP 明文传输信息的行为” ，具体 HTTP 地址涉及：
1. 小米推送 SDK：`http://new.api.ad.xiaomi.com/logNotificationAdActions，http://resolver.msg.xiaomi.net/psc/?t=a`
2. 魅族推送 SDK：`http://norma-external-collect.meizu.com/android/exchange/getpublickey.do，http://norma-external-collect.meizu.com/push/android/external/add.do`

以上 HTTP URL 均来自各厂商推送 SDK，TPNS 项目组无法明确其目的或控制其行为，但正在积极与厂商服务提供者联系并推动 HTTPS 改造；开发者当前可以自行评估选择是否继续使用以上厂商提供的推送服务。


### Android 版本4.4.4编译报错，怎么办？

由于工程加载方法数超过65K，请对工程做分包处理。

### 指定打开某个 Activity 页面，但经常不能正常跳转？

在部分手机，通知栏跳转到某个页面可能会出现权限问题。
处理方法：在 androidManifest.xml 中，需要打开的 Activity 加上 android:exported="true"。

### 注册方法能在线程中创建吗？
注册方法可以在任何地方调用，但注意要传递 ApplicationContext。

