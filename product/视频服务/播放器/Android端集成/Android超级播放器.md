## 简介

Android 播放器 SDK 是腾讯云开源的一款播放器组件，简单几行代码即可拥有类似腾讯视频强大的播放功能。包括横竖屏切换、清晰度选择、手势和小窗等基础功能，还支持视频缓存，软硬解切换，倍速播放等特殊功能。相比系统播放器，支持 FLV、MP4 及 HLS 多种播放格式，兼容性更好，功能更强大。同时还支持直播流（FLV + RTMP）播放，具备首屏秒开、低延迟的优点，以及清晰度无缝切换、直播时移等高级能力。

Android 播放器 SDK 完全免费开源，不对播放地址来源做限制，请放心使用。

## 阅读对象

本文档部分内容为腾讯云专属能力，使用前请开通 [腾讯云](https://cloud.tencent.com) 相关服务，未注册用户可 [注册账号](https://cloud.tencent.com/document/product/378/17985) 免费试用。

## 快速集成

### aar 集成

1. 下载 SDK + Demo 开发包，下载地址请参见：[SDK 下载 - Android](https://cloud.tencent.com/document/product/881/20205)。
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

<dx-codeblock>
::: java java
mSuperPlayerView = findViewById(R.id.main_super_player_view);

SuperPlayerModel model = new SuperPlayerModel();

model.url = "http://200024424.vod.myqcloud.com/200024424_709ae516bdf811e6ad39991f76a4df69.f20.mp4";

mSuperPlayerView.playWithModel(model);
:::
</dx-codeblock>

运行代码，可以看到视频在手机上播放，并且界面上大部分功能都处于可用状态。
![](https://main.qcloudimg.com/raw/128c45edfc77b319475868c21caec2de.png)

## 多清晰度

上面的示例代码只有一种清晰度，如果要添加多个清晰度，以直播为例：

打开 [直播控制台](https://console.cloud.tencent.com/live/livemanage)，找到需要播放的直播流，进入详情。
![](https://main.qcloudimg.com/raw/e7502f092eaabdafbca1450427eef5a9.png)

例如，您有不同清晰度、不同格式的播放地址。推荐使用 FLV 地址播放，代码如下：

```java
SuperPlayerModel model = new SuperPlayerModel();
model.multiURLs = new ArrayList<>();
model.multiURLs.add(new SuperPlayerModel.SuperPlayerURL("http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e_550.flv", "标清"));
model.multiURLs.add(new SuperPlayerModel.SuperPlayerURL("http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e_900.flv", "高清"));
model.multiURLs.add(new SuperPlayerModel.SuperPlayerURL("http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e.flv", "超清"));
model.playDefaultIndex = 1;// 默认播放高清

mSuperPlayerView.playWithModel(model);
```

在播放器中即可看到这几个清晰度，单击即可立即切换。

<img src="https://main.qcloudimg.com/raw/8cb10273fe2b6df81b36ddb79d0f4890.jpeg" width="670"/>

## 时移播放

播放器开启时移非常简单，您只需要在播放前配置好 appId：

```java
playerModel.appId = 1252463788;
```

>? appId 在【腾讯云控制台】>【[账号信息](https://console.cloud.tencent.com/developer)】中查看。

播放的直播流就能在下面看到进度条。往后拖动即可回到指定位置，单击【返回直播】可观看最新直播流。

<img src="https://main.qcloudimg.com/raw/a3a4a18819aed49b919384b782a13957.jpeg" width="670"/>

>! 时移功能处于公测申请阶段，如您需要可 [提交工单](https://console.cloud.tencent.com/workorder) 申请使用。

## FileId 播放

设置清晰度除了填写 url 外，更简单的使用方式是采用 fileId 播放。fileId 在一般是在视频上传后，由服务器返回：

1. 在 [腾讯云官网](https://cloud.tencent.com/) 注册腾讯云账号，然后开通点播服务。
2. 客户端视频发布后，服务器会返回 [fileId](https://cloud.tencent.com/document/product/584/15535) 到客户端。
3. 服务端视频上传，在 [确认上传](https://cloud.tencent.com/document/product/266/9757) 的通知中包含对应的 fileId。


如果文件已存在腾讯云，则可以进入 [媒资管理](https://console.cloud.tencent.com/vod/media)，找到对应的文件。点开后在右侧视频详情中，可以看到 appId 和 fileId。

播放 fileId 的代码如下：

```java
//不开防盗链
SuperPlayerModel model = new SuperPlayerModel();
model.appId = 1400329073;// 配置 AppId
model.videoId = new SuperPlayerVideoId();
model.videoId.fileId = "5285890799710670616"; // 配置 FileId
mSuperPlayerView.playWithModel(model);

//开启防盗链，需填写 psign， psign 签名介绍和生成方式参见链接：https://cloud.tencent.com/document/product/266/42436
SuperPlayerModel model = new SuperPlayerModel();
model.appId = 1400329071;// 配置 AppId
model.videoId = new SuperPlayerVideoId();
model.videoId.fileId = "5285890799710173650"; // 配置 FileId
mSuperPlayerView.playWithModel(model);
model.videoId.pSign = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTQwMDMyOTA3MSwiZmlsZUlkIjoiNTI4NTg5MDc5OTcxMDE3MzY1MCIsImN1cnJlbnRUaW1lU3RhbXAiOjEsImV4cGlyZVRpbWVTdGFtcCI6MjE0NzQ4MzY0NywidXJsQWNjZXNzSW5mbyI6eyJ0IjoiN2ZmZmZmZmYifSwiZHJtTGljZW5zZUluZm8iOnsiZXhwaXJlVGltZVN0YW1wIjoyMTQ3NDgzNjQ3fX0.yJxpnQ2Evp5KZQFfuBBK05BoPpQAzYAWo6liXws-LzU"; 
mSuperPlayerView.playWithModel(model);
```

视频在上传后，后台会自动转码（所有转码格式请参考 [转码模板](https://cloud.tencent.com/document/product/266/33478#.3Cspan-id-.3D-.22zm.22-.3E.3C.2Fspan.3E.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)）。转码完成后，播放器会自动显示多个清晰度。关于使用防盗链内容，您可以参考文档：[点播超级播放器使用文档 - Key 防盗链](https://cloud.tencent.com/document/product/266/14424#key-.E9.98.B2.E7.9B.97.E9.93.BE)。

## 打点信息

在播放长视频时，打点信息有助于观众找到该兴趣的点。使用腾讯云服务 API，能快速对视频处理。详情请参见 [增加打点信息](https://cloud.tencent.com/document/product/266/14190)。

任务执行成功后，播放器的界面会增加新的元素。
<img src="https://main.qcloudimg.com/raw/55ebce6d0c703dafa1ac131e1852e025.png" width="670"/>

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

<img src="https://main.qcloudimg.com/raw/d6783a450e339526e0ca0b2ed3ef6142.png" width="400"/>

## 退出播放

当不需要播放器时，调用`resetPlayer`清理播放器内部状态，释放内存。

```java
mSuperPlayerView.resetPlayer();
```

## 更多功能

完整功能可扫码下载视频云工具包体验，或直接运行工程 Demo。
<img src="https://main.qcloudimg.com/raw/344d9d41fc5e305a17e22e104b9305da.png" width="150"/>
