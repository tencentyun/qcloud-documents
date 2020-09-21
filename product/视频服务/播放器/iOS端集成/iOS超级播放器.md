## 简介
iOS 播放器 SDK 是腾讯云开源的一款播放器组件，简单几行代码即可拥有类似腾讯视频强大的播放功能。包括横竖屏切换、清晰度选择、手势、小窗等基础功能，还支持视频缓存，软硬解切换，倍速播放等特殊功能。相比系统播放器，支持 FLV、MP4 及 HLS 多种播放格式，兼容性更好，功能更强大。同时还支持直播流（FLV + RTMP）播放，具备首屏秒开、低延迟的优点，以及清晰度无缝切换、直播时移等高级能力。

iOS 播放器 SDK 完全免费开源，不对播放地址来源做限制，请放心使用。

## 阅读对象
本文档部分内容为腾讯云专属能力，使用前请开通 [腾讯云](https://cloud.tencent.com/) 相关服务，未注册用户可 [注册账号](https://cloud.tencent.com/document/product/378/17985) 免费试用。


## 快速集成

### 接入准备

请将下面代码加入到您的 Podfile 中：
```
pod 'SuperPlayer'
```

### 使用播放器
播放器主类为`SuperPlayerView`，创建后即可播放视频。

```objective-c
// 引入头文件
#import <SuperPlayer/SuperPlayer.h>

_playerView = [[SuperPlayerView alloc] init];
// 设置代理，用于接受事件
_playerView.delegate = self;
// 设置父 View，_playerView 会被自动添加到 holderView 下面
_playerView.fatherView = self.holderView;

SuperPlayerModel *playerModel = [[SuperPlayerModel alloc] init];
// 设置播放地址，直播、点播都可以
playerModel.videoURL = @"http://200024424.vod.myqcloud.com/200024424_709ae516bdf811e6ad39991f76a4df69.f20.mp4";
// 开始播放
[_playerView playWithModel:playerModel];
```
运行代码，可以看到视频在手机上播放，并且界面上大部分功能都处于可用状态。
![](https://main.qcloudimg.com/raw/128c45edfc77b319475868c21caec2de.png)


## 多清晰度
上面的示例代码只有一种清晰度，如果要添加多个清晰度，也非常简单。以直播为例，打开 [直播控制台](https://console.cloud.tencent.com/live/livemanage)，找到需要播放的直播流，进入详情。
![](https://main.qcloudimg.com/raw/e7502f092eaabdafbca1450427eef5a9.png)

这里有不同清晰度、不同格式的播放地址。推荐使用 FLV 地址播放，代码如下：
```
SuperPlayerUrl *url1 = [SuperPlayerUrl new];
url1.url = @"http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e.flv";
url1.title = @"超清";
SuperPlayerUrl *url2 = [SuperPlayerUrl new];
url2.url = @"http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e_900.flv";
url2.title = @"高清";
SuperPlayerUrl *url3 = [SuperPlayerUrl new];
url3.url = @"http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e_550.flv";
url3.title = @"标清";

SuperPlayerModel *playerModel = [[SuperPlayerModel alloc] init];
palyerModel.multiVideoURLs = @[url1, url2, url3];
playerModel.videoURL = url1.url; // 设置默认播放的清晰度
// 开始播放
[_playerView playWithModel:playerModel];
```
在播放器中即可看到这几个清晰度，单击即可立即切换。

<img src="https://main.qcloudimg.com/raw/8cb10273fe2b6df81b36ddb79d0f4890.jpeg" width="670"/>

## 时移播放
播放器开启时移非常简单，您只需要在播放前配置好 appId。

```objc
SuperPlayerVideoId *videoId = [[SuperPlayerVideoId alloc] init];
videoId.appId = 1252463788; // 这里换成您的 appID
SuperPlayerModel *playerModel = [[SuperPlayerModel alloc] init];
playerModel.videoId = videoId;
```
>? appId 在【腾讯云控制台】>【[账号信息](https://console.cloud.tencent.com/developer)】中查看。

播放的直播流就能在下面看到进度条。往后拖动即可回到指定位置，单击【返回直播】可观看最新直播流。

<img src="https://main.qcloudimg.com/raw/a3a4a18819aed49b919384b782a13957.jpeg" width="670"/>

>! 时移功能处于公测申请阶段，如您需要可 [提交工单](https://console.cloud.tencent.com/workorder) 申请使用。

## FileId 播放
设置清晰度除了填写 url 外，更简单的使用方式是采用 fileId 播放。fileId 一般是在视频上传后，由服务器返回：
1. 客户端视频发布后，服务器会返回 fileId 到客户端。
2. 服务端视频上传，在 [确认上传](https://cloud.tencent.com/document/product/266/9757) 的通知中包含对应的 fileId。


如果文件已存在腾讯云，则可以进入 [媒资管理](https://console.cloud.tencent.com/vod/media) ，找到对应的文件。点开后在右侧视频详情中，可以看到 appId 和 fileId。


播放 fileId 的代码如下：
```
SuperPlayerVideoId *videoId = [SuperPlayerVideoId new];
videoId.appId = 1252463788; // 这里换成您的 appID
videoId.fileId = @"4564972819219071679"; // 这里换成需要播放视频的 fileID
playerModel.videoId = videoId;
[_playerView playWithModel:self.playerModel];
```
视频在上传后，后台会自动转码（所有转码格式请参考 [转码模板](https://console.cloud.tencent.com/vod/video-process/template)）。转码完成后，播放器会自动显示多个清晰度。

## 雪碧图和打点信息
在播放长视频时，雪碧图和打点信息有助于观众找到感兴趣的点。使用腾讯云服务 API，能快速对视频处理。

- [截取雪碧图](https://cloud.tencent.com/document/product/266/8101)
- [增加打点信息](https://cloud.tencent.com/document/product/266/14190)

任务执行成功后，播放器的界面会增加新的元素。
<img src="https://main.qcloudimg.com/raw/55ebce6d0c703dafa1ac131e1852e025.png" width="670"/>

## 小窗播放
小窗播是指在 App 内，悬浮在主 window 上的播放器。使用小窗播放非常简单，只需要在适当位置调用下面代码即可：
```objective-c
[SuperPlayerWindow sharedInstance].superPlayer = _playerView; // 设置小窗显示的播放器
[SuperPlayerWindow sharedInstance].backController = self;  // 设置返回的 view controller
[[SuperPlayerWindow sharedInstance] show]; // 悬浮显示
```
![](https://main.qcloudimg.com/raw/e2ee64230af1b9c3a79cad935afa8b6a.jpeg)

## 退出播放
当不需要播放器时，调用 resetPlayer 清理播放器内部状态，释放内存。
```objective-c
[_playerView resetPlayer];
```

## 更多功能
完整功能可扫码下载视频云工具包体验，或直接运行工程 Demo。

<img src="https://main.qcloudimg.com/raw/b670e99ddb3f0d828798520e19f40fa7.png" width="150"/>

