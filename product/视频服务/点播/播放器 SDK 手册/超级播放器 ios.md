## 功能介绍

超级播放器是基于`TXVodPlayer`实现的集视频信息拉取、横竖屏切换、清晰度选择、弹幕等功能于一体的解决方案，**且完全开源**。帮助您在短时间内，打造一个媲美市面上各种流行视频App的播放体验。


![](https://mc.qcloudimg.com/static/img/c5a7b6e6e8cba617b76fee49aa03da18/image.png)

## 接入准备

1. 下载 SDK + Demo 开发包，下载地址为（[iOS](https://cloud.tencent.com/document/product/454/7873#iOS)）。

2. 超级播放器的 UI 部分源码开源，开源代码位于`Player`文件夹，图片资源位于`Resource/Player`文件夹，您需要先将这两部分拷贝的您的App工程中。其它依赖的第三方库您可以自行 Pod 添加或在 `Third` 目录中获取
 -  Masonry
 - SDWebImage


## 创建播放器

超级播放器主类为`ZFPlayerView`，您需求先创建它并添加的需要的父View中。

```objective-c
_playerView = [[ZFPlayerView alloc] init];
        
[_playerView playerControlView:nil playerModel:self.playerModel];

// 设置代理
_playerView.delegate = self;

// 加载成功后自动播放
[self.playerView autoPlayTheVideo];
```

## 视频信息获取

与播放普通url地址不同，获取视频信息需要通过fileId方式。

```objective-c
TXPlayerAuthParams *p = [TXPlayerAuthParams new];
p.appId = 1252463788;
p.fileId = @"4564972819220421305";

self.getInfoPlayer = [[TXVodPlayer alloc] init];
[self.getInfoPlayer setIsAutoPlay:NO];
self.getInfoPlayer.vodDelegate = self;
[self.getInfoPlayer startPlayWithParams:p];
```

fileId在一般是在视频上传后，由服务器返回：

1. 客户端视频发布后，服务器会返回[fileId](https://cloud.tencent.com/document/product/584/9367#8..E5.8F.91.E5.B8.83.E7.BB.93.E6.9E.9C)到客户端
2. 服务端视频上传，在[确认上传](https://cloud.tencent.com/document/product/266/9757)的通知中包含对应的fileId

如果文件已存在腾讯云，则可以进入 [点播视频管理](https://console.cloud.tencent.com/video/videolist) ，找到对应的文件。点开后在右侧视频详情中，可以看到appId和fileId。

![视频管理](https://mc.qcloudimg.com/static/img/fcad44c3392b229f3a53d5f8b2c52961/image.png)



SDK在请求成功后，视频信息将以事件的形式通知到上层

```objective-c
- (void)onPlayEvent:(TXVodPlayer *)player event:(int)EvtID withParam:(NSDictionary *)param
{
    
    if (EvtID == PLAY_EVT_GET_PLAYINFO_SUCC) {
        ListVideoModel *model = [ListVideoModel new];
        model.cover = param[EVT_PLAY_COVER_URL];
        model.duration = [param[EVT_PLAY_DURATION] intValue];
        model.url = param[EVT_PLAY_URL];
    }
}
```


## 切换视频

播放另一个视频，您需要重新创建一个`playerModel`，调用resetToPlayNewVideo即可

```objective-c
_playerModel.title = [cell getSource].title;
_playerModel.videoURL = [NSURL URLWithString:[cell getSource].url];
_playerModel.placeholderImage = [UIImage imageWithData:[NSData dataWithContentsOfURL:
                                [NSURL URLWithString:[cell getSource].cover]]];

[_playerView resetToPlayNewVideo:self.playerModel];
```
### 移除播放器

当不需要播放器时，调用resetPlayer清理播放器内部状态，防止干扰下次播放。

```objective-c
[self.playerView resetPlayer];  //非常重要
```

