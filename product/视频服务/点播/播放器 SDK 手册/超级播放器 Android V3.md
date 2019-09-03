## 简介

Android 超级播放器 SDK 是一款用于播放云点播视频的播放器组件，几行代码就能实现类似腾讯视频强大的播放功能。

* 基础功能：横竖屏切换、清晰度选择、手势和小窗等。
* 高级功能：视频缓存、软硬解切换、倍速播放、视频缩略图、DRM 加密播放等。

相比系统播放器，超级播放器支持格式更多，兼容性更好，功能更强大。同时还具备首屏秒开和低延迟的优点。

## SDK 下载

云点播 Android 超级播放器的下载地址是 [SuperPlayer_Android](https://github.com/tencentyun/SuperPlayer_Android)。

## 快速集成

通过以下步骤，您将以最简单的方式集成 Android 超级播放器 SDK，并实现视频播放。

### aar 集成

1. 下载 SDK + Demo 开发包，下载地址为 [SuperPlayer_Android](https://github.com/tencentyun/SuperPlayer_Android)。
2. 导入`SDK/LiteAVSDK_XXX.aar`以及`Demo/app/libs/lib_tcsuperplayer.aar`到工程中。
3. 在`app/build.gralde`中添加依赖：
```java
compile(name: 'LiteAVSDK_Professional', ext: 'aar')
compile(name: 'lib_tcsuperplayer', ext: 'aar')
// 超级播放器弹幕集成的第三方库
compile 'com.github.ctiao:DanmakuFlameMaster:0.5.3'
```
4. 在项目`build.gralde`中添加：
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

>? `lib_tcsuperplayer.aar`以 moudle 方式开源，您可在`Demo/lib_tcsuperplayer`中找到所有源代码。

### 准备视频

登录 [云点播控制台](https://console.cloud.tencent.com/vod/overview)，单击左侧菜单栏的【媒资管理】，在“**已上传**”栏的视频列表中，将看到上传完成的视频，以及视频对应的 ID（即 FileId）。如果您还没有视频，请先单击【上传视频】，上传一个视频。
![](https://main.qcloudimg.com/raw/69b347af5d260d31ed9eb16617388a3b.png)

通过 [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) ，对上传的视频发起 [转自适应码流](https://cloud.tencent.com/document/product/266/34071) 任务：
API 参数中的`MediaProcessTask.AdaptiveDynamicStreamingTaskSet.Definition`建议填10，表示转 HLS 格式的自适应码流。

### 开始播放

播放器主类为`SuperPlayerView`，创建后即可播放视频。
```java
mSuperPlayerView = findViewById(R.id.main_super_player_view);
//通过fileid方式的视频信息配置
SuperPlayerModel model = new SuperPlayerModel();
model.appid = 1256993030;   //AppId
model.fileid = "7447398157015849771"; //视频 FileId
model.videoId.playDefinition = "10";  // 播放模板
model.videoId.version = SuperPlayerVideoId.FILE_ID_V3;
// 开始播放
mSuperPlayerView.playWithMode(model);
```

代码中的`appid`是您的 AppId，`fileid`是您要播放的视频 ID，`playDefinition`是您播放时使用的 [播放模板](https://cloud.tencent.com/document/product/266/34101#.E6.92.AD.E6.94.BE.E6.A8.A1.E6.9D.BF) ID，`version`固定填`SuperPlayerVideoId.FILE_ID_V3`。

运行代码，可以看到视频在手机上播放，并且界面上大部分功能都处于可用状态。
![](https://main.qcloudimg.com/raw/128c45edfc77b319475868c21caec2de.png)

## 缩略图与打点

在播放视频时，进度条上的“缩略图”和“打点信息”，有助于观众找到感兴趣的点。缩略图通过 [雪碧图](https://cloud.tencent.com/document/product/266/8101) 实现，视频打点需要 [修改媒资中的打点信息](https://cloud.tencent.com/document/product/266/31762#.E7.A4.BA.E4.BE.8B3-.E4.BF.AE.E6.94.B9.E5.AA.92.E4.BD.93.E6.96.87.E4.BB.B6.E8.A7.86.E9.A2.91.E6.89.93.E7.82.B9.E4.BF.A1.E6.81.AF)。

为视频截取雪碧图，并添加打点信息后，播放器的界面会增加新的元素。
![](https://main.qcloudimg.com/raw/55ebce6d0c703dafa1ac131e1852e025.png)

## 播放 DRM 加密的视频

数字版权管理（Digital Rights Management，DRM），是通过技术手段对内容加密，保护版权内容的安全，适用于音乐和电影等带版权的多媒体内容。云点播提供了商业级 DRM 加密，详情请参见 [如何对内容做版权保护](https://cloud.tencent.com/document/product/266/34105#.E5.95.86.E4.B8.9A.E7.BA.A7-drm)。

Android 超级播放器，可以播放 [商业级 DRM](https://cloud.tencent.com/document/product/266/34105#.E5.95.86.E4.B8.9A.E7.BA.A7-drm) 中两种方式加密的输出：

* 基于 Widevine 加密的 Dash 格式。
* 基于 SimpleAES 加密的 HLS 格式。

云点播提供了基于 Web 超级播放器的 [DRM 入门教程](https://cloud.tencent.com/document/product/266/34690)，建议您先通过该教程的学习。

### 使用方法

首先，App 需要从您的**业务后台**获取 Token，Token 的生成方式请参见 [Token 生成](https://cloud.tencent.com/document/product/266/34102#token-.E7.94.9F.E6.88.90) 。然后，通过 FileId + Token 方式进行播放，播放代码如下：

```java
SuperPlayerModel model = new SuperPlayerModel();
String fileId = "7447398157015849771";
model.appId = 1256993030;
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

代码中的`playDefinition`是 [播放模板](https://cloud.tencent.com/document/product/266/34101#.E6.92.AD.E6.94.BE.E6.A8.A1.E6.9D.BF) ID，播放器会根据播放模板指定的行为播放。例如,模板 ID 为20时，先尝试播放商业级加密的输出，若无法播放再降级播放 SimpleAES 方式加密的输出。

## 小窗播放

通过小窗播放，视频就可以悬浮在所有 Activity 之上进行播放。使用小窗播放非常简单，只需要在开始播放前调用下面代码即可：
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

如果不需要播放器，可以调用`resetPlayer`清理播放器内部状态，释放内存。
```java
mSuperPlayerView.resetPlayer();
```

## 更多功能

完整功能可扫码下载视频云工具包体验，或直接运行工程 Demo。
![Android二维码下载](https://main.qcloudimg.com/raw/344d9d41fc5e305a17e22e104b9305da.png)
