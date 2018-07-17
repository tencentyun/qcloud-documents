## 功能介绍

超级播放器是基于`TXVodPlayer`和`TXLivePlayer`实现的集视频信息拉取、横竖屏切换、清晰度选择、弹幕、直播时移等功能于一体的解决方案，**且完全开源**。帮助您在短时间内，打造一个媲美市面上各种流行视频App的播放体验。


![](https://mc.qcloudimg.com/static/img/c5a7b6e6e8cba617b76fee49aa03da18/image.png)

## 接入准备

1. 下载 SDK + Demo 开发包。[下载地址](https://cloud.tencent.com/document/product/454/7873#iOS)）。

2. 超级播放器的 UI 部分源码开源，开源代码位于`Player/SuperPlayer`文件夹，图片资源位于`SuperPlayer.bundle`中，您需要src中的文件分拷贝的您的App工程中。其它依赖的第三方库您可以自行 Pod 添加或在 `Third` 目录中获取


超级播放器依赖的第三方库

- Masonry
- SDWebImage
- AFNetworking


## 创建播放器

超级播放器主类为`SuperPlayerView`，您需要先创建它并添加到合适的容器View中。

```objective-c
_playerView = [[SuperPlayerView alloc] init];

// 设置代理
_playerView.delegate = self;

// 设置父View
_playerView.fatherView = self.holderView;

// 开始播放
[_playerView playWithModel:self.playerModel];
```

## 设置播放数据

如您所见，播放器开始播放前，需要传入一个SuperPlayerModel对象。在Model对象中，可以设置标题、封面图，以及最重要的视频源。
视频源有两种格式：一种是常见的url地址，一种是腾讯云的fileId。请根据App需求选一种填写。

### url方式
url是最常见的播放源。根据url格式不同，播放器行为也有所不同。
如果url为rtmp协议或flv流，则播放器默认为直播流，并自动开启时移功能。

> 时移功能即在直播的过程中，可以回看前面任意时间点。超级播放器只支持腾讯云的直播地址回看。您可以用上面提供的Demo，在'RTMP 推流'里单击New开始推流，然后在超级播放中扫码播放，即可体验到时移功能。


如果url为mp4或m3u8流，则播放器认为是点播地址，会放开倍速播放、镜像等点播特有的能力。

### fileId方式
fileId在一般是在视频上传后，由服务器返回：

1. 客户端视频发布后，服务器会返回[fileId](https://cloud.tencent.com/document/product/584/9367#8..E5.8F.91.E5.B8.83.E7.BB.93.E6.9E.9C)到客户端
2. 服务端视频上传，在[确认上传](https://cloud.tencent.com/document/product/266/9757)的通知中包含对应的fileId

如果文件已存在腾讯云，则可以进入 [点播视频管理](https://console.cloud.tencent.com/video/videolist) ，找到对应的文件。点开后在右侧视频详情中，可以看到appId和fileId。

![视频管理](https://mc.qcloudimg.com/static/img/fcad44c3392b229f3a53d5f8b2c52961/image.png)

通过fileId方式播放，播放器界面会显示后台已转码的各个清晰度，并能实现自由切换。

## 切换视频

播放另一个视频，您只需重新调用`playWithModel:`方法。

## 小窗播放

小窗播是指在App内，悬浮在主window上的播放器。使用小窗播放非常简单，只需要在适当位置编写下面代码即可
```objective-c
SuperPlayerWindowShared.superPlayer = _playerView; // 设置小窗显示的播放器
SuperPlayerWindowShared.backController = self;  // 设置返回的view controller
[SuperPlayerWindowShared show]; // 悬浮显示
```

## 移除播放器

当不需要播放器时，调用resetPlayer清理播放器内部状态，防止干扰下次播放。

```objective-c
[_playerView resetPlayer];  //非常重要
```
