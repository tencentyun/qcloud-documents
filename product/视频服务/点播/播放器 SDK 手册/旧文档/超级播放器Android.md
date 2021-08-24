## 简介

Android 超级播放器 SDK 是腾讯云开源的一款播放器组件，简单几行代码即可拥有类似腾讯视频强大的播放功能，包括横竖屏切换、清晰度选择、手势和小窗等基础功能，还支持视频缓存，软硬解切换和倍速播放等特殊功能，相比系统播放器，支持格式更多，兼容性更好，功能更强大，同时还具备首屏秒开、低延迟的优点，以及视频缩略图等高级能力。

## SDK 下载

点播 Android 超级播放器的项目地址是 [SuperPlayer_Android](https://github.com/tencentyun/SuperPlayer_Android)。

## 阅读对象

本文档部分内容为腾讯云专属能力，使用前请开通 [腾讯云](https://cloud.tencent.com) 相关服务，未注册用户可注册账号 [免费试用](https://cloud.tencent.com/login)。

## 快速集成
### aar 集成
1. 下载 SDK + Demo 开发包，项目地址为 [Android](https://github.com/tencentyun/SuperPlayer_Android)。
2. 导入`SDK/LiteAVSDK_XXX.aar`以及`Demo/superplayerkit`这个 module 复制到工程中。
3. 在`app/build.gradle`中添加依赖：
<dx-codeblock>
::: java java
compile(name: 'LiteAVSDK_Player_7.4.9211', ext: 'aar')
compile project(':superplayerkit')
// 超级播放器弹幕集成的第三方库
compile 'com.github.ctiao:DanmakuFlameMaster:0.5.3'
:::
</dx-codeblock>
4. 在项目`build.gradle`中添加：
<dx-codeblock>
::: java java
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
:::
</dx-codeblock>
5. 权限声明。
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

### 使用播放器

播放器主类为`SuperPlayerView`，创建后即可播放视频。
```java
//不开防盗链
SuperPlayerModel model = new SuperPlayerModel();
model.appId = 1400329073;// 配置 AppId
model.videoId = new SuperPlayerVideoId();
model.videoId.fileId = "5285890799710670616"; // 配置 FileId
mSuperPlayerView.playWithModel(model);

//开启防盗链需填写 psign， psign 即超级播放器签名，签名介绍和生成方式参见链接：https://cloud.tencent.com/document/product/266/42436
SuperPlayerModel model = new SuperPlayerModel();
model.appId = 1400329071;// 配置 AppId
model.videoId = new SuperPlayerVideoId();
model.videoId.fileId = "5285890799710173650"; // 配置 FileId
mSuperPlayerView.playWithModel(model);
model.videoId.pSign = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTQwMDMyOTA3MSwiZmlsZUlkIjoiNTI4NTg5MDc5OTcxMDE3MzY1MCIsImN1cnJlbnRUaW1lU3RhbXAiOjEsImV4cGlyZVRpbWVTdGFtcCI6MjE0NzQ4MzY0NywidXJsQWNjZXNzSW5mbyI6eyJ0IjoiN2ZmZmZmZmYifSwiZHJtTGljZW5zZUluZm8iOnsiZXhwaXJlVGltZVN0YW1wIjoyMTQ3NDgzNjQ3fX0.yJxpnQ2Evp5KZQFfuBBK05BoPpQAzYAWo6liXws-LzU"; 
mSuperPlayerView.playWithModel(model);
```



运行代码，可以看到视频在手机上播放，并且界面上大部分功能都处于可用状态。
<img src="https://main.qcloudimg.com/raw/128c45edfc77b319475868c21caec2de.png" width="550">

### 选择 FileId

视频 FileId 在一般是在视频上传后，由服务器返回：

1. 客户端视频发布后，服务器会返回 FileId 到客户端。
2. 服务端视频上传时，在 [确认上传](https://cloud.tencent.com/document/product/266/9757) 的通知中包含对应的 FileId。

如果文件已存在腾讯云，则可以进入 [媒资管理](https://console.cloud.tencent.com/vod/media) ，找到对应的文件，查看 FileId。如下图所示，ID 即表示 FileId：
![](https://main.qcloudimg.com/raw/1a3677d5fe618227a117d7502be42793.png)



### 打点功能

在播放长视频时，打点信息有助于观众找到感兴趣的点。使用 [修改媒体文件属性](https://cloud.tencent.com/document/product/266/31762) API，通过 AddKeyFrameDescs.N 参数可以为视频设置打点信息。

调用后，播放器的界面会增加新的元素。
<img src="https://main.qcloudimg.com/raw/55ebce6d0c703dafa1ac131e1852e025.png" width="550">


### 小窗播放
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

<img src="https://main.qcloudimg.com/raw/2cab897e43e4a01ee5f8e48372ce79a3.jpg" width="350">

### 退出播放

当不需要播放器时，调用`resetPlayer`清理播放器内部状态，释放内存。

```java
mSuperPlayerView.resetPlayer();
```

## 更多功能

完整功能可扫码下载视频云工具包体验，或直接运行工程 Demo。
<img src="https://main.qcloudimg.com/raw/6790ddaf4ffe4afd0ceb96b309a16496.png" width="150">


