## 简介

iOS 超级播放器 SDK 是腾讯云开源的一款播放器组件，简单几行代码即可拥有类似腾讯视频强大的播放功能。包括横竖屏切换、清晰度选择、手势和小窗等基础功能，还支持视频缓存，软硬解切换和倍速播放等特殊功能。相比系统播放器，支持格式更多，兼容性更好，功能更强大。同时还具备首屏秒开、低延迟的优点，以及视频缩略图等高级能力。

## SDK 下载

点播 iOS 超级播放器的下载地址是 [SuperPlayer_iOS](https://github.com/tencentyun/SuperPlayer_iOS)。

## 阅读对象

本文档部分内容为腾讯云专属能力，使用前请开通 [腾讯云](https://cloud.tencent.com/) 相关服务，未注册用户可 [注册账号](https://cloud.tencent.com/login)。

## 快速集成

### 接入准备

#### 方案1. 官方 CocoaPods

请将下面代码加入到您的 Podfile 中：
```
pod 'SuperPlayer'
```

#### 方案2. 本地 CocoaPods

[下载 SDK](https://github.com/tencentyun/SuperPlayer_iOS)，解压到本地。此时您可以看到解压后的文件。

![](https://mc.qcloudimg.com/static/img/5ef04a5e101beea834813e58fc5115ec/androidzippkg.png)

其中，播放器代码位于`Demo/SuperPlayer`，SDK 库位于 SDK 目录。
在您的 Podfile 文件，添加下面代码：

```
pod 'SuperPlayer', :path => '<解压路径>/Demo/SuperPlayer/SuperPlayer.podspec', :subspecs => ['Player']
# subspecs根据下载SDK不同会不一样，如果您下载的是专业版，则需要将Player改为Professional，其它以此类推
```
命令行输入 `pod install` 或 `pod update` 执行安装。

### 使用播放器

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
//设置播放信息
playerModel.appId = 1252463788;  //AppId
playerModel.fileId = @"4564972819219071679";  //视频 FileId
// 开始播放
[_playerView playWithModel:self.playerModel];
```
运行代码，可以看到视频在手机上播放，并且界面上大部分功能都处于可用状态。
![](https://main.qcloudimg.com/raw/128c45edfc77b319475868c21caec2de.png)

### 选择 FileId

视频 FileId 在一般是在视频上传后，由服务器返回：
1. 客户端视频发布后，服务器会返回 [fileId](https://cloud.tencent.com/document/product/584/9367#8..E5.8F.91.E5.B8.83.E7.BB.93.E6.9E.9C) 到客户端。
2. 服务端视频上传时，在 [确认上传](https://cloud.tencent.com/document/product/266/9757) 的通知中包含对应的 fileId。

如果文件已存在腾讯云，则可以进入 [视频管理](https://console.cloud.tencent.com/video/videolist) ，找到对应的文件，查看 fileId。如下图所示，ID 即表示 fileId：
![视频管理](https://main.qcloudimg.com/raw/15c5d181b9037b58db5cf192fe831f1b.png)

## 缩略图与打点

在播放长视频时，缩略图（雪碧图）和打点信息有助于观众找到该兴趣的点。使用腾讯云服务 API，能快速对视频处理。
- [截取雪碧图](https://cloud.tencent.com/document/product/266/8101)
- [增加打点信息](https://cloud.tencent.com/document/product/266/14190)

任务执行成功后，播放器的界面会增加新的元素。

![](https://main.qcloudimg.com/raw/55ebce6d0c703dafa1ac131e1852e025.png)

## 播放 DRM 加密的视频

数字版权管理解决方案（Digital Rights Management，DRM），通过技术手段加密内容，用来控制带版权作品的使用、更改和分发，保护带版权内容的安全。适用于音乐、电影等带版权的多媒体内容。

iOS 播放器可以播放两种方式加密的输出：

1. 基于 FairPlay 加密的 HLS 格式
2. 基于 SimpleAES 加密的 HLS 格式

关于 DRM 的更多详情，您可以参考 [如何对内容做版权保护](<https://cloud.tencent.com/document/product/266/34105#.E5.95.86.E4.B8.9A.E7.BA.A7-drm>) 方案文档。

### 使用方法

首先，App 需要从您的**业务后台**获取 Token，Token 的生成方式请参考 [这里](<https://cloud.tencent.com/document/product/266/34102#token-.E7.94.9F.E6.88.90>) 。

如果需要播放 FairPlay 加密的内容，按照 [ASK 和 FPS 证书指引](https://cloud.tencent.com/document/product/266/34102#ask-.E5.92.8C-fps-.E8.AF.81.E4.B9.A6) 生成 FPS 证书，证书的内容用`fairplay_cer`表示。

然后，通过 FileId + Token 方式进行播放，播放代码如下：

```
SuperPlayerModel *model = [[SuperPlayerModel alloc] init];
SuperPlayerVideoId *video = [[SuperPlayerVideoId alloc] init];
video.appId = 1253039488;
video.fileId = @"15517827183850370616";
video.playDefinition = @"20";
video.version = FileIdV3; // DRM需要使用V3协议
model.videoId = video;
model.token = token; // 服务端下发的token
model.certificate = fairplay_cer; // FairPlay的certificate，从本地文件读取
```

代码中的`playDefinition`是 [播放模板](https://cloud.tencent.com/document/product/266/34101#.E6.92.AD.E6.94.BE.E6.A8.A1.E6.9D.BF) ID，播放器会根据播放模板指定的行为播放。例如当模板 ID 为20时，先尝试播放商业级加密的输出，若无法播放再降级播放 SimpleAES 方式加密的输出。

## 小窗播放

小窗播是指在 App 内，悬浮在主 Window 上的播放器。使用小窗播放非常简单，只需要在适当位置调用下面代码即可：
```objective-c
SuperPlayerWindowShared.superPlayer = _playerView; // 设置小窗显示的播放器
SuperPlayerWindowShared.backController = self;  // 设置返回的view controller
[SuperPlayerWindowShared show]; // 悬浮显示
```
![](https://main.qcloudimg.com/raw/e2ee64230af1b9c3a79cad935afa8b6a.jpeg)

## 退出播放

当不需要播放器时，调用 resetPlayer 清理播放器内部状态，释放内存。
```objective-c
[_playerView resetPlayer];
```

## 更多功能

完整功能可扫码下载视频云工具包体验，或直接运行工程 Demo。
![iOS二维码下载](https://main.qcloudimg.com/raw/b670e99ddb3f0d828798520e19f40fa7.png)
