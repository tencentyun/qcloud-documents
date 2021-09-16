## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | &#10003;  | &#10003;                                                            | -  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 概述
SDK 的各项监控指标可以从 [V2TXLivePusherObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusherObserver__ios.html) 和 [V2TXLivePlayerObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html) 的回调中获取。

## V2TXLivePusherObserver

### 获取推流的状态数据
V2TXLivePusherObserver 的 [onStatisticsUpdate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusherObserver__ios.html#ae93683da9240a752e7b6d70d8e940cbc) 回调，会每隔2秒会将 SDK 内部的状态指标同步出来，其中如下指标比较有意义：

|  推流状态                 |  含义说明                  |
| :------------------------  |  :------------------------ |
| appCpu        | 当前进程的 CPU 使用率。|
| systemCpu     | 本机总体的 CPU 使用率。|
| width         | 当前视频的宽度，单位：像素值。    |
| height        | 当前视频的高度，单位：像素值。    |
| fps           | 当前视频帧率，也就是视频编码器每条生产了多少帧画面。|
| videoBitrate  | 当前视频编码器输出的比特率，也就是编码器每秒生产了多少视频数据，单位：kbps。|
| audioBitrate  | 当前音频编码器输出的比特率，也就是编码器每秒生产了多少音频数据，单位：kbps。|

### 有参考价值的状态指标

| 状态指标 | 说明 |
|---------|---------|
| systemCpu | <ul style="margin:0"><li>如果<strong>系统 CPU 使用率</strong>超过80%，音视频编码的稳定性会受到影响，可能导致画面和声音的随机卡顿。</li><li>如果<strong>系统 CPU 使用率</strong>经常100%，会导致视频编码帧率不足，音频编码跟不上，必然导致画面和声音的严重卡顿。</li></ul> |
| fps | 常来说每秒15帧以上的视频流才能保证观看的流畅度，常规推流如果 FPS 在10帧以下，观众就会明显的感到画面卡顿。 |

>?很多客户会遇到的一个问题： App 在线下测试时性能表现极佳，但在 App 外发上线后，前排房间里的互动消息的滚屏和刷新会产生极大的 CPU 消耗导致直播画面卡顿严重。

### 看懂腾讯云推流图表 
在 【云直播控制台】>【[质量监控](https://console.cloud.tencent.com/live/livesdk)】 您可以看到您所属账户里的直播间情况，以及每个直播间的推流质量数据：

- **主播端-应发速率-实发速率曲线图**
蓝色曲线代表 BITRATE 的统计曲线，即 SDK 产生的音视频数据，绿色曲线代表实际网络发出去多少。两条线重合度越高表示推流质量越好。
![](https://main.qcloudimg.com/raw/d2ad188df4ca9ca6bb192a74db9cb95d.png)

- **主播端-音视频数据堆积情况**
 + 如果曲线始终贴着0刻度线走，说明整个推流过程非常顺畅，一点都没有堆积。
 + 如果出现大于0的部分，说明当时有网络波动导致数据积压，有可能在播放端产生轻微卡顿和音画不同步的现象。
 + 如果堆积超出红色警戒线，说明已经产生了丢包，必然会在播放端产生卡顿和音画不同步的现象。
![](https://main.qcloudimg.com/raw/ce31d7b603a9a9719340c16b5e1b9471.png)

- **云端-应收视频时长-实收视频时长曲线**
这里是腾讯云服务端的统计图表，如果您不是使用腾讯云 SDK 推流，那么您将只能看到这个图表，前面两个（数据源来自 SDK）是看不到的。蓝绿两条线重合度越高，说明推流质量越好。
![](https://main.qcloudimg.com/raw/c24863a60618db266bb6eaaab6da1833.png)

## V2TXLivePlayerObserver

### 获取播放的状态数据
V2TXLivePlayerObserver 的 [onStatisticsUpdate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a4cdfa0b36d4b9e910c1e0d1b5dc44cde) 回调，会每隔2秒会将 SDK 内部的状态指标同步出来，其中如下指标比较有意义：

|  播放状态                 |  含义说明                  |
| :------------------------  |  :------------------------ |
| appCpu        | 当前进程的 CPU 使用率。|
| systemCpu     | 本机总体的 CPU 使用率。|
| width         | 当前视频的宽度，单位：像素值。    |
| height        | 当前视频的高度，单位：像素值。    |
| fps           | 当前流媒体的视频帧率。|
| videoBitrate  | 当前流媒体的视频码率，单位：kbps。|
| audioBitrate  | 当前流媒体的音频码率，单位：kbps。|

### 有参考价值的状态指标

| 状态指标 | 说明 |
|---------|---------|
| systemCpu | <ul style="margin:0"><li>如果<strong>系统 CPU 使用率</strong>超过80%，音视频编码的稳定性会受到影响，可能导致画面和声音的随机卡顿。</li><li>如果<strong>系统 CPU 使用率</strong>经常100%，会导致视频编码帧率不足，音频编码跟不上，必然导致画面和声音的严重卡顿。</li></ul> |
| fps | 常来说每秒15帧以上的视频流才能保证观看的流畅度，常规推流如果 FPS 在10帧以下，观众就会明显的感到画面卡顿。 |

