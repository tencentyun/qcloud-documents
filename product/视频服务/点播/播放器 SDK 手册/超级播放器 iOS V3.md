## 简介

iOS 超级播放器 SDK 是一款用于播放云点播视频的播放器组件，几行代码就能实现类似腾讯视频强大的播放功能。

* 基础功能：横竖屏切换、清晰度选择、手势和小窗等。
* 高级功能：视频缓存、软硬解切换、倍速播放、视频缩略图、DRM 加密播放等。

相比系统播放器，超级播放器支持格式更多，兼容性更好，功能更强大。同时还具备首屏秒开和低延迟的优点。

## SDK 下载

云点播 iOS 超级播放器的下载地址是 [SuperPlayer_iOS](https://github.com/tencentyun/SuperPlayer_iOS)。

## 快速集成

### CocoaPods 集成

请将下面代码加入到您的 Podfile 中：
```
pod 'SuperPlayer'
```

命令行输入`pod install`或`pod update`执行安装。

### 准备视频

登录 [云点播控制台](https://console.cloud.tencent.com/vod/overview)，单击左侧菜单栏的【媒资管理】，在“**已上传**”栏的视频列表中，将看到上传完成的视频，以及视频对应的 ID（即 FileId）。如果您还没有视频，请先单击【上传视频】，上传一个视频。
![](https://main.qcloudimg.com/raw/f80e23558bee2bd33b1f29a522fe8da9.png)

通过 [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) ，对上传的视频发起 [转自适应码流](https://cloud.tencent.com/document/product/266/34071) 任务：
API 参数中的`MediaProcessTask.AdaptiveDynamicStreamingTaskSet.Definition`建议填10，表示转 HLS 格式的自适应码流。

### 开始播放

播放器主类为`SuperPlayerView`，创建后即可播放视频。
```objective-c
// 引入头文件
#import <SuperPlayer/SuperPlayer.h>
_playerView = [[SuperPlayerView alloc] init];
// 设置代理，用于接受事件
_playerView.delegate = self;
// 设置父View，_playerView会被自动添加到holderView下面
_playerView.fatherView = self.holderView;
SuperPlayerModel *playerModel = [[SuperPlayerModel alloc] init];
SuperPlayerVideoId *video = [[SuperPlayerVideoId alloc] init];
//设置播放信息
video.appId = 1256993030;  //AppId
video.fileId = @"7447398157015849771";  //视频 FileId
video.playDefinition = @"10";   //播放模板 ID
video.version = FileIdV3;
playerModel.videoId = video;
// 开始播放
[_playerView playWithModel:self.playerModel];
```

代码中的`appId`是您的 AppId，`fileId`是您要播放的视频 ID，`playDefinition`是您播放时使用的 [播放模板](https://cloud.tencent.com/document/product/266/34101#.E6.92.AD.E6.94.BE.E6.A8.A1.E6.9D.BF) ID，`version`固定填`SuperPlayerVideoId.FILE_ID_V3`。

运行代码，可以看到视频在手机上播放，并且界面上大部分功能都处于可用状态。
<img src="https://main.qcloudimg.com/raw/128c45edfc77b319475868c21caec2de.png" width="550">

## 缩略图与打点

在播放视频时，进度条上的“缩略图”和“打点信息”，有助于观众找到感兴趣的点。缩略图通过 [雪碧图](https://cloud.tencent.com/document/product/266/8101) 实现，视频打点需要 [修改媒资中的打点信息](https://cloud.tencent.com/document/product/266/31762#.E7.A4.BA.E4.BE.8B3-.E4.BF.AE.E6.94.B9.E5.AA.92.E4.BD.93.E6.96.87.E4.BB.B6.E8.A7.86.E9.A2.91.E6.89.93.E7.82.B9.E4.BF.A1.E6.81.AF)。

为视频截取雪碧图，并添加打点信息后，播放器的界面会增加新的元素。
<img src="https://main.qcloudimg.com/raw/55ebce6d0c703dafa1ac131e1852e025.png" width="550">

## 播放 DRM 加密的视频

数字版权管理（Digital Rights Management，DRM），是通过技术手段对内容加密，保护版权内容的安全，适用于音乐、电影等带版权的多媒体内容。云点播提供了商业级 DRM 加密，详情请参见 [如何对内容做版权保护](https://cloud.tencent.com/document/product/266/34105#.E5.95.86.E4.B8.9A.E7.BA.A7-drm)。

Android 超级播放器，可以播放 [商业级 DRM](https://cloud.tencent.com/document/product/266/34105#.E5.95.86.E4.B8.9A.E7.BA.A7-drm) 中两种方式加密的输出：

- 基于 FairPlay 加密的 HLS 格式。
- 基于 SimpleAES 加密的 HLS 格式。

云点播提供了基于 Web 超级播放器的 [DRM 入门教程](https://cloud.tencent.com/document/product/266/34690)，建议您先通过该教程的学习。

### 使用方法

首先，App 需要从您的**业务后台**获取 Token，Token 的生成方式请参见 [Token 生成](https://cloud.tencent.com/document/product/266/34102#token-.E7.94.9F.E6.88.90)。如果需要播放 FairPlay 加密的内容，按照 [ASK 和 FPS 证书指引](https://cloud.tencent.com/document/product/266/34102#ask-.E5.92.8C-fps-.E8.AF.81.E4.B9.A6) 生成 FPS 证书，证书的内容用`fairplay_cer`表示。

然后，通过 FileId + Token 方式进行播放，播放代码如下：

```
SuperPlayerModel *model = [[SuperPlayerModel alloc] init];
SuperPlayerVideoId *video = [[SuperPlayerVideoId alloc] init];
video.appId = 1256993030;
video.fileId = @"7447398157015849771";
video.playDefinition = @"20";
video.version = FileIdV3;
model.videoId = video;
model.token = token; // 服务端下发的token
model.certificate = fairplay_cer; // FairPlay的certificate，从本地文件读取
```

代码中的`playDefinition`是 [播放模板](https://cloud.tencent.com/document/product/266/34101#.E6.92.AD.E6.94.BE.E6.A8.A1.E6.9D.BF) ID，播放器会根据播放模板指定的行为播放。例如，模板 ID 为20时，先尝试播放商业级加密的输出，若无法播放再降级播放 SimpleAES 方式加密的输出。

## 小窗播放

小窗播放是指在 App 内，悬浮在主窗口上的播放器。使用小窗播放非常简单，只需要在适当位置调用下面代码即可：

```objective-c
[SuperPlayerWindow sharedInstance].superPlayer = _playerView; // 设置小窗显示的播放器
[SuperPlayerWindow sharedInstance].backController = self;  // 设置返回的view controller
[[SuperPlayerWindow sharedInstance] show]; // 悬浮显示
```
<img src="https://main.qcloudimg.com/raw/e2ee64230af1b9c3a79cad935afa8b6a.jpeg" width="300">

## 退出播放

如果不需要播放器，可以调用`resetPlayer`清理播放器内部状态，释放内存。
```objective-c
[_playerView resetPlayer];
```

## 更多功能

完整功能可扫码下载视频云工具包体验，或直接运行工程 Demo。
<img src="https://main.qcloudimg.com/raw/b670e99ddb3f0d828798520e19f40fa7.png" width="150">
