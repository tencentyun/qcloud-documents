## 简介

Android 播放器 SDK 是腾讯云开源的一款播放器组件，简单几行代码即可拥有类似腾讯视频强大的播放功能。包括横竖屏切换、清晰度选择、手势和小窗等基础功能，还支持视频缓存，软硬解切换，倍速播放等特殊功能。相比系统播放器，支持格式更多，兼容性更好，功能更强大。同时还支持直播流（flv + rtmp）播放，具备首屏秒开、低延迟的优点，清晰度无缝切换、直播时移等高级能力。

Android 播放器 SDK 完全免费开源，不对播放地址来源做限制，可以放心使用。

## 阅读对象

本文档部分内容为腾讯云专属能力，使用前请开通 [腾讯云](https://cloud.tencent.com) 相关服务，未注册用户可注册账号 [免费试用](https://cloud.tencent.com/login)。

## 快速集成

### aar 集成

1. 下载 SDK + Demo 开发包，下载地址为 （[Android](https://cloud.tencent.com/document/product/881/20205)）。
2. 导入 `SDK/LiteAVSDK_XXX.aar` 以及  `Demo/app/libs/lib_tcsuperplayer.aar`到工程中去。
3. 在 `app/build.gradle` 中添加依赖：

```java
compile(name: 'LiteAVSDK_Professional', ext: 'aar')
compile(name: 'lib_tcsuperplayer', ext: 'aar')
// 超级播放器弹幕集成的第三方库
compile 'com.github.ctiao:DanmakuFlameMaster:0.5.3'
```

4. 在项目`build.gradle`中添加：

```
...
allprojects {
    repositories {
        flatDir {
            dirs 'libs'
        }
        ...
    }
}
...
```

5. 权限声明

```java
<!--网络权限-->

<uses-permission android:name="android.permission.INTERNET" />

<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />

<!--点播播放器悬浮窗权限-->

<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />

<!--存储-->

<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
```

>!`lib_tcsuperplayer.aar` 以 module 方式开源，您可在 Demo/lib_tcsuperplayer 中找到所有源代码。



### 使用播放器

播放器主类为`SuperPlayerView`，创建后即可播放视频。

```java
mSuperPlayerView = findViewById(R.id.main_super_player_view);

SuperPlayerModel model = new SuperPlayerModel();

model.url = "http://200024424.vod.myqcloud.com/200024424_709ae516bdf811e6ad39991f76a4df69.f20.mp4";

mSuperPlayerView.playWithMode(model);
```

运行代码，可以看到视频在手机上播放，并且界面上大部分功能都处于可用状态。
![](https://main.qcloudimg.com/raw/128c45edfc77b319475868c21caec2de.png)

## 多清晰度

上面的示例代码只有一种清晰度，如果要添加多个清晰度，也非常简单。以直播为例，打开 [直播控制台](https://console.cloud.tencent.com/live/livemanage)，找到需要播放放的直播流，进入详情。

![](https://main.qcloudimg.com/raw/e3ee4765b25a9ada89dea341b9cb5cfd.png)

这里有不同清晰度、不同格式的播放地址。推荐使用 FLV 地址播放，代码如下：

```java
SuperPlayerModel model = new SuperPlayerModel();
model.multiURLs = new ArrayList<>();
model.multiURLs.add(new SuperPlayerModel.SuperPlayerURL("http://1252463788.vod2.myqcloud.com/95576ef5vodtransgzp1252463788/e1ab85305285890781763144364/v.f10.mp4", "流畅"));
model.multiURLs.add(new SuperPlayerModel.SuperPlayerURL("http://1252463788.vod2.myqcloud.com/95576ef5vodtransgzp1252463788/e1ab85305285890781763144364/v.f20.mp4", "标清"));
model.multiURLs.add(new SuperPlayerModel.SuperPlayerURL("http://1252463788.vod2.myqcloud.com/95576ef5vodtransgzp1252463788/e1ab85305285890781763144364/v.f30.mp4", "高清"));
model.playDefaultIndex = 1;// 默认播放标清

mSuperPlayerView.playWithModel(model);
```

在播放器中即可看到这几个清晰度，单击即可立即切换。

![直播清晰度](https://main.qcloudimg.com/raw/8cb10273fe2b6df81b36ddb79d0f4890.jpeg)

## 时移播放

播放器开启时移非常简单，您只需要在播放前配置好 appId：

```java
playerModel.appId = 1252463788;
```

>? appId 在【腾讯云控制台】>【[账号信息](https://console.cloud.tencent.com/developer)】中查到。

播放的直播流就能在下面看到进度条。往后拖动即可回到指定位置，单击【返回直播】可观看最新直播流。

![](https://main.qcloudimg.com/raw/a3a4a18819aed49b919384b782a13957.jpeg)

>! 时移功能处于公测申请阶段，如您需要可 [提交工单](https://console.cloud.tencent.com/workorder) 申请使用。

## FileId 播放

设置清晰度除了填写 url 外，更简单的使用方式是采用 fileId 播放。fileId 在一般是在视频上传后，由服务器返回：

1. 在 [腾讯云官网](https://cloud.tencent.com/) 注册腾讯云账号，然后开通点播服务。
2. 客户端视频发布后，服务器会返回 [fileId](https://cloud.tencent.com/document/product/584/9369) 到客户端。
3. 服务端视频上传，在 [确认上传](https://cloud.tencent.com/document/product/266/9757) 的通知中包含对应的 fileId。


如果文件已存在腾讯云，则可以进入 [媒资管理](https://console.cloud.tencent.com/vod/media)，找到对应的文件。点开后在右侧视频详情中，可以看到 appId 和 fileId。

![视频管理](https://mc.qcloudimg.com/static/img/fcad44c3392b229f3a53d5f8b2c52961/image.png)

播放 fileId 的代码如下：

```java
SuperPlayerModel model = new SuperPlayerModel();
model.appId = 1252463788;// 配置AppId
model.videoId = new SuperPlayerVideoId();
model.videoId.fileId = "5285890781763144364"; // 配置FileId
mSuperPlayerView.playWithModel(model);
```

视频在上传后，后台会自动转码（所有转码格式请参考 [转码模板](https://cloud.tencent.com/document/product/266/33478#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。转码完成后，播放器会自动显示多个清晰度。关于使用防盗链内容，您可以参考此篇文档：[点播超级播放器使用文档 - key 防盗链](https://cloud.tencent.com/document/product/266/14424#key-.E9.98.B2.E7.9B.97.E9.93.BE)。

### 视频缩略图&打点信息

在播放长视频时，雪碧图和打点信息有助于观众找到该兴趣的点。使用腾讯云服务 API，能快速对视频处理。

- [截取雪碧图](https://cloud.tencent.com/document/product/266/8101)
- [增加打点信息](https://cloud.tencent.com/document/product/266/14190)

任务执行成功后，播放器的界面会增加新的元素。
![](https://main.qcloudimg.com/raw/55ebce6d0c703dafa1ac131e1852e025.png)

### 数字版权管理
数字版权管理解决方案（Digital Rights Management, DRM），通过技术手段加密内容，用来控制带版权作品的使用、更改和分发，保护带版权内容的安全。适用于音乐、电影等带版权的多媒体内容。


Android SDK 可以播放云点播两种方式加密的输出：
1. 基于 Widevine 加密的 Dash 方案。
2. 基于 SimpleAES 加密的 HLS 方案。

关于 DRM 的更多详情，您可以参考此篇文档：[如何对内容做版权保护](<https://cloud.tencent.com/document/product/266/34105#.E5.95.86.E4.B8.9A.E7.BA.A7-drm>)。


#### 如何在 Android 平台使用腾讯云 DRM 服务

- 步骤1：集成 [超级播放器 Library ](<https://cloud.tencent.com/document/product/881/20213>)到您的工程中。
- 步骤2：从您的**业务后台**获取 Token，关于 Token 的内容，您可以参考此篇文档：[播放加密视频 - Token 生成](<https://cloud.tencent.com/document/product/266/34102#token-.E7.94.9F.E6.88.90>)。
- 步骤3：通过 FileId + Token 方式进行播放。

```java
SuperPlayerModel model = new SuperPlayerModel();
String fileId = "15517827183920333646";
model.appId = 1253039488;
model.videoId = new SuperPlayerVideoId();
model.videoId.fileId = fileId;
model.videoId.playDefinition = "20";  // 播放模板
model.videoId.version = SuperPlayerVideoId.FILE_ID_V3; // DRM需要使用V3协议
try {
    // Token需要进行URLEncoder
    String encodedToken = URLEncoder.encode("业务下发的Token", "UTF-8");
    model.token = encodedToken;
} catch (UnsupportedEncodingException e) {
    e.printStackTrace();
}
mSuperPlayerView.playWithModel(model);
```
>?
- 关于 FileId 的内容，您可以参考此篇文档：[超级播放器 - FileId 播放](<https://cloud.tencent.com/document/product/881/20213#667643674>)。
- 关于播放模板的内容，您可以参考此篇文档：[使用播放器播放视频 - 播放模板](https://cloud.tencent.com/document/product/266/34101#.E6.92.AD.E6.94.BE.E6.A8.A1.E6.9D.BF)。
- 播放器会根据播放模板 ID 指定的行为播放，例如当模板 ID 为20时，先尝试播放商业级加密的输出，若无法播放再降级播放 SimpleAES 方式加密的输出。
- 关于使用 DRM 防盗链内容，您可以参考此篇文档：[使用播放器播放视频](https://cloud.tencent.com/document/product/266/34101)。

## 小窗播放

小窗播放可以悬浮在所有 Activity 之上播放。使用小窗播放非常简单，只需要在开始播放前调用下面代码即可：

```java
// 播放器配置
SuperPlayerGlobalConfig prefs = SuperPlayerGlobalConfig.getInstance();
// 开启悬浮窗播放
prefs.enableFloatWindow = true;
//设置悬浮窗的初始位置和宽高
SuperPlayerGlobalConfig.TXRect rect = new SuperPlayerGlobalConfig.TXRect();
rect.x = 0;
rect.y = 0;
rect.width = 810;
rect.height = 540;
// ...其他配置
```

![](https://main.qcloudimg.com/raw/d6783a450e339526e0ca0b2ed3ef6142.png)

## 退出播放

当不需要播放器时，调用 `resetPlayer` 清理播放器内部状态，释放内存。

```java
mSuperPlayerView.resetPlayer();
```

## 更多功能

完整功能可扫码下载视频云工具包体验，或直接运行工程 Demo。

![Android二维码下载](https://main.qcloudimg.com/raw/344d9d41fc5e305a17e22e104b9305da.png)
